---
title: SceneDestroyObject
url: https://wiki.swganh.org/index.php/SceneDestroyObject
page_type: Server Packet
opcode: 4D45D504
revision_id: 66702
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# SceneDestroyObject

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| LONG | Object ID |

## Variable Descriptions
- Opperand_Count	     = X
- Opcode		     = 4D45D504

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 // priority
04 D5 45 4D // SceneDestroyObject
4F ED B0 56 0C 00 00 00 00 // object ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete