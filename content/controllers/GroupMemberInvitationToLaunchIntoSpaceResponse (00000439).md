---
title: GroupMemberInvitationToLaunchIntoSpaceResponse (00000439)
url: https://wiki.swganh.org/index.php/GroupMemberInvitationToLaunchIntoSpaceResponse_%2800000439%29
page_type: Object Controller
opcode: 00000439
revision_id: 257190
last_modified: 
completion: 50%
direction: unknown
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'ControllerIDs', 'Server Packets', '50% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Long', 'Template:Unknown', 'Template:Byte', 'Template:ObjControllerMessageTag', 'Template:50%']
---

# GroupMemberInvitationToLaunchIntoSpaceResponse (00000439)

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| LONG | ?? |
| BYTE | ?? |

## Variable Descriptions
- controllerID	     = 00000439

## Notes
- **NOTE:** The struct (coming soon), is from NGE, but likely to the same as prec.

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **50%** - This packet has been partially reversed.

## Sample Packet
```
* Researched by cAble (NGE packet reverser)
* NGE packet capture but likely to be same as precu.
* Below is a SPECULATED struct, given the similarities to other space invite packets. 


05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
37 04 00 00 #inviteOtherGroupMembersToLaunchIntoSpace
AC 3B 65 D2 00 00 00 00 #ObjectID: PlayerInviting
00 00 00 00 #UnknownINT
A1 56 89 27 00 00 00 00 #ObjectID: Player being Invited                                                       


or 

05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
37 04 00 00 #inviteOtherGroupMembersToLaunchIntoSpace
AC 3B 65 D2 00 00 00 00 #ObjectID: PlayerInviting
A1 56 89 27 00 00 00 00 #ObjectID: Player being Invited                                                       

or 

05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
37 04 00 00 #inviteOtherGroupMembersToLaunchIntoSpace
A1 56 89 27 00 00 00 00 #ObjectID: Player ID who responsed to invite.
AC 3B 65 D2 00 00 00 00 #ObjectID: Player ID who sent invite.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | ControllerIDs | Server Packets | 50% Complete