---
title: ITNO03
url: https://wiki.swganh.org/index.php/ITNO03
page_type: Baseline
opcode: 
revision_id: 39724
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ITNOArchitectureNAV', 'Template:100%']
---

# ITNO03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| FLOAT | Complexity |
| ASTRING | STF File |
| INT | STF Spacer |
| ASTRING | STF Name |
| USTRING | CustomName |
| INT | Volume |
| INT | GenericInt(CellID,SchematicQuantity) |

## Variable Descriptions
- ObjectOpperandCount = 5

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
03 5A D1 D6 13 00 00 00 // ID
4F 4E 54 49 03          // ONTI 3
3E 00 00 00 
05 00 00 00 
80 3F 
0C 00 
73 70 61 63 65 5F 69 74 65 6D 5F 6E  // space_item_n
00 00 00 00 
18 00 
73 6F 72 6F 73 75 75 62 5F                   // sorosuub_
73 70 61 63 65 5F 79 61 63 68 74 5F 70 63 64 // space_yacht_pcd
00 00 00 00 
01 00 00 00 
00 00 00 00 
49
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete