---
title: ChatOnRemoveModeratorFromRoom
url: https://wiki.swganh.org/index.php/ChatOnRemoveModeratorFromRoom
page_type: Server Packet
opcode: 1342FC47
revision_id: 28713
last_modified: 2008-05-11T06:28:36Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnRemoveModeratorFromRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | SWG |
| A_STRING | Galaxy |
| A_STRING | Target |
| A_STRING | SWG |
| A_STRING | Galaxy |
| A_STRING | Moderator |
| INT | Success Bitmask |
| A_STRING | ErrorCode |
| INT | RequestID |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = 1342FC47

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 
05 C7 
00 19 
69 
06 00 
47 FC 42 13                                       // ChatOnRemoveModeratorFromRoom
03 00                                             // string count
53 57 47                                          // SWG
0A 00                                             // string count
53 68 61 64 6F 77 66 69 72 65                     // Shadowfire
09 00                                             // string count 
73 70 65 74 79 6E 65 73 73                        // spetyness  / person removed from chat
03 00                                             // string count
53 57 47                                          // SWG
0A 00                                             // string count
53 68 61 64 6F 77 66 69 72 65                     // Shadowfire
08 00                                             // string count
72 75 62 69 6E 6C 65 65                           // rublinlee / mod that removed the person
00 00 00 00 
22 00                                             // string count 
53 57 47 2E 53 68                                 // SWG.Sh
61 64 6F 77 66 69 72 65 2E 74 75 74 6F 72 69 61   // adowfire.tutoria
6C 2E 43 68 61 74 2E 72 6F 75 73 65               // l.Chat.rouse
01 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete