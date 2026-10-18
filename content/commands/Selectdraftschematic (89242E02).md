---
title: Selectdraftschematic (89242E02)
url: https://wiki.swganh.org/index.php/Selectdraftschematic_%2889242E02%29
page_type: Command
opcode: 89242E02
revision_id: 18655
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Long', 'Template:U string', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Selectdraftschematic (89242E02)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | ?? poss id never used afaict |
| U_STRING | Nr of the schematic in the list send on *ObjectController::DraftSchematics* |

## Variable Descriptions
- Opperand_Count	     =
- Opcode		     = 89242E02

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
----

"89242E02",64,0,2,"23"
"89242E02",512,0,2,"27"
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands