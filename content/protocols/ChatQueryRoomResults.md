---
title: ChatQueryRoomResults
url: https://wiki.swganh.org/index.php/ChatQueryRoomResults
page_type: Server Packet
opcode: C4DE864E
revision_id: 28723
last_modified: 2008-05-11T06:37:32Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# ChatQueryRoomResults

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | OperandCount |
| INT | Opcode |
| INT | UserListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | UserName |
| INT | InvitedUserListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | InvitedUserName |
| INT | ModeratorListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | ModeratorName |
| INT | BannedUserListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | BannedUserName |
| INT | RequestID |
| INT | RoomID |
| INT | PrivateFlag |
| BYTE | ModeratedFlag |
| ASTRING | RoomPathName |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | Owner |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | Creator |
| USTRING | RoomTitle |
| INT | ModeratorListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | ModeratorName |
| INT | UserListSize |
| ASTRING | Game |
| ASTRING | Server |
| ASTRING | UserName |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = C4DE864E

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 
06 1A 
07 00                         // op count
4E 86 DE C4                   // ChatQueryRoomResults
01 00 00 00                   // ???????????????????????????????  
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
08 00                         // string count
72 75 62 69 6E 6C 65 65       // rubinlee
01 00 00 00                   // ??????????????????????????????? 
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
08 00                         // string count
72 75 62 69 6E 6C 65 65       // rubinlee
01 00 00 00                   // ??????????????????????????????? 
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
08 00                         // string count
72 75 62 69 6E 6C 65 65       // rubinlee
00 00 00 00                   // ???????????????????????????????
00 00 00 00                   // ???????????????????????????????
89 06 29 03                   // Room ID
01 00 00 00                   // ???????????????????????????????
01                            // ???????????????????????????????
22 00                                             // string count
53 57 47 2E 53 68                                 // SWG.Sh
61 64 6F 77 66 69 72 65 2E 74 75 74 6F 72 69 61   // adowfire.tutoria
6C 2E 43 68 61 74 2E 72 6F 75 73 65               // l.Chat.rouse
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
08 00                         // string count
72 75 62 69 6E 6C 65 65       // rubinlee
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
08 00                         // string count
72 75 62 69 6E 6C 65 65       // rubinlee
09 00 00 00                   // string count
52 00 6F 00 75 00 73 00 65 00 // R.o.u.s.e.
2D 00 73 00 77 00 67 00       // -.s.w.g
00 00 00 00                   // ???????????????????????????????
00 00 00 00                   // ????????????????????????????
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete