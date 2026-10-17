---
title: ObjControllerMessage
url: https://wiki.swganh.org/index.php/ObjControllerMessage
page_type: Client/Server Packet
opcode: 80CE5E46
revision_id: 257260
last_modified: 
completion: 50%
direction: C→S
sample_status: absent
categories: ['Packets', 'Server Packets', 'Client Packets', '50% Complete']
templates: ['Template:PageHeader', 'Template:Short', 'Template:Int', 'Template:Long', 'Template:Uncertain', 'Template:ServerPacket', 'Template:ClientPacket', 'Template:50%', 'Template:100P', 'Template:75P', 'Template:25P', 'Template:0P', 'Template:50P']
---

# ObjControllerMessage

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | priority routing |
| INT | Opcode |
| INT | Flag Bitmask |
| INT | Header |
| LONG | ObjectID |
| INT | TickCount |
| ? | Data |

## Variable Descriptions
- Operand_Count	     = 5
- Opcode		     = 80CE5E46

## Notes
_none_

## Tags
- **S→C** - This packet originates on the server.
- **C→S** - This packet originates on the client.
- **50%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
- [[DataTransform (00000071)]]
- [[CombatAction (000000CC)]]
- [[CombatDamage (000000CD)]]
- [[StartNpcConversation (000000DD)]]
- [[StopNpcConversation (000000DE)]]
- [[NpcConversationMessage (000000DF)]]
- [[NPCConversationOptions (000000E0)]]
- [[SetupSwgSharedNetworkMessages (000000E1)]]
- [[OpponentInfo (000000E3)]]
- [[NetworkId (000000E5)]]
- [[NetworkId (000000E6)]]
- [[NetworkId (000000E7)]]
- [[NetworkId (000000E8)]]
- [[NetworkId (000000E9)]]
- [[HarvesterResourceData (000000EA)]]
- [[NetworkIdPair (000000EB)]]
- [[NetworkIdPair (000000EC)]]
- [[ResourceEmptyHopper (000000ED)]]
- [[GenericResponse (000000EE)]]
- [[DataTransformWithParent (000000F1)]]
- [[Animation (000000F2)]]
- [[SpatialChat (000000F3)]]
- [[SpatialChat (000000F4)]]
- [[MissionListRequest (000000F5)]]
- [[MissionListResponse (000000F6)]]
- [[MissionDetailsRequest (000000F7)]]
- [[MissionDetailsResponse (000000F8)]]
- [[MissionGenericRequest (000000F9)]]
- [[MissionGenericRequest (000000FB)]]
- [[MissionGenericResponse (000000FA)]]
- [[MissionGenericResponse (000000FC)]]
- [[MissionCreateRequest (000000FF)]]
- [[MissionGenericResponse (00000100)]]
- [[DraftSchematics (00000102)]]
- [[DraftSlots (00000103)]]
- [[CraftIngredients (00000105)]]
- [[CraftExperiment (00000106)]]
- [[CraftFillSlot (00000107)]]
- [[CraftEmptySlot (00000108)]]
- [[nextCraftingStage (00000109)]]
- [[nextCraftingStage(00000109)]]
- [[Generic (0000010A)]]
- [[Generic (0000010B)]]
- [[CraftAcknowledge (0000010C)]]
- [[GenericResponse (0000010D)]]
- [[CraftSelectSchematic (0000010E)]]
- [[CraftRequestSession (0000010F)]]
- [[Generic (00000110)]]
- [[Generic (00000111)]]
- [[CraftExperimentationResponse (00000113)]]
- [[NetworkId (00000114)]]
- [[SecureTrade (00000115)]]
- [[CommandQueueEnqueue (00000116)]]
- [[CommandQueueRemove (00000117)]]
- [[NetworkId (0000011C)]]
- [[TargetObject (00000126)]]
- [[NetworkId (00000127)]]
- [[NetworkIdAndTransform (0000012D)]]
- [[PlayerEmote (0000012E)]]
- [[Posture (00000131)]]
- [[CombatSpam (00000134)]]
- [[String (00000139)]]
- [[String (0000013A)]]
- [[SitOnObject (0000013B)]]
- [[TeleportAck (0000013F)]]
- [[WeaponRanges (00000140)]]
- [[missionAbort (00000142)]]
- [[ObjectMenuRequest (00000146)]]
- [[ObjectMenuResponse (00000147)]]
- [[SetupSwgSharedNetworkMessages (00000149)]]
- [[SetupSwgSharedNetworkMessages (0000014A)]]
- [[SetupSwgSharedNetworkMessages (0000014B)]]
- [[SetupSwgSharedNetworkMessages (0000014C)]]
- [[SetupSwgSharedNetworkMessages (0000014D)]]
- [[SetupSwgSharedNetworkMessages (0000014E)]]
- [[SetupSwgSharedNetworkMessages (0000014F)]]
- [[SetupSwgSharedNetworkMessages (00000150)]]
- [[SetupSwgSharedNetworkMessages (00000151)]]
- [[SetupSwgSharedNetworkMessages (00000152)]]
- [[NetworkId (00000153)]]
- [[SetupSwgSharedNetworkMessages (00000154)]]
- [[SetupSwgSharedNetworkMessages (00000155)]]
- [[SetupSwgSharedNetworkMessages (00000156)]]
- [[SetupSwgSharedNetworkMessages (00000157)]]
- [[SetupSwgSharedNetworkMessages (00000158)]]
- [[SetupSwgSharedNetworkMessages (00000159)]]
- [[CraftCustomization (0000015A)]]
- [[SpatialChatInternal (00000161)]]
- [[SetupSwgSharedNetworkMessages (00000165)]]
- [[EntertainerFlourishType (00000166)]]
- [[commandQueueAdd (00000167)]]
- [[ShowFlyText (000001BD)]]
- [[nextCraftingStageResult (000001BE)]]
- [[DraftSlotsQueryResponse (000001BF)]]
- [[CraftingSessionEnded (000001C2)]]
- [[BiographyUpdate (000001DB)]]
- [[PlayersNearYou (000001E7)]]
- [[StartingLocationList (000001FC)]]
- [[startingLocationSelectionResult (000001FD)]]
- [[SetupSwgSharedNetworkMessages (00000205)]]
- [[ResourceWeights (00000207)]]
- [[SetupSwgSharedNetworkMessages (0000021C)]]
- [[SetupSwgSharedNetworkMessages (0000021D)]]
- [[Buffs (00000229)]]
- [[SetupSharedNetworkMessages (0000022A)]]
- [[RemovePlayerBuffMessage (0000022A)]]
- [[objectMenuDirty (0000022B)]]
- [[SetupSharedNetworkMessages (0000022C)]]
- [[ImageDesignChangeMessage (00000238)]]
- [[ImageDesignEndMessage (00000239)]]
- [[ImageDesignStartMessage (0000023A)]]
- [[incubatorStart (0000025D)]]
- [[incubatorCommit (0000025E)]]
- [[incubatorCancel (0000025F)]]
- [[SetupSwgSharedNetworkMessages (000003E8)]]
- [[SetupSharedNetworkMessages (000003F5)]]
- [[SetupSwgSharedNetworkMessages (000003F6)]]
- [[SetupSwgSharedNetworkMessages (000003F7)]]
- [[SetupSharedNetworkMessages (000003F8)]]
- [[SetupSharedNetworkMessages (000003F9)]]
- [[SetupSwgSharedNetworkMessages (000003FA)]]
- [[UpdateShipOnCollision (000003FD)]]
- [[aboutToHyperspace (000003FE)]]
- [[SetupSwgSharedNetworkMessages (000003FF)]]
- [[SetupSwgSharedNetworkMessages (00000400)]]
- [[uiPlayEffect (00000401)]]
- [[SetupSwgSharedNetworkMessages (00000412)]]
- [[SetupSwgSharedNetworkMessages (00000413)]]
- [[SetupSwgSharedNetworkMessages (0000041C)]]
- [[JTLShipLocationList (0000041D)]]
- [[hyperspaceOrientShipToPointAndLockPlayerInput (0000042D)]]
- [[SetupSwgSharedNetworkMessages (0000042E)]]
- [[SetupSwgSharedNetworkMessages (0000042F)]]
- [[ShipHit (00000433)]]
- [[DroidCommandProgrammingMessage (00000435)]]
- [[SetupSwgSharedNetworkMessages (00000436)]]
- [[inviteOtherGroupMembersToLaunchIntoSpace (00000437)]]
- [[askGroupMemberToLaunchIntoSpace (00000438)]]
- [[groupMemberInvitationToLaunchIntoSpaceResponse (00000439)]]
- [[SetupSwgSharedNetworkMessages (0000043C)]]
- [[SetupSwgSharedNetworkMessages (0000043D)]]
- [[SetupSwgSharedNetworkMessages (0000043E)]]
- [[SetupSwgSharedNetworkMessages (0000043F)]]
- [[QuestTaskCounterMessage (00000440)]]
- [[QuestTaskTimerMessage (00000441)]]
- [[questTaskTimerData (00000444)]]
- [[CommandTimer (00000448)]]
- [[changeRoleIconChoice (0000044D)]]
- [[showCombatText (0000045A)]]
- [[setCurrentWorkingSkill (0000045B)]]
- [[setProfessionTemplate (0000045C)]]
- [[RequestActivateQuest(000004B7)]]
- [[RequestActivateQuest (000004B7)]]
- [[RequestCompleteQuest(000004B8)]]
- [[RequestCompleteQuest (000004B8)]]
- [[showLootBox(000004BC)]]
- [[showLootBox (000004BC)]]
- [[Unknown (000004BB)]]
- [[forceActivateQuest (000004BE)]]
- [[Unknown (000004BF)]]
- [[Unknown (000004C5)]]

## Other Sections
### Flags
| Flag | Mask |
| --- | --- |
| NONE | 0x00000000 |
| SEND | 0x00000001 |
| RELIABLE | 0x00000002 |
| SOURCE_REMOTE_SERVER | 0x00000004 |
| DEST_AUTH_CLIENT | 0x00000008 |
| DEST_PROXY_CLIENT | 0x00000010 |
| DEST_AUTH_SERVER | 0x00000020 |
| DEST_PROXY_SERVER | 0x00000040 |
| SOURCE_REMOTE_CLIENT | 0x00000100 |

## Categories
Packets | Server Packets | Client Packets | 50% Complete