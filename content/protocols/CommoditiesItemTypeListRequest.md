---
title: CommoditiesItemTypeListRequest
url: https://wiki.swganh.org/index.php/CommoditiesItemTypeListRequest
page_type: Client Packet
opcode: 48F493C5
revision_id: 20963
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ClientPacket', 'Template:100%']
---

# CommoditiesItemTypeListRequest

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | From String |

## Variable Descriptions
- Opperand_Count	     = 02
- Opcode		     = 48F493C5

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
C5 93 F4 48 // CommoditiesItemTypeListRequest
0F 00                                        // string count
53 68 61 64 6F 77 66 69 72 65 2E 34 33 30 33 // Shadowfire.4303
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete