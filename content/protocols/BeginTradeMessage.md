---
title: BeginTradeMessage
url: https://wiki.swganh.org/index.php/BeginTradeMessage
page_type: Server Packet
opcode: 325932D8
revision_id: 19983
last_modified: 2007-12-28T18:40:11Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# BeginTradeMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | OpCode |
| LONG | Object Id |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 325932D8

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00       // Op Count
D8 32 59 32 // BeginTradeMessage
00 AB CD 19 20 00 00 00 // Object Id
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete