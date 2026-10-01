#!/usr/bin/env python3
"""Generate concept pages, sync concepts.json, rebuild wall links from concept-histories.json."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONCEPTS_DIR = ROOT / "concepts"
WALL = ROOT / "wall" / "index.html"

EPOCHS = {e["id"]: e for e in json.loads((DATA / "epochs.json").read_text())}
WORLDS = {w["id"]: w for w in json.loads((DATA / "worlds.json").read_text())}
ERAS = {e["id"]: e for e in json.loads((DATA / "eras.json").read_text())}
ARTEFACTS = {a["id"]: a for a in json.loads((DATA / "artefacts.json").read_text())}


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html)


def paragraphs_html(text: str) -> str:
    parts = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    return "\n".join(f"<p>{p}</p>" for p in parts)


def concept_page(hist: dict, concept_meta: dict) -> str:
    cid = hist["id"]
    slug = hist["slug"]
    name = hist["name"]
    era_id = concept_meta.get("era") or "origins"
    era = ERAS.get(era_id, ERAS["origins"])
    artefacts = hist.get("artefacts") or concept_meta.get("artefacts") or []
    epochs = hist.get("epochs") or []

    chips = []
    essays = []
    for ep in epochs:
        emeta = EPOCHS[ep["id"]]
        color = emeta["color"]
        glyph = emeta["glyph"]
        title = f'{ep["n"]} · {ep["title"]}'
        chips.append(
            f'<a class="epoch-chip" href="#epoch-{ep["id"]}" style="--epoch-color:{color}">'
            f'<span class="chip-glyph" aria-hidden="true">{glyph}</span>'
            f'{ep["n"]} · {ep["title"]}</a>'
        )
        world_html = "".join(
            f'<span class="world-chip">{WORLDS[w]["name"] if w in WORLDS else w}</span>'
            for w in ep.get("worlds") or []
        )
        essays.append(
            f'<article class="epoch-essay" id="epoch-{ep["id"]}" style="--epoch-color:{color}">'
            f'<div class="epoch-essay-head">'
            f'<span class="epoch-swatch" aria-hidden="true">{glyph}</span>'
            f'<h2 class="epoch-title">{title}</h2>'
            f'<div class="world-chips">{world_html}</div>'
            f"</div>"
            f'<div class="essay-body">{paragraphs_html(ep["text"])}</div>'
            f"</article>"
        )

    aside_bits = []
    primary = None
    for aid in artefacts:
        art = ARTEFACTS.get(aid)
        if not art:
            continue
        img_rel = f"../../assets/artefacts/{aid}.jpg"
        img_path = ROOT / "assets" / "artefacts" / f"{aid}.jpg"
        if primary is None and img_path.exists():
            primary = (aid, art["name"], img_rel)
        aside_bits.append(
            f'<button type="button" class="btn-artefact" data-artefact="{aid}">{art["name"]} → evolution</button>'
        )

    aside_img = ""
    if primary:
        aid, aname, img_rel = primary
        aside_img = (
            f'<div class="lesson-art">'
            f'<img class="lesson-photo" src="{img_rel}" alt="{aname}" width="280" height="350" loading="lazy" />'
            f'<div class="art-caption">{aname}</div>'
            f"</div>"
        )

    aside = ""
    if aside_img or aside_bits:
        actions = (
            f'<div class="artefact-actions">{"".join(aside_bits)}</div>' if aside_bits else ""
        )
        aside = f"<aside>\n{aside_img}\n{actions}\n</aside>"

    chips_block = (
        f'<nav class="epoch-chips" aria-label="History epochs">{"".join(chips)}</nav>'
        if len(epochs) > 1
        else ""
    )
    history_block = (
        f'<div class="history-panel">'
        f"{chips_block}"
        f'<div class="history-scroll">{"".join(essays)}</div>'
        f"</div>"
    )

    live_count = sum(1 for c in json.loads((DATA / "concepts.json").read_text()) if c.get("status") == "live")
    footer_right = (
        f"All 144 concepts live"
        if live_count >= 144
        else f"{live_count} concepts live"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{name} · Math History 101</title>
  <meta name="description" content="History of {name} across mathematical epochs — Math History 101." />
  <link rel="stylesheet" href="../../css/site.css" />
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <a class="brand" href="../../index.html">Math History 101 <span>History Network</span></a>
    <ul class="nav"><li><a href="../../epochs/">Epochs</a></li><li><a href="../../wall/">Wall</a></li><li><a href="../../worlds/">Worlds</a></li><li><a href="../../about/">About</a></li><li><a href="../../wall/" aria-current="page">Concepts</a></li></ul>
  </div>
</header>
<main class="wrap">
<a class="back-link" href="../../wall/">← Concept Wall</a>
<header class="concept-head">
  <span class="concept-num">Concept {cid:03d}</span>
  <h1>{name}</h1>
  <span class="era-chip" style="--era-color:{era['color']}">{era['roman']} · {era['name']}</span>
</header>
<div class="concept-layout">
  {history_block}
  {aside}
</div>
</main>
<footer class="site-footer">
  <span>Math History 101 · Civ-style lessons · History Epochs</span>
  <span><a href="../../about/">About</a> · {footer_right}</span>
</footer>
<script src="../../js/site.js"></script>
</body>
</html>
"""


def sync_concepts(histories: list[dict]) -> list[dict]:
    concepts = json.loads((DATA / "concepts.json").read_text())
    by_id = {h["id"]: h for h in histories}
    # era from concept-era-map birth
    era_map = {e["id"]: e for e in json.loads((DATA / "concept-era-map.json").read_text())}
    learner_eras = ["origins", "classical", "medieval", "renaissance", "enlightenment", "industrial", "modern"]
    for c in concepts:
        h = by_id.get(c["id"])
        if not h:
            continue
        c["status"] = "live"
        c["artefacts"] = h.get("artefacts") or c.get("artefacts") or []
        texts = [ep["text"] for ep in h.get("epochs") or []]
        # flat history: first epoch, tags stripped to plain-ish (keep em for compat)
        c["history"] = "\n\n".join(texts) if texts else c.get("history", "")
        if not c.get("era"):
            birth = era_map.get(c["id"], {}).get("birth_era", 1)
            c["era"] = learner_eras[max(0, min(6, birth - 1))]
    (DATA / "concepts.json").write_text(json.dumps(concepts, indent=2, ensure_ascii=False) + "\n")
    return concepts


def update_wall(concepts: list[dict]) -> None:
    html = WALL.read_text()
    # Update hero copy
    html = re.sub(
        r"<p>144 concept trophies.*?</p>",
        "<p>144 concept trophies on a 12×12 shelf. Each tile opens a concept history with scrollable History Epoch essays. Companion artefact portraits sit on every tile.</p>",
        html,
        count=1,
        flags=re.S,
    )
    live_n = sum(1 for c in concepts if c.get("status") == "live")
    html = re.sub(
        r'<div class="wall-legend">.*?</div>',
        f'<div class="wall-legend">\n    <span class="leg-live">Live · {live_n}/144 concepts</span>\n  </div>',
        html,
        count=1,
        flags=re.S,
    )

    # Rebuild trophy links: for each concept id, ensure href goes to slug page and live class
    # Match each trophy block by number
    def repl_trophy(m):
        block = m.group(0)
        num = int(m.group(1))
        c = concepts[num - 1]
        slug = c["slug"]
        name = c["name"]
        live = c.get("status") == "live"
        # replace href
        block = re.sub(
            r'href="[^"]*"',
            f'href="../concepts/{slug}/"',
            block,
            count=1,
        )
        block = re.sub(
            r'title="[^"]*"',
            f'title="{num:03d} · {name}"',
            block,
            count=1,
        )
        # class
        if live:
            block = re.sub(r'class="trophy[^"]*"', 'class="trophy live"', block, count=1)
            block = re.sub(
                r'<span class="trophy-tag">[^<]*</span>',
                '<span class="trophy-tag">live</span>',
                block,
                count=1,
            )
        return block

    html = re.sub(
        r'<a class="trophy[^"]*" href="[^"]*" title="(\d{3}) · [^"]*">.*?</a>',
        repl_trophy,
        html,
        flags=re.S,
    )
    # Write with real quotes (no escaped)
    WALL.write_text(html)


def main() -> None:
    hist_path = DATA / "concept-histories.json"
    histories = json.loads(hist_path.read_text())
    concepts = sync_concepts(histories)
    by_id = {c["id"]: c for c in concepts}

    for h in histories:
        slug = h["slug"]
        out_dir = CONCEPTS_DIR / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        page = concept_page(h, by_id[h["id"]])
        (out_dir / "index.html").write_text(page)

    update_wall(concepts)
    print(f"Generated {len(histories)} concept pages; wall updated.")


if __name__ == "__main__":
    main()
