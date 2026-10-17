---
title: ChatOnUninviteFromRoom
url: https://wiki.swganh.org/index.php/ChatOnUninviteFromRoom
page_type: Server Packet
opcode: BE33C7E8
revision_id: 28731
last_modified: 2008-05-11T11:36:15Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnUninviteFromRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | Room Name |
| A_STRING | Game |
| A_STRING | Server |
| A_STRING | Moderator |
| A_STRING | Game |
| A_STRING | Server |
| A_STRING | Target |
| INT | ErrorCode |
| INT | RequestID |

## Variable Descriptions
- Opperand_Count	     = 6
- Opcode		     = BE33C7E8

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 
05 0C 
00 19 
65 
06 00 
E8 C7 33 BE                                         // ChatOnUninviteFromRoom
22 00                                               // string count
53 57 47 2E 53 68 61 64 6F 77 66 69 72 65 2E 74 75  // SWG.Shadowfire.tu
74 6F 72 69 61 6C 2E 43 68 61 74 2E 72 6F 75 73 65  // torial.Chat.rouse
03 00                              // string count
53 57 47                           // SWG
0A 00                              // string count
53 68 61 64 6F 77 66 69 72 65      // Shadowfire
08 00                              // string count
72 75 62 69 6E 6C 65 65            // rubinlee
03 00                              // string count
53 57 47                           // SWG
0A 00                              // string count
53 68 61 64 6F 77 66 69 72 65      // Shadowfire 
05 00                              // string count
72 6F 75 73 65                     // rouse
00 00 00 00 
01 00 00 00 // RequestID
F3
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete