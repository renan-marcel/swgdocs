---
title: ChatInstantMessageToClient
url: https://wiki.swganh.org/index.php/ChatInstantMessageToClient
page_type: Server Packet
opcode: 3C565CED
revision_id: 21071
last_modified: 2008-01-07T02:48:06Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ChatInstantMessageToClient

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | Game ID |
| A_STRING | Galaxy Name |
| A_STRING | Playername |
| U_STRING | Message |
| INT | 0 |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 3C565CED

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00             // Op Count
ED 5C 56 3C       // ChatInstantMessageToClient
03 00             // string count
53 57 47          // SWG = Game type
05 00             // string count
4C 6F 77 63 61    // Lowca = Server name
05 00             // string count
68 69 72 65 64    // hired = Player name
03 00 00 00       // u-string count
6C 00 6F 00 6C 00 // lol = message
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete