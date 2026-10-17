---
title: UpdateCellPermissionMessage
url: https://wiki.swganh.org/index.php/UpdateCellPermissionMessage
page_type: Server Packet
opcode: F612499C
revision_id: 18456
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# UpdateCellPermissionMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand count |
| INT | Opcode |
| BYTE | Permission Flag (0/1) |
| LONG | cell ID |

## Variable Descriptions
- Operand_Count	     = 3
- Opcode		     = F612499C

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
[UINT16] 0x0003
	[UINT32] 0xf612499c
	[UINT8]  1
        [UINT64] cell ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete