---
title: ClientCreateCharacterSuccess
url: https://wiki.swganh.org/index.php/ClientCreateCharacterSuccess
page_type: Server Packet
opcode: 1DB575CC
revision_id: 20388
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# ClientCreateCharacterSuccess

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | CharacterID |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 1DB575CC

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 //Op Count
CC 75 B5 1D // ClientCreateCharacterSuccess
15 23 C9 00 00 00 00 00 // Character ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete