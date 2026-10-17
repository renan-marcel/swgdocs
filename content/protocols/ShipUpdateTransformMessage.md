---
title: ShipUpdateTransformMessage
url: https://wiki.swganh.org/index.php/ShipUpdateTransformMessage
page_type: Server Packet
opcode: 76026FB9
revision_id: 26082
last_modified: 2008-04-03T12:58:51Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# ShipUpdateTransformMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | priority routing |
| INT | Opcode |
| LONG | ObjectID |
| SHORT | Cord X |
| SHORT | Cord Y |
| SHORT | Cord Z |
| INT | Update Counter |
| BYTE | Posture |
| BYTE | Direction |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 76026FB9

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 // Op Count
B9 6F 02 76// ShipupdateTransformMessage
1F 0A 74 F0 D0 FA C8 46 // ObjectID
44 DF // X
B8 AE // Y
00 03 // Z
4A 86 00 00 // UpdateCounter
00 // Posture
C7 // Direction


----------------------------------------------------------------------
ShipUpdateTransformMessage

05 00 B9 6F 02 76 FB 02 EF 00 7D 04 54 58 F3 A8        ...o.v....}.TX..
5C CC FF 04 43 A3 00 00 00 19 EC 4D E8                 \...C......M.

-----------------------------------------------------------------------

SubMultiPacket

ShipUpdateTransformMessage

05 00 B9 6F 02 76 93 03 4A 08 65 F5 9B 44 F7 DB        ...o.v..J.e..D..
5E E3 B8 01 C9 69 00 00 00 19 EC 4D E8                 ^....i.....M.

-----------------------------------------------------------------------

SubMultiPacket

ShipUpdateTransformMessage

05 00 B9 6F 02 76 37 00 B5 D6 50 D3 69 4F 8F C5        ...o.v7...P.iO..
DA C7 BF 06 A5 E5 00 00 00 19 EC 4D E8                 ...........M.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete