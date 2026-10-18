---
title: ClientInactivityMessage
url: https://wiki.swganh.org/index.php/ClientInactivityMessage
page_type: Client Packet
opcode: 0F5D5325
revision_id: 22137
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Bool', 'Template:ClientPacket', 'Template:100%']
---

# ClientInactivityMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| BOOL | AFK_Flag |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 0F5D5325

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
25 53 5D 0F // ClientInactivityMessage
00 // afk flag
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete