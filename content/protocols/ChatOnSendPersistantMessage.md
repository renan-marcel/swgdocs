---
title: ChatOnSendPersistantMessage
url: https://wiki.swganh.org/index.php/ChatOnSendPersistantMessage
page_type: Server Packet
opcode: 94E7A7AE
revision_id: 21142
last_modified: 2008-01-07T05:13:13Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Byte', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnSendPersistantMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| BYTE | Opcode |
| INT | Error |
| INT | Count |

## Variable Descriptions
- Opperand_Count	     = 03
- Opcode		     = 94E7A7AE

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 81 B3 DB 88 00 00 00 00 01 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete