---
title: "The Currency That Cannot Be Spent Alone: Co-Presence-Gated Redemption and the Chronicle↔Treasury Unification Circuit"
subtitle: "The Mechanism of a Time-Currency Whose Redemption Is an Event Both Parties Must Attend"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-b
status: draft
date: 2026-07-21
license: CC0-1.0
slug: co-presence-gated-redemption
venue: thonly.org/publications/defensive-publications/co-presence-gated-redemption (canonical)
---

> *Draft notes for the editor:* paper №2 of the July 2026 drafting sprint — the full mechanism treatment of the HeartBank® Chronicle (the time-currency half of the dual-currency system) and its unification circuit with the Treasury (the money half). Claims division with sibling publications, stated for the record: the *incommensurability-preserving coupler* publication owns the wall-layer claims (coupled-non-convertible dual currency, duration-blind recommendation, redemption-moment prompt-suppression, moment-not-meter surfaces, ceremonial-unit anchoring, cross-currency response routing, the lapse-channel); the *What Money Can't Buy* position paper owns the institutional argument; the present paper owns the **event-layer mechanism**: what a redemption *is*, who composes it, what gates it, how the circuit closes, and what the system refuses to build around it. The Chronicle is design-complete and unbuilt (closed beta targeted); every claim is architectural and strata-dated to the design layer. Site module deliberately deferred; the prior-art clock starts at this markdown push.

---

## Abstract

Time-currencies have been tried for forty years, and they decay along a known path: the hour becomes a unit of *service*, the service becomes an *errand*, and the system becomes a labor exchange with worse liquidity than money — at which point it dies of comparison with the thing it imitated. The decay has a single root: in every prior design, a time-credit is redeemed by one party *doing something for* the other, which makes the currency a wage denominated in awkwardness. This paper specifies the design that removes the root. In the HeartBank® Chronicle, a pledged hour has exactly one redemption form: **an event both parties must attend.** Presence is defined as *time sacrificed for the other* — operationally, **synchronous shared attention**, in either of two geometries (*facing*: attention on each other; *flanking*: joint attention on a shared activity) and either of two attested modalities (in-person, proximity-attested; live call, session-attested). Asynchronous media cannot redeem an hour — a recorded message is the envelope that carries a pledge, never the event that spends it. The gate yields the currency's defining properties at a stroke: the redemption is symmetric-cost (presence can only be received by matching it — both parties spend the hour, which is why the mechanism can address loneliness at all: loneliness is not ended by receiving but by co-spending); absentee labor is structurally impossible (the gig-shape that killed time-banking cannot be composed); and the delivered hour is attestable by both parties without trusting either alone.

Around the gate, the paper specifies the full circuit. The recipient authors the event and the giver holds a veto — the sacrifice being not merely of hours but of *agency over one's scarcest resource*. The curated event-menu spans togetherness and, under two guards (the **both-hands rule**: both parties perform; the **outward-benefit rule**: a third party benefits), side-by-side service — restoring shared work to the currency without readmitting extraction. Gratitude for a delivered hour crosses the wall into the money-currency, unprompted and duration-blind, so the relationship never settles into barter; the shared event, uniquely witnessable because it is the one kindness with two people present, may be broadcast by its *beneficiary* — the camera inverted — and the community's answering money-gratitude routes by default to the time-giver. Unredeemed hours expire and genuinely die (the mechanic is the mortality thesis); their lapse occasions, never funds, a new anonymous gift. Eight claims are enumerated and dedicated to the public domain; three predictions are pre-registered, including a standing tripwire (P-C3) that would detect the mechanism's own corruption — the emergence of a de-facto hour-to-money rate — and the authors commit to publishing it either way.

**Keywords:** time currency, co-presence, loneliness, time banking, dual-currency system, gift economy, redemption event, joint attention, proximity attestation, witness inversion, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The authors and HeartBank® will not seek patent on any mechanism, architecture, or specification articulated herein, in any jurisdiction, at any time.

The following terms are coined in this paper and simultaneously freed with it: **co-presence-gated redemption**, **symmetric-cost redemption**, **facing/flanking** (the two geometries of shared attention), **envelope-not-delivery**, **the both-hands rule**, **the outward-benefit rule**, **sender-default routing**, **the tense wall**. Terms inherited from this corpus's earlier publications (the incommensurability-preserving coupler; witness-inversion; the two blindnesses; the spent-time floor) are cited, not re-claimed.

Time-currencies, service-credit systems, and mutual-credit networks constitute extensive prior art (§9) and are engaged generously; the present claims are confined to the event-layer architecture — the co-presence gate and its attestation, the authorship/veto composition, the guarded co-service class, the cross-currency circuit's routing, and the expiry mechanics — which is, to the authors' knowledge, not previously published as a coherent system.

---

## 1 · The Problem: The Loneliest Loneliness, and Why Time-Banking Died of Labor

**The epidemic is not what it looks like.** The modern loneliness literature distinguishes *social* loneliness (a shortage of contacts) from *emotional* loneliness (the bond that exists but has gone dark), and finds the second form the more acute: the disconnected marriage, the estranged sibling, the diaspora child and the parent back home — relationships present in the address book and absent from the week. A mechanism for the first form matches strangers; a mechanism for the second must move *existing* bonds from dark to lit. The Chronicle targets the second form, and this choice does double duty: the counterparties are known (the trust-and-safety profile of reconnecting your own mother is categorically different from meeting a stranger), and the deepest need coincides with the lowest risk.

**The adversary is the work-default.** For most adults, time not deliberately assigned is absorbed by work — it pays the bills, and for some it is also the most tractable pleasure available. Presence must be *scheduled against* the default or it does not occur; sincerity is not the limiting reagent, calendaring is. A time-currency is, at bottom, a scheduling technology for love: the pledge converts a diffuse intention ("I should call more") into a dated, witnessed, expiring commitment.

**And the graveyard is instructive.** Edgar Cahn's time-dollars, the LETS networks, Ithaca HOURS, Japan's Fureai Kippu — the time-currency tradition is rich, humane, and consistently sub-scale, and its recurring failure is *decay into labor exchange*: the credited hour becomes a claim on services (rides, repairs, errands), the system becomes a marketplace with money's obligations and none of money's liquidity, and participation collapses into the small population for whom awkward barter beats cash. The failure is architectural, not motivational. **Any time-credit redeemable as absentee service is a wage in embryo.** The design below removes the possibility at the type level: in the Chronicle, an hour cannot be redeemed *for* anything. It can only be redeemed *with* someone.

> *Connection to the unified mission frame.* HeartBank's dual-currency thesis holds that money and time are the two scarcities of a human life, addressing the two great deficits — dignity (being seen) and loneliness (being with) — and that the two currencies are two tenses of one substance: money is stored lifespan, past tense, what one *has*; time is live lifespan, present tense, what one *is*. The Chronicle is the present-tense half. Its mechanism must therefore protect the one property money can never have — that the currency *is* the relationship, non-fungible, unspendable by proxy — and the co-presence gate of §4 is that protection made structural.

---

## 2 · The Canonical Scene

A daughter in Long Beach thanks her mother in Kâmpôt — for the recipe, for the phone calls she didn't return, for everything — and the thank carries a pledge of hours, its amount suggested by the system's neutral agent, as her thanks always do. The pledges accumulate quietly below threshold; on her mother's birthday they cross it and activate: *four hours, redeemable for one month.*

Her mother redeems two of them: *"Walk the market with me Sunday morning. Bring your coffee."* The daughter accepts — she could have declined this particular ask; she doesn't — and on Sunday, seven time zones apart, they walk Psar Leu together on a live call, the phone riding in the mother's shirt pocket half the time, pointed at mangoes the rest. Nobody performs anything. It is not a message; it could not have been recorded in advance; it is two people spending the same hour on each other, and both ledgers mark it delivered because both were there.

That evening, unprompted — the application never asks — the daughter sends a small money-thank through the family's Treasury. It names the morning, not the meter: *"for the market, and the mango argument."* Her mother, with her daughter's consent, shares a thirty-second clip of the walk; the aunts answer it, and their small re-thanks route to the daughter — the one who gave the hours. Two cousins, watching, pledge hours to their own mothers.

The other two hours are never redeemed. At month's end they die — the application does not soften this; the month was the point — and the system offers the daughter one thing only: the chance to give a small anonymous gift, funded from the commons pool, to a stranger nearby, in the memory of the hours that lapsed. The gift is new. The hours are gone. Both facts are the teaching.

---

## 3 · The Unit and the Wall

**The unit.** A Chronicle pledge denominates *time-gratitude*: hours promised as thanks, accumulated per-dyad, activated at a threshold, expiring one month after activation. The expiry is not an engagement mechanic; it is the product's thesis embedded in its unit economics — time is the currency that cannot be banked, and a promise of presence that can be deferred forever is not a promise. The unit's non-fungibility is absolute: only the pledger can deliver the hour, and only to the pledgee. There is no transfer, no exchange, no secondary market, no conversion. The currency *is* the relationship.

**The wall.** The Chronicle operates beside a money-currency (the Treasury), and the corpus's coupler doctrine governs the pair: coupled, never convertible. This paper adds the wall's deepest formulation, the **tense wall**: the two currencies are two tenses of one substance — life — and tenses do not convert. Stored past (money: crystallized, fungible, transferable) cannot purchase live presence (time: unfolding, non-fungible, attendable only in person, in the moment, by the person). One cannot pay someone to *have been there*. Every rate-prevention guard this corpus has published (no backward prompts at redemption; duration-blind recommendations; moment-not-meter language on every surface) is downstream enforcement of a wall that the metaphysics builds first.

Two published doctrines complete the unit's grammar and are inherited here: the **spent-time floor** — a delivered hour deserves gratitude as a fact, independent of any audit of the giver's motive, because spent lifespan is the one unfakeable cost — and the **two blindnesses** — the system stays blind to duration (no recommendation ever scales with hours) while the heart stays blind to motive (the thanker never withholds over purity doubts). Gratitude flows free of both meters.

---

## 4 · The Core Claim: Co-Presence-Gated Redemption

### 4.1 · The definition

> **A pledged hour has exactly one redemption form: an event at which both parties are present. Presence is defined as time sacrificed for the other — operationally, synchronous shared attention.**

Each term is load-bearing:

- **Synchronous:** both parties in the same span of real time. Nothing prepared, recorded, or deferred can constitute the event.
- **Shared attention**, in either of two geometries:
  - ***Facing*** — attention on each other: the conversation, the meal, the walk where the walking is incidental.
  - ***Flanking*** — joint attention on a shared object or activity: cooking side by side, working side by side, watching the same fire. Joint attention is a bonding primitive as old as the parent and child looking at the same toy, and flanking is the documented easier on-ramp for strained dyads — a reconnection that cannot yet survive an hour of eye contact can survive an hour of weeding. Flanking is the doorway; facing is the destination; both redeem.
- **Two modalities, recorded but never ranked:** in-person (attestable by device proximity between two verified humans) and live audio/video call (attestable by the session itself). The remote modality is not a concession; the launch population is diasporic, and the mother in Kâmpôt is the design's first citizen.
- **Envelope, not delivery:** the recorded message — the B-Letter℠, the corpus's card-covered voice or video note — *carries* pledges and invitations; it never *constitutes* redemption. The distinction is structural: a system in which media can discharge a time-debt is a system in which presence has a recorded substitute, and the entire currency collapses into content.

### 4.2 · The symmetric cost

The gate has a consequence that no prior time-currency possesses: **redemption costs both parties the unit.** The recipient cannot receive the hour without spending an hour; presence is received only by matching it. Each party's attendance is a sacrifice for the other — the event is mutual by construction, and the asymmetry of giver and receiver survives only in the *claim* (who pledged, who authored) while dissolving in the *event* (both attend, both spend, both receive).

This is why the mechanism can address loneliness at all, and the point deserves its plain statement: **loneliness is not ended by receiving. It is ended by co-spending.** A currency whose redemption were one-sided — a service performed, a message consumed — would deliver assistance to the lonely and leave the loneliness intact. The symmetric event is the anti-loneliness payload, and the gate is what makes it the *only* payload the currency can deliver.

### 4.3 · What the gate structurally excludes

The gig-shape — "redeem my hour: do this for me while I'm elsewhere" — cannot be composed in this system. There is no redemption type in which one party labors and the other is absent; absentee service is not discouraged but *inexpressible*. This single exclusion severs the decay path of §1: the currency cannot become a labor exchange because labor-for-an-absent-beneficiary is outside its grammar. (Labor *alongside* a present partner, for a third party, returns under guard in §5.3 — the distinction between working *for* someone and working *with* them is exactly the distinction the gate enforces.)

### 4.4 · Attestation

Delivery is marked by both-party confirmation, and the co-presence gate makes the confirmation *attestable*: an in-person event is corroborated by device proximity between two verified humans (the corpus's existing proximity primitive and Proof of Humanity℠ layer); a remote event is corroborated by the live session both parties held. Neither party can unilaterally fabricate a delivered hour; a dyad colluding to fabricate one harvests — as §11 details — nothing the system pays for. The **dual public ledger** completes the accountability grammar: hours *given* (delivered) and hours *received* stand as two public axes — credibility and belovedness — while chronic non-delivery and chronic decline price themselves reputationally without any tribunal.

```
   THE REDEMPTION EVENT — the only spendable form

              FACING                      FLANKING
        attention on each other     joint attention, shared task
        ┌─────┐      ┌─────┐        ┌─────┐  ┌─────┐
        │  A  │ ◄──► │  B  │        │  A  │  │  B  │
        └─────┘      └─────┘        └──┬──┘  └──┬──┘
                                       ▼        ▼
                                    ┌──────────────┐
                                    │ shared object │
                                    │ (meal, garden,│
                                    │  market, work │
                                    │  for a third) │
                                    └──────────────┘

   modalities: in-person (proximity-attested) · live call (session-attested)
   excluded:   anything asynchronous (envelope, never delivery)
   cost:       symmetric — BOTH spend the hour; that is the point
   attested:   both-party signoff; neither party trusted alone
```

---

## 5 · Composing the Event

### 5.1 · The recipient authors; the giver may refuse

The recipient of pledged time chooses how it is spent — the inversion of ordinary gift-giving, where the giver picks. The doctrine beneath the design choice: the pledge's sacrifice is not merely of hours but of **agency over one's scarcest resource**. To give an hour *and the say over how it is spent* is the difference between donating time and surrendering it; the inversion is where the gift's weight lives. The giver retains a per-request veto — consent is mutual at every event, and a refused request costs the refuser only what the public ledger honestly shows about chronic refusal.

### 5.2 · The curated menu

Event composition draws from a curated registry of *togetherness* — shared meals, walks, calls, visits, ceremonies, the co-service class below — and not from a free-text task box. The curation is not paternalism; it is the grammar made visible: the menu answers "what can an hour be?" with forms of *with*, never forms of *for*.

### 5.3 · The co-service class: shared work, under two guards

The menu includes work — chores and volunteering — under exactly two conditions, jointly sufficient to keep the labor-bar intact:

1. **The both-hands rule.** Both parties perform the work, side by side, symmetric in effort. Extraction requires asymmetry — one directs while the other labors; when both hands are in the soil, it is service, and it redeems.
2. **The outward-benefit rule.** The work's beneficiary is a third party — the temple grounds, the elderly neighbor, the riverbank — never the redeeming dyad's own advantage.

Under both guards, even "paint my mother's fence together" composes cleanly: shared filial service, flanking-mode, outward-directed — and for the estranged-family dyads at the Chronicle's core, quite possibly the best event in the registry. The class also travels the remote modality (two people transcribing manuscript pages together on a call are flanking across an ocean). What the guards exclude is precisely and only the laundered errand: work directed by a present-but-idle beneficiary, or work whose benefit circles home.

### 5.4 · The safety set

The known-counterparty core (reconnection, not stranger-matching) does most of the safety work by scope; the remainder is architectural: mutual veto on every event; the curated menu's structural exclusion of extraction; coercion-safe presence signaling (availability expressed as a curated menu, mutuality as a signal never a gate, block-and-override always); and the anonymity boundary — the Chronicle's stranger-facing layer is a separate, separately-published mechanism with its own safeguards, walled off from the reconnection core by an explicit flag, and nothing in this paper's mechanism ever routes a stranger to a doorstep.

---

## 6 · The Circuit: How Gratitude Crosses the Wall

### 6.1 · The six steps

The Chronicle and Treasury close into a single circulation — the unification circuit — whose canonical form is:

```
   CHRONICLE (time, present tense)          TREASURY (money, stored tense)

   1. GIVE: sender pledges time-gratitude ──┐
   2. REDEEM: recipient authors the event   │  the wall: no conversion,
      (co-presence gate, §4)                │  no rate, no settlement —
   3. DELIVER: the shared hour —            │  gratitude crosses;
      the sender's time-sacrifice           │  price never does
              │                             │
              ▼                             ▼
   4. THANK: recipient's money-gratitude (unprompted, duration-blind)
      + optional witness-share of the event (dual consent)
   5. RECEIVE: the community rejoices with the shared moment
   6. RE-THANK: witnesses' money-sacrifice — routed by default
      to the TIME-GIVER (sender-default routing)
              │
              └──── the circuit closes: honored givers pledge again;
                    witnesses become senders in their own dyads
```

### 6.2 · The joints are canonical

Each arrow in the circuit is an instance of gratitude-that-acts — the classical pairing of *knowing* what was done with *making it known* in deed (the kataññū-katavedī structure, AN 2.31–32, engaged here as grounding). The same hour changes face across the circuit: at pledge it is gratitude (backward-looking recognition); at delivery it is sacrifice (forward-looking gift). One object, two faces, separated by time — the recognition-then-enactment joint rendered as a state machine.

### 6.3 · Why the response crosses currencies

The thank for a delivered hour lands in *money*, and the reason is the wall itself: same-currency response (time-for-time) would make the relationship a scheduling ledger — barter with extra steps, each hour begetting an owed hour forever — and would re-consume the giver's protected scarcity as the price of having given it. Cross-currency gratitude can never settle, because no shared unit exists in which the account could be squared; the unpayable response is what keeps the relationship *open*, which the gift literature has always identified as the gift's actual function. The routing is inherited from the coupler publication's claims; what this paper adds is the circuit position: the cross-currency response is step 4 of a loop, not a bilateral courtesy.

Three constitutional guards, previously published, hold the crossing uncorrupted and are restated as inherited: the application **never prompts** the money-thank at or after redemption (the flywheel is a description of what love does, never a funnel the interface drives); the neutral agent's money-thank recommendation is **duration-blind**, never arithmetic on hours; and gratitude language on every surface names **the moment, not the meter** — "the morning at the market," never "the two hours."

### 6.4 · The witness inversion, and sender-default routing

Most kindness is done alone, which is why self-recorded kindness dominates gratitude ledgers and why performative capture is its permanent risk. The co-present event is the structural exception: **it is the one kindness with two people present, so the beneficiary holds the camera.** Content about the event is captured *by the grateful party, about the giver* — testimony, not performance; the recording is itself an act of gratitude. Its broadcast is disciplined (dual consent always; a curated, rationed gallery, never an open feed; the success metric is reconnections-inspired, never watch-time) and its response flow is claimed here as mechanism: **community re-thanks route by default to the time-giver** — the witnessed deed's author — while the witness's own act of capture earns whatever gratitude it organically draws. The default is a routing rule, not a split: no forced division, no secondary market in witness credit.

### 6.5 · What closes the loop

Nothing in the circuit mints. The giver ends the loop with delivered-hours honor, received money-gratitude, and an intact relationship; the witness community ends it having *spent* (money-sacrifice, step 6); and the loop's growth engine is the scene's quiet last line — the cousins who watched a reconnection and pledged hours to their own mothers. The circuit recruits by witness, not by referral bonus; what it compounds is dispositions.

---

## 7 · Threshold, Expiry, and the Death of an Hour

**Threshold-activation.** Small thanks accumulate as pledged time without expiry pressure; at a threshold the accumulated pledge activates into a redeemable, expiring commitment. The two-stage design keeps casual gratitude light (no one owes a coffee date for a small thanks) while making accumulated gratitude *real* (at some point, the thanks want a Sunday).

**One-month expiry, and the hour genuinely dies.** An activated hour unredeemed after one month is lost — not banked, not transmuted, not softened. The individual hour has no afterlife: Chronicle time is dyadic and non-stored, an expired commitment is not a deposit, and "your hour flowed onward" would be a lie the system refuses to tell. The grief of the lapsed hour is the product's teaching — *redeem before it is too late* — and the mechanic is the message.

**The two-layer resolution, and the lapse-channel.** At the aggregate layer, the platform's revenue funds the commons pool as a platform-level flow scaled to system-wide activity — never a per-hour transmutation, never a user charge. At the per-event layer, a lapse *occasions* (never funds-from-the-hour) an offer to the giver: to direct a small, anonymous, pool-funded money-gift to a nearby verified stranger, in the memory of the hour that died. The gift is new; the amount is agent-set and duration-blind; the delivered event remains the visibly superior outcome. The channel — previously claimed in the coupler publication as the lapse-channel — completes the pledge's incentive shape: the worst case of pledging time is becoming the human hand of an anonymous gift, which makes the pledge downside-free without making the lapse rewarding.

---

## 8 · The Claims

Enumerated as prior art; each claimed severally and in combination:

1. **Co-presence-gated redemption:** a time-currency in which the sole redemption form is a synchronous shared-attention event attended by both pledger and pledgee — in either geometry (facing or flanking) and either attested modality (in-person via device-proximity between verified humans; remote via live session) — with asynchronous media structurally excluded from redemption (envelope-not-delivery).
2. **Symmetric-cost redemption:** the property, and its deliberate exploitation, that the redemption event costs both parties the unit — presence received only by matching presence — as the anti-loneliness payload of the currency.
3. **Recipient-authored, giver-vetoed event composition:** the redeeming party authors the event from a curated togetherness registry; the pledging party holds a per-event veto; chronic refusal and chronic non-delivery are priced reputationally by a dual public ledger (given/delivered × received) with both-party delivery signoff.
4. **The guarded co-service class:** shared work as a redemption event under the conjunction of the both-hands rule (symmetric performance by both parties) and the outward-benefit rule (third-party beneficiary), composable in-person or remote — restoring service to a time-currency while structurally excluding labor extraction.
5. **The cross-currency response circuit:** a dual-currency architecture in which gratitude for a delivered time-event is expressed in the money-currency (unprompted, duration-blind, moment-not-meter — wall-layer guards inherited from the coupler publication) as one step of a closed six-step circulation spanning both currencies.
6. **Witness-inversion broadcast with sender-default routing:** event-witness content captured by the beneficiary about the giver, shared only under dual consent into a curated rationed gallery measured by practices-inspired rather than watch-time, with community re-thanks routing by default to the time-giver.
7. **Threshold-activation with mortal expiry and the two-layer lapse resolution:** pledge accumulation below an activation threshold; one-month expiry after activation with the individual hour irrecoverably extinguished; aggregate platform-revenue funding of the commons pool decoupled from any individual hour; and lapse-occasioned giver-directed anonymous giving (lapse-channel per the coupler publication).
8. **The composition:** claims 1–7 as a single system — a time-currency that cannot be spent alone, cannot become labor, cannot convert to money, and closes its circulation through witnessed gratitude.

---

## 9 · Prior Art, Generously

**The time-currency tradition.** Edgar Cahn's time-dollars and the TimeBanking movement (the founding articulation of time as egalitarian currency, and the co-production ethic this design honors); LETS mutual-credit networks; Ithaca HOURS; Japan's Fureai Kippu caregiving credits (the tradition's most successful instance, and the closest ancestor in spirit — care delivered to elders, though redeemable as absentee service and transferable across parties, both of which this design excludes); Bernard Lietaer's complementary-currency scholarship; the WIR cooperative. The failure analysis of §1 is offered with respect: these systems discovered the demand; this design responds to their decay mode.

**The witnessed-conversation precedent.** StoryCorps — two decades of recorded conversations between people who love each other, publicly broadcast — proves mass demand to witness real reconnection. The distinction: StoryCorps archives the conversation as its terminus; the Chronicle's witness layer is one step of a circuit whose metric is the *next* reconnection it inspires, and whose recorded artifact is never the redemption itself.

**Synchronicity and presence mechanics.** BeReal's synchronous-authenticity prompt (the interaction pattern of unfakeable simultaneity); video-presence verification in dating and identity platforms; BLE proximity attestation (the contact-tracing engineering wave); shared-activity platforms (watch-together, exercise-together features) as flanking-mode precedents in commercial form.

**The gift and its literature.** Mauss on the obligation-structure of the gift; Hyde on the gift that must move; the sociology of earmarked monies (Zelizer); the crowding-out literature (Titmuss; Gneezy & Rustichini) that grounds the wall's necessity. Buber's I–Thou stands behind the facing geometry; the joint-attention literature of developmental psychology behind flanking.

**This corpus.** The incommensurability-preserving coupler (wall-layer claims; Terra/Luna as the coupled-with-convertibility anti-example); the gift-tag-time-reveal publication (the pledge's physical on-ramp); *The Grace That Settles Nothing* (the coupler's third instance and this paper's sibling in the mints-nothing family); the Heart volume's published circuit doctrine and pre-registered P3–P7; the recommendation-function methodology publication (the neutral agent's band-clamp seam).

**The clock.** The agentic-payments patent wave — automated agents negotiating, scheduling, and settling on humans' behalf — is the live enclosure risk for exactly this territory: an agent-scheduled "quality time" feature with dynamic pricing is this mechanism with the wall removed, and the reason this publication is timed to precede the wave's arrival at the household.

---

## 10 · Pre-Registered Predictions

Stated 2026-07-21, before the Chronicle exists; P3–P7 of the Heart volume (initiation/response directionality, anchoring, age-shape) remain in force and are not restated.

- **P-C1 (the event outlasts the exchange).** Dyads completing at least one co-present redemption will show greater reconnection persistence at ninety days (continued contact beyond the platform's mechanics, self-reported "understand each other better") than dyads with pledges and messages but no redeemed event. Falsified if pledge-only dyads reconnect at equal rates — which would imply the gate is ceremony, not mechanism.
- **P-C2 (flanking is the on-ramp).** Among long-estranged dyads, first redemptions will over-select the flanking geometry relative to facing, and the flanking share will decline within dyads across successive redemptions. Falsified if first events show no geometry preference.
- **P-C3 (the standing tripwire — the wall holds socially).** Across the population of post-redemption money-thanks, thank *amounts* will show no significant correlation with event *duration*. This is the mechanism auditing its own deepest guard: a positive correlation is the empirical signature of a de-facto hour-price forming despite the wall, and the authors commit to publishing the correlation, whichever way it runs, at every reporting interval. The wall is not proven by architecture; it is proven by this number staying null.

---

## 11 · The Adversarial Surface

**The darkest adjacency: paid companionship.** A time-currency touching money must answer the pattern it must never become. The answer is structural at four layers: no conversion exists (the wall); no rate can form on any surface (duration-blindness, prompt-suppression, and P-C3 watching); the reconnection core is known-counterparty (one's own mother is not a market); and the stranger-facing layer is a separate mechanism behind an explicit boundary, separately safeguarded, and never doorstep-routing. What remains — off-platform side-arrangements between consenting adults — is outside any system's surfaces; the design's honest claim is that *its* surfaces price nothing and its grammar cannot express the transaction.

**Coerced presence.** The gift of time must never become its obligation. Guards: availability is expressed as a curated menu (no open-ended asks), mutuality signals are never gates, blocking overrides everything, and the veto is per-event and unpenalized in the moment (only *chronic* refusal surfaces, and only as ledger fact).

**Attestation fraud.** A dyad colluding to fake delivered hours gains: ledger honor with no monetizable payout (delivered-hours confer no currency), and any follower re-thanks their staged content might attract — which is the witness layer's existing integrity problem, met by its existing machinery (human verification, curation, real-impact weighting) rather than a new one. The farming audit conclusion: the redemption layer mints nothing, so the redemption layer cannot be farmed; only the witness layer carries value, and it is already guarded.

**Guilt machinery.** An expiring currency can torment. The containments: expiry grief is channeled into the lapse-channel's outward gift (guilt metabolized as dāna, not as churn or shame); no lapse is ever billed, penalized, or publicly itemized; and the application never prompts the redeemed party toward reciprocation (the no-backward-prompt guard doubles as anti-guilt architecture).

**Menu gaming.** Attempts to compose extraction inside the co-service class fail the both-hands or outward-benefit conjunction, and anything that passes both while still feeling wrong meets the veto. The residual — genuinely consensual, genuinely mutual, genuinely outward work that an outside observer would still call lopsided — is a family's own business.

**Ledger shaming.** The dual public ledger could fuel comparison. Its axes are deliberately non-rankable (no leaderboards, no percentiles, no feeds of "worst decliners"); quadrant legibility serves the dyad's own calibration, not the crowd's judgment.

---

## 12 · Honest Limits

**Unbuilt, n = 0.** The Chronicle is design-complete and unimplemented; the pilot evidence in this corpus belongs to the money-half. Every mechanism here is strata-dated to the design layer, and the predictions of §10 are the paper's only empirical commitments.

**The wall governs surfaces, not side-deals.** As with every wall-layer publication in this corpus: architecture can make a rate inexpressible on the system's surfaces and cannot police arrangements struck beside them. Non-fungibility deters the side-deal (an hour of a specific person is a poor commodity); it does not abolish ingenuity. P-C3 is the honest instrument: if a shadow rate forms anyway, the number will say so in public.

**Co-presence excludes, at the margin.** Synchrony is a real cost — time zones, shift work, connectivity, disability, incarceration all tax it, unevenly. The remote modality and the flanking geometry recover much of the margin (a call redeems; silence side-by-side on a call redeems); what synchrony still excludes, this design accepts as the price of a currency whose entire value is that it cannot be delivered by proxy. A presence-currency with an asynchronous fallback is a messaging app with guilt.

**The launch modality is the call, not the room.** The diaspora wedge means the flagship redemption at launch is remote — proximity attestation, the richer of the two attestations, arrives with the density the product hopes to create. The design's own success metric would eventually shift the modality mix; at launch, honesty requires saying the market walk in the canonical scene happens through a lens.

**Attestation privacy.** Proximity attestation is data-minimal by design (a mutual confirmation, not a location trail), but any presence-verification carries surveillance adjacency; the implementation must hold the line that the system learns *that* two people met, never *where they went*.

**The elegance caution.** The circuit closes suspiciously well — six steps, two currencies, one wall, every doctrine of this corpus arriving on cue. Internal coherence is the cheapest of all evidence and the most seductive; the authors state, as always, that the elegance earned the specification and only the predictions can earn the product.

---

## 13 · Lineage and Close

*(Labeled lineage: grounding and translation, never mechanism; §§3–8 stand without it.)*

The circuit's joints carry the canon's oldest teaching about gratitude: that it is complete only when enacted — the grateful person the tradition praises is the one who *knows what was done and makes it known*, and the mechanism's every arrow is that completion given a form. The limit case stands where this corpus always places it: the Śaśa Jātaka's hare, who gave the two scarcities whole and at once — the possession-grade and the life-grade of giving converging in a single body — witnessed, the story says, by a sky that kept the image. The Chronicle trades no one toward that summit; it is a foundation practice for householders, denominated in Sunday mornings. But the summit fixes the axis: the economy below it circulates hours and dollars so that, between two people who had gone dark to each other, the thing the hare gave completely might circulate in installments — one market walk, one mango argument, one answered pin of rejoicing at a time. The currency that cannot be spent alone is, in the end, a machine for making sure that the sentence "we should talk more" sometimes becomes a date.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/co-presence-gated-redemption> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/co-presence-gated-redemption.md> |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/co-presence-gated-redemption> |

---

## Acknowledgments

The authors acknowledge Edgar Cahn and the TimeBanking movement, whose forty years of practice mapped both the promise and the decay path this design answers; the Fureai Kippu network; StoryCorps, for proving the witness demand; the complementary-currency scholarship of Bernard Lietaer; the gift-economy literature from Mauss to Hyde; and the founding family's pilot households, whose year of practiced gratitude precedes every mechanism here. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Cahn, E. (2000). *No More Throw-Away People: The Co-Production Imperative*. Essential Books. (Time-dollars; TimeBanking.)
2. *Aṅguttara Nikāya* 2.31–32 (kataññū-katavedī — the grateful person who acts). Pāli Text Society translations.
3. *Śaśa Jātaka* (Jātaka 316). Pāli Text Society translation. *(Lineage-tier limit case; see §13.)*
4. Hayashi, M. (2012). "Japan's Fureai Kippu Time-Banking in Elderly Care." *International Journal of Community Currency Research* 16.
5. Lietaer, B. (2001). *The Future of Money*. Century.
6. Mauss, M. (1925/1990). *The Gift*. Routledge. · Hyde, L. (1983). *The Gift: Imagination and the Erotic Life of Property*. Vintage.
7. Zelizer, V. (1994). *The Social Meaning of Money*. Basic Books.
8. Titmuss, R. (1970). *The Gift Relationship*. Allen & Unwin. · Gneezy, U., & Rustichini, A. (2000). "A Fine Is a Price." *Journal of Legal Studies* 29(1).
9. Buber, M. (1923/1970). *I and Thou*. Scribner. (The facing geometry's philosophical ancestor.)
10. Tomasello, M. (1995 and successors) — joint attention as bonding primitive. (The flanking geometry's empirical ancestor.)
11. StoryCorps (2003–). The recorded-conversation public archive.
12. Ly, T. (2026). "The Incommensurability-Preserving Coupler." thonly.org defensive publication. *(Wall-layer claims; claims division per the editor's note.)*
13. Ly, T. (2026). "The Grace That Settles Nothing: Sacrifice-Witness Without Discharge." thonly.org defensive publication. *(Sibling instance; the mints-nothing family.)*
14. Ly, T. (2026). "HeartBank®: The Heart That Keeps Nothing." heartbank.net white paper. *(The published circuit doctrine; pre-registered P3–P7; the spent-time floor; the two blindnesses.)*

---

*— End of paper —*

*Marks referenced: HeartBank®, Miss Aquarius℠, B-Letter℠, Proof of Humanity℠. Document SHA-256 computed at push and recorded in the institutional log. Document License: CC0 1.0 Universal. The authors and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its date.*
