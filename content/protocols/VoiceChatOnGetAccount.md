---
title: VoiceChatOnGetAccount
url: https://wiki.swganh.org/index.php/VoiceChatOnGetAccount
page_type: Server Packet
opcode: 326E6B43
revision_id: 257220
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# VoiceChatOnGetAccount

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| INT | GetAccountResult |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 326E6B43

## Notes
- **NOTE:** this is from an NGE packet capture and may not me applicable to precu.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 #Operand
43 6B 6E 32 #VoiceChatOnGetAccount
00 00 00 00 #GetAccountResult
	

14 00 #StringSize 
53 74 61 72 73 69 64 65 72 2E 76 69 63 74 6F 72 2D 64 72 61  #Starsider.victor-dra

0F 00 #StringSize
66 30 38 65 31 37 36 64 33 33 39 64 62 31 63 #f08e176d339db1c

19 00 #StringSize
68 74 74 70 73 3A 2F 2F 77 77 77 2E 73 77 70 2E 76 69 76 6F 78 2E 63 6F 6D #https://www.swp.vivox.com
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete