---
title: GuildRequestMessage
url: https://wiki.swganh.org/index.php/GuildRequestMessage
page_type: Server Packet
opcode: 81EB4EF7
revision_id: 20599
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# GuildRequestMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 81EB4EF7

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00  //'WORLDUPDATE 
 F7 4E EB 81  //'GuildRequestMessage 
 19 00 00 00 00 00 00 00 //'Player ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete