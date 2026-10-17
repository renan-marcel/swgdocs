---
title: PlayersNearYou (000001E7)
url: https://wiki.swganh.org/index.php/PlayersNearYou_%28000001E7%29
page_type: Server Packet
opcode: 000001E7
revision_id: 21229
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Unknown', 'Template:U string', 'Template:A string', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# PlayersNearYou (000001E7)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | player count |
| INT | Bitmask size / 4 |
| ?? | Flags Bitmask |
| U_STRING | Player Name |
| INT | Race ID |
| A_STRING | Region Name |
| A_STRING | Planet |
| A_STRING | Guild |
| A_STRING | Profession Title |

## Variable Descriptions
- controllerID	     = 000001E7

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
07 00 00 00  // player count

==================================

04 00 00 00 // bitmask counter
38 00 00 00 // bitmask
00 00 00 00                                
00 00 00 00 
00 00 00 00

0A 00 00 00 
53 00 65 00 6A 00 75 00 
6F 00 20 00 44 00 75 00  // Sejuo Dune  (player name)
6E 00 65 00
 
00 00 00 00 // race (human)

1E 00 
40 74 61 74 6F 6F 69 6E 
65 5F 72 65 67 69 6F 6E //@tatooine_region_names:bestine
5F 6E 61 6D 65 73 3A 62 
65 73 74 69 6E 65 

08 00 
74 61 74 6F 6F 69 6E 65 // tatooine

00 00 // no specified guild

00 00 // no specified title

===================================

04 00 00 00 // bitmask counter
38 00 00 00 // bitmask
00 00 00 00                                
00 00 00 00 
00 00 00 00 

07 00 00 00 
52 00 6F 00 75 00 20 00 // player name
42 00 6F 00 74 00                         

31 00 00 00 // race (Sullustan)

1E 00 
40 74 61 74 6F 6F 69 6E 
65 5F 72 65 67 69 6F 6E // region-name STF
5F 6E 61 6D 65 73 3A 62 
65 73 74 69 6E 65 

08 00 
74 61 74 6F 6F 69 6E 65  // tatooine

00 00 // no specified guild

00 00 // no specified title

====================================

04 00 00 00  // bitmask counter
38 00 00 00   // bitmask
00 00 00 00                               
00 00 00 00  
00 00 00 00 

0B 00 00 00  
6B 00 69 00 6C 00 6C 00
2D 00 63 00 72 00 69 00 // player name
7A 00 6F 00 77 00 

04 00 00 00 // race (Wookiee)

00 00 // no specified region

08 00 
74 61 74 6F 6F 69 6E 65  // tatooine

03 00
52 45 44  // RED (guild)

00 00  // no specified title

=======================================

04 00 00 00 // bitmask counter
38 00 00 00 // bitmask
00 00 00 00                                 
00 00 00 00 
00 00 00 00 

04 00 00 00 
56 00 6F 00 68 00 75 00 // player name (Vohu)

00 00 00 00 // race (Human)

1E 00 
40 74 61 74 6F 6F 69 6E 
65 5F 72 65 67 69 6F 6E  // region-name STF 
5F 6E 61 6D 65 73 3A 62 
65 73 74 69 6E 65 

08 00 
74 61 74 6F 6F 69 6E 65  // tatooine

00 00  // no specified guild

00 00  // no specified title


========================================

04 00 00 00 // bitmask counter
38 00 00 00// bitmask
00 00 00 00                                 
00 00 00 00 
00 00 00 00

05 00 00 00 
56 00 65 00 67 00 61 00 27 00 // player name

07 00 00 00 // race (Zabrak)

2B 00 
40 74 61 74 6F 6F 69 6E 
65 5F 72 65 67 69 6F 6E 
5F 6E 61 6D 65 73 3A 76// region-name STF  
61 6C 5F 68 61 75 6C 5F 
73 70 61 77 6E 5F 62 6C 
6F 63 6B 

08 00 
74 61 74 6F 6F 69 6E 65 // tatooine

00 00 // no specified guild

00 00  // no specified title

=========================================

04 00 00 00  // bitmask counter
38 00 00 00   // bitmask
00 00 00 00                                
00 00 00 00 
00 00 00 00 

04 00 00 00 
4E 00 61 00 74 00 27 00  // player name 

00 00 00 00  // race (Human)

00 00 // no specified region

08 00 
74 61 74 6F 6F 69 6E 65  // tatooine

00 00  // no specified guild

00 00  // no specified title
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete