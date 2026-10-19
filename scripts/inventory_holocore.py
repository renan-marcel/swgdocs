"""Create a deterministic source inventory for the pinned Holocore checkout."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2] / "Holocore"
OUT = Path(__file__).resolve().parents[1] / "data" / "holocore-inventory.json"
COMMIT = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
roots = [ROOT / "src" / name for name in ("main", "test", "utility")]
files = []
for base in roots:
    for path in sorted(base.rglob("*")):
        if path.is_file() and path.suffix in {".java", ".kt"}:
            rel = path.relative_to(ROOT).as_posix()
            parts = path.relative_to(ROOT / "src").parts
            source_set = parts[0]
            package_parts = path.relative_to(base).parts
            if source_set == "utility":
                area = "utility"
            elif len(package_parts) >= 5 and package_parts[0] == "java" and package_parts[1:4] == ("com", "projectswg", "holocore"):
                area = "entrypoint" if package_parts[4].endswith((".java", ".kt")) else package_parts[4]
            elif len(package_parts) >= 4 and package_parts[0] == "java":
                area = package_parts[1]
            else:
                area = "other"
            files.append({
                "path": rel,
                "source_set": source_set,
                "language": path.suffix[1:],
                "area": area,
                "bytes": path.stat().st_size,
                "sha256": sha256(path.read_bytes()).hexdigest(),
            })
manifest = {
    "repository": "ProjectSWGCore/Holocore",
    "commit": COMMIT,
    "scope": "Java/Kotlin files under src/main, src/test, src/utility; static inventory only",
    "counts": {
        "files": len(files),
        "by_source_set": dict(sorted(Counter(f["source_set"] for f in files).items())),
        "by_language": dict(sorted(Counter(f["language"] for f in files).items())),
        "by_area": dict(sorted(Counter(f["area"] for f in files).items())),
    },
    "files": files,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest["counts"], ensure_ascii=False))

\n