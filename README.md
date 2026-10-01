# Math History 101

Public GitHub Pages companion for the **Mathera History Network**: seven Epochs of math, twelve Worlds, and a 144-concept trophy wall.

**Live (once Pages is enabled):** https://julianlee314-hue.github.io/math-history-101/

## Framing

- **History Epochs** (Chinese 一–七): MARK → WRITE → ALGORITHM → PRINT → MECHANIZE → COMPUTE → INTELLIGENCE — how humanity stores, spreads, and automates mathematics.
- **Learner Eras** (Roman I–VII Count…Space) stay in the Mathera app; this site does not rename them.
- **Concept Wall**: 12×12 shelf of 144 trophies (text + pixel-art placeholders). Batch 1 (1–12) live.

Epoch colors (locked freeze):

| Glyph | Name | Hex |
|-------|------|-----|
| 一 | MARK | `#C68642` |
| 二 | WRITE | `#9A6239` |
| 三 | ALGORITHM | `#B08A3E` |
| 四 | PRINT | `#A8483A` |
| 五 | MECHANIZE | `#8C7352` |
| 六 | COMPUTE | `#6E5A48` |
| 七 | INTELLIGENCE | `#7B4558` |

Old Origins–Modern material colors remain on Batch 1 concept pages until a full Epoch remap.

## Layout

```
index.html                 Landing (Epochs + Worlds teaser + Wall CTA)
wall/index.html            12×12 Concept Wall (144 tiles)
epochs/index.html          Seven Epochs detail
eras/index.html            Note → Epochs (legacy path)
worlds/index.html          Twelve Worlds
about/index.html
artefacts/index.html       Batch 1 artefact lineages
concepts/<slug>/           Batch 1 concept pages (12)
concepts/coming/           Stub for concepts 13–144
css/site.css
js/site.js
data/epochs.json
data/worlds.json
data/concepts.json
data/artefacts.json
data/eras.json             (legacy)
data/concept-era-map.json  (legacy birth eras)
```

Links are **relative** for GitHub project Pages under `/math-history-101/`.

## Preview locally

```bash
cd math-history-101
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## GitHub Pages

1. Push to `julianlee314-hue/math-history-101`.
2. Settings → Pages → Deploy from branch `main` (root).
3. `.nojekyll` present.

Do not invent fake exact invention years. Do not push from agent tasks unless asked — parent commits.

## License / credit

History essays adapted from Mathera Concept Histories Batch 1. Freeze sheet: History Network companion (October 2026).
