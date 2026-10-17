---
title: CREO01
url: https://wiki.swganh.org/index.php/CREO01
page_type: Baseline
opcode: 
revision_id: 65979
last_modified: 2010-01-06T16:46:06Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:CREOArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:A string', 'Template:100%']
---

# CREO01

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Baseline Opcode |
| LONG | Container ID |
| INT | OERC |
| BYTE | 1 |
| SHORT | ?? |
| INT | Bank Credits |
| INT | Cash Credits |
| INT | Base HAM Mod List Size |
| INT | Update Counter |
| INT | Base HAM Mod Value |
| INT | Skills List Size |
| INT | Update Counter |
| A_STRING | Skill Name |

## Variable Descriptions
- Obj_OperandCount = 4

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
53 21 86 12 // DeltasMessage
D2 CD 31 6E 0C 00 00 00 // character id
4F 45 52 43 01 // OERC 1
0E 00 00 00 
02 00 
01 00 00 00 
00 00 00 00 
82 86 0F 00 // 1017474 credits
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete