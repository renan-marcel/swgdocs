---
title: ObjectMenuResponse (00000147)
url: https://wiki.swganh.org/index.php/ObjectMenuResponse_%2800000147%29
page_type: Object Controller
opcode: 00000147
revision_id: 24353
last_modified: 2008-03-04T03:38:41Z
completion: 100%
direction: S→C
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Long', 'Template:Int', 'Template:Beginlist', 'Template:Byte', 'Template:U string', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:ServerPacket', 'Template:100%']
---

# ObjectMenuResponse (00000147)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| LONG | Item ID |
| LONG | Receiver ID |
| INT | Options Count |

## Variable Descriptions
- controllerID	     = 00000147

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **S→C** - This packet originates on the server.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
46 5E CE 80                                    // ObjControllerMessage 
0B 00 00 00 
47 01 00 00                                    // ObjectMenuResponse 
71 E2 DB D9 00 00 00 00                        // Character ID 
00 00 00 00 
6D 56 76 00 00 00 00 00                        // Bank Terminal ID 
71 E2 DB D9 00 00 00 00                        // Character ID 

05 00 00 00 // List Size 
01 // radial option # 
00 // radial parent id 
15 // Radial Identifier (itemUseSelf) 
03 // option type 
00 00 00 00 // empty string 

02 // radial option # 
00 // radial parent id 
07 // Radial Identifier (examine) 
01 // option type 
00 00 00 00 // empty string 

03 // radial option # 
01 // radial parent id 
46 // Radial Identifier (serverMenu3) 
03 // option type 
11 00 00 00                                           // string count 
40 00 73 00 75 00                                     // @.s.u. 
69 00 3A 00 62 00 61 00 6E 00 6B 00 5F 00 63 00       // i.:.b.a.n.k._.c. 
72 00 65 00 64 00 69 00 74 00 73 00                   // r.e.d.i.t.s 

04 // radial option # 
01 // radial parent id 
47 // Radial Identifier (serverMenu4) 
03 // option type 
0F 00 00 00                                           // string count 
40 00 73 00 75 00 69 00 3A 00 62 00                   // @.s.u.i.:.b. 
61 00 6E 00 6B 00 5F 00 69 00 74 00 65 00 6D 00 73 00 // a.n.k._.i.t.e.m.s. 

05 // radial option # 
01 // radial parent id 
48 // Radial Identifier (serverMenu5) 
03 // option type 
14 00 00 00                                           // string count 
40 00 73 00 75 00                                     // @.s.u. 
69 00 3A 00 62 00 61 00 6E 00 6B 00 5F 00 64 00       // i.:.b.a.n.k._.d. 
65 00 70 00 6F 00 73 00 69 00 74 00 61 00 6C 00 6C 00 // e.p.o.s.i.t.a.l.l.
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 100% Complete