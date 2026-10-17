---
title: PlayClientEffectObjectTransformMessage
url: https://wiki.swganh.org/index.php/PlayClientEffectObjectTransformMessage
page_type: Server Packet
opcode: 4F5E09B6
revision_id: 59629
last_modified: 
completion: 0%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '0% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:0%']
---

# PlayClientEffectObjectTransformMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| BYTE | uint8 |
| SHORT | uint16 |
| INT | uint32 |
| FLOAT | uint32 |
| LONG | uint64 |
| A_STRING | ASCII String |
| U_STRING | Unicode String |
| C_STRING | Customization String |
| B_STRING | Byte String |
| { } | LIST Component |
| ? | Uncertain Values |
| ?? | Unknown Variable Name |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = 4F5E09B6

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **0%** - This packet has not been reversed.

## Sample Packet
```
Opcode[1331562934]05 00 B6 09 5E 4F 1B 00 61 70 70 65 61 72 61 6E 63 65 2F 70 74 5F 6C 6F 6F 74 5F 64 69 73 63 2E 70 72 74 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 00 00 00 00 33 33 33 3F 00 00 00 00 39 94 CF 02 25 00 00 00 06 00 6C 6F 6F 74 4D 65 

....^O..appearance/pt_loot_disc.prt...............?....333?....9...%.....lootMe
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 0% Complete