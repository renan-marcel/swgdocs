---
title: ChatAddFriend
url: https://wiki.swganh.org/index.php/ChatAddFriend
page_type: Client Packet
opcode: 6FE7BD90
revision_id: 21715
last_modified: 2008-01-11T15:05:47Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete', 'Rouse']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Unknown', 'Template:ClientPacket', 'Template:75%', 'Template:Rouse']
---

# ChatAddFriend

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | opperand count |
| INT | Op Code |
| A_STRING | Game |
| A_STRING | Galaxy |
| A_STRING | Creator |
| A_STRING | Friend Name (full path) |
| INT | ?? |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 6FE7BD90

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.
- **Rouse** - This document has been pinkified by Rouse.

## Sample Packet
```
00 09 
00 22 
04 00 
6F E7 BD 90                                       // ChatAddFriend
03 00                                             // string count
53 57 47                                          // SWG
0A 00                                             // string count
53 68 61 64 6F 77 66 69 72 65                     // Shadowfire
09 00                                             // string count
73 70 65 74 79 6E 65 73 73                        // spetyness
22 00                                             // string count
53 57 47 2E 53 68 61 64                           // SWG.Shad
6F 77 66 69 72 65 2E 74 75 74 6F 72 69 61 6C 2E   // owfire.tutorial.
43 68 61 74 2E 72 6F 75 73 65                     // Chat.rouse
01 00 00 00   // maybe flag for online or not?????????
BC 4E
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete | Rouse