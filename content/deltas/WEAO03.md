---
title: WEAO03
url: https://wiki.swganh.org/index.php/WEAO03
page_type: BaseLine
opcode: 
revision_id: 21414
last_modified: 
completion: 25%
direction: S→C
sample_status: present
categories: ['Packets', '25% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:WEAOArchitectureNAV', 'Template:25%', 'Template:ServerPacket']
---

# WEAO03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
_none_

## Variable Descriptions
- Obj_OperandCount =

## Notes
_none_

## Tags
- **25%** - This packet has been partially reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
B8 59 90 19 17 00 00 00 // Weapon ID
4F 41 45 57 03          // OAEW 3
62 00 00 00 
11 00 00 00 
00 00 
0B 00                            // String Count
77 65 61 70 6F 6E 5F 6E 61 6D 65 // weapon_name
00 00 00 00 
0E 00                                     // String Count
64 65 66 61 75 6C 74 5F 77 65 61 70 6F 6E // default_weapon
00 00 00 00 
01 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 01 
00 00 00 00 
00 00 00 00 
00 00 E8 03 // condition DMG
00 00 01 0A // Max Condition
00 00 00 00 
00 00 00 
00 00 A0 40 
01 00 00 00
00 00 00 00 
00 00 00 00 

--------------------------------------------------------
05 00 
0C 5F A7 68 
66 D3 29 6B 13 00 00 00 // ID
4F 41 45 57 03 // OAEW 3
AB 00 00 00
14 00 00 00 
40 42 

0B 00                            // string count
77 65 61 70 6F 6E 5F 6E 61 6D 65 // weapon_name (stf_file)
00 00 00 00                      // string spacer
0B 00                            // string count
72 69 66 6C 65 5F 6C 61 73 65 72 // rifle_laser (stf_name)

1A 00 00 00                                     // u-string count 
4B 00 72 00 61 00 79 00                         // K.r.a.y.  ---------------|
74 00 20 00 41 00 64 00 76 00 61 00 6E 00 63 00 // t...A.d.v.a.n.c. (custom |
65 00 64 00 20 00 4C 00 61 00 73 00 65 00 72 00 // e.d...L.a.s.e.r.  name)  |
20 00 52 00 69 00 66 00 6C 00 65 00             // R.i.f.l.e.  -------------|
01 00 00 00
00 00 00 00 
00 00 00 00 
00 00 
03 00 00 00 
00 00 00 00 
F0 CA 09 25 
ED E3 B4 49 
53 5E CD 49 
00 20 00 00 
00 00 00 00 
1D 00 00 00 
78 03 00 00 
01 CD CC 4C 
3F 06 00 00 
00 00 00 00 
00 00 00 80 
42 02 00 00 
00 00 00 00 
00 00 00 00 
00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 25% Complete | Server Packets