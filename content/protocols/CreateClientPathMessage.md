---
title: CreateClientPathMessage
url: https://wiki.swganh.org/index.php/CreateClientPathMessage
page_type: Server Packet
opcode: 71957628
revision_id: 42412
last_modified: 2008-07-16T01:33:07Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Beginlist', 'Template:Endlist', 'Template:ServerPacket', 'Template:100%']
---

# CreateClientPathMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | Coordinates Count |

## Variable Descriptions
- Operand_Count	     = 5
- Opcode		     = 71957628

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 
28 76 95 71  // CreateClientPathMessage

0B 00 00 00 
60 75 A2 45  // 5198.67
00 00 00 00 
5D 97 D0 45  // 6674.92

BE 6A A2 45  // 5197.34
00 00 00 00  
CC 14 D0 45  // 6658.60

E9 77 A2 45  // 5198.99 
00 00 00 00 
2B 88 CF 45  // 6641.02

57 86 A2 45  // 5200.79
00 00 00 00 
B5 FB CE 45  // 6623.46

FF D5 A2 45  // 5210.75
00 00 00 00 
79 A4 CE 45  // 6612.56

1D 05 A3 45  // 5216.64
00 00 00 00 
20 46 CE 45  // 6600.77

4A A5 A3 45  // 5236.66
00 00 00 00 
88 D5 CD 45  // 6586.69

F7 53 A4 45  // 5258.50
00 00 00 00 
45 A1 CD 45  // 6580.16

36 C6 A4 45  // 5272.78
00 00 00 00 
81 A5 CD 45  // 6580.69

35 82 A5 45  // 5296.28
00 00 00 00 
78 C5 CD 45  // 6584.68

6C 7C A6 45  // 5327.55
00 00 00 00 
00 69 CD 45  // 6573.13

01 E6 DA
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete