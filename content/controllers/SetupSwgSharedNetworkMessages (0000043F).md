---
title: "SetupSwgSharedNetworkMessages (0000043F)"
displaytitle: "SetupSwgSharedNetworkMessages (0000043F)"
opcode: "0000043F"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "C↔S"
completion: "0%"
discovery_source: "Decomp do Binary Ninja"
sample_status: "absent"
status: "stub"
---

# SetupSwgSharedNetworkMessages (0000043F)

> [!NOTE]
> **Origem da Descoberta: Decomp do Binary Ninja**
> Este opcode/identificador foi descoberto a partir da desmontagem e descompilação estática do executável cliente SWGEmu.exe via Binary Ninja, aguardando mapeamento completo de membros e serialização.

Jump to Lightspeed / Space flight controller message for ship component and flight state updates.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x0000043F |
| `LONG` | **ShipId** | Network ID of ship object |
| `INT` | **TickCount** | Tick counter |
| `DATA` | **FlightData** | Flight subsystem parameters (pending capture) |


## Variable Descriptions

- **Controller Opcode**: `0000043F (Hex) / 1087 (Dec)`
- **Subsystem**: `Jump to Lightspeed (JTL) Space Flight`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Part of the 0x438-0x43F block handling space operations.



## Sample Packet

```text
// Sample packet capture pending for opcode 0000043F
```

## Related

- [SetupSwgSharedNetworkMessages (0000043E)](../../controllers/SetupSwgSharedNetworkMessages (0000043E).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

