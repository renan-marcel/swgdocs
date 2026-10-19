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
| [**Guides**](guides/) | **22** | Technical guides on SOE transport, CRC, compression, encryption, and reversing |
| [**TRE Sub-Files**](tre-subfiles/) | **9** | Client asset file specifications (`TRE`, `STF`, `QST`, `TRN`, `TOC`) |
| [**Reversal History**](history/) | **28** | Chronological ledger of all decoded/reversed packets with unpack VAs and schemas |
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

No build tools, Node.js, or complex dependencies are needed! You can simply open `index.html` in your browser, or run a lightweight local HTTP server:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .
```
Then visit `http://localhost:8000`.

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub on the `main` branch.
2. In your repository settings:
   - Navigate to **Settings** > **Pages**.
   - Under **Build and deployment** > **Source**, select **GitHub Actions** (the included `.github/workflows/deploy.yml` will deploy automatically) OR select **Deploy from a branch** and choose `main` / `/ (root)`.
3. Your site will be live at `https://<username>.github.io/<repo-name>/`.
