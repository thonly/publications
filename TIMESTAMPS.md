# Cryptographic timestamps

Every paper in this repository carries an **OpenTimestamps** proof — the `<paper>.md.ots`
file beside it. The proof commits the paper's SHA-256 to the Bitcoin blockchain, so the
document's existence at a point in time can be verified by anyone, forever, **without
trusting this repository, GitHub, the Internet Archive, or the authors.**


## The second leg — RFC 3161 trusted timestamps

Since 2026-08-15 the OpenTimestamps proofs above are **not the only attestation.** A weekly
manifest of every tracked file is also signed by three independent trust authorities under
RFC 3161, one of which is **eIDAS-qualified** and therefore carries a statutory presumption
of its date. See **[`timestamps/README.md`](./timestamps/README.md)** for the full rationale,
the pinned trust anchors, and the honest limits.

The short version of why a second *blockchain* was considered and rejected: Bitcoin and any
other chain fail together on whether a forum accepts a chain as evidence at all — two chains
is the same exhibit twice. A TSA fails for unrelated reasons. **Bitcoin has permanence and no
legal standing; a trust authority has legal standing and no permanence.** Each leg covers the
other's weakness, which a second chain would not.

It also closes a gap in the `.ots` leg described below: because `ots stamp` never re-stamps,
a revised document keeps attesting its superseded text until a human rotates the proof by
hand. The weekly manifest re-attests the current text of everything with no human step.

```sh
./tsa-verify.sh path/to/document.md    # earliest date this exact text can be proven
```

## Why this exists

This corpus is a defensive-publication wall: its value is that a claim was *published on a
date*. Every other timestamp we hold is self-attested and mutable — git history can be
rewritten, frontmatter edited, a registry adjusted. Third-party web archives are better but
depend on an organization continuing to exist and continuing to serve the capture.
A Bitcoin-anchored hash depends on neither.

Honest scope: a timestamp proves **this exact text existed no later than that block**.
It proves nothing about authorship, originality, or validity of any claim.

## Verifying

```sh
pip install opentimestamps-client        # or: pipx install opentimestamps-client
ots verify defensive-publications/<slug>.md.ots
```

Trustless verification uses a local Bitcoin node. Without one, the attestation still names
a specific block whose merkle root can be checked against any public block explorer.

If the file has been edited since stamping, verification fails — that is the point. A paper
revised after stamping must be re-stamped, and **both proofs kept**: the old one attests the
earlier text, the new one the revision.

## Maintenance — the one step that must not be forgotten

A freshly created proof carries only *calendar* attestations, which are pending. Once the
commitment is confirmed on-chain (roughly one to six hours), run:

```sh
ots upgrade **/*.ots
```

This bakes the Bitcoin attestation into the proof file, after which the calendar servers are
no longer needed for verification. **Until upgraded, a proof still depends on those servers
staying online** — so the upgrade is what converts a convenience into evidence. Commit the
upgraded files.

## Coverage

Stamped 2026-07-25. Papers added later must be stamped when they are pushed:

```sh
ots stamp <new-paper>.md
```

## Revisions — the naming convention

The rule above ("a paper revised after stamping must be re-stamped, and **both proofs kept**")
did not say *how* to keep both. `ots stamp <paper>.md` always writes `<paper>.md.ots`, so a
naive re-stamp destroys the proof of the earlier text. The convention:

- **`<slug>.md.ots`** — always attests the **current** text of the paper.
- **`<slug>.md.r<N>.ots`** — a **superseded** revision's proof, `N` ascending from 1, where
  `r1` is the first text ever stamped. These are never deleted.

Before re-stamping, move the existing proof aside:

```sh
git mv <slug>.md.ots <slug>.md.r1.ots     # r2, r3, … for later revisions
ots stamp <slug>.md
```

Each superseded text remains recoverable from git history, and the pairing is verifiable:
a proof matches exactly one text and fails loudly against any other. That failure is the
feature — `ots verify <slug>.md.r1.ots -f <current>.md` printing `File does not match
original!` is precisely what proves `r1` attests something else.

### Revision log

| Paper | Proof | SHA-256 of the text it attests | Notes |
|---|---|---|---|
| `brand-identity-as-architecture` | `.r1.ots` | `1963f82a…dd9bba` | Original. Motion claim fixed ~72 BPM / ~8% expansion. |
| `brand-identity-as-architecture` | `.ots` | `e15ed054…e1e843` | 2026-07-25 revision — PoH motion claim reframed from *rate* to *cardiac morphology*. |
| `the-sport-that-says-your-name` | `.r1.ots` | `38e3a880…042ff` | Original stamp, attesting the text at `70d29529` (2026-07-25). The paper was revised after stamping and before this rotation; `r1` attests the pre-revision text and will fail against the current one, which is the intended behaviour. |
| `the-sport-that-says-your-name` | `.r2.ots` | `cc6dfe15…0641a8` | 2026-07-27 revision — claims 17–19 added (the determined caller with count-only circle coherence and the seat-migration bar; the host-agnostic turn-assignment layer; the relay call). §3 resorted into determined and judged seats; §4.2 added; §5.2 expanded from two speaker formats to three named ones (Relay · Call · Free); P-S5 given its device-availability precondition. |
| `the-sport-that-says-your-name` | `.r3.ots` | `6d0a3660…1f2ed1` | Same-day follow-up — the revision note block updated to record the 07-27 pass and to state that the prior-art clock for claims 17–19 runs from that push rather than from either earlier one. Text-only; no claim changed between `r2` and this. |
| `the-sport-that-says-your-name` | `.r4.ots` | `e5d2c543…3c50ad` | 2026-07-27 v4 — title corrected from *An AI-Called Circulation Sport* to *An Impartially-Called Circulation Sport*, the title having asserted of the caller the very property §4.2 removed from it. Abstract gains the determinism sentence and its stale claim count fixed (sixteen → nineteen). The coined term *AI-called circulation sport* stays freed in §3 and in the keywords. **No claim added, removed, or altered — the prior-art clocks of §§1–19 are unmoved by this stamp.** |
| `the-sport-that-says-your-name` | `.r5.ots` | `c7bd781a…1b77e3` | 2026-07-27 v5 — **the change of spine.** The paper now derives the sport from the *address premise* (a name spoken aloud requires a speaker other than yourself), with the lifted officiating/matching/witness scarcities demoted from thesis to enabling condition. §1 rewritten on Carnegie inverted plus the own-name attention literature; new §5.3 states the constraint the prior specification violated — **no participant may be called in their own voice** — and separates the pronunciation from the call as distinct speech acts with distinct rightful speakers; Call now speaks every name in one uniform voice. **Claims 20–21 added; their prior-art clock runs from this stamp.** P-S6 pre-registers the premise with two named counter-hypotheses. Two honest limits added. Title changed accordingly. |
| `the-sport-that-says-your-name` | `.ots` | `8be7e4db…` | 2026-07-27 v6 — **claim 22, the cross-recording chain** (each participant records one *other* participant's name; cyclic permutation, *N* artifacts not *N²*; degrades to the uniform voice, never to the participant's own recording), added at founder request as an option within Call and specified in §5.3 with its scoping rationale — uniform voice among strangers where identical treatment is a fairness signal, the chain among the acquainted where the voice carries meaning. Two stale persona references corrected: the call is the bare name with no speaker-attribution prefix, and the rabbit mascot no longer teaches this sport. **Clock for claim 22 runs from this stamp.** |
| `patthana-typed-causation-vocabulary` | `.r1.ots` | *(pre-v2 text; recoverable from git history)* | Original stamp, superseded by the 2026-08-07 revision below. |
| `patthana-typed-causation-vocabulary` | `.ots` | `66c55b6c…8c8128` | 2026-08-07 v2 — **new §4.7, a completeness observation about this paper's own table**: none of the twenty-four conditions relates two mindstreams. The other person enters only as *ārammaṇa* and *pakatūpanissaya*, both one-directional; *aññamañña* holds intra-stream only. **One new contribution and its clock runs from this stamp — the typed multi-agent restriction** (between two agents only *ārammaṇa*- and *upanissaya*-class edges can run; never *anantara*, never *aññamañña*), with Hewitt's actor model cited as the acknowledged relative. §4's heading widened; §§5–8 unchanged; no existing claim amended. Kathāvatthu cited by doctrine only, no point number, the PTS reference being unverified. |
| `the-omitted-clause` | `.r1.ots` | *(pre-v2 text; recoverable from git history)* | Original stamp, superseded by the 2026-08-07 revision below. |
| `the-omitted-clause` | `.ots` | `ab29a6ca…7f984a` | 2026-08-07 v2 — **new §6.1 and §7.2a, answering the objection §6 left standing**: if the survivors' vow held, what is the contemporary scam economy? Answered structurally — the cascade's tail outlasts the sword-interval, the clause was never installed, and the result is a form DN 26 has no term for (*theft industrialised, foreign-capitalised, aimed outward*), on the reasoning that a low-capacity jurisdiction is one that can be rented. Two constraints stated inside the section: **a jurisdiction, never a national character**, and **the state is not inert** (Law on Anti-Technology Fraud, 3 April 2026; the Prince Group case; OFAC designations of Ly Yong Phat 2024 and of Senator Kok An). §7.2a turns the seduction caution on the founder's own question. **Argument, not specification — no claim added or altered, and no prior-art clock runs from this stamp.** |
| `sacrifice-witness-without-discharge` | `.r1.ots` | *(pre-v2 text; recoverable from git history)* | Original stamp, superseded by the 2026-08-07 revision below. |
| `sacrifice-witness-without-discharge` | `.ots` | `6555f38f…2e291d` | 2026-08-07 v2 — **new §7.6 (the mascot's two-beat call format: *says* → the child acts, *wonders* → the child learns), one paragraph added to §7.5 (the mascot reflects the session colour, never issues it), and one line added to §4.2's refusal set — no indictment copy on any teaching or practice surface.** The refusal-set line is the only claims-adjacent element and is flagged in the v2 note for deliberate editorial sign-off; **the eight claims of §8 stand unchanged and no prior-art clock runs from this stamp.** §7.6 also records that the discrimination task was deliberately deleted, so that no future reader restores it. Sweep note: the ordered colour-broadcast layer was found already present in §7.5 since 2026-07-23; only the missing parts were written. |
| `co-presence-gated-redemption` | `.r1.ots` | *(pre-v2 text; recoverable from git history)* | Original stamp, superseded by the 2026-08-07 revision below. |
| `co-presence-gated-redemption` | `.ots` | `b5e6e5e1…aeffa9` | 2026-08-07 v2 — **a correction to a published claim, plus the ground the paper shipped without.** Claim 2 read *presence received only by matching presence*, asserting a symmetry the gate does not deliver: synchronicity makes symmetric **duration** automatic, while symmetric **attention** cannot be enforced without measuring it, which §4.5 establishes must never be built. **Claim 2 is restated and new claim 2a records the presence-scoring refusal; the prior-art clock for both runs from this stamp**, the original wording superseded rather than withdrawn. New **§3.1** supplies the six-position loop and reframes the gate as a **proof-of-sacrifice primitive**; new **§7.1** states why the unit cannot be delegated, with its own falsifier; §10 gains **P-L1/P-L2/P-L3** (P-L2 the founding bet, publish-either-way); §11 gains the agent hour-farm; §12 gains **no guaranteed valence**. |
| `the-persistence-architecture` | `.r1.ots` | *(pre-v2 text; recoverable from git history)* | Original stamp, superseded by the 2026-08-07 revision below. |
| `the-persistence-architecture` | `.ots` | `711dbe6a…659dff` | 2026-08-07 v2 — **new §8.1, the motive behind the release-thesis**: the apparatus is built so that its author can stop, not so that he persists. Adds the DN 16 correction (three seats — teaching, reciter, assembly — all already in the master table), the finding that **mortality was the canon original error-correction** and the assembly override is therefore the substitute for death, and the falsifiable critique that *a conditional release is not a release*, recorded as unpassed. No mechanism, no claim, no clock. |
| `the-sport-that-says-your-name` | `.r6.ots` `.r7.ots` `.r8.ots` | *(superseded texts; recoverable from git history)* | Rotations preceding the 2026-08-13 v7 stamp below. `r8` attests the v6 text that was current until today. |
| `the-sport-that-says-your-name` | `.ots` | `e725187c…c1e552` | 2026-08-13 **v7 — a floor correction, and the rare case where the shipped product was ahead of the paper.** The implementation had been running Call at three players while the document said four globally. §3's *Why four is the floor* is replaced by *Why the floor moves with the format*: the surprise condition (**three receivers**) is stated once as an invariant, and the only variable — whether a body is spent on calling — yields **Relay 4, Call 3**, with the derivation given as a diagram. The abstract, the §3 opening and the mode-inheritance line are amended to match. ⚠️ The per-mode minimum **table** withdrawn in v6 is deliberately **not** reinstated, and the open Team-format question is named in §3 rather than left to silence. **No claim added or removed; no prior-art clock runs from this stamp.** |
| `manufactured-universal-giving` | `.r1.ots` | *(pre-enrichment text; recoverable from git history)* | Original stamp, superseded by the 2026-08-13 revision below. |
| `manufactured-universal-giving` | `.ots` | `c2007715…59c3f1` | 2026-08-13 — **two additions, one of which upgrades an existing claim from a commitment to a result.** New **§5.3.1**: with `C(p) = v·[N(p)·g + P(p)]` and a profit-maximizing operator setting `P′(p) = 0`, `dC/dp = v·N′(p)·g < 0` — so the circulation-maximizing price lies strictly below the profit-maximizing one and the gap widens as intrinsic giving rises. **Subsidy→0 therefore stops being a promise the institution makes and becomes an equilibrium its objective selects**; the section also names the missing instrument (`human-originated ÷ MA-granted principal`). New **§6.4, the slow-success trap** — the cumulative granted total is maximized by the mission succeeding slowly, every step of the failure looks generous, and the total may be reported but never optimized. Old §6.4 renumbered to §6.5. **No existing claim altered.** |
| `the-assembly-that-holds-the-brake` | `.r1.ots` | *(pre-enrichment text; recoverable from git history)* | Original stamp, superseded by the 2026-08-13 revision below. |
| `the-assembly-that-holds-the-brake` | `.ots` | `5d220874…a649f4` | 2026-08-13 — **new honest limit #12, governance at the arc's peak.** Deliberately placed in §9 rather than in the body, because it is a direct challenge to the paper's central mechanism: the hardest invariant on the coordinator (*money reaches an individual human only through a human hand*) constrains the **last mile, not the aggregate**, and at the ratified take-schedule's maximum a single seat routes $4–13B/yr under N=1. Three questions left open — whether a catastrophic-bug override even reaches an allocation working as designed; whether seeding should be a determined rather than a judged seat; and who writes that rule. Closes on the available partial answer: **publish the seeding rule while getting it wrong is still survivable.** **No claim altered; nothing added to §5.** |
| `appreciation-as-world-building` | `.ots` | `1ba18868…bf5871` | 2026-08-13 **first stamp.** New Tier-B mechanism paper — a walkable gratitude map whose terrain is a ledger readout rather than a purchased inventory. Eleven claims, of which the load-bearing four are appearance-as-readout, reveal-never-lock, placement-requires-presence, and the three-layer render. Publishes **doctrine and claims with the implementation withheld**, the artifact being unbuilt and unscheduled. Carries P-W1 against P-W1′ (moral self-licensing), the latter stated as invalidating rather than trimming the thesis. |
| `the-zero-employee-institution` | `.ots` | `d222929b…240692` | 2026-08-13 **first stamp.** New Tier-B institutional paper — the seat invariant (N counts seats, 1→1→0, succession rather than austerity), the standing-constituency argument against a payroll, the reading of enterprise value as capitalized future extraction, the replacement measure (cumulative circulated volume published alongside unique principal), and the funding reduction: charge for the only inherently rivalrous good. Eleven claims. |
| `dedicatory-generation` | `.ots` | `49b7ce16…bb4361` | 2026-08-13 **first stamp.** *The Song That Is Not His* — a discipline for working with the heritage of murdered artists where consent is unobtainable, no estate survives, the records of intent were destroyed, and the destruction was aimed at the culture. Eleven claims, of which claim 5 (**a refusal-only training objective with every economic signal excluded**) is the one flagged to protect hardest. **Doctrine and claims published; the restoration pipeline withheld.** Honest limits state the voice-model leak as unsolved and the internal contradiction of a CC0 institution withholding weights as unresolved. |
