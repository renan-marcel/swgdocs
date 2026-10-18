---
title: ChatRoomList
url: https://wiki.swganh.org/index.php/ChatRoomList
page_type: Server Packet
opcode: 70DEB197
revision_id: 28725
last_modified: 2008-05-11T06:41:10Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete', 'Nogard']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# ChatRoomList

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | OperandCount |
| INT | Opcode |
| INT | RoomListSize |
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
- Opperand_Count	     = 2
- Opcode		     = 70DEB197

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 
97 B1 DE 70 // ChatRoomList
01 00 00 00 // Numberof_Chatrooms
5D 0A 72 02 // ChatRoom_ID
01 00 00 00 // NumberOf_RoomNames
00          // byte flag
27 00                                  // string count
53 57 47 2E 47 6F 72 61 74 68          // SWG.Gorath
2E 67 72 6F 75 70 2E                   // .group.
31 36 31 34 31 38 33 30 39 32 32 31 2E // 161418309221.   	
47 72 6F 75 70 43 68 61 74             // GroupChat
03 00             // string count
53 57 47          // SWG
06 00	          // string count	
47 6F 72 61 74 68 // Gorath
06 00             // string count
73 79 73 74 65 6D // system
03 00             // string count
53 57 47          // SWG
06 00             // string count
47 6F 72 61 74 68 // Gorath 
06 00             // string count
73 79 73 74 65 6D // system
0C 00 00 00                                  // u-string count
31 00 36 00 31 00 34 00 31 00 38 00 33 00 30 // 161418309221
00 39 00 32 00 32 00 31 00 
01 00 00 00  // moderator count
03 00             // string count
53 57 47          // SWG
06 00             // string count
47 6F 72 61 74 68 // Gorath 
06 00             // string count
73 79 73 74 65 6D // system
02 00 00 00   // user count
03 00             // string count
53 57 47          // SWG
06 00             // string count
47 6F 72 61 74 68 // Gorath
08 00                   // string count
70 61 74 72 69 7A 69 61 // patrizia
03 00             // string count
53 57 47          // SWG
06 00             // string count
47 6F 72 61 74 68 // Gorath
06 00             // string count
73 79 73 74 65 6D // system
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete | Nogard