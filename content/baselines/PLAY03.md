---
title: PLAY03
url: https://wiki.swganh.org/index.php/PLAY03
page_type: Baseline
opcode: 
revision_id: 257271
last_modified: 2014-01-27T20:54:13Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:PLAYArchitectureNAV', 'Template:100%']
---

# PLAY03

## Notices
_none_

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
| INT | GenericInt(NotUsed) |
| INT | MyFlagsList |
| INT | FlagBitmask |
| INT | MyProfileList |
| INT | ProfileBitmask |
| ASTRING | ProfessionTag |
| INT | BornDate |
| INT | TotalPlayTime |

## Variable Descriptions
- ObjectOpperandCount = 10

## Notes
- **NOTE:** The 4 integers get sent from the client when a change is made to their profile.

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
======================Xenos break======================================
0A 00
00 00 80 3F //Complexity

0F 00 // string count
73 74 72 69 6E 67 5F 69 64 5F 74 61 62 6C 65 // string_id_table
00 00 00 00 // string spacer
00 00
00 00 00 00 //CustomName
00 00 00 00 //Volume
00 00 00 00 //GenericINT(not used with PLAY)
04 00 00 00 //MyFlags (find possible values!)
00 00 00 00
00 00 00 00
00 00 00 00
00 00 00 00
04 00 00 00 //MyProfile (make chart of values!)
07 07 04 00
01 00 00 20
00 08 00 00
00 10 02 00
00 00 //Profession Tag
00 00 00 00 //BornDate (single integer.. not processed. might need to add xx/yy/zz format in .exe)
00 00 00 00 //TotalPlayTime (update every 30 seconds, count in seconds, displayed in seconds, client updates itself too).

MyFlags
[INT1]
1 - LFG(can combine with HELPER)
2 - HELPER(can combine with LFG)
4 - ROLEPLAYER (no tag)
80 - AFK (overrides previous tags)
100 - LD (overrides other tags)
200 - Faction Rank(seperate tag)

[INT4]
80000000 - Anonymous (no tag)

MyProfile
Large List.. you will need to clear your players cache from the client to get this to display.
It saves based on what the client sets, and then caches it only sending the values to the server.
Even if the server sends new ones, the client wont display (because it is relying on the cache)

===========Rouse breaks of nge packets
05 00 
53 21 86 12 // DeltaMessage
9C 97 9A 8F 25 00 00 00  // ID
59 41 4C 50 03 //  YALP 3
08 00 00 00 
01 00 09 00 
4A 01 00 
00 1C
=======================================

05 00 
0C 5F A7 68  // BaselineMessage
EB 28 50 B0 24 00 00 00 // ID
59 41 4C 50 03 // YALP 3
87 00 00 00 
10 00 00 00 
80 3F 
0F 00 // string count
73 74 72 69 6E 67 5F 69 64 5F 74 61 62 6C 65 // string_id_table
00 00 00 00 // string spacer
00 00
00 00 00 00 //CustomName
00 00 00 00 //Volume
00 00 00 00 //GenericINT(not used with PLAY)
04 00 00 00 //MyFlags (see above chart)
00 00 00 00 
00 00 00 00
00 00 00 00 
00 00 00 00 
04 00 00 00 //MyProfile 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 
92 08 00 00   
D6 70 04 00 
4B 00 00 00 
12 00               // string count
66 6F 72 63 65 5F   // force_
73 65 6E 73 69 74 69 76 65 5F 31 61 // sensitive_1a
5D 82 00 00
00 00 00 00 
88 C2 01 00 
00 00 00 00 
01 00 00 00      
49

=========== cAble @ projectswg's Play3Delta NGE Packet Break ===============

0x05, 0x00, #Update Type
0x53, 0x21, 0x86, 0x12, #Deltas Opcode
0xBF, 0xEE, 0x46, 0x3E, 0x33, 0x00, 0x00, 0x00, #Play ObjectID
0x59, 0x41, 0x4c, 0x50, 0x03, #Play03
0x08, 0x00, 
0x00, 0x00, 
0x01, 0x00, 
0x09, 0x00, #Delta variable for updating total time played
0x76, 0x4C, 0x62, 0x00, #TotalTimePlayed 74days13hours
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete