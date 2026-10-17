---
title: ClientRandomNameRequest
url: https://wiki.swganh.org/index.php/ClientRandomNameRequest
page_type: Client Packet
opcode: D6D1B6D1
revision_id: 21685
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ClientPacket', 'Template:100%']
---

# ClientRandomNameRequest

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | Player_Race_IFF |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = D6D1B6D1

## Notes
- **NOTE:** Do not confused with creature objects, or any other object types. These are located in the player objects folder. Used also in character listing and char creation.

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // op Count
D1 B6 D1 D6 // ClientRandomNameRequest
25 00 // string count
6F 62 6A 65 63 74 2F                       // object/
63 72 65 61 74 75 72 65 2F                 // creature
70 6C 61 79 65 72 2F                       // /player/
68 75 6D 61 6E 5F 6D 61 6C 65 2E 69 66 66  // human_male.iff
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete