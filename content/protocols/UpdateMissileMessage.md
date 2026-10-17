---
title: UpdateMissileMessage
url: https://wiki.swganh.org/index.php/UpdateMissileMessage
page_type: Server Packet
opcode: 1228CD01
revision_id: 59551
last_modified: 
completion: 0%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '0% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:0%']
---

# UpdateMissileMessage

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
- Opperand_Count	     = X
- Opcode		     = 1228CD01

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **0%** - This packet has not been reversed.

## Sample Packet
```
Processing:C:\cap2\list_2_jtl.pcap

05 00 01 CD 28 12 F9 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 FB 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 FC 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 FE 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 FD 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 FF 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

05 00 01 CD 28 12 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 04 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 06 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 17 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 2C 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

Processing:C:\cap2\instinct_JTL_6.pcap
05 00 01 CD 28 12 9E 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 9F 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A0 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A3 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A1 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A2 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A4 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A6 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A8 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 A9 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 AA 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 AE 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 AF 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 B0 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 B1 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 B2 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 B3 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 

05 00 01 CD 28 12 B5 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 0% Complete