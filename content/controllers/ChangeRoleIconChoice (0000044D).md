---
title: ChangeRoleIconChoice (0000044D)
url: https://wiki.swganh.org/index.php/ChangeRoleIconChoice_%280000044D%29
page_type: Object Controller
opcode: 0000044D
revision_id: 257211
last_modified: 2014-01-05T08:51:00Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# ChangeRoleIconChoice (0000044D)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown INT |
| INT | newRoleIconChoice |
| BYTE | Sequence ID |

## Variable Descriptions
- controllerID	     = 0000044D

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble

05 00 #operand
46 5E CE 80 #Obj Con
83 00 00 00 #Unknown INT

4D 04 00 00 #enum: changeRoleIconChoice
C7 E4 76 CD 10 00 00 00 #CharacterID
00 00 00 00 #Unknown INT
14 00 00 00 #newRoleIconChoice
00 #sequenceId
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete