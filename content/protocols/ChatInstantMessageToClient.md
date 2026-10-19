---
title: ChatInstantMessageToClient
url: https://wiki.swganh.org/index.php/ChatInstantMessageToClient
page_type: Server Packet
opcode: 3C565CED
revision_id: 21071
last_modified: 2008-01-07T02:48:06Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ServerPacket', 'Template:100%']
---

# ChatInstantMessageToClient

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| SHORT | Opperand_Count |
| INT | Opcode |
| A_STRING | Game ID |
| A_STRING | Galaxy Name |
| A_STRING | Playername |
| U_STRING | Message |
| U_STRING | OutOfBand |

## Variable Descriptions
- Opperand_Count	     = 4
- Opcode		     = 3C565CED

## Notes

<!-- pswgcommon-message-crosscheck:start -->
### PSWGCommon / client cross-check

The final field is a second U_STRING, named outOfBand in PSWGCommon. Its int32 prefix counts UTF-16 code units and is followed by twice that many bytes in UTF-16LE. The historical sample's trailing 00 00 00 00 is this empty string's length prefix; the sample remains unchanged. It does not establish that the field must always be zero.

The client reader at 0x00AF2610 registers ChatAvatarId and two Unicode strings (object members +0x38, +0x60, +0x70). These are in-memory offsets. The avatar decoder preserves the three narrow strings Game ID, Galaxy Name and Playername; Unicode unpack at 0x011948B0 reads int32 length followed by 2*length bytes.

Header discrepancy: native archive pack at 0x0118B6F0 derives operand count from the registered-field vector: opcode plus three registered fields gives 4, matching the historical sample. PSWGCommon ChatInstantMessageToClient.encode() writes 2. Native unpack at 0x0118B740 consumes the short without checking its value; PSWGCommon checkDecode also discards it. This documents the implementation difference without changing the library or replacing the historical sample.

With G/C the byte lengths of Galaxy Name/Playername and M/O the UTF-16 code-unit lengths of Message/OutOfBand: the message is 23+G+C+2*M+2*O bytes. Game ID starts at 6 (2-byte length plus SWG); Galaxy Name at 11; Playername at 13+G; Message at 15+G+C; OutOfBand at 19+G+C+2*M. Each offset identifies its length prefix. Offsets exclude SOE framing; lengths and opcode are little-endian.

PSWGCommon's A_STRING helper uses UTF-8 byte lengths, although this packet allocates space using Java String.length() for galaxy and character. Non-ASCII names can therefore exceed the allocated buffer. This is a library allocation limitation, not evidence that the native client uses UTF-8 for all narrow strings.

See [client message analysis](../guides/pswgcommon-client-messages.md). Evidence: [BN-PSWG-CHAT-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CHAT-READ.json), [BN-PSWG-ARCHIVE-PACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ARCHIVE-PACK.json), [BN-PSWG-ARCHIVE-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ARCHIVE-UNPACK.json), [BN-PSWG-AVATAR-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-AVATAR-UNPACK.json), [BN-PSWG-UNICODE-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-UNICODE-UNPACK.json).
<!-- pswgcommon-message-crosscheck:end -->

## Tags
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
04 00             // Op Count
ED 5C 56 3C       // ChatInstantMessageToClient
03 00             // string count
53 57 47          // SWG = Game type
05 00             // string count
4C 6F 77 63 61    // Lowca = Server name
05 00             // string count
68 69 72 65 64    // hired = Player name
03 00 00 00       // u-string count
6C 00 6F 00 6C 00 // lol = message
00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Server Packets | 100% Complete