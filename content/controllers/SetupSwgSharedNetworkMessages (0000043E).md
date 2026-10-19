---
title: "SetupSwgSharedNetworkMessages (0000043E)"
displaytitle: "SetupSwgSharedNetworkMessages (0000043E)"
opcode: "0000043E"
section: "controllers"
category: "Advanced Subsystem Triggers (0x151+)"
direction: "C↔S"
completion: "0%"
discovery_source: "Decomp do Binary Ninja"
sample_status: "absent"
status: "stub"
---

# SetupSwgSharedNetworkMessages (0000043E)

> [!NOTE]
> **Origem da Descoberta: Decomp do Binary Ninja**
> Este opcode/identificador foi descoberto a partir da desmontagem e descompilação estática do executável cliente SWGEmu.exe via Binary Ninja, aguardando mapeamento completo de membros e serialização.

Jump to Lightspeed / Space flight controller message for ship component and flight state updates.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `INT` | **Operand_Count** | 0x0000000B (ObjControllerMessage wrapper) |
| `INT` | **ControllerOpcode** | 0x0000043E |
| `LONG` | **ShipId** | Network ID of ship object |
| `INT` | **TickCount** | Tick counter |
| `DATA` | **FlightData** | Flight subsystem parameters (pending capture) |


## Variable Descriptions

- **Controller Opcode**: `0000043E (Hex) / 1086 (Dec)`
- **Subsystem**: `Jump to Lightspeed (JTL) Space Flight`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Part of the 0x438-0x43F block handling space operations.



## Sample Packet

```text
// Sample packet capture pending for opcode 0000043E
```

## Related

- [SetupSwgSharedNetworkMessages (0000043D)](../../controllers/SetupSwgSharedNetworkMessages (0000043D).html)
- [ObjControllerMessage](../../controllers/ObjControllerMessage.html)

