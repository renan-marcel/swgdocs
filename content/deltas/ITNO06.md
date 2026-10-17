---
title: ITNO06
url: https://wiki.swganh.org/index.php/ITNO06
page_type: Baseline
opcode: 
revision_id: 39700
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:ITNOArchitectureNAV', 'Template:50%']
---

# ITNO06

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT |  |
| INT | ?? |
| ASTRING | STF File |
| INT | STF Spacer |
| ASTRING | STF Name |

## Variable Descriptions
- Obj_OperandCount = 1

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
03 5A D1 D6 13 00 00 00 // ID
4F 4E 54 49 06          // ONTI 6
32 00 00 00 
02 00 6E 00 
00 00 
0C 00 
73 70 61 63 65 5F 69 74 65 6D 5F 6E // space_item_n
00 00 00 00 
18 00 
73 6F 72 6F 73 75 75 62 5F 73 70 61 63 65 5F 79 61 63 68 74 5F 70 63 64  // sorosuub_space_yacht_pcd
19
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete