---
title: "SOE Protocol Breakdown"
section: guides
category: "SOE / SWG Packet Related Tutorials"
slug: soe-protocol-breakdown
wiki_url: https://wiki.swganh.org/index.php/SOE_Protocol_Breakdown
wiki_revid: 257057
layout: guide
date_audited: 2026-10-17
---

# SOE Protocol Breakdown

<div style="border:0; margin: 0.2em 0px 0px;">

<p>SOE's Protocol is a systematic way to enhance the UDP protocol to make it more reliable, and also save bandwidth by merging and grouping packets. It can be combined in various ways, or not be used at all.
</p><p>The format of the SOE Protocol varies depending on what type of operation it is. SOE Protocol can function as a stand alone packet, or as a Header to SWG Packets. What is true about all of the SOE Protocol is that the beginning contains 2 bytes known as the SOE Opcode. Majority also contain a footer. Assume all packets have footers unless otherwise mentioned. The table of opcodes are as follows:
</p><p><b>Note</b> <font color="orange"><i>An SOE Opcode is stored as an unsigned short (uint16), and is in net byte order.</i></font>
</p><p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>SOE OpCodes</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick='copyToClipboard(`
(SOE Opcode)"in hex"	(Meaning) 		(       (ENUM_NAME) "used in code"

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
(SOE Opcode)"in hex"	(Meaning) 		(       (ENUM_NAME) "used in code"

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
<p><b>Note</b> <font color="orange"><i>These functions are seen on very malformed packets. Very rare occurance and the client will usually disconnect. It's inclusion in the documentation is for completion ONLY. SWGEmu will disconnect automatically when reciving a Error Acknowledge, and it will NOT send any, rather just disconnect itself.</i></font>
</p><p><br/>
SOE has their protocol premade to allow various channels of data transmission. However, no game to this date utilizes the multiple channels. SWG will only be using channel 0 and it will be assumed throughout the rest of the packet documentation.
</p><p><br/>
The following data is of packet breakdowns and explainations on each type. See the article "Packet Breakdown Format" for information on the specific used for documentation.
</p>
<h2 id="packet-type---00-01"><span class="mw-headline" id="Packet_Type_--_00_01">Packet Type -- <b>00 01</b></span></h2>
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
<ul><li> <b>SOE Opcode</b> is just the opcode number to identify the packet.</li>
<li> <b>CRC Length</b> is the amount of length of the CRC checksum to append at the end of a packet. SWG uses 2 bytes. </li>
<li> <b>Note</b> <font color="orange"><i>CRC32 checksums are 32bit, making them 4 bytes, but only 2 are appended.</i></font></li>
<li> <b>Connection ID</b> is some type of identification used for the connection. Only other time seen is during a disconnect.</li>
<li> <b>ClientUDPSize</b> is the maximum size allocated for the client's UDP packet buffer. No packet is allowed to exceed this size. If it is larger, it must be fragmented. This size is equal to 496 bytes.</li></ul>
<p><b>Note</b> <font color="orange"><i>This opcode DOES NOT have a footer.</i></font>
</p>
<h3 id="packet-samples---00-01"><span class="mw-headline" id="Packet_Samples_--_00_01">Packet Samples -- <b>00 01</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX Session Request 0x0001</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0001`, this)">Copy</button></div><pre class="code-block"><code>0x0001</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 00 02 27 38 24 61 00 00 01 F0`, this)">Copy</button></div><pre class="code-block"><code>00 00 00 02 27 38 24 61 00 00 01 F0</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`....'8\$a....`, this)">Copy</button></div><pre class="code-block"><code>....'8$a....</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN Session Request 0x0001</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0001`, this)">Copy</button></div><pre class="code-block"><code>0x0001</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 00 02 3C D6 0F BF 00 00 01 F0`, this)">Copy</button></div><pre class="code-block"><code>00 00 00 02 3C D6 0F BF 00 00 01 F0</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`....&lt;.......`, this)">Copy</button></div><pre class="code-block"><code>....&lt;.......</code></pre></div>
</td></tr>
</table></div>
<h2 id="packet-type---00-02"><span class="mw-headline" id="Packet_Type_--_00_02">Packet Type -- <b>00 02</b></span></h2>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 02  -  Session Response (Server -&gt; Client)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	 - Net Byte SHORT
Connection ID	 - Net Byte INT
CRCSeed		 - Net Byte INT
CRCLength	 - BYTE
UseCompression   - BYTE
SeedSize         - BYTE
ServerUDPSize	 - Net Byte INT
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	 - Net Byte SHORT
Connection ID	 - Net Byte INT
CRCSeed		 - Net Byte INT
CRCLength	 - BYTE
UseCompression   - BYTE
SeedSize         - BYTE
ServerUDPSize	 - Net Byte INT
</code></pre></div>
</td></tr></table></div>
<ul><li> <b>Connection ID</b> is replied using the same ID sent by the Session Request.</li>
<li> <b>CRCSeed</b> is a seed value used for the calculation of the CRC32 Checksum.</li>
<li> <b>CRCLength</b></li>
<li> <b>UseCompression</b> 0/1 Compression on/off</li>
<li> <b>SeedSize</b> Size in bytes for the XOR encryption key. Strange that this appears after the CRCSeed. Seed seems to have a max value of 5bytes. Standard is 4</li>
<li> <b>ServerUDPSize</b> is the maximum size allocated for the server's UDP packet buffer. No packet is allowed to exceed this size. So far the client has not sent anything large enough to fill this, or be fragmented. This size is equal to 496 bytes.</li></ul>
<p><b>Note</b> <font color="orange"><i>This opcode DOES NOT have a footer.</i></font>
</p>
<h3 id="packet-sample---00-02"><span class="mw-headline" id="Packet_Sample_--_00_02">Packet Sample -- <i>00 02</i></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX SessionResponse 0x0002</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0002`, this)">Copy</button></div><pre class="code-block"><code>0x0002</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`27 38 24 61 37 E4 BF 63 02 01 04 00 00 01 F0`, this)">Copy</button></div><pre class="code-block"><code>27 38 24 61 37 E4 BF 63 02 01 04 00 00 01 F0</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`'8\$a7..c.......`, this)">Copy</button></div><pre class="code-block"><code>'8$a7..c.......</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN SessionResponse 0x0002</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0002`, this)">Copy</button></div><pre class="code-block"><code>0x0002</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`3C D6 0F BF 3B BF 9B D5 02 01 04 00 00 01 F0`, this)">Copy</button></div><pre class="code-block"><code>3C D6 0F BF 3B BF 9B D5 02 01 04 00 00 01 F0</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`&lt;...;..........`, this)">Copy</button></div><pre class="code-block"><code>&lt;...;..........</code></pre></div>
</td></tr>
</table></div>
<h2 id="packet-type---00-03"><span class="mw-headline" id="Packet_Type_--_00_03">Packet Type -- <b>00 03</b></span></h2>
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
<p>These packets allow the combination of 2 or more SOE Protocol packets or stand alone SWG Packets with SOE Protocol packets.
</p><p>(SOE Protocol)((SOE Protocol)(SWG Packet)) or
(SOE Protocol)(SWG Packet)
</p><p>or as a better example:
</p><p>(Multiple SOE Proto)(Ackowledge)(Data) or
(Multiple SOE Proto)(Acknowledge)(SWG Packet) or
(Multiple SOE Proto)(Acknowledge)(Acknowledge)
</p><p>Each seperate packet is preceded by it's size. So a better example would be:
(Multiple SOE Proto)(size1)(Acknowlede)(size2)(Data)
</p><p>so a very basic hexadecimal version would be:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
(00 03)  (04)  (00 15 00 00)  (0A)  (00 09 00 01 01 00 FF FF FF FF)
 multi   size   acknowledge   size              data
`, this)">Copy</button></div><pre class="code-block"><code>
(00 03)  (04)  (00 15 00 00)  (0A)  (00 09 00 01 01 00 FF FF FF FF)
 multi   size   acknowledge   size              data
</code></pre></div>
<ul><li> <b>NOTE</b>: <i>The Size field will never exceed 255.</i></li></ul>
<h3 id="packet-sample---00-03"><span class="mw-headline" id="Packet_Sample_--_00_03">Packet Sample -- <b>00 03</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX MultiPacket 0x0003</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0003`, this)">Copy</button></div><pre class="code-block"><code>0x0003</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`06 01 00 AF F9 6C A1 1C 0A 00 08 F8 24 1B A8 1C 
95 AF 22 00 00 00 A2 54 40 01 2D 55 45 02 00 00 
00 D1 00 00 1C 0A 00 08 F8 24 1B A2 04 95 AF 22 
00 00 00 70 54 40 01 47 55 55 02 00 00 09 EB 00 
00 1C 0A 00 08 F8 24 1B AC 04 95 AF 22 00 00 00 
4E 54 40 01 5A 55 2D 01 00 00 0A EF 00 00 1C 0A 
00 08 F8 24 1B 70 04 95 AF 22 00 00 00 48 54 40 
01 16 55 17 02 00 00 0A 15 00 00 1C 0A 00 08 F8 
24 1B DB FA 94 AF 22 00 00 00 72 54 40 01 5E 55 
06 02 00 00 0A 30 00 00 1C 0A 00 08 F8 24 1B CA 
FD 94 AF 22 00 00 00 13 54 40 01 86 56 C3 06 00 
00 00 FC 00 00 1C 0A 00 08 F8 24 1B C0 FD 94 AF 
22 00 00 00 11 54 40 01 87 56 96 06 00 00 00 FD 
00 00 1C 0A 00 08 F8 24 1B 8E FD 94 AF 22 00 00 
00 55 53 40 01 8C 57 FC 06 00 00 02 D2 00 00 1C 
0A 00 08 F8 24 1B 70 FD 94 AF 22 00 00 00 61 53 
40 01 BF 57 26 07 00 00 02 D2 00 00 1C 0A 00 08 
F8 24 1B AC FD 94 AF 22 00 00 00 0F 54 40 01 86 
56 AE 06 00 00 00 FD 00 00 C1 00 09 19 64 00 19 
1C 0A 00 08 F8 24 1B 7A 04 95 AF 22 00 00 00 8D 
54 41 01 B8 54 EA 04 00 00 00 02 00 00 1C 05 00 
46 5E CE 80 1B 00 00 00 31 01 00 00 C9 1C 95 AF 
22 00 00 00 00 00 00 00 0E 01 46 05 00 46 5E CE 
80 1B 00 00 00 CC 00 00 00 AC 04 95 AF 22 00 00 
00 00 00 00 00 C0 B1 16 F3 AC 04 95 AF 22 00 00 
00 B2 04 95 AF 22 00 00 00 00 10 00 B7 2C 10 73 
00 01 00 C9 1C 95 AF 22 00 00 00 0E 01 00 00 4D 
0A 1C 0A 00 08 F8 24 1B B6 FD 94 AF 22 00 00 00 
11 54 40 01 86 56 92 06 00 00 00 FD 00 00 1C 0A 
00 08 F8 24 1B 0F F7 94 AF 22 00 00 00 C7 53 40 
01 0E 56 5A 08 00 00 02 29 00 00`, this)">Copy</button></div><pre class="code-block"><code>06 01 00 AF F9 6C A1 1C 0A 00 08 F8 24 1B A8 1C 
95 AF 22 00 00 00 A2 54 40 01 2D 55 45 02 00 00 
00 D1 00 00 1C 0A 00 08 F8 24 1B A2 04 95 AF 22 
00 00 00 70 54 40 01 47 55 55 02 00 00 09 EB 00 
00 1C 0A 00 08 F8 24 1B AC 04 95 AF 22 00 00 00 
4E 54 40 01 5A 55 2D 01 00 00 0A EF 00 00 1C 0A 
00 08 F8 24 1B 70 04 95 AF 22 00 00 00 48 54 40 
01 16 55 17 02 00 00 0A 15 00 00 1C 0A 00 08 F8 
24 1B DB FA 94 AF 22 00 00 00 72 54 40 01 5E 55 
06 02 00 00 0A 30 00 00 1C 0A 00 08 F8 24 1B CA 
FD 94 AF 22 00 00 00 13 54 40 01 86 56 C3 06 00 
00 00 FC 00 00 1C 0A 00 08 F8 24 1B C0 FD 94 AF 
22 00 00 00 11 54 40 01 87 56 96 06 00 00 00 FD 
00 00 1C 0A 00 08 F8 24 1B 8E FD 94 AF 22 00 00 
00 55 53 40 01 8C 57 FC 06 00 00 02 D2 00 00 1C 
0A 00 08 F8 24 1B 70 FD 94 AF 22 00 00 00 61 53 
40 01 BF 57 26 07 00 00 02 D2 00 00 1C 0A 00 08 
F8 24 1B AC FD 94 AF 22 00 00 00 0F 54 40 01 86 
56 AE 06 00 00 00 FD 00 00 C1 00 09 19 64 00 19 
1C 0A 00 08 F8 24 1B 7A 04 95 AF 22 00 00 00 8D 
54 41 01 B8 54 EA 04 00 00 00 02 00 00 1C 05 00 
46 5E CE 80 1B 00 00 00 31 01 00 00 C9 1C 95 AF 
22 00 00 00 00 00 00 00 0E 01 46 05 00 46 5E CE 
80 1B 00 00 00 CC 00 00 00 AC 04 95 AF 22 00 00 
00 00 00 00 00 C0 B1 16 F3 AC 04 95 AF 22 00 00 
00 B2 04 95 AF 22 00 00 00 00 10 00 B7 2C 10 73 
00 01 00 C9 1C 95 AF 22 00 00 00 0E 01 00 00 4D 
0A 1C 0A 00 08 F8 24 1B B6 FD 94 AF 22 00 00 00 
11 54 40 01 86 56 92 06 00 00 00 FD 00 00 1C 0A 
00 08 F8 24 1B 0F F7 94 AF 22 00 00 00 C7 53 40 
01 0E 56 5A 08 00 00 02 29 00 00</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick='copyToClipboard(`.....l......\$....."....T@.-UE...........
.\$....."...pT@.GUU............\$....."...
NT@.ZU-............\$.p..."...HT@..U.....
........\$....."...rT@.^U.....0.......\$..
..."....T@..V.............\$....."....T@.
.V.............\$....."...US@..W.........
....\$.p..."...aS@..W&amp;............\$....."
....T@..V............d.......\$.z..."....
TA..T...........F^......1.......".......
..F..F^.............."..............."..
.....".......,.s.......".......M......\$.
...."....T@..V.............\$....."....S@
..VZ....)..`, this)'>Copy</button></div><pre class="code-block"><code>.....l......$....."....T@.-UE...........
.$....."...pT@.GUU............$....."...
NT@.ZU-............$.p..."...HT@..U.....
........$....."...rT@.^U.....0.......$..
..."....T@..V.............$....."....T@.
.V.............$....."...US@..W.........
....$.p..."...aS@..W&amp;............$....."
....T@..V............d.......$.z..."....
TA..T...........F^......1.......".......
..F..F^.............."..............."..
.....".......,.s.......".......M......$.
...."....T@..V.............$....."....S@
..VZ....)..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN MultiPacket 0x0003</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0003`, this)">Copy</button></div><pre class="code-block"><code>0x0003</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`04 00 11 01 8E 04 00 11 01 8F`, this)">Copy</button></div><pre class="code-block"><code>04 00 11 01 8E 04 00 11 01 8F</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..........`, this)">Copy</button></div><pre class="code-block"><code>..........</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX MultiPacket 0x0003</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0003`, this)">Copy</button></div><pre class="code-block"><code>0x0003</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`04 00 15 0B 1E 9E 00 09 07 9E 00 19 2E 05 00 46 
5E CE 80 23 00 00 00 16 01 00 00 13 6C 35 E3 16 
00 00 00 00 00 00 00 80 00 00 00 02 B7 A8 D6 9B 
FC 19 AE 1A 00 00 00 00 00 00 00 22 05 00 46 5E 
CE 80 83 00 00 00 26 01 00 00 13 6C 35 E3 16 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 22 05 
00 46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 35 
E3 16 00 00 00 00 00 00 00 DF B5 1A AE 1A 00 00 
00 22 05 00 46 5E CE 80 83 00 00 00 26 01 00 00 
13 6C 35 E3 16 00 00 00 00 00 00 00 9B FC 19 AE 
1A 00 00 00 4F 05 00 46 5E CE 80 21 00 00 00 F1 
00 00 00 13 6C 35 E3 16 00 00 00 00 00 00 00 81 
49 E9 85 A2 01 00 00 EF B4 1A AE 1A 00 00 00 00 
00 00 00 33 FD 68 BD 00 00 00 00 E5 95 7F 3F D8 
AE 3E 3F 33 33 33 3F CA 56 49 40 00 00 00 41 00 
00 00 00 00 F0 00 09 07 9F 00 19 2E 05 00 46 5E 
CE 80 23 00 00 00 16 01 00 00 13 6C 35 E3 16 00 
00 00 00 00 00 00 80 00 00 00 02 B7 A8 D6 9B FC 
19 AE 1A 00 00 00 00 00 00 00 22 05 00 46 5E CE 
80 83 00 00 00 26 01 00 00 13 6C 35 E3 16 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 22 05 00 
46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 35 E3 
16 00 00 00 00 00 00 00 9B FC 19 AE 1A 00 00 00 
2E 05 00 46 5E CE 80 23 00 00 00 16 01 00 00 13 
6C 35 E3 16 00 00 00 00 00 00 00 80 00 00 00 02 
B7 A8 D6 9B FC 19 AE 1A 00 00 00 00 00 00 00 22 
05 00 46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 
35 E3 16 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 22 05 00 46 5E CE 80 83 00 00 00 26 01 00 
00 13 6C 35 E3 16 00 00 00 00 00 00 00 9B FC 19 
AE 1A 00 00 00`, this)">Copy</button></div><pre class="code-block"><code>04 00 15 0B 1E 9E 00 09 07 9E 00 19 2E 05 00 46 
5E CE 80 23 00 00 00 16 01 00 00 13 6C 35 E3 16 
00 00 00 00 00 00 00 80 00 00 00 02 B7 A8 D6 9B 
FC 19 AE 1A 00 00 00 00 00 00 00 22 05 00 46 5E 
CE 80 83 00 00 00 26 01 00 00 13 6C 35 E3 16 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 22 05 
00 46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 35 
E3 16 00 00 00 00 00 00 00 DF B5 1A AE 1A 00 00 
00 22 05 00 46 5E CE 80 83 00 00 00 26 01 00 00 
13 6C 35 E3 16 00 00 00 00 00 00 00 9B FC 19 AE 
1A 00 00 00 4F 05 00 46 5E CE 80 21 00 00 00 F1 
00 00 00 13 6C 35 E3 16 00 00 00 00 00 00 00 81 
49 E9 85 A2 01 00 00 EF B4 1A AE 1A 00 00 00 00 
00 00 00 33 FD 68 BD 00 00 00 00 E5 95 7F 3F D8 
AE 3E 3F 33 33 33 3F CA 56 49 40 00 00 00 41 00 
00 00 00 00 F0 00 09 07 9F 00 19 2E 05 00 46 5E 
CE 80 23 00 00 00 16 01 00 00 13 6C 35 E3 16 00 
00 00 00 00 00 00 80 00 00 00 02 B7 A8 D6 9B FC 
19 AE 1A 00 00 00 00 00 00 00 22 05 00 46 5E CE 
80 83 00 00 00 26 01 00 00 13 6C 35 E3 16 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 22 05 00 
46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 35 E3 
16 00 00 00 00 00 00 00 9B FC 19 AE 1A 00 00 00 
2E 05 00 46 5E CE 80 23 00 00 00 16 01 00 00 13 
6C 35 E3 16 00 00 00 00 00 00 00 80 00 00 00 02 
B7 A8 D6 9B FC 19 AE 1A 00 00 00 00 00 00 00 22 
05 00 46 5E CE 80 83 00 00 00 26 01 00 00 13 6C 
35 E3 16 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 22 05 00 46 5E CE 80 83 00 00 00 26 01 00 
00 13 6C 35 E3 16 00 00 00 00 00 00 00 9B FC 19 
AE 1A 00 00 00</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick='copyToClipboard(`...............F^..#........l5..........
..................."..F^......&amp;....l5...
.............."..F^......&amp;....l5........
........."..F^......&amp;....l5.............
....O..F^..!........l5..........I.......
...........3.h.......??..&gt;?333?.VI@...A.
..............F^..#........l5...........
.................."..F^......&amp;....l5....
............."..F^......&amp;....l5.........
...........F^..#........l5..............
..............."..F^......&amp;....l5.......
.........."..F^......&amp;....l5............
.....`, this)'>Copy</button></div><pre class="code-block"><code>...............F^..#........l5..........
..................."..F^......&amp;....l5...
.............."..F^......&amp;....l5........
........."..F^......&amp;....l5.............
....O..F^..!........l5..........I.......
...........3.h.......??..&gt;?333?.VI@...A.
..............F^..#........l5...........
.................."..F^......&amp;....l5....
............."..F^......&amp;....l5.........
...........F^..#........l5..............
..............."..F^......&amp;....l5.......
.........."..F^......&amp;....l5............
.....</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN MultiPacket 0x0003</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0003`, this)">Copy</button></div><pre class="code-block"><code>0x0003</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`04 00 15 02 0B 04 00 15 02 0F`, this)">Copy</button></div><pre class="code-block"><code>04 00 15 02 0B 04 00 15 02 0F</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..........`, this)">Copy</button></div><pre class="code-block"><code>..........</code></pre></div>
</td></tr>
</table></div>
<h2 id="packet-type---00-05"><span class="mw-headline" id="Packet_Type_--_00_05">Packet Type -- <b>00 05</b></span></h2>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>Packet Type 00 05  -  Disconnect (VARIOUS)</b></font>
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
<ul><li> <b>Connection ID</b> is the ID number assigned during the session request. Each client sends its own Connection ID. Reason ID is an ID number that corresponds for a reason for the disconnection.</li></ul>
<p>This packet is sent whenever one side wants to disconnect. It resends the clients specific Connection ID established during the session handshake, and then a reason for disconnection. The possible disconnect reasons and the associated ID seen in the packet are in the table below.
</p>
<div class="table-wrap"><table class="wikitable doc-table">
<tr>
<td><b>ID</b></td>
<td><b>String</b>
</td></tr>
<tr>
<td align="center">0</td>
<td>None
</td></tr>
<tr>
<td align="center">1</td>
<td>ICMP Error
</td></tr>
<tr>
<td align="center">2</td>
<td>Timeout
</td></tr>
<tr>
<td align="center">3</td>
<td>Other side terminated
</td></tr>
<tr>
<td align="center">4</td>
<td>Manager deleted
</td></tr>
<tr>
<td align="center">5</td>
<td>Connect fail
</td></tr>
<tr>
<td align="center">6</td>
<td>Application
</td></tr>
<tr>
<td align="center">7</td>
<td>Unreachable connection
</td></tr>
<tr>
<td align="center">8</td>
<td>Unacknowledged timeout
</td></tr>
<tr>
<td align="center">9</td>
<td>New connection attempt
</td></tr>
<tr>
<td align="center">10</td>
<td>Connection refused
</td></tr>
<tr>
<td align="center">11</td>
<td>Mutual connect error
</td></tr>
<tr>
<td align="center">12</td>
<td>Connecting to self
</td></tr>
<tr>
<td align="center">13</td>
<td>Reliable overflow
</td></tr></table></div>
<h2 id="packet-type---00-06"><span class="mw-headline" id="Packet_Type_--_00_06">Packet Type -- <b>00 06</b></span></h2>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 06   -  Keep Alive(VARIOUS)</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode	- Comp / CRC
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode	- Comp / CRC
</code></pre></div>
</td></tr></table></div>
<p>This packet is simply a keep alive to tell the other side that is still connected, but idle. It only consists of the opcode and a footer.
</p>
<h3 id="packet-samples---00-06"><span class="mw-headline" id="Packet_Samples_--_00_06">Packet Samples -- <b>00 06</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX Ping 0x0006</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0006`, this)">Copy</button></div><pre class="code-block"><code>0x0006</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`CB 3A 78`, this)">Copy</button></div><pre class="code-block"><code>CB 3A 78</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.:x`, this)">Copy</button></div><pre class="code-block"><code>.:x</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN Ping 0x0006</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0006`, this)">Copy</button></div><pre class="code-block"><code>0x0006</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`16 01 A7`, this)">Copy</button></div><pre class="code-block"><code>16 01 A7</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`...`, this)">Copy</button></div><pre class="code-block"><code>...</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX Ping 0x0006</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0006`, this)">Copy</button></div><pre class="code-block"><code>0x0006</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`C7 23 8F`, this)">Copy</button></div><pre class="code-block"><code>C7 23 8F</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.#.`, this)">Copy</button></div><pre class="code-block"><code>.#.</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN Ping 0x0006</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0006`, this)">Copy</button></div><pre class="code-block"><code>0x0006</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`CB 3A 78`, this)">Copy</button></div><pre class="code-block"><code>CB 3A 78</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.:x`, this)">Copy</button></div><pre class="code-block"><code>.:x</code></pre></div>
</td></tr>
</table></div>
<h2 id="packet-type---00-07"><span class="mw-headline" id="Packet_Type_--_00_07">Packet Type -- <b>00 07</b></span></h2>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 07  -  Client Network Status Update</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode		- Net Byte SHORT
Client TickCount	- Net Byte SHORT
Last update		- Net Byte INT
Average update		- Net Byte INT
Shortest update		- Net Byte INT
Longest update		- Net Byte INT
Last Server update	- Net Byte INT
Packets sent		- Net Byte LONG
Packets received	- Net Byte LONG
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode		- Net Byte SHORT
Client TickCount	- Net Byte SHORT
Last update		- Net Byte INT
Average update		- Net Byte INT
Shortest update		- Net Byte INT
Longest update		- Net Byte INT
Last Server update	- Net Byte INT
Packets sent		- Net Byte LONG
Packets received	- Net Byte LONG
</code></pre></div>
</td></tr></table></div>
<p>These packets consist of various data and network statistics. Because we do not care about network statistics, we will ignore these. To ignore these we send a special malformed Server Network Status Update.
</p><p><b>Note</b>: <font color="orange"><i>This packet is usually compressed but is optional.</i></font>
</p>
<h3 id="packet-samples---00-07"><span class="mw-headline" id="Packet_Samples_--_00_07">Packet Samples -- <b>00 07</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX NetStatRequest 0x0007</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0007`, this)">Copy</button></div><pre class="code-block"><code>0x0007</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`CA 3A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01`, this)">Copy</button></div><pre class="code-block"><code>CA 3A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.:....................................`, this)">Copy</button></div><pre class="code-block"><code>.:....................................</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p><p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN NetStatRequest 0x0007</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0007`, this)">Copy</button></div><pre class="code-block"><code>0x0007</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`D2 C7 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 `, this)">Copy</button></div><pre class="code-block"><code>D2 C7 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`......................................`, this)">Copy</button></div><pre class="code-block"><code>......................................</code></pre></div>
</td></tr>
</table></div>
<h2 id="packet-type---00-08"><span class="mw-headline" id="Packet_Type_--_00_08">Packet Type -- <b>00 08</b></span></h2>
<div class="table-wrap"><table class="doc-table" style="background-color: #FBF9FF; border: solid 1px #000000;" width="75%">
<tr>
<td style="background-color: #F1ECFF; border: solid 1px #FFFFFF"> <font size="-1"><b>00 08  -  Server Network Status Update</b></font>
</td></tr>
<tr>
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
SOE Opcode		- Net Byte SHORT
Client TickCount	- Net Byte SHORT (As in request)
Server TickCount	- Net Byte INT (I think this should be old server tickcount + client tickcount)
client packets sent	- Net Byte LONG
client packets received	- Net Byte LONG
server packets sent	- Net Byte LONG
server packets received - Net Byte LONG
`, this)">Copy</button></div><pre class="code-block"><code>
SOE Opcode		- Net Byte SHORT
Client TickCount	- Net Byte SHORT (As in request)
Server TickCount	- Net Byte INT (I think this should be old server tickcount + client tickcount)
client packets sent	- Net Byte LONG
client packets received	- Net Byte LONG
server packets sent	- Net Byte LONG
server packets received - Net Byte LONG
</code></pre></div>
</td></tr></table></div>
<h3 id="packet-samples---00-08"><span class="mw-headline" id="Packet_Samples_--_00_08">Packet Samples -- <b>00 08</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN NetStatResponse 0x0008</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0008`, this)">Copy</button></div><pre class="code-block"><code>0x0008</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`D2 C7 90 96 3F 20 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 02 `, this)">Copy</button></div><pre class="code-block"><code>D2 C7 90 96 3F 20 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 02 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`....?.................................`, this)">Copy</button></div><pre class="code-block"><code>....?.................................</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX NetStatResponse 0x0008</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0008`, this)">Copy</button></div><pre class="code-block"><code>0x0008</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`CA 3A 63 75 DB 1D 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 02 `, this)">Copy</button></div><pre class="code-block"><code>CA 3A 63 75 DB 1D 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 01 00 00 00 00 00 00 00 02 00 00 
00 00 00 00 00 02 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.:cu..................................`, this)">Copy</button></div><pre class="code-block"><code>.:cu..................................</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN NetStatResponse 0x0008</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0008`, this)">Copy</button></div><pre class="code-block"><code>0x0008</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 B9 6F 02 76 00 00 30 00 75 00 FE 7F 5F A8 2B 
CF 00 00 00 00 07 08 00 C6 27 F7 90 `, this)">Copy</button></div><pre class="code-block"><code>00 B9 6F 02 76 00 00 30 00 75 00 FE 7F 5F A8 2B 
CF 00 00 00 00 07 08 00 C6 27 F7 90 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..o.v..0.u..?_.+.........'..`, this)">Copy</button></div><pre class="code-block"><code>..o.v..0.u..?_.+.........'..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX NetStatResponse 0x0008</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0008`, this)">Copy</button></div><pre class="code-block"><code>0x0008</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 B9 6F 02 76 00 00 31 00 75 00 FE 7F 5F A8 2B 
CF 00 00 00 00 00 00 00 D3 03 F7 90 `, this)">Copy</button></div><pre class="code-block"><code>00 B9 6F 02 76 00 00 31 00 75 00 FE 7F 5F A8 2B 
CF 00 00 00 00 00 00 00 D3 03 F7 90 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..o.v..1.u..?_.+............`, this)">Copy</button></div><pre class="code-block"><code>..o.v..1.u..?_.+............</code></pre></div>
</td></tr>
</table></div>
<p>This packet is supposed to contain the Servers network statistics, however we felt it was a waste of time to reverse
these as we do not care about the statistics. Instead we send 38 bytes of 0x00, and then compress the packet, but skip appending a CRC.
The client seems to register that it recieved the servers statistics, but notices a bad CRC (or none in our case), 
and tosses out the packet as malformed. Because it recieved the packet it continues on without erroring.
</p><p>Note: This packet is usually compressed but is optional.
</p>
<h2 id="packet-type---00-09"><span class="mw-headline" id="Packet_Type_--_00_09">Packet Type -- <b>00 09</b></span></h2>
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
<h3 id="packet-samples---00-09"><span class="mw-headline" id="Packet_Samples_--_00_09">Packet Samples -- <b>00 09</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN DataChannel 0x0009</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0009`, this)">Copy</button></div><pre class="code-block"><code>0x0009</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 03 01 00 BE E9 2F D7 `, this)">Copy</button></div><pre class="code-block"><code>00 03 01 00 BE E9 2F D7 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`....../.`, this)">Copy</button></div><pre class="code-block"><code>....../.</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX DataChannel 0x0009</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0009`, this)">Copy</button></div><pre class="code-block"><code>0x0009</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`54 06 00 19 A4 05 00 2A 2F F1 F3 F2 BB 21 B6 1E 
00 00 00 00 00 04 00 00 00 09 00 63 6F 6E 64 69 
74 69 6F 6E 07 00 00 00 31 00 30 00 30 00 2F 00 
31 00 30 00 30 00 06 00 76 6F 6C 75 6D 65 01 00 
00 00 31 00 2D 00 63 61 74 5F 73 6B 69 6C 6C 5F 
6D 6F 64 5F 62 6F 6E 75 73 2E 40 73 74 61 74 5F 
6E 3A 73 74 72 65 6E 67 74 68 5F 6D 6F 64 69 66 
69 65 64 02 00 00 00 31 00 37 00 20 00 40 70 72 
6F 63 2F 70 72 6F 63 3A 72 65 71 75 69 72 65 64 
5F 63 6F 6D 62 61 74 5F 6C 65 76 65 6C 02 00 00 
00 38 00 35 00 FF FF FF FF 26 05 00 2A 2F F1 F3 
D5 C5 21 B6 1E 00 00 00 00 00 01 00 00 00 06 00 
76 6F 6C 75 6D 65 01 00 00 00 31 00 FF FF FF FF 
FF 01 18 05 00 2A 2F F1 F3 D6 C5 21 B6 1E 00 00 
00 00 00 08 00 00 00 06 00 76 6F 6C 75 6D 65 01 
00 00 00 31 00 20 00 40 70 72 6F 63 2F 70 72 6F 
63 3A 72 65 71 75 69 72 65 64 5F 63 6F 6D 62 61 
74 5F 6C 65 76 65 6C 02 00 00 00 32 00 30 00 15 
00 40 70 72 6F 63 2F 70 72 6F 63 3A 72 65 75 73 
65 5F 74 69 6D 65 07 00 00 00 35 00 20 00 2F 00 
20 00 73 00 65 00 63 00 17 00 40 70 72 6F 63 2F 
70 72 6F 63 3A 65 66 66 65 63 74 5F 6C 65 76 65 
6C 02 00 00 00 32 00 30 00 14 00 40 70 72 6F 63 
2F 70 72 6F 63 3A 70 72 6F 63 5F 6E 61 6D 65 18 
00 00 00 40 00 75 00 69 00 5F 00 62 00 75 00 66 
00 66 00 3A 00 61 00 67 00 69 00 63 00 6F 00 6E 
00 73 00 75 00 6D 00 61 00 62 00 6C 00 65 00 31 
00 35 00 04 00 74 69 65 72 01 00 00 00 32 00 0C 
00 74 6F 6F 6C 74 69 70 2E 74 69 65 72 01 00 00 
00 32 00 0C 00 6E 75 6D 5F 69 6E 5F 73 74 61 63 
6B 01 00 00 00 36 00 FF FF FF FF `, this)">Copy</button></div><pre class="code-block"><code>54 06 00 19 A4 05 00 2A 2F F1 F3 F2 BB 21 B6 1E 
00 00 00 00 00 04 00 00 00 09 00 63 6F 6E 64 69 
74 69 6F 6E 07 00 00 00 31 00 30 00 30 00 2F 00 
31 00 30 00 30 00 06 00 76 6F 6C 75 6D 65 01 00 
00 00 31 00 2D 00 63 61 74 5F 73 6B 69 6C 6C 5F 
6D 6F 64 5F 62 6F 6E 75 73 2E 40 73 74 61 74 5F 
6E 3A 73 74 72 65 6E 67 74 68 5F 6D 6F 64 69 66 
69 65 64 02 00 00 00 31 00 37 00 20 00 40 70 72 
6F 63 2F 70 72 6F 63 3A 72 65 71 75 69 72 65 64 
5F 63 6F 6D 62 61 74 5F 6C 65 76 65 6C 02 00 00 
00 38 00 35 00 FF FF FF FF 26 05 00 2A 2F F1 F3 
D5 C5 21 B6 1E 00 00 00 00 00 01 00 00 00 06 00 
76 6F 6C 75 6D 65 01 00 00 00 31 00 FF FF FF FF 
FF 01 18 05 00 2A 2F F1 F3 D6 C5 21 B6 1E 00 00 
00 00 00 08 00 00 00 06 00 76 6F 6C 75 6D 65 01 
00 00 00 31 00 20 00 40 70 72 6F 63 2F 70 72 6F 
63 3A 72 65 71 75 69 72 65 64 5F 63 6F 6D 62 61 
74 5F 6C 65 76 65 6C 02 00 00 00 32 00 30 00 15 
00 40 70 72 6F 63 2F 70 72 6F 63 3A 72 65 75 73 
65 5F 74 69 6D 65 07 00 00 00 35 00 20 00 2F 00 
20 00 73 00 65 00 63 00 17 00 40 70 72 6F 63 2F 
70 72 6F 63 3A 65 66 66 65 63 74 5F 6C 65 76 65 
6C 02 00 00 00 32 00 30 00 14 00 40 70 72 6F 63 
2F 70 72 6F 63 3A 70 72 6F 63 5F 6E 61 6D 65 18 
00 00 00 40 00 75 00 69 00 5F 00 62 00 75 00 66 
00 66 00 3A 00 61 00 67 00 69 00 63 00 6F 00 6E 
00 73 00 75 00 6D 00 61 00 62 00 6C 00 65 00 31 
00 35 00 04 00 74 69 65 72 01 00 00 00 32 00 0C 
00 74 6F 6F 6C 74 69 70 2E 74 69 65 72 01 00 00 
00 32 00 0C 00 6E 75 6D 5F 69 6E 5F 73 74 61 63 
6B 01 00 00 00 36 00 FF FF FF FF </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`T......*/....!.............condition....
1.0.0./.1.0.0...volume....1.-.cat_skill_
mod_bonus.@stat_n:strength_modified....1
.7...@proc/proc:required_combat_level...
.8.5.....&amp;..*/....!.............volume..
..1..........*/....!.............volume.
...1...@proc/proc:required_combat_level.
...2.0...@proc/proc:reuse_time....5.../.
..s.e.c...@proc/proc:effect_level....2.0
...@proc/proc:proc_name....@.u.i._.b.u.f
.f.:.a.g.i.c.o.n.s.u.m.a.b.l.e.1.5...tie
r....2...tooltip.tier....2...num_in_stac
k....6.....`, this)">Copy</button></div><pre class="code-block"><code>T......*/....!.............condition....
1.0.0./.1.0.0...volume....1.-.cat_skill_
mod_bonus.@stat_n:strength_modified....1
.7...@proc/proc:required_combat_level...
.8.5.....&amp;..*/....!.............volume..
..1..........*/....!.............volume.
...1...@proc/proc:required_combat_level.
...2.0...@proc/proc:reuse_time....5.../.
..s.e.c...@proc/proc:effect_level....2.0
...@proc/proc:proc_name....@.u.i._.b.u.f
.f.:.a.g.i.c.o.n.s.u.m.a.b.l.e.1.5...tie
r....2...tooltip.tier....2...num_in_stac
k....6.....</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN DataChannel 0x0009</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0009`, this)">Copy</button></div><pre class="code-block"><code>0x0009</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`01 F5 01 00 E0 5E 80 31 `, this)">Copy</button></div><pre class="code-block"><code>01 F5 01 00 E0 5E 80 31 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.....^.1`, this)">Copy</button></div><pre class="code-block"><code>.....^.1</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX DataChannel 0x0009</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0009`, this)">Copy</button></div><pre class="code-block"><code>0x0009</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`20 46 05 00 46 5E CE 80 23 00 00 00 16 01 00 00 
48 12 06 E1 01 00 00 00 00 00 00 00 80 0D 00 00 
EF 50 45 16 00 00 00 00 00 00 00 00 DD 00 00 00 
36 00 37 00 32 00 37 00 33 00 37 00 31 00 34 00 
33 00 30 00 36 00 20 00 30 00 20 00 31 00 30 00 
38 00 37 00 38 00 36 00 38 00 39 00 30 00 33 00 
39 00 37 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 36 00 39 00 31 00 39 00 39 00 
30 00 33 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 37 00 30 00 39 00 30 00 37 00 
32 00 34 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 37 00 31 00 31 00 37 00 37 00 
33 00 31 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 36 00 33 00 36 00 
34 00 37 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 36 00 38 00 32 00 
32 00 34 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 39 00 30 00 37 00 
33 00 30 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 31 00 34 00 35 00 
31 00 30 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 34 00 33 00 39 00 
34 00 38 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 39 00 30 00 38 00 
31 00 39 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 39 00 35 00 30 00 
39 00 37 00 20 00 2D 00 31 00 20 00 31 00 31 00 
30 00 36 00 30 00 36 00 34 00 34 00 32 00 35 00 
37 00 36 00 20 00 30 00 20 00 31 00 31 00 30 00 
36 00 37 00 39 00 33 00 38 00 33 00 35 00 31 00 
36 00 20 00 2D 00 31 00 20 00 `, this)">Copy</button></div><pre class="code-block"><code>20 46 05 00 46 5E CE 80 23 00 00 00 16 01 00 00 
48 12 06 E1 01 00 00 00 00 00 00 00 80 0D 00 00 
EF 50 45 16 00 00 00 00 00 00 00 00 DD 00 00 00 
36 00 37 00 32 00 37 00 33 00 37 00 31 00 34 00 
33 00 30 00 36 00 20 00 30 00 20 00 31 00 30 00 
38 00 37 00 38 00 36 00 38 00 39 00 30 00 33 00 
39 00 37 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 36 00 39 00 31 00 39 00 39 00 
30 00 33 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 37 00 30 00 39 00 30 00 37 00 
32 00 34 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 38 00 37 00 31 00 31 00 37 00 37 00 
33 00 31 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 36 00 33 00 36 00 
34 00 37 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 36 00 38 00 32 00 
32 00 34 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 31 00 39 00 30 00 37 00 
33 00 30 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 31 00 34 00 35 00 
31 00 30 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 34 00 33 00 39 00 
34 00 38 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 39 00 30 00 38 00 
31 00 39 00 20 00 2D 00 31 00 20 00 31 00 30 00 
38 00 37 00 39 00 35 00 32 00 39 00 35 00 30 00 
39 00 37 00 20 00 2D 00 31 00 20 00 31 00 31 00 
30 00 36 00 30 00 36 00 34 00 34 00 32 00 35 00 
37 00 36 00 20 00 30 00 20 00 31 00 31 00 30 00 
36 00 37 00 39 00 33 00 38 00 33 00 35 00 31 00 
36 00 20 00 2D 00 31 00 20 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`.F..F^..#.......H................PE.....
........6.7.2.7.3.7.1.4.3.0.6...0...1.0.
8.7.8.6.8.9.0.3.9.7...-.1...1.0.8.7.8.6.
9.1.9.9.0.3...-.1...1.0.8.7.8.7.0.9.0.7.
2.4...-.1...1.0.8.7.8.7.1.1.7.7.3.1...-.
1...1.0.8.7.9.5.1.6.3.6.4.7...-.1...1.0.
8.7.9.5.1.6.8.2.2.4...-.1...1.0.8.7.9.5.
1.9.0.7.3.0...-.1...1.0.8.7.9.5.2.1.4.5.
1.0...-.1...1.0.8.7.9.5.2.4.3.9.4.8...-.
1...1.0.8.7.9.5.2.9.0.8.1.9...-.1...1.0.
8.7.9.5.2.9.5.0.9.7...-.1...1.1.0.6.0.6.
4.4.2.5.7.6...0...1.1.0.6.7.9.3.8.3.5.1.
6...-.1...`, this)">Copy</button></div><pre class="code-block"><code>.F..F^..#.......H................PE.....
........6.7.2.7.3.7.1.4.3.0.6...0...1.0.
8.7.8.6.8.9.0.3.9.7...-.1...1.0.8.7.8.6.
9.1.9.9.0.3...-.1...1.0.8.7.8.7.0.9.0.7.
2.4...-.1...1.0.8.7.8.7.1.1.7.7.3.1...-.
1...1.0.8.7.9.5.1.6.3.6.4.7...-.1...1.0.
8.7.9.5.1.6.8.2.2.4...-.1...1.0.8.7.9.5.
1.9.0.7.3.0...-.1...1.0.8.7.9.5.2.1.4.5.
1.0...-.1...1.0.8.7.9.5.2.4.3.9.4.8...-.
1...1.0.8.7.9.5.2.9.0.8.1.9...-.1...1.0.
8.7.9.5.2.9.5.0.9.7...-.1...1.1.0.6.0.6.
4.4.2.5.7.6...0...1.1.0.6.7.9.3.8.3.5.1.
6...-.1...</code></pre></div>
</td></tr>
</table></div>
<p>Sequence # is a sequence number applied to every data packet. It increments in order for each packet and is used to help determine
out of order packets. This protocol is used to send an SWG Packet that NEEDS to be recieved by the other end. 
The reciver is then supposed to respond with a an ACKNOWLEDGE packet that contains the same sequence so the sender knows it
has been recieved. This system ensures packets not only get sent correctly, but also stay in order.
</p><p>After the sequence # comes the encapsulated SWG Packet. 
</p><p>Note* it is possible to combine multiple SWG PACKETs into a single 09. 
This is done similar to the 0x0003 packet, a multi data example:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
(00 09) (sequence) (00 19) (Size1) (SWG PACKET) (Size2) (SWG PACKET)
SOE op.  sequence   multi   size       data       size      data
`, this)">Copy</button></div><pre class="code-block"><code>
(00 09) (sequence) (00 19) (Size1) (SWG PACKET) (Size2) (SWG PACKET)
SOE op.  sequence   multi   size       data       size      data
</code></pre></div>
<p>if the Size byte is FF the following 2 bytes are the size Word Little ended (16bit).
Example:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
(00 09) (sequence) (00 19) (size byte) (size word) (SWG PACKET) (size byte) (SWG PACKET)
SOE op.  sequence   multi    FF          01 99        data         33          data
`, this)">Copy</button></div><pre class="code-block"><code>
(00 09) (sequence) (00 19) (size byte) (size word) (SWG PACKET) (size byte) (SWG PACKET)
SOE op.  sequence   multi    FF          01 99        data         33          data
</code></pre></div>
<p>In the above the first packet size is 409 Dec.
</p><p>Use these to combine SWG PACKETs together into 1 data packet/sequence number.
</p>
<h2 id="packet-type---00-0d"><span class="mw-headline" id="Packet_Type_--_00_0D">Packet Type -- <b>00 0D</b></span></h2>
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
<h3 id="packet-samples---00-0d"><span class="mw-headline" id="Packet_Samples_--_00_0D">Packet Samples -- <b>00 0D</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN DataFrag 0x000D</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x000D`, this)">Copy</button></div><pre class="code-block"><code>0x000D</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`04 CC 00`, this)">Copy</button></div><pre class="code-block"><code>04 CC 00</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`...`, this)">Copy</button></div><pre class="code-block"><code>...</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX DataFrag 0x000D</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x000D`, this)">Copy</button></div><pre class="code-block"><code>0x000D</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 02 00 00 02 00 03 00 B9 63 1C C1 1B 00 00 00 
02 00 00 00 04 00 42 72 69 61 80 8F FF FF 03 00 
00 00 05 00 41 68 61 7A 69 80 8F FF FF 0C 00 00 
00 06 00 46 6C 75 72 72 79 80 8F FF FF 0D 00 00 
00 08 00 49 6E 74 72 65 70 69 64 80 8F FF FF 0E 
00 00 00 09 00 4B 65 74 74 65 6D 6F 6F 72 80 8F 
FF FF 0F 00 00 00 07 00 4E 61 72 69 74 75 73 80 
8F FF FF 10 00 00 00 06 00 53 63 79 6C 6C 61 80 
8F FF FF 11 00 00 00 09 00 53 75 6E 72 75 6E 6E 
65 72 80 8F FF FF 12 00 00 00 06 00 56 61 6C 63 
79 6E 80 8F FF FF 13 00 00 00 07 00 54 65 6D 70 
65 73 74 80 8F FF FF 28 00 00 00 0C 00 4A 61 70 
61 6E 2D 4B 61 74 61 6E 61 00 00 00 00 29 00 00 
00 0B 00 4A 61 70 61 6E 2D 48 61 72 6C 61 00 00 
00 00 19 00 00 00 09 00 53 74 61 72 73 69 64 65 
72 80 8F FF FF 1A 00 00 00 09 00 54 61 72 71 75 
69 6E 61 73 80 8F FF FF 1B 00 00 00 0A 00 57 61 
6E 64 65 72 68 6F 6D 65 80 8F FF FF 1C 00 00 00 
0A 00 53 68 61 64 6F 77 66 69 72 65 80 8F FF FF 
05 00 00 00 08 00 42 6C 6F 6F 64 66 69 6E 80 8F 
FF FF 06 00 00 00 09 00 43 68 69 6C 61 73 74 72 
61 80 8F FF FF 07 00 00 00 07 00 45 63 6C 69 70 
73 65 80 8F FF FF 08 00 00 00 06 00 47 6F 72 61 
74 68 80 8F FF FF 09 00 00 00 05 00 4B 61 75 72 
69 80 8F FF FF 0A 00 00 00 05 00 4C 6F 77 63 61 
80 8F FF FF 0B 00 00 00 07 00 52 61 64 69 61 6E 
74 80 8F FF FF 04 00 00 00 09 00 43 6F 72 62 61 
6E 74 69 73 80 8F FF FF 22 00 00 00 0F 00 45 75 
72 6F 70 65 2D 43 68 69 6D 61 65 72 61 80 8F FF 
FF 23 00 00 00 0E 00 45 75 72 6F 70 65 2D 46 61 
72 53 74 61 72 80 8F FF FF 24 00 `, this)">Copy</button></div><pre class="code-block"><code>00 02 00 00 02 00 03 00 B9 63 1C C1 1B 00 00 00 
02 00 00 00 04 00 42 72 69 61 80 8F FF FF 03 00 
00 00 05 00 41 68 61 7A 69 80 8F FF FF 0C 00 00 
00 06 00 46 6C 75 72 72 79 80 8F FF FF 0D 00 00 
00 08 00 49 6E 74 72 65 70 69 64 80 8F FF FF 0E 
00 00 00 09 00 4B 65 74 74 65 6D 6F 6F 72 80 8F 
FF FF 0F 00 00 00 07 00 4E 61 72 69 74 75 73 80 
8F FF FF 10 00 00 00 06 00 53 63 79 6C 6C 61 80 
8F FF FF 11 00 00 00 09 00 53 75 6E 72 75 6E 6E 
65 72 80 8F FF FF 12 00 00 00 06 00 56 61 6C 63 
79 6E 80 8F FF FF 13 00 00 00 07 00 54 65 6D 70 
65 73 74 80 8F FF FF 28 00 00 00 0C 00 4A 61 70 
61 6E 2D 4B 61 74 61 6E 61 00 00 00 00 29 00 00 
00 0B 00 4A 61 70 61 6E 2D 48 61 72 6C 61 00 00 
00 00 19 00 00 00 09 00 53 74 61 72 73 69 64 65 
72 80 8F FF FF 1A 00 00 00 09 00 54 61 72 71 75 
69 6E 61 73 80 8F FF FF 1B 00 00 00 0A 00 57 61 
6E 64 65 72 68 6F 6D 65 80 8F FF FF 1C 00 00 00 
0A 00 53 68 61 64 6F 77 66 69 72 65 80 8F FF FF 
05 00 00 00 08 00 42 6C 6F 6F 64 66 69 6E 80 8F 
FF FF 06 00 00 00 09 00 43 68 69 6C 61 73 74 72 
61 80 8F FF FF 07 00 00 00 07 00 45 63 6C 69 70 
73 65 80 8F FF FF 08 00 00 00 06 00 47 6F 72 61 
74 68 80 8F FF FF 09 00 00 00 05 00 4B 61 75 72 
69 80 8F FF FF 0A 00 00 00 05 00 4C 6F 77 63 61 
80 8F FF FF 0B 00 00 00 07 00 52 61 64 69 61 6E 
74 80 8F FF FF 04 00 00 00 09 00 43 6F 72 62 61 
6E 74 69 73 80 8F FF FF 22 00 00 00 0F 00 45 75 
72 6F 70 65 2D 43 68 69 6D 61 65 72 61 80 8F FF 
FF 23 00 00 00 0E 00 45 75 72 6F 70 65 2D 46 61 
72 53 74 61 72 80 8F FF FF 24 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick='copyToClipboard(`.........c............Bria..........Ahaz
i..........Flurry..........Intrepid.....
.....Kettemoor..........Naritus.........
.Scylla..........Sunrunner..........Valc
yn..........Tempest....(.....Japan-Katan
a....).....Japan-Harla..........Starside
r..........Tarquinas..........Wanderhome
..........Shadowfire..........Bloodfin..
........Chilastra..........Eclipse......
....Gorath..........Kauri..........Lowca
..........Radiant..........Corbantis....
".....Europe-Chimaera....#.....Europe-Fa
rStar....\$.`, this)'>Copy</button></div><pre class="code-block"><code>.........c............Bria..........Ahaz
i..........Flurry..........Intrepid.....
.....Kettemoor..........Naritus.........
.Scylla..........Sunrunner..........Valc
yn..........Tempest....(.....Japan-Katan
a....).....Japan-Harla..........Starside
r..........Tarquinas..........Wanderhome
..........Shadowfire..........Bloodfin..
........Chilastra..........Eclipse......
....Gorath..........Kauri..........Lowca
..........Radiant..........Corbantis....
".....Europe-Chimaera....#.....Europe-Fa
rStar....$.</code></pre></div>
</td></tr>
</table></div>
<ul><li> <b>Sequence #</b> is the same type of sequence number described in the "00 09  -  Channel 0 Data" section. All the same rules apply.</li></ul>
<ul><li> <b>FragmentSize</b> is the total size of the combined fragments. This only appears in the FIRST packet of a group of fragmented packets.</li></ul>
<p>Next is just the piece data of the large SWG Packet. Fragments are made when the total UNCOMPRESSED packet exceeds the packet buffer size, which is 496 bytes.
</p>
<h2 id="packet-type---00-11"><span class="mw-headline" id="Packet_Type_--_00_11">Packet Type -- <b>00 11</b></span></h2>
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
<h3 id="packet-samples---00-11"><span class="mw-headline" id="Packet_Samples_--_00_11">Packet Samples -- <b>00 11</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN DataOrder 0x0011</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0011`, this)">Copy</button></div><pre class="code-block"><code>0x0011</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0B A0 `, this)">Copy</button></div><pre class="code-block"><code>0B A0 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX DataOrder 0x0011</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0011`, this)">Copy</button></div><pre class="code-block"><code>0x0011</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0B 87 `, this)">Copy</button></div><pre class="code-block"><code>0B 87 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN DataOrder 0x0011</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0011`, this)">Copy</button></div><pre class="code-block"><code>0x0011</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`20 C8 `, this)">Copy</button></div><pre class="code-block"><code>20 C8 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX DataOrder 0x0011</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0011`, this)">Copy</button></div><pre class="code-block"><code>0x0011</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`20 C7 `, this)">Copy</button></div><pre class="code-block"><code>20 C7 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
Sequence # is the sequence number of the out of order packet recieved. 
It will send one for every packet that is out of order, and the ones following.
</p><p>So if packet sequences recieved are:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
00 00
00 01
`, this)">Copy</button></div><pre class="code-block"><code>
00 00
00 01
</code></pre></div>
<p>And then:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
00 03
`, this)">Copy</button></div><pre class="code-block"><code>
00 03
</code></pre></div>
<p>an out of order will be sent for the packet with sequence 00 03. 
</p><p>If the packet sequences recieved are:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
00 00
00 01
`, this)">Copy</button></div><pre class="code-block"><code>
00 00
00 01
</code></pre></div>
<p>And then:
</p>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`
00 03
00 04
00 05
`, this)">Copy</button></div><pre class="code-block"><code>
00 03
00 04
00 05
</code></pre></div>
<p>An out of order packet will be sent for all 3 of the out of order sequences.
</p>
<h2 id="packet-type---00-15"><span class="mw-headline" id="Packet_Type_--_00_15">Packet Type -- <b>00 15</b></span></h2>
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
<h3 id="packet-samples---00-15"><span class="mw-headline" id="Packet_Samples_--_00_15">Packet Samples -- <b>00 15</b></span></h3>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MIN DataAck 0x0015</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0015`, this)">Copy</button></div><pre class="code-block"><code>0x0015</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 `, this)">Copy</button></div><pre class="code-block"><code>00 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Server MAX DataAck 0x0015</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0015`, this)">Copy</button></div><pre class="code-block"><code>0x0015</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 `, this)">Copy</button></div><pre class="code-block"><code>00 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MIN DataAck 0x0015</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0015`, this)">Copy</button></div><pre class="code-block"><code>0x0015</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 `, this)">Copy</button></div><pre class="code-block"><code>00 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<p><br/>
</p>
<div class="table-wrap"><table class="doc-table" style="background-color: #FFFFFB; border: solid 1px #cacaca;" width="75%">
<tr>
<td colspan="3" style="background-color: #D7E5E4; border: solid 1px #FFFFFF"> <font size="-1"><b>Client MAX DataAck 0x0015</b></font>
</td></tr>
<tr align="center">
<td> <b>Def</b> </td>
<td> <b>HEX</b> </td>
<td> <b>ASCII</b>
</td></tr>
<tr valign="top">
<td>
<div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`0x0015`, this)">Copy</button></div><pre class="code-block"><code>0x0015</code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`00 00 `, this)">Copy</button></div><pre class="code-block"><code>00 00 </code></pre></div>
</td>
<td> <div class="code-container"><div class="code-header"><span>Specification / Code</span><button class="copy-btn" onclick="copyToClipboard(`..`, this)">Copy</button></div><pre class="code-block"><code>..</code></pre></div>
</td></tr>
</table></div>
<ul><li> <b>Sequence #</b> is the sequence number of the packet to acknowledge to the sender that it was recieved correctly.</li></ul>
<p>Every packet sent with a sequence number MUST be acknowledeged.
</p><p>They do not neccesarily need to be Acknowledeged 1 by 1. For example:
If packet sequences recieved are:
00 00
00 01
00 02
</p><p>An Acknowledge of 00 15 00 02 will cover all the packets up to the sequence 00 02.
</p><p>The client will stop processing packets after about 4 unacknowledeged packets so frequent acknowledges are needed.
</p>
<h2 id="appendix"><span class="mw-headline" id="Appendix">Appendix</span></h2>
<p><a href="../guides/swg-packet-examples.html" title="SWGPacketExamples">SWG Packet Examples used in this document</a>
</p>
<font color="blue"><b>Thanks to Acid1789 for the abundant information on the SOE Protocol!</b></font></div>

NewPP limit report
Cached time: 20261017052151
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.218 seconds
Real time usage: 0.220 seconds
Preprocessor visited node count: 1449/1000000
Preprocessor generated node count: 4448/1000000
Post‐expand include size: 16437/2097152 bytes
Template argument size: 4852/2097152 bytes
Highest expansion depth: 3/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%   70.496      1 - -total
 60.13%   42.391     32 - Template:InfoboxPacketSample
 13.24%    9.334     12 - Template:InfoboxPacketDetail
  3.32%    2.340      1 - Template:PageHeader

Saved in parser cache with key swganh_wiki:pcache:idhash:1826-0!*!0!!*!*!* and timestamp 20261017052150 and revision id 257057
