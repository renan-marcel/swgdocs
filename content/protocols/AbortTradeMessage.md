---
title: AbortTradeMessage
url: https://wiki.swganh.org/index.php/AbortTradeMessage
page_type: Server Packet
opcode: 9CA80F98
revision_id: 73274
last_modified: 2010-06-10T18:43:08Z
completion: 100%
direction: S→C
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# AbortTradeMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | OpCount |
| INT | OpCode |

## Variable Descriptions
- Opperand_Count	     = 1
- Opcode		     = 9CA80F98

## Notes
- **NOTE:** You must send this in order to clear the trade window! It must be followed by TradeCompleteMessage to clear the trade session on both clients.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
Insert Sample Packet Here...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 100% Complete