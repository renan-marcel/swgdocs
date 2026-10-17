---
title: ConnectionServerLagResponse
url: https://wiki.swganh.org/index.php/ConnectionServerLagResponse
page_type: Client Packet
opcode: 1590F63C
revision_id: 79358
last_modified: 2012-03-30T14:08:01Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# ConnectionServerLagResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 1590F63C

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00       // Op Count
15 90 F6 3C // ConnectionServerLagResponse
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete