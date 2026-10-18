---
title: SpatialChat (000000F4)
url: https://wiki.swganh.org/index.php/SpatialChat_%28000000F4%29
page_type: Object Controller
opcode: 000000F4
revision_id: 58876
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Unknown', 'Template:U string', 'Template:Short', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# SpatialChat (000000F4)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Source ID |
| INT | ?? |
| LONG | Source ID |
| LONG | Target ID |
| INT | Unicode String Size |
| U_STRING | Text |
| INT | String Spacer |
| SHORT | ?? |
| SHORT | Mood 1 |
| SHORT | Mood 2 |
| BYTE | ?? |
| BYTE | Language |
| LONG | ?? |

## Variable Descriptions
- controllerID	     = 000000F4

## Notes
- **NOTE:** The first ID in this OCM needs to be the ID of the receiving object

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
46 5E CE 80 
0B 00 00 00 
F4 00 00 00 
52 1C 81 16 0F 00 00 00 
00 00 00 00 
A2 BB 24 B1 08 00 00 00 
00 00 00 00 
00 00 00 00 
81 00 00 00 
48 00 69 00 2C 00 20 00 57 00 65 00 6C 00   ..H.i.,. .W.e.l.
63 00 6F 00 6D 00 65 00 20 00 74 00 6F 00 20 00   c.o.m.e. .t.o. .
74 00 68 00 65 00 20 00 43 00 6F 00 72 00 6F 00   t.h.e. .C.o.r.o.
6E 00 65 00 74 00 20 00 43 00 61 00 6E 00 74 00   n.e.t. .C.a.n.t.
69 00 6E 00 61 00 21 00 20 00 53 00 69 00 74 00   i.n.a.!. .S.i.t.
20 00 64 00 6F 00 77 00 6E 00 20 00 61 00 6E 00    .d.o.w.n. .a.n.
64 00 20 00 77 00 61 00 74 00 63 00 68 00 20 00   d. .w.a.t.c.h. .
74 00 68 00 65 00 20 00 65 00 6E 00 74 00 65 00   t.h.e. .e.n.t.e.
72 00 74 00 61 00 69 00 6E 00 65 00 72 00 73 00   r.t.a.i.n.e.r.s.
20 00 66 00 6F 00 72 00 20 00 49 00 6E 00 73 00    .f.o.r. .I.n.s.
70 00 69 00 72 00 61 00 74 00 69 00 6F 00 6E 00   p.i.r.a.t.i.o.n.
20 00 62 00 75 00 66 00 66 00 73 00 2E 00 20 00    .b.u.f.f.s... .
54 00 69 00 70 00 73 00 20 00 61 00 72 00 65 00   T.i.p.s. .a.r.e.
20 00 61 00 6C 00 73 00 6F 00 20 00 61 00 70 00    .a.l.s.o. .a.p.
70 00 72 00 69 00 63 00 69 00 61 00 74 00 65 00   p.r.i.c.i.a.t.e.
64 00 2E 00 20 00 54 00 68 00 61 00 6E 00 6B 00   d... .T.h.a.n.k.
73 00 21 00 s.!.
32 00 01 00 
00 00 00 01 
00 00 00 00
00 00 00 00 
==================================================================
05 00 
46 5E CE 80 
0B 00 00 00 
F4 00 00 00        ....F^..........
EE B4 79 8B 33 00 00 00 // characterID
00 00 00 00 
EE B4 79 8B 33 00 00 00 // characterID
00 00 00 00 
00 00 00 00 
23 00 00 00     // u-string count
79 00 6F 00 20 00 68 00 6F 00 20 00 68 00 6F 00        // y.o...h.o...h.o.
20 00 69 00 74 00 73 00 20 00 61 00 20 00 70 00        // ..i.t.s...a...p.
69 00 72 00 61 00 74 00 65 00 73 00 20 00 6C 00        // i.r.a.t.e.s...l.
69 00 66 00 65 00 20 00 66 00 6F 00 72 00 20 00        // i.f.e...f.o.r...
6D 00 65 00 21 00                                      // m.e.!.
00 00 00 00 	// string spacer
64 00 
50 00 00 00 
01 00 
00 00 00 00 
00 00 00 


====================================================

05 00 
46 5E CE 80 
0B 00 00 00 
F4 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
00 00 00 00 
64 00 00 00 
79 00 6F 00 75 00 20 00 73        ...d...y.o.u...s
00 6F 00 20 00 68 00 61 00 69 00 72 00 79 00 20        .o...h.a.i.r.y..
00 74 00 68 00 61 00 74 00 20 00 77 00 68 00 65        .t.h.a.t...w.h.e
00 6E 00 20 00 79 00 6F 00 75 00 20 00 77 00 65        .n...y.o.u...w.e
00 6E 00 74 00 20 00 74 00 6F 00 20 00 73 00 68        .n.t...t.o...s.h
00 61 00 76 00 65 00 20 00 79 00 6F 00 75 00 72        .a.v.e...y.o.u.r
00 20 00 63 00 72 00 6F 00 74 00 63 00 68 00 2C        ...c.r.o.t.c.h.,
00 20 00 74 00 68 00 65 00 20 00 66 00 6C 00 65        ...t.h.e...f.l.e
00 61 00 73 00 20 00 73 00 61 00 69 00 64 00 20        .a.s...s.a.i.d..
00 74 00 68 00 61 00 6E 00 6B 00 20 00 67 00 6F        .t.h.a.n.k...g.o
00 64 00 20 00 77 00 65 00 20 00 63 00 61 00 6E        .d...w.e...c.a.n
00 20 00 73 00 65 00 65 00 20 00 74 00 68 00 65        ...s.e.e...t.h.e
00 20 00 6C 00 69 00 67 00 68 00 74 00 21 00 
00 00 00 00 
32 00 
09 00 00 00 
01 00 
00 00 00 00 
00 00 00 2F 

====================================================

05 00
46 5E CE 80 
0B 00 00 00 
F4 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
00 00 00 00 
27 00 00 00 
74 00 6F 00 20 00 62 00 65 00 20        .'...t.o...b.e..
00 6F 00 72 00 20 00 6E 00 6F 00 74 00 20 00 74        .o.r...n.o.t...t
00 6F 00 20 00 62 00 65 00 20 00 74 00 68 00 61        .o...b.e...t.h.a
00 74 00 20 00 69 00 73 00 20 00 74 00 68 00 65        .t...i.s...t.h.e
00 20 00 71 00 75 00 65 00 73 00 74 00 69 00 6F        ...q.u.e.s.t.i.o
00 6E 00 
00 00 00 00 
32 00 
34 00 00 00 
01 00 
00 00 00 00 
00 00 00 2F 


====================================================

05 00 
46 5E CE 80 
0B 00 00 00 
F4 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
EE B4 79 8B 33 00 00 00 
00 00 00 00 
00 00 00 00 
19 00 00 00 
6C 00 6F 00 72 00 64 00 20 00 76        .....l.o.r.d...v
00 61 00 64 00 65 00 72 00 20 00 69 00 73 00 20        .a.d.e.r...i.s..
00 6E 00 6F 00 74 00 20 00 70 00 6C 00 65 00 61        .n.o.t...p.l.e.a
00 73 00 65 00 64 00 
00 00 00 00 
32 00 
09 00 00 00 
01 00 
00 00 00 00 
00 00 00 2F
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 50% Complete