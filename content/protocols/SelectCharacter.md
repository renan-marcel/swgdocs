---
title: SelectCharacter
url: https://wiki.swganh.org/index.php/SelectCharacter
page_type: Client Packet
opcode: B5098D76
revision_id: 22123
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:ClientPacket', 'Template:100%']
---

# SelectCharacter

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| LONG | CharacterID |

## Variable Descriptions
- Opperand_Count	     = 2
- Opcode		     = B5098D76

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
02 00 // Op Count
76 8D 09 B5 // SelectCharacter
AA ED AC 2F 17 00 00 00 // Character ID
00 12 D5 // comp+crc
```

## Related Pages
- [[LoginEnumerateCharId]]
- [[ClientCreateCharacterSuccess]]

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete