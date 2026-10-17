---
title: PlayMusicMessage
url: https://wiki.swganh.org/index.php/PlayMusicMessage
page_type: Server Packet
opcode: 04270D8A
revision_id: 22612
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:Long', 'Template:Byte', 'Template:ServerPacket', 'Template:100%']
---

# PlayMusicMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand_Count |
| INT | Opcode |
| A_STRING | SoundFile String |
| LONG | 00 00 00 00 00 00 00 00 |
| INT | 00 00 00 00 |
| BYTE | 00 |

## Variable Descriptions
- Opperand_Count	     = 5
- Opcode		     = 04270D8A

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
8A 0D 27 04              // PlayMusicMessage
20 00                    // sting count
73 6F 75 6E 64 2F                               // sound/
6D 75 73 69 63 5F 61 63 71 5F                   // music_acq_
62 6F 75 6E 74 79 68 75 6E 74 65 72 2E 73 6E 64 // bountyhunter.snd
00 00 00 00 
00 00 00 00
01 00 00 00  // might be a play loop or repeat flag or number of times to play
00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete