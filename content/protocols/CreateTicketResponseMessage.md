---
title: "CreateTicketResponseMessage"
displaytitle: "CreateTicketResponseMessage (550A407A)"
opcode: "550A407A"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# CreateTicketResponseMessage (550A407A)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client customer support response confirming the successful submission or status of a Customer Service (CSR) support ticket.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0x550A407A (CreateTicketResponseMessage) |
| `INT` | **TicketId** | Assigned Customer Service ticket identifier number |
| `INT` | **ResultCode** | Result status code (0 = success, non-zero = error code) |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `550A407A (CreateTicketResponseMessage)`
- **C++ Class**: `CreateTicketResponseMessage (vtables 0x015ebc34, 0x015ebc2c)`
- **Constructor Address**: `0x00afa5ee (ReadIterator ctor)`
- **AutoVariables**: `AutoVariable<unsigned int> TicketId (+0x2c), AutoVariable<unsigned int> ResultCode (+0x3c)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Disassembly of ctor 0x00afa5ee shows initialization of two 32-bit AutoVariable members: TicketId and ResultCode.

> [!NOTE]
> **CSR Interface Integration**: The client CSR dialog updates with the newly created ticket reference ID, allowing the player to view ticket status in the Help UI.



## Sample Packet

```text
02 00 7a 40 0a 55 2a 00 00 00 00 00 00 00
```

## Related

- [GetCommentsResponseMessage](../../protocols/GetCommentsResponseMessage.html)
- [CancelTicketResponseMessage](../../protocols/CancelTicketResponseMessage.html)
- [AppendCommentResponseMessage](../../protocols/AppendCommentResponseMessage.html)

