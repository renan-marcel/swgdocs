"""Validate generated Holocore guide pages and local links without network access."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ["holocore-overview", "holocore-network", "holocore-services", "holocore-clientdata"]


def main():
    issues = []
    checked = 0
    for slug in SLUGS:
        page = ROOT / "guides" / f"{slug}.html"
        assert page.exists()
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        assert len(soup.select("main article h1")) == 1
        assert soup.html["lang"] == "pt-BR"
        for node in soup.select("a[href],script[src],link[href]"):
            url = node.get("href", node.get("src"))
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            checked += 1
            target = (page.parent / unquote(parts.path)).resolve() if parts.path else page
            if not target.exists():
                issues.append(f"{page.name}: missing {url}")
            elif parts.fragment and target.suffix == ".html":
                linked = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
                if not linked.find(id=unquote(parts.fragment)):
                    issues.append(f"{page.name}: missing fragment {url}")
    data = json.loads((ROOT / "data/holocore-inventory.json").read_text(encoding="utf-8"))
    assert data["counts"]["files"] == len(data["files"])
    for path in ROOT.joinpath("data/holocore-evidence").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    index = json.loads((ROOT / "search-index.json").read_text(encoding="utf-8"))
    for slug in SLUGS:
        assert sum(x["u"] == f"guides/{slug}.html" for x in index) == 1
    assert not issues, "\n".join(issues)
    print(json.dumps({"pages": len(SLUGS), "local_links_checked": checked,
                      "inventory_files": data["counts"]["files"], "issues": issues}, indent=2))


if __name__ == "__main__":
    main()

\n