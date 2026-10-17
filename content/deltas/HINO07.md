---
title: HINO07
url: https://wiki.swganh.org/index.php/HINO07
page_type: Baseline
opcode: 
revision_id: 64503
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:HINOArchitectureNAV', 'Template:75%']
---

# HINO07

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | Num Items Available List Size |
| INT | Num Items Available Update Count |
| LONG | Resource ID |
| INT | Num Items Available List Size |
| INT | Num Items Available Update Count |
| LONG | Resource ID |
| INT | Num Items Available List Size |
| INT | Num Items Available Update Count |
| A_String | Resource Name |
| INT | Num Items Available List Size |
| INT | Num Items Available Update Count |
| A_String | Resource Type |
| LONG | Current Resource ID active in Harvester |
| BYTE | Operation Status 00 or 01 |
| FLOAT | Capacity |
| FLOAT | Spec Rate |
| FLOAT | Actual Rate |
| FLOAT | Hopper Quantity |
| INT | Hopper Size |
| BYTE | Count (List size +1, except when zero, so it seems) |
| INT | List Size    Items in Hopper |
| INT | Update Count |
| LONG | ResourceID |
| FLOAT | Quantity |
| BYTE | Integrity |

## Variable Descriptions
- Obj_OperandCount = ??

## Notes
_none_

## Tags
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68 
25 B2 CF 1C 21 00 00 00 // Harvester ID
4F 4E 49 48 07 // ONIH 7
1E 04 00 00 
0F 
00 01 
16 00 00 00 
16 00 00 00 
56 71 D7 0A 21 00 00 00 // Resource IDS
2B EC D9 0A 21 00 00 00 
29 81 D9 0A 21 00 00 00 
EC DB BD 01 21 00 00 00 
C3 DC DD 0A 21 00 00 00 
ED DB BD 01 21 00 00 00 
12 36 36 03 21 00 00 00 
92 AD D1 F2 20 00 00 00 
5D 40 EC 19 21 00 00 00 
6C 24 D7 0A 21 00 00 00 
8E 8E 62 1C 21 00 00 00 
45 E7 94 13 21 00 00 00 
8F 11 98 13 21 00 00 00 
7A FC 08 FB 20 00 00 00 
2B 3E 5E 1C 21 00 00 00 
13 39 38 03 21 00 00 00 
5C AE DC 0A 21 00 00 00 
D4 8F 00 FB 20 00 00 00 
DA DC D6 0A 21 00 00 00 
A1 D8 95 13 21 00 00 00 
5E B2 B8 18 21 00 00 00 
6E 4A 77 00 21 00 00 00 
16 00 00 00 
16 00 00 00 
56 71 D7 0A 21 00 00 00 
2B EC D9 0A 21 00 00 00 
29 81 D9 0A 21 00 00 00 
EC DB BD 01 21 00 00 00 
C3 DC DD 0A 21 00 00 00 
ED DB BD 01 21 00 00 00 
12 36 36 03 21 00 00 00 
92 AD D1 F2 20 00 00 00 
5D 40 EC 19 21 00 00 00 
6C 24 D7 0A 21 00 00 00 
8E 8E 62 1C 21 00 00 00 
45 E7 94 13 21 00 00 00 
8F 11 98 13 21 00 00 00 
7A FC 08 FB 20 00 00 00 
2B 3E 5E 1C 21 00 00 00 
13 39 38 03 21 00 00 00 
5C AE DC 0A 21 00 00 00 
D4 8F 00 FB 20 00 00 00 
DA DC D6 0A 21 00 00 00 
A1 D8 95 13 21 00 00 00 
5E B2 B8 18 21 00 00 00 
6E 4A 77 00 21 00 00 00 
16 00 00 00               // Start Of resource names below
16 00 00 00 
09 00 
44 75 72 6F 77 61 69 73 6D // Durowaism
0B 00 
4F 6D 6E 69 6A 69 77 65 69 6E 65 // Omnijiweine
0B 00 
44 69 6D 65 73 61 67 6F 69 73 6D // Dimesagoism
06 00 
41 6D 65 75 6E 69 // Ameuni
0C 00 
4F 6D 6E 69 70 6F 68 61 70 69 61 6E // Omnipohapian
05 00 
57 61 67 69 66 // Wagif
06 00 
45 63 61 69 61 6E // Ecaian
07 00 
45 69 6C 65 6B 65 70 // Eilekep

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


00 0D 05 F3 06 00 49 66 69 67 65 6F 0A 00 44 75        ......Ifigeo..Du
72 65 6E 69 6D 72 69 73 07 00 46 6F 62 69 69 74        renimris..Fobiit
65 07 00 41 77 6F 76 69 73 6D 09 00 4F 6D 6E 69        e..Awovism..Omni
66 65 75 77 69 06 00 49 64 69 72 69 73 0A 00 50        feuwi..Idiris..P
65 65 72 61 66 69 61 74 65 04 00 47 61 62 6F 04        eerafiate..Gabo.
00 52 6F 6E 65 0D 00 4F 6D 6E 69 64 69 74 6F 63        .Rone..Omniditoc
65 69 61 6D 06 00 4F 77 6F 69 75 6D 07 00 44 65        eiam..Owoium..De
61 64 69 6F 6B 09 00 51 75 61 64 64 69 61 74 65        adiok..Quaddiate
09 00 4D 6F 67 65 61 6B 69 61 6E // Mogeakian
16 00 00 00
16 00 00 00                // Start of resource Types Below
1A 00 
70 65 74 72 6F 63 68 65 6D 5F 66 // petrochem_f
75 65 6C 5F 73 6F 6C 69 64 5F 74 79 70 65 33 11        uel_solid_type3.
00 72 61 64 69 6F 61 63 74 69 76 65 5F 74 79 70        .radioactive_typ
65 33 0D 00 73 74 65 65 6C 5F 72 68 6F 64 69 75        e3..steel_rhodiu
6D 0E 00 73 74 65 65 6C 5F 63 75 62 69 72 69 61        m..steel_cubiria
6E 0E 00 73 74 65 65 6C 5F 63 75 62 69 72 69 61        n..steel_cubiria
6E 0F 00 73 74 65 65 6C 5F 74 68 6F 72 61 6E 69        n..steel_thorani
75 6D 10 00 73 74 65 65 6C 5F 6E 65 75 74 72 6F        um..steel_neutro
6E 69 75 6D 0E 00 73 74 65 65 6C 5F 64 75 72 61        nium..steel_dura
6C 6C 6F 79 0C 00 69 72 6F 6E 5F 61 78 69 64 69        lloy..iron_axidi
74 65 0C 00 69 72 6F 6E 5F 6B 61 6D 6D 72 69 73        te..iron_kammris
11 00 61 6C 75 6D 69 6E 75 6D 5F 74 69 74 61 6E        ..aluminum_titan
69 75 6D 12 00 61 6C 75 6D 69 6E 75 6D 5F 6C 69        ium..aluminum_li
6E 6B 73 74 65 65 6C 0B 00 63 6F 70 70 65 72 5F        nksteel..copper_
64 65 73 68 0F 00 63 6F 70 70 65 72 5F 74 68 61        desh..copper_tha
6C 6C 69 75 6D 0E 00 63 6F 70 70 65 72 5F 64 69        llium..copper_di
61 74 69 75 6D 0D 00 63 6F 70 70 65 72 5F 6D 79        atium..copper_my
74 68 72 61 15 00 6F 72 65 5F 63 61 72 62 6F 6E        thra..ore_carbon
61 74 65 5F 6C 6F 6D 6D 69 74 65 15 00 6F 72 65        ate_lommite..ore
5F 73 69 6C 69 63 6C 61 73 74 69 63 5F 63 72 69        _siliclastic_cri
73 6D 0E 00 61 72 6D 6F 70 68 6F 75 73 5F 72 79        sm..armophous_ry
6C 6C 12 00 61 72 6D 6F 70 68 6F 75 73 19 5C           ll..armophous.\

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


00 0D 05 F4 5F 62 61 6C 74 61 72 61 6E 21 00 63        ...._baltaran!.c
72 79 73 74 61 6C 6C 69 6E 65 5F 6C 61 62 6F 69        rystalline_laboi
5F 6D 69 6E 65 72 61 6C 5F 63 72 79 73 74 61 6C        _mineral_crystal
12 00 63 72 79 73 74 61 6C 6C 69 6E 65 5F 76 65        ..crystalline_ve
72 74 65 78                                            rtex
00 00 00 00 00 00 00 00 // Current Resource ID Harvesting
00 // Harvester Status Flag 00 off 01 on
08 00 00 00 // Capacity (float)
00 00 00 41 // Spec Rate (float)
00 00 00 00 // Actual Rate (float)
00 00 00 00 // Hopper Amount (float)
3D E3 00 00 // Hopper Size (float)
00 
00 00 00 00 
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete