---
title: CommandQueueAdd (00000167)
url: https://wiki.swganh.org/index.php/CommandQueueAdd_%2800000167%29
page_type: Object Controller
opcode: 00000167
revision_id: 257241
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# CommandQueueAdd (00000167)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown Int |
| INT | Unknown Int |
| INT | Attack Crc |

## Variable Descriptions
- controllerID	     = 00000167

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
CU struct by cAble

05 00 #Operand
46 5E CE 80 #Obj Con
0B 00 00 00 #Unknown INT
67 01 00 00 #enum: commandQueueAdd  
37 C8 59 45 04 00 00 00 #Character ID
00 00 00 00 #Unknown INT
01 00 00 40 #Unknown INT
FA C0 60 3E # CRC for saberhit
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete