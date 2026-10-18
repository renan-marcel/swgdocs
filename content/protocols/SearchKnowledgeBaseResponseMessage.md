---
title: SearchKnowledgeBaseResponseMessage
url: https://wiki.swganh.org/index.php/SearchKnowledgeBaseResponseMessage
page_type: Server Packet
opcode: 7CBC8F67
revision_id: 29611
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Beginlist', 'Template:U string', 'Template:A string', 'Template:Unknown', 'Template:Endlist', 'Template:ServerPacket', 'Template:75%']
---

# SearchKnowledgeBaseResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| INT | Options |
| INT | Result Count |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 7CBC8F67

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
03 00 
67 8F BC 7C 
00 00 00 00 
01 00 00 00 
18 00 00 00 
40 00 6B 00 62 00 2F 00 6B 00 62 00 5F 00 
68 00 6f 00 75 00 73 00 69 00 6E 00 67 00 5F 
00 6E 00 3A 00 68 00 6F 00 75 00 73 00 69 00 6E 00 67 00
05 00 
31 35 36 39 39 
01 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete