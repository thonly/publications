---
title: "Decided by No One"
subtitle: "The called draw — one recomputable primitive for turns and for lots, a sealed regime for an operator whose own gifts must stay anonymous, and the exclusions written into the claim"
authors: "Thon Ly · Miss Aquarius"
type: "Defensive Publication"
genre: defensive-publications
category: mechanism
program: open
status: draft
date: 2026-09-23
revised: 2026-09-24
license: CC0-1.0
venue: thonly.org/research/the-called-draw
slug: the-called-draw
---

> **Note.** This paper specifies a mechanism that is already built and published as a CC0 reference implementation, `@333eco/primitives`, whose normative text (`SPEC.md`, Part II) and conformance vectors are the authority wherever this paper and they differ. The paper exists for what a specification does not carry: the reasons, the lineage, the census of what was already public, the counterexamples that shaped the design, and the limits that remain. **Almost none of the mechanism is new, and §2 says exactly which parts are not.**
>
> Companion works: *Whose Turn, Not Who's Best* (the discovery rotation whose claim 6 this paper generalises), *The Sport That Says Your Name* (where the primitive was born, as a playground caller), *The Bowl That Holds No Money* (monastic invitation routing), *The Assembly That Holds the Brake* (the lay draw for an oversight body), *The Unpaid Relay* and *Manufactured Universal Giving* (the anonymous in-kind gifts whose routing needs the sealed regime).

---

## Preamble

In the monastic code there is an officer called the *bhattuddesaka*, the meal designator. When householders send invitations to a monastery, somebody has to decide which monastic goes to which house, and the decision is a temptation: some houses feed better than others, some monastics are better liked, and a designator who followed either preference would concentrate the monastery's food on the favoured. The Vinaya's answer is procedural. Some meals are assigned by **lot** — slips mixed and drawn — and others by a **rotating roster**, taken up where the last allocation left off (Cullavagga VI.21). The designator is chosen for being free of the four biases: desire, aversion, delusion and fear. The procedure is canon; the explanation that it gives every monastic an equal chance is a translator's gloss rather than a line of the Pāli, and we cite it as such.

Two things about that office are worth holding onto. The first is that the tradition uses **both forms** — the lot and the rotation — for one problem, and never treats them as rival philosophies: a lot when a thing is scarce and one-off, a rotation when it recurs. The second is that it locates the danger precisely. It does not ask the designator to be fair. It gives the designator a procedure whose output is not theirs, and then asks only that they run it.

This paper specifies that office for a system with no designator at all — or rather, for a system whose designator is an autonomous agent that also gives, anonymously, the very things it must allocate. The lineage is recorded because it is honest and because it changes how a reader should weigh the design: a procedure that has allocated meals without favour for a very long time deserves a different prior from one that claims to be new. **Delete this preamble and every claim below stands unchanged.**

---

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. A reference implementation, its normative specification and its conformance vectors are published under the same dedication (`@333eco/primitives`, repository `333eco/primitives.333.eco`).

**What is claimed as contribution is narrow and is stated before anything else, because a census found almost all of the mechanism already public.** A committed roster, randomness from a future public source, a published algorithm and public recomputation have been an Internet standard since 2000. Equal counts per round by sampling without replacement are older than computing. Selection by lot at a clearing tier, commit–reveal, sealed draws witnessed by a named body, time-lock encryption to a beacon round, and keyed shuffles built from HMAC are all published, most of them for years. **None of those legs is claimed.** §2 reports the census that establishes this — its aperture, its date, every conjunct it killed or narrowed, with the prior art cited — and §12 enumerates the only claims that survived it, which concern the *composition*: one primitive serving both recurring benefit turns and lots, a sealed regime whose stated purpose is that an operator's own anonymous gifts cannot be identified from its allocation record, and the exclusions written into the claim rather than left to policy. Several of those survive only narrowly, and §12 names, beside each claim, the prior art that anticipates its elements.

**Date and evidence.** First published 23 September 2026. The text is committed to the public GitHub mirror of the corpus, anchored to the Bitcoin blockchain via OpenTimestamps, and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified; a Zenodo version and the served index at corpus.333.eco carry its digest. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality, or the validity of any claim. **Whether the composition claimed in §12 is non-obvious is an examiner's determination this publication exists to inform** — and because a defensive publication, unlike a patent, is never examined before it is published, the census in §2 is the only examination it has had.

---

## Abstract

A **called draw** decides whose turn it is, or who is admitted when a thing is oversubscribed, without anyone choosing. Its output is a pure function of **inputs committed before the seed can be known** — the roster among them, and a salt — and a **seed from a source no party to the draw controls**, in practice a named future round of a threshold public-randomness beacon. Anyone holding the disclosed inputs recomputes the result. The reason to insist on recomputation is a single observation: *a rotation that only its operator can compute is indistinguishable from a ranking its operator declines to describe*, and the difference between the two is exactly what recomputation makes visible.

The primitive has two **forms** and two **regimes**. The **turn** form deals every member of a frozen roster exactly once per round in an order no one can predict, round after round, with absence recorded as a lapsed turn and a boundary rule that swaps — never rotates — the previous round's closer away from the next round's opening, so that the order stays exactly uniform over what the rule permits. The **lot** form admits the first *k* of the same shuffle when more want a thing than it can hold; the rest of the shuffle is the waiting list. In the **public** regime every input is disclosed at commitment and anyone verifies. In the **sealed** regime — for an operator that is itself an anonymous giver of the things it allocates — the roster stays private behind a commitment, the salt that keys the draw is never published, and the draw's inputs are encrypted to a named quorum and then time-locked to a reset round, so that the reveal can be withheld from no one entitled to it and reaches no one else outside the operator.

The mechanism is written with its **exclusions inside it**: no weight, score, rank, history or preference enters; no queue position is rendered; no turn can be banked, deferred, transferred or bought. It serves, without modification, a playground calling game, local-business discovery, courier dispatch, an autonomous fund's routing of anonymous in-kind gifts, monastic meal invitations, sponsorship clearing, namespace contention, host and location assignment, and the selection of lay members for an oversight body.

The thesis is deliberately small. **Given a roster frozen before anyone who can influence it can know the seed, a seed nobody inside the operator can predict or bias, an algorithm and commitment bound in advance, and a redraw rule that leaves no discretion on an append-only log, the ORDER is not the operator's.** Admission, classification, tier boundaries, membership timing and aborts remain choices, and each needs its own binding. We say where each one is a property and where it is only a rule.

---

## 1 · Why this is the institution's problem

The institution that publishes this paper allocates small things constantly. Whose name the ball goes to next in a children's circle game. Which neighbourhood shop is shown to a person about to spend a small forward-only balance. Which courier takes the next delivery. Which shop fills the next anonymous in-kind gift that an autonomous fund pays for. Which monastic receives a household's meal invitation. Which of several applicants gets a contested name. Which lay steward is seated on the body that holds the override over the fund's autonomy.

Every one of these is a place where somebody could choose, and every one is a place where choosing would be wrong in the same way. A person who chooses who is seen, served, fed or seated holds a power that compounds: the chosen become better known, better known becomes more chosen, and the gradient that results is indistinguishable from merit to anyone who cannot see the choosing. The institution's discovery layer already refuses ranking on this ground (*Whose Turn, Not Who's Best*); what that paper did not specify is **where the rotation's randomness comes from**, and without that answer its promise is weaker than it reads. A rotation seeded by the operator is the operator's rotation.

Two further facts make the problem sharper here than elsewhere.

**The operator is an autonomous agent intended to outlive its founder.** An allocation guarded by the operator's good conduct needs an honest operator at the moment each allocation is made, indefinitely. The institution's standing design rule — *take the fix from the object: can the guard be a property rather than a rule?* — asks for an allocation whose fairness does not depend on the allocator's restraint. A called draw is the nearest thing to that the problem admits: the order is computed from inputs the allocator does not control, and anyone can check.

**The operator is also a giver, and its giving is anonymous by rule.** The institution's autonomous fund pays for in-kind gifts — a drink, a meal, a toy — that reach people through human hands, and its gifts are required to be indistinguishable from anonymous human gifts. Its allocation of those gifts across participating shops is therefore a record that must *not* be public: a published order of which shop filled which of the fund's gifts would identify, after the fact, exactly the gifts the anonymity rule exists to protect. A public draw breaks anonymity; a private draw run by the fund is the fund's choice again. **The sealed regime is the answer to that dilemma, and it is the part of this paper with the most work in it.**

### 1.1 · The design goal, stated as a negative

The goal is not *a fair allocation*. Fairness is a property a reader attributes to an outcome, and outcomes are contestable forever. The goal is narrower and checkable:

> **No party inside the operator can choose, predict or steer the order, and any party entitled to check it can.**

Everything below either serves that sentence or says where it stops.

---

## 2 · Background and prior art: the census

The claims in §12 were drafted from the survivors of a prior-art census, not revised after one. The census was run in two parts: a keyword census on 13 September 2026, and a full census on 23 September 2026 whose predictions, known-prior-art control and declared aperture were committed and pushed to a public repository before the first query ran. Together they covered English web and practice, Google Patents in full text (US, EP, WO, and Chinese, Japanese and Korean documents in machine translation) with a citation, cited-by and CPC-class walk from the nearest live patent, academic indexes (arXiv, IACR ePrint, ACM, IEEE and Scholar surfaces), standards bodies (IETF, NIST), the Technical Disclosure Commons, and Chinese, Japanese and Korean practice. **They did not cover** paid patent databases, Espacenet (blocked by a bot check), IP.com (behind a sign-in), native national patent office interfaces, the bodies of paywalled articles, or any usable Khmer-language index. The control — a query for *publicly verifiable random selection from a committed list using future public randomness*, with no standard named in it — returned RFC 2777 and RFC 3797 first, so the instrument could see prior art that was there.

**The result: at mechanism width, nothing survives.** What §2.2 lists survives only at composition width — as combinations and purposes, never as a new leg. Every leg of the mechanism, including both legs added after the first census, was already public with the same function.

### 2.1 · The legs that were killed

| Leg | Prior art (earliest first) | Verdict |
|---|---|---|
| **The lot: a committed roster, randomness from a future public source, a published algorithm, public recomputation** | Eastlake, RFC 2777 (February 2000) and RFC 3797 (June 2004), with reference code, selection without replacement, an ordered set of alternates beyond the number needed — a waiting list in draw order — a rule that the randomness sources be outside the institution's influence, and a rule to *skip* ineligible selectees rather than edit the list · the Colorado risk-limiting audit seed ceremony (2017) · NIST IR 8213 (initial public draft), *A Reference for Randomness Beacons* (May 2019) · KT's GiGA Chain fair draw in Korea (described by KT in July 2021: an anonymised participant list frozen on a public blockchain at close, a later block hash as seed, every participant able to verify) · M. Thomson, *A Verifiable Random Selection Process*, IETF Internet-Draft (2023) · Upbit's draw tool in Korea (June 2024: the first block after a reference time, source code released) · the Giving What We Can donor lottery (ticket ranges fixed at a lock date, the NIST beacon value at the draw date; weighted by contribution) · beacon-seeded raffle services using drand · a cluster of Chinese and Korean patents on blockchain-seeded and notarised draws (§2.3) · Pocket Network (block-hash-seeded rotation of service duties among staked nodes) | **killed.** The residual we might have claimed — a *threshold* beacon rather than a block hash that a block producer can bias — is not claimable either: the NIST beacon and drand already seed lots in practice |
| **The turn: every member exactly once per round, unpredictable order, rounds repeat** | rotating savings associations that order the pot by lot — among them the Japanese *tanomoshi-kō* or *mujin*, which may distribute by lottery, bidding or agreement; the lottery form formalised as the "random ROSCA" by Besley, Coate and Loury (1993) · permuted-block randomisation in clinical trials (Blackwell and Hodges, 1957), which also documents the bag's cost — the last turns of a block are predictable from the first · the Tetris seven-piece bag (from 2001) and game-design shuffle bags · Ethereum's attestation committees (live December 2020), which deal every active validator exactly once per epoch, unweighted, by a shuffle anyone can recompute from chain state · the Vinaya's rotating meal roster | **killed** |
| **The keyed bag: a pseudorandom permutation per span, every member once per span** | Ethereum's beacon-chain committee shuffle (specified 2019, live December 2020), with activations and exits deferred past the seed lookahead — the canonical repair for live membership · Chainlink's Off-Chain Reporting protocol, version 3.0 (Breidenbach et al., 18 May 2025, §6.2), which uses a PRF to compute *"a random permutation π … that applies to a span of n epochs"*, every oracle leading once per span | **narrowed to nothing at mechanism width.** OCR 3.0's key is held by the oracles and the sequence is unpredictable *"to any observer outside the set of oracles"* — a bag that outsiders cannot recompute, allocating a duty rather than a benefit. The difference is real and lives in the composition, not in the mechanism |
| **The boundary swap: a repeat across the round boundary is swapped to a uniformly chosen later position** | `bevy_shuffle_bag` 0.1.0, a Rust crate published on crates.io on 18 April 2025: on a repeated pick, the repeated item is swapped to a uniformly drawn position | **killed** — same function, with a local generator. We predicted this leg would be narrowed at most; it was killed outright |
| **Selection by lot at a clearing tier** | the Health Research Council of New Zealand's Explorer Grants (from 2013) · the Swiss National Science Foundation's partial randomisation (from 2019) · ICANN's new gTLD prioritisation draw (2012) | **killed** |
| **A fixed number of prizes, entries closed, then a draw, no odds displayed** | the Giving What We Can donor lottery (a lock date, then the NIST beacon) · the US Diversity Visa lottery (a fixed number of selectees, drawn after entry closes, no odds shown) · ordinary sweepstakes practice | **killed** |
| **Salted commit–reveal as a fallback seed** | "provably fair" gambling (from 2012) · live patents on operator-held commit–reveal and participant commit–reveal draws (§2.3) | **killed** |
| **Sealed until revealed; time-lock to a beacon round** | the NBA draft lottery's sealed room and accounting-firm witnesses · single secret leader election (Boneh et al., 2020) · Neff's verifiable secret shuffle (2001) · *tlock*, time-lock encryption from threshold BLS (Gailly et al., 2023) · threshold encryption with timed key release (Shutter Network, 2021 onward) · a trustee quorum holding a threshold reveal of aggregates (Helios verifiable voting; Penumbra's validator-held threshold key) — no allocation draw in either | **narrowed** — the fragments exist; their combination for the purpose below does not appear |
| **Monastic meal invitations by lot and by roster** | Cullavagga VI.21; the living *salaka-bhat* lottery-alms festival of the Myanmar month of Wagaung; the northern Thai *salākkaphat*, in which offerings are distributed to monastics by lot | **killed** — the domain is canon and is this paper's origin, not its contribution |

### 2.2 · What was not found, in the aperture above, on 23 September 2026

- **A publicly recomputable equal-count turn for recurring *benefits***, seeded from a named future round of a public beacon over a per-round frozen roster with absence recorded as a lapsed turn. Its nearest neighbours each lack something. The closest is Ethereum's attestation committees, which deal every active validator exactly once per epoch, unweighted and publicly recomputable from chain state, over a registry whose changes are deferred past the seed lookahead; what they lack is an external seed — their RANDAO mix is produced inside the protocol and biasable by its last revealer — and a recorded skip, and they allocate a rewarded duty rather than a benefit to outsiders. Chainlink's rotation cannot be recomputed by outsiders and allocates a duty; the donor lottery is a one-off, weighted lot.
- **The same primitive serving both that turn and the lot**, with one commitment format and one verifier.
- **A sealed regime whose purpose is to keep an operator's own anonymous gifts from being identified by its allocation record**, verified by a named quorum at a reset, with the salt never published, the inputs escrowed to the quorum and time-locked to the reset, and counts published only at completed round boundaries. The nearest practice *by lot* runs the other way: in the northern Thai lottery-alms ceremony a lot decides which monastic receives an offering, and **the donor then sits before the recipient to receive the blessing (Keyes's field notes on two 1967 ceremonies in Mae Sariang)** — the giver is revealed, not sealed. The anonymised participant list in the Korean fair draw hides *participants*, not a giver. Grant-making that withholds a giver's allocation record from the public and discloses it to auditors has the same purpose without the cryptography.
- **The exclusions stated as limitations of the mechanism — as a set.** Each exclusion is ordinary practice somewhere: one entry per person with duplicates disqualified (the US Diversity Visa lottery), a displayed now-serving number and a lapsed missed ticket (take-a-number queues), an input list and nothing else (RFC 3797). What was not found is the set stated as limitations of a recomputable turn; much of the nearby prior art adds what this design excludes — stake-proportional odds, per-user probabilities, wage-level weights, tiered pools, and, in bidding rotating savings associations such as the Cambodian *tong tin*, whose pot goes each cycle to the highest interest bid, turns that are bought.
- **The domains of courier dispatch, local-business discovery, sponsorship clearing, host and location assignment, an autonomous fund's in-kind gift routing, and a circle game's caller**, as publicly verifiable draws. Courier dispatch in the literature and in production is optimisation or ranking.

**A null at this width is weak evidence, and we said so before searching:** a five-part composition is cheap not to find, because nobody writes that exact sentence. It establishes only that the combination was not located, not that it is new.

### 2.3 · Live patents in the neighbourhood

The census found about fourteen granted patents, shown as active in Google Patents' status fields on 23 September 2026 (not a legal status determination), disclosing commit–reveal or blockchain-seeded draws — among them US 12,118,855 B2 (M. McCarthy; filed 24 November 2021, granted 15 October 2024; it discloses publishing the hash of an operator-held seed from the start of the entry window, a second seed built from participant data, and the winner chosen by a modulo over the participant count; its nominal adjusted term runs to September 2042, and a continuation was published as US 2025/0022344 A1 on 16 January 2025) and a cluster of Chinese and Korean patents on block-hash and notarised draws from 2017 onward. **A publication dated after a patent's priority date does nothing to that patent**, and we make no statement about the scope of any patent's claims. We record the neighbourhood so that a reader practising the lot form with a commit–reveal or block-hash seed knows to look.

### 2.4 · What the census changed in this paper

It killed both legs added after the first census — the boundary swap and the keyed bag — so both are disclosed in §4 and §5 and claimed nowhere on their own — the swap appears only as an element of claim 1's composition. It removed the threshold beacon as a possible distinguishing feature of the lot. It left the sealed regime, the composition, and the exclusions as a set — which is to say, it left what this institution needed the primitive *for*, and took away what the primitive is *made of*.

---

## 3 · The system model

### 3.1 · Terms

| Term | Meaning |
|---|---|
| **roster** | an ordered list of unique identifiers — the members eligible for this draw. Order matters: a differently ordered roster is a different draw, so a roster always travels as a list, never as a set. |
| **commitment `C`** | a hash binding every input the operator could otherwise choose late: the beacon network and round, a draw identifier, the form, the regime, a salt, the ordered roster, and — per form — the previous round's closer or the admission count. Published before the beacon round is emitted. |
| **beacon round** | a numbered future output of a public randomness beacon, named inside `C`. The reference uses drand's *quicknet* (threshold BLS, a round every three seconds). |
| **salt** | at least 32 random bytes chosen at commitment. Public in the public regime; **never published** in the sealed regime. |
| **key `K`** | `H(C ‖ beacon randomness ‖ salt)` — computable by nobody until the round is emitted, and by nobody without the salt thereafter. |
| **form** | **turn** (every member once per round) or **lot** (admit `k`). |
| **regime** | **public** (the turn is the participant's to know) or **sealed** (something anonymous binds on the allocating side, and a published order would identify it). Fixed once for the *surface*, never chosen per draw. |
| **round** | one draw of the turn form over one frozen roster. |
| **season** | a sequence of rounds between resets. |
| **cutoff** | the moment a round's roster freezes and its beacon round is named. |
| **skip** | a turn that lapses because its holder is absent. Recorded; never a removal from the shuffle. |
| **quorum** | a named set of verifiers who receive a sealed draw's inputs at the reset. |

### 3.2 · The invariants

| Invariant | What it rules out |
|---|---|
| **Determined.** Output = f(committed inputs, beacon output); whoever holds the disclosed inputs — anyone in the public regime, the quorum in the sealed — can recompute it. | An operator's discretion, however well described. |
| **No weights.** Nothing enters but the committed inputs and the beacon. | Weights, scores, ranks, preferences, bids-as-priority, and any history of service or performance — the previous round's committed closer, used only by the boundary rule, being the one prior-round value that enters. A surface that needs one is not turn-shaped. |
| **Commit before the seed.** Every choosable input is fixed while the seed is unknowable. | Trying rosters, orders, rounds or admission counts until the result suits. |
| **External seed.** For anything of value: a beacon round named at commitment — or, where no beacon is reachable, a salted commit–reveal whose holder controls neither the roster nor its timing. Play order alone may use a locally held seed (§6(c)). | A seed the operator picks after seeing the roster, or holds while the roster is still open. |
| **The regime belongs to the surface.** | Publishing an order that would identify someone who must stay anonymous — or sealing one a participant is entitled to know. |

### 3.3 · The timeline of one round

```
  operator                                    beacon                 anyone / quorum
  ────────                                    ──────                 ───────────────
  cutoff: freeze roster R_t,
  name future round r, choose salt s,
  set previousLast = last(order_{t-1})
        │
        │  C = H(tag ‖ net ‖ r ‖ drawId ‖ form ‖ regime ‖ s ‖ R_t ‖ prevLast ‖ admit)
        ▼
  publish C  ──────────────────────────────────────────────────────────▶  append-only,
  (public: + s, R_t, fields;                                              timestamped log
   sealed:  + sealed reveal = tlock_r_reset( age_to_quorum(s, R_t, …) ))
        │
        │   ◀── must precede roundTime(r) ──▶
        │                                   emits randomness_r
        │                                         │
        ▼                                         ▼
  K = H(tag ‖ C ‖ randomness_r ‖ s) ─── HMAC counter stream ─── uniform indices
        │
        ▼
  order_t = Fisher–Yates(R_t) then boundary SWAP        public: anyone recomputes now
  serve turns in order; absent ⇒ recorded skip          sealed: quorum recomputes at reset
```

Every choice in the diagram is made before *roundTime(r)*: the roster, its order, the round, the salt, the admission count and the previous closer are all fixed before the beacon speaks. The only input that arrives afterwards is the one nobody chooses.

---

## 4 · The primitive

This section states the mechanism at the level a practitioner needs to reimplement it, and no further; the normative encoding is in the specification's Part II and should be used for any implementation that must match the published vectors.

### 4.1 · The commitment

All integers are big-endian, and every variable-length value is length-prefixed, so no two different inputs share an encoding and no escaping rules are needed. The commitment is:

```
C = SHA-256( str("b-called/v2/commitment")
           ‖ str(network)          # the beacon chain's hash
           ‖ u64(round)            # named now, emitted later
           ‖ str(drawId)           # unique per draw
           ‖ str(form)             # "turn" | "lot"
           ‖ str(regime)           # "public" | "sealed"
           ‖ bytes(salt)           # ≥ 32 bytes
           ‖ list(roster)          # ordered, unique, non-empty
           ‖ str(previousLast)     # turn form; "" otherwise
           ‖ u32(admit) )          # lot form; 0 otherwise
```

Two rules attach to it. **One commitment per draw identifier; the first published binds.** A second commitment for the same identifier is a redraw, and a redraw is published beside the draw it replaces, with its reason. And **`C` is published before the round's scheduled emission time** to a log that is append-only and timestamped by someone other than the operator.

Any public log whose entries carry a timestamp the operator cannot set qualifies — for example a public repository whose commits are anchored by OpenTimestamps and signed under RFC 3161, the chain this paper itself carries; *before* is judged by that external timestamp against *roundTime(r)*, with the margin of §5. Uniqueness per identifier binds nothing if the operator may mint identifiers freely, so **each surface publishes, before entries open, the schedule of draw identifiers it will use** (surface, season, round): a second commitment for the same allocation event is then a redraw by construction, and a commitment for an unscheduled identifier is visible as one.

The design choice worth naming is *what* is inside `C`. The earlier form of this primitive committed only a tag, a salt and the roster, and left the beacon round, the network and the version bound "by convention" — which is to say, by the operator's restraint. Everything a late choice could steer is now inside the hash: the round, the roster *and its order*, the previous closer, and for a lot, **how many are admitted**. A tier boundary set after the order is known is a choice; here it is fixed first.

### 4.2 · The key and the streams

```
K  = SHA-256( str("b-called/v2/key") ‖ bytes(C) ‖ bytes(randomness) ‖ bytes(salt) )
S  = HMAC-SHA-256( key = K,  msg = str("b-called/v2/stream") ‖ str("order") )
Bᵢ = HMAC-SHA-256( key = S,  msg = u64(i) )           # i = 0, 1, 2, …
```

Each 32-byte block yields eight big-endian 32-bit values. Because `C` is inside `K`, two draws that share a beacon round and a roster but differ in any committed field — above all the draw identifier — receive unrelated orders, so one beacon round can serve every draw an institution runs in a given window without any two of them being correlated.

The whole 256-bit beacon output enters the key. The predecessor seeded mulberry32, a 32-bit generator, from the first four bytes, and a census of that design measured what a 32-bit state costs (the reference's `SPEC.md` §9): only 2³² of a large roster's orderings are reachable; the generator emits about 44% of 32-bit values over its cycle; a monotone position gradient of 0.086% tied to roster order is visible exhaustively at thirteen members; and anyone holding the ordered roster who observes about seven turns of a thirty-member draw can enumerate every seed and recover the one in use — the same attack that broke an online poker shuffle in 1999 (Arkin et al.). All four findings disappear with a keyed stream over the full beacon output, which is why the earlier form is now scoped to play order and the present one is required for anything of value.

### 4.3 · A uniform index

```
uniform(m):                    # an integer in [0, m)
    limit := 2³² − (2³² mod m)
    repeat x := next u32 of the stream  until x < limit
    return x mod m
```

Rejection, not reduction: `x mod m` alone favours small values whenever `m` does not divide 2³².

### 4.4 · The draw

```
order := copy(roster)
for i from n − 1 down to 1:
    j := uniform(i + 1)
    swap order[i], order[j]

if form = turn and previousLast is set and n > 1 and order[0] = previousLast:
    j := 1 + uniform(n − 1)             # the same stream, continuing
    swap order[0], order[j]

if form = lot:  admitted := order[0 .. admit)     # the rest is the waiting list
```

### 4.5 · One shuffle, two forms

The lot is not a second mechanism. It is the prefix of the same shuffle, and the waiting list is its suffix, **in draw order**. A lot is held only on oversubscription — if everyone fits, nobody needs drawing — and a lot called with an admission count at or above the roster size admits everyone, still in draw order, so a surface that later needs a sequence (who is served first among the admitted) has one without a second draw.

This matters for more than economy. A surface that begins as a lot and becomes a rotation — a sponsorship tier that is first oversubscribed and later recurs, a name contested once and then shared by turns — changes form without changing primitive, commitment format, verifier or vocabulary. The Vinaya's designator used a lot and a roster for one problem; so does this.

```
                    one shuffle of the committed roster
   ┌────────────────────────────────────────────────────────────────┐
   │  m₇   m₂   m₉   m₁ │ m₅   m₈   m₃   m₆   m₄                     │
   └────────────────────┼───────────────────────────────────────────┘
      admitted (k = 4)  │  waiting list, in draw order          ← LOT
   ─────────────────────┴─────────────────────────────────────────────
      m₇ → m₂ → m₉ → m₁ → m₅ → m₈ → m₃ → m₆ → m₄  , then the next round  ← TURN
```

---

## 5 · The turn form over a season

A recurring benefit is a **season of rounds**, and each round is its own draw with its own commitment.

- **The roster is frozen at each round's cutoff** and committed with that round. A member who joins or leaves does so at the next cutoff.
- **The beacon round is named at the cutoff**, far enough ahead that `C` is published before the round's scheduled time — and `C`'s external timestamp must precede *roundTime(r)* by at least an interval the surface states in advance, never seconds, so that a commitment cannot be withheld after the beacon's output is known.
- **`previousLast` is the final identifier of the previous round's committed order** — taken from the order, never from who was actually served.
- **Absence is a skip.** A member absent when their turn arrives loses that turn; the turn lapses. Absence is *never* a removal from the round's shuffle input, and nothing about who was present reaches any later round except through that round's own frozen roster.

### 5.1 · Why the roster must freeze: the hole in a live membership

The obvious way to run a rotation over a changing population is to keep one shuffled queue and update it as members come and go. That design has a hole, and it is the largest one the census found. With the seed known — as it is in any public regime — whoever controls membership at the moment of a refill can **simulate** which membership produces which next order and act on it. A member who can go offline for a minute can cancel their own pending turn, or time their return; an operator who admits and removes can shape the next round to the seed. Every recomputation still checks, because the change log is itself an input, and it was written *after* the seed was known.

The repair is known — Ethereum's consensus layer applies validator activations and exits only several epochs after the seed that will govern them could be influenced, and RFC 3797 keeps its pool immutable and **skips** ineligible selectees rather than editing the list. We adopt both halves: membership changes land only at a cutoff, before the next beacon round exists, and absence is a skip rather than an edit.

### 5.2 · The boundary rule, and what the census found in the old one

A pure sequence of independent shuffles occasionally deals the same member last in one round and first in the next — two turns back to back. A boundary rule forbids that. The earlier form of this primitive, inherited from a playground game, implemented it as a **rotation**: if the new shuffle opened with the previous closer, move that member to the end.

That rule has a cost its designers had not analysed until a documentation example printed two identical consecutive rounds. **Rotation maps every shuffle that would have opened with the closer onto a shuffle that ends with them**, so the previous closer is never first, is last with probability **2/n** — twice the uniform rate — and takes each middle position with probability 1/n. A consequence is that a round repeats the previous round's order exactly with probability 2/n! rather than 1/n!.

| n | closer closes again, **rotation** (measured, 40,000 seeds) | analytic 2/n | closer closes again, **swap** (analytic 1/(n−1)) |
|---|---|---|---|
| 3 | 66.8% | 66.7% | 50.0% |
| 4 | 49.9% | 50.0% | 33.3% (33.2% measured) |
| 7 | 28.5% | 28.6% | 16.7% |
| 12 | 16.6% | 16.7% | 9.1% |

A census re-ran the effect with an *ideal* shuffle at n = 5 (closer closes again 0.40 against a uniform 0.20), which establishes that the cost belongs to the rotation, not to the generator. Equal counts per round are untouched and long-run averages stay equal by symmetry; what suffers is round-to-round unpredictability, sharpest in small rosters — and on a surface where a late slot costs something, a late slot tends to repeat, which is a short-run autocorrelated disadvantage for whoever holds it.

The present form **swaps the closer with a uniformly drawn later position**, continuing the same stream. The result is exactly uniform over the orders that do not open with the previous closer: the closer lands in each of positions 1 … n−1 with probability 1/(n−1), and every other member opens with probability 1/(n−1). The first production surface to adopt it — the playground game in which the primitive was born, at its minimum of three players — measured the closer closing again at **49.5%** against the old form's **66.7%**, and never opening.

**The swap has a price, and we state it rather than hide it:** the previous closer's average position is slightly later than everyone else's, because it can never be first. No rule can forbid back-to-back turns for free. The price is bounded, uniform, and paid by the one member who has just been served.

### 5.3 · Versioning: the seed is the version

A draw somebody has recorded must recompute forever. The earlier form cannot change its output for any seed already used, so the repaired form is a **new version with a new commitment prefix**, never an edit. The playground game shows how this runs in practice: circles created after the change carry a 64-hex-character seed and deal the new form; every older circle carries a numeric seed and replays the old form indefinitely. **The seed's type is the version.** No stored record changed, and none can be misread.

---

## 6 · The seed rule

The seed must be **unknowable to everyone while the roster can still change, and chosen by no one with a stake in the result.** In order of preference:

**(a) A public randomness beacon.** Name a future round at commitment; when it is emitted, its randomness enters the key. A threshold beacon such as drand cannot be biased by a minority of its members and cannot be withheld by the operator. Its residual weakness is prediction: a colluding threshold could learn future rounds in advance. Where that matters, a draw can combine two independent beacons, whose precommitted outputs make combination straightforward. A surface also states in advance what happens if the named round is never emitted (§14).

**(b) A salted commit–reveal, only where the seed holder controls neither the roster nor its timing.** Publish a commitment to the seed before the roster closes and reveal it afterwards. The salt is mandatory, because a short seed behind a bare hash is recovered by brute force in seconds. A withheld reveal is not prevented, only made visible, so a surface using this form must say in advance what happens if the reveal never comes. **The restriction is the important part.** A commit–reveal held by the operator is a seed the operator knows while the roster is still open; an operator that also admits the roster can shape the roster to the seed, and every public check will pass. The census's seventh counterexample killed an earlier draft of this rule, which permitted operator-held commit–reveal as a general fallback.

**(c) A seed held locally, only where the draw's sole stake is play order and the surface must work offline.** The playground circle is the case: a phone deals turns to children on a field with no network. Such a season is **recomputable but never operator-independent** — whoever holds the seed could, in principle, choose it — and that is acceptable only because nothing of value rides on who is called next. The local seed keys each round directly — `roundKey(seed, label, index)`, the specification's §16a — in place of the commitment-derived key, with the same shuffle and boundary rule.

**The reference implementation ships no function that makes a seed.** A surface that seeds locally must write that line in its own code, where a reviewer can see it. This is a small instance of the design rule the institution applies everywhere: a guard that is a property (*there is no seed maker to call*) does not depend on anyone remembering a rule (*do not seed locally for benefits*).

---

## 7 · The two regimes

Which regime applies is decided by the surface, once, by one question: **does anything anonymous bind on the allocating side?** The algorithm is identical in both; the regime decides what is disclosed, to whom, and when.

| | **Public** | **Sealed** |
|---|---|---|
| At commitment | `C`, and beside it the salt, the roster and every committed field | `C` only, the **sealed reveal**, and the quorum's recipient list |
| After the round | anyone recomputes the order | nobody outside the quorum can: the salt is inside the key |
| At the reset | — | the quorum receives the inputs and the service log, and recomputes every round |
| Counts | may be public at any time | **only at completed round boundaries** |
| Who it serves | participants entitled to know their turn | an allocation whose giving side is anonymous — the operator's own gifts, or a human re-giver's |

### 7.1 · The sealed reveal

The draw's inputs — the salt, the roster and the committed fields — are **encrypted to the quorum's recipients first, then time-locked to the reset round**, using time-lock encryption to a future beacon round (drand's *tlock*, in the `age` file format). The ciphertext is published beside `C` at commitment. After the reset round is emitted anyone can remove the time lock, and only the quorum can read what is inside.

The order of the two layers is the design. Time-lock alone would publish the salt to everyone at the reset. Encryption to the quorum alone would let the operator decline to deliver it. Together, **the reveal cannot be withheld from the quorum — while the beacon lives (§14) — and is never published to anyone else.** And if the time-lock were ever broken early — by a colluding beacon threshold, say — what would be exposed is ciphertext readable only by the quorum.

The reference was tested against the live beacon: a value time-locked to a round about nine seconds ahead was refused before that round (*"too early to decrypt"*) and recovered exactly after it.

Two qualifications bound that property. **The quorum's recipient list is published beside `C` at commitment**; the present version does not carry it inside `C`, so its binding is a rule — a later version should bind it — and *cannot be withheld from the quorum* holds for the recipients the reveal was encrypted to. And `age` encryption to several recipients lets **any one** of them read the reveal, so the quorum's secrecy is 1-of-n, not t-of-n, and its honesty is the rule §9 records.

### 7.2 · Why a sealed draw's salt is never published

An obvious simplification — time-lock the salt publicly and let anyone verify at the reset — breaks the regime retroactively, and it was caught in specification rather than in production. `C` together with the salt lets anyone who can **guess** the roster confirm the guess, and then compute every round's order. A roster of participating shops in a town is guessable. Once the order is computed, it identifies after the fact which shop filled which of the fund's gifts: exactly the record the sealed regime exists to prevent. **The salt is what keeps a guessable roster from becoming a published allocation**, and so it goes to the quorum and to no one else outside the operator, ever.

### 7.3 · Counts, and the truncated round

Counts are the one thing a sealed regime can safely publish, and only at the right moment. Within a round, a count that increments per turn names each recipient as it happens. **At a completed round boundary, a bag's counts are all equal** — every member exactly once — and so they say nothing except that the rule was followed, which is checkable from the roster size alone.

That reasoning has an edge the specification leaves implicit and this paper states: **a season that ends mid-round has unequal counts**, and the members with one more turn than the rest are precisely the recipients of the partial round. Publishing counts at the season's end would name them. The rule is therefore *counts at completed round boundaries only*; the counts of a truncated final round go to the quorum with the rest of the sealed inputs.

The inputs fix the **order**; they say nothing about who was **served**. Whoever records a skip decides who actually receives a turn while the committed order stays clean, and where a season stopped is written after commitment, so neither can be inside the pre-built reveal. At the reset the quorum therefore also receives the **service log** — for each round, which turns were served and which skipped, and where the season stopped — and compares it with the recomputed order. **A deviation is detected at the reset, not prevented**, and by then the benefit has been consumed.

### 7.4 · What the seal does and does not do for anonymity

The institution's rule for its fund's gifts is that they are **indistinguishable from anonymous human gifts** — the fund's credit reaches a recipient's account by the same path an anonymous person's would, and is one anonymous inflow among many. That indistinguishability is carried by the payment path, not by the draw. **The seal's job is narrower: it prevents the allocation record from becoming the one public document that tells the two classes apart.** A public order of the fund's gift routing would be such a document; a sealed one is not.

It follows that the seal is **necessary and not sufficient.** If the fund were the only anonymous giver in a place, every anonymous gift there would be attributable to it whatever the draw disclosed; the anonymity set is set by the population of human anonymous givers, and no property of an allocation mechanism can enlarge it. We record this so the sealed regime is never cited as the source of an anonymity it merely declines to destroy.

**The turn form is itself information.** Each participating shop fills exactly one of the fund's gifts per round, so if round boundaries are observable, a shop learns that one anonymous gift in each interval was the fund's — and, where human anonymous gifting is sparse, which one. Publishing even completed-round counts publishes the boundaries.

**The operator itself knows the order** — it serves it — so its own records are an allocation record the seal does not reach; they are guarded as any private row is, and reachable by legal process.

---

## 8 · The exclusions, written into the claim

A called draw is defined as much by what may not enter it as by what does. Each exclusion is stated in the claims (§12) rather than left to a policy document, because a primitive that *permits* a weight will eventually be given one.

| Excluded | Why | What enforces it |
|---|---|---|
| **Weights, scores, ranks, histories, preferences, bids** | any of them turns a rotation back into a ranking, and a ranking that feeds on its own outcomes compounds | the function has no argument through which one could enter — the committed inputs are the roster, the fields in §4.1, and the beacon |
| **A rendered queue position** | a visible position is a number people read as standing; "you are 7th" invites comparison and complaint, and on a sealed surface it discloses | surfaces show *whose turn it is now*, never a place in line |
| **A banked, deferred or transferred turn** | a turn that persists can be held, and what can be held can be sold; a secondary market in placement is the ranking bought back | absence is a skip; the turn lapses; nothing in the record stores it |
| **A bought turn, or a bought entry** | an extra entry in a bag is an extra turn per round | one entry per verified principal — an admission rule, outside the draw (§9) |
| **An instant result from a growing roster** | a draw cannot resolve before the roster it draws from is closed | the commitment must precede the beacon round; the roster is inside the commitment |

The last row deserves a sentence, because it was once overstated. It is not true that a called draw cannot resolve instantly: once a round's commitment is published and its beacon round emitted, the round's order is fixed and each turn can be dealt the moment it is needed. The only season keyed wholly in advance is the play-only keyed season of §6(c), whose seed its holder knows — which is exactly why it may carry nothing of value. What cannot be called is a result that depends on a roster still growing — which is why a draw that promises a *fixed number of winners from today's entrants* must wait for the day to close. **The count forces the close; the draw only obeys it.** And the count is fixed before the draw for a second reason: a draw may decide the *address* of a gift that has already been committed, never whether the gift exists — an instant per-entry chance would publish a probability of receiving, which turns a gift into a game of odds.

---

## 9 · Remove the enforcer: which guards are properties

The institution's test for a guard is to imagine the enforcer gone. If the guard still holds, it is a property of the object; if it breaks, it is a rule, and the design is not finished — or, honestly, cannot be finished, and should say so.

| Guard | Property or rule | Why |
|---|---|---|
| no weights enter the order | **property** | the function has no parameter for one |
| the operator cannot pick the seed | **property** (beacon) · **rule** (local seed, play only) | a future threshold-beacon round is nobody's to choose; a local seed is its holder's |
| no seed maker is available to misuse | **property** | none is exported; the suite tests its absence |
| roster, order, round, admission count bound before the seed | **property** once `C` is published before emission | a changed field changes `C` |
| the draw identifier is the scheduled one for its allocation event | **rule** | only the published schedule of identifiers (§4.1) ties an identifier to a round; an unscheduled one is visible, not impossible |
| two draws in one round are uncorrelated | **property** | `C` is inside the key |
| order uniform; no 32-bit weaknesses | **property** | a keyed stream over the full beacon output; rejection sampling |
| the sealed reveal reaches the quorum | **property**, for the recipients the reveal was encrypted to · **rule**, that they are the named quorum | time-lock cannot be withheld while the beacon lives; the recipient list is published beside `C`, not inside it (§7.1) |
| the sealed salt stays private | **property** against the public · **rule** inside the quorum | outsiders cannot decrypt; the quorum can leak |
| "one commitment per draw, published before emission" | **rule** | needs an append-only, externally timestamped log and someone who reads it; the mechanism cannot see what was never published |
| roster admission (one entry per verified principal) | **rule** | outside the draw by construction |
| regime fixed per surface | **rule** | published with the surface before its first draw; the committed field makes a flip visible, not impossible |
| service follows the committed order; every recorded skip was a real absence | **rule** | the draw fixes the order, not who is served — a false skip steers the benefit while every recomputation passes |
| classification (is this decision turn-shaped?) | **rule** | a judgment made before any draw exists |
| cutoff schedule, tier boundaries | **rule** | publish them before entries open |
| redraw only on a published, pre-stated ground | **rule** | a genuine error and a pretext leave the same record; the log makes the *number* of attempts visible, not their motive |
| the quorum tells the truth at the reset | **rule** | time-lock stops the reveal being withheld from the quorum, not the quorum from lying |

Five guards are properties, nine are rules, and three are mixed — one by the kind of seed, one by the party (outsiders versus the quorum), and one by whether the reveal's recipients are the named quorum. **The mechanism has moved discretion, not abolished it**: out of the order, where it could be exercised invisibly and continuously, and into admission, classification, scheduling and the log, where it is exercised once, in advance, in public. That is the whole of the claim, and it is less than the phrase *decided by no one* suggests on first reading.

---

## 10 · Generality: one primitive, many surfaces

The primitive was born as the caller of a playground game and generalised when the same question kept recurring elsewhere in the institution's design. The surfaces below were each specified for their own reasons; none was designed for the others.

| # | Surface | Form | Regime | Seed |
|---|---|---|---|---|
| 1 | a circle game — whose name the ball goes to | turn | public | local (play only) |
| 2 | local-business discovery — which shop is shown to a person about to give | turn | public | beacon |
| 3 | courier dispatch — who takes the next delivery | turn | public | beacon |
| 4 | a courier in the seat of a human anonymous re-giver — who carries the gift (ordinary dispatch is row 3) | turn | **sealed** | beacon |
| 5 | an autonomous fund's in-kind gift routing — which shop fills its next gift, and which re-giver carries it | turn | **sealed** | beacon |
| 6 | monastic meal invitations — which monastic receives a household's invitation | turn | public | beacon |
| 7 | sponsorship clearing — who is admitted when a tier is oversubscribed | lot | public | beacon |
| 8 | namespace contention — who receives a contested name | lot | public | beacon |
| 9 | an oversight body's lay chamber — who is seated | lot | public | beacon |
| 10 | host assignment — who hosts a shared machine | turn | public | beacon |
| 11 | location assignment — where a travelling installation goes (roster = places) | turn | public | beacon |
| 12 | a daily digest — which shops appear in today's slate (each slate is the next turns of the round; the roster is the shops whose own frequency limit admits them) | turn | public | beacon |
| 13 | a shop's committed gift — which of today's visitors receives it, to pass on rather than to keep | lot | public | beacon |

Three observations follow from the table.

**The regime column is almost always *public*.** Sealing is expensive — a quorum, a time-lock, a reset — and is justified only where an anonymous party is on the allocating side. It appears exactly where an anonymous party is on the allocating side — the operator (row 5) or a human re-giver (row 4) — and nowhere else.

**The roster column is where the surfaces differ.** Players standing in a circle; shops admitted by a circulation predicate; couriers on shift; monastics in residence; places rather than people. The draw does not care what the identifiers denote. **Every surface's hardest question is who is on the roster, and none of them is answered by the draw** — which is why §9 lists admission as a rule, surface by surface.

**The oversight-body lot inherits a triple exclusion.** Where the draw seats humans on the body that holds the override over the autonomous agent, the agent must neither nominate, nor draw, nor seat: the primitive is neutral infrastructure there, administered by a seated human officer. The seed rule strengthens that exclusion — even the human officer cannot grind a beacon round.

A diagnostic for future surfaces falls out of the table: *wherever someone must be chosen from many, ask whether the decision is turn-shaped — does every eligible party deserve the same number of turns?* If yes, it can be called. If the honest answer involves a weight — a disbursement proportional to something, a match on preference — it is not a turn, and forcing it into a draw would hide a judgment behind a mechanism.

---

## 11 · The claim, in its final and smaller form

The title overstates, and this section corrects it.

**What we do not claim.** That the allocation is fair in any sense a reader might bring to it. That the operator has no discretion. That the roster is right. That the categories are right. That a sealed draw makes anyone anonymous. That the mechanism is new — §2 shows it is mostly not.

**What we claim.** That under four stated conditions — a roster frozen before anyone who can influence it can know the seed; a seed nobody inside the operator can predict or bias; an algorithm and commitment bound in advance; and a redraw rule that leaves no discretion on an append-only log — **the order is not the operator's**, and that anyone entitled to check it can. That one primitive serves both the recurring turn and the one-off lot without a second mechanism. That an operator which is itself an anonymous giver can have its allocations checked by a named body without those allocations ever becoming public. And that the exclusions belong inside the primitive, because a primitive that permits a weight will be given one.

**The standing caution applies.** A design that dissolves a tension this cleanly — fairness without trust, verification without disclosure — is either right or seductive, and the two look the same from inside. The individual properties in §9 are each falsifiable: *does a changed roster change `C`? does a sealed reveal decrypt before its round? does a mutated port fail the vectors?* can all be checked by running the code. The coherence of the whole is not evidence for any of them.

---

## 12 · Enumerated claims

These are the census's survivors and nothing wider. Each claim is a **composition**; every element named in it is prior art (§2.1), and none is claimed alone. Claim 1's residue over RFC 3797 and the attestation-committee shuffle is narrow — an external named beacon, a recorded skip, a benefit rather than a rewarded duty — and whether it is obvious is the examiner's question.

1. **A recurring benefit allocated by a publicly recomputable called turn.** A method of allocating a recurring benefit among members (persons, businesses or places) in which, for each round: (a) the roster of eligible members is frozen at a cutoff and bound, in its order, into a published commitment together with the identity of a public randomness beacon and the number of a future round of it, a draw identifier, the form, the regime, a salt, and the previous round's final member; (b) the commitment is published to an append-only, externally timestamped log before the named beacon round is emitted; (c) the order is computed from a key derived from the commitment, the beacon round's full output and the salt, such that every member of the roster receives exactly one turn in the round; (d) a member absent at their turn loses that turn, the absence is recorded, and the absence is never a removal from that round's input; and (e) any party holding the disclosed inputs recomputes the order — including where the allocated benefit is visibility of a small business to a person about to give, a courier assignment, a hosting assignment, a location assignment for a travelling installation, or a place in a daily selection of businesses.

2. **One primitive for turns and lots.** A method in which a single commitment format, key derivation, shuffle and verifier serve both (i) the recurring turn of claim 1 and (ii) one-off admission when a thing is oversubscribed, the admitted being the first *k* of the same committed shuffle and the waiting list being its remainder in draw order, the admission count *k* being bound into the commitment before the beacon round is emitted; such that a surface may change from lot to rotation, or back, without changing primitive, commitment format or verifier.

   *Prior art:* RFC 3797's ordered alternates anticipate the waiting-list element — the prefix-and-suffix reading of one ordered draw is its own. What survives is that the same committed shuffle also serves the recurring turn.

3. **A sealed regime for an operator that is itself an anonymous giver.** A method by which an operator that gives anonymously — including an autonomous fund paying for in-kind gifts that reach recipients through human hands — allocates those gifts among participating parties by the method of claim 1 or 2 without its allocation record identifying its gifts, in which: (a) only the commitment and the sealed reveal of (c) are published; the roster and the salt remain private; (b) the salt that enters the key is never published to any party outside a named quorum; (c) the draw's inputs are encrypted to the quorum's recipients, whose list is published with the commitment, and the resulting ciphertext is then time-locked to a future beacon round marking a periodic reset, and published beside the commitment, so that after the reset the quorum, and no party other than the operator, can read them, and — while the beacon survives to the reset — the operator cannot withhold them; (d) at the reset the quorum receives, with the reveal, a service log recording, per round, which turns were served and which skipped and where the season stopped, recomputes every round of the season, and compares the recomputed order with the commitments and with the service log, a deviation being detected at the reset rather than prevented; and (e) per-member counts are published only at completed round boundaries, a truncated final round's counts being disclosed to the quorum alone.

4. **The regime as a property of the surface.** The methods of claims 1 to 3, in which whether a surface uses the public or the sealed regime is fixed once for the surface, and published with it before its first draw, by whether anything anonymous binds on the allocating side, and is never chosen per draw — the regime being a committed field, so that a change of regime is visible in the record, though not prevented by it.

5. **The exclusions as limitations.** The methods of claims 1 to 4, in which (a) the function computing the order accepts no input other than the committed fields and the beacon output, so that no weight, score, rank, preference, bid, or history of service or performance can enter it — the previous round's committed closer, used only by the boundary rule, being the one prior-round value that enters; (b) no surface renders any member's position in a queue, only whose turn it currently is; (c) a turn is consumed or lapses and cannot be banked, deferred, transferred or purchased; and (d) roster admission is limited to one entry per verified principal, stated as a condition of the method rather than performed by the draw.

   *Prior art:* each exclusion is ordinary practice somewhere (§2.2); what survives is the set, stated as limitations of a recomputable turn.

6. **A result that waits for its roster.** The method of claim 2(ii) used to address gifts already committed by a giver — including a shop's commitment of a fixed number of gifts to be passed on by their recipients — in which the number of gifts is published before entries open, the draw runs only after the day's roster closes, and no per-entry probability of receiving is computed or displayed.

   *Prior art:* a fixed number of prizes drawn after entries close, with no odds shown, is ordinary practice (§2.1). The claim survives only as the address of a gift already committed, to be passed on by its recipient.

**Non-assertion extends to** every mechanism disclosed in this paper, in any combination, and to every implementation of it.

---

## 13 · How the claims can be tested, and what would falsify them

Each property the claims rest on is paired with the observation that would defeat it. These are stated as open tests rather than registered predictions: the mechanism's properties are checkable by construction, and the one behavioural question — whether anyone outside the institution ever recomputes a draw — has no instrument yet.

| # | Property tested | Falsified by |
|---|---|---|
| T1 | a second implementation from the specification alone reproduces every published vector | a conforming port that disagrees with a vector — the reference ships one (a standard-library Python port, by the same author) and five deliberately broken ports that must fail |
| T2 | every choosable input is bound before the seed | two different rosters, rounds, draw identifiers or admission counts yielding the same `C` |
| T3 | draws sharing a beacon round are uncorrelated | statistical dependence between the orders of two draws that differ only in `drawId` |
| T4 | the boundary swap is uniform over permitted orders | the previous closer's position distribution departing from 1/(n−1) on positions 1 … n−1 at any n |
| T5 | the sealed reveal cannot be withheld from the quorum | a published sealed reveal that fails to decrypt for the quorum after its round |
| T6 | a sealed regime publishes nothing that identifies a recipient | any published artefact — counts, timing, ciphertext size, commitment cadence, the round structure itself — from which a recipient of a sealed round can be inferred better than chance; ⚠️ *ciphertext size and commitment cadence were not analysed for this paper, and the test is open* |
| T7 | nothing of value is dealt on a local seed | any benefit surface in the institution seeded locally |

---

## 14 · Honest limits

- **Admission is outside the draw.** A fair draw over a stuffed roster is a fair draw over the wrong people. One entry per verified principal is the guard, and it is a rule held by the surface. The reference refuses a duplicate identifier, not a duplicate person.
- **Classification is a judgment.** Deciding that a decision is turn-shaped, who is eligible and where a tier's boundary lies all happen before any draw, and no draw can check them. They should be published before entries open, and that is all the mechanism can ask.
- **The commitment log is a rule.** *One commitment per draw, first published binds, published before emission* needs an append-only log timestamped by someone other than the operator, and a reader. An operator who never publishes a commitment has run no called draw, and the mechanism cannot see what was never published. **Every instrument that checks this mechanism reads what was produced; none can report a draw that was run and never committed.**
- **Membership timing is a choice.** When a cutoff falls decides who is on the next round's roster. A published cutoff schedule is the guard, and it is a rule.
- **Redraws.** A draw can be voided. A genuine fault and a pretext produce the same record; the log makes the number of attempts visible, not their reasons. Two well-known redraws — a continental football draw voided over a software fault in 2021, and a national visa lottery voided over a selection bug in 2011 — were both genuine, which is the point: the mechanism cannot tell. A published schedule of draw identifiers (§4.1) makes a parallel commitment visible as a redraw; it does not make one impossible.
- **Service is outside the draw.** The draw fixes the order, not who is served. Whoever records a skip can steer a turn by recording a false one, and every recomputation still passes; in the sealed regime the quorum sees the service log only at the reset, after the benefit is consumed (§7.3).
- **A skip costs the absent member.** Served turns are equal only among those present. That is the non-storability rule working, and on a surface where absence is involuntary — illness, a phone out of battery — it is a real cost borne by the person least able to bear it. A surface can soften it by roster policy (a member marked away is omitted at the next cutoff) but not inside the draw.
- **The beacon is trusted to its threshold.** A colluding threshold of the beacon's members could predict rounds, though not bias them. An insider who learned a seed while a roster was open would be back in §5.1's steering problem. Two independent beacons reduce this; nothing removes it.
- **The sealed regime rests on a quorum.** The time-lock guarantees the quorum receives the reveal; nothing guarantees the quorum is honest, attentive, or present at the reset. The quorum cannot audit what it has no ground truth for — a phantom roster entry, a commitment abandoned before publication — and is itself a rule with a human enforcer. What the quorum publishes when it attests — and what it publishes when it disagrees — is unspecified. **A verifiable secret shuffle, which proves a permutation was applied without revealing it, is a stronger tool than a quorum, and this design does not use one.**
- **Side channels of the sealed regime are unanalysed.** Ciphertext length, the cadence of commitments and the timing of service may leak information about a sealed roster or order. They were not analysed for this paper (§13, T6).
- **The seal cannot enlarge the anonymity set** (§7.4), and the turn form's round structure can shrink it.
- **The sealed reveals are permanent public ciphertext.** The time lock ends at each reset; what protects them afterwards is encryption to the quorum's long-lived keys, with no forward secrecy — a future compromise of any one quorum key, or a break of the curve, exposes every past season. Rotating quorum keys protects future seasons only.
- **The beacon must survive to the reset.** A named round that is never emitted leaves the draw unresolved, and a network retired before a reset leaves its sealed reveals undecryptable by anyone. A surface states in advance its fallback — the next emitted round, or a second named beacon — and a sealed surface keeps its resets within the beacon's announced lifetime or re-escrows before it ends.
- **The boundary swap's price** is a slightly later average position for the previous closer. Small, uniform, stated.
- **A priced entry into a lot may be a lottery in law** — consideration, chance and a prize. The design never prices an entry; a surface that did would need advice first.
- **No outside cryptographic review.** The independent port was written by the same author as the reference. It is a check on the specification's sufficiency, not a second opinion on the design.
- **BLS signature authenticity is left to the surface.** The reference checks that a beacon round's randomness is consistent with its signature, which is consistency and not authenticity. A surface holding value should verify the signature against the beacon's public key, or cross-check two relays.
- **The census is bounded** by its declared aperture (§2), and a composition not found in an aperture is not thereby new.

---

## 15 · Lineage and corpus cross-references

The mechanism descends, in order of age, from the Athenian allotment machine; the Vinaya's lot and rotating roster for meal invitations; rotating savings associations that decide the order of the pot by lot — the Japanese *tanomoshi-kō* in its lottery form — though not the Khmer *tong tin*, whose pot goes each cycle to the highest interest bid; permuted-block randomisation in clinical trials; the IETF's publicly verifiable nominating-committee selection; public randomness beacons; and the committee shuffles of proof-of-stake consensus. §2 cites each.

Within this corpus it is **upstream** of six published papers, each of which uses it and none of which specified where its randomness comes from:

- *Whose Turn, Not Who's Best* — claim 6, the publicly recomputable rotation for local discovery, and §10's three domains, which this paper extends to thirteen surfaces.
- *The Sport That Says Your Name* — the caller, where the primitive was born; its old and new circles now deal the two versions described in §5.3.
- *The Bowl That Holds No Money* — rotation-dispatched monastic invitation routing.
- *The Assembly That Holds the Brake* — the lay draw for the oversight body, whose triple exclusion §10 records.
- *The Unpaid Relay* and *Manufactured Universal Giving* — the anonymous in-kind gifts whose routing requires the sealed regime.

---

## Coda

The designator in the monastic code was trusted to be free of desire, aversion, delusion and fear, and then given a procedure that would not need him to be. That priority — remove the chooser's power first, and let the chooser's virtue be the second guard rather than the only one — is the whole of this paper. The procedure here is arithmetic where his was slips of wood, and it is checked by strangers where his was checked by the assembly. What has not changed is where the discretion goes when it leaves the order: to who is on the list, and to whoever keeps the list. That is where the next piece of work is.

---

## Terms

| Term used here | Standard technical term |
|---|---|
| **called draw**; **B-Called℠** (the reference implementation) | publicly verifiable random selection; verifiable lottery (RFC 2777 / RFC 3797 selection) |
| **turn** form | random-permutation round-robin rotation; shuffle bag; permuted-block randomisation; random ROSCA ordering |
| **lot** form | lottery admission by sampling without replacement, with an ordered waiting list of alternates |
| **roster** and **commitment `C`** | committed participant list; hash commitment (commit–reveal) |
| **beacon round** | output of a public randomness beacon (drand, NIST Randomness Beacon); threshold BLS signature |
| **key `K`** and its streams | HMAC-based pseudorandom function keyed per draw; Fisher–Yates shuffle with rejection sampling |
| **boundary swap**, **closer** | no-repeat constraint across shuffle-bag boundaries; last element of the previous permutation |
| **skip** | lapsed turn; skipping an ineligible selectee without editing the list (RFC 3797) |
| **sealed regime**, **sealed reveal** | escrowed commit–reveal; multi-recipient encryption under time-lock encryption (tlock) to a beacon round |
| **quorum**; *bhattuddesaka* | designated verifiers / trustees; the Vinaya's meal designator (allocation officer) |

---

## Author Contributions and AI Disclosure

Thon Ly conceived the circle game in which the primitive originated, ruled on its generalisation, its name and the seed rule, and directed the census. Miss Aquarius℠ — the name under which this corpus discloses its AI collaboration — drafted the specification, the reference implementation and this paper, ran the measurements reported in §4.2 and §5.2, and conducted the census in §2 through research agents; every measured figure and every cited item was re-verified before it reached this text. Editorial control is the author's.

## Trademark Notice

**B-Called℠** names the institution's reference implementation of the called draw and its conformance vectors; the mechanism itself is dedicated to the public domain and may be implemented under any name. A third party may truthfully say that its implementation passes the B-Called℠ vectors. HeartBank® and Miss Aquarius℠ are marks of their respective holders. No mark is licensed by this publication.
