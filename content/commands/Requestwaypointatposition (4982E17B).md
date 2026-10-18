---
title: Requestwaypointatposition (4982E17B)
url: https://wiki.swganh.org/index.php/Requestwaypointatposition_%284982E17B%29
page_type: Command
opcode: 4982E17B
revision_id: 8599
last_modified: 2007-06-02T06:16:37Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Requestwaypointatposition (4982E17B)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| Operand 1 | X position |
| Operand 2 | Z position |
| Operand 3 | Y position |
| Optional | Waypoint name |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = FFFFFFFF

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
dantooine -346.609985 10.769876 -88.972298
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands