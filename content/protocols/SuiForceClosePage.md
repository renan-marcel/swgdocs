---
title: SuiForceClosePage
url: https://wiki.swganh.org/index.php/SuiForceClosePage
page_type: Server Packet
opcode: 990B5DE0
revision_id: 44404
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# SuiForceClosePage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | op Count |
| INT | Op Code |
| INT | Window ID |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 990B5DE0

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00        
E0 5D 0B 99  //SuiForceClosePage 
71 63 00 00  //Window ID
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete