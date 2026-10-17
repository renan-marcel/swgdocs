---
title: SetProfessionTemplate (0000045C)
url: https://wiki.swganh.org/index.php/SetProfessionTemplate_%280000045C%29
page_type: Object Controller
opcode: 0000045C
revision_id: 257238
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Ascii', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# SetProfessionTemplate (0000045C)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Spacer |
| ASCII | Text Output |

## Variable Descriptions
- controllerID	     = 0000045C

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
CU struct by cAble


05 00 #Operand
46 5E CE 80 #Obj Con	
2B 00 00 00 #Unknown INT
5C 04 00 00 #enum: setProfessionTemplate
71 F6 46 DF 07 00 00 00 #Character ID
00 00 00 00 #Spacer
09 00 #Ascii
74 72 61 64 65 72 5F 31 64 #Text output = trader_1d
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete