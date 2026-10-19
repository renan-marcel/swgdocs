"""Verify retained MCP reads against the PE and decode documented samples.

All operations are static. Synthetic examples are not captured traffic or JVM tests.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT/'data/pswgcommon-evidence/messages-01'
EXPECTED = '58012e57cebc499454812ba7ed96b1289db01e520963b4fc364edb41c322b2a8'


def payload(result):
    if result.get('isError'):
        raise ValueError('MCP evidence contains error')
    return result.get('structuredContent') or json.loads(result['content'][0]['text'])


def crc_name(name):
    value = 0xffffffff
    for byte in name.encode('utf-8'):
        value ^= byte << 24
        for _ in range(8):
            value = ((value << 1) ^ (0x04c11db7 if value & 0x80000000 else 0)) & 0xffffffff
    return value ^ 0xffffffff


def decode_chat(data):
    cursor = 6
    count, opcode = struct.unpack_from('<HI', data)
    if opcode != crc_name('ChatInstantMessageToClient'):
        raise ValueError('Unexpected chat opcode')
    fields = []
    prefixes = []
    for _ in range(3):
        length = struct.unpack_from('<H', data, cursor)[0]
        cursor += 2
        if length == 0xffff:
            length = struct.unpack_from('<I', data, cursor)[0]
            cursor += 4
        fields.append(data[cursor:cursor+length].decode('ascii'))
        cursor += length
    for _ in range(2):
        prefixes.append(cursor)
        length = struct.unpack_from('<I', data, cursor)[0]
        cursor += 4
        end = cursor+2*length
        if end > len(data):
            raise ValueError('Truncated Unicode body')
        fields.append(data[cursor:end].decode('utf-16le'))
        cursor = end
    if cursor != len(data):
        raise ValueError('Trailing chat bytes')
    return {'operand_count': count, 'opcode': f'{opcode:08X}',
            'game': fields[0], 'galaxy': fields[1], 'character': fields[2],
            'message': fields[3], 'out_of_band': fields[4],
            'unicode_prefix_offsets': prefixes, 'bytes_consumed': cursor}


def sample(name):
    text = (ROOT/'content/protocols'/f'{name}.md').read_text(encoding='utf-8')
    section = text.split('## Sample Packet', 1)[1]
    block = re.search(r'```[^\n]*\n(.*?)```', section, re.S).group(1)
    tokens = []
    for line in block.splitlines():
        line = line.split('//', 1)[0]
        tokens.extend(re.findall(r'\b[0-9A-Fa-f]{2}\b', line))
    return bytes.fromhex(' '.join(tokens))


def main(binary):
    raw = binary.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED:
        raise ValueError('Unexpected target identity')
    pe = struct.unpack_from('<I', raw, 0x3c)[0]
    optional = pe+24
    base = struct.unpack_from('<I', raw, optional+28)[0]
    section_start = optional+struct.unpack_from('<H', raw, pe+20)[0]
    sections = [struct.unpack_from('<IIII', raw, section_start+i*40+8)
                for i in range(struct.unpack_from('<H', raw, pe+6)[0])]
    def offset(va, length):
        rva = va-base
        for _, start, size, pointer in sections:
            if start <= rva and rva+length <= start+size:
                return pointer+rva-start
        raise ValueError('Memory range is not fully file-backed')
    checks = []
    queries = []
    for file in sorted(EVIDENCE.glob('BN-*.json')):
        rec = json.loads(file.read_text(encoding='utf-8'))
        if rec['result'].get('isError'):
            raise ValueError(file.name)
        queries.append({'id': rec['id'], 'tool': rec['tool'],
                        'sha256': hashlib.sha256(file.read_bytes()).hexdigest()})
        if rec['tool'] != 'bn_memory_read':
            continue
        data = payload(rec['result'])
        observed = bytes.fromhex(data['hex'])
        loc = offset(int(data['address'], 16), len(observed))
        if raw[loc:loc+len(observed)] != observed:
            raise ValueError('PE/MCP mismatch: '+file.name)
        checks.append({'id': rec['id'], 'va': data['address'], 'file_offset': hex(loc),
                       'bytes': len(observed), 'sha256': hashlib.sha256(observed).hexdigest(), 'matches': True})
    # Preserve exact vtable -> COL -> type-descriptor identity and pack/unpack slots.
    types = []
    for table in [0x15dd9d8, 0x15dda48, 0x15dda58, 0x15dda84, 0x15de44c, 0x15eb9d0, 0x15ead30]:
        col = struct.unpack_from('<I', raw, offset(table-4, 4))[0]
        descriptor = struct.unpack_from('<I', raw, offset(col+12, 4))[0]
        start = offset(descriptor+8, 1)
        end = raw.index(0, start)
        slots = struct.unpack_from('<3I', raw, offset(table, 12))
        types.append({'vtable': hex(table), 'col': hex(col), 'type_descriptor': hex(descriptor),
                      'rtti': raw[start:end].decode('ascii'),
                      'destructor': hex(slots[0]), 'pack': hex(slots[1]), 'unpack': hex(slots[2])})
    examples = []
    for name, size, fmt in [('UpdateContainmentMessage', 26, '<HIQQi'),
                            ('SceneCreateObjectByCrc', 47, '<HIQ7fIB')]:
        data = sample(name)
        values = struct.unpack(fmt, data)
        if len(data) != size or values[1] != crc_name(name):
            raise ValueError('Documented sample mismatch: '+name)
        examples.append({'name': name, 'kind': 'existing documented sample; capture origin not re-established',
                         'bytes': len(data), 'operand_count': values[0], 'opcode': f'{values[1]:08X}',
                         'decoded_values': list(values[2:])})
    historical_chat = decode_chat(sample('ChatInstantMessageToClient'))
    def ascii_field(value):
        b = value.encode('ascii')
        return struct.pack('<H', len(b))+b
    def unicode_field(value):
        b = value.encode('utf-16le')
        return struct.pack('<I', len(b)//2)+b
    synthetic = struct.pack('<HI', 4, crc_name('ChatInstantMessageToClient'))
    synthetic += b''.join(ascii_field(x) for x in ['SWG', 'Lowca', 'hired'])
    synthetic += unicode_field('lol')+unicode_field('X')
    decoded = decode_chat(synthetic)
    if decoded['out_of_band'] != 'X':
        raise ValueError('Second Unicode string was not consumed')
    count2 = bytearray(synthetic)
    struct.pack_into('<H', count2, 0, 2)
    decoded2 = decode_chat(count2)
    report = {'id': 'PSWG-MESSAGES-01-VERIFICATION', 'target_sha256': digest,
              'method': 'static byte comparison plus independent documentation sample decoder',
              'memory_checks': checks, 'type_vtables': types, 'queries': queries,
              'documented_fixed_samples': examples, 'documented_chat_sample': historical_chat,
              'synthetic_nonempty_oob': {'classification': 'synthetic; layout example only, not valid OOB grammar or captured traffic',
                                         'hex': synthetic.hex(' '), 'decoded': decoded},
              'synthetic_count2': {'hex': count2.hex(' '), 'decoded': decoded2,
                                   'limitation': 'Independent decoder accepts header value; this is not a client acceptance test.'},
              'limitations': ['No client/JVM execution or observed network traffic.',
                              'Not all packet semantic handlers were traced.',
                              'The ASCII decoder here handles fixture ASCII only; native charset is not established.']}
    (EVIDENCE/'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'memory_ranges_verified': len(checks), 'retained_queries': len(queries),
                      'memory_bytes_verified': sum(c['bytes'] for c in checks),
                      'fixed_samples': len(examples), 'chat_samples': 3, 'issues': []}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binary', type=Path, default=ROOT.parent/'recovered/installation/SWGEmu.exe')
    args = parser.parse_args()
    main(args.binary)
