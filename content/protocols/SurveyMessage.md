---
title: SurveyMessage
url: https://wiki.swganh.org/index.php/SurveyMessage
page_type: Server Packet
opcode: 877F79AC
revision_id: 21596
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Float', 'Template:ServerPacket', 'Template:100%']
---

# SurveyMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | Points |
| FLOAT | X Coord |
| FLOAT | Y Coord |
| FLOAT | Z Coord |
| FLOAT | % Ratio |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 877F79AC

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
AC 79 7F 87 // SurveyMessage
09 00 00 00 // points
(Point 1)
35 EC 3F C3 // x
00 00 00 00 // y
A6 FD 99 C5 // z
D9 AA 4A 3E // ratio
(Point 2) 
35 EC 3F C3 // x
00 00 00 00 // y
A6 FD 98 C5 // z
52 DD 50 3E // ratio
(Point 3) 
35 EC 3F C3 // x
00 00 00 00 // y
A6 FD 97 C5 // z
F2 CD 57 3E // ratio
(Point 4) 
35 EC 1F C3 // x
00 00 00 00 // y
A6 FD 99 C5 // z
10 DC 46 3E // ratio
(Point 5) 
35 EC 1F C3 // x
00 00 00 00 // y
A6 FD 98 C5 // z
FB B4 4D 3E // ratio
(Point 6) 
35 EC 1F C3 // x
00 00 00 00 // y
A6 FD 97 C5 // z
6B 61 55 3E // ratio
(Point 7) 
6A D8 FF C2 // x
00 00 00 00 // y
A6 FD 99 C5 // z
62 09 3F 3E // ratio
(Point 8) 
6A D8 FF C2 // x
00 00 00 00 // y
A6 FD 98 C5 // z
05 47 46 3E // ratio
(Point 9) 
6A D8 FF C2 // x
00 00 00 00 // y
A6 FD 97 C5 // z
84 66 4E 3E // ratio
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete