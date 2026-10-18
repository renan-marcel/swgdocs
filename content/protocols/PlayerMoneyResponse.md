---
title: PlayerMoneyResponse
url: https://wiki.swganh.org/index.php/PlayerMoneyResponse
page_type: Server Packet
opcode: 367E737E
revision_id: 256889
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# PlayerMoneyResponse

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | CreditsBank |
| INT | CreditsInventory |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 367E737E

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 # Operand
7E 73 7E 36 # Opcode
B8 B3 0A 00 # CreditsBank
AF EB 00 00 # CreditsInventory 

NGE struct from cAble projectswg
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete