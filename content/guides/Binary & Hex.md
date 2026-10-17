---
title: Binary & Hex
section: guides
wiki_url: https://wiki.swganh.org/index.php/Binary_%26_Hex
wiki_revid: 44447
layout: guide
date_audited: 2026-10-17
---

# Binary & Hex

This guide will help you to understand both packet and file analysis. This understanding is an essential tool to be a successful analyzer.

# The Binary Language

A computer is made up of millions of transistors. Each one of them can either be on or off depending if the electricity flows through or not. These status are represented by 2 numbers: 0 (off) and 1 (on). This is called the binary language and it's the only thing your computer understands. This language is said to be base 2 because it has only 2 possible digits: 0 and 1. Here a little example:

```text

0 0 1 0 0 1 1 0 1 1 0 1 1 1 0 0 1 1 0...

```

In binary language a digit is called a bit . Binary language being a bit too hard to read for humans, we decided to group them in packets of 8 bits and to call this packet a byte . The 8 bits of a byte a used and read the same way we do in decimal system. Here are the different values a byte can have:

```text

1 byte = 8 bits  -> corresponding decimal value
0 0 0 0 0 0 0 0               0
0 0 0 0 0 0 0 1               1
0 0 0 0 0 0 1 0               2
0 0 0 0 0 0 1 1               3
0 0 0 0 0 1 0 0               4
...
1 1 1 1 1 1 1 1             255

```

To calculate an integer number in decimal (the base 10 we commonly use), we add 1 bit to each as a representation of the power of 2. The following powers are used as 2^N, where N is the place holder.

```text

_  _  _  _  _  _  _  _
7  6  5  4  3  2  1  0

```

Example: 0 0 0 0 1 1 0 1 = 2^3 + 2^2 + 2^0 = 13

To more easily add it up, you can precalculate each 2^N value:

```text

 _  _  _  _  _ _ _ _
128 64 32 16 8 4 2 1 

```

And just add the numbers when the bit is 1, so..

Example: 0 1 0 1 0 1 1 1 = 64 + 16 + 4 + 2 + 1 = 87

# The Hexadecimal Language

The hexadecimal language is a base 16 system. It means each digit has 16 possible value: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F (0 to 15 in decimal). Because 2^4=16 it makes binary reading far more easier. An hexadecimal digit consist of 4 consecutive bits. It means you can write any byte value using 2 hexadecimal digits as follows:

```text

 original bits  -> 4 bits groups -> hexadecimal
0 1 0 1 0 1 1 1      0101 0111         0x57

```

As you see we added a "0x" prefix to our hexadecimal number. This is the standard used to let readers know that the following digits are hexadecimal digits. 57 is decimal, 0x57 is hexadecimal (87 in decimal).

Another example:

```text

1 1 0 0 1 0 1 1  = 128 + 64 + 8 + 2 + 1 = 203

1100 1011 binary
 12   11  decimal
  C    B  hexadecimal

```

So 203 = 0xCB in hexadecimal.

TIP : You can use windows calculator to do these convesions quickly. Just change its mode to scientific.

For simplicity of this article, signed (positive and negative) are not covered, as well as floating point numbers. More info here:

- Signed numbers : Two's complement
- Floats : IEEE Floating Point

# The data types

The programmation languages provides various pre defined data types. This array shows what type can be expected from input data:

<div class="table-wrap"><table class="wikitable doc-table">
<tr>
<th>bytes amount
</th>
<th>type
</th>
<th>sign
</th>
<th>values
</th>
<th>C++ corresponding types
</th>
<th>C# corresponding types
</th>
<th>SWGANH Alias
</th></tr>
<tr>
<td>1
</td>
<td>integer
</td>
<td>
</td>
<td>0=false, else=true
</td>
<td>bool
</td>
<td>bool
</td>
<td align="center" style="background:#4169E1; color:white;" width="80px"><b>BOOL</b>
</td></tr>
<tr>
<td>1
</td>
<td>integer
</td>
<td>signed
</td>
<td> -128 to +127 (ascii characters)
</td>
<td>char
</td>
<td>sbyte (NB:Not CLS Compliant)
</td>
<td align="center" style="background:#B3C0DE; color:white;" width="80px"><b>SBYTE</b>
</td></tr>
<tr>
<td>1
</td>
<td>integer
</td>
<td>unsigned
</td>
<td>0 to +255 (ansi characters)
</td>
<td>unsigned char
</td>
<td>byte
</td>
<td align="center" style="background:#B3C0DE; color:white;" width="80px"><b>BYTE</b>
</td></tr>
<tr>
<td>2
</td>
<td>integer
</td>
<td>signed
</td>
<td> -32768 to +32767
</td>
<td>short
</td>
<td>short
</td>
<td align="center" style="background:#6C86BF; color:white;" width="80px"><b>SHORT</b>
<p><br/>
</p>
</td></tr>
<tr>
<td>2
</td>
<td>integer
</td>
<td>unsigned
</td>
<td>0 to +65535
</td>
<td>unsigned short
</td>
<td>ushort
</td>
<td align="center" style="background:#6C86BF; color:white;" width="80px"><b>USHORT</b>
</td></tr>
<tr>
<td>2
</td>
<td>char
</td>
<td>
</td>
<td>unicode character
</td>
<td>wchar_t
</td>
<td>char
</td>
<td>
</td></tr>
<tr>
<td>4
</td>
<td>integer
</td>
<td>signed
</td>
<td> -2147483648 to +2147483647
</td>
<td>int, long
</td>
<td>int
</td>
<td align="center" style="background:#3C548A; color:white;" width="80px"><b>INT</b>
<p><br/>
</p>
</td></tr>
<tr>
<td>4
</td>
<td>integer
</td>
<td>unsigned
</td>
<td>0 to +4294967295
</td>
<td>unsigned int, unsigned long, void*
</td>
<td>uint
</td>
<td align="center" style="background:#3C548A; color:white;" width="80px"><b>UINT</b>
</td></tr>
<tr>
<td>4
</td>
<td>real
</td>
<td>signed
</td>
<td> -3.4*10^-38 to +3.4*10^38 (7 digits)
</td>
<td>float
</td>
<td>float
</td>
<td align="center" style="background:#3C5466; color:white;" width="80px"><b>FLOAT</b>
</td></tr>
<tr>
<td>8
</td>
<td>integer
</td>
<td>signed
</td>
<td> -9223372036854775808 to +9223372036854775807
</td>
<td>long long
</td>
<td>long
</td>
<td align="center" style="background:#3C4565; color:white;" width="80px"><b>LONG</b>
<p><br/>
</p>
</td></tr>
<tr>
<td>8
</td>
<td>integer
</td>
<td>unsigned
</td>
<td>0 to +18446744073709551615
</td>
<td>unsigned long long
</td>
<td>ulong
</td>
<td align="center" style="background:#3C4565; color:white;" width="80px"><b>ULONG</b>
</td></tr>
<tr>
<td>8
</td>
<td>real
</td>
<td>signed
</td>
<td> -1.7*10^-308 to +1.7*10^308 (15 digits)
</td>
<td>double
</td>
<td>double
</td>
<td align="center" style="background:#465945; color:white;" width="80px"><b>DOUBLE</b>
</td></tr>
<tr>
<td>n
</td>
<td>char
</td>
<td>
</td>
<td>ansi/ascii characters
</td>
<td>string, char[]
</td>
<td>
</td>
<td align="center" style="background:#D8F2E0; color:#3C4565;" width="80px"><b>A_STRING</b>
</td></tr>
<tr>
<td>2n
</td>
<td>char
</td>
<td>
</td>
<td>unicode characters
</td>
<td>wstring, wchar_t[]
</td>
<td>string
</td>
<td align="center" style="background:#8BD9A3; color:white;" width="80px"><b>U_STRING</b>
</td></tr>
</table></div>

