---
title: UpdatePostureMessage
url: https://wiki.swganh.org/index.php/UpdatePostureMessage
page_type: Server Packet
opcode: 0BDE6B41
revision_id: 21516
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# UpdatePostureMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| BYTE | PostureID |
| LONG | ObjectID |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 0BDE6B41

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 // Op Count
41 6B DE 0B // UpdatePostureMessage
00 // Posture ID
79 56 90 19 17 00 00 00 // object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete