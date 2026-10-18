---
title: ChatCreateRoom
url: https://wiki.swganh.org/index.php/ChatCreateRoom
page_type: Packet
opcode: 35366BED
revision_id: 39868
last_modified: 2008-06-27T05:24:55Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:A string', 'Template:ClientPacket', 'Template:100%']
---

# ChatCreateRoom

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| BYTE | Permission Flag |
| BYTE | Moderation Flag |
| SHORT | ? |
| A_STRING | Room Address |
| A_STRING | Room Title |
| INT | Counter |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = 0x35366BED

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
07 00 				// OpCount
ED 6B 36 35 			// ChatCreateRoom
01 				// public flag
00 				// moderated flag

00 00				// unknown

30 00 
53 57 47 2E 47 6F 72 61 74 68 2E 67 72 6F 75 70       
2E 31 36 31 34 31 38 33 30 39 32 32 31 2E 47 72       
6F 75 70 43 68 61 74 2E 52 6F 6F 6D 4E 61 6D 65    
//"SWG.Gorath.group.161418309221.GroupChat.RoomName" 

09 00
52 6F 6F 6D 54 69 74 6C 65     // "RoomTitle"				

05 00 00 00     	       // Counter
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete