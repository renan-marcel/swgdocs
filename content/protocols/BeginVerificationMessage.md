---
title: BeginVerificationMessage
url: https://wiki.swganh.org/index.php/BeginVerificationMessage
page_type: Server Packet
opcode: E7481DF5
revision_id: 21523
last_modified: 2008-01-09T13:44:39Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# BeginVerificationMessage

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
- Opcode		     = E7491DF5

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00 // Op Count
F5 1D 49 E7 // BeginVerificationMessage
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete