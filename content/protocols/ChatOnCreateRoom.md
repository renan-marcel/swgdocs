---
title: ChatOnCreateRoom
url: https://wiki.swganh.org/index.php/ChatOnCreateRoom
page_type: Server Packet
opcode: 35D7CC9F
revision_id: 26325
last_modified: 2008-04-07T02:50:07Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnCreateRoom

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | ErrorCode |
| INT | ChatRoom ID |
| INT | Private Flag |
| BYTE | Moderated Flag |
| A_STRING | Room Full Address |
| A_STRING | Game |
| A_STRING | Galaxy |
| A_STRING | Creator |
| A_STRING | Game |
| A_STRING | Galaxy |
| A_STRING | Owner |
| U_STRING | Room Name |
| INT | Moderator List Size |
| A_STRING | Game |
| A_STRING | Galaxy |
| A_STRING | Moderator Name |
| INT | User List Size |
| A_STRING | Game |
| A_STRING | Galaxy |
| A_STRING | User Name |
| INT | Request ID |

## Variable Descriptions
- Op Count	     = 4
- Opcode		     = 0x35D7CC9F
- 00000001 = Private
- 00000000 = Public
- 01 = Moderated
- 00 = Open

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00
 9F CC D7 35                     // ChatOnCreateRoom
 00 00 00 00                     // unknown
 A8 14 81 02                     // Chatroom ID 
 01 00 00 00                     // might be part of the chatroom id
 01                              // unknown
 1D 00                           // String count(29)
 53 57 47 2E 4B 61 75 72 69 
 2E 64 61 6E 74 6F 6F 69 6E 65 
 2E 43 68 61 74 2E 74 65 73 74   // 'SWG.Kauri.dantooine.Chat.test'

 03 00                           // String count(3)
 53 57 47                        // 'SWG' 
 05 00                           // String count(5)
 4B 61 75 72 69                  // 'Kauri'
 08 00                           // String count(8)
 73 69 77 72 6F 74 69 61         // 'siwrotia' Creator

 03 00                           // String count(3)
 53 57 47                        // 'SWG'
 05 00                           // String count(5)
 4B 61 75 72 69                  // 'Kauri' 
 08 00                           // String count(8)
 73 69 77 72 6F 74 69 61         // 'siwrotia' Creator
 04 00 00 00                     // String count(4)
 74 00 65 00 73 00 74 00         // 'test' Room name

 01 00 00 00                     // Number of Moderators
 03 00                           // String count(3)
 53 57 47                        // 'SWG' Game tye
 05 00                           // String count(5)
 4B 61 75 72 69                  // 'Kauri' Server name
 08 00                           // String count(8)
 73 69 77 72 6F 74 69 61         // 'siwrotia' Mod names

 01 00 00 00                     // Number of users in Chat
 03 00                           // String count(3)
 53 57 47                        // 'SWG'
 05 00                           // String count(5)
 4B 61 75 72 69                  // 'Kauri'
 08 00                           // String count(8)
 73 69 77 72 6F 74 69 61         // 'siwrotia'
 01 00 00 00                     // uknown
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete