---
title: SHIP03
url: https://wiki.swganh.org/index.php/SHIP03
page_type: Baseline
opcode: 
revision_id: 39728
last_modified: 2008-06-25T17:56:50Z
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:SHIPArchitectureNAV', 'Template:50%']
---

# SHIP03

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| FLOAT | ?? (1.0) |
| A_STRING | STF File |
| INT | STF Spacer |
| A_STRING | STF Name |
| U_STRING | Object/Owner Name |
| INT | ?? |
| SHORT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| BYTE | ?? |
| FLOAT | ?? |
| FLOAT | Chassis Current Value |
| FLOAT | Chassis Max Value |
| INT | Engine Rel. |
| INT | List Size |
| INT | Update Count |
| BYTE | ?? |
| INT | Component Index |
| FLOAT | Current Armor Value |
| INT | List Size |
| INT | Update Count |
| BYTE | ?? |
| INT | Component Index |
| FLOAT | Max Armor Value |
| INT | List Size |
| INT | Update Count |
| BYTE | ?? |
| INT | Component Index |
| FLOAT | Current Hitpoints Value |
| INT | List Size |
| INT | Update Count |
| BYTE | ?? |
| INT | Component Index |
| FLOAT | Max Hitpoints Value |
| LIST5 |  |
| INT | List Size |
| INT | Update Count |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| FLOAT | frontshield hitpoints denomenator |
| FLOAT | backshield hitpoints denomenator |

## Variable Descriptions
- Obj_OperandCount = 16
- STF File = A_STRING(space_ship)

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
04 5A D1 D6 13 00 00 00 // ID
50 49 48 53 03          // PIHS 3
D1 01 00 00 
16 00 00 00 
80 3F 
0A 00 
73 70 61 63 65 5F 73 68 69 70 // space_ship
00 00 00 00 
1B 00 
70 6C 61 79 65 72 5F 73 6F 72 6F 73 75    // player_sorosu
75 62 5F 73 70 61 63 65 5F 79 61 63 68 74 // ub_space_yacht
00 00 00 00 
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 01 00 
00 00 00 00 
00 00 00 00 
00 00 64 00 
00 00 
01 CD CC 8C 3F 00 80 3B 45 00 80 3B 45 3A 7A 37   ....?..;E..;E:z7
DE 07 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
96 43 00 01 00 00 00 00 00 C8 42 00 02 00 00 00   .C........B.....
00 00 FA 43 00 04 00 00 00 00 00 48 43 00 05 00   ...C.......HC...
00 00 00 00 48 43 00 06 00 00 00 00 00 C8 42 00   ....HC........B.
07 00 00 00 00 00 A0 41 07 00 00 00 00 00 00 00   .......A........
00 00 00 00 00 00 00 96 43 00 01 00 00 00 00 00   ........C.......
C8 42 00 02 00 00 00 00 00 FA 43 00 04 00 00 00   .B........C.....
00 00 48 43 00 05 00 00 00 00 00 48 43 00 06 00   ..HC.......HC...
00 00 00 00 C8 42 00 07 00 00 00 00 00 A0 41 07   .....B........A.
00 00 00 00 00 00 00 00 00 00 00 00 00 00 96 43   ...............C
00 01 00 00 00 00 00 C8 42 00 02 00 00 00 00 00   ........B.......
C8 43 00 04 00 00 00 00 00 48 43 00 05 00 00 00   .C.......HC.....
00 00 48 43 00 06 00 00 00 00 00 C8 42 00 07 00   ..HC........B...
00 00 00 00 A0 41 07 00 00 00 00 00 00 00 00 00   .....A..........
00 00 00 00 00 96 43 00 01 00 00 00 00 00 C8 42   ......C........B
00 02 00 00 00 00 00 C8 43 00 04 00 00 00 00 00   ........C.......
48 43 00 05 00 00 00 00 00 48 43 00 06 00 00 00   HC.......HC.....
00 00 C8 42 00 07 00 00 00 00 00 A0 41 07 00 00   ...B........A...
00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 01   ................
00 00 00 02 00 00 00 00 02 00 00 00 02 00 00 00   ................
00 04 00 00 00 02 00 00 00 00 05 00 00 00 02 00   ................
00 00 00 06 00 00 00 02 00 00 00 00 07 00 00 00   ................
02 00 00 00 00 00 75 44 00 00 75 44 01 9D 8F
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete