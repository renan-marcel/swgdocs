---
title: Packet Guide
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet_Guide
wiki_revid: 3767
layout: guide
date_audited: 2026-10-17
---

# Packet Guide

## Packet Structure

Each Page should have a STRUCT section, which gives the variable type and a variable name if known.

## Variable Types

<div class="table-wrap"><table class="wikitable doc-table">
<tr>
<th>Render</th>
<th>Keyword</th>
<th>Type Details
</th></tr>
<tr>
<td align="center" style="background:#4169E1; color:white;" width="80px"><b>BOOL</b>
</td>
<td>bool</td>
<td><b>bool</b> (1byte, 0:false, other value:true)
</td></tr>
<tr>
<td align="center" style="background:#B3C0DE; color:white;" width="80px"><b>SBYTE</b>
</td>
<td>sbyte</td>
<td><b>sbyte</b> (1byte, signed)
</td></tr>
<tr>
<td align="center" style="background:#B3C0DE; color:white;" width="80px"><b>BYTE</b>
</td>
<td>byte</td>
<td><b>byte</b> (1byte, unsigned)
</td></tr>
<tr>
<td align="center" style="background:#6C86BF; color:white;" width="80px"><b>SHORT</b>
</td>
<td>short</td>
<td><b>short</b> (2bytes, signed)
</td></tr>
<tr>
<td align="center" style="background:#6C86BF; color:white;" width="80px"><b>USHORT</b>
</td>
<td>ushort</td>
<td><b>ushort</b> (2bytes, unsigned)
</td></tr>
<tr>
<td align="center" style="background:#3C548A; color:white;" width="80px"><b>INT</b>
</td>
<td>int</td>
<td><b>int</b> (4bytes, signed)
</td></tr>
<tr>
<td align="center" style="background:#3C548A; color:white;" width="80px"><b>UINT</b>
</td>
<td>uint</td>
<td><b>uint</b> (4bytes, unsigned)
</td></tr>
<tr>
<td align="center" style="background:#3C5466; color:white;" width="80px"><b>FLOAT</b>
</td>
<td>float</td>
<td><b>float</b> (4bytes, signed)
</td></tr>
<tr>
<td align="center" style="background:#3C4565; color:white;" width="80px"><b>LONG</b>
</td>
<td>long</td>
<td><b>long</b> (8bytes, signed, mostly used for object ids)
</td></tr>
<tr>
<td align="center" style="background:#3C4565; color:white;" width="80px"><b>ULONG</b>
</td>
<td>ulong</td>
<td><b>ulong</b> (8bytes, unsigned, mostly used for object ids)
</td></tr>
<tr>
<td align="center" style="background:#465945; color:white;" width="80px"><b>DOUBLE</b>
</td>
<td>double</td>
<td><b>double</b> (8bytes, signed)
</td></tr>
<tr>
<td align="center" style="background:#D8F2E0; color:#3C4565;" width="80px"><b>A_STRING</b>
</td>
<td>a_string</td>
<td><b>ANSI/ASCII String</b> (2 -packets- or 4 -files- bytes size + 1byte chars, ASCII:leading0+7bits, ANSI:8bits)
</td></tr>
<tr>
<td align="center" style="background:#8BD9A3; color:white;" width="80px"><b>U_STRING</b>
</td>
<td>u_string</td>
<td><b>Unicode String</b> (4bytes size + 2bytes chars)
</td></tr>
<tr>
<td align="center" style="background:#3EC166; color:white;" width="80px"><b>C_STRING</b>
</td>
<td>c_string</td>
<td><b>Customization String</b> (<a href="https://wiki.swganh.org/index.php/Character%20Appearance%20%28Sequence%29#Xeno TRAC Docs" rel="noopener" target="_blank" title="Character Appearance (Sequence)">look here for details</a>)
</td></tr>
<tr>
<td align="center" style="background:#25733D; color:white;" width="80px"><b>B_STRING</b>
</td>
<td>b_string</td>
<td><b>Byte String</b> (4bytes size + 1byte chars, used for session key only)
</td></tr>
<tr>
<td align="center" style="background:#C6C600; color:white;" width="80px"><b>{ }</b>
</td>
<td>list</td>
<td><b>LIST Component</b> (this is a sub section repeated as a list of data. Indent Variable types with 1 space.)
</td></tr>
<tr>
<td align="center" style="background:#DF97A7; color:white;"><b>?</b>
</td>
<td>uncertain</td>
<td><b>Uncertain Values</b> (use a single question mark ? in the name to display uncertainty in the variables understanding.)
</td></tr>
<tr>
<td align="center" style="background:#C84966; color:white;"><b>??</b>
</td>
<td>unknown</td>
<td><b>Unknown Variable Name</b> (use ?? or Unknown for the name to display that there is no clue as to what the data does.)
</td></tr>
</table></div>

XML style list tags sample: (use as many ":" as needed to multi-indent)

```text

{% raw %}{{{% endraw %}beginlist|myitems|mycount{% raw %}}}{% endraw %}
:{| class="wikitable"
|}
{% raw %}{{{% endraw %}endlist|myitems{% raw %}}}{% endraw %}

```

<myitems count=mycount >

<myitems/>

## Additional Guidelines

In Addition, each page should contain a section for Variable Descriptions should be made. This should include a brief, or detailed description as needed to document what the variable does and how it can be used. Also the Opperand_Count and Opcode should be listed with it.

Finally an Additional Info section should be provided to give more info in the case it is needed for that packet.

```text

= STRUCT =
{% raw %}{{{% endraw %}{
SHORT:		VarName
SHORT:		16bitVariable
INT:		32bitVariable
INT:		LookAList
{
 LONG:		64bitVariable
 BYTE:		8bitVariable
 BYTE:		??
}
A_STRING:	AsciiString
U_STRING:	UnicodeString
C_STRING:	CustomizationString
{% raw %}}}{% endraw %}}
----
= Variable Description =
{% raw %}{{{% endraw %}{
OpperandCount	= 9
Opcode		= FFFFFFFF

AsciiString:
This variable is a string for the name.

64bitVariable:
This variable is an ID for that guy.

8bitVariable:
This byte is a flag for stuff.
{% raw %}}}{% endraw %}}
----
= Notes =
{% raw %}{{{% endraw %}{
Anything Additional Goes here.
{% raw %}}}{% endraw %}}

```

NewPP limit report
Cached time: 20261017110508
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.059 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 70/1000000
Preprocessor generated node count: 257/1000000
Post‐expand include size: 4686/2097152 bytes
Template argument size: 21/2097152 bytes
Highest expansion depth: 3/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%   48.024      1 - -total
100.00%   48.024      1 - Template:Field_types
  4.84%    2.325      1 - Template:Beginlist
  4.40%    2.111      1 - Template:Bool
  4.24%    2.034      1 - Template:Endlist
  4.04%    1.939      1 - Template:Sbyte
  4.00%    1.922      1 - Template:Short
  3.84%    1.842      1 - Template:Unknown
  3.81%    1.828      1 - Template:Byte
  3.80%    1.826      1 - Template:Long

Saved in parser cache with key swganh_wiki:pcache:idhash:1629-0!*!0!!*!*!* and timestamp 20261017110508 and revision id 3767
