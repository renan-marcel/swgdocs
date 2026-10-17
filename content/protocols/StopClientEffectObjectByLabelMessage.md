---
title: StopClientEffectObjectByLabelMessage
url: https://wiki.swganh.org/index.php/StopClientEffectObjectByLabelMessage
page_type: Server Packet
opcode: AD6F6B26
revision_id: 17731
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# StopClientEffectObjectByLabelMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| A_STRING | Effect Label |

## Variable Descriptions
- Operand_Count	     = 4
- Opcode		     = AD6F6B26

## Notes
- **NOTE:** This packet is needed to make the remounting of swoops work. Without it the client will not move the swoop

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00 
26 6B 6F AD  //CRC = 'StopClientEffectObjectByLabelMessage 
AB F5 9A 8E 22 00 00 00 //mountID
09 00 76 65 68 69 63 6C 65 5F 32  'vehicle_2'
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete