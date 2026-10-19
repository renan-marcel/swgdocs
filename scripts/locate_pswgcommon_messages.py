"""Find bounded PE32 RTTI/vtable and literal-reference candidates, without execution.

Candidates require instruction/decompiler verification; byte matches are not xrefs.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['UpdateContainmentMessage', 'SceneCreateObjectByCrc', 'ChatInstantMessageToClient']


def locate(path, names):
    raw = path.read_bytes()
    pe = struct.unpack_from('<I', raw, 0x3c)[0]
    if raw[pe:pe+4] != b'PE\0\0':
        raise ValueError('Expected PE')
    machine, count = struct.unpack_from('<HH', raw, pe+4)
    optional = pe+24
    if machine != 0x14c or struct.unpack_from('<H', raw, optional)[0] != 0x10b:
        raise ValueError('This locator handles PE32 x86 RTTI only')
    base = struct.unpack_from('<I', raw, optional+28)[0]
    start = optional+struct.unpack_from('<H', raw, pe+20)[0]
    sections = []
    for i in range(count):
        off = start+i*40
        _, rva, size, pointer = struct.unpack_from('<IIII', raw, off+8)
        sections.append({'name': raw[off:off+8].split(b'\0')[0].decode('ascii'),
                         'va': base+rva, 'offset': pointer, 'size': size,
                         'executable': bool(struct.unpack_from('<I', raw, off+36)[0] & 0x20000000)})

    def va(off):
        for s in sections:
            if s['offset'] <= off < s['offset']+s['size']:
                return s['va']+off-s['offset']
        return None

    def offset(address):
        for s in sections:
            if s['va'] <= address < s['va']+s['size']:
                return s['offset']+address-s['va']
        return None

    def find(blob, executable=None):
        results = []
        for s in sections:
            if executable is not None and executable != s['executable']:
                continue
            cursor, end = s['offset'], s['offset']+s['size']
            while True:
                found = raw.find(blob, cursor, end)
                if found < 0:
                    break
                results.append(found)
                cursor = found+1
        return results

    messages = []
    for name in names:
        descriptors = []
        for string_off in find(('.?AV'+name+'@@\0').encode('ascii'), False):
            descriptor = va(string_off)-8
            locators = []
            for ref in find(struct.pack('<I', descriptor), False):
                col_off = ref-12
                if col_off < 0:
                    continue
                signature, object_offset, ctor_offset = struct.unpack_from('<III', raw, col_off)
                if signature != 0 or object_offset > 0x10000 or ctor_offset > 0x10000:
                    continue
                col_va = va(col_off)
                if col_va is None:
                    continue
                tables = []
                for slot in find(struct.pack('<I', col_va), False):
                    table = va(slot)+4
                    entry_off = offset(table)
                    if entry_off is None:
                        continue
                    first = struct.unpack_from('<I', raw, entry_off)[0]
                    if not any(s['executable'] and s['va'] <= first < s['va']+s['size'] for s in sections):
                        continue
                    tables.append({'vtable': hex(table), 'first_function': hex(first),
                                   'code_byte_references': [hex(va(o)) for o in find(struct.pack('<I', table), True)]})
                locators.append({'locator': hex(col_va), 'object_offset': object_offset,
                                 'constructor_displacement': ctor_offset, 'vtables': tables})
            descriptors.append({'type_descriptor': hex(descriptor), 'rtti_string': hex(va(string_off)), 'locators': locators})
        literal_refs = []
        for literal_off in find(name.encode('ascii')+b'\0', False):
            literal_va = va(literal_off)
            literal_refs.append({'string_va': hex(literal_va),
                                 'code_byte_references': [hex(va(o)) for o in find(struct.pack('<I', literal_va), True)]})
        messages.append({'name': name, 'rtti': descriptors, 'literal_candidates': literal_refs})
    return {'id': 'PSWG-MESSAGES-01-LOCATOR', 'target': path.name,
            'target_sha256': hashlib.sha256(raw).hexdigest(), 'image_base': hex(base),
            'method': 'static bounded raw PE32 RTTI candidate search',
            'limitations': ['Raw immediate matches are candidates, not decoded code references.',
                            'RTTI/vtable candidates must be corroborated with Binary Ninja functions.'],
            'messages': messages}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--binary', type=Path, default=ROOT.parent/'recovered/installation/SWGEmu.exe')
    p.add_argument('--output', type=Path, default=ROOT/'data/pswgcommon-evidence/messages-01/locator.json')
    p.add_argument('names', nargs='*', default=NAMES)
    args = p.parse_args()
    report = locate(args.binary, args.names)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
