---
title: BUIO06
url: https://wiki.swganh.org/index.php/BUIO06
page_type: Baseline
opcode: 
revision_id: 257265
last_modified: 2014-01-22T14:47:09Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', '100% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:BUIOArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:100%', 'Template:ServerPacket']
---

# BUIO06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Baseline Opcode |
| LONG | Object ID |
| INT | OIUB |
| BYTE | 6 |
| SHORT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **100%** - This packet has been completely reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68 
56 33 23 6F 02 00 00 00 
4F 49 55 42 06  // OIUB 6
02 00 
42 00 00 00 
00 00 00 00 
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 100% Complete | Server Packets