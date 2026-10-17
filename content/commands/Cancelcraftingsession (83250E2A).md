---
title: Cancelcraftingsession (83250E2A)
url: https://wiki.swganh.org/index.php/Cancelcraftingsession_%2883250E2A%29
page_type: Command
opcode: 83250E2A
revision_id: 21619
last_modified: 2008-01-10T02:50:52Z
completion: 25%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '25% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:25%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Cancelcraftingsession (83250E2A)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
|  | OpCode |
|  | Timer? |
|  | 0 |
|  | 0 |

## Variable Descriptions
- Opperand_Count	     =
- Opcode		     = 83250E2A

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **25%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
----

"83250E2A",224,0,0,""
"83250E2A",448,0,0,""
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 25% Complete | CommandQueueEnqueue | Client Commands