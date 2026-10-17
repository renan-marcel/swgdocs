---
title: OpenHolocronToPageMessage
url: https://wiki.swganh.org/index.php/OpenHolocronToPageMessage
page_type: Server Packet
opcode: 7CB65021
revision_id: 44408
last_modified: 2008-08-26T13:11:03Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# OpenHolocronToPageMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| SHORT | 0 |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = 7CB65021

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
09 00 // Op Count
21 50 B6 7C // OpenHolocronToPageMessage
00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete