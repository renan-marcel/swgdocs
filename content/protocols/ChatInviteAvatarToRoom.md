---
title: ChatInviteAvatarToRoom
url: https://wiki.swganh.org/index.php/ChatInviteAvatarToRoom
page_type: Client Packet
opcode: D3EC7372
revision_id: 20958
last_modified: 2008-01-06T23:20:31Z
completion: 25%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:25%']
---

# ChatInviteAvatarToRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
_none_

## Variable Descriptions
- Opperand_Count	     = X
- Opcode		     = D3EC7372

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **25%** - This packet has been partially reversed.

## Sample Packet
```
00 09 
00 1E 
03 00 
D3 EC 73 72                    // ChatInviteAvatarToRoom
03 00                          // string count
53 57 47                       // SWG
0A 00                          // string count
53 68 61 64 6F 77 66 69 72 65  // Shadowfire
09 00                          // string count
73 70 65 74 79 6E 65 73 73     // spetyness
22 00                          // string count
53 57 47 2E 53 68 61 64                           // SWG.Shad
6F 77 66 69 72 65 2E 74 75 74 6F 72 69 61 6C 2E   // owfire.tutorial.
43 68 61 74 2E 72 6F 75 73 65                     // Chat.rouse..
C7 9A
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 25% Complete