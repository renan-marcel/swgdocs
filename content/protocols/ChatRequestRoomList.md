---
title: ChatRequestRoomList
url: https://wiki.swganh.org/index.php/ChatRequestRoomList
page_type: Client Packet
opcode: 4C3D2CFA
revision_id: 22134
last_modified: 2008-01-24T17:52:23Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ClientPacket', 'Template:100%']
---

# ChatRequestRoomList

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Op Count	     = 1
- Opcode		     = 4C3D2CFA

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00 // Op Count
FA 2C 3D 4C // ChatRequestRoomList
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete