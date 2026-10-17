---
title: STAO03
url: https://wiki.swganh.org/index.php/STAO03
page_type: Baseline
opcode: 
revision_id: 39708
last_modified: 2008-06-25T17:26:34Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', '100% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:STAOArchitectureNAV', 'Template:100%', 'Template:ServerPacket']
---

# STAO03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| FLOAT | Complexity |
| ASTRING | STF File(Table) |
| INT | STF Spacer |
| ASTRING | STF Name(ID) |
| USTRING | CustomName |
| INT | Volume |

## Variable Descriptions
- ObjectOpperandCount = 4

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
B2 53 90 19 17 00 00 00  // ID
4F 41 54 53 03           // OATS 3
29 00 00 00 
04 00 00 00 
00 00 
05 00          // String count
6F 62 6A 5F 6E // obj_n
00 00 00 00 
0E 00                                     // String count
75 6E 6B 6E 6F 77 6E 5F 6F 62 6A 65 63 74 // unknown_object
00 00 00 00 
FF 00 
00 00 3E
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete | Server Packets