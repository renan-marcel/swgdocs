---
title: Reversing Structs
section: guides
wiki_url: https://wiki.swganh.org/index.php/Reversing_Structs
wiki_revid: 9224
layout: guide
date_audited: 2026-10-17
---

# Reversing Structs

How to reverse packet structures via live debugging in ollydbg:

1. Set a break point at location: 0x0118B064, it should read POP EBX

2. Send your packet

3. Olly should break, the client is now reading your packet, the number of bytes it is reading is in register ESI,

you must first let it read the header, so you should go through a sequence of two bytes then four bytes, three times, eg:

ESI reads:

2

4

2

4

2

4

4. Hit play every time you want the next value, after going through the header you are in the data!  Write down ESI and hit play continually until the client stops breaking at that location

NewPP limit report
Cached time: 20261017154724
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.003 seconds
Real time usage: 0.002 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:3501-0!*!*!*!*!*!* and timestamp 20261017154724 and revision id 9224
