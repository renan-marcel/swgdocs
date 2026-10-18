---
title: MSCO06
url: https://wiki.swganh.org/index.php/MSCO06
page_type: Baseline
opcode: 
revision_id: 79175
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:MSCOArchitectureNAV', 'Template:50%']
---

# MSCO06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | ServerID |
| CSTRING | CustomizationString |
| ASTRING | CustomizationModel |
| INT | prototypeCRC |
| BYTE | ActiveFlag |
| BYTE | SlotCount |

## Variable Descriptions
- Obj_OperandCount = 6

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
24 2A FA 04 0F 00 00 00 // ID
4F 43 53 4D 06          // OCSM 6
18 00 00 00 
07 00 6E 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 
8B 3C 1D F1 
00 00 19
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete