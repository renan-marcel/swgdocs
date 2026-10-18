---
title: SuiUpdatePageMessage
url: https://wiki.swganh.org/index.php/SuiUpdatePageMessage
page_type: Server Packet
opcode: 5F3342F6
revision_id: 59573
last_modified: 
completion: 0%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '0% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:0%']
---

# SuiUpdatePageMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| BYTE | uint8 |
| SHORT | uint16 |
| INT | uint32 |
| FLOAT | uint32 |
| LONG | uint64 |
| A_STRING | ASCII String |
| U_STRING | Unicode String |
| C_STRING | Customization String |
| B_STRING | Byte String |
| { } | LIST Component |
| ? | Uncertain Values |
| ?? | Unknown Variable Name |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = 5F3342F6

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **0%** - This packet has not been reversed.

## Sample Packet
```
00 0D 06 E4 00 00 02 D7 02 00 F6 42 33 5F 43 67        ............B3_C
0B 00 0E 00 53 63 72 69 70 74 2E 6C 69 73 74 42        g....Script.list
6F 78 01 00 00 00 03 01 00 00 00 40 01 00 00 40        Box.........@...
00 62 00 61 00 73 00 65 00 5F 00 70 00 6C 00 61        @.b.a.s.e._.p.l.
00 79 00 65 00 72 00 3A 00 63 00 6C 00 6F 00 6E        a.y.e.r.:.c.l.o.
00 65 00 5F 00 70 00 72 00 6F 00 6D 00 70 00 74        n.e._.p.r.o.m.p.
00 5F 00 68 00 65 00 61 00 64 00 65 00 72 00 20        t._.h.e.a.d.e.r.
00 0A 00 0A 00 20 00 40 00 62 00 61 00 73 00 65        ........@.b.a.s.
00 5F 00 70 00 6C 00 61 00 79 00 65 00 72 00 3A        e._.p.l.a.y.e.r.
00 63 00 6C 00 6F 00 6E 00 65 00 5F 00 70 00 72        :.c.l.o.n.e._.p.
00 6F 00 6D 00 70 00 74 00 5F 00 64 00 61 00 74        r.o.m.p.t._.d.a.
00 61 00 20 00 0A 00 20 00 40 00 62 00 61 00 73        t.a.......@.b.a.
00 65 00 5F 00 70 00 6C 00 61 00 79 00 65 00 72        s.e._.p.l.a.y.e.
00 3A 00 63 00 6C 00 6F 00 6E 00 65 00 5F 00 70        r.:.c.l.o.n.e._.
00 72 00 6F 00 6D 00 70 00 74 00 5F 00 6C 00 6F        p.r.o.m.p.t._.l.
00 63 00 61 00 74 00 69 00 6F 00 6E 00 20 00 40        o.c.a.t.i.o.n...
00 62 00 61 00 73 00 65 00 5F 00 70 00 6C 00 61        @.b.a.s.e._.p.l.
00 79 00 65 00 72 00 3A 00 63 00 6C 00 6F 00 6E        a.y.e.r.:.c.l.o.
00 65 00 5F 00 6C 00 6F 00 63 00 61 00 74 00 69        n.e._.l.o.c.a.t.
00 6F 00 6E 00 5F 00 72 00 65 00 67 00 69 00 73        i.o.n._.r.e.g.i.
00 74 00 65 00 72 00 65 00 64 00 5F 00 73 00 65        s.t.e.r.e.d._.s.
00 6C 00 65 00 63 00 74 00 5F 00 62 00 65 00 67        e.l.e.c.t._.b.e.
00 69 00 6E 00 20 00 40 00 79 00 61 00 76 00 69        g.i.n...@.y.a.v.
00 6E 00 34 00 5F 00 72 00 65 00 67 00 69 00 6F        i.n.4._.r.e.g.i.
00 6E 00 5F 00 6E 00 61 00 6D 00 65 00 73 00 3A        o.n._.n.a.m.e.s.
00 79 00 61 00 76 00 69 00 6E 00 34 00 5F 00 6D        :.y.a.v.i.n.4._.
00 69 00 6E 00 69 00 6E 00 67 00 5F 00 6F 00 75        m.i.n.i.n.g._.o.
00 74 00 70 00 6F 00 73 00 74 00 20 00 40 00 62        u.t.p.o.s.t...@.
00 61 00 73 00 65 00 5F 00 70 00 6C 00 61 00 79        b.a.s.e._.p.l.a.
00 65 00 72 00 3A 00 63 00 6C 00 6F 00 6E 00 65        y.e.r.:.c.l.o.n.
00 5F 00 6C 00 6F 00 63 00 61 00 74 00 78 D0             ._.l.o.c.a.t.x.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Packet : 36

SOE_DATA_FRAG_A [0xD00]

199.108.197.148:44463 -> 192.168.0.150:4579 (Server -> Client)
Enc: T   Comp: T    Seed: 0xDDF778C7

00 0D 06 E5 69 00 6F 00 6E 00 5F 00 72 00 65 00        .....i.o.n._.r.e
67 00 69 00 73 00 74 00 65 00 72 00 65 00 64 00        .g.i.s.t.e.r.e.d
5F 00 73 00 65 00 6C 00 65 00 63 00 74 00 5F 00        ._.s.e.l.e.c.t._
65 00 6E 00 64 00 0A 00 20 00 40 00 62 00 61 00        .e.n.d.....@.b.a
73 00 65 00 5F 00 70 00 6C 00 61 00 79 00 65 00        .s.e._.p.l.a.y.e
72 00 3A 00 63 00 6C 00 6F 00 6E 00 65 00 5F 00        .r.:.c.l.o.n.e._
70 00 72 00 6F 00 6D 00 70 00 74 00 5F 00 64 00        .p.r.o.m.p.t._.d
69 00 73 00 74 00 61 00 6E 00 63 00 65 00 20 00        .i.s.t.a.n.c.e..
40 00 62 00 61 00 73 00 65 00 5F 00 70 00 6C 00        .@.b.a.s.e._.p.l
61 00 79 00 65 00 72 00 3A 00 63 00 6C 00 6F 00        .a.y.e.r.:.c.l.o
6E 00 65 00 5F 00 6C 00 6F 00 63 00 61 00 74 00        .n.e._.l.o.c.a.t
69 00 6F 00 6E 00 5F 00 75 00 6E 00 6B 00 6E 00        .i.o.n._.u.n.k.n
6F 00 77 00 6E 00 02 00 00 00 10 00 50 72 6F 6D        .o.w.n.......Pro
70 74 2E 6C 62 6C 50 72 6F 6D 70 74 04 00 54 65        mpt.lblPrompt..T
78 74 00 00 00 00 00 00 00 00 00 00 00 00 00 00        ext.............
00 00 00 00 00 00 24 82                                                ......$.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 0% Complete