---
title: "SWG Packets"
section: guides
category: "SOE / SWG Packet Related Tutorials"
slug: swg-packets
wiki_url: https://wiki.swganh.org/index.php/SWG_Packets
wiki_revid: 2523
layout: guide
date_audited: 2026-10-17
---

# SWG Packets

SWG Packets are the actual packets of data that are within the SOE Protocol. They follow a general trend, and then have 
their own specific breakdowns as to what data is where.

All SWG Packets consist of an opperand count, and an opcode. An opcode is a number to help identify what type of data the packet contains, and the opperand count is to know how many variables are within the packet. The format is as follows:

```text

[Opperand Count:Host Byte SHORT]
[Opcode:INT]
[DATA...]

```

Opcodes appear as very large integer, and there is no pattern between them, so we recognize them as just an INT data type that is 4 bytes in size.

## MULTIPLE SWG PACKETS

There is a special case within an SWG Packet which allows multiple SWG Packets to be combined into one. This can be identified 
when there is an opperand count of 0x0019 (in a packet, you would see 00 19 versues 02 00 or some other host byte number that is a count).

The format then follows the same as the Multiple SOE Protocols Opcode.

```text

[special opperand count of 00 19]

[Size1:Byte]
[Data1..]

[Size2:Byte]
[Data2..]

[Repeat..]

```

Again, if the packet must exceed 255, the same format is used as the SOE Multiple Protocols opcode. The first byte is FF for 255, the next byte is how many bytes to add to that value (so 01) and the byte after that is the actual number to add.

```text

so 256 would appear as FF 01 01 or FF + 01 or 255 + 1.
265 would appear as FF 01 0A or FF + 0A or 255 + 10.

```

Because no packet can exceed 496 bytes (because that is the set buffer), at most 1 byte will be added to 255, so FF 01 __ is the general format for every byte 255 and above.

NOTE: As stated in the SOE Protocol documentation, we have not seen a case for a size of 255. 
There are a few ways that this MAY be done, but we believe FF 01 00 is the correct method, where FF + 00 or 255 + 0 is computed.

## COMMON SWG DATA TYPES

The following data types are what commonly appear in SWG packets, and each count as 1 operand. 
Note: (HB) is short for (Host Byte) (NB) is short for (Net Byte). This is assumed throughout the rest of the packet documentation.

```text

BYTE			(a 1 byte integer number)
(HB)SHORT		(a 2 byte integer number)
(HB)INT			(a 4 byte integer number)
(HB)LONG	       (an 8 byte integer number)
(NB)FLOAT		(a 4 byte floating point number)
A_STRING		(an ASCII string)
U_STRING		(a UNICODE string)

```

Note : There are a few other ways an "operand" can be counted. Lists that have a counter preceding them is also a common "operand". So seeing something like this:

```text

04 00 00 00 (HB)INT - a counter for some list
DATA1..
DATA2..
DATA3..
DATA4..

```

that would all count as a single operand.

Operand counting really helps when reversing a packet as you know how many data pieces to break it into. There is no real use to them beyond that. Also operands will be marked in the packet breakdowns if needed. They are more a reversing tool for the packet analyzer than necessary in the server.

## ASCII STRINGS

A_STRING data types have the following format. Instead of being null terminated, the string size 
preceeds the data as a (HB)SHORT. So the string "ABC" in binary would be:

```text

"ABC"
03 00 65 66 67

```

where 03 00 is the integer number 3, and each byte is a character of the string.

## UNICODE STRINGS

U_STRING follow the same format as A_STRING, however, there are 2 bytes to each character, instead of 1 like in Ascii. Each unicode character is represented as a (HB)SHORT so "ABC" as a U_STRING would be:

```text

"ABC"
03 00 65 00 66 00 67 00

```

where 03 00 is the size, and each following (HB)SHORT is a character of the string.

NewPP limit report
Cached time: 20261017155643
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.014 seconds
Real time usage: 0.016 seconds
Preprocessor visited node count: 73/1000000
Preprocessor generated node count: 162/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1827-0!*!*!!*!*!* and timestamp 20261017155643 and revision id 2523
