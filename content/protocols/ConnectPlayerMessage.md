---
title: ConnectPlayerMessage
url: https://wiki.swganh.org/index.php/ConnectPlayerMessage
page_type: Client Packet
opcode: 2E365218
revision_id: 19956
last_modified: 2007-12-28T17:14:34Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ClientPacket', 'Template:100%']
---

# ConnectPlayerMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| INT | 0 |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 2E365218

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 // Op Count
18 52 36 2E // ConnectPlayerMessage
00 00 00 00 // unk int always 0
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete