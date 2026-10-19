"""Render the PSWGCommon guides and integrate them without rebuilding legacy pages.

Run from any directory. Dependencies: requirements-pswgcommon.txt.
The Markdown files are authoritative; generated HTML is committed for Pages.
"""
from pathlib import Path
import html
import json
import re

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ['pswgcommon-overview', 'pswgcommon-network', 'pswgcommon-data',
         'pswgcommon-assets', 'pswgcommon-binary', 'pswgcommon-client-messages', 'pswgcommon-catalog']
START = '<!-- pswgcommon:start -->'
END = '<!-- pswgcommon:end -->'
SUMMARIES = {
    'pswgcommon-overview': 'Arquitetura, dependências, fluxos e limites da investigação.',
    'pswgcommon-network': 'Codecs, endian, framing, factories, baseline, delta e controllers.',
    'pswgcommon-data': 'Modelos, CRC, customização, OOB, SUI e persistência Mongo.',
    'pswgcommon-assets': 'As duas APIs IFF, formatos, caches e motor de terreno.',
    'pswgcommon-binary': 'Evidências do Binary Ninja e limitações do provedor REA.',
    'pswgcommon-client-messages': 'Contenção, criação de objetos e chat confrontados com leitores e escritores do cliente.',
    'pswgcommon-catalog': 'Inventário completo de arquivos e cruzamento nominal de mensagens.'}


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding='utf-8') != value:
        path.write_text(value, encoding='utf-8')


def inject(path, block, before='<footer>'):
    text = path.read_text(encoding='utf-8')
    fragment = START+'\n'+block+'\n'+END
    if START in text:
        text = re.sub(re.escape(START)+r'.*?'+re.escape(END), lambda _: fragment,
                      text, count=1, flags=re.S)
    else:
        assert before in text, (path, before)
        text = text.replace(before, fragment+'\n'+before, 1)
    write(path, text)


def build():
    titles = {}
    documents = {}
    for slug in SLUGS:
        raw = (ROOT/'content/guides'/f'{slug}.md').read_text(encoding='utf-8')
        raw = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', raw, count=1, flags=re.S)
        titles[slug] = re.search(r'^# (.+)$', raw, re.M).group(1)
        documents[slug] = raw
    for slug in SLUGS:
        raw = documents[slug]
        title = titles[slug]
        body = BeautifulSoup(markdown.markdown(raw, extensions=['tables', 'fenced_code', 'toc']), 'html.parser')
        for link in body.find_all('a', href=True):
            href = link['href']
            if href.startswith(('https:', 'http:', '#')):
                continue
            # content/guides -> guides: references out of content lose one level.
            if href.startswith('../../'):
                href = href[3:]
            if re.search(r'\.md(?:#.*)?$', href):
                href = re.sub(r'\.md(?=#|$)', '.html', href)
            link['href'] = href
        for table in body.find_all('table'):
            table['class'] = ['doc-table']
            wrapper = body.new_tag('div', attrs={'class': 'table-wrap'})
            table.wrap(wrapper)
        # Link unambiguous inline source references to the pinned revision.
        inventory_path = ROOT/'data/pswgcommon-inventory.json'
        if inventory_path.exists():
            inventory = json.loads(inventory_path.read_text(encoding='utf-8'))
            sources = [f for f in inventory['files'] if f['path'].endswith(('.java', '.kt'))]
            for code in list(body.find_all('code')):
                if code.parent.name == 'pre':
                    continue
                match = re.fullmatch(r'(?:J/)?([\w/.-]+\.(?:java|kt)):(\d+)[\d–—,: -]*', code.get_text())
                if not match:
                    continue
                candidates = [f for f in sources if f['path'].endswith('/'+match[1])]
                if len(candidates) == 1:
                    anchor = body.new_tag('a', href=candidates[0]['source_url']+'#L'+match[2])
                    code.wrap(anchor)
        template = BeautifulSoup((ROOT/'guides/swg-packet-crc.html').read_text(encoding='utf-8'), 'html.parser')
        navbar = str(template.select_one('header.navbar'))
        sidebar = ''.join(f'<li><a href="{s}.html">{html.escape(titles[s])}</a></li>' for s in SLUGS)
        page = f'''<!DOCTYPE html>
<html lang="pt-BR" data-theme="dark">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} | SWG Docs</title>
<meta name="description" content="{html.escape(SUMMARIES[slug], quote=True)}">
<link rel="stylesheet" href="../assets/css/style.css">
<style>.pswg-content{{max-width:1200px;margin:2rem auto;padding:0 1.5rem;overflow-wrap:anywhere}}
.pswg-content h1,.pswg-content h2,.pswg-content h3{{margin:1.5rem 0 1rem}}
.pswg-content p,.pswg-content ul,.pswg-content ol{{margin:1rem 0;line-height:1.75}}
.pswg-content pre{{overflow-x:auto;padding:1rem;background:var(--bg-secondary);border:1px solid var(--border-color);border-radius:.5rem;line-height:1.6}}
.pswg-content ul,.pswg-content ol{{padding-left:1.5rem}}.pswg-content .table-wrap{{max-width:100%;overflow-x:auto}}
.pswg-content details{{margin:1rem 0}}.pswg-content summary{{cursor:pointer;font-weight:600}}</style></head>
<body data-root="../">{navbar}
<main class="pswg-content">
<nav aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Guides</a> / PSWGCommon</nav>
<details><summary>Guias PSWGCommon</summary><ul>{sidebar}</ul></details>
<p><a href="../content/guides/{slug}.md">Ler Markdown</a> · Revisão 9ab4234 · Evidência estática</p>
<article class="guide-body">{body}</article>
</main><footer><a href="pswgcommon-overview.html">PSWGCommon</a> · <a href="../index.html">SWG Docs</a></footer>
<script src="../assets/js/app.js"></script></body></html>
'''
        write(ROOT/'guides'/f'{slug}.html', page)

    cards = '<section class="container" style="margin:2rem auto;padding:1.5rem" aria-label="PSWGCommon"><h2>PSWGCommon — análise da biblioteca</h2><p>Fontes, arquitetura e evidências estáticas; inclui limites da comparação com o cliente.</p><ul>'
    cards += ''.join(f'<li><a href="{slug}.html">{html.escape(titles[slug])}</a> — {html.escape(SUMMARIES[slug])}</li>' for slug in SLUGS)
    cards += '</ul></section>'
    inject(ROOT/'guides/index.html', cards)
    inject(ROOT/'index.html', f'<section class="container" style="margin:2rem auto;padding:1.5rem"><h2>PSWGCommon</h2><p>{len(SLUGS)} guias sobre arquitetura, rede, modelos, assets e comparação binária.</p><a href="guides/pswgcommon-overview.html">Explorar a análise da biblioteca →</a></section>')
    data_path = ROOT/'data/guides.json'
    data = json.loads(data_path.read_text(encoding='utf-8'))
    data['sections'] = [s for s in data['sections'] if s['id'] != 'pswgcommon']
    data['sections'].append({'id': 'pswgcommon', 'title': 'PSWGCommon', 'count': len(SLUGS), 'guides': [
        {'title': titles[s], 'slug': s, 'html_file': s+'.html', 'md_file': s+'.md',
         'badge': 'Source analysis', 'summary': SUMMARIES[s], 'category': 'PSWGCommon'} for s in SLUGS]})
    data['total_guides'] = sum(len(s['guides']) for s in data['sections'])
    write(data_path, json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    overview_path = ROOT/'guides/index.html'
    overview_html = overview_path.read_text(encoding='utf-8')
    overview_html = re.sub(r'\(\d+ (?:documented|curated) entries\)',
                           f"({data['total_guides']} curated entries)", overview_html)
    overview_html = re.sub(r'\d+ Guides Documented',
                           f"{data['total_guides']} Guides Documented", overview_html)
    write(overview_path, overview_html)
    index_path = ROOT/'search-index.json'
    index = json.loads(index_path.read_text(encoding='utf-8'))
    index = [x for x in index if x.get('u') not in {'guides/'+s+'.html' for s in SLUGS}]
    # Packet source notes update the existing schemas separately; synchronize search terms.
    summary = json.loads((ROOT/'data/packets_summary.json').read_text(encoding='utf-8'))
    refreshed = {p['u']: p for p in summary if p['u'] in {
        'protocols/UpdateContainmentMessage.html', 'protocols/SceneCreateObjectByCrc.html',
        'protocols/ChatInstantMessageToClient.html'}}
    for entry in index:
        if entry['u'] in refreshed:
            entry['k'] = refreshed[entry['u']]['k']
    index.extend({'t': titles[s], 's': 'guides', 'st': 'Packet Guides', 'sc': 'PSWGCommon',
                  'o': '', 'd': 'unknown', 'c': 'source', 'ss': 'absent', 'u': 'guides/'+s+'.html',
                  'k': SUMMARIES[s]+' '+s+' pswgcommon Java Kotlin ProjectSWG REA Binary Ninja'} for s in SLUGS)
    write(index_path, json.dumps(index, ensure_ascii=False, indent=2)+'\n')
    related = {
        'guides/soe-protocol-breakdown': ('pswgcommon-network', 'NetworkProtocol usa um envelope de comprimento próprio. Veja o contrato implementado pela biblioteca e seus limites.'),
        'baselines/BaselinesMessage': ('pswgcommon-network', 'Implementação PSWGCommon: envelope baseline e limitações ao decodificar e serializar novamente.'),
        'deltas/DeltasMessage': ('pswgcommon-network', 'Implementação PSWGCommon: envelope delta, índices e dados de atualização.')}
    for target, (slug, label) in related.items():
        inject(ROOT/(target+'.html'), f'<aside class="container" style="padding:1.5rem;margin:2rem auto"><strong>Referência de implementação</strong><p><a href="../guides/{slug}.html">{html.escape(label)}</a></p><p>Análise de fontes; não altera o status de verificação desta página.</p></aside>')
        md_path = ROOT/'content'/(target+'.md')
        block = f'\n## Referência de implementação PSWGCommon\n\n[{label}](../guides/{slug}.md)\n\nAnálise de fontes; não altera o status de verificação desta página.\n'
        if START in md_path.read_text(encoding='utf-8'):
            inject(md_path, block)
        else:
            write(md_path, md_path.read_text(encoding='utf-8')+'\n'+START+'\n'+block+'\n'+END+'\n')
    print(f'Rendered {len(SLUGS)} guides; search, navigation and related references updated.')


if __name__ == '__main__':
    build()
