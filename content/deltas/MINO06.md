---
title: MINO06
url: https://wiki.swganh.org/index.php/MINO06
page_type: Baseline
opcode: 
revision_id: 21706
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:MINOArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:50%']
---

# MINO06

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Baseline Opcode |
| LONG | Instulation ID |
| INT | ONIM |
| BYTE | 6 |
| SHORT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |

## Variable Descriptions
- Obj_OperandCount =

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
52 9F 65 46 00 00 00 00  // Instulation ID
4F 4E 49 4D 06           // ONIM 6
02 00 
42 00 00 00 
00 00 00 00 
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete