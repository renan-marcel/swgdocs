---
title: Placestructure (7AF26B0B)
url: https://wiki.swganh.org/index.php/Placestructure_%287AF26B0B%29
page_type: Command
opcode: 7AF26B0B
revision_id: 9402
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Placestructure (7AF26B0B)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| UNICODE String |  |
| Operand 1 | Structure ID |
| Operand 2 | Coord X |
| Operand 3 | Coord Y |
| Operand 4 | direction |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 7AF26B0B

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
00 09 00 77 
05 00 
46 5E CE 80 23 00 00 00 16 01 00 00 

E5 55 DB 70 05 00 00 00 
00 00 00 00 00 00 00 00 

0B 6B F2 7A                          Opcode place structure

00 00 00 00 
00 00 00 00 
// start Unicode string
1E 00 00 00 

31 00 31 00 39 00 30 00 37 00 37 00 36 00              ..1.1.9.0.7.7.6.
32 00 37 00 34 00 39 00 30 00 20 00 31 00 35 00        2.7.4.9.0...1.5.
31 00 36 00 2E 00 30 00 38 00 20 00 35 00 32 00        1.6...0.8...5.2.
35 00 31 00 2E 00 39 00 32 00 20 00 30 00 8D 73        5.1...9.2...0..s
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands