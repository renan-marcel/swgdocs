---
title: BUIO03
url: https://wiki.swganh.org/index.php/BUIO03
page_type: Baseline
opcode: 
revision_id: 257262
last_modified: 2014-01-21T23:16:38Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', '100% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:BUIOArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:A string', 'Template:U string', 'Template:100%', 'Template:ServerPacket']
---

# BUIO03

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Baseline Opcode |
| LONG | Object ID |
| INT | OIUB |
| BYTE | 3 |
| INT | Length of remaining packet |
| SHORT | ?? |
| A_STRING | Building STF File |
| INT | STF Spacer |
| A_STRING | Building STF Name |
| U_STRING | Custom Name |
| INT | Volume |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| SHORT | ?? |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
56 33 23 6F 02 00 00 00  // ID
4F 49 55 42 03           // OIUB 3
0B 00 00 00 
00 00 
05 00           // String count
70 6F 69 5F 6E  // poi_n
00 00 00 00 
11 00                                                // String count
62 61 73 65 5F 70 6F 69 5F 62 75 69 6C 64 69 6E 67   // base_poi_building.
0D 00 00 00                                          // U-String count
55 00 73 00 73 00 79 00 6E 00 6F 00 27               // U.s.s.y.n.o.'
00 73 00 20 00 43 00 61 00 6D 00 70 00 64 00         // .s. .C.a.m.p.d
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 01 00 00 
00 00 00 00 
00 00 00 00 
E8 03 00 00 
00 21
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete | Server Packets