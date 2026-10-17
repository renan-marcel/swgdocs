---
title: ChatInstantMessageToCharacter
url: https://wiki.swganh.org/index.php/ChatInstantMessageToCharacter
page_type: Client Packet
opcode: 84BB21F7
revision_id: 79339
last_modified: 2012-02-26T21:49:15Z
completion: 75%
direction: C→S
sample_status: placeholder
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ClientPacket', 'Template:75%']
---

# ChatInstantMessageToCharacter

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Op Count |
| INT | Opcode |
| A_STRING | Game ID |
| A_STRING | Galaxy Name |
| A_STRING | Player name |
| U_STRING | Message |
| INT | ?? |
| INT | Sequence |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 84BB21F7

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
- [[ChatOnSendInstantMessage]]
- [[ChatInstantMessageToClient]]

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete