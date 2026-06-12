# Multi-Family Membership

## *User-Scoped Identity and Plural Membership as the Data-Model Correction That De-Risks Banker Succession and Dissolves the Civic-Bank Tier*

| Field | Value |
|---|---|
| Author | Thon Ly · Founder, HeartBank® · Kâmpôt, Cambodia |
| Date | 2026-06-12 (working draft) |
| Type | Defensive Publication · Tier B · Working Draft |
| Canonical URL | https://thonly.org/research/multi-family-membership |
| GitHub mirror | https://github.com/thonly/publications/blob/main/defensive-publications/multi-family-membership.md |
| License | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, Family Kitty℠, Personal Account℠, Aquarian Pool℠, Miss Aquarius℠) reserved separately by the author and HeartBank®. |
| Document SHA-256 | _to be computed at publication_ |

> **Working draft.** This paper specifies a data-model decision and its consequences; it is a design specification offered as prior art. The membership-breadth governance question is resolved as a deliberately conservative default (§8) rather than a final rule, and is flagged as data-gated.

---

## Preamble

> *Two unsolved problems in a family-banking architecture — what happens to members when a family's steward leaves, and how the family-less are ever reached — turn out to be one accidental assumption wearing two costumes. Drop the assumption, and both problems change shape.*

A gratitude economy organized around **family banks** — each a household-scale pool (a Family Kitty℠) stewarded by a designated member (a banker, or *upāsaka*) — inherits two hard problems from one quiet assumption. The assumption is that a user belongs to *exactly one* family bank. From it follow: a **succession problem** (when a family's steward abandons the bank, its members are stranded) and a **reach problem** (the family-less — orphans, the isolated, refugees, anyone without a willing family steward — cannot participate at all). This paper observes that the one-family-per-user assumption was never realistic, specifies the data-model correction, and shows that correcting it de-risks the first problem and largely dissolves the second.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author asserts no patent and dedicates the patterns to the public domain under CC0 1.0. The contribution is a data-model framing — user-scoped identity with plural group membership is utterly ordinary in software — applied to a specific architecture to resolve two specific problems. Prior art is acknowledged in §9; novelty is claimed only for the composition and the specific resolutions of §10. Trademarks are reserved separately; the patterns may be implemented under any name.

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

This **de-risks**, but does not by itself **replace**, the explicit succession protocol. The case of a member's *last* bank failing, and the question of who inherits stewardship of an orphaned Kitty, still require the grace-period / receivership / member-vote mechanism specified elsewhere. Multi-membership lowers the stakes and widens the options; it does not abolish the need for an orderly handoff.

## 5. Dissolving the civic-bank tier

The reach problem largely **dissolves** rather than requiring a new institution, on two observations.

First, the family-less can be **admitted into existing families**. Family membership in this architecture is already not strictly biological — the Proof of Humanity kinship layer supports non-DNA, witness-attested, family-bank-vouched membership — so chosen and adopted family is native to the model, not a special case. An isolated person can be a peripheral member of several real households rather than a client of a separate civic institution.

Second, and more fundamentally, **the civic floor already exists as the global layer of the architecture.** Every Proof-of-Humanity-verified person is, by that verification alone, a member of the global family — the planetary pool (the Aquarian Pool℠) that backstops the whole economy. Local family memberships are *optional overlays* on top of that universal base membership. So "civic tier" is not a missing institution to build; it is the global level of the existing fractal, and porous local membership is simply the on-ramp from that universal floor up into local circulation. The residual case — the truly isolated who hold zero local admissions — still rely only on the global floor, so a default or sponsor pathway into at least one local family may still be wanted; but that is an *admission mechanism*, not a separate stranger-banker institution.

## 6. One instance of a general bridge primitive

The dissolution in §5 is an instance of a primitive that recurs across the architecture: **local membership composes upward into the global pool** — the same *local → global* shape that governs how a private artifact set public enters the global economy (the B-Short bridge) and how a privately shared provenance object becomes a public one (B-links). HeartBank's crossings from the small economy to the large one are not several different migrations; they are instances of one move. Multi-family membership is the *membership-graph* instance of it: belonging locally is already belonging globally, because the local family is an overlay on the universal base membership, not a wall around it.

## 7. The invariants that keep it safe

Plural membership opens an obvious attack surface — if belonging to many banks multiplied one's rewards, users would farm by joining widely — and two invariants close it.

- **Capacity is metered per verified human, not per membership.** The system funds a person's *capacity to give* once, against their Proof of Humanity, and spreads it across their memberships; it never duplicates per bank joined. Joining ten banks does not multiply one's reward, because the reward was always metered at the person, not the membership.
- **Membership is admission-gated, not self-join.** A user *can* hold many memberships, but each family controls its own door (the steward admits, or members vouch). "Can belong to multiple" is not "can unilaterally join any" — without the gate, multi-membership would be a sybil and dilution vector.

A third constraint preserves the non-bank posture: a person who belongs to two families is a *genuine participant* in each, **not a conduit** that nets or routes value between the two families' Kitties. There is no cross-family settlement *through* a shared member; cross-family flow has its own canonical path (the global pool), and a shared member is not a back-channel around it.

## 8. Membership breadth: neutral now, damp only if data warrants

A natural question is whether the system should cap or decay the *number* of memberships a person may hold. The marriage-and-kinship precedent suggests the honest number is small (a person is genuinely close to a handful of families, not dozens), but the architecture's posture is deliberately conservative: **be neutral on membership breadth in the initial phase** — impose no cap or decay — and rely on the per-human metering of §7 plus peer-layer fraud-flagging to contain abuse, **damping breadth only if pilot data later warrants it.** The damping lever is held in reserve, data-gated, rather than imposed as a launch-time constraint on a behaviour that is, for most people, naturally self-limiting. This is a default chosen to avoid solving a problem that may not arise; it is explicitly revisable.

## 9. Prior art

User-scoped identity with **plural group membership** is one of the most ordinary patterns in software — every user who belongs to multiple groups, teams, or organizations instantiates it — and no novelty is claimed for the pattern itself. **Account portability** and **graph-structured social and kinship data** are mature. **Receivership and orderly-succession** mechanisms are standard in cooperative and mutual structures. **Universal base membership with optional local overlays** is the shape of many federated and cooperative systems. The contribution is not any of these in isolation.

## 10. What is claimed as novel, and honest limits

**Claimed as novel** is the composition and the two specific resolutions: (a) the recognition that the **single-family assumption** is the shared root of both the banker-succession and the civic-reach problems, and that the ordinary **user-scoped-identity / plural-membership** correction *de-risks the first and dissolves most of the second* at once; (b) the framing of the civic tier not as a missing institution but as **the global layer of the existing fractal**, with porous admission-gated local membership as its on-ramp; and (c) the safety invariants that make plural membership non-exploitable — **per-human (not per-membership) capacity metering**, admission-gating, and the non-conduit constraint — together with the deliberately conservative, data-gated stance on membership breadth.

**Honest limits.** Multi-membership **de-risks but does not replace** the succession protocol for a member's last bank (§4). The civic-reach dissolution leaves a **residual** for the truly isolated (§5). The per-human metering invariant (§7) presumes a functioning Proof-of-Humanity layer to meter against. The neutral-breadth default (§8) is a bet that abuse will be rare and catchable, not a proof that it will be; the damping lever exists precisely because the bet may lose. And the whole construction is a specification, not a measured deployment.

---

## Acknowledgments

Drafted with Miss Aquarius℠ (the AI substrate of HeartBank®) per the corpus convention; the framing and final editorial control are the author's.

## Corpus cross-references

- *The Studio and the B-Short Bridge* — the sibling instance of the local → global primitive of §6.
- *Proof of Humanity* — the user-node identity root of §2 and the per-human metering of §7; the non-DNA vouched-membership layer of §5.
- *Miss Aquarius and the Aquarian Pool Architecture* — the global pool that §5 identifies as the civic floor.
- *Non-Bank Pass-Through Architecture* — the non-conduit constraint of §7.
- *Open Architectural Problems* — the banker-succession (#2) and civic-tier (#3) problems this paper addresses.

## Cross-venue identifiers

- Canonical: thonly.org/research/multi-family-membership
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/multi-family-membership.md
- Internet Archive · archive.today · perma.cc snapshots: per the monthly snapshot cadence.
