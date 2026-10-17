---
title: MissionAbort (00000142)
url: https://wiki.swganh.org/index.php/MissionAbort_%2800000142%29
page_type: Object Controller
opcode: 00000142
revision_id: 257234
last_modified: 2014-01-07T20:44:41Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# MissionAbort (00000142)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown Int |
| LONG | Mission Object ID |

## Variable Descriptions
- controllerID	     = 00000142

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE Struct by cAble

05 00 #Opernad
46 5E CE 80 #Obj con
0B 00 00 00 #Unknonw INT
42 01 00 00 #mission abort
DB E1 72 BF 07 00 00 00 # CharacterID
00 00 00 00 #Spacer 
60 F8 39 67 23 00 00 00 # Mission Object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete