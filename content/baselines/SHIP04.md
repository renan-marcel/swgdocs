---
title: SHIP04
url: https://wiki.swganh.org/index.php/SHIP04
page_type: Baseline
opcode: 
revision_id: 26825
last_modified: 2008-04-14T10:59:52Z
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:SHIPArchitectureNAV', 'Template:50%']
---

# SHIP04

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| FLOAT | Mass |
| FLOAT | Weapon Charge |
| FLOAT | ?? |
| INT | ?? |
| INT | List size |
| INT | Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |

## Variable Descriptions
- Obj_OperandCount = 6
- Mass = Total Mass of ship

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68 
04 5A D1 D6 13 00 00 00 
50 49 48 53 04 // PIHS 4
22 00 00 00 
06 00 
00 00 00 00 
CD CC 4C 3F 
00 00 
00 44 
00 00 
C8 42 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete