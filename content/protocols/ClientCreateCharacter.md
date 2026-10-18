---
title: ClientCreateCharacter
url: https://wiki.swganh.org/index.php/ClientCreateCharacter
page_type: Client Packet
opcode: B97F3074
revision_id: 22133
last_modified: 
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:C string', 'Template:U string', 'Template:A string', 'Template:Byte', 'Template:Unknown', 'Template:Float', 'Template:ClientPacket', 'Template:75%']
---

# ClientCreateCharacter

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| C_STRING | CharCustomization |
| U_STRING | CharName |
| A_STRING | Player_Race_IFF |
| A_STRING | StartLocation |
| A_STRING | HairObject |
| C_STRING | HairCustomization |
| A_STRING | StartProfession |
| BYTE | ?? |
| FLOAT | Height |
| U_STRING | Biography |
| BYTE | Tutorial_Flag |

## Variable Descriptions
- Op Count	     = 0C
- Opcode		     = B97F3074

## Notes
- **TODO:** Find how to change StartLocation.
- **TODO:** Figure out the purpose of this byte.

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
0C 00 
74 30 7F B9 
72 00 02 23 17 C3 
BF 01 18 C3 A4 1C C3 BF 01 1B 62 05 43 1A C2 BF        ..........b.C...
19 C3 BF 01 0D C3 BF 01 09 2D 12 C2 AD 13 C3 BF        .........-......
01 20 C3 BF 01 10 C3 BF 01 21 C2 8A 0F 73 14 2A        .........!...s.*
11 C3 BF 01 0E C3 96 03 C3 BF 01 0B 5E 0C C3 BF        ............^...
01 06 C3 BF 01 08 C2 82 15 C3 BF 01 16 28 04 C3        .............(..
9F 07 51 0A C3 BF 01 23 0A 25 02 24 C3 BF 01 01        ..Q....#.%.$....
17 1D C3 BF 01 1F 0B 1E C3 BF 01 C3 BF 03 05 00        ................
00 00 6D 00 69 00 6E 00 6B 00 6F 00 25 00 6F 62        ..m.i.n.k.o.%.ob
6A 65 63 74 2F 63 72 65 61 74 75 72 65 2F 70 6C        ject/creature/pl
61 79 65 72 2F 68 75 6D 61 6E 5F 6D 61 6C 65 2E        ayer/human_male.
69 66 66 07 00 62 65 73 74 69 6E 65 32 00 6F 62        iff..bestine2.ob
6A 65 63 74 2F 74 61 6E 67 69 62 6C 65 2F 68 61        ject/tangible/ha
69 72 2F 68 75 6D 61 6E 2F 68 61 69 72 5F 68 75        ir/human/hair_hu
6D 61 6E 5F 6D 61 6C 65 5F 73 30 37 2E 69 66 66        man_male_s07.iff
07 00 02 01 02 0D C3 BF 03 0F 00 63 6F 6D 62 61        ...........comba
74 5F 6D 61 72 6B 73 6D 61 6E 00 08 52 84 3F 00        t_marksman..R.?.
00 00 00 00 01 FB 29                                   ......)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete