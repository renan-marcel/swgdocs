---
title: Packet:Encryption
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet%3AEncryption
wiki_revid: 1670
layout: guide
date_audited: 2026-10-17
---

# Packet:Encryption

SWG uses a XOR Mask encryption based off the value of the CRCSeed exhanged in the Session Reply packet. 
All the data between the SOE Opcode and CRC value are encrypted. 
If the packet does not contain any SOE Protocol, it is encrypted between the 1st byte and the CRC value. XOR is a simple bitwise 
operation on 2 numbers, know as an exclusive-or, when ONLY 1 bit is 1, results in a 1. This is it's truth table.

A  B     C
0  0     0
0  1     1
1  0     1
1  1     0

For more information on the XOR operator, use Google.

Here are code samples of the Encrypt() and Decrypt() functions.

//PROTOTYPES

void Decrypt(char *pData,unsigned short nLength, unsigned int nCrcSeed);
void Encrypt(char *pData,unsigned short nLength,unsigned int nCRCSeed);

//DECRYPT

void Decrypt(char *pData,unsigned short nLength,unsigned int nCrcSeed)
{

```text
   nLength-=4;
   unsigned int *Data = (unsigned int*)(pData+2);
   short block_count = (nLength / 4);
   short byte_count = (nLength % 4);
   unsigned int itemp;
   for(short count = 0;count<block_count;count++)
   {
       itemp = *Data;
       *Data ^= nCrcSeed;
       nCrcSeed = itemp;
       Data++;
   }
   pData = (char*)Data;
   for(short count = 0;count<byte_count;count++)
   {
       *pData ^= nCrcSeed;
       pData++;
   }

```

}

//ENCRYPT

void Encrypt(char *pData, unsigned short nLength,unsigned int nCrcSeed)
{

```text
   nLength-=4;
   unsigned int *Data = (unsigned int*)(pData+2);
   short block_count = (nLength / 4);
   short byte_count = (nLength % 4);
   unsigned int itemp;
   for(short count = 0;count<block_count;count++)
   {
       *Data ^= nCrcSeed;
       nCrcSeed = *Data;
       Data++;
   }
   pData = (char*)Data;
   for(short count = 0;count<byte_count;count++)
   {
       *pData ^= (char)nCrcSeed;
       pData++;
   }

```

}

Encryption Explained:

It begins by adjusting the pointer and data length to exclude the SOE Opcode and CRC Value at the beginning and end of the packet.
Then the number of "blocks" or 4 byte chunks of data are calculated. Then a remainder of bytes are calculated. 
The algorithm uses a for loop to go through each chunk, 
and then each remaining byte of the packet to encrypt/decrypt.
The algorithm stats off by using the CRCSeed as the first mask value to do the XOR operation against.
For encryption, the resulted data is then set as the new mask. For decryption, the original data is copied, 
then the XOR operation occures, and the 
copy of the encrypted data is set as the new mask.
This recurses for EACH "block" of data.
When it gets down to the remainder, the first byte of the last mask is XOR'd against each individual remaining byte until the process 
becomes completed.

The following is a step by step example on an arbitrarily made-up packet.

00 09 00 01 00 02 AB 43 E3 D5 00 FF 00 11 45 32 76 43 D4 F1 00 AB CD

First we know the first 2 bytes are the SOE opcode 0x09 (data on channel 00) So we ignore this as we need it to identify the packet.
We also ignore the last two because it is for the CRC value. The remainder is what needs to be encrypted (or decrypted in another case).

Say our Key is (1D 4E 32 87)
this will also act as our first mask.

So, taking the first 4 bytes after the SOE opcode (00 01 00 02)
00 01 00 02 XOR
1D 4E 32 87

1D 4F 32 85

So the beginning of the new packet is 00 09 1D 4F 32 85
Now we take the result as our new mask and xor the next 4 bytes
AB 43 E3 D5 XOR
1D 4F 32 85

B6 0C D1 50

New packet so far: 00 09 1D 4F 32 85 B6 0C D1 50
New mask: B6 0C D1 50
00 FF 00 11 XOR
B6 0C D1 50

B6 F3 D1 41

New packet so far:  00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41
New mask: B6 F3 D1 41
45 32 76 43 XOR
B6 F3 D1 41

F3 C1 A7 02

New packet so far: 00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41 F3 C1 A7 02
New mask: F3 C1 A7 02

Now that we are out of full 4 byte blocks, we xor each last byte with the first byte in our “key”

D4 F1 00 XOR   This is done in a separate loop, and per byte, so D4 xor F3, then F1 
F3 F3 F3       xor F3, then 0E xor F3. And the results are all appended to our packet

27 02 F3

Final Encrypted Packet: 00 09 1D 4F 32 85 B6 0C D1 50 B6 F3 D1 41 F3 C1 A7 02 27 02 F3 AB CD

Decryption would be the reverse of the encryption process.
Encryption is applied AFTER Compression, but BEFORE a CRC value is appended.

VERY IMPORTANT NOTE:

```text
After the discovery of stand-alone SWG Packets (Outside of SOE protocol), the encryption and decryption algorithms 

```

have a slight difference in how they adjust for the CRC/SOE opcode. Stand alone SWG Packets are encrypted between the 
first byte and the CRC value. SOE protocol'd packets are encrypted between the SOE Opcode(2nd byte) and the CRC value.
The actual code should account for this however the explaination will not. 
TODO:Update the Code - Xeno

NewPP limit report
Cached time: 20261017165635
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.011 seconds
Real time usage: 0.011 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1552-0!*!*!*!*!*!* and timestamp 20261017165635 and revision id 1670
