---
title: NewbieTutorialRequest
url: https://wiki.swganh.org/index.php/NewbieTutorialRequest
page_type: Client Packet
opcode: 90DD61AF
revision_id: 21599
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# NewbieTutorialRequest

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Code |
| INT | Opcode |
| A_STRING | clientReady |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 90DD61AF

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
AF 61 DD 90 // NewbieTutorialRequest
0B 00 // String count
63 6C 69 65 6E 74 52 65 61 64 79 // clientReady
```

## Related Pages
- [[NewbieTutorialResponse]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete