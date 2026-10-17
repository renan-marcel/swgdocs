---
title: StopNpcConversation (000000DE)
url: https://wiki.swganh.org/index.php/StopNpcConversation_%28000000DE%29
page_type: Object Controller
opcode: 000000DE
revision_id: 17799
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# StopNpcConversation (000000DE)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| LONG | Converser ID |
| INT | unknown |
| INT | unknown |
| INT | unknown |
| INT | unknown |

## Variable Descriptions
- controllerID	     = 000000DE

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
05 00                     'Opperand Count
46 5E CE 80               'Object Controller
0B 00 00 00               
DE 00 00 00               'Command ID
9C 4B D3 1B 18 00 00 00   'Player ID
00 00 00 00               'unknown
F3 EB F9 1B 20 00 00 00   'Converser ID
00 00 00 00               'unknown
00 00 00 00               'unknown
00 00 00 00               'unknown
00 00 00 00               'unknown
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete