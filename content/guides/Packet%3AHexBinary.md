---
title: Packet:HexBinary
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet%3AHexBinary
wiki_revid: 1663
layout: guide
date_audited: 2026-10-17
---

# Packet:HexBinary

This page is a summary of basic binary and hexadecimal number systems to help
understand packet analysis. These skills are essential tools to be a successful
analyzer.

BINARY NUMBERS:

Binary numbers are a base 2 number system that consist of 0's and 1's, which usually represent voltage, or no voltage on a computer system.

0 0 0 0 0 0 0 0 0

Each number is commonly called a "bit". 8 bits is equal to a single byte, which is the most common form of data. 
All data is made up of bytes.

To calculate an integer number in decimal (base 10, what we commonly use), we add each 1 bit as a representation of the power of 2. 
The following powers are used as 2 ^ N, where N is the place holder.

_  _  _  _  _  _  _  _
7  6  5  4  3  2  1  0

so 0 0 0 0 1 1 0 1 is equal to 2^0 + 2^2 + 2^3 = 13

to more easily add it up, think of:

```text
_  _  _  _  _ _ _ _

```

128 64 32 16 8 4 2 1

and just add the numbers when the bit is 1

so..

0 1 0 1 0 1 1 1 is.. 64 + 16 + 4 + 2 + 1 = 87

HEXADECIMAL NUMBERS:

Because binary numbers can get VERY long, hexadecimal, a base 16 number system is used. Because 16 is a power of 2, 
it works out nicely. Intead of 0-9 like decimal uses, hexadecimal uses 0-F, which is just 0-9 with the 
additon of A B C D E F as digits. Most data viewed on computers is in hexadecimal. 
To convert from binary to hexadecimal and vice versa, use the following method:

Each digit represents 1/2 of a byte. so 2 hexacedimal numbers is equal to 1 byte. So devide your "bits" into two groups.
Lets use the example from above.

0 1 0 1     0 1 1 1

Now, add them up seperatly:

```text
5             7

```

and there you go, your hexadecimal representation is 0x57. 0x is a common prefix to writing the numbers to let readers 
know it is base 16.0x57 is not equal to 57, rather it is equal to 87. So where do the letters come in? 
Well lets do another example:

1 1 0 0 1 0 1 1  = 128 + 64 + 8 + 2 + 1 = 203

1 1 0 0   1 0 1 1  BINARY

```text
12        11      DECIMAL
C         B       HEX

```

so 203 is equal to 0xCB in hexadecimal.

TIP: You can use windows calculator to do these convesions quickly. Just change the mode to scientific.

For simplicity of this article, signed (positive and negative) are not covered, as well as floating point numbers. 
You can google the following examples for further research.

Signed numbers : "Two's complement"
Floats : "IEEE Floating Point"

TIP: Also, if these guides do not suffice or are confusing, use google for better explainations, 
Wikipedia has A LOT more information on all of the subjects in this document.

DATA TYPES:

C++ uses the following data types: These are the sizes in bytes they take to store, and these units are commonly 
used throughout the rest of our documentation. These apply for both signed and unsigned (positive and negative)

CHAR		1 Byte		(8 bit integer)
SHORT		2 Bytes		(16 bit integer)
INT		4 Bytes		(32 bit integer)
LONG		8 Bytes		(64 bit integer)
FLOAT		4 BYtes		(32 bit floating point)

NOTE: LONG is commonly represented as "long long" while "long" by itself is interpreted as a 32 bit (4 byte) 
int on GCC and other ANSI standard compilers. For the sake of shortness however, 
we will refer "LONG" as a 64 bit (8 byte) integers.

TIP: For information on maximum numerical storage capacity of each data type as signed or unsigned, use google,
it is readily available on the internet.

HOST BYTE vs NET BYTE ORDERS:

This is also known as Big Endian vs Little Endian, and they are just a standard for reading multiple byte integers.

HOST BYTE ORDER or BIG ENDIAN is a format that has the higher value byte to the right, and lower value byte to the left. 
to Represent the number 1 as a SHORT or INT is as follows:

0x0100		(SHORT)
0x01000000	(INT)

if this is confusing to understand, think of the 1000's, 100's, 10's, and 1's place in our decimal number system. We go:

1000's   100's    10's     1's

Higher value to the left, lower value to the right.
Now just apply this same method to hexadecimal. However, host byte has this reversed.

NET BYTE ORDER or LITTLE ENDIAN is the exact opposite. It's larger value is to the left, and lower value to the right, 
exactly like our decimal number system above. The number 1 as a SHORT or INT is as follows:

0x0001		(SHORT)
0x00000001	(INT)

Windows commonly uses HOST BYTE, Unix/Linux use NET BYTE. Most of our packets deal with HOST BYTE for INTs and SHORTs. 
However some of the protocol uses NET BYTE. It will be specified which order is used in the packet breakdown documentations.

This is just a summary of the common information that is assumed to be understood throughout the rest of our documentation. 
If you have any specific questions, as someone, or use you're best friend Google (or his friend Wikipedia).

www.Google.com

NewPP limit report
Cached time: 20261017165636
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.009 seconds
Real time usage: 0.010 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1547-0!*!*!*!*!*!* and timestamp 20261017165636 and revision id 1663
