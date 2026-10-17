---
title: ChatSystemMessage
url: https://wiki.swganh.org/index.php/ChatSystemMessage
page_type: Server Packet
opcode: 6D2A6413
revision_id: 51944
last_modified: 2009-04-26T19:31:21Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Byte', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ChatSystemMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| BYTE | Display type |
| U_STRING | Message |
| U_STRING | OutOfBandPackage |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 6D2A6413

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
------STF Driven System Message-------
04 00 // Op Count
13 64 2A 6D  // ChatSystemMessage  
00 // makes system message only display in the chat window 00 for both and 02 for chat only
00 00  00 00 
3C 00 00 00    // Unicode Buffer Size (STFLoc.size() + StringName.size() + remaning bytes /2)
01 00          // Mystery Bool
01             // Static
FF FF FF FF    // Static
05 00          // String count 
67 75 69 6C 64 // guild
00 00 00 00    // string spacer
1E 00                          //String Count
63 72 65 61 74 65  5F 66 61 69   
6C 5F 61 62 62 72 65 76 5F 6E  
6F 74 5F 61 6C 6C 6F 77 65 64  // create_fail_abbrev_not_allowed
00 00 00 00 00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete