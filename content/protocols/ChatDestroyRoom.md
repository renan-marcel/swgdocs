---
title: ChatDestroyRoom
url: https://wiki.swganh.org/index.php/ChatDestroyRoom
page_type: Client Packet
opcode: 772A4B09
revision_id: 20989
last_modified: 2008-01-06T23:37:19Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ClientPacket', 'Template:75%']
---

# ChatDestroyRoom

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | Room ID |
| INT | ?? |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 094b2a77

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
03 00 // Op Count
77 2A 4B 09  // ChatDestroyRoom
82 06 29 03  // Room ID
01 00 00 00  // ??
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete