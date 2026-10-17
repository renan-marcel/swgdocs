---
title: LoginClientToken
url: https://wiki.swganh.org/index.php/LoginClientToken
page_type: Server Packet
opcode: AAB296C6
revision_id: 19784
last_modified: 2007-12-27T23:16:10Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:B string', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# LoginClientToken

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| B_STRING | Session_Key |
| INT | UserID |
| A_STRING | UserName |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = AAB296C6

## Notes
- **NOTE:** 

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00			//Operand_Count
C6 96 B2 AA		//Opcode LoginClientToken



3C 00 00 00		//Session_Key Size 60


20 00 00 00 15 00 00 00
0E D6 93 DE D2 EF BF 8E
A1 AC D2 EE 4C 55 BE 30 
5F BE 23 0D B4 AB 58 F9       //Session_Key
62 69 79 67 E8 10 6E D3 
86 9B 3A 4A 1A 72 A1 FA
8F 96 FF 9F A5 62 5A 29
11 00 00 00


00 00 00 00 00 		//UserID

05 00			//String Size 5
6D 75 67 6C 79		//mugly

00 26 6D	        //comp flag, crc
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete