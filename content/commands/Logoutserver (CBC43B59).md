---
title: Logoutserver (CBC43B59)
url: https://wiki.swganh.org/index.php/Logoutserver_%28CBC43B59%29
page_type: Command
opcode: CBC43B59
revision_id: 20338
last_modified: 2007-12-31T17:36:51Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ClientPacket', 'Template:100%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Logoutserver (CBC43B59)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | int1 |
| INT | CommandQueueEnqueue |
| LONG | Object ID |
| INT | 0 |
| INT | 0 |
| INT | CRC= Logoutserver |
| INT | 0 |
| INT | 0 |
| INT | 0 |

## Variable Descriptions
- Opcode		     = CBC43B59

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
71 E2 DB D9 00 00 00 00 // Object ID
00 00 00 00 
00 00 00 00 
50 59 B6 03 // logoutserver
00 00 00 00 
00 00 00 00 
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete | CommandQueueEnqueue | Client Commands