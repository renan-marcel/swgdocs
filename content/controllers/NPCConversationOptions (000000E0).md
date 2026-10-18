---
title: NPCConversationOptions (000000E0)
url: https://wiki.swganh.org/index.php/NPCConversationOptions_%28000000E0%29
page_type: Object Controller
opcode: 000000E0
revision_id: 20659
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Beginlist', 'Template:Int', 'Template:U string', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# NPCConversationOptions (000000E0)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Option Count |

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
04 00 00 00                String Buffer Size
74 00 65 00 73 00 74 00    test
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete