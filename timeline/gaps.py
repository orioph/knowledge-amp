"""Gap report for a KA timeline lane (a Seashell-shaped genome).

Usage: python3 gaps.py <genome.json> [lane-name]
Prints Markdown: sourcing (and source kinds), fingerprints (researched vs partial), places,
precision, the telling block, era balance, and the next entries to work on.
"""
import json, sys, collections

path = sys.argv[1]
lane = sys.argv[2] if len(sys.argv) > 2 else "lane"
g = json.load(open(path))
E = g["entries"]
n = len(E)


def pct(k):
    return f"{k}/{n} ({100 * k // max(n, 1)}%)"


def has_source(e):
    return bool(e.get("source") or e.get("sources"))


sourced = sum(has_source(e) for e in E)
fp = sum("fingerprint" in e for e in E)
fp_res = sum((e.get("fingerprint") or {}).get("factual") is not None for e in E)
tell = sum(bool(e.get("telling")) for e in E)
kinds = collections.Counter(e.get("source_kind", "unrecorded") for e in E if has_source(e))
one_src = [e for e in E if has_source(e) and len(e.get("sources") or [e.get("source")]) == 1]
where = sum("where" in e for e in E)
prec = sum("precision" in e for e in E)
people = sum(bool(e.get("person")) for e in E)
ids = {e["id"] for e in E}
broken = sorted({l if isinstance(l, str) else l.get("to")
                 for e in E for l in e.get("links", [])} - ids)

eras = [("before 10,000 BCE", -1e9, -10000), ("10,000 BCE–0", -10000, 0),
        ("1–1799", 0, 1800), ("1800–1946", 1800, 1947),
        ("1947–1999", 1947, 2000), ("2000–now", 2000, 1e9)]
era_n = [(name, sum(lo <= e["year"] < hi for e in E)) for name, lo, hi in eras]

print(f"# Gap report: {lane} ({g.get('name', '')}, v{g.get('version', '?')}, {g.get('updated', '')})\n")
print(f"- Entries: {n} (people: {people})")
print(f"- **With a source: {pct(sourced)}**  ← sources-first rule")
print(f"- With a fingerprint: {pct(fp)} (researched, both wings: {pct(fp_res)})")
print(f"- With a `telling` block: {pct(tell)}")
print(f"- Source kinds: " + ", ".join(f"{k} {v}" for k, v in kinds.most_common()))
print(f"- Resting on a single source: {pct(len(one_src))}")
print(f"- With a place (`where`): {pct(where)}")
print(f"- With date precision: {pct(prec)}")
print(f"- Links pointing to missing ids: {len(broken)}" + (f" ({', '.join(broken[:10])})" if broken else ""))
print("\n## By grade (unsourced in brackets)\n")
gn = g.get("grades", {})
for k, c in collections.Counter(e["grade"] for e in E).most_common():
    uns = sum(e["grade"] == k and not has_source(e) for e in E)
    print(f"- {gn.get(k, k)}: {c} [{uns}]")
print("\n## By strand (unsourced in brackets)\n")
sn = g.get("strands", {})
for k, c in collections.Counter(e["strand"] for e in E).most_common():
    uns = sum(e["strand"] == k and not has_source(e) for e in E)
    print(f"- {sn.get(k, {}).get('n', k)}: {c} [{uns}]")
print("\n## By era\n")
for name, c in era_n:
    print(f"- {name}: {c}")
print("\n## Unsourced `doc` entries (fix these first)\n")
for e in E:
    if e["grade"] == "doc" and not has_source(e):
        print(f"- `{e['id']}` {e['name']} ({e['year']})")

print("\n## Telling\n")
for facet in ("medium", "check", "custody"):
    c = collections.Counter((e.get("telling") or {}).get(facet) for e in E if (e.get("telling") or {}).get(facet))
    print(f"- {facet}: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
for facet in ("forecast", "period", "readings", "template"):
    ids_f = [e["id"] for e in E if (e.get("telling") or {}).get(facet)]
    print(f"- {facet}: {len(ids_f)}" + (f" ({', '.join(ids_f)})" if ids_f else ""))
print("\n## Next to work on\n")
todo = [e for e in E if (e.get("fingerprint") or {}).get("factual") is None]
todo.sort(key=lambda e: (-e.get("weight", 1), e["year"]))
print(f"- Without a researched fingerprint ({len(todo)}), heaviest first: " + ", ".join(f"`{e['id']}`" for e in todo[:20]) + (" …" if len(todo) > 20 else ""))
nop = [e for e in E if not e.get("person") and "where" not in e]
print(f"- Events without a place ({len(nop)}): " + ", ".join(f"`{e['id']}`" for e in nop[:25]) + (" …" if len(nop) > 25 else ""))
