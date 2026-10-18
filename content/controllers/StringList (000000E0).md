---
title: StringList (000000E0)
url: https://wiki.swganh.org/index.php/StringList_%28000000E0%29
page_type: Object Controller
opcode: 000000E0
revision_id: 21792
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Beginlist', 'Template:Int', 'Template:U string', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# StringList (000000E0)

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | strings count |

## Variable Descriptions
- controllerID	     = 000000E0

## Notes
- **NOTE:** 

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00                      Opperand Count
46 5E CE 80                Op-Code (ObjController)
0B 00 00 00                Sub-Op
E0 00 00 00                command Op (Dialog Options)
CA 42 D0 57 05 00 00 00    Character ID
00 00 00 00                Table of Strings Error ID #
01                         Number of options in list
3C 00 00 00              String Buffer Size (in UniCode.. calculated with formula: 
                             #=(STFLoc.size + StringName.size() + Size of remaining data 
                             (0x56 or 0x57 depending on Mystery Byte Value 
                               everything must be divided by 2 because its a unicode buffer)
00 00                    Unk Data 1                   
00 00                    Mystery Bool (either 0 or 1)
01                       unk Data 2 (static) 
FF FF FF FF 	          unk Data 3 (static)
18 00  		  String Size
conversation/chassis_npc Location of the *.stf file in String\en\ (needs to be in hex)
00 00 00 00              Table of Strings Error ID #
0A 00 			  String Size
s_94e3013f    		  Points to a location in above stf (needs to be in hex)
00 00 00 00              Table of String Error ID #
00 00 00 00 00 00 00 00  Buffering
00 00 00 00 00 00 00 00  
00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | ControllerIDs | 100% Complete