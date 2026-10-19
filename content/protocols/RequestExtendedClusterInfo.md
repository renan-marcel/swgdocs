---
title: "RequestExtendedClusterInfo"
displaytitle: "RequestExtendedClusterInfo (8E33ED05)"
opcode: "8E33ED05"
section: "protocols"
category: "Login & Connection"
direction: "C→S"
completion: "0%"
discovery_source: "Decomp do Binary Ninja"
sample_status: "absent"
status: "stub"
---

# RequestExtendedClusterInfo (8E33ED05)

> [!NOTE]
> **Origem da Descoberta: Decomp do Binary Ninja**
> Este opcode/identificador foi descoberto a partir da desmontagem e descompilação estática do executável cliente SWGEmu.exe via Binary Ninja, aguardando mapeamento completo de membros e serialização.

Client-to-server request sent during cluster / server selection to retrieve extended cluster status, population indicators, and connection metrics.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Number of operands (header) |
| `INT` | **Opcode** | 0x8E33ED05 |
| `INT` | **ClusterId** | Identifier of target galaxy cluster |


## Variable Descriptions

- **Operand_Count**: `1`
- **Opcode**: `8E33ED05 (Client Packet)`
- **Subsystem**: `Login Server Cluster Selection`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: Sent by the client while browsing the galaxy selection list before establishing a game connection. Field layout requires verification against live cluster packets.



## Sample Packet

```text
// Sample packet capture pending for opcode 8E33ED05
```

## Related

- [LoginClusterStatus](../../protocols/LoginClusterStatus.html)
- [LoginClientId](../../protocols/LoginClientId.html)
- [Main::Login (PacketTypeGroup)](../../protocols/Main--Login (PacketTypeGroup).html)

