---
title: Addfriend (2A2357ED)
url: https://wiki.swganh.org/index.php/Addfriend_%282A2357ED%29
page_type: Command
opcode: 2A2357ED
revision_id: 20918
last_modified: 2008-01-06T23:03:19Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Addfriend (2A2357ED)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| Operand 1 | character name |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 2A2357ED

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
05 00
46 5E CE 80                      // ObjControllerMessage
23 00 00 00
16 01 00 00
71 E2 DB D9 00 00 00 00          // character id
00 00 00 00
00 00 00 00 
ED 57 23 2A                      // addfriend
00 00 00 00
00 00 00 00
06 00 00 00                      // u-string count
65 00 74 00 27 00 74 00 61 00 6C // e.t.'.t.a.l
00 CD 64
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands