---
title: ChatOnLeaveRoom
url: https://wiki.swganh.org/index.php/ChatOnLeaveRoom
page_type: Server Packet
opcode: 60B5098B
revision_id: 26332
last_modified: 2008-04-07T04:31:24Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnLeaveRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | OpCode |
| A_STRING | Game Name |
| A_STRING | Galaxy Name |
| A_STRING | Character Name |
| INT | Error Code |
| INT | ChatRoom ID |
| INT | Request ID |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 60B5098B

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00                         // op count
8B 09 B5 60                   // ChatOnLeaveRoom
03 00                         // string count
53 57 47                      // SWG
0A 00                         // string count
53 68 61 64 6F 77 66 69 72 65 // Shadowfire
06 00                         // string count
61 6C 6C 79 6E 61             // allyna
00 00 00 00                   // string spacer
41 01 29 03                   // room id
00 00 00 00 // ??
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete