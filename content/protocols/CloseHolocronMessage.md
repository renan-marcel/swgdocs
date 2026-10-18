---
title: CloseHolocronMessage
url: https://wiki.swganh.org/index.php/CloseHolocronMessage
page_type: Server Packet
opcode: C0938A9D
revision_id: 44409
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# CloseHolocronMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = C0938A9D

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00 // op count
9D 8A 93 C0 // CloseHolocronMessage

This packet was created since no way to get it on live.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete