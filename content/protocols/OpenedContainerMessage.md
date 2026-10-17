---
title: OpenedContainerMessage
url: https://wiki.swganh.org/index.php/OpenedContainerMessage
page_type: Server Packet
opcode: 2E11E4AB
revision_id: 257053
last_modified: 2013-09-19T22:09:17Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# OpenedContainerMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Priority Routing |
| INT | Opcode |
| LONG | Object ID |
| SHORT | ?? |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 2E11E4AB

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
NGE break by cAble 

02 00 # Operand
AB E4 11 2E #Opccode
11 00 00 00 #SlotType
16 A2 E6 92 39 00 00 00 #ObjectID
00 00 #Unknown Short
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete