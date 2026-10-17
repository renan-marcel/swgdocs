---
title: MISO03
url: https://wiki.swganh.org/index.php/MISO03
page_type: Baseline
opcode: 
revision_id: 56484
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:MISOArchitectureNAV', 'Template:75%']
---

# MISO03

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Object Opperand Count |
| FLOAT | Complexity |
| ASTRING | STF Name(Table) |
| INT | STF Spacer |
| ASTRING | STF Name(ID) |
| USTRING | Custom Name |
| INT | Volume |
| INT | Generic Int(NotUsed) |
| INT | Difficulty Level |
| FLOAT | Start Coord X |
| FLOAT | Start Coord Z |
| FLOAT | Start Coord Y |
| LONG | Start Object ID |
| INT | Start Planet CRC |
| USTRING | Creator Name |
| INT | Credits Reward |
| FLOAT | Destination Coord X |
| FLOAT | Destination Coord Z |
| FLOAT | Destination Coord Y |
| LONG | Destination Object ID |
| INT | Destination Planet CRC |
| INT | Target Object Iff CRC |
| ASTRING | Mission Description STF |
| INT | STF Spacer |
| ASTRING | Mission Description |
| ASTRING | Mission TitleSTF |
| INT | STF Spacer |
| ASTRING | Mission Title |
| INT | Repeat Counter |
| INT | Mission Type CRC |
| ASTRING | Target Name |
| INT | ?? |
| FLOAT | Waypoint X Coord |
| FLOAT | Waypoint Z Coord |
| FLOAT | Waypoint Y Coord |
| LONG | Waypoint Target ID |
| INT | Waypoint Planet Crc |
| USTRING | Waypoint Name |
| LONG | Waypoint Object ID |
| BYTE | Color |
| BYTE | Active Flag |

## Variable Descriptions
- ObjectOpperandCount = 5

## Notes
_none_

## Tags
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68 
6F 14 B8 30 42 00 00 00 
4F 53 49 4D 03 17 01 00 00 11 00 
00 00 80 3F // complexity
16 00 
6D 69 73 73 69 6F 6E 2F 6D 69 73 73 69 6F 6E 5F 6F 62 6A 65 63 74 
00 00 00 00 
0F 00 
64 65 73 74 72 6F 79 5F 6D 69 73 73 69 6F 6E 
00 00 00 00 
00 00 00 00 
00 00 00 00 
01 00 00 00 // Volume
63 C6 F0 44 // start x
00 00 00 00 // start Y
2E FB 16 45 // Start Z
00 00 00 00 00 00 00 00 
58 B5 D7 AF // Planet CRC
03 00 00 00 
41 00 67 00 69 00 
38 00 00 00 
FC 25 A6 44 // x
00 00 00 00 // y
FE AF 26 45 // Z
00 00 00 00 00 00 00 00 
58 B5 D7 AF 
AB DB 91 E1 
24 00 
6D 69 73 73 69 6F 6E 2F 6D 69 73 73 69 6F 6E 5F 64 65 6C 69 76 65 72 5F 6E 65 75 74 72 61 6C 5F 65 61 73 79 
00 00 00 00 
03 00 
6D 38 64 24 00 6D 69 73 73 69 6F 6E 2F 6D 69 73 73 69 6F 6E 5F 64 65 6C 69 76 65 72 5F 6E 65 75 74 72 61 6C 5F 65 61 73 79 
00 00 00 00 
03 00 
6D 38 74 
AC 06 00 00 
C6 7E C2 E5 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 00 00 00 00 
00 00 00 00 
00 00 
70 14 B8 30 42 00 00 00 
01
00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete