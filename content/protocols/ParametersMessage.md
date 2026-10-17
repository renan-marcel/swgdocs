---
title: ParametersMessage
url: https://wiki.swganh.org/index.php/ParametersMessage
page_type: Server Packet
opcode: 487652DA
revision_id: 22124
last_modified: 2008-01-24T14:44:02Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# ParametersMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | Parameter_Flags |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 487652DA

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
DA 52 76 48 // ParametersMessage
84 03 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete