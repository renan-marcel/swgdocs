"""Record the bounded Binary Ninja comparison as a separate history batch.

Run the workspace's scripts/update_history.py afterward to render the history.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = 'data/pswgcommon-evidence/messages-01/'


def record():
    verification = json.loads((ROOT/EVIDENCE/'verification.json').read_text(encoding='utf-8'))
    if not verification['memory_checks'] or not all(c['matches'] for c in verification['memory_checks']):
        raise ValueError('Static memory verification required')
    specs = [
        ('UpdateContainmentMessage', '56CBDE9E', 5, '0x00adc6d0', ['0x015eb2d4', '0x015eb2cc'], '100%',
         'Layout estático verificado',
         'Opcode + dois NetworkIds de 8 bytes + int de 4 bytes; 26 bytes. Registro dos membros +0x38/+0x48/+0x58. Semântica dos arrangement IDs não foi rastreada.',
         ['BN-PSWG-CONTAIN-READ', 'BN-PSWG-NETID-UNPACK64', 'BN-PSWG-ARCHIVE-PACK']),
        ('SceneCreateObjectByCrc', 'FE89DDEA', 12, '0x00ad51b0', ['0x015eafe8', '0x015eafe0'], '75%',
         'Layout estático; semântica parcial',
         'NetworkId, Transform wire de 28 bytes (quaternion xyzw + posição xyz), CRC uint32 e bool; 47 bytes. Matriz interna de 48 bytes. ByteFlag permanece com semântica parcial; completude histórica mantida em 75%.',
         ['BN-PSWG-SCENE-READ', 'BN-PSWG-TRANSFORM-PACK', 'BN-PSWG-TRANSFORM-UNPACK']),
        ('ChatInstantMessageToClient', '3C565CED', 7, '0x00af2610', ['0x015eba3c', '0x015eba34'], '100%',
         'Layout estático verificado',
         'ChatAvatarId (três strings de bytes) + duas strings Unicode. INT 0 final corrigido como comprimento da segunda string vazia. Contador nativo 4 versus encoder PSWGCommon 2. Conteúdo OOB e aceitação por todas as camadas não foram rastreados.',
         ['BN-PSWG-CHAT-READ', 'BN-PSWG-AVATAR-UNPACK', 'BN-PSWG-UNICODE-UNPACK', 'BN-PSWG-ARCHIVE-PACK', 'BN-PSWG-ARCHIVE-UNPACK']),
    ]
    packets = []
    for name, opcode, fields, address, vtables, completion, status, details, ids in specs:
        packets.append({'name': name, 'opcode': opcode, 'section': 'protocols', 'section_name': 'Protocols',
                        'direction': 'S→C', 'category': 'PSWGCommon / client cross-check',
                        'url': f'protocols/{name}.html', 'fields_count': fields,
                        'unpack_address': address, 'vtables': vtables, 'completion': completion,
                        'reversal_details': details, 'status': status,
                        'evidence_scope': 'static layout only; no client/JVM execution or network capture',
                        'target_sha256': verification['target_sha256'],
                        'evidence_ids': ids, 'evidence_urls': [EVIDENCE+i+'.json' for i in ids],
                        'analysis_url': 'guides/pswgcommon-client-messages.html'})
    path = ROOT/'data/reversal_history.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    previous = json.loads(path.read_text(encoding='utf-8'))
    batch = {'batch_id': 3, 'date': '2026-10-19',
             'title': 'PSWGCommon: contenção, criação de objetos e chat confrontados com Binary Ninja',
             'description': 'Três layouts comparados com readers/writers nativos. Corrige o tipo do campo final de chat e registra diferenças da biblioteca, mantendo limites semânticos e completudes existentes.',
             'methodology': 'Binary Ninja MCP direto; RTTI -> vtable -> registro AutoVariable -> codecs. 46 respostas retidas e nove trechos de memória comparados com o PE. Sem execução ou tráfego.',
             'packets': packets}
    old = next((b for b in data['batches'] if b.get('batch_id') == 3), None)
    if old is not None and old.get('title') != batch['title']:
        raise ValueError('History batch 3 already belongs to another investigation')
    data['batches'] = [b for b in data['batches'] if b.get('batch_id') != 3]+[batch]
    order = 0
    for b in sorted(data['batches'], key=lambda item: item['batch_id']):
        for packet in b['packets']:
            order += 1
            packet['order'] = order
    data['batches'].sort(key=lambda item: item['batch_id'], reverse=True)
    data['total_reversed'] = order
    data.pop('last_updated_note', None)
    comparable = lambda value: {k: v for k, v in value.items() if k not in {'last_updated', 'last_updated_note'}}
    if comparable(data) != comparable(previous) or 'last_updated_note' in previous:
        data['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    updated = json.dumps(data, ensure_ascii=False, indent=2)+'\n'
    if path.read_text(encoding='utf-8') != updated:
        path.write_text(updated, encoding='utf-8')
    print(f'Recorded batch 3; {order} history entries. Render with workspace scripts/update_history.py.')


if __name__ == '__main__':
    record()
