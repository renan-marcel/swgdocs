---
title: Binary & Hex
url: https://wiki.swganh.org/index.php/Binary_%26_Hex
page_type: Other
opcode: 
revision_id: 44447
last_modified: 2008-08-28T15:18:43Z
completion: unknown
direction: unknown
sample_status: present
categories: []
templates: ['Template:En', 'Template:Bool', 'Template:Sbyte', 'Template:Byte', 'Template:Short', 'Template:Ushort', 'Template:Int', 'Template:Uint', 'Template:Float', 'Template:Long', 'Template:Ulong', 'Template:Double', 'Template:A string', 'Template:U string']
---

# Binary & Hex

## Notices
_none_

## Description
_none_

## Struct
| Type | Name |
| --- | --- |
| bytes amount | type |
| 1 | integer |
| 1 | integer |
| 1 | integer |
| 2 | integer |
| 2 | integer |
| 2 | char |
| 4 | integer |
| 4 | integer |
| 4 | real |
| 8 | integer |
| 8 | integer |
| 8 | real |
| n | char |
| 2n | char |

## Variable Descriptions
_none_

## Notes
- **NOTE:** In C++, the long types have a size that varies upon operating system and processor. It has the size of all pointers (void*, int*, ...). If an environment has a 32bits RAM indexation (4GB max) then the longs will be 4 bytes. If the environment has a 64 bits RAM indexation, the longs will be 8 bytes.
- **NOTE:** also known as NETWORK BYTE ORDER, it's the standard used for IP communications as defined by the OSI model link layer. Though it does not mean all protocols respect the standard! It's used by: Sun Solaris (SPARC), HP-UX, (Motorola 68000), IBM System/370, ...
- **NOTE:** also known as HOST BYTE ORDER. It's used by: SCO Unix, DEC Unix (Digital), Microsoft Windows, ...

## Tags
_none_

## Sample Packet
```
_  _  _  _  _ _ _ _
128 64 32 16 8 4 2 1
```

## Related Pages
_none_

## Other Sections
_none_

## Categories
_none_