---
title: StartNpcConversation (000000DD)
url: https://wiki.swganh.org/index.php/StartNpcConversation_%28000000DD%29
page_type: Object Controller
opcode: 000000DD
revision_id: 21230
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# StartNpcConversation (000000DD)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Converser ID |
| INT | unknown |
| BYTE | unknown |
| BYTE | unknown |
| BYTE | unknown |

## Variable Descriptions
- controllerID	     = 000000DD

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
(uint16)5;		   //05 00
	(Obj_controller_opcode);   //46 5e ce 80
	(uint32)                   //0b 00 00 00
	(uint32)0x000000dd;	   //dd 00 00 00
	(uint64)_player->ObjID;	   //19 00 00 00 00 00 00 00
	(uint32)0;		   //00 00 00 00
	(uint64)_NPCID->Target;    //04 1e 06 00 00 00 00 00
	(uint32)0;		   //00 00 00 00
	(uint8)0 << (uint16)0;	   //00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete