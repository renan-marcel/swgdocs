---
title: Packet:Intro
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet%3AIntro
wiki_revid: 1722
layout: guide
date_audited: 2026-10-17
---

# Packet:Intro

### Introduction to Packets

Packets are a form of data communication over networks. In online games, packets are sent between the client(game) 
and a server to communicate various technical aspects of the game such as health,location,item data, player messages, etc.

They are usually just a chain of 0's and 1's that can be interpreted. Because binary is difficult to read, packets are usually
displayed in hexadecimal, which is a base 16 number system that makes them smaller and easier to read.

Instead of "01011100", you would read "5C". The rest of the packet documentation assumes you understand binary and 
hexadecimal number systems.

SWG uses an outer protocol that is unique to only SOE games. From now on this will be refered to as the "SOE Protocol". 
It's purpose is to enhance the UDP packet system they use for the game. 
Google "UDP vs TCP" to learn more about the two network protocols.

There are a few various ways SOE protocol can be used along with SWG packets.

(SOE Protocol)(*Footer) - This form is just a standalone packet that is part of the SOE protocol, 
no SWG data is attached to it.

(SOE Protocol)(SWG Packet)(Footer) - This form is an SWG packet wrapped around the SOE protocol.

(SOE Protocol)((SOE Protocol)(SWG Packet))(Footer) - Multiple SOE protocol pieces are put together.

(SWG Packet)(Footer) - This is a stand-alone SWG packet, its only common for data that does not need to be 
verified by the server or client and can potentially be lost without causing problems.

((SWG Packet)(SWG Packet))(Footer) - 2 SWG packets can be combined within the same set of data.

(SOE Protocol)((SWG Packet)(SWG Packet))(Footer) - Same as above but wrapped around the SOE protocol.

Packets can even get as complicated as this:
(SOE Protocol)((SOE Protocol)(SOE Protocol(((SWG Packet)(SWG Packet)))(SOE Protocol)(SWG Packet))(Footer)

- Notice: Every packet regardless of its formation has a footer. There are a few exceptions in the SOE Protocol.

See SOE Protocol for more information on it.

Within the footer of a packet is a CRC32 checksum which is used to check the validity of a packet transmitted. 
SWG also has its packets encrypted, and some are also compressed. Please read the corresponding articles for more information.

NewPP limit report
Cached time: 20261017165638
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.011 seconds
Real time usage: 0.011 seconds
Preprocessor visited node count: 2/1000000
Preprocessor generated node count: 8/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total

Saved in parser cache with key swganh_wiki:pcache:idhash:1546-0!*!*!*!*!*!* and timestamp 20261017165638 and revision id 1722
