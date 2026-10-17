---
title: DeleteCharacterReplyMessage
url: https://wiki.swganh.org/index.php/DeleteCharacterReplyMessage
page_type: Server Packet
opcode: 8268989B
revision_id: 19959
last_modified: 2007-12-28T17:17:46Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# DeleteCharacterReplyMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | Failure Flag |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 8268989B

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 // Op Count
9B 98 68 82 // DeleteCharacterReplyMessage
00 00 00 00 // delete status 00= deleted  01 = error
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete