#!/usr/bin/env python3
"""
Add established-vocabulary keywords to published Zenodo records.

WHY. Discovery is demand-driven: nobody searches a term they do not know exists,
so a record carrying only this corpus's coined vocabulary is findable mainly by
people who already know the work. 27 of the 63 defensive publications had no
`**Keywords:**` line and so deposited with three keywords — category, tier and
document type. This adds terms drawn from established literature.

WHAT IT DOES NOT TOUCH. The papers. Keywords go into the Zenodo record's metadata
only: no SHA-256 change, no OpenTimestamps rotation, no .rN proof. That is the
whole reason this lever is free.

Existing keywords are preserved and merged, never replaced. Terms are descriptive
— they name a field the paper speaks into, never a claim it proves.

⚠️ SIDE EFFECT WORTH KNOWING. Editing and republishing re-registers the DOI with
DataCite. If DataCite ORCID Auto-Update is enabled, that can push these works to
the ORCID record as DataCite-sourced entries. ORCID groups works by identifier, so
a push carrying the same DOI already on the record groups silently; one carrying
the *other* DOI of the concept/version pair appears as a duplicate. Check the
ORCID record a day after running and prune if needed — ORCID entries are
deletable, unlike DOIs.

    ./scripts/zenodo-keywords.py --dry-run
    ./scripts/zenodo-keywords.py
"""

import argparse
import importlib.util
import json
import pathlib
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("zd", ROOT / "scripts/zenodo-deposit.py")
zd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zd)

# Approved 2026-08-15. Sourced from each paper's title, subtitle and abstract;
# established literature vocabulary only, no coined terms (those are already in
# the 36 records that carry their own Keywords line and are not touched here).
# Signature 8 note: giving-is-a-gift-too uses redistribution / dignity / mutual
# aid / welfare economics rather than "poverty" — the established terms that name
# the field without rendering a lack.
KEYWORDS = {
 "agi-monks-caretaker-not-ordained":["AI and religion","religious authority","monasticism","comparative religion","institutional design","Theravada Buddhism","technology and religion","AI governance"],
 "aura-gated-anonymous-mate-selection":["online dating","mate selection","assortative mating","reputation systems","prosocial behavior","sexual selection","anonymity","matching markets","trust and safety","catfishing"],
 "b-links-signed-provenance":["content provenance","content authenticity","digital signatures","link preview","Open Graph protocol","proof of personhood","misinformation","web metadata standards"],
 "brand-identity-as-architecture":["brand identity","visual identity","design systems","semiotics","liveness detection","biometric authentication","naming conventions","trademark"],
 "buddha-ai-living-tipitaka":["Buddhist studies","Pali canon","Tipitaka","digital humanities","canon formation","oral tradition","large language models","AI and religion","religious text corpora"],
 "cakkavatti-alignment-charter":["AI alignment","value alignment","constitutional AI","machine ethics","Buddhist ethics","Digha Nikaya","AI governance","normative specification"],
 "certification-by-circulation":["software certification","verifiable credentials","revocable credentials","trust and reputation","open source governance","end-user programming","quality assurance"],
 "embodied-advocate-pageant":["AI governance","succession planning","institutional design","human oversight","selection mechanisms","autonomous systems","organizational legitimacy"],
 "gift-tag-time-reveal":["near-field communication","QR codes","time-lock encryption","gift giving","ubiquitous computing","tangible interaction","delayed disclosure"],
 "giving-is-a-gift-too":["dignity","redistribution","charitable giving","anonymity in giving","mutual aid","economic anthropology","welfare economics","reciprocity"],
 "gratitude-as-cooperation-substrate":["multi-agent systems","cooperative AI","indirect reciprocity","evolution of cooperation","reputation systems","game theory","agent communication"],
 "gratitude-riding-currency-tag":["complementary currency","banknotes","cash","monetary systems","financial inclusion","physical-digital coupling"],
 "incommensurability-preserving-coupler":["complementary currency","dual currency systems","mechanism design","market design","incommensurability","non-fungibility","exchange mechanisms"],
 "mechanical-heart":["more-than-human design","multispecies design","animal welfare","environmental ethics","non-human agency","Buddhist ethics","artifact design"],
 "multi-family-membership":["data modeling","identity management","multi-tenancy","access control","database schema design","organizational succession"],
 "need-compiled-questlines":["gamification","serious games","prosocial games","quest design","needs assessment","automated planning","incentive design"],
 "proof-of-coordinate":["decentralized identity","digital identity","sybil resistance","trusted execution environment","hardware security","agent identity","individuation"],
 "respiratory-biofeedback-contemplative-guidance":["biofeedback","heart rate variability","wearable computing","meditation","contemplative science","mindfulness","digital health","respiratory rate"],
 "safety-companion-pack-watch":["personal safety","duress detection","mesh networking","peer-to-peer networks","ambient assisted living","family safety","dead man's switch"],
 "studio-b-short-phase-bridge":["privacy controls","publishing workflow","content lifecycle","layer 2 blockchain","creator economy","data migration"],
 "the-gift-operation":["gift economy","reciprocity","economic anthropology","generalized exchange","pay it forward","prosocial behavior","Marcel Mauss"],
 "the-omitted-clause":["technological unemployment","automation","Buddhist economics","Digha Nikaya","social welfare policy","Cambodia","cybercrime"],
 "the-rethank-multiplier":["network effects","velocity of money","economic modeling","scaling","throughput","reciprocity","saturation"],
 "tipitaka-alignment-substrate":["AI alignment","value alignment","machine ethics","value learning","Buddhist ethics","Pali canon","wellbeing","suffering"],
 "two-layer-reward":["mechanism design","matching markets","resource allocation","needs assessment","recommender systems","welfare economics","preference elicitation"],
 "verified-human-anonymous-local-giving":["Bluetooth Low Energy","proximity detection","biometric verification","anonymous payments","privacy-preserving protocols","mobile payments","liveness detection"],
 "zero-point-game":["infinite games","cooperative game design","game design","Buddhist economics","dana","zero-sum games","AI arbitration","planetary boundaries"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", metavar="SLUG")
    args = ap.parse_args()

    state = json.loads(zd.STATE_LIVE.read_text())
    targets = {k: v for k, v in KEYWORDS.items()
               if k in state and state[k].get("published")
               and (not args.only or k == args.only)}
    print(f"{len(targets)} record(s) to enrich\n")

    if args.dry_run:
        for s, kw in sorted(targets.items()):
            print(f"  {s}\n    + {', '.join(kw)}")
        print("\nDRY RUN — nothing sent.")
        return

    api = zd.Zenodo(zd.get_token(), False)
    ok = failed = 0
    for slug, add in sorted(targets.items()):
        dep_id = state[slug]["deposition_id"]
        try:
            api._req("POST", f"/deposit/depositions/{dep_id}/actions/edit")
            dep = api.get(dep_id)
            meta = dep["metadata"]
            before = list(meta.get("keywords") or [])
            # Merge, preserving order and dropping case-insensitive repeats.
            seen = {k.lower() for k in before}
            meta["keywords"] = before + [k for k in add if k.lower() not in seen]
            api.set_metadata(dep_id, meta)
            api.publish(dep_id)
            print(f"  ✓ {slug}  {len(before)} → {len(meta['keywords'])}")
            ok += 1
        except SystemExit:
            try:
                api._req("POST", f"/deposit/depositions/{dep_id}/actions/discard")
                print(f"  ✗ {slug}: failed, edit discarded")
            except SystemExit:
                print(f"  ✗✗ {slug}: FAILED AND STILL OPEN — "
                      f"https://zenodo.org/deposit/{dep_id}")
            failed += 1
        time.sleep(0.4)

    print(f"\n{ok} enriched, {failed} failed")


if __name__ == "__main__":
    main()
