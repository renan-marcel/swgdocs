---
title: DraftSlots (00000103)
url: https://wiki.swganh.org/index.php/DraftSlots_%2800000103%29
page_type: Object Controller
opcode: 00000103
revision_id: 257039
last_modified: 2013-09-19T19:21:21Z
completion: 75%
direction: S→C
sample_status: absent
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Byte', 'Template:Beginlist', 'Template:A string', 'Template:U string', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:ServerPacket', 'Template:75%']
---

# DraftSlots (00000103)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | PlayerID |
| INT | Slots |
| LONG | crafttoolID |
| LONG | SchematicID |
| LONG | ItemID |
| INT | datapadsize of the schem |
| BYTE | ?? limited use flag or loot flag?? 0 or 1 |
| INT | slots count |

## Variable Descriptions
- controllerID	     = 00000103

## Notes
- **NOTE:** The byte after the u_string will be replaced by uint8(2),uint16(1),uint32,uint32, if the slot represents a subcomponent.

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete