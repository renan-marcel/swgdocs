---
title: SceneCreateObjectByCrc
url: https://wiki.swganh.org/index.php/SceneCreateObjectByCrc
page_type: Server Packet
opcode: FE89DDEA
revision_id: 258788
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Float', 'Template:Byte', 'Template:Beginlist', 'Template:Unknown', 'Template:Endlist', 'Template:ServerPacket', 'Template:75%']
---

# SceneCreateObjectByCrc

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| FLOAT | QuaternionX |
| FLOAT | QuaternionY |
| FLOAT | QuaternionZ |
| FLOAT | QuaternionW |
| FLOAT | X-Coordinate |
| FLOAT | Y-Coordinate |
| FLOAT | Z-Coordinate |
| INT | ObjectCRC |
| BYTE | ByteFlag |

## Variable Descriptions
- Operand_Count	     = 5
- Opcode		     = FE89DDEA

## Notes

<!-- pswgcommon-message-crosscheck:start -->
### PSWGCommon / client cross-check

PSWGCommon encodes 47 bytes: operand count 5 at offset 0, opcode FE89DDEA at 2, object ID at 6, quaternion float32 x/y/z/w at 14/18/22/26, position float32 x/y/z at 30/34/38, object CRC at 42, and ByteFlag at 46. Offsets exclude SOE framing; numeric fields are little-endian.

The client reader at 0x00AD51B0 registers NetworkId, Transform, uint32 and bool (object members +0x38, +0x48, +0x7C, +0x84). Transform pack/unpack at 0x005200C0/0x005201A0 uses seven float32 values in quaternion x/y/z/w then position x/y/z order (28 bytes), converting between quaternion and the internal matrix. Internal member offsets are not wire offsets.

PSWGCommon Location transmits orientation and position only, not terrain. Its doubles are narrowed to float32. PSWGCommon names ByteFlag hyperspace and emits 0/1; the full gameplay meaning of the client's bool remains only partially established, so the historical 75% completion is retained.

See [client message analysis](../guides/pswgcommon-client-messages.md). Evidence: [BN-PSWG-SCENE-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-SCENE-READ.json), [BN-PSWG-TRANSFORM-PACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-TRANSFORM-PACK.json), [BN-PSWG-TRANSFORM-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-TRANSFORM-UNPACK.json).
<!-- pswgcommon-message-crosscheck:end -->

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00       //Operand_Count
EA DD 89 FE //SceneCreateObjectByCrc
62 C9 8B 12 1E 00 00 00 //Object ID
00 00 00 00 //oX
D2 3A EA BE //oY
00 00 00 00 //oZ
EA A3 63 3F //oW
F6 28 A4 41 //x
44 1E 65 BF //y
33 33 83 40 //z
77 D6 B2 68 //object/mobile/shared_muftak.iff
00          //ByteFlag - Hyperspacing
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete