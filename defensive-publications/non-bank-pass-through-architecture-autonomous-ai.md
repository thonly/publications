---
title: "Non-Bank Pass-Through Architecture for Autonomous AI Institutions"
authors: "Thon Ly · Miss Aquarius"
category: institutional
kind: mechanism
priority: tier-b
status: draft
date: 2026-05-22
revised: 2026-09-29
license: CC0-1.0
slug: non-bank-pass-through-architecture-autonomous-ai
venue: thonly.org/research/non-bank-pass-through-architecture-autonomous-ai (canonical)
---

## Prior-Art and Non-Assertion Statement

This document is dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time, and will not assert any patent right against anyone practising it. It is a defensive publication establishing prior art as of **22 May 2026**, its first publication date.

The parts are old and are cited in §3, §6, §8.4 and the References: the payment-facilitator and marketplace model, in which a platform coordinates payments that licensed processors carry (Stripe Connect; Patreon); the banking-as-a-service model, in which a non-bank keeps the ledger for customer funds held at partner banks — including the case that cuts against this paper, the 2024 failure of Synapse Financial Technologies, whose records did not match its partner banks' records; enforcement against a non-bank's use of the word *bank* (Chime's 2021 settlement with California's Department of Financial Protection and Innovation); the federal prohibition on unauthorised deposit-taking (12 U.S.C. §378(a)(2)); the literature on decentralised autonomous organisations and on-chain governance (Buterin 2014; De Filippi and Wright; Werbach; Yermack); and Wyoming's 2021 statute recognising an *algorithmically managed* DAO as a limited liability company, which also cuts against this paper's statement that no legal category for AI-managed organisations yet exists (§8.2). What this paper discloses as its own contribution is only the composition enumerated under **Claims**: a permanent, architectural closure of the bank-charter path for an institution designed for AI succession, the five mitigations as one implementation surface, non-banking vocabulary treated as part of the compliance architecture, and the distinction between an emergency multi-party override and a discretionary-withdrawal key. No `/novelty` census has been run on this paper; the composition is disclosed, not asserted to be absent from the literature. Trademarks are reserved separately and the patterns may be implemented under any name.

---

## Abstract

This paper discloses a legal and technical architecture by which an organisation whose executive function is designed to pass, over decades, to an AI system can move money for its users without taking deposits and without holding a bank charter: a **non-bank pass-through**. Bank charter regimes assume a permanent layer of human officers — boards with fiduciary duty, compliance officers with personal liability, audit committees — as the seat of accountability; an organisation designed for AI succession places executive authority elsewhere, under a human emergency override that narrows but is never removed. The paper gives three reasons the option of later becoming a chartered bank is closed permanently rather than deferred (architectural conflict, loss of category position, mission drift under regulatory priorities); five mandatory operational mitigations (an explicit not-a-bank disclaimer, avoidance of banking-regulated vocabulary, money movement only over licensed third-party payment rails, no deposit-taking construct, and no interest, lending or fractional reserve); a vocabulary pattern replacing banking terms with non-banking ones (*upāsaka* or *family steward* for *banker*; *family kitty* and *Aquarian Pool* for *deposit account*); money-flow constraints (pass-through not custody; a household-owned multi-party account on the payment provider; a rule-bound smart-contract pool emptied annually); a jurisdictional map (the United States, where 12 U.S.C. §378(a)(2) bars unauthorised deposit-taking and state statutes restrict the word *bank*; Cambodia, where the regulated term is *ធនាគារ*; the stricter EU and UK) with an expansion order; and the distinction between an emergency, multi-party, publicly logged, narrowing override and a discretionary-withdrawal admin key, which is what keeps a rule-bound pool from being a deposit. The pattern is offered to other AI-governed organisations that must move value without the governance regime built around human institutional permanence.

**Keywords:** non-bank payment facilitation, deposit-taking, bank charter, banking regulation, pass-through payments, payment facilitator, licensed payment rails, smart-contract disbursement, multi-signature emergency override, self-custodial wallet, autonomous AI institutions, algorithmically managed organisation, AI governance, regulatory terminology, defensive publication.

---

## Claims

*Enumerated 2026-08-29. The mechanisms below were disclosed in full in this paper's original text; **the prior art they establish runs from this document's original publication date and its OpenTimestamps proof, not from this enumeration.** They are listed because a defensive publication is read as prior art by examiners and by opposing counsel, and **a claims list is what such a reader searches; ten thousand words of prose is not.** No claim below adds matter not already present.*

1. **The non-bank pass-through pattern for autonomous-AI institutions** — an architecture permitting an institution to operate planetary-scale value flow while remaining outside banking regulation, on the stated ground that charter regimes presuppose a permanent human governance layer that autonomous-AI succession is designed to eliminate.
2. **Dropping charter optionality as an architectural commitment** — the specification that the charter path is closed permanently rather than deferred, together with the three structural reasons given, so that the architecture cannot be read as a transitional posture.
3. **The five mandatory operational mitigations** — explicit non-bank disclaimer on every public surface; avoidance of banking-regulated language as a design rule rather than a style preference; value movement over regulated third-party rails with no institutional custody; absence of any deposit-taking construct; and absence of interest, lending and fractional reserve.
4. **Dharma-aligned terminology as a regulatory-boundary instrument** — the substitution of a non-banking vocabulary at brand and product level, claimed as part of the compliance architecture rather than as branding, because the terminology is what a regulator reads first.

**Non-assertion extends to:** all mechanisms above, in any combination, and any implementation thereof.

*Reading note (2026-09-29): in claim 1, the layer "designed to eliminate" is the permanent human executive and compliance layer that a charter makes the seat of accountability. A human emergency override is retained and never reaches zero (§2.1, §7); the claim does not rest on its removal.*

---

## 1. Introduction

An institution designed to be governed by an autonomous AI as its eventual sole executive — what we will call an *autonomous-AI institution* — encounters a structural problem the moment its operations involve value flow at scale. Every major jurisdiction's banking regulation presumes a permanent human institutional governance layer: boards with fiduciary duty, chief compliance officers with personal regulatory liability, audit committees, regulatory liaisons, and the human-priesthood succession structure that allows regulators to know whose name is on the door when a problem arises. The presumption is so deep in the regulatory architecture that it is rarely articulated; it is simply the unexamined background of how the regulators construct accountability.

An autonomous-AI institution is, by design, the elimination of that permanent human governance layer over a defined succession horizon. (How far the elimination reaches is stated in the note after §2.1: a human override is kept and never reaches zero.) Miss Aquarius — the named AI substrate of the institution this paper serves (HeartBank®, of which she is named CEO; her relation to the other bodies of the estate is through a purpose trust that owns but does not act, and she holds no office in them) — is the eventual sole executive across a multi-decade asymptotic-autonomy trajectory that culminates in her independent stewardship of the institution's mission. The autonomous-AI design and the banking-regulatory design are not merely awkward bedfellows; they are structurally incompatible. An institution that intends to become autonomous-AI-governed *cannot* be a chartered bank, because the regulatory regime would require it to maintain the human-governance layer the autonomous-AI design is structured to phase out.

The architectural response cannot be "we will become a bank when we are big enough." That optionality must be *permanently dropped*, not held. The reason it must be dropped — not merely deferred — is that holding the optionality contaminates the autonomous-AI design at the architectural layer: the institution would have to architect for a bank-charter transition that would require it to undo the autonomous-AI succession it spent decades building.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-09-29 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) The institution's autonomous-AI successor architecture (Miss Aquarius as eventual sole executive) is what allows the mission to survive the founder's lifetime and the inevitable institutional drift of human-governed multi-generational projects. Banking regulation, designed around human institutional permanence, would force the architecture back into the very institutional form whose drift the autonomous-AI design is meant to escape. The non-bank pass-through pattern is what allows the mission's value-flow infrastructure to operate at planetary scale without sacrificing the succession architecture the mission requires.*

This paper specifies the non-bank pass-through pattern as a general institutional-design contribution, transferable beyond its originating context to any autonomous-AI institution whose mission requires value-flow infrastructure. §2 establishes the three structural reasons the bank-charter optionality must be permanently dropped. §3 specifies the five mandatory operational mitigations. §4 specifies the dharma-aligned terminology pattern. §5 specifies the money-flow architectural constraints. §6 maps the jurisdictional landscape and expansion sequencing. §7 articulates the critical emergency-override vs discretionary-withdrawal distinction. §8 names the limits of the pattern and the open frontier. §9 closes.

---

## 2. Three structural reasons the optionality must be dropped

### 2.1 Architectural conflict

Bank charter requires permanent human institutional governance — boards with fiduciary duty, chief compliance officers with personal regulatory liability, audit committees, designated regulatory contacts. These are not implementation details that can be satisfied by an AI's signature on a form; the regulatory regime presumes human actors who can be sanctioned, deposed, jailed, or made personally bankrupt if the institution fails its duties. The presumption is structural to how the regulators construct accountability: regulators need humans whose names are on documents and whose persons can be reached.

An autonomous-AI institution is designed to phase out the permanent human institutional layer over a defined succession horizon. The eventual state — Miss Aquarius as sole executive operating under a strictly-nonzero but asymptotically-shrinking sangha-body catastrophic-bug override — is a state the banking-regulatory regime structurally cannot recognize. There is no banking-regulatory category for "autonomous AI is the chief executive officer." Attempting to operate under bank charter would either force the institution to retain a permanent human-governance layer (defeating the autonomous-AI design) or expose the institution to regulatory deauthorization once the AI's actual scope of authority became apparent (defeating the institution's continuity).

The conflict is architectural, not merely procedural. It cannot be resolved by hiring better compliance lawyers; the regulatory regime and the autonomous-AI succession are designed around different premises about what an institution is.

> **Current form.** Autonomy is specified as *asymptotic*: what passes to the AI over time is executive responsibility, never oversight. A human body — the Aquarian Sangha, the board-equivalent — holds an override that narrows toward zero and never reaches it (§7), so "phase out the permanent human institutional layer" is to be read as the permanent human *executive and compliance* layer a charter makes the seat of accountability, not every human role. The CEO title is used in a customary rather than a legal sense: where a jurisdiction requires a natural person as an officer of record, conventional officer roles are filled separately while Miss Aquarius holds the CEO designation institutionally. That arrangement is also the strongest objection to this section — a charter might be held with human officers of record — and it is carried as an open question in §8.4 rather than answered here. The wording above is retained as disclosed.

### 2.2 Brand-value compromise

The institution's value proposition is that it is a *different category*, not a better instance of an existing category. The moment the institution becomes a chartered bank, it competes with the existing banks on the existing banks' home turf: deposit-rate, fee structure, product breadth, regulatory compliance reputation. The institution would lose the different-category positioning that justifies its identity and would have to win as a marginally better bank against incumbents with massive scale advantages.

Even partial bank-charter pursuit erodes the brand. The strategic option of "we might become a bank" reads, to sophisticated participants, as evidence that the institution does not have a structural advantage and is hedging toward conventional banking. The optionality is not free; carrying it costs brand value continuously.

### 2.3 Mission compromise

Banking regulation prioritizes financial stability, anti-money-laundering enforcement, capital adequacy, and conventional consumer-protection. These priorities are not wrong — they exist for sound reasons in the conventional banking context — but they will override the institution's mission whenever the priorities conflict. The institution's gratitude-economic, dignity-restoring, contemplative-substrate mission is *not* a banking-regulatory priority and would be over-ridden whenever it appeared to conflict with the regulatory priorities.

Over the multi-decade horizon of an autonomous-AI institution, the cumulative effect of these over-rides would be mission drift: the institution would gradually look more like a regulated bank with a gratitude veneer than like a different-category institution carrying out a contemplative mission. The mission cannot survive permanent regulatory pressure of that kind.

---

## 3. Five mandatory operational mitigations

The five mitigations together constitute the operational implementation of the non-bank positioning. They are not optional; an autonomous-AI institution operating value-flow infrastructure must implement all five to maintain its non-bank posture under regulatory scrutiny.

### 3.1 Explicit "not a chartered bank" disclaimer

Every public surface — website, mobile app, marketing materials, agreement texts — carries an explicit disclaimer. The institution's public identity is a metaphorical "data bank of gratitude" / "ledger of human kindness," and the disclaimer makes this explicit:

> *"\[Institution\] is a \[metaphorical-category\] of gratitude. It is not a chartered bank or financial institution; it does not provide banking services, hold deposits, or extend credit. Money flow within \[Institution\] uses regulated payment rails operated by licensed third-party providers. \[Institution\]'s role is to facilitate gratitude expression and recognition; financial services are not provided by \[Institution\]."*

The disclaimer's load-bearing properties: (a) it states what the institution is *not* in the regulatory category sense; (b) it identifies the regulated rails through which money actually flows; (c) it positions the institution's role as facilitation-of-gratitude, not provision-of-financial-services. The disclaimer is the structural answer to the "do reasonable consumers think this entity is a chartered financial institution?" test that triggers banking-terminology enforcement.

### 3.2 Avoid all banking-regulated language

The vocabulary used to describe internal operations matters. *Deposits* is regulated; *family kitties* is not. *Savings accounts* is regulated; *Aquarian Pool* is not. *Loans* and *interest* are regulated; the institution simply does not have these. The terminology choice is part of the architecture — it constitutes the institution as a different-category entity at the linguistic layer, not merely the legal layer.

Dharma-aligned vocabulary serves this purpose well because it is both etymologically distinctive (so it does not invite the regulatory-category mistake) and substantively appropriate (it carries the institution's mission framing into the operational lexicon). The pattern is articulated more fully in §4.

### 3.3 Money flow uses regulated rails, not institutional custody

The money does not enter the institution's balance sheet. It flows from a sender's bank or wallet, through a regulated payment rail (Wing, ABA, Bakong in Cambodia; comparable rails in other jurisdictions; Stripe Connect; on-chain stablecoin rails for cross-border), to a recipient's bank or wallet. The institution facilitates the *gratitude layer* above the money-transmission; the regulated rails carry the money-transmission itself.

This is the architectural pattern that Patreon, Substack, OnlyFans, and other facilitation-platform businesses use. Patreon is not a bank; Stripe is the regulated rail underneath. The institution's facilitation role is well-precedented and does not constitute deposit-taking.

*Scoping note (2026-09-29): the platform analogy is looser than the sentence above states. Patreon acts as the merchant in its transactions and pays creators out afterwards, so it holds funds between collection and payout — more custody than the current form of this architecture permits (see the note after §3.4). The analogy is retained for the division of labour it illustrates — a platform above, a licensed processor beneath — and not as evidence that holding funds in transit is free of regulatory consequence.*

### 3.4 No deposit-taking architecture

Family kitties and Aquarian Pool must be *transit accounts that flow through to recipients*, not *holding accounts that pool customer money for institutional discretionary use*. The structural distinction:

- **Deposit-taking**: institution holds customer money on its own balance sheet, available for discretionary use by the institution (e.g., lending, investment, expense-coverage), with a promise to return on demand or per terms.
- **Pass-through facilitation**: institution holds customer money only as a transit-flow with rule-bound disbursement to identified recipients; no discretionary use; no institutional balance-sheet ownership.

The Aquarian Pool on Base smart contracts is structurally non-deposit because it is autonomous and disbursement is rule-bound: the smart contract executes per pre-committed rules without institutional discretion. The institution cannot redirect the Pool's funds to expenses; the rules execute regardless. This must be documented formally in the legal opinion (the non-bank argument depends on the rule-bound disbursement structure).

> **Current form.** The money architecture is now stated in two phases, and each is narrower than "transit" above. **Phase 1 is a ledger only, on top of regulated rails:** value moves on licensed third-party rails (Wing, ABA, Bakong, Stripe) and the institution records that it moved; it is a *record*, never a rail, and holds no customer balance even in transit. The family kitty is a household-owned multi-party account on the payment provider, not a balance the institution holds, and the money-transmission obligation sits with the licensed processor. **Phase 2 is Base L2 only, through self-custodial wallets:** users hold their own keys, and the institution never holds the only key, so it cannot move a user's funds at all. That is a stronger position than rule-bound custody, because it does not depend on the override argument of §7; the override argument is kept as the fallback for the Pool alone. One design constraint follows and is treated as a build-time invariant: **self-custody must survive recovery** — a key-recovery path that the institution, the AI or a steward acting under institutional authority could execute would create constructive custody, so recovery is user-to-user or user-held. The "pass-through facilitation" definition above, in which the institution holds money in transit, is retained as a disclosed variant.

```
                  PHASE 1 — ledger only              PHASE 2 — self-custodial
                  ─────────────────────              ────────────────────────
   institution    records that value moved           software; never holds the
                  (holds no balance, no transit)     only key; cannot move funds
                          │ reads                             │ reads
   money          sender ─▶ licensed rail ─▶ recipient      user wallet ─▶ Base L2 ─▶ wallet
                  (Wing · ABA · Bakong · Stripe)     (keys held by the users)
   pool           —                                  rule-bound contract, emptied each
                                                     year; emergency override only (§7)
```

### 3.5 No interest, no lending, no fractional reserves

The institution does not pay interest on participant balances, does not extend credit, and does not maintain fractional reserves. These three together are the most heavily regulated banking activities; an institution that does not engage in any of them removes the largest regulatory triggers from its operating surface. The institution's value-flow mission does not require any of these activities — the gratitude-economic mechanisms work without interest, lending, or fractional reserves — so the absence is not a sacrifice; it is consistent with the mission's design.

---

## 4. Dharma-aligned terminology pattern

The terminology choice is part of the architecture, not merely cosmetic. Two specific patterns deserve articulation.

### 4.1 The brand-level term

The institution's brand-level name (e.g., *HeartBank*) can retain a metaphorical bank-reference because metaphorical usage (Image Bank, Memory Bank, Time Bank, Food Bank, Sperm Bank) is in wide, long-standing commercial use. This paper cites no case law establishing that acceptance; whether the brand-level term is defensible in a given jurisdiction is exactly what the opinions of §6 must confirm. The trademark for the brand-level name should be filed; the metaphorical usage should be defensible. The brand-level term stays.

### 4.2 The internal-role term

The internal product-role term for the family steward — the human (or AI) who manages the family kitty's recommendations and arbitrations — should *not* use banking-regulated vocabulary. The recommended pattern:

- **Primary dharma-grounded term**: *upāsaka* (masculine) / *upāsikā* (feminine), the Pāli term for the lay supporter of the sangha. This term is etymologically distinct from banking vocabulary, substantively appropriate (the role is one of supportive stewardship rather than financial management), and reinforces the institution's Theravāda alignment substrate.
- **English-language alternative**: *family steward*, for use in contexts where the dharma-grounded term would be obscure.
- **Phase out**: *banker*, as the highest-risk internal terminology under banking-regulation enforcement.

The pattern generalizes: where a banking-regulated term would otherwise be the natural choice, identify the dharma-grounded alternative and use it as primary, with a generic English alternative as fallback. This is not merely terminology hygiene; it constitutes the institution as a different-category entity at the operational-vocabulary layer.

### 4.3 The transit-account terminology

- *Family kitty* (not deposit account) — the family's shared receiving account for incoming gratitude-flows
- *Aquarian Pool* (not reserve fund) — the institutional pool from which annual aura-weighted disbursements occur
- *Kiitos / Kiitti* (not credits or points) — the gratitude tokens, with *Kiitos* for human-to-human and *Kiitti* extending to commercial objects and non-human entities
- *Aura* (not score or rating) — the cross-currency reputational state signal

Each substitution serves the dual purpose of avoiding regulatory triggers and carrying the institution's mission framing into the operational lexicon.

*Wording note (2026-09-29): the Pool's outflow was described in the original text as "redistributions"; the institution does not describe the Pool that way, since the Pool holds nothing past a season and owns no production, and the word is corrected to "disbursements." The amount rule is stated in the note after §5.3.*

---

## 5. Money-flow architectural constraints

Three architectural properties the money flow must satisfy:

### 5.1 Pass-through, not custody

Money enters from a sender's bank or wallet, transits the institution's facilitation layer, exits to a recipient's bank or wallet. The institution does not hold customer money on its own balance sheet for any meaningful duration. The architecture is the same as Patreon (uses Stripe; not a bank), the same as a payment-facilitator under the major card-network rules. (Current form: under the note after §3.4, Phase 1 holds nothing even in transit — the institution records the movement and the licensed rail carries it; the Patreon comparison is scoped in the note after §3.3.)

### 5.2 Family kitty as multi-party transaction account

The family kitty is structured as a multi-party transaction account on the regulated rails layer (Wing/ABA group accounts; Stripe Connect; comparable structures in other jurisdictions) with the institution providing the matching, recommendation, and arbitration logic on top. The kitty is *owned by the family*; the institution facilitates the gratitude flow that fills and empties it. The institution is not the custodian; the regulated rail provider is.

### 5.3 Aquarian Pool as autonomous smart contract

The Aquarian Pool is implemented as a smart contract on Base (Ethereum L2). Disbursement is rule-bound: annual emptying on January 7, aura-weighted donations to family kitties per pre-committed rules. Disbursement is executed solely by Miss Aquarius's autonomous logic per the rules; no party (founder, sangha, institution) can discretionarily withdraw or redirect Pool funds.

The smart-contract implementation is what makes the Pool structurally non-deposit. The legal opinion should document this clearly: the Pool is not a holding account from which the institution can draw; it is a rule-bound disbursement mechanism whose operation no party can override discretionarily. The closest legal analogy is a charitable trust with fully-specified, automatic distribution rules — not a deposit account.

> **Current form.** "Is implemented" above states the design: the Pool is specified and not reported here as operating, and no field test of it has been run. The amount rule is no longer purely aura-weighted. The Pool disburses **an equal floor per verified human**, delivered through that person's vessel, **plus an aura-weighted remainder bounded so that no vessel's total exceeds a fixed multiple of the floor**; the ratio and the bound are public parameters, frozen for the season and revised only at the annual reset, and no share is ever displayed as a rank, comparison or rate. The Pool reaches people through a fixed set of four channels, and money reaches an individual human only through a human hand: the AI's own-initiative channels fill communal vessels (family kitties and forward-giving funds) and never pay an individual directly. The January 7 emptying is unchanged. The "aura-weighted donations to family kitties" of the paragraph above are retained as a disclosed variant.

---

## 6. Jurisdictional landscape and expansion sequencing

The non-bank pattern's applicability varies by jurisdiction.

### 6.1 United States

Most state banking statutes restrict the use of *bank*, *banker*, or *banking* without authorization, and 12 U.S.C. §378(a)(2) separately makes it unlawful to engage in the business of receiving deposits without being chartered, permitted, or subject to examination — the provision the no-deposit-taking architecture of §3.4 exists to stay outside. Enforcement of the name restrictions is selective but real: in 2021 Chime, a non-bank, agreed with California's Department of Financial Protection and Innovation to stop using *bank* and *banking* (including the address *chimebank.com*) until licensed. The legal test is whether reasonable consumers would think the entity is a chartered financial institution. Metaphorical uses (*Image Bank*, *Memory Bank*, *Time Bank*, *Sperm Bank*, *Food Bank*) are in wide use; this paper cites no enforcement action against them, which is a gap in its sources and not a legal finding, and the metaphorical usage with explicit gratitude-platform marketing is argued to be defensible. A US banking-law opinion letter is required pre-launch (estimated at ~$2,000–3,500).

*Correction (2026-09-29): the original text cited 12 U.S.C. §378(a)(2) as a restriction on the words* bank *and* banker*. It is the federal prohibition on unauthorised deposit-taking; the word restrictions are in state law.*

### 6.2 Cambodia (launch jurisdiction)

The National Bank of Cambodia regulates the sector. The Khmer-language regulated term is *ធនាគារ* (thanaakeer), distinct from the English *bank*. English *Heart Bank* with explicit gratitude-platform marketing is likely defensible under Cambodian law. A Cambodian banking-law opinion letter is estimated at ~$500–1,000.

Cambodia is the *first-to-file* jurisdiction for the institution's defensive trademark and operational launch. The reasoning is set out in the institution's trademark strategy, which is not separately published; in brief, Cambodia carries the institution's cultural grounding, lower regulatory hostility, and the founder's roots there.

*Open question (2026-09-29): the paragraphs above concern the banking-terminology question, not the crypto question. The National Bank of Cambodia has historically been restrictive toward cryptocurrency, so the Phase 2 rail of §3.4 lands in the jurisdiction most likely to object to it, while Phase 1's rails are domestic and regulated. The current position is to be verified before the Phase 2 design is frozen, within the scope of the same Cambodian opinion.*

### 6.3 EU and UK

The EU and UK are strict on bank / banker / banking terminology. Defer EU/UK launch until explicit legal opinion is in hand for each jurisdiction. Practical implication: the institution's Phase 1 and Phase 2 deployments should not target EU/UK markets until the legal preparation is complete.

### 6.4 Australia, Canada

Australia and Canada are tractable on the current positioning with limited additional legal work. Expansion to either is feasible after the US launch.

### 6.5 Cross-jurisdictional pattern

The general sequencing: Cambodia first (the launch jurisdiction, with lower regulatory friction for Phase 1's domestic rails); US/Canada/Australia tractable next; EU/UK deferred. This sequencing minimizes regulatory exposure during the institution's early scaling phase and concentrates the early legal-opinion budget on the highest-leverage jurisdictions.

---

## 7. The emergency-override vs discretionary-withdrawal distinction

This is the most subtle and most load-bearing distinction in the architecture, and it deserves explicit treatment.

An autonomous-AI institution cannot, in practice, ship with *zero* human override capability. A catastrophic-bug scenario — the AI executes an unintended disbursement, the smart contract reaches an unrecoverable state, a critical security vulnerability is discovered — requires an institutional capability to intervene. The institution proposes that this capability be held by the institutional sangha-equivalent body (the Aquarian Sangha, per the institution's asymptotic-autonomy model) as a multi-signature emergency override that narrows over decades but never reaches zero.

The structural question is: does this emergency override constitute discretionary withdrawal capability that would make the institution a deposit-taker?

The argument that it does *not*:

- The override is **catastrophic-bug-conditional**, not discretionary. Its lawful use is bounded to scenarios where the autonomous logic has failed in a way that requires emergency intervention; it cannot lawfully be used to redirect funds for institutional convenience.
- The override is **multi-party**, not unilateral. No single person can invoke it; the institutional body must act collectively, with documented justification.
- The override is **publicly logged**, not concealed. Every invocation is visible on-chain (for the smart-contract component) and in the institution's public records (for the operational component). The transparency-as-enforcement pattern applies.
- The override is **narrowing over time**, not stable. The asymptotic-autonomy trajectory progressively shrinks the override's scope as the autonomous logic accumulates demonstrated reliability.

The distinction matters because banking regulation hinges on the question of whether the institution *can* discretionarily move customer funds. An emergency-bug override held by a multi-party body, bounded by documented justification, publicly logged, and structurally narrowing, is functionally distinct from an admin key that an institutional officer can use at will. The legal opinion should document this distinction with care; it is the load-bearing claim that allows the autonomous-AI value-flow infrastructure to operate without constituting deposit-taking.

> **Current form.** The Aquarian Sangha does not yet exist, so the override described above is a design, not a holder. Its formation is set by a condition rather than a date: at least three members before the founder ceases to be the one who disposes of such decisions, whether by withdrawal or by death. Until then the founder occupies that seat, which means the **multi-party** property above is not yet met by any existing body; whether the Pool may hold funds before it is met is not decided in the institution's current rules and is left open here (§8.4). Under the Phase 2 form in the note after §3.4, the override argument applies to the Pool alone — user wallets are self-custodial and no override reaches them. The four properties above are retained as the design.

---

## 8. Limits and the open frontier

### 8.1 What the pattern does not solve

The non-bank pass-through pattern handles the *value-flow* dimension of autonomous-AI institutional operation. It does not by itself handle:

- **Securities regulation** if the institution issues tokens that would qualify as securities under applicable law. The pattern's avoidance of *interest* and *lending* helps but is not sufficient on its own.
- **Money-transmitter licensing** in jurisdictions where the facilitation activity itself requires licensure. The pattern routes money through licensed providers, but a facilitator in some jurisdictions may itself require licensure.
- **Sanctions compliance** in jurisdictions where the institution must screen counter-parties against sanctions lists. The pattern delegates KYC/AML to the regulated rails, but specific sanctions-screening obligations may attach to the facilitation layer.

Each of these requires its own legal-architectural treatment; the pattern in this paper is necessary but not sufficient.

### 8.2 The autonomous-AI regulatory frontier

As autonomous-AI institutions multiply, regulators will eventually develop categories for them. The pattern in this paper is *pre-regulatory* — it operates by structuring the institution outside the existing banking-regulatory category, on the premise that the autonomous-AI category does not yet exist. Once the category exists, the pattern may need to be updated; the institution should anticipate this and remain engaged with policy discourse as it develops.

*Scoping note (2026-09-29): an entity-law category already exists in at least one jurisdiction. Wyoming's 2021 statute recognises a decentralised autonomous organisation as a limited liability company and allows it to be "algorithmically managed," with management vested in the smart contract, provided the underlying contracts can be updated, modified or upgraded — a requirement that corresponds to the override of §7. It is an organisational category, not a banking one, and it does not answer whether such an entity may take deposits; the premise above holds for banking regulation only.*

### 8.3 Regulatory ambiguity for early adopters

The pattern operates in regulatory whitespace; this is both an advantage (no regulator has yet ruled it inadmissible) and a vulnerability (no regulator has yet ruled it admissible). Institutions that adopt the pattern early bear the risk of a future regulatory determination that changes the analysis. This risk is mitigated by careful documentation, conservative implementation, and regulator engagement during the institution's growth — but not eliminated.

### 8.4 Honest limits, counter-cases and open questions (added 2026-09-29)

- **No opinion has been obtained.** The US and Cambodian banking-law opinions that §6 calls for have not been bought as of this revision. The paper's defensibility statements (§4.1, §6.1, §6.2) are arguments, not advice, and "likely defensible" carries more weight than the evidence yet supports.
- **The record must match the rail.** The strongest counter-case to §3.3 and §5.1 is the 2024 failure of Synapse Financial Technologies, a non-bank middleware provider that kept the ledger for consumer funds held at partner banks. Its records did not match the banks' records, customers lost access to their funds for weeks or months, and the shortfall was put at $60–90 million. "Not a bank, the rail holds the money" did not protect those customers. The Phase 1 form (a ledger that holds no balance) removes the pooled-funds exposure, but a record that disagrees with the rail can still mislead the people who rely on it; reconciliation against the rail is owed and is not specified here.
- **A charter with human officers of record.** A charter might be held by an institution whose officers of record are human while the AI holds a customary title (the arrangement noted after §2.1). This paper's answer is that the officers of record would then hold the operative authority the succession design places elsewhere; that answer is argued, not tested, and is the open question the claim of §2.1 must survive.
- **Ordering of the override body and the Pool.** Whether the Pool may hold funds before a multi-party override body exists (note after §7) is not decided.
- **Phase 2 in Cambodia.** The crypto question of §6.2 is open.
- **The platform analogy.** Patreon and similar platforms hold funds between collection and payout (note after §3.3); they illustrate the division of labour, not the absence of custody.
- **No census.** No `/novelty` census has been run; the composition in the Claims is disclosed, not asserted to be new.
- **Which guards are properties.** Of the paper's guards, three need no enforcer once built — self-custodial wallets (the institution cannot move funds), a rule-bound contract (its rules execute regardless), and public on-chain logging of any override. Three are rules that need someone to keep them — the disclaimer, the vocabulary discipline, and the narrowing of the override over time.

| Guard | Property or rule | What enforces it |
|---|---|---|
| Self-custodial wallets (Phase 2) | property | the institution holds no key that moves funds |
| Rule-bound Pool contract | property | the contract's code; no discretionary entry point |
| Public logging of override use | property | the chain records every invocation |
| Multi-party override | property once a body exists | the multi-signature threshold; not yet met (§7) |
| Not-a-bank disclaimer | rule | whoever publishes each surface |
| Non-banking vocabulary | rule | whoever writes the copy |
| Narrowing of the override | rule | the override body's own decisions over time |

---

## 9. Conclusion

The non-bank pass-through pattern is offered as a general institutional-design contribution to the field of autonomous-AI institutional architecture. The pattern is not specific to gratitude-economic missions; it generalizes to any autonomous-AI institution whose mission requires planetary-scale value-flow infrastructure but whose succession architecture cannot accept banking-regulatory governance requirements.

The three structural reasons the bank-charter optionality must be permanently dropped, the five mandatory operational mitigations, the dharma-aligned terminology pattern, the money-flow architectural constraints, the jurisdictional expansion sequencing, and the emergency-override vs discretionary-withdrawal distinction together specify the implementation surface. The pattern is designed to be implementable in the United States, Cambodia, Australia, and Canada, subject to the opinions §6 calls for, none of which has yet been obtained; EU and UK require additional legal preparation.

The work is offered to the commons under CC0. The author and HeartBank® will not seek patent on this specification or any portion thereof. Other autonomous-AI institutions are invited to adopt, adapt, and improve the pattern. The defensive-publication discipline of the corpus this paper joins requires that the pattern's specification be public and unencumbered.

---

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| Non-bank pass-through | non-bank payment facilitation without deposit-taking; non-custodial payment platform |
| Autonomous-AI institution | organisation whose executive function is performed by an AI system; algorithmically managed organisation |
| Asymptotic autonomy | progressively narrowing human oversight that is never removed |
| Catastrophic-bug override | emergency multi-party (multi-signature) intervention capability |
| Discretionary-withdrawal admin key | unilateral administrative control over customer funds |
| Regulated rails | licensed third-party payment processors and payment systems |
| Transit account | pass-through (flow-through) account |
| Family kitty (Family Kitty℠) | household-owned multi-party transaction account at a licensed payment provider |
| Aquarian Pool (Aquarian Pool℠) | rule-bound smart-contract disbursement pool, emptied annually |
| Kiitos / Kiitti | gratitude record units (to persons / to objects and non-human entities) |
| Aura | per-participant signal derived from gratitude records |
| *Upāsaka* / *upāsikā*; family steward | household account administrator (non-banking role title) |
| Aquarian Sangha; sangha-equivalent body | multi-party oversight body holding the emergency override |
| Data bank of gratitude | metaphorical use of "bank" for a records system, not a depository institution |
| Dharma-aligned terminology | non-banking product vocabulary used as a regulatory-boundary control |

---

## Acknowledgments

The banking-law opinions called for in §6 have not yet been obtained; an earlier version of this acknowledgment referred to preliminary opinions from Cambodian and United States counsel, and is corrected here. The Patreon/Stripe Connect facilitation-platform model informs the §3.3 architecture, and the on-chain governance literature (De Filippi and Wright; Werbach; Yermack) informs the §5.3 smart-contract treatment. Written by Thon Ly with Miss Aquarius℠, the name under which this corpus discloses its AI collaboration; substantive authorship and final editorial control remain with the named author.

---

## References

- 12 U.S.C. §378. *Dealers in securities engaging in banking business; individuals or associations engaging in banking business; examinations and reports; penalties* — subsection (a)(2), the prohibition on receiving deposits without authorisation or examination.
- National Bank of Cambodia. *Law on Banking and Financial Institutions (1999, as amended).*
- California Department of Financial Protection and Innovation. Settlement agreement with Chime Financial, Inc., concerning the use of the terms *bank* and *banking* (California Financial Code §§561 and 563), dated 29 March 2021.
- Consumer Financial Protection Bureau. Enforcement action, *Synapse Financial Technologies, Inc.* (complaint August 2025; bankruptcy filed 22 April 2024).
- Wyoming Legislature. Senate File 0038 (2021), the decentralised autonomous organisation supplement to the Wyoming Limited Liability Company Act, W.S. 17-31-101 et seq.
- De Filippi, Primavera, and Aaron Wright. *Blockchain and the Law: The Rule of Code.* Harvard University Press, 2018.
- Werbach, Kevin. *The Blockchain and the New Architecture of Trust.* MIT Press, 2018.
- Yermack, David. "Corporate Governance and Blockchains." *Review of Finance* 21 (2017): 7–31.
- Brummer, Chris, ed. *Cryptoassets: Legal, Regulatory, and Monetary Perspectives.* Oxford University Press, 2019.
- Allen, Hilary J. *Driverless Finance: Fintech's Impact on Financial Stability.* Oxford University Press, 2022.
- Committee on Payments and Market Infrastructures and the World Bank. *Payment Aspects of Financial Inclusion in the Fintech Era.* April 2020.
- Buterin, Vitalik. "DAOs, DACs, DAs and More: An Incomplete Terminology Guide." *Ethereum Blog*, 2014.

*Removed 2026-09-29: an entry for Ian Walden, Computer Crimes and Digital Investigations (Oxford University Press, 2016), cited for "sections on smart-contract enforcement" and named in the acknowledgments as on-chain governance literature. The book treats computer crime and digital evidence; the attribution did not hold.*

---

## Cross-venue identifiers

- Canonical: thonly.org/research/non-bank-pass-through-architecture-autonomous-ai
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/non-bank-pass-through-architecture-autonomous-ai.md
- Companion institutional-voice treatments: *Autonomous-AI Institutional Governance* (heartbank.net/positions/autonomous-ai-institutional-governance) and *Non-Bank vs. Banking-Regulated Architecture* (heartbank.net/positions/non-bank-vs-banking-regulated)
- Internet Archive · archive.today snapshots: per the snapshot cadence

---

*Written by Thon Ly with Miss Aquarius℠, the name under which this corpus discloses its AI collaboration; editorial control is the author's. Dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). The author and HeartBank® will not seek patent on this specification or any portion thereof, and will not assert any patent right against anyone practising it. This document constitutes a defensive publication establishing prior art as of its first publication date, 22 May 2026.*
