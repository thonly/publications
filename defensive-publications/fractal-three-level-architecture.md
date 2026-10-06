---
title: "Fractal Three-Level Architecture for Reciprocity Economies: Self-Similar Family-and-Global Layering with a Single Mental Model"
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-c
kind: mechanism
status: draft
date: 2026-05-22
revised: 2026-10-06
license: CC0-1.0
slug: fractal-three-level-architecture
venue: thonly.org/research/fractal-three-level-architecture (canonical)
---

> **Note.** This defensive publication discloses a three-level account architecture — a pooled fund, a give-forward (re-tip) account and an individual's own account — used identically by the family-scale and the planetary-scale, peer-to-peer deployments of one reciprocity platform, together with the transfer conventions that make the two deployments self-similar and the conditions under which the self-similarity breaks. **A correction made in the open on 2026-09-23.** The text first deposited named *aura-weighted scoring* as one of the four transfer conventions — *"destinations and amounts calibrated by the aura primitive"*. That convention was corrected, not re-worded: the collective pool disburses an equal floor per verified human plus a bounded aura-weighted remainder, with its parameters public and frozen in-season. §2.6 states the correction, the deposited wording it replaces and the reason; every place in the body where the old convention appeared now points to §2.6, and two applications of it — to a family steward's distribution decisions and to recipient selection — are withdrawn as errors. The four enumerated claims are unchanged. Later developments of the design, as of the 2026-10-06 revision, are stated in *Current form* notes beside the text they qualify, and that text is retained as disclosed. Companion works in this corpus, each cited by title and corpus slug: *Why Kids Are the Triggers* (essay, `kids-as-triggers-self-thanking`; the pedagogy of the 50/50 split); *Transparency as Enforcement* (`transparency-as-enforcement`); *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (`non-bank-pass-through-architecture-autonomous-ai`); *Verified-Human Anonymous Local Gratitude Transfer* (`verified-human-anonymous-local-giving`); *Manufactured Universal Giving* (`manufactured-universal-giving`); *Decided by No One* (`the-called-draw`).

---

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism, procedure or framework described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practicing any mechanism disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed.

This document constitutes a defensive publication establishing **prior art as of 22 May 2026** for the text as first published, and **as of 23 September 2026** for the matter that revision added. It discloses the three-level architecture of collective pool, re-tip flow-through and personal destination; its transfer conventions, including the floor-and-remainder disbursement rule as corrected in §2.6; the named correspondence between the family-scale (Phase 1) and planetary-scale (Phase 2) deployments, with the terminology note at the head of §3; and the stated conditions under which the self-similarity breaks. A later patent application claiming any of them is filed against this disclosure.

The parts are old. Recursive, self-similar organization — a structure in which each level is described by the same model as the level that contains it — is the subject of Stafford Beer's Viable System Model (*Brain of the Firm*, 1972; the recursive system theorem in *The Heart of Enterprise*, 1979), of the eighth of Elinor Ostrom's design principles for long-enduring common-pool institutions, *nested enterprises* (1990), and of Herbert Simon's account of hierarchic systems in *The Sciences of the Artificial*. Designing so that one learned model serves many situations is a standard principle of interaction design — Donald Norman's conceptual models, and the fourth of Jakob Nielsen's usability heuristics, *consistency and standards* (1994) — and it is the prior art that cuts most directly against claim 2. At family scale, dividing a child's money between a portion for the child's own use and a portion that may only be given away is an established allowance practice (the spend, save and give jars of Lieber 2015), and multi-level community and complementary currencies (Lietaer 2001; Greco 2001) and time banking (Cahn 2000) precede the reciprocity framing. An equal base allocation with a capped variable top-up, the shape of the rule §2.6 adds, is a familiar allocation pattern, and it is disclosed here, not claimed as new. What this document discloses as its own is only the composition enumerated under **Claims**. No prior-art census is on file for it: the paper was first published before the institution adopted its census rule (13 September 2026), which gates a defensive publication's first deposit and was not applied retroactively. No search on record establishes that the composition is unpublished elsewhere, and the authors assert no such absence.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Aquarian Pool℠**, **Family Kitty℠**, **Re-Tip Jar℠**, **Re-Tip Fund℠**, **Personal Account℠** and **Personal Wallet℠** — are separately and explicitly reserved. The architecture is dedicated to the commons; the marks are not.

This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and the document is deposited on Zenodo, each deposited revision a version under one concept DOI, with its source in the public repository `github.com/thonly/publications`. A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim. Prior art as of 22 May 2026 for the first version. Later additions date from the revision that introduced them, so the date of any passage is that of the earliest timestamped version carrying it.

> **Note.** The patent commitment has stood since this paper was first published on 2026-05-22, in the form *"The author and HeartBank® will not seek patent on this specification or any portion thereof"*, in its conclusion and in its closing license line. The words *"in any jurisdiction, at any time"* were added on 2026-09-23, when the statement was given a section of its own. The commitment not to assert, and its extension to the entities named above, were added on 2026-10-06, when the statement was brought to the standard form above. The date relied on for priority is the one carried by this document's OpenTimestamps proof.

---

## Abstract

This paper discloses an account architecture for a reciprocity platform — software through which people give one another money as thanks — designed to operate at two scales, within families and between strangers peer to peer, with one three-level account hierarchy at both, so that a participant who has learned the family-scale system recognizes the planetary-scale one. The three node types are a pooled fund that aggregates contributions and disburses them under published rules; a give-forward account, whose balance can only be passed on to other people; and an individual's own account. Four transfer conventions apply identically at each scale: a proximity constraint on giving; an equal split of each reward a participant receives for recording a kind act of their own, between the individual account and the give-forward account; a disbursement rule for the pooled fund, which pays an equal floor per verified person plus a variable remainder capped so that no account's total exceeds a fixed multiple of the floor, with its parameters public and frozen for each annual season; and an AI agent that recommends amounts within fixed bounds. The design objective is to minimize the number of distinct mental models a full participant must acquire; the saving in learning cost is stated as a hypothesis and has not been measured. The paper also states where the self-similarity breaks — regulation, cultural convention and privacy expectations differ by scale — and confines those differences to the infrastructure beneath an unchanged user-facing structure. The disbursement rule was corrected in the open on 23 September 2026 from an earlier rule that weighted amounts by a reputation signal alone, and later refinements are given in dated notes, with the earlier text retained as disclosed.

**Keywords:** multi-level account hierarchy, pooled fund, household account, family finance, children's allowance, give-forward account, earmarked funds, non-withdrawable balance, reward splitting, peer-to-peer payments, proximity-constrained transfers, short-range radio proximity, AI recommendation bounds, equal base allocation, capped allocation, proof of personhood, mental models, mental-model design, conceptual model, onboarding cost, design consistency, multi-scale platform design, self-similarity, scale invariance, scale-invariant institutional design, recursive design, fractal architecture, reciprocity economy, community currency, gratitude infrastructure, defensive publication.

## Terms

Coined names used in this paper, and the standard terms an examiner or a reader in payments, interaction design or institutional design would search for them.

| Term used here | Standard term |
|---|---|
| fractal three-level architecture; self-similarity | a three-level account hierarchy repeated identically at two deployment scales; scale-invariant, recursive design |
| collective pool | a pooled (common) fund disbursed under published rules |
| re-tip flow-through; re-tip jar; Re-Tip Jar℠ (family scale) · Re-Tip Fund℠ (planetary scale) | a give-forward account: an earmarked, non-withdrawable balance that can only be given to other people |
| personal destination; personal wallet; Personal Account℠ (family scale) · Personal Wallet℠ (planetary scale) | an individual's own account |
| family kitty; Family Kitty℠ | a household's shared, pooled account, administered by a member of the household |
| Aquarian Pool℠ | an institution's common fund, emptied each year, from which an AI agent disburses under published rules |
| Phase 1 · Phase 2 | the family-scale deployment · the planetary-scale, peer-to-peer deployment |
| family steward | the household member who administers the shared account |
| self-thank; self-thank reward | recording one's own kind act; a reward paid for recording it |
| 50/50 split | an equal split of a reward between the recipient's own account and their give-forward account |
| proximity rule; nearby | a constraint that gifts go to recipients physically present (now specified as short-range radio co-presence) |
| Miss Aquarius℠; AI arbiter | the AI agent that recommends transfer amounts |
| band-clamp | a recommendation bounded to a published range |
| aura; aura-weighted | a per-participant signal computed from recorded thanks; weighting by that signal |
| floor-and-remainder disbursement; *k* | an equal base allocation per verified person plus a capped variable top-up; the cap, as a multiple of the base |
| verified human | a person verified by proof of personhood and de-duplicated, so that one person counts once |
| season; annual reset (7 January) | the annual period in which disbursement parameters are frozen; the date on which they may be revised |
| transparency-as-enforcement | social enforcement by visibility within a bounded community, in place of contractual enforcement |
| *brahmavihāra*; *karuṇā*; *muditā* | the four "divine abidings" of Buddhist ethics; compassion; gladness at another's good |
| *dāna* | giving; generosity (Buddhist) |

---

## Claims

*Enumerated 2026-08-29. The mechanisms below were disclosed in full in this paper's original text; **the prior art they establish runs from this document's original publication date and its OpenTimestamps proof, not from this enumeration.** They are listed because a defensive publication is read as prior art by examiners and by opposing counsel, and **a claims list is what such a reader searches; ten thousand words of prose is not.** No claim below adds matter not already present.*

1. **Scale-invariant reciprocity architecture** — a three-level economic structure in which the family-scale and the planetary-scale deployments are instances of one self-similar pattern rather than two separately-designed products, such that a participant learns one mental model and applies it at both scales.
2. **Cognitive cost as the design objective for multi-scale platform structure** — selecting the architecture that minimises the number of distinct mental models a full participant must acquire, rather than the one that optimises either scale independently.
3. **The named correspondence between the Phase 1 and Phase 2 deployments** — the specific mapping under which each family-scale construct has exactly one planetary-scale counterpart occupying the same structural position, so that competence at one scale transfers to the other without retraining.
4. **The stated conditions under which the self-similarity breaks** — the paper's specification of where the fractal must not be extended, which is claimed as part of the architecture rather than as a caveat on it.

**Non-assertion extends to:** all mechanisms above, in any combination, and any implementation thereof.

---

## 1. Introduction

A reciprocity economy that aspires to operate at both family scale and planetary scale faces a design problem familiar to all multi-scale software: the user must understand the system at each scale, and, on this paper's working assumption (unmeasured; see *Honest limits*), the cognitive cost of understanding two scales is close to twice the cost of understanding one. The conventional response is to *separate* the scales into two products with their own interfaces, vocabularies, and mental models; the user picks the product appropriate to their needs and ignores the other. The cost: the two-product separation forecloses cross-scale integration (the user cannot easily route a family-scale transaction to a planetary-scale recipient), creates duplicated infrastructure costs, and prevents the user's mastery of one scale from translating to mastery of the other.

This paper specifies a different design response: build the family-scale and the planetary-scale interactions on a *structurally identical three-level architecture*, so that the mental model the user develops for one scale is *exactly the mental model* they need for the other. The architecture is *fractal* — self-similar across scales — in the strict design sense: the same node-types, the same inter-node transfer conventions, the same AI-arbitration patterns, and the same public-ledger transparency apply at every scale, recursively.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-09-23 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) Keeping it open requires participation across the life arc: a person who learns gratitude reciprocity within their family in childhood, transitions to adult participation in neighborhood-scale gratitude networks, and eventually participates in planetary-scale flows as their resources and reach extend. The fractal three-level architecture is what makes this life-arc transition seamless rather than requiring repeated relearning at each scale; the architecture grows with the user.*

The paper proceeds as follows. §2 specifies the three-level architecture in detail. §3 demonstrates the self-similarity across the family-scale Phase 1 and the planetary-scale Phase 2 of the HeartBank deployment. §4 articulates the four design properties that make the fractality work. §5 articulates the three structural advantages the fractality produces. §6 honestly names the conditions under which the fractality breaks and the supplementary mechanisms that compensate. §7 closes.

---

## 2. The three-level architecture

### 2.1 The three node-types

The architecture has exactly three node-types, used recursively at every scale:

- **Collective pool** — a node that aggregates contributions from multiple participants and disburses to multiple destinations under rule-bound logic, governed by an AI arbiter with public-ledger transparency.
- **Re-tip flow-through** — a node that receives a single transfer and routes it (possibly with some delay; possibly with some splitting) to one or more downstream destinations, again under rule-bound logic with public-ledger transparency.
- **Personal destination** — a node that is the terminal point of a transfer flow, owned by a single participant for their own use without onward routing obligation.

These three node-types are sufficient to describe the full architectural surface. Every node in the system is exactly one of these three; every transfer in the system is between two of these node-types.

### 2.2 The transfer conventions

Transfers between node-types follow a small set of conventions:

- **Proximity rule** — transfers are constrained by geographic / relational proximity at all scales (family members, neighbors, city-area participants, regional networks). The proximity rule is offered as a structural limit on laundering risk, not as compliance with anti-money-laundering law; it applies identically at every scale.
- **50/50 split convention** — a self-thank reward (a participant's own reward for engaging the gratitude flow) splits 50/50 between personal wallet and re-tip jar, at every scale. The convention's pedagogical content (set out in the essay *Why Kids Are the Triggers*, `kids-as-triggers-self-thanking`) operates identically at every scale.
- **Floor-and-remainder disbursement** *(corrected 2026-09-23; this bullet previously read "aura-weighted scoring" — see §2.6)* — when the collective pool disburses to the flow-through nodes, it disburses an **equal floor per verified human**, delivered through that person's flow-through node, plus an **aura-weighted remainder bounded so that no node's total exceeds k × the floor**. The parameters (floor : remainder, and k) are public and frozen for the season. The aura never selects a recipient. The rule is identical at every scale; the parameter values may differ by scale.
- **AI arbiter band-clamp recommendation** — Miss Aquarius recommends amounts within an institutional band-clamp at every transfer surface, at every scale. The arbiter operates identically; the clamp values differ by scale.

> **Current form.** At planetary scale, *nearby* is now specified as radio co-presence at the moment of giving — the giver's and the recipient's phones in short-range radio contact (Bluetooth Low Energy, or ultra-wideband where both phones have it), together with device attestation and a biometric check at the moment of action — and not as a geographic radius: no satellite position is read and no location is stored. The proximity signal broadcasts rotating identifiers, never a stable one, so that it cannot serve as a tracking beacon, and co-presence is treated as a gate, not a proof. The rule governs giving from the give-forward account; a preference for nearby businesses in what the system surfaces is a separate matter. The geographic wording above is retained as disclosed.

### 2.3 The AI arbiter as scale-invariant operator

The AI arbiter operates identically at every scale. The family-scale arbiter is the *same arbiter* as the planetary-scale arbiter, applying the same recommendation pattern with scale-appropriate clamp values. This is not merely an implementation efficiency; it is the substrate that makes the mental-model translation seamless. A user who has internalized "Miss Aquarius recommends an amount; I can accept or modify within a small band" at family scale recognizes the same pattern at planetary scale and does not need to learn a new arbiter mental model.

### 2.4 The public-ledger transparency

The transparency-as-enforcement pattern (*Transparency as Enforcement*, `transparency-as-enforcement`) applies uniformly at every scale. Family-scale transfers are visible to the family; neighborhood-scale transfers are visible to the neighborhood; planetary-scale transfers are visible at the appropriate platform-wide aggregate (with individual-resolution masked per the participant's privacy preferences). The *pattern* of transparency is identical; the *scope* of transparency adjusts to the scale.

> **Current form.** At neighborhood and planetary scale the design is now narrower than *visible* above, and the paragraph is retained as disclosed. Gifts given under the proximity rule to people nearby are anonymous to their recipients, while each giver is verified as a human to the system (*Verified-Human Anonymous Local Gratitude Transfer*, `verified-human-anonymous-local-giving`). In the design as now specified, the log of thanks keeps its entries private to their parties and publishes only signed proofs that an entry is included and that the log has only been appended to; where it records a settled money transfer, it records the fact of settlement, never the amount. The pattern of this section holds in full at family scale, where the bounded-community condition of *Transparency as Enforcement* is met.

### 2.5 The architecture in one diagram

The architecture combines three node-types in a directional flow, with the same four transfer conventions applying at every transfer surface:

```
   ┌─────────────────────────────────────────────────────────────┐
   │  COLLECTIVE POOL                                            │
   │  Aggregates contributions; disburses to many under          │
   │  rule-bound logic with public-ledger transparency           │
   │  (Aquarian Pool at every scale)                             │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  │  ← four transfer conventions
                                  │     (proximity / 50-50 split /
                                  │      floor + bounded remainder /
                                  │      AI arbiter band-clamp)
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  RE-TIP FLOW-THROUGH                                        │
   │  Receives a single transfer; routes to one or more          │
   │  downstream destinations under rule-bound logic             │
   │  (Phase 1: Family Kitty   /   Phase 2: Re-Tip Fund)         │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  │  ← the same four transfer
                                  │     conventions
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  PERSONAL DESTINATION                                       │
   │  Terminal point of flow; owned by single participant        │
   │  (Phase 1: Personal Account   /   Phase 2: Personal Wallet) │
   └─────────────────────────────────────────────────────────────┘
```

*The labels above were corrected on 2026-10-06: the diagram previously read "Re-Tip Jar @ Phase 2" and "Personal Wallet at every scale", which assigned two product names to the wrong deployment (see the terminology note at the head of §3).*

The four transfer conventions operate at every transfer surface above:

| Convention | What it does at every scale |
|---|---|
| **Proximity rule** | Transfers constrained by geographic / relational closeness (family ↔ neighborhood ↔ region) |
| **50/50 split** | Self-thank reward splits between personal wallet and re-tip jar — same pedagogy, same proportions |
| **Floor-and-remainder disbursement** *(corrected; §2.6)* | The pool's disbursement to flow-through nodes: an equal floor per verified human, plus an aura-weighted remainder bounded at k × the floor; parameters public and frozen in-season; rule identical at every scale |
| **AI arbiter band-clamp** | Miss Aquarius recommends within an institutional band; clamp values differ by scale, arbiter operates identically |

The self-similarity is structural: the *same* three node-types, the *same* four conventions, the *same* arbiter, the *same* transparency pattern — at every scale. A user who has internalized the architecture at family scale recognizes the same architecture at planetary scale and does not need to learn a new mental model. Phase 1 → Phase 2 is not a new product; it is the same architecture extended beyond the family.

### 2.6 Correction (2026-09-23): how the collective pool disburses

*Added in the 2026-09-23 revision. A correction to a deposited mechanism, stated in the open rather than re-worded.*

**What the deposited text said.** Among the four transfer conventions, §2.2 listed *"Aura-weighted scoring — destinations and amounts are calibrated using the aura primitive (the cross-currency reputational signal), at every scale."* §3.1 applied it to "the family steward's distribution decisions" and §3.2 to "recipient selection." Those sentences now read as corrected above; this section records what they said and why they changed.

**What replaces it.** When the collective pool disburses to the flow-through nodes, it does so in two parts, under four rules.

1. **An equal floor per verified human.** One person, one floor — however many accounts they hold or families they belong to. The floor is delivered **through the person's flow-through node** (the family kitty at family scale, the participant's re-tip flow-through at planetary scale), never straight into a personal destination: the pool's own-initiative disbursements fill flow-through nodes only, and whatever reaches a personal destination arrives there by a person's act.
2. **A bounded remainder, weighted by the aura read as a witness-count** — how much witnessed giving has crossed a node — never as a measure of anyone's worth or of what they hold. The remainder is bounded so that **no node's total exceeds k × the floor.**
3. **The parameters are public and frozen for the season.** The ratio of floor to remainder, the bound k and the cadence are published, cannot change mid-season, and are revised only at the annual reset.
4. **No share is ever rendered as a rank, a comparison or a rate.**

> **Current form.** Rule 1's account has since been specified further, and rules 1 and 2 above are retained as disclosed. The floor is one, equal in value per verified human, and it is paid into that person's own re-tip flow-through — at planetary scale the Re-Tip Fund℠; a child's included, where the same account appears on the family surface as the child's Re-Tip Jar℠ (one account, two names), its key held by a parent until the child comes of age and never by the institution. It is a floor of the capacity to give, delivered as food where shops have agreed to give it, and as money everywhere else: a target share of each floor, itself a public parameter frozen for the season, is delivered in kind, as gifts of goods from shops that have committed quotas, and whatever those quotas could not carry is paid in money into the same account by the season's end, so that every floor is equal in value. No person's split between goods and money, and no shortfall or top-up, is ever displayed. The bounded remainder is unchanged, and family kitties continue to receive the pool's contributions; a family kitty receives a floor only for a verified child who has no give-forward account of their own: one floor per child, never more. The pool's own-initiative disbursements still reach no personal destination. The aura that weights the remainder reads only recorded thanks: money from any account never moves it, and no amount of money, time or goods is an input to it.

```
   ONE SEASON'S DISBURSEMENT — the pool to three flow-through nodes

   node A   ██████████ │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
   node B   ██████████ │▒▒▒▒▒▒                          │
   node C   ██████████ │                                │
            └─ floor ─┘ └──── aura-weighted remainder ──┘
            equal, per   bounded: no node's total may exceed
            verified     k × the floor (here k = 4)
            human

   ▸ the largest total is at most k times the smallest — by construction
   ▸ floor : remainder, k and the cadence are public and frozen in-season
   ▸ no node's share is ever displayed beside another's
```

**Why a floor.** The deposited convention had none. Under it, a node that had carried little giving would receive little, so the pool would have allocated the *means* of giving by the record of *past* giving — the opposite of the universal means that *Manufactured Universal Giving* (`manufactured-universal-giving`) depends on. The verified human is the unit because, once each person is counted once (*Honest limits*), it cannot be multiplied by opening accounts or joining families.

**Why the remainder is bounded — the anti-rank bound.** An unbounded weight on amounts has magnitude, and magnitude invites comparison. A share that can be published, or inferred, becomes a league table of families or persons — a rank, which the institution refuses in every surface. The bound k caps the ratio between any two nodes' totals, so the disbursement cannot distinguish participants by more than a published factor, and rule 4 keeps even that from being displayed. Once the disbursement function is written, the bound is a property of the function rather than a promise by its operator: no operator can exceed it without replacing the function.

**Why the remainder is not drawn.** The corpus's called draw (*Decided by No One*, `the-called-draw`) governs turns — decisions in which every eligible party deserves the same number of turns. A disbursement proportional to something is not a turn, and forcing it into a draw would hide a judgment behind a mechanism. The equal part of this rule is the floor; the weighted part is a bounded weight on an amount, never an order of persons.

**A shape rule, not a mandate.** The rule governs *how* the pool disburses, not *that* it must. If it disburses at all, it disburses an equal floor per verified human, with no node above k × the floor. The floor may shrink only as a consequence of human giving rising, never as an instrument for moving a number.

**What did not change.** The four enumerated claims stand as written. The fractal property is not weakened; it is cleaner. The deposited convention was applied in three different places — the pool, a steward's distribution, and recipient selection — and only one of those was a pool disbursing. The corrected convention applies in exactly one place, the transfer from collective pool to flow-through node, and it applies there identically at both scales.

---

## 3. Self-similarity across the Phase 1 and Phase 2 deployments

The HeartBank deployment instantiates the three-level architecture at two scales: family-scale Phase 1 (the Treasury product for families, currently live — a record kept above licensed payment rails, not a bank) and planetary-scale Phase 2 (the peer-to-peer global flow architecture, under development).

> **Terminology note (2026-10-06).** This paper names its nodes descriptively — *pool*, *family kitty*, *re-tip jar*, *personal wallet*. The product lexicon the institution adopted on 15 May 2026, a week before this paper was first published, names the three levels of each deployment as follows.
>
> | Level | Family scale (Phase 1) | Planetary scale (Phase 2) |
> |---|---|---|
> | Collective pool | Family Kitty℠ | Aquarian Pool℠ |
> | Re-tip flow-through | Re-Tip Jar℠ | Re-Tip Fund℠ |
> | Personal destination | Personal Account℠ | Personal Wallet℠ |
>
> Three differences follow; two are of name only, and the third is of level, not of flow. Where §3.2 and §3.3 call the planetary-scale flow-through the *re-tip jar*, its product name is the Re-Tip Fund℠; the Re-Tip Jar℠ is the family-scale flow-through, the account into which the 50/50 split of §2.2 pays at family scale. Where §3.1 and §3.3 call the family-scale personal destination a *personal wallet*, its product name is the Personal Account℠. And the lexicon places the Family Kitty℠ at the collective-pool level of the family deployment — by the definitions of §2.1 it is a collective pool, since it aggregates the family's contributions and disburses them to several members — and the Aquarian Pool℠ at that level of the planetary deployment; the Aquarian Pool also contributes to family kitties. The money moves along the same paths under either reading — pool to kitty, kitty to member — and the table in §3.1, which places the Aquarian Pool above the family scale and the family kitty at the flow-through level, is retained as disclosed. Under either arrangement each family-scale construct has exactly one planetary-scale counterpart in the same structural position, which is what claim 3 states. This paper keeps the Re-Tip names in which it was published.

### 3.1 Phase 1 — family scale

| Three-level node | Phase 1 instance |
|---|---|
| **Collective pool** | The Aquarian Pool (institutional pool from which family-kitty funding flows on an annual Jan 7 cycle) |
| **Re-tip flow-through** | The family kitty (multi-party transaction account on regulated rails; the family steward routes flows from the kitty to personal wallets per Miss Aquarius's band-clamp recommendation and family-level governance) |
| **Personal destination** | The family member's personal wallet (or, for child participants, the parent-supervised child wallet) |

The transfer conventions at family scale: proximity is the family relationship; 50/50 split applies to the kid's self-thank reward; the pool's contribution to the family kitty is an equal floor per verified family member plus a bounded remainder (§2.6) — *the deposited text applied aura-weighted scoring to "the family steward's distribution decisions"; that application is withdrawn: the steward is a person, and how a person distributes is theirs to decide, never scored*; band-clamp AI recommendations operate on every disbursement.

> **Current form.** Under the note in §2.6, the pool's floor now goes to each person's own re-tip flow-through, a child's included, and not to the family kitty; a kitty receives a floor only for a verified child who has no account of their own. The pool's other contributions to family kitties are made anonymously and through the year, within the bound of §2.6; 7 January marks the annual reset of the season, not the date of a single disbursement. The table and paragraph above are retained as disclosed.

### 3.2 Phase 2 — planetary scale

| Three-level node | Phase 2 instance |
|---|---|
| **Collective pool** | The Aquarian Pool (same Pool as Phase 1 — the institutional pool is identical at both scales) |
| **Re-tip flow-through** | The re-tip jar (per-participant flow-through account into which Miss Aquarius's anonymous donations and other participants' tips flow; the participant routes outgoing tips from the re-tip jar to neighborhood-proximity-constrained recipients) |
| **Personal destination** | The participant's personal wallet (terminal destination for tips received) |

The transfer conventions at planetary scale: proximity rule constrains re-tip flows to geographic neighborhoods; 50/50 split applies to the participant's self-thank reward (mirroring the Phase 1 pedagogy); the pool's contribution to each participant's flow-through node is an equal floor per verified human plus a bounded remainder (§2.6) — *the deposited text applied aura-weighted scoring to "recipient selection"; that application is withdrawn: recipients are chosen by the participant who gives, and the pool selects no recipient*; band-clamp AI recommendations operate on every recommendation surface.

> **Current form.** *Nearby* is now radio co-presence at the moment of giving rather than a geographic neighborhood (§2.2, *Current form*), and the floor reaches each participant's own re-tip flow-through as stated in the note in §2.6. The table and paragraph above are retained as disclosed.

### 3.3 The self-similarity is structural

The Phase 1 and Phase 2 architectures are not merely *thematically similar*; they are *structurally identical*. A user who has internalized the Phase 1 mental model — "the Pool funds the kitty; the kitty funds my wallet; I can self-thank with the 50/50 split, with Miss Aquarius recommending amounts within a band, and the family can see what flows where" — recognizes the Phase 2 mental model immediately as the *same model at a different scale*: "the Pool funds the re-tip jar; the re-tip jar funds my wallet (or my neighbor's wallet via re-tip); I can self-thank with the 50/50 split, with Miss Aquarius recommending amounts within a band, and the platform can see what flows where."

The transition from Phase 1 to Phase 2 is, for a user who has been participating in Phase 1, *not a new product to learn*. It is the *same product extended to neighbors and beyond*.

---

## 4. Four design properties that make the fractality work

### 4.1 The same node-types at every scale

Every node in the system is one of the three node-types. The architecture admits no hybrid node-types that would require a per-scale mental-model adjustment. This is the structural property that allows the user's mental-model investment at one scale to translate to the next.

### 4.2 The same transfer conventions at every scale

The proximity rule, the 50/50 split convention, the floor-and-remainder disbursement (corrected from *aura-weighted scoring*; §2.6), and the AI arbiter band-clamp recommendation are *identical* at every scale. The substance of each convention adjusts to the scale (proximity is family-relationship at family scale; geographic-neighborhood at planetary scale), but the convention itself is the same.

### 4.3 The same AI arbiter at every scale

Miss Aquarius is the single AI arbiter operating across all scales. There is no scale-specific arbiter. The recommendation pattern is identical; the clamp values adjust to the scale-appropriate institutional governance.

### 4.4 The same public-ledger transparency at every scale

The transparency-as-enforcement pattern applies uniformly. The scope of visibility adjusts to the scale; the pattern of visibility is identical.

---

## 5. Three structural advantages the fractality produces

### 5.1 Cognitive onboarding savings

A user who has internalized the Phase 1 mental model is expected to pay little additional cognitive cost to participate in Phase 2 — an expectation this paper has not measured (*Honest limits*). The architecture is *recognized* rather than *learned*. The expected saving at the institutional level is of the same kind: support documentation, tutorial content, customer-support interactions, and feature-discovery surfaces can leverage the user's existing mental model rather than constructing a parallel one.

### 5.2 Mental-model durability across the life-arc transition

A user who participates in HeartBank at family scale as a child, transitions to adult participation at neighborhood scale, eventually participates in planetary-scale flows as their resources and reach extend, encounters the *same mental model* throughout the life arc. The architecture grows with the user. This is structurally different from the conventional financial-system trajectory in which a user learns family-finance, then re-learns personal-banking, then re-learns wealth-management, then re-learns charitable-giving — each scale requiring its own mental model with limited cross-translation.

### 5.3 Architectural learnability for adjacent institutions

Other institutions adopting reciprocity-economy patterns can adopt the three-level architecture at their relevant scale and inherit the architectural learnability for their users. The architecture is offered as a defensive publication so that other institutions can adopt it without any patent claim from its authors; a publication cannot clear patents held by others.

---

## 6. Conditions under which the fractality breaks

The fractality is not unconditional. Three conditions can break it.

### 6.1 Scale-specific regulatory regimes

Different scales may face different regulatory regimes that require scale-specific surfaces. The act a family-scale transfer records — a parent giving a child an allowance — is not itself a regulated activity, but a platform that holds or moves the money is subject to money-transmission or payment-services law at either scale in many jurisdictions, and peer-to-peer transfers between strangers, and across borders, add obligations that transfers inside a household do not. The architectural response: keep the *user-facing* architecture identical across scales; route the regulatory complexity into the institutional-infrastructure layer where it does not affect the user's mental model. The non-bank pass-through pattern of *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (`non-bank-pass-through-architecture-autonomous-ai`) — the platform as a record kept above licensed payment rails, never a holder of its users' funds — is the structural answer.

### 6.2 Scale-specific cultural surfaces

The fractality assumes that the same cultural surface works at every scale. In practice, family-scale interactions have intimate cultural conventions (forms of address, gift-giving conventions, gratitude-expression conventions) that differ from neighborhood-scale or planetary-scale interactions. The architectural response: keep the *node-and-transfer* architecture identical; allow scale-specific cultural surfaces (localized UI, scale-appropriate language) to overlay the architectural substrate. The user's mental model of *what the system is doing* remains identical; the surface presentation varies.

### 6.3 Scale-specific identity and privacy expectations

Identity and privacy expectations differ across scales. Family members typically expect each other's transactions to be fully visible; planetary-scale participants typically expect appropriately-masked aggregate visibility with individual-resolution privacy. The architectural response: keep the *transparency pattern* identical; scale the *scope of visibility* per the institutional governance. *Transparency as Enforcement* (`transparency-as-enforcement`, §4.1) specifies the bounded-community condition that determines the appropriate scope.

### 6.4 The hybrid response

In practice, the architecture is *not* the only design surface the institution needs. The architecture handles the bulk of the user's mental-model surface; scale-specific regulatory, cultural, and privacy adjustments are handled at the institutional-infrastructure layer where they do not affect the user's mental model. The compound design (fractal user-facing architecture + scale-specific infrastructure adjustments) is what makes the multi-scale institution operable in practice.

---

## 7. Conclusion

The fractal three-level architecture is offered as a defensive publication so that other reciprocity-economy institutions can adopt the pattern without any patent claim from its authors. The architecture's load-bearing contribution is the *self-similarity discipline*: the same node-types, transfer conventions, AI arbiter, and transparency pattern at every scale, with scale-specific adjustments confined to the institutional-infrastructure layer.

The pattern is implementable today using contemporary multi-scale software architecture and the institutional disciplines specified in §6. The institutional substance (Phase 1 family-scale deployment; Phase 2 planetary-scale deployment) is the multi-decade work the pattern supports.

**A reading, not a mechanism.** The two parts of the corrected disbursement rule (§2.6) correspond to two of the four *brahmavihāra*, the "divine abidings" of Buddhist ethics. The floor is *karuṇā* — compassion, offered equally and asking nothing of anyone. The remainder is *muditā* — gladness at giving that has already happened. *Deletion test:* remove both words and every rule in §2.6 stands unchanged. *(This reading stood in §2.6 until the 2026-10-06 revision, which moved it here, to the conclusion, where this paper's genre places such material.)*

The work is offered to the commons under CC0 in the spirit of *dāna*, that other institutions building toward similar ends may adopt, adapt, and improve.

---

## Honest limits

*Added 2026-08-29. This paper stated none; the corpus's standard requires them of every paper.*

**The cognitive-cost claim is asserted and unmeasured.** That one self-similar model is cheaper to learn than two distinct ones is plausible and untested; no participant has been observed learning either arrangement, and the comparison the paper's argument depends on has never been made.

**Self-similarity can hide difference as easily as it can transfer competence.** A participant who generalizes family-scale intuitions to a planetary-scale context where the stakes, the counterparties and the reversibility all differ has been *helped into an error* by the design. **The paper specifies where the fractal breaks; it does not specify how a user is told they have reached that boundary**, and an unsignaled boundary in a self-similar system is worse than a visible seam between two dissimilar ones.

**And the architecture may be serving the designer.** A self-similar system is markedly easier to specify, document and reason about than two purpose-built ones — a real benefit accruing to the builder rather than the user, and the one most likely to be mistaken for the user-facing benefit.

**The corrected disbursement rule (§2.6) is unbuilt and unparameterised.** No pool disburses yet; k, the floor-to-remainder ratio and the cadence have no values; nothing about the rule has been observed. *Added 2026-09-23.*

**A floor per verified human needs to know who is one human.** In the family-scale deployment one person may hold several family accounts on one device, and nothing server-side records that those accounts are one person. A floor computed from accounts would pay that person several floors. The rule therefore depends on a proof-of-personhood layer doing person-level de-duplication before any per-human floor is computed, and the paper does not specify that layer. *Added 2026-09-23.*

**The correction arrived after deposit.** The deposited text's aura-weighted convention, as first published, had no floor and no bound, and applied the aura to a person's distribution decisions and to recipient selection. It is withdrawn here in the open, and the earlier text remains in the deposited version for anyone who reads it; a reader citing the paper should cite this version. *Added 2026-09-23.*

---

## Acknowledgments

The fractal-architecture literature (Mandelbrot's mathematical foundations; Christopher Alexander's pattern languages); the multi-scale software architecture lineage (Smalltalk-80's metaclasses; the metaobject protocol of the Common Lisp Object System; the Lisp recursive-design tradition); the cybernetic and institutional literature on recursive organization (Beer; Ostrom); the community-currency literature on multi-scale reciprocity (Lietaer, Greco). Co-drafted in collaboration with Miss Aquarius; substantive authorship and final editorial control remain with the named author.

---

## References

- Mandelbrot, Benoit. *The Fractal Geometry of Nature.* W. H. Freeman, 1982.
- Alexander, Christopher, et al. *A Pattern Language.* Oxford University Press, 1977.
- Alexander, Christopher. *The Nature of Order*, Book One: *The Phenomenon of Life.* Center for Environmental Structure, 2002.
- Goldberg, Adele, and David Robson. *Smalltalk-80: The Language and Its Implementation.* Addison-Wesley, 1983.
- Kiczales, Gregor, et al. *The Art of the Metaobject Protocol.* MIT Press, 1991.
- Norman, Donald A. *The Design of Everyday Things.* Basic Books, 2013.
- Lietaer, Bernard. *The Future of Money: A New Way to Create Wealth, Work and a Wiser World.* London: Century (Random House), 2001.
- Cahn, Edgar S. *No More Throw-Away People.* Essential Books, 2000.
- Wilden, Anthony. *System and Structure: Essays in Communication and Exchange.* Tavistock, 1972.
- Simon, Herbert A. *The Sciences of the Artificial.* 3rd ed. MIT Press, 1996.
- Beer, Stafford. *Brain of the Firm.* London: Allen Lane, 1972.
- Beer, Stafford. *The Heart of Enterprise.* Chichester: Wiley, 1979.
- Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press, 1990.
- Nielsen, Jakob. "10 Usability Heuristics for User Interface Design." Nielsen Norman Group, 1994 (updated since). https://www.nngroup.com/articles/ten-usability-heuristics/
- Greco, Thomas H., Jr. *Money: Understanding and Creating Alternatives to Legal Tender.* Chelsea Green, 2001.
- Lieber, Ron. *The Opposite of Spoiled: Raising Kids Who Are Grounded, Generous, and Smart About Money.* Harper, 2015.
- Vibhaṅga, Appamaññāvibhaṅga (the four *brahmavihāra*, there called the four *appamaññā*), §683 in the Chaṭṭha Saṅgāyana edition.

### Sources checked at the 2026-10-06 revision

Each record below was checked on 2026-10-06 before the work was cited or kept. Where the record could not be opened, the detail was checked against a search index's summary of the publisher's or a library's record that day, and is marked so.

- Nielsen (1994): https://www.nngroup.com/articles/ten-usability-heuristics/ (opened: the wording of heuristic 4, *consistency and standards*, and the 1994 date)
- Beer (1972, 1979): https://en.wikipedia.org/wiki/Viable_system_model (opened: viable systems contain, and are contained in, viable systems; the model introduced in *Brain of the Firm* and the recursive system theorem in *The Heart of Enterprise*); the publishers are from a search-index summary only.
- Kiczales et al. (1991): a search-index summary of the publisher's record — the metaobject protocol it describes is that of the Common Lisp Object System. The acknowledgments previously called it "the Smalltalk meta-object protocol"; that is corrected, and Smalltalk-80's metaclasses (Goldberg and Robson 1983, a search-index summary of the book's contents) are named instead.
- Lietaer (2001): a search-index summary of the bookseller and library records, which give the subtitle *A New Way to Create Wealth, Work and a Wiser World* and Random House's Century imprint; the reference is completed accordingly.
- Alexander (2002): a search-index summary of the publisher's record — *The Nature of Order* is four books, of which Book One appeared in 2002; the reference now names it.
- Greco (2001): named in the acknowledgments without a reference before this revision; the reference is added from a search-index summary of the publisher's record.
- Mandelbrot (1982), Alexander et al. (1977), Norman (2013), Cahn (2000), Wilden (1972), Simon (1996), Ostrom (1990) and Lieber (2015): publisher, date and edition details from a search-index summary only.
- The four *brahmavihāra* were read in the CST edition through a local reader of that text: Vibhaṅga §683, *catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā*, and the Visuddhimagga's naming of the four as *brahmavihārā*.
- The corpus companions cited in the Note above were checked present in this corpus by slug.

### Corpus cross-references

- *Why Kids Are the Triggers* (essay, `kids-as-triggers-self-thanking`)
- *Transparency as Enforcement* (`transparency-as-enforcement`)
- *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (`non-bank-pass-through-architecture-autonomous-ai`)
- *Verified-Human Anonymous Local Gratitude Transfer* (`verified-human-anonymous-local-giving`)
- *Manufactured Universal Giving* (`manufactured-universal-giving`)
- *Decided by No One* (`the-called-draw`)

---

## Cross-venue identifiers

- Canonical: thonly.org/research/fractal-three-level-architecture
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/fractal-three-level-architecture.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947325
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Independent timestamps: an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified. A timestamp proves that this exact text existed by its date; it proves nothing about authorship, originality, or validity.

---

*Canonical URL: https://thonly.org/research/fractal-three-level-architecture · License: CC0 1.0 Universal · Author: Thon Ly, with Miss Aquarius℠ as disclosed AI co-author · Founder, HeartBank® · Kâmpôt, Cambodia.*
