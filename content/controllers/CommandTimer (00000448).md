---
title: CommandTimer (00000448)
url: https://wiki.swganh.org/index.php/CommandTimer_%2800000448%29
page_type: Object Controller
opcode: 00000448
revision_id: 256909
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Byte', 'Template:Int', 'Template:Float', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# CommandTimer (00000448)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| BYTE | Unknown byte |
| INT | Unknown Int |
| INT | Unknown Int |
| INT | Sequence Id |
| INT | CommandNameCrc |
| INT | CoolDownGroup |
| FLOAT | CoolDownMin |
| FLOAT | CoolDownMax |

## Variable Descriptions
- controllerID	     = 00000448

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble and Apathy

05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 
48 04 00 00 #CommandTimer
ER 98 D7 D0 4B 00 00 00 #CharacterID
00 00 00 00 #tickCount,
04 #UnknownByte
20 00 00 40 #Unknown Int
00 00 00 00 #Unknown Int
00 00 00 00 #SequenceID 
33 BA C2 F3 #me_fld_dm_dot_3 (commandNameCrc: TraugerGasCanister)
F1 9D 04 25 #CooldownGroup
00 00 00 00 #CoolDownMin
00 00 80 41 #CoolDownMAx
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete