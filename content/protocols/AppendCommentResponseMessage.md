---
title: AppendCommentResponseMessage
url: https://wiki.swganh.org/index.php/AppendCommentResponseMessage
page_type: Server Packet
opcode: A04A3ECA
revision_id: 20427
last_modified: 2007-12-31T20:38:24Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# AppendCommentResponseMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| INT | Message |
| INT | Ticket |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = A04A3ECA

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 // Op Count
CA 3E 4A A0 // AppendCommentResponseMessage
01 00 00 00 // Message  
12 00 00 00 // Ticket number

This packet was created as no packets exsisted
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete