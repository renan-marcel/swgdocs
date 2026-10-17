---
title: ChatEnterRoomById
url: https://wiki.swganh.org/index.php/ChatEnterRoomById
page_type: Client Packet
opcode: BC6BDDF2
revision_id: 20668
last_modified: 2008-01-04T14:03:52Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:ClientPacket', 'Template:75%']
---

# ChatEnterRoomById

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | Opcode |
| INT | ?? |
| INT | Room ID |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 0xBC6BDDF2

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
03 00 // Op Count
F2 DD 6B BC // ChatEnterRoomById
14 00 00 00 // ?? Maybe Server Number??
5D 0A 72 02 // Room ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete