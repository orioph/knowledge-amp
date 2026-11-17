# KA Timeline Layer — Event Format v0.1 (draft, 2026-11-17)

One shared event format that every KA feature reads and writes: the Seashell,
Vantasner, Inherit, Ka's archive, the fingerprint, Luci, Jinglia itself.
Each feature is a **lane**; **lineage links** cross lanes.

Model notes: ufotimeline.com gave us year lists, counted filters, People as
entries, and contribute/report buttons. The Seashell gives us what it lacks:
place, sources, ratings, lineage, and the three lines. Rule from the Display
Center: **no invented events — every event needs at least one source.**

## Fields

| field | required | meaning |
|---|---|---|
| `id` | yes | stable slug, e.g. `ev-1561-nuremberg-sky` |
| `title` | yes | short, our own words |
| `summary` | no | our own words; never copied text |
| `when` | yes | see *Time* below |
| `where` | no | place name, optional lat/lon, how exact |
| `people` | no | ids of People entries (`pp-…`), each with a role |
| `lane` | yes | which feature owns it: `seashell`, `vantasner`, `inherit`, `ka-archive`, `fingerprint`, `luci`, `jinglia` |
| `category` | yes | one main category (counted in filters) |
| `tags` | no | free tags |
| `sources` | yes, ≥1 | see *Sources* |
| `rating` | yes | see *Pedigree* — never true/false |
| `line` | yes | `seed` (untouched), `evolved` (validated, self-updating), `visitor` (user-modified) |
| `links` | no | lineage edges to other events — see *Lineage* |
| `media` | no | images, audio, video (paths or URLs) |
| `history` | yes | every change: who/what, when, which line |

## Time
Deep time and exact days must share one axis (the spiral is log-time).
```json
"when": {
  "start": "1561-04-14",      // ISO date, or a year like "-12000" for BCE
  "end": null,                // for spans
  "precision": "day",         // day | month | year | decade | century | millennium | epoch
  "uncertainty_years": 0,     // ± range; drives fuzz on every view
  "calendar_note": "Julian"   // optional
}
```

## Sources (sources first)
```json
"sources": [{
  "title": "…", "url": "…", "outlet": "…",
  "kind": "primary | secondary | testimony | document | book | media | lead",
  "accessed": "2026-11-17",
  "archived_copy": "https://web.archive.org/…",
  "found_via": "ufotimeline.com"   // leads are kept, but a lead alone can't rate above 'unverified'
}]
```

## Pedigree (the two wings)
```json
"rating": {
  "factual": 0.0,      // 0 = no evidence it happened as told … 1 = well documented
  "figurative": 0.0,   // 0 = literal claim … 1 = myth, symbol, story, art
  "confidence": "unverified | weak | moderate | strong",
  "rated_by": "evolved-run 2026-11-17T08:00 | D | visitor:<name>",
  "reason": "one line"
}
```

## Lineage (the Vetting Sentinel)
```json
"links": [
  {"to": "ev-…", "type": "derived_from"},
  {"to": "ev-…", "type": "echoes"},          // pattern rhymes across time or lanes
  {"to": "ev-…", "type": "contradicts"},
  {"to": "ev-…", "type": "first_appears_in"},
  {"to": "ev-…", "type": "same_as"}          // duplicates merged, both kept
]
```

## People entries (from ufotimeline's model)
`pp-<slug>`: name, roles (e.g. "Physics Professor", "witness", "author"),
lifespan `when`, sources, links to events.

## Views (all read the same files)
1. **Spiral** — log-time, deep past to now (the Seashell).
2. **Year list** — ufotimeline style, counted category filters; the plain way in.
3. **Lanes** — features side by side, lineage links drawn across.
4. **Map** — from `where`.
5. **People web** — from `people`.

## Storage
- `timeline/events/<lane>/<id>.json` — one file per event, so every change is
  a git commit (every version kept).
- `timeline/people/<id>.json`
- Contributions and broken-link reports → GitHub Issues on orioph/knowledge-amp,
  landing in the `visitor` line.
- The 8-hour evolve runs write only to the `evolved` line and log in `history`.

## Already exists — use, don't rebuild
- Knight Lab TimelineJS can render the year/lane view from a sheet.
- Wikidata supplies dated, located events with references — import as `lead`
  sources.
- New here: lineage links, the pedigree rating, the three lines.
