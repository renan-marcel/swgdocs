---
title: GuildResponseMessage
url: https://wiki.swganh.org/index.php/GuildResponseMessage
page_type: Server Packet
opcode: 32263F20
revision_id: 19781
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:A string', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# GuildResponseMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | Guild ID |
| A_STRING | GuildName |
| SHORT | ?? |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 32263F20

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
04 00
 20 3F 26 32             //GuildResponseMessage
 D2 CD 31 6E 0C 00 00 00 // Guild ID
 10 00                                             //string count
 44 61 65 6C 61 27 20 45 73 27 65 6D 62 6C 65 79   //'Daela' Es'embley' (guild's name)
 00 00 


------Unguilded player----
 04 00
 20 3F 26 32  //CRC = 'GuildResponseMessage
 00 26 69 B3
 23 00 00 00
 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete