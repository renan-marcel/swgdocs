---
title: UiPlayEffect (00000401)
url: https://wiki.swganh.org/index.php/UiPlayEffect_%2800000401%29
page_type: Object Controller
opcode: 00000401
revision_id: 257250
last_modified: 2014-01-10T23:00:45Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Ascii', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# UiPlayEffect (00000401)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Character ID |
| INT | Unknown INT |
| LONG | Character ID |
| ASCII | UI String |

## Variable Descriptions
- controllerID	     = 00000401

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
CU research and object controller struct by cAble


sample1


05 00 #operand
46 5E CE 80 #obj con
0B 00 00 00 #unknown int
01 04 00 00 #Enum: UiPlayEffect

70 F6 46 DF 07 00 00 00 #char id
00 00 00 00 #Unknown Int
70 F6 46 DF 07 00 00 00 ##char id

17 00 #StringSize
73 68 6F 77 4D 65 64 69 61 74 6F 72 3D 77 73 5F 72 6F 61 64 6D 61 70 #showMediator=ws_roadmap


sample2

05 00 
46 5E CE 80 
0B 00 00 00 
01 04 00 00 
70 F6 46 DF 07 00 00 00 
00 00 00 00 
70 F6 46 DF 07 00 00 00 

28 00 
73 68 6F 77 4D 65 64 69 61 74 6F 72 3D 77 73 5F 70 72 6F 66 
65 73 73 69 6F 6E 74 65 6D 70 6C 61 74 65 
73 65 6C 65 63 74 #showMediator=ws_professiontemplateselect
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete