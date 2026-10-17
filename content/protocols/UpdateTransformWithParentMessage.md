---
title: UpdateTransformWithParentMessage
url: https://wiki.swganh.org/index.php/UpdateTransformWithParentMessage
page_type: Server Packet
opcode: C867AB5A
revision_id: 20321
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# UpdateTransformWithParentMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | CellID |
| LONG | ObjectID |
| SHORT | PositionX |
| SHORT | PositionY |
| SHORT | PositionZ |
| INT | UpdateCounter |
| BYTE | Posture |
| BYTE | Direction |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = C867AB5A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
09 00 // op count
5A AB 67 C8 // UpdateTransformWithParentMessage
C8 EE 40 00 00 00 00 00 // Cell ID
2A 98 F8 28 00 00 00 00 // Object ID
C7 01 // x
07 00 // y
AB 00 // z
92 2A 00 00 // counter
04 // posture
00 // direction
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete