---
title: CombatAction (000000CC)
url: https://wiki.swganh.org/index.php/CombatAction_%28000000CC%29
page_type: Object Controller
opcode: 000000CC
revision_id: 49321
last_modified: 
completion: 100%
direction: unknown
sample_status: present
categories: ['Packets', 'ControllerIDs', '100% Complete']
templates: ['Template:PageHeader', 'Template:ObjControllerMessageTag', 'Template:100%']
---

# CombatAction (000000CC)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
| fire_single | 0xA198F47D |
| fire_burst | 0xC5ACFDD8 |
| fire_suppression | 0x9DC309E9 |
| ranged_coup_de_grace | 0x18E40286 |
| unarmed_coup_de_grace | 0x96008CB9 |
| melee_coup_de_grace | 0xAA69DF3 |
| fire_acrobatic | 0xBF7F2AA |
| tumble_facing | 0x1E904B4F |
| tumble | 0x9D2BC971 |
| warcry | 0x2C71E1EA |
| force_throw_1_arc_particle_level_1_light | 0xA32D4F4F |
| force_throw_1_arc_particle_level_1_medium | 0xD38F8A6 |
| force_throw_1_particle_level_1_light | 0xA12F155B |
| force_throw_1_particle_level_1_medium | 0xA197EFA3 |
| force_mind_blast_1_arc_particle_level_1_light | 0x2F6BDDB3 |
| force_mind_blast_1_arc_particle_level_1_medium | 0x60D20A88 |
| force_mind_blast_1_particle_level_1_light | 0x3F37228A |
| force_mind_blast_1_particle_level_1_medium | 0xFF5FAD81 |
| force_knockdown_1_particle_level_1 | 0xCE4B23A1 |
| force_knockdown_1_arc_particle_level_1 | 0x542EE645 |
| force_intimidate | 0x73C5BE9D |
| force_intimidate_chain | 0xA982DE84 |
| force_weaken_1_arc_particle_level_1_light | 0xD9B51B63 |
| force_weaken_1_arc_particle_level_1_medium | 0x896F4F5F |
| force_weaken_1_particle_level_1_light | 0x60BBC63C |
| force_weaken_1_particle_level_1_medium | 0x33C099C2 |
| force_healing_1 | 0xBF050580 |
| force_drain_1 | 0xE6D39F0C |
| force_transfer_1 | 0xFA3497F6 |
| mind_trick_1 | 0x895A4380 |
| force_lightning_1_particle_level_1_light | 0xF14F310A |
| force_lightning_1_particle_level_1_medium | 0x1171D9FB |
| force_lightning_1_particle_level_2_light | 0xC2F7C8DB |
| force_lightning_1_particle_level_2_medium | 0x4F143B17 |
| force_lightning_1_particle_level_3_light | 0xD39F9F94 |
| force_lightning_1_particle_level_3_medium | 0x85C89A4C |
| force_lightning_1_particle_level_4_light | 0x139AFA7C |
| force_lightning_1_particle_level_4_medium | 0x44C33ECA |
| force_lightning_1_particle_level_5_light | 0x2F2AD33 |
| force_lightning_1_particle_level_5_medium | 0x8E1F9F91 |
| force_lightning_1_arc_particle_level_1_light | 0x73D92090 |
| force_lightning_1_arc_particle_level_1_medium | 0x591ED8E0 |
| force_lightning_1_arc_particle_level_2_light | 0x4061D941 |
| force_lightning_1_arc_particle_level_2_medium | 0x77B3A0C |
| force_lightning_1_arc_particle_level_3_light | 0x51098E0E |
| force_lightning_1_arc_particle_level_3_medium | 0xCDA79B57 |
| force_lightning_1_arc_particle_level_4_light | 0x910CEBE6 |
| force_lightning_1_arc_particle_level_4_medium | 0xCAC3FD1 |
| force_lightning_1_arc_particle_level_5_light | 0x8064BCA9 |
| force_lightning_1_arc_particle_level_5_medium | 0xC6709E8A |
| force_choke_1_arc_particle_level_1_light | 0x18B5E779 |
| force_choke_1_arc_particle_level_1_medium | 0x2FA3D4C0 |
| force_choke_1_particle_level_1_light | 0x45CD3B94 |
| force_choke_1_particle_level_1_medium | 0x855EC8E8 |
| force_channel_2_particles_light | 0x43869982 |
| force_channel_2_particles_medium | 0x47CE141C |
| force_channel_1_particle_light | 0xBAA5A7B5 |
| force_channel_1_particle_medium | 0xD20A42E8 |
| force_blast_2_particles_light | 0x85BCDAC5 |
| force_blast_2_particles_medium | 0x3528EF75 |
| force_blast_1_particle_light | 0xE0D07B0D |
| force_blast_1_particle_medium | 0x143001AF |
| force_absorb_2_particles_light | 0x129732F9 |
| force_absorb_2_particles_medium | 0xC149FA7C |
| force_absorb_1_particle_light | 0xD9DEB6D |
| force_absorb_1_particle_medium | 0x831BE993 |
| point_and_laugh | 0x952A74B9 |
| intimidate | 0x5027C538 |
| rescue | 0xEE6E222F |
| fire_defender_posture_change_up | 0x4CCDBF4E |
| fire_defender_posture_change_down | 0xAEBEC072 |
| fire_area_light | 0x20A82F7F |
| fire_area_medium | 0x9DD64F12 |
| fire_area_no_trails_light | 0x74B8822B |
| fire_area_no_trails_medium | 0x465FCCD4 |
| fire_5_single_medium | 0xD1126A8A |
| fire_5_single_light | 0xFFBB704B |
| fire_5_single_medium_face | 0xBB5B427 |
| fire_5_single_light_face | 0x199B6040 |
| fire_7_single_medium | 0x82CDB434 |
| fire_7_single_light | 0x7D269FC4 |
| fire_7_single_medium_face | 0xA7AAB14F |
| fire_7_single_light_face | 0xAB8B5754 |
| fire_9_single_medium | 0xE2F7EF01 |
| fire_9_single_light | 0x2AD05266 |
| fire_9_single_medium_face | 0x54E96B53 |
| fire_9_single_light_face | 0xB5F8D238 |
| fire_5_special_single_light | 0xCC61B17C |
| fire_5_special_single_medium | 0x441CC581 |
| fire_5_special_single_light_face | 0xB1ED3658 |
| fire_5_special_single_medium_face | 0xC32BDB1B |
| fire_3_single_light | 0xCE0081DF |
| fire_3_single_medium | 0x936EC84D |
| fire_3_single_light_face | 0xCFAA397C |
| fire_3_single_medium_face | 0xFF95BB9F |
| fire_3_special_single_light | 0x8EEA3C5C |
| fire_3_special_single_medium | 0xA4E86D94 |
| fire_3_special_single_light_face | 0xC9BF89A5 |
| fire_3_special_single_medium_face | 0x1928FC1C |
| fire_1_single_light | 0x4C9D6E50 |
| fire_1_single_medium | 0xC0B116F3 |
| fire_1_single_light_face | 0x7DBA0E68 |
| fire_1_single_medium_face | 0x538ABEF7 |
| fire_1_special_single_light | 0xDD98F8BF |
| fire_1_special_single_medium | 0x4BBF598 |
| fire_1_special_single_light_face | 0x8C7A5C0D |
| fire_1_special_single_medium_face | 0xAFD61E1E |
| test_swoosh | 0x12CCB50E |
| test_homing | 0x25355503 |
| test_heavy_weapon | 0x263ADB53 |
| test_heavy_weapon_particle_system | 0x76598837 |
| test_sword_ricochet | 0xE30B91AA |
| test_sword_throw | 0x7DAE60BF |
| test_flamethrower_arc | 0x737DB3A3 |
| test_lightning_1 | 0xDB614110 |
| test_lightning_2 | 0x247021D |
| test_lightning_passive_actors | 0xE0FD567 |
| fire_flame_thrower_cone_1_light | 0xF338D78F |
| fire_flame_thrower_cone_1_medium | 0x94F86763 |
| fire_flame_thrower_cone_2_light | 0xC0802E5E |
| fire_flame_thrower_cone_2_medium | 0xCA9D858F |
| fire_flame_thrower_single_1_light | 0xA4AE26EC |
| fire_flame_thrower_single_1_medium | 0xDA4F1733 |
| fire_flame_thrower_single_2_light | 0x9716DF3D |
| fire_flame_thrower_single_2_medium | 0x842AF5DF |
| fire_lightning_rifle_single_1_light | 0xFA1A12B7 |
| fire_lightning_rifle_single_1_medium | 0xBC717F54 |
| fire_lightning_rifle_single_2_light | 0xC9A2EB66 |
| fire_lightning_rifle_single_2_medium | 0xE2149DB8 |
| fire_acid_rifle_single_1_light | 0x24BA04B1 |
| fire_acid_rifle_single_1_medium | 0xEE25958 |
| fire_acid_rifle_single_2_light | 0x1702FD60 |
| fire_acid_rifle_single_2_medium | 0x5087BBB4 |
| test_flamethrower | 0x71DEA592 |
| saberthrow_posture_change | 0x298A023F |
| saberthrow_light | 0x3737DE16 |
| saberthrow_medium | 0x5F7BC6D |
| fire_heavy_rocket_launcher_light | 0xB3743368 |
| fire_heavy_rocket_launcher_medium | 0xE8CEC55C |
| fire_heavy_particle_beam_light | 0xF61155B7 |
| fire_heavy_particle_beam_medium | 0xBC7D7413 |
| fire_heavy_lightning_beam_light | 0x28C12D20 |
| fire_heavy_lightning_beam_medium | 0x27C8FE50 |
| fire_heavy_acid_beam_light | 0xFCB2CA1A |
| fire_heavy_acid_beam_medium | 0x61A7354C |
| change_posture | 0x450229AB |
| posture_scramble | 0xA620916D |
| dodge | 0x4FF30E4 |
| go_incapacitated | 0x82021A0D |
| get_hit_light | 0xC1496B10 |
| get_hit_medium | 0xB74C44C2 |
| attack_high_left_light_0 | 0x28664799 |
| attack_high_center_light_0 | 0x917B54F5 |
| attack_high_right_light_0 | 0xEC73E23C |
| attack_mid_left_light_0 | 0xCC03407 |
| attack_mid_center_light_0 | 0xD0FFC443 |
| attack_mid_right_light_0 | 0x78CCD756 |
| attack_low_left_light_0 | 0xFBCA414B |
| attack_low_center_light_0 | 0xEB876830 |
| attack_low_right_light_0 | 0x6BD05722 |
| attack_high_left_medium_0 | 0xFB582775 |
| attack_high_center_medium_0 | 0x8BC93FF |
| attack_high_right_medium_0 | 0x9EA1D836 |
| attack_mid_left_medium_0 | 0x6FE7121F |
| attack_mid_center_medium_0 | 0xC43DAFC8 |
| attack_mid_right_medium_0 | 0xDF254880 |
| attack_low_left_medium_0 | 0x7CFB926B |
| attack_low_center_medium_0 | 0xFA3D2089 |
| attack_low_right_medium_0 | 0xE45DE4F3 |
| attack_high_left_light_1 | 0x9F7B869D |
| attack_high_center_light_1 | 0x266695F1 |
| attack_high_right_light_1 | 0x5B6E2338 |
| attack_mid_left_light_1 | 0xBBDDF503 |
| attack_mid_center_light_1 | 0x67E20547 |
| attack_mid_right_light_1 | 0xCFD11652 |
| attack_low_left_light_1 | 0x4CD7804F |
| attack_low_center_light_1 | 0x5C9AA934 |
| attack_low_right_light_1 | 0xDCCD9626 |
| attack_high_left_medium_1 | 0x4C45E671 |
| attack_high_center_medium_1 | 0xBFA152FB |
| attack_high_right_medium_1 | 0x29BC1932 |
| attack_mid_left_medium_1 | 0xD8FAD31B |
| attack_mid_center_medium_1 | 0x73206ECC |
| attack_mid_right_medium_1 | 0x68388984 |
| attack_low_left_medium_1 | 0xCBE6536F |
| attack_low_center_medium_1 | 0x4D20E18D |
| attack_low_right_medium_1 | 0x534025F7 |
| attack_high_left_light_2 | 0x465DC590 |
| attack_high_center_light_2 | 0xFF40D6FC |
| attack_high_right_light_2 | 0x82486035 |
| attack_mid_left_light_2 | 0x62FBB60E |
| attack_mid_center_light_2 | 0xBEC4464A |
| attack_mid_right_light_2 | 0x16F7555F |
| attack_low_left_light_2 | 0x95F1C342 |
| attack_low_center_light_2 | 0x85BCEA39 |
| attack_low_right_light_2 | 0x5EBD52B |
| attack_high_left_medium_2 | 0x9563A57C |
| attack_high_center_medium_2 | 0x668711F6 |
| attack_high_right_medium_2 | 0xF09A5A3F |
| attack_mid_left_medium_2 | 0x1DC9016 |
| attack_mid_center_medium_2 | 0xAA062DC1 |
| attack_mid_right_medium_2 | 0xB11ECA89 |
| attack_low_left_medium_2 | 0x12C01062 |
| attack_low_center_medium_2 | 0x9406A280 |
| attack_low_right_medium_2 | 0x8A6666FA |
| attack_high_left_light_3 | 0xF1400494 |
| attack_high_center_light_3 | 0x485D17F8 |
| attack_high_right_light_3 | 0x3555A131 |
| attack_mid_left_light_3 | 0xD5E6770A |
| attack_mid_center_light_3 | 0x9D9874E |
| attack_mid_right_light_3 | 0xA1EA945B |
| attack_low_left_light_3 | 0x22EC0246 |
| attack_low_center_light_3 | 0x32A12B3D |
| attack_low_right_light_3 | 0xB2F6142F |

## Variable Descriptions
_none_

## Notes
_none_

## Tags
- **OCM** - This header is part of the ObjControllerMessage .
- **100%** - This packet has been completely reversed.

## Sample Packet
```
05 00 			   'Opperand Count
46 5E CE 80 		   'ObjController
1B 00 00 00 		   'Sub-Op
CC 00 00 00 		   'CommandOp
19 00 00 00 00 00 00 00   'Reciepeint ID
00 00 00 00 		   'Spacing
08 E3 38 40 		   'Animation CRC
19 00 00 00 00 00 00 00   'Character ID
3A 00 00 00 00 00 00 00   'Character ID + Weapon ID Offset (58)
00 			   'Posture
FF FF 			   'Red Tail
01 00 			   'Num of Defenders
7C 1B 06 00 00 00 00 00   'Defender ID
00                        'posture of defender
01 00 
C2 AD
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | ControllerIDs | 100% Complete