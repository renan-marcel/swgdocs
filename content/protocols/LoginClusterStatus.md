---
title: LoginClusterStatus
url: https://wiki.swganh.org/index.php/LoginClusterStatus
page_type: Server Packet
opcode: 3436AEB6
revision_id: 21601
last_modified: 2008-01-10T00:45:02Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Beginlist', 'Template:A string', 'Template:Byte', 'Template:Endlist', 'Template:ServerPacket', 'Template:100%']
---

# LoginClusterStatus

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| INT | Server_Count |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = 3436AEB6

## Notes
- **NOTE:** This seems to be old data floating around.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
B6 AE 36 34 // LoginClusterStatus
19 00 00 00 // Total Number of Servers
02 00 00 00 // Server ID
0C 00 // String Count
31 39 39 2E 31 30 38 2E 36 2E 33 39 // 199.108.6.39
AF AD // Server Port
AE AD // Ping Port
FF FF FF FF <--------------------------this here
02 00 00 00  // server pop
08 00 00 00  // Max Cap
80 8F FF FF  // Max char per server
02 00 00 00  // Distance
01           // Status
C4 09 00 00  // Recommended flag
FA 00 00 00  // ??
03 00 00 00 
0C 00 
31 39 39 2E 31        ............199.
30 38 2E 36 2E 37 35 AF AD AE AD FF FF FF FF 01        108.6.75........
00 00 00 08 00 00 00 80 8F FF FF 02 00 00 00 01        ................
C4 09 00 00 FA 00 00 00 

0C 00 00 00 0D 00 31 39        ...............1
39 2E 31 30 38 2E 36 2E 31 33 33 AF AD AE AD FF        99.108.6.133....
FF FF FF 02 00 00 00 08 00 00 00 80 8F FF FF 02        ................
00 00 00 00 C4 09 00 00 FA 00 00 00 

0D 00 00 00        ................
0D 00 31 39 39 2E 31 30 38 2E 36 2E 31 38 33 AF        ...199.108.6.183
AD AE AD FF FF FF FF 01 00 00 00 08 00 00 00 80        ................
8F FF FF 02 00 00 00 00 C4 09 00 00 FA 00 00 00        ................

0E 00 00 00 0D 00 31 39 39 2E 31 30 38 2E 38 2E        .......199.108.8
31 30 31 AF AD AE AD FF FF FF FF 01 00 00 00 08        .101............
00 00 00 80 8F FF FF 02 00 00 00 00 C4 09 00 00        ................
FA 00 00 00 

0F 00 00 00 0D 00 31 39 39 2E 31 30        ...........199.1
38 2E 38 2E 31 34 35 AF AD AE AD FF FF FF FF 01        08.8.145........
00 00 00 08 00 00 00 80 8F FF FF 02 00 00 00 00        ................
C4 09 00 00 FA 00 00 00 

10 00 00 00 0C 00 31 39        ...............1
39 2E 31 30 38 2E 37 2E 35 31 AF AD AE AD FF FF        99.108.7.51.....
FF FF 01 00 00 00 08 00 00 00 80 8F FF FF 02 00        ................
00 00 00 C4 09 00 00 FA 00 00 00 

11 00 00 00 0C        ................
00 31 39 39 2E 31 30 38 2E 37 2E 38 30 AF AD AE        ..199.108.7.80..
AD FF FF FF FF 01 00 00 00 08 00 00 00 80 8F FF        ................
FF 02 00 00 00 00 C4 09 00 00 FA 00 00 00 12 00        ................
00 00 0D 00 31 39 39 2E 31 30 38 2E 37 2E 31 31        .....199.108.7.1
34 AF AD AE AD FF FF FF FF 01 00 00 00 08 00 00        14..............
00 80 8F FF FF 02 00 00 00 00 C4 09 00 00 FA 00        ................
00 00 13 00 00 00 0D 00 31 39 39 2E 31 94 8D           ........199.1..

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Packet : 9

TransOp:[0]
SOE_DATA_FRAG_A

199.108.6.33:44453 -> 192.168.0.150:1903 (Server -> Client)
Enc: T   Comp: T    Seed: 0xFB75D235

00 0D 00 05 30 38 2E 37 2E 31 34 30 AF AD AE AD        .....08.7.140...
FF FF FF FF 01 00 00 00 08 00 00 00 80 8F FF FF        ................
02 00 00 00 00 C4 09 00 00 FA 00 00 00 19 00 00        ................
00 0E 00 31 39 39 2E 31 30 38 2E 31 39 37 2E 35        ....199.108.197.
30 AF AD AE AD FF FF FF FF 01 00 00 00 08 00 00        50..............
00 80 8F FF FF 02 00 00 00 00 C4 09 00 00 FA 00        ................
00 00 1A 00 00 00 0E 00 31 39 39 2E 31 30 38 2E        .........199.108
31 39 37 2E 37 39 AF AD AE AD FF FF FF FF 01 00        .197.79.........
00 00 08 00 00 00 80 8F FF FF 02 00 00 00 00 C4        ................
09 00 00 FA 00 00 00 1B 00 00 00 0F 00 31 39 39        ..............19
2E 31 30 38 2E 31 39 37 2E 31 31 38 AF AD AE AD        9.108.197.118...
FF FF FF FF 01 00 00 00 08 00 00 00 80 8F FF FF        ................
02 00 00 00 00 C4 09 00 00 FA 00 00 00 1C 00 00        ................
00 0F 00 31 39 39 2E 31 30 38 2E 31 39 37 2E 31        ....199.108.197.
33 32 AF AD AE AD FF FF FF FF 01 00 00 00 08 00        132.............
00 00 80 8F FF FF 02 00 00 00 00 C4 09 00 00 FA        ................
00 00 00 05 00 00 00 0E 00 31 39 39 2E 31 30 38        ..........199.10
2E 31 39 36 2E 35 30 AF AD AE AD FF FF FF FF 02        8.196.50........
00 00 00 08 00 00 00 80 8F FF FF 02 00 00 00 00        ................
C4 09 00 00 FA 00 00 00 06 00 00 00 0E 00 31 39        ...............1
39 2E 31 30 38 2E 31 39 36 2E 38 31 AF AD AE AD        99.108.196.81...
FF FF FF FF 02 00 00 00 08 00 00 00 80 8F FF FF        ................
02 00 00 00 00 C4 09 00 00 FA 00 00 00 07 00 00        ................
00 0F 00 31 39 39 2E 31 30 38 2E 31 39 36 2E 31        ....199.108.196.
31 30 AF AD AE AD FF FF FF FF 01 00 00 00 08 00        110.............
00 00 80 8F FF FF 02 00 00 00 01 C4 09 00 00 FA        ................
00 00 00 08 00 00 00 0F 00 31 39 39 2E 31 30 38        ..........199.10
2E 31 39 36 2E 31 34 34 AF AD AE AD FF FF FF FF        8.196.144.......
01 00 00 00 08 00 00 00 80 8F FF FF 02 00 00 00        ................
01 C4 09 00 00 FA 00 00 00 09 00 00 00 0F 00 31        ................
39 39 2E 31 30 38 2E 31 39 36 2E 31 36 27 6C           99.108.196.16'l
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete