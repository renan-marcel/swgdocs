---
title: "GetCommentsResponseMessage"
displaytitle: "GetCommentsResponseMessage (EADB08CA)"
opcode: "EADB08CA"
section: "protocols"
category: "General & System Packets"
direction: "S→C"
completion: "100%"
sample_status: "present"
status: "verified"
---

# GetCommentsResponseMessage (EADB08CA)

> [!NOTE]
> **Verified via Binary Analysis (SWGEmu.exe)**
> This payload structure and deserialization sequence has been fully reversed and verified against the client binary using Binary Ninja and Rea decompiler evidence.

Server-to-client customer service response returning the conversation thread and comment history of an existing CSR ticket.

## Struct

| Data Type | Field Name | Notes |
| :--- | :--- | :--- |
| `SHORT` | **Operand_Count** | Standard operand count header (0x0002) |
| `INT` | **Opcode** | 0xEADB08CA (GetCommentsResponseMessage) |
| `INT` | **TicketId** | Target CSR ticket identifier number |
| `INT` | **CommentCount** | Number of comment entries in the array |
| `INT` | **CommentId** | CustomerServiceComment field: unique comment ID |
| `INT` | **Timestamp** | CustomerServiceComment field: UNIX timestamp of comment |
| `BYTE` | **FromPlayer** | CustomerServiceComment field: boolean flag (1 if from player, 0 if from CSR staff) |
| `UNICODE` | **AuthorName** | CustomerServiceComment field: display name of comment author |
| `UNICODE` | **CommentText** | CustomerServiceComment field: full comment text content |


## Variable Descriptions

- **Operand_Count**: `0x0002 (Short count)`
- **Opcode**: `EADB08CA (GetCommentsResponseMessage)`
- **C++ Class**: `GetCommentsResponseMessage (vtables 0x015ebba4, 0x015ebb9c)`
- **Constructor Address**: `0x00af8dd4 (ReadIterator ctor)`
- **AutoArray Element Struct**: `CustomerServiceComment (36 bytes: CommentId, Timestamp, FromPlayer, AuthorName, CommentText)`


## Notes & Warnings

> [!NOTE]
> **Binary Reversal Verification**: Fully verified against SWGEmu.exe client binary. Constructor registers AutoVariable<unsigned int> TicketId (+0x2c) and AutoArray<CustomerServiceComment> (+0x40). CustomerServiceComment serialization at 0x00b1cbc0 writes CommentId (4 bytes), Timestamp (4 bytes), FromPlayer (1 byte), AuthorName (Unicode::String), and CommentText (Unicode::String).



## Sample Packet

```text
02 00 ca 08 db ea 2a 00 00 00 01 00 00 00 01 00 00 00 37 45 92 41 00 03 00 00 00 43 00 53 00 52 00 09 00 00 00 57 00 65 00 20 00 61 00 72 00 65 00 20 00 6f 00 6e 00
```

## Related

- [CreateTicketResponseMessage](../../protocols/CreateTicketResponseMessage.html)
- [AppendCommentResponseMessage](../../protocols/AppendCommentResponseMessage.html)

