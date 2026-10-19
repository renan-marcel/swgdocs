"""Validate the generated PSWGCommon documentation without network access."""
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from build_pswgcommon_docs import SLUGS

ROOT = Path(__file__).resolve().parents[1]


def main():
    pages = sorted((ROOT/'guides').glob('pswgcommon-*.html'))
    assert {p.stem for p in pages} == set(SLUGS), len(pages)
    issues = []
    link_count = 0
    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
        assert len(soup.select('main article h1')) == 1, page
        assert soup.html['lang'] == 'pt-BR'
        assert soup.select_one('#global-search-input')
        assert soup.select_one('#theme-toggle-btn')
        assert len(soup.select('main details a')) == len(SLUGS)
        for item in soup.select('a[href],script[src],link[href]'):
            url = item.get('href', item.get('src'))
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            link_count += 1
            target = (page.parent/unquote(parts.path)).resolve() if parts.path else page
            if not target.exists():
                issues.append(f'{page.name}: missing {url}')
            elif parts.fragment and target.suffix == '.html':
                linked = BeautifulSoup(target.read_text(encoding='utf-8'), 'html.parser')
                if not linked.find(id=unquote(parts.fragment)):
                    issues.append(f'{page.name}: missing fragment {url}')
    index = json.loads((ROOT/'search-index.json').read_text(encoding='utf-8'))
    for page in pages:
        entries = [x for x in index if x['u'] == 'guides/'+page.name]
        assert len(entries) == 1 and entries[0]['c'] == 'source'
        assert (ROOT/'content/guides'/page.with_suffix('.md').name).exists()
    data = json.loads((ROOT/'data/guides.json').read_text(encoding='utf-8'))
    assert data['total_guides'] == sum(len(s['guides']) for s in data['sections'])
    assert len([s for s in data['sections'] if s['id'] == 'pswgcommon']) == 1
    inventory = json.loads((ROOT/'data/pswgcommon-inventory.json').read_text(encoding='utf-8'))
    assert len(inventory['files']) == len({f['path'] for f in inventory['files']})
    for path in sorted((ROOT/'data/pswgcommon-evidence').rglob('*.json')):
        json.loads(path.read_text(encoding='utf-8'))
    for path in [ROOT/'index.html', ROOT/'guides/index.html']:
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        assert any('pswgcommon-overview.html' in x.get('href', '') for x in soup.find_all('a'))
    assert not issues, '\n'.join(issues)
    manifest = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in pages}
    print(json.dumps({'pages': len(pages), 'local_links_checked': link_count,
                      'inventory_files': len(inventory['files']), 'issues': issues,
                      'html_sha256': manifest}, indent=2))


if __name__ == '__main__':
    main()
