---
title: UpdatePvpStatusMessage
url: https://wiki.swganh.org/index.php/UpdatePvpStatusMessage
page_type: Server Packet
opcode: 08A1C126
revision_id: 78277
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# UpdatePvpStatusMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | PVPStatus |
| INT | Faction |
| LONG | ObjectID |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 08A1C126

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00 // Op Count
26 C1 A1 08 // UpdatePvpStatusMessage
02 00 00 00 // PVP status
00 00 00 00 // Faction
A1 56 90 19 17 00 00 00 // Object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete