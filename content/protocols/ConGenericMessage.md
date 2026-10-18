---
title: ConGenericMessage
url: https://wiki.swganh.org/index.php/ConGenericMessage
page_type: Server Packet
opcode: 8C5FC76
revision_id: 19874
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ConGenericMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| A_STRING | Message |
| INT | String Spacer |

## Variable Descriptions
- Operand_Count	     = 3
- Opcode		     = 8C5FC76

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 
76 FC C5 08                                      // ConGenericMessage
F9 00                                            // string count
5C 23 46 46                                      // ......v.....\#FF
30 30 30 30 47 72 65 65 74 69 6E 67 73 21 20 50  // 0000Greetings!.P
6C 65 61 73 65 20 62 65 20 61 77 61 72 65 20 74  // lease.be.aware.t
68 61 74 20 74 68 65 20 62 75 79 69 6E 67 20 6F  // hat.the.buying.o
72 20 73 65 6C 6C 69 6E 67 20 6F 66 20 69 6E 2D  // r.selling.of.in-
67 61 6D 65 20 63 72 65 64 69 74 73 20 69 73 20  // game.credits.is.
61 67 61 69 6E 73 74 20 74 68 65 20 53 74 61 72  // against.the.Star
20 57 61 72 73 20 47 61 6C 61 78 69 65 73 20 54  // .Wars.Galaxies.T
65 72 6D 73 20 6F 66 20 53 65 72 76 69 63 65 2E  // erms.of.Service.
20 41 6E 79 6F 6E 65 20 66 6F 75 6E 64 20 70 61  // .Anyone.found.pa
72 74 69 63 69 70 61 74 69 6E 67 20 69 6E 20 74  // rticipating.in.t
68 65 73 65 20 74 72 61 6E 73 61 63 74 69 6F 6E  // hese.transaction
73 20 77 69 6C 6C 20 62 65 20 68 61 72 73 68 6C  // s.will.be.harshl
79 20 70 75 6E 69 73 68 65 64 20 62 79 20 74 68  // y.punished.by.th
65 20 47 61 6C 61 63 74 69 63 20 43 72 65 64 69  // e.Galactic.Credi
74 20 43 6F 6D 6D 69 73 73 69 6F 6E 21 5C 23 46  // t.Commission!\#F
46 46 46 46 46 00 00 00 00                       // FFFFF.......
01 B6 83                                         // comp+crc
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete