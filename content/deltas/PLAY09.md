---
title: PLAY09
url: https://wiki.swganh.org/index.php/PLAY09
page_type: Baseline
opcode: 
revision_id: 257270
last_modified: 2014-01-27T17:03:06Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:PLAYArchitectureNAV', 'Template:100%']
---

# PLAY09

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | AbilityListSize |
| INT | UpdateCounter |
| ASTRING | AbilityString |
| INT | ExperimentationFlag |
| INT | CraftingStage |
| LONG | NearestCraftingStationID |
| INT | DraftSchematicList |
| INT | UpdateCounter |
| INT | ServerSchematicCRC |
| INT | SchematicCRC |
| INT | ExperimentationPoints |
| INT | AccomplishmentCounter |
| INT | FriendList |
| INT | UpdateCounter |
| ASTRING | FriendName |
| INT | IgnoreList |
| INT | UpdateCounter |
| ASTRING | IgnoreName |
| INT | CurrentLanguageID |
| INT | CurrentStomach |
| INT | MaxStomach |
| INT | CurrentDrink |
| INT | MaxDrink |
| INT | CurrentConsumable(NotUsed) |
| INT | MaxConsumable(NotUsed) |
| INT | UnusedWaypointList |
| INT | UpdateCounter |
| BYTE | DeltaByte(00) |
| LONG | WaypointObjectID |
| INT | CellID |
| FLOAT | XCoord |
| FLOAT | ZCoord |
| FLOAT | YCoord |
| LONG | LocationNetworkID |
| INT | PlanetCRC |
| USTRING | WaypointName |
| LONG | WaypointObjectID |
| BYTE | Color |
| BYTE | ActiveFlag |
| INT | JediState |

## Variable Descriptions
- OpperandCount = 17

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 0D #DataFrag
03 2A #Sequence
00 00 04 AF #TotalPacketSize
05 00 #Operand
0C 5F A7 68 #BaselinesMessage
44 C8 59 45 04 00 00 00 #PlayID 
(this is unique for all PLAY and links to the character via UpdateContainmentMessage)
59 41 4C 50 09 #PLAY09



98 04 00 00 #Data size that follows


12 00 #opcode

00 00 00 00 

00 00 00 00 

00 00 00 00 

00 00 00 00 



0F 00 00 00 #Size
0F 00 00 00 # size again?
00 # Unk byte




####### useable Draft Schematics that a player can select from ########



A1 D4 09 04 #SchematicID
4F 56 B0 83 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_one_hand_gen1.iff
01 
00 00 00 00 


C9 12 2E 05 #SchematicID
7A 43 6F E8 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_training.iff
01
00 00 00 00 


2B 0F 02 13 #SchematicID
C5 8D BB 94 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_two_hand_gen1.iff
01 
00 00 00 00 


F8 AD 84 21 #SchematicID
9A 18 6A A1 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_polearm_gen2.iff
01 
00 00 00 00 


75 CA 89 68 #SchematicID
17 7F 67 E8 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_polearm_gen3.iff
01 
00 00 00 00 


AF 30 F0 6D #SchematicID
41 B2 49 EA #object/draft_schematic/weapon/lightsaber/shared_lightsaber_one_hand_gen4.iff
01 
00 00 00 00 


25 EB FB 7A #SchematicID
CB 69 42 FD #object/draft_schematic/weapon/lightsaber/shared_lightsaber_two_hand_gen4.iff
01 
00 00 00 00 


31 C0 18 81 #SchematicID
DF 42 A1 06 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_two_hand_gen3.iff
01 
00 00 00 00 


61 E1 6A 93 #SchematicID
03 54 84 13 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_polearm_gen4.iff
01 
00 00 00 00 

BB 1B 13 96 #SchematicID
55 99 AA 11 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_one_hand_gen3.iff
01 
00 00 00 00
 
79 40 F7 97 #SchematicID
06 93 DC DD #object/draft_schematic/item/shared_item_jedi_tool.iff
01 
00 00 00 00   

 
42 24 B3 C2 #SchematicID
AB 0E 31 85 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_refined_crystal_pack.iff
01 
00 00 00 00 


BC A7 15 C8 #SchematicID
52 25 AC 4F #object/draft_schematic/weapon/lightsaber/shared_lightsaber_two_hand_gen2.iff
01 
00 00 00 00 


36 7C 1E DF #SchematicID
D8 FE A7 58 #object/draft_schematic/weapon/lightsaber/shared_lightsaber_one_hand_gen2.iff
01 
00 00 00 00


6F 05 93 FA #SchematicID
0D B0 7D 7A #object/draft_schematic/weapon/lightsaber/shared_lightsaber_polearm_gen1.iff
01
00 00 00 00 

00 00 00 00 
00 00 
00 08 
00 00 00 00 
00 00 00 00

65 00 00 00 # Friends list Size

98 01 00 00 # update counter?



############## Friends and IGNORE list #################


06 00 
73 63 6F 6F 62 65 

04 00 
67 61 6E 74 

04 00 
63 68 61 76 

04 00 
6E 65 6F 27 

06 00
73 68 6F 67 75 6E 

05 00 
69 7A 6F 74 65 

05 00 
70 69 6C 61 72 

09 00 
70 72 6F 63 61 72 69 61 6E 

0E 00 
6F 63 74 61 76 69 61 6E 63 61 65 73 61 72 

07 00 
74 73 75 62 61 73 61 

07 00 
6D 61 73 61 2D 72 6F 

05 00 
6D 61 64 61 72 

