---
title: NewbieTutorialEnableHudElement
url: https://wiki.swganh.org/index.php/NewbieTutorialEnableHudElement
page_type: Server Packet
opcode: CA375124
revision_id: 22611
last_modified: 
completion: 50%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Unknown', 'Template:Byte', 'Template:ServerPacket', 'Template:50%']
---

# NewbieTutorialEnableHudElement

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | ALL |
| INT | ?? |
| BYTE | ?? |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = CA375124

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **50%** - This packet has been partially reversed.

## Sample Packet
```
04 00       // Op Count
24 51 37 CA // NewbieTutorialEnableHudElement
03 00       // string count
61 6C 6C    // all
01 00 00 00 // ??
00          // ??
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete