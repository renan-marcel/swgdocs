---
title: ShowCombatText (0000045A)
url: https://wiki.swganh.org/index.php/ShowCombatText_%280000045A%29
page_type: Object Controller
opcode: 0000045A
revision_id: 257227
last_modified: 2014-01-06T23:39:17Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Ascii', 'Template:Short', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# ShowCombatText (0000045A)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Spacer |
| LONG | Defender ID |
| LONG | Attacker ID |
| ASCII | Output text |
| INT | Spacer |
| ASCII | Output text |
| INT | Scale |
| INT | Text color |
| SHORT | flag |

## Variable Descriptions
- controllerID	     = 0000045A

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 #Operand
46 5E CE 80 #Obj COn
0B 00 00 00 #Unknown INT
5A 04 00 00 #enum: showCombatText 

1D 03 1E E3 1A 00 00 00 #Character ID

00 00 00 00 #Spacer

ED D7 88 80 1E 00 00 00 #Defender ID 
1D 03 1E E3 1A 00 00 00 #Attacker ID

0E 00 #StringSize
63 6F 6D 62 61 74 5F 65 66 66 65 63 74 73 = combat_effects

00 00 00 00 #StringSpacer

04 00 #StringSize
6D 69 73 73 = miss
00 00 00 00 

00 00 C0 3F #scale
FF FF FF #white = string colour
01 #flag
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete