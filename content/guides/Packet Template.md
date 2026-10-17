---
title: Packet Template
section: guides
wiki_url: https://wiki.swganh.org/index.php/Packet_Template
wiki_revid: 3773
layout: guide
date_audited: 2026-10-17
---

# Packet Template

<div class="table-wrap"><table class="doc-table">
<tr align="center">
<td>
<div class="table-wrap"><table align="center" class="expansion doc-table" style="background: #E2EBF5; border: 2px solid #000; padding: .2em; margin-bottom: 3px; font-size: 95%;" width="85%">
<tr>
<td style="padding-right: 4px; padding-left: 4px;"> <a class="image" href="https://wiki.swganh.org/index.php/File%3AExquisite-khelpcenter.png" rel="noopener" target="_blank"><img alt="Exquisite-khelpcenter.png" height="75" src="../assets/images/Exquisite-khelpcenter.png" srcset="/images/thumb/8/89/Exquisite-khelpcenter.png/113px-Exquisite-khelpcenter.png 1.5x, /images/8/89/Exquisite-khelpcenter.png 2x" style="max-width: 64px; vertical-align: middle; margin-right: 8px;" width="75"/></a>
</td>
<td> <font size="3"><b>Instructions</b></font><br/><small>In order to keep all documentation the same format, please use the source to this page to begin a new packet description, the template contains all the options, simply remove what is not required and fill in the details.</small>
</td></tr></table></div>
<p><br/>
</p>
</td></tr>
</table></div>

<div class="table-wrap"><table border="0" cellpadding="6" class="doc-table" width="90%">
<tr>
<td valign="top">
<h3 id="struct"><span class="mw-headline" id="Struct">Struct</span></h3>
<hr/>
<div class="table-wrap"><table class="wikitable doc-table">
<tr>
<td align="center" style="background:#3C548A; color:white;" width="80px"><b>INT</b>
</td>
<td>description of the int value
</td></tr>
<tr>
<td align="center" style="background:#6C86BF; color:white;" width="80px"><b>USHORT</b>
</td>
<td>description of the ushort value
</td></tr>
<tr>
<td align="center" style="background:#3C5466; color:white;" width="80px"><b>FLOAT</b>
</td>
<td>description of the float value
</td></tr>
<tr>
<td align="center" style="background:#8BD9A3; color:white;" width="80px"><b>U_STRING</b>
</td>
<td>description of the u_string value
</td></tr>
<tr>
<td>...</td>
<td>...
</td></tr></table></div>
<p><a class="external text" href="http://wiki2.swganh.org/index.php/Category:Field_Type" rel="nofollow">Look here for all available types</a>
</p>
<h3 id="variable-descriptions"><span class="mw-headline" id="Variable_Descriptions">Variable Descriptions</span></h3>
<hr/>
<p>Opperand_Count	     = <b>9</b>
</p><p>Opcode		     = <b>FFFFFFFF</b>
</p>
<hr/>
<ul><li> Additional Descriptions go here...</li>
<li> --</li>
<li> ---</li>
<li> ----</li></ul>
</td>
<td valign="top">
<h3 id="tags"><span class="mw-headline" id="Tags">Tags</span></h3>
<hr/>
<div class="table-wrap"><table align="center" class="doc-table">
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #dddddd; text-align: center; font-size: 14pt; color: #000000;"> <b>S→C</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet originates on the server.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #dddddd; text-align: center; font-size: 14pt; color: #000000;"> <b>C→S</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet originates on the client.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #336600; text-align: center; font-size: 14pt; color: #FFFFFF;"> <b>100%</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet has been completely reversed.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #669933; text-align: center; font-size: 14pt; color: #FFFFFF;"> <b>75%</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet has been partially reversed.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #99CC66; text-align: center; font-size: 14pt; color: #FFFFFF;"> <b>50%</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet has been partially reversed.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #CCFF99; text-align: center; font-size: 14pt; color: #000000;"> <b>25%</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet has been partially reversed.
</td></tr></table></div></div><br clear="all"/>
</td></tr>
<tr>
<td><div style="float: left; border:solid #dddddd 1px; margin: 1px;">
<div class="table-wrap"><table cellspacing="0" class="doc-table" style="width: 238px; background: #ffffff;">
<tr>
<td style="width: 45px; height: 45px; background: #FF6666; text-align: center; font-size: 14pt; color: #000000;"> <b>0%</b>
</td>
<td style="font-size: 8pt; padding: 4pt; line-height: 1.25em; color: black;"> This packet has not been reversed.
</td></tr></table></div></div>
</td></tr>
</table></div>
</td></tr></table></div>

## Sample Code

```text

Insert Code Snippet Here...

```

## Sample Packet

```text

Insert Sample Packet Here...

```

NewPP limit report
Cached time: 20261017165631
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.095 seconds
Real time usage: 0.109 seconds
Preprocessor visited node count: 95/1000000
Preprocessor generated node count: 236/1000000
Post‐expand include size: 4014/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100

Transclusion expansion time report (%,ms,calls,template)
100.00%   26.372      1 - -total
  8.49%    2.239      1 - Template:50%
  7.83%    2.064      1 - Template:PacketGuide
  7.36%    1.941      1 - Template:ServerPacket
  7.31%    1.927      1 - Template:100%
  7.26%    1.914      1 - Template:75%
  7.23%    1.907      1 - Template:ClientPacket
  7.12%    1.877      1 - Template:0%
  7.05%    1.860      1 - Template:25%
  6.70%    1.766      1 - Template:Int

Saved in parser cache with key swganh_wiki:pcache:idhash:1630-0!*!*!!*!5!* and timestamp 20261017165631 and revision id 3773
