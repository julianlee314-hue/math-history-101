# Math History 101

Public GitHub Pages curiosity cabinet: short Civ-style math history lessons on 144 concepts (Batch 1 live).

**Live (once Pages is enabled):** https://julianlee314-hue.github.io/math-history-101/

## Concept

- Hub index: messy-but-pretty grid of all 144 concept chips (1–12 clickable; 13–144 muted “coming”).
- Concept pages: historical era chip + history blurb + simple illustration + artefact buttons.
- Artefact drawer: shadowed Pokémon-style evolution strip. You can count level-ups; era labels stay fogged until hover/focus.

Colors mark **historical eras** (Origins → Modern), not Mathera learner eras.

## Historical era colors

| Era | Dates | Color |
|-----|-------|-------|
| I Origins | Prehistory–c.600 BCE | `#A35C2D` |
| II Classical | c.600 BCE–500 CE | `#8A6D3B` |
| III Medieval | c.500–1400 | `#3F715B` |
| IV Renaissance | c.1400–1650 | `#8B3948` |
| V Enlightenment | c.1650–1800 | `#3D5578` |
| VI Industrial | c.1800–1900 | `#505860` |
| VII Modern | c.1900–present | `#285A8C` |

Locked as CSS variables in `css/site.css` (`--era-origins` … `--era-modern`).

## Layout

```
index.html              Hub
about/index.html
eras/index.html
artefacts/index.html
concepts/<slug>/index.html   Batch 1 (12 pages)
css/site.css
js/site.js
data/eras.json
data/concepts.json
data/artefacts.json
```

Links are **relative** so the site works both locally and as a GitHub project Pages site under `/math-history-101/` (no absolute `/` roots).

## Preview locally

```bash
cd math-history-101
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or open `index.html` directly; fetch of JSON for the artefact drawer needs a local server (file:// may block).

## GitHub Pages

1. Push this repo to `julianlee314-hue/math-history-101`.
2. Settings → Pages → Source: Deploy from branch `main` (root).
3. `.nojekyll` is present so GitHub does not run Jekyll.

Do not invent fake exact invention years; history blurbs use ranges from Batch 1 essays.

## Data

- `data/concepts.json` — all 144; first 12 have `history`, `era`, `artefacts`, `status:"live"`.
- `data/artefacts.json` — launch lineages with evolution stages tagged by historical era id.
- `data/eras.json` — the seven eras with colors and material cues.

## License / credit

History essays adapted from Mathera Concept Histories Batch 1. Site shell for Math History 101.
