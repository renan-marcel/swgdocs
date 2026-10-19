---
title: LinkDeadMessage
url: https://wiki.swganh.org/index.php/LinkDeadMessage
page_type: Server Packet
opcode: A16CF9AF
revision_id: 79390
last_modified: 2012-07-19T21:31:03Z
completion: 0%
discovery_source: "Wiki SWGANH"
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '0% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:0%']
---

# LinkDeadMessage

> [!NOTE]
> **Origem da Descoberta: Wiki SWGANH**
> Esta entrada foi catalogada originalmente na Wiki do SWGANH (completude de 0%). A estrutura do pacote e seus campos permanecem pendentes de reversão e validação binária.

## Notices
_none_

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
- Opcode		     = A16CF9AF

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **0%** - This packet has not been reversed.

## Sample Packet
```
01 00 AF F9 6C A1
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 0% Complete