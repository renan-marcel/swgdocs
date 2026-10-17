---
title: FCYT03
url: https://wiki.swganh.org/index.php/FCYT03
page_type: Baseline
opcode: 
revision_id: 65638
last_modified: 2010-01-01T18:01:39Z
completion: 25%
direction: unknown
sample_status: present
categories: ['Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:FCYTArchitectureNAV', 'Template:Short', 'Template:Float', 'Template:A string', 'Template:Int', 'Template:U string', 'Template:Byte', 'Template:25%']
---

# FCYT03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Object Operand Count |
| FLOAT | complexity |
| A_STRING | STF File |
| INT | String spacer |
| A_STRING | STF Name |
| U_STRING | Custom Name |
| INT | ?volume? |
| SHORT | ?customization? |
| INT | ?compcustlistsize? |
| INT | ?compcustlistupdcount? |
| INT | ?opt bitmask? |
| INT | ?? |
| INT | ?? |
| INT | content of crate |
| INT | ?? |
| INT | ?condition? |
| BYTE | ?flag? |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **25%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
62 BA 03 B5 10 00 00 00  //ID
54 59 43 46 03           // TYCF 3
C7 00 00 00 
0B 00 00 00 
80 42 
09 00                      // String count
66 61 63 74 6F 72 79 5F 6E // factory_n
00 00 00 00 
0B 00                            // String count
61 72 6D 6F 72 5F 63 72 61 74 65 // armor_crate
41 00 00 00                                      // U-String count
50 00 65 00 72 00 73 00                          // P.e.r.s.
6F 00 6E 00 61 00 6C 00 20 00 53 00 68 00 69 00  // o.n.a.l. .S.h.i.
65 00 6C 00 64 00 20 00 47 00 65 00 6E 00 65 00  // e.l.d. .G.e.n.e.
72 00 61 00 74 00 6F 00 72 00 20 00 49 00 6D 00  // r.a.t.o.r. .I.m.
70 00 65 00 72 00 69 00 61 00 6C 00 20 00 54 00  // p.e.r.i.a.l. .T.
65 00 73 00 74 00 20 00 50 00 72 00 6F 00 74 00  // e.s.t. .P.r.o.t.
6F 00 74 00 79 00 70 00 65 00 20 00 5B 00 4A 00  // o.t.y.p.e. .[.J.
65 00 64 00 69 00 20 00 46 00 65 00 6E 00 64 00  // e.d.i. .F.e.n.d.
65 00 72 00 20 00 32 00 5D 00                    // e.r. .2.]
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 21 
00 00 01 00 
00 00 00 00 
00 00 64 00 
00 00 01 39
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 25% Complete