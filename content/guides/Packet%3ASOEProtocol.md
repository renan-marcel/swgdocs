---
title: Packet:SOEProtocol
url: https://wiki.swganh.org/index.php/Packet%3ASOEProtocol
page_type: Other
opcode: 
revision_id: 1729
last_modified: 2006-12-16T07:50:54Z
completion: unknown
direction: unknown
sample_status: absent
categories: []
templates: ['Template:InfoboxPacketDetail']
---

# Packet:SOEProtocol

## Notices
_none_

## Description
_none_

## Struct
_none_

## Variable Descriptions
_none_

## Notes
- **NOTE:** These functions are seen on very malformed packets. Very rare occurance and the client will usually disconnect. It's inclusion in the documentation is for completion ONLY. SWGEmu will disconnect automatically when reciving a Error Acknowledge, and it will NOT send any, rather just disconnect itself.
- **NOTE:** Because 255 may be done in a few ways, the following way is how we have seen it. (0xFF 0x00 0xFF) or 255 + 0 (do not add the following byte) = 255.
- **NOTE:** This packet is usually compressed but is optional.
- **NOTE:** This packet is usually compressed but is optional.

## Tags
_none_

## Sample Packet
_none_

## Related Pages
_none_

## Other Sections
_none_

## Categories
_none_