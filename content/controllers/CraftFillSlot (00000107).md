---
title: CraftFillSlot (00000107)
url: https://wiki.swganh.org/index.php/CraftFillSlot_%2800000107%29
page_type: Object Controller
opcode: 00000107
revision_id: 257019
last_modified: 2013-09-17T16:00:13Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:ClientPacket', 'Template:100%']
---

# CraftFillSlot (00000107)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Resource or Container ID |
| INT | Slot ID |
| INT | Option |
| BYTE | Sequence ID |

## Variable Descriptions
- controllerID	     = 00000107

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE break by cAble 

05 00 #Operand
46 5E CE 80 #ObjCon
83 00 00 00 
07 01 00 00 #CraftFillSlot
00 2E E9 E9 31 00 00 00 
00 00 00 00 #unknown
16 A5 C8 50 32 00 00 00 #ObjectID for Ingredient
01 00 00 00 #Slot01
00 00 00 00 #Option
85 #sequence



05 00 #Operand
46 5E CE 80 #ObjCon
83 00 00 00 
07 01 00 00 #CraftFillSlot
00 2E E9 E9 31 00 00 00 #CharacterID
00 00 00 00 #Unknown
9D 3F EB F9 3A 00 00 00 #ObjectID for Ingredient
02 00 00 00 #Slot02
00 00 00 00 #Option
86 #Sequence
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Client Packets | 100% Complete