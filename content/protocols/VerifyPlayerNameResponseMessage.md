---
title: VerifyPlayerNameResponseMessage
url: https://wiki.swganh.org/index.php/VerifyPlayerNameResponseMessage
page_type: Server Packet
opcode: F4C498FD
revision_id: 19964
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# VerifyPlayerNameResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| BYTE | Result |
| INT | Null |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = F4C498FD

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
09  // Op Count
FD 98 C4 F4 // VerifyPlayerNameResponseMessage
01  // Verify Flag
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete