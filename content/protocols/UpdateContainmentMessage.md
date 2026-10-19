---
title: UpdateContainmentMessage
url: https://wiki.swganh.org/index.php/UpdateContainmentMessage
page_type: Server Packet
opcode: 56CBDE9E
revision_id: 79402
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# UpdateContainmentMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| LONG | Parent Id |
| INT | Arrangement Id |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 56CBDE9E

## Notes

<!-- pswgcommon-message-crosscheck:start -->
### PSWGCommon / client cross-check

PSWGCommon encodes 26 bytes: operand count 4 at offset 0, opcode 56CBDE9E at 2, objectId (8 bytes) at 6, containerId (8 bytes) at 14, and slotIndex (4 bytes) at 22. Offsets start at the SWG message and exclude SOE framing; integers are little-endian.

The client reader at 0x00ADC6D0 registers two NetworkId fields and one int in that order (object members +0x38, +0x48, +0x58). These are in-memory offsets, not packet offsets. This corroborates the field sequence; arrangement/slot semantics and special values are not established by the registration alone.

See [client message analysis](../guides/pswgcommon-client-messages.md). Evidence: [BN-PSWG-CONTAIN-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CONTAIN-READ.json).
<!-- pswgcommon-message-crosscheck:end -->

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00       //Operand_Count
9E DE CB 56 //UpdateContainmentMessage
62 C9 8B 12 1E 00 00 00 //Object ID
FD 85 10 00 00 00 00 00 //Cell ID
FF FF FF FF //ContainmentType?
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete