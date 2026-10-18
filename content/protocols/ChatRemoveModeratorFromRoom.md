---
title: ChatRemoveModeratorFromRoom
url: https://wiki.swganh.org/index.php/ChatRemoveModeratorFromRoom
page_type: Client Packet
opcode: 048E3F8A
revision_id: 20961
last_modified: 2008-01-06T23:21:18Z
completion: 25%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:25%']
---

# ChatRemoveModeratorFromRoom

## Notices
_none_

## Struct
_none_

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 8A3F8E04

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **25%** - This packet has been partially reversed.

## Sample Packet
```
00 09 
00 23 
04 00 
04 8E 3F 8A                                       // ChatRemoveModeratorFromRoom
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
01 00 00 00 
20 FA
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 25% Complete