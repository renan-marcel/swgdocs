---
title: ObjcontrollerPacketTemplate
url: https://wiki.swganh.org/index.php/ObjcontrollerPacketTemplate
page_type: Other
opcode: FFFFFFFF
revision_id: 2067
last_modified: 
completion: 0%
direction: C→S
sample_status: absent
categories: ['Notice', 'Packets', 'Server Packets', 'Client Packets', 'ControllerIDs', '100% Complete', '75% Complete', '50% Complete', '25% Complete', '0% Complete']
templates: ['Template:PacketGuide', 'Template:ServerPacket', 'Template:ClientPacket', 'Template:ObjControllerMessageTag', 'Template:100%', 'Template:75%', 'Template:50%', 'Template:25%', 'Template:0%']
---

# ObjcontrollerPacketTemplate

## Notices
_none_

## Description
_none_

## Struct
| Type | Name |
| --- | --- |
| BYTE | uint8 |
| SHORT | uint16 |
| INT | uint32 |
| FLOAT | uint32 |
| LONG | uint64 |
| A_STRING | ASCII String |
| U_STRING | Unicode String |
| C_STRING | Customization String |
| B_STRING | Byte String |
| { } | LIST Component |
| ? | Uncertain Values |
| ?? | Unknown Variable Name |

## Variable Descriptions
- controllerID	     = FFFFFFFF

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **C→S** - This packet originates on the client.
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.
- **75%** - This packet has been partially reversed.
- **50%** - This packet has been partially reversed.
- **25%** - This packet has been partially reversed.
- **0%** - This packet has not been reversed.

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
Notice | Packets | Server Packets | Client Packets | ControllerIDs | 100% Complete | 75% Complete | 50% Complete | 25% Complete | 0% Complete