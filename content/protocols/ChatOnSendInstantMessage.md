---
title: ChatOnSendInstantMessage
url: https://wiki.swganh.org/index.php/ChatOnSendInstantMessage
page_type: Server Packet
opcode: 88DBB381
revision_id: 79342
last_modified: 2012-02-27T00:23:52Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Byte', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnSendInstantMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| BYTE | Opcode |
| INT | Error Code |
| INT | Count |

## Variable Descriptions
- Opperand_Count	     = 03
- Opcode		     = 88DBB381

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