04 00 
67 69 61 6E 

05 00
74 6F 73 68 69 

0C 00 
6E 75 6B 65 73 79 6F 75 72 6D 6F 6D 

0B 00 
6B 72 69 73 74 69 61 6E 69 75 73

0A 00 
6A 61 77 69 69 61 72 65 61 6E 


09 00 
62 61 72 74 61 6C 62 79 27 

06 00 
68 61 73 74 61 27 

05 00 
6A 61 76 69 6E 

0A 00 
63 73 72 5F 6A 61 73 6F 6E 70 

07 00 
68 69 6B 65 72 61 6E 

0E 00 
68 69 72 65 64 2D 61 73 73 61 73 73 69 6E 

09 00 #String Size
01 75 2B This rest of this name continues in the next datafragment after sequence (03 2B #Sequence)



############## Friends and IGNORE list  continues #################


00 0D #DatrFrag
03 2B #Sequence (Name date resumes after this)
76 61 6C 65 6E 74 69 6E 6F 05 00 6D
79 73 69 61 06 00 61 6C 6C 69 6F 73 05 00 6F 63
6B 69 6D 06 00 65 79 65 6F 77 6E 04 00 62 61 6E
65 07 00 74 79 67 72 65 73 73 07 00 64 72 61 65
6C 6F 76 05 00 6C 61 74 65 61 06 00 76 61 6C 6C
6F 72 04 00 6D 61 65 69 06 00 70 6F 6C 61 6E 64
05 00 68 61 73 74 61 09 00 6D 6F 75 72 6E 62 6C
61 64 08 00 72 61 79 6D 75 6E 64 6F 07 00 61 72
74 65 6F 75 73 09 00 74 68 65 2D 6A 6F 6B 65 72
05 00 72 65 78 6F 72 06 00 76 69 70 65 72 78 05
00 77 6F 61 64 61 0A 00 6E 65 72 6F 63 61 65 73
61 72 07 00 2D 68 69 72 65 64 2D 07 00 27 63 68
72 6F 67 72 06 00 61 73 68 65 6C 79 06 00 71 75
65 62 65 63 06 00 6F 61 64 72 61 73 07 00 6D 6F
72 64 72 69 73 08 00 7A 61 6E 7A 69 62 61 72 03
00 77 75 6E 08 00 72 6F 62 65 72 74 2D 6D 05 00
74 69 64 65 73 05 00 68 69 72 65 64 05 00 6C 6F
74 75 73 08 00 66 61 62 72 69 7A 69 6F 0B 00 69
6E 74 65 72 63 65 70 74 65 72 06 00 68 61 61 76
69 64 06 00 77 61 73 61 76 69 06 00 6B 61 65 7A
61 72 07 00 6C 75 63 69 61 74 68 05 00 64 6F 6D
61 71 05 00 73 6F 6E 6E 79 03 00 74 6F 6F 06 00
6E 61 63 68 6F 73 05 00 61 6E 6A 65 6C 04 00 64
6D 61 71 08 00 64 6F 6C 74 68 72 61 6E 06 00 6D
79 74 68 69 63 0A 00 76 6F 6F 68 65 64 72 61 73
68 05 00 64 65 76 6F 65 03 00 72 68 69 04 00 77
79 63 6B 04 00 70 65 65 67 05 00 61 6B 61 6C 65
0B 00 73 69 6C 76 65 72 6E 65 78 75 73 07 00 7A
79 69 70 6C 65 78 08 00 61 6E 61 63 6F 6E 64 61
09 00 6C 6F 72 64 64 65 61 74 68 06 00 73 74 61
62 62 79 04 00 62 61 6C 6C 04 00 62 61 01 54 4A




############## Friends and IGNORE list continues #################


00 0D 03 2C 61 6C 07 00 75 6E 6B 6E 6F 77 6E 06
00 6A 6F 2D 73 65 66 06 00 73 6D 65 72 66 79 0A
00 63 73 72 2D 6A 61 73 6F 6E 70 06 00 74 75 6C
6B 61 73 06 00 73 6E 61 70 70 79 0A 00 77 61 6C
6B 65 72 2D 62 6F 68 06 00 6A 6F 76 61 63 6B 05
00 6F 6D 6F 73 69 06 00 74 69 6D 6E 61 72 06 00
6E 65 69 6B 6B 61 0A 00 43 53 52 5F 4A 61 73 6F
6E 50 05 00 66 61 7A 65 72 07 00 70 72 61 69 64
65 6E 0A 00 61 67 65 6E 74 77 6F 72 6B 73 0B 00
74 68 65 67 72 65 61 74 72 61 79 08 00 64 72 61
67 6D 69 72 65 07 00 73 6F 75 6C 6D 61 6E 01 00
00 00 08 00 00 00 05 00 73 6B 65 65 74 


01 00 00 00 #language_basic_speak (INT)
2C 00 00 00 #Food
64 00 00 00 #max food
10 00 00 00 #Drink
64 00 00 00 #MaxDrink
00 00 00 00 #Meds
64 00 00 00 #MaxMeds 

#Unsure of data below

00 00 00 00 
00 00 00 00 
08 00 00 
00 01 DD DB

(Language) 

language_basic_speak	
language_rodian_speak	
language_trandoshan_speak
language_moncalamari_speak
language_wookiee_speak
language_bothan_speak
language_twilek_speak
language_zabrak_speak
language_lekku_speak
language_ithorian_speak
language_sullustan_speak
language_hutt_speak
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete