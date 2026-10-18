---
title: NpcConversationMessage (000000DF)
url: https://wiki.swganh.org/index.php/NpcConversationMessage_%28000000DF%29
page_type: Object Controller
opcode: 000000DF
revision_id: 20656
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:U string', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# NpcConversationMessage (000000DF)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | Unicode String Size |
| U_STRING | Main Dialog Box Text |

## Variable Descriptions
- ControllerID	     = 000000DF

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00                    Opperand Count
46 5E CE 80              Op Code (ObjController)
0B 00 00 00 	          Sub-op
DF 00 00 00		  Command Op (Add to Main Body)	
19 00 00 00 00 00 00 00  Character ID
00 00 00 00 	          
04 00 00 00              Unicode string size
74 00 65 00 73 00 74 00  test
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete