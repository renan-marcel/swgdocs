---
title: PlayClientEffectObjectMessage
url: https://wiki.swganh.org/index.php/PlayClientEffectObjectMessage
page_type: Server Packet
opcode: 8855434A
revision_id: 21817
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# PlayClientEffectObjectMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | File |
| A_STRING | AuxString |
| LONG | Object ID |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 8855434A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
4A 43 55 88 // PlayClientEffectObjectMessage 
2E 00 // String count 
63 6C 69 65 6E 74 65 66 66 65 63 74 2F 63 
6F 6D 62 61 74 5F 73 70 65 63 69 61 6C 5F 
64 65 66 65 6E 64 65 72 5F 62 6C 69 6E 64 
2E 63 65 66 // clienteffect/coender_blind.cef 
00 00 
19 00 00 00 00 00 00 00 // Target ID 
------------------------------------------------
05 00 
4A 43 55 88 // PlayClientEffectObjectMessage
1E 00 // string count
63 6C 69 65 6E 74 65 66 66 65 63 74 2F 65 6C 65 76 // clienteffect/elev
61 74 6F 72 5F 72 69 73 65 2E 63 65 66             //  ator_rise.cef
00 00 
71 E2 DB D9 00 00 00 00 // character ID
00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete