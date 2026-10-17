---
title: CmdStartScene
url: https://wiki.swganh.org/index.php/CmdStartScene
page_type: Server Packet
opcode: 3AE6DFAE
revision_id: 21052
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:Long', 'Template:A string', 'Template:Float', 'Template:ServerPacket', 'Template:100%']
---

# CmdStartScene

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| BYTE | IgnoreLayoutFiles_Flag |
| LONG | CharID |
| A_STRING | TerrainMap |
| FLOAT | X-Coordinate |
| FLOAT | Z-Coordinate |
| FLOAT | Y-Coordinate |
| A_STRING | Shared_Race_Template |
| LONG | Galactic_Time |

## Variable Descriptions
- Operand_Count	     = 8
- Opcode		     = 3AE6DFAE

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
08 00       // Op Count
AE DF E6 3A // CmdStartScene
00          // IgnoreLayoutFiles_Flag 00/01
D2 CD 31 6E 0C 00 00 00 // Object ID
14 00                               // string count
74 65 72 72 61 69 6E 2F             // terrain/
74 61 74 6F 6F 69 6E 65 2E 74 72 6E // tatooine.trn
9A 36 67 C5 // -3699.41
90 97 9F 3E // 0.31
75 D9 9E C5 // -5083.18
26 D1 41 40 //<--CU/NGE thing crashes pre-CU
2C 00                                                 // string count
6F 62 6A 65 63 74 2F 63 72 65 61 74 75 72 65 2F 70 6C // object/creature/pl
61 79 65 72 2F 73 68 61 72 65 64 5F 68 75 6D 61       // ayer/shared_huma
6E 5F 6D 61 6C 65 2E 69 66 66                         // n_male.iff
75 5E 28 06 00 00 00 00                               // Galaxy Time
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete