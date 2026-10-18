---
title: ClientIdMsg
url: https://wiki.swganh.org/index.php/ClientIdMsg
page_type: Client Packet
opcode: D5899226
revision_id: 257143
last_modified: 
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Unknown', 'Template:B string', 'Template:ClientPacket', 'Template:75%']
---

# ClientIdMsg

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | ?? |
| INT | Opcode |
| B_STRING | Session_Hash |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = D5899226

## Notes
- **NOTE:** B_STRING has a size of 4, but 1 character per byte. Only found in session_hash.
- **NOTE:** This packet can be used to pass information from the login server to the zone server

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
Ongoing piece of work by cAble (Nge packet reverser) 


04 00 #Operand
26 92 89 D5 #Opcode
00 00 00 00 #getGameBitsToClear 
38 00 00 00 #Token
20 00 00 00 

15 00 00 00 


AF 53 60 76 66 CD E0 58 B4 85 DC F5 60 A2 BE 44 53 C2 E3 CA 47 20 DC 6A 7E 23
FB C0 13 C9 6D BC B3 91 47 79 FB 22 90 47 35 93
30 31 36 4F 4E C8 0E 00 32 30 31 31 31 31 33 30
2D 31 35 3A 34 36
```

## Related Pages
- [[LoginClientToken]]

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete