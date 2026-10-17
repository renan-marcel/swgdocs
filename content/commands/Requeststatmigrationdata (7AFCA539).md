---
title: Requeststatmigrationdata (7AFCA539)
url: https://wiki.swganh.org/index.php/Requeststatmigrationdata_%287AFCA539%29
page_type: Command
opcode: 7AFCA539
revision_id: 22471
last_modified: 2008-02-08T05:06:50Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:Long', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Requeststatmigrationdata (7AFCA539)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | Object Controller |
| INT | ?? |
| INT | CommandQueueEnqueue |
| LONG | Character ID |
| INT | 0 |
| INT | 0 |
| INT | Requeststatmigrationdata |
| INT | Character ID |
| INT | 0 |

## Variable Descriptions
- Opperand_Count	     = 10
- Opcode		     = 7AFCA539

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
05 00 // Op Count
46 5E CE 80 // ObjectControllerMessage
23 00 00 00 
16 01 00 00 // CommandQueueEnqueue
D9 59 00 00 02 00 00 00 // Toon ID
00 00 00 00 
00 00 00 00 
39 A5 FC 7A // requeststatmigrationdata
D9 59 00 00 02 00 00 00 // Toon ID
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands