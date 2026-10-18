---
title: DenyTradeMessage
url: https://wiki.swganh.org/index.php/DenyTradeMessage
page_type: Server Packet
opcode: 6EC28670
revision_id: 21553
last_modified: 2008-01-09T19:20:54Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# DenyTradeMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 6EC28670

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00 // Op Count
70 86 C2 6E // DenyTradeMessage
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete