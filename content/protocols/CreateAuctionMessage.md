---
title: CreateAuctionMessage
url: https://wiki.swganh.org/index.php/CreateAuctionMessage
page_type: Client Packet
opcode: AD47021D
revision_id: 20983
last_modified: 2008-01-06T23:35:10Z
completion: 100%
direction: C→S
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Client Packets', '100% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:U string', 'Template:Byte', 'Template:ClientPacket', 'Template:100%']
---

# CreateAuctionMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| LONG | ItemID |
| LONG | Terminal / Vendor ID |
| INT | Price |
| INT | Time in Seconds |
| U_STRING | Item description |
| BYTE | Flag premium Auction |

## Variable Descriptions
- Opperand_Count	     = 8
- Opcode		     = AD47021D

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