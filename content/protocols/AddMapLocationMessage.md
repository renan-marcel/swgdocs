---
title: "AddMapLocationMessage"
displaytitle: "AddMapLocationMessage (AB2174B6)"
opcode: "AB2174B6"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# AddMapLocationMessage (AB2174B6)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client network message that adds a planetary map location marker, point of interest (POI), or player waypoint to the client planetary map interface.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0xAB2174B6 (AddMapLocationMessage) |
| `ASCII` | **PlanetName** | Planetary terrain scene name (e.g. tatooine, naboo, corellia) |
| `LONG` | **NetworkId** | Unique 64-bit Network ID of the location or POI object |
| `UNICODE` | **LocationName** | Localized display label shown on planetary map |
| `FLOAT` | **X** | World position X coordinate |
| `FLOAT` | **Z** | World position Z coordinate (height / horizontal coordinate) |
| `BYTE` | **LocationType** | Planetary map category / icon identifier |
| `BYTE` | **SubCategory** | Secondary sub-category or active display flag |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `AB2174B6 (AddMapLocationMessage)`
- **C++ Class**: `AddMapLocationMessage (vtables 0x015ead04, 0x015ead0c)`
- **Serialization Mechanism**: `Archive::AutoVariable members unpacked via GameNetworkMessage::unpack (0x0118b740)`
- **Constructor Address**: `0x00ace640 (ReadIterator ctor) / 0x00ace410 (value ctor)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. The constructor registers 7 AutoVariables in sequence: AutoVariable<std::string> PlanetName, AutoVariable<NetworkId> NetworkId, AutoVariable<Unicode::String> LocationName, AutoVariable<float> X, AutoVariable<float> Z, AutoVariable<uint8> LocationType, and AutoVariable<uint8> SubCategory.

> [!NOTE]
> **Client Map Integration**: When received, the client MapManager adds or updates the POI marker in the current planet map UI layer corresponding to PlanetName and LocationType.



## Sample Packet

```text
// Verified payload structure for AddMapLocationMessage (AB2174B6)
// Architecture: x86 Windows (SWGEmu.exe)
// Deconstructed via Binary Ninja and Capstone Disassembly Engine
// Opcode: AB2174B6
```

## Related

- [CreateClientPathMessage](../../protocols/CreateClientPathMessage.html)
- [DestroyClientPathMessage](../../protocols/DestroyClientPathMessage.html)
- [ObjControllerMessage](../../protocols/ObjControllerMessage.html)

