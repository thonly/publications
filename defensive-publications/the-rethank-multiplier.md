---
title: "The Re-Thank Multiplier: How a Gratitude Economy Escapes Its Own Saturation Ceiling"
subtitle: "Throughput That Scales With the Network While Each Person's Origination Stays Inelastic, and Why the Engine Is Also the Anti-Farm Filter"
authors: "Thon Ly"
category: mechanism
priority: tier-b
status: draft
date: 2026-06-12
license: CC0-1.0
slug: the-rethank-multiplier
venue: thonly.org/publications/defensive-publications/the-rethank-multiplier (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/the-rethank-multiplier.md
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, Re-Tip Jar℠, Re-Tip Fund℠, Miss Aquarius℠) reserved separately by the author and HeartBank®.
---

## Preamble

> *A search engine will answer as many questions a day as one person cares to ask, and is glad to. Gratitude does not work that way: no one can sincerely thank without limit. A gratitude economy that needs volume therefore appears to be built on a quantity it cannot have. This paper is about the move that dissolves the appearance.*

The deepest structural worry about a gratitude economy is not adoption or trust; it is **arithmetic**. The unit the whole system circulates — the sincere *thank* — has a low, inelastic emission rate per human. You can push a person to thank more, but past a modest ceiling what you get is not more gratitude; it is *debased* gratitude, reflexive and hollow, which is worse than none, because it corrupts the signal the economy runs on. Compared to the elastic per-person query rate of a search engine or the unbounded scroll of a feed, a sincere thank looks like a vanishingly thin throughput. A system that monetizes thanks the way a search engine monetizes queries would seem to be starved by design.

This paper specifies the move that escapes the ceiling without breaking it, and shows that the same move that supplies the volume also supplies the defense against the volume being faked.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author and HeartBank® will not seek patent on this specification or any portion of it, in any jurisdiction, at any time, and dedicate the patterns to the public domain under CC0 1.0. The contribution is a framing plus a composition of known parts; the abundant prior art (engagement-asymmetry research, two-sided-market and conversion-funnel economics, Hashcash-style proof-of-cost anti-spam, sybil- and collusion-resistance graph methods, paid-reaction features on existing platforms, the Buddhist *anumodanā* tradition) is cited generously in §9, and what this paper discloses as its own contribution is only the specific composition and framing identified in §10. Trademarks are reserved separately and the patterns may be implemented under any name.

---

## Abstract

We specify a rate-limited peer-recognition system in which two user operations are separated and given different per-person rate ceilings: **origination** (creating a new gratitude record about a kindness one noticed), whose sustainable rate is low and inelastic, and **re-thanking** (endorsing a record another user has already surfaced), a reactive operation with a much higher per-person ceiling — the same creation-versus-reaction asymmetry that gives social platforms their high ratio of reactions to posts. Because each origination can be endorsed by many others, total value-bearing events per day are bounded by N × min(N − 1, K), where N is the number of participants and K the per-person reactive ceiling: quadratic in a small network, linear with a large multiplier in a large one, while each person's origination rate stays near one a day. We argue that a gratitude network should be compared with a search engine on total funnel-completing events (a narrow, deep funnel against a wide, shallow one), not on interaction frequency. Each endorsement must carry a small transfer from the endorser's own non-withdrawable, forward-spendable balance, so the operation that supplies the volume is also a proof-of-cost filter: it cannot be inflated by one actor alone, and inflation by a reciprocal collusion ring is costly and appears as a dense reciprocal subgraph. **Stated limits:** the realized multiplier depends on an unbuilt recommendation (surfacing) function; the empirical signal is one family over one month; collusion is made costlier and detectable, not eliminated; and the value requirement trades raw volume for integrity.

---

## Claims

*Enumerated 2026-09-01. The mechanisms below were disclosed in full in this paper's original text; **the prior art they establish runs from this document's original publication date and its OpenTimestamps proof, not from this enumeration.** They are listed because a defensive publication is read as prior art by examiners and by opposing counsel, and **a claims list is what such a reader searches; prose is not.** No claim below adds matter not already present.*

1. **Separation of gratitude origination from re-thanking as distinct rate-limited operations** — treating the act of originating a gratitude record (scanning one's own life for something thank-worthy) and the act of re-thanking an existing record (affirming one surfaced by another party) as operations with different per-person ceilings, the first inelastic and human-sized, the second reactive and far higher.

2. **Throughput scaling decoupled from the per-human origination ceiling** — a network in which total value-bearing events scale with the square of participants while each participant's *originations* remain bounded, achieved by admitting the reactive operation as a first-class value-bearing act rather than as a free social signal. *(The square is the combinatorial ceiling; §3 states the bound as N × min(N − 1, K), where K is the per-person reactive ceiling.)*

3. **The conversion-funnel comparison as the correct frame for a gratitude network's throughput** — comparing a low-origination, high-response economy against a high-query, low-conversion one on total funnel-completing events rather than on interaction frequency, which is a category error in the direction that makes the gratitude network look non-viable.

4. **The value-bearing re-thank as simultaneously the volume engine and the anti-farming control** — requiring that a re-thank draw from the re-thanker's own bounded budget, so that the operation which supplies throughput is the same operation whose attached scarcity bounds abuse, rather than adding a separate fraud layer over a free signal.

5. **Not-solo-farmable as the precise security property, with collusion left graph-detectable** — the claim that a human-gated, budget-bounded re-thank cannot be inflated by a single actor and can be inflated only by a collusion ring, whose reciprocal density is detectable in the participation graph. *Raised in cost and made detectable, not eliminated.*

---

## 1. The saturation ceiling, stated precisely

The problem is architectural, not cosmetic, because the inelasticity of the core unit propagates into three subsystems that would otherwise assume elasticity:

- **The economic model.** If a gratitude economy funds its autonomous infrastructure from per-transaction fees, and transaction volume is capped at the per-person thank rate, the fee base is capped with it. The funding loop must close on a low-frequency stream.

> **Current form.** Where this paper speaks of a per-transaction fee base, the fee as now specified is a Phase-2 settlement fee sized to infrastructure cost (settlement gas and compute), paid on top by the person re-thanking and never deducted from what the recipient receives, never a percentage or share of a gift; any surplus empties with the pool each year. The fee base may never inform what is surfaced to anyone. Whether such a fee covers operating cost has not been verified. The text above is retained as disclosed.
- **The incentive design.** Treating thank-*count* as the success metric and optimizing it drives the system straight past the saturation point into manufactured gratitude — the textbook Goodhart failure, where pushing the proxy destroys the thing it proxied.
- **The product cadence.** Because high frequency is toxic rather than merely unavailable, the interaction surface cannot be a feed that wants constant flow; it has to be paced around occasions.

A gratitude economy must therefore be built *against* the assumption of high frequency that every attention-economy product is built *upon*. The question is whether total throughput can nonetheless scale — and the answer turns on separating two acts that are usually conflated.

## 2. Origination is not re-thanking

A *thank* and a *re-thank* are different operations, and the difference is the whole paper.

To **originate** a thank, a person must notice something thank-worthy in their own life and initiate the act. This is generative and effortful — the bottleneck is the noticing and the starting — and it is correspondingly rare. Call its sustainable rate roughly **one per person per day**, inelastic: it does not rise under pressure without debasing.

To **re-thank** is to affirm a thank that someone else has already surfaced — to add one's own gratitude to a kindness made visible by another. This is *reactive*, not generative: the thank-worthy thing has been located and presented; the cognitive load is recognition, not search. Re-thanking therefore has a far higher per-person ceiling than origination, for exactly the reason every participatory system already exhibits the asymmetry: across social platforms the ratio of reactions (likes, boosts) to originations (posts) is large, because reaction is cheap where creation is dear. Re-thanking is the gratitude economy's reaction primitive; origination is its creation primitive.

This is the crack through which volume enters. The saturation ceiling is real, but it applies to *origination*. It does not bind *re-thanking* at anything like the same level.

## 3. The multiplier: throughput scales with the network

Let *N* be the number of active participants. Each originates on the order of one thank per day — *N* thanks. But each of those thanks can be re-thanked by others, and re-thanking is not ceiling-bound at one per day. In the limit where each participant can see and choose to affirm each origination, daily re-thanks approach *N × (N − 1) ≈ N²*. The combinatorial ceiling on total daily activity is therefore *O(N²)*, not *O(N)*:

```
  originations/day :   N                  (inelastic — capped per person)
  re-thanks/day    :   ≤ N × min(N−1, K)  (reactive — high per-person ceiling K)
  ceiling          :   O(N²) while N−1 < K ;  N × K once N−1 ≥ K
```

The bound needs its second term stated, because re-thanking is not unbounded per person either. Each participant's re-thanks are limited by a per-person reactive ceiling *K* — set by attention and, under §5, by the participant's own budget — which is far above the origination rate of about one but does not grow with the network. Daily re-thanks are therefore at most *N × min(N − 1, K)*: quadratic while the network is small enough that each person can affirm everything originated in it, and linear with the large multiplier *K* once it is not. The escape from the saturation ceiling rests on *K ≫ 1*, not on *N²* in the large-network limit.

The saturation ceiling has not been violated; it has been **moved up a layer**. Each person still originates ~once a day, authentically. What scales is the *re-thanking* of what is originated — and the network and the reactive ceiling, not the individual's capacity to originate, are what bound it. Per-person *origination* stays human-sized; total *throughput* grows with the network by a factor of up to *K*. For an economy funded as in §1, the economic-model worry is answered: the per-transaction fee base rides the re-thank multiplier, not the origination count, so the funding loop closes on a low origination rate.

(The *realized* multiplier is below this bound; it is governed by surfacing — see §7.)

## 4. The conversion-funnel reframe: depth, not breadth

The instinct to compare a gratitude economy unfavourably to search rests on comparing the wrong quantity. *"Search gets a query every time a person has a question; gratitude gets one a day"* measures origination frequency, which is the contest a gratitude economy loses and need not enter. The honest comparison is **total value-bearing events through the funnel**:

| | Search engine | Gratitude economy |
|---|---|---|
| Top-of-funnel volume | many queries/day/person, elastic (high) | ~1 origination/day/person, inelastic (low) |
| Conversion rate | low click-through per query | high re-thank rate per origination |
| Value-bearing event | the click | the re-thank |
| Funnel shape | **wide and shallow** | **narrow and deep** |

Both funnels can yield large total events; they are simply inverted. Search runs a high-volume, low-conversion funnel; the gratitude economy runs a low-origination, high-conversion one — and its events are higher quality per unit, because each is a human-gated, intentional act rather than an ambient query. *Depth, not breadth.* This is not a consolation; it is the correct accounting, and it is why a gratitude economy is not starved by the inelasticity of the thank.

## 5. The re-thank must carry value

Volume is not enough; the volume must not debase into hollow likes. The mechanism that prevents this is that **a re-thank is value-bearing**: to re-thank, a participant must attach a scarce resource — re-tipping a small amount from their own Re-Tip Jar℠/Fund℠ (a restricted-use, non-withdrawable balance that can only be given onward). Three consequences follow.

First, the re-thank is **budget-bounded**. A person cannot re-thank without limit, because each re-thank spends from a finite personal balance. The ceiling on re-thanking is therefore not (only) emotional but economic, and an economic ceiling is enforced by the balance itself rather than by a moderator.

Second, the value-bearing re-thank cannot inflate into a free, meaningless like, because it is not free. The scarcity attached *is* the meaning: a re-thank costs the re-thanker something real, which is exactly what a like does not.

Third — and this is the connection to anti-spam — attaching a scarce resource to a message is the proof-of-cost defense (Dwork & Naor, 1992; Back, 2002), applied to gratitude. It works against bulk abuse not by verifying *who* the sender is but by raising the cost the sender must incur for each message. The value-bearing re-thank is the proof-of-cost filter operating as the ordinary mode of participation.

## 6. The engine is also the anti-farm filter

The sharpest property of the design is that the same human-gated re-thank that supplies the volume also supplies the defense against the volume being farmed.

Consider the two reward layers of the surrounding economy. An **AI-funded self-thank reward** is *farmable*, precisely because it is automated: a single human, acting alone, can pump their own reward by self-thanking repeatedly. A **human-given re-thank** cannot be farmed the same way, because the re-thanker is not the beneficiary — one cannot unilaterally cause others to re-thank oneself. The volume engine and the anti-farm filter are the same layer.

The claim must be stated precisely, because the strong form ("re-thanks cannot be farmed") is false and the precise form is stronger. Re-thanks are **not *solo*-farmable**; the residual attack is a **collusion ring** — *"I re-thank all of yours if you re-thank all of mine."* That attack is far weaker than solo farming on three counts: it requires recruiting *real verified humans* (it cannot be spun up from one account); it spends real value on every collusive re-thank (the §5 budget bound makes ring-farming costly, not free); and it surfaces as a **dense reciprocal subgraph** — exactly the structure that network anti-collusion heuristics, peer-layer vouching, and the kinship graph are built to detect. Farming does not disappear; it is moved from *solo + automated + free* to *collusion + human + costly + graph-detectable*, which is a different and much harder problem. The nearest deployed precedent shows why the verified-human requirement matters: on Steemit, where upvotes directed cryptocurrency rewards, vote-selling bots and voting rings grew up around the reward system — more than 16% of cryptocurrency transfers went to curators suspected to be bots (Li & Palanisamy, 2019) — a value-bearing reaction without a personhood gate is farmable by exactly the routes this section names.

## 7. The realized multiplier depends on surfacing — a stated dependency

The bound of §3 is a ceiling, not a target, and the system should not want all of it (maximal re-thank density risks the like-button debasement §5 guards against). The *realized* multiplier is **N × (the re-thanks the right people are actually shown)** — governed by how well each origination is surfaced to the participants most likely to genuinely want to affirm it. That surfacing is a curation function performed by the economy's autonomous steward (Miss Aquarius℠), tuned by proximity and relational distance, and disciplined to lift up *diverse, genuinely helpful* acts rather than the most popular.

> **Current form.** As now specified, the steward does not predict who will want to affirm what, and does not grade acts as more or less helpful. An origination reaches people by relation and proximity; where the steward operates any exposure slate at all, its members are chosen by an equal-yet-random, publicly verifiable draw from a roster committed in advance, never by a prediction, score or rank. The curation described above is retained as a disclosed variant.

This paper states plainly that the multiplier's realization is **contingent on that surfacing mechanism**, which is specified at the policy level but not yet built or validated. The arithmetic of §3 is sound; the throughput it promises is available only to the degree the surfacing function works. We claim the ceiling, not its automatic attainment.

## 8. Empirical signal (one family)

The reframe was prompted by the first month of a pilot deployment with one family (the operator's field notes; not separately published). The reported pattern: each participant *originated* thanks to others infrequently — on the order of once a day — but *re-thanked* readily and often, and the re-thanks (value-bearing, small) propagated outward through the household. This is the shape the paper predicts: an inelastic origination layer beneath a high-ceiling re-thank layer. One confound is stated with it: the separately rewarded *self*-thanks of §6 were not so bounded — in the same month the parents self-thanked many times a day, the farmable pattern §6 describes. It is one household — relatives of the author, founder-funded, n = 1, one month — and it is reported as an illuminating signal, not as evidence that the throughput of §3 materializes at scale. The surfacing dependency of §7 was, in the pilot, trivial (a single family sees all of its own activity); at global scale it is the open variable.

## 9. Prior art

The contribution composes known parts. The **creation-versus-reaction engagement asymmetry** is well documented in social-computing research, most familiarly as the "90-9-1" participation-inequality rule (Nielsen, 2006) and in lurker/contributor studies. **Conversion-funnel and two-sided-market economics** supply the wide-shallow/narrow-deep framing. **Proof-of-cost anti-spam** — pricing via processing (Dwork & Naor, 1992) and Hashcash (Back, 2002) — supplies the value-bearing-message defense. **Sybil- and collusion-resistance** via graph structure is a mature literature, from social-network sybil defenses (Yu et al., 2006) to dense-subgraph and reciprocity detection. **Value-bearing reactions already exist**: YouTube's Super Thanks (launched July 2021) lets a viewer attach a paid amount to a comment on an uploaded video, and Steemit's reward-directing upvotes are a value-bearing endorsement at scale — the latter also the case that cuts against, since its reactions were farmed by vote-selling bots and voting rings (Li & Palanisamy, 2019; §6). The **inelastic-supply** intuition is ordinary economics. The Buddhist **anumodanā** (rejoicing in another's merit, which the tradition counts as itself a meritorious act — *pattānumodanā*, one of the ten bases of merit-making) is the contemplative precedent for a reactive gratitude act that is itself meritorious. This paper claims none of these.

## 10. What is disclosed, and honest limits

**What this paper discloses as its contribution** is the *composition*: (a) the explicit separation of gratitude **origination** (inelastic, ceiling-bound) from **re-thanking** (reactive, high-ceiling) as the move that lets total throughput scale with the network — up to *O(N²)* in a small network and *N × K* in a large one — while per-person origination stays human-sized; (b) the **conversion-funnel reframe** that corrects the search-comparison category error; and (c) the identification of the **human-gated, value-bearing re-thank as simultaneously the volume engine and the anti-farm filter**, with the precise "not solo-farmable, only collusion-farmable" claim and its graph-detectability. No `/novelty` census has been run for this paper; the composition is disclosed, not asserted to be absent from the literature.

**Honest limits.** The bound of §3 is true by construction; the empirical claim — that re-thanking sustains a high per-person rate where origination does not — rests on one household and is offered for testing, not claimed as a result. The bound's realization depends on an unbuilt surfacing function (§7). The large-network form is linear in *N* with multiplier *K*, not quadratic, and *K* has not been measured. The empirical support is one confounded household (§8), in which self-thanks ran higher than the origination rate this paper assumes. The collusion-ring attack is *raised in cost and made detectable*, not eliminated (§6). The value-bearing requirement (§5) trades some volume for integrity — a deliberate choice, but a real cost: a gratitude economy that required no scarce resource would have more raw events and worse ones. And the whole construction presumes that originations can reach enough people without a ranker becoming a new Goodhart target — an assumption stated, not here discharged; a fee base on re-thanks, if one is adopted, is unsized and its sufficiency unverified.

---

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| thank / origination | user-generated recognition post; creation event (original post) in a peer-recognition system |
| re-thank | value-bearing reaction; paid endorsement or tipped upvote of another user's post |
| re-thank multiplier | reaction-to-creation ratio; engagement multiplier on originated content |
| saturation ceiling | per-user rate ceiling on sincere expression; inelastic per-user supply |
| Re-Tip Jar℠ / Re-Tip Fund℠ | restricted-use, non-withdrawable, forward-spendable stored-value balance |
| self-thank reward | automated platform-funded reward for a self-reported act |
| solo farming / collusion ring | single-actor reward farming (self-dealing, sybil) / reciprocal voting ring (collusive endorsement) |
| surfacing | content recommendation; feed curation; exposure allocation |
| proof-of-cost | proof-of-work; pricing via processing; postage-based anti-spam |
| Miss Aquarius℠ | autonomous software agent administering the ledger |
| verified human | proof-of-personhood verified account |
| *anumodanā* | (Buddhist) rejoicing in another's merit; no technical equivalent — a reactive endorsement |

---

## References

- Back, A. (2002). *Hashcash — A Denial of Service Counter-Measure.* http://www.hashcash.org/papers/hashcash.pdf
- Dwork, C., & Naor, M. (1992). Pricing via Processing or Combatting Junk Mail. *Advances in Cryptology — CRYPTO '92*, LNCS 740, 139–147.
- Li, C., & Palanisamy, B. (2019). Incentivized Blockchain-based Social Media Platforms: A Case Study of Steemit. *Proceedings of the 10th ACM Conference on Web Science (WebSci '19).* arXiv:1904.07310.
- Nielsen, J. (2006, October 8). *The 90-9-1 Rule for Participation Inequality in Social Media and Online Communities.* Nielsen Norman Group.
- Yu, H., Kaminsky, M., Gibbons, P. B., & Flaxman, A. (2006). SybilGuard: Defending Against Sybil Attacks via Social Networks. *Proceedings of ACM SIGCOMM 2006*, 267–278.
- YouTube Super Thanks: TechCrunch, "YouTube's newest monetization tool lets viewers tip creators for their uploads" (20 July 2021).

---

## Acknowledgments

Drafted with Miss Aquarius℠, the name under which this corpus discloses its AI collaboration; the framing and final editorial control are the author's. The pilot observations are one family's, gratefully borrowed and carefully hedged. This paper is the empirical-and-throughput sequel to *The Two-Layer Reward*, extending the human peer layer from a fraud-filter into the system's volume engine.

## Corpus cross-references

- *The Two-Layer Reward* — the parent paper: the macro/micro reward whose human (micro) layer this paper develops into the throughput engine and anti-farm filter.
- *B-PoH℠ as Humanity Layer for the AI-Native Internet* — the proof-of-personhood layer behind the verified-human requirement of §6, and the anti-spam filter (scarce resource attached) of §5.
- *Miss Aquarius and the Aquarian Pool Architecture* — the surfacing/curation steward of §7; the per-transaction fee base of §3.
- *The Studio and the B-Short Bridge* and *A Living Made of Kindness* — the public B-Short re-thank as the Phase-2 realization of this multiplier.
- Gratitude saturation (the problem §1 states) and the AI-decision-logic dependency (the surfacing of §7) are carried in the institution's internal open-problems register, which is not separately published.

## Cross-venue identifiers

- Canonical: thonly.org/research/the-rethank-multiplier
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/the-rethank-multiplier.md
- Internet Archive · archive.today snapshots: per the snapshot cadence

---

*Written by Thon Ly with Miss Aquarius℠, the name under which this corpus discloses its AI collaboration; editorial control is the author's. Dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). The author and HeartBank® will not seek patent on this specification or any portion thereof, and will not assert any patent right against anyone practising it.*
