---
title: INSO07
url: https://wiki.swganh.org/index.php/INSO07
page_type: Baseline
opcode: 
revision_id: 21381
last_modified: 
completion: 75%
direction: unknown
sample_status: placeholder
categories: ['Packets', 'Server Packets', '75% Complete']
templates: ['Template:PageHeader', 'Template:INSOArchitectureNAV', 'Template:75%']
---

# INSO07

## Notices
_none_

## Description
SWGANH Wiki is a repository of Star Wars Galaxies Developer information. This site is only meant to be used by SWGANH Developer team.

## Struct
| Type | Name |
| --- | --- |
| SHORT | ObjectOpperandCount |
| BYTE | ResourcePoolUpdateFlag |
| INT | ResourcePoolIDs |
| INT | UpdateCounter |
| LONG | GlobalResourceID |
| INT | ResourcePoolIDs |
| INT | UpdateCounter |
| LONG | GlobalResourceID |
| INT | ResourcePoolNames |
| INT | UpdateCounter |
| ASTRING | ResourceName |
| INT | ResourcePoolTypes |
| INT | UpdateCounter |
| ASTRING | ResourceType |
| LONG | SelectedGlobalResourceID |
| BYTE | ActiveFlag |
| INT | ExtractionRateMaxDisplayed |
| FLOAT | ExtractionRateMax |
| FLOAT | CurrentExtractionRate |
| FLOAT | CurrentHopperSize |
| INT | HopperSizeMax |
| BYTE | HopperUpdateFlag |
| INT | HopperContentsSize |
| INT | UpdateCounter |
| LONG | GlobalResourceID |
| FLOAT | ResourceQuantity |
| BYTE | Condition |

## Variable Descriptions
- ObjectOpperandCount = 16

## Notes
- **NOTE:** If the data doesnt finish "downloading", you probably need to send a blank baseline and a full Delta Message, or just a Delta Message with the BYTE flags as 1's (or zeros) . Something to toy with still...

## Tags
- **75%** - This packet has been partially reversed.

## Sample Packet
_none_

## Related Pages
- [[ResourceHarvesterActivatePageMessage]]
- [[HarvesterResourceData (000000EA)]]

## Other Sections
_none_

## Categories
Packets | Server Packets | 75% Complete