---
title: TANO06
url: https://wiki.swganh.org/index.php/TANO06
page_type: Baseline
opcode: 
revision_id: 79224
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', '100% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:TANOArchitectureNAV', 'Template:100%', 'Template:ServerPacket']
---

# TANO06

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| INT | ServerID |
| INT | DefenderList |
| INT | UpdateCounter |
| LONG | DefenderID |

## Variable Descriptions
- ObjOpperandCount = 2

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
1D 92 14 6D 02 00 00 00 // ID
4F 4E 41 54 06          // ONAT 6
02 00 42 00 
00 00 00 00
00 00 00 00 
00 00 0E
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete | Server Packets