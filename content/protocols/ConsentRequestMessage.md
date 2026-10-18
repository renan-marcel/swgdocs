---
title: ConsentRequestMessage
url: https://wiki.swganh.org/index.php/ConsentRequestMessage
page_type: Server Packet
opcode: 99DCB094
revision_id: 78564
last_modified: 2011-07-12T09:26:20Z
completion: 100%
direction: S→C
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# ConsentRequestMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpperandCount |
| INT | Opcode |
| ASTRING | BaseMessageSTF |
| INT | Spacer |
| ASTRING | BaseMessageString |
| LONG | ObjectID |
| ASTRING | STFFile |
| INT | Spacer |
| ASTRING | STFString |
| USTRING | String |
| LONG | ObjectID |
| ASTRING | STFFile |
| INT | Spacer |
| ASTRING | STFString |
| USTRING | String |
| LONG | ObjectID |
| ASTRING | STFFile |
| INT | Spacer |
| ASTRING | STFString |
| USTRING | String |
| INT | Integer |
| FLOAT | Float |
| BYTE | DisplayFlag?(00-Display,01-Blank) |
| INT | ConsentID |

## Variable Descriptions
- Opperand_Count		= 3
- Opcode			= 99DCB094

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
Insert Sample Packet Here...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete