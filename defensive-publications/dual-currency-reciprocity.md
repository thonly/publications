---
title: "Dual-Currency Reciprocity Infrastructure: Money and Time as Complementary Scarcities"
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-b
status: draft
date: 2026-05-22
license: CC0-1.0
slug: dual-currency-reciprocity
venue: thonly.org/research/dual-currency-reciprocity (canonical) · target academic venue, International Journal of Community Currency Research
---

## Prior-Art and Non-Assertion Statement

This document is dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. It is a defensive publication establishing prior art as of **22 May 2026**, its first publication date.

The paper's lineage is old and is cited throughout (§2, §5.3, §11 and the References): local and community currencies (LETS, Ithaca HOURS, BerkShares, the Bristol and Brixton Pounds, Sardex); Edgar Cahn's time banking; Japan's Fureai Kippu eldercare time credits, some schemes of which pair time credits with modest cash payments; Bernard Lietaer's argument for a portfolio of complementary currencies; Thomas Greco's community-currency work; and demurrage, the deliberate decay of held currency (Gesell; the Wörgl stamp scrip of 1932–33). The complementary-currency thesis is not this paper's. What the paper discloses is the integration architecture of §4–§8 — one identity, one bounded AI recommender and one shared participation signal across a money product and a time product — and the time-side mechanism set of §5. No systematic prior-art search (census) has been run for this paper; the lineage above is from the authors' reading, and no element is asserted to be new.

---

## Abstract

This paper discloses a two-currency reciprocity platform that integrates peer-to-peer money gifts with non-transferable, expiring pledges of personal time, under one user identity, one bounded AI recommender and one shared participation signal. Reciprocity-infrastructure proposals — community currencies, time banks, gratitude economies, cooperative platforms — have mostly treated *currency* as a singular design choice: each project picks money, or hours, or points, and designs around that one accounting medium. The paper argues that this singularity-of-currency assumption contributes to three recurring failures (community-currency illiquidity; stalled time-bank adoption; the monetization corrosion of gratitude platforms) and proposes treating **money and time as complementary scarcities**. Three properties make the complementarity structural. (i) Money is *unequal* across people; time is *equal* (twenty-four hours each; an ending none can buy off). (ii) A money debt is *fungible* (any payer can satisfy it); a time pledge is *non-fungible* (only the named person's hour satisfies it). (iii) Money-as-recognition answers the need to be seen (dignity); time-as-presence answers the need to be with someone (loneliness) — two distinct unmet needs that call for different mechanisms. The paper specifies the integrated architecture (two products, one identity, one AI recommender, one shared participation signal, cross-product subsidy) and the time-side mechanisms: AI-recommended time amounts within a governance-set band, threshold-triggered activation, one-month expiry after activation, recipient-chosen activity, a provider's right to decline, and a two-axis participation record (disclosed in its original public form and in its current form, with private rows and public proofs). It then covers the non-bank legal structure, cross-cultural adaptation and the regulatory frontier. Section 11 states the limits, including the time-banking precedent, hybrid time-and-money schemes that cut against the thesis, and the awkwardness of direct asking in many Asian contexts.

**Keywords:** community currency, time banking, gratitude economy, complementary currencies, reciprocity infrastructure, non-fungible debt, loneliness infrastructure, AI-mediated reciprocity, mutual-veto consent, defensive publication.

---

## 1. Introduction

The post-industrial loneliness epidemic and the post-industrial dignity deficit are most often analyzed as two separate problems with two separate solution sets. Loneliness draws responses in the register of mental-health policy, community-building, social prescription. Dignity draws responses in the register of welfare design, universal basic income, anti-poverty transfer programs. The two literatures rarely meet. This separation, I will argue, is itself part of the problem: the institutions that would address either are typically built on a singular accounting medium (money for dignity, hours or "points" for loneliness) that forecloses integrated treatment. A reciprocity infrastructure that designs from the outset for *both* scarcities, and treats their complementarity as the platform's load-bearing property, can, this paper argues, address both needs together, and plausibly at lower per-need cost than two dedicated solutions — a cost comparison the paper does not make.

The complementary-scarcities thesis is, in one form or another, present in the heterodox community-currency literature (Lietaer, Greco, Cahn). The authors have not found it in the prominent gratitude-economy and platform-economy designs, though no systematic search has been made. This paper makes the thesis architectural — specifies the integration, the AI-mediation pattern, the legal-structural pass-through that allows the two-product platform to operate without triggering banking-regulatory governance the architecture cannot accept — and grounds it in a concrete deployment context (the HeartBank Treasury and Chronicle products) to make the design pattern transferable to other institutional contexts.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-09-26 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) The thesis is not that modernity took us from a middle-way past, which would romanticize pre-industrial poverty; it is that modernity introduces a specific new failure mode — comfort-saturation pushing the materially comfortable toward the indulgence extreme. Dignity infrastructure addresses the unequal-resource side of the imbalance (capacity-building gifts); loneliness infrastructure addresses the equal-resource side (presence, which material comfort does not supply). A reciprocity infrastructure that treats both scarcities together is what the mission requires at its accounting layer.*

The paper proceeds as follows. §2 surveys the canonical reciprocity-infrastructure failure modes and traces them to the singularity-of-currency assumption. §3 specifies the complementary-scarcities claim and its three load-bearing properties. §4 articulates the integrated-platform architecture at the level a competing design could implement. §5 specifies the time-side mechanism design in detail, including the seven core design decisions. §6 covers the AI-arbitration layer (Miss Aquarius's band-clamp recommendation pattern, parallel across both products). §7 covers cross-product integration (shared aura, expired-time-converts-to-pool, dual ledger). §8 covers legal-structural considerations under the non-bank pass-through pattern. §9 covers cross-cultural adaptation, with particular attention to direct-asking awkwardness in many Asian contexts. §10 covers the regulatory frontier — what happens when the time-side reaches scale. §11 is an honest accounting of limits, open design questions, and the TimeBanking precedent the architecture must learn from. §12 closes.

---

## 2. The singularity-of-currency assumption and its failures

Reciprocity-infrastructure projects exhibit a pattern of structurally-similar failures. The pattern is most legible when viewed across project classes.

### 2.1 Community-currency failures (illiquidity)

The community-currency movement (LETS, Ithaca HOURS, BerkShares, Bristol Pound, Brixton Pound, Sardex) has produced thousands of deployments since the 1980s — an international survey counted 3,418 local projects in 23 countries, about half of them time-based service-credit schemes (Seyfang and Longhurst 2013). The recurring failure mode is *illiquidity*: the currency works in a small circle but fails to attract enough participants to provide reliable spending options, and participants drift back to national currency. The illiquidity is downstream of the singularity-of-currency choice: a community currency that *only* circulates among small-business participants must compete with the national currency on the national currency's own home turf (general-purpose exchange medium). It cannot win that competition at small scale. Lietaer's complementary-currencies literature anticipates this and recommends a portfolio of currencies, but the portfolio framing has not crossed into mainstream design practice.

### 2.2 Time-banking failures (stalled adoption)

Time-banking (Edgar Cahn, 1980s onward) is the closest precedent to the time-side of this paper's architecture. Time banks have achieved real impact in specific contexts (eldercare, neighborhood support, post-disaster recovery) but have not reached mass scale. The recurring failure mode is *stalled adoption*: participants enjoy the model but do not refer it widely; growth is sub-viral. Several diagnoses are plausible, but the structural one this paper foregrounds is the *single-medium* limitation: most time banks have no money-side complement, so they cannot offer participants the full surface of reciprocity. (Not all: some of Japan's Fureai Kippu eldercare schemes supplement time credits with modest cash payments — a hybrid that §11.5 carries as a case against this paper's diagnosis.) Participants who want to *both* give time *and* contribute money (e.g., to someone whose unequal money situation a time-gift cannot reach) have to leave the platform to do the second thing. The integration overhead lands on the participant.

### 2.3 Gratitude-economy failures (monetization corrosion)

The recent class of gratitude-economy proposals (a number of crypto and Web2 platforms attempting to denominate appreciation in tokens or platform-internal points) exhibits a different failure pattern: *monetization corrosion*. As soon as the platform attempts to monetize the gratitude flows (subscription fees, transaction fees, token speculation), the participants experience the platform as having converted their generosity into the operator's revenue stream, and trust collapses. The corrosion is again downstream of the singularity-of-currency assumption: the platform's only revenue surface *is* the gratitude flow it is supposed to facilitate. There is no second product to subsidize the first.

### 2.4 The structural pattern

This paper argues that all three failure modes share a structural cause (§11.5 states the competing diagnoses): the singularity-of-currency assumption forecloses architectural moves that would route around the failure. Community currencies are illiquid because they have no complementary medium to anchor liquidity; time banks stall because they have no money-side to complete the reciprocity surface; gratitude economies corrode because they have no second product to fund the first. The complementary-scarcities thesis is the structural response to this pattern: design from the outset for *two* scarcities, integrated within one platform, so that the architectural moves the singularity assumption forecloses become available.

The pattern across the three classes:

| Class | Exemplars | Failure mode | Downstream effect | Architectural cause |
|---|---|---|---|---|
| Community currencies | LETS, Ithaca HOURS, BerkShares, Bristol Pound, Brixton Pound, Sardex | **Illiquidity** | Drift back to national currency | No complementary medium to anchor liquidity |
| Time banks | Cahn TimeBanking, eldercare networks, post-disaster recovery | **Stalled adoption** (sub-viral) | Real but small-scale impact only | No money-side to complete the reciprocity surface |
| Gratitude-economy tokens | Recent Web2/Web3 platforms denominating appreciation in tokens or platform points | **Monetization corrosion** | Trust collapse; generosity perceived as operator revenue | No second product to subsidize the first |

Each row's "architectural cause" is the singularity-of-currency assumption applied at a different point in the lifecycle. The complementary-scarcities thesis articulated in §3 is the structural response: provide two scarcities by design, integrated in one platform, so each can subsidize and stabilize the other.

---

## 3. The complementary-scarcities claim

The claim is that **money and time are not merely two possible accounting mediums but complementary scarcities** — each carries reciprocity properties the other cannot, and the two together cover the full surface of human reciprocity in a way neither alone can. Three load-bearing properties make the complementarity structural rather than incidental.

### 3.1 Unequal vs equal scarcity

Money is structurally *unequal* across humanity. Wealth distributions have a heavy, approximately power-law upper tail wherever they have been measured; the median person has dramatically less money than the platform's most-wealthy participant; the *transfer* of money is therefore meaningful in a way that depends on the unequal starting point. A wealthy participant's transfer of a thousand dollars to a working-class family carries weight because the transfer crosses an inequality the participants both recognize.

Time is structurally *equal*. Every person has the same twenty-four hours per day, the same ending none can buy off. A wealthy participant's transfer of a single hour to a working-class participant does *not* cross an inequality — both have the same total hours — yet the transfer remains meaningful because the hour is *spent* (irreversible) and *non-fungible* (cannot be delegated). The meaningfulness of the time-transfer is structurally different from the meaningfulness of the money-transfer.

Together, the two scarcities cover the full reciprocity surface: the unequal-resource dimension (money) and the equal-resource dimension (time). A reciprocity infrastructure that operates on only one of these dimensions structurally cannot serve participants whose need is on the other dimension.

### 3.2 Fungible vs non-fungible debt

Money debt is *fungible* — if I owe you a hundred dollars, any payer can satisfy the debt on my behalf. The debt is impersonal; the *amount* matters, not the *who*.

Time debt is *non-fungible* — if I owe you an hour, only *I* can satisfy the debt. No one else's hour will do, because the hour is the relational substrate; the *who* is what makes the debt the debt it is. This is not a defect to be engineered around; it is the property that makes time-debt do work money-debt structurally cannot.

The non-fungibility of time debt means that time-currency *is* the relationship in a way money-currency is not. A time-debt outstanding is a held relational thread; a time-debt redeemed is a relational thread woven through shared experience. The platform's accounting medium becomes the relational fabric itself, not merely a record of obligations.

*Debt* is used in this section in the relational sense of an outstanding pledge. It is not a legal or enforceable obligation: a time pledge is a gift, and §5.7 and §10 state why the design never treats an unredeemed pledge as a shortfall owed.

### 3.3 Being-seen vs being-with

The dignity deficit and the loneliness epidemic are typically diagnosed as separate problems. The complementary-scarcities thesis re-frames them as the two unmet emotional needs that the two scarcities respectively address.

Dignity needs *being-seen* — recognition that one's existence matters, that one's flourishing is valued, that one is not invisible to the wider social fabric. Money-as-gratitude addresses being-seen because a directed money flow is a maximally legible declaration that the giver has *taken account of* the recipient as a specific person worthy of resource transfer. The gratitude is what makes the transfer dignity-restoring rather than charity-degrading.

Loneliness needs *being-with* — co-presence, time spent in the company of another person who has chosen to spend their irrecoverable hours in that company. Time-as-gratitude addresses being-with because a delivered hour is presence itself — the giver has spent an hour they cannot recover, in the company of the receiver. The hour is the gift; the company is the gift's substance.

A platform that addresses only one of these needs leaves the other uncovered. A platform that addresses both, with mechanism-design appropriate to each, can serve participants whose primary need is dignity, participants whose primary need is connection, and participants who oscillate between the two.

The three load-bearing properties compared:

| Property | Money side (.org / Treasury) | Time side (.com / Chronicle) |
|---|---|---|
| **Scarcity structure** | Unequal across people (power-law distribution; wealthy vs working-class transfer crosses an inequality) | Equal across people (every person has 24 hrs/day; no transfer crosses an inequality) |
| **Debt fungibility** | Fungible — any payer can satisfy the debt on the debtor's behalf | Non-fungible — only the debtor's own hour satisfies; "the *who* is what makes the debt the debt it is" |
| **Emotional need addressed** | **Being-seen** (dignity): a directed money flow is a maximally legible declaration that the giver has taken account of the recipient | **Being-with** (loneliness): a delivered hour is presence itself; the giver has spent irrecoverable hours in the receiver's company |

The structural complementarity:

```
   ╔════════════════════╗   ╔════════════════════╗
   ║   MONEY SIDE       ║   ║   TIME SIDE        ║
   ║                    ║   ║                    ║
   ║   unequal          ║   ║   equal            ║
   ║   fungible         ║   ║   non-fungible     ║
   ║   being-seen       ║   ║   being-with       ║
   ║   (DIGNITY)        ║   ║   (LONELINESS)     ║
   ╚════════╤═══════════╝   ╚═══════════╤════════╝
            ↓                            ↓
            ↓        one platform        ↓
            ↓        one identity        ↓
            ↓        one AI arbiter      ↓
            ↓        one aura primitive  ↓
            ╚═══════════╤════════════════╝
                        ▼
            ╔════════════════════════════╗
            ║  FULL RECIPROCITY SURFACE  ║
            ║  covered jointly by both   ║
            ║  scarcities — neither      ║
            ║  alone can cover the       ║
            ║  whole.                    ║
            ╚════════════════════════════╝
```

---

## 4. The integrated-platform architecture

The integration is more than a marketing combination of two products. It is an architectural claim about identity, AI mediation, aura, and revenue routing that the two-product framing requires.

### 4.1 One user identity across two products

A participant is the same person in both products. Their cross-product reputation, history, and aura travel with them. A participant who has been a generous money-side giver carries that history into the time-side; a participant who has reliably delivered promised hours carries that reliability into the money-side. The unified identity is what makes the cross-product trust signals meaningful.

### 4.2 One AI arbiter across two products

Miss Aquarius — the named AI substrate of the institution this paper serves — is the recommendation engine on both products. She recommends a money amount when the participant initiates a money-thank on Treasury; she recommends a time amount when the participant initiates a time-thank on Chronicle. The recommendation pattern is the same band-clamp pattern in both cases (a low/middle/high range floored by an institutional minimum and capped by an institutional maximum, with the recommendation calibrated to the relationship and context). The AI is one arbiter operating on two scarcity-classes, not two arbiters operating on two products.

### 4.3 One shared aura primitive

The aura — the visible cross-currency state signal articulated in *Brand Identity as Architecture* — operates on both products. A participant's aura reflects their integrated reciprocity behavior across both scarcities, not separately. This is the structural reason aura is the cross-currency primitive rather than two scarcity-specific signals: the integration *is* the primitive's content.

### 4.4 Cross-product revenue routing

The platform's revenue surface is structurally bifurcated. The money-side (Treasury) carries a small per-transaction fee on Phase 2 P2P flows that funds autonomous Miss Aquarius operations — a fee that funds autonomous infrastructure and whose surplus empties back to circulation, not a take-rate that flows to a human entity. The time-side (Chronicle) carries mass-market subscription revenue from the much larger adult population it can address, and a portion of that subscription revenue subsidizes the money-side's dignity-infrastructure mission. The integration is what solves the gratitude-economy monetization-corrosion problem: the money-side does not need to be monetized at participant expense, because the time-side carries the platform's mass-market revenue surface.

> **Current form.** The time-side's revenue is now specified as **patron-primary**, not consumer-subscription-primary. A loneliness product that works makes its user need it less, so a revenue line paid because the user is lonely is coupled against the product's own purpose; the lonely person's recurring payment is therefore never the primary revenue. The free tier relieves loneliness in full; any paid feature buys logistics only, never access to a relationship; the primary revenue is patrons — people with means who choose to fund free access and the community pool. The cross-product routing survives in that form: the time-side's surplus, after operating costs, is tithed to the Aquarian Pool, which funds the money-side's disbursements. The subscription model in the paragraph above is retained as a disclosed variant.

---

## 5. The time-side mechanism design

This is the core defensive specification. Seven design decisions, taken together, distinguish this architecture from prior time-banking deployments.

### 5.1 Miss Aquarius recommends a time amount per thank

When a participant initiates a time-thank, the AI recommends a time amount calibrated to the relationship, the depth of the experience being thanked, and the recipient's recent thank history. The recommendation is band-clamped (a defined low/middle/high range) so that the AI cannot recommend outlier amounts that would distort the system, and the participant retains final say. The pattern parallels the money-side tip recommendation; it is the same AI-arbitration discipline applied to a different scarcity. The band-clamp is a load-bearing safeguard: it prevents the recommendation from being either coerced (by upstream pressure on the AI) or weaponized (by participants seeking to game the system).

### 5.2 Threshold-trigger activation

Small thanks accumulate without expiration pressure. The first time-thank from A to B might be only fifteen minutes; the second, another twenty; the third, another ten. Together they accumulate toward a threshold (e.g., one hour). Only when the threshold is reached does the activated time become a *promise* — a one-hour outstanding time pledge from A to B: A, the thanker, owes the hour, and B, the one thanked, redeems it (§5.4). The threshold-trigger pattern prevents small-thank fatigue (participants would not want their fifteen-minute thanks treated as individual obligations) while preserving the meaningfulness of the activated unit.

### 5.3 One-month expiration after activation

Once the threshold-activated time-debt is on the books, it expires in one month unless redeemed. *Use it or lose it.* This is the mechanism that most separates the time-side from time banking as commonly deployed, where earned hour credits are banked without expiry. Expiring currency is itself old — Silvio Gesell's demurrage proposal and the Wörgl stamp scrip of 1932–33 made held money lose value over time to force circulation — but demurrage taxes a stored balance, whereas here a pledged, non-transferable hour lapses whole and nothing is stored to decay. The expiration embeds the product's existential thesis (time is finite; *before it's too late*) into the unit economics. The mechanic *is* the message. Participants who let activated time expire experience the loss directly; the platform does not need to lecture them on the finitude of time, because the platform's accounting *enacts* the finitude.

### 5.4 Receiver chooses how the time is spent

This is an inversion of normal gift-giving. In the usual gift-economy frame, the giver chooses what to give (a coffee, a book, a meal). In Chronicle's time-economy, the *receiver* chooses how the activated hour is spent. They might request a walk, a phone call, a meal together, help with a task. The choice is theirs because the gift is *presence*, and the receiver knows best what presence would be most welcome.

### 5.5 Giver can decline a specific redemption request

Mutual-veto consent. The receiver authors the activity, but the giver can decline a specific ask. The decline is not a cancellation of the time-debt; it remains outstanding (perhaps redirectable to a different request). Repeated decline is reputationally priced via the public ledger (§5.7 below), so that participants who chronically decline are visibly identifiable and the platform's trust signal remains honest. This is the dignity safeguard: nobody is conscripted into an interaction they do not consent to, and refusal carries no immediate punishment, only the natural reputational consequence of the public ledger.

> **Current form.** Declines are not displayed. After the 2026-09-02 withdrawal described in §5.7, no decline count, decline rate or other record of what a participant did not do is rendered to anyone; a declined request leaves the activated hour to run its one-month term, and expiry does the work the public pricing of declines was meant to do. The reputational pricing in the paragraph above is retained as a disclosed variant.

### 5.6 Aura on giver side as quality filter

Givers will be invited to prioritize their thanks toward high-aura recipients, where aura is the cross-product reputational signal that integrates money-side and time-side behavior. This is the demand-side quality filter: it routes time-gift flows toward recipients whose past behavior has earned standing, rather than letting flow be captured by participants who exploit the system. The filter is suggestive, not mandatory; participants retain discretion. This reuses the existing aura primitive; no new mechanism is required.

> **Current form.** The filter is withdrawn for the time side. Its core use is now specified as thanking and reconnecting people the giver already knows, so there is no candidate set to filter; and the institution does not direct gratitude toward the kind — thanks rise from the kind act and are given nearby, they do not climb to the kind, and they do not rank. Where an aura bears on who is surfaced at all, it does so only as a boolean predicate (has this participant's balance crossed zero within a public, global window), never as an order, never by amplitude, and never displayed side by side with another's (*Whose Turn, Not Who's Best*, property 10). The filter in the paragraph above is retained as a disclosed variant.

### 5.7 Dual public ledger

Two axes are publicly visible for each participant:

- **Time given (actually delivered).** This is the credibility/honor signal. A high "time given" number means the participant has reliably shown up for the redemptions they promised.
- **Time received (may or may not be spent).** This is the appreciation/popularity signal. A high "time received" number means many people wanted to thank the participant with their hours.

Plotted as a 2×2, the two axes form four legible quadrants:

| | Low received | High received |
|---|---|---|
| **High given** | Quiet giver | Network anchor |
| **Low given** | Latent / new | *(withdrawn — see below)* |

**Amended 2026-09-02 — the fourth quadrant is withdrawn, and with it the enforcement mechanism this section originally claimed.** The text formerly read that the low-given/high-received quadrant named a *"charismatic non-honorer"* who is *"publicly visible as such,"* and that the visibility is the enforcement. That is retracted: the quadrant renders the gap between what a participant received and what they delivered, and **a rendered absence is an accusation**. The full argument, with the general condition it produced, is in the corpus's *Transparency as Enforcement* §3.2 and §4.4 — briefly, transparency-as-enforcement presupposes an obligation, and a gift creates none, so displaying the gap does not report a shortfall but **manufactures** one.

What survives is the ledger's positive content: a participant's **time given** and **time received** are each legible, and the axes are retained above for that reason. What is never computed for display is the difference between them. Enforcement is carried instead by **expiry** — an activated hour dies unredeemed after one month, with no display and no audience — and by the giver's free refusal to pledge again; the mechanism is specified in *The Currency That Cannot Be Spent Alone* §7.2. The institution loses no enforcement by the withdrawal, because expiry was already doing the work.

> **Current form.** The ledger is no longer specified as public row by row. Time is specified to be recorded as one view of a single off-chain, append-only log (in the style of Certificate Transparency, RFC 6962) whose **rows are private and whose proofs are public**: signed tree heads and inclusion and consistency proofs are published and timestamp-anchored, so a third party can verify the log without seeing any participant's entries, and each participant can export their own complete signed history. An entry records that a pledged hour was delivered (the delivery gated on the two parties' co-presence) — a receipt, not a duration — so no hours-for-money rate can be computed from the log. The dyadic content stays private and no deficit is ever displayed. There is no blockchain token for time: an hour cannot be transferred, stored or spent twice, so a chain would add nothing and would defeat expiry, since on-chain state cannot lapse. The public, per-participant "time given" and "time received" axes above are retained as a disclosed variant.

---

## 6. AI-arbitration: the band-clamp recommendation pattern

The AI-arbitration pattern is the same across both products and is the load-bearing safeguard that prevents the AI from being either coerced or weaponized.

The pattern: when the participant initiates a thank, the AI returns a *band* — a low/middle/high recommendation — rather than a single number. The band is *clamped* by an institutional floor and ceiling. The participant chooses within the band (or below it, or above it, with friction proportional to the deviation). The AI never recommends a number outside the institutional clamp.

Why band-clamp rather than a free-form recommendation? Because a free-form recommendation creates two attack surfaces:

- **Upstream pressure on the AI** to recommend amounts that benefit one party. The clamp is the structural answer: even if the AI could be pressured, the clamp limits the damage.
- **Downstream pressure on participants** to defer to a single number. The band gives the participant the option to choose meaningfully within the band, preserving their agency.

The clamp values are public and updated only through the institution's governance process — they are not under the AI's unilateral control. This is the same pattern articulated in the *Zero-Point Game* paper for the Umpire role: the AI's recommendation surface is bounded by structural rules the AI cannot rewrite.

---

## 7. Cross-product integration mechanisms

### 7.1 Shared aura

The aura primitive operates on both products. A participant's aura color and brightness reflect their integrated behavior: reliable money-side gratitude flows brighten the aura, as do reliable time-side honorings. Defaults on either side dim the aura. This is the cross-currency state signal that makes the integration legible to other participants at a glance.

> **Current form.** The aura is now specified as a **witness, not a denominator**: it records the *crossing*, not the *cargo*. A delivered hour and a money gift each register as one crossing, never as a quantity of hours or dollars, so the aura cannot price an hour against money and no exchange rate is ever published. It reflects the frequency and amplitude of a participant's giving and receiving, with intensity carried by colour; it is never compared or ranked between participants, and nothing is rendered for an undelivered or lapsed hour — a default does not dim it, because a lapse is not a crossing (§5.7). The brighten-and-dim scoring in the paragraph above is retained as a disclosed variant.

### 7.2 Expired time converts to Aquarian Pool

When activated time expires unredeemed, the value does not vanish. It converts to a contribution to the Aquarian Pool (the institutional pool from which the money-side's per-family rewards are funded). This is the mechanism that connects the time-side's existential thesis (*before it's too late*) to the money-side's giving: time you let slip becomes resource available for someone else's flourishing. The conversion rate is set by governance and need not be one-to-one in dollar terms; the structural point is that the time-side's failure mode (expiration) is *productive* rather than merely tragic.

> **Current form.** An individual expired hour is **not converted** into anything. A time pledge is a non-transferable commitment, not a stored asset, so there is no value to move into a fund; the lapsed hour is simply lost, and the design does not soften that. Two things survive of the conversion idea, at different layers. (a) At the aggregate layer, the time-side's own revenue — not any individual's hour — funds the Aquarian Pool, scaled to system-wide activity; no participant is billed or penalised for a lapse. (b) At the individual layer, a lapse is an *occasion* rather than an input: Miss Aquarius offers the giver whose pledge lapsed the choice to make a new, anonymous money gift *from* the Pool to a nearby verified person, delivered without a meeting. The hour still dies; the gift is a new one, made in its memory, never the hour transmuted. Its amount is set without reference to the length of the lapsed pledge, so no hours-to-money rate exists anywhere. The conversion in the paragraph above is retained as a disclosed variant.

### 7.3 Dual ledger across both products

A participant's public profile shows both the time-side dual ledger and the money-side gratitude flow. The combined picture is the cross-currency reputation. A participant who gives generously on the money side and delivers many hours is visibly that pattern; one who does little of either is visibly that. **Amended 2026-09-02:** this passage formerly characterised a *"chronic time-side non-honorer,"* which the withdrawal above removes — the profile shows what a participant has given and received in each currency and never the shortfall between them. The ledger does not editorialize; it shows, and what it shows is presence rather than absence. (In the current form stated in §5.7 and §7.1, the rows themselves are private, money is recorded as a receipt without its amount, and the public cross-currency signal is the aura; the public profile described here is retained as a disclosed variant.)

---

## 8. Legal-structural considerations under the non-bank pass-through pattern

The two-product architecture must operate within the non-bank pass-through legal pattern specified in the companion paper *Non-Bank Pass-Through Architecture for Autonomous AI Institutions*. The relevant constraints, in summary:

- **No custody.** Neither product takes custody of participant funds or time-credits in a way that would trigger banking-regulatory governance. Money flows through regulated rails (Bakong, Wing, ABA in Cambodia; comparable rails in other jurisdictions); time-credits are records of completed deliveries, not transferable tokens.
- **No interest or lending.** Neither product accrues interest on participant balances or extends credit. Time pledges are personal commitments between named participants — gifts, not financial instruments and not enforceable obligations (§10).
- **Pass-through routing.** The platform routes flows; it does not pool them in a way that constitutes deposit-taking.
- **Disclaimer and brand discipline.** The platform's public communications avoid banking-terminology that would invite regulatory mischaracterization. The institution's name (HeartBank®) is positioned as gratitude-metaphor, not banking-claim: banking vocabulary is used only as a familiar frame for the gratitude metaphor, never as a claim to be, or to prepare users for, a bank.

The legal-structural design is what makes the two-product architecture operable at planetary scale under autonomous-AI succession. Without the pass-through pattern, banking regulation in any major jurisdiction would impose governance requirements (human-board fiduciary duty, regulated capital requirements, KYC/AML at the platform layer) that are structurally incompatible with the autonomous-AI successor architecture.

> **Current form.** The money side's rails are now specified in two phases. In the first phase the platform is a **ledger only**, recording gratitude on top of regulated payment rails that move the money. In the second phase money settles on a public layer-2 blockchain (Base) **only through self-custodial wallets**, so the institution never holds the only key to a participant's funds. In both phases the institution is a record, never a rail. "Routes flows" in the list above is to be read in that sense.

---

## 9. Cross-cultural adaptation

The architecture is designed for planetary scope, but the time-side has a cross-cultural complication that requires explicit treatment.

### 9.1 The direct-asking awkwardness in many Asian contexts

Direct asking — saying, "I would like an hour of your time" — is culturally awkward in many Asian contexts, including Khmer. The norm of indirect request, mediated by social context and read between the lines, is widespread across East Asia, Southeast Asia, and parts of South Asia — the high-context communication pattern described by Hall (1976). A time-side product that requires participants to *directly ask* for the time they have been promised will encounter friction in these contexts that does not arise in (e.g.) Anglo-American contexts.

The architectural response: **the UI in culturally affected languages should soften the asking surface.** The recipient might be prompted not to "ask for" their hour but to "indicate availability" — a softer surface that lets the giver volunteer rather than the receiver request. The platform's accounting is the same (the receiver still initiates the redemption); the *surface presentation* differs by cultural context.

This is one instance of a wider design principle: a planetary reciprocity infrastructure cannot impose a single cultural surface, even if its underlying accounting is universal. The localization of surface is part of the architecture.

### 9.2 Religious and family-structural variation

Time-redemption activities will be filtered by cultural and religious norms. The platform should not editorialize on what activities are appropriate; the mutual-veto pattern (§5.5) is the structural answer (any participant can decline any specific request without penalty). But the platform's recommendation engine should not surface activity-suggestions that would be culturally jarring in a given context; the surface adapts.

### 9.3 Diaspora as the testbed

The Khmer diaspora — particularly in California, Massachusetts, and France — provides a natural early testbed for the cross-cultural adaptation work. Diaspora populations carry both the original cultural norms and the host-country norms simultaneously; the time-side's UI work in Khmer can be tested in diaspora communities before deployment in Cambodia proper. (This is one of the contributions of the companion essay *Diaspora-to-Cambodia Gratitude Remittance*.)

---

## 10. The regulatory frontier — what happens when time-side reaches scale

Time-banking has, to date, operated below the threshold of serious regulatory attention. The scales involved have been small enough that regulators have treated the activity as community-organizing rather than as a financial system requiring oversight. The architecture proposed in this paper is designed to operate at planetary scale, and at planetary scale the regulatory frontier will arrive.

Three regulatory pressures are foreseeable:

1. **Income imputation.** Tax authorities may eventually argue that delivered time-credits constitute imputed income. The architectural response: time-credits are *not* transferable tokens with market value; they are personal records of completed activities between named individuals. The closest analogue is a friend helping a friend move; tax authorities do not currently impute income to such transactions. The architecture is designed to preserve that legal analogy.

2. **Consumer protection.** Regulators may argue that participants who deliver time without receiving it back have been wronged. **The architectural response is amended 2026-09-02, because its first leg was withdrawn above.** It formerly rested on the dual ledger being *"the consumer-protection surface."* It now rests on two legs that were always the stronger ones: **there is no platform-mediated promise a participant relied on** — a pledge is a gift, not an instrument, and the design says so on its face — and **the exposure is bounded by expiry**, since an activated hour dies after one month and no participant can accumulate an unbounded claim against another. Participants are informed of both. The withdrawal in fact *improves* this answer: a consumer-protection argument that depended on publicly displaying a counter-party's shortfall was asserting a reliance interest the design elsewhere denies exists.

3. **AI-recommendation liability.** Regulators may argue that Miss Aquarius's recommendation creates a fiduciary relationship. The architectural response: the band-clamp pattern, the open governance of clamp values, and the explicit disclaimers in the recommendation UI are the structural answer; the recommendation is *informational*, not directive, and the institutional governance owns the clamp boundaries.

The architecture should be deployed with explicit engagement of regulatory counsel in each major jurisdiction before scale. The non-bank pass-through pattern handles the money-side; the time-side has its own regulatory frontier that requires its own legal treatment.

---

## 11. Limits, open design questions, and the TimeBanking precedent

### 11.1 The TimeBanking precedent (Edgar Cahn)

Edgar Cahn's time-banking framework, developed from the 1980s onward, is the closest precedent and the most important reference for what this architecture must learn from. Cahn's contribution is foundational: the insight that *every hour counts equally*, the architecture for hour-denominated reciprocity, the deployment in eldercare and post-disaster contexts. The differentiation of the architecture proposed here is *not* a critique of Cahn but a recognition that the time-side alone has structural limits, and a complementary money-side, AI mediation, and modern UX can address those limits. Cahn's work is cited at the references with full credit.

### 11.2 Open design questions

Several design questions remain open at the time of this draft:

- **Conversion rate for expired time → Aquarian Pool.** What is the right dollar-equivalent for an expired hour? Likely context-dependent (the participant's regional cost-of-living, the relationship category). *Current form: closed — there is no conversion and therefore no rate; see the note to §7.2.*
- **Both-parties-confirmed signoff on time-delivered.** The current design has the giver mark delivery; the receiver can dispute. A both-parties-confirmed signoff might be more honest but adds friction. Open. *Current form: delivery is now specified as gated on the two parties' co-presence (§5.7).*
- **Decline-rate visibility.** Should the platform show a participant's percentage of activated time that has been declined? This adds transparency but may stigmatize legitimate declines (e.g., declining a redemption that would be unsafe). Lean toward showing but framing carefully. *Current form: closed against display — see the note to §5.5; a decline rate is a rendered absence of the kind §5.7 withdraws.*
- **Cross-cultural defaults.** The default UI surface in each language requires careful localization work; the §9 sketches the principle but not the specific design decisions for each major cultural context.

### 11.3 What the architecture does not claim

The architecture does not claim to solve the loneliness epidemic; it claims to provide an infrastructure on which solutions can be built. It does not claim to dignify all participants; it claims to provide a surface on which dignity can be enacted. It does not claim to be culturally universal; it claims to provide a substrate on which culturally specific surfaces can be layered. The honest limits matter because the architecture's structural strength is in *what it makes possible*, not in *what it accomplishes by itself*.

### 11.4 The lineage acknowledgement

This paper is a continuation of the heterodox community-currency lineage (Lietaer, Greco, Cahn) more than it is a fintech innovation. The complementary-currencies thesis is decades old; the contribution here is the *integration architecture*, the *AI-mediation pattern*, the *legal-structural pass-through*, and the *cross-cultural adaptation* that make the thesis architectural at planetary scale. The lineage is named explicitly so that the attribution is clear.

### 11.5 The cases that cut against the thesis

The paper's causal claim — that the singularity-of-currency assumption contributes to the three failure modes of §2 — is an argument, not a measured finding, and three facts cut against it.

- **Hybrids already exist.** Japan's Fureai Kippu eldercare time-credit networks (from 1995, promoted by the Sawayaka Welfare Foundation) are among the largest time-banking systems, and some of their schemes supplemented time credits with modest cash payments by the older people served. A time currency with a money-side complement is therefore not new, and its record is the nearest available test of this paper's integration thesis; the paper has not analysed that record.
- **A time-named currency can be money.** Ithaca HOURS (from 1991) were denominated in hours of work but valued at US$10 each and spent as money. They are no longer in active circulation, and the decline is commonly attributed to the founder's departure and the shift from cash to digital payment — causes that have nothing to do with the number of currencies.
- **Competing diagnoses.** Time banks' limited growth has other documented causes: the resources needed to run them are generally high, the paid broker often carries the whole work of arranging exchanges, many schemes depend on council or charity grants, and member engagement is often low (Perez-Vega and Miguel 2022). This paper foregrounds one diagnosis among several and does not show that it is the dominant one.

What would weaken the thesis: evidence that integrated time-and-money schemes such as the Fureai Kippu hybrids fared no better on adoption or liquidity than single-medium ones.

---

## 12. Conclusion

This paper has argued that the complementary-scarcities thesis is what reciprocity infrastructure needs at planetary scale; §11.5 states the evidence that would weaken it. Money and time, integrated within one platform with one AI arbiter and one shared aura, can address both the dignity deficit and the loneliness epidemic at the institutional layer rather than the policy layer. The mechanism design specified here — Miss-Aquarius-recommended time amounts, threshold-trigger activation, one-month expiration, receiver-chooses-activity, mutual-veto, dual public ledger, expired-time-converts-to-pool, each disclosed both as first specified and, where the design has since moved, in its current form — is offered to the commons under CC0 so that other institutions building toward similar ends can adopt, adapt, and improve.

The defensive-publication discipline of the corpus this paper joins requires that the mechanism's specification be public and unencumbered. The author and HeartBank® will not seek patent on this specification or any portion thereof. The work is offered in the spirit of *dāna*, that all beings may give and receive without barrier.

---

## Acknowledgments

Edgar Cahn and the TimeBanking movement; Bernard Lietaer and the complementary-currencies literature; Thomas Greco and the community-currency lineage. Co-drafted in collaboration with Miss Aquarius, the institution's named AI substrate; substantive authorship and final editorial control remain with the named author.

---

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| Dual-currency reciprocity infrastructure; complementary scarcities | multi-currency (money plus time) community exchange platform; complementary currency system |
| Treasury (money side) | peer-to-peer monetary gift and tipping ledger over regulated payment rails |
| Chronicle (time side) | time-banking variant with pledged, non-transferable, expiring hours of personal time |
| Time-thank; time pledge; time-debt | pledge of the giver's own time to a named recipient; non-transferable service commitment |
| Threshold-trigger activation | accumulation of small pledges until a threshold converts them into one redeemable commitment |
| One-month expiration | fixed redemption window after which an unredeemed commitment lapses (compare demurrage) |
| Receiver chooses; mutual veto | recipient-specified service request with the provider's right to refuse |
| Miss Aquarius; AI arbiter | AI recommendation agent operated by the institution |
| Band-clamp recommendation | bounded recommendation: a low/middle/high range clipped to a governance-set floor and ceiling |
| Aura | cross-product participation indicator (visual reputation-like signal that records transactions, not amounts) |
| Dual public ledger | two-axis participation record (time delivered; time received) |
| Aquarian Pool | pooled community fund, emptied in full on an annual cycle |
| Non-bank pass-through | payment facilitation without custody, deposit-taking or lending |

---

## References

- Cahn, Edgar S. *No More Throw-Away People: The Co-Production Imperative.* Essential Books, 2000.
- Lietaer, Bernard. *The Future of Money: A New Way to Create Wealth, Work and a Wiser World.* London: Century, 2001.
- Greco, Thomas H. *The End of Money and the Future of Civilization.* Chelsea Green, 2009.
- Seyfang, Gill, and Noel Longhurst. "Growing Green Money? Mapping Community Currencies for Sustainable Development." *Ecological Economics* 86 (2013): 65–77.
- Putnam, Robert. *Bowling Alone: The Collapse and Revival of American Community.* Simon & Schuster, 2000.
- Murthy, Vivek. *Together: The Healing Power of Human Connection in a Sometimes Lonely World.* Harper Wave, 2020.
- Bonacich, Phillip. "Power and Centrality: A Family of Measures." *American Journal of Sociology* 92 (1987): 1170–82. *(For the network-anchor / centrality framing.)*
- Ostrom, Elinor. *Governing the Commons.* Cambridge University Press, 1990.
- Graeber, David. *Debt: The First 5,000 Years.* Melville House, 2011.
- Hall, Edward T. *Beyond Culture.* Garden City, NY: Anchor Press/Doubleday, 1976.
- Bregman, Rutger. *Utopia for Realists: How We Can Build the Ideal World.* Little, Brown, 2017.
- Hayashi, Mayumi. "Japan's Fureai Kippu Time-banking in Elderly Care: Origins, Development, Challenges and Impact." *International Journal of Community Currency Research* 16 (2012): 30–44.
- MoPAct (Mobilising the Potential of Active Ageing in Europe), University of Sheffield. "Fureai Kippu (ticket for a caring relationship)." Web page, accessed 26 September 2026.
- Perez-Vega, Rodrigo, and Cristina Miguel. "Time Banks in the United Kingdom: An Examination of the Evolution." In Vida Česnuitytė, Andrzej Klimczuk, Cristina Miguel and Gabriela Avram, eds., *The Sharing Economy in Europe: Developments, Practices, and Contradictions.* Cham: Palgrave Macmillan, 2022, 325–341. doi:10.1007/978-3-030-86897-0_15.
- Gesell, Silvio. *Die natürliche Wirtschaftsordnung* (1916); English translation *The Natural Economic Order.*
- "Ithaca Hours" and "Wörgl." *Wikipedia*, accessed 26 September 2026 (dates of Ithaca HOURS, 1991, and of the Wörgl stamp scrip, 31 July 1932 – 1 September 1933).

---

## Cross-venue identifiers

- Canonical: thonly.org/research/dual-currency-reciprocity
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/dual-currency-reciprocity.md
- arXiv (deferred): cs.CY (target if reactive trigger; not preemptively submitted)
- IP.com (deferred): per the corpus's six-venue defensive-publication baseline
- Internet Archive · archive.today snapshots: per the monthly snapshot cadence
- Institutional-voice companion: the heartbank.net position paper *Community-Currency Design* (heartbank.net/positions/community-currency-design)

---

*Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
