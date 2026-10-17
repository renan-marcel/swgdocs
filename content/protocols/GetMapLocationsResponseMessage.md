---
title: GetMapLocationsResponseMessage
url: https://wiki.swganh.org/index.php/GetMapLocationsResponseMessage
page_type: Server Packet
opcode: 9F80464C
revision_id: 78286
last_modified: 
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:75%']
---

# GetMapLocationsResponseMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | Planet |
| INT | List |
| LONG | id |
| U_STRING | Name |
| FLOAT | X |
| FLOAT | Y |
| BYTE | isCategory |
| BYTE | isSubCategory |
| BYTE | isActive |
| INT | List |
| LONG | id |
| U_STRING | Name |
| FLOAT | X |
| FLOAT | Y |
| BYTE | isCategory |
| BYTE | isSubCategory |
| BYTE | isActive |
| INT | List |
| LONG | id |
| U_STRING | Name |
| FLOAT | X |
| FLOAT | Y |
| BYTE | isCategory |
| BYTE | isSubCategory |
| BYTE | isActive |
| INT | Unknown |
| INT | Unknown |
| INT | Unknown |

## Variable Descriptions
- Opperand_Count	     = 28
- Opcode		     = 9F80464C

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
00 09 1D BA 
08 00       // opcount
4C 46 80 9F // GetMapLocationsResponseMessage
03 00              // string count
6C 6F 6B 00        // lok
00 00 00 00 
00 00 00 00 
00 00 00 72 
02 00 00 E4      
04 00 00 01 
00 00 
00 2F 2D // comp+crc
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete