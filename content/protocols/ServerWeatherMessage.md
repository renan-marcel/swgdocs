---
title: ServerWeatherMessage
url: https://wiki.swganh.org/index.php/ServerWeatherMessage
page_type: Server Packet
opcode: 486356EA
revision_id: 79176
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Float', 'Template:ServerPacket', 'Template:100%']
---

# ServerWeatherMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | Weather_ID |
| FLOAT | CloudVector_X-Coordinate |
| FLOAT | CloudVector_Z-Coordinate |
| FLOAT | CloudVector_Y-Coordinate |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 486356EA

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 
EA 56 63 48 
01 00 00 00 
17 5E FC 3F 
00 00 00 00 
3B 12 9D 3F 
32 
===================================================
03 00
EA 56 63 48 
01 00 00 00 
B0 CB EA 3F
00 00 00 00
D6 8D 92 3F 
1C
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete