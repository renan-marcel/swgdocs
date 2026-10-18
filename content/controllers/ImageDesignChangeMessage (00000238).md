---
title: ImageDesignChangeMessage (00000238)
url: https://wiki.swganh.org/index.php/ImageDesignChangeMessage_%2800000238%29
page_type: Object Controller
opcode: 00000238
revision_id: 48248
last_modified: 
completion: 75%
direction: unknown
sample_status: absent
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Byte', 'Template:A string', 'Template:Unknown', 'Template:Int', 'Template:Beginlist', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# ImageDesignChangeMessage (00000238)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | ID of the image designer |
| LONG | ID of the one getting Image designed |
| LONG | ID of the image tent (NOT the cell) |
| BYTE | ?? 1 when hair changed |
| A_STRING | hair |
| A_STRING | ?? |
| INT | bitmap (?) timer - only timer left is for statmigration though (>2) |
| INT | Session ID |
| INT | moneyDemanded |
| INT | moneyOffered |
| BYTE | flag commited by designer |
| INT | flag accepted by customer |
| BYTE | flag stat Migration |
| INT | bodyform/markingdesign Skill |
| INT | faceform/hairstyling Skill |
| INT | bodyform/markingdesign Skill |
| INT | faceform/hairstyling Skill |
| INT | Counter of changed Body attributes |

## Variable Descriptions
- controllerID	     = 00000238

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete