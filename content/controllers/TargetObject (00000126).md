---
title: TargetObject (00000126)
url: https://wiki.swganh.org/index.php/TargetObject_%2800000126%29
page_type: Object Controller
opcode: 00000126
revision_id: 79425
last_modified: 2013-03-03T05:42:21Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete', 'Client Packets']
templates: ['Template:PageHeader', 'Template:Long', 'Template:ObjControllerMessageTag', 'Template:100%', 'Template:ClientPacket']
---

# TargetObject (00000126)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | ObjectID |

## Variable Descriptions
- controllerID	     = 00000126

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.
- **C→S** - This packet originates on the client.

## Sample Packet
```
05 00
46 5E CE 80 
83 00 00 00 
26 01 00 00 
AA ED AC 2F 17 00 00 00 // character ID
00 00 00 00 
49 C8 B5 2D 17 00 00 00 // Object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete | Client Packets