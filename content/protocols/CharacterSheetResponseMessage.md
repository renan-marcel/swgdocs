---
title: CharacterSheetResponseMessage
url: https://wiki.swganh.org/index.php/CharacterSheetResponseMessage
page_type: Server Packet
opcode: 9B3A17C4
revision_id: 20801
last_modified: 2008-01-06T04:08:33Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Float', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# CharacterSheetResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | Op Code |
| INT | 0 |
| INT | 0 |
| FLOAT | Bind Location X |
| FLOAT | Bind Location Y |
| FLOAT | Bind Location Z |
| A_STRING | Bind Planet |
| INT | Bank X Not used |
| INT | Bank Y Not used |
| INT | Bank Z Not used |
| A_STRING | Bank Planet |
| FLOAT | Home Location X |
| FLOAT | Home Location Y |
| FLOAT | Home Location Z |
| A_STRING | Home Planet |
| U_STRING | Spouse Name |
| INT | Lots Remaining |
| INT | Faction CRC |
| INT | Faction Status |

## Variable Descriptions
- Opperand_Count	     = 0D
- Opcode		     = 0x9B3A17C4

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
0D 00        // Op Count
C4 17 3A 9B  // CharacterSheetResponseMessage
00 00 00 00
00 00 00 00
00 00 FA C3  //Float (-500)  Bind X
00 00 E0 41  //Float (28)    Bind Y 
00 A0 8C C5  //Float (-4500) Bind Z
08 00                    // string count
63 6F 72 65 6C 6C 69 61  // corellia
00 00 00 00 // Bank X not used
00 00 00 00 // Bank Y not used
00 00 00 00 // Bank Z not used
08 00                    // string count
74 61 74 6F 6F 69 6E 65  // tatooine (bank Location)
00 00 FA C3  //Float (-500)  Home X
00 00 E0 41  //Float (28)    Home Y 
00 A0 8C C5  //Float (-4500) Home Z
08 00                    // string count
74 61 74 6F 6F 69 6E 65  // tatooine (home Location)
0D 00 00 00                               // String count
49 00 6C 00 6C 00 69 00 73 00 61 00 20 00 // I.l.l.i.s.a. .
44 00 61 00 65 00 6C 00 61 00 27 00       // D.a.e.l.a.'.
0a 00 00 00  // lots remaining
50 88 14 16  // CRC = 'rebel
00 00 00 00  // faction state 0/1/2
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete