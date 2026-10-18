---
title: ImageDesignEndMessage (00000239)
url: https://wiki.swganh.org/index.php/ImageDesignEndMessage_%2800000239%29
page_type: Object Controller
opcode: 00000239
revision_id: 27965
last_modified: 
completion: 75%
direction: unknown
sample_status: absent
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Byte', 'Template:A string', 'Template:Unknown', 'Template:Int', 'Template:Beginlist', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# ImageDesignEndMessage (00000239)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | id of the image designer |
| LONG | id of the one getting Image designt |
| LONG | always 0 |
| BYTE | ?? 1 when hair changed |
| A_STRING | hair |
| A_STRING | ?? |
| INT | ?? |
| INT | Session Id |
| INT | moneyDemanded |
| INT | money Offered |
| BYTE | ?? |
| INT | 1 when canceled by client |
| BYTE | ?? |
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