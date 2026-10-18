---
title: CraftingSessionEnded (000001C2)
url: https://wiki.swganh.org/index.php/CraftingSessionEnded_%28000001C2%29
page_type: Object Controller
opcode: 000001C2
revision_id: 257026
last_modified: 2013-09-17T20:41:34Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# CraftingSessionEnded (000001C2)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Player ID |
| INT | unknown |
| BYTE | count |

## Variable Descriptions
- controllerID	     = 000001C2

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble

05 00 #Opcode
46 5E CE 80 #ObjCont
0B 00 00 00 
C2 01 00 00 #CraftingSessionEnded
00 2E E9 E9 31 00 00 00 #CharactedID
00 00 00 00 #UnknownINT
01 #Count
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete