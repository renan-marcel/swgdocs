---
title: AuctionQueryHeadersMessage
url: https://wiki.swganh.org/index.php/AuctionQueryHeadersMessage
page_type: Client Packet
opcode: 679E0D00
revision_id: 37123
last_modified: 2008-06-12T11:08:21Z
completion: 75%
direction: C→S
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:U string', 'Template:Long', 'Template:ClientPacket', 'Template:75%']
---

# AuctionQueryHeadersMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand count |
| INT | Opcode |
| INT | Region |
| INT | UpdateCounter |
| INT | Window Type |
| BYTE | Subcategory |
| BYTE | Cat I |
| BYTE | Cat II |
| BYTE | Cat III |
| INT | itemtype ID |
| U_STRING | searchstring |
| INT | unknown |
| INT | search min Price |
| INT | search max Price |
| BYTE | include entrance fee flag |
| LONG | Vendor ID |
| BYTE | VendorFlag |
| SHORT | nr of 1st Auction to show |

## Variable Descriptions
- Opperand_Count	     = 14
- Opcode		     = 679E0D00

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
Insert Sample Packet Here...
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Client Packets | Server Packets | 75% Complete