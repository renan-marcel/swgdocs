---
title: AuctionQueryHeadersResponseMessage
url: https://wiki.swganh.org/index.php/AuctionQueryHeadersResponseMessage
page_type: Server Packet
opcode: FA500E52
revision_id: 258190
last_modified: 2024-08-15T22:30:49Z
completion: 75%
direction: S→C
sample_status: present
categories: ['Pages with missing packet samples', 'Packets', 'Server Packets', '75% Complete', 'Schmunzel', 'Rouse', 'Hakry', 'Bazaar']
templates: ['Template:MissingPacket', 'Template:Ambox', 'Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Uint', 'Template:Beginlist', 'Template:A string', 'Template:Endlist', 'Template:U string', 'Template:Long', 'Template:Byte', 'Template:ServerPacket', 'Template:75%', 'Template:Schmunzel', 'Template:Rouse', 'Template:Hakry', 'Template:Bazaar']
---

# AuctionQueryHeadersResponseMessage

## Notices
- This article or section needs additional data . Please add a sample packet!

## Struct
| Type | Name |
| --- | --- |
| SHORT | Operand Count |
| INT | Opcode |
| INT | Page count |
| INT | (2 = item listing, 4 = auctions listing) |
| UINT | TScount: Number of unique terminals and unique sellers |

## Variable Descriptions
- Operand_Count	     = 9
- Opcode		     = FA500E52

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **75%** - This packet has been partially reversed.
- **WOOF!** - This document has been woofed by Schmunzel.
- **Rouse** - This document has been pinkified by Rouse.
- **H** - This has been approved by Hakry.
- **Bazaar** - Bazaar related stuff.

## Sample Packet
```
256	Armor	Armor
257	Body Armor	Armor
258	Head Amor	Armor
259	Misc Armor	Armor
260	Leg Armor	Armor
261	Arm Armor	Armor
262	Hand Armor	Armor
263	Foot Armor	Armor
264	Shield Generator	Armor
512	Building	Building
513	Municipal Building	Building
514	Player Building	Building
515	Factional Building	Building
1024	Entity	Entity
1025	Character	Entity
1026	Droid	Entity
1027	Probe Droid	Entity
1028	Creature	Entity
2048	Data	Data
2049	Draft Schematic	Data
2050	Manufacturing Schematic	Data
2051	Mission Object	Data
2052	Token	Data
2053	Waypoint	Data
2054	Data	Data
2055	Pet Control Device	Data
2056	Vehicle Control Device	Data
2058	Ship Control Device	Data
2059	Droid Control Device	Data
4096	Installation	Installation
4097	Factory	Installation
4098	Generator	Installation
4099	Harvester	Installation
4100	Turret	Installation
4101	Minefield	Installation
8192	Misc	Misc
8193	Ammunition	Misc
8194	Chemical	Misc
8197	Container	Misc
8198	Crafting Station	Misc
8200	Electronics	Misc
8201	Flora	Misc
8202	Food	Misc
8203	Furniture	Misc
8204	Instrument	Misc
8205	Pharmaceutical	Misc
8207	Sign	Misc
8208	Counter	Misc
8209	Factory Crate	Misc
8210	Travel Ticket	Misc
8211	Generic Item	Misc
8212	Trap	Misc
8213	Wearable Container	Misc
8214	Fishing Pole	Misc
8215	Fishing Bate	Misc
8216	Drink	Misc
8217	Firework	Misc
8218	Item	Misc
8219	Pet Medicine	Misc
8220	Firework Show	Misc
8221	Clothing Attachment	Misc
8222	Live Sample	Misc
8223	Armor Attachment	Misc
8224	Community Crafting Project	Misc
8225	Crystal	Misc
8226	Droid Programming Chip	Misc
8227	Asteroid	Misc
8228	Pilot Chair	Misc
8229	Operations Chair	Misc
8230	Turret Access Ladder	Misc
8231	Container	Misc
16384	Terminal	Terminal
16385	Bank Terminal	Terminal
16386	Commodities Terminal	Terminal
16387	Cloning Terminal	Terminal
16388	Insurance Terminal	Terminal
16389	Management Terminal	Terminal
16390	Mission Terminal	Terminal
16391	Permissions Terminal	Terminal
16392	Player Structure Terminal	Terminal
16393	Shipping Terminal	Terminal
16394	Travel Terminal	Terminal
16395	Space Terminal	Terminal
16386	Terminal	Terminal
32768	Tool	Tool
32769	Crafting Tool	Tool
32770	Survey Tool	Tool
32771	Repair Tool	Tool
32772	Camp Kit	Tool
32773	Ship Componet Repair Item	Tool
65536	Vehicle	Vehicle
65537	Hover Vehicle	Vehicle
131072	Weapon	Weapon
131073	Melee Weapon	Weapon
131074	Ranged Weapon	Weapon
131075	Thrown Weapon	Weapon
131076	Heavy Weapon	Weapon
131077	Mine	Weapon
131078	Special Heavy Weapon	Weapon
131079	1-Handed Melee Weapon	Weapon
131080	2-Handed Melee Weapon	Weapon
131081	Polearm	Weapon
131082	Pistol	Weapon
131083	Carbine	Weapon
131084	Rifle	Weapon
262144	Component	Component
262145	Armor Component	Component
262146	Chemistry Component	Component
262147	Clothing Component	Component
262148	Droid Component	Component
262149	Electronics Component	Component
262150	Munition Component	Component
262151	Structure Component	Component
262152	Melee Weapon Component	Component
262153	Ranged Weapon Component	Component
262154	Tissue Component	Component
262155	Genetic Component	Component
262156	Light Saber Crystal	Component
262157	Community Crafting Component	Component
524288	Weapon Powerup	Weapon Powerup
524289	Melee Weapon Powerup	Weapon Powerup
524290	Ranged Weapon Powerup	Weapon Powerup
524291	Thrown Weapon Powerup	Weapon Powerup
524292	Heavy Weapon Powerup	Weapon Powerup
524293	Mine Powerup	Weapon Powerup
524294	Special Heavy Weapon Powerup	Weapon Powerup
1048576	Armor Powerup	Armor Powerup
1048577	Body Armor Powerup	Armor Powerup
1048578	Head Armor Powerup	Armor Powerup
1048579	Misc Armor Powerup	Armor Powerup
1048580	Leg Armor Powerup	Armor Powerup
1048581	Arm Armor Powerup	Armor Powerup
1048582	Hand Armor Powerup	Armor Powerup
1048583	Foot Armor Powerup	Armor Powerup
2097152	Jewelry	Jewelry
2097153	Ring	Jewelry
2097154	Bracelet	Jewelry
2097155	Necklace	Jewelry
2097156	Earring	Jewelry
4194304	Resource Container	Resource Container
4194305	Energy (Gas)	Resource Container
4194306	Energy (Liquid)	Resource Container
4194307	Energy (Radioactive)	Resource Container
4194308	Energy (Solid)	Resource Container
4194309	Inorganic Chemical	Resource Container
4194310	Inorganic Gas	Resource Container
4194311	Inorganic Mineral	Resource Container
4194312	Water	Resource Container
4194313	Organic Food	Resource Container
4194314	Organic Hide	Resource Container
4194315	Organ ic Structural	Resource Container
4194316	Resource Container	Resource Container
8388608	Deed	Deed
8388609	Building Deed	Deed
8388610	Installation Deed	Deed
8388611	Pet Deed	Deed
8388612	Droid Deed	Deed
8388613	Vehicle Deed	Deed
16777216	Clothing	Clothing
16777217	Bandolier	Clothing
16777218	Belt	Clothing
16777219	Bodysuit	Clothing
16777220	Cape	Clothing
16777221	Cloak	Clothing
16777222	Footwear	Clothing
16777223	Dress	Clothing
16777224	Handwear	Clothing
16777225	Eyewear	Clothing
16777226	Headwear	Clothing
16777227	Jacket	Clothing
16777228	Pants	Clothing
16777229	Robe	Clothing
16777230	Shirt	Clothing
16777231	Vest	Clothing
16777232	Wookie Garb	Clothing
16777233	Misc Clothing	Clothing
16777234	Skirt	Clothing
1073741824	Ship Component	Ship Component
1073741825	Reactor	Ship Component
1073741826	Engine	Ship Component
1073741827	Shield	Ship Component
1073741828	Armor	Ship Component
1073741829	Weapon	Ship Component
1073741830	Capacitor	Ship Component
1073741831	Booster	Ship Component
1073741832	Droid Interface	Ship Component
1073741833	Hangar	Ship Component
1073741834	Targeting Station	Ship Component
1073741835	Bridge	Ship Component
1073741836	Ship Chassis	Ship Component
1073741837	Missile Pack	Ship Component
1073741838	Countermeasure Pack	Ship Component
1073741839	Missile Launcher	Ship Component
1073741840	Countermeasure Launcher	Ship Component
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Pages with missing packet samples | Packets | Server Packets | 75% Complete | Schmunzel | Rouse | Hakry | Bazaar