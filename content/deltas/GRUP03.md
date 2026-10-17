---
title: GRUP03
url: https://wiki.swganh.org/index.php/GRUP03
page_type: Baseline
opcode: 
revision_id: 39716
last_modified: 2008-06-25T17:34:28Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', '100% Complete', 'Server Packets']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:GRUPArchitectureNAV', 'Template:100%', 'Template:ServerPacket']
---

# GRUP03

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| FLOAT | Complexity |
| ASTRING | STF File |
| INT | STF Spacer |
| ASTRING | STF Name |
| USTRING | CustomName |
| INT | Volume |

## Variable Descriptions
- Obj_OperandCount = 4

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselineMessage
65 EE 47 95 25 00 00 00  // Group ID
50 55 52 47 03           // PURG 3
25 00 00 00 
04 00 
00 00 80 3F 
0F 00                    // string count
73 74 72 69 6E 67 5F 69  // string_i
64 5F 74 61 62 6C 65     // d_table
00 00 00 00 
00 00 00 00 
00 00 00 00 
00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | 100% Complete | Server Packets