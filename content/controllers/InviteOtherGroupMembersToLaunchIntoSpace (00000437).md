---
title: InviteOtherGroupMembersToLaunchIntoSpace (00000437)
url: https://wiki.swganh.org/index.php/InviteOtherGroupMembersToLaunchIntoSpace_%2800000437%29
page_type: Object Controller
opcode: 00000437
revision_id: 257223
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# InviteOtherGroupMembersToLaunchIntoSpace (00000437)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Object ID: player inviting group member |
| INT | Unknown INT |
| LONG | Object ID: player being invited |

## Variable Descriptions
- controllerID	     = 00000437

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
cAble 
* NGE packet capture but likely to be same as precu.

05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
37 04 00 00 #inviteOtherGroupMembersToLaunchIntoSpace
AC 3B 65 D2 00 00 00 00 #ObjectID: PlayerInviting

00 00 00 00 #UnknownINT
A1 56 89 27 00 00 00 00 #ObjectID: Player being Invited
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete