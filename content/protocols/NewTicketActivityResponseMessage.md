---
title: NewTicketActivityResponseMessage
url: https://wiki.swganh.org/index.php/NewTicketActivityResponseMessage
page_type: Server Packet
opcode: 6EA42D80
revision_id: 22128
last_modified: 
completion: 25%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:Unknown', 'Template:ServerPacket', 'Template:25%']
---

# NewTicketActivityResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| BYTE | ?? |
| INT | ?? |

## Variable Descriptions
- Op Count	     = 3
- Opcode		     = 6EA42D80

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **25%** - This packet has been partially reversed.

## Sample Packet
```
03 00 
80 2D A4 6E // NewTicketActivityResponseMessage
00 
01 00 00 00 
72 04 60 // comp +crc
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 25% Complete