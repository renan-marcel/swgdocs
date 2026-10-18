---
title: ChatQueryRoom
url: https://wiki.swganh.org/index.php/ChatQueryRoom
page_type: Client Packet
opcode: 92B1F29C
revision_id: 20956
last_modified: 2008-01-06T23:19:12Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ClientPacket', 'Template:75%']
---

# ChatQueryRoom

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| INT | ?? |
| A_STRING | Room Name |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 92B1F29C

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
03 00 
92 B1 F2 9C                                      // ChatQueryRoom
01 00 00 00 
22 00                                            // string count
53 57 47 2E 53 68 61 64 6F 77 66 69 72 65 2E 74  // SWG.Shadowfire.t
75 74 6F 72 69 61 6C 2E 43 68 61 74 2E 72 6F 75  // utorial.Chat.rou
73 65                                            // se
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete