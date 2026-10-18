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
_none_

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