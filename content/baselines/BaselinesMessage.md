---
title: BaselinesMessage
url: https://wiki.swganh.org/index.php/BaselinesMessage
page_type: Server Packets
opcode: 68A75F0C
revision_id: 78421
last_modified: 2011-07-06T00:30:28Z
completion: 50%
direction: S→C
sample_status: absent
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Uncertain', 'Template:ServerPacket', 'Template:50%', 'Template:PacketBaselines']
---

# BaselinesMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| LONG | ObjectID |
| INT | Object_TYPE |
| BYTE | TYPE_# |
| INT | Object_Data_Size |
| ? | Data |

## Variable Descriptions
- Operand_Count	     = 5
- Opcode		     = 68A75F0C

## Notes
- **NOTE:** This is just a string used in the debugging message. Parsing methods are set on object creation.

## Tags
- **S→C** - This packet originates on the server.
- **50%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete