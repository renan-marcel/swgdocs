---
title: CancelLiveAuctionResponseMessage
url: https://wiki.swganh.org/index.php/CancelLiveAuctionResponseMessage
page_type: Server Packet
opcode: 7DA2246C
revision_id: 51933
last_modified: 2009-04-26T19:07:13Z
completion: 75%
direction: S→C
sample_status: placeholder
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '75% Complete']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Byte', 'Template:Unknown', 'Template:ServerPacket', 'Template:75%']
---

# CancelLiveAuctionResponseMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| LONG | Auction ID |
| INT | Errorcode |
| BYTE | ?? |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 7DA2246C
- Errorcode is either 0 for no error or != 0 for an error

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
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
Pages with missing packet samples | Packets | Server Packets | 75% Complete