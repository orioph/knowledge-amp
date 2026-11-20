"""Build atlas data for the Knowledge Amp Start toy.
Reads the KA seed dictionary (D's 2010-2026 writings, digested) and joins it with
what exists now (skills, toys, digests) and the chat sweep of 2026-11-17."""
import json, sys

ka = json.load(open(sys.argv[1]))
E = {e['id']: e for e in ka['entries']}

# Present-day pieces (from memory, repos and Desktop, 2026-11-17)
now = [
 ("n-jinglia","Jinglia","toy","A metasynth web experience: Wraywrai, wardrobe, songome, linguisynth, plidge recordings. D calls it a toy of KA.","built"),
 ("n-ww","Wraywrai","toy","Jinglia's origin character: synths words (wyrdulation), wardrobe looks, illoscopia lips.","built"),
 ("n-display","KA Display Center 0.02","toy","Petals of images left, facts right, bridges middle, etymology above the input, the first shell below; sources first.","partial"),
 ("n-seashell","Strange Temporal Seashell","toy","Log-time spiral of anomalous history; chosen as the model of the Vetting Sentinel: lineage, origin, 'factual vs figurative'.","partial"),
 ("n-kaskill","Ka skill","skill","Gathers all historical data into one verified archive with a catalog of every copy's origin.","partial"),
 ("n-visit","Visit + fingerprint","skill","Consented self-inspection of D's machines: assistive self-surveillance, owned by the user.","built"),
 ("n-digest","digest + dictionaries","skill","Reads a folder or site into a seed + pool dictionary. KA 66/499, Organelle 108/10,922, Wondercloud, Dreamknots, Ovum.","built"),
 ("n-bseek","bseek","skill","Maps the whole possibility space of an item across cost, value, risk, irony; steps people down.","built"),
 ("n-e3","e3 + JiSp","skill","Four tenders re-resolve a target and return one contender; JiSp sphere where organs share a warp-proof reading.","partial"),
 ("n-inherit","inherit","skill","Everything, the Contender question and the Babelfish: searching through lineages of genres and artists.","built"),
 ("n-mantic","Mantic Librarian, ia, CoSu","skill","Record-keeping organs: harvest every chat, keep history, advise next sessions.","built"),
 ("n-keys","Inception keys / Jinglian key","seed","Sticker, QR and punch-card keys whose reach is tracked and shown to their owner.","seed"),
 ("n-network","Jinglia network game","seed","Tokens to message and notify, groups, everyone's secret mission; cell-groups that invert problems.","seed"),
 ("n-income","Income Agents + Mac box service","seed","Agents and the 'customized box' business: the dividends side, paid on Thursday.","seed"),
 ("n-luci","Luci (voice to illustrated video)","seed","Turns spoken recordings into RSA-style whiteboard videos: D's hundreds of hours of talk made visible.","seed"),
 ("n-story","Metafiction story engine","seed","A self-rewriting story organism with genes, invariants and engine natures.","seed"),
 ("n-pkd","PKD + VALIS","seed","A library of sci-fi devices and metamethods, tended from above by VALIS. Not built.","seed"),
]
NOW = {n[0]: n for n in now}

# Organ / flow / word -> present-day embodiment (Claude's proposal, for D's judgment)
embody = [
 ("o-interface","n-display"),("o-constellator","n-display"),("o-etym","n-display"),("o-ce","n-display"),
 ("f-travel","n-display"),("f-periphery","n-display"),
 ("o-sentinel","n-seashell"),("f-newscast","n-seashell"),("f-photo","n-seashell"),("w-rhetological","n-seashell"),
 ("o-iar","n-kaskill"),("o-iar","n-visit"),("p-surveillance","n-visit"),("o-iar","n-mantic"),
 ("o-passforge","n-keys"),("o-sna","n-network"),("o-adventure","n-network"),("w-avatars","n-network"),
 ("o-pods","n-network"),("w-supergroups","n-network"),("f-trance","n-jinglia"),
 ("o-dividends","n-income"),("p-mindright","n-income"),("w-mindright","n-income"),
 ("f-searchas","n-inherit"),("f-swarm","n-e3"),("w-metaphy","n-jinglia"),("w-dreamdata","n-jinglia"),
 ("w-synth","n-jinglia"),("w-synth","n-ww"),("f-ecogame","n-bseek"),("p-dreaming","n-seashell"),
 ("s-video2013","n-digest"),("s-video2026","n-digest"),("s-video2026","n-luci"),("p-connotation","n-display"),
 ("p-verity","n-seashell"),("p-roles","n-network"),("p-burning","n-e3"),("w-hach","n-pkd"),
]

# Chat sweep, 2026-11-17: ~55 chats outside Projects (back to the first, 2026-09-19).
# Jinglia Project chats are not reachable from here; they were CoSu-harvested into orioph/jinglia.
chats = [
 ("2026-11-17","Interface dev KA","n-display","Built the KA Display Center 0.01-0.02; D's verdict: invented timelines are unacceptable, so sources first."),
 ("2026-11-17","UFO/UAP interactive timeline project","n-seashell","The Seashell became the Vetting Sentinel's model: vet anything by tracing its lineage, 'like infra solving a crime'."),
 ("2026-11-17","YouTube upload workflow","n-luci","Getting D's hundreds of hours of video and audio out into the channels Jinglia and Signals for Intelligence."),
 ("2026-11-17","Meta B-seek product research","n-bseek","bseek turned on itself: mapping the space before directing within it."),
 ("2026-11-16","System fingerprint and skill setup","n-visit","Visit and Ka born; Ka named as the gatherer of all historical data."),
 ("2026-11-16","Local mirror golden safety","n-mantic","Every version kept in real storage: 'I am not the repository.'"),
 ("2026-11-16","Mac Logic Files recovery / investigation","n-kaskill","Recovering scattered music work: the 8 TB duplicated archive problem in miniature."),
 ("2026-11-16","Auren investment and deleting E2","n-e3","Retired the always-on pre-check; kept the skills that learn every run."),
 ("2026-11-16","QuickTime audio routing fix","n-visit","Fingerprint growth: the audio rig."),
 ("2026-11-15","Mac mini backup drive options","n-kaskill","Sizing the archive's home: capacity over speed."),
 ("2026-11-15","Toothbrush substance and hygiene protocol","n-bseek","Alchemica: a prescriptionist dictionary, the same seed+pool shape as KA."),
 ("2026-11-15","Infrared bath mat","n-bseek","A bseek run."),
 ("2026-11-15","Deleted chat recovery","n-mantic","Chats are workspaces, never the only copy."),
 ("2026-11-13","Custom computer setup business","n-income","D and J: 'Jinglia is a toy of it. The box is a toy of it.' A pod of two."),
 ("2026-11-13","Oscilloscope nematode lips visualization","n-ww","Illoscopia; Loopscape dictionary; judging feature-by-feature, not whole toys."),
 ("2026-11-12","Reminan sphere manifold","n-e3","JiSp: a shared, warp-proof reading organs can hold. PKD and VALIS named."),
 ("2026-11-12","Inherit3 skill design","n-inherit","Searching through lineages of works: 'searching as someone else'."),
 ("2026-11-12","Garbled text requests","n-ww","Posarium; principle 'Stay on the prowl': every feature learns from every other."),
 ("2026-11-11","Touchless task completion","n-mantic","Batch decisions into one round; the night works while D sleeps."),
 ("2026-11-09","Snakespeak seed prompt","n-jinglia","Glossolaliary, songome, word-genomes."),
 ("2026-11-09","Vantasner Danger Pipe project","n-story","A warning generator plus a timeline: trope lineage as play."),
 ("2026-11-06","RSA-style prompt-to-video demo","n-luci","Speech made into illustrated thought."),
 ("2026-11-03","Video rompler for mixing and morphing","n-jinglia","Morphing media as a synth."),
 ("2026-11-02","Silicon planet story seed","n-story","A story that rewrites itself per reader: genes, invariants, a witness always present."),
 ("2026-10-18","Podcast title ideas","p-dreaming","D's talk: time as relation, machines make 'dead time', the mind as a vehicle for traveling."),
 ("2026-10-03","Godel's incompleteness and complex systems","o-sentinel","No system certifies itself: vetting must come from lineage and other systems, never self-declared authority."),
 ("2026-09-23","Cassirer, The Intuition of Time","p-dreaming","Memory as forward-directed and symbolic, not storage."),
 ("2026-09-19","Hyperstructures and nonphysical aspects of cognition","p-relation","Distributed cognition, noosphere; D: interiority first, intelligence between minds."),
 ("2026-09-21","Hiding domain registration details","o-server","The one-way barrier in miniature: showing the net a 'no one' face."),
 ("2026-10-30","Claude desktop app data access","o-server","Consent and scope: what may watch you, and who keeps what it sees."),
]

lineage = [
 ("2003","toyMaker contact","The KA is sketched to D by the NHI consortium toyMaker (date confirmed by D, 2026-11-17)."),
 ("2002-2016","organelle.org","'New Ways of Knowing': essays, glossaries, an oracle; about 547,000 words of D's writing."),
 ("2003","Systems Science sketch","Hand-drawn map from galactic to cellular to social systems, kept in the KA folder."),
 ("2013","Sketching The Knowledge Amp (video)","29:55, one take to camera: 'it collectively magnifies the intelligence of human users who touch data'."),
 ("2010s","Scrivener drafts","Adaptive Heuristics / Active Knowledge Modulants; the Knowledge Amp; Notes, Quotes, Principles."),
 ("~2023-2025","The Intelligence Amp (IA.docx), KA 1.docx, RK.docx","The organs written out: browser, Passforge, Data democracy, Vetting Sentinels."),
 ("2026-09-19","First chat with Claude","Within weeks: hyperstructures, Godel, Cassirer on time."),
 ("2026-10","Jinglia begins","D's 'very first project': a toy of KA."),
 ("2026-11-07","GitHub: orioph/jinglia","Every version kept in real storage."),
 ("2026-11-12","e2/e3, JiSp, Loopscape","Skills that learn every run."),
 ("2026-11-16","Ka, Visit, digests, the 2026 talk","KA folder digested: 66 seed entries, 499 in the pool. Organelle: 108 / 10,922."),
 ("2026-11-17","Seashell + Display Center; this chat","Knowledge Amp gets its own home. This is the original chat."),
]

nodes, links = [], []
nodes.append(dict(id="ka", label="Knowledge Amp", kind="root", gist=E['ka']['gist'], status="core"))
for e in ka['entries']:
    if e['kind'] in ('principle','organ','flow','word') :
        nodes.append(dict(id=e['id'], label=e['name'], kind=e['kind'], gist=e.get('gist',''),
                          quote=e.get('quote',''), src=e.get('src',{}).get('path',''), status="idea"))
        links.append(dict(s="ka", t=e['id'], k="has"))
# sources that present pieces embody (the 2013 and 2026 videos) become nodes too (fix 2026-11-20)
for sid in dict.fromkeys(s for s,t in embody if E.get(s,{}).get('kind')=='source'):
    e=E[sid]
    nodes.append(dict(id=sid, label=(e.get('aka') or [e['name']])[0], title=e['name'], kind="source", gist=e.get('gist',''), src=e.get('src',{}).get('path',''), url=e.get('url',''), status="source"))
    links.append(dict(s="ka", t=sid, k="has"))
for n in now:
    nodes.append(dict(id=n[0], label=n[1], kind="now", sub=n[2], gist=n[3], status=n[4]))
for s,t in embody:
    links.append(dict(s=s, t=t, k="embodied"))
# status of an idea = best status of what embodies it
rank = {"built":3,"partial":2,"seed":1}
for nd in nodes:
    if nd['kind'] in ('principle','organ','flow','word'):
        st = [NOW[t][4] for s,t in embody if s==nd['id']]
        nd['status'] = max(st, key=lambda x: rank[x]) if st else "unbuilt"
for i,c in enumerate(chats):
    links.append(dict(s="c%d"%i, t=c[2], k="chat"))
data = dict(nodes=nodes, links=links,
            chats=[dict(id="c%d"%i, date=c[0], title=c[1], node=c[2], gist=c[3]) for i,c in enumerate(chats)],
            lineage=[dict(when=a,title=b,gist=c) for a,b,c in lineage])
json.dump(data, open(sys.argv[2],'w'), indent=1, ensure_ascii=False)
cnt = {}
for nd in nodes: cnt[nd['status']] = cnt.get(nd['status'],0)+1
print(len(nodes), "nodes", len(links), "links", cnt)
