---
title: GetMapLocationsMessage
url: https://wiki.swganh.org/index.php/GetMapLocationsMessage
page_type: Client Packet
opcode: 1A7AB839
revision_id: 20491
last_modified: 2008-01-01T09:31:16Z
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Float', 'Template:Byte', 'Template:ClientPacket', 'Template:100%']
---

# GetMapLocationsMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | Planet_String |
| FLOAT | X cord |
| FLOAT | Z cord |
| BYTE | Category |
| BYTE | SubCategory |
| BYTE | Icon |

## Variable Descriptions
- Opperand_Count	     = 05
- Opcode		     = 1A7AB839

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 // Op Count
39 B8 7A 1A // GetMapLocationsMessage
05 00 // sting count
65 6E 64 6F 72 // endor
17 00 00 00 
01 00 00 00 
01 
00 
00 
------------------------------------------
05 00 // Op Count
39 B8 7A 1A // GetMapLocationsMessage
08 00 // string count
64 75 6E 67 65 6F 6E 31 // dungeon1
00 00 00 00 
00 00 00 00 
00 
00 
00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete