---
title: GRUP06
url: https://wiki.swganh.org/index.php/GRUP06
page_type: Baseline
opcode: 
revision_id: 257339
last_modified: 2023-07-10T18:14:03Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:GRUPArchitectureNAV', 'Template:75%', 'Template:ServerPacket']
---

# GRUP06

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjOpperandCount |
| INT | ?? |
| INT | MemberList_Size |
| INT | MemberList_UpdateCounter |
| LONG | MemberObjID |
| ASTRING | MemberName |
| INT | ??ListSize |
| INT | ??ListUpdateCounter |
| LONG | ?? |
| INT | ?? |
| ASTRING | ?? |
| SHORT | GroupCon/Difficulty |
| INT | ?? |
| LONG | LootMaster |
| INT | LootRule |

## Variable Descriptions
- Obj_OperandCount = 8

## Notes
- **TODO:** Reverse the JTL data and whatever else is left...

## Tags
- **75%** - This packet has been partially reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselineMessage
65 EE 47 95 25 00 00 00 // Group ID
50 55 52 47 06          // PURG 6
8A 00 00 00 
09 00 43 00 
00 00 
0F 00                          // string count
73 74 72 69 6E 67 5F 69 64 5F  // string_id_
74 61 62 6C 65                 // table
00 00 00 00 
00 00 
02 00 00 00 // Member List Size
02 00 00 00 // Member List Update Counter
B8 A1 AF 61 0C 00 00 00 // Patrizia's character ID
12 00                                                 // string count
50 61 74 72 69 7A 69 61 20 46 6C 79 72 75 6E 6E 65 72 // Patrizia.Flyrunner
8A 97 9A 8F 25 00 00 00 // Rouse's Character ID
0B 00                                   // string count
52 6F 75 73 65 20 44 61 65 6C 61        // Rouse.Daela
02 00 00 00 // Ship List Size
02 00 00 00 // Ship List Update Counter
00 00 00 00 00 00 00 00 // Ship ID 1
00 00 00 00 // Ship Position for formation
00 00 00 00 00 00 00 00 // Ship ID 2
01 00 00 00 // Ship Position for formation
00 00 // Unknown Short
05 00  // con dificulty????
00 00 00 00 
B8 A1 AF 61 0C 00 00 00 // Patrizia's character ID  Group leader
00 00 00 00 // loot rule
0E
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete