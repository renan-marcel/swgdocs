---
title: GrantCommand
url: https://wiki.swganh.org/index.php/GrantCommand
page_type: Server Packet
opcode: E67E3875
revision_id: 257255
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Ascii', 'Template:ServerPacket', 'Template:100%']
---

# GrantCommand

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| SHORT | StringSize |
| ASCII | CommandGranted |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = E67E3875

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 #Operand
75 38 7E E6 #Opcode
07 00 #StringSize
63 6F 5F 64 6D 5F 31 #CommandGranted #co_dm_1


Note: the RevokeCommand gets sent to remove all the skills and abilities of the former profession.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete