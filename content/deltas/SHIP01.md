---
title: SHIP01
url: https://wiki.swganh.org/index.php/SHIP01
page_type: Baseline
opcode: 
revision_id: 21405
last_modified: 2008-01-08T17:50:52Z
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:SHIPArchitectureNAV', 'Template:50%']
---

# SHIP01

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | ?? |
| INT | ?? |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Energy Drain for corresponding component |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Mass for corresponding component |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | ?? |
| INT | ?? |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Weapon Refire Rate |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Value |
| FLOAT | Total Mass |
| FLOAT | Shield Recharge Rate |
| FLOAT | Weapon Recharge Rate? (need confirm) |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | Max Speed |
| FLOAT | Total Energy |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |

## Variable Descriptions
- Obj_OperandCount = 29

## Notes
- **TODO:** 

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 // Op Count
0C 5F A7 68 // Baseline Message
04 5A D1 D6 13 00 00 00 // SHIP id
50 49 48 53 // PIHS
01 
25 02 00 00 
29 00 00 00 
00 00 00 00 
00 00 
07 00 00 00 
00 00 00 00 
00 
00 00 00 00 
00 00 80 3F 
00 
01 00 00 00 
00 00 80 3F 
00 
02 00 00 00 
00 00 80 3F 
00 
04 00 00 00 
00 00 80 3F 
00 
05 00 00 00 
00 00 80 3F 
00 
06 00 00 00 
00 00 80 3F 
00 
07 00 00 00 
00 00 80 3F 
07 00 00 00 
00 00 00 00 
00 00 00 00 
00 
00 00 80 3F 
00 
01 00 00 00 
00 00 80 3F 
00 
02 00 00 00 
00 00 80 3F 
00 
04 00 00 00 
00 00 80 3F 
00 
05 00 00 00 
00 00 80 3F 
00 
06 00 00 00 
00 00 80 3F 
00 
07 00 00 00 
00 00 80 3F 
07 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 
01 00 00 00 
00 00 00 
00 00 
02 00 00 00 00 00 00 00 00 04 00 00 00 00   ................
00 00 00 00 05 00 00 00 00 00 00 00 00 06 00 00   ................
00 00 00 00 00 00 07 00 00 00 00 00 00 00 07 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00   ................
00 00 04 00 00 00 00 00 00 00 00 05 00 00 00 00   ................
00 00 00 00 06 00 00 00 00 00 00 00 00 07 00 00   ................
00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00   ................
02 00 00 00 00 00 00 00 00 04 00 00 00 00 00 00   ................
00 00 05 00 00 00 00 00 00 00 00 06 00 00 00 00   ................
00 00 00 00 07 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 50 C3 47   .............P.G
00 00 A0 40 00 00 00 44 66 66 00 42 00 01 12 17   ...@...Dff.B....


Packet : 577
199.108.198.52:44463 -> 24.1.10.254:1304 (Server->Client)
Zone Server: Fragmented: Enc: T: Comp: T 

00 0D 00 CA 00 A0 40 00 00 A0 40 F3 66 5F 3F F3   ......@...@.f_?.
66 5F 3F 36 8D 27 3F 94 30 37 3F 66 A8 BB 3E 94   f_?6.'?.07?f..>.
30 37 3F 00 00 38 42 28 6B 6E 4E 00 00 C8 42 00   07?..8B(knN...B.
00 A0 40 00 00 20 41 00 00 A0 41 00 00 70 41 00   ..@.. A...A..pA.
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 01 E0 DD         ..............
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete