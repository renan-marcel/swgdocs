---
title: ClientRandomNameResponse
url: https://wiki.swganh.org/index.php/ClientRandomNameResponse
page_type: Server Packet
opcode: E85FB868
revision_id: 21689
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ClientRandomNameResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | Player_Race_IFF |
| U_STRING | RandomName |
| A_STRING | STFFile |
| INT | String spacer |
| A_STRING | Approval_String |

## Variable Descriptions
- Op Count	     = 4
- Opcode		     = E85FB868

## Notes
- **NOTE:** Not to be confused with creature objects, or any other object types.
- **NOTE:** must be "name_approved" for generated name to take.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00       // Op Count
68 B8 5F E8 // ClientRandomNameResponse
25 00                                     // string count
6F 62 6A 65 63 74 2F                      // object/
63 72 65 61 74 75 72 65 2F                // creature/
70 6C 61 79 65 72 2F                      // player/
68 75 6D 61 6E 5F 6D 61 6C 65 2E 69 66 66 // human_male.iff
11 00 00 00                         // u-string count
4E 00 65 00 61 00 73 00 63 00 65    // N.e.a.s.c.e
00 75 00 72 00 65 00 20 00          // .u.r.e. .
45 00 67 00 65 00 73 00 61 00 63 00 65 00        E.g.e.s.a.c.e.
02 00 // string count
75 69 // ui
00 00 00 00 // string spacer
0D 00 // string count
6E 61 6D 65 5F 61 70 70 72 6F 76 65 64 // name_approved
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete