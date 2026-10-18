---
title: GalaxyLoopTimesResponse
url: https://wiki.swganh.org/index.php/GalaxyLoopTimesResponse
page_type: Server Packet
opcode: 4E428088
revision_id: 19738
last_modified: 2007-12-27T21:37:31Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Byte', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# GalaxyLoopTimesResponse

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| BYTE | op count |
| INT | opcode |
| INT | Time |
| INT | Time |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 4E428088

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00 
88 80 42 4E // GalaxyLoopTimesResponse
34 DF 04 00 // time
34 DF 04 00 // time
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete