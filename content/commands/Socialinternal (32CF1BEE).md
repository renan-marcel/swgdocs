---
title: Socialinternal (32CF1BEE)
url: https://wiki.swganh.org/index.php/Socialinternal_%2832CF1BEE%29
page_type: Command
opcode: 32CF1BEE
revision_id: 79349
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Uint', 'Template:Byte', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Socialinternal (32CF1BEE)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Target character ID |
| UINT | Emote ID |
| BYTE | Send type |
| BYTE | Send animation |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 32CF1BEE

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

"32CF1BEE",352,0,9,"0 214 1 0"
"32CF1BEE",160,0,9,"0 294 1 0"
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands