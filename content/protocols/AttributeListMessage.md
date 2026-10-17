---
title: AttributeListMessage
url: https://wiki.swganh.org/index.php/AttributeListMessage
page_type: Server Packet
opcode: F3F12F2A
revision_id: 257264
last_modified: 2014-01-21T23:49:21Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Beginlist', 'Template:A string', 'Template:U string', 'Template:Endlist', 'Template:ServerPacket', 'Template:100%']
---

# AttributeListMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcde |
| LONG | ObjectID |
| INT | ListCount |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = F3F12F2A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00                                           // Operand Count
2A 2F F1 F3                                     // OpCode
4A 1F 9C 1F 01 00 00 00                         // Object ID
13 00 00 00                                     // List Count
09 00 					   	// A_string
63 6F 6E 64 69 74 69 6F 6E                 	// "condition"
07 00 00 00                                	// U_string size
34 00 36 00 31 00 2F 00 39 00 35 00 30 00  	// "461/950"
06 00 		  			   	// A_string size
76 6F 6C 75 6D 65 			   	// "volume"
01 00 00 00       			   	// U_string size
31 00             			   	// "1"
07 00 					   	// A_string size
63 72 61 66 74 65 72 			   	// "crafter" 
16 00 00 00 				   	// U_string size
44 00 65 00 6D 00 6F 00 73 00 74 00 68 00 65    
00 6E 00 65 00 73 00 20 00 4B 00 61 00 67 00    // "Demosthenes Kaggazzari"
67 00 61 00 7A 00 7A 00 61 00 72 00 69 00     

etc...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete