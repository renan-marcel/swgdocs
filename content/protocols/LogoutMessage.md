---
title: LogoutMessage
url: https://wiki.swganh.org/index.php/LogoutMessage
page_type: Server Packet
opcode: 42FD19DD
revision_id: 21461
last_modified: 2008-01-09T02:26:55Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# LogoutMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | Op Count |
| INT | OpCode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 0x42FD19DD

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00 // Op Count
DD 19 FD 42 // LogoutMessage
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete