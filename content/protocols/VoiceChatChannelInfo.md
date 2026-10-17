---
title: VoiceChatChannelInfo
url: https://wiki.swganh.org/index.php/VoiceChatChannelInfo
page_type: Server Packet
opcode: 4BF970FE
revision_id: 257167
last_modified: 
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:ServerPacket', 'Template:100%']
---

# VoiceChatChannelInfo

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| INT | channelInfoFlags |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = 4BF970FE

## Notes
- **NOTE:** this is from an NGE packet capture and may not me applicable to precu.

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
07 00 #Operand
FE 70 F9 4B #VoiceChatChannelInfo
10 00 00 00 # channelInfoFlags (ForcedShortlist = 0x10)


24 00 #StringSize
53 57 47 2E 53 74 61 72 73 69 64 65 72 2E 67 75 69 6C 64 2E 31 34 31 30 30 34 2E 47 75 69 6C 64 43 68 
61 74 #SWG.Starsider.guild.141004.GuildChat (channel name)
//141004 (313431303034) represents the players GuildID. 
// This is the "guildchat tab


24 00 #StringSize
53 57 47 2E 53 74 61 72 73 69 64 65 72 2E 67 75 69 6C 64 2E 31 34 31 30 30 34 2E 47 75 69 6C 64 43 68 
61 74 #SWG.Starsider.guild.141004.GuildChat (channel name)


22 00 
73 69 70 3A 63 6F 6E 66 63 74 6C 2D 31 31 32 35 36 32 36 38 40 73 77 70 2E 76 69 76 6F 78 2E 
63 6F 6D #sip:confctl-11256268@swp.vivox.com
//this contains channelUri (sip:confctl-), ChannelPassword (11256268@) and (host? swp.vivox.com)

00 00 00 00 #unknown INT
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete