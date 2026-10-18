---
title: BiographyUpdate (000001DB)
url: https://wiki.swganh.org/index.php/BiographyUpdate_%28000001DB%29
page_type: Object Controller
opcode: 000001DB
revision_id: 19337
last_modified: 2007-12-18T03:43:57Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:U string', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# BiographyUpdate (000001DB)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Bio Owner ID |
| INT | Unicode String Size |
| U_STRING | Biography |

## Variable Descriptions
- controllerID	     = 000001DB

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00                                          //'OBJECTUPDATE
46 5E CE 80                               //'ObjControllerMessage
0B 00 00 00
DB 01 00 00
D2 CD 31 6E 0C 00 00 00          //'character ID
00 00 00 00
D2 CD 31 6E 0C 00 00 00          //'character ID
0B 00 00 00                             //UNICODE STRING SIZE(11)
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete