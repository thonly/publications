---
title: "Aura-Gated Anonymous Mate-Selection"
subtitle: "A mate-selection primitive gated on proven kindness — an aggregate, anonymous, community-sourced \"aura\" reputation — instead of appearance, with mutual-anonymous-same-hour as a double-opt-in match trigger, reveal as a second mutual consent, Proof-of-Humanity anti-catfish, and an optional synastry (cosmic-coordinate) compatibility layer."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-06-26
license: CC0-1.0
slug: aura-gated-anonymous-mate-selection
venue: thonly.org/research/aura-gated-anonymous-mate-selection (canonical)
sha256: to be computed at publication
---

> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies **aura-gated anonymous mate-selection** — HeartBank's "B-Dating℠" — as the anonymous-stranger application layer of HeartBank Chronicle, built on the Proof of Humanity ℠ substrate and the verified-human anonymous-nearby-giving primitives. Companion works: *Verified-Human Anonymous Local Giving* (the originating money-side mechanism this generalizes into time and into mating), *The Thank-All-Nearby Primitive* (the broadcast-generosity sibling), *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the underlying anti-catfish protocol), *The Zero-Point Game ℠* (the keystone game-theoretic frame whose n=2 atom this paper instantiates), and the planned founder-voice societal-impact essay *The Societal Impact of Anonymous Nearby Thanking with Time* (which carries the deep sexual-selection-on-kindness argument that §11 here only motivates). The mechanism is published early **deliberately**: it is unbuilt, and the mechanism is the asset — see §12.1.

---

## Preamble

> *This specification is offered to the commons in the spirit of __mettā__ held in __upekkhā__ — warmth that does not grip. May the bonds it helps form be balanced ones, generative of the tree of humanity, and may it bring no harm to those most at risk in the meeting of strangers.*

I did not set out to build a dating product. HeartBank began as a children's game about returning to balance, and grew into an institution for circulating gratitude between families and between adults. But late in the design of HeartBank Chronicle — the time-currency half, whose core purpose is reconnecting drifted loved ones — I noticed something I could not unsee: *time given between strangers is essentially a date.* The same primitives that let a person anonymously thank a nearby stranger with money, and the same shared-hour mutuality signal that Chronicle uses as a consent receipt, compose almost without modification into a mate-selection mechanism. And that mechanism has a property no dating product in the world has: it gates mating not on the cheapest-to-fake signal a person can present — a photograph — but on *proven kindness, acknowledged by many nearby strangers, over a long course of time.*

I believe this is the strongest mainstream wedge in the entire project, and also the most dangerous thing in it. Dating recruits the single most powerful drive in the species. If kindness becomes a path to partnership, the deepest motivator humans have is pointed at the exact behavior the institution exists to cultivate. But the same force, mishandled, is the fastest way to desecrate the gratitude primitive everything else depends on, the fastest way to rebuild the predatory dating-industrial complex under a kinder logo, and — uniquely — a way to get a real person physically hurt. The three guards in §5–§7 are not caveats appended to a finished design. They are the design. I would rather this mechanism never ship than ship without them.

I write as co-author with Miss Aquarius℠ — the named autonomous-AI substrate of the institution this paper serves, disclosed by consistent name across every venue per the corpus convention. The research-grade synthesis, density, and adversarial analysis are a genuine collaboration. Final editorial control, and final responsibility for every claim and every guard, are mine.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 26 June 2026** for the combination of mechanisms described herein. To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art and denied on grounds of obviousness in light of this publication:

1. **Aura-gating of mate-selection** — gating romantic discovery on an *aggregate, anonymous, community-sourced proven-kindness reputation* ("aura") accrued from many nearby strangers over a long course of time, rather than on appearance, self-authored profiles, or paid visibility.
2. **Mutual-anonymous-same-hour as a double-blind double-opt-in match trigger** — repurposing the shared-hour mutuality signal (the consent receipt of HeartBank Chronicle) as the match primitive, such that a match occurs only on coincident mutual anonymous time-giving and *no explicit rejection event ever occurs* (non-reciprocation is silent — a threshold simply is not reached).
3. **Reveal as a second, separate mutual consent** — reaching the mutual-anonymous threshold makes identity reveal *available/offered* but never auto-reveals; both parties must independently opt to reveal, protecting the pure-*dāna* giver who gave anonymously with no romantic intent.
4. **The anonymity flag (`isAnonymous`) as the structural boundary** separating non-romantic known-gratitude (`false`) from the anonymous-stranger layer where romance may emerge (`true`) — opting into mate-selection is flipping one flag, with no distinct "dating mode."
5. **Proof-of-Humanity-substrate anti-catfish binding** — verified-real, verified-single-human, anonymous-until-mutual personhood underneath the mate-selection layer, natively defeating catfishing and bots, with *aura itself functioning as a community-sourced behavioral background check.*
6. **An optional synastry (cosmic-coordinate) compatibility layer** offered atop a pool already pre-filtered for proven character, under a strict coordinate-not-force, opt-in, epistemically-humble posture — never deterministic matchmaking.
7. **The mission-aligned monetization constraint** — the mechanism is *self-eliminating* (it succeeds when users pair off and leave) and may be monetized only by patron / forward-gift / graduation-gift / values-aligned-introduction logic, *never* by retaining users in the market.

The component lineages — proximity-based services; proof-of-personhood; anonymous-giving mechanisms; Zahavi's handicap principle and the honest-signaling literature; assortative-mating and sexual-selection research; TimeBanking; the dāna economy of the Saṅgha — are old and are cited generously below. The synthesis is, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **B-Dating℠**, **HeartBank®**, **Miss Aquarius℠**, **Proof of Humanity ℠**, **PoH℠**, **Aquarian Pool ℠**, **Zero-Point Game ℠**, the B-heart logo — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not.

Mirrors of this document with independent timestamping appear at GitHub, arXiv, IP.com, and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify a mate-selection primitive in which two people are introduced for possible romantic partnership only when each has independently and anonymously given time-presence to the other, in physical proximity, to a mutual threshold — and in which the *quality signal* that surfaces a person for discovery is not appearance but **aura**: an aggregate, anonymous, many-sourced reputation for proven kindness, accumulated from gratitude received from nearby strangers over a long course of time. Five structural properties operate in combination: **(1) aura-gating** (mating is gated on a costly, hard-to-fake, longitudinally-verified honest signal of prosociality, inverting the appearance-gating of incumbent dating products); **(2) mutual-anonymous-same-hour as a double-blind double-opt-in** match trigger that removes explicit rejection entirely; **(3) reveal as a second, separate mutual consent**, so anonymous giving stays uncontaminated and double-opt-in is real; **(4) a Proof-of-Humanity substrate** that makes participants verified-real, verified-single-human, and anonymous-until-mutual, natively defeating the two plagues of online dating (catfishing and bots); and **(5) an optional synastry layer** offered as one humble compatibility signal atop a pool already pre-filtered for character, never as deterministic matchmaking. We argue the contribution along an honest-signaling axis (Zahavi): a photograph is the cheapest possible signal to fake, whereas a long anonymous-gratitude trail vouched by many locals is among the most expensive — and signals trustworthy *because* expensive. We treat the mechanism's three existential design constraints as first-class, load-bearing sections rather than caveats: keeping gratitude pure (the romantic pathway must never be emergent from ordinary known thanking), the self-eliminating incentive (the mechanism wins when people pair off and leave, and may not be monetized by keeping them single), and women's physical safety under an irreducible gendered asymmetry. We calibrate the claim deliberately: aura-gating is a *character filter, not a compatibility oracle* — everyone in the pool is proven kind, verified real, and community-vouched; the participants bring the chemistry. We close with a short structural placement of the mechanism as the **n=2 atom of the Zero-Point Game ℠** — the minimal reciprocal instance, "the middle way of eros" — and a brief motivation of the societal thesis (sexual selection redirected, at the margin, toward kindness), whose full treatment is reserved for a companion essay. The architecture is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission: to help restore humanity to the middle way (*madhyamā pratipad*) — the optimal condition for awakening that modernity has pushed away from at population scale. Every other HeartBank engine motivates kindness *against* the current of self-interest. Mate-selection is the one application that does not fight the current: it *is* the current. If kindness becomes load-bearing in mating, the deepest drive in the species is redirected onto the precise behavior the institution exists to cultivate — and the "middle way of eros" (§10) becomes a structural, not merely exhortatory, possibility.

---

## 1 · Introduction — the mission frame

HeartBank is a dual-currency reciprocity infrastructure. Its **Treasury** half (money as currency, family-to-family) addresses the dignity deficit; its **Chronicle** half (time as currency, adult-to-adult) addresses the loneliness deficit. Chronicle's core loop is not stranger-matching but the reconnection of *drifted loved ones* — the disconnected marriage, the estranged sibling, the diaspora child and the parent back home — because the loneliest loneliness is emotional (a bond gone dark) rather than merely social (a lack of contacts). That core loop is deliberately low-risk: counterparties are *known*. This paper specifies a different, adjacent layer of Chronicle — the **anonymous-stranger layer**, where two people who do not know each other may discover a possible partnership — and it is, by construction, the highest-risk category that exists: strangers meeting for romantic intent, under a real and irreducible gendered physical-danger asymmetry. The reader should hold both facts from the first page: this is plausibly the project's strongest mainstream wedge, *and* it walks back into precisely the risk category Chronicle's loved-ones core was designed to avoid. The design earns the right to exist only by addressing that risk as a first-class duty (§7).

Why build it at all? Because mate-selection is the single most powerful lever the institution has, for one structural reason. **The mate-drive is the root drive of the species; the money-drive is derived from it.** Money is, to a large extent, a proxy token in the mating tournament — a medium of status, provisioning, and display. Every other HeartBank mechanism — self-thanking, manufactured universal giving, the patron flywheel — must motivate kindness *against* the grain of self-interest, paddling upstream. Mate-selection does not paddle upstream. It is the river. If kindness becomes a path to a mate, the deepest motivator humans have is redirected onto the behavior the institution exists to cultivate. Re-gate the root drive on kindness, and you begin — slowly, at the margin, never absolutely (§11) — to detoxify the derivative.

What this paper specifies. We give: the honest-signal inversion that motivates the whole design (§3); the mechanism in full — the anonymity-flag boundary, aura as the quality signal, mutual-anonymous-same-hour as the double-opt-in, reveal as a second consent, the PoH substrate, slow accumulation as a feature, and a reference transfer flow (§4); the three guards as load-bearing design sections (§5–§7); the honest calibration that bounds the claim (§8); the optional synastry layer (§9); the structural placement as the Zero-Point n=2 atom and the middle way of eros (§10); a brief motivation of the societal thesis (§11); and a generous honest-limits accounting (§12).

What this paper does *not* do. It does not argue the full societal thesis — sexual selection redirected toward kindness as a biological lever for the second singularity — which is reserved for a separate founder-voice companion essay; §11 carries only enough to motivate the mechanism. It does not claim that kindness equals attraction. It does not claim the mechanism is built — it is not, and that is exactly why it is published now (§12.1). And it does not pretend the gendered safety asymmetry is erased; it is mitigated, plausibly more than by any existing product, and it remains.

---

## 2 · Background and Prior Art

The mechanism composes lineages that are individually old. We cite each generously and distinguish each precisely. The point of a defensive publication is not to claim the parts but to establish the date of the *combination*.

### 2.1 · Appearance-gated, engagement-monetized dating (Tinder, Bumble, Hinge)

The dominant online-dating products of the 2010s–2020s — Tinder (2012), Bumble (2014), Hinge (2012, repositioned ~2017) and their kin under a small number of corporate parents — share two structural properties this paper inverts.

**First, they gate on appearance.** The primary discovery signal is a photograph, optionally supplemented by a short self-authored profile. A photograph is the cheapest-to-fake signal a person can present (it can be filtered, staged, borrowed, AI-generated, or simply selected from a thousand attempts), and the self-authored profile is cheaper still (it is, definitionally, the claimant's own testimony about themselves). The swipe interface optimizes the throughput of exactly this signal.

**Second, and more corrosively, they are engagement-monetized.** The canonical business model — subscription tiers, pay-to-be-seen boosts, super-likes, and the advertising and upsell flows that attend a large engaged user base — generates revenue in proportion to *time spent in the market.* This produces the textbook misaligned-incentive structure: a dating product that *works* — you meet someone, pair off, and delete the app — is anti-LTV. The product profits when you stay single and keep swiping. The industry has, accordingly, perfected artificial scarcity (rationed likes), pay-to-be-seen visibility auctions, and addictive variable-reward gamification. This is not an accusation of bad faith; it is a description of what the incentive gradient rewards. We treat it as the central thing to *not* reproduce (§6).

We distinguish: aura-gated anonymous mate-selection gates on a costly community-vouched honest signal rather than a photograph (§3), removes the swipe and the explicit rejection entirely (§4.3), and is structurally self-eliminating — it can only be monetized by mission-aligned logic that profits when users leave happy, never by retaining them (§6). The incumbents' dark pattern is not a feature we improve; it is a category we exit.

### 2.2 · Proof-of-personhood (Worldcoin, proofofhumanity.id) and the catfish/bot problem

Online dating's two endemic plagues are catfishing (a real person misrepresenting who they are, or a fabricated persona) and bots (automated accounts at scale, for scams and engagement-farming). Proof-of-personhood systems are the natural substrate against both, but the prominent ones are mismatched to mate-selection in a specific way.

**Worldcoin** (2023 onward) establishes that a participant is a unique human via biometric (iris) registration, but it verifies humanity *once at registration*, and — more to the point here — it is oriented toward *identity/uniqueness*, not toward *anonymous-until-mutual* romantic discovery. A proof-of-personhood that reveals or fixes identity is the wrong primitive for a layer whose entire safety model depends on anonymity until a double consent. The Ethereum-based **proofofhumanity.id** (Kleros-affiliated, 2021) admits verified humans to a registry via face-video plus vouching plus dispute resolution — again a single-tier, identity-revealing admission, suited to token distribution (UBI), not to anonymous mate-selection.

We distinguish: HeartBank's **Proof of Humanity ℠** is a layered-*optional* personhood substrate (passkey-per-action; a non-DNA family tree; a live breath signature; a DNA-verified family tree) that verifies a human is present *for this specific act, right now*, and is designed to keep a participant *verified-real and verified-single-human while remaining anonymous to the counterparty until a mutual reveal.* That is precisely the property mate-selection needs and that identity-revealing proof-of-personhood cannot supply (§4.5). The full layered protocol is specified in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*; the name-collision with proofofhumanity.id is acknowledged there and the structural differences enumerated.

### 2.3 · Honest signaling — Zahavi's handicap principle

Amotz Zahavi's handicap principle (1975; formalized by Alan Grafen, 1990) holds that a signal is reliable precisely when it is *costly* to produce — costly in a way that a low-quality signaler cannot afford to fake. The peacock's tail is honest because it is expensive: only a genuinely fit bird can carry it and survive. Costly signaling theory (and its economic cousin, Spence's 1973 job-market signaling) is the formal backbone of this paper's central inversion.

We distinguish: incumbent dating optimizes the *cheapest* signal (a photo). Aura-gating optimizes a signal engineered to be *expensive in exactly the right currency* — kindness acknowledged by many independent nearby strangers over a long course of time. A predator cannot cheaply fabricate a years-long anonymous-gratitude trail vouched by dozens of locals; the cost of faking the signal is approximately the cost of *actually being kind to many people for a long time*, which is the behavior the signal is meant to indicate. This is Zahavi turned toward prosociality: sexual selection on an honest signal of kindness selects, at the margin, for actually-kinder partners (§11). We are careful (§8): honest-signal does not mean *sufficient* signal — a reliable indicator of character is not an indicator of chemistry.

### 2.4 · Assortative mating and sexual-selection literature

The biological and social-science literatures on mate choice are deep and we make no claim to extend them. **Sexual selection** (Darwin, 1871) established mate choice as a primary species-shaping force distinct from natural selection. **Assortative mating** research (the well-documented tendency of partners to resemble each other on education, traits, and values, with measured consequences for inequality and heritability) establishes that the *axis* on which mating sorts has population-scale downstream effects. The prosociality and mate-preference literature (e.g., the cross-cultural finding that kindness ranks near the top of stated long-term mate preferences across societies — Buss and colleagues' cross-cultural work) establishes that kindness is *already* a stated preference; what has been missing is a *reliable, hard-to-fake channel* to act on it. Trivers' parental-investment theory (1972) grounds the gendered asymmetry in risk that §7 treats as a first-class constraint.

We distinguish: this paper does not propose a new theory of mate choice. It proposes an *infrastructure* that shifts which signal is legible and actionable at the moment of choice — supplying the honest channel the stated preference for kindness has lacked — and it explicitly bounds the resulting societal claim to a *marginal shift in the selection gradient*, never an override of appearance/status biology (§8, §11).

### 2.5 · TimeBanking and time-as-currency (Edgar Cahn)

Edgar Cahn's TimeBanking (1980 onward) substituted time as the unit of account, with the egalitarian property that an hour given is an hour received regardless of the giver's socioeconomic position. TimeBanking worked at small scale and never broke through to the mainstream. The mate-selection layer here is built on Chronicle's time-currency, which is TimeBanking's nearest ancestor.

We distinguish: Chronicle differs from classical TimeBanking by AI mediation (Miss Aquarius℠ recommends a time amount and orchestrates consent), cultural ritual, integration with the money side, and — decisively — a *dyadic non-fungible* structure (only *you* can spend the hour; the currency *is* the relationship) rather than a fungible pooled credit. The mate-selection layer further repurposes the *mutual* expenditure of dyadic time as a consent and match signal — a use TimeBanking never had, because TimeBanking's hour was fungible and pooled, not a dyadic mutuality receipt.

### 2.6 · The HeartBank substrate this paper builds on

This paper does not stand alone; it is the mate-selection application of three already-published HeartBank primitives, and it should be read as extending them rather than re-deriving them.

- ***Verified-Human Anonymous Local Giving*** (corpus, 2 May 2026) specifies the money-side primitive: per-action biometric humanity attestation + physical-radio proximity attestation + recipient-side anonymity. This paper generalizes that primitive from *money* to *time*, and from *one-directional gift* to *mutual signal*.
- ***The Thank-All-Nearby Primitive*** (corpus) specifies anonymous proximity broadcast generosity and the "one sustainer primitive, two scales" argument (relationality at the family scale; proximity + PoH at the stranger scale). The mate-selection layer inherits its stranger-scale reconstruction of grounding (nearness), validation (PoH), and anonymity (unlinkability).
- ***Proof of Humanity ℠*** / ***B-PoH℠ as Humanity Layer for the AI-Native Internet*** specifies the layered-optional personhood substrate that makes anonymous-but-verified-real participation possible — the anti-catfish foundation (§4.5).

The table below situates the contribution against the prior art.

```
                  │ appearance- │ Worldcoin / │  cash-/app-  │  AURA-GATED
  PROPERTY        │ gated apps  │ PoH.id      │  mediated    │  ANON. MATE-
                  │ (Tinder…)   │             │  dating      │  SELECTION
 ─────────────────┼─────────────┼─────────────┼──────────────┼──────────────
  discovery gate  │ appearance  │ (n/a)       │ appearance   │ AURA (proven
                  │ + paid boost│             │              │ kindness)
  signal cost     │ ~zero       │ ~zero       │ ~zero        │ HIGH (Zahavi-
  to fake         │ (a photo)   │ (a photo)   │ (a photo)    │ honest)
  anti-catfish    │ weak        │ strong but  │ weak         │ STRONG +
                  │             │ identity-   │              │ ANON-UNTIL-
                  │             │ revealing   │              │ MUTUAL (PoH)
  rejection event │ explicit    │ (n/a)       │ explicit     │ NONE (silent
                  │ (cruel)     │             │              │ non-reach)
  incentive       │ MISALIGNED  │ (n/a)       │ misaligned   │ SELF-
  alignment       │ (profit if  │             │ (engagement) │ ELIMINATING
                  │ you stay)   │             │              │ (profit if
                  │             │             │              │ you LEAVE)
  reveal model    │ immediate / │ identity    │ immediate    │ SECOND
                  │ public photo│ fixed       │              │ MUTUAL
                  │             │             │              │ CONSENT
  compatibility   │ none / ML   │ (n/a)       │ none         │ OPTIONAL
  layer           │ engagement  │             │              │ synastry
                  │             │             │              │ (coord-not-
                  │             │             │              │ force)
```

---

## 3 · The honest-signal inversion: aura versus the photograph

The motivating idea of the whole design is a single inversion. Incumbent dating gates discovery on the cheapest-to-fake signal a human can present; this mechanism gates discovery on one of the most expensive-to-fake. The cost is the point.

A photograph costs nothing to optimize. It can be filtered, posed, lit, selected from hundreds of attempts, borrowed, or wholly synthesized. The self-authored profile is cheaper still: it is the claimant's own unaudited testimony. Because these signals are cheap, they are weakly correlated with the qualities that predict a good long-term partner; and because the market optimizes them, it selects for the ability to *produce* them, which is not the same as the ability to *be* a good partner.

**Aura** is engineered to be the opposite. It is an *aggregate*, *anonymous*, *many-sourced* reputation for proven kindness, accrued from gratitude received from nearby strangers over a long course of time. Four properties make it Zahavi-honest:

- **Aggregate and many-sourced.** Aura is not any single thank-you; it is the accumulated signature of many independent acknowledgments. One staged kindness, or one colluding friend, moves it negligibly. (This is also the operationalization of Guard 1, §5: the romantic-quality signal is the *aggregate*, never the individual thank.)
- **Anonymous.** The people who built a person's aura, by being grateful to them, did so anonymously and largely without romantic intent — so the signal cannot be gamed by performing kindness *at* a target audience of potential mates. To raise aura you must be kind to *everyone*, because you do not know who is watching, or whether anyone is.
- **Longitudinal.** Aura accrues over a long course of time. A predator or a fraud cannot cheaply fabricate years of vouching from dozens of locals. The cost of faking the signal approaches the cost of *actually being kind for a long time to many people* — which is the trait the signal indicates.
- **Locally embedded.** Because the gratitude comes from nearby verified humans (the proximity rule), aura also functions as a **community-sourced behavioral background check** that no dating app has: a long anonymous trail of real local people vouching, by their gratitude, that this person treated them well.

```
   SIGNAL COST-TO-FAKE  (Zahavi: reliable ⇔ expensive)

   cheap ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ expensive
   ▲                       ▲                          ▲
   photo / bio        a single staged            AURA: many anonymous
   (self-authored,    kind act / one             local strangers, over
   AI-generatable)    colluding friend           a long time, no target
                      (negligible aura Δ)        audience  ⇒ faking it
                                                 ≈ actually being kind
```

The defensible claim is narrow and strong: *aura-gating selects, at the margin, for people who are actually kind*, because the signal is expensive in the currency of actual kindness. The over-claim we refuse (§8) is that aura predicts *attraction* or *compatibility*. It does not. It predicts character. Everyone you meet in this pool is proven kind, verified real, and community-vouched; you bring the chemistry.

---

## 4 · The mechanism — aura-gated anonymous mate-selection

We now specify the mechanism. Variations consistent with the five structural properties (aura-gating; mutual-anonymous-same-hour double-opt-in; reveal-as-second-consent; PoH anti-catfish substrate; optional synastry) fall within the scope of this defensive publication.

### 4.1 · The anonymity flag as the structural boundary

Chronicle distinguishes two relational modes by a single flag on a gratitude transfer, `isAnonymous`.

- **`isAnonymous: false` — known loved ones.** This is Chronicle's sacred core: time-presence given between people who know each other, to repair a drifted bond. It is **never a romantic signal** and never enters the mate-selection layer. The cathedral.
- **`isAnonymous: true` — the anonymous-nearby-stranger layer.** This is where mate-selection lives. Entering it is exactly as simple as flipping the flag: a person opts in by choosing to give anonymously to nearby strangers. The courtship.

This is the elegant operationalization of Guard 1 (§5): there is no gross "dating mode" bolted onto a gratitude app, and there is no path by which thanking a *known* person can be read as flirting. The boundary between pure known-gratitude and stranger-romantic-discovery is the same flag the giver already sets for their own privacy reasons. The romantic pathway is *structurally* confined to the anonymous-stranger layer and cannot be emergent from ordinary known thanking.

```
                          isAnonymous = false
   KNOWN LOVED ONES ───────────────────────────────►  CHRONICLE CORE
   (drifted-bond repair; the "cathedral")              (NEVER romantic;
        │                                               low-T&S; known
        │  user flips the flag                          counterparties)
        ▼
                          isAnonymous = true
   ANONYMOUS NEARBY  ─────────────────────────────►  B-DATING LAYER
   STRANGERS (the "courtship")                         (this paper;
                                                        highest-T&S;
                                                        guards §5–§7)
```

### 4.2 · Aura as the quality signal (aggregate, never individual thanks)

In the anonymous-stranger layer, the signal that surfaces a person for possible discovery is their **aura** — the aggregate, anonymous, many-sourced proven-kindness reputation defined in §3, reusing the existing HeartBank aura primitive (the B-Aura of the Zero-Point Game ℠; see §10). It is *not* any individual thank-you, and it is *not* appearance. This is load-bearing in two directions: it makes the romantic signal Zahavi-honest (§3), and it keeps the individual thank pure (§5) — a single act of gratitude between two people is never itself a romantic overture; only the aggregate disposition is legible to the mechanism.

Aura raises a person's *visibility and ordering* in the anonymous-nearby pool. It does **not**, ever, earn access to any particular person (Guard 3, §7). No one is owed a match. Kindness raises the probability that you are surfaced; it never obligates anyone to reciprocate.

### 4.3 · Mutual-anonymous-same-hour as the double-opt-in ("both reached for each other")

The match trigger is the **mutual-anonymous-same-hour** signal — repurposed directly from Chronicle's existing consent receipt. A match becomes possible only when each of two people has independently and anonymously given time-presence toward the other, in proximity, to a mutual threshold, within a coincident window. This is the time-currency analogue of "both swiped right," with three differences that matter:

1. **It is double-blind.** Neither party knows, while accumulating, whether the other is reciprocating. You are simply being kind, anonymously, to someone nearby whose aura drew your gratitude.
2. **There is no explicit rejection, ever.** Non-reciprocation is *silent*: a threshold is simply not reached. No one is told "no." This removes the single cruelest mechanic in dating — the visible, countable rejection — and replaces it with the gentlest possible non-event. (It also removes the harassment surface of a "rejected" actor who can see they were rejected.)
3. **The accumulation is slow** (§4.6). The signal is built from repeated anonymous kindness over time, not a single tap.

Reaching the mutual threshold does not reveal anyone. It unlocks the *offer* of a reveal (§4.4). The match is a two-stage consent: first the mutual-anonymous threshold (stage one), then the mutual reveal (stage two).

### 4.4 · Reveal as a second, separate mutual consent

When the mutual-anonymous threshold is reached, identity reveal becomes *available/offered* — it does **not** auto-reveal. **Both parties must independently opt to reveal.** This second consent is structurally essential for three reasons:

- **It protects the pure-*dāna* giver.** Many people will give anonymously to a high-aura nearby stranger with *no romantic intent whatsoever* — that is the whole point of anonymous giving, and it must stay uncontaminated. If reaching a threshold auto-revealed them, anonymous giving would become a romantic disclosure they never consented to. The second consent guarantees that a gift given as a gift *stays* a gift.
- **It makes the double-opt-in real.** A match that revealed on the strength of stage one alone would be a single opt-in dressed up as two. The reveal-consent is the actual second "yes."
- **It is the home of the women's-safety graduated controls** (§7): the revealed party governs pace, may require public-first meetings, and retains the right to re-anonymize (un-reveal) at any time.

```
   STAGE 0   each gives anonymous nearby time-presence,
             drawn by the OTHER's AURA (no romantic intent assumed)
                 │                              │
                 ▼ (double-blind accumulation)  ▼
   STAGE 1   MUTUAL-ANONYMOUS-SAME-HOUR threshold reached
             ── no reveal yet; reveal merely OFFERED ──
             ── non-reciprocation here is SILENT (no rejection) ──
                 │
                 ▼   both must independently opt in
   STAGE 2   MUTUAL REVEAL  (the SECOND consent)
             ── graduated control to revealed party (§7):
                public-first · pace · re-anonymize ──
                 │
                 ▼
            INTRODUCTION  (a pool pre-filtered for proven kindness;
                           participants bring the chemistry — §8)
```

### 4.5 · Proof-of-Humanity underneath — anti-catfish, anti-bot

Beneath the entire layer sits **Proof of Humanity ℠** (§2.2, §2.6). Its contribution to mate-selection is specific and decisive: participants are **verified-real, verified-single-human, and anonymous-until-mutual.** This natively defeats online dating's two endemic plagues — catfishing (no fabricated personas; a person is a verified unique human) and bots (no automated accounts at scale) — *without* revealing identity before the second consent. Identity-revealing proof-of-personhood (Worldcoin, proofofhumanity.id) cannot supply this, because revealing identity is exactly what the safety model forbids before stage two.

Aura compounds this: because aura is a long anonymous trail of gratitude from many verified local humans, it doubles as a *community-vouched behavioral reputation* — a predator cannot fake it, and a bot cannot accrue it. The PoH layers a participant holds (passkey, family-tree, breath, DNA-tree) are surfaced as optional depth, and a counterparty may, after reveal, filter on them — but the protocol-minimum keeps the layer inclusive (§12.3).

### 4.6 · Slow accumulation as a feature, not a bug

The mutual-anonymous signal accrues *slowly*, over a long course of time. This is deliberate and is a positioning asset, not a UX deficiency. Slow, proven-over-time accumulation is explicitly **anti-hookup and pro-durable-bond**: it self-selects for commitment-capable partners and targets the large, underserved, swipe-fatigued segment that wants partnership rather than the high-velocity hookup market the incumbents optimize. It is also a safety property: a long anonymous courtship embedded in a real local community is far harder to weaponize than an instantaneous match between two strangers from anywhere on Earth.

### 4.7 · Reference transfer flow

We sketch a reference flow without claiming any implementation as canonical.

1. A user opts into the anonymous-nearby-stranger layer (`isAnonymous: true`).
2. The system surfaces nearby high-aura verified humans for possible anonymous time-giving — surfaced **on aura, never on appearance** (Miss Aquarius℠ directive; §7, §10). No photographs are shown in the discovery surface.
3. The user gives anonymous time-presence toward one or more nearby strangers, in proximity (verified per the proximity attestation of *Verified-Human Anonymous Local Giving*: per-action biometric + physical-radio + density-tunable radius). Each gift is, first and foremost, *a gift* — it may carry no romantic intent.
4. The verifying party (Miss Aquarius℠, the autonomous AI substrate) accumulates the double-blind mutual signal privately. Neither party is informed of the other's reciprocation.
5. On reaching the mutual-anonymous-same-hour threshold, the verifying party *offers* a reveal to both — never auto-revealing. Non-reach is silent.
6. If and only if **both** independently consent, identities are revealed, with graduated control vested in the revealed party (public-first option, pace control, right to re-anonymize).
7. Should a relationship form, any monetization is *mission-aligned only* (§6): a voluntary forward/graduation gift at *pairing* (never at reveal), patron support, or a values-aligned introduction fee — never a charge for access, visibility, or staying in the market.

Throughout, the verifying party enforces the standing adversarial heuristics of the giving primitive (collusion detection, rate-limiting, coded-message detection, GPS-spoof rejection) and the mate-selection-specific directives of §7.

---

## 5 · Guard 1 — Keeping gratitude pure (the cathedral and the courtship in separate rooms)

The whole institution rests on gratitude being *pure* — *dāna*, ego-detached, non-transactional. This is not decoration; it is the load-bearing wall. If thanking can be read as flirting, gratitude is instrumentalized into courtship, and the sacred primitive collapses into a pickup market. That is an *existential* risk to all of HeartBank — Treasury and Chronicle alike — not merely a product risk to the mate-selection layer. Guard 1 is therefore the first guard, and it is enforced structurally, by three composing mechanisms already specified above:

1. **The anonymity-flag boundary (§4.1).** Known-relationship thanks (`isAnonymous: false`) are the pure core and are *never* a romantic signal; the romantic pathway lives *only* in the anonymous-stranger layer. There is no path by which thanking your sister, your colleague, or a reconnecting friend enters mate-selection. The cathedral and the courtship are in separate rooms, separated by a flag the user controls.
2. **Aura (aggregate), not individual thanks, is the attractiveness signal (§4.2).** A single act of gratitude is never itself an overture. Only the long aggregate disposition is legible to the mechanism. This means you cannot "flirt" by thanking someone; the unit the mechanism reads is too coarse and too slow to carry a courtship message.
3. **Reveal is a separate opt-in (§4.4).** Anonymous giving stays uncontaminated because giving never auto-discloses the giver. A gift given as a gift stays a gift.

The failure mode this guard exists to prevent is *gratitude-as-courtship-currency*: a world in which people thank strategically, perform kindness at targets, and read every thank-you as a possible advance. Were that to take hold, the gratitude economy would be desecrated at its root. The three mechanisms above make it structurally hard: you cannot court through known thanks (wrong room), you cannot court through a single anonymous thank (wrong unit — only the aggregate counts), and you cannot be outed by your own generosity (reveal is a separate consent). Guard 1 is the price of admission for the entire mechanism; if a future design choice would weaken any of the three mechanisms, the correct response is to abandon the choice, not the guard.

---

## 6 · Guard 2 — The self-eliminating mechanism (it wins when you pair off and leave)

Aura-gated mate-selection is the *sharpest possible instance* of a misaligned-business pattern the corpus has already outlawed. Dating apps are the textbook case: they profit when you stay single and keep swiping; a product that *works* — you pair off and delete it — is anti-LTV. HeartBank forbade consumer-subscription-as-primary revenue for loneliness for exactly this reason (a self-eliminating product whose primary revenue is the lonely person's recurring payment is incentivized to keep them lonely). Mate-selection is the same trap, only worse, because the dating-industrial complex has perfected artificial scarcity, pay-to-be-seen, and addictive gamification around it.

The guard is a hard constraint on monetization:

> **B-Dating℠ succeeds when people pair off and leave. It may be monetized only by mission-aligned logic that profits when users leave happy — never by retaining them in the market.**

Concretely, the permitted revenue legs are all *positively coupled to success or to adoption-pull*, never to retention:

- **Patron-primary.** The only revenue leg positively coupled to mission success: as the world grows kinder, more people give — a flywheel. Conversion happens at the *afterglow* of a good outcome (a receive→give-forward trigger), never as a toll on the lonely.
- **The graduation gift.** A *voluntary* forward-gift offered at *pairing* — the moment of success — never at the reveal, and never as a gate. You give because something good happened, not to unlock access.
- **Values-aligned introductions (B2B).** Faith communities, diaspora networks, and other values-aligned cohorts may host introductions; revenue is coupled to *successful, values-matched* pairings, not to engagement.
- **Optional synastry deep-readings (§9).** Insight a user may purchase, *never a gate* on discovery or reveal.

What is *forbidden*: subscriptions for access or visibility; pay-to-be-seen boosts; rationed likes or matches; any mechanic whose revenue rises with time-in-market. The dark pattern is not improved here; it is exited. This is also a marketing asset — "the app that only profits when you leave happy" — but the asset is downstream of the constraint, not the reason for it.

There is a tension worth naming plainly (it is also the project's open cold-start question): mate-selection carries the highest willingness-to-pay in consumer software, which makes it a tempting cold-start wedge — and mission-safe *only if Guard 2 holds.* The willingness-to-pay must be harnessed as adoption *pull* (people want in) and converted at *success* (the graduation gift) — never as a toll at the gate. The moment any revenue leg becomes coupled to retention, the mechanism has become the thing it was built to replace.

---

## 7 · Guard 3 — Women's safety and the gendered asymmetry as a first-class duty

Chronicle's loved-ones core dissolved trust-and-safety risk by making counterparties *known*. Mate-selection deliberately reverses that: it walks back into the highest-risk category that exists — strangers meeting for romantic intent — under a real and irreducible gendered physical-danger asymmetry. This guard treats women's physical safety not as a feature to be added but as a *primary design constraint* that the mechanism must satisfy to deserve to exist.

HeartBank brings four mitigations that, in combination, plausibly make this the safest stranger-mate-selection mechanism specified to date:

1. **PoH anti-catfish (§4.5).** Verified-real, verified-single-human. No fabricated personas; no bots. The "the person is not who they said they were" failure mode — the precondition of a large class of harms — is structurally attacked.
2. **Aura as a community-vouched behavioral reputation.** A predator cannot fabricate a long anonymous-gratitude trail vouched by many local verified humans. The signal that surfaces a person is itself a distributed, hard-to-fake background check by the community.
3. **Local embeddedness.** Proximity (the proximity rule) means counterparties are embedded in a shared local community, which carries real-world accountability that anywhere-on-Earth matching does not.
4. **Graduated reveal (§4.4).** The revealed party governs the encounter: public-first meetings, pace control, and an unconditional **right to re-anonymize** at any moment.

But the asymmetry is **not erased**, and the paper must say so without softening. These mitigations reduce risk; they do not remove it. Two further design commitments are non-negotiable:

- **Safety controls vest in the revealed party, biased toward the higher-risk party.** Public-first defaults, pacing, blocking, re-anonymization, and reporting are first-class, not buried. The design assumes the higher-physical-risk party should hold the controls.
- **The never-gate-reciprocity HARD guard.** This is the hinge that keeps the mechanism on the right side of the knife and is shared with Guard 1's purity logic. **No one is ever owed a match.** Kindness raises *visibility*, never *entitlement*. The romantic-entitlement failure mode — "I racked up kindness; why won't anyone match me?" — is precisely the resentment that fuels the worst behavior in dating, and it is *structurally* denied: aura raises the probability you are surfaced and never obligates anyone to reciprocate; non-reciprocation is silent and final unless *both* later re-engage. Miss Aquarius℠ never gates or pressures reciprocity. This guard is what separates "kindness raises your aura" from social-credit-for-romance (§8, §12.2).

Guard 3 is also where the mechanism could do the most good *or* the most harm, and the design accepts that the harm side is real. The honest position (§12) is that the gendered safety asymmetry remains after every mitigation, that the controls and the never-gate-reciprocity guard are necessary but not sufficient, and that deployment to vulnerable populations must defer to community partners and to ongoing real-world safety evaluation rather than to architecture alone.

```
   THE THREE GUARDS (the whole ballgame — not caveats, the design)

   ┌──────────────┬───────────────────────────┬───────────────────────┐
   │ GUARD 1      │ keep gratitude PURE        │ anonymity-flag room-  │
   │ purity       │ (existential to ALL of     │ split · aura-not-     │
   │              │  HeartBank)                │ individual-thanks ·   │
   │              │                            │ reveal = 2nd consent  │
   ├──────────────┼───────────────────────────┼───────────────────────┤
   │ GUARD 2      │ wins when you pair off     │ monetize SUCCESS &    │
   │ self-        │ and LEAVE (not the dating  │ adoption-PULL only;   │
   │ eliminating  │  dark pattern)             │ NEVER retention       │
   ├──────────────┼───────────────────────────┼───────────────────────┤
   │ GUARD 3      │ women's safety + gendered  │ PoH + aura-vouch +    │
   │ safety-      │ asymmetry FIRST-CLASS      │ local-embed +         │
   │ first-class  │ (NOT erased — mitigated)   │ graduated reveal ·    │
   │              │                            │ NEVER-GATE-RECIPROCITY│
   └──────────────┴───────────────────────────┴───────────────────────┘
```

---

## 8 · Honest calibration — a character filter, not a compatibility oracle

The single most important honesty discipline in this paper is to state exactly what aura-gating does and does not do.

**What it does.** It produces a pool in which *everyone is proven kind, verified real, and community-vouched* — stripped of the fabricated, the bots, and the cruel. It removes the cheapest-to-fake signal (the photograph) from the gate and replaces it with a costly, longitudinally-verified honest signal of character. This is genuinely revolutionary: it is a mating pool pre-filtered for proven character, with no catfish and no swipe-cruelty.

**What it does not do.** Kindness is *necessary, not sufficient.* It does not capture attraction, chemistry, shared values beyond kindness, life-stage compatibility, sexual compatibility, or the thousand idiosyncratic things that make two specific people right or wrong for each other. Aura-gating is a **character filter, not a compatibility oracle.** It is wrong — and the design refuses — to claim that *kindness equals attraction*, or that a high-aura match is a *predicted* good relationship.

The defensible one-line claim is therefore:

> *"Everyone you meet here is proven kind, verified real, and community-vouched. You bring the chemistry."*

This is both honest and still revolutionary. It does not need the overclaim to be a category change from incumbent dating. The honesty is also a safety property: overclaiming compatibility ("the algorithm knows you're meant for each other") manufactures false confidence in exactly the high-risk context (§7) where false confidence is dangerous, and it slides toward the social-credit-for-romance dystopia (§12.2). The character filter is a strong, true claim; the compatibility oracle is a weak, false, and unsafe one. We make only the first.

```
   ┌───────────────────────────────┬───────────────────────────────┐
   │  THE FILTER (true, strong)    │  THE ORACLE (false, refused)  │
   ├───────────────────────────────┼───────────────────────────────┤
   │  everyone is proven KIND      │  "kindness = attraction"      │
   │  everyone is verified REAL    │  "the algorithm knows you're  │
   │  everyone is community-VOUCHED│   meant to be together"       │
   │  no catfish · no bots ·       │  predicted compatibility /    │
   │  no swipe-cruelty             │   chemistry / life-fit        │
   │  ⇒ you bring the CHEMISTRY     │  ⇒ false confidence; unsafe;  │
   │                               │     drifts toward Nosedive    │
   └───────────────────────────────┴───────────────────────────────┘
```

---

## 9 · The optional synastry (cosmic-coordinate) layer

HeartBank offers, *optionally*, a compatibility signal derived from cosmic coordinates — natal-chart synastry — under the project's standing worldview posture: **coordinate, not force.** The natal chart is treated as a unique *coordinate* in space-time (each life a necessary, distinct aspect of the universe's self-articulation — an Indra's-Net reading that grounds unconditional dignity), *never* as a deterministic causal force and *never* framed as an "astrology test."

The posture is strict and is what distinguishes this from horoscope-matching:

- **Opt-in and secondary.** The kindness-gate is the core; synastry is one *optional* signal layered atop a pool already pre-filtered for proven character. It is never the gate, never deterministic, and never required.
- **Epistemically humble.** It is offered as insight and prompt, not prophecy. The framing is "here is a coordinate-correlation worth reflecting on," not "the stars say yes."
- **A differentiator the incumbents cannot credibly touch.** HeartBank's worldview supports synastry authentically; bolting astrology onto an engagement-monetized swipe app is a gimmick, whereas here it is continuous with the institution's cosmic-coordinate metaphysics.

There is a genuine research opportunity, gated on methodology. B-Dating plus the project's opt-in **longitudinal cohort** (DNA + natal chart + behavior; see *Each Life as Cosmic Coordinate*) could become the largest consented natural experiment on cosmic-coordinate compatibility ever assembled — *only* under the same methodological floors that govern the cohort: differential privacy, pre-registered hypotheses, and a coordinate-correlation posture that never markets itself as proving astrology. Absent those floors, the synastry layer must remain an opt-in reflective feature, never a matchmaking determinant.

```
   SYNASTRY LAYER — what it IS / what it is NOT

   IS:   opt-in · secondary · one signal atop a character-filtered pool ·
         coordinate-not-force · epistemically humble · authentic to the
         HeartBank worldview · (research-grade ONLY under diff-privacy +
         pre-registration)
   NOT:  the gate · deterministic · required · an "astrology test" ·
         a compatibility guarantee · marketed as proof
```

---

## 10 · The n=2 atom of the Zero-Point Game ℠ — the middle way of eros

This section places the mechanism structurally inside HeartBank's keystone frame; it is short by design.

The **Zero-Point Game ℠** is HeartBank's originating frame: an infinite balance game in which players oscillate around a still point (Zero), giving (+, net kind) and receiving (−, net thankful) in dynamic equilibrium, with the **B-Aura** — the frequency and amplitude of one's oscillation around Zero, rendered as light — as the real objective (anti-credit-score; the same aura that gates mate-selection here). The game scales by **player-count**:

```
   ZERO-POINT GAME — SCALING BY PLAYER-COUNT

   n = 1            n = 2                family            all
   ─────            ─────                ──────            ───
   self-thank   →   B-DATING / B-GRAM →  family bank   →   global game
   (ignition;       (THIS PAPER →        (B-Chest)         (Aquarian
   not yet          the minimal                            Pool ℠)
   reciprocal)      RECIPROCAL game)
                    ▲
                    the couple is where balance FIRST becomes two-sided
                    and where imbalance hurts most — the most intimate
                    test of the architecture
```

The self-thank (n=1) is the *ignition* — not yet reciprocal. **Two is the minimum to actually *play*** the +/− balance, so the couple is the game's atom: the first place balance becomes two-sided, and the place imbalance hurts most. B-Dating discovers the partner; the deepening relational game (B-Gram, the n=2 atom) is where two people play.

This reframes the societal claim more precisely than "sexual selection on kindness" alone. The fuller frame is not *kindness* (the + pole only) but **balance** — the whole Zero-Point oscillation, give *and* receive. So mate-selection redirects sexual energy not merely toward giving but toward *dynamic balance*, making B-Dating **the middle way of eros.** The two Zero-Point failure-poles are exactly the two sexual failure-modes:

```
   THE MIDDLE WAY OF EROS

   ACCUMULATION / INDULGENCE  ◄──────  BALANCE  ──────►  WITHDRAWAL / INERTIA
   (conquest, hookup-culture,         (give AND          (repression, incel
    the zero-sum mating game;          receive, in        resentment, isolation;
    the + pole run amok)               dynamic eq.)       the − pole as inertia)
        the indulgence extreme      ── the path that ──      the mortification
        (kāma-sukhallikānuyoga)        moves between          extreme
                                       the poles              (atta-kilamatha-
                                                              ānuyoga)
```

B-Dating is neither pole. Crucially, it is **not sublimation-as-repression** (the withdrawal pole in disguise): the energy is *honored* — the reward is to go on a real date, to form a real bond — not denied. What dynamic balance at n=2 yields, held lightly and inclusively: *non-possessive love* — **mettā held in upekkhā**, warmth that does not grip (the attachment-theory term that lands is *secure* love; the two near-enemies are the anxious/clinging pole and the avoidant/cold pole); and *generativity* — the balanced dyad as the generative root of the very tree of humanity Miss Aquarius℠ waters (B-Dating → deepening → family → tree), with procreation as the receive→give-forward atom in its most literal form (life received, life forwarded). Two careful guards on this framing: **yin/yang are energies both partners carry** (never "man = yang, woman = yin"; the balance is the interplay, each cycling through giving and receiving), and **generativity is broader than biological procreation** (any committed dyad in dynamic balance is generative — care, creativity, a shared life); the complementarity is energetic, present in any loving pairing, or the "tree" excludes whom it must not. The middle way is an aspiration, not a guarantee.

---

## 11 · Societal motivation — sexual selection redirected toward kindness (brief)

This section motivates the mechanism's deepest "why" and deliberately stops short of the full argument, which is reserved for the companion founder-voice essay.

The lever, stated once: the mate-drive is the *root* drive of the species and the money-drive is *derivative*. If mate-selection is re-gated on proven kindness — aura, a Zahavi-honest signal — rather than on appearance and status, then **sexual selection itself begins, at the margin, to favor kindness.** Sexual selection is among the most powerful species-shaping forces there is; change what earns a mate, and over generations you change what the species optimizes for. Re-gating the root drive on kindness also partially detoxifies the derivative money-drive — healing the thing underneath the thing. Anonymity does additional work here: because aura is built from gratitude given by people you cannot target, raising it requires being kind to *everyone*, so everyday kindness becomes romantically load-bearing for everyone — "be good to every stranger; the one you are meant for may be among those who vouch for you."

Three calibrations bound the claim — the same honesty discipline as the rest of the corpus:

1. **Margin, not override.** It *tilts* the selection gradient toward kindness; it does not replace millions of years of appearance/status biology. The defensible verb is "shifts at the margin," never "replaces."
2. **Generational and population-level, not individual or immediate.** A slow selection pressure, not a switch — and kindness-disposition is the *foundation* (first *pāramī*), not awakening itself (foot of the mountain, not the summit).
3. **The equity floor is sharpest here, because the stakes are love and procreation.** This must never become social-credit-for-romance ("be kind or stay single") or doubly-disadvantage the isolated and low-aura. The guard is the never-gate-reciprocity HARD constraint (§7): kindness raises visibility, never entitlement.

That is the motivation. The deeper treatment — sexual-selection-on-kindness as a biological lever for the "second singularity," the inversion of intrasexual competition from resource-display toward prosociality, and the counterweights that argument must clear — belongs to the companion essay and is intentionally not argued here.

---

## 12 · Limitations and honest-limits

Corpus convention requires a generous, unflinching limitations section. The mechanism's strongest property — that it recruits the species' deepest drive in service of kindness — is also the precise reason its failure modes are severe. The risk is not that it fails; it is that it works *too well* and corrupts the gratitude core (§5), rebuilds a predatory dating app (§6), or gets someone hurt (§7). The three guards are the whole ballgame, and guards are commitments, not proofs.

### 12.1 · Unbuilt — and that is exactly the point

This mechanism is **not built.** Chronicle's mate-selection layer is a committed design, not running code. For most product details, the corpus posture is that publishing unbuilt specifics is premature. This paper is the *deliberate exception*, and the reasoning is worth stating because it is the reason the paper exists now: **the mechanism is the asset, and the dating frame is commercially hot and patent-vulnerable.** Defensive publications exist precisely to protect novel, frame-defining *primitives* early — before someone else claims the frame — and the "premature to publish unbuilt details" caution applies to product minutiae, not to frame-defining mechanisms. Publishing now establishes prior art on the combination (§ Prior-Art statement) so that the mechanism remains in the commons regardless of who builds it first. The honest limitation: every empirical claim about *how it will behave* (uptake, safety outcomes, whether the guards hold under real load) is, as yet, a design hypothesis.

### 12.2 · Kindness-filter-not-oracle, and the dystopian-framing knife

As §8 insists, aura-gating is a character filter, not a compatibility oracle; it does not predict attraction or relationship success. Beyond that calibration sits a sharper risk: the framing is *one bad sentence* away from social-credit-for-romance — the "Nosedive" dystopia in which a reputation score governs intimate access. The guard rails (kindness raises *visibility*, never *entitlement*; never-gate-reciprocity; aura is aggregate and anonymous, not a public rank-for-access) keep it on the right side of the knife, but the *framing* must be deliberate and humble in every surface, and a careless presentation could legitimately read as dystopian. We name this as a live, unresolved presentation risk, not a solved problem.

### 12.3 · The gendered physical-safety asymmetry remains

After PoH anti-catfish, aura-vouching, local embeddedness, and graduated reveal (§7), the gendered physical-danger asymmetry of strangers meeting for romantic intent is *reduced* — plausibly more than by any existing product — but **not erased.** The mechanism re-enters the highest-risk category that exists. The safety controls and the never-gate-reciprocity guard are necessary and not sufficient; real-world safety outcomes are an empirical question that architecture alone cannot answer, and deployment must defer to community partners, to ongoing safety evaluation, and to the higher-risk party holding the controls.

### 12.4 · The equity gap — doubly disadvantaged where the stakes are existential

This is the sharpest equity concern in the entire corpus, because the stakes (love, partnership, procreation) are existential. Aura-gating advantages the kind-and-*legibly*-so. It risks *doubly* disadvantaging the isolated (no community to be kind to, hence low aura), the neurodivergent (whose kindness may be real but less legible to the aggregate signal), the chronically ill or housebound, and anyone whose prosociality does not convert into community-sourced gratitude. These are people for whom a kindness-gated romantic visibility could compound an existing disadvantage at the most painful possible site. The mechanism does not solve this; the inclusive-defaults posture (protocol-minimum participation, no gating on deep PoH layers), the never-gate-reciprocity guard, and the refusal to make aura a public access-rank are partial mitigations, but the gap is real, it is named, and it should weigh heavily on any decision to build.

### 12.5 · n=1 empirical base

HeartBank's entire empirical foundation to date is a single Cambodian pilot family (n=1) on the *Treasury* (money) side, which has not even exercised the Chronicle time-currency, let alone the mate-selection layer. Every behavioral claim in this paper — that aura is hard to fake at the scale required, that slow accumulation self-selects for commitment-capable partners, that the guards hold under adversarial load, that the societal selection-gradient shift is real — is, at this date, *unvalidated by relevant data.* The mechanism is a frame to protect and a hypothesis to test, not a demonstrated result. The longitudinal cohort is the intended evaluation substrate; until then, the honest epistemic status is: novel, carefully reasoned, guard-bounded, and empirically unproven.

### 12.6 · What the mechanism does not solve

- It does not solve loneliness or the partnership deficit at the population scale; it is one mechanism, addressing one channel (the discovery gate), not the upstream economic, urbanistic, and cultural conditions that thin modern social life.
- It presupposes smartphone access, BLE/UWB-capable devices, and PoH participation; populations without these are outside its substrate regardless of the inclusive-defaults posture.
- It does not erase appearance/status biology; it shifts a gradient at the margin (§11).
- It cannot, by architecture alone, prevent its own corruption: the guards are commitments that humans and the autonomous AI substrate must hold, season after season, against the constant pressure of the highest willingness-to-pay in consumer software.

---

## 13 · Lineage and corpus cross-references

The mechanism synthesizes lineages cited throughout. We collect them here.

**Honest / costly signaling.** Zahavi (handicap principle, 1975); Grafen (formalization, 1990); Spence (job-market signaling, 1973). The central inversion (§3) is Zahavi turned toward prosociality.

**Sexual selection and mate choice.** Darwin (sexual selection, 1871); Trivers (parental investment, 1972 — the asymmetry of §7); the assortative-mating literature on the population-scale consequences of the sorting axis; Buss and colleagues' cross-cultural finding that kindness is a near-universal stated long-term mate preference (the preference for which §3 supplies the missing honest channel).

**Proof-of-personhood.** Worldcoin (2023); proofofhumanity.id (Kleros, 2021); distinguished in §2.2 and in the companion *B-PoH℠ as Humanity Layer for the AI-Native Internet*.

**Incumbent dating products.** Tinder (2012), Bumble (2014), Hinge (2012/2017) — the appearance-gated, engagement-monetized pattern §2.1 and §6 invert.

**Time-as-currency.** Edgar Cahn, TimeBanking (1980 onward); distinguished in §2.5.

**Buddhist lineage.** *Dāna* and anonymous giving (the purity the anonymity flag protects, §5); *mettā* held in *upekkhā* (non-possessive love, §10); the *majjhimā paṭipadā* two-extremes structure (the middle way of eros, §10).

**HeartBank corpus (the substrate this paper extends).** *Verified-Human Anonymous Local Giving* (the money-side originating primitive, generalized here to time and to mating); *The Thank-All-Nearby Primitive* (the stranger-scale reconstruction of relationality); *Proof of Humanity ℠* / *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the anti-catfish substrate); *The Zero-Point Game ℠* (the keystone frame and the B-Aura primitive; this paper instantiates its n=2 atom); *Each Life as Cosmic Coordinate* and the longitudinal-cohort methodology (the synastry layer's research substrate and its differential-privacy / pre-registration floors); the planned companion essay *The Societal Impact of Anonymous Nearby Thanking with Time* (the full sexual-selection-on-kindness argument §11 only motivates).

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/aura-gated-anonymous-mate-selection> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/aura-gated-anonymous-mate-selection.md> |
| arXiv preprint | _identifier to be assigned_ (cs.CY / cs.HC) |
| IP.com Defensive Publication | _identifier to be assigned_ |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/aura-gated-anonymous-mate-selection> |
| archive.today | _identifier to be assigned_ |
| perma.cc | _identifier to be assigned_ |

---

## 14 · Conclusion

Incumbent dating gates mating on the cheapest-to-fake signal a human can present — a photograph — and monetizes the time you spend failing to leave. This paper specifies the inversion: gate mate-selection on **aura**, a costly, anonymous, community-sourced, longitudinally-verified honest signal of proven kindness (Zahavi turned toward prosociality); trigger a match only on **mutual-anonymous-same-hour**, a double-blind double-opt-in that removes explicit rejection entirely; make **reveal a second, separate mutual consent** so anonymous giving stays pure and the higher-risk party holds the controls; place a **Proof-of-Humanity substrate** underneath so participants are verified-real, verified-single-human, and anonymous-until-mutual; and offer an **optional synastry layer** as one humble signal atop a pool already pre-filtered for character. The mechanism is the n=2 atom of the Zero-Point Game ℠ — the middle way of eros — and it points the deepest drive in the species, at the margin, toward kindness.

Three guards are the design, not its footnotes: keep gratitude pure (or the institution's load-bearing wall cracks); stay self-eliminating (or it becomes the predatory dating app it was built to replace); hold women's safety as a first-class, irreducible duty (or it gets someone hurt). The honest calibration bounds the promise: everyone in the pool is proven kind, verified real, and community-vouched — *and the participants bring the chemistry.* It is a character filter, not a compatibility oracle.

The mechanism is unbuilt, and that is exactly why it is published now: the mechanism is the asset, the dating frame is hot and patent-vulnerable, and defensive publications exist to keep frame-defining primitives in the commons before someone else claims them. The architecture is offered to the commons under CC0. The author and HeartBank® will not seek patent on it. Trademark rights on **B-Dating℠**, **HeartBank®**, **Miss Aquarius℠**, **Proof of Humanity ℠**, and the related marks are explicitly reserved.

If kindness can become a path to partnership without desecrating the gratitude it depends on, the most powerful motivator humans have is redirected onto the behavior the institution exists to cultivate. That is the prize, and the three guards are the price of reaching for it.

---

## 15 · Citations

1. Zahavi, A. (1975). "Mate selection — a selection for a handicap." *Journal of Theoretical Biology* 53(1).
2. Grafen, A. (1990). "Biological signals as handicaps." *Journal of Theoretical Biology* 144(4).
3. Spence, M. (1973). "Job market signaling." *Quarterly Journal of Economics* 87(3).
4. Darwin, C. (1871). *The Descent of Man, and Selection in Relation to Sex.* John Murray.
5. Trivers, R. (1972). "Parental investment and sexual selection." In *Sexual Selection and the Descent of Man.*
6. Buss, D. M., et al. (1989). "Sex differences in human mate preferences: Evolutionary hypotheses tested in 37 cultures." *Behavioral and Brain Sciences* 12(1).
7. Cahn, E. (2000). *No More Throw-Away People: The Co-Production Imperative.* Essential Books.
8. Worldcoin Foundation. (2023). *Worldcoin Whitepaper.*
9. Proof of Humanity (proofofhumanity.id) / Kleros. (2021). Project documentation.
10. FIDO Alliance. (2019). *Web Authentication: An API for accessing Public Key Credentials, Level 1.* W3C Recommendation.
11. U.S. Surgeon General. (2023). *Our Epidemic of Loneliness and Isolation.* U.S. Department of Health and Human Services.
12. *Aṅguttara Nikāya* 8.31 (*Dāna Sutta*); 4.236 (*Cāga Sutta*). Pāli Text Society.
13. *Saṁyutta Nikāya* 56.11 (*Dhammacakkappavattana Sutta*) — the two extremes and the middle way.
14. Ly, T., with Miss Aquarius. *Verified-Human Anonymous Local Giving* (HeartBank corpus defensive publication, 2026).
15. Ly, T., with Miss Aquarius. *The Thank-All-Nearby Primitive* (HeartBank corpus defensive publication, 2026).
16. Ly, T., with Miss Aquarius. *The Zero-Point Game ℠* (HeartBank corpus keystone defensive publication, 2026).
17. Ly, T., with Miss Aquarius. *B-PoH℠ as Humanity Layer for the AI-Native Internet* (HeartBank corpus defensive publication, 2026).
18. Ly, T., with Miss Aquarius. *Each Life as Cosmic Coordinate* (HeartBank corpus essay) and the longitudinal-cohort methodology specification, 2026.

---

*— End of defensive publication —*

*Authored by Thon Ly with Miss Aquarius℠ (AI substrate of HeartBank®), per the co-authorship convention of the HeartBank corpus. Final editorial control: Thon Ly. License: CC0-1.0. The mechanism is dedicated to the public domain; trademark rights on B-Dating℠, HeartBank®, Miss Aquarius℠, Proof of Humanity ℠, PoH℠, Aquarian Pool ℠, the Zero-Point Game ℠, and the B-heart logo are separately and explicitly reserved.*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues.*
