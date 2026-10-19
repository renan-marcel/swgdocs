"""Compare retained Binary Ninja CRC bytes with the exact PE and Java table.

This verifies static evidence. It does not execute SWG or the JVM library.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct

DOCS = Path(__file__).resolve().parents[1]


def verify(source, binary):
    evidence = DOCS / 'data/pswgcommon-evidence'
    record = json.loads((evidence / 'BN-PSWG-CRC-TABLE.json').read_text(encoding='utf-8'))
    result = record['result']
    data = result.get('structuredContent')
    if data is None:
        data = json.loads(result['content'][0]['text'])
    observed = bytes.fromhex(data['hex'])
    java_path = source / 'src/main/java/com/projectswg/common/data/CRC.java'
    java_bytes = java_path.read_bytes()
    java = java_bytes.decode('utf-8')
    table_text = java.split('CRC_TABLE[] = {', 1)[1].split('};', 1)[0]
    values = [int(x, 16) for x in re.findall(r'0x[0-9a-fA-F]+', table_text)]
    expected = struct.pack('<256I', *values)
    assert observed == expected, 'Binary Ninja table differs from Java CRC_TABLE'
    raw = binary.read_bytes()
    pe = struct.unpack_from('<I', raw, 0x3c)[0]
    assert raw[pe:pe+4] == b'PE\0\0'
    machine, sections = struct.unpack_from('<HH', raw, pe+4)
    optional = pe + 24
    assert struct.unpack_from('<H', raw, optional)[0] == 0x10b
    image_base = struct.unpack_from('<I', raw, optional+28)[0]
    section_table = optional + struct.unpack_from('<H', raw, pe+20)[0]
    rva = int(data['address'], 16) - image_base
    offset = None
    for i in range(sections):
        _, start, size, pointer = struct.unpack_from('<IIII', raw, section_table+i*40+8)
        if start <= rva and rva+len(observed) <= start+size:
            offset = pointer+rva-start
            break
    assert offset is not None and raw[offset:offset+len(observed)] == observed
    sha = lambda b: hashlib.sha256(b).hexdigest()
    report = {
        'id': 'PSWG-CRC-STATIC-VERIFY', 'method': 'static-byte-comparison',
        'target': binary.name, 'target_sha256': sha(raw), 'machine': hex(machine),
        'image_base': hex(image_base), 'table_va': data['address'], 'table_rva': hex(rva),
        'table_file_offset': hex(offset), 'table_bytes': len(observed),
        'table_sha256': sha(observed), 'java_source_sha256': sha(java_bytes),
        'table_entries': len(values), 'pe_matches_binary_ninja': True,
        'java_matches_binary_ninja': True,
        'limitations': ['Static bytes and pseudocode only; no client or JVM execution.',
                        'Shared table does not prove every call site normalizes strings identically.',
                        'No packet schema is promoted to binary verified by this comparison.']}
    (evidence / 'crc-verification.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=DOCS.parent/'pswgcommon')
    parser.add_argument('--binary', type=Path, default=DOCS.parent/'recovered/installation/SWGEmu.exe')
    args = parser.parse_args()
    verify(args.source, args.binary)