NOTE : In C++, the long types have a size that varies upon operating system and processor. It has the size of all pointers (void*, int*, ...). If an environment has a 32bits RAM indexation (4GB max) then the longs will be 4 bytes. If the environment has a 64 bits RAM indexation, the longs will be 8 bytes.

# Big Endian vs Little Endian (byte orders)

The little story: The term "endian" can be traced to Jonathan Swift's novel "Gulliver's Travels." In one of Gulliver's adventures, he encounters an island whose inhabitants bitterly argue over the correct way to open soft-boiled eggs - the little end or the big end. Little endians and big endians are each convinced that their method is the only correct method for opening an egg.

## Big Endian

The BIG ENDIAN byte order is the natural read order: highest weigth digits on the left, and lowest weigth digits on the right.

Example: let's write 16909060 in hexadecimal (0x?? = 1byte = 8bits):

```text

0x01 0x02 0x03 0x04 (bytes sequence in memory)
0x01020304          (reconstitued associated hexadecimal value)
16909060            (corresponding decimal value)

```

Note: also known as NETWORK BYTE ORDER, it's the standard used for IP communications as defined by the OSI model link layer. Though it does not mean all protocols respect the standard! It's used by: Sun Solaris (SPARC), HP-UX, (Motorola 68000), IBM System/370, ...

## Little Endian

The LITTLE ENDIAN byte order is BIG ENDIAN opposite: lowest weigth digits on the left, and highest weigth digits on the right.

Example: let's write again 16909060 in hexadecimal (0x?? = 1byte = 8bits):

```text

0x04 0x03 0x02 0x01 (bytes sequence in memory)
0x01020304          (reconstitued associated hexadecimal value)
16909060            (corresponding decimal value)

```

Why does LITTLE ENDIAN exists?

Let's see an example, we have an INT value of 8. Let's store it in LITTLE ENDIAN and look at each byte memory address:

```text

   0    1    2    3 (memory address)
0x08 0x00 0x00 0x00 (bytes sequence in memory)
0x00000008          (reconstitued associated hexadecimal value)
8                   (corresponding decimal value)

```

Imagine now we want to convert this int variable into a short or a byte. Because it's stored reversly we don't need to change the starting address of our variable (it means conversions are faster in LITTLE ENDIAN):

```text

   0    1    2    3 (memory address)
0x08 0x00 0x00 0x00 (int)
0x08 0x00           (short)
0x08                (byte)

```

The little endian was used in the first place as you can guess for compatibility reasons when we went from 8bits, to 16bits, to 32bits, to 64bits systems...

Note: also known as HOST BYTE ORDER. It's used by: SCO Unix, DEC Unix (Digital), Microsoft Windows, ...

## SWG and bytes orders

- Most (if not all) files of SWG use the LITTLE ENDIAN format to store values.
- Network transmissions also use the LITTLE ENDIAN for most of it.

It will be specified which order is used in the packet breakdown documentations.

This is just a summary of the common information that is assumed to be understood throughout the rest of our documentation. 
If you have any specific questions, ask someone, or use you're best friend Google (or his friend Wikipedia).

NewPP limit report
Cached time: 20261017055137
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.090 seconds
Real time usage: 0.266 seconds
Preprocessor visited node count: 180/1000000
Preprocessor generated node count: 420/1000000
Post‐expand include size: 1332/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%   77.347      1 - -total
 18.02%   13.934      1 - Template:Bool
 15.59%   12.058      1 - Template:Ushort
 14.60%   11.292      2 - Template:En
 10.69%    8.271      1 - Template:Ulong
  8.97%    6.941      1 - Template:Long
  5.79%    4.481      1 - Template:U_string
  4.48%    3.462      1 - Template:Uint
  2.33%    1.800      1 - Template:Double
  2.31%    1.783      1 - Template:Int

Saved in parser cache with key swganh_wiki:pcache:idhash:1821-0!*!*!!*!5!* and timestamp 20261017055137 and revision id 44447
