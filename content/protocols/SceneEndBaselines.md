---
title: SceneEndBaselines
url: https://wiki.swganh.org/index.php/SceneEndBaselines
page_type: Server Packet
opcode: 2C436037
revision_id: 20407
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# SceneEndBaselines

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | Object ID |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 2C436037

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
37 60 43 2C // SceneEndBaselines
9A 96 98 00 00 00 00 00 // Object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete