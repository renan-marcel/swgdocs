---
title: DestroyShipMessage
url: https://wiki.swganh.org/index.php/DestroyShipMessage
page_type: Server Packet
opcode: 5C680884
revision_id: 59648
last_modified: 2009-08-24T01:27:12Z
completion: 0%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '0% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:0%']
---

# DestroyShipMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

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
- Opcode		     = 5C680884

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **0%** - This packet has not been reversed.

## Sample Packet
```
03 00 84 08 68 5C EA 17 53 BF 21 00 00 00 57 AC 50 3F 

03 00 84 08 68 5C 45 19 53 BF 21 00 00 00 49 52 83 3D 

03 00 84 08 68 5C 1A 1A 53 BF 21 00 00 00 F0 F1 64 3F 

03 00 84 08 68 5C 21 1A 53 BF 21 00 00 00 4D 8F 58 3E 

03 00 84 08 68 5C 28 19 53 BF 21 00 00 00 41 F9 2E 3F 

03 00 84 08 68 5C 48 2A 53 BF 21 00 00 00 12 C4 82 3E
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 0% Complete