---
title: TeleportAck (0000013F)
url: https://wiki.swganh.org/index.php/TeleportAck_%280000013F%29
page_type: Object Controller
opcode: 0000013F
revision_id: 257080
last_modified: 2013-09-27T19:43:16Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# TeleportAck (0000013F)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Object ID |
| INT | Unknown |
| INT | Sequence Id |

## Variable Descriptions
- controllerID	     = 0000013F

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
'''NGE struct by cAble'''

A teleportACK message is sent from a client to a game server to "acknowledge" receipt of a teleport message.


05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
3F 01 00 00 #Teleport ACK
F0 B4 E1 74 32 00 00 00 #ObjectID
00 00 00 00 # unknown
FE FF FF FF # SequenceID (INT)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete