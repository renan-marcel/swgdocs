---
title: DataTransformWithParent (000000F1)
url: https://wiki.swganh.org/index.php/DataTransformWithParent_%28000000F1%29
page_type: Object Controller
opcode: 000000F1
revision_id: 20927
last_modified: 2008-01-06T23:06:01Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Long', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# DataTransformWithParent (000000F1)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | Counter |
| LONG | CellID |
| INT | OrientationX |
| INT | OrientationY |
| INT | OrientationZ |
| INT | OrientationW |
| INT | PositionX |
| INT | PositionZ |
| INT | PositionY |
| INT | Speed |

## Variable Descriptions
- controllerID	     = 000000F1

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
46 5E CE 80 // ObjControllerMessage
0B 00 00 00 
F1 00 00 00 // DataTransformWithParent
71 E2 DB D9 00 00 00 00 // Character ID
00 00 00 00 
00 00 00 00 <-NGE version has 2 ints before the counter 
70 00 00 00 // counter
E3 93 86 5B 19 00 00 00 // cell ID
00 00 00 00 // 0x = 0
C1 5F C1 BE // 0y = -0.38
00 00 00 00 // 0z = 0
0E 0A 6D 3F // 0w = 0.93
FD FF B7 BD // x  = -0.09
93 EC CF C1 // y  = -25.99
00 C0 89 BE // z  = -0.27
00 00 00 00 // speed
00 00 00 00 <-unk NGE version
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete