---
title: IncubatorCancel (0000025E)
url: https://wiki.swganh.org/index.php/IncubatorCancel_%280000025E%29
page_type: Object Controller
opcode: 0000025F
revision_id: 257139
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# IncubatorCancel (0000025E)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | ObjController |
| INT | Unknown |
| INT | Enum |

## Variable Descriptions
- controllerID	     = 0000025F

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE Object controller by cAble (packet researcher) 



05 00 #Operand

46 5E CE 80 #Obj Controller

23 00 00 00 #Unknown INT

5F 02 00 00 #Enum

F0 B4 E1 74 32 00 00 00 #Character ID

00 00 00 00 #spacer

00 ## Bool (0 cancel?) 

30 04 F3 B6 3F 00 00 00 #Incubator Object ID

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete