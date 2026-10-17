---
title: SecureTrade (00000115)
url: https://wiki.swganh.org/index.php/SecureTrade_%2800000115%29
page_type: Object Controller
opcode: 00000115
revision_id: 256927
last_modified: 
completion: 75%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Unknown', 'Template:Long', 'Template:ObjControllerMessageTag', 'Template:75%']
---

# SecureTrade (00000115)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | ?? |
| LONG | Sender ID |
| LONG | Receiver ID |

## Variable Descriptions
- controllerID	     = 00000115

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **75%** - This packet has been partially reversed.

## Sample Packet
```
cAble@projectswg.com

05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 
15 01 00 00 #secureTrade
AC 3B 65 D2 00 00 00 00 #trader Sender
00 00 00 00 
01 00 00 00 #Request Trade
A1 56 89 27 00 00 00 00 #Trader Sender
AC 3B 65 D2 00 00 00 00 #trade receiver


05 00 #Operand
46 5E CE 80 #ObjController
0B 00 00 00 
15 01 00 00 #SecureTrade
AC 3B 65 D2 00 00 00 
00 00 00 00 
00 #ExtraByte?
01 00 00 00 #Request Trade
A1 56 89 27 00 00 00 00 #trade Sender
AC 3B 65 D2 00 00 00 00 #trade receiver                                               
                  

05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 #Unknown
15 01 00 00 #SecureTrade
AC 3B 65 D2 00 00 00 #Sender
00 00 00 00
00 #ExtraByte?
02 00 00 00 #TradeRequested
00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 00 00 


05 00 #Operand
46 5E CE 80 #ObjController
23 00 00 00 
15 01 00 00 #SecureTrade
AC 3B 65 D2 00 00 00 00 #CharacterID
00 00 00 00 
02 00 00 00 #TradeRequested
00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | Server Packets | 75% Complete