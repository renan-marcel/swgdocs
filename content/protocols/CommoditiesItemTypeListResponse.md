---
title: CommoditiesItemTypeListResponse
url: https://wiki.swganh.org/index.php/CommoditiesItemTypeListResponse
page_type: Client Packet
opcode: D4E937FC
revision_id: 19870
last_modified: 
completion: 100%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:A string', 'Template:U string', 'Template:ClientPacket', 'Template:100%']
---

# CommoditiesItemTypeListResponse

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | Opcode |
| A_STRING | Server Name.Total Number of Items |
| INT | Sub Category Counter |
| INT | Sub Category |
| INT | Number of Typelistings in the Subcategory |
| A_STRING | String Directory |
| INT | 0 |
| U_STRING | String Type Name |

## Variable Descriptions
- Opperand_Count	     = 7
- Opcode		     = D4E937FC

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **100%** - This packet has been completely reversed.

## Sample Packet
```
00 09 
FF FF 
02 00 
FC 37 E9 D4 
Shadowfire.4606
7A 00 00 00                                     amount of subcategories

01 01 00 00 					category/subcategory bitmask
20 00 00 00 					amount of types in the subcategory

72 0F 30 89 					itemtype crc (??)
wearables.name					string lookup directory
00 00 00 00 					string custom name vs stringlookup
armor.tantel.skreej.chest.plate.quest 		string lookup

D5 43 73 90 
wearables.name
00 00 00 00 
armor.kashyyykian.hunting.chestplate

EF 09 EC 90 
wearables.name
00 00 00 00
armor.scout.trooper.chest.plateg

67 5C C4 92 
wearables.name
00 00 00 00 
armor.ris.chest.plate
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | 100% Complete