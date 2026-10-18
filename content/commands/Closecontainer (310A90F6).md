---
title: Closecontainer (310A90F6)
url: https://wiki.swganh.org/index.php/Closecontainer_%28310A90F6%29
page_type: Command
opcode: 310A90F6
revision_id: 29727
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Closecontainer (310A90F6)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Container ID |
| INT | null bytes |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 310A90F6

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
05 00 
46 5E CE 80 //ObjControllerMessage
23 00 00 00 
16 01 00 00 //Command Queue Enqueue
47 76 BB BB 2F 00 00 00 //character id
00 00 00 00 
20 00 00 00 //tick count
F6 90 0A 31 //Close Container
4B 76 BB BB 2F 00 00 00 //container id 
00 00 00 00 
----

"310A90F6",1664,144573371814,0,""
"310A90F6",288,111466501565,0,""
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands