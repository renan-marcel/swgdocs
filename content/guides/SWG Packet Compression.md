---
title: SWG Packet Compression
section: guides
wiki_url: https://wiki.swganh.org/index.php/SWG_Packet_Compression
wiki_revid: 2308
layout: guide
date_audited: 2026-10-17
---

# SWG Packet Compression

The compression algorithm used on SWG packets is a standard ZLIB algorithm.

Please refer to ZLIB documentation on how the algorithm functions, for the sake of  simplicity, we use the ZLIB's Compress/Decompress functions on the data at a standard level of compression.

The data that is compressed is between the SOE Opcode and the footer. So far no stand-alone SWG Packets have been recorded that are compressed.

If data is compressed, the first byte of the footer (which is a compression byteflag) is 1. If it is not compressed, it is a 0.

Compression will occur BEFORE encryption, and BEFORE a CRC value is appended.

Compression is applied on all network status updates (both client and server), and on packets that are generally > 100 bytes. The largest any packet can be uncompressed is 496 bytes, which includes the footer. If it is larger it must be fragmented first.

NewPP limit report
Cached time: 20261017165722
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.004 seconds
Real time usage: 0.005 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1825-0!*!*!*!*!*!* and timestamp 20261017165722 and revision id 2308
