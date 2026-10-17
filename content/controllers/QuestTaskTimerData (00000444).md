---
title: QuestTaskTimerData (00000444)
url: https://wiki.swganh.org/index.php/QuestTaskTimerData_%2800000444%29
page_type: Object Controller
opcode: 00000444
revision_id: 257107
last_modified: 2013-09-28T00:24:27Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:A string', 'Template:Int', 'Template:U string', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# QuestTaskTimerData (00000444)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Object ID |
| A_STRING | QuestName |
| INT | Task ID |
| U_STRING | SourceName |
| INT | timerlength |

## Variable Descriptions
- controllerID	     = 00000444

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
44 04 00 00 #questTaskTimerData
4E C7 80 B7 51 00 00 00 #Object ID
00 00 00 00 #UnknownInt
17 00 #StringSize
71 75 65 73 74 2F 73 6D 75 67 67 6C 65 5F 67 65 
6E 65 72 69 63 5F 31 #questName (quest/smuggle_generic_1) 
04 00 00 00 #taskId 
22 00 00 00 #UString
71 00 75 00 65 00 73 00 74 00 2F 00 67 00 72 00 
6F 00 75 00 6E 00 64 00 71 00 75 00 65 00 73 00 
74 00 73 00 3A 00 74 00 69 00 6D 00 65 00 72 00 
5F 00 74 00 69 00 6D 00 65 00 72 00 74 00 65 00 
78 00 74 00 #sourceName = quest/groundquests:timer_timertext
38 D7 73 00 #timerLength
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete