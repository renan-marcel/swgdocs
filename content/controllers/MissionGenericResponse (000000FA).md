---
title: MissionGenericResponse (000000FA)
url: https://wiki.swganh.org/index.php/MissionGenericResponse_%28000000FA%29
page_type: Object Controller
opcode: 000000FA
revision_id: 20740
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:Long', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# MissionGenericResponse (000000FA)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | 05 |
| INT | Object Controller |
| INT | ?? |
| INT | MissionGenericResponse |
| LONG | Char ID |
| INT | ?? |
| LONG | Mission ID |
| BYTE | ?? |
| BYTE | ?? |

## Variable Descriptions
- controllerID	     = 000000FA

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
46 5E CE 80             // ObjControllerMessage 
0B 00 00 00 
FA 00 00 00             // MissionGenericResponse 
4D FB F3 A5 0D 00 00 00 // Character ID 
00 00 00 00 
43 8E 78 FD 23 00 00 00 // Mission ID 
01 
04
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 50% Complete