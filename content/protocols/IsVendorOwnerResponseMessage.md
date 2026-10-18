---
title: IsVendorOwnerResponseMessage
url: https://wiki.swganh.org/index.php/IsVendorOwnerResponseMessage
page_type: Server Packet
opcode: CE04173E
revision_id: 21467
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# IsVendorOwnerResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | operand Count |
| INT | OPCODE |
| INT | permission flag |
| INT | error msg |
| LONG | Terminal ID |
| A_STRING | ASCII String |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = CE04173E

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 02 CC 00 19 85 

06 00 

3E 17 04 CE                              opcode IsVendorOwnerResponseMessage

02 00 00 00 00 00 00 00 
F1 D7 14 00 00 00 00 00 

[ASCII]                                plane.region.terminal.location

dantooine.@dantooine_region_names:dantooine_mining_outpost.
@terminal_name:terminal_bazaar.1366001#-618,2490
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete