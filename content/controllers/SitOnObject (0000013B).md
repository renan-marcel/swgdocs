---
title: SitOnObject (0000013B)
url: https://wiki.swganh.org/index.php/SitOnObject_%280000013B%29
page_type: Object Controller
opcode: 0000013B
revision_id: 21788
last_modified: 2008-01-13T08:10:22Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Float', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# SitOnObject (0000013B)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Cell ID |
| FLOAT | coord X |
| FLOAT | Coord Z |
| FLOAT | Coord Y |

## Variable Descriptions
- controllerID	     = 0000013B

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
ObjectController 13Bh (S->C) SitOnObject
   //Packet Break for SitOnObject Controller
   ObjectControllerHeader (1Bh,13Bh)
   E0 BE 2F 2A 09 00 00 00  //CellID
   1F A2 AF 40 //5.48854
   DC 84 6B BE //-0.229999
   8E 58 A6 C0 //-5.19831
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete