---
title: PermissionListCreateMessage
url: https://wiki.swganh.org/index.php/PermissionListCreateMessage
page_type: Server Packet
opcode: 52F364B8
revision_id: 63965
last_modified: 2009-10-14T13:05:16Z
completion: 50%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '50% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:50%']
---

# PermissionListCreateMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | listsize |
| U_STRING | Unicode Name of person on the list |
| INT | 61hex unknown |
| WORD | 0hex unknown |
| U_STRING | listname |

## Variable Descriptions
- Opperand_Count	     = X
- Opcode		     = 52F364B8

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **50%** - This packet has been partially reversed.

## Sample Packet
```
Opcode[1391682744]04 00 B8 64 F3 52 01 00 00 00 04 00 00 00 57 00 6F 00 6C 00 61 00 00 00 00 00 05 00 00 00 41 00 44 00 4D 00 49 00 4E 00 

...d.R........W.o.l.a.........A.D.M.I.N.

Opcode[1391682744]04 00 B8 64 F3 52 02 00 00 00 04 00 00 00 57 00 6F 00 6C 00 61 00 06 00 00 00 52 00 65 00 65 00 63 00 65 00 27 00 00 00 00 00 05 00 00 00 41 00 44 00 4D 00 49 00 4E 00 

...d.R........W.o.l.a.....R.e.e.c.e.'.........A.D.M.I.N.

Opcode[1391682744]04 00 B8 64 F3 52 03 00 00 00 04 00 00 00 57 00 6F 00 6C 00 61 00 06 00 00 00 52 00 65 00 65 00 63 00 65 00 27 00 04 00 00 00 52 00 65 00 63 00 65 00 00 00 00 00 05 00 00 00 41 00 44 00 4D 00 49 00 4E 00 

...d.R........W.o.l.a.....R.e.e.c.e.'.....R.e.c.e.........A.D.M.I.N.

Opcode[1391682744]04 00 B8 64 F3 52 04 00 00 00 04 00 00 00 57 00 6F 00 6C 00 61 00 06 00 00 00 52 00 65 00 65 00 63 00 65 00 27 00 04 00 00 00 52 00 65 00 63 00 65 00 06 00 00 00 4A 00 65 00 73 00 69 00 6E 00 65 00 00 00 00 00 05 00 00 00 41 00 44 00 4D 00 49 00 4E 00 

...d.R........W.o.l.a.....R.e.e.c.e.'.....R.e.c.e.....J.e.s.i.n.e.........A.D.M.I.N.

Opcode[1391682744]04 00 B8 64 F3 52 05 00 00 00 04 00 00 00 57 00 6F 00 6C 00 61 00 06 00 00 00 52 00 65 00 65 00 63 00 65 00 27 00 04 00 00 00 52 00 65 00 63 00 65 00 06 00 00 00 4A 00 65 00 73 00 69 00 6E 00 65 00 05 00 00 00 4B 00 72 00 69 00 6B 00 79 00 00 00 00 00 05 00 00 00 41 00 44 00 4D 00 49 00 4E 00 

...d.R........W.o.l.a.....R.e.e.c.e.'.....R.e.c.e.....J.e.s.i.n.e.....K.r.i.k.y.........A.D.M.I.N.

Opcode[1391682744]04 00 B8 64 F3 52 20 00 00 00 06 00 00 00 4A 00 65 00 73 00 69 00 6E 00 65 00 0B 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 68 00 61 00 72 00 6F 00 77 00 06 00 00 00 4B 00 6F 00 64 00 69 00 61 00 6B 00 04 00 00 00 50 00 65 00 64 00 6F 00 06 00 00 00 58 00 61 00 76 00 65 00 67 00 61 00 0B 00 00 00 53 00 74 00 72 00 6F 00 6E 00 67 00 62 00 65 00 61 00 72 00 64 00 04 00 00 00 52 00 65 00 63 00 65 00 06 00 00 00 56 00 61 00 6C 00 6F 00 72 00 56 00 05 00 00 00 50 00 6F 00 6F 00 6C 00 65 00 05 00 00 00 4B 00 72 00 69 00 6B 00 79 00 09 00 00 00 53 00 69 00 64 00 65 00 53 00 6C 00 61 00 73 00 68 00 08 00 00 00 42 00 6C 00 75 00 65 00 53 00 74 00 61 00 72 00 07 00 00 00 4A 00 65 00 73 00 65 00 72 00 69 00 63 00 05 00 00 00 4C 00 6F 00 67 00 61 00 72 00 05 00 00 00 52 00 69 00 73 00 6B 00 79 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 52 00 65 00 65 00 63 00 65 00 27 00 08 00 00 00 49 00 6E 00 73 00 74 00 69 00 6E 00 63 00 74 00 07 00 00 00 73 00 61 00 63 00 6B 00 65 00 74 00 74 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 06 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 09 00 00 00 47 00 75 00 69 00 6C 00 64 00 3A 00 4E 00 58 00 53 00 00 00 00 00 05 00 00 00 45 00 4E 00 54 00 52 00 59 00 

...d.R........J.e.s.i.n.e.....G.u.i.l.d.:.h.a.r.o.w.....K.o.d.i.a.k.....P.e.d.o.....X.a.v.e.g.a.....S.t.r.o.n.g.b.e.a.r.d.....R.e.c.e.....V.a.l.o.r.V.....P.o.o.l.e.....K.r.i.k.y.....S.i.d.e.S.l.a.s.h.....B.l.u.e.S.t.a.r.....J.e.s.e.r.i.c.....L.o.g.a.r.....R.i.s.k.y.....G.u.i.l.d.:.....R.e.e.c.e.'.....I.n.s.t.i.n.c.t.....s.a.c.k.e.t.t.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.....G.u.i.l.d.:.N.X.S.........E.N.T.R.Y.

Opcode[1391682744]04 00 B8 64 F3 52 00 00 00 00 01 00 00 00 08 00 00 00 49 00 6E 00 73 00 74 00 69 00 6E 00 63 00 74 00 03 00 00 00 42 00 41 00 4E 00 

...d.R............I.n.s.t.i.n.c.t.....B.A.N.

Opcode[1391682744]04 00 B8 64 F3 52 01 00 00 00 06 00 00 00 45 00 63 00 69 00 6C 00 61 00 4D 00 00 00 00 00 05 00 00 00 45 00 4E 00 54 00 52 00 59 00 

...d.R........E.c.i.l.a.M.........E.N.T.R.Y.

Opcode[1391682744]04 00 B8 64 F3 52 00 00 00 00 01 00 00 00 06 00 00 00 45 00 63 00 69 00 6C 00 61 00 4D 00 03 00 00 00 42 00 41 00 4E 00 

...d.R............E.c.i.l.a.M.....B.A.N.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 50% Complete