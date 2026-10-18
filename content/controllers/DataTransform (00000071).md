---
title: DataTransform (00000071)
url: https://wiki.swganh.org/index.php/DataTransform_%2800000071%29
page_type: Object Controller
opcode: 00000071
revision_id: 79412
last_modified: 2012-09-11T07:55:53Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Int', 'Template:Float', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# DataTransform (00000071)

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| INT | Counter |
| FLOAT | OrientationX |
| FLOAT | OrientationY |
| FLOAT | OrientationZ |
| FLOAT | OrientationW |
| FLOAT | PositionX |
| FLOAT | PositionY |
| FLOAT | PositionZ |
| FLOAT | Speed |

## Variable Descriptions
- controllerID         = 00000071 Flags		     = 0B,21,23,53

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
DataTransform NGE packet

05 00 #operand
46 5E CE 80 #obj controller message
21 00 00 00 #flag
71 00 00 00 #controller ID
AD A4 51 D2 4B 00 00 00 #Object ID

00 00 00 00 
C0 E8 B9 43 
01 00 00 00 

00 00 00 00 #Orientation-X
BB 69 6E 3F #Orientation-Y
00 00 00 00 #Orientation-Z
1D 7F BA 3E #Orientation-W


14 A4 98 C5 #Position-X
00 00 C0 40 #Position-Y
04 D2 81 45 #Position-Z

9A 99 E9 40 #Speed   


00 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | ControllerIDs | 100% Complete