---
title: SpatialChatInternal (00000161)
url: https://wiki.swganh.org/index.php/SpatialChatInternal_%2800000161%29
page_type: Object Controller
opcode: 00000161
revision_id: 79215
last_modified: 
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:U string', 'Template:ClientPacket', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# SpatialChatInternal (00000161)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | unknown |
| INT | CRC = 'spatialchatinternal' |
| INT | unknown |
| INT | unknown |
| INT | UniCode String Size |
| U_STRING | Text |

## Variable Descriptions
- controllerID	     = 00000116

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00                    // OpperandCount
46 5e ce 80              // ObjController
23 00 00 00              // sub-op
16 01 00 00              // Command OP
19 00 00 00 00 00 00 00  // Character ID
00 00 00 00 
00 00 00 00 
d4 63 8d 7c   // spatialchatinternal
00 00 00 00 
00 00 00 00  
04 00 00 00 // u-string count
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | ControllerIDs | Server Packets | 75% Complete