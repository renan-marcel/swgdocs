---
title: ChatOnEnteredRoom
url: https://wiki.swganh.org/index.php/ChatOnEnteredRoom
page_type: Server Packet
opcode: E69BDC0A
revision_id: 19406
last_modified: 2007-12-22T04:07:42Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete', 'Nogard']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# ChatOnEnteredRoom

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| A_STRING | Game Name |
| A_STRING | Galaxy Name |
| A_STRING | Character Name |
| INT | Success Bitmask |
| INT | ChatRoom_ID |
| INT | Nothing |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = E69BDC0A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
0A DC 9B E6                 //CRC = 'ChatOnEnteredRoom 
03 00                       //INT(3) 
53 57 47                    //'SWG'
09 00                       //INT(9) 
43 6F 72 62 61 6E 74 69 73  //'Corbantis' 
07 00                       //INT(7)
61 72 79 73 6C 61 74        //'aryslat' 
00 00 00 00 
78 9E 6E 01                 //ChatRoom ID
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete | Nogard