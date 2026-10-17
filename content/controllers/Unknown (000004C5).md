---
title: Unknown (000004C5)
url: https://wiki.swganh.org/index.php/Unknown_%28000004C5%29
page_type: Object Controller
opcode: 000004C5
revision_id: 20651
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# Unknown (000004C5)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Object ID |
| INT | ?? |
| LONG | ?? |

## Variable Descriptions
- controllerID	     = 000004C5

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
46 5E CE 80 
83 00 00 00 
C5 04 00 00 
00 26 69 B3 23 00 00 00 
00 00 00 00 
1A 04 F0 FE 24 00 00 00
----
05 00 
46 5E CE 80 // ObjControllerMessage 
83 00 00 00 
C5 04 00 00 //unknown Command ID 0.o 
4D FB F3 A5 0D 00 00 00 00 // Character ID 
00 00 00 00 
00 00 00 00 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 50% Complete