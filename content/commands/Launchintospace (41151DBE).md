---
title: Launchintospace (41151DBE)
url: https://wiki.swganh.org/index.php/Launchintospace_%2841151DBE%29
page_type: Command
opcode: 41151DBE
revision_id: 15770
last_modified: 2007-09-09T02:40:25Z
completion: 75%
direction: C→S
sample_status: present
categories: ['Packets', 'Client Packets', 'Server Packets', '75% Complete', 'CommandQueueEnqueue', 'Client Commands']
templates: ['Template:PageHeader', 'Template:ClientPacket', 'Template:75%', 'Template:CommandQueueEnqueue', 'Template:ClientCommands']
---

# Launchintospace (41151DBE)

## Notices
_none_

## Struct
| Type | Name |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

## Variable Descriptions
- Opperand_Count	     =
- Opcode		     = 41151DBE

## Notes
_none_

## Tags
- **C→S** - This packet originates on the client.
- **75%** - This packet has been partially reversed.
- **CQE** - This Command is part of the CommandQueueEnqueue .
- **Command** - This is a client command.

## Sample Packet
```
05 00 
46 5E CE 80 // ObjControllerMessage
23 00 00 00 
16 01 00 00 
D2 CD 31 6E 0C 00 00 00 // character ID
00 00 00 00 
20 00 00 40 
BE 1D 15 41 // launchintospace
9A 3C 2F 00 00 00 00 00 
0D 00 00 00                               // u-string count
35 00 33 00 34 00 33 00 30 00 34 00 33 00 // 5.3.4.3.0.4.3.
36 00 31 00 37 00 31 00 20 00 30 00       // 6.1.7.1.
01 48 01     // comp+crc
----

"41151DBE",1073741920,4116124,39,"130686489931 0 corellia Tyrena_Starport"
"41151DBE",1073741952,3095711,43,"130686489931 0 tatooine Mos_Eisley_Starport"
"41151DBE",1073742048,1279066,35,"130686489931 0 lok Nym's_Stronghold"
"41151DBE",1073748992,1270278,47,"144508853207 0 dantooine Dantooine_Agro_Outpost"
"41151DBE",1073745472,1270278,49,"114291279249 0 dantooine Dantooine_Mining_Outpost"
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
Packets | Client Packets | Server Packets | 75% Complete | CommandQueueEnqueue | Client Commands