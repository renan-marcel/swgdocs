---
title: StatMigrationTargetsMessage
url: https://wiki.swganh.org/index.php/StatMigrationTargetsMessage
page_type: Server Packet
opcode: EFAC38C4
revision_id: 28685
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# StatMigrationTargetsMessage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand |
| INT | Opcode |
| INT | Health Target |
| INT | Strength Target |
| INT | Constitution Target |
| INT | Action Target |
| INT | Quickness Target |
| INT | Stamina Target |
| INT | Mind Target |
| INT | Focus Target |
| INT | Willpower Target |
| INT | Points Remaining |

## Variable Descriptions
- Opperand_Count	     = 9
- Opcode		     = EFAC38C4

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
09 00 // Op Count
C4 38 AC EF // StatMigrationTargetsMessage
01 00 00 00 // Health
01 00 00 00 // Strength
01 00 00 00 // Constitution
01 00 00 00 // Action
01 00 00 00 // Quickness
01 00 00 00 // Stamina
01 00 00 00 // Mind
01 00 00 00 // Focus
01 00 00 00 // Willpower
01 00 00 00 // Points Left to Migrate
==================================================
Wookiee starting Ham for Artisan

09 00 // Op Count
C4 38 AC EF // StatMigrationTargetsMessage
B6 03 00 00 // 950
8A 02 00 00 // 650
C2 01 00 00 // 450
E8 03 00 00 // 1000
F4 01 00 00 // 500
F4 01 00 00 // 500
E8 03 00 00 // 1000
26 02 00 00 // 550
58 02 00 00 // 600
00 00 00 00 // Points Left to Migrate
```

## Related Pages
- [[Species Info]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete