---
title: MSCO03
url: https://wiki.swganh.org/index.php/MSCO03
page_type: Baseline
opcode: 
revision_id: 39261
last_modified: 
completion: 50%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:MSCOArchitectureNAV', 'Template:50%', 'Template:ServerPacket']
---

# MSCO03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| FLOAT | Complexity |
| ASTRING | ItemNameSTFTable |
| INT | NotUsed |
| ASTRING | ItemNameSTFID |
| USTRING | CustomName |
| INT | Volume |
| INT | SchematicQuantity |
| INT | PropertiesList |
| INT | UpdateCounter |
| BYTE | DeltaUpdateType(00 in baseline) |
| ASTRING | PropertySTFTable |
| INT | NotUsed |
| ASTRING | PropertySTFID |
| FLOAT | PropertyValue |
| USTRING | CreatorsName |
| INT | Complexity |
| FLOAT | SchematicDataSize |

## Variable Descriptions
- Obj_OperandCount = 9
- 1 point = 8 seconds.

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
00 09 00 DD 
05 00 
0C 5F A7 68 
3D C8 12 6D 02 00 00 00 
4F 43 53 4D 03 // OCSM 3
09 00 00 00 
B0 41 
0F 00 
73 74 72 69 6E 67 5F 69 64 5F 74 61 62 6C 65 // string_id_table
00 00 00 00
00 00 
07 00 00 00 
41 00 42 00 52 00 69 00 66 00 6C 00 65 00 // A.B.R.i.f.l.e
00 00 00 00 
C8 03 00 00 
0B 00 00 00 
20 00 00 00 
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting
00 00 00 00 
0B 00 
61 74 74 61 63 6B 53 70 65 65 64 // attackSpeed
50 BB 49 C0                      // -3.15
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting
00 00 00 00 
0A 00 
63 6F 6D 70 6C 65 78 69 74 79    // complexity
00 00 D0 41                      // 26
00 
08 00 
63 72 61 66 74 69 6E 67         // crafting
00 00 00 00 
09 00 
68 69 74 50 6F 69 6E 74 73      // hitPoints
2E 6D 99 41                     // 19
00 
08 00 
63 72 61 66 74 69 6E 67         // crafting 
00 00 00 00 
09 00 
6D 61 78 44 61 6D 61 67 65      // maxDamage
1A 1E 34 41                     // 11.26
00 
08 00 
63 72 61 66 74 69 6E 67         // crafting  
00 00 00 00 
0B 00 
6D 61 78 52 61 6E 67 65 4D 6F 64 // maxRangeMod
00 00 00 00 
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
0B 00 
6D 69 64 52 61 6E 67 65 4D 6F 64 // midRangeMod
14 18 90 41                      // 18
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
09 00 
6D 69 6E 44 61 6D 61 67 65       // minDamage
1A 1E 34 41                      // 11
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
0B 00 
6D 69 6E 52 61 6E 67 65 4D 6F 64 // minRangeMod
00 00 00 00 
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
0B 00 
77 6F 75 6E 64 43 68 61 6E 63 65 // woundChance
14 18 90 40                      // 4.5
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
02 00
78 70                            // xp
00 00 E6 42                      // 115.0
00 
08 00 
63 72 61 66 74 69 6E 67          // crafting 
00 00 00 00 
0C 00 
7A 65 72 6F 52 61 6E 67 65 4D 6F 64 // zeroRangeMod
00 00 00 00 
05 00 00 00 
4B 00 61 00 6D 00 6D 00 69 00       // K.a.m.m.i
19 00 00 00 
00 00 00 41 
01 F0 23
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete