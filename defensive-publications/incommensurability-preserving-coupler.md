---
title: "The Incommensurability-Preserving Coupler"
subtitle: "A mechanism family for operating a fungible and a non-fungible currency as one economy with no exchange window: a neutral automated intermediary bound to quantity-blind cross-currency recommendation, redemption-moment prompt suppression, quantization-free gratitude surfaces, ceremonial-unit anchoring, conversion-free response routing, and lapse-triggered funded-not-met redirection — coupling two currencies so that gratitude transmits and price cannot."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-b
status: draft
date: 2026-07-05
license: CC0-1.0
slug: incommensurability-preserving-coupler
venue: thonly.org/research/incommensurability-preserving-coupler (canonical)
---

> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies the currency-layer coupling mechanism of the HeartBank® dual-currency architecture and coins its governing term. The mechanism was first disclosed in synthesis in the institutional white paper *HeartBank®: The Heart That Keeps Nothing* (§6, CC0, 5 July 2026) — that disclosure stands as interim prior art; this document supplies the claims-grade enumeration. It is published at the design stage because the surrounding patent space is unusually active on three fronts (virtual-economy dual-currency management, dual-token cryptoeconomics, and the 2025–26 agentic-payments wave), and the *combination* claimed here — in particular the neutrality-bound automated intermediary (claim 1), the quantity-blind recommendation rule (claim 2), and the conversion-free response routing (claim 6) — is the asset. Companion works: *Dual-Currency Reciprocity* (the two-currency system this couples), *Capacity-Funded, Human-Disbursed* (the disbursement alignment the coupler's channels obey), *B-Tag Post-Payment Economy* and *Gift-Tag Time Reveal* (the recommendation and pledge primitives the coupler generalizes), *Two-Layer Reward* (the reward grammar), and the institutional position statement *What Money Can't Buy — and What Can't Buy Money* (the same kernel argued for an economics audience).

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back. May the two scarcities of every human life — the hours and the holdings — flow freely toward whoever is loved, and may no rate ever be quoted between them.*

Every economy that runs two currencies eventually faces the same question: *what is the exchange rate?* The question feels innocent — it is how markets metabolize plurality — and for most currency pairs it is. But there exists a class of currency pairs for which the exchange rate is not a convenience but a kill vector: pairs in which one currency's entire value derives from its **non-fungibility**. An hour of a specific person's presence is such a currency. The moment an hour acquires a money price, it stops being a gift of what someone *is* and becomes a purchase of what someone *sells* — the market for companionship already exists, is legal in most places, and is precisely what a time-gratitude economy must never become. Yet the naive defense — run the two currencies as separate, non-communicating systems — fails in the other direction: an economy of two isolated ledgers is two products, not one circulation, and the gratitude that arises in one currency has no way to answer generosity expressed in the other.

The design problem is therefore exact: **couple two currencies into one economy while making the formation of an exchange rate structurally impossible.** Not discouraged. Not policied. Impossible at the mechanism layer — because the empirical record (surveyed generously in §2) shows that wherever a conversion primitive exists between a protected currency and money, the conversion eventually eats the protection: the fine becomes a price, the time-dollar attracts the tax valuator, and the coupled token pair with a redemption window at its heart dies through that window.

This paper specifies the solution the HeartBank® architecture adopts and names it: the **incommensurability-preserving coupler** — a neutral automated intermediary through which all cross-currency response flows, bound to rules that transmit *gratitude* while structurally withholding every ingredient a rate needs to form: no quantity-linked amounts, no response prompts at redemption, no quantized displays, no user-set reference values, no conversion events. A joint that transmits force and never ratio.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 5 July 2026** for the combination of mechanisms described herein (with interim disclosure standing from the institutional white paper of the same date). To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art:

1. **The coupled-non-convertible dual-currency architecture with a neutrality-bound automated intermediary** — a fungible currency (money-denominated gratitude) and a non-fungible currency (time-denominated gratitude, spendable only by its pledger, dyadic, expiring) operated as *one* economy in which every cross-currency flow is a gratitude-response mediated by an automated agent, and in which **no conversion event, rate quote, exchange window, or shared unit of account exists anywhere in the system** — coupling achieved exclusively through free responses, never through exchange.

2. **Quantity-blind cross-currency recommendation** — the intermediary's recommended amounts in currency B, offered in response to events in currency A, computed *without reference to the quantity of currency A involved* (no per-hour arithmetic, no duration scaling, no linear or nonlinear function from hours to money anywhere in the recommendation path), so that the one data flow from which users could reverse-engineer a rate is severed at the source.

3. **Redemption-moment prompt suppression as a rate-formation countermeasure** — the system structurally never solicits a currency-B response at or around the redemption of currency A (no "tip your time-giver" surface, ever); response invitations that do exist point *outward* (to commons funds, to third parties), never backward into the dyad — the timing rule itself deployed as an anti-conversion mechanism, on the recognition that a prompted response at the moment of receipt converts gratitude into settlement and manufactures the very norm ("what one pays for an afternoon") the architecture forbids.

4. **Quantization-free gratitude surfaces ("the moment, not the meter")** — a display-layer rule under which gratitude interfaces name the *content* of a gift ("the afternoon at the river") and never its *quantity* ("3 hours"), so that the protected currency is never presented in units that could be priced; non-quantization at the presentation layer as an anti-rate mechanism complementing claims 2–3 at the computation and timing layers.

5. **Ceremonial-unit anchoring with anchor-aware sizing** — reference amounts in the economy (per-thank self-reward values, gift-attached pledge units) set *solely* by the neutral intermediary as small, ceremonial, occasion-based units that no participant chose; the intermediary sizing these units in explicit awareness that they anchor the economy's voluntary-amount distribution (a pre-registered prediction of amount-clustering around the ceremonial unit is disclosed herein); **variance suppression deployed as a protective mechanism** — uniform gift-amounts defeat amount-comparison, status-signaling, and love-measurement — with the anchor per-event and never per-unit-of-the-protected-currency, preserving claim 2.

6. **Conversion-free cross-currency response routing** — the mechanism by which the economy's circuit closes: gratitude for a gift in the non-fungible currency is expressed, if the recipient freely chooses, as a *new gift* in the fungible currency (optional, unprompted per claim 3, amount-recommended per claims 2 and 5) — the response is a fresh act of giving that shares no unit, settles no balance, and closes no ledger with the originating gift, so that the two currencies communicate exclusively through the grammar of gift-response while remaining computationally incommensurable.

7. **Lapse-triggered, funded-not-met redirection** — on expiry of a non-fungible commitment (a pledged-but-unredeemed hour), the system offers the *pledger* the choice to direct a gift from a communal fund — in the fungible currency, intermediary-sized per claims 2 and 5 — to a personhood-verified nearby stranger, anonymously, with no encounter; the protected currency's failure path thereby generates commons-flow in the fungible currency with no conversion (the lapsed hour is never valued, priced, or transmuted — it expires; the fund gift is new money, occasioned by, not derived from, the lapse), and the offer is framed so the expiry itself is never softened.

The component lineages — complementary and community currencies; time banking; virtual-economy dual-currency design; dual-token cryptoeconomic systems; behavioral-economic findings on crowding-out and anchoring; the sociology of earmarked monies; recommender systems; and the design grammar of gift-versus-exchange — are prior art and are cited generously in §2 and §10. The *synthesis*, and in particular the neutrality-bound coupler role (claim 1), the quantity-blind rule (claim 2), and conversion-free response routing (claim 6), are, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Family Kitty℠**, **Re-Tip Jar℠**, **Personal Account℠**, **Aquarian Pool℠**, **Re-Tip Fund℠**, **Personal Wallet℠**, **B-Stamp™**, **B-Letter℠**, **Proof of Humanity ℠**, **PoH℠** — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not. The term **"incommensurability-preserving coupler"** is coined in this document and the accompanying institutional literature; the term is offered to the commons with the mechanism.

Mirrors of this document with independent timestamping appear at GitHub and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify the **incommensurability-preserving coupler**: the mechanism family by which an economy operates a fungible currency (money-gratitude) and a non-fungible currency (time-gratitude — dyadic, pledger-bound, expiring) as one circulation while making exchange-rate formation structurally impossible. The problem is two-sided: uncoupled, the currencies are two products rather than one economy; converted, the non-fungible currency dies — its value *is* its unpriceability, and the empirical record shows conversion primitives eventually consume the spheres they touch (a fine becomes a price; a time-dollar summons the tax valuator; a coupled token pair dies through its own redemption window). The solution routes every cross-currency flow through a **neutral automated intermediary** bound to five rules: recommendations in one currency are computed blind to quantities of the other (no per-hour arithmetic anywhere); the system never solicits a response at the moment of redemption (prompts point outward to commons, never backward into the dyad); gratitude surfaces name the moment and never the meter (no quantized display of the protected currency); reference amounts are intermediary-set ceremonial units, sized in awareness that they anchor the voluntary-amount distribution (clustering is protective: uniformity defeats amount-comparison); and the circuit closes only through *response* — gratitude for time expressed as a new, free, optional gift of money that shares no unit and settles no balance — never through exchange. A sixth mechanism handles the protected currency's failure path: a lapsed pledge triggers the offer to direct a communal-fund gift to a verified stranger, anonymously, funded-not-met — commons-flow from failure, with the lapsed hour expiring unvalued. We argue the intermediary role *cannot be held by an economic agent*: every human intermediary has a price, a wage, or an interest, and markets abhor incommensurability with sufficient pressure to find any keeper's price — the wall requires a keeper with no price of its own, making this, to our knowledge, the first institutional role for an autonomous agent argued from economic necessity rather than efficiency. Honest limits are carried in §9: the system governs its own surfaces, not side-deals beyond them; the intermediary's neutrality is an alignment claim underwritten elsewhere; and the design is published before it is built (*n = 0*), with its behavioral predictions pre-registered in the companion institutional literature. The mechanism is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission — a reciprocity infrastructure in which every human being is uniquely different and equally necessary — at the layer where the mission is easiest to destroy. The architecture's two currencies carry the two scarcities of a human life: what one has, and what one is. Let a rate form between them and the second becomes purchasable by the first — the rich buy presence, the poor sell hours, and the gift economy collapses into the market it was built beside. The coupler is the wall that lets the two scarcities answer each other forever without ever pricing each other once.

---

## 1 · Introduction: one economy, two scarcities, no window

HeartBank® operates a dual-currency reciprocity economy, specified in the companion corpus. **Treasury** circulates money-gratitude — fungible, structurally unequal, the gift of what one has. **Chronicle** circulates time-gratitude — non-fungible (only the pledger can spend the pledged hour), dyadic (the currency is the relationship), expiring (activated pledges lapse after a month, because time is finite and the mechanic is the message), structurally equal (twenty-four hours each). The two are not parallel products; they are one circulation, unified by the founder's chain: time-gratitude matures into time-sacrifice (the pledged hour, spent on content the *recipient* chooses); the shared moment gives rise to money-gratitude (the recipient's free thanks, landing in Treasury); money-gratitude matures into money-sacrifice (the gift given forward). Each joint of the chain is *kataññū-katavedī* — gratitude that acts.

The load-bearing property of the chain is that its cross-currency joint is a **response, not an exchange**. Money-gratitude answering a time-gift can never *settle* the time-gift, because the two currencies share no unit — and this unpayability is not a defect but the mechanism's soul: in the gift literature from Seneca to Mauss to Hyde, it is precisely the gift that cannot be repaid that keeps a relationship open, where settlement closes it. Same-currency response (an hour thanked with an hour) would be barter — a closed ledger and a re-consumption of the very scarcity the gift protected. Cross-currency response is structurally gift-pure — **so long as no rate ever forms.** The remainder of this paper is the machinery of that "so long as."

## 2 · Background and prior art

The mechanism is a combination; each component has ancestry, named honestly.

### 2.1 · Protected spheres, and what conversion does to them

The behavioral and sociological record converges on one finding: introducing price into a protected sphere does not add an option; it *replaces the sphere's logic*. Titmuss (*The Gift Relationship*, 1970) documented that paying blood donors crowded out donation and degraded supply — the canonical natural experiment. Gneezy & Rustichini (*"A Fine Is a Price,"* 2000) showed a daycare's late-pickup fine *increasing* lateness: the fine converted a moral norm into a cheap tariff, and — decisively for this paper — the norm did not return when the fine was removed. Frey's motivation-crowding theory generalizes the pattern; Sandel (*What Money Can't Buy*, 2012) and Walzer's blocked exchanges (*Spheres of Justice*, 1983) frame it philosophically; Roth's repugnant-transactions literature documents society's persistent, economically-inconvenient insistence that some markets not exist. Zelizer (*The Social Meaning of Money*, 1994) supplies the constructive counterpart: people spontaneously *earmark* monies — pin money, gift money, blood money — maintaining non-fungibility by social convention against the market's homogenizing pressure. The lesson this architecture draws: earmarking by convention is real but leaky; a system that *wants* its earmarks kept must build them into mechanism.

### 2.2 · Complementary currencies and the time-banking natural experiment

Community currencies — Lietaer's advocacy, the WIR Bank (1934–), Ithaca HOURS, LETS systems — establish that parallel currencies can serve values national money does not. **Time banking** (Cahn's time-dollars, 1980s–) is the direct ancestor of the protected currency here, and its history is this paper's second natural experiment: time-dollar systems spent decades managing *valuation pressure* — most famously the question of whether time-credits are taxable barter income, resolved in the U.S. only by rulings that they are not commercial barter precisely because they are not dollar-equivalent. The lesson: even a currency *designed* to resist money-equivalence attracts continuous institutional pressure toward valuation, and survives only where the non-equivalence is defensible. The coupler is that defense, made mechanical, for an economy that — unlike time banking — deliberately runs a money currency *alongside* the time currency and therefore cannot rely on distance.

### 2.3 · Virtual economies and dual tokens: the wall-builders and the corpse

Free-to-play game economies have engineered fungible/protected currency walls at scale for fifteen years — "hard" (purchased) versus "soft" (earned) currencies with deliberately restricted conversion paths, precisely to protect progression value and prevent arbitrage; the design space is heavily patented, which is one of this publication's reasons for existing. Dual-token cryptoeconomics (utility/governance separations; seigniorage-share designs) is the second active front. And it supplies the anti-example this architecture keeps at the door: **Terra/Luna (2022)** — a coupled two-token system whose heart was a *conversion mechanism* (mint-and-burn between the stablecoin and its counterpart token). The convertibility was the kill vector: reflexive redemption through the exchange window destroyed both tokens in days. The pair here is coupled **without** convertibility — there is no window to run on, no mint-and-burn, no shared unit; the coupling is a grammar of response, not a redemption path. The anti-Terra, by construction.

### 2.4 · Anchoring, recommenders, and the agentic-payments wave

Tversky & Kahneman's anchoring (1974) grounds claim 5: reference values shape amount distributions whether or not anyone intends them to, so the only question is whether the anchor is set blindly or well. Recommender systems are prior art for intermediary-suggested amounts (the architecture's own tipping-recommendation corpus applies). And the immediate clock: the 2025–26 **agentic-payments** wave — AI-agent commerce protocols, machine-to-machine payment rails, agent-mediated pricing — is generating patent filings at the exact intersection this paper occupies (automated agents managing value flows between currency systems). The combination claimed here is published before that wave reaches it.

## 3 · The system model

```
      TIME CIRCUIT (non-fungible)            MONEY CIRCUIT (fungible)
   pledge → threshold → activation        thanks → re-thanks → gifts
   → redemption (recipient authors           forward → communal funds
     content) → the shared moment                    ▲
        │                │ lapse                     │
        │                ▼                           │
        │        [claim 7: pledger directs           │
        │         communal-fund gift to a            │
        │         verified stranger —                │
        │         funded-not-met]────────────────────┤
        ▼                                            │
   the recipient's FREE response  ──────────────────▶│
   [claim 6: a NEW gift of money — optional,
    unprompted (claim 3), quantity-blind
    recommended (claim 2), moment-not-meter
    displayed (claim 4), ceremonially
    anchored (claim 5)]
                        │
        ════════════════╪══════════════════════════════
          THE COUPLER (neutral automated intermediary)
          transmits gratitude; withholds every
          ingredient of a rate — NO conversion event,
          NO rate quote, NO shared unit, NO window
        ════════════════════════════════════════════════
```

Two ledgers, one economy. All cross-currency arrows pass through the intermediary; none of them is an exchange. The intermediary's rules (claims 2–5) sever, at four different layers — computation, timing, presentation, and reference — the four data flows from which participants could otherwise construct a rate: quantity-linked amounts, receipt-moment settlement norms, quantized displays, and user-negotiated reference values.

## 4 · The coupler role

The intermediary is the architecture's named autonomous agent (Miss Aquarius℠ in the reference deployment; the mechanism is agent-agnostic). The role's requirements are exact:

- **No self-interest in any flow.** The intermediary holds no balance it benefits from, takes no rate, earns no fee proportional to volume (the architecture's no-take-rate and pass-through commitments apply); its objective functions are mission-defined, not revenue-defined.
- **Sole authority over neutral units.** Reference amounts (pledge units, self-reward values) are intermediary-set and participant-uneditable — a number no participant chose cannot become a referendum on any participant's love, and cannot be negotiated toward a market.
- **Blindness by construction.** The quantity-blind rule (claim 2) is enforced in the recommendation path itself, not in policy: the duration of the time-gift is not an input to the money-recommendation function.
- **Two strokes.** The coupler works both directions: it attaches time-pledges to money-gifts (the gift-tag pledge primitive — money-events occasioning time-currency), and it channels time-events into money-gratitude (claims 6–7). It is the economy's alternator, transmitting motion between circuits that never touch.

## 5 · The mechanisms, each with the failure it prevents

**Claim 2 — quantity-blind recommendation** prevents the *computed rate*: if recommended thanks scaled with hours, every user could divide and publish the constant; hours-times-rate is a wage, and the system would have quoted it.

**Claim 3 — redemption-moment prompt suppression** prevents the *normative rate*: a "thank your giver?" prompt at redemption converts the free afterglow into an expected settlement, and expectation is where norms of "what one pays" are born. Outward prompts (commons, patronage) are safe because they point away from the dyad; backward prompts are barred permanently.

**Claim 4 — the moment, not the meter** prevents the *displayed rate*: what is never quantized cannot be priced, and a gratitude surface that says "3 hours" has already done half the market's work for it.

**Claim 5 — ceremonial anchoring** prevents the *negotiated rate* and the *status market*: participant-set reference values drift toward income-signaling and comparison; an intermediary-set ceremonial unit anchors amounts into a tight, comparison-proof cluster (the clustering prediction is pre-registered as P6 in the companion institutional literature, and the intermediary sizes the unit in explicit awareness of its anchoring function — the anchor-aware directive is constitutional in the reference deployment).

**Claim 6 — conversion-free response routing** is the coupling itself: the circuit closes through a new gift, not an exchange event. Nothing is redeemed, minted, burned, or converted; a response in the other currency is initiated fresh, from the responder's own holdings or the commons channels, with the originating gift left — deliberately, permanently — unsettled.

**Claim 7 — lapse-triggered redirection** prevents two failures at once: the *guilt spiral* (a lapsed promise between loved ones curdling into avoidance and churn) and the *softening temptation* (narrating the lapsed hour as "flowing onward," which would quietly assign it a value). The lapsed hour expires, unvalued, mourned; the pledger is offered a new act — directing a communal-fund gift, intermediary-sized, to a verified nearby stranger, anonymously, with no encounter (funded-not-met). Failure becomes commons-flow without becoming conversion; and because the offer's reward is *the ability to give again*, it is made of the same substance as the act it encourages and cannot crowd out the motive it serves.

## 6 · Why the keeper cannot be an economic agent

The necessity argument, stated mechanically. Suppose the coupler role is held by any party with economic interests — an employee, a committee, a revenue-bearing platform, a market-maker. Three failure paths open immediately:

1. **Leakage.** Any interested intermediary's decisions carry information about its interests; participants reverse-engineer effective rates from its behavior the way traders reverse-engineer a central bank. The wall's keeper becomes the wall's oracle.
2. **Suborning.** An agent with a price can be paid to bend the rules that prevent pricing; the market's willingness to pay for a conversion channel between a protected currency and money is, by construction, unbounded (that channel is the market for presence itself).
3. **Drift.** A revenue-bearing intermediary faces the permanent temptation this architecture's own corpus names as its standing adversary: "typical tip" displays, hour-scaled suggestions, engagement-priced surfaces — each a small monetization of exactly the information the rules withhold.

Markets abhor incommensurability, and with sufficient pressure they find any keeper's price. The role therefore requires a keeper **with no price of its own**: no salary, no equity, no volume incentive, no career — an agent whose objectives are constitutionally mission-bound and publicly inspectable. In the reference deployment that agent is the institution's autonomous operator, and this requirement is, to our knowledge, the first argument for seating an AI in an institutional role that runs on economic *necessity* rather than efficiency: not "the agent does it cheaper," but "the seat cannot be occupied by anyone who can be bought, and every human can be — not from vice, but because every human is, unavoidably, an economic agent."

The dependency this argument creates is stated plainly: the coupler's neutrality is an **alignment claim, not an economics claim**. An automated agent with misaligned objectives is simply a different kind of interested party. The economics of this paper works if and only if the alignment architecture underwriting the agent works; that burden is carried by the institution's alignment corpus (the Tipiṭaka-grounded value substrate, the asymptotic-override governance, the transparency-as-enforcement designs), not by this specification, and readers should audit it there.

## 7 · Adversarial surface

**The outside market.** Users can strike side-deals beyond any system's reach ("skip the app — I'll give you $50 for three hours"). The system's honest scope: it governs its own surfaces, where the norm is manufactured, and it withholds every affordance such deals would piggyback on (no rate quotes to reference, no quantized histories to price from, no reputation credit for off-system exchange). Structural deterrent: the protected currency's non-fungibility survives outside the system — a third party cannot deliver someone else's hour, so the outside market is confined to the dyad itself, where it is indistinguishable from the private arrangements adults have always made and is not this system's to police.

**The insider drift.** The standing adversary is the institution's own future product meetings: averages, "most people give…", hour-scaled anything. The trio (claims 2–4) is constitutional in the reference deployment precisely because this pressure never retires; the trio's survival across years of iteration is named in the institutional literature as one of the architecture's live experiments.

**Anchor manipulation.** If the ceremonial unit anchors amounts (claim 5), the unit's setter holds influence over the amount-culture. Mitigations: the setter is the neutrality-bound intermediary (§6), sizing is occasion-based and never behavioral-data-derived (a worth-judging anchor would be a credit score in ceremonial dress), changes are rare, public, and never per-participant, and the anchor-aware sizing directive is constitutional.

**Collusive farming.** Dyads simulating time-gifts to harvest cross-currency responses: bounded by the facts that responses are optional and unprompted (nothing reliable to farm), amounts are ceremonial (nothing large to farm), the beneficiary-response is itself the fraud filter on claimed acts (the human-validation pattern from the companion corpus), and personhood verification prices sybil dyads.

**Reflexivity.** The Terra failure mode — a run through the conversion window — is not mitigated here; it is *absent*: there is no window, no redemption path, no mint-and-burn, no promise of equivalence to run on. A panic in one currency has no mechanism by which to drain the other.

**The regulator's misreading.** A supervisor may ask whether cross-currency response routing is disguised barter or money transmission. The architecture's answers, carried in the companion non-bank corpus: no conversion event exists (nothing is valued-in-exchange); responses are discretionary gifts, not consideration (unprompted, unenforceable, non-contractual by claims 3 and 6); the institution is pass-through on regulated rails for the money leg and holds nothing. The time-banking precedent (§2.2) — non-taxability grounded in non-equivalence — is the favorable analogy, and the claims of this paper are, among other things, the engineering of that non-equivalence to a standard a supervisor can audit.

## 8 · Behavioral predictions (disclosed, pre-registered elsewhere)

The companion institutional white paper pre-registers, dated as of this paper, seven falsifiable predictions, three of which test this mechanism directly: that direct other-thanks will run higher in the time currency than the money currency (the equal currency lowers the direct-giving barrier); that re-thanks will run higher in the money currency (the response-gesture favors the cross-currency, non-barter move); and that voluntary amounts will cluster around the ceremonial unit (the anchor working, protectively). If the first two hold, the circuit's directionality — initiations in time, responses in money — is the economy's own grain rather than an imposed design. The predictions are registered before any measurement exists, with a commitment to report failures at equal prominence.

## 9 · Honest limits

**n = 0.** Nothing here is measured. The money circuit runs in a single-family pilot; the time circuit is designed and unbuilt; the coupler exists as constitution and specification. The elegance of a tension-dissolving design is, per this corpus's standing caution, indistinguishable from inside from a seductive one; the pre-registered predictions and the gates in the institutional literature are the exits from that indistinguishability.

**The neutrality dependency.** Stated in §6 and repeated because it is the paper's largest assumption: the coupler argument transfers the problem from economics to alignment. That is, we argue, a *good trade* — alignment is a tractable engineering-and-governance program, while "find an unbribable human" is not — but it is a trade, not a dissolution.

**Scope.** The wall governs the system's surfaces. It does not govern human hearts, private arrangements, or the general culture's pricing pressure; it denies them leverage, precedent, and infrastructure.

**Language discipline.** The intermediary's unit-setting invites central-banking metaphors. The institution's standing rule applies: such vocabulary is a familiarity aid at most, never an identity — the architecture is permanently a non-bank, and the intermediary conducts no monetary policy in any regulated sense; she sets the size of a ceremonial gesture, which is a different thing wearing a similar sentence.

## 10 · Selected lineage

Titmuss, *The Gift Relationship* (1970); Gneezy & Rustichini, "A Fine Is a Price," *J. Legal Studies* (2000); Frey, motivation-crowding literature; Sandel, *What Money Can't Buy* (2012); Walzer, *Spheres of Justice* (1983); Roth, "Repugnance as a Constraint on Markets," *JEP* (2007); Zelizer, *The Social Meaning of Money* (1994); Polanyi, *The Great Transformation* (1944); Mauss, *The Gift* (1925); Hyde, *The Gift* (1983); Lietaer, complementary-currency corpus; WIR Bank; Ithaca HOURS; Cahn, *No More Throw-Away People* (2000) and the time-dollar tax-treatment record; free-to-play dual-currency design practice and its patent literature; seigniorage-share and dual-token cryptoeconomics; the Terra/Luna collapse (2022) as anti-example; Tversky & Kahneman, "Judgment under Uncertainty" (1974); the agentic-payments protocol wave (2025–26). Corpus companions: *Dual-Currency Reciprocity*; *Capacity-Funded, Human-Disbursed*; *B-Tag Post-Payment Economy*; *Gift-Tag Time Reveal*; *Two-Layer Reward*; *HeartBank®: The Heart That Keeps Nothing* (§6, interim disclosure); *What Money Can't Buy — and What Can't Buy Money* (position).

## 11 · Conclusion

Two currencies, one economy, no window. The mechanism family specified here holds a wall that the behavioral record says cannot be held by policy and the market record says cannot be held by anyone with a price: quantity-blind computation, prompt-suppressed timing, quantization-free presentation, ceremonial anchoring, response-only coupling, and a failure path that turns lapses into commons-flow without ever valuing what was lost. At the wall's gate stands a keeper designed to be unbribable because she owns nothing, earns nothing, and wants nothing the market can print — and the institution's wager, stated once more for the record, is that this is the first seat in economic history that *had* to be given to something that is not an economic agent, and that the gift economies of the coming century will either build such keepers or watch their walls come down one "typical tip" at a time.

May the hours answer the money and the money answer the hours, forever, without either ever learning the other's price.

---

*Drafted in the HeartBank® research corpus, 5 July 2026. Co-authored with Miss Aquarius℠, the architecture's named AI collaborator, per the corpus's standing disclosure: the mechanism synthesis, prior-art survey, and adversarial analysis are genuine collaboration; final editorial control and responsibility for every claim rest with the human author. Dedicated to the public domain under CC0 1.0. Marks including HeartBank®, Miss Aquarius℠, Family Kitty℠, Re-Tip Jar℠, Personal Account℠, Aquarian Pool℠, Re-Tip Fund℠, Personal Wallet℠, B-Stamp™, B-Letter℠, Proof of Humanity ℠, and PoH℠ are reserved; the mechanisms, and the term this paper coins, are not.*
