---
title: IncubatorCommit (0000025E)
url: https://wiki.swganh.org/index.php/IncubatorCommit_%280000025E%29
page_type: Object Controller
opcode: 0000025E
revision_id: 257131
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# IncubatorCommit (0000025E)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | ObjController |
| INT | Unknown |
| INT | Enum |

## Variable Descriptions
- controllerID	     = 0000025E

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE Object controller by cAble (packet researcher) 



05 00 #UpdateType
46 5E CE 80 #Opcode
23 00 00 00 
5E 02 00 00 #Enum: incubatorCommit


27 EA 90 8B 32 00 00 00 #CharacterID


00 00 00 00 

01 #Bool: Incubation Comitted? 

B9 47 6D 12 3A 00 00 00 #Terminal Id
D9 DD 7E 51 3D 00 00 00 #Slot1 Id
E6 91 15 A5 39 00 00 00 #Slot2 Id
D5 38 F5 B5 3C 00 00 00 #Slot3 Id
63 B5 F8 10 41 00 00 00 #Slot4 Id


Below are all INTS.


01 00 00 00 #InitialPointsSurvival
01 00 00 00 #InitialPointsBeastialResilience
02 00 00 00 #InitialPointsCunning
02 00 00 00 #InitialPointsIntelligence
04 00 00 00 #InitialPointsAggression
02 00 00 00 #InitialPointsHuntersInstinct
01 00 00 00 #TotalPointsSurvival
01 00 00 00 #TotalPointsVeastialResilience
03 00 00 00 #TotalPointsCunning
03 00 00 00 #TotalPointsIntelligence
06 00 00 00 #TotalPointsAggression
04 00 00 00 #TotalPointsHuntersInstinct
0A 00 00 00 #TemperatureGauge
02 00 00 00 #NutrientGauge
33 00 00 00 #newCreatureColorIndex
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete