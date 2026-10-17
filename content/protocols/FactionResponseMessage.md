---
title: FactionResponseMessage
url: https://wiki.swganh.org/index.php/FactionResponseMessage
page_type: Server Packet
opcode: 5DD53957
revision_id: 78289
last_modified: 2011-05-16T04:09:56Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Beginlist', 'Template:A string', 'Template:Endlist', 'Template:Float', 'Template:ServerPacket', 'Template:100%']
---

# FactionResponseMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | FactionRank |
| INT | RebelPoints |
| INT | ImperialPoints |
| INT | FactionNamesListCount |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = 5DD53957

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
06 00                             //Opperand Count
 57 39 D5 5D                            //FactionResponseMessage
00 0A 00 00                             //Faction Rank
78 EC FF FF                             //Rebel Points
78 EC FF FF                             //Imperial Points

33 00 00 00  //INT(51) 'List Size (missing 3 factions?)

04 00                                                                         //INT(4)
48 75 74 74                                                                //'Hutt'
08 00                                                                         //INT(8)
49 6D 70 65 72 69 61 6C                                          //'Imperial'
05 00                                                                          //INT(5)     
52 65 62 65 6C                                                         //'Rebel'
07 00                                                                          //INT(7)
61 61 6B 75 61 6E 73                                               //'aakuans'
07 00                                                                         //INT(7)       
61 6C 6B 68 61 72 61                                             //'alkhara'
06 00                                                                          //INT(6)
62 61 6E 64 69 74                                                    //'bandit'
10 00                                                                          //INT(16)
62 65 6C 64 6F 6E 6E 61 73 5F 6C 65 61 67 75 65                               //'beldonnas_league'
07 00                                                                          //INT(7)
62 69 6E 61 79 72 65                                                 //'binayre'
0A 00                                                                         //INT(10)
62 6C 6F 6F 64 72 61 7A 6F 72 05 00 62 6F 72 76 6F      //'bloodrazor�
0E 00                                                                         //INT(14)
61 6E 79 6F 6E 5F 63 6F 72 73 61 69 72                  //'anyon_corsair'
06 00                                                                          //INT(6)
63 6F 62 72 61 6C 06 00 63 6F 72 73 65 63             //'cobral�
0F 00                                                                          //INT(15)
64 61 6E 74 61 72 69 5F 72 61 69 64 65 72 73         //'dantari_raiders'
0C 00                                                                          //INT(12)
64 65 73 65 72 74 5F 64 65 6D 6F 6E                       //'desert_demon'
05 00                                                                          //INT(5)
64 72 61 6C 6C  //'drall'
0E 00                                                                          //INT(14)
65 6E 64 6F 72 5F 6D 61 72 61 75 64 65 72           //'endor_marauder'
07 00                                                                          //INT(7)
66 65 64 5F 64 75 62                                                //'fed_dub'
16 00                                                                          //INT(22)
66 6F 6C 6C 6F 77 65 72 73 5F 6F 66 5F 6C 6F 72 64 5F 6E 79 61 78   //'followers_of_lord_nyax'
11 00                                                                         //INT(17)
66 6F 72 65 73 74 5F 6B 65 72 72 69 74 61 6D 62 61               //'forest_kerritamba'
0E 00                                                                         //INT(14)
66 6F 72 65 73 74 5F 6F 75 74 63 61 73 74             //'forest_outcast'
05 00                                                                          //INT(5)
67 61 72 79 6E                                                          //'garyn'
0D 00                                                                         //INT(13)
67 6F 6E 64 75 6C 61 5F 74 72 69 62 65                 //'gondula_tribe'
06 00                                                                         //INT(6)
67 75 6E 67 61 6E                                                  //'gungan'
05 00                                                                          //INT(5)
6A 61 62 62 61                                                         //'jabba'
0B 00                                                                         //INT(11)
6A 61 6E 74 61 5F 74 72 69 62 65                         //'janta_tribe'
04 00                                                                         //INT(4)
6A 61 77 61                                                             //'jawa'
0B 00                                                                         //INT(11)
6B 75 6E 67 61 5F 74 72 69 62 65                           //'kunga_tribe'
10 00                                                                          //INT(16)
6C 69 62 65 72 61 74 69 6F 6E 5F 70 61 72 74 79        //'liberation_party'
0F 00                                                                          //INT(15)
6C 6F 6B 5F 6D 65 72 63 65 6E 61 72 69 65 73        //'lok_mercenaries'
0D 00                                                                          //INT(13)
6C 6F 73 74 5F 61 71 75 61 6C 69 73 68                 //'lost_aqualish'
0A 00                                                                          //INT(10)
6D 6F 6B 6B 5F 74 72 69 62 65                                   //'mokk_tribe'
08 00                                                                          //INT(8)
6D 74 6E 5F 63 6C 61 6E 05 00 6E 61 62 6F 6F         //'mtn_clan�
14 00                                                                          //INT(20)
6E 61 62 6F 6F 5F 73 65 63 75 72 69 74 79 5F 66 6F 72 63 65       //'naboo_security_force'
06 00                                                                          //INT(6)
6E 61 72 6D 6C 65                                                  //'narmle'
0B 00                                                                         //INT(11)
6E 69 67 68 74 73 69 73 74 65 72                          //'nightsister'
03 00                                                                          //INT(3)
6E 79 6D   //'nym'
0D 00                                                                         //INT(13)
70 61 6E 73 68 65 65 5F 74 72 69 62 65                 //'panshee_tribe'
06 00                                                                         //INT(6)
70 69 72 61 74 65                                                //'pirate' 
0C 00                                                                          //INT(12)
70 6C 61 73 6D 61 5F 74 68 69 65 66                //'plasma_thief'
07 00                                                                         //INT(7)
72 65 73 74 75 73 73                                            //'restuss'
0B 00                                                                         //INT(11)
73 69 74 68 5F 73 68 61 64 6F 77                          //'sith_shadow'
12 00                                                                          //INT(18)
73 70 69 64 65 72 5F 6E 69 67 68 74 73 69 73 74 65 72      //'spider_nightsister'
09 00                                                                         //INT(9)
73 77 61 6D 70 5F 72 61 74                                   //'swamp_rat'
05 00                                                                         //INT(5)
73 77 6F 6F 70                                                          //'swoop'
04 00                                                                          //INT(4)
74 68 75 67                                                             //'thug'
0B 00                                                                         //INT(11)
74 6F 77 6E 73 70 65 72 73 6F 6E                         //'townsperson'
10 00                                                                                //INT(16)
74 72 61 64 65 5F 66 65 64 65 72 61 74 69 6F 6E        //'trade_federation'
0D 00                                                                         //INT(13)
74 75 73 6B 65 6E 5F 72 61 69 64 65 72                 //'tusken_raider'
08 00                                                                          //INT(8)
76 61 6C 61 72 69 61 6E                                          //'valarian'

33 00 00 00  //'list size (51)
00 40 9C C5  //Float(-5000)
00 40 9C C5  //Float(-5000)
94 09 20 45  //Float(2560.599)
00 40 9C C5   //Float(-5000)
00 E0 92 45  //Float(4700)
00 E0 E9 44  //Float(1871)
00 40 9C 45  //Float(5000)
00 40 9C 45   //Float(5000)
00 40 9C 45   //Float(5000)
00 80 F2 44   //Float(1940)
00 40 9C C5  //Float(-5000)
00 E0 49 C5   //Float(-3230)
00 40 9C 45   //Float(5000)
00 40 9C 45  //Float(5000)
00 80 95 C5   //Float(-4784)
00 00 8C 43   //Float(280)
00 40 9C C5  //Float(-5000)
00 40  9C 45  //Float(5000)
00 40 9C C5  //Float(-5000)
00 80 C0 43  //Float(385)
00 80 40 C4  //Float(-770)
00 40 83 C5  //Float(-4200)
00 30 1D 45  //Float(2515)
00 00 7A C3   //Float(-250)
00 B0 95 C5  //Float(-4790)
00 40 9C C5  //Float(-5000)
00 40 92 45  //Float(4680)
00 40 9C 45  //Float(5000)
00 40 9C 45   //Float(5000)
00 40 9C C5  //Float(-5000)
00 40 08 C5  //Float(-2180)
00 20 A8 44  //Float(1345)
00 C0 55 45  //Float(3420)
00 00 C8 C2  //Float(-100)
00 90 17 45  //Float(2425)
00 00 16 44  //Float(600)
00 90 83 C5   //Float(-4210)
00 40 9C 45  //Float(5000)
00 30 1D 45  //Float(2515)
00 40 9C C5  //Float(-5000)
00 00 FA 42   //Float(125)
00 40 9C 45   //Float(5000)
00 40 9C C5  //Float(-5000)
00 40 9C C5  //Float(-5000)
00 00 FA 42  //Float(125)
00 00 CB C2  //Float(-101.5)
00 28 9B C5  //Float(-4965)
00 30 98 45  //Float(4870)
00 00 E1 C3  //Float(-450)
00 90 92 C5  //Float(-4690)
00 70 63 45   //Float(3639)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete