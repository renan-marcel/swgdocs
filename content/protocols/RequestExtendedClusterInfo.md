---
title: "RequestExtendedClusterInfo"
displaytitle: "RequestExtendedClusterInfo (8E33ED05)"
opcode: "8E33ED05"
section: "protocols"
category: "Login & Connection"
direction: "C→S"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# RequestExtendedClusterInfo (8E33ED05)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `8E33ED05`), but requires packet captures to fully verify all payload offsets.

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
- [Main::Login (PacketTypeGroup)](../../protocols/Main%3A%3ALogin (PacketTypeGroup).html)

