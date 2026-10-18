---
title: MINO03
url: https://wiki.swganh.org/index.php/MINO03
page_type: Baseline
opcode: 
revision_id: 21707
last_modified: 
completion: 25%
direction: unknown
sample_status: present
categories: ['Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:MINOArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:Float', 'Template:A string', 'Template:U string', 'Template:25%']
---

# MINO03

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Baseline Opcode |
| LONG | Installation ID |
| INT | ONIM |
| BYTE | 3 |
| SHORT | ?? |
| FLOAT | ?? |
| A_STRING | STF File |
| INT | String Spacer |
| A_STRING | STF Name |
| U_STRING | Custom Name |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | Max Condition |
| INT | ?? |
| INT | ?? |
| INT | ?? |

## Variable Descriptions
- Obj_OperandCount =

## Notes
_none_

## Tags
- **25%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
52 9F 65 46 00 00 00 00  // Instulation ID
4F 4E 49 4D // ONIM
03          // 3
0E 00 
00 00 80 3F 
0E 00                                       // String count
69 6E 73 74 61 6C 6C 61 74 69 6F 6E 5F 6E   // installation_n
00 00 00 00                                 // string spacer
0C 00                                       // String count
69 74 65 6D 5F 66 61 63 74 6F 72 79         // item_factory
10 00 00 00                                 // u-String count
4B 00 61 00 6D 00 4B 00 61 00 6D 00         // K.a.m.K.a.m.
20 00 46 00 61 00 63 00 74 00 6F 00 72 00   // F.a.c.t.o.r.
79 00 20 00 49 00                           // y. .I
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 01 01 
00 00 00 00 
00 00 00 00 
00 00 E8 03 // max condition
00 00 01 01 
96 22 41 46 
00 00 48 42
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 25% Complete