---
title: PlayerEmote (0000012E)
url: https://wiki.swganh.org/index.php/PlayerEmote_%280000012E%29
page_type: Object Controller
opcode: 0000012E
revision_id: 256973
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Short', 'Template:Byte', 'Template:Unknown', 'Template:ObjControllerMessageTag', 'Template:75%', 'Template:Int']
---

# PlayerEmote (0000012E)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Source ID |
| LONG | Receiver ID |
| SHORT | emote ID |
| BYTE | ?? |
| SHORT | ?? |

## Variable Descriptions
- controllerID	     = 0000012E

## Notes
- **NOTE:** The first ID in the OBJ needs to be the ID of the object receiving the packet (recipID).

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 #
2E 01 00 00 #ControllerType: SocialEmoteReceive
CA 16 09 91 45 00 00 00 #CharacterID
00 00 00 00 #Unknown INT
CA 16 09 91 45 00 00 00 #SenderID
CA 16 09 91 45 00 00 00 #ReceiverID
6F 01 00 00 #EmoteType
03 #Flag
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete