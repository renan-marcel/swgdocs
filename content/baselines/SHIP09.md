---
title: SHIP09
url: https://wiki.swganh.org/index.php/SHIP09
page_type: Baseline
opcode: 
revision_id: 78546
last_modified: 2011-07-08T04:27:51Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:SHIPArchitectureNAV', 'Template:100%']
---

# SHIP09

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| LONG | ObjectID |
| INT | Object_TYPE |
| BYTE | TYPE_# |
| INT | Object_Data_Size |
| SHORT | OpperandCount |

## Variable Descriptions
- Obj_OperandCount = 0

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
0C 5F A7 68 
04 5A D1 D6 13 00 00 00 
50 49 48 53 09 // PIHS 9
02 00 00 00 
00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete