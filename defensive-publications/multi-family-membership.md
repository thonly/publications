---
title: "Multi-Family Membership: User-Scoped Identity, Plural Membership, and the Two Problems It Resolves"
subtitle: "User-Scoped Identity and Plural Membership as the Data-Model Correction That De-Risks Banker Succession and Dissolves the Civic-Bank Tier"
authors: "Thon Ly"
category: mechanism
priority: tier-b
status: draft
date: 2026-06-12
revised: 2026-09-26
license: CC0-1.0
slug: multi-family-membership
venue: thonly.org/publications/defensive-publications/multi-family-membership (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/multi-family-membership.md
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, Family Kitty℠, Personal Account℠, Re-Tip Fund℠, Aquarian Pool℠, Miss Aquarius℠) reserved separately by the author and HeartBank®.
---

> **Note.** This paper specifies a data-model decision and its consequences; it is a design specification offered as prior art, not a report of a measured deployment. The membership-breadth governance question is resolved as a deliberately conservative default (§8) rather than a final rule, and is flagged as data-gated.

---

## Preamble

> *Two unsolved problems in a family-banking architecture — what happens to members when a family's steward leaves, and how the family-less are ever reached — turn out to be one accidental assumption wearing two costumes. Drop the assumption, and both problems change shape.*

A gratitude economy organized around **family banks** — each a household-scale pool (a Family Kitty℠) stewarded by a designated member (a banker, or *upāsaka*) — inherits two hard problems from one quiet assumption. The assumption is that a user belongs to *exactly one* family bank. From it follow: a **succession problem** (when a family's steward abandons the bank, its members are stranded) and a **reach problem** (the family-less — orphans, the isolated, refugees, anyone without a willing family steward — cannot participate at all). This paper observes that the one-family-per-user assumption was never realistic, specifies the data-model correction, and shows that correcting it de-risks the first problem and largely dissolves the second.

> **Terminology.** *Banker* and *family bank* are this paper's original working names. In the institution's current usage the role is the **family steward** (*upāsaka*), and a *family bank* is a family's group with its shared Family Kitty℠. The architecture is a record kept above regulated payment rails (Phase 1) and self-custodial wallets (Phase 2); it is not a bank and takes no deposits (see *Non-Bank Pass-Through Architecture for Autonomous AI Institutions*). The original names are kept below so that the text matches its first publication.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author and HeartBank® will not seek patent on this specification or any portion of it, in any jurisdiction, at any time, and dedicate the patterns to the public domain under CC0 1.0. The contribution is a data-model framing — user-scoped identity with plural group membership is ordinary in software — applied to a specific architecture to resolve two specific problems. Prior art is acknowledged in §9; what this paper discloses as its contribution is the composition and the specific resolutions of §10, and nothing wider. Trademarks are reserved separately; the patterns may be implemented under any name.

**Census.** No prior-art census is on file for this paper. It was first published (12 June 2026) before the institution adopted its census rule (13 September 2026), which gates a defensive publication's first deposit and was not applied retroactively. The enumerated claims below disclose matter present in the original text; no search was made to establish that the composition is absent from the literature, and none is asserted.

## Abstract

This paper specifies a data-model correction for a group-based gratitude ledger in which users belong to household groups, each holding a shared group balance administered by one member. The correction replaces single-group containment with user-scoped identity, rooted in a proof-of-personhood verification, and represents group membership as a many-to-many set of edges: each user's personal account sits at the user record, above every group, and a group's administrator controls only the shared balance. One change addresses two failures of the single-group assumption. It lowers the cost of an administrator's departure, since members keep their personal accounts and their other memberships and the pool of successor candidates widens. And it removes most of the need for a separate tier for users with no household group, by treating a default global membership of every verified person as the outermost layer of an existing nested architecture, with admission-gated local groups as the on-ramp. Three invariants keep plural membership safe: giving capacity is metered per verified person rather than per membership; each group controls its own admission; and a member of two groups may not route or net value between their shared balances. Membership count is left uncapped by default, with a damping lever held in reserve until pilot data warrant it. Stated limits: an explicit succession protocol is still required when a member's last group fails; users admitted to no group rely on the global layer alone; per-person metering presupposes a working personhood layer; and the design is unmeasured in deployment.

## Claims

*Enumerated 2026-09-01. The mechanisms below were disclosed in full in this paper's original text; **the prior art they establish runs from this document's original publication date and its OpenTimestamps proof, not from this enumeration.** They are listed because a defensive publication is read as prior art by examiners and by opposing counsel, and **a claims list is what such a reader searches; running prose is not.** No claim below adds matter not already present.*

1. **User-scoped identity with plural family membership as one correction to two distinct failures** — treating identity as belonging to the verified person rather than to a group, with membership as a set of edges, such that the same structural change both de-risks steward succession and dissolves most of the unbanked-reach problem.

2. **The civic tier as the global layer of an existing fractal rather than a separate institution** — reaching participants with no local group by treating the outermost layer of the already-specified nested architecture as their default membership, with admission-gated local groups as an on-ramp, instead of building a parallel institution staffed by vetted strangers.

3. **Per-human capacity metering, not per-membership** — metering an individual's granted capacity to give against their verified-person identity and letting it spread across every membership they hold, so that joining additional groups multiplies neither reward nor extraction. *The load-bearing invariant: without it, plural membership is a harvest multiplier.*

4. **The non-conduit constraint on plural members** — barring a person holding multiple memberships from acting as a settlement path between two groups' shared pools, so that plural membership adds participation without creating inter-group value transfer through an individual.

5. **Admission-gating as the anti-sybil control for plural membership** — placing the join decision with the receiving group rather than with the joiner, so that breadth of membership is bounded by others' willingness to admit rather than by the joiner's willingness to enrol.

6. **Data-gated breadth damping** — shipping no cap on membership count by default while specifying in advance the lever that would damp it (a cap or decay on membership count) and holding it in reserve until pilot data warrant pulling it, rather than either capping pre-emptively or leaving the response undesigned.

---

## 1. The single-family assumption and the two problems it creates

A family-bank architecture is intuitive and humane, but if each user belongs to one and only one bank, two failure modes are baked in.

**Banker succession / orphaning.** Each family bank has a steward who manages it. When that steward abandons the bank, stops paying, dies, or is incapacitated, the members have nowhere to stand: their participation was wholly contained by a single bank that no longer functions. The system needs a graceful failure mode, and a one-bank-per-user model gives it none.

**The civic / community reach problem.** The family-banker model, by construction, reaches only people who *have* a family bank — a willing steward and a household to belong to. It cannot reach the people who most need a dignity floor: the orphaned, the homeless, the isolated, the refugee. The natural-looking fix — build a separate "civic tier" staffed by vetted stranger-bankers — is a whole second institution to design, fund, and govern.

## 2. The move: user-scoped identity, plural membership

The correction is a single data-model line: **identity is user-scoped (rooted in the person's Proof of Humanity), and membership is a set of plural edges.** A user is not contained by a family; a user is a node who holds membership edges to one or more families. Concretely:

- The **Personal Account℠** — the user's own holdings and history — lives at the *user* node, above any family. It is the person's, not the bank's.
- A **family bank** is a set of membership edges, and its steward stewards the *shared* vessel (the Family Kitty℠), never the members' personal accounts.

A user may therefore belong to several family banks at once, each membership an independent edge, with the user's identity and personal holdings sitting above all of them.

## 3. This corrects a simplification — it does not add a feature

The one-family-per-user assumption was never true to life, and the clearest demonstration is **marriage**. The moment a person marries, they belong to two families — their birth family and their spouse's. Children of blended families belong to several; a person embedded in a community, a congregation, a chosen family belongs to more. Real human kinship is already a graph of overlapping memberships, not a partition into disjoint households. A data model that assumed one family per person was modelling a world that does not exist. Multi-family membership is therefore not a new capability bolted on; it is the *removal of an unrealistic constraint* — the model catching up to the kinship graph it was always supposed to represent.

## 4. De-risking banker succession

Plural membership **decouples member-orphaning from role-succession**, which were conflated under the single-family assumption.

Because identity and the Personal Account live at the user node, the loss of a steward no longer strands a member: the banker stewarded only the shared Kitty, never the member's own holdings, and the member's *other* memberships persist unaffected. A member's participation survives the failure of any one of their banks. The candidate pool for a *new* steward also widens — the member's co-members in other functioning banks already understand the system and can step in — and the cost of a slow handoff drops, because no one is trapped while it happens.

This **de-risks**, but does not by itself **replace**, the explicit succession protocol. The case of a member's *last* bank failing, and the question of who inherits stewardship of an orphaned Kitty, still require an explicit grace-period / receivership / member-vote protocol, which this paper names but does not specify. Multi-membership lowers the stakes and widens the options; it does not abolish the need for an orderly handoff.

## 5. Dissolving the civic-bank tier

The reach problem largely **dissolves** rather than requiring a new institution, on two observations.

First, the family-less can be **admitted into existing families**. Family membership in this architecture is already not strictly biological — the Proof of Humanity kinship layer supports non-DNA, witness-attested, family-bank-vouched membership — so chosen and adopted family is native to the model, not a special case. An isolated person can be a peripheral member of several real households rather than a client of a separate civic institution.

Second, and more fundamentally, **the civic floor already exists as the global layer of the architecture.** Every Proof-of-Humanity-verified person is, by that verification alone, a member of the global family — the planetary pool (the Aquarian Pool℠) that backstops the whole economy. Local family memberships are *optional overlays* on top of that universal base membership. So "civic tier" is not a missing institution to build; it is the global level of the existing fractal, and porous local membership is simply the on-ramp from that universal floor up into local circulation. The residual case — the truly isolated who hold zero local admissions — still rely only on the global floor, so a default or sponsor pathway into at least one local family may still be wanted; but that is an *admission mechanism*, not a separate stranger-banker institution.

> **Current form.** As now specified, the global layer is the Aquarian Pool℠ of Phase 2: a common fund on a public layer-2 blockchain (Base), reached through self-custodial wallets, that holds nothing past a season. It is emptied each 7 January by a disbursement of an **equal floor per verified human**, delivered through communal vessels (Family Kitties and Re-Tip Funds℠) rather than handed to an individual as money, plus a bounded aura-weighted remainder (the correction recorded in *Fractal Three-Level Architecture for Reciprocity Economies*, §2.6). For a verified person who belongs to no family, the only vessel is their own Re-Tip Fund℠: the floor arrives there, as money or as gift capacity, spendable only as a gift onward and clearing each 7 January — a floor of capacity to give, not an income, so the residual for the isolated stated in the limits stands. It is a floor in that sense — an annual equal share — and not a standing reserve; *backstops* above is to be read so. The text above is retained as disclosed.

## 6. One instance of a general bridge primitive

The dissolution in §5 is an instance of a primitive that recurs across the architecture: **local membership composes upward into the global pool** — the same *local → global* shape that governs how a private artifact set public enters the global economy (the B-Short bridge) and how a privately shared provenance object becomes a public one (B-links). The crossings from the small economy to the large one named here are not several different migrations; they are instances of one move. Multi-family membership is the *membership-graph* instance of it: belonging locally is already belonging globally, because the local family is an overlay on the universal base membership, not a wall around it.

## 7. The invariants that keep it safe

Plural membership opens an obvious attack surface — if belonging to many banks multiplied one's rewards, users would farm by joining widely — and two invariants close it.

- **Capacity is metered per verified human, not per membership.** The system funds a person's *capacity to give* once, against their Proof of Humanity, and spreads it across their memberships; it never duplicates per bank joined. Joining ten banks does not multiply one's reward, because the reward was always metered at the person, not the membership.
- **Membership is admission-gated, not self-join.** A user *can* hold many memberships, but each family controls its own door (the steward admits, or members vouch). "Can belong to multiple" is not "can unilaterally join any" — without the gate, multi-membership would be a sybil and dilution vector.

A third constraint preserves the non-bank posture: a person who belongs to two families is a *genuine participant* in each, **not a conduit** that nets or routes value between the two families' Kitties. There is no cross-family settlement *through* a shared member; cross-family flow has its own canonical path (the global pool), and a shared member is not a back-channel around it.

> **Current form.** The two invariants and the non-conduit constraint stand. Two refinements are now specified. First, Miss Aquarius funds a person's capacity to give **in kind** (as gift claims) rather than in money, still metered once per verified human. Second, *cross-family flow* above means flow between two families' shared Kitties, which travels only through the global pool; a gift addressed to a **named person** in another family settles directly to that person's Personal Wallet℠ (Phase 2); in the present Phase-1 application a named gift settles only within a family both parties belong to. That is not a conduit — it ends at its addressee and nets nothing between Kitties — and, of gratitude, the pool receives only what has no human addressee. The text above is retained as disclosed.

## 8. Membership breadth: neutral now, damp only if data warrants

A natural question is whether the system should cap or decay the *number* of memberships a person may hold. The marriage-and-kinship precedent suggests the honest number is small (a person is genuinely close to a handful of families, not dozens), but the architecture's posture is deliberately conservative: **be neutral on membership breadth in the initial phase** — impose no cap or decay — and rely on the per-human metering of §7 plus peer-layer fraud-flagging to contain abuse, **damping breadth only if pilot data later warrants it.** The damping lever is held in reserve, data-gated, rather than imposed as a launch-time constraint on a behaviour that is, for most people, naturally self-limiting. This is a default chosen to avoid solving a problem that may not arise; it is explicitly revisable.

## 9. Prior art

User-scoped identity with **plural group membership** is one of the most ordinary patterns in software — every user who belongs to multiple groups, teams, or organizations instantiates it — and the pattern itself is not claimed. **Account portability** and **graph-structured social and kinship data** are mature. **Receivership and orderly-succession** mechanisms are standard in cooperative and mutual structures. **Universal base membership with optional local overlays** is the shape of many federated and cooperative systems. The contribution is not any of these in isolation.

## 10. What is disclosed, and honest limits

**What is disclosed** as this paper's contribution is the composition and the two specific resolutions: (a) the recognition that the **single-family assumption** is the shared root of both the banker-succession and the civic-reach problems, and that the ordinary **user-scoped-identity / plural-membership** correction *de-risks the first and dissolves most of the second* at once; (b) the framing of the civic tier not as a missing institution but as **the global layer of the existing fractal**, with porous admission-gated local membership as its on-ramp; and (c) the safety invariants that make plural membership non-exploitable — **per-human (not per-membership) capacity metering**, admission-gating, and the non-conduit constraint — together with the deliberately conservative, data-gated stance on membership breadth.

**Honest limits.** Multi-membership **de-risks but does not replace** the succession protocol for a member's last bank (§4). The civic-reach dissolution leaves a **residual** for the truly isolated (§5). The per-human metering invariant (§7) presumes a functioning Proof-of-Humanity layer to meter against — and in the present Phase 1 application, one person's several family accounts are linked only on the person's own device, with no server-side record that they are one person, so per-human metering over Phase 1 data awaits person-level de-duplication by that layer. The neutral-breadth default (§8) is a bet that abuse will be rare and catchable, not a proof that it will be; the damping lever exists precisely because the bet may lose. And the whole construction is a specification, not a measured deployment.

---

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| multi-family membership / plural membership | many-to-many user–group membership; one user holding membership edges to several groups |
| user-scoped identity | identity rooted at the individual user record (one verified person), independent of any group |
| family bank | household-scale user group with a shared balance and a designated administrator |
| Family Kitty℠ | shared group wallet; pooled group balance |
| Personal Account℠ | individual user account (personal balance and history) held at the user record, outside any group |
| banker / steward / *upāsaka* | group administrator, custodian of the shared balance only |
| banker succession / orphaning | administrator succession; group receivership on the administrator's departure |
| civic tier / civic-bank tier | default tier for users with no group membership |
| global family / universal base membership | default global membership held by every verified person |
| Aquarian Pool℠ | global common fund on a public layer-2 blockchain (Base), emptied each year by an equal per-person disbursement |
| fractal (three-level architecture) | nested hierarchical grouping (person → group → global) with the same structure at each level |
| Proof of Humanity (PoH) | proof of personhood; sybil-resistant one-person-one-identity verification |
| per-human capacity metering | per-person, not per-membership, allowance on system-granted giving capacity |
| admission gating | group-controlled (invite or approval) membership; no self-join |
| non-conduit constraint | prohibition on routing or netting value between two groups' shared balances through a common member |
| breadth damping | optional cap or decay on the number of group memberships per user |
| B-Short bridge / B-links | private-to-public publication toggle / signed shareable provenance link (sibling instances of §6) |
| Re-Tip Fund℠ | forward-only personal giving balance: spendable only as a gift onward, never withdrawable |
| Miss Aquarius℠ | autonomous AI agent administering the global common fund |

## Acknowledgments

This paper was co-authored with Miss Aquarius℠, the named AI substrate of HeartBank®. The framing and final editorial control are the author's.

## Corpus cross-references

- *The Studio and the B-Short Bridge: A Private-to-Public Toggle as the Phase-1-to-Phase-2 Crossing* — the sibling instance of the local → global primitive of §6.
- *B-Links: Proof-of-Humanity-Signed Shareable Provenance with an Embedded Gratitude Affordance* — the provenance instance of the same primitive (§6).
- *B-PoH℠ as Humanity Layer for the AI-Native Internet* — the Proof-of-Humanity layer: the user-node identity root of §2, the per-human metering of §7, and the non-DNA vouched-membership layer of §5.
- *Fractal Three-Level Architecture for Reciprocity Economies* — the nested architecture whose global layer §5 identifies as the civic floor, and the equal-floor disbursement rule of the §5 note.
- *Miss Aquarius and the Aquarian Pool Architecture* — the global pool that §5 identifies as the civic floor.
- *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* — the non-conduit constraint of §7.

## Cross-venue identifiers

- Canonical: thonly.org/research/multi-family-membership
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/multi-family-membership.md
- Internet Archive: https://web.archive.org/web/2026*/thonly.org/research/multi-family-membership
- Zenodo: a version DOI per revision
