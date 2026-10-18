---
title: HINO03
url: https://wiki.swganh.org/index.php/HINO03
page_type: Baseline
opcode: 
revision_id: 66705
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:HINOArchitectureNAV', 'Template:50%']
---

# HINO03

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjOpperandCount |
| INT | Opcode |
| FLOAT | Complexity |
| ASTRING | STF File |
| INT | STF Spacer |
| ASTRING | STF Name |
| USTRING | CustomName |
| INT | Volume |
| CSTRING | CustomizationString |
| INT | ??List |
| INT | UpdateCounter |
| INT | ?? |
| INT | OptionsBitmask |
| INT | Timer(Incap/Prototype) |
| INT | ConditionDamage |
| INT | MaxCondition |
| BYTE | ?? |
| BYTE | ActiveFlag |
| FLOAT | PowerReserves |
| FLOAT | PowerCost |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselineMessage   
36 21 FF FB 1A 00 00 00  // object ID
4F 4E 49 48 03           // ONIH 3
56 00 00 00 
0E 00 
00 00 80 3F 
0E 00                    // string count
69 6E 73 74 61 6C 6C     // instal
61 74 69 6F 6E 5F 6E     // lation_n
00 00 00 00 
0E 00 
77 69 6E 64 5F 67 65 6E 65 72 61 74 6F 72      // wind_generator
00 00 00 00 
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 01 
00 00 00 00 
00 00 00 00 
00 00 E8 03 
00 00 01 00 
00 00 00 00 
00 00 00 00 
25
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete