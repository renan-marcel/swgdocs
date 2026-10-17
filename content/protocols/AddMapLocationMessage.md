---
title: "AddMapLocationMessage"
displaytitle: "AddMapLocationMessage (AB2174B6)"
opcode: "AB2174B6"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "0%"
sample_status: "absent"
status: "stub"
---

# AddMapLocationMessage (AB2174B6)

> [!CAUTION]
> **Documentation Pending / Reversal Needed**
> This packet was identified in SWG network specifications (Opcode: `AB2174B6`), but requires packet captures to fully verify all payload offsets.

Server-to-client message that adds a planetary map location marker, point of interest (POI), or player waypoint to the client map interface.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Number of operands (header) |
| `INT` | **Opcode** | 0xAB2174B6 |
| `ASCII` | **LocationName** | Name/label displayed on planetary map |
| `FLOAT` | **X** | World X coordinate |
| `FLOAT` | **Z** | World Z coordinate (height) |
| `FLOAT` | **Y** | World Y coordinate |
| `INT` | **LocationType** | Planetary map icon / category identifier |
| `LONG` | **LocationId** | Unique location / waypoint object ID |


## Variable Descriptions

- **Operand_Count**: `2 (standard operand header count)`
- **Opcode**: `AB2174B6 (Server Packet)`
- **Subsystem**: `Planetary Map & Waypoint Navigation`


## Notes & Warnings

> [!WARNING]
> **Pending Reversal**: This packet was identified in client network tables (opcode AB2174B6) with 100% recognition in master protocol lists, but detailed field layout requires confirmation from packet captures.



## Sample Packet

```text
// Sample packet capture pending for opcode AB2174B6
```

## Related

- [PlanetMapManagerClient (PacketTypeGroup)](../../protocols/PlanetMapManagerClient (PacketTypeGroup).html)
- [CreateClientPathMessage](../../protocols/CreateClientPathMessage.html)
- [DestroyClientPathMessage](../../protocols/DestroyClientPathMessage.html)

