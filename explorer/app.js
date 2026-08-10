(function () {
  const data = window.LEGISLATIVE_DATA;
  if (!data) return console.error("data.js não carregado");

  let active = new Set(data.countries.map(c => c.id));

  const $ = id => document.getElementById(id);
  const controls = $("controls");
  const thead = $("compareTable").querySelector("thead");
  const tbody = $("compareTable").querySelector("tbody");
  const sourcesDiv = $("sources");

  function renderControls() {
    controls.innerHTML = "";
    data.countries.forEach(c => {
      const isActive = active.has(c.id);
      const btn = document.createElement("button");
      btn.className = "btn" + (isActive ? " active" : "");
      btn.style.borderColor = isActive ? c.color : "#dee2e6";
      if (isActive) btn.style.background = c.color;
      btn.textContent = c.name;
      btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      btn.setAttribute("aria-label", c.name + " (" + c.status + ")");
      const badge = document.createElement("span");
      badge.className = "badge";
      badge.textContent = c.status;
      badge.setAttribute("aria-hidden", "true");
      btn.appendChild(badge);
      btn.onclick = () => {
        if (active.has(c.id)) {
          if (active.size > 1) active.delete(c.id);
        } else {
          active.add(c.id);
        }
        renderControls();
        renderTable();
        renderSources();
      };
      controls.appendChild(btn);
    });
  }

  function renderTable() {
    const cols = data.countries.filter(c => active.has(c.id));
    thead.innerHTML = `<tr><th scope="col">Característica</th>${cols.map(c => `<th scope="col" style="color:${c.color}">${c.name}</th>`).join("")}</tr>`;
    tbody.innerHTML = "";
    data.categories.forEach(cat => {
      const tr = document.createElement("tr");
      tr.className = "cat-header";
      tr.innerHTML = `<td colspan="${cols.length + 1}">${cat.name}</td>`;
      tbody.appendChild(tr);
      cat.features.forEach(f => {
        const row = document.createElement("tr");
        let html = `<th scope="row">${f.label}</th>`;
        cols.forEach(c => {
          const val = f[c.id] || "—";
          html += `<td>${val}</td>`;
        });
        row.innerHTML = html;
        tbody.appendChild(row);
      });
    });
  }

  function renderSources() {
    const cols = data.countries.filter(c => active.has(c.id));
    let html = "<h2>Fontes e Referências</h2>";
    cols.forEach(c => {
      const list = data.sources[c.id] || [];
      html += `<div class="country-sources">
        <h3><span class="dot" style="background:${c.color}"></span>${c.name}</h3>
        <ul>${list.map(s => `<li><strong>[${s.key}]</strong> ${s.text}</li>`).join("")}</ul>
      </div>`;
    });
    html += `<p style="font-size:.85rem;color:var(--muted);margin-top:1rem">Citações no formato <code>[@chave]</code> correspondem às entradas em <code>references.bib</code> do documento principal.</p>`;
    sourcesDiv.innerHTML = html;
  }

  renderControls();
  renderTable();
  renderSources();
})();
