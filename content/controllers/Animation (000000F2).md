---
title: Animation (000000F2)
url: https://wiki.swganh.org/index.php/Animation_%28000000F2%29
page_type: Object Controller
opcode: 000000F2
revision_id: 22001
last_modified: 2008-01-17T23:42:40Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:A string', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# Animation (000000F2)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | String Size |
| A_STRING | Animation |

## Variable Descriptions
- controllerID	     = 000000F2

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00          // Op Count
46 5E CE 80    // ObjController       
1B 00 00 00    // Sub-Op Code							
F2 00 00 00    // Command Op (Animation)
F6 14 08 2E 21 00 00 00 // Target ID (NPC Performing Animation)
00 00 00 00        // Table of Strings Error ID #
05 00              // string size
77 61 76 65 31	   // wave1 (animation)
================================================================
05 00          // Op Count
46 5E CE 80    // ObjController       
1B 00 00 00    // Sub-Op Code							
F2 00 00 00    // Command Op (Animation)
71 E2 DB D9 00 00 00 00 // character ID
00 00 00 00 
0E 00 // string size
73 6B 69 6C 6C 5F 61 63 74 69 6F 6E 5F 31  // skill_action_1
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete