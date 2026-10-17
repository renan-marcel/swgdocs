---
title: AskGroupMemberToLaunchIntoSpace (00000438)
url: https://wiki.swganh.org/index.php/AskGroupMemberToLaunchIntoSpace_%2800000438%29
page_type: Object Controller
opcode: 00000438
revision_id: 257187
last_modified: 2014-01-03T00:03:12Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# AskGroupMemberToLaunchIntoSpace (00000438)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | CharacterID |
| INT | Spacer |
| LONG | CharcterID Invited |

## Variable Descriptions
- controllerID	     = 00000438

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble (NGE packet Reverser)

05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 #Unknown INT
38 04 00 00 #Enum: askGroupMemberToLaunchIntoSpace
A1 56 89 27 00 00 00 00 #Character ID 
00 00 00 00 #Spacer
AC 3B 65 D2 00 00 00 00 #Id of character being invited.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete