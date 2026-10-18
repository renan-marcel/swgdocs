---
title: TRN (FileFormat)
url: https://wiki.swganh.org/index.php/TRN_%28FileFormat%29
page_type: FileFormat
opcode: 
revision_id: 78292
last_modified: 2011-07-02T20:36:32Z
completion: unknown
direction: unknown
sample_status: present
categories: []
templates: ['Template:PageHeader']
---

# TRN (FileFormat)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| BREC | Boundary Rectangle |
| BCIR | Boundary Circle |
| BPOL | Boundary Polygon |
| BPLN | Boundary PolyLine |

## Variable Descriptions
_none_

## Notes
- **NOTE:** Every Affector has an IHDR child wich is holding the user-custom name of the affector (here AffectorFloraCollidableConstant).
- **NOTE:** Boundaries can have a special footer allowing them to behave as a water area. (TODO)

## Tags
_none_

## Sample Packet
```
4A 3A 5C 73 77 67 5C 63 75 72 72 65 6E 74 5C 64 61 74 61 5C 	J..swg.current.data.
73 6B 75 2E 30 5C 73 79 73 2E 73 68 61 72 65 64 5C 62 75 69 	sku.0.sys.shared.bui
6C 74 5C 67 61 6D 65 5C 74 65 72 72 61 69 6E 5C 64 61 6E 74 	lt.game.terrain.dant
6F 6F 69 6E 65 2E 74 72 6E 00 00 00 80 46 00 00 00 41 02 00 	ooine.trn....F...A..
00 00 01 00 00 00 CD CC CC BD 00 00 00 40 77 74 65 72 5F 64 	..............wter.d
61 6E 74 5F 6C 61 6B 65 00 00 30 04 46 00 00 00 00 00 00 00 	ant.lake..0.F.......
43 00 00 00 41 00 00 00 40 00 00 00 00 00 00 00 00 00 00 80 	C...A...............
42 00 00 80 40 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 F0 	B...................
41 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 43 00 00 00 	A...............C...
44 00 00 00 42 00 00 00 41 00 00 00 00 	                        D...B...A....
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
_none_