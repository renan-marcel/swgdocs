---
title: AboutToHyperspace (000003FE)
url: https://wiki.swganh.org/index.php/AboutToHyperspace_%28000003FE%29
page_type: Object Controller
opcode: 000003FE
revision_id: 257222
last_modified: 2014-01-06T00:45:46Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Ascii', 'Template:Float', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# AboutToHyperspace (000003FE)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | ObjConMessage |
| INT | Unknown Int |
| INT | enum message name |
| LONG | Object ID ship |
| INT | spacer |
| ASCII | String |
| FLOAT | Waypoint x |
| FLOAT | Waypoint y |
| FLOAT | Waypoint z |

## Variable Descriptions
- controllerID	     = 000003FE

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct 

05 00 #Operand
46 5E CE 80 #obj con
0B 00 00 00 #unknown INT
FE 03 00 00 #Enum: aboutToHyperspace
56 F2 01 94 16 00 00 00 #ObjectID for Ship
00 00 00 00 #Spacer

0F 00 #StringSize 
73 70 61 63 65 5F 64 61 6E 74 6F 6F 69 6E 65 #Location: = space_dantooine

00 EC CB C5 #x
4A 2C CE 45 #Y 
96 7E C7 45 #z
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete