---
title: ShowLootBox (000004BC)
url: https://wiki.swganh.org/index.php/ShowLootBox_%28000004BC%29
page_type: Object Controller
opcode: 000004BC
revision_id: 257228
last_modified: 2014-01-07T04:40:59Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# ShowLootBox (000004BC)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown Int |
| INT | Number of Looted Items |
| LONG | Object ID for Looted Item |

## Variable Descriptions
- controllerID	     = 000004BC

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble@projectswg

05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 #Controller Type
BC 04 00 00 #Controller Id 
EC 98 D7 D0 4B 00 00 00 #CharacterID

00 00 00 00 #Unknown INT
01 00 00 00 #Number of Items Looted
B9 4E 54 F6 51 00 00 00 #ObjectID for Item Looted.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete