---
title: TRE STFFileType
url: https://wiki.swganh.org/index.php/TRE_STFFileType
page_type: Other
opcode: 
revision_id: 3874
last_modified: 2007-03-22T13:58:29Z
completion: unknown
direction: unknown
sample_status: absent
categories: []
templates: ['Template:Box TREformats', 'Template:Int', 'Template:Byte', 'Template:Beginlist', 'Template:U string', 'Template:Endlist', 'Template:A string']
---

# TRE STFFileType

## Notices
_none_

## Description
_none_

## Struct
| Type | Name |
| --- | --- |
| INT | STF file type header id (sequence: 0xCD 0xAB 0x00 0x00, value: 0x0000ABCD = 43981) |
| BYTE | useless? flag (might be a boolean, seen so far: 0x01 and 0x00) |
| INT | next free index in file to add an item, always > items count (useless for us) |
| INT | items count |

## Variable Descriptions
_none_

## Notes
_none_

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