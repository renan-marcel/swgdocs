---
title: MissionGenericRequest (000000F9)
url: https://wiki.swganh.org/index.php/MissionGenericRequest_%28000000F9%29
page_type: Object Controller
opcode: 000000F9
revision_id: 20738
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:Long', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# MissionGenericRequest (000000F9)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | 05 |
| INT | Object Controller |
| INT | ?? |
| INT | MissionGenericRequest |
| LONG | Char ID |
| INT | ?? |
| LONG | Mission ID |
| LONG | Mission Term ID |
| BYTE | ?? |

## Variable Descriptions
- controllerID	     = 000000F9

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
46 5E CE 80 // ObjControllerMessage 
83 00 00 00 
F9 00 00 00 // MissionGenericRequest 
4D FB F3 A5 0D 00 00 00 // Character ID 
00 00 00 00 
43 8E 78 FD 23 00 00 00 // Mission ID 
BF F1 2C 00 00 00 00 00 // Prob. Terminal ID 
04
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 50% Complete