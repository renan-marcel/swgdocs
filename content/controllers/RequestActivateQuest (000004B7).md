---
title: RequestActivateQuest (000004B7)
url: https://wiki.swganh.org/index.php/RequestActivateQuest_%28000004B7%29
page_type: Object Controller
opcode: 000004B7
revision_id: 257116
last_modified: 2013-09-28T20:51:54Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# RequestActivateQuest (000004B7)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown INT |
| INT | Quest ID |

## Variable Descriptions
- controllerID	     = 000004B7

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble

05 00 # Operand
46 5E CE 80 # Obj Controller
0B 00 00 00 
B7 04 00 00 # requestActivateQuest
CA 16 09 91 45 00 00 00 # CharacterID
00 00 00 00 # Unknown INT
F1 59 C9 C7 # quest ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete