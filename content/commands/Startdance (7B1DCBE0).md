---
title: Startdance (7B1DCBE0)
url: https://wiki.swganh.org/index.php/Startdance_%287B1DCBE0%29
page_type: Command
opcode: 7B1DCBE0
revision_id: 15846
last_modified: 
completion: 50%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '50% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:50%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Startdance (7B1DCBE0)

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
- Opcode		     = 7B1DCBE0

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **50%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
05 00 
46 5E CE 80 // objectControllerMessage
23 00 00 00 
16 01 00 00 // CommandQueueEnqueue
98 40 B2 2D 03 00 00 00 // Character ID
00 00 00 00 
20 00 00 40 
E0 CB 1D 7B // startdance
00 00 00 00 
00 00 00 00 
00 00 00 00 
01 7B FC  // CRC
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 50% Complete | CommandQueueEnqueue | Client Commands