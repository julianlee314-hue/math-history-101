/* Math History 101 — artefact drawer + shared helpers */
(function () {
  const ERA_COLORS = {
    origins: "#A35C2D",
    classical: "#8A6D3B",
    medieval: "#3F715B",
    renaissance: "#8B3948",
    enlightenment: "#3D5578",
    industrial: "#505860",
    modern: "#285A8C",
  };
  const ERA_NAMES = {
    origins: "Origins",
    classical: "Classical",
    medieval: "Medieval",
    renaissance: "Renaissance",
    enlightenment: "Enlightenment",
    industrial: "Industrial",
    modern: "Modern",
  };

  function dataUrl(file) {
    // Resolve relative to this script: ../data/...
    const scripts = document.getElementsByTagName("script");
    let base = "";
    for (let i = scripts.length - 1; i >= 0; i--) {
      const src = scripts[i].src || "";
      if (src.includes("site.js")) {
        base = src.replace(/js\/site\.js.*$/, "");
        break;
      }
    }
    return base + "data/" + file;
  }

  let artefactsCache = null;
  async function loadArtefacts() {
    if (artefactsCache) return artefactsCache;
    const res = await fetch(dataUrl("artefacts.json"));
    artefactsCache = await res.json();
    return artefactsCache;
  }

  function ensureDrawer() {
    let backdrop = document.getElementById("drawer-backdrop");
    let drawer = document.getElementById("artefact-drawer");
    if (backdrop && drawer) return { backdrop, drawer };

    backdrop = document.createElement("div");
    backdrop.id = "drawer-backdrop";
    backdrop.className = "drawer-backdrop";
    backdrop.setAttribute("aria-hidden", "true");

    drawer = document.createElement("aside");
    drawer.id = "artefact-drawer";
    drawer.className = "artefact-drawer";
    drawer.setAttribute("role", "dialog");
    drawer.setAttribute("aria-modal", "true");
    drawer.setAttribute("aria-labelledby", "drawer-title");
    drawer.innerHTML = `
      <div class="drawer-handle" aria-hidden="true"></div>
      <div class="drawer-head">
        <div>
          <h2 id="drawer-title">Artefact</h2>
          <div class="level-hint" id="drawer-levels"></div>
        </div>
        <button type="button" class="drawer-close" id="drawer-close" aria-label="Close">Close</button>
      </div>
      <div class="evo-viewport" id="evo-viewport">
        <div class="evo-fog" aria-hidden="true"></div>
        <div class="evo-strip" id="evo-strip"></div>
      </div>
      <p class="drawer-blurb" id="drawer-blurb"></p>
    `;

    document.body.appendChild(backdrop);
    document.body.appendChild(drawer);

    function close() {
      drawer.classList.remove("open");
      backdrop.classList.remove("open");
      document.body.classList.remove("drawer-open");
      backdrop.setAttribute("aria-hidden", "true");
    }

    backdrop.addEventListener("click", close);
    drawer.querySelector("#drawer-close").addEventListener("click", close);
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && drawer.classList.contains("open")) close();
    });

    return { backdrop, drawer };
  }

  function renderEvolution(artefact) {
    const strip = document.getElementById("evo-strip");
    const stages = artefact.stages || [];
    let html = "";
    stages.forEach((stage, i) => {
      if (i > 0) html += `<div class="evo-arrow" aria-hidden="true">→</div>`;
      const color = ERA_COLORS[stage.era] || "#666";
      const eraLabel = ERA_NAMES[stage.era] || stage.era;
      html += `
        <div class="evo-stage" tabindex="0" style="--stage-era:${color};--stage-i:${i}" title="">
          <div class="evo-silhouette" aria-hidden="true"></div>
          <div class="evo-label">${escapeHtml(stage.name)}</div>
          <div class="evo-era-tag">${escapeHtml(eraLabel)}</div>
        </div>`;
    });
    strip.innerHTML = html;
    document.getElementById("drawer-title").textContent = artefact.name;
    document.getElementById("drawer-levels").textContent =
      stages.length + " level-up" + (stages.length === 1 ? "" : "s") + " · era-span fogged";
    document.getElementById("drawer-blurb").textContent =
      artefact.summary || "Hover a silhouette to glimpse its name. The full era timeline stays deliberately foggy.";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  async function openArtefact(id) {
    const list = await loadArtefacts();
    const artefact = list.find((a) => a.id === id);
    if (!artefact) return;
    const { backdrop, drawer } = ensureDrawer();
    renderEvolution(artefact);
    drawer.classList.add("open");
    backdrop.classList.add("open");
    document.body.classList.add("drawer-open");
    backdrop.setAttribute("aria-hidden", "false");
    drawer.querySelector("#drawer-close").focus();
  }

  function bindButtons() {
    document.querySelectorAll("[data-artefact]").forEach((btn) => {
      btn.addEventListener("click", () => openArtefact(btn.getAttribute("data-artefact")));
    });
  }

  // Expose for inline use
  window.MathHistory101 = { openArtefact, ERA_COLORS, ERA_NAMES };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindButtons);
  } else {
    bindButtons();
  }
})();
