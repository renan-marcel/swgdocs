---
title: SWG Packet Encryption
url: https://wiki.swganh.org/index.php/SWG_Packet_Encryption
page_type: Other
opcode: 
revision_id: 2316
last_modified: 2006-12-21T07:42:49Z
completion: unknown
direction: unknown
sample_status: present
categories: []
templates: []
---

# SWG Packet Encryption

## Notices
_none_

## Description
_none_

## Struct
_none_

## Variable Descriptions
_none_

## Notes
_none_

## Tags
_none_

## Sample Packet
```
00 09 00 01 00 02 AB 43 E3 D5 00 FF 00 11 45 32 76 43 D4 F1 00 AB CD

First we know the first 2 bytes are the SOE opcode 0x09 (data on channel 00) So we ignore this as we need it to identify
the packet. We also ignore the last two because it is for the CRC value. The remainder is what needs to be encrypted
(or decrypted in another case).

Say our Key is '''(1D 4E 32 87)''' this will also act as our first mask.

So, taking the first 4 bytes after the SOE opcode '''(00 01 00 02)'''

00 01 00 02 XOR
1D 4E 32 87
-------------
1D 4F 32 85

So the beginning of the new packet is '''00 09 1D 4F 32 85'''. Now we take the result as our new mask and xor the next 4 bytes

AB 43 E3 D5 XOR
1D 4F 32 85
-------------
B6 0C D1 50

New packet so far: 00 09 1D 4F 32 85 B6 0C D1 50
New mask: B6 0C D1 50
00 FF 00 11 XOR
B6 0C D1 50
------------
B6 F3 D1 41

New packet so far:  00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41
New mask: B6 F3 D1 41
45 32 76 43 XOR
B6 F3 D1 41
-------------
F3 C1 A7 02

New packet so far: 00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41 F3 C1 A7 02
New mask: F3 C1 A7 02

Now that we are out of full 4 byte blocks, we xor each last byte with the first byte in our “key” 

D4 F1 00 XOR   This is done in a separate loop, and per byte, so D4 xor F3, then F1 
F3 F3 F3       xor F3, then 0E xor F3. And the results are all appended to our packet
---------             
27 02 F3

Final Encrypted Packet: 00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41 F3 C1 A7 02 27 02 F3 AB CD
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
_none_