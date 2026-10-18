---
title: ChatPersistentMessageToServer
url: https://wiki.swganh.org/index.php/ChatPersistentMessageToServer
page_type: Client Packet
opcode: 25A29FA6
revision_id: 20950
last_modified: 2008-01-06T23:17:34Z
completion: 75%
direction: C→S
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:U string', 'Template:A string', 'Template:ClientPacket', 'Template:75%']
---

# ChatPersistentMessageToServer

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | Opcode |
| U_STRING | Mail Body |
| INT | Filler? |
| INT | ??? |
| U_STRING | Mail Subject |
| INT | Filler |
| A_STRING | Recipient |

## Variable Descriptions
- Operand_Count	     = 6
- Opcode		     = 25A29FA6

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
Insert Sample Packet Here...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Client Packets | Server Packets | 75% Complete