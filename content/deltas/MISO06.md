---
title: MISO06
url: https://wiki.swganh.org/index.php/MISO06
page_type: Baseline
opcode: 
revision_id: 51742
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:MISOArchitectureNAV', 'Template:75%']
---

# MISO06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | ServerID |

## Variable Descriptions
- Obj_OperandCount = 1

## Notes
_none_

## Tags
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
B3 85 A4 1C 17 00 00 00  // ID
4F 53 49 4D 06           // OSIM 6
0E 00 00 00 
02 00 6E 00 
00 00 00 00 
00 00 00 00 
00 00 19
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete