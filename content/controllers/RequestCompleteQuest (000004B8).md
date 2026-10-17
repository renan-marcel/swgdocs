---
title: RequestCompleteQuest (000004B8)
url: https://wiki.swganh.org/index.php/RequestCompleteQuest_%28000004B8%29
page_type: Object Controller
opcode: 000004B8
revision_id: 257118
last_modified: 2013-09-28T20:57:38Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# RequestCompleteQuest (000004B8)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown INT |
| INT | Quest ID |

## Variable Descriptions
- controllerID	     = 000004B8

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
B8 04 00 00 # requestCompleteQuest
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