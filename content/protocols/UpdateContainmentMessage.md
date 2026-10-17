---
title: UpdateContainmentMessage
url: https://wiki.swganh.org/index.php/UpdateContainmentMessage
page_type: Server Packet
opcode: 56CBDE9E
revision_id: 79402
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# UpdateContainmentMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| LONG | Parent Id |
| INT | Arrangement Id |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 56CBDE9E

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00       //Operand_Count
9E DE CB 56 //UpdateContainmentMessage
62 C9 8B 12 1E 00 00 00 //Object ID
FD 85 10 00 00 00 00 00 //Cell ID
FF FF FF FF //ContainmentType?
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete