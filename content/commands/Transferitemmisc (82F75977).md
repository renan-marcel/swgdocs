---
title: Transferitemmisc (82F75977)
url: https://wiki.swganh.org/index.php/Transferitemmisc_%2882F75977%29
page_type: Command
opcode: 82F75977
revision_id: 21584
last_modified: 2008-01-10T00:35:45Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:U string', 'Template:Byte', 'Template:ClientPacket', 'Template:ServerPacket', 'Template:75%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Transferitemmisc (82F75977)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | int1 |
| INT | CommandQueueEnqueue |
| LONG | Character ID |
| INT | ?? |
| INT | ?? |
| INT | Transferitemmisc |
| LONG | Object ID |
| U_STRING | ID number |

## Variable Descriptions
- Opcode		     = 82F75977

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
----
05 00 
46 5E CE 80 // ObjControllerMessage
23 00 00 00 
16 01 00 00 
A1 56 89 27 00 00 00 00 // character id
00 00 00 00 
C0 00 00 40 
77 59 F7 82             // transferitemmisc
A5 0B 9A 79 1E 00 00 00 // object id being moved or bank id 
28 00 00 00                                         // u-string count
20 00 36 00 36 00 33 00 33 00 31 00 32 00           // .6.6.3.3.1.2.
30 00 33 00 37 00 20 00 2D 00 31 00 20 00 30 00     // 0.3.7...-.1...0.
2E 00 30 00 30 00 30 00 30 00 30 00 30 00 20 00     // ..0.0.0.0.0.0...
30 00 2E 00 30 00 30 00 30 00 30 00 30 00 30 00     // 0...0.0.0.0.0.0.
20 00 30 00 2E 00 30 00 30 00 30 00 30 00 30 00     // ..0...0.0.0.0.0.
30 00 06 BA                                         // 0...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete | CommandQueueEnqueue | Client Commands