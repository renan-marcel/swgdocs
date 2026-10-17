---
title: Nextcraftingstage (6AD8ED4D)
url: https://wiki.swganh.org/index.php/Nextcraftingstage_%286AD8ED4D%29
page_type: Command
opcode: 6AD8ED4D
revision_id: 70868
last_modified: 
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:75%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Nextcraftingstage (6AD8ED4D)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

## Variable Descriptions
- Opperand_Count	     =
- Opcode		     = 6AD8ED4D

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
----

"6AD8ED4D",96,0,1,"1"
"6AD8ED4D",320,0,1,"6"
"6AD8ED4D",352,0,1,"3"
"6AD8ED4D",544,0,2,"11"

==== CU packet ============
05 00 
46 5E CE 80 
23 00 00 00 
16 01 00 00 
92 7C A0 B3 1A 00 00 00 // Character ID
00 00 00 00 
60 00 00 00 // counter of some kind
4D ED D8 6A // /nextCraftingStage Opcode
00 00 00 00 
00 00 00 00 
01 00 00 00 // could be the step in the crafting phase ie Screen 1 after selecting schem
31 00 B0 00 
09 00 28
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete | CommandQueueEnqueue | Client Commands