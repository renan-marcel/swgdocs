---
title: LaunchBrowserMessage
url: https://wiki.swganh.org/index.php/LaunchBrowserMessage
page_type: Server Packet
opcode: 8DE7E213
revision_id: 44890
last_modified: 2008-09-04T17:57:44Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:100%']
---

# LaunchBrowserMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | OpCode |
| A_STRING | URL |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 0x8DE7E213

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
09 00
13 E2 E7 8D                    // opcode
0A 00                          // string size
73 77 67 61 6E 68 2E 63 6F 6D  // swganh.com
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete