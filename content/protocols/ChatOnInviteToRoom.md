---
title: ChatOnInviteToRoom
url: https://wiki.swganh.org/index.php/ChatOnInviteToRoom
page_type: Server Packet
opcode: 0x493FE7A4
revision_id: 19348
last_modified: 2007-12-18T07:19:25Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnInviteToRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | Channel |
| A_STRING | swg |
| A_STRING | Server name |
| A_STRING | Name of Channel creator |
| A_STRING | swg |
| A_STRING | Server name |
| A_STRING | Name of Invited Person |
| INT | Nothing |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 0x493FE7A4

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 
05 B6 
00 19 
65 
05 00 
4A E7 3F 49                                           // ChatOnInviteToRoom
22 00                                                 // String count
53 57 47 2E 53 68 61 64 6F 77 66 69 72 65 2E 74 75    // SWG.Shadowfire.tu
74 6F 72 69 61 6C 2E 43 68 61 74 2E 72 6F 75 73 65    // torial.Chat.rouse
03 00                             // String count
53 57 47                          // SWG
0A 00                             // String count
53 68 61 64 6F 77 66 69 72 65     // Shadowfire
08 00                             // String count
72 75 62 69 6E 6C 65 65           // rubinlee  leader/maker of room
03 00                             // String count
53 57 47                          // SWG
0A 00                             // String count
53 68 61 64 6F 77 66 69 72 65     // Shadowfire
09 00                             // String count
73 70 65 74 79 6E 65 73 73        // spetyness // person invited
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete