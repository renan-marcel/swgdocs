"""Render Holocore guides and add their links to the existing guide indexes."""
from pathlib import Path
import html
import json
import re

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ["holocore-overview", "holocore-flows", "holocore-network", "holocore-services", "holocore-clientdata"]
START = "<!-- holocore-guides:start -->"
END = "<!-- holocore-guides:end -->"
SUMMARIES = {
    "holocore-overview": "Mapa funcional, estrutura do repositório, inicialização e limites.",
    "holocore-flows": "Fluxos de inicialização, login, zone-in, awareness, rede e persistência.",
    "holocore-network": "Transporte TCP/WebSocket, handshake, CRC e comparação estática com Binary Ninja.",
    "holocore-services": "Managers, intents, gameplay, objetos, login, chat e persistência.",
    "holocore-clientdata": "Conversores de clientdata, arquivos SDB/IFF e loaders runtime.",
}
REVISION = "ff53903"


def write(path, value):
    if not path.exists() or path.read_text(encoding="utf-8") != value:
        path.write_text(value, encoding="utf-8")


def inject(path, block):
    text = path.read_text(encoding="utf-8")
    fragment = START + "\n" + block + "\n" + END
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: fragment, text, count=1, flags=re.S)
    else:
        assert "<footer>" in text
        text = text.replace("<footer>", fragment + "\n<footer>", 1)
    write(path, text)


def build():
    titles, docs = {}, {}
    for slug in SLUGS:
        raw = (ROOT / "content/guides" / f"{slug}.md").read_text(encoding="utf-8")
        raw = re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", raw, count=1, flags=re.S)
        titles[slug] = re.search(r"^# (.+)$", raw, re.M).group(1)
        docs[slug] = raw
    template = BeautifulSoup((ROOT / "guides/swg-packet-crc.html").read_text(encoding="utf-8"), "html.parser")
    navbar = str(template.select_one("header.navbar"))
    for slug in SLUGS:
        body = BeautifulSoup(markdown.markdown(docs[slug], extensions=["tables", "fenced_code", "toc"]), "html.parser")
        for link in body.find_all("a", href=True):
            href = link["href"]
            if href.startswith(("https:", "http:", "#")):
                continue
            if href.startswith("../../"):
                href = href[3:]
            if re.search(r"\.md(?:#.*)?$", href):
                href = re.sub(r"\.md(?=#|$)", ".html", href)
            link["href"] = href
        for table in body.find_all("table"):
            table["class"] = ["doc-table"]
            wrapper = body.new_tag("div", attrs={"class": "table-wrap"})
            table.wrap(wrapper)
        links = "".join(f'<li><a href="{s}.html">{html.escape(titles[s])}</a></li>' for s in SLUGS)
        page = f'''<!DOCTYPE html>
<html lang="pt-BR" data-theme="dark">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(titles[slug])} | SWG Docs</title>
<meta name="description" content="{html.escape(SUMMARIES[slug], quote=True)}">
<link rel="stylesheet" href="../assets/css/style.css">
<style>.holocore-content{{max-width:1200px;margin:2rem auto;padding:0 1.5rem;overflow-wrap:anywhere}}
.holocore-content h1,.holocore-content h2,.holocore-content h3{{margin:1.5rem 0 1rem}}
.holocore-content p,.holocore-content ul,.holocore-content ol{{margin:1rem 0;line-height:1.75}}
.holocore-content pre{{overflow:auto;padding:1rem;background:var(--bg-secondary);border:1px solid var(--border-color);border-radius:.5rem}}
.holocore-content ul,.holocore-content ol{{padding-left:1.5rem}}.holocore-content .table-wrap{{overflow-x:auto}}</style></head>
<body data-root="../">{navbar}
<main class="holocore-content"><nav aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Guides</a> / Holocore</nav>
<details><summary>Guias Holocore</summary><ul>{links}</ul></details>
<p><a href="../content/guides/{slug}.md">Ler Markdown</a> · Revisão {REVISION} · Análise estática</p>
<article class="guide-body">{body}</article></main>
<footer><a href="holocore-overview.html">Holocore</a> · <a href="../index.html">SWG Docs</a></footer>
<script src="../assets/js/app.js"></script></body></html>
'''
        write(ROOT / "guides" / f"{slug}.html", page)
    block = '<section class="container" style="margin:2rem auto;padding:1.5rem" aria-label="Holocore"><h2>Holocore — análise do servidor</h2><p>Arquitetura, transporte, serviços e pipeline de dados, com limites de evidência registrados.</p><ul>'
    block += "".join(f'<li><a href="{s}.html">{html.escape(titles[s])}</a> — {html.escape(SUMMARIES[s])}</li>' for s in SLUGS)
    block += "</ul></section>"
    inject(ROOT / "guides/index.html", block)
    inject(ROOT / "index.html", f'<section class="container" style="margin:2rem auto;padding:1.5rem"><h2>Holocore</h2><p>{len(SLUGS)} guias de arquitetura, rede, serviços e dados do cliente.</p><a href="guides/holocore-overview.html">Explorar a análise de Holocore →</a></section>')
    data_path = ROOT / "data/guides.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    data["sections"] = [s for s in data["sections"] if s["id"] != "holocore"]
    data["sections"].append({"id": "holocore", "title": "Holocore", "count": len(SLUGS), "guides": [
        {"title": titles[s], "slug": s, "html_file": s + ".html", "md_file": s + ".md",
         "badge": "Source analysis", "summary": SUMMARIES[s], "category": "Holocore"} for s in SLUGS]})
    data["total_guides"] = sum(len(s["guides"]) for s in data["sections"])
    write(data_path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    guide_index = (ROOT / "guides/index.html").read_text(encoding="utf-8")
    guide_index = re.sub(r"\(\d+ curated entries\)", f"({data['total_guides']} curated entries)", guide_index)
    guide_index = re.sub(r"\d+ Guides Documented", f"{data['total_guides']} Guides Documented", guide_index)
    write(ROOT / "guides/index.html", guide_index)
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    total_guides = data["total_guides"]
    home = re.sub(r'(class="section-card-count">)\d+( Guides)', rf'\g<1>{total_guides}\2', home, count=1)
    write(ROOT / "index.html", home)
    index_path = ROOT / "search-index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    index = [x for x in index if x.get("u") not in {"guides/" + s + ".html" for s in SLUGS}]
    index.extend({"t": titles[s], "s": "guides", "st": "Packet Guides", "sc": "Holocore",
                  "o": "", "d": "unknown", "c": "source", "ss": "absent", "u": "guides/" + s + ".html",
                  "k": SUMMARIES[s] + " Holocore Java Kotlin ProjectSWG server networking gameplay"} for s in SLUGS)
    write(index_path, json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {len(SLUGS)} Holocore guides; guide index and search updated.")


if __name__ == "__main__":
    build()
