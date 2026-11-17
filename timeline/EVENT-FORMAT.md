# KA Timeline Layer — Event Format v0.2 (draft, 2026-11-17)

One event format every KA feature reads and writes. Each feature is a **lane**;
lineage links cross lanes.

**v0.2 is built on the Seashell's genome** (orioph/jinglia, branch `seashell`,
`toys/seashell/evolved/genome.json`, version 3, 182 entries) instead of beside it.
A Seashell genome is already a valid lane file. Everything below marked *new* is
optional, so nothing existing breaks. v0.1 (written before the genome was read)
is kept as `EVENT-FORMAT-v0.1.md`.

Model notes from ufotimeline.com: year lists, counted filters, People as
entries, contribute and broken-link buttons. Rule from the Display Center:
**no invented events — sources first.**

## Lane file = a genome
`timeline/lanes/<lane>.json`, same shape as the Seashell genome:
`name, kind, version, updated, time, strands, grades, entries, daughters`.
The Seashell lane stays where it lives (jinglia `seashell` branch) and is read
from there, not copied, until D says otherwise.

## Entry fields

| field | from | meaning |
|---|---|---|
| `id` | genome | stable slug |
| `name` | genome | short title |
| `year` | genome | decimal year (2026.36 ≈ May 2026); negative = BCE |
| `endYear` | genome | for spans |
| `strand` | genome | the lane's own category (counted in filters) |
| `grade` | genome | `doc` Documented record · `test` Testimony · `claim` Claim · `folk` Folklore & legend · `fic` Fiction |
| `weight` | genome | 1–5, size on the spiral |
| `person` | genome | true = a People entry (ufotimeline's People, already here) |
| `description` | genome | our own words |
| `links` | genome | ids; *new:* an item may also be `{"to": id, "type": …}` |
| `tags` | genome | free tags |
| `source` | genome | one URL; kept as is |
| `fingerprint` | Seashell EVOLVE.md | factual + figurative wings, origin, ancestors, mutations, purposes, corroboration, notes |
| `lane` | *new* | owning feature: `seashell`, `vantasner`, `inherit`, `ka-archive`, `fingerprint`, `luci`, `jinglia`; default = the file's lane |
| `precision` | *new* | `day · month · year · decade · century · millennium · epoch` |
| `uncertainty_years` | *new* | ± range; views draw it as blur |
| `where` | *new* | `{"name", "lat", "lon", "precision"}` — feeds the map |
| `sources` | *new* | list, when one `source` isn't enough (below) |
| `roles` | *new* | for `person` entries, e.g. "Physics Professor", "witness" |
| `line` | *new* | `seed · evolved · visitor` when an entry moves between lines |

### `sources` (when there's more than one)
```json
{"url": "…", "title": "…", "kind": "primary | secondary | testimony | document | book | media | lead",
 "accessed": "2026-11-17", "archived_copy": "https://web.archive.org/…", "found_via": "ufotimeline.com"}
```
A `lead` (e.g. found via ufotimeline or Wikidata) is kept but counts as 0 toward
`corroboration` until the original is read.

### Typed links (cross-lane lineage)
`derived_from · echoes · contradicts · first_appears_in · same_as · related`.
A plain id in `links` means `related`. `fingerprint.ancestors` stays the
authority for descent within the Seashell.

## Views (all read the same lane files)
1. **Spiral** — log-time (the Seashell's `time.scale`).
2. **Year list** — ufotimeline style, filters counted by strand and grade.
3. **Lanes** — features side by side, typed links drawn across.
4. **Map** — from `where`.
5. **People web** — `person` entries and their links.

## Lines and runs (unchanged from the Seashell)
`seed/` frozen · `evolved/` vetted only · `visitor/` contributions.
Contributions and broken-link reports → GitHub Issues on orioph/knowledge-amp.
Each 8-hour run proposes; nothing lands in `evolved/` without D's approval.

## Tools
`timeline/gaps.py <genome.json>` — reports what each lane is missing
(sources, fingerprints, places, era balance) as Markdown.

## Already exists — use, don't rebuild
- Knight Lab TimelineJS renders a year/lane view from a sheet.
- Wikidata: dated, located events with references → import as `lead` sources.
- New here: typed cross-lane links, the two-wing fingerprint on every lane, the three lines.
