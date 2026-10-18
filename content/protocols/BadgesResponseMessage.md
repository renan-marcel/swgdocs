---
title: BadgesResponseMessage
url: https://wiki.swganh.org/index.php/BadgesResponseMessage
page_type: Server Packet
opcode: 6D89D25B
revision_id: 78278
last_modified: 2011-04-08T19:30:04Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Beginlist', 'Template:Endlist', 'Template:ServerPacket', 'Template:100%']
---

# BadgesResponseMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | CharacterID |
| INT | Bit Masks Count (# of Bitmasks) |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = 6D89D25B
- int h = highestBadgeIndexNumber; //From the badge_map.iff
- int numberOfBitmasks = ceil(h / 32);

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
03 00                          // ACCOUNTUPDATE
5B D2 89 6D                    // BadgesResponseMessage
19 00 00 00 00 00 00 00        // CharacterID
0F 00 00 00                    // Size of Bitmask List (15)
0F F0 EF CD                    // Bitmask 1
C0 10 0B 00                    // Bitmask 2
02 7C 4A 89                    // Bitmask 3
36 98 00 14                    // Bitmask 4
00 10 00 A0                    // Bitmask 5
00 18 02 00                    // Bitmask 6
10 00 00 00                    // Bitmask 7
00 00 00 00                    // Bitmask 8
00 00 00 00                    // Bitmask 9
00 00 00 00                    // Bitmask 10
00 00 00 00                    // Bitmask 11
00 00 00 00                    // Bitmask 12
00 00 00 00                    // Bitmask 13
00 00 00 00                    // Bitmask 14
00 00 00 00                    // Bitmask 15
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete