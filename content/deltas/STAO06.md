---
title: STAO06
url: https://wiki.swganh.org/index.php/STAO06
page_type: Baseline
opcode: 
revision_id: 51744
last_modified: 2009-03-18T15:09:29Z
completion: 50%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:STAOArchitectureNAV', 'Template:50%', 'Template:ServerPacket']
---

# STAO06

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | ServerID |

## Variable Descriptions
- OpperandCount = 1

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68 //baseline
20 34 E9 FF FF FF DF FB //objid
4F 41 54 53 06 //STAO6
1D 00 00 00 
02 00 
68 00 00 00 
0F 00 73 74 72 69 6E 67 5F 69 64 5F 74 61 62 6C 65 //string_id_table
00 00 00 00 
00 00 //empty string


05 00 
0C 5F A7 68 //baseline
FC FF FF FF FF FF DF FB //objid
4F 41 54 53 06 //STAO6
27 00 00 00 
02 00 
68 00 00 00 
0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 //string_table
00 00 00 00 
0D 00 70 72 69 73 74 69 6E 65 20 77 61 6C 6C //pristine wall

05 00 
0C 5F A7 68 //baseline
A1 FF FF FF FF FF DF FB //objid
4F 41 54 53 06 //STAO6
24 00 00 00 
02 00 
68 00 00 00 
0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 //string_table
00 00 00 00 
0A 00 47 72 61 76 65 73 74 6F 6E 65 //Gravestone

05 00 
0C 5F A7 68 //baseline
E5 FF FF FF FF FF 59 FC //objid
4F 41 54 53 06 //STAO6
25 00 00 00 
02 00 
5A 00 00 00 
0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 //string_table
00 00 00 00 
0B 00 4D 65 64 69 75 6D 20 54 65 6E 74 //Medium Tent


05 00 
0C 5F A7 68 //baseline
52 01 6F 90 1F 00 00 00 //objid
4F 41 54 53 06 
26 00 00 00 
02 00 
6B 00 00 00 
0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 //string_table
00 00 00 00 
0C 00 73 6F 75 6E 64 5F 6F 62 6A 65 63 74 //sound_object

05 00 
0C 5F A7 68 //baseline
1C DD 63 F1 FF FF B5 FC //objid
4F 41 54 53 06 //STAO6
33 00 00 00 
02 00 
43 00 00 00 
0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 //string_table
00 00 00 00 
19 00 4A 61 77 61 20 45 78 70 6F 20 54 65 6E 74 20 30 31 20 2D 20 53 6D 61 6C 6C //Jawa Expo Tent 01 - Small

 05 00 0C 5F A7 68 DB E8 19 9A FF FF 09 FC 4F 41 54 53 06 29 00 00 00 02 00 51 00 00 00 0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 00 00 00 00 0F 00 6D 69 6C 69 74 61 72 79 20 63 6F 6C 75 6D 6E 
..._.h........OATS.).....Q.....string_table......military.column

 05 00 0C 5F A7 68 96 68 68 CF FF FF B5 FC 4F 41 54 53 06 2A 00 00 00 02 00 7C 00 00 00 0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 00 00 00 00 10 00 44 65 61 74 68 73 74 61 72 20 44 65 62 72 69 73 
..._.h.hh.....OATS.*.....|.....string_table......Deathstar.Debris

05 00 0C 5F A7 68 D0 9D 07 E6 FF FF B5 FC 4F 41 54 53 06 1E 00 00 00 02 00 46 00 00 00 0C 00 73 74 72 69 6E 67 5F 74 61 62 6C 65 00 00 00 00 04 00 69 74 65 6D 
..._.h........OATS.......F.....string_table......item

baseline:STAO6 05 00 0C 5F A7 68 5B F1 8D AF 22 00 00 00 4F 41 54 53 06 22 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 14 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6C 67 5F 64 
..._.h[..."...OATS.".....H...........mun_decal_blast_lg_d

baseline:STAO6 05 00 0C 5F A7 68 5C F1 8D AF 22 00 00 00 4F 41 54 53 06 24 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 16 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6D 61 69 6E 5F 64 
..._.h\..."...OATS.$.....H...........mun_decal_blast_main_d

baseline:STAO6 05 00 0C 5F A7 68 11 F2 8D AF 22 00 00 00 4F 41 54 53 06 22 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 14 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6C 67 5F 64 
..._.h...."...OATS.".....H...........mun_decal_blast_lg_d

baseline:STAO6 05 00 0C 5F A7 68 12 F2 8D AF 22 00 00 00 4F 41 54 53 06 22 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 14 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6C 67 5F 64 
..._.h...."...OATS.".....H...........mun_decal_blast_lg_d

baseline:STAO6 05 00 0C 5F A7 68 AC F2 8D AF 22 00 00 00 4F 41 54 53 06 22 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 14 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6C 67 5F 64 
..._.h...."...OATS.".....H...........mun_decal_blast_lg_d

baseline:STAO6 05 00 0C 5F A7 68 04 F3 8D AF 22 00 00 00 4F 41 54 53 06 24 00 00 00 02 00 48 00 00 00 00 00 00 00 00 00 16 00 6D 75 6E 5F 64 65 63 61 6C 5F 62 6C 61 73 74 5F 6D 61 69 6E 5F 64 
..._.h...."...OATS.$.....H...........mun_decal_blast_main_d
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete