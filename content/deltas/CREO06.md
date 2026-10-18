---
title: CREO06
url: https://wiki.swganh.org/index.php/CREO06
page_type: Baseline
opcode: 
revision_id: 79212
last_modified: 2011-09-12T14:25:51Z
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:CREOArchitectureNAV', 'Template:100%']
---

# CREO06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjOpperandCount |
| INT | ServerID |
| INT | CombatDefenderListSize |
| INT | UpdateCounter |
| LONG | DefenderID |
| SHORT | DifficultyCon |
| ASTRING | CurrentAnimation |
| ASTRING | MoodAnimation |
| LONG | WeaponID |
| LONG | GroupID |
| LONG | InviteSenderID |
| LONG | InviteCounter |
| INT | GuildID |
| LONG | TargetID |
| BYTE | MoodID |
| INT | PerformanceStartTime |
| INT | PerformanceID |
| INT | CurrentHAMListSize |
| INT | UpdateCounter |
| INT | CurrentHAMValue |
| INT | MaxHAMListSize |
| INT | UpdateCounter |
| INT | MaxHAMValue |
| INT | EquiptmentListSize |
| INT | UpdateCounter |
| CSTRING | CustomizationString |
| INT | ContainmentType |
| LONG | ObjectID |
| INT | TemplateCRC |
| ASTRING | SetObjectTemplateString |
| BYTE | StationaryFlag |

## Variable Descriptions
- Obj_OperandCount = 16

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.

## Sample Packet
```
CombatDefender:
This list stores a list of all the objects you are in combat with.
It also initiates default combat animation used between combat animations.
(it keeps the consistancy of combat going).

DefenderObjIndex:
This is the index value of the defenderID in the list. IE. Position in the list.
4 Objects. List is 00 01 02 03
Remove 3rd Object. Index = 02.

DifficultyCon:
This is the ID number of what color difficulty CON to display for the target.

CurrentAnimation:
This is a string of what animation this object is doing.
Set for entertainer, as well as misc types of animation.

MoodAnimation:
This is a string for what type of facial/mood animation to set on the object.

WeaponID:
The ObjectID of the currently equipped weapon.

GroupID:
The ObjectID of the GROUP Object if this object is in a group.

InviteSenderID:
This is the ID of the Object that sent a group invite to you.

InviteCounter:
This is a counter or an InviteID to differentiate invites and allow multiple invites.
SWG seems to have only allowed 1 invite at a time (Counter set to 0).
But by changing the counter we got multiple Invites sent.

GuildID:
The ID number from the GUILD Object that corresponds to your GUILD Tag.

TargetID:
The Object ID number of the current Object in your target.

MoodID:
The numeric ID number for your current Mood used in text and /mood.

PerformanceStartTime:
A timestamp used to mark the start of a performance. It is in number of seconds.
Also appears to be from the server start time, tested on TC Prime with 278.91 days.

PerformanceID:
The ID number of what song+instrument/dance is being done by this object.
For entertainers, obviously.

CurrentHAM:
A list of the 9 values for how much HAM is current in the pool.

MaxHAM:
A list of the 9 values for how much HAM the pool can hold.

EquiptmentList:
A list of Objects that are equipped on this Object. (Weapons, Clothes, Inventory/Bank etc).
ContainmentType is the same type of integer found in UpdateContainmentMessage

SetObjectTemplateString:
This is a string of a CRC Template found in the object/ folder. It can be used to turn
your object into another object for events, fun, CSR stuffs!

StationaryFlag:
This flag when set to 1 freezes the creature object in place. UpdateTransforms no longer work
affect the object. However, if a transform was sent, once it unfreezes (set to 0), the object will update
itself.
0 = Moveable
1 = Stationary
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete