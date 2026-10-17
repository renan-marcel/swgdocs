---
title: Packet:PacketFooter
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet%3APacketFooter
wiki_revid: 1666
layout: guide
date_audited: 2026-10-17
---

# Packet:PacketFooter

Packet Footers:

Every packet in SWG, regardless wether it is just SOE Protocol, just an SWG Packet, or a combination of the both, has a footer.

The footer's format is as follows:

[Compression Flag: 1 byte][CRC value:2 bytes]
total of 3 bytes
[CompFlag][CRC1][CRC2]

The checksum algorithm used is a seeded CRC32 checksum of all the data in a packet EXCEPT the crc value located in the footer
(so that includes the compression flag). The CRC is calculated after the compression and then encryption are both applied.

The compression used is a default level ZLIB compression applied on the data BETWEEN the SOE opcode(part of the SOE Protocol) and the footer. 
So far no record has been made of a compressed packet that is NOT inside the SOE Protocol. If the packet is compressed, the Compression Flag 
(CompFlag) is a 1. Uncompressed packets have a Compression Flag (CompFlag) of 0.

NewPP limit report
Cached time: 20261017165641
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.006 seconds
Real time usage: 0.006 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1549-0!*!*!*!*!*!* and timestamp 20261017165641 and revision id 1666
