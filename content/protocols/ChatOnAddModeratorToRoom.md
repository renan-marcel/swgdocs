---
title: ChatOnAddModeratorToRoom
url: https://wiki.swganh.org/index.php/ChatOnAddModeratorToRoom
page_type: Server Packet
opcode: 36A03858
revision_id: 28709
last_modified: 2008-05-11T06:07:31Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnAddModeratorToRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | OperandCount |
| INT | Opcode |
| A_STRING | Game |
| A_STRING | Server |
| A_STRING | Target |
| A_STRING | Game |
| A_STRING | Server |
| A_STRING | Moderator |
| INT | ErrorCode |
| A_STRING | RoomPathName |
| INT | RequestID |

## Variable Descriptions
- Opperand_Count	     = 6
- Opcode		     = 0x36A03858

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
06 00 
58 38 A0 36                                       // ChatOnAddModeratorToRoom
03 00                                             // string count
53 57 47                                          // SWG
0A 00                                             // string count
53 68 61 64 6F 77 66 69 72 65                     // Shadowfire
09 00                                             // string count
73 70 65 74 79 6E 65 73 73                        // spetyness
03 00                                             // string count
53 57 47                                          // SWG
0A 00                                             // string count
53 68 61 64 6F 77 66 69 72 65                     // Shadowfire 
08 00                                             // string count
72 75 62 69 6E 6C 65 65                           // rubinlee
00 00 00 00 
22 00                                             // string count
53 57 47 2E 53 68 61 64 6F                        // SWG.Shado
77 66 69 72 65 2E 74 75 74 6F 72 69 61 6C 2E 43   // wfire.tutorial.C
68 61 74 2E 72 6F 75 73 65                        // hat.rouse....O.
01 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete