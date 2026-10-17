---
title: PlayClientEffectLocMessage
url: https://wiki.swganh.org/index.php/PlayClientEffectLocMessage
page_type: Server Packet
opcode: 02949E74
revision_id: 20588
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Float', 'Template:Long', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# PlayClientEffectLocMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| A_STRING | File |
| A_STRING | Planet |
| FLOAT | PositionX |
| FLOAT | PositionZ |
| FLOAT | PositionY |
| LONG | ?? |
| INT | ?? |

## Variable Descriptions
- Operand_Count	     = 8
- Opcode		     = 02949E74

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
08 00 	    	// opCount
74 9E 94 02 	//PlayClientEffectLocMessage

24 00 
63 6C 69 65 6E 74 65 66 66 65 63 74 
2F 73 75 72 76 65 79 5F 74 6F 6F 6C  //clienteffect/survey_tool_mineral.cef
5F 6D 69 6E 65 72 61 6C 2E 63 65 66 

05 00 
6E 61 62 6F 6F 	// naboo

A6 59 A5 45 	// X
AC 07 45 C3 	// Z
AB A9 BE 45 	// Y

00 00 00 00 00 00 00 00 
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete