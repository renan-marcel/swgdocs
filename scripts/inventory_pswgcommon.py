#!/usr/bin/env python3
"""Build a deterministic lexical inventory; Python standard library only.

This is deliberately not a Java/Kotlin parser, call graph, or protocol verifier.
Run: python scripts/inventory_pswgcommon.py [--source PATH] [--docs PATH]
"""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote


SOURCE_ROOT = "src/main/java/com/projectswg/common/"
GITHUB = "https://github.com/ProjectSWGCore/pswgcommon/blob/"


def git(source, *args):
    return subprocess.check_output(
        ["git", "-C", str(source), *args], encoding="utf-8"
    ).strip()


def mask(text):
    """Return comment-free and comment/string-free views with original offsets.

    Handles escaped quoted strings, Kotlin triple strings and nested block
    comments. Does not implement Kotlin interpolation or a complete lexer.
    """
    comments = list(text)
    code = list(text)
    i = 0
    while i < len(text):
        start = i
        comment = False
        if text.startswith("//", i):
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
            comment = True
        elif text.startswith("/*", i):
            i += 2
            depth = 1
            while i < len(text) and depth:
                if text.startswith("/*", i):
                    depth += 1
                    i += 2
                elif text.startswith("*/", i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            if depth:
                raise ValueError("unterminated block comment")
            comment = True
        elif text.startswith('"""', i):
            end = text.find('"""', i + 3)
            if end < 0:
                raise ValueError("unterminated triple string")
            i = end + 3
        elif text[i] in "\"'":
            delimiter = text[i]
            i += 1
            while i < len(text):
                if text[i] == "\\":
                    i += 2
                elif text[i] == delimiter:
                    i += 1
                    break
                else:
                    i += 1
            else:
                raise ValueError("unterminated quoted literal")
        else:
            i += 1
            continue
        for j in range(start, min(i, len(text))):
            if text[j] not in "\r\n":
                code[j] = " "
                if comment:
                    comments[j] = " "
    return "".join(comments), "".join(code)


def line_at(text, offset):
    return text.count("\n", 0, offset) + 1


def nominal(name):
    """Case/punctuation-insensitive name equality, never opcode validation."""
    return "".join(c for c in name.casefold() if c.isalnum())


def source_info(path, source, commit):
    data = path.read_bytes()
    relative = path.relative_to(source).as_posix()
    entry = {
        "path": relative,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "extension": path.suffix.lower() or "<none>",
        "source_set": relative.split("/")[1] if "/" in relative else None,
        "package": None,
        "top_level_types": [],
        "top_level_type": None,
        "crc_declarations": [],
        "getCrc_literals": [],
        "source_url": GITHUB + commit + "/" + quote(relative, safe="/"),
    }
    if path.suffix.lower() not in {".java", ".kt"}:
        return entry
    text = data.decode("utf-8-sig")
    comments, code = mask(text)
    packages = re.findall(r"(?m)^\s*package\s+([\w.]+)", code)
    if len(packages) > 1:
        raise ValueError(f"multiple package declarations: {relative}")
    entry["package"] = packages[0] if packages else None
    pattern = r"\b(enum(?:\s+class)?|class|interface|object|record)\s+([A-Za-z_$][\w$]*)"
    for match in re.finditer(pattern, code):
        prefix = code[:match.start()]
        if prefix.count("{") != prefix.count("}"):
            continue
        # Java .class literals and Kotlin object expressions do not match names.
        entry["top_level_types"].append({
            "kind": match[1], "name": match[2],
            "line": line_at(text, match.start()),
        })
    if len(entry["top_level_types"]) == 1:
        entry["top_level_type"] = entry["top_level_types"][0]
    # Extract declarations, not arbitrary calls in comments or string contents.
    for match in re.finditer(r"\b(?:int|long|val|var)\s+(?:CRC|crc)\b\s*(?::[^=\r\n]+)?\s*=(?!=)\s*([^;\r\n]+)", comments):
        if not code[match.start():match.start() + 3].strip():
            continue
        expression = match[1].strip()
        literal = re.fullmatch(r"(-?(?:0[xX][0-9a-fA-F_]+|\d[\d_]*))[lL]?", expression)
        entry["crc_declarations"].append({
            "line": line_at(text, match.start()),
            "expression": expression,
            "numeric_literal": literal[1] if literal else None,
            "getCrc_literal": None,
        })
    for match in re.finditer(r'\bgetCrc\s*\(\s*"([^"\\]*)"\s*\)', comments):
        if not code[match.start():match.start() + 6].strip():
            continue
        item = {"name": match[1], "line": line_at(text, match.start())}
        entry["getCrc_literals"].append(item)
        for declaration in entry["crc_declarations"]:
            if declaration["line"] == item["line"]:
                declaration["getCrc_literal"] = item["name"]
    return entry


def protocol_pages(docs):
    pages = []
    for path in sorted((docs / "content/protocols").rglob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        titles = []
        if text.startswith("---\n"):
            frontmatter = text.split("---", 2)[1]
            titles = re.findall(r"(?m)^title:\s*(.*?)\s*$", frontmatter)
            if len(titles) > 1:
                raise ValueError(f"multiple title fields: {path}")
        title = titles[0].strip("\"'") if titles else path.stem
        pages.append({"path": path.relative_to(docs).as_posix(),
                      "title": title, "names": sorted({title, path.stem})})
    return pages


def markdown_escape(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(inventory):
    counts = inventory["counts"]
    lines = [
        "---", 'title: "PSWGCommon: catálogo lexical das fontes"',
        "section: guides", 'category: "PSWGCommon"',
        "slug: pswgcommon-catalog", "layout: guide", "---", "",
        "# PSWGCommon: catálogo lexical das fontes", "",
        "Gerado por `scripts/inventory_pswgcommon.py`, usando apenas a biblioteca padrão do Python. "
        "O [inventário JSON](../../data/pswgcommon-inventory.json) contém todos os arquivos sob `src`, "
        "SHA-256, tamanho, pacote, tipos reconhecidos, referências de CRC e vínculos nominais.", "",
        f"Revisão de referência: `{inventory['source_revision']}`. "
        f"Arquivos: **{counts['files']}**; Java/Kotlin: **{counts['code_files']}**; "
        f"arquivos sob `src/test`: **{counts['test_files']}**; "
        f"candidatos em `network/packets`: **{counts['packet_candidates']}**.", "",
        "## Escopo e limites", "",
        "A cobertura é lexical: expressões regulares com comentários e strings mascarados, "
        "sem AST, resolução de herança, call graph, execução, decompilação ou comparação de payloads. "
        "A lista de candidatos inclui classes auxiliares no diretório de packets. "
        "Os tipos de topo são reconhecidos apenas quando a declaração tem forma simples; "
        "funções Kotlin, aliases e estruturas complexas podem não receber um tipo identificado. "
        "Valores de CRC são literais extraídos, não calculados. Arquivos não Java/Kotlin recebem hash, "
        "mas não análise de declarações.", "",
        "A associação com `content/protocols` compara o nome da classe/arquivo e os argumentos "
        "literais de `getCrc` com o título ou nome do arquivo Markdown, ignorando caixa e pontuação. "
        "Ela não verifica opcode, direção, versão, campos ou compatibilidade. Todas as correspondências "
        "são candidatas; múltiplas páginas ou arquivos com o mesmo nome são mantidos e expostos "
        "como ambiguidades no JSON, sem escolher uma silenciosamente.", "",
        "Os links GitHub fixam a revisão Git. Os hashes descrevem os bytes locais; alterações locais "
        "ou arquivos não rastreados podem divergir dessa revisão. O JSON registra o estado Git de `src`.", "",
        "Para regenerar, execute `python scripts/inventory_pswgcommon.py` na raiz de `swgdocs`. "
        "Use `--source` e `--docs` para outras localizações. Não há timestamps na saída.", "",
        "## Contagens", "", "| Extensão | Arquivos |", "| --- | ---: |",
    ]
    for extension, total in counts["by_extension"].items():
        lines.append(f"| `{extension}` | {total} |")
    lines += ["", "| Conjunto de fontes | Arquivos |", "| --- | ---: |"]
    for source_set, total in counts["by_source_set"].items():
        lines.append(f"| `{source_set}` | {total} |")
    lines += ["", "## Pacotes", "", "| Pacote | Arquivos Java/Kotlin |", "| --- | ---: |"]
    for package, total in counts["by_package"].items():
        lines.append(f"| `{package}` | {total} |")
    lines += ["", "## Candidatos a packets e correspondências nominais", "",
              "CRC ausente significa que não foi extraída uma declaração simples nesse arquivo. "
              "Chamadas `getCrc` também podem pertencer a auxiliares ou seletores internos.", "",
              "| Fonte | CRC / argumento literal de getCrc | Páginas candidatas |", "| --- | --- | --- |"]
    for packet in inventory["packets"]:
        source = packet["path"]
        label = source.removeprefix(SOURCE_ROOT + "network/packets/")
        references = []
        for crc in packet["crc_declarations"]:
            references.append(f"`{markdown_escape(crc['expression'])}` (L{crc['line']})")
        for call in packet["getCrc_literals"]:
            if not any(crc["getCrc_literal"] == call["name"] for crc in packet["crc_declarations"]):
                references.append(f"`getCrc(\"{markdown_escape(call['name'])}\")` (L{call['line']})")
        links = [f"[{markdown_escape(p['title'])}]({quote('../protocols/' + p['path'].split('content/protocols/', 1)[1], safe='/')})"
                 for p in packet["protocol_candidates"]]
        lines.append(f"| [{markdown_escape(label)}]({packet['source_url']}) | "
                     f"{'<br>'.join(references) or '—'} | {'<br>'.join(links) or 'Sem correspondência nominal'} |")
    lines += ["", "## Ambiguidades explícitas", "",
              f"Grupos de nomes de fontes duplicados: **{len(inventory['ambiguities']['source_names'])}**; "
              f"nomes associados a múltiplas páginas: **{len(inventory['ambiguities']['protocol_names'])}**; "
              f"arquivos com múltiplos tipos de topo reconhecidos: **{len(inventory['ambiguities']['multiple_top_level_types'])}**; "
              f"tipos de topo com nome qualificado repetido: **{len(inventory['ambiguities']['qualified_type_names'])}**.", "",
              "Consulte `ambiguities` no JSON para os caminhos completos. Um candidato sem página "
              "não prova ausência de documentação: nomes alternativos e páginas agregadas podem "
              "não ser reconhecidos por este método.", ""]
    return "\n".join(lines)


def build(source, docs):
    if not (source / "src").is_dir() or not (docs / "content/protocols").is_dir():
        raise ValueError("source/src and docs/content/protocols must exist")
    commit = git(source, "rev-parse", "HEAD")
    if not re.fullmatch(r"[0-9a-f]{40,64}", commit):
        raise ValueError("invalid Git revision")
    files = sorted(p for p in (source / "src").rglob("*") if p.is_file())
    folded_paths = defaultdict(list)
    for path in files:
        if path.is_symlink():
            raise ValueError(f"symlink requires explicit handling: {path}")
        folded_paths[path.relative_to(source).as_posix().casefold()].append(str(path))
    collisions = [paths for paths in folded_paths.values() if len(paths) > 1]
    if collisions:
        raise ValueError(f"case-insensitive path collisions: {collisions}")
    entries = [source_info(path, source, commit) for path in files]
    pages = protocol_pages(docs)
    page_names = defaultdict(dict)
    for page in pages:
        for name in page["names"]:
            page_names[nominal(name)][page["path"]] = page
    source_names = defaultdict(set)
    packets = []
    for entry in entries:
        if "/network/packets/" not in entry["path"] or entry["extension"] not in {".java", ".kt"}:
            continue
        names = {Path(entry["path"]).stem}
        names.update(t["name"] for t in entry["top_level_types"])
        names.update(call["name"] for call in entry["getCrc_literals"])
        candidates = {}
        for name in sorted(names):
            source_names[nominal(name)].add(entry["path"])
            candidates.update(page_names.get(nominal(name), {}))
        packets.append({**entry, "nominal_names": sorted(names),
                        "protocol_candidates": [candidates[p] for p in sorted(candidates)],
                        "match_status": "nominal_candidate_only"})
    code = [e for e in entries if e["extension"] in {".java", ".kt"}]
    qualified_types = defaultdict(list)
    for entry in code:
        for declaration in entry["top_level_types"]:
            qualified_name = ".".join(filter(None, [entry["package"], declaration["name"]]))
            qualified_types[qualified_name].append({"path": entry["path"], "line": declaration["line"]})
    inventory = {
        "schema_version": 1,
        "method": "lexical_only_no_ast_no_callgraph_no_protocol_verification",
        "source_repository": "https://github.com/ProjectSWGCore/pswgcommon",
        "source_revision": commit,
        "source_worktree_status": git(source, "status", "--porcelain=v1", "--untracked-files=all", "--", "src").splitlines(),
        "counts": {
            "files": len(entries), "code_files": len(code),
            "test_files": sum(e["source_set"] == "test" for e in entries),
            "packet_candidates": len(packets), "protocol_pages": len(pages),
            "packets_with_nominal_candidates": sum(bool(p["protocol_candidates"]) for p in packets),
            "by_extension": dict(sorted(Counter(e["extension"] for e in entries).items())),
            "by_source_set": dict(sorted(Counter(e["source_set"] for e in entries).items())),
            "by_package": dict(sorted(Counter(e["package"] or "<none>" for e in code).items())),
        },
        "ambiguities": {
            "source_names": {k: sorted(v) for k, v in sorted(source_names.items()) if len(v) > 1},
            "protocol_names": {k: sorted(v) for k, v in sorted(page_names.items()) if len(v) > 1},
            "multiple_top_level_types": [e["path"] for e in entries if len(e["top_level_types"]) > 1],
            "qualified_type_names": {k: v for k, v in sorted(qualified_types.items()) if len(v) > 1},
            "unresolved_crc_expressions": [{"path": e["path"], **crc} for e in entries
                                           for crc in e["crc_declarations"]
                                           if crc["numeric_literal"] is None and crc["getCrc_literal"] is None],
        },
        "files": entries, "packets": packets,
    }
    return inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_docs = Path(__file__).resolve().parent.parent
    parser.add_argument("--source", type=Path, default=default_docs.parent / "pswgcommon")
    parser.add_argument("--docs", type=Path, default=default_docs)
    args = parser.parse_args()
    try:
        inventory = build(args.source.resolve(), args.docs.resolve())
        json_path = args.docs / "data/pswgcommon-inventory.json"
        markdown_path = args.docs / "content/guides/pswgcommon-catalog.md"
        json_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        markdown_path.write_text(render(inventory), encoding="utf-8", newline="\n")
        print(json.dumps(inventory["counts"], ensure_ascii=False, indent=2))
    except (OSError, ValueError, UnicodeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"inventory failed: {error}\n")


if __name__ == "__main__":
    main()
