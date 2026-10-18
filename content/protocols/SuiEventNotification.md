---
title: SuiEventNotification
url: https://wiki.swganh.org/index.php/SuiEventNotification
page_type: Server Packet
opcode: 092D3564
revision_id: 67323
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Server Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:U string', 'Template:ServerPacket', 'Template:ClientPacket', 'Template:100%']
---

# SuiEventNotification

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | op Count |
| INT | Op Code |
| INT | Window ID |
| INT | action (bool - true if cancel pressed) |
| INT | item count n |
| INT | item count n |
| U_STRING | Submitted Data string 1...n |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 092D3564

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00 
 64 35 2D 09                                                            //SuiEventNotification 
 83 49 02 00                                                            //Window ID
 00 00 00 00 
 02 00 00 00 
 02 00 00 00 
 0E 00 00 00                                                           //UNICODE STRING SIZE(14)
 66 00 75 00 63 00 6B 00 73 00 6F 00 65 00 62 00 69 00 74 00 
 63 00 68 00 65 00 73 00                                               //UNICODE ('fucksoebitches')
 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | Client Packets | 100% Complete