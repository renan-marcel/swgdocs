---
title: Spatialchatinternal (7C8D63D4)
url: https://wiki.swganh.org/index.php/Spatialchatinternal_%287C8D63D4%29
page_type: Command
opcode: 7C8D63D4
revision_id: 58858
last_modified: 
completion: 0%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '0% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:0%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Spatialchatinternal (7C8D63D4)

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
- Opperand_Count	     =
- Opcode		     = 7C8D63D4

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **0%** - This packet has not been reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
----

"7C8D63D4",0,0,14,"0 0 0 0 1 bank"
"7C8D63D4",0,0,23,"0 0 0 0 1 deposit money"
"7C8D63D4",0,0,47,"0 0 0 0 1 5 credit deposit will do this 3 times"

05 00 
46 5E CE 80 
23 00 00 00 
16 01 00 00 
EE B4 79 8B 33 00 00 00 // characterID
00 00 00 00 
00 00 00 00 
D4 63 8D 7C // Spatialchatinternal
00 00 00 00 
00 00 00 00 
2E 00 00 00 
30 00 20 00 
38 00 30 00 
20 00 30 00 
20 00 30 00 
20 00 31 00 
20 00 
79 00 6F 00 20 00 // y.o.
68 00 6F 00 20 00 // h.o.
68 00 6F 00 20 00 // h.o.
69 00 74 00 73 00       //i.t.s.
20 00 61 00 20 00 70 00 69 00 72 00 61 00 74 00   // ..a...p.i.r.a.t.
65 00 73 00 20 00 6C 00 69 00 66 00 65 00 20 00   // e.s...l.i.f.e...
66 00 6F 00 72 00 20 00 6D 00 65 00 21 00         // f.o.r...m.e.!.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 0% Complete | CommandQueueEnqueue | Client Commands