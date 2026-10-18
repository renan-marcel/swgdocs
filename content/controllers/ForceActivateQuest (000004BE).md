---
title: ForceActivateQuest (000004BE)
url: https://wiki.swganh.org/index.php/ForceActivateQuest_%28000004BE%29
page_type: Object Controller
opcode: 000004BE
revision_id: 257090
last_modified: 2013-09-27T20:24:34Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# ForceActivateQuest (000004BE)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown Int |
| INT | Waypoint data |

## Variable Descriptions
- controllerID	     = 000004BE

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble

05 00 #Operand
46 5E CE 80 #Obj Controller
0B 00 00 00 
BE 04 00 00 #forceActivateQuest 
4E C7 80 B7 51 00 00 00 #Character ID
00 00 00 00 #unknown INT 
1D F0 D9 0C #Unknown INT  (seems to relate to an INT assigned to the '''QuestWP''' in logs)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete