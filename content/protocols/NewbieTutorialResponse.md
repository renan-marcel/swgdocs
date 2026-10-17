---
title: NewbieTutorialResponse
url: https://wiki.swganh.org/index.php/NewbieTutorialResponse
page_type: Client Packet
opcode: CA88FBAD
revision_id: 44418
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:ClientPacket', 'Template:100%']
---

# NewbieTutorialResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | clientReady |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = CA88FBAD

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00       // Op Count
AD FB 88 CA // NewbieTutorialResponse
0D 00                                  // string count
6F 70 65 6E 49 6E 76 65 6E 74 6F 72 79 //openInventory
-----------------------------------------------------------------------
02 00       // Op Count
AD FB 88 CA // NewbieTutorialResponse
0B 00                            // string count
63 6C 69 65 6E 74 52 65 61 64 79 // clientReady
```

## Related Pages
- [[NewbieTutorialRequest]]

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete