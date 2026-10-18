---
title: TANO03
url: https://wiki.swganh.org/index.php/TANO03
page_type: Baseline
opcode: 
revision_id: 79406
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', '100% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:TANOArchitectureNAV', 'Template:100%', 'Template:ServerPacket']
---

# TANO03

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| FLOAT | Complexity |
| ASTRING | STFName |
| INT | String Spacer |
| ASTRING | DefaultName |
| USTRING | CustomName |
| INT | Volume |
| CSTRING | Customization |
| INT | ComponentCustomizationListSize |
| INT | ComponentCustomizationUpdateCounter |
| INT | ComponentCustomizationCRC |
| INT | OptionsBitmask |
| INT | IncapTimer |
| INT | ConditionDamage |
| INT | MaxCondition |
| BYTE | Bool for static object |

## Variable Descriptions
- ObjectOpperandCount = 11

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68
1D 92 14 6D 02 00 00 00 // Object ID
4F 4E 41 54 03 // ONAT 3
0B 00 
00 00 80 3F // Complexity
06 00              // String count
69 74 65 6D 5F 6E  // item_n
00 00 00 00 // String spacer
11 00                                              // String count
64 65 66 61 75 6C 74 5F 66 75 72 6E 69 74 75 72 65 // default_furniture
13 00 00 00                                        // U-string count
45 00 71 00 75 00 75 00 6C 00 75 00 73 00          // E.q.u.u.l.u.s.
20 00 4E 00 65 00 6D 00 75 00 73 00 27 00 20 00    // .N.e.m.u.s.'. .
43 00 61 00 6D 00 70 00                            // C.a.m.p
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 01 
00 00 00 00 
00 00 00 00 
00 00 64 00 
00 00 01 21
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete | Server Packets