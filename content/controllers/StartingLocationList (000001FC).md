---
title: StartingLocationList (000001FC)
url: https://wiki.swganh.org/index.php/StartingLocationList_%28000001FC%29
page_type: Object Controller
opcode: 000001FC
revision_id: 52241
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:Int', 'Template:Beginlist', 'Template:A string', 'Template:Float', 'Template:Byte', 'Template:Endlist', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# StartingLocationList (000001FC)

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| INT | starting location count |

## Variable Descriptions
- controllerID	     = 000001FC

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 
46 5E CE 80 
1B 00 00 00
FC 01 00 00 
15 A8 0A 56 03 00 00 00  // player ID
00 00 00 00 

10 00 00 00  // number of starting locations


//tatooine =====================================

!bestine
!tatooine
00 00 00 00
00 00 00 00
00 00
!styles.location.tatooine.bestine
00 00
01

!mos_espa
!tatooine
00 00 00 00
00 00 00 00
00 00
!styles.location.tatooine.mos_espa
00 00
01

!mos_eisley
!tatooine
00 00 00 00
00 00 00 00
00 00
!styles.location.tatooine.mos_eisley
00 00
01

!mos_entha
!tatooine
00 00 00 00
00 00 00 00
00 00
!styles.location.tatooine.mos_entha
00 00
01


//corellia =======================================

!coronet
!corellia
00 00 00 00
00 00 00 00
00 00
!styles.location.corellia.coronet
00 00
01

!tyrena
!corellia
00 00 00 00
00 00 00 00
00 00
!styles.location.corellia.tyrena
00 00
01


!kor_vella
!corellia
00 00 00 00
00 00 00 00
00 00
!styles.location.corellia.kor_vella
00 00
01

!doaba_guerfel
!corellia
00 00 00 00
00 00 00 00
00 00
!styles.location.corellia.doaba_guerfel
00 00
01

//talus =============================================

!dearic
!talus
00 00 00 00
00 00 00 00
00 00
!styles.location.talus.dearic
00 00
01

!nashal
!talus
00 00 00 00
00 00 00 00
00 00
!styles.location.talus.nashal
00 00
01

//rori ==============================================

!narmle
!rori
00 00 00 00
00 00 00 00
00 00
!styles.location.rori.narmle
00 00
01

!restuss
!rori
00 00 00 00
00 00 00 00
00 00
!styles.location.rori.restuss
00 00
01

// naboo ============================================

!theed
!naboo
00 00 00 00
00 00 00 00
00 00
!styles.location.naboo.theed
00 00
01

!moenia
!naboo
00 00 00 00
00 00 00 00
00 00
!styles.location.naboo.moenia
00 00
01

!keren
!naboo
00 00 00 00
00 00 00 00
00 00
!styles.location.naboo.keren
00 00
01

!kaadara
!naboo
00 00 00 00
00 00 00 00
00 00
!styles.location.naboo.kaadara
00 00
01
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete