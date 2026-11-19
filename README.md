# knowledge-amp
Core of KA Project

## Knowledge Amp

The Knowledge Amp (KA) is D's core idea: a new internet layer where using data makes people
and groups more intelligent, sketched to him by toyMaker. Jinglia, the Seashell, Ka and the
other skills are toys and organs of it.

- **Origin chat:** "Knowledge Amp Start" (listed as "Knowledge Amp prototyping"), 2026-11-17, now inside the claude.ai Project "Knowledge Amp".
- **Toy:** Knowledge Amp Start, https://claude.ai/artifact/MKaXjS1U4Dr7vSrEH2Pa5k
  (Map, Lineage, Examples).
- **Home:** this repo. The first copy also stays on branch `knowledge-amp-start` of orioph/e2.

## What's here

| File | What it is |
|---|---|
| `atlas/atlas.json` | 52 ideas from the writings (principles, organs, flows, words), 17 present pieces, 30 chats, 12 lineage moments, with links. |
| `atlas/build_data.py` | Rebuilds `atlas.json` from `records/ka/dict-ka.json` in orioph/jinglia. The organ-to-present links and the chat abstracts are written in it. |
| `atlas/template.html` | The toy's page; `atlas/index.html` = template + atlas. |
| `timeline/` | **Timeline layer v0.3 (draft)**: one event format for every feature, built on the Seashell genome (`EVENT-FORMAT.md`; v0.1 and v0.2 kept). v0.3 adds `source_kind`, `precision_basis`, `where.basis` and the `telling` block. `gaps.py` reports a lane's gaps and next entries; latest report `gaps-seashell-2026-11-19.md`: 232 entries, all sourced (120 primary, 112 secondary), 109 researched fingerprints, 115 places, 182 tellings. Earlier reports kept. |
| `barrier/index.html` | **One-Way Barrier 0.01**, the first organ prototype (the server's barrier, layers, seven chambers). Toy: https://claude.ai/artifact/N3gpDgZetcDJ1RckLffNDT. Each version is also kept as `barrier/vX.html`; `barrier/frames/` holds the checked screenshots. |
| `analogia/` | **Analogia 0.1**: the analogy gesture (A : B \| C : ?, and chains) with its process clarify, represent, question, await, then evolve. Master copy is `rhetoric/analogia_dict.json` in orioph/jinglia; toys `cocoon/` (https://claude.ai/artifact/DWckGQbynR78uCCjGQtqZ2) and `bees-and-x/` (https://claude.ai/artifact/24Za4AjBAhEUZUpF2Zi6ek). |

## Sources used (nothing re-digested)

- KA seed dictionary (66 entries) from orioph/jinglia `records/ka/`, itself a digest of ~/Desktop/KA.
- Spot reads of ~/Desktop/KA: Knowledge Amp.scriv, KA 1.docx, IA.docx, RK.docx, the 2013 transcript.
- Organelle digest README (organelle.org, 2002-2016).
- Chat sweep: every chat outside Projects, 2026-09-19 to 2026-11-17 (about 55). Jinglia Project chats can't be seen from outside the Project; they were CoSu-harvested into orioph/jinglia.

## Status counts (proposed; D to judge)

Of 52 ideas: 8 built, 15 partly built, 11 seeded, 18 idea only.
Unbuilt organs include the Server / One-Way Barrier. Social organs (Pods, Trance,
superGroups, Passforge, Data dividends) are seeds at most.

## Requests

Requests, open questions and builds live in **GitHub Issues** on this repo (labels: `request`, `organ`, `for D`), not in a REQUESTS.md file.

## Open questions for D

1. toyMaker date: settled, 2003 (D, 2026-11-17).
2. Are the organ-to-present links right? (e.g. Seashell = Vetting Sentinel, bseek = nature-cost lens)
3. Done 2026-11-17: this repo and the claude.ai Project "Knowledge Amp" (account memory on).

## Done, timeline dev (2026-11-19)

- Seashell lane (jinglia `seashell` branch) brought to genome v5: the 12 flags, runs 1631/0038 (17 Nov) and 0841/1629/0028/0829 (19 Nov) applied; Voyager 1 one light-day added; six sourcing mutations written; every "from general knowledge" line in the run logs checked against search results (two corrections). Two passes ran in parallel that morning; the second (telling block, checks) sits on top of the first. Logs: `toys/seashell/runs/2026-11-19-apply.md` and `2026-11-19-0356-apply.md` on that branch.
- Event format v0.3 with the `telling` block; `gaps.py` extended. (The first pass's `for-knowledge-amp/event-format-v0.3.patch` on the jinglia branch is superseded by this.)

## Next (handoff, 2026-11-17)

Where things stand: repo, Project (account memory on), atlas toy and the e2 backup copy are all in place. The origin chat is long; start new work in a fresh chat in the Project.

Start with:
1. D checks the map's organ-to-present links (Map view in the toy) and says which are wrong.
2. "Make req's": D to say which was meant: a REQUESTS.md log like Jinglia's, or the requirements for the next build.
3. Pick the first unbuilt organ to prototype: the Server / One-Way Barrier, or the social side (Pods, Trance, Passforge, superGroups).

Don't redo: ~/Desktop/KA and organelle.org are already digested (orioph/jinglia `records/ka/`, `records/reforge/digests/`). The KA Display Center toy already covers the browser organ (orioph/jinglia `toys/ka-display-center/`).

## Done, KA first day (2026-11-17, second chat)

- The request log is GitHub Issues: #1 One-Way Barrier, #2 check the map's links (for D), #3 social organs.
- First organ prototype: One-Way Barrier 0.01 in `barrier/`, built from IA.docx paras 43-59 and 110-116.
