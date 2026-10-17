---
title: Setmatchmakingpersonalid (D63286B8)
url: https://wiki.swganh.org/index.php/Setmatchmakingpersonalid_%28D63286B8%29
page_type: Command
opcode: D63286B8
revision_id: 21737
last_modified: 
completion: 25%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '25% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:U string', 'Template:ClientPacket', 'Template:25%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Setmatchmakingpersonalid (D63286B8)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| U_STRING | 4 ints in unicode each int divided by a space |

## Variable Descriptions
- Opperand_Count	     =
- Opcode		     = D63268B8

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **25%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
00 09 00 24 05 00 
46 5E CE 80 
23 00 00 00 
16 01 00 00 
37 B5 4E 97 27 00 00 00 

00 00 00 00 
00 00 00 00 
B8 86 32 D6 00 00 00 00 

00 00 00 00 
0B 00 00 00 
34 00 20 00 
32 00 35 00 36 00 20 00 
30 00 20 00 
30 00 20 00 
30 00                           

..4...2.5.6...0...0...0.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 25% Complete | CommandQueueEnqueue | Client Commands