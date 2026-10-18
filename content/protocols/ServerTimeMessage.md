---
title: ServerTimeMessage
url: https://wiki.swganh.org/index.php/ServerTimeMessage
page_type: Server Packet
opcode: 2EBC3BD9
revision_id: 21495
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ServerPacket', 'Template:100%']
---

# ServerTimeMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | Galactic_Time |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 2EBC3BD9

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00                    //World Update
 D9 3B BC 2E              //ServerTimeMessage
 4E 9F 71 DE 46 00 00 00  //Time in ms
```

## Related Pages
- [[CmdStartScene]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete