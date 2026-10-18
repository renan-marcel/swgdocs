---
title: SetupSharedNetworkMessages (0000022B)
url: https://wiki.swganh.org/index.php/SetupSharedNetworkMessages_%280000022B%29
page_type: Object Controller
opcode: 0000022B
revision_id: 256937
last_modified: 2013-09-11T20:05:45Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# SetupSharedNetworkMessages (0000022B)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | ObjControllerMessage |
| INT | ObjType |
| INT | ControllerName |
| LONG | CharacterID |
| INT | Unknown INT |

## Variable Descriptions
- controllerID	     = 0000022B

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble@projectswg

05 00 # Operand
46 5E CE 80 #ObjControllerMessage
1B 00 00 00 #ObjType
2B 02 00 00 #objectMenuDirty
89 42 D5 2B 33 00 00 00 #CharacterID
00 00 00 00 #Unknown INT
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete