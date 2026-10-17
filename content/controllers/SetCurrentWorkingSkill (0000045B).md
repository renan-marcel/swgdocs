---
title: SetCurrentWorkingSkill (0000045B)
url: https://wiki.swganh.org/index.php/SetCurrentWorkingSkill_%280000045B%29
page_type: Object Controller
opcode: 0000045B
revision_id: 257249
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Ascii', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# SetCurrentWorkingSkill (0000045B)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | String spacer |
| ASCII | Skill |

## Variable Descriptions
- controllerID	     = 0000045B

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 #Operand
46 5E CE 80 #Obj COn
2B 01 00 00 #Unknown INT
5B 04 00 00 #Enum: setCurrentWorkingSkill
92 7C A1 B3 1A 00 00 00 #CharacterID
00 00 00 00 #String Spacer
14 00 #String Size 
73 6F 63 69 61 6C 5F 64 61 6E 63 65 72 5F 6D 61 73 74 65 72 #social_dancer_master (the skill that is set)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete