---
title: SOE Protocol Breakdown
url: https://wiki.swganh.org/index.php/SOE_Protocol_Breakdown
page_type: Guides
opcode: 
revision_id: 257057
last_modified: 2013-09-21T15:40:18Z
completion: unknown
direction: unknown
sample_status: present
categories: []
templates: ['Template:PageHeader', 'Template:InfoboxPacketDetail', 'Template:InfoboxPacketSample']
---

# SOE Protocol Breakdown

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| ID | String |
| 0 | None |
| 1 | ICMP Error |
| 2 | Timeout |
| 3 | Other side terminated |
| 4 | Manager deleted |
| 5 | Connect fail |
| 6 | Application |
| 7 | Unreachable connection |
| 8 | Unacknowledged timeout |
| 9 | New connection attempt |
| 10 | Connection refused |
| 11 | Mutual connect error |
| 12 | Connecting to self |
| 13 | Reliable overflow |

## Variable Descriptions
_none_

## Notes
- **NOTE:** The Size field will never exceed 255.
- **NOTE:** This packet is usually compressed but is optional.
- **NOTE:** This packet is usually compressed but is optional.

## Tags
_none_

## Sample Packet
```
00 00 00 02 27 38 24 61 00 00 01 F0
```

## Related Pages
- [[SWGPacketExamples]]

## Other Sections
_none_

## Categories
_none_