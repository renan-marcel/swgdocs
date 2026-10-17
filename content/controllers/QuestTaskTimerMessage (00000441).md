---
title: QuestTaskTimerMessage (00000441)
url: https://wiki.swganh.org/index.php/QuestTaskTimerMessage_%2800000441%29
page_type: Object Controller
opcode: 00000441
revision_id: 21676
last_modified: 2008-01-10T15:24:19Z
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:Long', 'Template:A string', 'Template:U string', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# QuestTaskTimerMessage (00000441)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | ObjController |
| INT | ?? |
| INT | QuestTaskTimerMessage |
| LONG | Character ID |
| INT | ?? |
| A_STRING | Mission STF Name |
| INT | ?? |
| U_STRING | Note 1 |
| INT | ?? |
| INT | ?? |

## Variable Descriptions
- controllerID	     = 00000441

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
46 5E CE 80 // ObjControllerMessage
0B 00 00 00 
41 04 00 00 // QuestTaskTimerMessage
D2 CD 31 6E 0C 00 00 00 // Character ID
00 00 00 00 
21 00                                            // string count
71 75 65 73 74 2F 65 70 33 5F 74 72 61           // quest/ep3_tra
6E 64 6F 5F 68 73 73 69 73 73 6B 5F 7A 73 73 69  // ndo_hssissk_zssi
6B 5F 31 30                                      // k_10
01 00 00 00 
22 00 00 00 // u-string count
71 00 75 00 // q.u.
65 00 73 00 74 00 2F 00 67 00 72 00 6F 00 75 00        e.s.t./.g.r.o.u.
6E 00 64 00 71 00 75 00 65 00 73 00 74 00 73 00        n.d.q.u.e.s.t.s.
3A 00 64 00 65 00 73 00 74 00 72 00 6F 00 79 00        :.d.e.s.t.r.o.y.
5F 00 63 00 6F 00 75 00 6E 00 74 00 65 00 72 00        _.c.o.u.n.t.e.r.
00 00 00 00 
01 00 00 00 


05 00 
46 5E CE 80 // ObjControllerMessage
0B 00 00 00 
41 04 00 00 // QuestTaskTimerMessage
D2 CD 31 6E 0C 00 00 00 // Character ID
00 00 00 00 
19 00                                     // string count
71 75 65 73 74 2F 73 6F 6D 5F 78          // quest/som_x
61 6E 64 61 6E 6B 5F 74 72 6F 70 68 65 79 // andank_trophey..
06 00 00 00 
22 00 00 00                                      // u-string count
71 00 75 00 65 00 73 00 74 00                    // q.u.e.s.t.
2F 00 67 00 72 00 6F 00 75 00 6E 00 64 00 71 00  // /.g.r.o.u.n.d.q.
75 00 65 00 73 00 74 00 73 00 3A 00 64 00 65 00  // u.e.s.t.s.:.d.e.
73 00 74 00 72 00 6F 00 79 00 5F 00 63 00 6F 00  // s.t.r.o.y._.c.o.
75 00 6E 00 74 00 65 00 72 00                    // u.n.t.e.r.
00 00 00 00 
06 00 00 00 
 

05 00 
46 5E CE 80 // ObjControllerMessage
0B 00 00 00 
41 04 00 00 // QuestTaskTimerMessage
D2 CD 31 6E 0C 00 00 00 // Character ID
00 00 00 00 
19 00                                              // string count
71 75 65 73 74 2F 73 6F 6D 5F 78 61 6E 64 61 6E 6B // quest/som_xandank
5F 68 75 6E 74 5F 32 35                            // _hunt_25
01 00 00 00 
22 00 00 00                                      // u-string count
71 00 75 00 65 00 73 00 74 00 2F 00 67 00 72 00  // q.u.e.s.t./.g.r.
6F 00 75 00 6E 00 64 00 71 00 75 00 65 00 73 00  // o.u.n.d.q.u.e.s.
74 00 73 00 3A 00 64 00 65 00 73 00 74 00 72 00  // t.s.:.d.e.s.t.r.
6F 00 79 00 5F 00 63 00 6F 00 75 00 6E 00 74 00  // o.y._.c.o.u.n.t.
65 00 72 00                                      // e.r.
00 00 00 00 
19 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 50% Complete