---
title: ChatOnSendRoomMessage
url: https://wiki.swganh.org/index.php/ChatOnSendRoomMessage
page_type: Server Packet
opcode: E7B61633
revision_id: 28732
last_modified: 2008-05-11T11:37:13Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnSendRoomMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | Operand Count |
| INT | Opcode |
| INT | ErrorCode |
| INT | MessageID |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = E7B61633

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 
33 16 B6 E7 // ChatOnSendRoomMessage
00 00 00 00 // Error Code
01 00 00 00 // MessageID
```

## Related Pages
- [[ChatRoomMessage]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete