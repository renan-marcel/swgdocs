---
title: RevokeCommand
url: https://wiki.swganh.org/index.php/RevokeCommand
page_type: Server Packet
opcode: 22C9A55E
revision_id: 257254
last_modified: 2014-01-14T22:06:34Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Ascii', 'Template:ServerPacket', 'Template:100%']
---

# RevokeCommand

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| SHORT | StringSize |
| ASCII | CommandRevoked |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 22C9A55E

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
This is an example of skills an entertainer would loose when changing to another profession (this list is NOT complete but will give you sense!). 

The revoke command must be sent for every single skill of the profession being changed. 

This network messages are sent inconjunction with object controllers setProfessionTemplate and setCurrentWorkingSkill. 


droid_follow_other
droid_friend
droid_group
droid_guard
droid_patrol
droid_patrol_clear
droid_patrol_point
droid_regenerative_plating_1
droid_stay
droid_store
droid_torturous_needle_1
droid_transfer
droid_trick_1
droid_trick_2
droid_trick_3
droid_trick_4
prop_sword  startDance+rhythmic2
startMusic+pop
firejet
prop_glowstick
startDance+formal2
traz
startDance+formal
startMusic+starwars3
wear_all_armor
distract
prop_sparkler
startDance+footloose2
kloohorn
startDance+footloose
startMusic+folk
dazzle
droid_attack
droid_battery_dump_1
droid_droideka_shield_1
droid_electrical_shock_1
droid_flame_jet_1
droid_follow


Note: the GrantCommand gets sent to add new skills and abilities when Respec'ing.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete