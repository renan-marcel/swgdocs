---
title: Transferitem (3CFB449D)
url: https://wiki.swganh.org/index.php/Transferitem_%283CFB449D%29
page_type: Command
opcode: 3CFB449D
revision_id: 79353
last_modified: 2012-03-19T03:42:15Z
completion: 100%
direction: C→S
sample_status: placeholder
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Float', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Transferitem (3CFB449D)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | target container id |
| INT | link type |
| FLOAT | x |
| FLOAT | y |
| FLOAT | z |

## Variable Descriptions
- Opperand_Count	     = X
- Opcode		     = 3CFB449D
- Then the link type: this can be either link = 4 or unlink = 0xFFFFFFFF

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
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands