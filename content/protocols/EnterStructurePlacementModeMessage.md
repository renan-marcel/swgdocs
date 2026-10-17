---
title: EnterStructurePlacementModeMessage
url: https://wiki.swganh.org/index.php/EnterStructurePlacementModeMessage
page_type: Server Packet
opcode: E8A54DC1
revision_id: 44378
last_modified: 2008-08-22T15:56:26Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# EnterStructurePlacementModeMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| LONG | DeedID |
| A_STRING | Object String |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = E8A54DC1

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 // Op Count
C1 4D A5 E8 // EnterStructurePlacementMode
9C 41 49 D4 1A 00 00 00 // Deed ID
46 00                                           // String Count
6F 62 6A 65 63 74 2F 62 75 69                   // object/bu
6C 64 69 6E 67 2F 70 6C 61 79 65 72 2F 73 68 61 // ilding/player/sh
72 65 64 5F 70 6C 61 79 65 72 5F 68 6F 75 73 65 // ared_player_hous
5F 74 61 74 6F 6F 69 6E 65 5F 73 6D 61 6C 6C 5F // e_tatooine_small
73 74 79 6C 65 5F 30 31 2E 69 66 66             // style_01.iff
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete