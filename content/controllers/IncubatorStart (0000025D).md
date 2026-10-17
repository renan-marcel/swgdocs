---
title: IncubatorStart (0000025D)
url: https://wiki.swganh.org/index.php/IncubatorStart_%280000025D%29
page_type: Object Controller
opcode: 0000025D
revision_id: 257136
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# IncubatorStart (0000025D)

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
- controllerID	     = 0000025D

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE Object controller by cAble (packet researcher) 

05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 #Unknown
5D 02 00 00 #Enum:IncubatorStart
27 EA 90 8B 32 00 00 00 #Character Id

00 00 00 00 

03 00 00 00 #Int: Session Number (this was from a 3rd stage mutation packet!)
(note: Sessions will follow a normal numeric pattern. Session 1 will be 01 00 00 00) etc. 


27 EA 90 8B 32 00 00 00 #Character Id
B9 47 6D 12 3A 00 00 00 #Terminal Id

Below are all INTS

52 03 00 00 #powerGauge
01 00 00 00 #initialPointsSurvival
01 00 00 00 #initialPointsBeastialResilience
02 00 00 00 #initialPointsCunning
02 00 00 00 #initialPointsIntelligence
04 00 00 00 #initialPointsAggression
02 00 00 00 #initialPointsHuntersInstinct
05 00 00 00 #TemperatureGauge
05 00 00 00 #nutrientGauge
33 00 00 00 #initialCreatureColorIndex

29 00 #StringSize
6F 62 6A 65 63 74 2F 6D 6F 62 69 6C 65 2F 62 65 
61 73 74 5F 6D 61 73 74 65 72 2F 62 6D 5F 67 75 
72 72 65 63 6B 2E 69 66 66 #object/mobile/beast_master/bm_gurreck.iff
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete