---
title: Getattributesbatch (164550EF)
url: https://wiki.swganh.org/index.php/Getattributesbatch_%28164550EF%29
page_type: Command
opcode: 164550EF
revision_id: 70866
last_modified: 
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:75%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Getattributesbatch (164550EF)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

## Variable Descriptions
- Opperand_Count	     = 2 * n
- Opcode		     = 164550EF

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
CU PACKET

05 00 
46 5E CE 80 
23 00 00 00 
16 01 00 00 
92 7C A0 B3 1A 00 00 00 // Character ID
00 00 00 00 
20 00 00 00 // this number seems to go 20, 40, 60, 80, C0, E0 unknown at this time
EF 50 45 16 // getAttributesBatch Opcode
00 00 00 00 
00 00 00 00 
22 00 00 00 // unicode count
31 00 31 00 35 00 30 00 32 00 36 00 36 00              ..1.1.5.0.2.6.6.
38 00 31 00 33 00 32 00 33 00 20 00 2D 00 31 00        8.1.3.2.3...-.1.
20 00 31 00 31 00 35 00 30 00 32 00 36 00 36 00        ..1.1.5.0.2.6.6.
38 00 31 00 33 00 32 00 33 00 20 00 2D 00 32 00        8.1.3.2.3...-.2.
35 00 35 00 20 00                                      5.5...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete | CommandQueueEnqueue | Client Commands