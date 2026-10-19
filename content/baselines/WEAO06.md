---
title: WEAO06
url: https://wiki.swganh.org/index.php/WEAO06
page_type: BaseLine
opcode: 
revision_id: 79422
last_modified: 
completion: 0%
discovery_source: "Wiki SWGANH"
direction: S→C
sample_status: present
categories: ['Packets', '0% Complete', 'Server Packets']
templates: ['Template:PageHeader', 'Template:WEAOArchitectureNAV', 'Template:0%', 'Template:ServerPacket']
---

# WEAO06

> [!NOTE]
> **Origem da Descoberta: Wiki SWGANH**
> Esta entrada foi catalogada originalmente na Wiki do SWGANH (completude de 0%). A estrutura do pacote e seus campos permanecem pendentes de reversão e validação binária.

## Notices
_none_

## Struct
_none_

## Variable Descriptions
- Obj_OperandCount =

## Notes
_none_

## Tags
- **0%** - This packet has not been reversed.
- **S→C** - This packet originates on the server.

## Sample Packet
```
05 00 
0C 5F A7 68             // BaselinesMessage
B8 59 90 19 17 00 00 00 // ID
4F 41 45 57 06          // OAEW 6
2B 00 00 00 
03 00 6E 00 
00 00 
0B 00                             // String count
77 65 61 70 6F 6E 5F 6E 61 6D 65  // weapon_name
00 00 00 00 
0E 00                                     // String count
64 65 66 61 75 6C 74 5F 77 65 61 70 6F 6E // default_weapon
06 00 00 00 
00 00 01 00 
00 00 00 00 
00 00 00 00 
00 
16 #size
04 00 #Operand
26 C1 A1 08 #UpdatePvpStatusMessage
02 00 00 00 #PvpStatus
00 00 00 00 #Faction
----

05 00 
0C 5F A7 68 
66 D3 29 6B 13 00 00 00 // ID
4F 41 45 57 06 // OAEW 6
32 00 00 00 
04 00 
4C 00 00 00 
0D 00                                  // string count
77 65 61 70 6F 6E 5F 64 65 74 61 69 6C // weapon_detail
00 00 00 00                            // string spacer
0B 00                                  // string count
72 69 66 6C 65 5F 6C 61 73 65 72       // rifle_laser
00 00 00 00 
00 00 00 00 
00 00 00 00 
0B 00   -------------------------|
02 02 				 |
22 C3 BF                         |
01 02 	   Rifles Customization	 |?????? 
37 C3 BF     			 |
03 04 				 |
00 00 00 ------------------------|
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | 0% Complete | Server Packets