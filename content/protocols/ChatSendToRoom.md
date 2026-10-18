---
title: ChatSendToRoom
url: https://wiki.swganh.org/index.php/ChatSendToRoom
page_type: Client Packet
opcode: 20E4DBE3
revision_id: 20946
last_modified: 2008-01-06T23:16:16Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:U string', 'Template:ClientPacket', 'Template:100%']
---

# ChatSendToRoom

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| U_STRING | Message |
| INT | String Spacer |
| INT | Room ID |
| INT | Message Counter |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 20E4DBE3

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00       // Op Count
E3 DB E4 20 // ChatSendToRoom
12 00 00 00                                           // string count
74 00 65 00 73 00 74 00 69 00 6E 00 67 00 20 00 67 00 // t.e.s.t.i.n.g. .g.
75 00 69 00 6C 00 64 00 20 00 63 00 68 00 61 00 74 00 // u.i.l.d...c.h.a.t.
00 00 00 00 // string spacer
68 D5 28 03 // room ID
01 00 00 00 // Message counter
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete