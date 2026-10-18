---
title: ConnectPlayerResponseMessage
url: https://wiki.swganh.org/index.php/ConnectPlayerResponseMessage
page_type: Server Packet
opcode: 6137556F
revision_id: 22129
last_modified: 2008-01-24T16:47:42Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# ConnectPlayerResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | ?? |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 6137556F

## Notes
- **TODO:** Look into when this packet is used in the login process.

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
02 00 // Op Count
6F 55 37 61 // ConnectPlayerResponseMessage
00 00 00 00 // ??
------------------------
CU log
========================
02 00 
6F 55 37 61 
00 00 00 00 
12 
03 00 
94 B5 7A E9 //unknown opcode
AA ED AC 2F 17 00 00 00 
00 00 00 00 
12 
03 00 
B0 75 C2 F8 // unknown opcode
AA ED AC 2F 17 00 00 00 
00 00 00 00
```

## Related Pages
- [[ConnectPlayerMessage]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete