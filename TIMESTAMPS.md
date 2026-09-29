### 2026-09-29 (early) — the owed rotations, the two riders, and P-ZP1's chain (founder: *"check bitcoin now; the watcher may be broken"*)

| paper | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **a-promise-that-cannot-grow** *(+ riders: the bondage sentence §1, the Coupler lineage §18)* | `.ots` → `.r1.ots` (Bitcoin-complete); new proof, calendar-only | `2026-09-29.sha256` | ⏸ held (A257) | ⏸ HELD |
| **prediction-register** *(P-ZP1)* | `.ots` → `.r15.ots` (Bitcoin-complete); new proof, calendar-only | `2026-09-29.sha256` | 10.5281/zenodo.23033184 *(new version)* | 2.5.27 |

⚠️ **The deferral of 2026-09-28 was decided on a BLIND probe.** `ots` is not on the session shell's PATH (the client lives in `~/.cache/ots-venv/bin/`), and the check that reported "0 Bitcoin attestations", like the background watcher after it, sent the command-not-found error to `/dev/null`. The founder asked for a direct check; a known-good control proof then read 3, and both retiring proofs upgraded to Bitcoin-complete on the first real run. Whether they were complete at 21:00 is unknown.

### 2026-09-28 (night) — `a-promise-that-cannot-grow` (new DP, polish r1 + founder rulings 3–5) and the prediction register (P-PM1–3) (founder: *"approve"*)

| paper | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **a-promise-that-cannot-grow** | ⏳ rotation OWED: the retiring `.ots` (`2712bb93…`, first push) was calendar-only at chain time — rotate to `.r1.ots` once Bitcoin-complete, then stamp | `2026-09-29.sha256` | ⏸ held — first deposit waits on the A257 census rerun (conjuncts h–k) | ⏸ HELD (`holds.json`, review by 2026-10-28) |
| **prediction-register** | ⏳ rotation OWED (retiring proof `799f93d2…` calendar-only) → `.r15.ots` | `2026-09-29.sha256` | 10.5281/zenodo.23030493 *(new version)* | 2.5.26 |

⚠️ Both leg-1 rotations are deferred, not skipped: an incomplete proof archived is an incomplete proof forgotten. The TSA leg covers today's bytes meanwhile. ⚠️ **Later the same night the register gained P-ZP1 (`b339357`), so 10.5281/zenodo.23030493 and index 2.5.26 cover the P-PM text, not the current one: the register's next `/publish` run owes legs 1–4 together (rotation, TSA, a new Zenodo version, index).**

### 2026-09-28 (evening) — first deposits of the two mechanisms, after their FULL censuses (founder: *"do open items"*)

Both full censuses were pre-registered publicly before the first query (`74851d1` machine-dana · `9bf6a3d` counts-check) and
pass `census.py gate`. Each paper folded its census in: Prior-Art Statement, survivor, and narrowed claims (machine-dana 3–6,
counts-check 1, 2, 4, 5, 6). Machine-dana gained a Keywords line before its mint. Counts-check: an L22 breach found and closed
(Khmer script in two places, now described by Unicode names).

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **machine-dana-from-share-to-vow** | ⏳ rotation deferred — retiring proof calendar-only; text `8af30fe81b30…` | `2026-09-28.sha256` (fourth run) | **first deposit** `10.5281/zenodo.23020669` | 2.5.25 (hold lifted) |
| **the-counts-check** | ⏳ rotation deferred — retiring proof calendar-only; text `edc3fa58718e…` | `2026-09-28.sha256` | **first deposit** `10.5281/zenodo.23020671` | 2.5.25 (hold lifted) |

`holds.json` is now empty.

### 2026-09-28 (later) — first deposits of the two studies; two rulings into machine-dana (founder: *"do open items"* → *"Bar it"* · *"Mechanism test only"* · *"Reword now, deposit"*)

The census gate's priority list was corrected before acting: a census reported as *"not found in <aperture> on <date>"* (which the
2026-09-13 rule REQUIRES) and a citation of the *nearest prior instance* are not priority claims. With the list corrected both
studies pass as written; the only rewording was one stale sentence in the discrete-QG paper ("a full census is owed").

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **the-vibhajjavadin-view-of-time** | covered (`b57668357f9c…`, calendar-only at deposit) | `2026-09-28.sha256` | **first deposit** `10.5281/zenodo.23020016` | 2.5.24 (hold lifted) |
| **abhidhamma-and-discrete-quantum-gravity** | ⏳ rotation deferred — the retiring proof (`dd2c03deb071…`) is calendar-only; new text `0137cadb9df6…` | `2026-09-28.sha256` (second run) | **first deposit** `10.5281/zenodo.23020021` | 2.5.24 (hold lifted) |
| **machine-dana-from-share-to-vow** | ⏳ rotation deferred — the retiring proof (`bbf2d5373cc4…`) is calendar-only; new text `96bd829b55ab…` | `2026-09-28.sha256` (second run) | ⏸ held (full census running) | ⏸ held |

⚠️ Leg 4's first CI run failed on the README counts (built but not committed); fixed and re-dispatched without a new version.

### 2026-09-28 — polish r1 revisions of the four 9/27 papers + the prediction register (P-MD1a) (founder: *"approve all"*)

One batched revision each after the first cold-review round (`TH/notes/reviews/<slug>/2026-09-28-r1/`). Two papers carry the new
`kind: study` (ruled 2026-09-28) and a `## Findings disclosed` section; two carry `kind: mechanism`. **Legs 3–4 stay HELD for all
four** (`holds.json`, re-reasoned): the mechanisms await their FULL census; the studies assert priority, so `census.py gate` wants
a LITERATURE census or reworded priority sentences (ruled 2026-09-28). The register ran the full chain.

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r14.ots` (Bitcoin-complete, 2 attestations); new `799f93d20a7c…` *(calendar-only at stamping)* | `2026-09-28.sha256` (covers `799f93d20a7c…`) | `10.5281/zenodo.23019376` | 2.5.23 |
| **machine-dana-from-share-to-vow** | `.ots` → `.r2.ots` (upgraded, then Bitcoin-complete); new `bbf2d5373cc4…` | `2026-09-28.sha256` | ⏸ held (full census) | ⏸ held |
| **the-counts-check** | `.ots` → `.r1.ots` (Bitcoin-complete); new `ebf0b006af25…` | `2026-09-28.sha256` | ⏸ held (full census) | ⏸ held |
| **the-vibhajjavadin-view-of-time** | `.ots` → `.r1.ots` (Bitcoin-complete); new `b57668357f9c…` | `2026-09-28.sha256` | ⏸ held (literature census or reword) | ⏸ held |
| **abhidhamma-and-discrete-quantum-gravity** | `.ots` → `.r1.ots` (Bitcoin-complete); new `dd2c03deb071…` | `2026-09-28.sha256` | ⏸ held (literature census or reword) | ⏸ held |

Site modules regenerated (all generated, not hand-authored; ids kept, `+findings-disclosed` ×2, `+appendix-a` on the counts check,
one renamed §6 id on the Vibhajjavādin paper with no inbound anchors; the register's `sig-ok` markers restored by hand again).

### 2026-09-27 — wave 3 SUBMITTED to TDCommons (mirrors, not revisions; founder: *"1: yes"*)

The ten wave-3 papers, one form each through `ir_submit.cgi`, inventor Thon Ly (institution blank), CC BY 4.0, each confirmed
on its confirmation page (the server's echo of title, inventor and the full abstract, 241–250 words) and recorded in
`submitted/manifest.json`: co-presence-gated-redemption · the-rethank-multiplier · two-layer-reward · multi-family-membership · the-wager-that-isnt · steward-routed-alms · dual-currency-reciprocity · the-game-that-graduates-you · the-sport-that-says-your-name · studio-b-short-phase-bridge. My Account after the tenth: 33 submissions — 21 posted, 10 under
review, 2 `queued_for_update` (buddha-ai-living-tipitaka, capacity-funded-human-disbursed-ai-alignment; recheck Monday
2026-09-28, founder: *"wait until monday"*), no duplicates.

### 2026-09-27 (late night) — the prediction register: outcomes for P-FA2a, P-FA2b, P-FA5; the deferred rotation done (founder: *"do 1 and 2"*)

Outcomes written beside the unchanged wording (all three confirmed); the P-FA row names `the-counts-check`. **The deferred leg 1
is closed:** the retiring proof confirmed on Bitcoin at 17:34 PDT (watched in the background), was upgraded, and rotated to
`.r13.ots`; this revision stamped fresh. ⚠️ The intermediate revision (1de70d8, which registered P-FA2a/2b/5) therefore carries
no OpenTimestamps proof of its own — it is attested by RFC 3161 (`2026-09-27.sha256`) and Zenodo `10.5281/zenodo.23003593`.
The `.ots.bak` blocker that forced the deferral is fixed in all five `ots-upgrade.sh` (clear stale backups BEFORE the loop).

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r13.ots` (Bitcoin-complete, 1 attestation); new *(calendar-only at stamping)* | `2026-09-28.sha256` (UTC day of the run; covers `a488f2616ded…`) | `10.5281/zenodo.23004359` | 2.5.20 |

### 2026-09-27 (night) — the prediction register: P-FA2a, P-FA2b, P-FA5 registered before rung 3; outcomes for P-FA1, P-FA4, P-FA1b, P-FA3 (founder: *"go"*)

Three predictions registered before any Dhammasaṅgaṇī text was read (first public in `SiliconWat/formal-abhidhamma`
`PREREGISTRATION-2026-09-27b.md`, commit `f4a26e5`, GitHub push 2026-09-27T23:04:29Z); outcomes written beside the unchanged
wording of four earlier ones. Total 109 → 112, reconciled (112 = 112). ⚠️ **LEG 1 DEFERRED, deliberately:** the retiring proof
(`.ots`, stamped this evening) was still calendar-only, and rotating it would archive an incomplete proof. The current `.ots`
therefore covers the PREVIOUS text until `/ots` confirms it and the rotation to `.r13.ots` + a fresh stamp are done — ⏳ owed.
⚠️ **Found: `ots upgrade` leaves a `.ots.bak`, and the NEXT upgrade of that file then silently refuses to write** ("Could not
backup timestamp: … already exists") — hit twice today on the register; `ots-upgrade.sh` does not handle it; two other stale
`.bak` files remain in this tree (not touched). Site module regenerated (ids identical; `sig-ok` restored by hand again).

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | ⏳ rotation deferred (retiring proof calendar-only) | `2026-09-27.sha256` (covers `9297130034c2…`) | `10.5281/zenodo.23003593` | 2.5.18 |

### 2026-09-27 (evening) — the prediction register: P-FA1, P-FA1b, P-FA2, P-FA3, P-FA4, the Formal Abhidhamma predictions (founder: *"do all 8"* · *"do rung 1"* · *"do what's best"*)

Five predictions registered in *Instrumented but outside the core*, first public minutes earlier in the pre-registration of the
public repository `SiliconWat/formal-abhidhamma` (commit `259e5e8`, GitHub push record 2026-09-27T22:07:02Z, before any code):
whether general cetasika rules generate the 89/121 citta-types (P-FA1, 0.6), with ≥3 narrow exceptions (P-FA1b, 0.7); the canon
alone under-determined (P-FA2, 0.65); Khmer = CST (P-FA3, 0.85); compression below 0.5 (P-FA4, 0.5). Total 104 → 109, reconciled by
the index build (109 = 109). ⚠️ The retiring proof was calendar-only; upgraded to Bitcoin-complete (2 attestations) BEFORE rotation
— an ignored `.ots.bak` from 2026-09-26 blocked `ots upgrade` from writing (moved aside, not deleted). `stamp-new.sh` also stamped
`machine-dana-from-share-to-vow` (pushed with no proof); its legs 3–4 stay HELD. Site module regenerated (ids identical, `doi.org`
and `https` counts unchanged, zero words lost, v13) — ⚠️ the generator DROPPED the two `sig-ok` markers on P-PL5's registered
wording; restored by hand after `/check` refused the commit.

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r12.ots` (Bitcoin-complete, 2 attestations); new `b043e2542657…` *(calendar-only at stamping)* | `2026-09-27.sha256` (covers `d8a75382e040…`) | `10.5281/zenodo.23003209` | 2.5.17 |
| defensive-publications/machine-dana-from-share-to-vow | first proof *(calendar-only)* | — | ⏸ held | ⏸ held |

### 2026-09-27 — the prediction register: P-MD1–3, the Machine Dāna predictions (founder set direction, measure, threshold and window)

Three predictions registered before the paper and before any instrument, in *Instrumented but outside the core*: P-MD1
(separation, at most half the defection rate) · P-MD2 (a pledge extracted under threat carries no signal, ±5 points) · P-MD3
(principal-funded giving carries none, ±5 points); window 2027-06-30. Total 101 → 104, reconciled by the index build (104 = 104).
⚠️ **The index's own check caught two register defects before the deposit, both fixed in the register, never the check:** the
first push omitted the outside-core table row (a substrate edit error — the IDs lived only in a sub-table), and that sub-table's
`ID` header was read as an identifier (105 vs 104). The wording is now a list; the row is in the table. ⚠️ Index **2.5.16**, not
2.5.15 as its commit message says — a concurrent session had published 2.5.15. Site module hand-inserted (ids identical).

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r11.ots` (Bitcoin-complete, 3 attestations); new `35e7cb4c09db…` *(calendar-only at stamping)* | `2026-09-27.sha256` (covers `517f4a847c46…`) | `10.5281/zenodo.22998924` | 2.5.16 |

### 2026-09-27 — wave 3 (A232): ten defensive publications revised for the TDCommons mirror

co-presence-gated-redemption · the-rethank-multiplier · two-layer-reward · multi-family-membership · the-wager-that-isnt ·
steward-routed-alms · dual-currency-reciprocity · the-game-that-graduates-you · the-sport-that-says-your-name ·
studio-b-short-phase-bridge. One drafter per paper (mirror-lint refusals, bare novelty → disclosure, Terms tables, an
examiner-read fix pass: self-contradictions, wrong figures, a misattributed director, a misattributed Montessori source, an
unsourced lineage, a mis-stated N² scaling bound), then the founder's approvals (2026-09-27: pilot family generalized,
standard non-assertion in three papers, studio built-state, claim-6 narrowed) and the doctrine reconciliation he delegated
(*"reconcile Doctrine questions for me"*) as `> **Current form.**` notes — nothing disclosed was deleted (the variant rule).
No new claimed matter. Legs: OTS rotated (each retiring proof Bitcoin-complete) + re-stamped (calendar-only) · TSA
`2026-09-27.sha256` · Zenodo ten new versions (`10.5281/zenodo.22990556` … `22990585`) · index 2.5.15 · site `32dd0d4`
(eight regenerated, dual-currency hand-ported).

### 2026-09-26 (later) — the prediction register: a naming note for P-PL5 (founder: *"do F3QR in P-PL5 now"*)

A Revisions note gives the public form `H3QR @name #family` for the internal shape name P-PL5 and the dated 2026-09-05 entry
print; neither wording is edited (the revision rule; dated records). Registers nothing — total stays 101, reconciled by the index
build. The site module carries the note, plus `sig-ok` with a reason on the two lines holding the registered wording.

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r10.ots` (Bitcoin-complete, 1 attestation); new `b652a1286f00…` *(calendar-only at stamping)* | `2026-09-27.sha256` (covers `16796de473ed…`) | `10.5281/zenodo.22985892` | 2.5.14 |

### 2026-09-26 — the prediction register: P-PL12, cross-income gravitation among strangers (founder: *"Register the prediction"*)

One row in Chapter I beside P-PL9 and a Revisions entry; total 100 → 101, reconciled by the index build (101 counted vs 101
stated). The founder chose the measure (per view, not share of flows) and the 2× threshold; the sample floors are substrate-set.
Entered **before any observation exists** and Unrun until a surface shows one family's B-Shorts to another. Mirrored as a
`blocked` entry in `thank.heartbank.org`'s `predictions.json`. ⛔ No `##` change.

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r9.ots` (Bitcoin-complete, 2 attestations); new `7a60e22742ad…` *(calendar-only at stamping)* | `2026-09-27.sha256` (covers `553ac17bac94…`) | `10.5281/zenodo.22984924` | 2.5.13 |

### 2026-09-25 — nine of wave 2's eleven POSTED at TDCommons (mirrors, not revisions)

Nine "New submission posted" notices (MS #13232–33, #13236–42) reached the inventor address on 2026-09-25; each record
checked on the venue's own series page and in My Account (title as submitted, inventor Thon Ly, CC BY 4.0): embodied-advocate-pageant [11874](https://www.tdcommons.org/dpubs_series/11874) · mechanical-heart [11875](https://www.tdcommons.org/dpubs_series/11875) · miss-aquarius-and-aquarian-pool-architecture [11876](https://www.tdcommons.org/dpubs_series/11876) · the-referee-not-the-governor [11877](https://www.tdcommons.org/dpubs_series/11877) · tipitaka-alignment-substrate [11878](https://www.tdcommons.org/dpubs_series/11878) · what-a-vow-must-cost [11879](https://www.tdcommons.org/dpubs_series/11879) · zero-point-game [11880](https://www.tdcommons.org/dpubs_series/11880) · agi-monks-caretaker-not-ordained [11881](https://www.tdcommons.org/dpubs_series/11881) · b-poh-humanity-layer-ai-native-internet [11882](https://www.tdcommons.org/dpubs_series/11882).
**Not posted:** buddha-ai-living-tipitaka (MS #13234) and capacity-funded-human-disbursed-ai-alignment (MS #13235) show
`queued_for_update` in My Account on 2026-09-26, with no editor comment and no e-mail. **21 of 23 submissions posted.**
✅ **Posted PDFs verified 9/9 on 2026-09-27** (`check-mirrors.py --verify-posted`, word for word in order, 0 extra · 0 missing; each
control fails as it must) — after fixing the verifier's running-title match for titles carrying ℠ or ṭ.


⛔ **No leg ran, and none was owed:** no markdown changed. Each mirror is a dated snapshot of the text submitted, never a
canonical venue. Recorded with `check-mirrors.py --posted`; the check reads 12 of 12 clean. ✅ **Posted PDFs
verified the same day, all twelve (file one too): `check-mirrors.py --verify-posted` — each posting is our submitted PDF
word for word, IN ORDER, plus the venue's one-page cover, page numbers and running stamps (a checksum cannot say this:
the venue re-writes the file). Controls: a one-word swap caught, a wrong-paper comparison fails on every run.** Fetched
through Chrome — the site now serves `curl` a Cloudflare challenge.

### 2026-09-25 — silica-wat-food-network: one crossing, never a rate (A240; reconciled by the substrate under the founder's delegation, shipped on his word: *"1"*)

A homegrown contribution no longer earns Kiitos / Kiitti "at a higher rate": every contribution registers as one crossing and
provenance is honoured in the story, never weighted (`the-zero-point-game` §6.1; Signature 8). Step 5b brought §3.1 · §3.3 ·
§4.2 · §5.1 · §5.3 · §11.3 into line with later rulings, each as a *Current form* note beside the superseded mechanism; the A126
mission sentence retired (`MISSION_PAST_DEBT` −1); perma.cc removed. Drafted under the `drafter` contract. Legs: OTS `.ots` →
`.r3.ots` (Bitcoin-complete, 3 attestations) + re-stamped *(calendar-only)* · TSA `2026-09-26.sha256` (covers `723590c844aa…`) ·
Zenodo new version `10.5281/zenodo.22969388` · index 2.5.12 · site: hand-authored module ported (0,0,0), regaining 2,605 abridged words.

### 2026-09-24 (evening) — A232 wave 2: the final fix pass before the mirror (founder: *"1: yes 2: yes 3: cut 4: dash 5: do the fix pass first"*)

The same eleven papers, second revision today. The packet reads (one reader per paper, examiner's eye) found what no lint
could: **self-contradictions** (resolved toward each paper's own detailed sections), **emoji and editor notes**, two
**unsourced quotations** (now cited: *Lawfare*, *TIME*), **unscoped superlatives** (scoped to what each paper surveyed),
and **citations** verified on the web — corrected, added (Ford & Strauss 2008; Borge et al. 2017; El-Yaniv & Wiener 2010;
Buterin, Hitzig & Weyl 2019; Roth, Sönmez & Ünver 2004; Soares et al. 2015) or cut (an unfindable product; three
unverified fatwa examples); a wrong Worldcoin figure corrected. Founder rulings: *operates under Cambodian incorporation*
cut; a reference to the founder's father by relation and the birthday stand. `md2html.py` fixed the same day
(`__bold__`, split-list numbering, autolinks, `<sub>`/`<sup>`). Legs: OTS rotated (each retiring proof Bitcoin-complete,
14:34) + re-stamped (calendar-only) · TSA `2026-09-24.sha256` (re-run) · Zenodo eleven new versions
(`10.5281/zenodo.22947092` … `22947111`) · index 2.5.11 · site: seven regenerated (three-axis clean), four hand-authored
modules edited by hand (ids identical).

### 2026-09-24 (afternoon) — A232 wave 2: eleven tier-a defensive publications, pre-mirror repairs + doctrine reconciliation, one chain run (founder: *"do next batch"* · *"reconcile CI checker and Doctrine problems"*)

`agi-monks-caretaker-not-ordained` · `b-poh-humanity-layer-ai-native-internet` · `buddha-ai-living-tipitaka` ·
`capacity-funded-human-disbursed-ai-alignment` · `embodied-advocate-pageant` · `mechanical-heart` ·
`miss-aquarius-and-aquarian-pool-architecture` · `the-referee-not-the-governor` · `tipitaka-alignment-substrate` ·
`what-a-vow-must-cost` · `zero-point-game` — the ten remaining tier-a papers plus zero-point-game, all without an
enumerated-claims section. **Mirror repairs** (mirror-lint 0 REFUSE on all eleven, `check.py --pii` clean): the retired
A126 mission sentence out of nine; draft/editor banners removed or made a reader-facing Note; perma.cc, arXiv, LessWrong,
archive.today and "TBD" placeholders removed; unscoped novelty turned into disclosure; a **Terms** table in every paper.
**Doctrine reconciliation, by the variant rule** — a superseded mechanism stays disclosed and a `Current form` note states
the design as now specified: Pool inflow by purchase only · capacity funded in kind through B-ReGift℠, shop and re-giver
drawn by B-Called℠. **Factual corrections:** the retrodiction no longer flattened to "invalid on all four"
(`what-a-vow-must-cost`); Re-Tip Jar℠ / Re-Tip Fund℠ one account in two phases; the Sangha and the pageant postponed,
the override a design; the Pool on Base L2, not regulated rails; CEO of HeartBank® only; lease/tick for the digital
credential; Silicon Wat not a HeartBank program; no "HeartBank Foundation"; a patent blocks practice, not publication;
no stale "position paper" or "publication timed to 2027"; literature-gap claims scoped to the work surveyed.
`check-frontmatter`: nine paid `MISSION_PAST_DEBT` entries and seven already-paid banned-field / body-claim entries removed.
Legs: OTS rotated (each retiring proof Bitcoin-complete) + re-stamped (calendar-only) · TSA `2026-09-24.sha256` (re-run) ·
Zenodo eleven new versions (`10.5281/zenodo.22946089` … `22946112`) · index 2.5.10 · site: seven regenerated
(three-axis verified), four hand-authored modules edited by hand.

### 2026-09-24 — eleven defensive publications POSTED at TDCommons (mirrors, not revisions)

**Founder, 2026-09-24: *"all TDCommons submissions now posted."*** Verified against each record's own metadata (author
`Ly, Thon`, online date `2026/9/24`, title matching the submitted packet), all posted **24 September 2026**, CC BY 4.0:
rotation-over-liveness [11860](https://www.tdcommons.org/dpubs_series/11860) · the-reciters-protocol
[11861](https://www.tdcommons.org/dpubs_series/11861) · gratitude-riding-currency-tag
[11862](https://www.tdcommons.org/dpubs_series/11862) · subject-released-attestation
[11863](https://www.tdcommons.org/dpubs_series/11863) · provenance-carrying-retrieval
[11864](https://www.tdcommons.org/dpubs_series/11864) · the-called-draw [11865](https://www.tdcommons.org/dpubs_series/11865)
· gift-tag-time-reveal [11866](https://www.tdcommons.org/dpubs_series/11866) · verified-human-anonymous-local-giving
[11867](https://www.tdcommons.org/dpubs_series/11867) · aura-gated-anonymous-mate-selection
[11868](https://www.tdcommons.org/dpubs_series/11868) · respiratory-biofeedback-contemplative-guidance
[11869](https://www.tdcommons.org/dpubs_series/11869) · thank-all-nearby-primitive
[11870](https://www.tdcommons.org/dpubs_series/11870). With file one (11797), **12 of 12 submissions posted, none awaiting.**

### 2026-09-24 — A230: the retired A126 mission sentence out of five defensive publications (founder: *"yes"* — do A230 alongside the-called-draw)

`gift-tag-time-reveal` · `verified-human-anonymous-local-giving` · `aura-gated-anonymous-mate-selection` ·
`respiratory-biofeedback-contemplative-guidance` · `thank-all-nearby-primitive` — the sentence that read a middle-way PAST
(*restore humanity to the middle way … that modernity has pushed away from*) replaced by the A126 form (*keep the middle way
open at population scale against comfort-saturation — the new extreme that material abundance makes possible*), each paper
keeping its own subject. `MISSION_PAST_DEBT` shrinks by five; `BANNED_FIELD_DEBT` and `BODY_CLAIM_DEBT` also lost stale
entries for three of them, verified paid (no banned field, no body claim). Legs: OTS rotated (each retiring proof
Bitcoin-complete) + re-stamped (calendar-only) · TSA `2026-09-24.sha256` · Zenodo five new versions · index 2.5.9 · site:
three regenerated, two hand-authored modules edited by hand.

### 2026-09-24 — the-called-draw: its polish round, ruled and applied; first deposit (founder: *"let's polish now then submit to TDCommons"* · *"do per your recommendation"*)

Model round `TH/notes/reviews/the-called-draw/2026-09-23-r1` — gpt-5 · grok-4.6 · gemini-3.8-flash · the cold control on
claude-opus-5-5 (Message Batches); 40 points triaged: **29 accepted, 10 rejects upheld, 1 verify resolved** (six citations
confirmed against primary sources). **The claims narrowed to the census survivors** after four neighbours the full census
missed — Ethereum's attestation committees, RFC 3797's ordered alternates, Shutter-style timed key release, and the exclusions
as ordinary practice; contradictions fixed; rules added (service follows the committed order · a draw-id schedule · the
quorum's recipient list published with the commitment); honest limits added (no forward secrecy once a time-lock releases ·
a beacon that must survive to the reset). The patent parenthetical restated as disclosure and bibliography only. Draft banner
→ note; Terms table. Legs: OTS `.ots` → `.r1.ots` (Bitcoin-complete), new proof calendar-only · TSA `2026-09-24.sha256` ·
**Zenodo FIRST DEPOSIT `10.5281/zenodo.22933319` (concept `10.5281/zenodo.22933318`)**, census gate passed · index 2.5.8,
hold lifted. `status: draft` kept (the claims changed; no human round yet).

### 2026-09-23 (late night) — wave-1 TDCommons pre-mirror repairs, nine defensive publications, one chain run (founder: *"please do for me"* · *"do a quick census only where a claim is worth keeping"*)

The all-72 eligibility screen and `scripts/mirror-lint.py` (built the same night) found what must never reach a permanent,
examiner-read posting. **Novelty: the adjective removed, the disclosure kept** — no census ran, because no novelty sentence
was worth keeping for the mirror. Each retiring proof was checked Bitcoin-complete before rotation (`the-reciters-protocol`'s
was calendar-only from its evening revision and was upgraded first). Legs: OTS rotated + re-stamped (calendar-only at
stamping) · TSA `2026-09-24.sha256` · Zenodo new versions below · index 2.5.7.

| document | repair | Zenodo |
|---|---|---|
| provenance-carrying-retrieval | unscoped novelty → disclosure (3) | `10.5281/zenodo.22931208` |
| thank-all-nearby-primitive | draft note → Note; novelty → disclosure (2); ⛔ an **unverifiable citation** ("Glazerman, Hagar …", no source found) replaced with Biçer & Küpçü, PoPETs 2020(4); Terms table | `10.5281/zenodo.22931213` |
| rotation-over-liveness | draft banner → Note (content kept); Terms table | `10.5281/zenodo.22931216` |
| the-reciters-protocol | *"a new composition"* → *"a composition of known parts"* (claim 7, abstract, §1, §4–§5); Terms table | `10.5281/zenodo.22931221` |
| gratitude-riding-currency-tag | ⛔ **a false "Mirrors of this document … arXiv, IP.com, perma.cc" line** replaced with the true venues; novelty → disclosure (6); Terms table | `10.5281/zenodo.22931228` |
| gift-tag-time-reveal | draft banner → Note; novelty → disclosure (6); Terms table | `10.5281/zenodo.22931231` |
| verified-human-anonymous-local-giving | §4.3 *"The novel combination"* → *"The combination disclosed"*; novelty → disclosure (4); Terms table | `10.5281/zenodo.22931236` |
| aura-gated-anonymous-mate-selection | draft banner → Note; perma.cc and placeholder venue rows removed; *"no dating product in the world"*, *"revolutionary"*, an unscoped superiority line → disclosure; Terms table | `10.5281/zenodo.22931237` |
| respiratory-biofeedback-contemplative-guidance | "Working draft" banners removed; novelty → disclosure; §9.5 therapeutic use restated as a field of use requiring clinical validation, **no efficacy claimed**; *"prevents enclosure"* → available as prior art; Terms table | `10.5281/zenodo.22931242` |

⏸ **`the-called-draw` stays held** (awaiting `/polish`); the dry run listed it as the one "new" and it was not deposited.

### 2026-09-23 (night) — two-singularities: the held revision, published on the founder's word (*"yes, publish two-singularities"*)

Checklist A items 3–5: the failed nearest prior attempt (the OpenAI nonprofit board, November 2023), the author's stake, what
has and has not been done; one factual fix (*the Khmer Tipiṭaka*, not *into Khmer*). Leg 1 `.ots` → `.r6.ots` (Bitcoin-complete),
new proof calendar-only · leg 2 `2026-09-24.sha256` (hash checked) · leg 3 `10.5281/zenodo.22930050` · leg 4 index 2.5.6
(served within ~10 s of deploy). The same night the mission check was widened to the variant wording the eightfold revision
exposed; two unlisted carriers surfaced and were recorded as existing debt.

### 2026-09-23 (evening) — every queued revision rider, one chain run (founder: *"All riders now"*)

**Founder ruling, overriding the queue's "ride the next revision — never a batch" for this pass.** Eight drafting passes
ran in parallel, one per paper group; the chain ran once. Each retiring proof was checked Bitcoin-complete before rotation.
Legs: OTS rotated + re-stamped (calendar-only at stamping) · TSA `2026-09-24.sha256` (hashes checked against the tree) ·
Zenodo new versions below · index 2.5.5.

| document | rider | Zenodo |
|---|---|---|
| eightfold-path-institutional-architecture | *override → 0* corrected in the open against the asymptotic override; the retired subsidy test fixed at its one site; cross-reference to the persistence paper's §8.3 | `10.5281/zenodo.22929898` |
| four-body-architecture | the banned plural recast; non-assertion statement added | `10.5281/zenodo.22929904` |
| need-compiled-questlines | the B-Dog family renamed, with a terminology note | `10.5281/zenodo.22929906` |
| safety-companion-pack-watch | the same rename; responders are never the pack | `10.5281/zenodo.22929909` |
| the-reciters-protocol | §9.11 — the canonical count does not balance (the queued premise was re-verified and recast) | `10.5281/zenodo.22929913` |
| the-sport-that-says-your-name | §4.4 — the v1/v2 caller, the closer effect, the seed as the version | `10.5281/zenodo.22929916` |
| zero-point-game | Peskin (1976) verified and cited | `10.5281/zenodo.22929921` |
| essays/four-elements-as-breadth-check | four errors | `10.5281/zenodo.22929924` |
| essays/breadth-check-on-the-work | the banned plural | — (no record) |
| essays/each-life-as-cosmic-coordinate · essays/silicon-wat-architecture | no longer call themselves defensive publications | — (no record) |

⏸ **`essays/two-singularities` drafted and HELD** — its new stake paragraph awaits the founder's word; its proof and record are
untouched. `MISSION_PAST_DEBT` shrank by four, founder-authorized.

### 2026-09-23 — eight revisions in one chain run (the A92 bundle and the queued enrichments), and one new paper held

**Founder: *"Continue with DRAFTABLE NOW and the A92 bundle. Use agents whenever possible."*** Seven drafting passes ran in
parallel, one per document, each carrying every rider queued for its document (the `/draft` revision lane, step 5b);
the chain then ran once, serially, for all eight. ⛔ **Each retiring proof was checked Bitcoin-complete before it was
rotated.** The A92 gate (the unpaid relay's 9/05 proof) was open: it carried its Bitcoin attestation.

| document | leg 1 · OTS (new proof, calendar-only at stamping) | leg 2 · TSA | leg 3 · Zenodo (new version) | leg 4 · index |
|---|---|---|---|---|
| the-unpaid-relay | `.ots` → `.r2.ots`; new `aa17fe6885c6…` | `2026-09-24.sha256` | `10.5281/zenodo.22929362` | 2.5.4 |
| rotation-over-liveness | `.ots` → `.r1.ots`; new `070b60115eef…` | `2026-09-24.sha256` | `10.5281/zenodo.22929354` | 2.5.4 |
| manufactured-universal-giving | `.ots` → `.r3.ots`; new `f86dbc4c95e8…` | `2026-09-24.sha256` | `10.5281/zenodo.22929351` | 2.5.4 |
| fractal-three-level-architecture | `.ots` → `.r3.ots`; new `5b3d77b98037…` | `2026-09-24.sha256` | `10.5281/zenodo.22929350` | 2.5.4 |
| the-persistence-architecture | `.ots` → `.r6.ots`; new `b307a491d699…` | `2026-09-24.sha256` | `10.5281/zenodo.22929361` | 2.5.4 |
| the-gift-operation | `.ots` → `.r4.ots`; new `3857de663cce…` | `2026-09-24.sha256` | `10.5281/zenodo.22929355` | 2.5.4 |
| essays/the-water-cycle | `.ots` → `.r2.ots`; new `fc1c6ac641af…` | `2026-09-24.sha256` | `10.5281/zenodo.22929365` | 2.5.4 |
| program/prediction-register | `.ots` → `.r8.ots`; new `208e3c2f3558…` | `2026-09-24.sha256` | `10.5281/zenodo.22929363` | 2.5.4 |
| **the-called-draw** *(new)* | first proof | `2026-09-24.sha256` | ⏸ **not deposited** — awaiting its `/polish` round | ⏸ HELD (`holds.json`) |

⚠️ **Two things the run caught and did not ship.** (1) The index builder reads the working tree, and an unpushed personal
essay held for the founder's pass was in it — the essay was parked outside the tree and the index rebuilt to 146
documents, so CI's fresh-checkout build agrees with the served one. (2) `stamp-new.sh` stamps any proofless document in the
tree, and it stamped the same held essay once; that proof was deleted uncommitted (only its hash had reached the calendar),
and the essay was parked for the second stamping run. ⭐ **Both are the same shape: a tree-wide instrument cannot tell a
held draft from a published one** — nothing marks the held state except that the file is untracked.
The ledger `MISSION_PAST_DEBT` shrank by two (fractal, gift-operation), the A126 retrofit having ridden both revisions.

### 2026-09-21 — b-links-signed-provenance: POSTED at TDCommons (a mirror, not a revision)

**Founder, 2026-09-23: *"b-links-signed-provenance has posted on tdcommons."*** The estate's first posting in an
examiner-facing prior-art venue is live: **[tdcommons.org/dpubs_series/11797](https://www.tdcommons.org/dpubs_series/11797)**,
publication date **21 September 2026** (submitted 2026-09-19), inventor Thon Ly, **CC BY 4.0** (the venue offers no CC0).
The posted abstract opens with the submitted packet's first sentence (`submitted/b-links-signed-provenance.packet.txt`).

⛔ **No leg ran, and none was owed:** the markdown did not change, so its `.ots`, manifest, DOI and index entry all still
cover the current bytes. The mirror is a **dated snapshot of the 2026-09-05 text**, never a canonical venue.
`check-mirrors.py` now records the posting (`--posted`) and keeps it if a later second submission re-records the paper.
⚠️ **Not verified byte-for-byte:** the posted PDF could not be fetched (bot wall); the venue lists 408 KB against our
344 KB submitted, which a cover page would account for.

### 2026-09-20 — the prediction register: P-MA1…MA4, Miss Aquarius's suggested thanks

**Founder: *"Yes, draft that entry now"*** — four predictions registered **the day the surface shipped and before any
customer had seen it**, because the stated purpose was *"so we can study the user's engagement"* and a study begun after
the data exists is unscorable however carefully it is written up later. Four table rows and a Revisions entry; ⛔ no `##`
change, so the `published` label is untouched.

⚠️ **The honest limit is the instrument, and it is recorded in the entry rather than discovered later:** the shops
platform stores **no figure for a thank anywhere**, so there is no shop-side instrument at all — the only record of a
completed thank is the Treasury ledger. ⭐ Determinism is what makes the comparison possible without a second record:
the suggestion is a pure published function of the goods, so it can be **recomputed** for any completed thank, which is
also what **P-MA4** tests as a property rather than a behaviour.

⚠️ **Leg 2 ran twice.** The weekly manifest landed *between* the markdown push and the proof rotation, so it attested the
current text (which is leg 2's job) while its `.ots` entry still named the superseded proof and `.r7.ots` was absent.
The re-run covers the rotated set. ⭐ *The manifest is signed either way, so only its hashes say anything.*

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **program/prediction-register** | `.ots` → `.r7.ots` (`cf30e4fc…cf29fc78f8`, Bitcoin-complete); new `b82616a2…0c7a5830b4d1e588eba7502e904f31` *(calendar-only at stamping)* | `2026-09-20.sha256` | `10.5281/zenodo.22861762` | 2.5.3 |

### 2026-09-16 — the founder page: the Machine Door, singular

**Founder: *"rename the page: I think the singular 'Machine Door' creates a nice dramatic effect"*** — the site's menu already
says *Machine Door*; the page it opens and this document's link said *Machine doors*. One link text changes; no `##` change.
Not a Zenodo document (`about/` is outside the deposit scope), so leg 3 does not apply.

| document | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **about/the-founder** | `.ots` → `.r2.ots` (`0d87ffff…3c193e428a`, Bitcoin-complete); new `905ecfbc…96851d95771383d0d32cb0761d7db46ce6b9` *(calendar-only at stamping)* | `2026-09-17.sha256` | n/a | 2.5.1 |

### 2026-09-14 — provenance-carrying-retrieval: the oral canon as prior art

**Founder: *"3: do it"*** — the queued §-enrichment, ungated once *The Reciters' Protocol* was deposited. Two sentences in §2
*Archival provenance* and a §14 entry; prose only, no `##` change, `status: draft` unchanged. The counterexample hunt narrowed the
queue's wording three ways before drafting: roughly four centuries without writing (not *no writing*), a different threat (loss and
drift, not substitution), and divergence made detectable, never prevented.

| paper | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **provenance-carrying-retrieval** | `.ots` → `.r2.ots` (`d6ac93f9…a50ecc3c`, Bitcoin-complete); new `14cd053c…c74bfc03` | `2026-09-14.sha256` | 10.5281/zenodo.22745407 *(new version)* | 2.5.0 |



### 2026-09-13 (evening) — two-singularities: `published`

**Founder: *"two-singularities sets up the context for understanding the institutional mission. let's make it
'published' to signal confidence?"*** — answered: `published` measures review, not confidence, and the founder's own
pass counts. Round `2026-09-13-h1` opened on v5; **founder, verbatim: *"clean"*** — ruled, zero items.

| paper | leg 1 · OTS | leg 2 · TSA | leg 3 · Zenodo | leg 4 · index |
|---|---|---|---|---|
| **two-singularities** *(status → published)* | `.ots` → `.r5.ots` (`f36e876f…b9e93e3c`, ⚠️ retired calendar-only); new `db0df665…2745e5a3` | `2026-09-13.sha256` | 10.5281/zenodo.22737385 *(new version)* | 2.3.4 |

The only byte change is the front-matter `status`; the `##` heading set matches the ruled round (17), which is what
`check-frontmatter.mjs` rule 4 admits. A third Zenodo outage (504 on the new-version call) was checked for a half-made draft
before retrying. ⚠️ A hostile outside reader is still owed under the standing rule; it does not gate the label.
