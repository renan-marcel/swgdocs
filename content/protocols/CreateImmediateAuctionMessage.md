---
title: CreateImmediateAuctionMessage
url: https://wiki.swganh.org/index.php/CreateImmediateAuctionMessage
page_type: Server Packet
opcode: 1E9CE308
revision_id: 20982
last_modified: 2008-01-06T23:34:58Z
completion: 100%
direction: C→S
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Client Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:U string', 'Template:Byte', 'Template:ClientPacket', 'Template:100%']
---

# CreateImmediateAuctionMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ObjectID |
| LONG | TerminalID |
| INT | price |
| INT | time of Auction in seconds |
| U_STRING | description |
| BYTE | Flag Premium Auction |

## Variable Descriptions
- Opperand_Count	     = '
- Opcode		     = 1E9CE308

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
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
Pages with missing packet samples | Packets | Client Packets | 100% Complete