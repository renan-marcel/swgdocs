"""Apply the bounded PSWGCommon/client message cross-check after site generation.

Only the three named protocol pages and their CSV/summary entries are changed.
Run from any directory; repeated runs produce the same bytes.
"""
from pathlib import Path
import csv
import html
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- pswgcommon-message-crosscheck:start -->"
END = "<!-- pswgcommon-message-crosscheck:end -->"
EVIDENCE = "../data/pswgcommon-evidence/messages-01/"
MESSAGES = {
    "UpdateContainmentMessage": {
        "completion": "100%",
        "text": [
            "PSWGCommon encodes 26 bytes: operand count 4 at offset 0, opcode 56CBDE9E at 2, objectId (8 bytes) at 6, containerId (8 bytes) at 14, and slotIndex (4 bytes) at 22. Offsets start at the SWG message and exclude SOE framing; integers are little-endian.",
            "The client reader at 0x00ADC6D0 registers two NetworkId fields and one int in that order (object members +0x38, +0x48, +0x58). These are in-memory offsets, not packet offsets. This corroborates the field sequence; arrangement/slot semantics and special values are not established by the registration alone.",
        ],
        "evidence": ["CONTAIN-READ"],
        "notes": {"3": "Wire offset 6; objectId; 8 bytes", "4": "Wire offset 14; containerId; 8 bytes", "5": "Wire offset 22; PSWGCommon slotIndex; semantics not fully established by field registration"},
        "keywords": "Operand_Count Opcode ObjectID Parent Id Arrangement Id containerId slotIndex PSWGCommon client cross-check",
    },
    "SceneCreateObjectByCrc": {
        "completion": "75%",
        "text": [
            "PSWGCommon encodes 47 bytes: operand count 5 at offset 0, opcode FE89DDEA at 2, object ID at 6, quaternion float32 x/y/z/w at 14/18/22/26, position float32 x/y/z at 30/34/38, object CRC at 42, and ByteFlag at 46. Offsets exclude SOE framing; numeric fields are little-endian.",
            "The client reader at 0x00AD51B0 registers NetworkId, Transform, uint32 and bool (object members +0x38, +0x48, +0x7C, +0x84). Transform pack/unpack at 0x005200C0/0x005201A0 uses seven float32 values in quaternion x/y/z/w then position x/y/z order (28 bytes), converting between quaternion and the internal matrix. Internal member offsets are not wire offsets.",
            "PSWGCommon Location transmits orientation and position only, not terrain. Its doubles are narrowed to float32. PSWGCommon names ByteFlag hyperspace and emits 0/1; the full gameplay meaning of the client's bool remains only partially established, so the historical 75% completion is retained.",
        ],
        "evidence": ["SCENE-READ", "TRANSFORM-PACK", "TRANSFORM-UNPACK"],
        "notes": {"11": "Wire offset 42; uint32 template CRC", "12": "Wire offset 46; client bool; PSWGCommon hyperspace; full semantics remain partial"},
        "keywords": "Operand_Count Opcode ObjectID QuaternionX QuaternionY QuaternionZ QuaternionW X-Coordinate Y-Coordinate Z-Coordinate ObjectCRC ByteFlag Transform hyperspace PSWGCommon client cross-check",
    },
    "ChatInstantMessageToClient": {
        "completion": "100%",
        "text": [
            "The final field is a second U_STRING, named outOfBand in PSWGCommon. Its int32 prefix counts UTF-16 code units and is followed by twice that many bytes in UTF-16LE. The historical sample's trailing 00 00 00 00 is this empty string's length prefix; the sample remains unchanged. It does not establish that the field must always be zero.",
            "The client reader at 0x00AF2610 registers ChatAvatarId and two Unicode strings (object members +0x38, +0x60, +0x70). These are in-memory offsets. The avatar decoder preserves the three narrow strings Game ID, Galaxy Name and Playername; Unicode unpack at 0x011948B0 reads int32 length followed by 2*length bytes.",
            "Header discrepancy: native archive pack at 0x0118B6F0 derives operand count from the registered-field vector: opcode plus three registered fields gives 4, matching the historical sample. PSWGCommon ChatInstantMessageToClient.encode() writes 2. Native unpack at 0x0118B740 consumes the short without checking its value; PSWGCommon checkDecode also discards it. This documents the implementation difference without changing the library or replacing the historical sample.",
            "With G/C the byte lengths of Galaxy Name/Playername and M/O the UTF-16 code-unit lengths of Message/OutOfBand: the message is 23+G+C+2*M+2*O bytes. Game ID starts at 6 (2-byte length plus SWG); Galaxy Name at 11; Playername at 13+G; Message at 15+G+C; OutOfBand at 19+G+C+2*M. Each offset identifies its length prefix. Offsets exclude SOE framing; lengths and opcode are little-endian.",
            "PSWGCommon's A_STRING helper uses UTF-8 byte lengths, although this packet allocates space using Java String.length() for galaxy and character. Non-ASCII names can therefore exceed the allocated buffer. This is a library allocation limitation, not evidence that the native client uses UTF-8 for all narrow strings.",
        ],
        "evidence": ["CHAT-READ", "ARCHIVE-PACK", "ARCHIVE-UNPACK", "AVATAR-UNPACK", "UNICODE-UNPACK"],
        "notes": {"1": "Native writer/sample: 4; PSWGCommon encoder: 2; readers consume without validating", "7": "int32 UTF-16 code-unit count followed by 2*count bytes; historical sample is empty"},
        "keywords": "Opperand_Count Opcode Game ID Galaxy Name Playername Message OutOfBand U_STRING PSWGCommon client operand count discrepancy",
    },
}


def write_if_changed(path, value):
    if path.read_text(encoding="utf-8") != value:
        path.write_text(value, encoding="utf-8", newline="\n")


def remove_block(text):
    return re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*", "", text, flags=re.S)


def update_pages(name, spec):
    md_path = ROOT / "content/protocols" / (name + ".md")
    md = remove_block(md_path.read_text(encoding="utf-8"))
    assert f"completion: {spec['completion']}" in md
    md = md.replace("## Notes\n_none_\n\n", "## Notes\n\n", 1)
    if name == "ChatInstantMessageToClient":
        md = md.replace("| INT | 0 |", "| U_STRING | OutOfBand |")
        assert "| U_STRING | OutOfBand |" in md
    md_block = BEGIN + "\n### PSWGCommon / client cross-check\n\n"
    md_block += "\n\n".join(spec["text"])
    md_block += "\n\nSee [client message analysis](../guides/pswgcommon-client-messages.md). Evidence: "
    md_block += ", ".join(f"[BN-PSWG-{e}](../{EVIDENCE}BN-PSWG-{e}.json)" for e in spec["evidence"])
    md_block += ".\n" + END + "\n\n"
    assert md.count("## Tags") == 1
    md = md.replace("## Tags", md_block + "## Tags", 1)
    write_if_changed(md_path, md)

    page_path = ROOT / "protocols" / (name + ".html")
    page = remove_block(page_path.read_text(encoding="utf-8"))
    if name == "ChatInstantMessageToClient":
        pattern = r'(<td><span class="type-pill">)INT(</span></td>\s*<td style="font-weight:600;">)0(</td>\s*<td style="color:var\(--text-muted\); font-size:0.8rem;">)(.*?)(</td>)'
        page = re.sub(pattern, lambda m: m[1]+"U_STRING"+m[2]+"OutOfBand"+m[3]+html.escape(spec["notes"]["7"])+m[5], page, count=1, flags=re.S)
        assert '<span class="type-pill">U_STRING</span></td>\n              <td style="font-weight:600;">OutOfBand' in page
    section = BEGIN + '\n<section class="doc-section">\n<h2>PSWGCommon / client cross-check</h2>\n'
    section += "\n".join("<p>"+html.escape(p)+"</p>" for p in spec["text"])
    section += '\n<p>See <a href="../guides/pswgcommon-client-messages.html">client message analysis</a>. Evidence: '
    section += ", ".join(f'<a href="{EVIDENCE}BN-PSWG-{e}.json">BN-PSWG-{e}</a>' for e in spec["evidence"])
    section += ".</p>\n</section>\n" + END + "\n"
    # The sample's section is a stable insertion anchor; preserve all sample bytes.
    anchor = re.search(r'<section class="doc-section">\s*<h2>📦 Sample Hex Dump / Packet Payload</h2>', page)
    assert anchor, name
    page = page[:anchor.start()] + section + page[anchor.start():]
    write_if_changed(page_path, page)


def main():
    for name, spec in MESSAGES.items():
        update_pages(name, spec)
    csv_path = ROOT / "data/all_packets.csv"
    lines = csv_path.read_text(encoding="utf-8").splitlines(keepends=True)
    fields = next(csv.reader([lines[0]]))
    seen = set()
    for i, line in enumerate(lines[1:], 1):
        if not any(line.startswith(name + ",") for name in MESSAGES):
            continue
        row = dict(zip(fields, next(csv.reader([line]))))
        if row["page"] not in MESSAGES:
            continue
        spec = MESSAGES[row["page"]]
        assert row["completion"] == spec["completion"]
        if row["order"] not in spec["notes"]:
            continue
        row["notes"] = spec["notes"][row["order"]]
        if row["page"] == "ChatInstantMessageToClient" and row["order"] == "7":
            assert (row["type"], row["name"]) in [("INT", "0"), ("U_STRING", "OutOfBand")]
            row["type"], row["name"] = "U_STRING", "OutOfBand"
        output = io.StringIO(newline="")
        csv.writer(output, lineterminator="\n").writerow([row[f] for f in fields])
        lines[i] = output.getvalue()
        seen.add((row["page"], row["order"]))
    assert len(seen) == sum(len(s["notes"]) for s in MESSAGES.values())
    write_if_changed(csv_path, "".join(lines))
    summary_path = ROOT / "data/packets_summary.json"
    summary = summary_path.read_text(encoding="utf-8")
    for name, spec in MESSAGES.items():
        pattern = r'\{\s*"t": ' + re.escape(json.dumps(name)) + r',.*?\n  \}'
        matches = list(re.finditer(pattern, summary, re.S))
        assert len(matches) == 1, name
        match = matches[0]
        record = json.loads(match[0])
        assert record["s"] == "protocols" and record["c"] == spec["completion"]
        block, n = re.subn(r'"k": "[^"\n]*"', '"k": '+json.dumps(spec["keywords"]), match[0])
        assert n == 1
        summary = summary[:match.start()] + block + summary[match.end():]
    json.loads(summary)
    write_if_changed(summary_path, summary)
    print("Applied cross-check to 3 HTML/Markdown protocol pairs and targeted CSV/summary entries.")


if __name__ == "__main__":
    main()
