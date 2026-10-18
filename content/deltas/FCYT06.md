---
title: FCYT06
url: https://wiki.swganh.org/index.php/FCYT06
page_type: Baseline
opcode: 
revision_id: 79419
last_modified: 2012-11-29T21:58:48Z
completion: 25%
direction: unknown
sample_status: present
categories: ['Packets', '25% Complete']
templates: ['Template:PageHeader', 'Template:FCYTArchitectureNAV', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Byte', 'Template:25%']
---

# FCYT06

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Object Operand Count |
| INT | ??? |
| A_STRING | STF detail File |
| INT | String spacer |
| A_STRING | STF detail Name |
| INT | ??? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| INT | ?? |
| BYTE | ?? |

## Variable Descriptions
- Obj_OperandCount = ??

## Notes
_none_

## Tags
- **25%** - This packet has been partially reversed.

## Sample Packet
```
05 00 
0C 5F A7 68              // BaselinesMessage
62 BA 03 B5 10 00 00 00  // ID
54 59 43 46 06           // TYCF 6
22 00 00 00 // remaining length of packet
02 00 // unknown
6E 00 00 00 
09 00                       // String count
66 61 63 74 6F 72 79 5F 64  // factory_d
00 00 00 00                 // string spacer
0B 00                             // String count
61 72 6D 6F 72 5F 63 72 61 74 65  // armor_crate
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 25% Complete