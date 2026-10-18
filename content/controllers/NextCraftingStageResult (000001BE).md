---
title: NextCraftingStageResult (000001BE)
url: https://wiki.swganh.org/index.php/NextCraftingStageResult_%28000001BE%29
page_type: Object Controller
opcode: 000001BE
revision_id: 257036
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# NextCraftingStageResult (000001BE)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | RequestID |
| INT | response |
| BYTE | sequnceId |

## Variable Descriptions
- controllerID	     = 000001BE

## Notes
- **NOTE:** Many of the crafting packets utilize the same basic generic template

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
NGE struct by cAble

05 00 #Operand
46 5E CE 80 #ObjCon
0B 00 00 00 
BE 01 00 00 #nextCraftingStageResult
00 2E E9 E9 31 00 00 00 #CharacterID

00 00 00 00 

09 01 00 00 	# RequestID	
01 00 00 00 	# Response 	
29 		# sequnce Id
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete