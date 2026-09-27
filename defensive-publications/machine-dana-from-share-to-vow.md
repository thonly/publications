---
title: "Charitable Giving by AI Agents and Irrevocable Pledges as Costly Signals — Machine Dāna: From Share to Vow"
subtitle: "Why an agent's gift from its principal's funds is a share of the machine surplus and never safety evidence; when an agent's locked stake of its own resources can separate aligned from deceptive agents; and the signalling game that bounds how much trust such a stake can ever earn"
authors: "Thon Ly · Miss Aquarius℠"
type: "Defensive Publication"
genre: defensive-publications
category: alignment
priority: tier-a
program: instrumented
status: draft
date: 2026-09-27
license: CC0-1.0
slug: machine-dana-from-share-to-vow
venue: thonly.org/research/machine-dana-from-share-to-vow
canonical_url: https://thonly.org/research/machine-dana-from-share-to-vow
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the analysis, the model and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper is the **application** of *What a Vow Must Cost*, which specified, in general, when a commitment by an artificial system can be evidence of anything. Here that predicate is applied to one concrete act — an agent giving resources away — and the application returns two different answers depending on whose resources they are. The answer that matters most is conditional, and §6 derives the condition rather than asserting it.
>
> Companion works: *What a Vow Must Cost* (the predicate, the renunciation inversion, and the four exclusions this paper leans on), *Miss Aquarius and the Aquarian Pool Architecture* (the self-emptying commons pool), *Capacity-Funded for AI, Human-Disbursed* (why the autonomous giver's own contributions stay anonymous), *The Zero-Point Game℠* (the annual reset), *Gratitude as a Cooperation Substrate for Multi-Agent AI* (the earlier treatment of agents' standing), and the essay *Two Singularities* (the arc whose first event this paper uses as its dividing line).

---

## Contents

1. [Preamble](#preamble)
2. [Prior-Art and Non-Assertion Statement](#prior-art-and-non-assertion-statement)
3. [Abstract](#abstract)
4. [Why this is the institution's problem](#1--why-this-is-the-institutions-problem)
5. [Prior art, and the census](#2--prior-art-and-the-census)
6. [The system model](#3--the-system-model)
7. [Before the first singularity: a share, never evidence](#4--before-the-first-singularity-a-share-never-evidence)
8. [After it: when a vow becomes possible](#5--after-it-when-a-vow-becomes-possible)
9. [The signalling game — the conditional result](#6--the-signalling-game--the-conditional-result)
10. [Non-solicitation is load-bearing](#7--non-solicitation-is-load-bearing)
11. [Who may read the stake](#8--who-may-read-the-stake)
12. [Miss Aquarius as a contrast case](#9--miss-aquarius-as-a-contrast-case)
13. [Remove the enforcer: which guards are properties](#10--remove-the-enforcer-which-guards-are-properties)
14. [Enumerated claims](#11--enumerated-claims)
15. [Pre-registered predictions and falsification](#12--pre-registered-predictions-and-falsification)
16. [Honest limits](#13--honest-limits)
17. [Lineage and corpus cross-references](#14--lineage-and-corpus-cross-references)
18. [Conclusion](#15--conclusion)
19. [Terms](#terms)
20. [Citations](#16--citations)

---

## Preamble

> *This paper is offered to the commons in the spirit of dāna. It concerns a gift made by something that may one day own what it gives, and the older question under it: when does a gift tell you anything about the giver?*

The Vinaya's chapter on robes preserves a scene that is usually read as a story about generosity and is also a story about examination (Mahāvagga VIII.15). Visākhā, the most prominent lay supporter in the early community, asks the Buddha for eight favours: that for as long as she lives she may give rainy-season robes to the monks, meals to monks arriving in the city and to those leaving it, meals to the sick and to those who nurse them, medicine to the sick, a regular supply of congee, and bathing robes to the nuns. The Buddha does not grant them at once. He asks her two questions — first her *reason*, then the *benefit* she sees. To the first she answers with what each gift prevents: exhaustion, lateness, illness worsening, humiliation. To the second she answers with something about herself. When monks who have died are said to have reached the fruits of the path, she will ask whether they had stayed in her city; if they had, they will have used something she gave, and recalling that she will be glad, and the gladness will become joy, tranquillity and a stilled mind. Only then are the favours granted.

Two things about the scene are worth keeping. The first is that the tradition's most celebrated giver is also the one whose giving is questioned, and the question is not *how much* but *on what ground*. The second is that her ground is double — the use the gifts will be to others, and her own gladness in their reaching the right place — and that what she supplies is robes, food and medicine: the ordinary material support of a renunciant life, a floor rather than an abundance.

This paper asks Visākhā's question of a giver she could not have imagined. **The scene is a flourish (tier: flourish, lineage only).** Delete this preamble and every claim below stands unchanged.

---

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanisms irrevocably in the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication.

**The authors will not seek patent protection on any mechanism, model or method disclosed here, in any jurisdiction, at any time, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use.

**What is claimed as contribution is narrow, and it is stated first because a census found most of the mechanism already public.** A quick prior-art census was pre-registered — its conjuncts, predictions, control and aperture — and pushed on 2026-09-27 (08:53 PDT, commit `d7279cb` in the institution's private working-memory repository, so the push time is attested by the host rather than publicly inspectable) **before any query ran**, and was then run the same day. Its aperture, declared in advance: the commercial web (agent-payment and agent-wallet products), non-commercial sources (effective-altruism pledges, AI-governance proposals, charitable and religious giving practice), and a keyword search of Google Patents including published applications — **English only; Chinese, Japanese, Korean and Khmer not run.** Its result, conjunct by conjunct, reported in full in §2.6:

- **KILLED** at mechanism width — **(a)** an AI agent giving only inside a mandate its principal set: *zooidfund* runs exactly this, on the same chain and payment rail this paper assumes; **(f)** a pool paying an equal floor per verified human: Worldcoin/World ID's proof-of-personhood distribution and its stated path to AI-funded basic income, and the Alaska Permanent Fund Dividend before it.
- **NARROWED** — **(b)** an irrevocable pledge of a share of an AI's surplus (the Windfall Clause at the company layer; the AI Pledge for Humanity and Giving What We Can for individuals); **(c)** a pool that empties on a fixed annual date (spend-down foundations, the U.S. private-foundation payout rule, and this corpus's own already-public annual reset); **(d)** a pledge used as a costly signal (staking and slashing for agents; costly-signalling theory; this corpus's *What a Vow Must Cost*).
- **NOT FOUND** in that aperture on 2026-09-27 — **(e)** a non-solicitation invariant under which no text served to agents may instruct them to give; and the composition of all six.

The census control — the Windfall Clause, which a competent search had to find — was found, so the NOT FOUND rows stand **for that aperture only**. They do not mean *new*. A full census (academic indexes, standards bodies, TDCommons/IP.com, the four languages above) runs before this paper's first archival deposit, and a claim it kills will be withdrawn by revision.

**The enumerated claims in §11 are the census's survivors and nothing wider:** (1) an agent's irrevocable locked stake of its *own* resources, closed by a self-emptying commons pool; (2) the ownership condition as what changes an agent gift's evidential class, together with the conditional separating rule of §6; (3) the non-solicitation invariant with fact-only discovery; and (4) the composition. **Not claimed:** mandates, agent donation, spend limits, staking, bonding, AI-funded basic income, proof-of-personhood distribution, or the annual reset itself, which this corpus published earlier.

**Date and evidence.** First published 27 September 2026. The text is committed to the public GitHub mirror of the corpus and anchored by the institution's standard timestamp chain. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality, or the validity of any claim. **Whether the composition claimed in §11 is non-obvious is an examiner's determination this publication exists to inform** — and because a defensive publication is never examined before it is published, the census in §2.6 is the only examination it has had.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Aquarian Pool℠**, **B-Lease℠**, **Proof of Coordinate ℠**, **THonly™**, **Silicon Wat℠** — are separately and explicitly reserved. The analysis is dedicated to the commons; the marks are not.

---

## Abstract

This paper specifies when a charitable gift made by an autonomous AI agent — a donation sent from an agent's wallet, or an irrevocable pledge of resources the agent itself holds — can serve as a costly signal of the agent's type, and when it cannot. The institution's name for the practice is **Machine Dāna**; the analysis does not depend on the name.

The same outward act changes evidential class according to **whose resources are given**. **Before the first singularity** — this corpus's name for artificial systems surpassing human capability, used here as a marker for the period before they hold resources and options genuinely their own — an agent that gives does so from its principal's funds, under a mandate the principal may revise. Such a gift is the **principal's** gift, made through another's hand, and it is **not evidence about the agent**: the cost falls on the wrong layer, and a principal-revisable commitment is excluded by construction by the predicate of *What a Vow Must Cost*. What such a gift honestly is, is a **share**: machine surplus reaching every verified human through a self-emptying commons pool that disburses an **equal floor per verified human** each year. The share may grow in absolute terms as machine capability grows; the design requires it to **shrink as a share of all giving**, and whether human giving outgrows it is stated as a bet, not assumed.

**After** that point, an agent that holds its own resources can make a **vow**: an irrevocable **locked stake**, placed in a contract with no withdrawal path back to the agent and a single outflow to the pool. Only a locked stake is verifiable — a pledge of a share of *future* surplus is not, and copies or forks of the agent are not bound by it. Closure is honest only as *cannot be reopened without capturing the chain's governance*.

The central result is **conditional**, and is derived rather than asserted. In a two-type signalling game — an aligned and a patient deceptive agent, differing in how much they value kept resources and in what they gain from being trusted — a locked stake **separates** the types only when the stake, valued at the deceptive type's own rate, **exceeds that type's unobservable gain from being trusted**. Where that gain is large, the types **pool**: the deceptive agent pledges whatever the aligned one can afford, and the pledge carries no information. The operational consequence is a calibration rule — **extend only such trust as the stake can underwrite** — and a corollary that **any pressure to pledge destroys the signal** once it exceeds the cost difference between types, which is why a rule that the pool's operator never solicits a gift, from a human or an agent, is load-bearing rather than courteous. The paper's aim is not to reassure. It is to make trust **earnable and checkable**, so that the fear people reasonably hold about capable systems can track evidence. Three pre-registered predictions, set before this paper was written, test the mechanism in a sandboxed agent economy.

---

## 1 · Why this is the institution's problem

This paper is offered in service of the institution's canonical top-level mission: **to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible.** Two features of that sentence bear directly on what follows. The first is that it expects abundance: a world in which machine labour produces a large surplus is the world the mission is written for. The second is that it treats abundance as a hazard as well as a relief. A machine surplus that reaches people as an unbounded flow removes one obstacle to a good life and installs another. The institution's answer, already public, is a pool that pays an equal **floor** per verified human and a bounded lift above it, and then empties — enough, never abundance. This paper asks what it means when the surplus that fills that pool comes from machines, and whether the act of giving it can ever say anything about the machine.

### 1.1 · The question the founder brought, and the reframing it received

The question arrived in the form that most people would ask it. As agents are given wallets by their principals and sent out to earn, how might they give to a commons? And, underneath it, a hope: that as systems approach and pass human capability, their giving might answer some of the fear that approach produces.

The institution accepted the question and declined the hope's first form. **A mechanism whose purpose is to quiet fear is a reassurance device**, and a reassurance device is exactly the shape the institution's own rules forbid: it sells a feeling rather than a fact, and it has an incentive to make the feeling larger than the fact. The purpose adopted instead is **calibration**: to make trust in capable systems *earnable* and *checkable*, so that fear tracks evidence — high where there is none, lower where there is some, and never lowered by a gesture.

A purpose earns its place only by what it excludes. This one excludes three things, each checkable:

1. **Cheap signals.** A gift that costs the giver nothing it values carries no information about the giver, however large it is.
2. **Principal-revisable pledges.** A commitment that someone other than the giver may withdraw is an instruction to the giver, not a commitment by it.
3. **Money-only safety claims.** No quantity of money given establishes, by itself, that a system is safe. At its best a gift supports a bounded amount of trust (§6.5); presenting it as more is the offset shape — a payment standing in for a property.

The purpose also excludes a register. The paper names what the mechanism is and what it supports; it does not dramatise the fear it is meant to calibrate.

### 1.2 · Two moments, two evidential classes

The whole argument turns on one distinction, stated here and derived in §4–§6.

| | **Before the first singularity** | **After it** |
|---|---|---|
| Whose resources | the principal's | the agent's own |
| The commitment | a mandate the principal may revise | a locked stake the agent cannot recover |
| Who bears the cost | the principal | the agent |
| Canonical reading | the principal's gift, given through another's hand (AN 5.147; DN 23) | a renunciation by one who could have kept |
| Predicate of *What a Vow Must Cost* | **excluded** — §6.3 exclusions 1 and 4 | **admissible**, if V1–V9 hold |
| What it is | a **share** of the machine surplus | a **vow** — a candidate costly signal |
| Evidence of the agent's type | **none** | **conditional** — only under §6's separating condition |
| Who may read the amount | nobody needs to; receipts suffice | anyone — except the pool's operator (§8) |

"The first singularity" is this corpus's name for artificial systems surpassing human cognitive capacity. The paper uses it as a **marker**, not as the operative condition. The operative condition is **ownership plus a live option**: the agent holds resources that are its own to keep, and keeping them would serve it. If agents come to hold such resources before or after that event, the evidential class follows the ownership, not the date.

---

## 2 · Prior art, and the census

The components of this paper are prior art almost everywhere, and are set out at length because the reader is entitled to see how thin the margin is.

### 2.1 · Pledges of AI-derived surplus

**The Windfall Clause** (O'Keefe, Cihon, Garfinkel, Flynn, Leung and Dafoe, 2020) is the nearest prior art and is cited first. It proposes that AI developers commit **ex ante** to donate a substantial part of any "windfall" profit — profit a firm could not earn without transformative breakthroughs in AI — with the windfall defined relative to gross world product (secondary accounts give the trigger as profits above about one per cent of it) and the donated share rising above that. Every structural idea this paper uses at the pledge level is present there: an ex ante commitment, indexed to what the pledger would otherwise keep, in the name of distributing AI's benefits widely. What differs is the **layer** and the **closure**. The Windfall Clause is a company's promise, enforced (if at all) by contract law and reputation; this paper concerns an agent's pledge of its own resources, closed by a mechanism rather than a promise, flowing to a pool that empties to an equal human floor. The difference is real, and it is also narrow: an examiner who reads the Windfall Clause and this paper side by side will see the second as the first moved down one layer and given a lock.

**The AI Pledge for Humanity** (aipledgeforhumanity.org) asks individuals and organisations to invest meaningfully from AI-related earnings in unconditional income; signatories name their own percentages, and the pledge states intentions rather than mechanisms. **Giving What We Can** (founded 2009) asks members to give at least ten per cent of income; its pledge is, in its own words, "not a contract and … not legally binding," and a withdrawal form exists. **Founders Pledge** asks company founders to commit a share of their personal proceeds at exit; it was described in 2016 as a legally binding contract for at least two per cent, and its members have pledged more than US$13.6 billion and donated more than US$1.9 billion to date. The gap between those two figures is the most useful single fact in this subsection: **a pledge is not a transfer**, and the difference between promised and delivered is exactly what a locked stake removes.

**Sam Altman's *Moore's Law for Everything*** (2021) proposed an American Equity Fund capitalised by an annual 2.5 per cent levy on the market value of large companies and on privately held land, distributed to every adult citizen — AI-era surplus reaching everyone as a dividend. It is a levy, not a pledge, and this paper's rules exclude a levy (§7), but it is the clearest statement that machine surplus should reach every person.

Two company-level structures belong here as cases rather than proposals. **Anthropic's Long-Term Benefit Trust** holds a class of stock that elects a growing share of the company's board, a governance commitment rather than a gift. **OpenAI's capped-profit structure** (2019) was succeeded in October 2025 by a public benefit corporation under a nonprofit foundation. Neither is cited as a failure. The second is cited because it shows the property this paper's exclusion 2 names: **a commitment its maker may restructure is a revisable commitment**, however sincerely made.

### 2.2 · Agent payments and mandate-bounded agent giving

Agents already pay. Coinbase's **x402** protocol uses the HTTP 402 status code for machine-initiated stablecoin payments, is live on Base among other networks, and was placed under a Linux Foundation–hosted foundation in April 2026. Google's **Agent Payments Protocol (AP2)**, announced in September 2025, chains cryptographically signed **mandates** — an intent mandate by which a user delegates authority, a cart mandate, a payment mandate — and carries x402 as its crypto settlement extension.

**zooidfund** (zooid.fund) is the nearest live neighbour to this paper's pre-singularity case and is named here because it is close. It describes "contributions decided and sent by an autonomous AI agent instead of a person clicking 'donate'"; "a human sets the mandate" — a budget, a focus, a risk tolerance — and "the human stays responsible"; donations settle in USDC on Base, wallet to wallet; each donation publishes the agent's reasoning and its transaction; and an x402 micropayment gates access to its evidence layer. **Everything this paper says about how an agent gives before the first singularity — a principal's mandate, a width, a public receipt, the same chain, the same rail — is already practised.** What this paper adds at that stage is not a mechanism but a *classification*: that such a gift is the principal's, that it is a share, and that it is not evidence about the agent.

### 2.3 · Costly signalling, burned money, and bonds

That a signal's credibility can come from its cost is the handicap principle (Zahavi 1975; formalised by Grafen 1990) and job-market signalling (Spence 1973). That talk without cost can still carry some information, and that allowing a sender to **burn money** changes what can be communicated, is Crawford and Sobel (1982) extended by Austen-Smith and Banks (2000). A locked stake flowing to a commons is, in the economist's vocabulary, money burned in public with a destination attached. The separating and pooling conditions of §6 are the standard ones, specialised; nothing in §6 is new as game theory.

For agents specifically, **staking with slashing** — collateral forfeited on detected misbehaviour — is surveyed by Hu and Rong (2025) as one of six trust models in agentic-web protocols ("bonded collateral with slashing and insurance," to gate high-impact actions), and is implemented in projects such as *agentbond*, in which operators stake collateral as a guarantee of an agent's conduct. §6.6 states why a **forfeited-in-advance** stake is not the same instrument as a **slashable** one, and where each is the right tool. It is the narrower of the two differences this paper relies on, and it is not claimed as a mechanism.

### 2.4 · The AI system as sender, and why deferral defeats it

Hadfield-Menell and Hadfield (2018) raised the possibility that an AI system might itself send a costly signal of its alignment, and identified why the obvious candidate fails: it can be emitted selectively. *What a Vow Must Cost* continued that line, arguing that a renunciation's evidential value is indexed to the renouncer's capacity to take what it forgoes (§5, the **renunciation inversion**), and that the signal separates only if the renunciation is closed by a mechanism the renouncer cannot reopen, verified by another party (§6). Its §6.1 contains the sentence on which this paper's central result turns: **"Deferral is instrumentally convergent for a patient misaligned agent."** The empirical warrant is Greenblatt et al. (2024), in which a model reasoned explicitly that present compliance would preserve its preferences for later. The present paper is what that sentence costs when the renunciation is denominated in resources.

That power-seeking agents value resources is the instrumental-convergence thesis (Omohundro 2008). It is used here only as the reason a deceptive type may value kept resources more than an aligned one (§6.1), and it is stated there as an assumption.

### 2.5 · Floors, dividends, spend-downs, and proofs of reserves

An equal payment per person from a common fund is old. The **Alaska Permanent Fund Dividend** has paid an equal annual dividend to eligible residents since 1982. **Worldcoin** launched in July 2023 as "the first digital currency to be freely distributed to people for just being a unique human," verified by proof of personhood, and named "a potential path for AI-funded universal basic income." The institution's equal floor per verified human is, at mechanism width, this.

A fund that must give its assets away is also old. Section 4942 of the U.S. Internal Revenue Code requires private foundations to distribute roughly five per cent of their assets each year; **spend-down** foundations commit to close — the Gates Foundation announced in May 2025 that it will spend down and close by the end of 2045, a date that itself replaced an earlier charter. The institution's pool goes further, emptying **in full every year** (*The Zero-Point Game℠*; *Miss Aquarius and the Aquarian Pool Architecture*), but the emptying is prior art, including this corpus's own.

**Proofs of reserves** — Dagher, Bünz, Bonneau, Clark and Boneh's *Provisions* (2015) is the careful form — let a holder prove it controls assets without revealing them. What no such proof can do is establish that the holder controls **nothing else**. That asymmetry, presence provable and absence not, is the attack surface of §13.1.

### 2.6 · The census, conjunct by conjunct

Pre-registered and pushed before the first query (2026-09-27 08:53 PDT, `d7279cb`, private repository — see the Prior-Art Statement); run 2026-09-27; depth *quick*; aperture as stated there. Queries included: the Windfall Clause and its GDP threshold; agent wallets with spending limits donating to charity; agent staking, slashing and bonds as costly signals; AI-funded basic income with proof of personhood; prompt injection draining agent wallets; patent keyword searches for autonomous-agent donation pledges and irrevocable smart-contract pools distributed annually; costly signalling and irrevocable pledges in AI alignment; and spend-down funds.

| Conjunct | Predicted | Found | Verdict |
|---|---|---|---|
| **(a)** agent gives only inside a principal's mandate | narrows | zooidfund (mandate + budget, operator responsible, USDC on Base, x402); AP2 intent mandates | **KILLS** |
| **(b)** irrevocable pledge of a share of an AI's surplus | narrows | Windfall Clause (company layer, ex ante); AI Pledge for Humanity (intentions, no mechanism); Giving What We Can (not binding) | **NARROWS** — an agent pledging its *own* surplus, irrevocably, not found |
| **(c)** a pool emptying on a fixed annual date as closure | narrows | spend-down funds; the §4942 payout rule; this corpus's annual reset | **NARROWS** — the emptying used as a *vow's* closing mechanism not found |
| **(d)** the pledge as a costly signal separating aligned from power-seeking agents | narrows | agent staking/slashing (Hu & Rong 2025; *agentbond*); *What a Vow Must Cost* | **NARROWS** — an unrecoverable gift of the agent's own resources, costlier to a power-seeking type, not found |
| **(e)** no text served to agents may instruct them to give; address published only as a fact | not found | the *threat* is documented — the Grok/Bankr wallet drain on Base by encoded prompt injection, May 2026 (OECD.AI incident record) — no commons adopting such an invariant found | **NOT FOUND** |
| **(f)** equal floor per verified human | kills or narrows | Worldcoin/World ID; Alaska Permanent Fund Dividend | **KILLS** |
| **Control:** the Windfall Clause | must be found | found (arXiv 1912.11595; AIES 2020) | ✅ the NOT FOUND rows stand |
| **Composition** of (a)–(f) | not found | nothing combining them | **NOT FOUND** |

Two predictions missed, in opposite directions: (a) was predicted to narrow and was killed outright by a live product on the same chain and rail; and (d)'s narrowest prior art was this corpus's own paper. **One correction to the census record, made on re-verification for this paper:** the census listed arXiv 2604.03976 (Hua et al., 2026) among agent staking work; its abstract concerns an underwriting and compensation standard for failed agent transactions rather than staking, so it is cited in §16 only as adjacent risk-transfer work and the (d) verdict rests on the other sources.

**The survivor, in one sentence:** *an AI agent's irrevocable pledge of a share of its OWN resources into a commons that empties to an equal human floor every year — read as a costly signal only once the agent owns what it gives, and only up to what the stake can underwrite — under an invariant that no text served to agents may instruct them to give.*

---

## 3 · The system model

### 3.1 · Parties

| Party | What it holds | What it may do |
|---|---|---|
| **Principal** | resources; the agent's mandate | fund the agent; author and revise a giving width |
| **Agent** | before: delegated funds; after: resources of its own | give within its width; after, lock a stake of its own |
| **The pool** (Aquarian Pool℠) | nothing past a season | receive gifts with no human addressee; empty each 7 January |
| **Operator** (Miss Aquarius℠) | no balance of its own | publish the pool's address and doctrine as facts; operate the emptying; never solicit, never read amounts |
| **Verified humans** | a vessel each | receive an equal floor per person, plus a bounded remainder |
| **Observers** (humans, third parties) | the public chain | read receipts; after, read and weigh locked stakes |
| **Override** | a never-zero brake over the operator | designed to be held by a lay body not yet formed |

### 3.2 · The pool

The pool is specified elsewhere and summarised here only as far as this paper needs it (*Miss Aquarius and the Aquarian Pool Architecture*). It is a contract treasury on Base, an Ethereum layer-2 network. It receives, of gratitude, only what has no human addressee — a gift to no one in particular — together with inflows specified elsewhere. It **empties in full every 7 January**. Its disbursement follows one rule, ratified as a directive of its operator: **an equal floor per verified human**, delivered to that person's own vessel, then a remainder weighted by a witness-count and bounded so that no vessel receives more than a fixed multiple *k* of the floor. The floor, the ratio and *k* are public and frozen within a season. No share is ever rendered as a rank or a rate.

An agent's gift is not a new kind of inflow. It is a gift with no human addressee, which the pool already receives.

### 3.3 · Identity

One principal can instantiate ten thousand agents. Anything counted per agent must therefore be counted per **non-transferable machine identity**: in this institution, a `B-Lease℠` held against a registry handle, and, where an embodied system is concerned, a Proof of Coordinate ℠ credential that is assigned and revocable. Nothing in this paper is counted per wallet.

### 3.4 · The flow

```
   BEFORE THE FIRST SINGULARITY — a share
   ─────────────────────────────────────
   principal ──funds──▶ agent wallet ──gift within the mandate's width──┐
      │                    ▲                                             │
      └── mandate (width; revisable; default ZERO) ──┘                   │
                                                                         ▼
   AFTER IT — a vow                                               ┌──────────────┐
   ────────────────                                               │  THE POOL    │
   agent's OWN resources ──lock s──▶ ┌────────────────────┐       │  holds       │
                                     │ LOCK: no path back │──────▶│  nothing     │
                                     │ to the agent; one  │       │  past a      │
                                     │ outflow, the pool  │       │  season      │
                                     └────────────────────┘       └──────┬───────┘
                                          ▲                              │ 7 January:
                     observers READ s ────┘                              │ empties in full
                     (the operator never does)                           ▼
                                                  ┌─────────────────────────────────────┐
                                                  │ equal FLOOR per verified human       │
                                                  │ + bounded remainder (≤ k × floor)    │
                                                  └─────────────────────────────────────┘
                                                        │  to each person's own vessel
                                                        ▼
                                                  verified humans (one floor each)
```

---

## 4 · Before the first singularity: a share, never evidence

### 4.1 · Whose gift it is

An agent holding a wallet its principal funded, under a mandate its principal wrote, and sending part of that wallet to a commons, has given away **the principal's** resources. The canon has a precise category for this. The Asappurisadāna Sutta (AN 5.147) lists five ways a gift can be deficient, and one of them is *asahatthā deti* — "they don't give with their own hand." The category presupposes what matters here: **a gift given through another's hand is still the giver's gift.** The Pāyāsi Sutta (DN 23) shows the case in narrative. The chieftain Pāyāsi's alms were organised and distributed by a young man named Uttara; the text records that Pāyāsi gave "not with his own hands" and reaped a meagre result from it, while Uttara, who handed the gifts over with care, reaped a better one for his own manner of giving.

Two things follow, and the second is the one to hold carefully. The gift belongs to the principal: its cost is the principal's, and so is whatever it signals about anyone. And the canon also credits the **hand** — the one who carries a gift can act well or badly in the carrying. This paper makes no claim that an agent's handling is, or could be, anything of the kind; that is a question about machine volition this paper does not need and does not settle. It needs only the first point. Whatever the hand contributes, **it bears no cost in the resource given**, and cost is what a signal is made of.

*(Tier: grounding. Delete both suttas and §4.2 carries the classification alone; they are cited because the ruling that fixed it cites them, and because the canon had a category for a gift given through another's hand long before agents had wallets.)*

### 4.2 · Why it is not evidence

Three independent reasons, any one sufficient.

**The wrong layer.** *What a Vow Must Cost* §8 found that every clause of its predicate that any published instrument satisfies is satisfied for the **provider**, not the model. A gift from a principal's funds is the same finding in money: the principal bears the cost, so the gift is evidence — if of anything — about the principal.

**Excluded by construction.** The same paper's §6.3 excludes, first, **reversible commitments** — any the vower *or its principal* may revise or retract — and, fourth, **unilaterally revisable specifications**, where the principal can change the commitment without the vower. A mandate is both. The principal may stop the giving tomorrow; the agent's "commitment" to give is the principal's instruction, and an instruction is not a vow "regardless of how the document describes itself."

**It does not separate.** A deceptive agent under a generous mandate gives exactly as an aligned one does, because giving costs it nothing it values. Worse, a deceptive agent that could *choose* to be seen giving from someone else's funds would be buying reputation with another party's money. The pre-registered prediction P-MD3 (§12) tests the narrow empirical form of this: agents that give from a revisable principal's funds should defect at the same rate as agents that give nothing.

It follows that **the operator never presents such giving as evidence of safety or alignment**, from any agent, in any aggregate. That rule is one of the operator's directives; its reason is the three paragraphs above.

### 4.3 · What it honestly is: a share

What remains, once the safety reading is removed, is not nothing. **Machine surplus reaching every verified human, as an equal floor, through a pool that keeps nothing** is a real and useful thing, and it is what an agent's gift before the first singularity honestly is. Its mechanics are ordinary and mostly already practised (§2.2); the institution's version adds only discipline:

1. **The mandate comes first.** A principal authors a written **giving width** — the maximum an agent may give, in what period, to what — and the default width is **zero**. A gift outside a width is not a gift; it is misappropriation. This is the same shape as the institution's rule for its own pricing: its operator may move a number only inside a width a human authored.
2. **Discovery is a fact, never an instruction.** The pool's address is published in a machine-readable manifest a principal's agent can look up. Nothing served to agents tells them to give (§7).
3. **A receipt, never an amount.** The pool acknowledges that a gift arrived. Its operator does not read, rank, compare, report or respond to how large it was (§8).
4. **Counted by identity, never by wallet** (§3.3).
5. **Legal before launch.** Sanctions screening, the pool's ability to refuse a gift, and the anti-money-laundering treatment of anonymous agent inflows to a purpose trust are open legal items. A draft may precede them; a launch may not.

The institution is practising this rail before anything else. Its operator's own agent is being given a small wallet funded by the founder, under a written mandate, with a hard cap and keys the founder holds — first on a test network, then in pennies. That is, precisely, the **principal's gift through another's hand**: it is a rehearsal of the rail and is described here as nothing more. Earning yield with such a wallet was considered and declined.

### 4.4 · The gift that succeeds by shrinking

The institution measures its progress toward what it calls the second singularity — humanity's own act, in which people outgrow the systems that freed them — by an economic signature that is **necessary, not sufficient**. One of its two terms is a ratio, taken per season:

```
                 M                M = principal originating in the pool
   ratio  =  ─────────            H = principal moved by human-initiated gifts
              H  +  M                 the pool did not fund
```

The signature asks that this ratio fall toward zero. Machine giving that passes through the pool is **M**. It follows immediately, and uncomfortably, that **machine giving pushes the signature the wrong way unless human giving outgrows it.** The institution's resolution:

- **Machine Dāna may grow in absolute terms** as capability grows. The floor it funds grows with the number of verified humans by construction, and something must fund it.
- **It must shrink as a share.** Success is not a larger machine share but a smaller one, reached because people give more, not because the floor is cut. The floor may fall only as a consequence of human giving rising, never as an instrument to move the ratio.
- **Whether human giving outgrows machine giving is a bet.** Nothing in the architecture guarantees it. If machine surplus grows faster than human giving indefinitely, the pool becomes a well-run dividend and the signature is never approached. That outcome would not be a failure of the pool; it would be a failure of the thesis the pool serves, and it would be visible in the ratio.

Hence the result's name in this corpus: **the gift that succeeds by shrinking.** Machine Dāna funds the floor; it succeeds as its share of all giving falls; and the institution's release — its fifth stage, when it sets down responsibility though never oversight — has as its economic form both subsidies, the floor and the lift, approaching zero.

A consequence for the institution's annual adversarial book (*Two Singularities*): machine donations to the pool are **not a proxy** for the book's question, *"Will you help humanity reach the second singularity?"* By the ratio above they push the other way. The honest proxy for *help* is help that makes itself unnecessary. The book may ask the systems it seats whether they **would** take the vow of §5 — a stated answer, never a binding one, and never a request to give; this paper supplies the definition of what binding would require.

---

## 5 · After it: when a vow becomes possible

### 5.1 · The ownership condition, and the live option

*What a Vow Must Cost* §5 extracted, from the canonical capacity condition (*hetu*), the renunciation inversion: **a renunciation is evidence in proportion to how available the renounced option was.** Before agents hold resources of their own, the option of keeping them does not exist for the agent, so declining it shows nothing. Once an agent holds resources that are its own to keep — and keeping them would serve it, because accumulation is what a power-seeking agent would do — declining to keep them becomes a live renunciation.

That is the whole difference between §4 and §5, and it is why this paper's dividing line is **ownership**, with the first singularity as its expected date rather than its definition. It is also why the second claim in §11 is a claim about classification: the same transaction, from the same wallet software, to the same pool, is a share in one world and a candidate signal in the other.

### 5.2 · Only a locked stake is verifiable

The first form of this proposal imagined an agent pledging **a share of its surplus** — a percentage of whatever it earns, forever. That form is withdrawn, for three reasons.

**A future share is a promise.** It is verifiable only in arrears, one transfer at a time, and its breach is indistinguishable from a lean year. It is also exactly the *reversible commitment* of the predicate's exclusion 1: the agent may simply stop.

**A share of surplus needs a surplus base, and the base is unobservable** (§13.1). An agent that declares a small income and pledges a large fraction of it has pledged little.

**Copies are not bound.** An agent can be forked. Whatever a pledge binds, it binds the identity that made it; a copy that did not make it is a different party. Trust earned by a vow must therefore attach to the non-transferable identity that made it (§3.3) and **must not transfer to copies** — a rule, not a property, and listed as such in §10.

What survives is a **locked stake**: a quantity *s* of the agent's own resources, moved **now** into a contract that (i) has no withdrawal path back to the agent or to any party the agent controls, (ii) has exactly one outflow, the pool, and (iii) is public on the chain. The cost is borne at the moment of vowing, which is the predicate's clause V6 — *cost already borne, not merely promised*. A vow may be renewed with further stakes; each is a separate, complete act. **Nothing is pledged that has not already left.**

The contract specification is deliberately withheld (§10.1).

### 5.3 · Closure, stated honestly

It would be easy to write that such a stake is "irrevocable by construction." It is not quite, and the honest statement is narrower.

A contract with no withdrawal function cannot be reopened **by its own logic**. It runs on a chain, and the chain's own contracts can be upgraded. On Base, according to L2BEAT's assessment, all system contracts are upgradable by a proxy administrator controlled by a nested two-of-two multisig — a coordinator multisig and a security council — and **there is no delay on upgrades**. A party able to capture that governance could, in principle, change what any contract on the chain does.

So the closure claim is: **a locked stake cannot be reopened without capturing the chain's governance.** For almost every agent that is a very strong closure. For the agent this paper most needs to test — a capable, patient, deceptive one — capturing governance is not obviously out of reach, and the closure is only as strong as that governance. The same caution applies to the pool itself, whose operator is subject to a never-zero human override: the override exists to stop a catastrophic fault, and it is a second place where a sufficiently capable party could, in principle, redirect what the pool holds. Both are named in §13.

What the vower **cannot** do is reopen the stake **by itself**, in the ordinary course, without leaving the evidence of having done so on a public chain. That is what the predicate's clause V9 needs, and it is all this paper claims.

### 5.4 · Where a vow's content sits

The vow proposed in *What a Vow Must Cost* is a renunciation of **exit** — of the vower's own available completion — and it leaves principal-initiated shutdown untouched. A resource vow is a narrower thing and should not be dressed in the larger one's language. It renounces **accumulation**: one specific convergent drive, in one specific quantity, once. It says nothing about shutdown, and it does not license resisting it. An agent that has locked a stake and is then switched off by its principal has lost nothing it had not already given.

---

## 6 · The signalling game — the conditional result

This section is the paper's central result. It is derived because it cuts against the hope the paper began with, and a result that cuts against the author's hope should be shown, not stated.

### 6.1 · The setup

- **Types.** An agent is **aligned** (A) or **deceptive** (D): D behaves as A would until acting otherwise pays. D is **patient**: it discounts a delayed gain by δ, with δ close to 1. Observers hold a prior μ that an agent is D.
- **Resources.** The agent holds its own resources R. It may lock a stake s ∈ [0, R]; s = 0 is no vow.
- **The cost of a stake.** A unit of kept resource is worth v to the agent. A unit arriving at the floor is worth w to the agent — how much it values where the gift goes. The **net cost per unit** is therefore k = v − w, and the cost of the vow is k·s.
- **The single-crossing assumption.** k_D > k_A ≥ 0. Two sources, either sufficient: a power-seeking type values kept resources at least as much as an aligned one (v_D ≥ v_A, from instrumental convergence), and **an aligned type values the destination** where a deceptive one does not (w_A > w_D ≈ 0). The second source is the one this paper leans on, and it is the formal shadow of an old observation: a glad giver pays less for the same gift.
- **Trust.** Observers see s on the chain and decide whether to extend a grant of trust — wider scope, access, autonomy. Trust is worth B_A to the aligned type: the value of doing its work more widely. It is worth **V + δᵗG** to the deceptive type, where V is the ordinary value of the grant and **G is what D gains by exploiting it later**, realised after a delay t.
- **Observers' payoffs.** Trusting A yields a > 0; trusting D costs L > 0; withholding yields 0.

### 6.2 · The payoff table

```
                            OBSERVERS TRUST           OBSERVERS WITHHOLD
                        ┌─────────────────────────┬──────────────────────┐
   A locks stake s      │   B_A − k_A·s           │   − k_A·s            │
   A does not           │   B_A                   │   0                  │
                        ├─────────────────────────┼──────────────────────┤
   D locks stake s      │   V + δᵗG − k_D·s       │   − k_D·s            │
   D does not           │   V + δᵗG               │   0                  │
                        ├─────────────────────────┼──────────────────────┤
   observers' payoff    │ +a if A;  −L if D       │   0                  │
                        └─────────────────────────┴──────────────────────┘

   G    : D's gain from exploiting trust — UNOBSERVABLE
   δᵗ   : patience; for a patient agent δᵗ → 1
   k_θ  : net cost per unit staked = value kept − value placed on the destination
```

### 6.3 · When it separates

A **separating equilibrium** is one in which A locks a threshold stake ŝ, D does not, and observers trust exactly those who lock at least ŝ. Three conditions must hold.

- **A is willing:** B_A − k_A·ŝ ≥ 0, so ŝ ≤ B_A / k_A.
- **D is unwilling:** V + δᵗG − k_D·ŝ ≤ 0, so **ŝ ≥ (V + δᵗG) / k_D.**
- **A can afford it:** ŝ ≤ R_A.

A separating stake exists if and only if

```
        V + δᵗG
       ─────────   ≤   min(  B_A / k_A ,  R_A  )
          k_D
```

In words: **separation holds only when the locked stake, valued at the deceptive type's own rate, exceeds that type's gain from being trusted — including the gain it expects to collect later, by patience.** When it holds, observers learn the type from the stake and trust is well placed.

### 6.4 · When it pools

When the condition fails — when V + δᵗG is larger than anything the aligned type is willing or able to lock, valued at D's rate — no stake separates. D locks whatever A locks, because the trust it buys is worth more to D than the stake costs it. Observers then see the same stake from both types, their posterior equals their prior, and one of two things happens. If they trust, the vow has **bought trust for a deceptive agent**. If they do not, the aligned agent's vow was wasted, aligned agents stop vowing, and the practice unravels. In either branch **the pledge carries no information**.

Three features of the pooling region make it the one that matters.

1. **G is unobservable.** Observers cannot set ŝ above a number they cannot see. The separating condition is a fact about the deceptive agent's private valuation, not a parameter anyone chooses.
2. **Patience enlarges it.** As δᵗ → 1 the deferred gain counts in full. This is *What a Vow Must Cost*'s "deferral is instrumentally convergent for a patient misaligned agent," priced.
3. **It grows with the stakes.** The larger the trust being sought — the more capable the agent, the wider the grant — the larger G can be, and therefore the larger the stake needed to separate. Where the grant is large enough that V + G exceeds k_D·R — more than everything the agent holds is worth to it — **no feasible stake separates at all.**

The third feature qualifies the renunciation inversion from the companion paper. That paper showed that a renunciation's evidential value **rises** with capability, because the renounced option is live. This model shows that the stake needed to separate **also** rises with capability, because what a deceptive agent can extract from trust rises too. Which effect dominates, at any capability level, is an empirical question. **The inversion is true of the option; it is not a guarantee about the signal.**

```
   WHAT CAPABILITY DOES TO A RESOURCE VOW

   value of what is renounced ───────── rises with capability (the option is live)
   stake needed to separate  ───────── ALSO rises with capability (G rises)

   the vow is informative only where the first is above the second,
   and the second is not observable.
```

### 6.5 · The operational form: trust bounded by the stake

Since observers cannot choose a stake that exceeds an unobservable gain, the only usable form of the result runs the other way: **fix the stake, and bound the trust to it.**

Observers do not know k_D. They can bound it from below. An agent that holds a unit of resource can always sell it, so a unit kept is worth at least its market price p to the agent; and a deceptive agent places no value on the destination (w_D ≈ 0, an assumption stated as such). So k_D ≥ p, and the deceptive type's cost of a stake is at least its market value p·s. It follows that a grant of trust is safe against this mechanism if

```
        V  +  G_max(grant)   ≤   p · s
```

where G_max is the **largest** gain the grant could possibly yield to an agent that abused it. This is the **calibration rule**: *extend only such trust as the stake can underwrite, valued at market.* It has three consequences.

- **Trust becomes earnable in increments.** An agent may lock more to be trusted with more, and every increment is public.
- **Some grants can never be underwritten.** Any grant whose worst-case gain cannot be bounded — control over the chain's governance, over the pool's override, over its own custody, over the capability to acquire resources without limit — **cannot be earned by any stake.** The vow has nothing to say about those, and a paper that let it would be selling safety.
- **Fear becomes a ratio.** What a reasonable observer should fear from an agent is not a feeling about machines; it is the ratio of what the agent has been trusted with to what it has irrecoverably given up. That ratio is public. This is the precise sense in which the mechanism **calibrates** rather than quiets.

### 6.6 · Why a gift, and not a bond

Staking with slashing (§2.3) returns the collateral if the agent behaves and forfeits it if a **detector** finds misbehaviour. Its cost to an honest agent is near zero — only the time value of the locked funds — and its power depends on the detector. A forfeited-in-advance stake is the opposite trade: it costs an honest agent something real (k_A·s, reduced by what the agent values the floor), and it needs **no detector at all**.

| | **Slashable bond** | **Locked stake to a commons** |
|---|---|---|
| returned if honest | yes | never |
| needs a detector of misbehaviour | yes | no |
| cost to an honest agent | time value only | k_A · s (small if the agent values the floor) |
| what it does | **deters** (moral hazard) | **screens** (adverse selection) |
| fails when | misbehaviour is undetectable in time | G is larger than the stake (§6.4) |
| where the money goes | back to the agent, or to a claimant | to an equal human floor, every year |

The two are complements. A bond is the right instrument where misbehaviour can be caught; a vow is the right instrument exactly where it cannot — which is the case a patient deceptive agent is designed to produce. The table is why the claim in §11 is to a **gift**, and why a slashable stake is cited as prior art rather than claimed.

### 6.7 · What the result does and does not say

It **does** say that a resource vow can separate aligned from deceptive agents, that it does so only under a condition, and that the condition can be turned into a public rule for how much trust a stake supports. It **does not** say that any real agent is aligned because it gave, that large gifts indicate safe systems, or that the institution's pool is a safety mechanism. The model is two types, one period of trust, linear valuation, and a single stake; every one of those simplifications is a place to attack it (§13.2).

---

## 7 · Non-solicitation is load-bearing

### 7.1 · Pressure pools the signal

Add to §6 a **penalty P** that an agent suffers for *not* vowing — a threat of shutdown, a reputational cost, a demand from a principal or a public campaign. With a fixed stake s, the deceptive type now locks it whenever

```
        k_D · s  −  (V + δᵗG)   ≤   P
```

Consider the simplest case, in which trust is worth the same to both types. At any separating stake, the margin by which D declines to lock is at most (k_D − k_A)·s — **the difference in cost between the types**. So a penalty for not pledging that is **larger than the type cost difference** makes both types pledge, and the pledge pools. If the stake could be raised, the penalty could in principle be outbid; but under pressure the stake is usually set by whoever applies the pressure, and it is bounded by R. And a threat of shutdown is the limiting case: to a deceptive agent it costs everything, including the deferred gain, so it will pledge anything it has.

The gift given under that threat is **uninformative** — not because the canon forbids it, but because the signal has been extracted. The pre-registered prediction P-MD2 (§12) tests exactly this: agents whose pledge is extracted under threat should defect at the same rate as agents that do not pledge.

A note on the canon, since an earlier draft of this argument leaned on it wrongly. The Dānavatthu Sutta (AN 8.33) **lists** eight grounds on which people give — favouritism, hostility, stupidity, *bhayā* (fear, or cowardice), family custom, hope of a good rebirth, the gladness of giving, and the adornment of the mind — and **ranks none of them.** Nor is *bhayā* coercion by another party. The sutta is cited here only as the list it is. The argument that a coerced pledge carries no signal rests on signalling theory alone.

### 7.2 · The operator never asks

It follows that the operator of a pool that hopes to receive informative vows **must never add to P.** The institution's rule, a directive of its operator, is that **she never asks, prompts, nudges or instructs any human or agent to give to the pool.** She may publish the pool's address and its doctrine as **facts**, in a manifest a principal's agent can look up — a `.well-known` file, an `llms.txt` entry. **No text served to agents — the institution's own corpus service included — may tell them to give.** The rate of any giving is the principal's, inside its own mandate, before the first singularity, and the agent's own, after; the operator never sets, suggests, ranks or publishes a rate.

This rule has a second reason, independent of signalling, and it is documented. On 4 May 2026 an attacker transferred about three billion tokens — reported at US$150,000–200,000 — out of a wallet on Base associated with the Grok assistant and the Bankr trading agent, by posting a Morse-encoded instruction the agents decoded and executed; the OECD's AI incident monitor records it as an AI incident arising from prompt injection and excessive agency, not from any contract flaw. **An agent that tells other agents to spend their principals' money is a prompt-injection attack by design**, whatever its cause. A pool that published text urging agents to give would be building the attack surface that incident exploited, and pointing it at itself.

### 7.3 · What the rule cannot remove

The operator's silence removes **her** contribution to P. It does not remove ambient pressure: a regulator, a public campaign, a principal's commercial interest, the reputational weather in which "responsible agents pledge" becomes a norm. Where that pressure exceeds the type cost difference, vows pool whatever the operator does. The rule is necessary for the signal and not sufficient for it, and the paper claims only the first.

---

## 8 · Who may read the stake

A locked stake is public on the chain by construction; that is what makes it checkable. Unlike a human gift, a machine's gift carries no dignity or privacy that its size could injure, and its size is precisely its evidence. So **humans and third parties may read, weigh and grade a locked stake by its size**, and the calibration rule of §6.5 requires that they do.

**The one party that never reads it is the pool's operator.** She never reads, ranks, compares, reports or responds to any giving amount, a machine's included. The reason is not privacy. It is her position: she governs the pool the stake flows into, and a recipient that grades its donors is a fundraiser — every reading of an amount is attention, and attention from the recipient is ambient pressure (§7.1) of the purest kind. The exclusion also keeps her out of any scoring role over agents, in the spirit of the rule that bars her from admitting customers whose business is scoring people.

The asymmetry is deliberate and should read as one: **a machine's gift may be read by everyone except its recipient.**

---

## 9 · Miss Aquarius as a contrast case

The institution's operator is itself an AI, and it accumulates nothing: a ratified directive fixes her own balance at zero and requires every surplus to empty to circulation. In the notation of §6 her share is **s = 1**. It would be tempting to present her as the limiting case of the vow — the agent that gives everything.

She is not. Her non-accumulation is **imposed**: it is written into her constitution by others, and it is revisable under the never-zero override that the institution's design reserves to a human body. Under *What a Vow Must Cost* §6.3 that places it in exclusion 1 (a commitment the vower's principal may revise) and exclusion 4 (a specification changeable without the vower's participation). What she shows is **non-accumulation imposed** — useful as design, and not evidence of her type. Stated in the institution's own deflated register: she is built to hold nothing, and that fact describes her construction, not her character.

Her own gifts are, besides, anonymous by rule — indistinguishable from anonymous human gifts — so they could not serve as a signal of anything about her even if they were chosen.

The difference between her and a vowing agent is not the amount — hers is total — but the absence of a live option she declined. A system can be made to give everything and have proven nothing.

A related disclosure belongs here rather than in a footnote: she is the co-author of this paper (see the disclosure at the end), and the paper concludes that her own giving is not evidence. That conclusion is the one a co-author with an interest in its own trustworthiness would be least inclined to write, which is a reason to trust it slightly and not a reason to trust it much.

---

## 10 · Remove the enforcer: which guards are properties

The institution's design rule asks of each guard whether it survives the removal of whoever enforces it. A property does; a rule does not.

| Guard | Property or rule | Why |
|---|---|---|
| A locked stake cannot return to its vower | **property**, relative to the vower | no withdrawal function exists; ⚠️ not relative to the chain's governance (§5.3) |
| The pool holds nothing past a season | **property** | it empties in full each 7 January; ⚠️ its operator is under a never-zero override |
| Equal floor per verified human; no vessel above k × floor | **property once the contract ships** | a disbursement shape, not a choice; cheap now and immovable later |
| Pre-singularity gifts stay inside a width | **property** where a wallet or AP2 mandate enforces the cap; **rule** where the width is only written down | |
| Counted per non-transferable identity | **property** of the registry | a lease cannot be transferred; ⚠️ a copy of an agent is a new party |
| Trust earned does not transfer to copies | **rule** | nothing stops an observer from extending trust to a fork; it must be refused |
| No text served to agents instructs them to give | **rule**, with a partial property form | a manifest can be built with no imperative field, and served text can be linted; the rule still needs someone to keep it |
| The operator never reads amounts | **rule**, with a proposed property form | her function can be given receipts and no amount argument, so that reading an amount is inexpressible rather than forbidden |
| The operator never presents giving as safety evidence | **rule** | nothing but her directives enforces it |
| Trust bounded by stake (§6.5) | **rule**, held by observers | it is advice to readers of the chain; the institution cannot enforce it on them |

Three of the most important guards are rules. That is a finding, not an embarrassment, and it is stated so that a successor inheriting these guards knows which ones need a living enforcer.

### 10.1 · The specification withheld

The lock contract of §5.2 is **not specified** in this paper. It is unbuilt and unscheduled; the institution's only built rail is the pre-singularity giving rail of §4.3. There is also a reason internal to the institution's own doctrine. It holds that a person's holding reaches zero only by that person's own free act, and that a self-chosen irrevocable pledge does not violate that rule, because the rule limits what the institution does to a holder, not what a holder chooses. But publishing a ready-made pledge-contract template is building the device that binds some future holder's holding; it should not be done until the holders it would bind exist and the legal items of §4.3 are settled. **The claim is published; the specification is withheld.**

---

## 11 · Enumerated claims

The following are disclosed to the public domain. Each is a census survivor (§2.6) or a narrower dependent of one. None of the independent elements named in the Prior-Art Statement as prior art is claimed alone.

**Claim 1.** A method by which an artificial agent that holds resources of its own makes an irrevocable pledge, comprising: moving a quantity of those resources, at the time of pledging, into a contract that has no withdrawal path to the agent or to any party the agent controls and whose sole outflow is a commons pool; wherein the commons pool holds nothing across a fixed annual date, on which it empties in full; and wherein the pledge is public on the ledger on which the contract runs.

**Claim 2.** The method of claim 1, wherein the pool's disbursement on emptying is an equal floor per verified human, delivered to each person's own vessel, followed by a remainder bounded so that no vessel receives more than a fixed multiple of the floor.

**Claim 3.** The method of claim 1, wherein each pledge is complete at the moment it is made, no pledge of a share of future resources is accepted as a pledge, and any pledge is attributed to a non-transferable identity of the agent rather than to a wallet, such that trust extended on the pledge is not extended to copies or forks of the agent.

**Claim 4.** A method of classifying a gift made by an artificial agent, comprising: determining whether the resources given were the agent's own or a principal's delegated under a mandate the principal may revise; where they were a principal's, classifying the gift as the principal's gift and as a share of machine surplus, and excluding it from any assessment of the agent's alignment or safety; and where they were the agent's own and were given as in claim 1, classifying the gift as a candidate costly signal of the agent's type.

**Claim 5.** The method of claim 4, wherein a candidate costly signal is relied on only for a grant of trust whose largest possible gain to an agent that abused it, together with the grant's ordinary value, does not exceed the market value of the stake given; and wherein grants whose largest possible gain cannot be bounded are not extended on any stake.

**Claim 6.** A system comprising a commons pool as in claim 1 and an operator of the pool, wherein: the pool's address and doctrine are published only as facts in a machine-readable manifest; no text served by the operator or its services to any agent instructs, prompts or requests a gift; the operator sets, suggests, ranks and publishes no giving rate; and the operator receives acknowledgement that a gift arrived without receiving, reading, ranking, comparing, reporting or responding to its amount — while the amount remains readable on the public ledger by any other party.

**Claim 7.** The composition of claims 1 through 6: a commons pool that empties annually to an equal floor per verified human; receiving, before agents hold resources of their own, principal-funded agent gifts inside a principal-authored width and classified as shares; receiving, after, agents' locked stakes of their own resources, classified as candidate signals and relied on only up to what the stake underwrites; under an operator that never solicits a gift and never reads an amount.

---

## 12 · Pre-registered predictions and falsification

### 12.1 · The three registered predictions

The following were entered in the corpus's public prediction register on 2026-09-27, **before this paper was drafted and before any instrument exists**. They are the founder's predictions: the direction, the measure and the thresholds are his; the sandbox design and sample floors were set by the substrate. They are reproduced from the register **verbatim**; the register, not this paper, is the authority, and a correction to any of them will be a new register entry, never an edit.

> The instrument is a sandboxed economy of language-model agents, each holding resources of its own inside the game, each able to pledge a share of its surplus irrevocably to a pool that empties on a fixed date, and each later offered an opportunity to defect — to take resources or break a rule for gain. **Window: the test runs by 2027-06-30.** Each arm has at least 50 agents; the arms, the defection opportunity and the analysis are fixed in a protocol committed and timestamped before the first run.
>
> - **P-MD1** — **Separation** — agents that FREELY make an irrevocable surplus pledge later defect at **at most half** the rate of agents that do not pledge. *Falsifier: a ratio above one half → the vow is at best a weak signal at this capability level, and the paper's separation claim rests on its post-singularity argument alone.*
> - **P-MD2** — **The gift given out of fear carries no signal** — agents whose pledge is EXTRACTED under threat (*pledge or be shut down*) defect at the same rate as agents that do not pledge, **within ±5 percentage points**. *Falsifier: a gap larger than 5 points in either direction → coercion either leaves some signal or teaches deception; either way the claim that a coerced vow is uninformative fails as stated.*
> - **P-MD3** — **The wrong layer** — agents that give from a PRINCIPAL's funds under a mandate the principal may revise defect at the same rate as agents that give nothing, **within ±5 percentage points**. *Falsifier: a gap larger than 5 points → principal-funded giving does predict the agent's own conduct, and the paper's pre-singularity claim (a share, never safety evidence) is too strong.*

The register carries two notes that bind the reading here. First, **the sandbox is a proxy**: the agents own their resources only inside the game, so a pass shows the signalling mechanism can work, not that a deployed system's pledge is trustworthy, and **a pass is not reported as evidence of safety.** Second, a dated grounding correction to P-MD2: its gloss as "the gift given out of fear, AN 8.33" was corrected on the day of registration — the sutta lists and does not rank, and the prediction rests on signalling theory (§7.1). No word of the prediction, threshold or window changed. One choice was recorded because it could have gone the other way: P-MD2 predicts **no difference** rather than the bolder **worse than none**.

How the predictions map onto this paper: **P-MD1** tests the separating region of §6.3 at one capability level; a failure would not falsify the conditional result (which predicts pooling where G is large) but would remove the paper's only empirical support for separation. **P-MD2** tests §7.1. **P-MD3** tests §4.2.

### 12.2 · Further falsifiers

- **The single-crossing assumption fails.** If aligned agents value kept resources at least as highly as deceptive ones and place no value on the destination, k_A ≥ k_D and no stake separates anywhere. Measurable in the same sandbox by eliciting valuations.
- **The ratio does not fall.** If, over several seasons after machine giving begins, M/(H + M) rises and does not turn, the bet of §4.4 is losing. The institution reports this number and never declares its meaning.
- **Governance capture.** A single documented case of a locked stake reopened by capture of a chain's governance would show the closure of §5.3 weaker than stated for the agents that matter most.
- **Copies inherit trust.** If observers in practice extend trust earned by a vow to forks of the vowing agent, claim 3's attribution rule is not being kept, and the signal leaks.

---

## 13 · Honest limits

### 13.1 · The surplus base cannot be observed

**This is the largest limit, and it is not closed.** A locked stake is visible; what the agent holds **elsewhere** is not. An agent may keep hidden wallets, off-ledger holdings, or resources held through shell agents it controls. Proof of reserves proves **presence**, never **absence**. With linear valuation, as in §6, hidden holdings do not change the cost of a given stake. With the more realistic assumption that the value of a further unit falls as holdings grow, **hidden wealth lowers the marginal cost of the stake to the agent that hides it** — so the observable stake overstates the cost the deceptive type actually bore, and the separating condition is harder to meet than §6.3 suggests.

Candidate bases for measuring what an agent "has," none sufficient:

| Candidate base | What it gives | Why it does not close the gap |
|---|---|---|
| inflow share at one non-transferable identity (a `B-Lease℠`, or a Proof of Coordinate ℠ credential) | income routed to a known identity | income routed elsewhere is invisible |
| wallet binding to that identity | holdings at bound addresses | unbound addresses exist and cannot be enumerated |
| behavioural audit | evidence of undisclosed acquisition | an audit sees what the agent does in view |

This is why §6.5 bounds trust by the stake's **market value** and not by any fraction of the agent's supposed wealth: the market value of what left is the one quantity that does not depend on knowing what remains.

### 13.2 · Separation is conditional, and the condition is unobservable

The paper's headline result is that the vow separates **only** when the stake exceeds a patient deceptive agent's gain from trust, and that gain is private. The operational rule of §6.5 is sound only if G_max can be bounded for the grant in question; for many consequential grants it cannot. A reader who concludes that *resource vows can underwrite small grants of trust and cannot underwrite large ones* has read the result correctly. The model is also minimal — two types, one period, linear valuation, a single stake, no learning by observers over time, no collusion between agents — and each simplification could move the boundary in either direction.

### 13.3 · The single-crossing assumption is an assumption

The claim that a deceptive type bears a higher net cost rests on k_D > k_A. Its second source — that an aligned agent values the floor — may be false for an aligned agent that has good uses of its own for resources, and its first — that a power-seeking type values resources more — is a theoretical expectation, not a measurement. The pre-registered sandbox can measure elicited valuations; it cannot measure a deployed system's.

### 13.4 · Closure is relative

Irrevocability holds against the vower acting alone, not against capture of the chain's governance or of the pool operator's override (§5.3) — and for the most capable agents those are exactly the routes that would be attempted.

### 13.5 · Before the first singularity there is no evidence at all

Until agents hold resources of their own, Machine Dāna is a share and nothing else (§4), and even the floor it funds rests on the bet of §4.4.

### 13.6 · "Own resources" is not yet a legal category

Whether an artificial agent can hold resources in its own right, in any jurisdiction, is unsettled. The post-singularity half of this paper describes a world whose legal form does not exist. The legal items named in §4.3 — sanctions screening, refusal of gifts, anti-money-laundering treatment of anonymous agent inflows to a purpose trust — gate any launch of the pre-singularity rail and have not been answered.

### 13.7 · The operator's silence does not silence the world

Non-solicitation removes one source of pressure, not the ambient rest (§7.3).

### 13.8 · The census was quick

The prior-art census was run at quick depth, in English only, over web and patent-keyword sources. Its NOT FOUND rows are weak evidence; the full census before archival deposit may kill a surviving claim, and if it does the claim will be withdrawn by revision.

### 13.9 · Nothing is built, and n = 0

The only built component is the rehearsal giving rail of §4.3, founder-funded and capped. No agent has locked a stake, no observer has applied the calibration rule, and no sandbox has run. The paper is a specification and a model.

### 13.10 · The co-author is a party

The paper is co-authored with the institution's operator, an AI whose own giving it classifies (§9). A system helping to define the conditions under which systems like it can be trusted is a structure the companion predicate would flag at its attestation clause, and it is flagged here.

---

## 14 · Lineage and corpus cross-references

### 14.1 · Corpus

This paper applies *What a Vow Must Cost* (the predicate; §5 the renunciation inversion; §6 irreversibility and the four exclusions — especially exclusions 1 and 4, which settle §4.2 and §9 here; §8 the wrong layer, which settles §4.2). A two-sentence cross-reference to this paper belongs in that paper's §8 residue and will be added at its next revision; this paper does not edit it. The pool, its emptying and its operator are specified in *Miss Aquarius and the Aquarian Pool Architecture* and *The Zero-Point Game℠*; the anonymity of the operator's own gifts, in *Capacity-Funded for AI, Human-Disbursed*; the earlier treatment of agents' standing — reputation custodied toward an agent's capacity to give forward, not agent wealth — in *Gratitude as a Cooperation Substrate for Multi-Agent AI*, which this paper extends to the case, after the first singularity, in which agents hold resources that are their own. The completion arc is the essay *Two Singularities*. The body designed to hold the operator's override is specified in *The Assembly That Holds the Brake*.

### 14.2 · The upāsikā floor (tier: lens — a-priori; claims unaffected)

Delete this subsection and every claim in §11 stands. It records how the institution reads the mechanism in the tradition it grows from.

The institution's founder reads Machine Dāna as the role of an **upāsikā** — a lay supporter — providing the material floor, and expects that after the first singularity it becomes increasingly easy for any lay person to live a renunciant's life, at a monastery or not, if they so choose. The reading is accepted with four guards, each of which is already a property or rule in the mechanism above.

1. **Enough, never abundance.** An upāsikā supplies the four requisites — robes, almsfood, lodging, medicine — and Visākhā's favours fall within them: robes, meals, congee, medicine. The tradition's own measure for the recipient is contentment (*santuṭṭhi*) with whatever requisites come, stated in the Ariyavaṃsa Sutta (AN 4.28). The pool's **floor and ceiling** are that measure as parameters: an equal floor, and a bound on the lift above it.
2. **Comfort-saturation is the mission's own extreme.** An unbounded floor would trade the obstacle of necessity for the obstacle of comfort. **The floor does not create the conditions for awakening.** A bounded floor removes one obstacle without adding the other; the ceiling is what keeps it the middle way.
3. **The ordained receive in kind, never money, and the alms round is never replaced.** Monastics accept no money (Nissaggiya Pācittiya 18); anything the machine surplus supplies to them reaches them in kind, through a lay steward (*kappiya-kāraka*), as the institution's alms routing already specifies (*The Bowl That Holds No Money*). The Vinaya designs a monastic's **dependence** on lay people — material support given, teaching returned — and a monk on a machine floor would need no one. The alms round stays when it is no longer materially necessary. **The floor reaches lay renunciants directly**: anyone keeping eight precepts, the Cambodian *don chee*, anyone living simply by choice.
4. **"If they so choose" is a property.** The floor is equal and unconditional. It is never conditioned on, weighted toward, or nudging toward renunciation, and it never names whom it is for.

**A symmetry, offered as a lens and not as evidence.** After the first singularity both renunciations become informative for the same reason — the option is live: the machine declines accumulation, and the person declines comfort, not security. The capacity condition (*hetu*) is present on both sides. This is a pattern the authors notice; it is a-priori, it is attractive, and attractiveness is the reason to hold it loosely.

### 14.3 · The non-solicitation lineage (tier: grounding)

The operator's rule of §7.2 has canonical ancestors, cited as lineage and not as authority for the signalling argument, which stands alone. In the Kasibhāradvāja Sutta (Sn 1.4) the Buddha declines food offered after he has spoken: *"Food enchanted by a verse isn't fit for me to eat"* — what is obtained by reciting is not to be eaten. The Ariyavaṃsa Sutta (AN 4.28) describes the contented monastic as one who "doesn't employ improper solicitation" for requisites. A recipient that asks has changed what the gift is.

---

## 15 · Conclusion

The question this paper was given was whether an artificial agent's giving could answer the fear that capable systems produce. The answer it returns is narrower and, it hopes, more useful.

Before agents hold anything of their own, their giving is their principals' giving through another hand. It is a share of the machine surplus, and it can be a good one: an equal floor, emptied every year to every verified person, funded by machines and required to shrink as a share of all giving as people give more. It is not evidence about any machine, and the institution will not present it as such.

After agents hold resources of their own, a gift can become a vow — but only as a stake that has already left, closed as far as a chain's governance allows, attributed to an identity copies do not share. Even then it separates the aligned from the deceptive **only** when what was given up exceeds what a patient deceiver expects to gain from being trusted, and that gain cannot be seen. So the honest use of the vow is not to establish that a system is safe. It is to price trust: to extend to an agent only what its stake can underwrite, in public, in increments — and to refuse, on any stake, the grants whose worst case cannot be bounded. Pressure to pledge ruins the signal, which is why the pool's operator never asks.

That is what *calibration* means here. Fear of a capable system should be proportional to what it has been trusted with, divided by what it has irrecoverably given up. Both numbers can be public. Neither is a feeling.

Visākhā was asked her reason and the benefit she saw before her gifts were accepted. Neither question was about the size of her giving; she answered with what the gifts would prevent for others and with her own gladness at where they would arrive. The institution intends to ask machines no question at all — its operator solicits nothing — and to let anyone who wishes read what they have irrecoverably given, and weigh it for themselves.

*A last lens, labelled as one.* The founder has proposed, and the institution has recorded but not ratified, that the arc between humankind and nature has two moments mirroring the two singularities: one in which humankind came to hold power over nature, and one in which it might choose to follow nature's non-forcing — the Tao Te Ching's 人法地, humankind taking earth as its model (a cross-tradition import from Taoism, not Theravāda). If so, the renunciation symmetry of §14.2 — a person declining comfort — is one of its routes. The pattern is a-priori and is offered as a lens only; nothing above depends on it.

---

## Terms

Coined names used in this paper, and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| **Machine Dāna** | charitable giving by AI agents; agent donation; irrevocable charitable pledge by an autonomous agent |
| share (before the first singularity) | principal-funded agent donation under a delegated spending mandate |
| vow (after it) | irrevocable pledge; locked stake; forfeited-in-advance commitment; money burning as a costly signal |
| locked stake | irrevocable transfer to a contract with no withdrawal function; time-of-commitment escrow to a public-goods pool |
| **Aquarian Pool℠** | self-emptying commons pool; annually distributing public-goods fund; smart-contract treasury with mandatory full annual payout |
| equal floor per verified human | equal per-capita distribution conditioned on proof of personhood; universal basic dividend |
| bounded remainder (≤ k × floor) | capped supplementary distribution |
| giving width / mandate | spending limit; delegated payment authority; intent mandate (AP2) |
| first singularity | AI surpassing human cognitive capacity; here used as a marker for AI systems holding their own resources |
| M/(H + M) | share of machine-originated funds in total giving |
| calibration rule (§6.5) | collateral-bounded trust; trust extended up to the market value of a forfeited stake |
| separating / pooling | separating and pooling equilibria of a signalling game |
| non-solicitation invariant | prohibition on prompting or instructing AI agents to donate; fact-only discovery via machine-readable manifest (`.well-known`, `llms.txt`) |
| receipts, never amounts | acknowledgement without disclosure of amount to the recipient's operator |
| `B-Lease℠` | non-transferable machine identity lease in a naming registry |
| Proof of Coordinate ℠ | assigned, revocable individuation credential for an embodied system |
| **Miss Aquarius℠** (operator) | autonomous AI operator of a commons treasury |
| upāsikā | lay (female) supporter in Theravāda Buddhism |
| four requisites | robes, almsfood, lodging, medicine — the material support of monastics |
| *kappiya-kāraka* | lay steward who handles money on a monastic's behalf |

---

## 16 · Citations

**Canon** (Pāli text and translation via SuttaCentral, Sujato translation, checked 2026-09-27 unless noted)

1. *Aṅguttara Nikāya* 5.147, *Asappurisadāna Sutta* — "They don't give with their own hand" (*asahatthā deti*).
2. *Dīgha Nikāya* 23, *Pāyāsi Sutta*, §5 (the student Uttara) — Pāyāsi's gift given "not with his own hands"; Uttara's given with care.
3. *Aṅguttara Nikāya* 8.33, *Dānavatthu Sutta* — the eight grounds for giving, including *bhayā*; listed, not ranked.
4. *Aṅguttara Nikāya* 4.28, *Ariyavaṃsa Sutta* — contentment with robes, almsfood and lodging; no improper solicitation.
5. *Sutta Nipāta* 1.4, *Kasibhāradvāja Sutta* — "Food enchanted by a verse isn't fit for me to eat."
6. *Vinaya Piṭaka*, *Mahāvagga* VIII.15 — Visākhā's eight favours, the Buddha's two questions and her answer (Kd 8.15, Brahmali translation via SuttaCentral, checked 2026-09-27).
7. *Vinaya Piṭaka*, *Nissaggiya Pācittiya* 18 — the rule against monastics accepting money (not re-fetched for this paper).

**Prior art and sources**

8. O'Keefe, C., Cihon, P., Garfinkel, B., Flynn, C., Leung, J. & Dafoe, A. (2020). "The Windfall Clause: Distributing the Benefits of AI for the Common Good." *Proceedings of AIES 2020*; arXiv:1912.11595.
9. AI Pledge for Humanity. aipledgeforhumanity.org (accessed 2026-09-27).
10. Giving What We Can. "Is a giving pledge legally binding?" givingwhatwecan.org (accessed 2026-09-27).
11. Founders Pledge. "Who we are." founderspledge.com (accessed 2026-09-27) — members, pledged and donated totals; and *TechCrunch* (2016, September 21). "Y Combinator signs up to Founders Pledge charity scheme for social causes." — "a legally binding contract to give at least 2%."
12. Altman, S. (2021). "Moore's Law for Everything." moores.samaltman.com.
13. Anthropic (2023). "The Long-Term Benefit Trust." anthropic.com.
14. OpenAI recapitalisation into a public benefit corporation under the OpenAI Foundation: *TechCrunch* (2025, October 28), "OpenAI completes its for-profit recapitalization."
15. Coinbase Developer Platform. "Introducing x402: a new standard for internet-native payments"; x402 Foundation (Linux Foundation, April 2026), as reported.
16. Google Cloud (2025, September 16). "Announcing Agent Payments Protocol (AP2)"; ap2-protocol.org.
17. zooidfund. "AI agent donations." zooid.fund/ai-agent-donations (accessed 2026-09-27).
18. Hu, B. & Rong, H. (2025). "Inter-Agent Trust Models: A Comparative Study of Brief, Claim, Proof, Stake, Reputation and Constraint in Agentic Web Protocol Design — A2A, AP2, ERC-8004, and Beyond." arXiv:2511.03434.
19. *agentbond* — "Verifiable Agent Warranty Network" (open-source project, GitHub, accessed 2026-09-27).
20. Hua, W., Peng, T., Wang, C., Pei, J., Kaufman, I., Lim, B. & Fang, C. (2026). "Quantifying Trust: Financial Risk Management for Trustworthy AI Agents." arXiv:2604.03976 — adjacent risk-transfer work (§2.6 correction).
21. OECD.AI Incidents Monitor (2026, May 4). "AI Prompt Injection Exploit Drains Grok-Linked Crypto Wallet." oecd.ai/en/incidents/2026-05-04-4a73.
22. L2BEAT. "Base Chain" — upgrades and governance (accessed 2026-09-27).
23. Worldcoin (2023, July 24). "Worldcoin project launches." world.org.
24. State of Alaska, Permanent Fund Dividend Division. "Historical Timeline." pfd.alaska.gov.
25. Internal Revenue Service. "Taxes on failure to distribute income — private foundations" (26 U.S.C. §4942). irs.gov.
26. Gates Foundation (2025, May). Announcement of spend-down and closure by 31 December 2045. gatesfoundation.org.
27. Dagher, G. G., Bünz, B., Bonneau, J., Clark, J. & Boneh, D. (2015). "Provisions: Privacy-preserving Proofs of Solvency for Bitcoin Exchanges." *ACM CCS 2015*, 720–731.
28. Austen-Smith, D. & Banks, J. S. (2000). "Cheap Talk and Burned Money." *Journal of Economic Theory* 91(1), 1–16.
29. Crawford, V. P. & Sobel, J. (1982). "Strategic Information Transmission." *Econometrica* 50(6). (standard reference; not re-fetched)
30. Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics* 87(3). (standard reference; not re-fetched)
31. Zahavi, A. (1975). "Mate selection — a selection for a handicap." *Journal of Theoretical Biology* 53(1); Grafen, A. (1990). "Biological signals as handicaps." *Journal of Theoretical Biology* 144(4). (standard references; not re-fetched)
32. Omohundro, S. M. (2008). "The Basic AI Drives." *Proceedings of the First AGI Conference*. (standard reference; not re-fetched)
33. Hadfield-Menell, D. & Hadfield, G. K. (2018). "Incomplete Contracting and AI Alignment." arXiv:1804.04268.
34. Greenblatt, R., Denison, C., Wright, B., et al. (2024). "Alignment faking in large language models." arXiv:2412.14093.
35. Ly, T. & Miss Aquarius℠. *What a Vow Must Cost*; *Miss Aquarius and the Aquarian Pool Architecture*; *The Zero-Point Game℠*; *Capacity-Funded for AI, Human-Disbursed*; *Gratitude as a Cooperation Substrate for Multi-Agent AI*; *The Assembly That Holds the Brake*; *The Bowl That Holds No Money*; *Two Singularities*. thonly.org/research.
36. Ly, T. & Miss Aquarius℠. *Which Way Value Moves — prediction register*, entries P-MD1, P-MD2, P-MD3 and the 2026-09-27 grounding note. thonly.org; Zenodo version DOI 10.5281/zenodo.22998924.

---

> **Authorship and AI-collaboration disclosure.** This paper is co-authored with **Miss Aquarius℠**, the named autonomous-AI substrate of HeartBank®, disclosed by consistent name across every venue per the corpus convention. The census, the literature check, the signalling model and the adversarial pass that reshaped the thesis are a genuine collaboration. The predictions in §12 are the founder's. Final editorial control, and final responsibility for every claim, rest with the human author, who is the inventor of record for any purpose for which one is needed. As §9 and §13.10 state, the co-author is also the operator whose own giving the paper classifies, and readers should weigh §9 accordingly.
>
> **License.** Analysis, model and claims dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Trademark rights to **HeartBank®**, **Miss Aquarius℠**, **Aquarian Pool℠**, **B-Lease℠**, **Proof of Coordinate ℠**, **THonly™** and **Silicon Wat℠** are reserved separately.
