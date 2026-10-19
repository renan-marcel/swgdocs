---
title: ObjectMenuSelectMessage::MESSAGE TYPE
url: https://wiki.swganh.org/index.php/ObjectMenuSelectMessage%3A%3AMESSAGE_TYPE
page_type: Client Packet
opcode: 7CA18726
revision_id: 79413
last_modified: 2012-10-03T07:03:26Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:ClientPacket', 'Template:100%']
---

# ObjectMenuSelectMessage::MESSAGE TYPE

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| BYTE | MessageType |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 7CA18726

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00   //'ACCOUNTUPDATE
 26 87 A1 7C   //'ObjectMenuSelectMessage::MESSAGE_TYPE
 CE A9 03 E3 1E 00 00 00 //Item ID
 00 //Message Type
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete