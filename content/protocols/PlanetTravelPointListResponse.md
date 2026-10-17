---
title: PlanetTravelPointListResponse
url: https://wiki.swganh.org/index.php/PlanetTravelPointListResponse
page_type: Server Packet
opcode: 4D32541F
revision_id: 78288
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Beginlist', 'Template:Endlist', 'Template:Float', 'Template:Bool', 'Template:ServerPacket', 'Template:100%']
---

# PlanetTravelPointListResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | OpCode |
| A_STRING | Query Planet String |
| INT | PlanetsCount (number of planets) |

## Variable Descriptions
- Operand_Count	     = 9
- Opcode		     = 4D32541F

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
06 00                                           operand count
1F 54 32 4D			                crc
dathomir					respective planet string
32 02 00 00 00 					counter of starports / shuttleports
Dathomir.Outpost				name 1
Science.Outpost					name 2
02 00 00 00 					counter of starports / shuttleports
20 B9 1A 44 					x 1
78 44 C1 40 					z
3A 40 41 45 					y
73 16 44 C2 					x 2
00 00 90 41 					z
4A 17 C6 C4 					y
02 00 00 00 					counter of starports / shuttleports
2C 01 00 00 					add to tocket price 1
2C 01 00 00 					add to ticket price 2
02 00 00 00 					counter of starports / shuttleports
01 						reachable ? 1 = true 0 = false
01
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete