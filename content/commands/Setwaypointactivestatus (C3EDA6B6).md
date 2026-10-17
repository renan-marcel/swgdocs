---
title: Setwaypointactivestatus (C3EDA6B6)
url: https://wiki.swganh.org/index.php/Setwaypointactivestatus_%28C3EDA6B6%29
page_type: Command
opcode: C3EDA6B6
revision_id: 20637
last_modified: 2008-01-03T18:58:13Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Long', 'Template:U string', 'Template:ClientPacket', 'Template:ServerPacket', 'Template:100%', 'Template:CommandQueueEnqueue']
---

# Setwaypointactivestatus (C3EDA6B6)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | Opcode |
| LONG | Waypoint ID |
| U_STRING | o.f.f. |

## Variable Descriptions
- Opcode		     = C3EDA6B6

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .

## Sample Packet
```
05 00 
46 5E CE 80 
23 00 00 00 
16 01 00 00 
4D FB F3 A5 0D 00 00 00 //CharacterID 
00 00 00 00 
00 43 00 00 
B6 A6 ED C3 // setwaypointactivestatus 
44 8E 78 FD 23 00 00 00 // waypoint id 
03 00 00 00 // u-string count 
6F 00 66 00 66 00 // o.f.f.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 100% Complete | CommandQueueEnqueue | Client Commands