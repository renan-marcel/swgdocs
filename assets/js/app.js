// SWG Docs App JS
let searchIndex = [];

// Initialize Theme
function initTheme() {
  const saved = localStorage.getItem('swgdocs-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcon(saved);
}

function toggleTheme() {
  const curr = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = curr === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('swgdocs-theme', next);
  updateThemeIcon(next);
}

function updateThemeIcon(theme) {
  const btn = document.getElementById('theme-toggle-btn');
  if (btn) {
    btn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
  }
}

// Copy to Clipboard
function copyToClipboard(text, btnElement) {
  navigator.clipboard.writeText(text).then(() => {
    const orig = btnElement.innerText;
    btnElement.innerText = 'Copied!';
    btnElement.style.color = '#4ade80';
    setTimeout(() => {
      btnElement.innerText = orig;
      btnElement.style.color = '';
    }, 1500);
  });
}

// Load Search Index
async function loadSearchIndex() {
  if (searchIndex.length > 0) return searchIndex;
  try {
    const rootPath = document.body.getAttribute('data-root') || '';
    const res = await fetch(rootPath + 'search-index.json');
    searchIndex = await res.json();
    return searchIndex;
  } catch (e) {
    console.error('Failed to load search index:', e);
    return [];
  }
}

// Setup Global Quick Search Modal / Dropdown
function setupGlobalSearch() {
  const input = document.getElementById('global-search-input');
  const resultsContainer = document.getElementById('search-dropdown-results');
  if (!input || !resultsContainer) return;

  input.addEventListener('focus', () => loadSearchIndex());

  input.addEventListener('input', async (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (q.length < 2) {
      resultsContainer.style.display = 'none';
      return;
    }
    const idx = await loadSearchIndex();
    const matches = idx.filter(item => 
      item.t.toLowerCase().includes(q) || 
      item.o.toLowerCase().includes(q) || 
      item.k.toLowerCase().includes(q)
    ).slice(0, 10);

    if (matches.length === 0) {
      resultsContainer.innerHTML = '<div style="padding:0.75rem; color:var(--text-muted); font-size:0.85rem;">No packets found</div>';
      resultsContainer.style.display = 'block';
      return;
    }

    const rootPath = document.body.getAttribute('data-root') || '';
    resultsContainer.innerHTML = matches.map(m => `
      <a href="${rootPath}${m.u}" style="display:flex; justify-content:space-between; align-items:center; padding:0.6rem 0.85rem; border-bottom:1px solid var(--border-color); font-size:0.85rem; color:var(--text-primary); text-decoration:none;">
        <div>
          <strong>${m.t}</strong>
          <span style="color:var(--text-muted); font-size:0.75rem; margin-left:0.5rem;">${m.st}</span>
        </div>
        <div>
          ${m.o ? `<code style="color:var(--accent-cyan); font-family:var(--font-mono); font-size:0.8rem; margin-right:0.5rem;">${m.o}</code>` : ''}
          <span class="badge badge-${m.c.replace('%','')}">${m.c}</span>
        </div>
      </a>
    `).join('');
    resultsContainer.style.display = 'block';
  });

  document.addEventListener('click', (e) => {
    if (!input.contains(e.target) && !resultsContainer.contains(e.target)) {
      resultsContainer.style.display = 'none';
    }
  });
}

// Master Explorer Table (on home and section indexes)
let currentPage = 1;
const PAGE_SIZE = 50;

async function initMasterTable() {
  const tableBody = document.getElementById('master-table-body');
  if (!tableBody) return;

  const idx = await loadSearchIndex();
  const searchInput = document.getElementById('table-search-input');
  const sectionFilter = document.getElementById('table-section-filter');
  const directionFilter = document.getElementById('table-direction-filter');
  const completionFilter = document.getElementById('table-completion-filter');
  const sampleFilter = document.getElementById('table-sample-filter');
  const paginationControls = document.getElementById('table-pagination');

  function render() {
    const q = searchInput ? searchInput.value.trim().toLowerCase() : '';
    const sec = sectionFilter ? sectionFilter.value : '';
    const dir = directionFilter ? directionFilter.value : '';
    const comp = completionFilter ? completionFilter.value : '';
    const sample = sampleFilter ? sampleFilter.value : '';

    const filtered = idx.filter(item => {
      if (sec && item.s !== sec) return false;
      if (dir && item.d !== dir) return false;
      if (comp && item.c !== comp) return false;
      if (sample && item.ss !== sample) return false;
      if (q) {
        return item.t.toLowerCase().includes(q) || 
               item.o.toLowerCase().includes(q) || 
               item.k.toLowerCase().includes(q) ||
               item.sc.toLowerCase().includes(q);
      }
      return true;
    });

    const totalPages = Math.ceil(filtered.length / PAGE_SIZE) || 1;
    if (currentPage > totalPages) currentPage = 1;

    const start = (currentPage - 1) * PAGE_SIZE;
    const pageItems = filtered.slice(start, start + PAGE_SIZE);

    const rootPath = document.body.getAttribute('data-root') || '';
    
    if (pageItems.length === 0) {
      tableBody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:var(--text-muted);">No matching packets found.</td></tr>';
    } else {
      tableBody.innerHTML = pageItems.map(item => `
        <tr>
          <td><a href="${rootPath}${item.u}" style="font-weight:600;">${item.t}</a></td>
          <td>${item.o ? `<span class="opcode-pill" onclick="copyToClipboard('${item.o}', this)">${item.o}</span>` : '<span style="color:var(--text-muted);">-</span>'}</td>
          <td><span style="color:var(--text-secondary); font-size:0.8rem;">${item.st}</span></td>
          <td>
            ${item.d === 'S→C' ? '<span class="badge badge-sc">S→C</span>' : ''}
            ${item.d === 'C→S' ? '<span class="badge badge-cs">C→S</span>' : ''}
            ${item.d !== 'S→C' && item.d !== 'C→S' ? '<span style="color:var(--text-muted); font-size:0.8rem;">-</span>' : ''}
          </td>
          <td><span class="badge badge-${item.c.replace('%','')}">${item.c}</span></td>
          <td><span class="badge badge-sample-${item.ss}">${item.ss}</span></td>
        </tr>
      `).join('');
    }

    // Pagination
    if (paginationControls) {
      paginationControls.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-size:0.85rem; color:var(--text-secondary);">
          <div>Showing ${filtered.length > 0 ? start + 1 : 0} to ${Math.min(start + PAGE_SIZE, filtered.length)} of <strong>${filtered.length}</strong> items</div>
          <div style="display:flex; gap:0.5rem;">
            <button class="copy-btn" ${currentPage === 1 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''} onclick="changePage(-1)">Previous</button>
            <span style="padding:0.25rem 0.5rem; font-weight:600;">Page ${currentPage} of ${totalPages}</span>
            <button class="copy-btn" ${currentPage === totalPages ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''} onclick="changePage(1)">Next</button>
          </div>
        </div>
      `;
    }
  }

  window.changePage = function(delta) {
    currentPage += delta;
    render();
  };

  [searchInput, sectionFilter, directionFilter, completionFilter, sampleFilter].forEach(el => {
    if (el) el.addEventListener('input', () => { currentPage = 1; render(); });
  });

  render();
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  setupGlobalSearch();
  initMasterTable();
});
