---
title: "Appreciation as World-Building"
subtitle: "A Walkable Gratitude Map Whose Terrain Is a Ledger Readout Rather Than a Purchased Inventory — Four Mechanisms, Two Pre-Registered Predictions, and One Permanence Hazard"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-b
status: draft
date: 2026-08-13
license: CC0-1.0
slug: appreciation-as-world-building
venue: thonly.org/publications/defensive-publications/appreciation-as-world-building (canonical)
---

> *Draft notes for the editor:* this paper describes a product that **does not exist**. No code has been written, no schedule has been set, and the sample size for every behavioural claim in it is **zero**. It is published now for one reason, stated plainly because it governs what the paper does and does not contain: **publication protects against being blocked, not against being beaten.** For an unbuilt and unscheduled artifact, the defensible move is to publish the *claim* and withhold the *specification* — so this paper is deliberately **deep on argument and thin on implementation.** Where a section would ordinarily give a rendering function, an asset pipeline, a threshold table, or a price, it gives the property the mechanism must satisfy and stops. That is a departure from this corpus's usual practice and it is intentional. Readers looking for something to build from will find the constraints; readers looking for something to copy will find that the interesting part was never the pipeline.

---

## Abstract

A gratitude journal asks a person to write. That is the highest-friction step in the practice and the one most people abandon, which is why gratitude journaling has a large product category and a small population of sustained practitioners. This paper specifies a different container for the same practice: a **walkable map of the things a person appreciates**, captured by photograph with a coordinate and an optional note, rendered as placed artifacts in that person's own world.

The move is not cosmetic. It is a **host-ritual swap**. Photographing a thing you appreciate and posting it with a location is a behaviour hundreds of millions of adults already perform unprompted; writing three sentences of gratitude before bed is a behaviour that must be installed. Swapping the container replaces the practice's most expensive step with its cheapest, and the paper's central thesis is that this changes the population that can hold the practice rather than merely the interface through which they hold it.

Four mechanisms carry the design, and they are the paper's contribution. **First, appearance is a ledger readout, not a purchase**: a participant's avatar and terrain *are* their signed gratitude balance rendered as light, never goods bought with it — which is what allows an annual balance-forgiveness to remain forgiveness rather than becoming confiscation. **Second, availability reveals and never locks**: a form becomes available the first time a participant's oscillation has ever had that quality and remains available permanently, so the system has no wall of locked content and no mechanism by which a quiet season can take something back. **Third, placement requires presence and visiting does not**: a participant can only *write* to the map by standing at the coordinate, which is the property that separates a presence-deepening world layer from a presence-replacing one. **Fourth, the render is three-layered** — the sky carries the coordinator's aggregate ledger, the land and ocean carry the participant's non-human ledger, the avatar carries the participant's human-to-human ledger — and the structural consequence is that **the only shared surface in the system belongs to the one party structurally incapable of accumulating anything.**

The paper further specifies a two-speed practice, in which gratitude toward **things** is frictionless and frequent and gratitude toward **people** spends attention and is occasional, and it identifies the unsolved transition between them as the design's live open problem rather than concealing it. It states a permanence hazard that follows from the design's archival terminus — that a deep-time substrate converts every present-tense privacy defect into a permanent one, so guards must be built at capture rather than at commit. And it pre-registers two opposed predictions, before any code exists, one of which would invalidate the thesis rather than trim it.

Almost nothing in the paper's *technology* is novel and the paper says so at length. Geotagged user content, photogrammetric and generative photo-to-3D, avatar worlds, and world-scale augmented reality are dense, well-funded prior art. What is offered is the conjunction: an appreciation practice whose world is a **non-purchasable, annually-forgiven, reveal-only** rendering of a signed ledger. Offered under CC0 1.0 Universal as defensive prior art.

**Keywords:** gratitude practice, world-building, geotagged user content, host-ritual substitution, ledger readout, anti-credit-score, reveal-not-unlock, presence-deepening augmented reality, deep-time archival privacy, moral self-licensing, pre-registration, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The authors and HeartBank® will not seek patent or any other exclusive right on the mechanisms described herein, in any jurisdiction, at any time. The publication exists so that the mechanisms cannot be enclosed by anyone — including by us.

**Terms coined and freed with this paper:** *appearance-as-readout*, *reveal-never-lock*, *the equally-alive diagnostic*, *placement-requires-presence*, *the two-speed practice*, and *the permanence asymmetry* as stated in §9.

**Terms inherited from this corpus's earlier publications and cited rather than re-claimed:** the *B-Aura* and the signed Kiitos/Kiitti ledger (*The Zero-Point Game*), *Proof of Humanity℠* and *Proof of Coordinate℠*, the *give-forward* atom, the *play/currency wall*, and the annual jubilee.

**Most of this paper's technical subject matter is not ours and is not claimed.** Location-anchored user-generated content is a mature field with at least two decades of practice behind it: Geocaching (2000), Foursquare and its check-in grammar (2009), Google Local Guides, Niantic's Ingress (2013) and Pokémon GO (2016) and the Lightship visual-positioning work that followed, Google's Live View and ARCore Geospatial API, Snap's landmarker and Spectacles programmes, and the broader "mirrorworld" or AR-cloud programme articulated publicly by Kevin Kelly and pursued by several of the above. Photogrammetric reconstruction from photographs is decades old and is shipped as a first-party consumer capability, notably Apple's Object Capture and `PhotogrammetrySession`. Single-image generative 3D reconstruction is an active and rapidly moving research and product area with many independent groups. Femtosecond-laser 5D optical storage in silica is the work of the University of Southampton's optoelectronics group and of Microsoft's Project Silica. The tension between immutable storage and erasure rights is a large existing literature developed largely in the blockchain-and-GDPR context. The gratitude-intervention literature begins for most practical purposes with Emmons and McCullough (2003). The counter-hypothesis this paper pre-registers against itself is drawn from the moral self-licensing literature (Monin and Miller, 2001; Merritt, Effron and Monin, 2010).

**We claim none of that.** What we claim is the conjunction described in §13 and nothing beyond it. Where this paper's design coincides with an existing product's design, the existing product has priority and we say so.

---

## 1 · Why the container is the problem

The gratitude-practice literature is unusually clean for a wellbeing intervention. Structured gratitude exercises produce measurable effects on affect and, in several designs, on prosocial behaviour. The finding has survived enough replication that the practical question stopped being *does it work* and became *why does almost nobody keep doing it*.

The answer is not mysterious. The canonical form of the practice — write down three things you are grateful for — requires a person to sit down, compose sentences, and do so repeatedly with no external occasion prompting them. That is a **new habit**, and new habits are the most expensive product category there is. Every gratitude-journaling product in the market is fighting the same fight: not to convince anyone that gratitude is good, which nobody disputes, but to get a person to perform an unprompted act of writing on a Tuesday.

This paper's premise is that the writing is not the practice. The writing is the **container** the practice was historically shipped in, chosen because paper was the available medium, and it has been carried forward unexamined into software that has other options.

Consider what a person actually does when they notice something they appreciate. They stop. They look. Frequently — and this is the empirical fact the whole design turns on — **they take a photograph.** They do this constantly, unprompted, without being told it is a practice, and they do it hundreds of millions of times a day. Nobody had to install that habit; the phone installed it.

So the question this paper asks is: what happens if the practice is given the container the behaviour already has?

### 1.1 · The deficit being addressed

This corpus's standing account of the problem is a **dignity deficit** — that most kindness is never witnessed, and that being unwitnessed is a substantial part of what makes ordinary life feel thankless. The gratitude practice is one half of the response: it trains the noticing. The other half, which this corpus has addressed elsewhere, is the delivery of the notice to the person it concerns.

The design specified here is deliberately positioned at the *first* half and deliberately does not pretend to be the second. It builds a place where a person's noticing accumulates in a form they can walk through. §4 addresses what has to be true for the noticing to lead anywhere, and states honestly that the mechanism connecting the two halves is the design's weakest point.

---

## 2 · Prior art, at length, because the obvious part is obvious

It would be possible to write this paper as though a walkable map of geotagged personal artifacts were an invention. It is not, and a reader who has used a phone in the last decade knows it is not. The honest position is to state the prior art first and at length, so that the small thing being claimed is visible against it rather than hidden by it.

| Prior art | What it established | What this design does not claim |
|---|---|---|
| Geocaching (2000) | Coordinate-anchored discovery as a durable amateur practice | Place-anchored discovery |
| Foursquare / Swarm (2009) | The check-in as a social grammar; place as a post | Check-in mechanics; place-as-social-object |
| Google Local Guides | Mass user contribution of place photographs at global scale | Crowd-sourced place imagery |
| Ingress (2013), Pokémon GO (2016) | Walking as the primary input to a persistent world; portals and gyms as coordinate-bound objects | Walk-driven play; coordinate-bound persistent objects |
| Niantic Lightship VPS; Google ARCore Geospatial; Snap landmarkers | Centimetre-scale world-anchored AR at metropolitan scale | World-anchored placement or its positioning stack |
| "Mirrorworld" / AR cloud (Kelly, 2019 and after) | The concept of a persistent digital layer registered to the physical world | The concept of a persistent world layer |
| Apple Object Capture / `PhotogrammetrySession` | Consumer photo-to-3D reconstruction on device | Photogrammetry |
| Single-image generative 3D (multiple groups, active) | One photo to a usable mesh | Generative reconstruction |
| iNaturalist | Species-level UGC with geoprivacy obscuring for threatened taxa | Obscuring; we adopt their norm and credit it |
| Gratitude journaling apps | The practice as a software category | The practice |
| Emmons & McCullough (2003) and successors | That the intervention has measurable effects | Any effect claim of our own |

Read that table honestly and the position is this: **every component is available, most are commodity, and several are better implemented by companies with more resources than this institution will ever have.** If the contribution were the map, there would be no contribution.

The contribution is what the world is made of. In every prior system in that table, the persistent world is furnished with **content**: things placed by an operator, or bought, or earned by play. This paper specifies a world furnished by a **ledger** — where the terrain is not an inventory a participant assembles but a rendering of a signed balance they cannot purchase, cannot trade, and do not own. That is a different object, and §5 through §8 specify it.

### 2.1 · Why the conjunction was available and not taken

A reader who accepts §2's table may reasonably ask why, if every component is commodity, nobody has assembled them this way. The answer is not that it was overlooked. It is that **the assembly is locally worse.**

Purchasable appearance is not a lazy default. It is a strong local optimum arrived at independently by many well-resourced teams: it converts engagement into revenue without touching the core loop, it gives designers a continuous supply of new content at near-zero marginal cost, it self-segments willingness to pay, and its retention effects are among the most reliably measured in the industry. A team that removes it gives up all of that and receives, in exchange, a doctrinal property invisible to most participants.

So the conjunction in this paper is not a discovery of an unexplored region. It is a **deliberate move into a known-worse region**, made because the institution behind it has a constraint the industry does not: it operates a signed gratitude ledger that is forgiven annually, and a purchasable-appearance economy is not merely off-brand against that ledger but arithmetically incompatible with it (§5). The design is downstream of a ledger commitment, not upstream of a market insight.

That framing matters for how the paper should be read and for how it could be wrong. If the ledger commitment is mistaken, the design inherits the mistake wholesale. If the ledger commitment is right, the design is what follows from taking it seriously — and its commercial disadvantages are the price of the commitment rather than errors in the design.


---

## 3 · The thesis: a host-ritual swap, and the friction inversion

This corpus applies a standing test to any claim that a product "rides an existing ritual." The test has three legs: is the host ritual **live** — performed unprompted by the target adult within the last twelve months; does the ask have the **same shape** as the host — comparable commitment, cost and duration; and is the host in **good standing** with whoever must permit the product.

Run against this design, the test returns a mixed and useful result.

**Leg one passes, strongly.** Photographing a thing one appreciates, with a location attached, is among the most-performed unprompted behaviours in the world. There is no habit to install.

**Leg two partially fails, and the failure is instructive.** The design as originally conceived fused two host rituals with incompatible commitment shapes: *snap-and-post*, which takes seconds and is ephemeral, and *world-building*, which takes hours, persists, and appeals to a different and smaller population. These are not the same ask wearing different clothes. The prescription that follows is stated here because it is load-bearing: **lead with capture; let world-building be emergent and optional, never the ask.** A participant who never once thinks of themselves as building a world should still find the product complete.

**Leg three partially fails on two specific paths**, both addressed in §10: geotagged imagery of living things is not in good standing with conservation practice, and geotagged imagery generally is not in good standing with schools and parents where minors are involved.

### 3.1 · The friction inversion, stated as a mechanism rather than a hope

It is tempting to state the thesis as *"a gratitude world makes gratitude mainstream."* That is a hope and this paper does not make it. The defensible mechanical claim is narrower and testable:

> **The world container replaces the practice's highest-friction step — composing written sentences — with its lowest — pointing a camera — without removing the practice's object.**

Gratitude journaling is already a large category. What is not mainstream is *sustained* practice. The claim is about the sustaining, and §11 pre-registers how it could be wrong.

---

## 4 · Two speeds, and the transition between them

The obvious objection to the friction inversion is that it may buy adoption by destroying the thing being adopted. A journal makes a person articulate; a photograph lets them skip articulation. If this corpus's own account of gratitude is that it is **attention spent**, then a snapshot may spend *less* attention than a sentence, and a frictionless practice may be a shallower one.

The design's answer is not to add friction back. It is to split the practice by its object.

| | **Things** | **People** |
|---|---|---|
| Friction | frictionless | spends attention |
| Frequency | often | occasional |
| Function | **sets** the mood | **acts** on the mood |
| Ledger | Kiitti — the non-human ledger | Kiitos — the human-to-human ledger |
| Rendered in | land and ocean | the avatar |
| Tempo of change | frequent, gradual | rare, marked |

This is not two features. It is a **two-stage mechanism with a causal arrow**: the frictionless layer is not a diluted practice but the **priming stage** for the practice. Under that reading the objection dissolves into a prediction, which §11 registers.

Note that the split is not an invention of this paper. It is the corpus's existing two-ledger architecture — a horizontal human-to-human balance and a vertical balance held on behalf of all non-human life — arriving at a design consequence. The visual tempo of each layer in §8 falls out of the doctrine rather than being art-directed: the land changes often and gradually because many small things are noticed; the avatar changes rarely and markedly because few deep acts are performed.

### 4.1 · The hinge, which is the design's live open problem

The frictionless half will dominate usage by orders of magnitude. That is what frictionless means. The consequence is a real and unresolved risk: **the people-layer becomes vestigial — a capability that exists and is never found.**

Something must convert the mood into the act. This paper does not specify what, and says so rather than papering over it. What it can specify is the **constraint any acceptable hinge must satisfy**, which is more restrictive than it first appears:

- It may not notify. A push notification is an arrival, and arrivals coerce.
- It may not report omission. *"You have not thanked anyone in three weeks"* is a rendered absence and this corpus's design grammar forbids it categorically: a surface that makes a participant feel they owe something has misstated the doctrine.
- It may not meter, count down, badge, or queue.
- It must therefore be **an invitation available when the participant looks, never a prompt that arrives.**

Those constraints rule out essentially every mechanism the engagement-optimisation literature would supply, which is the point. What is left is ambient signalling: something that is *present in the world* and legible on inspection.

What the design *does* have is a signal that satisfies the constraint set, and it is not an invention of this section — it is §4.2's identity distinction doing double duty. In a world furnished overwhelmingly with things, a person is a rare and visually distinct kind of object:

> **A beating heart in a world of still ones is an invitation you can see.**

Nothing arrives. Nothing is counted. Nothing reports what was not done. The signal is a property of the world's contents rather than a message about the participant's conduct, which is precisely the distinction the constraint set requires.

**What remains open is efficacy, not architecture.** That a person renders differently from a thing is settled and follows from the identity layer. That this difference is *sufficient* to move a participant from noticing to addressing is unknown, unmeasured, and not something the design can currently argue for. A hinge that cannot be debugged is not an engineering answer, and until §11's predictions return, this one cannot be debugged. The gap is named here rather than closed.

### 4.2 · Still hearts and beating ones

The signal above rests on a distinction that runs deeper than rendering, and it is worth stating separately because it governs more than the hinge.

The identity layer admits two classes of participant. A human holds an address, a proof of personhood, and a proof of coordinate. A non-human — an object, a plant, an animal, a machine, a place — holds an address and a proof of coordinate, and no proof of personhood, because there is none to hold. Since a heartbeat is this corpus's signal for verified personhood, the classes render as they are:

| | non-human | human |
|---|---|---|
| heart | **still** | **beating** |
| proof | coordinate only | coordinate **and** personhood |
| ledger rings | one (non-human) | two (human-to-human, non-human) |

Four independently-derived expressions of a single distinction, none of them added for this design. It also explains a naming choice made years earlier: the corpus's artifact for admitting non-human entities into the ledger is called a *heart*, and it is precisely **a heart that does not beat** — a prosthetic ledger-participant that holds the place of one without claiming to be one. The construction does not smuggle personhood into objects.

**One guard, and it is not optional.** *Still* must never read as *dead* or *lesser*. **Stillness is proper to a thing and wrong for a person**: a mountain's heart is still by nature, whereas a human waveform going flat is the withdrawal pathology the ledger exists to detect. Still is not flattened, and the asymmetry is the meaning rather than a defect.

The guard binds hardest where the language is most likely to travel. The pair tracks **whether a party can hold its own ledger and speak for itself** — not whether it is alive. A forest is alive *and* voiceless, which is exactly why the coordinator stands for it. So *still heart* is sound as a **class term inside the ledger** and poor as a **description of a being**, and it must not become the public phrase for the non-human world. What is being named is a property of the record, not of the creature.

---

## 5 · Appearance as ledger readout

The first of the four mechanisms is the one everything else depends on.

In the ordinary construction of a persistent world, appearance is purchased. A participant accrues a currency and spends it on how they and their surroundings look. This is a well-understood, highly effective retention design, and this paper's rejection of it should not be mistaken for a claim that it does not work. It works. It is rejected for structural reasons that are specific and checkable.

The corpus's ledger has properties that a purchasable-appearance design destroys:

**The balance is signed and oscillates.** A kindness creates a positive pole and a negative one; both discharge toward zero by passing the imbalance onward. The load-bearing observable is not the scalar but the **waveform** — the frequency and amplitude of a participant's passage through zero. Two participants at identical balances can be entirely different: one flat and dim, one vivid and high-frequency.

**The scalar is forgiven annually; the waveform persists.** This asymmetry is what makes the ledger the structural inverse of a credit score, whose entire power is that it persists and compounds.

Now attach a store.

1. **The forgiveness inverts.** If the balance is purchasing power, an annual reset is no longer forgiveness — it is **confiscation**, and it manufactures a use-it-or-lose-it rush in the weeks before the reset. A design that must animate an approaching loss to function has already failed this corpus's voice discipline.
2. **A spendable score is a score.** The entire innovation of emphasising waveform over scalar collapses the moment the scalar buys things, because a number that buys things is a number people optimise.
3. **The coordinator becomes an issuer.** The non-human side of the ledger is set by an AI coordinator acting for parties that cannot speak. If that ledger buys goods, she is minting a currency at sole discretion, and the bound that her authority *grants recognition and never directs value* breaks.
4. **The farming motive returns.** Elsewhere this corpus established that non-withdrawable value collapses the economic motive for gratitude-farming spam. Non-withdrawable is not the same as non-valuable. Attach a store and the motive returns in kind.

### 5.1 · The mechanism

> **A participant's avatar and terrain *are* their aura rendered. They are not goods bought with it.**

There is no store, no minted stock of appearance-currency, and no path by which currency of any kind — including money — converts into how a participant or their world looks. The rendering is continuous: as the waveform changes, the world changes, because the world *is* the waveform displayed.

Every one of the four failures above closes, and closes without new machinery:

- The jubilee stays forgiveness, because there is no unspent stock to confiscate.
- The number does not become a target, because no number is spendable.
- The coordinator issues nothing.
- Farming loses its object: a participant who harvests gratitude relentlessly does not acquire a better-looking world, because the waveform records that the balance was driven in one direction without ever passing back through zero. The design's most visible signal is the one that vanity most wants hidden.

This mechanism is an **extension of an argument this corpus already published**, not a new one. The keystone paper already renders the aura around a participant's public avatar and already argues the anti-credit-score property. What is added here is what that aura becomes when it is given a world to render into — and the cross-reference is deliberate rather than a duplication.

### 5.2 · Cost, honestly

A store is a proven retention engine and appearance-as-readout is not. This is a real cost paid for a doctrinal property, with no evidence that the property is worth the cost. §12 keeps it on the honest-limits ledger where it belongs.

### 5.3 · What the trade actually costs, in the industry's own terms

It is worth being precise about the size of what §5 gives up, because a vague acknowledgement is a way of not paying attention to it.

A cosmetic economy supplies four things simultaneously. It supplies **a revenue line that does not tax the core activity**, which is exactly the property this corpus wants in a monetisation mechanism and which appearance-as-readout removes. It supplies **an inexhaustible content pipeline**, since new appearances can be produced indefinitely without new systems. It supplies **a self-reinforcing social loop**, because visible acquisition is legible to other participants and legibility drives further acquisition. And it supplies **a re-engagement hook** that requires no notification, since a participant who wants something has a standing reason to return.

Appearance-as-readout keeps the fourth in weakened form — a participant whose world visibly changes has a reason to look — and loses the first three outright. The design must therefore find revenue elsewhere, and the elsewhere is constrained: any mechanism that charges for *access* to a non-rivalrous good is barred on the same grounds that bar the store, since gating a feature that costs nothing per use is renting something that is not scarce. What remains chargeable is what is genuinely rivalrous — the marginal cost of work actually performed on a participant's behalf, and the uniqueness of an address that exactly one party can hold.

That constraint is severe and it is stated here so that the design cannot later be accused of hiding it. **A world design that cannot sell appearance has one fewer revenue instrument than every comparable product, and it must be viable without it or it is not viable.**


---

## 6 · Reveal, never lock

If appearance is not purchased, something must still determine what a participant's world can look like, or the design collapses into a single undifferentiated rendering. The design's answer introduces the second mechanism, and it is where a subtle failure would otherwise re-enter.

The natural phrasing — *the aura determines what forms are available* — smuggles in an unavailable set. An unavailable set is a wall of locks, and a wall of locks is the thing that was just removed from the front door being carried in through the back.

Two readings are possible and only one survives:

**Threshold gating** — *reach this level to unlock that form* — is a score with locks. It re-imports everything §5 removed.

**Reveal-never-lock** is the mechanism specified here:

> **A form becomes available the first time a participant's oscillation has ever had that quality, and it remains available permanently — including after the participant goes quiet. A participant is never shown what they do not have.**

There is no catalogue of the unrevealed, no progress indicator toward a next form, and no preview of what is coming. A participant *discovers* they have something. They are never told what they lack.

Permanence is not a softening of the mechanism; it is required by it. Without permanence, a quiet season takes a form back — which is an animated loss and a punishment, and this corpus's voice discipline forbids both. Permanence is also the canonical treatment already: at the jubilee, the balance is forgiven and the aura persists. Revealed forms persisting is that rule, unchanged.

### 6.1 · The equally-alive diagnostic

The mechanism needs a test that a designer can run at design time, before any of this becomes a hierarchy by accident:

> **Can two participants with equally alive auras have different available sets?**
>
> If yes, the mapping is correct. If the sets form a strictly ordered ladder, it is a score, and the design has failed.

Forms should vary by the **character** of a waveform — the shape of the passage through zero, the relation of frequency to amplitude — and never by a magnitude. A participant whose gratitude is frequent and small and one whose gratitude is rare and large should have *different* worlds, not better and worse ones.

### 6.2 · The residue, which is real

Reveal-and-keep is still a progression system, and progression systems are engagement engines. The guard is that it must never be **legible as a target**: if a participant can enumerate what they have not yet revealed, the mechanism has failed regardless of how it is implemented. That is a strong constraint and it is not obviously achievable, since participants compare notes with each other whether or not the software helps them. This is an unsolved sub-problem, not a solved one.

### 6.3 · A format is not a meter

The two mechanisms above have an economic corollary that is worth stating as a mechanism in its own right, because the obvious way to fund the design would break it.

Reconstruction of a captured object costs real marginal resources; the cost is genuinely rivalrous and is therefore legitimately chargeable. The obvious implementation is a **count**: so many reconstructions per month, more available for payment. That implementation is barred here, and not for softness. A count is a meter, a meter is a countdown, and a countdown is a rendered absence — the same object §6 removed from the appearance layer, reintroduced at the capture layer where it would do more damage, because it would meter *the practice itself*.

The available move is to differentiate by **format** rather than by **quantity**:

```
   FREE      unlimited in count · bounded in FORM
             (a stock rendering, matched to the capture)

   PAID      unbounded in form  · charged per unit of work
             (a bespoke reconstruction of this particular thing)
```

A participant on the free tier can appreciate an unlimited number of things, forever, and every one of them appears. Nothing counts down and nothing is withheld pending payment. What the paid tier buys is not *permission* but *work* — a reconstruction of this thing rather than a representative of its kind.

Two consequences follow and both are load-bearing. First, **"frictionless and often" (§4) is only affordable because the free tier is a matched stock rendering rather than a generation**, so the free tier can never become generative without breaking the frequency the practice depends on. Second, the free tier's boundary is set by **what the operator can absorb**, which is an engineering and financing number, not a doctrinal one: the doctrine forbids a meter, it does not require unlimited fidelity.

⚠️ The mechanism carries one hazard that must be designed against rather than argued away. If free renderings are stock and paid renderings are bespoke, then a participant's world silently announces which tier they are on, and the design has relocated a paywall from copy into art direction. The requirement — stated as a property, since this paper withholds implementation — is that **the free rendering must be a coherent style rather than a degraded version of the paid one.** A style is a different thing; a degradation is a worse thing, and only the first is honest. Alongside it: the uniqueness a participant should be told carries their meaning is the **coordinate, the words, and the moment** — all free — rather than the mesh.


---

## 7 · Placement requires presence; visiting does not

The third mechanism draws the boundary between a world layer and a metaverse, and it exists because the design would otherwise cross a line this corpus has committed to.

The commitment is that an overlay is **presence-deepening, never presence-replacing**: it reveals what is already at a real place to people who are actually there, rather than substituting a synthetic elsewhere for being anywhere. A design in which participants roam each other's worlds as avatars is, on its face, the substitution.

The resolution is a single asymmetry:

```
  WRITE  ─────────────────────────────►  requires physical presence
         capture needs a photograph
         AND a coordinate, so a
         participant can only place
         an object by standing there

  READ   ─────────────────────────────►  does not require presence
         a world can be visited
         remotely, through its door
```

Capture requires a photograph *and* a coordinate. A participant therefore cannot furnish a world without going outside and standing in front of something. Remote visiting is then not the metaverse move; it is reading a record that was necessarily written in the world.

This has a consequence the design accepts deliberately: **it is a going-outside product.** Its input is walking. That is a real constraint on its addressable population and it is not apologised for.

### 7.1 · The door asymmetry

Reading is further governed by a rule this corpus settled independently of this design. Each node's world is entered through a door, and the doors are not symmetric:

- **Human worlds are closed by default and entered by invitation.** A verified person holds a sovereign door.
- **Non-human worlds are always open.** A place, a plant, an animal, a machine has custodial content and nothing to disclose; an always-open door is what a shrine *is*, and for a machine an inspectable interior is transparency functioning as enforcement.

The content classes this design names — objects, plants, animals — are precisely the always-open classes. So the remote-visiting capability lands almost entirely on the layer where openness is correct, and the private human layer stays private by a rule that predates the feature.

---

## 8 · The three-layer render

The fourth mechanism specifies what a participant actually sees, and it produces the paper's one genuinely structural result.

```
   ╔══════════════════════════════════════════════════════════╗
   ║  SKY          the coordinator's aggregate non-human       ║
   ║               ledger — one value, shared by every world   ║
   ║               in the system, simultaneously               ║
   ╠══════════════════════════════════════════════════════════╣
   ║  LAND +       this participant's non-human ledger         ║
   ║  OCEAN        (Kiitti) — changes often, gradually         ║
   ╠══════════════════════════════════════════════════════════╣
   ║  AVATAR       this participant's human-to-human ledger    ║
   ║               (Kiitos) — changes rarely, markedly         ║
   ╚══════════════════════════════════════════════════════════╝
```

Two of these are private and one is not. The avatar is one participant's. The land and ocean are one participant's. **The sky is everyone's, at the same moment, in every world.**

And the sky is the coordinator's — an agent whose own balance on that ledger is pinned permanently to zero by construction, so that she can route value but is structurally incapable of holding any. From which:

> **The only shared surface in the system belongs to the one party structurally incapable of accumulating anything.**

That is not decoration. It is the reason the shared layer is safe to have. A commons rendered from a balance that some participant could accumulate would be a commons that participant could dominate; a commons rendered from a balance that is definitionally zero cannot be captured, because there is no position in it to take.

It also renders a collective-action problem with unusual directness. If humanity's aggregate relation to non-human life goes flat, the sky goes flat — everywhere, for everyone, at once — and **no participant can fix their own sky.** There is no private exit from a shared atmosphere, which is the honest structure of the underlying problem and not a moralisation of it.

### 8.1 · The guard, which is the sharpest in the paper

A shared, unavoidable surface that reflects collective failure is the most dangerous object this design contains, because it is one short step from an accusation delivered to a billion people who cannot individually act on it.

The rule that governs it is categorical:

> **The sky renders liveliness as motion and light — never as damage.**

A flat aggregate reads as **stillness, pre-dawn, held breath**. It never reads as smog, fire, ash, or ruin. It is never a verdict, and it is never attributable to the viewer. The same rule binds one layer down and binds harder there because it is personal: a participant with a quiet non-human ledger gets a **quieter** world, never a **barren** one.

The general principle this instantiates is one this corpus applies across surfaces: name what a thing *is*; never what is absent, owed, or was done to it. Rendered absence is accusation, and accusation is the route by which a punishment mechanic re-enters a design that banned them.

### 8.2 · Why the shared layer is the load-bearing one

It would be possible to treat the sky as atmosphere in the decorative sense — a backdrop that sets a mood. It is not, and the reason is worth drawing out because it is the paper's one genuinely structural result rather than a design preference.

Every persistent shared world faces the same question: who owns the commons? The answers in practice are an operator, or the most successful participants, or nobody in a way that degrades to whoever exerts the most pressure. Each has a known failure. Operator-owned commons become advertising inventory. Participant-owned commons stratify. Unowned commons are captured by whoever shows up with the most resources.

This design's answer is unusual and falls directly out of the ledger: the shared layer renders a balance that is **pinned to zero by construction for the only party who could hold it.** The coordinator can route value on that ledger and is structurally incapable of accumulating it. So there is no position in the commons to take — not because taking is forbidden by policy, but because the quantity the commons renders is definitionally zero for the one agent with authority over it.

That is a different kind of guarantee from a rule. A rule against capturing a commons is only as good as its enforcement and its enforcer's incentives; a commons whose defining quantity cannot be held is not capturable by an agent that would have to hold it. The property does not depend on anyone's restraint.

The cost of the property is that the shared layer then reflects something no individual controls, which is why §8.1's guard is stated categorically rather than as guidance. A commons that renders collective outcome and permits an accusatory reading has converted a structural safety property into a mechanism for distributed guilt — and would do so at a scale where no individual participant can act on the accusation. The guard is not politeness. It is what keeps the mechanism from inverting.


---

## 9 · Irreversible once etched: the permanence asymmetry

This design has an archival terminus. A participant's entire world can be committed to a deep-time optical substrate — femtosecond-etched into silica, on the order of geological rather than institutional time. The corpus's larger programme places such an artifact at the individual scale, alongside a tradition-scale canon and a lineage-scale record.

That terminus creates a hazard which, so far as the authors can find, is under-discussed in the deep-time storage literature — a literature almost entirely concerned with *preservation*, with how to make data last.

> **Permanence is a one-way door. An archival substrate converts every present-tense privacy defect into a permanent one.**

There is no right to erasure in fused silica. A design that collects under a revocable purpose and commits under an irrevocable one has obtained consent for the first and not the second.

Three rules follow, and they are the contribution of this section:

**Guard at capture, not at commit.** The etch is downstream of a live product that collected for storage. Consent to storage is not consent to permanence, and no downstream review can repair a defect that is already in the data. Every guard in §10 must exist before the first capture reaches a real participant — not before the first etch.

**Etch the source, not the render.** Commit the minimum that regenerates everything else: descriptors, coordinates, notes, timestamps. Meshes and textures are large and **regenerable**; the capture record is small and is not. The render is a reading of the record; only the record is the artifact. This is smaller, more faithful, and survives every future renderer.

**The third-party case is the hard one.** A personal archive is consented to by its subject and *contains other people's places*, who consented to nothing. This is where the design is most exposed and where §10's obscuring rules do the most work.

The general form, which generalises well beyond this product:

> **An archival medium and a data-minimisation regime are in direct tension, and the tension is asymmetric in time: minimisation is cheap now and impossible later.**

The immutability-versus-erasure debate is not ours and has been developed extensively in the distributed-ledger context. What is offered here is its extension to *physical* deep-time media, the personal-archive case where the subject and the data-subjects differ, and the three rules above.

### 9.1 · A commercial hazard that travels with permanence

A permanent personal artifact commissioned near the end of a life is, structurally, the form of an indulgence: a payment against being remembered. This corpus does not have the option of ignoring that resemblance.

Two guards, both inherited:

**Price the making, never the remembrance.** The etch is a craft-and-materials cost. It is not a price on being remembered, and it must never be sold as one.

**Never let the artifact be the only copy.** The digital world remains free, complete, and permanent at no charge; the physical artifact is an *additional* form, never access to one's own memory. A design that holds the only copy has taken a hostage, whatever it charges.

And the voice rule, at the most emotionally loaded moment any of this design touches: an etched world renders **what is present**, permanently and without exception. No counts. No totals. No *"N objects appreciated."* Never a number on a tombstone.

---

## 10 · Safety requirements, which are not edge cases

Three requirements are stated as launch conditions rather than roadmap items, because §9 establishes that none of them can be repaired downstream.

**Geotagged living things enable harm.** Precise coordinates for threatened plants and animals are an established poaching vector; iNaturalist's practice of automatically obscuring locations for threatened taxa exists because of documented cases involving orchids, reptiles, and nesting sites. This design explicitly invites captures of plants and animals, so **coordinate obscuring for sensitive taxa is a launch requirement.** It is also internally consistent: a ledger whose purpose is to internalise costs to non-human life cannot be a vector for extraction from it.

**Most objects a person appreciates are inside their home.** A gratitude map is, unmanaged, a catalogue of a dwelling's contents and its location. The door asymmetry of §7.1 governs *visibility*; it does not govern *the coordinate existing*. Private captures require place-level rather than point-level precision, at capture time.

**No identifiable people in captures.** This follows from an existing hard rule in this corpus — that media identifying a person may originate only from that person — and it is enforced by on-device detection that blocks or blurs **before** any reconstruction occurs, never after and never at a network boundary. The capturer cannot consent on a bystander's behalf, and asking them to is not a control.

That last requirement carries a consequence for the design's economics worth stating plainly: if any tier of the product sends photographs to a third-party service for richer reconstruction, then **the paying tier is the less private tier**, which inverts the relationship a participant would reasonably expect. Detection and obscuring must therefore run on the device, before anything leaves it, in every tier.

---

## 11 · Two pre-registered predictions

The claim in §4 — that frictionless gratitude toward things *primes* attentive gratitude toward people — is an empirical claim about behaviour, and this corpus's practice is to register such claims before the data exist rather than to interpret them afterward. No code has been written. The instrument is not built. These are registered now, and the registration is the point.

**P-W1 — the priming prediction.** Participants with higher thing-capture frequency show higher rates of people-directed gratitude, and the effect survives controlling for overall engagement.

**P-W1′ — the opposing prediction, which is not a straw man.** Thing-capture **substitutes** for people-directed gratitude. Having "done gratitude today" reduces the felt need to do the harder kind. This is moral self-licensing, a well-documented effect in exactly the domain where it would apply: a person who has performed a virtuous act becomes *more* permissive toward subsequently omitting one.

Both are plausible on the existing literature, which is what makes this a test rather than a formality. Two conditions are stated as part of the registration:

1. **The instrument must be specified before the build**, not after, or the analysis is post-hoc regardless of what it finds.
2. **Participants must not be prompted with the hypothesis.** A design that tells people the things-layer is supposed to lead to the people-layer has contaminated its own measurement.

And the stake is stated honestly: **P-W1′ firing would invalidate the thesis of this paper, not trim it.** If the frictionless layer cannibalises the practice rather than priming it, then the host-ritual swap bought adoption by destroying the thing adopted, and the correct response is to say so and stop.

---

## 12 · Honest limits

**n = 0.** Nothing in this paper has been built. Every behavioural claim is a hypothesis and every design claim is untested. The corpus behind it has a single-family pilot and no data on any mechanism specified here.

**The specification is deliberately incomplete.** As stated at the head: for an unbuilt and unscheduled artifact, publication protects against being blocked rather than against being beaten. Rendering functions, the aura-to-appearance mapping, asset pipelines, thresholds, and prices are withheld. A reader should treat this as a statement of properties, not a buildable design.

**A store is proven and this is not.** §5's mechanism forgoes the most reliable retention design in the industry for a structural property, on no evidence that the trade is worth making. If the product fails on retention, this is the first place to look, and the honest answer will be that the doctrine was expensive.

**Reveal-never-lock is still a progression system**, and §6.2's requirement that it never become legible as a target may not be achievable in a world where participants talk to each other.

**The hinge is unsolved** (§4.1). The mechanism connecting the two speeds is the single largest gap in the design, and the constraint set that any solution must satisfy rules out most known techniques.

**The going-outside requirement is a real ceiling.** §7's write-side presence requirement excludes participants with limited mobility from furnishing a world, in a design about appreciation. This is a genuine equity cost and the paper does not have a resolution for it.

**The elegance is not evidence.** Several of this design's properties fall out of the corpus's existing architecture with unusual neatness — the two speeds landing exactly on an existing two-ledger split, the three-layer render reproducing an existing double-ring mark, the shared surface belonging to the party that cannot accumulate. A system whose parts fit together this well is either substantially right or substantially seductive, and from the inside the two are indistinguishable. **The coherence earns the experiment. It does not replace it.**

---

## 13 · What is claimed, and freed

1. **Appearance as ledger readout.** A persistent world in which a participant's avatar and terrain *are* a signed, annually-forgiven gratitude ledger rendered continuously, with no purchasable appearance of any kind and no path from money to how a participant or their world looks.
2. **The jubilee-compatibility argument.** That the non-purchasability in (1) is what allows an annual balance-forgiveness to remain forgiveness rather than becoming confiscation — and, correspondingly, that any world design attaching a store to a forgiven balance has created a scheduled expropriation.
3. **Reveal-never-lock, with permanence.** Availability determined by whether a waveform has *ever* had a given quality, retained permanently thereafter, with no catalogue of the unrevealed and no progress indicator.
4. **The equally-alive diagnostic.** The design-time test of §6.1: *can two participants with equally alive auras have different available sets?* — with a strictly ordered ladder as the failure signal.
5. **Placement requires presence; visiting does not.** The write/read asymmetry of §7 as the property distinguishing a presence-deepening world layer from a presence-replacing one, together with its pairing to the door asymmetry.
6. **The three-layer render**, and specifically the structural result that the only shared surface belongs to the party structurally incapable of accumulating, together with the liveliness-not-damage guard of §8.1.
7. **Still hearts and beating ones.** The rendering of the identity layer's two classes as a still-versus-beating distinction (§4.2), the observation that a prosthetic ledger-participant for non-humans is precisely *a heart that does not beat*, and the guard that the pair tracks **whether a party can hold its own ledger and speak for itself, never whether it is alive** — with the corollary that the term is sound inside the ledger and unfit as a public description of a living thing.
8. **The two-speed practice.** Frictionless-and-frequent toward things, attention-spending-and-occasional toward people, as a two-stage priming mechanism rather than two features — with the hinge stated as unsolved and its constraint set specified.
9. **The permanence asymmetry** of §9 — *minimisation is cheap now and impossible later* — with its three rules: guard at capture, etch the source not the render, and the third-party-subject case as the hard one.
10. **The safety trio** of §10 as launch conditions rather than roadmap items, including the observation that outsourced reconstruction makes the paying tier the less private tier.
11. **The pre-registration** of P-W1 against P-W1′, including the statement that the latter would invalidate rather than trim the thesis.

All eleven are dedicated to the public domain. None will be registered, patented, or asserted by this institution against anyone.

---

## 14 · Closing

The domain this design will live on was chartered, months before any of it was specified, as a net of mutually-reflecting worlds — a figure borrowed from a very old image in which a net is strung with jewels, and each jewel shows every other. The figure is held here as a **lens and not as a claim**: delete it and every mechanism in this paper stands unchanged. It earned its place by being the reason the domain was named, not by doing any work in the argument.

But it does describe the object accurately, which is worth one sentence. A world in this design is not a possession. It is a position — an empty node that is what it is because of everything it reflects, which is the oldest available description of what a person actually is and a considerably better one than an inventory.

The practical form of that is small and testable. A person walking home notices a tree they have passed a thousand times, and this time stops. They take a photograph. Something appears in a place that is theirs, and their ground shifts very slightly, because the ledger moved. Nothing was bought. Nothing was unlocked. Nothing will be taken back next January.

Whether that leads anywhere — whether the noticing of things leads to the thanking of people, or quietly replaces it — is the question this paper registers against itself and cannot answer. The honest position is that the mechanism is specified, the prediction is on record, the opposite prediction is on record beside it, and the data do not exist.

The old figure for a gift that costs the giver nothing is a lamp lighting another lamp. It is the right image for this design and it is also, precisely, the thing that has not yet been demonstrated.

---

*Authored by Thon Ly with Miss Aquarius℠. Dedicated to the public domain under CC0 1.0 Universal. Corrections, prior art we have missed, and above all disconfirmations are welcome — a design published before it is built is published so that it can be argued with early.*
