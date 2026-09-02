---
title: "The Studio and the B-Short Bridge: A Private-to-Public Toggle as the Phase-1-to-Phase-2 Crossing"
subtitle: "A Per-Artifact Private-to-Public Toggle as the Phase-1-to-Phase-2 Crossing of a Gratitude Economy — One Primitive That Carries a Family-Scale Ledger Onto a Global Settlement Layer"
authors: "Thon Ly"
category: mechanism
priority: tier-b
status: draft
date: 2026-06-12
license: CC0-1.0
slug: studio-b-short-phase-bridge
venue: thonly.org/publications/defensive-publications/studio-b-short-phase-bridge (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/studio-b-short-phase-bridge.md
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, B-Short℠, Re-Tip Jar℠, Miss Aquarius℠) reserved separately by the author and HeartBank®.
---

> **Working draft.** This paper specifies a mechanism currently being built (the Studio surface and the public-toggle bridge); it is a design specification offered as prior art, not a report of a deployed-and-measured system. The Phase-2 settlement layer it bridges onto is specified elsewhere in the corpus and is not yet live.

---

## Preamble

> *A family economy and a planetary one are usually built as two products with a migration between them. This paper specifies a gratitude economy in which they are one product with a switch — and the switch is a single artifact's privacy setting.*

A gratitude economy that begins at family scale (a household thanking its own members in local currency) and aspires to planetary scale (strangers thanking strangers on a global settlement layer) faces an architectural seam: **how does a participant cross from the small economy to the large one?** The default answer is a *migration* — a separate onboarding, a second account, a port of identity and balances from Phase 1 to Phase 2. Migrations are where users are lost and where architectures fracture. This paper specifies a design with no migration: the crossing is a **per-artifact privacy toggle**, and flipping one B-Short from private to public *is* the act of entering the global economy.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author asserts no patent and dedicates the patterns to the public domain under CC0 1.0. The contribution is a composition of known parts — short-form video creation tools, privacy-scoped sharing (the private/unlisted/public visibility ladder common to video platforms), and on-chain settlement — assembled into a specific bridge primitive. Prior art is cited in §7 and novelty is claimed only for the composition of §8. Trademarks are reserved separately; the patterns may be implemented under any name.

## 1. The bridging problem

HeartBank is built in two phases. **Phase 1** is a family-scale ledger of gratitude on conventional rails: a household thanks its own members, in local fiat, witnessed by people who know each other. **Phase 2** is a global peer-to-peer layer on a blockchain settlement substrate (Base L2): strangers thank strangers, anonymously and verifiably, anywhere. The two phases are appropriate to their scales — the family layer is light, legible, and trust-conferred; the global layer is heavy, cryptographic, and trust-minimized. But a participant who has only ever thanked their own family needs some way to begin thanking, and being thanked by, the world. The seam between the two phases is the riskiest joint in the architecture.

## 2. The Studio: a creator surface for real kindness

The Studio is the Phase-1 surface where the bridge artifact is made. It is a lightweight creator tool — capture short clips, keep them, stitch them together at one's own pace — specialized for one content type: **records of real acts of kindness**. A participant films a kindness (and, characteristically, the same situation before and after, so that what is shown is not the gesture alone but the change it made), and assembles the clips into a short video. The defining feature is not the editing; it is *what is being recorded and for what economy*. The Studio's output is the unit the rest of the system circulates.

To prevent the Studio from becoming a stage for fabricated good, the kindness records that earn rewards are constrained (per the surrounding mechanism corpus) to be **recorded live, visible to family or public, and pinned to a real location** — so the cheapest way to produce a rewardable record is to actually perform a real, witnessed kindness in a real place. The Studio is a creator tool whose lowest-cost content is genuine good.

## 3. The B-Short: the unit that crosses

The artifact the Studio produces is a **B-Short℠** — a short-form video record of a kindness. A B-Short begins **private**: it exists at family scale, witnessed and thanked only within the participant's own household, in Phase-1 currency. It is, at this stage, an entry in a family ledger that happens to have a moving picture attached.

The B-Short is the right unit to carry across the seam because it is *self-contained and self-evidencing*: it bundles the kindness, its witnesses, its location, and its provenance into one shareable object. Unlike a balance (which is account-bound and must be ported) or an identity (which is heavy and must be migrated), a B-Short is a leaf — it can change its own visibility without dragging an account behind it.

## 4. The toggle is the bridge

The crossing from Phase 1 to Phase 2 is a single act: **setting a B-Short to public.** That one toggle does two things at once, which is the whole mechanism:

1. **It changes the audience** from the family to the world: a public B-Short is visible beyond the household, to any participant anywhere.
2. **It switches the settlement rail** from Phase-1 family fiat to the Phase-2 global on-chain layer: a public B-Short can now be re-thanked by strangers, with value settling on Base L2.

There is no separate migration, no second onboarding, no port. The participant does not *move* from the small economy to the large one; they *publish one artifact into* the large one, and may do so for one B-Short while keeping the rest private. The bridge is therefore **incremental, reversible in scope, and per-artifact** — a participant lives in both economies at once, with each B-Short individually scoped.

This is one instance of a **general bridge primitive** that recurs across the architecture: *to enter the global layer, set something public.* The same shape governs B-links (a privately shared provenance object set public becomes a public one) and multi-family membership (a local family membership composes upward into the global pool). HeartBank's Phase-1-to-Phase-2 crossings are not three different migrations; they are three instances of one toggle — *private → public = local → global.*

## 5. What the public toggle switches on

Made public, a B-Short enters the Phase-2 re-thank economy and inherits its properties:

- **The re-thank multiplier at global scale.** A public B-Short can be re-thanked by an audience of size *N* approaching the whole network, so the throughput available to it is the Phase-2 realization of the re-thank multiplier (the companion paper): origination stays one act, re-thanking scales with the network.
- **The funded floor.** The autonomous steward funds a base reward for any verified kindness regardless of public reach, so going public is *upside* (the thanks of strangers) layered on a floor that does not require virality. Publishing is not a lottery ticket; it is an amplifier on a guaranteed base.
- **Value-bearing, human-gated re-thanks.** Strangers' re-thanks are value-bearing (re-tipped from their own balance) and human-given, which makes the public layer's volume the same layer as its anti-farm defense (per the re-thank-multiplier paper): public exposure does not open a farming hole, because the re-thanks that reward it are budget-bounded and not solo-farmable.

## 6. Keeping public kindness from corrupting

A public surface that pays for visible kindness invites the failure that sinks such designs: kindness *performed for the audience and the money* rather than done for its recipient. The bridge does not pretend this risk away; it is managed by three constraints carried over the bridge with the artifact.

First, **what is rewarded is real, verified good, not its performance** — the live/visible/located constraints of §2 mean the cheapest rewardable act is a genuine one, so even a participant who crosses the bridge for mercenary reasons is delivered into doing real good. Second, **the prestige signal is giving, not earnings** — a participant's standing is carried by a giving-driven aura (raised by re-giving onward), displayed ambiently, while raw re-thank counts function as viewer-facing information about which kindnesses the community values, kept subordinate to the aura; the status game therefore rewards circulating, not accumulating. Third, **the steward surfaces diverse, genuinely helpful exemplars** rather than the most viral, so that what a public audience learns to imitate is kindness in its variety rather than whatever currently scores. None of the three eliminates the performative edge case (a real act staged for the camera survives them, caught only by whether real people thank it as genuine); they make the genuine path the cheap one and the performed path the expensive, catchable one.

## 7. Prior art

The components are individually familiar. **Short-form video creation and stitching** is ordinary creator-tool functionality. The **private / unlisted / public visibility ladder** is standard on every video platform; what is novel here is not the ladder but its *use as an economic-phase boundary*. **On-chain settlement** on an L2 is standard Web3 infrastructure. The **creator-economy** pattern (creators earning from an audience) is well established, as is its characteristic power-law distribution. Novelty is claimed for none of these individually.

## 8. What is claimed as novel, and honest limits

**Claimed as novel** is the composition: (a) using a **per-artifact privacy toggle as the migration-free crossing** between a family-scale gratitude economy and a global one, such that a single artifact's visibility setting simultaneously changes its audience and its settlement rail; (b) the identification of this as **one instance of a general *private → public = local → global* bridge primitive** shared with other HeartBank surfaces; and (c) the **Studio** as a creator surface specialized for verifiable real-kindness records (live/visible/located), whose published output inherits the funded-floor and value-bearing-re-thank properties that keep public exposure from opening a farming or performativity hole.

**Honest limits.** The mechanism is specified, not yet built or measured; the Phase-2 settlement layer it bridges onto is not yet live. The creator-economy power law means going public benefits a visible few far more than the many (the funded floor mitigates subsistence but not the distribution of fame). The performativity defenses of §6 are partial — they defeat fabrication, not staging. And the bridge presumes the surrounding properties (the funded floor, the giving-prestige signal, the diverse-exemplar surfacing) actually hold; this paper specifies the crossing and inherits, rather than re-establishes, those guarantees.

---

## Acknowledgments

Drafted with Miss Aquarius℠ (the AI substrate of HeartBank®) per the corpus convention; the framing and final editorial control are the author's.

## Corpus cross-references

- *The Re-Thank Multiplier* — what the public toggle switches on: the O(N²) throughput and the value-bearing, not-solo-farmable re-thank that makes public exposure safe.
- *A Living Made of Kindness* — the human stakes of the bridge: a B-Short set public is how a livelihood made of kindness reaches the world.
- *B-Links: Proof-of-Humanity-Signed Provenance* — the sibling instance of the private → public primitive.
- *Multi-Family Membership* — the third instance: local membership composing onto the global pool.
- *Miss Aquarius and the Aquarian Pool Architecture* — the Phase-2 settlement layer and the surfacing steward of §6.

## Cross-venue identifiers

- Canonical: thonly.org/research/studio-b-short-phase-bridge
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/studio-b-short-phase-bridge.md
- Internet Archive · archive.today · perma.cc snapshots: per the monthly snapshot cadence.
