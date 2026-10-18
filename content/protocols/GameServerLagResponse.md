---
title: GameServerLagResponse
url: https://wiki.swganh.org/index.php/GameServerLagResponse
page_type: Client Packet
opcode: 789A4E0A
revision_id: 79356
last_modified: 2012-03-30T14:01:39Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# GameServerLagResponse

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 789A4E0A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00       // Op Count
78 9A 4E 0A // GameServerLagResponse
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete