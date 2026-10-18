---
title: UpdateTransformMessage
url: https://wiki.swganh.org/index.php/UpdateTransformMessage
page_type: Server Packet
opcode: 1B24F808
revision_id: 258792
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# UpdateTransformMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| LONG | ObjectID |
| SHORT | PositionX |
| SHORT | PositionY |
| SHORT | PositionZ |
| INT | UpdateCounter |
| BYTE | Speed |
| BYTE | Direction |

## Variable Descriptions
- Opperand_Count	     = 8
- Opcode		     = 1B24F808

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
08 00 // op count
08 F8 24 1B // UpdateTransformMessage
EB 4F 90 19 17 00 00 00 // object ID
AD CF // x
7C 00 // y
CB 2B // z
03 03 00 00 // counter
00 // Speed
2F // direction

08 00 //opcount
08 F8 24 1B // UpdateTransformMessage
D5 4F 90 19 17 00 00 00 // ID
FA CF // x -3073.5
7C 00 // y 31
11 2C // z 2820.25
6E 02 00 00 // update counter
00 // speed
E7 // direction
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete