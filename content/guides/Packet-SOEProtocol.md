---
title: Packet:SOEProtocol
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet%3ASOEProtocol
wiki_revid: 1729
layout: guide
date_audited: 2026-10-17
---

# Packet:SOEProtocol

SOE's Protocol is a systematic way to enhance the UDP protocol to make it more reliable, and also save bandwidth by merging and grouping packets. It can be combined in various ways, or not be used at all.

The format of the SOE Protocol varies depending on what type of operation it is. SOE Protocol can function as a stand alone packet, or as a Header to SWG Packets. What is true about all of the SOE Protocol is that the beginning contains 2 bytes known as the SOE Opcode. Majority also contain a footer. Assume all packets have footers unless otherwise mentioned. The table of opcodes are as follows:

Note- An SOE Opcode is stored as an unsigned short (uint16), and is in net byte order.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>SOE OpCodes</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick='copyToClipboard(`
(SOE Opcode)"in hex"	(Meaning) 		(ENUM_NAME)"used in code"

00 01		Session Request				(SOE_SESSION_REQUEST)
00 02		Session Response			(SOE_SESSION_REPLY)
00 03		Multiple SOE Protocols			(SOE_MULTI_SOE)
00 04		Not Used				(SOE_NOT_USED)
00 05		Disconnect				(SOE_DISCONNECT)
00 06		Keep Alive				(SOE_PING)
00 07 		Client Network Status Update		(SOE_NET_STATUS_REQ)
00 08 		Server Network Status Update		(SOE_NET_STATUS_RES)

00 09 		Channel 0 - Data Packet			(SOE_CHL_DATA_A)
00 0A		Channel 1 - Data Packet			(SOE_CHL_DATA_B)
00 0B		Channel 2 - Data Packet			(SOE_CHL_DATA_C)
00 0C		Channel 3 - Data Packet			(SOE_CHL_DATA_D)

00 0D		Channel 0 - Fragmented Data Packet	(SOE_DATA_FRAG_A)
00 0E		Channel 1 - Fragmented Data Packet	(SOE_DATA_FRAG_B)
00 0F		Channel 2 - Fragmented Data Packet	(SOE_DATA_FRAG_C)
00 10		Channel 3 - Fragmented Data Packet	(SOE_DATA_FRAG_D)

00 11		Channel 0 - Out of Order Packet		(SOE_OUT_ORDER_PKT_A)
00 12		Channel 1 - Out of Order Packet		(SOE_OUT_ORDER_PKT_B)
00 13		Channel 2 - Out of Order Packet		(SOE_OUT_ORDER_PKT_C)
00 14		Channel 3 - Out of Order Packet		(SOE_OUT_ORDER_PKT_D)

00 15		Channel 0 - Acknowledge Packet		(SOE_ACK_A)
00 16		Channel 1 - Acknowledge Packet		(SOE_ACK_B)
00 17		Channel 2 - Acknowledge Packet		(SOE_ACK_C)
00 18		Channel 3 - Acknowledge Packet		(SOE_ACK_D)

00 19		Channel 0 - Multi SWG Packets		(SOE_MULTI_SWG_A)
00 1A		Channel 1 - Multi SWG Packets		(SOE_MULTI_SWG_B)
00 1B		Channel 2 - Multi SWG Packets		(SOE_MULTI_SWG_C)
00 1C		Channel 3 - Multi SWG Packets		(SOE_MULTI_SWG_D)

00 1D		*Serious Error Acknowledge		(SOE_FATAL_ERR)
00 1E		*Serious Error Reply			(SOE_FATAL_ERR_REP)
`, this)'>Copy</button></div><pre class="code-block"><code>
(SOE Opcode)"in hex"	(Meaning) 		(ENUM_NAME)"used in code"

00 01		Session Request				(SOE_SESSION_REQUEST)
00 02		Session Response			(SOE_SESSION_REPLY)
00 03		Multiple SOE Protocols			(SOE_MULTI_SOE)
00 04		Not Used				(SOE_NOT_USED)
00 05		Disconnect				(SOE_DISCONNECT)
00 06		Keep Alive				(SOE_PING)
00 07 		Client Network Status Update		(SOE_NET_STATUS_REQ)
00 08 		Server Network Status Update		(SOE_NET_STATUS_RES)

00 09 		Channel 0 - Data Packet			(SOE_CHL_DATA_A)
00 0A		Channel 1 - Data Packet			(SOE_CHL_DATA_B)
00 0B		Channel 2 - Data Packet			(SOE_CHL_DATA_C)
00 0C		Channel 3 - Data Packet			(SOE_CHL_DATA_D)

00 0D		Channel 0 - Fragmented Data Packet	(SOE_DATA_FRAG_A)
00 0E		Channel 1 - Fragmented Data Packet	(SOE_DATA_FRAG_B)
00 0F		Channel 2 - Fragmented Data Packet	(SOE_DATA_FRAG_C)
00 10		Channel 3 - Fragmented Data Packet	(SOE_DATA_FRAG_D)

00 11		Channel 0 - Out of Order Packet		(SOE_OUT_ORDER_PKT_A)
00 12		Channel 1 - Out of Order Packet		(SOE_OUT_ORDER_PKT_B)
00 13		Channel 2 - Out of Order Packet		(SOE_OUT_ORDER_PKT_C)
00 14		Channel 3 - Out of Order Packet		(SOE_OUT_ORDER_PKT_D)

00 15		Channel 0 - Acknowledge Packet		(SOE_ACK_A)
00 16		Channel 1 - Acknowledge Packet		(SOE_ACK_B)
00 17		Channel 2 - Acknowledge Packet		(SOE_ACK_C)
00 18		Channel 3 - Acknowledge Packet		(SOE_ACK_D)

00 19		Channel 0 - Multi SWG Packets		(SOE_MULTI_SWG_A)
00 1A		Channel 1 - Multi SWG Packets		(SOE_MULTI_SWG_B)
00 1B		Channel 2 - Multi SWG Packets		(SOE_MULTI_SWG_C)
00 1C		Channel 3 - Multi SWG Packets		(SOE_MULTI_SWG_D)

00 1D		*Serious Error Acknowledge		(SOE_FATAL_ERR)
00 1E		*Serious Error Reply			(SOE_FATAL_ERR_REP)
</code></pre></div>
</td></tr></table></div>

- Note: These functions are seen on very malformed packets. Very rare occurance and the client will usually disconnect. It's inclusion in the documentation is for completion ONLY. SWGEmu will disconnect automatically when reciving a Error Acknowledge, and it will NOT send any, rather just disconnect itself.

SOE has their protocol premade to allow various channels of data transmission. However, no game to this date utilizes the multiple channels. SWG will only be using channel 0 and it will be assumed throughout the rest of the packet documentation.

The following data is of packet breakdowns and explainations on each type. See the article "Packet Breakdown Format" for information on the specific used for documentation.

## Packet Type --00 01

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 01</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
00 01  -  Session Request (Client -&gt; Server)
SOE Opcode	- Net Byte SHORT	
CRC Length	- Net BYte INT
Connection ID	- Net Byte INT
ClientUDPSize	- Net Byte INT	
`, this)">Copy</button></div><pre class="code-block"><code>
00 01  -  Session Request (Client -&gt; Server)
SOE Opcode	- Net Byte SHORT	
CRC Length	- Net BYte INT
Connection ID	- Net Byte INT
ClientUDPSize	- Net Byte INT	
</code></pre></div>
</td></tr></table></div>

The SOE Opcode is just the opcode number to identify the packet.

CRC Length is the amount of length of the CRC checksum to append at the end of a packet. SWG uses 2 bytes. 
Note CRC32 checksums are 32bit, making them 4 bytes, but only 2 are appended.

Connection ID is some type of identification used for the connection. Only other time seen is during a disconnect.

ClientUDPSize is the maximum size allocated for the client's UDP packet buffer. No packet is allowed to exceed this size. 
If it is larger, it must be fragmented. This size is equal to 496 bytes.

Note* This opcode DOES NOT have a footer.

## Packet Type --00 02

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 02  -  Session Response(Server -&gt; Client)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Connection ID	- Net Byte SHORT
CRCSeed		- Net Byte INT
CRCLength	- BYTE
UNKNOWN		- SHORT
ServerUDPSize	- Net Byte INT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Connection ID	- Net Byte SHORT
CRCSeed		- Net Byte INT
CRCLength	- BYTE
UNKNOWN		- SHORT
ServerUDPSize	- Net Byte INT
</code></pre></div>
</td></tr></table></div>

Connection ID is replied using the same ID sent by the Session Request.
CRCSeed is a seed value used for the calculation of the CRC32 Checksum.
CRCLength
UNKNOWN is an unknown value that is constant and equal to 0x0104 (260).
ServerUDPSize is the maximum size allocated for the server's UDP packet buffer. No packet is allowed to exceed this size.

```text
So far the client has not sent anything large enough to fill this, or be fragmented. This size is equal to 496 bytes.

```

Note* This opcode DOES NOT have a footer.

## Packet Type --00 03

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 03  -  Multiple SOE Protocols(Various)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Data Size	- (VARIOUS)
DATA		- (VARIOUS)
Data Size	- (VARIOUS)
DATA		- (VARIOUS)
...
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Data Size	- (VARIOUS)
DATA		- (VARIOUS)
Data Size	- (VARIOUS)
DATA		- (VARIOUS)
...
</code></pre></div>
</td></tr></table></div>

These packets allow the combination of 2 or more SOE Protocol packets or stand alone SWG Packets with SOE Protocol packets.

(SOE Protocol)((SOE Protocol)(SWG Packet)) or
(SOE Protocol)(SWG Packet)

or as a better example:

(Multiple SOE Proto)(Ackowledge)(Data) or
(Multiple SOE Proto)(Acknowledge)(SWG Packet) or
(Multiple SOE Proto)(Acknowledge)(Acknowledge)

Each seperate packet is preceded by it's size. So a better example would be:
(Multiple SOE Proto)(size1)(Acknowlede)(size2)(Data)

so a very basic hexadecimal version would be:
(00 03)  (04)  (00 15 00 00)  (0A)  (00 09 00 01 01 00 FF FF FF FF)

```text
multi   size   acknowledge   size              data

```

In the case where the size exceeds 0xFF (255) bytes, the following sytem is used for the "Data Size" component.

The first byte will be 0xFF. The next byte will be 0x01. The following byte will be how much to add to 255. Because no packet can exceed 496 bytes, The 3rd bye will never exceed 0xFF. We believe the 0x01 is the amount of following bytes to add to 255, but that cannot be determined.

```text

(0XFF 0X01 0X01) = 255 + 1 = 256 bytes
(0xFF 0X01 0X0A) = 255 + 10 = 265 bytes
(0xFF 0x01 0x25) = 255 + 37 = 292 bytes

```

- NOTE:Because 255 may be done in a few ways, the following way is how we have seen it. (0xFF 0x00 0xFF) or 255 + 0 (do not add the following byte) = 255.

## Packet Type --00 04

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 05  -  Disconnect(VARIOUS)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Connection ID	- Net Byte INT
Reason ID	- Net Byte SHORT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Connection ID	- Net Byte INT
Reason ID	- Net Byte SHORT
</code></pre></div>
</td></tr></table></div>

Connection ID is the ID number assigned during the session request. Each client sends its own Connection ID.
Reason ID is an ID number that corresponds for a reason for the disconnection.

This packet is sent whenever one side wants to disconnect. It resends the clients specific Connection ID 
established during the session handshake, and then a reason for disconnection. 
So far the standard reason ID seen has been 6. Others have been tested and do not have any different effect. 
No table correspnding IDs to reasons has been located.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 06   -  Keep Alive(VARIOUS)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
</code></pre></div>
</td></tr></table></div>

This packet is simply a keep alive to tell the other side that is still connected, but idle.
It only consists of the opcode and a footer.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 07  -  Client Network Status Update</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Data..
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Data..
</code></pre></div>
</td></tr></table></div>

These packets consist of various data and network statistics. Because we do not care about network statistics,
we will ignore these. To ignore these we send a special malformed Server Network Status Update.

Note: This packet is usually compressed but is optional.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 08  -  Server Network Status Update</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Data..
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Data..
</code></pre></div>
</td></tr></table></div>

This packet is supposed to contain the Servers network statistics, however we felt it was a waste of time to reverse
these as we do not care about the statistics. Instead we send 38 bytes of 0x00, and then compress the packet, but skip appending a CRC.
The client seems to register that it recieved the servers statistics, but notices a bad CRC (or none in our case), 
and tosses out the packet as malformed. Because it recieved the packet it continues on without erroring.

Note: This packet is usually compressed but is optional.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 09  -  Channel 0 Data</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
SWG PACKET..
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
SWG PACKET..
</code></pre></div>
</td></tr></table></div>

Sequence # is a sequence number applied to every data packet. It increments in order for each packet and is used to help determine
out of order packets. This protocol is used to send an SWG Packet that NEEDS to be recieved by the other end. 
The reciver is then supposed to respond with a an ACKNOWLEDGE packet that contains the same sequence so the sender knows it
has been recieved. This system ensures packets not only get sent correctly, but also stay in order.

After the sequence # comes the encapsulated SWG Packet.

Note* it is possible to combine multiple SWG PACKETs into a single 09. 
This is done similar to the 03 system with the sizes (1 byte, or the 0xFF 0x01 0xXX which is 255 + XX) 
but there are 2 bytes after the sequence that flag a multiple SWG packet. It looks something like this:

(00 09) (sequence) (00 19) (Size1) (SWG PACKET) (Size2) (SWG PACKET)
SOE op.  sequence   multi   size       data       size      data

Use these to combine SWG PACKETs together into 1 data packet/sequence number.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 0D  -  Fragmented Data Packet</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
*FragmentSize	- Net Byte INT
SWG Packet...
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
*FragmentSize	- Net Byte INT
SWG Packet...
</code></pre></div>
</td></tr></table></div>

Sequence # is the same type of sequence number described in the "00 09  -  Channel 0 Data" section. All the same rules apply.

- FragmentSize is the total size of the combined fragments. This only appears in the FIRST packet of a group of fragmented packets.

Next is just the piece data of the large SWG Packet. Fragments are made when the total UNCOMPRESSED packet 
exceeds the packet buffer size, which is 496 bytes.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 11  -  Out of Order Packet</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
</code></pre></div>
</td></tr></table></div>

Sequence # is the sequence number of the out of order packet recieved. 
It will send one for every packet that is out of order, and the ones following.

So if packet sequences recieved are:
00 00
00 01

And then:
00 03

an out of order will be sent for the packet with sequence 00 03.

If the packet sequences recieved are:
00 00
00 01

And then:
00 03
00 04
00 05

An out of order packet will be sent for all 3 of the out of order sequences.

<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 15  -  Acknowledge</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Net Byte SHORT
Sequence #	- Net Byte SHORT
</code></pre></div>
</td></tr></table></div>

Sequence # is the sequence number of the packet to acknowledge to the sender that it was recieved correctly.
Every packet sent with a sequence number MUST be acknowledeged.

They do not neccesarily need to be Acknowledeged 1 by 1. For example:
If packet sequences recieved are:
00 00
00 01
00 02

An Acknowledge of 00 15 00 02 will cover all the packets up to the sequence 00 02.

The client will stop processing packets after about 4 unacknowledeged packets so frequent acknowledges are needed.

Thanks to Acid1789 for the abundant information on the SOE Protocol!

NewPP limit report
Cached time: 20261017065936
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.046 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 168/1000000
Preprocessor generated node count: 652/1000000
Post‐expand include size: 3018/2097152 bytes
Template argument size: 810/2097152 bytes
Highest expansion depth: 3/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%   13.213      1 - -total
 73.23%    9.676     12 - Template:InfoboxPacketDetail

Saved in parser cache with key swganh_wiki:pcache:idhash:1553-0!*!*!!en!*!* and timestamp 20261017065936 and revision id 1729
