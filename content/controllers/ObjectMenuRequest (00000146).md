---
title: ObjectMenuRequest (00000146)
url: https://wiki.swganh.org/index.php/ObjectMenuRequest_%2800000146%29
page_type: Object Controller
opcode: 00000146
revision_id: 79395
last_modified: 2012-08-14T03:40:02Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Beginlist', 'Template:Byte', 'Template:U string', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:ClientPacket', 'Template:100%']
---

# ObjectMenuRequest (00000146)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Item ID |
| LONG | Receiver ID |
| INT | Options Count |

## Variable Descriptions
- controllerID	     = 00000146

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00  //'OBJECTUPDATE 
46 5E CE 80   //'ObjControllerMessage
23 00 00 00   //sub-op
46 01 00 00   //command op
07 8A D8 CE 13 00 00 00 //character id
00 00 00 00 
CE A9 03 E3 1E 00 00 00  //object id
07 8A D8 CE 13 00 00 00  //character id
01 00  00 00 //list size
01 //option #
00 //parent ID
07  //option ID ("EXAMINE")
01 //option type
00 00 00 00 //unicode string length
03 //radial counter
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Client Packets | 100% Complete