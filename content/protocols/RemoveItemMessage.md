---
title: RemoveItemMessage
url: https://wiki.swganh.org/index.php/RemoveItemMessage
page_type: Server Packet
opcode: 4417AF8B
revision_id: 20583
last_modified: 2008-01-03T04:30:55Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# RemoveItemMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| LONG | ObjectID |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 4417AF8B

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00
8B AF 17 44
DE AD BA BE 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete