# SWG Docs — Star Wars Galaxies Protocol Documentation

A clean, modern, and comprehensive technical documentation portal for Star Wars Galaxies (SWG) protocols, network packets, opcodes, client commands, object controllers, baselines, and file formats.

This repository is ready to be hosted directly on **GitHub Pages** with zero configuration required.

---

## 🌟 What is in this Repository?

| Section | Count | Description |
|---|---|---|
| [**Protocols**](protocols/) | **252** | Core SWG network packets (Chat, Trade, Auction, Login, Scene, Player State, Guilds) |
| [**Client Commands**](commands/) | **889** | Every client command executed via `CommandQueueEnqueue` (00000116) |
| [**Object Controllers**](controllers/) | **177** | `ObjControllerMessage` (0000000B) sub-handlers and controller IDs |
| [**Baselines**](baselines/) | **77** | Full object serialization definitions (`CREO`, `PLAY`, `TANO`, `SHIP`, etc.) |
| [**Deltas**](deltas/) | **76** | Differential update packets modifying object baselines and counters |
| [**Guides**](guides/) | **21** | Technical guides on SOE transport, CRC, compression, encryption, reversing, and server implementation |
| [**PSWGCommon**](guides/pswgcommon-overview.html) | **7 guides** | Architecture, codecs, models, assets, source catalog, and Binary Ninja message comparisons |
| [**Holocore**](guides/holocore-overview.html) | **5 guides** | Server architecture, execution flows, network, gameplay services, and client-data conversion |
| [**TRE Sub-Files**](tre-subfiles/) | **9** | Client asset file specifications (`TRE`, `STF`, `QST`, `TRN`, `TOC`) |
| [**Reversal History**](history/) | **31** | Chronological ledger of decoded/reversed packets with unpack VAs and schemas |
| [**Pending Backlog (0%)**](pending/) | **895** | Master catalog of all unmapped packets, commands, and controllers at 0% completion |
| [**Interactive Inspector**](tools/inspector.html) | **Tool** | Real-time packet inspector, decoder, and payload generator for opcodes and controllers |

---

## 🛠️ Reverse Engineering Workflow & Automation

For detailed reverse engineering guidelines, binary evidence extraction procedures (`SWGEmu.exe`), and instructions for the **automated history and backlog tasks**, please consult:

👉 [**WORKFLOW.md**](WORKFLOW.md)

To automatically rebuild and update the Reversal History and Pending Backlog pages at any time:
```bash
# Update reversal history
python scripts/update_history.py

# Update pending 0% catalog
python scripts/generate_pending_page.py
```

- **Instant Search & Opcode Finder**: Search by 8-digit hex opcode (e.g. `9CA80F98`, `00000116`), packet name, or field across all 1,427 documents.
- **Interactive Multi-Filter Table**: Filter by section, packet direction (`S→C` / `C→S`), completion badge (`100%`, `75%`, etc.), or sample packet status.
- **Clean Developer Interface**: Dark and Light theme toggle, responsive layout, monospace type pills, and structured struct tables.
- **Sample Hex Dumps**: Over 448 real byte-for-byte hex packet dumps with a 1-click **Copy Sample** button.
- **Multiple Formats Available**:
  - **Interactive Web Pages**: `.html` files in each section.
  - **Raw Markdown**: `.md` files in `content/` for reading in GitHub, Obsidian, or VS Code.
  - **Structured CSV**: [`data/all_packets.csv`](data/all_packets.csv) containing 6,929 struct fields.
  - **JSON Catalog**: [`data/packets_summary.json`](data/packets_summary.json) for bots and emulators.

---

## 💻 Running Locally

### PSWGCommon implementation reference

Start with [the architecture guide](content/guides/pswgcommon-overview.md). The analysis covers the local Java/Kotlin library at revision `9ab4234`, with a deterministic inventory of 433 source/resource files and separate guides for networking, shared data, and client assets. The [binary evidence guide](content/guides/pswgcommon-binary.md) records the CRC table comparison and the REA provider limitation on this x86 target. Source-derived findings do not change packet verification percentages.

The HTML is committed and needs no build to view. To regenerate these guides from Markdown, run from the `swgdocs` directory:

```powershell
python -m pip install -r scripts/requirements-pswgcommon.txt
python scripts/inventory_pswgcommon.py --source ../pswgcommon
python scripts/build_pswgcommon_docs.py
python scripts/validate_pswgcommon_docs.py
```

The source clone is required only to regenerate the inventory. To repeat the static CRC comparison, with the preserved original executable available, run `python scripts/verify_pswgcommon_evidence.py`. For the three message layouts, run `python scripts/verify_pswgcommon_messages.py`; their cross-reference notes are maintained by `python scripts/apply_pswgcommon_message_crosscheck.py`. The library and its JVM tests were not executed for this documentation update.

No build tools, Node.js, or complex dependencies are needed! You can simply open `index.html` in your browser, or run a lightweight local HTTP server:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .
```
Then visit `http://localhost:8000`.

### Holocore implementation reference

The [Holocore guides](content/guides/holocore-overview.md) describe revision `ff53903bbb8b0ff2edcd2493d66f940767036aaa` and inventory 828 Java/Kotlin files across main, test, and utility source sets. The local `Holocore/pswgcommon` Git submodule is uninitialized; shared packet codecs are documented as an external dependency. Binary Ninja client cross-checks and retained pseudocode are under `data/holocore-evidence/`. REA MCP was unavailable in the analysis session, so no REA setup or client execution was performed.

With the Holocore checkout adjacent to this repository, regenerate and validate its source inventory and guides from the `swgdocs` directory:

```powershell
python scripts/inventory_holocore.py
python scripts/build_holocore_docs.py
python scripts/validate_holocore_docs.py
```

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub on the `main` branch.
2. In your repository settings:
   - Navigate to **Settings** > **Pages**.
   - Under **Build and deployment** > **Source**, select **GitHub Actions** (the included `.github/workflows/deploy.yml` will deploy automatically) OR select **Deploy from a branch** and choose `main` / `/ (root)`.
3. Your site will be live at `https://<username>.github.io/<repo-name>/`.
