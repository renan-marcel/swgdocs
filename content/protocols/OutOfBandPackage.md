---
title: OutOfBandPackage
url: https://wiki.swganh.org/index.php/OutOfBandPackage
page_type: Server Packet
opcode: 
revision_id: 51942
last_modified: 2009-04-26T19:28:45Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:ServerPacket', 'Template:75%']
---

# OutOfBandPackage

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| USTRING | Length = Size/2 (it is parsed out as a USTRING) |
| SHORT | NumberOfPackages (Basically a list) |
| BYTE | PackageType |
| INT | NegativeInt(1-TypeID ??) |
| 00 | Nothing |
| 01 | ProsePackage[Add's To End Of Body] |
| ASTRING | BaseMessageSTF |
| INT | ?? |
| ASTRING | BaseMessageString |
| LONG | %TU ObjectID |
| ASTRING | %TU STFFile |
| INT | ?? |
| ASTRING | %TU STFString |
| USTRING | %TU String |
| LONG | %TT ObjectID |
| ASTRING | %TT STFFile |
| INT | ?? |
| ASTRING | %TT STFString |
| USTRING | %TT String |
| LONG | %TO ObjectID |
| ASTRING | %TO STFFile |
| INT | ?? |
| ASTRING | %TO STFString |
| USTRING | %TO String |
| INT | %DI Integer |
| FLOAT | %DF Float |
| BYTE | DisplayFlag?(00-Display,01-Blank) |
| 02 | AuctionToken[needs more work...] |
| INT | ?? |
| SHORT | ?? |
| SHORT | ?? |
| 03 | USTRING[needs more work...] |
| USTRING | ?? |
| 04 | WaypointDataBase[NegInt Must be -3] |
| INT | ?? |
| FLOAT | X-Coord |
| FLOAT | Y-Coord |
| FLOAT | Z-Coord |
| LONG | ?? |
| INT | PlanetCRC |
| USTRING | WaypointName |
| LONG | WaypointObjectID |
| BYTE | ColorByte |
| BYTE | ActivatedFlag |
| 06 | ASTRING[needs more work...] |
| ASTRING | ?? |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.

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
Packets | Server Packets | 75% Complete