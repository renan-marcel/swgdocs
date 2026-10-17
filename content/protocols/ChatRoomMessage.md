---
title: ChatRoomMessage
url: https://wiki.swganh.org/index.php/ChatRoomMessage
page_type: Server Packet
opcode: CD4CE444
revision_id: 28733
last_modified: 2008-05-11T11:50:04Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete', 'Nogard']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ChatRoomMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | Game Name |
| A_STRING | Galaxy Name |
| A_STRING | Character Name |
| INT | Room ID |
| U_STRING | Message |
| U_STRING | OutOfBandPackage |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = CD4CE444

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
44 E4 4C CD                       // ChatRoomMessage
03 00                             // string count
53 57 47                          // SWG
0A 00                             // String count
53 68 61 64 6F 77 66 69 72 65     // Shadowfire
05 00                             // string count
65 73 27 65 6D                    // es'em
68 D5 28 03                       // Room ID
0D 00 00 00                                     // string count
61 00 6E 00 79 00                               // a.n.y.
6F 00 6E 00 65 00 20 00 61 00 72 00 6F 00 75 00 // o.n.e...a.r.o.u.
6E 00 64 00                                     // n.d
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete | Nogard