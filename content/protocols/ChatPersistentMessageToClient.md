---
title: ChatPersistentMessageToClient
url: https://wiki.swganh.org/index.php/ChatPersistentMessageToClient
page_type: Server Packet
opcode: 08485E17
revision_id: 22604
last_modified: 2008-02-12T16:53:48Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:A string', 'Template:Byte', 'Template:Unknown', 'Template:U string', 'Template:ServerPacket', 'Template:75%']
---

# ChatPersistentMessageToClient

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | CRC |
| A_STRING | Sender Name |
| A_STRING | SWG |
| A_STRING | Galaxy Name |
| INT | DBMailId |
| INT | MailCounter (Sender) |
| BYTE | ?? |
| U_STRING | Subject |
| INT |  |
| BYTE | MailStatus |
| BYTE | TimeSend |

## Variable Descriptions
- Opperand_Count	     = 02
- Opcode		     = 08485E17

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

## Sample Packet
```
02 00 
17 5E 48 08                          // ChatPersistentMessageToClient
0C 00                                // string count
62 65 61 76 65 72 20 68 65 61 64 73  // beaver.heads (guild Name)
03 00                                // string count
53 57 47                             // SWG
0A 00                                // string count
53 68 61 64 6F 77 66 69 72 65        // Shadowfire
32 15 EF 2B                          // email id 
01 00 00 00                          // counter
00                                   //??????????????????
17 00 00 00                          // string count
40 00 67 00 75 00 69 00 6C 00                    // @.g.u.i.l.
64 00 6D 00 61 00 69 00 6C 00 3A 00 6B 00 69 00  // d.m.a.i.l.:.k.i.
63 00 6B 00 5F 00 73 00 75 00 62 00 6A 00 65 00  // c.k._.s.u.b.j.e.
63 00 74 00                                        //  c.t
00 00 00 00                          //???????????????????
4E 68 0B 13                          //???????????????????
46 C6 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete