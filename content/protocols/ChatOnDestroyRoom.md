---
title: ChatOnDestroyRoom
url: https://wiki.swganh.org/index.php/ChatOnDestroyRoom
page_type: Packet
opcode: E8EC5877
revision_id: 28702
last_modified: 2008-05-11T05:54:34Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnDestroyRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | Game |
| A_STRING | Server |
| A_STRING | Owner |
| INT | ErrorCode |
| INT | Room ID |
| INT | RequestID |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 0xE8EC5877

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
ChatOnDestroyRoom

00 09 
0C 6B 
00 19 
2B 
05 00                         // op_count
77 58 EC E8                   // ChatOnDestroyRoom
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
06 00                         // string count
73 79 73 74 65 6D             // system
00 00 00 00                   // string spacer
4C 06 29 03                   // Room id 
00 00 00 00 
2B 
05 00                         // op_count
77 58 EC E8                   // ChatOnDestroyRoom
03 00                         // string count
53 57 47                      // SWG
0A 00                         // String count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire 
06 00                         // string count
73 79 73 74 65 6D             // system
00 00 00 00                   // string spacer 
4A 06 29 03                   // Room id
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete