---
title: ChatFriendsListUpdate
url: https://wiki.swganh.org/index.php/ChatFriendsListUpdate
page_type: ServerPacket
opcode: 6CD2FCD8
revision_id: 21069
last_modified: 2008-01-07T02:47:26Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# ChatFriendsListUpdate

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | SWG |
| A_STRING | Server Name |
| A_STRING | Friend |
| BYTE | OnlineFlag |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 6CD2FCD8

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00                         // Opcode Count
D8 FC D2 6C                   // ChatFriendsListUpdate
03 00                         // String Count
53 57 47                      // SWG
0A 00                         // String Count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
09 00                         // String Count
74 69 6A 61 69 72 61 75 6E    // tijairaun
00                            // Online Status 0 = off 1 = on
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete