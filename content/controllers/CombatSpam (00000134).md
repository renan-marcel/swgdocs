---
title: CombatSpam (00000134)
url: https://wiki.swganh.org/index.php/CombatSpam_%2800000134%29
page_type: Server Packet
opcode: 00000134
revision_id: 20694
last_modified: 
completion: 100%
direction: S→C
sample_status: absent
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:A string', 'Template:Byte', 'Template:U string', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# CombatSpam (00000134)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Attacker |
| LONG | Defender |
| LONG | Armor |
| INT | Damage |
| A_STRING | File |
| INT | Padding |
| A_STRING | Text |
| BYTE | ColorFlag |
| U_STRING | Unicode String |

## Variable Descriptions
- controllerID	     = 00000134

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete