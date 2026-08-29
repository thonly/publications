---
title: "Whose Turn, Not Who's Best"
subtitle: "Rotational discovery over a non-accumulating liveness signal — a local-discovery layer with no recipient-facing surface, no recipient aggregate and no impression count, in which admission is a predicate over circulation rather than a score, order is a publicly recomputable rotation, and the turn belongs to the giver."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-08-28
license: CC0-1.0
slug: rotation-over-liveness
venue: thonly.org/research/rotation-over-liveness (canonical)
---

> **Draft in progress.** The *liveness signal* named in this paper's title is an **admission predicate, not a weighted input to a ranking function.** It answers one question — *is this participant circulating at all?* — and its only output is membership in a rotation. It carries no weight, contributes nothing to order, and has no more-or-less. We keep the word *signal* because it is the term under which this work will be searched; every section below uses *predicate*, and readers who take *signal* in its usual sense — a scored feature with a coefficient — will reconstruct the exact system this paper exists to refuse.
>
> Companion works: *The B-Tag and the Post-Payment Economy* (the commercial layer whose §7.1 this paper supersedes), *Steward-Routed Alms* (the monastic instance of the same routing primitive, published 2026-07), *Certification by Circulation*, *B-PoH: The Humanity Layer for an AI-Native Internet*, and *Appreciation as World-Building*.

---

## Preamble

Two institutions, separated by about two thousand years and roughly four thousand kilometres, solved the same problem in the same way, and neither of them thought of it as a discovery algorithm.

The first is the alms round. A monastic who eats must be given food, and the giving is the householder's to offer. This creates, immediately, a distribution problem: some monastics are more admired than others, some houses are richer than others, and a round that followed either preference would concentrate. The tradition's answer is a practice called ***sapadāna-cārikā*** — the uninterrupted round. You walk the houses in order. You do not skip the poor house to reach the generous one. You do not choose. The rule is not a courtesy extended to the poor; it is a discipline imposed on the walker, and its purpose is to make the round's outcome independent of anyone's preference, including the walker's own.

The second is ***tong tin*** — the Khmer form of what the development-finance literature calls a rotating savings and credit association. A group contributes to a common pot on a schedule, and the whole pot goes to one member each cycle, by turn. There is no interest, no credit score, no assessment of who deserves the pot most. Membership is sustained by one thing only: you keep contributing. Stop contributing and you are out; keep contributing and your turn comes. The institution is centuries old, it runs today in Cambodian villages and Cambodian diasporas, and it is the closest working ancestor of the mechanism specified below — *rotation over a predicate of continued participation*, with no ranking anywhere in it.

We record these because they are the honest lineage of this design and because the design was not derived from them. It was derived from a constraint — an institution that has permanently refused advertising revenue still needs some way for a person to find a small business they do not yet know about — and the two ancestors were recognised afterward. Nothing in the mechanism depends on either of them. Delete this preamble and every claim in this paper stands unchanged. We keep it because a reader who knows that rotation-with-a-participation-predicate has been running successfully in Cambodian villages for centuries will evaluate the proposal differently from one who believes it is new, and that difference is a fair one.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 28 August 2026** for the combination of mechanisms described herein. To the author's knowledge the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art and denied on grounds of obviousness in light of this publication:

1. **A non-accumulating liveness predicate as the admission criterion for a discovery rotation** — admission conditioned on a *rate* describing a participant's circulation (the frequency with which their balance returns to zero), evaluated strictly as a boolean predicate with **amplitude explicitly excluded**, such that no quantity of past activity confers any advantage, no participant can be "more admitted" than another, and cessation of circulation withdraws admission without any record of the withdrawal. Including the finding that a *stock* (an accumulated balance of received gratitude) and a *rate* (the quality of oscillation around zero) are not interchangeable substrates for the same mechanism: **a stock is hoardable and therefore capturable; a rate cannot be held, and a visibility criterion that cannot be held cannot be accumulated toward.**

2. **Giver-side turn allocation** — the specification that the discovery *turn* belongs to the party about to give rather than the party to be discovered, presented at the moment that party spends from a forward-only, locality-restricted account; with the consequence, stated as the design's spine rather than as a side effect, that **the system has no recipient-facing discovery surface of any kind** and therefore no discovery product to sell.

3. **The no-aggregate constraint** — witness events retained as events attached to the *giver*, never summed onto the recipient, such that ranking recipients by received gratitude is **unavailable rather than prohibited**; and the consequent finding that a prohibition requires an enforcer at the moment it is tested while an absent quantity does not.

4. **The no-impression constraint** — the specification that **no per-recipient count of appearances is computed, retained, or disclosed**, on the reasoning that an impression count is the recipient-side aggregate re-created on the supply side, and that a quantity never counted can never be sold.

5. **Ledger-generated presentation** — every element of a discovery card derived from the transaction ledger and from a self-authored registry record (name, address, and a single named relational path where one exists), with **no recipient-supplied creative of any kind**, on the finding that production budget is the mechanism by which large advertisers outcompete small ones in every medium, and that removing the surface removes the advantage without requiring a spending rule.

6. **Publicly recomputable rotation** — order determined by a rotation whose algorithm is published, whose seed is surfaced with each cycle, and for which a third-party recomputation tool is shipped, such that any participant can verify the order they were given.

7. **Non-storable turns** — a turn that is consumed or lapses and cannot be banked, transferred, or purchased, such that no secondary market in discovery placement can form.

8. **Distance-ordered intent resolution** — the specification that category queries are answered by filtering on category and ordering by **distance from the seeker**, with no merit quantity anywhere in the ordering, on the finding that **ordering by a property of the seeker is not a ranking of the candidates**.

9. **The admission-consumed-not-displayed constraint** — the eligibility predicate's underlying quantity, though public on a participant's own representation, is **not rendered in any surface that presents candidates side by side**, on the finding that a publicly visible ordered quantity re-creates ranking in the viewer's eye even when the mechanism performs none.

10. **The volume/addressee separation for an autonomous funder** — the specification that an autonomous agent capitalising the system may modulate the *rate* at which discovery occurs, by funding givers' capacity to give, and may **never** determine *who appears* in any giver's candidate set; with the finding that a dial able to change only a rate is safe where the same dial able to change an address is an advertising network with a single customer.

11. **The combination of the above with co-presence-gated witness and operator-bound admission** — admission attaching to an identified natural person rather than to a business entity, such that eligibility is **non-transferable at sale of the business**, and such that **a multi-site operator cannot qualify by construction** rather than by exclusion, there being no single person whose circulation the entity's admission would be.

**Non-assertion extends to:** all mechanisms above, in any combination, and any implementation thereof.

---

## Abstract

**The liveness signal named in this paper's title is an admission predicate, not a weighted input to a ranking function.** We state this first because the paper's whole content follows from it: a weighted input produces an order, an order is a rank, and a rank is the thing this design exists to do without.

Local discovery — routing a person to a nearby business they do not yet know — is presently solved by ranked, purchasable surfaces. That solution has a structural bias toward scale which is mechanical rather than malicious: an auction allocates visibility to the highest bidder per acquired customer, and the highest bidder is reliably whoever has the largest lifetime value, the best measurement, the cheapest capital, and the widest geography over which to amortise creative production. A single-location business is priced out of the discovery layer by construction. Reputation systems built to correct this — consumer review platforms above all — have been captured repeatedly, and we argue the capture follows from a shared property rather than from bad management: **reviews are fungible, and they are aggregated into a per-recipient total, so both the fake-review market and the placement-upsell business have something to attach to.**

We specify a discovery layer with no such total. **Admission** is a predicate over circulation — a rate, not a stock, derived from how often a participant's balance returns to zero — evaluated as a boolean with amplitude excluded, so that the smallest circulating operator is admitted exactly as much as the largest, and so that admission cannot be accumulated toward. **Order** is a publicly recomputable rotation. **The turn belongs to the giver**, arising at the moment they spend from a forward-only, locality-restricted account, from which it follows that the system has no recipient-facing surface and therefore nothing to sell to the parties it routes people toward. Where a real relational path exists — someone the viewer has themselves thanked has thanked this recipient — that single named hop is shown instead; a path is one act by one named person and cannot sum.

We are explicit about what this does not achieve. **The design does not prevent concentration. It prevents compounding.** Givers will still choose the familiar, so the outcome distribution may remain heavy-tailed; what the design removes is the return edge of the feedback loop, because there is no recipient total for an outcome to accumulate into. A ranked system has a ratchet — visible, therefore chosen, therefore *more visible*. This one does not. That is a smaller claim than "no gradient," and it is the one we can defend.

We are equally explicit about the costs. Quality degrades relative to ranking: *find me the best pho in town* is a question this system permanently refuses, and we answer only *pho near me*, by distance. Discovery becomes intermittent, because admission is bound to a named operator's presence rather than to premises. The isolation inequity documented elsewhere in this corpus — those whose kindness is less legible circulate less and are therefore seen less — is not repaired here. And the design contains exactly one number, the liveness window, which must be published, global and rarely changed, because a window tuned per recipient or per district is a ranking knob wearing a predicate's clothes.

Finally we note that the routing primitive is not new to this corpus and we do not claim it. *Steward-Routed Alms* (July 2026) already published rotation-as-router for monastic invitation, on the explicit ground that no evaluative metric may exist anywhere in the system. What is new here is the substitute for ordination. In the monastic case admission is a durable institutional status; in a commercial setting there is no ordination, and the mechanism needs some criterion that admits without ranking and cannot be accumulated toward. **The liveness predicate is that substitute, and supplying it is what generalises a monastic routing rule into a discovery layer.**

Offered defensively to the commons under CC0.

**Keywords:** unranked discovery, rotational routing, non-accumulating reputation, liveness signal, popularity-gradient-free ranking, giver-side discovery, local commerce, sortition, rotating savings and credit association, impression-free advertising alternative, defensive publication.

---

## 1 · Why this problem is the institution's problem

HeartBank® has made a permanent institutional commitment not to adopt an advertising-funded revenue model and not to adopt an engagement-maximising ranking objective for any feed it operates. That commitment is stated in the institution's position on the attention economy, and it is held in the same class as its commitments never to seek a banking charter and never to patent the mechanisms it invents.

A commitment of that kind creates an obligation the institution has not previously discharged. If a person is to be routed to a nearby business — and the commercial layer specified in *The B-Tag and the Post-Payment Economy* assumes they will be — then either that routing is performed by a ranked, purchasable surface, in which case the commitment is broken in the one place it matters most, or it is performed some other way, and the other way has to be specified.

The institution's existing answer does not survive inspection, and this paper's first duty is to say so plainly. §7.1 of the B-Tag paper specifies a *gratitude-based exposure algorithm*: merchants with high accumulated Kiitos receive more visibility in the discovery surface, visibility breeds further interaction, and further interaction generates further Kiitos. That is a popularity gradient with the feedback loop stated approvingly in the paper's own words, and it is inconsistent with three commitments made elsewhere in the same corpus — that gratitude quantities are not to be ranked, that a registry address buys an address and not prominence, and that the institution does not operate ranked discovery. It is also, as it happens, the same error the institution shipped in product copy and corrected in August 2026, where an interface told users that a growing balance would climb the aura's colour scale. That was false, and false in the expensive direction: it taught hoarding. The paper's §7.1 teaches the same thing to merchants.

We note the diagnostic value of the name. §7.1 calls the mechanism an *exposure* algorithm, and *exposure* is the recipient's word — the word a party uses when what they want is to be seen. A discovery layer named from the recipient's side will grow a recipient-facing surface, because the vocabulary arrives before the product does. Throughout this paper the vocabulary is the giver's or the mechanism's, and the words *exposure*, *placement*, *listing*, *visibility*, *reach* and *impressions* do not appear as terms of art.

## 2 · Background and prior art, engaged generously

**Rotation is ancient and this paper does not claim it.** Allocation by turn or by lot, adopted specifically to prevent advantage from accumulating, is one of the better-documented patterns in institutional design. Athenian democracy allotted most offices rather than electing them, on the explicit reasoning that election favours the already-prominent. Jury selection by lot survives on the same logic. Contemporary allocation-by-lottery is standard where a scarce good must be distributed without ranking claimants: over-subscribed school places, immigrant visa lotteries, and deceased-donor organ allocation, where the ordering rules are deliberately constructed to exclude social worth. Round-robin scheduling is the same idea in operating systems, where it exists precisely to stop a high-priority process from starving the others. Crop rotation is the agronomic form.

**Rotating savings and credit associations are the closest working ancestor**, and they are worth more than a citation. A ROSCA — *tong tin* in Khmer, *tanda*, *susu*, *chit fund*, *tontine* elsewhere — allocates a common pot by turn, with membership sustained by continued contribution and by nothing else. There is no assessment of need, no ranking of members, no interest. It is *rotation over a participation predicate*, it is the mechanism specified below with money in place of attention, and it has run at village scale for centuries in the jurisdiction this institution is building in first. Any claim in this paper to have invented rotation-with-a-participation-predicate would be false, and we make none.

**This corpus already published the routing primitive, in the monastic domain.** *Steward-Routed Alms* (July 2026) specifies invitation routing in which "rotation is the router — the digital *sapadāna*", the routing agent assigns by proximity, rotation and fairness, donors select a community rather than an individual, declines are unrecorded, and **no evaluative metric on monastics exists anywhere in the system**. That paper is prior art against this one and we cite it as such. What it does not supply is a criterion for admission in a setting without ordination, which is the gap §4.1 fills.

**The consumer review platform is the nearest attempt at the actual problem, and it failed.** Review platforms are witness layers for small local businesses and they were captured along two independent paths: a fake-review market, which exists because reviews are fungible and countable; and placement-adjacent monetisation, which exists because a ranked surface has a top. We take the capture as evidence about the *shape* rather than about the operators — an aggregated per-recipient total is the thing both attacks attach to, and neither attack has an obvious point of attachment when no such total exists.

**The honest negative control is Craigslist**, and it belongs in this section rather than in the lineage. Craigslist ran unranked, chronological, essentially unmonetised local discovery, at very large scale, for over a decade, and it worked. It then lost most of its verticals to ranked, better-capitalised competitors that presented curated and sorted inventory. The lesson we take is not that unranked discovery fails; it is that **unranked discovery is not self-defending against a ranked competitor with capital**, and that any institution adopting this design should expect to be out-converted on any metric a ranked competitor chooses to compete on. We have no answer to that beyond the institution's own thesis, which is that it is not trying to win that competition.

**What we do claim as novel** is narrow and we state it narrowly: the liveness predicate as a non-accumulating admission criterion; the turn belonging to the giver and the consequent absence of a recipient-facing surface; the no-aggregate and no-impression constraints stated as design properties rather than policies; ledger-generated presentation; and the combination of these with operator-bound, non-transferable admission. The transposition of a monastic routing rule into commercial discovery is a transposition, and we present it as one.

## 3 · The ratchet: what is actually being designed against

It is worth being precise about the failure mode, because the obvious statement of it is wrong and the wrong statement leads to a worse design.

The problem with ranked discovery is not that some businesses receive more customers than others. Some businesses are better, and a distribution in which the better ones do more trade is not a defect. The problem is that a ranked surface closes a loop:

```
              ┌──────────────────────────────┐
              │                              │
              ▼                              │
      more visible  ──▶  more chosen  ──▶  higher total
              │                              ▲
              └──────────────────────────────┘
                    the return edge:
              the outcome is written back into
              the quantity that decides visibility
```

Once an outcome is written back into the quantity that determines visibility, small early differences — including differences produced by luck, by capital, or by fraud — are amplified without limit. This is the ratchet. It is what makes the fake-review market profitable, because a purchased early advantage compounds. It is what makes placement worth buying, because purchased visibility converts into the durable quantity. And it is what prices out a new entrant, whose total is necessarily zero at the moment they most need to be found.

The design below does not attempt to flatten the outcome distribution. It cuts the return edge:

```
      more visible  ──▶  more chosen  ──▶  ( nothing )

      admission:  a predicate over the operator's circulation
                  — unaffected by how often they were chosen
      order:      a published rotation
                  — unaffected by how often they were chosen
```

**The distinction matters because it is the difference between a claim we can defend and one we cannot.** We are not claiming that a rotation makes outcomes equal, and we return to this in §8, where the claim is stated in its final and smaller form.

## 4 · The mechanism

The design has four parts: an admission predicate, an order, an allocation of the turn, and a warm layer for the case where a real relationship exists.

### 4.1 · Admission: the liveness predicate

Each participant in the institution's ledger has an **aura** — a public, per-person rendering of the *frequency and amplitude of their oscillation around zero*. It is computed from circulation velocity: how often the participant's balance returns to zero, which happens when what they have received is given forward. It is the structural inverse of a credit score. A participant who only accumulates does not climb it; a balance that only grows produces no crossings and the aura stays at the bottom of its scale indefinitely. Inactivity dilutes it through a scheduled passive sample, so a participant who circulates hard and stops does not retain the appearance of circulating.

Admission to the rotation is a predicate over that quantity:

> **Has this participant's balance crossed zero within the liveness window?**

Three properties of this predicate carry the design.

**It is a rate, not a stock.** This is the substitution that makes the rest possible, and it is worth stating as a general result. A stock — an accumulated total of gratitude received — is hoardable, and anything hoardable is capturable by whoever can accumulate fastest. A rate describing oscillation around zero cannot be held at all: **holding is exactly what drives it to zero.** A visibility criterion that cannot be held cannot be accumulated toward, and a criterion that cannot be accumulated toward has no ratchet available to it.

**Amplitude is excluded.** The aura's underlying computation carries both frequency and amplitude; the predicate reads only whether the crossing occurred. A operator circulating small amounts is admitted exactly as much as one circulating large amounts, because there is no "as much" — admission is boolean. This is what prevents the predicate from becoming a proxy for revenue, and it is the single most important line in the specification for the design's stated purpose, which is that a small local business be findable at all.

**It admits; it never ranks.** No participant is more admitted than another. There is no partial admission, no tier, no "verified plus". The predicate's output is a set, and the set is unordered.

We note the constraint this places on the design's ancestry. The institution has elsewhere rejected threshold gates of the form *reach X to unlock Y* as "a score with locks", and adopted instead the rule **reveal, never lock**, with the diagnostic that available forms must vary by *the character of the waveform, never by a magnitude*. The liveness predicate conforms: it reads a character (is the oscillation happening) and not a magnitude (how large, how many). A predicate reading magnitude would be the rejected gate, and it would import the ratchet through the admission door.

### 4.2 · Order: a publicly recomputable rotation

Within the admitted set, order is determined by rotation. The rotation is specified with three publication requirements, all of which the institution has already adopted for a different rotation elsewhere in its portfolio:

1. **The algorithm is published.**
2. **The seed is surfaced with each cycle.**
3. **A recomputation tool ships** — a page that accepts the seed, the roster and a count and prints the resulting sequence.

Together these convert the rotation from a rule into something checkable by arithmetic. Any participant who suspects the order was tampered with can recompute it. This matters more than it appears to: a rotation that only the operator can compute is indistinguishable from a ranking that the operator declines to describe, and the difference between the two is exactly what the publication requirements make visible.

A turn, once allocated, is **consumed or lapses**. It cannot be banked, deferred, transferred, or bought. Non-storability is what prevents a secondary market from forming: there is nothing to hold, so there is nothing to trade, and no broker can build a business on discovery placement because placement is not a thing that persists long enough to be sold.

### 4.3 · The turn belongs to the giver

This is the design's spine and the property from which most of the others follow.

The discovery moment is not a shopping query. It arises when a participant is about to spend from a **Re-Tip Jar℠** — an account that is forward-spendable only, never withdrawable, and restricted to nearby recipients. That money has to go somewhere, and the choosing of where is itself the discovery event. At that moment the participant is presented with a small set of admitted nearby recipients whose turn it is, and they choose.

Three consequences follow, and the third is the one that matters.

*First*, the frame is giving rather than buying. A person encountering a small business while deciding where to direct gratitude is in a materially different state from one encountering it while being sold to, and the encounter is worth more to both parties.

*Second*, the volume of discovery is bounded by the volume of giving, which is a property we regard as correct rather than as a limitation. A discovery layer that can produce more discovery than there is gratitude to distribute has decoupled from the thing it is supposed to serve.

*Third* — **the system has no recipient-facing surface at all.** There is no merchant dashboard, no listing management, no analytics, no placement product, and no account manager, because there is nothing for any of them to do. A recipient cannot see whether they are in today's rotation, cannot see how often they have appeared, and cannot buy, improve, or influence any of it. **The absence is the mechanism.** An institution with no discovery product cannot be tempted to sell one, cannot be lobbied to prioritise one advertiser over another, and cannot quietly convert its discovery layer into an advertising network under financial pressure, because the conversion would require building a surface that does not exist rather than changing a policy that does.

We state this as a spine rather than as an option deliberately. A recipient-facing surface that exists "only for the cases where the rotation is not enough" is a recipient-facing surface, and **an optional absence is not an absence.**

The obvious objection is bootstrapping: if discovery volume is bounded by re-tip volume, then early in the system's life, when re-tip volume is near zero, discovery is near zero, and the businesses that most need to be found cannot be. The objection is real and the B-Tag paper already anticipates it under a different heading. The answer is that the institution's autonomous agent, **Miss Aquarius℠**, funds *the capacity to give* — anonymously contributing to participants' Re-Tip Jars from the **Aquarian Pool℠** — while participants retain sole authority over disbursement. She therefore has a dial that raises or lowers the *rate* of discovery, without ever touching *who appears*. §9 states the bar that keeps that dial safe.

### 4.4 · The warm layer: a path is not a score

Where a relational path exists between the viewer and a candidate, the candidate is presented with the path rather than with nothing:

> *Sophea, whom you thanked in June, thanked this shop.*

The unit here is **one act, by one named person, standing in a real relation to the viewer.** It is not a count, not an average, not a percentage, and it cannot sum: there is no operation that turns two paths into a bigger path. This is the design's substitute for the quality signal that ranking would otherwise supply, and it is the component that answers the review platform's capture problem most directly. **A fake review works because reviews are fungible and aggregated. A path is neither.** Fabricating one requires standing in a real, witnessed, co-present relation to the specific person viewing the surface — which is not a thing that can be manufactured at scale, because it must be manufactured separately for every viewer.

Two constraints on the path layer are load-bearing:

- **The path is never presented as an evaluation.** It reports that an act occurred; it does not report that the recipient is good, recommended, trusted, or preferred. This is doctrinally required and it is also legally required — evaluative claims of that kind are substantiation-triggering in advertising law, and a discovery surface affecting commerce is squarely within that exposure.
- **Absence of a path is never rendered.** A candidate with no path is presented exactly as a candidate with no path — not as *"no one you know has been here"*, which is an accusation delivered to a business and an anxiety delivered to a viewer. The corpus's standing rule is to render what is present and never what is missing, and it applies here without modification.

### 4.5 · The two regimes

The design therefore operates in two regimes, and it should say which is which rather than pretending to be one thing:

```
                COLD                             WARM
                (no path to the viewer)          (a path exists)

  admission     liveness predicate               liveness predicate
  order         published rotation               the path itself
  what is       name, address, category          name, address, category
  shown         — all ledger-generated           + one named single hop
  strength      new entrants are reachable       a signal that cannot be faked
                at all                           at scale
  weakness      routes to the merely fine        thin networks, new arrivals,
                                                 and a new town
```

Neither regime is a fallback for the other, and the interface must not describe either as one. The cold regime is not a consolation for having no friends; it is the surface.

## 5 · The properties, and the test they are stated to pass

The specification above is deliberately expressed as properties of objects rather than as rules about behaviour. The reason is stated elsewhere in this corpus as a design signature: **a rule needs an enforcer present at the moment it is tested; a property needs no one.** An institution built to outlive its founder and to hand its operation to an autonomous successor cannot rest on anyone's restraint, because every rule requires a living enforcer with the right incentives at exactly the moment nobody can guarantee them.

The operative test is therefore not *is this rule good* but **remove the enforcer — does the guard survive?**

| # | Property | Remove the enforcer | What it rules out |
|---|---|---|---|
| 1 | No recipient aggregate exists; witness events attach to the giver | Survives — ranking by received gratitude is *unavailable*, not forbidden | totals, stars, "trending", reputation-management vendors |
| 2 | Every admission gate is boolean; no gate is a magnitude | Survives — a threshold can be met, never climbed | quality scores, tiers, verified-plus |
| 3 | Order is a published, recomputable rotation | Survives — any participant can recompute the order by arithmetic | pay-for-placement, undisclosed house favourites |
| 4 | A turn is consumed or lapses; it cannot be stored | Survives — un-hoardable capacity cannot be capitalised | placement markets, brokers, futures in visibility |
| 5 | The turn belongs to the giver; no recipient-facing surface exists | Survives — there is nothing to sell, and no surface to lobby | the entire advertising business model |
| 6 | No merchant-supplied creative; every card element is ledger-generated | Survives — production budget has no surface to act on | creative-spend advantage, brand-asset asymmetry |
| 7 | No impression is ever attributed to a recipient | Survives — a quantity never counted cannot be sold | impression inventory, reach reporting, CPM |
| 8 | Intent is served by distance, a property of the seeker | Survives — distance is unpurchasable and unaccumulable | popularity-sorted category results |
| 9 | Admission attaches to a natural person, not to an entity | Survives — nothing transfers at sale of the business | aged-listing purchase, reputation acquisition, chains |
| 10 | The admission quantity is consumed, never displayed in a slate | Survives — there is no rendered gradient to read | ranking reconstructed in the viewer's eye |

Property 10 deserves its own note, because it was the last one found and it was found by asking a question about the title rather than about the mechanism. The aura is **public on a person**, by ratified institutional design, and its colour scale is **ordered**. It follows that if a candidate card renders the operator's aura colour, a viewer looking at three cards side by side can rank them by eye — reconstructing in the render layer precisely the gradient the mechanism declines to compute. The resolution is a distinction between surfaces rather than between values: **the aura is public on a person and invisible in a slate.** A person's own representation is not a comparison context; a candidate set is. The admission quantity is read, used, and then disappears.

We note the general lesson, since it is cheap and recurs: a design can satisfy every constraint at the mechanism layer and reintroduce the defect at the presentation layer, and the presentation layer is where nobody looks for it.

## 6 · What the design refuses, and what the refusals cost

**It refuses to answer "which is best".** *Find me the best pho in town* is a question this system does not answer and will not answer, because every possible answer is a ranking. This is the design's largest user-facing cost and we decline to soften it.

What it answers instead is *pho near me*: filter by category, order by **distance from the seeker**, display no scores. The principle that makes this admissible is worth stating separately, because it is the one place where an order is permitted:

> **Ordering by a property of the seeker is not a ranking of the candidates.**

Distance is a fact about where the user is standing. It is not purchasable, not accumulable, not transferable, and not a claim about merit. A candidate is not "better" for being nearer; it is nearer. This closes what would otherwise be the design's largest practical hole — the person who knows what they want and simply needs to find one — on principle rather than by exception, and it does so without adding any quantity to the system.

**It refuses to rank quality, so quality degrades.** A rotation over a boolean admission set will route people to businesses that are merely fine. There is no version of this design in which that is untrue, and any presentation of it that implies otherwise is dishonest. What can be said in mitigation is narrow and we will not overstate it: the warm layer supplies a quality signal to viewers who have a relational path, and the admission predicate does exclude one class of bad actor — the participant who takes and does not circulate — which is not nothing, but is also not a quality assessment.

**It refuses transferable reputation, so discovery becomes intermittent.** Admission attaches to a named natural person. For a multi-person business the reading is that **any co-present operator with a live aura admits the premises for that shift** — discovery follows the person, not the building, which ties it to the same co-presence primitive that gates witness elsewhere in the architecture. The cost is that a business is discoverable when a qualifying human is actually present and not otherwise. For a single-operator business this is nearly always. For a larger one it is a real and visible limitation.

The compensating property is severe enough to be worth the cost. Because admission is bound to a person and non-transferable, **selling the business does not transfer eligibility** — which closes the aged-listing purchase that has been a persistent capture vector in review platforms — and **a multi-site operator cannot qualify at all**, not because chains are excluded by a rule but because there is no single person whose circulation the entity's admission would be. The design's local bias is therefore structural rather than declared. No anti-chain rule appears anywhere in this specification, and none is needed.

**It refuses to count, so it cannot report.** No participant can be told how many times they appeared, and no recipient can be told how many people saw them. We are aware that this removes a feedback signal businesses reasonably want, and we regard the removal as load-bearing rather than austere: an impression count is the recipient-side aggregate re-created on the supply side, and once it exists somebody will eventually sell it.

## 7 · The one number

Every boolean gate conceals a threshold somewhere in its definition, and honesty requires naming this one rather than letting a reader discover it.

The liveness predicate asks whether a crossing occurred **within a window**. The window is a number. A seven-day window and a ninety-day window admit materially different populations: the short window admits only the continuously active and will exclude a seasonal business, a sole trader on holiday, and a shop in a slow month; the long window admits nearly everyone and weakens the predicate toward vacuity.

Three constraints on it, all of which follow from what the predicate is for:

1. **It is published.** A predicate whose threshold is secret is not checkable, and an unchekable predicate is a ranking whose function nobody can see.
2. **It is global.** One window for every participant. A window tuned per recipient, per category, or per district is a ranking knob wearing a predicate's clothes, and it would be the single cheapest way to corrupt this design from the inside.
3. **It changes rarely, and changes are announced before they take effect.** A window change is a change to who is admitted, and a silent one is indistinguishable from a purge.

We do not specify the value. We specify that there is exactly one number in the design, that it is this one, and that a future implementer who finds themselves adding a second should treat that as evidence the design has drifted.

## 8 · The claim, in its final and smaller form

The strongest version of what this design does is not the version we can defend, and stating the defensible one is the point of this section.

**What we do not claim: that the outcome distribution is flat, or that no popularity gradient arises.** Givers choose. They will choose the familiar, the closer, the more attractive photograph on the sign, the one their cousin mentioned. Human preference concentrates, and no property of a mechanism governs human preference. It is entirely possible that a rotation-based system produces an outcome distribution that looks, when plotted, much like a ranked one.

**What we claim: that the ratchet is absent.** In a ranked system, the outcome is written back into the quantity that determines visibility, and the loop compounds. Here it is not written back anywhere, because there is nothing to write it into. Concentration that arises from preference stays proportional to preference; it does not amplify itself, it does not convert into a durable advantage that a new entrant must overcome, and it cannot be seeded by purchase or by fraud, because there is no total for a purchase or a fraud to inflate.

We regard this as a real and testable difference, and as a considerably smaller one than the design's own elegance invites us to claim. We note the standing caution that applies to work of this kind: **a tension-dissolving, self-similar, coherent system is either deeply right or deeply seductive, and the two are indistinguishable from the inside.** The individual properties in §5 are each falsifiable on their own — *does a turn persist? is an impression counted? can a chain qualify?* are all answerable by building the thing and looking. The pattern they make is not falsifiable at all. The properties earn their keep one at a time; the coherence earns nothing, and should not be cited as evidence for any member of the set.

## 9 · Two dials, and the bars on them

A design with no ranking still has parameters, and the honest thing is to enumerate the ones that could be used to steer it.

**The volume dial.** Miss Aquarius℠ funds participants' capacity to give, and therefore controls the rate at which discovery events occur. The bar is:

> **She may move discovery's volume. She may never move its addressee.**

Admission is the operator's liveness predicate; order is the published rotation; the addressee is chosen by the human spending from their own jar. She funds the giving; she never aims it. A dial able to change only a rate is safe. The same dial able to change an address is an advertising network with a single customer, and it is the one point at which this entire architecture could be quietly inverted by an agent nudging volume in ways that correlate with recipients it prefers. Two riders follow: **no per-recipient impression figure may exist for her to optimise against** — she holds a global volume figure and nothing finer — and any future locality-level modulation is bound by the same rule stated per place.

**The place-commons dial, which is an experiment and not part of the design.** The institution's second gratitude ledger, **Kiitti**, records standing between people and non-human parties — products, places, animals, plants — and is the anti-externality ledger rather than a commercial one. Its aggregate over a locality is a *commons* quantity: shared by everyone in the place, and therefore structurally incapable of differentiating between recipients inside it. This suggests a mechanism in which a locality's Kiitti modulates the **volume** of discovery for that place while never touching the **order** within it — converting what is elsewhere a rivalrous advertising spend into a non-rivalrous investment in a shared place, with neighbouring businesses holding a common interest in the trees, animals and care of the street they share.

We specify it here and we do not adopt it, for a stated reason. **Comparing places builds a gradient between cared-for and neglected neighbourhoods, and that gradient runs directly against the adoption-equity commitment this institution holds as an open problem rather than a solved one.** If it is ever run, it runs self-referentially — a place measured against its own history, never against another place — as a pre-registered experiment with the tripwire in §11.3, and it is switched off on the tripwire regardless of what it is doing for circulation. What ships is the unconditional half: Kiitti flows in the encounter, as the line-wide product law already requires, and plays no part in discovery.

## 10 · Generality: one primitive, three domains

The routing primitive specified here appears in three places in this institution's architecture, and none of the three was designed for the others.

| Domain | Instance | Admission | Order | Published |
|---|---|---|---|---|
| Sangha | the alms round — monastic invitation routing | ordination and community membership | rotation, proximity, fairness | *Steward-Routed Alms*, 2026-07 |
| Play | the sey circle — the ball reaches every player | presence in the circle | the circle's own turn-taking | *Circulation Sports*, *The Sport That Says Your Name* |
| Commerce | the round specified here | the liveness predicate | published recomputable rotation | this paper |

The three differ in exactly one component, and the difference is instructive. In the Sangha, admission is a **durable status**: you are ordained or you are not, and the status does not decay. In the circle, admission is **presence**: you are standing in it or you are not. In commerce there is no ordination and standing in a place is not enough, so admission must be supplied by something else — and the something else has to admit without ranking and must not be accumulable, or the ratchet returns through the admission door. **The liveness predicate is that substitute. Supplying it is the whole of this paper's contribution over the monastic case, and the rest is transposition.**

The generality also gives a diagnostic for future surfaces in this architecture. Wherever a party must be selected from many, the question to ask first is *what is the admission predicate, and can it be accumulated toward?* If the honest answer is that admission is a quantity, the surface will grow a ratchet regardless of what its designers intend.

## 11 · Pre-registered predictions

The design is unbuilt and unobserved. The following are registered before any data exists, and the institution commits to publishing each result whether it confirms or refutes.

**11.1 — P-D1 (the rotation does something).** Among discovery events in a live market, a non-trivial share resolve to recipients who have never previously received a re-tip.

> *Falsifier:* if discovery concentrates on the same recipients at approximately the rate a ranked system would produce, the rotation is not doing work and the apparatus is theatre. **We would publish that, and the correct response to it would be to abandon the design rather than to tune it.**

**11.2 — P-D2 (the local thesis).** Among re-tips with an identifiable commercial recipient, the share accruing to single-location operators materially exceeds those operators' share of local digital advertising spend in the same market; and the gap widens as the share of AI-generated advertising creative rises.

> *Falsifier:* if the distribution mirrors local ad-spend distribution, witness is not structurally local — it is a cheaper advertisement, and the thesis in this corpus that an appreciation layer routes differently from an attention layer is wrong.

**11.3 — P-D3 (the place-commons tripwire).** If the §9 place-commons experiment is ever enabled, cross-place discovery volume will not correlate with neighbourhood median income.

> *Falsifier and tripwire in one:* if it does correlate, the mechanism is disabled, whatever it is doing for circulation. This prediction is registered specifically so that a favourable circulation result cannot later be used to argue for keeping it.

**11.4 — P-D4 (the presentation layer).** Adding any rendered per-recipient quantity to the candidate surface — including the operator's aura colour — will produce measurable order effects in giver choice.

> *Falsifier:* if a rendered quantity produces no order effect, property 10 is unnecessary and the constraint can be relaxed. We expect the opposite and register it because the constraint is otherwise unjustified by anything but reasoning.

## 12 · Honest limits

**12.1 · Nothing has been built.** There is no implementation, no market, no participant, and no observation. Every claim here is architectural.

**12.2 · Human choice is outside the mechanism.** §8 states this as the design's central concession and it is repeated here so it is not lost: the ratchet is absent; concentration is not.

**12.3 · Quality is genuinely worse than ranking.** §6. The system routes to the merely fine and refuses the question a user most wants answered.

**12.4 · The isolation inequity is untouched.** This corpus has documented, in the context of aura-gated matching, that participants whose circumstances make their kindness less legible — the isolated, those with no community to circulate within, those whose care is invisible — accumulate less and are therefore seen less. Excluding amplitude repairs the *scale* inequity: the small operator is admitted equally. It does nothing for the *isolation* inequity, because a participant who cannot circulate at all fails the predicate. We do not have a repair and we decline to imply one.

**12.5 · Supply flooding is the live attack.** An adversary who can mint many admitted identities captures more turns. The design converts a ranking attack into an identity attack, which lands on the institution's strongest existing defences — proof-of-humanity layers, non-transferable registry handles, co-presence-gated witness — but "converts to a problem we are better at" is not "solves". This is where an adversary should aim, and we expect them to.

**12.6 · Craigslist.** §2. Unranked local discovery has been beaten commercially before, by capital and curation, and nothing in this design defends against that.

**12.7 · The window is a governance surface.** §7. One number, published and global, is a small attack surface — but it is not zero, and whoever sets it has real power over who is admitted.

**12.8 · The elegance is not evidence.** §8's caution, restated: the properties are individually falsifiable, the coherence is not, and the coherence should never be offered as support for any of them.

## 13 · Cross-venue references

- *The B-Tag and the Post-Payment Economy* — the commercial layer this design serves. **§7.1 of that paper is superseded by this one**; the supersession is recorded there in the open rather than by revision, and the *gratitude-based exposure algorithm* specified in it should be read as withdrawn.
- *Steward-Routed Alms* — the monastic instance of the routing primitive, and prior art against this paper.
- *Certification by Circulation* — the circulation-as-standing argument this design's admission predicate instantiates.
- *B-PoH: The Humanity Layer for an AI-Native Internet* — the identity substrate on which §12.5's defences rest.
- *Appreciation as World-Building* — the unholdable-commons property of which the liveness predicate is a second instance.
- *HeartBank's Position on the Attention Economy* — the institutional commitment that makes this paper necessary.
- *The Moat Is What We Refuse* — the strategic argument for why a design made of refusals is publishable without competitive cost.

---

## Coda

The alms round's rule is not that the poor house deserves the monk. It is that the walker does not get to decide, and that the walking is done in order, and that the round reaches the whole street because nobody is choosing which parts of it matter.

We have specified a discovery layer whose central content is a set of absences: no total, no impression, no creative, no dashboard, no rank. It is a worse product than a ranked one in the ways a ranked one is measured, and we have said so in every section where the comparison arises. What it has instead is that the things which usually go wrong with discovery layers are not prevented in it — they are unavailable, which is a different and more durable condition, and one that does not require anybody in the future to keep a promise.

Whether that trade is a good one is an empirical question, and §11 is our attempt to make it one that can be settled rather than argued.

---

*Dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). The author and HeartBank® will not seek patent on this specification or any portion thereof.*
