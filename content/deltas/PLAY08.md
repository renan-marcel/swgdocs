---
title: PLAY08
url: https://wiki.swganh.org/index.php/PLAY08
page_type: Baseline
opcode: 
revision_id: 79171
last_modified: 2011-09-11T12:59:52Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:PLAYArchitectureNAV', 'Template:100%']
---

# PLAY08

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | XPListSize |
| INT | XPListUpdateCounter |
| BYTE |  |
| ASTRING | XPType |
| INT | XPValue |
| INT | WaypointListSize |
| INT | WaypointListUpdateCounter |
| BYTE | DeltaByte(00) |
| LONG | WaypointObjectID |
| INT | CellID |
| FLOAT | XCoord |
| FLOAT | ZCoord |
| FLOAT | YCoord |
| LONG | LocationNetworkId |
| INT | PlanetCRC |
| USTRING | WaypointName |
| LONG | WaypointObjectID |
| BYTE | Color |
| BYTE | ActiveFlag |
| INT | CurrentForcePower |
| INT | MaxForcePower |
| INT | CurrentFSQuestList |
| INT | UpdateCounter |
| BYTE | CurrentFSQuestMask |
| INT | CompletedFSQuestList |
| INT | UpdateCounter |
| BYTE | CompletedFSQuestMask |
| INT | QuestJournalList |
| INT | UpdateCounter |
| BYTE | DeltaByte(00) |
| INT | QuestCRC |
| LONG | OwnerID |
| SHORT | ActiveStepBitmask |
| SHORT | CompletedStepBitmask |
| BYTE | CompletedFlag |
| INT | QuestCounter |

## Variable Descriptions
- OpperandCount = 7

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
07 00
//================================XPList
03 00 00 00 //ListSize
00 00 00 00 //UpdateCounter

00 //Delta Padding  01 - remove, 00 - set, 02 - set (not intended to be used.. same as 00)
0E 00                                      // string count
63 6F 6D 62 61 74 5F 67 65 6E 65 72 61 6C  // combat_general
64 00 00 00 //Value (Ammount of XP)
00 // Delta Padding
05 00          // string count
73 63 6F 75 74 // scout
A3 1C 00 00 // amount of xp 7331
00 // Delta Padding
0C 00                               // sting count
75 6E 6F 62 74 61 69 6E 61 62 6C 65 // unobtainable
39 05 00 00 // amount of xp 1337

//=============================Waypoint List
01 00 00 00 // List Size
00 00 00 00 // Update Counter
00 // Delta Padding
AA BB 66 99 0A 00 00 00 // (waypoint object ID)
00 00 00 00  // ??(JTL?)
26 78 32 C3  // (FLOAT:X CORD)
00 00 E0 41  // (FLOAT:Z CORD)
6B 87 97 C5  // (FLOAT:Y CORD)
00 00 00 00  // ??(JTL?)
00 00 00 00  // ??(JTL?)
58 B5 D7 AF  // PlanetCRC
13 00 00 00  // u-string count
53 00 57 00 47 00 45 00 6D 00 75 00 27 00 73 00 20 00 46 00
69 00 72 00 73 00 74 00 20 00 53 00 74 00 65 00 70 00 // S W G E m u ' s   F i r s t   S t e p
AA BB 66 99 0A 00 00 00 //(Waypoint Object ID. again.)
01   //(BYTE: Color) (1 - blue, 2 - green, 3 - orange, 4 - yellow, 5 -purple/red, 6- white, 7 -JTL)
01   // (BYTE: activated flag)
00 00 00 00 // Current Force
00 00 00 00 // Max Force
05 00 00 00 // CurrentFSQuestMask
00 00 00 00
00 00 00 00
00
05 00 00 00  // CompletedFSQuestMask
00 00 00 00
00 00 00 00
00
01 00 00 00  // RegularQuestJournal
00 00 00 00
00  //Unused in ASM.. Might be leftover for a delta or something that they botched.
92 9B 44 C5 // QuestCRC
15 A8 0A 56 03 00 00 00 // Owner/Character ID? Not Used either really.
04 00 // ActiveBitMask For which parts of the quest you have
01 00 // CompletedBitMask For which parts of the quest you completed
00    // CompletedFlag For completing the entire quest and its parts
01 00 00 00 // ? no idea, some sort of counter, default value gets incremented with each
           // new quest. Individual Quest Counter?
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete