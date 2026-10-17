---
title: ChatBanAvatarFromRoom
url: https://wiki.swganh.org/index.php/ChatBanAvatarFromRoom
page_type: Client Packet
opcode: 9401FAD9
revision_id: 21681
last_modified: 2008-01-10T16:01:24Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Unknown', 'Template:ClientPacket', 'Template:75%']
---

# ChatBanAvatarFromRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | Game |
| A_STRING | Server Name |
| A_STRING | Moderator Name |
| A_STRING | Full Room Name |
| INT | ?? |

## Variable Descriptions
- Op Count	     = 4
- Opcode		     = D9FA0194

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
04 00 
94 01 FA D9                                        // ChatBanAvatarFromRoom
03 00                                              // String Count
53 57 47                                           // SWG
0A 00                                              // string count
53 68 61 64 6F 77 66 69 72 65                      // Shadowfire
09 00                                              // string count
73 70 65 74 79 6E 65 73 73                         // spetyness
22 00                                              // string count 
53 57 47 2E 53 68 61 64                            // SWG.Shad
6F 77 66 69 72 65 2E 74 75 74 6F 72 69 61 6C 2E    // owfire.tutorial.
43 68 61 74 2E 72 6F 75 73 65                      // Chat.rouse
01 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete