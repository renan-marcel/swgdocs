---
title: SHIP06
url: https://wiki.swganh.org/index.php/SHIP06
page_type: Baseline
opcode: 
revision_id: 256890
last_modified: 2013-08-15T06:09:25Z
completion: 50%
direction: unknown
sample_status: present
categories: ['Packets', 'Server Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:SHIPArchitectureNAV', 'Template:50%']
---

# SHIP06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| SHORT | ?? |
| FLOAT | ?? |
| FLOAT | Min Speed |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | ?? |
| FLOAT | Max Speed (see notes) |
| LONG | Ship Object ID |
| INT | ?? [1] |
| INT | ?? |
| INT | ?? [2] |
| INT | ?? [1] |
| INT | ?? |
| INT | List size |
| INT | List Update Counter |
| BYTE | ?? |
| INT | Component Index |
| INT | Component CRC |
| SHORT | ?? [3] |
| SHORT | ?? |
| SHORT | ?? |
| SHORT | ?? |
| FLOAT | Current Frontshield |
| FLOAT | Current Backshield |
| INT | ?? |

## Variable Descriptions
- Obj_OperandCount = 18
- The first 2 floats have been seen to be the same. The last float has been seen as 1/2 of the first 2 floats. Default Values = { 10.472f,10.472f,5.23599f }
- This is the _real_ max speed value. The display value for max speed is in SHIP1. This Value * 10 = Max Speed. (ex. if this = 45. 45 * 10 = 450 max speed)

## Notes
_none_

## Tags
- **50%** - This packet has been partially reversed.

## Sample Packet
```
05 00 0C 5F A7 68 04 5A D1 D6 13 00   ......._.h.Z....
00 00 50 49 48 53 06 B6 00 00 00 17 00 6E 00 00   ..PIHS.......n..
00 0F 00 73 74 72 69 6E 67 5F 69 64 5F 74 61 62   ...string_id_tab
6C 65 00 00 00 00 00 00 00 00 00 00 00 00 00 00   le..............
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00 00 00 00 00 00 73 00 00 00 04 00 00 00 1F 00   ......s.........
00 00 07 00 00 00 07 00 00 00 15 00 00 00 00 00   ................
00 00 00 04 FC 2E D7 00 01 00 00 00 3E 98 D3 79   ............>..y
00 02 00 00 00 CD E8 36 A4 00 04 00 00 00 FD 53   .......6.......S
08 B0 00 05 00 00 00 FD 53 08 B0 00 06 00 00 00   ........S.......
8F 6A A4 4C 00 07 00 00 00 91 D4 AB 5A 00 00 00   .j.L........Z...
00 00 00 00 00 00 00 75 44 00 00 75 44 00 00 00   .......uD..uD...
00 01 0A EA
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 50% Complete