---
title: HyperspaceOrientShipToPointAndLockPlayerInput (0000042D)
url: https://wiki.swganh.org/index.php/HyperspaceOrientShipToPointAndLockPlayerInput_%280000042D%29
page_type: Object Controller
opcode: 0000042D
revision_id: 257207
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Unknown', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# HyperspaceOrientShipToPointAndLockPlayerInput (0000042D)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | ?? |

## Variable Descriptions
- controllerID	     = 0000042D

## Notes
- **NOTE:** The struct is from NGE, but likely to the same as precu

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 #Operand
46 5E CE 80 #Obj Con
0B 00 00 00 #Unknown iNT
2D 04 00 00 #Enum: hyperspaceOrientShipToPointAndLockPlayerInput
56 F2 01 94 16 00 00 00 #Ship Object ID
00 00 00 00 #Spacer 


0F 00 #String size
73 70 61 63 65 5F 64 61 6E 74 6F 6F 69 6E 65 #Location: = space_dantooine

00 58 C8 C5 #x
00 20 D3 45 #y
00 D0 C8 45 #z
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete