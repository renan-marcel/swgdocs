---
title: DeltasMessage
url: https://wiki.swganh.org/index.php/DeltasMessage
page_type: Server Packet
opcode: 12862153
revision_id: 18685
last_modified: 2007-12-06T15:03:49Z
completion: 100%
direction: S→C
sample_status: placeholder
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Uncertain', 'Template:ServerPacket', 'Template:100%', 'Template:PacketBaselines', 'Template:PacketDeltas']
---

# DeltasMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| INT | Object_TYPE |
| BYTE | TYPE_# |
| INT | Object_Data_Size |
| ? | Data |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 12862153

## Notes
- **NOTE:** This is just a string used in the debugging message.

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
Packets | Server Packets | 100% Complete
<!-- pswgcommon:start -->

## Referência de implementação PSWGCommon

[Implementação PSWGCommon: envelope delta, índices e dados de atualização.](../guides/pswgcommon-network.md)

Análise de fontes; não altera o status de verificação desta página.

<!-- pswgcommon:end -->
