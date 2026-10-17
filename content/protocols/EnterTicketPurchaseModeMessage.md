---
title: EnterTicketPurchaseModeMessage
url: https://wiki.swganh.org/index.php/EnterTicketPurchaseModeMessage
page_type: Server Packet
opcode: 904DAE1A
revision_id: 258793
last_modified: 2025-01-07T18:06:26Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ServerPacket', 'Template:100%']
---

# EnterTicketPurchaseModeMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | Planet |
| A_STRING | Destination |

## Variable Descriptions
- Opperand_Count	     = 3
- Opcode		     = 904DAE1A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00 
1A AE 4D 90 // EnterTicketPurchaseModeMessage
08 00 74 61 74 6F 6F 69 6E 65 // Tatooine
10 00 42 65 73 74 69 6E 65    // Bestine
20 53 74 61 72 70 6F 72 74    // (space)Starport
00 1C
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete