---
title: ClientPermissionsMessage
url: https://wiki.swganh.org/index.php/ClientPermissionsMessage
page_type: Server Packet
opcode: E00730E5
revision_id: 19854
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# ClientPermissionsMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| BYTE | Galaxy_Open_Flag |
| BYTE | CharacterSlot_Open_Flag |
| BYTE | Unlimited_CharCreation_Flag |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = E00730E5

## Notes
- **NOTE:** Unlimited_CharCreation_Flag OVERRIDES this.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00         //Operand_Count
E5 30 07 E0   //Opcode ClientPermissionsMessage

01            //Galaxy_Open_Flag
01            //CharacterSlot_Open_Flag
00            //Unlimited_CharCreation_Flag

00 67 B8      //Comp flag, crc
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete