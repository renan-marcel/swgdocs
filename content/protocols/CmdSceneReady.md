---
title: CmdSceneReady
url: https://wiki.swganh.org/index.php/CmdSceneReady
page_type: Client Packet
opcode: 43FD1C22
revision_id: 20936
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Server Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:ClientPacket', 'Template:100%']
---

# CmdSceneReady

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 43FD1C22

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
01 00       // Op Count
22 1C FD 43 // CmdSceneReady
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | Client Packets | 100% Complete