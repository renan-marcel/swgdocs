---
title: ChatServerStatus
url: https://wiki.swganh.org/index.php/ChatServerStatus
page_type: Server Packet
opcode: 7102B15F
revision_id: 21047
last_modified: 2008-01-07T01:53:29Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# ChatServerStatus

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| BYTE | Status |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 7102B15F

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 
5F B1 02 71 //ChatServerStatus
01          //0 = offline and 1= online
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete