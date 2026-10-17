---
title: ShowFlyText (000001BD)
url: https://wiki.swganh.org/index.php/ShowFlyText_%28000001BD%29
page_type: Object Controller
opcode: 000001BD
revision_id: 21422
last_modified: 2008-01-09T01:35:00Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Short', 'Template:A string', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# ShowFlyText (000001BD)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | ObjectID |
| SHORT | STFLoc Size |
| A_STRING | STC Location |
| INT | Padding |
| A_STRING | Text |
| INT | Padding |
| BYTE | Red |
| BYTE | Green |
| BYTE | Blue |
| BYTE | Display Flag |

## Variable Descriptions
- controllerID	     = 000001BD

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00			'Opperand Count 
46 5E CE 80 		'ObjController
1B 00 00 00 		'Sub-op
BD 01 00 00 		'Command Op
19 00 00 00 00 00 00 00 'Character ID
00 00 00 00 		'Spacing
19 00 00 00 00 00 00 00 'Target ID
0E 00 			'String Size
63 6F 6D 62 61 74 5F 65 66 66 65 63 74 73 'combat_effects
00 00 00 00 		'Spacing
08 00 			'String Size
68 69 74 5F 6C 6C 65 67 'hit_lleg
00 00 00 00 		'spacing
00 FF 00 		'RGB
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete