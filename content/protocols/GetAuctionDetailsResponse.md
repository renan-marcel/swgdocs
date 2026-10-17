---
title: GetAuctionDetailsResponse
url: https://wiki.swganh.org/index.php/GetAuctionDetailsResponse
page_type: Server Packet
opcode: FE0E644B
revision_id: 21445
last_modified: 2008-01-09T02:19:41Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Beginlist', 'Template:A string', 'Template:U string', 'Template:Endlist', 'Template:ServerPacket', 'Template:100%']
---

# GetAuctionDetailsResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | OperandCode |
| INT | OpCode |
| LONG | Item ID |
| INT | Counter |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = FE0E644B

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 0D 04 FD 00 00 02 75 
02 00 

4B 64 0E FE 

A1 46 15 EB 10 00 00 00 

26 00 00 00 
4D 00 79 00 20 00      
62 00 65 00 73 00 74 00 20 00 63 00 6F 00 70 00        b.e.s.t...c.o.p.
70 00 65 00 72 00 20 00 6F 00 6E 00 6C 00 79 00        p.e.r...o.n.l.y.
20 00 6F 00 6E 00 20 00 69 00 6E 00 66 00 69 00        ..o.n...i.n.f.i.
62 00 6E 00 74 00 79 00 20 00 65 00 75 00 72 00        b.n.t.y...e.u.r.
6F 00 70 00 65 00                                      o.p.e.

0D 00 00 00 09 00 63 6F 6E 64        ......cond
69 74 69 6F 6E 07 00 00 00 31 00 30 00 30 00 2F        ition....1.0.0./
00 31 00 30 00 30 00 06 00 76 6F 6C 75 6D 65 01        .1.0.0...volume.
00 00 00 31 00 11 00 72 65 73 6F 75 72 63 65 5F        ...1...resource_
63 6F 6E 74 65 6E 74 73 0C 00 00 00 35 00 36 00        contents....5.6.
30 00 38 00 2F 00 31 00 30 00 30 00 30 00 30 00        0.8./.1.0.0.0.0.
30 00 30 00 0D 00 72 65 73 6F 75 72 63 65 5F 6E        0.0...resource_n
61 6D 65 09 00 00 00 51 00 75 00 61 00 64 00 61        ame....Q.u.a.d.a
00 76 00 6F 00 6E 00 6F 00 0E 00 72 65 73 6F 75        .v.o.n.o...resou
72 63 65 5F 63 6C 61 73 73 2C 00 00 00 40 00 72        rce_class,...@.r
00 65 00 73 00 6F 00 75 00 72 00 63 00 65 00 2F        .e.s.o.u.r.c.e./
00 72 00 65 00 73 00 6F 00 75 00 72 00 63 00 65        .r.e.s.o.u.r.c.e
00 5F 00 6E 00 61 00 6D 00 65 00 73 00 3A 00 63        ._.n.a.m.e.s.:.c
00 6F 00 70 00 70 00 65 00 72 00 5F 00 62 00 6F        .o.p.p.e.r._.b.o
00 72 00 6F 00 63 00 61 00 72 00 62 00 69 00 74        .r.o.c.a.r.b.i.t
00 69 00 63 00 0F 00 72 65 73 5F 63 6F 6C 64 5F        .i.c...res_cold_
72 65 73 69 73 74 03 00 00 00 35 00 37 00 31 00        resist....5.7.1.
10 00 72 65 73 5F 63 6F 6E 64 75 63 74 69 76 69        ..res_conductivi
74 79 03 00 00 00 35 00 32 00 35 00 10 00 72 65        ty....5.2.5...re
73 5F 64 65 63 61 79 5F 72 65 73 69 73 74 03 00        s_decay_resist..
00 00 36 00 36 00 34 00 0F 00 72 65 73 5F 68 65        ..6.6.4...res_he
61 74 5F 72 65 73 69 73 74 03 00 00 00 39 00 39        at_resist....9.9
00 39 00 10 00 72 65 73 5F 6D 61 6C 6C 65 61 62        .9...res_malleab
69 6C 69 74 79 03 00 00 00 37 00 32 00 36 00 0B        ility....7.2.6..
00 72 65 73 5F 71 75 61 6C 69 74 79 03 04 B0           .res_quality...




00 0D 04 4F 00 00 02 55 02 00 

4B 64 0E FE                                Opccode GetAuctionDetailsResponse

39 3D B1 2F 0F 00 00 00                    ID Item

00 00 00 00 
[UINT32] counter

  [ASCII]    condition [UNICODE]  6.0.0./.6.0.0.
  volume....1...
  healing_combat_level_required....7.2.
  tooltip.healing_combat_level_required....7.2..
  skillmodmin N.o.n.e...
  tooltip.skillmodmin....N.o.n.e...
  cat_wpn_damage.wpn_damage_type....@.o.b.j._.a.t.t.r._.n.:.a.r.m.o.r._.e.f.f._.e.n.e.rgy
  tooltip.wpn_damage_type..


object/weapon/melee/polearm/shared_polearm_vibro_axe.iff
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete