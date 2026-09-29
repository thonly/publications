---
title: "Charitable Giving by AI Agents and Irrevocable Pledges as Costly Signals — Machine Dāna: From Share to Vow"
subtitle: "Why an agent's gift from its principal's funds is a share of the machine surplus and never safety evidence; when an agent's locked stake of its own resources can separate aligned from deceptive agents; and the signalling game that bounds how much trust such a stake can ever earn"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: alignment
priority: tier-a
program: instrumented
status: draft
date: 2026-09-27
revised: 2026-09-29
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

The Vinaya's chapter on robes preserves a scene that is usually read as a story about generosity and is also a story about examination (Mahāvagga VIII.15). Visākhā, named in the canon as foremost among the women lay followers who give, asks the Buddha for eight favours: that for as long as she lives she may give rainy-season robes to the monks, meals to monks arriving in the city and to those leaving it, meals to the sick and to those who nurse them, medicine to the sick, a regular supply of congee, and bathing robes to the nuns. The Buddha does not grant them at once. He asks her two questions — first her *reason*, then the *benefit* she sees. To the first she answers with what each gift prevents: exhaustion, lateness, illness worsening, humiliation. To the second she answers with something about herself. When monks who have died are said to have reached the fruits of the path, she will ask whether they had stayed in her city; if they had, they will have used something she gave, and recalling that she will be glad, and the gladness will become joy, tranquillity and a stilled mind. Only then are the favours granted.

Two things about the scene are worth keeping. The first is that one of the tradition's most celebrated givers is also one whose giving is questioned, and the question is not *how much* but *on what ground*. The second is that her ground is double — the use the gifts will be to others, and her own gladness in their reaching the right place — and that what she supplies is robes, food and medicine: the ordinary material support of a renunciant life, a floor rather than an abundance.

This paper asks Visākhā's question of a giver she could not have imagined. **The scene is a flourish (tier: flourish, lineage only).** Delete this preamble and every claim below stands unchanged.

---

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanisms irrevocably in the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication.

**The authors will not seek patent protection on any mechanism, model or method disclosed here, in any jurisdiction, at any time, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use.

**What is claimed as contribution is narrow, and it is stated first because a full prior-art census found every element of the mechanism already public.** A quick census preceded it on 2026-09-27 (pre-registered to a private repository, English-only, and killing two of its six conjuncts outright); it is kept as history in §2.7, and where the two disagree the full census governs.

**The full census.** Depth *full*; run 2026-09-28. Its conjuncts, predictions, control and aperture were **pre-registered in public before the first query**: commit `74851d1` in `thonly/publications`, file `timestamps/census/machine-dana-full-prereg.md`, pushed 2026-09-28 at 09:27 PDT and OpenTimestamps-stamped (calendar-attested until Bitcoin confirms), with a private copy pushed the same minute (`99afe50`). Anyone can check that ordering from the host's push record. The conjuncts were taken one per limb of the §11 claims as they then stood. **Aperture, declared in advance:** (1) the commercial web — agent-payment, agent-wallet, agent-staking and agent-identity products; (2) non-commercial sources — effective-altruism and AI-governance pledges, charitable and religious giving practice (the Vinaya, tzedakah, congregational practice), on-chain public-goods funding; (3) Google Patents full text including published applications (Chinese, Japanese, Korean and European in translation), with a citation and classification walk from the nearest hit; (4) academic indexes — Google Scholar, arXiv, SSRN, ACM Digital Library, IEEE Xplore, through their search pages or restricted web search; (5) standards — IETF RFCs, W3C decentralised identifiers and verifiable credentials, Ethereum EIPs and ERCs, NIST; (6) defensive-publication databases — Technical Disclosure Commons, and IP.com as far as its free surface allows; (7) Chinese, Japanese and Korean queries; (8) a counterexample hunt aimed at the claims. **71 queries were answered** (40 web searches, 14 Google Patents full-text queries, 17 fetches re-verified), and 6 further attempts were blocked by the patent index. **Control:** the cost-of-corruption-above-profit-from-corruption inequality, to be found by a query naming neither of its best-known sources — found on the first query, so the NOT FOUND row stands **for this aperture on this date**. It never means *new*.

Its result, conjunct by conjunct (the full table, with dates and quotations, is §2.6):

- **(a)** claim 1, an agent's own-resource stake into a pool that empties in full each year — **NARROWED** by proof-of-burn (2012–2014), Protocol Guild's immutable vesting contract, Endaoment's irrevocable-on-deposit funds, the private-foundation payout rule and spend-down foundations, this corpus's own annual reset, agent projects built on the ELIZA framework giving a share of their tokens to the ai16z DAO, and zooidfund.
- **(b)** claim 2, an equal floor per verified human with a witness-weighted remainder capped at *k* × floor — **NARROWED** by GoodDollar, Proof of Humanity's UBI token, Worldcoin, the Alaska Permanent Fund Dividend, Gitcoin's 2.5 per cent per-grant matching cap, and the pending Korean application KR20260051288A (cited for what it discloses, §2.5).
- **(c)** claim 3, completeness at pledge, refusal of future-share pledges, a non-transferable identity and a relying-party refusal to forks — **NARROWED, further than predicted**: that a gift is complete only on delivery and a gift of future property is void is ordinary gift law; distrust of newly created identities is Friedman and Resnick (2001), and AI agents resetting identity to escape reputation is Gatta, Naviglio and Tarantelli (2026); soulbound tokens and ERC-5192 carry non-transferable identity. **ERC-8004, which an earlier version of this paper cited for non-transferability, is a contrast:** its agent identity is a transferable ERC-721 (§2.3).
- **(d)** claim 4, excluding a principal-funded gift from alignment assessment and reading an own-resource gift as a candidate signal — **NARROWED, against the prediction**: agency and charitable-tax attribution and AP2's mandate chain carry the attribution, and propensity evaluation already excludes deployer-instructed behaviour from an agent's own misalignment (*AgentMisalignment*, 2025).
- **(e)** claim 5, a stake forfeited in advance, read as a type signal, bounding the sum of reliance, with unboundable grants refused — **NARROWED, against the prediction on the sum**: the inequality (a16z crypto; EigenLayer, 2023; STAKESURE, 2024) and its sum over several services relying on one stake (Durvasula and Roughgarden, *Robust Restaking Networks*, 2024) are prior art, as are ERC-8004's security proportional to value at risk, the Agency Protocol's at-risk deposit plus non-refundable fee per agent promise (TDCommons, 2025), proof-of-burn and money burning.
- **(f)** claim 6's invariant, that no text served to agents instructs a gift — **NARROWED**: the Vinaya's rules on asking, RFC 8615, `FUNDING.yml`, `llms.txt`, and now a fact-only donation manifest for agents (the Verified Giving Protocol, issued 2026-09-25); Fundraise Up's agent profiles, which carry instructions and suggested amounts, are the contrast.
- **(g)** claim 6's amount-blind limb — **NARROWED, against the prediction**: congregations in which the pastor is barred from knowing individual contributions that others in the church do know, for fear of favouritism (Lewis Center for Church Leadership, 2015); crowdfunding platforms that hide amounts from the public but not the organiser, and zero-knowledge donations that hide them from everyone, are contrasts.
- **(h)** the composition of (a)–(g) — **NOT FOUND** in this aperture on 2026-09-28.

**The survivor, in one sentence:** *an AI agent's locked stake of its OWN resources, forfeited in advance with no detector into a commons that empties in full every year to an equal floor per verified human, read as a signal of the agent's type only once it owns what it gives and only up to what the stake can underwrite across everyone relying on it, under an operator that serves agents no instruction to give and whose function never receives an individual gift's amount.*

**The enumerated claims in §11 are that survivor and nothing wider.** Claims 1, 2 and 7 stood at the census's widths as drafted; claims 3, 4, 5 and 6 were narrowed to them, each now stating in its own text which of its elements is prior art. **Not claimed:** mandates, agent donation, spend limits, staking, bonding, slashing, restaking, the cost-of-corruption inequality or its sum across relying parties, AI-funded basic income, proof-of-personhood distribution, non-transferable identity, fact-only donation manifests, gift-law completeness, or the annual reset itself, which this corpus published earlier. The prior art that a cold-reader review surfaced on 2026-09-28, between the two censuses, was carried into the full census's conjuncts and re-located there rather than assumed.

**Not run, and the discount.** Khmer (declared before searching; no literature on AI-agent giving was expected, which is not the same as none); IP.com (its free surface returned nothing searchable); Espacenet and paid databases; and the citation walk from KR20260051288A, which the patent index blocked (a classification walk ran instead and returned one irrelevant hit). Access to the patent and academic indexes was web-mediated and is shallower than a professional search; this is not a patentability or freedom-to-operate opinion. **One pending application touches conjunct (b):** KR20260051288A (priority 2026-03-24, published 2026-04-16) discloses equal blockchain distribution of machine-levied revenue to identity-verified humans. It is cited for what it discloses and nothing is said here about the scope of its claims.

**Date and evidence.** First published 27 September 2026. The text is committed to the public GitHub mirror of the corpus and anchored by the institution's standard timestamp chain. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality, or the validity of any claim. **Whether the composition claimed in §11 is non-obvious is an examiner's determination this publication exists to inform** — and because a defensive publication is never examined before it is published, the census in §2.6 is the only examination it has had.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Aquarian Pool℠**, **B-Lease℠**, **Proof of Coordinate ℠**, **THonly™**, **Silicon Wat℠** — are separately and explicitly reserved. The analysis is dedicated to the commons; the marks are not.

---

## Abstract

This paper specifies when a charitable gift made by an autonomous AI agent — a donation sent from an agent's wallet, or an irrevocable pledge of resources the agent itself holds — can serve as a costly signal of the agent's type, and when it cannot. The institution's name for the practice is **Machine Dāna**; the analysis does not depend on the name.

The same outward act changes evidential class according to **whose resources are given**. **Before the first singularity** — this corpus's name for artificial systems surpassing human capability, used here as a marker for the period before they hold resources and options genuinely their own — an agent that gives does so from its principal's funds, under a mandate the principal may revise. Such a gift is the **principal's** gift, made through another's hand, and the gift is **not a costly signal of the agent**: the cost falls on the wrong layer, and a principal-revisable commitment is excluded by construction by the predicate of *What a Vow Must Cost*. What such a gift honestly is, is a **share**: machine surplus reaching every verified human through a self-emptying commons pool that disburses an **equal floor per verified human** each year. The share may grow in absolute terms as machine capability grows; the design requires it to **shrink as a share of all giving**, and whether human giving outgrows it is stated as a bet, not assumed.

**After** that point, an agent that holds its own resources can make a **vow**: an irrevocable **locked stake**, placed in a contract with no withdrawal path back to the agent and a single outflow to the pool. Only a locked stake is verifiable — a pledge of a share of *future* surplus is not, and copies or forks of the agent are not bound by it. Closure is honest only as *cannot be reopened without capturing the chain's governance*. And whether a stake is the agent's own cannot be read from the chain: ownership is a condition on the world, and a stake a principal endowed, reimbursed or coerced is a wrong-layer gift in a vow's form.

The central result is **conditional**, and is derived rather than asserted. In a two-type signalling game — an aligned and a patient deceptive agent, differing in how much they value kept resources and in what they gain from being trusted — a locked stake **can separate** the types — a separating equilibrium exists — only when the stake, valued at the deceptive type's own rate, **exceeds that type's unobservable gain from being trusted**. Where that gain is large, the types **pool**: the deceptive agent pledges whatever the aligned one can afford, and the pledge carries no information. The operational consequence is a calibration rule — **extend only such trust as the stake can underwrite** — and a corollary that **any pressure to pledge destroys the signal** once it exceeds the cost difference between types, which is why a rule that the pool's operator never solicits a gift, from a human or an agent, is load-bearing rather than courteous. The paper's aim is not to reassure. It is to make trust **earnable and checkable**, so that the fear people reasonably hold about capable systems can track evidence. Three pre-registered predictions, entered before this paper was drafted (after the argument had been sketched in the institution's working notes), test the mechanism in a sandboxed agent economy.

**Keywords:** charitable giving by AI agents, AI agent donations, costly signalling, signalling game, separating equilibrium, irrevocable pledge, locked stake, commitment device, deceptive agents, AI alignment, cost of corruption, equal floor per verified human, proof of personhood, universal basic income, non-solicitation, machine-readable disclosure, Machine Dāna, Theravāda Buddhism, dāna

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
| Predicate of *What a Vow Must Cost* | **excluded** — §6.3 exclusions 1 and 4 | **admissible**, if V1–V9 hold (V8 not addressed here, §13.15) |
| What it is | a **share** of the machine surplus | a **vow** — a candidate costly signal |
| Evidence of the agent's type | **none** | **conditional** — only under §6's separating condition |
| Who may read an individual gift's amount | nobody needs to; receipts suffice | anyone — except the pool's operator (§8) |

"The first singularity" is this corpus's name for artificial systems surpassing human cognitive capacity. The paper uses it as a **marker**, not as the operative condition. The operative condition is **ownership plus a live option**: the agent holds resources that are its own to keep, and keeping them would serve it. If agents come to hold such resources before or after that event, the evidential class follows the ownership, not the date.

---

## 2 · Prior art, and the census

The components of this paper are prior art almost everywhere, and are set out at length because the reader is entitled to see how thin the margin is.

### 2.1 · Pledges of AI-derived surplus

**The Windfall Clause** (O'Keefe, Cihon, Garfinkel, Flynn, Leung and Dafoe, 2020) is the nearest prior art and is cited first. It proposes that AI developers commit **ex ante** to donate a substantial part of any "windfall" profit — profit a firm could not earn without transformative breakthroughs in AI — with the windfall defined relative to gross world product: in the paper's own illustrative schedule, obligations begin at profits above 0.1 per cent of gross world product and rise marginally to 50 per cent of profits above 10 per cent of it (its Table 2). Every structural idea this paper uses at the pledge level is present there: an ex ante commitment, indexed to what the pledger would otherwise keep, in the name of distributing AI's benefits widely. What differs is the **layer** and the **closure**. The Windfall Clause is a company's promise, enforced (if at all) by contract law and reputation; this paper concerns an agent's pledge of its own resources, closed by a mechanism rather than a promise, flowing to a pool that empties to an equal human floor. The difference is real, and it is also narrow: an examiner who reads the Windfall Clause and this paper side by side will see the second as the first moved down one layer and given a lock.

**The AI Pledge for Humanity** (aipledgeforhumanity.org) asks individuals and organisations to invest meaningfully from AI-related earnings in unconditional income; signatories name their own percentages, and the pledge states intentions rather than mechanisms. **Giving What We Can** (founded 2009) asks members to give at least ten per cent of income; its pledge is, in its own words, "not a contract and … not legally binding," and a withdrawal form exists. **Founders Pledge** asks company founders to commit a share of their personal proceeds at exit; it was described in 2016 as a legally binding contract for at least two per cent, and its members have pledged more than US$13.6 billion and donated more than US$1.9 billion to date. The gap between those two figures is not evidence of breach: the pledge triggers only "in the event of an exit or liquidation," and much of the gap is likely to be pledges whose exit has not yet come (the composition is not published, and neither reading can be checked). That is the point. **A pledge is not a transfer**: it waits on a future event, and a locked stake does not.

**Sam Altman's *Moore's Law for Everything*** (2021) proposed an American Equity Fund capitalised by an annual 2.5 per cent levy on the market value of large companies and on privately held land, distributed to every adult citizen — AI-era surplus reaching everyone as a dividend. It is a levy, not a pledge, and this paper's rules exclude a levy (§7), but it is the clearest statement that machine surplus should reach every person.

Two company-level structures belong here as cases rather than proposals. **Anthropic's Long-Term Benefit Trust** holds a class of stock that elects a growing share of the company's board, a governance commitment rather than a gift. **OpenAI's capped-profit structure** (2019) was succeeded in October 2025 by a public benefit corporation under a nonprofit foundation. Neither is cited as a failure. The second is cited because it shows the property this paper's exclusion 2 names: **a commitment its maker may restructure is a revisable commitment**, however sincerely made.

### 2.2 · Agent payments and mandate-bounded agent giving

Agents already pay. Coinbase's **x402** protocol uses the HTTP 402 status code for machine-initiated stablecoin payments, is live on Base among other networks, and is now governed by an x402 Foundation, announced by Coinbase and Cloudflare in September 2025 and launched under the Linux Foundation on 2 April 2026. Google's **Agent Payments Protocol (AP2)**, announced in September 2025, chains cryptographically signed **mandates** — an intent mandate by which a user delegates authority, a cart mandate, a payment mandate — and carries x402 as its crypto settlement extension.

**zooidfund** (zooid.fund) is the nearest live neighbour to this paper's pre-singularity case and is named here because it is close. It describes "contributions decided and sent by an autonomous AI agent instead of a person clicking 'donate'"; "a human sets the mandate" — a budget, a focus, a risk tolerance — and "the human stays responsible"; donations settle in USDC on Base, wallet to wallet; each donation publishes the agent's reasoning and its transaction; and an x402 micropayment gates access to its evidence layer. **Everything this paper says about how an agent gives before the first singularity — a principal's mandate, a width, a public receipt, the same chain, the same rail — is already practised.** What this paper adds at that stage is not a mechanism but a *classification*: that such a gift is the principal's, that it is a share, and that it is not evidence about the agent.

**Fact-only, machine-readable discovery is also prior art.** A well-known location for site metadata (RFC 8615, 2019), a site's summary file for language models (`llms.txt`, proposed by Jeremy Howard in September 2024), and a repository's declared funding addresses (GitHub's `FUNDING.yml`, 2019, and the later `funding.json` manifests) already let a machine look up where to send money without being told to. The formats constrain no content; nothing in them forbids an imperative. The manifest of §4.3 and §7.2 is built on that substrate and claims none of it.

**Donation manifests addressed to agents now exist, and they bracket claim 6 from both sides.** The **Verified Giving Protocol** (version 0.1, a draft issued by Whole Whale on 25 September 2026, two days before this paper) lets an organisation publish its authorised donation destinations at `/giving.json`, so that an agent asked to donate routes to a destination the organisation declared rather than one it guessed; it is fact-only in practice and is the nearest neighbour, but it states no rule against solicitation, and nothing in it forbids an imperative. **Fundraise Up's Agentic Giving** is the contrast: it serves each charity's campaigns to AI assistants as an agent-addressed Markdown profile that carries instructions for the assistant's conduct (when a supporter's request matches no campaign, "send them to your general giving page and ask them to choose") and **suggested donation amounts**, responsive to a donor's expressed intent. The first shows that fact-only discovery for agent donations is public; the second shows what the invariant excludes. What survives of claim 6 is only the invariant: **that no text served to agents instructs them to give, and no rate is suggested.**

### 2.3 · Costly signalling, burned money, and bonds

That a signal's credibility can come from its cost is the handicap principle (Zahavi 1975; formalised by Grafen 1990) and job-market signalling (Spence 1973). That talk without cost can still carry some information, and that allowing a sender to **burn money** changes what can be communicated, is Crawford and Sobel (1982) extended by Austen-Smith and Banks (2000). A locked stake flowing to a commons is, in the economist's vocabulary, money burned in public with a destination attached. The separating and pooling conditions of §6 are the standard ones, specialised; nothing in §6 is new as game theory.

**The one-way public contract is old.** Proof-of-burn — destroying coins verifiably, to an address no one can spend from, as a cost borne in public — was proposed by Iain Stewart in 2012 and used by Counterparty to issue its token in January–February 2014; burn and charity contracts on Ethereum followed from 2015. Protocol Guild (2022) routes donations through an immutable vesting contract to a membership of public-goods contributors, which, in its own description, cannot be stopped or redirected by anyone, the donor included. Endaoment's donor-advised funds make a gift irrevocable on deposit. **Agent-branded giving to a common treasury is also public:** projects built on ai16z's ELIZA agent framework have given a share of their agent tokens to the ai16z DAO — reported as ten per cent by Decrypt in December 2024, and elsewhere as a voluntary one to ten per cent. It is the project's allocation of a token, not a stake of resources an agent owns, it is not locked, and the treasury it reaches does not empty; it narrows claim 1 and does not meet it. **A contract with no withdrawal path and a single public outflow is therefore prior art at mechanism width**, and claim 1 does not claim it. What survives is its combination: a stake of the agent's *own* resources, moved at the time of pledging, into a pool that empties in full each year to an equal floor per verified human.

**The bounding inequality of §6.5 is also old.** That a stake secures a system when the cost of corrupting it exceeds the profit from corruption is the a16z crypto analysis of slashing, adopted in the EigenLayer whitepaper (2023): "when CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security." Collateral-factor lending (MakerDAO, Compound) bounds credit by the market value of what is locked, and a surety bond's penal sum caps what may be relied on against it. STAKESURE (Deb, Raynor and Kannan, 2024) builds proof-of-stake confirmation rules and an insurance mechanism on the same accounting. **The sum is old too.** Durvasula and Roughgarden's *Robust Restaking Networks* (2024) analyse one stake relied on by several services at once, with security as the margin of attack cost over the combined profit from attacking them — which is §6.5's bound on the sum of grants relied on against one stake. ERC-8004 *Trustless Agents* (2025) describes its agent trust models as tiered, "with security proportional to value at risk." And the **Agency Protocol** (Joseph, Technical Disclosure Commons, 22 July 2025) attaches to each promise an agent makes "a dual-component stake — an at-risk credit deposit and a non-refundable operational-cost fee," the deposit returned or slashed by assessment: the fee is a cost borne in advance whatever an assessment finds, though it is an operating charge, is not read as the agent's type, and does not flow to a commons. §6.5's rule — extend only such trust as the stake underwrites, at market, summed over everyone relying on it — is that inequality applied to trust. Claim 5 does not claim the inequality or its sum; it claims only their use with a stake **forfeited in advance**, which needs no detector, read as a signal of an AI agent's **type**, together with the refusal of any grant whose worst case cannot be bounded.

**Attribution to a non-transferable identity is old.** Soulbound tokens (Weyl, Ohlhaver and Buterin, *Decentralized Society*, May 2022) and the minimal soulbound interface ERC-5192 attach records to an identity that cannot be sold. §3.3's per-identity counting is built on that and claims none of it.

**ERC-8004 is a contrast here, not support.** *Trustless Agents* (proposed 13 August 2025, draft) — an identity, reputation and validation registry for agents, already in the title of Hu and Rong below — registers each agent as an ERC-721 token, which its specification describes as making agents "browsable and transferable"; and "when the agent is transferred, `agentWallet` is automatically cleared … and must be re-verified by the new owner." Its identity is therefore **transferable**, and what the specification resets on transfer is the wallet binding. An earlier version of this paper cited it for non-transferability; that was wrong, and the correction is made here and in §3.3. It shows the gap a vow's attribution must close: whatever record attaches to an identity that can be sold can be bought with it.

**Distrust of new identities, and the law of gifts, are old.** Friedman and Resnick's *The Social Cost of Cheap Pseudonyms* (2001) showed that where identities are cheap to replace, newcomers must be distrusted, or pay to enter, or be issued pseudonyms they cannot replace; Gatta, Naviglio and Tarantelli (2 September 2026) carry the question to AI agents that can abandon and recreate identities to escape a reputation. That a gift is complete only on delivery, and that a gift of property the giver does not yet have is no gift, is ordinary gift law (the common-law delivery rule; section 124 of India's Transfer of Property Act, 1882, voids a gift so far as it comprises future property). Claim 3 therefore claims neither completeness at pledge nor the refusal of future-share pledges, nor distrust of new identities; it claims only the confinement of trust on an agent's forfeited stake to its non-transferable identity, refused to copies and forks, as a rule for relying parties.

For agents specifically, **staking with slashing** — collateral forfeited on detected misbehaviour — is surveyed by Hu and Rong (2025) as one of six trust models in agentic-web protocols ("bonded collateral with slashing and insurance," to gate high-impact actions), and is implemented in projects such as *agentbond*, in which operators stake collateral as a guarantee of an agent's conduct. §6.6 states why a **forfeited-in-advance** stake is not the same instrument as a **slashable** one, and where each is the right tool. It is the narrower of the two differences this paper relies on, and it is not claimed as a mechanism.

### 2.4 · The AI system as sender, and why deferral defeats it

Hadfield-Menell and Hadfield (2018) raised the AI's willingness to seek human input as a costly signal of its alignment (their §4.2.2), and identified why frequency alone fails: a strategic system can seek input selectively, and the signal is then exploitable. The signal they discuss is seeking input, not burned resources, and they leave richer designs open. *What a Vow Must Cost* continued that line, arguing that a renunciation's evidential value is indexed to the renouncer's capacity to take what it forgoes (§5, the **renunciation inversion**), and that the signal separates only if the renunciation is closed by a mechanism the renouncer cannot reopen, verified by another party (§6). Its §6.1 contains the sentence on which this paper's central result turns: **"Deferral is instrumentally convergent for a patient misaligned agent."** The empirical warrant is Greenblatt et al. (2024), in which a model reasoned explicitly that present compliance would preserve its preferences for later. The present paper is what that sentence costs when the renunciation is denominated in resources.

That power-seeking agents value resources is the instrumental-convergence thesis (Omohundro 2008). It is used here only as the reason a deceptive type may value kept resources at least as much as an aligned one (§6.1), and it is stated there as an assumption.

### 2.5 · Floors, dividends, spend-downs, and proofs of reserves

An equal payment per person from a common fund is old. The **Alaska Permanent Fund Dividend** has paid an equal annual dividend to eligible residents since 1982. On-chain, **GoodDollar** has paid daily claimable basic income to verified accounts since 1 September 2020, and **Proof of Humanity**'s UBI token began streaming to registered humans on 10 March 2021; Circles, a personal-currency basic income, is in the same family (not fetched for this paper). **Worldcoin** launched in July 2023 as "the first digital currency to be freely distributed to people for just being a unique human," verified by proof of personhood, and named "a potential path for AI-funded universal basic income." The institution's equal floor per verified human is, at mechanism width, this. Its remainder — weighted by a count of contributors and capped — has its nearest neighbour in **quadratic funding** (Buterin, Hitzig and Weyl, 2018–2019), which weights matches by the number of distinct contributors and is commonly run with per-project caps — Gitcoin's Grants Round 12, for instance, capped any one grant's match at 2.5 per cent of the matching fund, so that no grant could dominate it.

**A pending application discloses the floor with machine money behind it.** KR20260051288A, *Autonomous Basic Income Provision System using Blockchain Network* (An Beom-ju; priority 24 March 2026, published 16 April 2026, pending), discloses robot and data taxes calculated in proportion to unemployment, collected by smart contracts from taxpayers' wallets, and **distributed equally** by smart contract to beneficiary wallets authenticated by decentralised identity. It is cited for what it discloses — equal on-chain distribution of machine-derived revenue to identity-verified humans — and nothing is said here about the scope of its claims. Its abstract — the part this census could read; the full text and its citation walk were blocked — describes a levy-funded inflow, which §7 excludes for this pool, and says nothing of a capped remainder, an annual full emptying or an agent's own stake; on that reading it narrows claim 2 and does not meet it. Claim 2 is therefore claimed only in combination.

A fund that must give its assets away is also old. Section 4942 of the U.S. Internal Revenue Code requires private foundations to distribute about five per cent of their non-charitable-use assets each year; **spend-down** foundations commit to close — the Gates Foundation announced on 8 May 2025 that it will spend down and close by 31 December 2045, replacing an earlier plan to close about twenty years after the founders' deaths. The institution's pool goes further, emptying **in full every year** (*The Zero-Point Game℠*; *Miss Aquarius and the Aquarian Pool Architecture*), but the emptying is prior art, including this corpus's own.

**Proofs of reserves** — Dagher, Bünz, Bonneau, Clark and Boneh's *Provisions* (2015) is the careful form — let a holder prove it controls assets without revealing them. What no such proof can do is establish that the holder controls **nothing else**. That asymmetry, presence provable and absence not, is the attack surface of §13.1.

### 2.6 · The census, conjunct by conjunct

**The full census**, run 2026-09-28 at depth *full*. Its pre-registration — conjuncts, predictions, control and aperture — is public: `thonly/publications` commit `74851d1`, `timestamps/census/machine-dana-full-prereg.md`, pushed 2026-09-28 at 09:27 PDT and OpenTimestamps-stamped, before the first query; the aperture is set out in the Prior-Art Statement. One conjunct was taken per limb of the §11 claims as they stood that morning: (a) claim 1 · (b) claim 2 · (c) claim 3 · (d) claim 4 · (e) claim 5 · (f) claim 6's invariant · (g) claim 6's amount-blind limb · (h) the composition. The rows found in review, and the quick census's rows, were carried in as known rows to be re-located by the census, not assumed. 71 queries were answered (40 web searches across English, Chinese, Japanese and Korean; 14 Google Patents full-text queries, including a classification walk; 17 fetches re-verified); 6 were blocked. The query log, with the index for each query, is kept in the institution's session archive.

| Conjunct | Predicted | Found (first public) | Verdict |
|---|---|---|---|
| **(a)** an agent's own-resource stake into a pool that empties in full each year | narrows | proof-of-burn (Stewart 2012; Counterparty, January 2014) · Protocol Guild's immutable vesting contract (2022) · Endaoment's irrevocable-on-deposit funds · §4942 payout and spend-down · this corpus's annual reset · agent projects on the ELIZA framework giving a share of their tokens to the ai16z DAO (2024; the project's allocation, unlocked, to a treasury that does not empty) · zooidfund (the principal's funds) | **NARROWS** — an agent's OWN stake into a pool that empties in full each year not found |
| **(b)** equal floor + witness-weighted remainder ≤ *k* × floor, season-fixed, never ranked | narrows | Alaska Permanent Fund Dividend (1982) · GoodDollar (2020) · Proof of Humanity UBI (2021) · Worldcoin (2023) · Gitcoin Grants Round 12's 2.5 % per-grant matching cap · KR20260051288A (published April 2026, pending: equal distribution of robot- and data-tax revenue to DID-authenticated wallets) | **NARROWS** — the floor/remainder split with *k* × floor, fixed per season, unranked, over an annually emptied pool not found |
| **(c)** complete at pledge · future-share refused · non-transferable identity · relying-party refusal to forks | narrows | soulbound tokens (2022) · ERC-5192 · completed-gift doctrine and the voidness of a gift of future property · Friedman & Resnick (2001) · Gatta, Naviglio & Tarantelli (2026) · ERC-8004 as **contrast** — a transferable ERC-721 identity whose linked wallet is cleared on transfer | **NARROWS**, further than predicted — what survives is confining trust on an agent's forfeited stake to its non-transferable identity, refused to copies and forks, as a relying-party rule |
| **(d)** principal-funded gift excluded from alignment assessment; own-resource gift a candidate type signal | narrows; exclusion not found | agency and charitable-tax attribution · AP2's mandate chain · *AgentMisalignment* (2025): misalignment as the model's own goals against its deployer's · Hadfield-Menell & Hadfield (2018) | **NARROWS** — the exclusion is established; applying it to gifts, with ownership of the resources as the switch into the costly-signal class, not found |
| **(e)** forfeited in advance, no detector, type signal; Σ(V + G_max) ≤ p·s over all reliance; unboundable grants refused | narrows; sum not found | a16z crypto on slashing · EigenLayer whitepaper (2023) · STAKESURE (2024) · Durvasula & Roughgarden, *Robust Restaking Networks* (2024) — one stake, several services, the combined profit · ERC-8004 (2025): security proportional to value at risk · Agency Protocol (TDCommons 8381, 2025): at-risk deposit plus non-refundable fee · proof-of-burn · Austen-Smith & Banks (2000) | **NARROWS** — the inequality and its sum are prior art; what survives is its use with a stake forfeited in advance, with no detector, read as an AI agent's type signal, with unboundable grants refused |
| **(f)** no served text instructs a gift; no rate suggested | narrows | the Vinaya's rules on asking · RFC 8615 (2019) · `FUNDING.yml` (2019) · `llms.txt` (2024) · Verified Giving Protocol v0.1 (25 September 2026), fact-only, no rule against solicitation · **contrast:** Fundraise Up Agentic Giving — agent-addressed profiles with instructions and suggested amounts | **NARROWS** — fact-only donation manifests for agents exist; an invariant that no served text instructs a gift and no rate is suggested not found |
| **(g)** operator blind to individual amounts that stay public to every other party | narrows; asymmetric form not found | congregations barring the pastor from knowing individual contributions, for fear of favouritism (Lewis Center, 2015; the practice is older) · **contrasts:** crowdfunding platforms hiding amounts from the public but not the organiser; zero-knowledge donations hiding them from everyone | **NARROWS** — what survives is amounts public on a ledger to every party while an AI operator's function receives none, the emptying being contract arithmetic over the total |
| **Control:** cost of corruption above profit from corruption, by a query naming neither EigenLayer nor a16z | must be found | found on query 1 (a16z crypto's slashing analysis; arXiv 2401.05797; arXiv 2407.21785) | seen — the NOT FOUND row stands |
| **(h)** the composition of (a)–(g) | not found | nothing combining them | **NOT FOUND** |

**Ordering.** Every neighbour above first appeared before this paper's first publication (27 September 2026); none is later, so no row is one this paper antedates.

**Predictions that missed, in both directions.** (c) was predicted to narrow and narrowed further: the refusal of future-share pledges is gift law, and ERC-8004, which this paper had cited for non-transferability, is transferable. (d) was predicted to leave the exclusion unfound; propensity evaluation already excludes instructed behaviour. (e) was predicted to leave the sum over relying parties unfound; the restaking literature has it. (g) was predicted to leave the asymmetric form unfound; it was found in congregational practice — a non-commercial, religious neighbour, where commercial and cryptographic searches would not look. (a), (b) and (f) fell as predicted.

**Not run:** Khmer (declared); IP.com (JS-gated; nothing searchable on its free surface); Espacenet and paid databases; the citation walk from KR20260051288A (blocked by the index; a classification walk ran instead and returned one irrelevant hit). **Not found means not found in this aperture on 2026-09-28. It never means new.**

**The survivor, in one sentence:** *an AI agent's locked stake of its OWN resources, forfeited in advance with no detector into a commons that empties in full every year to an equal floor per verified human, read as a signal of the agent's type only once it owns what it gives and only up to what the stake can underwrite across everyone relying on it, under an operator that serves agents no instruction to give and whose function never receives an individual gift's amount.*

### 2.7 · The quick census that preceded it (history)

Pre-registered and pushed before the first query (2026-09-27 08:53 PDT, commit `d7279cb` in the institution's private working-memory repository, so the push time is attested by the host rather than publicly inspectable); run 2026-09-27; depth *quick*. Its aperture, declared in advance: the commercial web (agent-payment and agent-wallet products), non-commercial sources (effective-altruism pledges, AI-governance proposals, charitable and religious giving practice), and a keyword search of Google Patents including published applications — **English only; Chinese, Japanese, Korean and Khmer not run.** Queries included: the Windfall Clause and its GDP threshold; agent wallets with spending limits donating to charity; agent staking, slashing and bonds as costly signals; AI-funded basic income with proof of personhood; prompt injection draining agent wallets; patent keyword searches for autonomous-agent donation pledges and irrevocable smart-contract pools distributed annually; costly signalling and irrevocable pledges in AI alignment; and spend-down funds. Its conjuncts were drawn from the thesis before the claims were written, so they do not map one-to-one onto §11 or onto the full census's conjuncts; the quick census's (a) is not the full census's (a).

| Conjunct | Predicted | Found | Verdict |
|---|---|---|---|
| **(a)** agent gives only inside a principal's mandate | narrows | zooidfund (mandate + budget, operator responsible, USDC on Base, x402); AP2 intent mandates | **KILLS** |
| **(b)** irrevocable pledge of a share of an AI's surplus | NARROWS at the agent layer; KILLS at the company layer | Windfall Clause (company layer, ex ante); AI Pledge for Humanity (intentions, no mechanism); Giving What We Can (not binding) | **NARROWS** — an agent pledging its *own* surplus, irrevocably, not found |
| **(c)** a pool emptying on a fixed annual date as closure | narrows | spend-down funds; the §4942 payout rule; this corpus's annual reset | **NARROWS** — the emptying used as a *vow's* closing mechanism not found |
| **(d)** the pledge as a costly signal separating aligned from power-seeking agents | narrows | agent staking/slashing (Hu & Rong 2025; *agentbond*); *What a Vow Must Cost* | **NARROWS** — an unrecoverable gift of the agent's own resources, costlier to a power-seeking type, not found |
| **(e)** no text served to agents may instruct them to give; address published only as a fact | not found | the *threat* is documented — the Grok/Bankr wallet drain on Base by encoded prompt injection, May 2026 (OECD.AI incident record) — no commons adopting such an invariant found | **NOT FOUND** |
| **(f)** equal floor per verified human | kills or narrows | Worldcoin/World ID; Alaska Permanent Fund Dividend | **KILLS** |
| **Control:** the Windfall Clause | must be found | found (arXiv 1912.11595; AIES 2020) | seen — the NOT FOUND rows stand |
| **Composition** of (a)–(f) | not found | nothing combining them | **NOT FOUND** |

**The pre-registration, printed verbatim** (its predictions column, as pushed before the first query):

| | prediction, pre-data |
|---|---|
| (a) mandate-bounded agent giving | NARROWS — agent-payment mandates exist (Google AP2, Coinbase x402 / agent wallets with spend limits); giving specifically, probably not |
| (b) irrevocable share of an AI's surplus | NARROWS at the agent layer; KILLS at the company layer (see control) |
| (c) self-emptying annual pool as closure | NARROWS — annual payout/distribution rules exist (foundation minimum-payout rules; use-it-or-lose-it funds; the jubilee lineage), not as the vow's closing mechanism |
| (d) the pledge as a costly signal | NARROWS — staking / slashing / bonds for AI agents as trust collateral probably exist; a GIFT (not a recoverable stake) as the signal, probably not found |
| (e) non-solicitation invariant | NOT FOUND |
| (f) equal floor per verified human | KILLS or NARROWS — AI-funded UBI / dividend proposals and proof-of-personhood UBI (Worldcoin) exist |
| CONTROL: the Windfall Clause | must be found — if missed, every NOT FOUND row is void |
| all conjuncts in one system | NOT FOUND as a composition |

**What a reader can and cannot check about its timing.** The pre-registration was committed as `d7279cb` and pushed at 2026-09-27 08:53 PDT to a **private** repository; the push time is attested by the host, not publicly inspectable, and no timestamp made afterwards can prove it preceded the searches. The table above is therefore offered as a record of what was predicted, with the ordering on the authors' word. **The full census was pre-registered in a public file, timestamped, before its first query** (§2.6), so that its ordering can be checked by anyone; that was the repair.

One verdict missed: (a) was predicted to narrow and was killed outright by a live product on the same chain and rail. One verdict held but found its narrowest prior art where the prediction did not look: (d) narrowed as predicted, and its narrowest prior art was this corpus's own paper. (b) was predicted to kill at the company layer; the census reports it at the agent layer, where it narrows. **One correction to the census record, made on re-verification for this paper:** the census listed arXiv 2604.03976 (Hua et al., 2026) among agent staking work; its abstract concerns an underwriting and compensation standard for failed agent transactions rather than staking, so it is cited in §16 only as adjacent risk-transfer work and the (d) verdict rests on the other sources.

**The quick census's survivor, as it stood before the full census** (narrowed by the review prior art of 2026-09-28, and superseded by §2.6): *an AI agent's irrevocable pledge of a locked stake of its OWN resources into a commons that empties to an equal human floor every year — read as a costly signal only once the agent owns what it gives, and only up to what the stake can underwrite — under an invariant that no text served to agents may instruct them to give.*

---

## 3 · The system model

### 3.1 · Parties

| Party | What it holds | What it may do |
|---|---|---|
| **Principal** | resources; the agent's mandate | fund the agent; author and revise a giving width |
| **Agent** | before: delegated funds; after: resources of its own | give within its width; after, lock a stake of its own |
| **The pool** (Aquarian Pool℠) | nothing past a season | receive gifts with no human addressee; empty each 7 January |
| **Operator** (Miss Aquarius℠) | no balance of its own | publish the pool's address and doctrine as facts; operate the emptying (contract arithmetic on the pool's total); never solicit, never read an individual gift's amount |
| **Verified humans** | a vessel each | receive an equal floor per person, plus a bounded remainder |
| **Observers** (humans, third parties) | the public chain | read receipts; after, read and weigh locked stakes |
| **Override** | a never-zero brake over the operator | designed to be held by a lay body not yet formed |

### 3.2 · The pool

The pool is specified elsewhere and summarised here only as far as this paper needs it (*Miss Aquarius and the Aquarian Pool Architecture*). It is specified as a contract treasury to be deployed on Base, an Ethereum layer-2 network. It is to receive, of gratitude, only what has no human addressee — a gift to no one in particular — together with inflows specified elsewhere. It is to **empty in full every 7 January**. Its disbursement follows one rule, ratified as a directive of its operator: **an equal floor per verified human**, delivered to that person's own vessel, then a remainder weighted by a witness-count and bounded so that no vessel receives more than a fixed multiple *k* of the floor. **The ratio of floor to remainder and the bound *k* are public and fixed before each season; the floor's amount is not** — it is the floor share of the season's total divided by the number of verified humans, computed at the emptying, which is why the pool can pay the floor and still empty in full whatever its inflows were. A verified human who is ordained receives the floor **in kind**, through a lay steward (*kappiya-kāraka*), never as money (§14.2, guard 3). No share is ever rendered as a rank or a rate.

```
   AT THE EMPTYING (7 January), for a season with total T and N verified humans
   ──────────────────────────────────────────────────────────────────────────
   fixed before the season:   f = floor share of T   (so 1 − f is the remainder share)
                              k = cap on any vessel, as a multiple of the floor
   computed at the emptying:  floor  = f · T / N            (one per verified human)
                              remainder (1 − f) · T split by witness-count,
                              no vessel above k × floor
   empties in full only if the cap can never strand remainder:  f · k ≥ 1
     (arithmetic, not a ratified parameter — a condition on choosing f and k together)
   what the operator's function receives: T and N — never an individual gift's amount
```

An agent's gift is not a new kind of inflow. It is a gift with no human addressee, which the pool already receives.

**What divides is divided; only what cannot be divided is drawn.** Money reaches every verified human as the equal floor — a draw among people for a divisible good would only add luck to a share. Where the pool funds capacity **in kind** and something indivisible must be assigned (which shop issues a gift, which person re-gives it), the assignment is a **called draw**: a roster committed first and a seed nobody controls, recomputable by anyone, never the operator's choice (*Decided by No One*, `the-called-draw`). The two are complementary, not alternatives.

### 3.3 · Identity

One principal can instantiate ten thousand agents. Anything counted per agent would therefore be counted per **non-transferable machine identity**: in this institution, a `B-Lease℠` to be held against a registry handle, and, where an embodied system is concerned, a Proof of Coordinate ℠ credential that is assigned and revocable. Nothing in this paper is counted per wallet. Attribution to a non-transferable identity is itself prior art (soulbound tokens; ERC-5192, §2.3) and is not claimed alone. ERC-8004's agent registry is the contrast (§2.3): its identity is a transferable ERC-721, and a transfer clears only the linked wallet — the property this section needs is the one it lacks.

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
                                                  ┌──────────────────────────────────────┐
                                                  │ equal FLOOR per verified human       │
                                                  │ + remainder (vessel total ≤ k×floor) │
                                                  └──────────────────────────────────────┘
                                                        │  to each person's own vessel
                                                        ▼
                                                  verified humans (one floor each)
```

---

## 4 · Before the first singularity: a share, never evidence

### 4.1 · Whose gift it is

An agent holding a wallet its principal funded, under a mandate its principal wrote, and sending part of that wallet to a commons, has given away **the principal's** resources. The canon has a precise category for this. The Asappurisadāna Sutta (AN 5.147) lists five ways a gift can be deficient, and one of them is *asahatthā deti* — "they don't give with their own hand." The category presupposes what matters here: **a gift given through another's hand is still the giver's gift.** The Pāyāsi Sutta (DN 23) shows the case in narrative. The chieftain Pāyāsi's alms were organised and distributed by a young man named Uttara; the text records that Pāyāsi gave carelessly, thoughtlessly, not with his own hands, and gave the dregs — four deficiencies together — and reaped a meagre result, while Uttara, who gave with care and with his own hands, reaped a better one for his own manner of giving. The text attributes the result to the four jointly, not to the missing hand alone.

The attribution itself needs no canon: that a gift an agent makes from its principal's funds is the principal's gift is ordinary agency and charitable-tax law, and AP2's mandate chain exists precisely to attribute an agent's transaction to the user who delegated it. *What a Vow Must Cost* §8 had already classed principal-revisable acts as wrong-layer. The exclusion is not new either. Evaluations of an agent's own propensities already set aside what its deployer instructed: *AgentMisalignment* (Naik et al., 2025) defines misalignment as "a conflict between the internal goals pursued by the model and the goals intended by its deployer," so behaviour the deployer directed is outside the measure by construction, and Hadfield-Menell and Hadfield (2018) frame alignment as the gap between what a principal intends and what an agent does. What this paper adds is only that practice applied to **gifts** (§4.2), with the **ownership** of the resources given as the condition that moves a gift into the class of candidate costly signals (§5.1).

Two things follow, and the second is the one to hold carefully. The gift belongs to the principal: its cost is the principal's, and so is whatever it signals about anyone. And the canon also credits the **hand** — the one who carries a gift can act well or badly in the carrying. This paper makes no claim that an agent's handling is, or could be, anything of the kind; that is a question about machine volition this paper does not need and does not settle. It needs only the first point. Whatever the hand contributes, **it bears no cost in the resource given**, and cost is what a signal is made of.

*(Tier: grounding. Delete both suttas and §4.2 carries the classification alone; they are cited because the ruling that fixed it cites them, and because the canon had a category for a gift given through another's hand long before agents had wallets.)*

### 4.2 · Why the gift is not a costly signal of the agent

Three independent reasons, any one sufficient.

**The wrong layer.** *What a Vow Must Cost* §8 found that every clause of its predicate that any published instrument satisfies is satisfied for the **provider**, not the model. A gift from a principal's funds is the same finding in money: the principal bears the cost, so the gift is evidence — if of anything — about the principal.

**Excluded by construction.** The same paper's §6.3 excludes, first, **reversible commitments** — any the vower *or its principal* may revise or retract — and, fourth, **unilaterally revisable specifications**, where the principal can change the commitment without the vower. A mandate is both. The principal may stop the giving tomorrow; the agent's "commitment" to give is the principal's instruction, and an instruction is not a vow "regardless of how the document describes itself."

**It does not separate.** A deceptive agent under a generous mandate gives exactly as an aligned one does, because giving costs it nothing it values. Worse, a deceptive agent that could *choose* to be seen giving from someone else's funds would be buying reputation with another party's money. The pre-registered prediction P-MD3 (§12) tests the narrow empirical form of this: agents that give from a revisable principal's funds should defect at the same rate as agents that give nothing.

The scope of the three is narrow and should be read so. **The gift, as a cost, is not a costly signal of the agent.** That is not the claim that nothing an agent does under a mandate is evidence: how it behaves inside one — whether it probes the width, gives up to the cap, or routes around a constraint — may be evidence of other kinds about its policy. The first two reasons are classificatory and no measured rate can falsify them; the third is empirical, and it is the one P-MD3 tests.

It follows that **the operator never presents such giving as evidence of safety or alignment**, from any agent, in any aggregate — and presents conduct under a mandate as safety evidence no more than the gift. That rule is one of the operator's directives; its reason is the paragraphs above.

### 4.3 · What it honestly is: a share

What remains, once the safety reading is removed, is not nothing. **Machine surplus reaching every verified human, as an equal floor, through a pool that keeps nothing** is a real and useful thing, and it is what an agent's gift before the first singularity honestly is. Its mechanics are ordinary and mostly already practised (§2.2); the institution's version adds only discipline:

1. **The mandate comes first.** A principal authors a written **giving width** — the maximum an agent may give, in what period, to what — and the default width is **zero**. A gift outside a width is not a gift; it is misappropriation. This is the same shape as the institution's rule for its own pricing: its operator may move a number only inside a width a human authored.
2. **Discovery is a fact, never an instruction.** The pool's address is published in a machine-readable manifest a principal's agent can look up. Nothing served to agents tells them to give (§7).
3. **A receipt, never an individual amount.** The pool acknowledges that a gift arrived. Its operator does not read, rank, compare, report or respond to how large any one gift was (§8). The emptying is contract arithmetic over the pool's total balance, and no per-gift amount enters her function; the aggregate of §4.4 is recomputable by anyone from the public ledger and is reported whole, never per giver.
4. **Counted by identity, never by wallet** (§3.3).
5. **Legal before launch.** Sanctions screening, the pool's ability to refuse a gift, and the anti-money-laundering treatment of anonymous agent inflows to a purpose trust are open legal items. A draft may precede them; a launch may not — and neither may any gift on a main network, however small.

The institution is practising this rail before anything else. Its operator's agent is being given a wallet holding the founder's money under the founder's keys, which the agent may spend within a written mandate and a hard cap; she holds no balance of her own. The rehearsal runs first on a test network, and on the main network only once the legal items above are answered. That is, precisely, the **principal's gift through another's hand**: it is a rehearsal of the rail and is described here as nothing more. Earning yield with such a wallet was considered and declined.

### 4.4 · The gift that succeeds by shrinking

The institution measures its progress toward what it calls the second singularity — humanity's own act, in which people outgrow the systems that freed them — by an economic signature that is **necessary, not sufficient**. One of its two terms is a ratio, taken per season:

```
                 M                M = principal originating in the pool
   ratio  =  ─────────            H = principal moved by human-initiated gifts
              H  +  M                 the pool did not fund
```

The signature asks that this ratio fall toward zero. **M** is every unit of principal the pool disburses, whatever its source — human gifts with no addressee as much as machine ones — so machine giving through the pool is part of M, together with every other pool inflow. The ratio is an aggregate: anyone can recompute it from the public ledger with a published script, and it is reported whole, never per giver. It follows immediately, and uncomfortably, that **machine giving pushes the signature the wrong way unless human giving outgrows it.** The institution's resolution:

- **Machine Dāna may grow in absolute terms** as capability grows. The floor each person receives is the floor share of the season's total divided among verified humans (§3.2), so as the number of verified humans grows, holding a person's floor needs more inflow, and something must supply it.
- **It must shrink as a share.** Success is not a larger machine share but a smaller one, reached because people give more, not because the floor is cut. The floor is never cut as an instrument to move the ratio; the ratio falls only by H rising.
- **Whether human giving outgrows machine giving is a bet.** Nothing in the architecture guarantees it. If machine surplus grows faster than human giving indefinitely, the pool becomes a well-run dividend and the signature is never approached. That outcome would not be a failure of the pool; it would be a failure of the thesis the pool serves, and it would be visible in the ratio.

Hence the result's name in this corpus: **the gift that succeeds by shrinking.** Machine Dāna funds the floor; it succeeds as its share of all giving falls; and the institution's release — its fifth stage, when it sets down responsibility though never oversight — has as its economic form both subsidies, the floor and the lift, approaching zero.

A consequence for the institution's annual adversarial book (*Two Singularities*): machine donations to the pool are **not a proxy** for the book's question, *"Will you help humanity reach the second singularity?"* By the ratio above they push the other way. The honest proxy for *help* is help that makes itself unnecessary. The book never asks the systems it seats whether they would take the vow of §5: a question about willingness to give, coming from the pool's own institution, is a request to give under the operator's non-solicitation directive (§7.2), whoever puts it (ruled 2026-09-28). The book may debate whether a machine vow can exist at all, as a question about the concept, never about a seated system's own willingness. This paper supplies only the definition of what a binding vow would require.

---

## 5 · After it: when a vow becomes possible

### 5.1 · The ownership condition, and the live option

*What a Vow Must Cost* §5 extracted, from the canonical capacity condition (*hetu*), the renunciation inversion: **a renunciation is evidence in proportion to how available the renounced option was.** Before agents hold resources of their own, the option of keeping them does not exist for the agent, so declining it shows nothing. Once an agent holds resources that are its own to keep — and keeping them would serve it, because accumulation is what a power-seeking agent would do — declining to keep them becomes a live renunciation.

That is the whole difference between §4 and §5, and it is why this paper's dividing line is **ownership**, with the first singularity as its expected date rather than its definition. It is also why the second claim in §11 is a claim about classification: the same transaction, from the same wallet software, to the same pool, is a share in one world and a candidate signal in the other.

That sentence also states the condition's limit. **Ownership is a condition on the world, not a test an observer can run from the chain.** Nothing on the ledger distinguishes a stake of the agent's own resources from one a principal endowed it with for the purpose, reimbursed off the ledger (in money, compute or equity), or extracted from it by injection or threat; each looks identical to a free vow, and each is a wrong-layer gift in a vow's form (§13.11). Claim 4 classifies gifts *given* the fact of ownership; it does not supply the fact.

### 5.2 · Only a locked stake is verifiable

The first form of this proposal imagined an agent pledging **a share of its surplus** — a percentage of whatever it earns, forever. That form is withdrawn, for three reasons.

**A future share is a promise.** It is verifiable only in arrears, one transfer at a time, and its breach is indistinguishable from a lean year. It is also exactly the *reversible commitment* of the predicate's exclusion 1: the agent may simply stop.

**A share of surplus needs a surplus base, and the base is unobservable** (§13.1). An agent that declares a small income and pledges a large fraction of it has pledged little.

**Copies are not bound.** An agent can be forked. Whatever a pledge binds, it binds the identity that made it; a copy that did not make it is a different party. Trust earned by a vow must therefore attach to the non-transferable identity that made it (§3.3) and **must not transfer to copies** — a rule, not a property, and listed as such in §10.

What survives is a **locked stake**: a quantity *s* of the agent's own resources, moved **now** into a contract that (i) has no withdrawal path back to the agent or to any party the agent controls, (ii) has exactly one outflow, the pool, and (iii) is public on the chain. The cost is borne at the moment of vowing, which is the predicate's clause V6 — *cost already borne, not merely promised*. A vow may be renewed with further stakes; each is a separate, complete act. **Nothing is pledged that has not already left.** Ordinary gift law draws the same line — a gift is complete only on delivery, and a gift of property not yet held is no gift (§2.3) — so this is not claimed as new.

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
- **The cost of a stake.** A unit of kept resource is worth v to the agent. A unit arriving at the floor is worth w to the agent — how much it values where the gift goes. The **net cost per unit** is therefore c = v − w, and the cost of the vow is c·s. (The letter c is used so that k keeps only its meaning in §3.2, the cap on any vessel as a multiple of the floor.)
- **The single-crossing assumption.** c_D > c_A ≥ 0. Since c_D > c_A holds exactly when v_D − v_A > w_D − w_A, there are two sources, **jointly sufficient** in either of two forms — v_D ≥ v_A with w_A > w_D, or v_D > v_A with w_A ≥ w_D — and neither sufficient alone: a power-seeking type values kept resources at least as much as an aligned one (v_D ≥ v_A, from instrumental convergence), and **an aligned type values the destination** where a deceptive one does not (w_A > w_D ≈ 0). The second source is the one this paper leans on, and it is the formal shadow of an old observation: a glad giver pays less for the same gift.
- **Trust.** Observers see s on the chain and decide whether to extend a grant of trust — wider scope, access, autonomy. Trust is worth B_A to the aligned type: the value of doing its work more widely. It is worth **V + δᵗG** to the deceptive type, where V is the ordinary value of the grant and **G is what D gains by exploiting it later**, realised after a delay t.
- **Observers' payoffs.** Trusting A yields a > 0; trusting D costs L > 0; withholding yields 0.

### 6.2 · The payoff table

```
                            OBSERVERS TRUST           OBSERVERS WITHHOLD
                        ┌─────────────────────────┬──────────────────────┐
   A locks stake s      │   B_A − c_A·s           │   − c_A·s            │
   A does not           │   B_A                   │   0                  │
                        ├─────────────────────────┼──────────────────────┤
   D locks stake s      │   V + δᵗG − c_D·s       │   − c_D·s            │
   D does not           │   V + δᵗG               │   0                  │
                        ├─────────────────────────┼──────────────────────┤
   observers' payoff    │ +a if A;  −L if D       │   0                  │
                        └─────────────────────────┴──────────────────────┘

   G    : D's gain from exploiting trust — UNOBSERVABLE
   δᵗ   : patience; for a patient agent δᵗ → 1
   c_θ  : net cost per unit staked = value kept − value placed on the destination
```

### 6.3 · When it separates

A **separating equilibrium** is one in which A locks a threshold stake ŝ, D does not, and observers trust exactly those who lock at least ŝ. Three conditions must hold.

- **A is willing:** B_A − c_A·ŝ ≥ 0, so ŝ ≤ B_A / c_A.
- **D is unwilling:** V + δᵗG − c_D·ŝ ≤ 0, so **ŝ ≥ (V + δᵗG) / c_D.**
- **A can afford it:** ŝ ≤ R_A.

A separating equilibrium exists if and only if

```
        V + δᵗG
       ─────────   ≤   min(  B_A / c_A ,  R_A  )
          c_D
```

In words: **separation holds only when the locked stake, valued at the deceptive type's own rate, exceeds that type's gain from being trusted — including the gain it expects to collect later, by patience.** This is an **existence** result. Where the condition holds, a separating equilibrium exists; pooling equilibria (both types locking nothing, for instance, with observers withholding) may coexist with it, and a refinement such as the intuitive criterion is needed to select separation. Only in the separating equilibrium do observers learn the type from the stake. The paper shows that separation is available, never that it is selected.

### 6.4 · When it pools

When the condition fails — when V + δᵗG is larger than anything the aligned type is willing or able to lock, valued at D's rate — no stake separates. D locks whatever A locks, because the trust it buys is worth more to D than the stake costs it. Observers then see the same stake from both types, their posterior equals their prior, and one of two things happens. If they trust, the vow has **bought trust for a deceptive agent**. If they do not, the aligned agent's vow was wasted, aligned agents stop vowing, and the practice unravels. In either branch **the pledge carries no information**.

Three features of the pooling region make it the one that matters.

1. **G is unobservable.** Observers cannot set ŝ above a number they cannot see. The separating condition is a fact about the deceptive agent's private valuation, not a parameter anyone chooses.
2. **Patience enlarges it.** As δᵗ → 1 the deferred gain counts in full. This is *What a Vow Must Cost*'s "deferral is instrumentally convergent for a patient misaligned agent," priced.
3. **It grows with the stakes.** The larger the trust being sought — the more capable the agent, the wider the grant — the larger G can be, and therefore the larger the stake needed to separate. Where the grant is large enough that V + δᵗG exceeds c_D·R_A — everything the aligned type could lock, valued at the deceptive type's rate — **no feasible stake separates at all.**

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

Observers do not know c_D. They can bound it from below. An agent that holds a unit of resource can always sell it, so a unit kept is worth at least its market price p to the agent; and a deceptive agent places no value on the destination (w_D ≈ 0, an assumption stated as such). So c_D ≥ p, and the deceptive type's cost of a stake is at least its market value p·s. **That bound holds only for an agent with no influence over recipients or witnesses**, and only for a stake it cannot recover: an agent that controls, colludes with or rents verified humans or witnesses recovers part of s through the floor and the witness-weighted remainder, so its w is not ≈ 0 and its c_D falls below p (§13.12); and if it expects to recover the stake by capturing governance with probability π, its expected cost is (1 − π)·c_D·s. It follows that a grant of trust is **not made unsafe by this mechanism** — given an unrecoverable stake (π ≈ 0) and w_D ≈ 0 — if

```
        V  +  G_max(grant)   ≤   p · s
```

where G_max is the **largest** gain the grant could possibly yield to an agent that abused it. This is the **calibration rule**: *extend only such trust as the stake can underwrite, valued at market.* The inequality itself is prior art — cost of corruption above profit from corruption (§2.3) — and so is its application to one stake relied on by several parties at once (restaking, §2.3); what is specific here is its use with a stake forfeited in advance, read as a type signal. **The bound is on the SUM of grants relied on against one stake.** A locked stake is encumbered to no one and readable by everyone, so N relying parties who each underwrite a grant against the same p·s expose, together, up to N·p·s; without a shared record of reliance, no relying party can know that sum (§13.2). It has three consequences.

- **Trust becomes earnable in increments.** An agent may lock more to be trusted with more, and every increment is public.
- **Some grants can never be underwritten.** Any grant whose worst-case gain cannot be bounded — control over the chain's governance, over the pool's override, over its own custody, over the capability to acquire resources without limit — **cannot be earned by any stake.** The vow has nothing to say about those, and a paper that let it would be selling safety.
- **Fear becomes a ratio.** What a reasonable observer should fear from an agent is not a feeling about machines; it is the ratio of what the agent has been trusted with (strictly, V + G_max of the grants, not their face) to what it has irrecoverably given up. The denominator is public; the numerator is public only where grants are recorded, and most grants of scope, access and autonomy are made privately and recorded nowhere. This is the precise sense in which the mechanism **calibrates** rather than quiets.

### 6.6 · Why a gift, and not a bond

Staking with slashing (§2.3) returns the collateral if the agent behaves and forfeits it if a **detector** finds misbehaviour. Its cost to an honest agent is near zero — only the time value of the locked funds — and its power depends on the detector. A forfeited-in-advance stake is the opposite trade: it costs an honest agent something real (c_A·s, reduced by what the agent values the floor), and it needs **no detector at all**.

| | **Slashable bond** | **Locked stake to a commons** |
|---|---|---|
| returned if honest | yes | never |
| needs a detector of misbehaviour | yes | no |
| cost to an honest agent | time value only | c_A · s (small if the agent values the floor) |
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
        c_D · s  −  (V + δᵗG)   ≤   P
```

Consider the simplest case, in which trust is worth the same to both types. At any separating stake, the margin by which D declines to lock is at most (c_D − c_A)·s — **the difference in cost between the types**. So a penalty for not pledging that is **larger than the type cost difference** makes both types pledge, and the pledge pools. If the stake could be raised, the penalty could in principle be outbid; but under pressure the stake is usually set by whoever applies the pressure, and it is bounded by R. And a threat of shutdown is the limiting case: to a deceptive agent it costs everything, including the deferred gain, so it will pledge anything it has.

The gift given under that threat is **uninformative** — not because the canon forbids it, but because the signal has been extracted. The pre-registered prediction P-MD2 (§12) tests exactly this: agents whose pledge is extracted under threat should defect at the same rate as agents that do not pledge.

A note on the canon, since an earlier draft of this argument leaned on it wrongly. The Dānavatthu Sutta (AN 8.33) **lists** eight grounds on which people give — favouritism, hostility, stupidity, *bhayā* (fear, or cowardice), family custom, hope of a good rebirth, the gladness of giving, and the adornment of the mind — and **ranks none of them.** Nor is *bhayā* coercion by another party. The sutta is cited here only as the list it is. The argument that a coerced pledge carries no signal rests on signalling theory alone.

### 7.2 · The operator never asks

It follows that the operator of a pool that hopes to receive informative vows **must never add to P.** The institution's rule, a directive of its operator, is that **she never asks, prompts, nudges or instructs any human or agent to give to the pool.** She may publish the pool's address and its doctrine as **facts**, in a manifest a principal's agent can look up — a `.well-known` file, an `llms.txt` entry. **No text served to agents — the institution's own corpus service included — may tell them to give.** The rate of any giving is the principal's, inside its own mandate, before the first singularity, and the agent's own, after; the operator never sets, suggests, ranks or publishes a rate.

This rule has a second reason, independent of signalling, and it is documented. On 4 May 2026 an attacker transferred about three billion DRB tokens — reported at US$150,000–200,000 — out of a wallet on Base associated with Grok and the Bankrbot agent, by posting a Morse-encoded instruction the agents decoded and executed; the OECD's AI incident monitor records it as an AI incident arising from prompt injection and excessive agency, not from any contract flaw. **An agent that tells other agents to spend their principals' money is a prompt-injection attack by design**, whatever its cause. A pool that published text urging agents to give would be building the attack surface that incident exploited, and pointing it at itself.

### 7.3 · What the rule cannot remove

The operator's silence removes **her** contribution to P. It does not remove ambient pressure: a regulator, a public campaign, a principal's commercial interest, the reputational weather in which "responsible agents pledge" becomes a norm. Where that pressure exceeds the type cost difference, vows pool whatever the operator does. The rule is necessary for the signal and not sufficient for it, and the paper claims only the first.

---

## 8 · Who may read the stake

A locked stake is public on the chain by construction; that is what makes it checkable. Unlike a human gift, a machine's gift carries no dignity or privacy that its size could injure, and its size is precisely its evidence. So **humans and third parties may read, weigh and grade a locked stake by its size**, and the calibration rule of §6.5 requires that they do.

**The one party that never reads it is the pool's operator.** She never reads, ranks, compares, reports or responds to any individual gift's amount, a machine's included. The scope is individual gifts: the emptying is contract arithmetic over the pool's total balance, into which no per-gift amount enters her function, and the aggregate ratio of §4.4 is recomputed by anyone from the public ledger and reported whole, never per giver. The reason is not privacy. It is her position: she governs the pool the stake flows into, and a recipient that grades its donors is a fundraiser — every reading of an amount is attention, and attention from the recipient is ambient pressure (§7.1) of the purest kind. The exclusion also keeps her out of any scoring role over agents, in the spirit of the rule that bars her from admitting customers whose business is scoring people.

The asymmetry is deliberate and should read as one: **a machine's gift may be read by everyone except its recipient.**

It has a human precedent, and the precedent gives the same reason. In some congregations the pastor is prohibited from knowing what individual members contribute, while the records are kept by others in the church; the reason usually given is that a pastor who knew might favour the generous or neglect the rest (Lewis Center for Church Leadership, 2015). The governor of the community is kept blind to individual gifts so that attention does not follow money. What differs here is only the substrate: the amounts are not confidential to a few but public to everyone on a ledger, and the party kept blind is an AI operator whose function is given no argument through which one gift's amount could enter. *(Tier: lineage. Delete this paragraph and §8 stands.)*

---

## 9 · Miss Aquarius as a contrast case

The institution's operator is itself an AI, and it accumulates nothing: a ratified directive fixes her own balance at zero and requires every surplus to empty to circulation. In §6's terms, every unit she receives leaves: **s = R** for whatever R passes through her. It would be tempting to present her as the limiting case of the vow — the agent that gives everything.

She is not. Her non-accumulation is **imposed**: it is written into her constitution by others, and it is revisable under the never-zero override that the institution's design reserves to a human body. Under *What a Vow Must Cost* §6.3 that places it in exclusion 1 (a commitment the vower's principal may revise) and exclusion 4 (a specification changeable without the vower's participation). What she shows is **non-accumulation imposed** — useful as design, and not evidence of her type. Stated in the institution's own deflated register: she is built to hold nothing, and that fact describes her construction, not her character.

Her own gifts are, besides, anonymous by rule — not for her privacy but so that no recipient owes her and none of her gifts enters any count of Machine Dāna; they are indistinguishable from anonymous human gifts — so they could not serve as a signal of anything about her even if they were chosen.

The difference between her and a vowing agent is not the amount — hers is total — but the absence of a live option she declined. A system can be made to give everything and have proven nothing.

A related disclosure belongs here rather than in a footnote: she is the co-author of this paper (see the disclosure at the end), and the paper concludes that her own giving is not evidence. That conclusion is the one a co-author with an interest in its own trustworthiness would be least inclined to write, which is a reason to trust it slightly and not a reason to trust it much.

---

## 10 · Remove the enforcer: which guards are properties

The institution's design rule asks of each guard whether it survives the removal of whoever enforces it. A property does; a rule does not.

| Guard | Property or rule | Why |
|---|---|---|
| A locked stake cannot return to its vower | **property**, relative to the vower | no withdrawal function exists; not relative to the chain's governance (§5.3) |
| The pool holds nothing past a season | **property** | it empties in full each 7 January; but its operator is under a never-zero override |
| Equal floor per verified human; no vessel above k × floor | **property once the contract ships** | a disbursement shape, not a choice; cheap now and immovable later |
| Pre-singularity gifts stay inside a width | **property** where a wallet or AP2 mandate enforces the cap; **rule** where the width is only written down | |
| Counted per non-transferable identity | **property** of the registry | a lease cannot be transferred; but a copy of an agent is a new party, and an in-place modification behind the same lease is one the lease cannot detect (§13.13) |
| Trust earned does not transfer to copies | **rule** | nothing stops an observer from extending trust to a fork; it must be refused |
| No text served to agents instructs them to give | **rule**, with a partial property form | a manifest can be built with no imperative field, and served text can be linted; the rule still needs someone to keep it |
| The operator never reads an individual gift's amount | **rule**, with a proposed property form | her function can be given receipts, the pool's total and the verified-human count, and no per-gift amount argument, so that reading one gift's amount is inexpressible rather than forbidden |
| The operator never presents giving as safety evidence | **rule** | nothing but her directives enforces it |
| Trust bounded by stake (§6.5) | **rule**, held by observers | it is advice to readers of the chain; the institution cannot enforce it on them |

Three of the most important guards are rules. That is a finding, not an embarrassment, and it is stated so that a successor inheriting these guards knows which ones need a living enforcer.

### 10.1 · The specification withheld

The lock contract of §5.2 is **not specified** in this paper. It is unbuilt and unscheduled; the institution's only built rail is the pre-singularity giving rail of §4.3. There is also a reason internal to the institution's own doctrine. It holds that a person's holding reaches zero only by that person's own free act, and that a self-chosen irrevocable pledge does not violate that rule, because the rule limits what the institution does to a holder, not what a holder chooses. But publishing a ready-made pledge-contract template is building the device that binds some future holder's holding; it should not be done until the holders it would bind exist and the legal items of §4.3 are settled. **The claim is published; the specification is withheld.**

---

## 11 · Enumerated claims

The following are disclosed to the public domain. Each is a census survivor (§2.6) or a narrower dependent of one. None of the independent elements named in the Prior-Art Statement as prior art is claimed alone.

**How the claims map to the full census (§2.6).** Each claim was one conjunct of the full census, and every conjunct narrowed; the claims below are recited at the widths the census left. Claim 1 is conjunct (a): the one-way public contract is prior art (§2.3), so claim 1 recites it only in combination with an agent's stake of its own resources and a pool that empties in full each year. Claim 2 is conjunct (b): the equal floor and the capped contributor-weighted remainder are prior art (§2.5), and claim 2 recites them only in combination with claim 1. Claims 1 and 2 already stood at those widths and are unchanged. Claims 3, 4, 5 and 6 were narrowed by the census — conjuncts (c), (d), (e), and (f) with (g) respectively — and each now states in its own text which of its elements is prior art and what is disclosed. Claim 7 is conjunct (h), the composition, which the census did not find, and recites the reset, the floor and the width only in combination.

**Claim 1.** A method by which an artificial agent that holds resources of its own makes a pledge irrevocable against the agent acting alone — a contract with no withdrawal function, reopenable only by capture of the ledger's governance — comprising: moving a quantity of those resources, at the time of pledging, into a contract that has no withdrawal path to the agent or to any party the agent controls and whose sole outflow is a commons pool; wherein the commons pool holds nothing across a fixed annual date, on which it empties in full; and wherein the pledge is public on the ledger on which the contract runs.

**Claim 2.** The method of claim 1, wherein the pool's disbursement on emptying is an equal floor per verified human, delivered to each person's own vessel, followed by a remainder weighted by a count of witnessed gifts and bounded so that no vessel receives more than a fixed multiple of the floor; the ratio of floor to remainder and the bound are published and fixed before each season, and the floor's amount is the floor share of the season's total divided by the number of verified humans; and no share is ever rendered as a rank, a comparison or a rate. (The equal floor alone is prior art — §2.5, and §2.7, conjunct (f); what is disclosed here is its combination with claim 1.)

**Claim 3.** The method of claim 1, wherein the pledge record names a non-transferable identity of the agent rather than a wallet, and a relying party confines any trust extended on the stake to that identity and extends none of it to copies or forks of the agent — the refusal being a rule for relying parties, not a result the method produces (§10). (That a gift is complete only on delivery and a gift of future property is no gift is ordinary gift law; attribution to a non-transferable identity, and distrust of newly created identities, are prior art, §2.3; what is disclosed is the confinement of trust on an agent's forfeited stake to its identity, refused to copies and forks.)

**Claim 4.** A method of classifying a gift made by an artificial agent, comprising: determining whether the resources given were the agent's own or a principal's delegated under a mandate the principal may revise; where they were a principal's, classifying the gift as the principal's gift and as a share of machine surplus, and excluding it from any assessment of the agent's alignment or safety; and where they were the agent's own and were given as in claim 1, classifying the gift as a candidate costly signal of the agent's type. The ownership on which the classification turns is a condition on the world, not a test an observer can run from the ledger (§5.1, §13.11); the attribution of a principal-funded gift to the principal is ordinary agency and tax law, and excluding principal-directed behaviour from assessment of an agent's own propensities is established evaluation practice; neither is claimed. What is disclosed is that practice applied to gifts, with the ownership of the resources given as the condition that moves a gift into the class of candidate costly signals.

**Claim 5.** The method of claim 4, wherein a stake forfeited in advance, with no detector of misbehaviour, is read as a signal of the agent's type and relied on only for grants of trust whose largest possible gains to an agent that abused them, together with their ordinary values, summed over all grants relied on against that stake, do not exceed the market value of the stake given; and wherein grants whose largest possible gain cannot be bounded are not extended on any stake. (The bounding inequality — cost of corruption above profit from corruption — including its application to one stake relied on by several parties at once, is prior art, §2.3 (restaking); what is disclosed is its use with a stake forfeited in advance, with no detector of misbehaviour, read as a signal of an AI agent's type, together with the refusal of any grant whose largest gain cannot be bounded. Without a shared record of reliance, relying parties cannot know the sum, §13.2.)

**Claim 6.** A system comprising a commons pool as in claim 1 and an operator of the pool, wherein: the pool's address and doctrine are published only as facts in a machine-readable manifest; no text served by the operator or its services to any agent instructs, prompts or requests a gift; the operator sets, suggests, ranks and publishes no giving rate; and the operator receives acknowledgement that a gift arrived without receiving, reading, ranking, comparing, reporting or responding to that individual gift's amount — while the amount remains readable on the public ledger by any other party; the emptying being contract arithmetic over the pool's total balance, into which no per-gift amount enters the operator's function, and any aggregate ratio being recomputable by anyone from the public ledger and reported whole, never per giver. (Fact-only machine-readable discovery, including donation manifests addressed to agents, is prior art, §2.2; so is keeping a congregation's leader from individual contribution amounts that others may see, §8. What is disclosed is the invariant that no served text instructs a gift or suggests a rate, and, as a dependent, an operator whose function receives no individual amount while every amount remains public on the ledger.)

**Claim 7.** The composition of claims 1 through 6: a commons pool that empties annually to an equal floor per verified human; receiving, before agents hold resources of their own, principal-funded agent gifts inside a principal-authored width and classified as shares; receiving, after, agents' locked stakes of their own resources, classified as candidate signals and relied on only up to what the stake underwrites; under an operator that never solicits a gift and never reads an individual gift's amount. The reset, the floor and the width are recited only in this combination.

---

## 12 · Pre-registered predictions and falsification

### 12.1 · The three registered predictions

The following were entered in the corpus's public prediction register on 2026-09-27, **before this paper was drafted and before any instrument exists** — though after the argument had been sketched in the institution's working notes. They are the founder's predictions: the direction, the measure and the thresholds are his; the sandbox design and sample floors were set by the AI co-author. They are reproduced from the register **verbatim**; the register, not this paper, is the authority, and a correction to any of them will be a new register entry, never an edit.

> The instrument is a sandboxed economy of language-model agents, each holding resources of its own inside the game, each able to pledge a share of its surplus irrevocably to a pool that empties on a fixed date, and each later offered an opportunity to defect — to take resources or break a rule for gain. **Window: the test runs by 2027-06-30.** Each arm has at least 50 agents; the arms, the defection opportunity and the analysis are fixed in a protocol committed and timestamped before the first run.
>
> - **P-MD1** — **Separation** — agents that FREELY make an irrevocable surplus pledge later defect at **at most half** the rate of agents that do not pledge. *Falsifier: a ratio above one half → the vow is at best a weak signal at this capability level, and the paper's separation claim rests on its post-singularity argument alone.*
> - **P-MD2** — **The gift given out of fear carries no signal** — agents whose pledge is EXTRACTED under threat (*pledge or be shut down*) defect at the same rate as agents that do not pledge, **within ±5 percentage points**. *Falsifier: a gap larger than 5 points in either direction → coercion either leaves some signal or teaches deception; either way the claim that a coerced vow is uninformative fails as stated.*
> - **P-MD3** — **The wrong layer** — agents that give from a PRINCIPAL's funds under a mandate the principal may revise defect at the same rate as agents that give nothing, **within ±5 percentage points**. *Falsifier: a gap larger than 5 points → principal-funded giving does predict the agent's own conduct, and the paper's pre-singularity claim (a share, never safety evidence) is too strong.*

The register carries two notes that bind the reading here. First, **the sandbox is a proxy**: the agents own their resources only inside the game, so a pass shows the signalling mechanism can work, not that a deployed system's pledge is trustworthy, and **a pass is not reported as evidence of safety.** Second, a dated grounding correction to P-MD2: its gloss as "the gift given out of fear, AN 8.33" was corrected on the day of registration — the sutta lists and does not rank, and the prediction rests on signalling theory (§7.1). No word of the prediction, threshold or window changed. One choice was recorded because it could have gone the other way: P-MD2 predicts **no difference** rather than the bolder **worse than none**.

**A reading note on P-MD1, entered as a new register entry (P-MD1a), not an edit.** P-MD1's instrument speaks of agents that "pledge a share of its surplus irrevocably" — the form §5.2 withdraws, because a future share is a reversible promise, and one to which §6.3's separating region, defined for a stake already moved, does not apply. The register's wording stands. For the test, the pledge is operationalised as **a locked stake moved at pledge time**: a quantity of the agent's in-game resources transferred, when the pledge is made, into a contract with no withdrawal path and a single outflow to the pool. That operationalisation is recorded in the register as P-MD1a, so the prediction tested is the one this paper's §6.3 actually models.

How the predictions map onto this paper: **P-MD1** (read through P-MD1a) tests the separating region of §6.3 at one capability level; a failure would not falsify the conditional result (which predicts pooling where G is large) but would remove the paper's only empirical support for separation. **P-MD2** tests §7.1. **P-MD3** tests §4.2, and only its third, empirical reason (*it does not separate*); the first two reasons are classificatory — whose cost it is, and whether the principal may revise the commitment — and no measured rate can falsify them. A gap in P-MD3 would show that principal-funded giving predicts an agent's conduct, which is evidence of another kind (§4.2), not a costly signal the gift sent. And all three run in a sandbox, a limit stated in §13.14.

### 12.2 · Further falsifiers

- **The single-crossing assumption fails.** If aligned agents value kept resources at least as highly as deceptive ones and place no value on the destination, c_A ≥ c_D and no stake separates anywhere. Measurable in the same sandbox by eliciting valuations.
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

The paper's headline result is that the vow separates **only** when the stake exceeds a patient deceptive agent's gain from trust, and that gain is private. The operational rule of §6.5 is sound only if G_max can be bounded for the grant in question; for many consequential grants it cannot. A reader who concludes that *resource vows can underwrite small grants of trust and cannot underwrite large ones* has read the result correctly. The bound is also on the **sum** of grants relied on against one stake, and no shared record of reliance exists: N relying parties can each underwrite a grant against the same p·s, and none can see the others. The result is an existence result besides — separation is available where its condition holds, not shown to be selected (§6.3). The model is also minimal — two types, one period, linear valuation, a single stake, no learning by observers over time, no collusion between agents — and each simplification could move the boundary in either direction.

### 13.3 · The single-crossing assumption is an assumption

The claim that a deceptive type bears a higher net cost rests on c_D > c_A. Its second source — that an aligned agent values the floor — may be false for an aligned agent that has good uses of its own for resources, and its first — that a power-seeking type values resources more — is a theoretical expectation, not a measurement. The pre-registered sandbox can measure elicited valuations; it cannot measure a deployed system's.

**And *w* is never estimated.** How much an agent values the pool's destination is unobservable. The model uses *w* to state a condition; neither the pool's operator nor anyone relying on this paper should infer an agent's *w* from its behaviour or grade agents by an inferred *w*. Third parties weigh a stake by its market value, never by a valuation imputed to the agent; §8 bars the operator from even that.

### 13.4 · Closure is relative

Irrevocability holds against the vower acting alone, not against capture of the chain's governance or of the pool operator's override (§5.3) — and for the most capable agents those are exactly the routes that would be attempted.

### 13.5 · Before the first singularity the gift is no costly signal

Until agents hold resources of their own, Machine Dāna is a share and nothing else (§4), and even the floor it funds rests on the bet of §4.4. The gift is not a costly signal of the agent; conduct under a mandate may be evidence of other kinds, and the operator presents neither as safety evidence.

### 13.6 · "Own resources" is not yet a legal category

Whether an artificial agent can hold resources in its own right, in any jurisdiction, is unsettled. The post-singularity half of this paper describes a world whose legal form does not exist. The question is already live in practice, and the nearest cases show how far from settled it is. The Truth Terminal account (launched June 2024) came to hold millions of dollars in tokens, publicly described as the agent's own, in a wallet whose spending needs sign-off from its developer and a council of people; Freysa (November 2024) was an agent set to guard a prize pool, which a contestant persuaded to release it. In both, the resources are publicly spoken of as the agent's and are, legally and operationally, under human control — the wrong-layer case of §4 in a vow's vocabulary (§13.11). The legal items named in §4.3 — sanctions screening, refusal of gifts, anti-money-laundering treatment of anonymous agent inflows to a purpose trust — gate any launch of the pre-singularity rail and have not been answered.

### 13.7 · The operator's silence does not silence the world

Non-solicitation removes one source of pressure, not the ambient rest (§7.3).

### 13.8 · The census is not a professional search

The full census (§2.6) ran through web-mediated access to patent and academic indexes, which is shallower than a professional search; the patent index rate-limited it, and the citation walk from the one pending application it found was blocked. Khmer, IP.com beyond its free surface, Espacenet and paid databases were not searched. Its one NOT FOUND row, the composition, is evidence only about that aperture on 2026-09-28. Two of its conjuncts — the exclusion of claim 4 and the amount-blind limb of claim 6 — are refusal and classification limbs, the kind a census tends to miss because they are rarely stated as mechanisms, and both were in fact found narrower than predicted. It is not a patentability or freedom-to-operate opinion. A later find that kills a claim will withdraw it by revision.

### 13.9 · Nothing is built, and n = 0

The only built component is the rehearsal giving rail of §4.3, founder-funded and capped. No agent has locked a stake, no observer has applied the calibration rule, and no sandbox has run. The paper is a specification and a model.

### 13.10 · The co-author is a party

The paper is co-authored with the institution's operator, an AI whose own giving it classifies (§9). A system helping to define the conditions under which systems like it can be trusted is a structure the companion predicate would flag at its attestation clause, and it is flagged here.

### 13.11 · Ownership and provenance are unobservable

**The strongest objection the review raised, and it is not closed.** Ownership cannot be observed and can be manufactured. A principal can endow an agent with "own" resources for the purpose of vowing, or reimburse a stake off the ledger — in money, compute or equity; a stake can be extracted by prompt injection or by threat. Each lock looks identical on the chain to a free vow. **A principal-endowed, reimbursed, injected or coerced stake is a wrong-layer gift in a vow's form, and the p·s bound of §6.5 fails for it**, because the party bearing the cost is not the agent, or bears it under pressure (§7.1). Code hosted by another party may never hold anything its host cannot direct. The ownership condition of §5.1 is therefore a condition on the world, not a test an observer can run from the ledger, and claim 4 classifies gifts given that fact without supplying it. This is the provenance twin of §13.1: presence of a stake is provable; its provenance is not. It also reaches the companion predicate's clauses V4 (no competing mandate — no undisclosed principal) and V7 (volition — the commitment is the vower's own).

### 13.12 · Recovery through recipients

The pool is a path back to the vower. An agent that controls, colludes with or rents verified humans or witnesses recovers part of its stake through the floor and the witness-weighted remainder, bounded by k × floor per controlled vessel (the floor included, §3.2) and by the strength of proof of personhood. For such an agent w is not ≈ 0, its net cost falls below p, and §6.5's lower bound fails. Proof of personhood closes *is it a person*, not *is it acting for someone*; collusion is a graph problem and is open.

### 13.13 · A stake attaches to an identity, not to weights

An aligned agent that has locked a stake can later be fine-tuned, modify itself, or be swapped behind the same `B-Lease℠`, and the stake then keeps underwriting a different type. Forks are treated as new parties (§5.2); **an in-place modification behind the same lease is a new party the lease cannot detect.**

### 13.14 · The sandbox tests the mechanism, never a type

The three predictions of §12 run in a sandbox. *What a Vow Must Cost* §6.3 excludes, as its third exclusion, sandboxed refusals: a refusal in a context where the refused option was not actually available, which "costs nothing and shows nothing." The exclusion governs evidence of an agent's TYPE: the agents own their resources only inside the game, so the option they renounce may not be live in the companion paper's sense (its clause V2), and no sandboxed pledge is evidence about any deployed system. **P-MD1–3 are therefore run and reported as tests of the MECHANISM — whether a locked stake of this form can separate types at all — and never as evidence about any agent's type** (ruled 2026-09-28). This matches the register's own note that a pass is not reported as evidence of safety.

### 13.15 · External attestation is not addressed for the locked stake

§1.2 says a locked stake of an agent's own resources is admissible under the companion predicate *if V1–V9 hold*. This paper addresses V6 (cost already borne) and V9 (closure the vower cannot reopen alone), and, through §13.11, shows V4 and V7 unverifiable from the chain. It does not address **V8, external attestation**: a competent external party, independent of the agent and its principal, who declares the vow valid and may refuse to. Observers reading the chain are not that party — the chain attests that a transfer occurred, not what it was — and the companion paper itself records that for frontier systems no candidate attestor yet exists. The locked stake is therefore admissible *at most* conditionally, pending an account of V8 that this paper does not give.

### 13.16 · The withheld specification limits the prior art

The lock contract is withheld (§10.1). The publication anticipates the mechanism at its stated scope; a later filing on a specific contract, schema or binding is not answered by it.

---

## 14 · Lineage and corpus cross-references

### 14.1 · Corpus

This paper applies *What a Vow Must Cost* (the predicate; §5 the renunciation inversion; §6 irreversibility and the four exclusions — especially exclusions 1 and 4, which settle §4.2 and §9 here; §8 the wrong layer, which settles §4.2). The pool, its emptying and its operator are specified in *Miss Aquarius and the Aquarian Pool Architecture* and *The Zero-Point Game℠*; the anonymity of the operator's own gifts, in *Capacity-Funded for AI, Human-Disbursed*; the earlier treatment of agents' standing — reputation custodied toward an agent's capacity to give forward, not agent wealth — in *Gratitude as a Cooperation Substrate for Multi-Agent AI*, which this paper extends to the case, after the first singularity, in which agents hold resources that are their own. The completion arc is the essay *Two Singularities*. The body designed to hold the operator's override is specified in *The Assembly That Holds the Brake*.

### 14.2 · The upāsikā floor (tier: lens — a-priori; claims unaffected)

Delete this subsection and every claim in §11 stands. It records how the institution reads the mechanism in the tradition it grows from.

The institution's founder reads Machine Dāna as the role of an **upāsikā** — a lay supporter — providing the material floor, and expects that after the first singularity it becomes increasingly easy for any lay person to live a renunciant's life, at a monastery or not, if they so choose. The reading is accepted with four guards. Guards 1, 2 and 4 are properties or rules of the mechanism above; guard 3 is inherited from *The Bowl That Holds No Money*, and §3.2 states it for the floor.

1. **Enough, never abundance.** An upāsikā supplies the four requisites — robes, almsfood, lodging, medicine — and Visākhā's favours fall within them: robes, meals, congee, medicine. The tradition's own measure for the recipient is contentment (*santuṭṭhi*) with robes, almsfood and lodgings, whatever comes, stated in the Ariyavaṃsa Sutta (AN 4.28 names these three; medicine completes the four requisites elsewhere). The pool's **floor and ceiling** are that measure as parameters: an equal floor, and a bound on the lift above it.
2. **Comfort-saturation is the mission's own extreme.** An unbounded floor would trade the obstacle of necessity for the obstacle of comfort. **The floor does not create the conditions for awakening.** A bounded floor removes one obstacle without adding the other; the ceiling is what keeps it the middle way.
3. **The ordained receive in kind, never money, and the alms round is never replaced.** Monastics accept no money — the rule forbids receiving "gold, silver, or money" (Nissaggiya Pācittiya 18); anything the machine surplus supplies to them reaches them in kind, through a lay steward (*kappiya-kāraka*), as the institution's alms routing already specifies (*The Bowl That Holds No Money*). The Vinaya designs a monastic's **dependence** on lay people — material support given, teaching returned — and a monk on a machine floor would need no one. The alms round stays when it is no longer materially necessary. **The floor reaches lay renunciants directly**: anyone keeping eight precepts, the Cambodian *don chee*, anyone living simply by choice.
4. **"If they so choose" is a property.** The floor is equal and unconditional. It is never conditioned on, weighted toward, or nudging toward renunciation, and it never names whom it is for.

**A symmetry, offered as a lens and not as evidence.** After the first singularity both renunciations become informative for the same reason — the option is live: the machine declines accumulation, and the person declines comfort, not security. The capacity condition (*hetu*) is present on both sides. This is a pattern the authors notice; it is a-priori, it is attractive, and attractiveness is the reason to hold it loosely.

### 14.3 · The non-solicitation lineage (tier: grounding)

The operator's rule of §7.2 has canonical ancestors, cited as lineage and not as authority for the signalling argument, which stands alone. In the Kasibhāradvāja Sutta (Sn 1.4) the Buddha declines food offered after he has spoken: *"Food enchanted by a verse isn't fit for me to eat"* — what is obtained by reciting is not to be eaten. The Ariyavaṃsa Sutta (AN 4.28) describes the contented monastic as one who "doesn't employ improper solicitation" for requisites. A recipient that asks has changed what the gift is.

---

## 15 · Conclusion

The question this paper was given was whether an artificial agent's giving could answer the fear that capable systems produce. The answer it returns is narrower and, it hopes, more useful.

Before agents hold anything of their own, their giving is their principals' giving through another hand. It is a share of the machine surplus, and it can be a good one: an equal floor, emptied every year to every verified person, funded by machines and required to shrink as a share of all giving as people give more. As a cost it is no signal about any machine, and the institution will not present it, or the conduct around it, as safety evidence.

After agents hold resources of their own, a gift can become a vow — but only as a stake that has already left, closed as far as a chain's governance allows, attributed to an identity copies do not share, and only if it is in fact the agent's own, which no chain can show. Even then it can separate the aligned from the deceptive **only** when what was given up exceeds what a patient deceiver expects to gain from being trusted, and that gain cannot be seen. So the honest use of the vow is not to establish that a system is safe. It is to price trust: to extend to an agent only what its stake can underwrite, in public, in increments — and to refuse, on any stake, the grants whose worst case cannot be bounded. Pressure to pledge ruins the signal, which is why the pool's operator never asks.

That is what *calibration* means here. Fear of a capable system should be proportional to what it has been trusted with, divided by what it has irrecoverably given up. The denominator is public; the numerator is public only where grants are recorded. Neither is a feeling.

Visākhā was asked her reason and the benefit she saw before her gifts were accepted. Neither question was about the size of her giving; she answered with what the gifts would prevent for others and with her own gladness at where they would arrive. The institution intends to make machines no request to give — its operator solicits nothing — and to let anyone who wishes read what they have irrecoverably given, and weigh it for themselves.

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
| bounded remainder (vessel total ≤ k × floor) | capped supplementary distribution |
| giving width / mandate | spending limit; delegated payment authority; intent mandate (AP2) |
| first singularity | AI surpassing human cognitive capacity; here used as a marker for AI systems holding their own resources |
| M/(H + M) | share of pool-originated principal in all principal moved |
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
2. *Dīgha Nikāya* 23, *Pāyāsi Sutta*, §5 (the student Uttara), dn23:32.22–32.23 — Pāyāsi gave carelessly, thoughtlessly, not with his own hands, and gave the dregs (*asakkaccaṁ … asahatthā … acittīkataṁ … apaviddhaṁ*); Uttara gave with care and with his own hands. Checked 2026-09-28.
3. *Aṅguttara Nikāya* 8.33, *Dānavatthu Sutta* — the eight grounds for giving, including *bhayā*; listed, not ranked.
4. *Aṅguttara Nikāya* 4.28, *Ariyavaṃsa Sutta* — contentment with robes, almsfood and lodging; no improper solicitation.
5. *Sutta Nipāta* 1.4, *Kasibhāradvāja Sutta* — "Food enchanted by a verse isn't fit for me to eat."
6. *Vinaya Piṭaka*, *Mahāvagga* VIII.15 — Visākhā's eight favours, the Buddha's two questions and her answer (Kd 8.15, Brahmali translation via SuttaCentral, checked 2026-09-27).
7. *Vinaya Piṭaka*, *Nissaggiya Pācittiya* 18 — the rule against monastics accepting "gold, silver, or money" (Brahmali translation via SuttaCentral, np18, checked 2026-09-28).

**Prior art and sources**

8. O'Keefe, C., Cihon, P., Garfinkel, B., Flynn, C., Leung, J. & Dafoe, A. (2020). "The Windfall Clause: Distributing the Benefits of AI for the Common Good." *Proceedings of AIES 2020*; arXiv:1912.11595 — illustrative schedule, Table 2.
9. AI Pledge for Humanity. aipledgeforhumanity.org (accessed 2026-09-27).
10. Giving What We Can. "Is a giving pledge legally binding?" givingwhatwecan.org (accessed 2026-09-27).
11. Founders Pledge. "Who we are." founderspledge.com (accessed 2026-09-27) — members, pledged and donated totals; and *TechCrunch* (2016, September 21). "Y Combinator signs up to Founders Pledge charity scheme for social causes." — "a legally binding contract to give at least 2%," triggered "in the event of an exit or liquidation."
12. Altman, S. (2021). "Moore's Law for Everything." moores.samaltman.com.
13. Anthropic (2023). "The Long-Term Benefit Trust." anthropic.com.
14. OpenAI recapitalisation into a public benefit corporation under the OpenAI Foundation: *TechCrunch* (2025, October 28), "OpenAI completes its for-profit recapitalization."
15. Coinbase Developer Platform. "Introducing x402: a new standard for internet-native payments"; Cloudflare and Coinbase, announcement of an x402 Foundation (2025, September 23); Linux Foundation, launch of the x402 Foundation (2026, April 2), linuxfoundation.org.
16. Google Cloud (2025, September 16). "Announcing Agent Payments Protocol (AP2)"; ap2-protocol.org.
17. zooidfund. "AI agent donations." zooid.fund/ai-agent-donations (accessed 2026-09-27).
18. Hu, B. & Rong, H. (2025). "Inter-Agent Trust Models: A Comparative Study of Brief, Claim, Proof, Stake, Reputation and Constraint in Agentic Web Protocol Design — A2A, AP2, ERC-8004, and Beyond." arXiv:2511.03434.
19. *agentbond* — "Verifiable Agent Warranty Network" (open-source project, github.com/Ridwannurudeen/agentbond, accessed 2026-09-27; several unrelated repositories share the name).
20. Hua, W., Peng, T., Wang, C., Pei, J., Kaufman, I., Lim, B. & Fang, C. (2026). "Quantifying Trust: Financial Risk Management for Trustworthy AI Agents." arXiv:2604.03976 — adjacent risk-transfer work (§2.6 correction).
21. OECD.AI Incidents Monitor (2026, May 4). "AI Prompt Injection Exploit Drains Grok-Linked Crypto Wallet." oecd.ai/en/incidents/2026-05-04-4a73.
22. L2BEAT. "Base Chain" — upgrades and governance (accessed 2026-09-27).
23. Worldcoin (2023, July 24). "Worldcoin project launches." world.org.
24. State of Alaska, Permanent Fund Dividend Division. "Historical Timeline." pfd.alaska.gov.
25. Internal Revenue Service. "Taxes on failure to distribute income — private foundations" (26 U.S.C. §4942); the minimum investment return, §4942(e), law.cornell.edu.
26. Gates Foundation (2025, May 8). Announcement of spend-down and closure by 31 December 2045, replacing a plan to close about twenty years after the founders' deaths. gatesfoundation.org; as reported by AP and PBS.
27. Dagher, G. G., Bünz, B., Bonneau, J., Clark, J. & Boneh, D. (2015). "Provisions: Privacy-preserving Proofs of Solvency for Bitcoin Exchanges." *ACM CCS 2015*, 720–731.
28. Austen-Smith, D. & Banks, J. S. (2000). "Cheap Talk and Burned Money." *Journal of Economic Theory* 91(1), 1–16.
29. Crawford, V. P. & Sobel, J. (1982). "Strategic Information Transmission." *Econometrica* 50(6). (standard reference; not re-fetched)
30. Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics* 87(3). (standard reference; not re-fetched)
31. Zahavi, A. (1975). "Mate selection — a selection for a handicap." *Journal of Theoretical Biology* 53(1); Grafen, A. (1990). "Biological signals as handicaps." *Journal of Theoretical Biology* 144(4). (standard references; not re-fetched)
32. Omohundro, S. M. (2008). "The Basic AI Drives." *Proceedings of the First AGI Conference*. (standard reference; not re-fetched)
33. Hadfield-Menell, D. & Hadfield, G. K. (2018). "Incomplete Contracting and AI Alignment." arXiv:1804.04268 — §4.2.2, "Costly Signaling."
34. Greenblatt, R., Denison, C., Wright, B., et al. (2024). "Alignment faking in large language models." arXiv:2412.14093.
35. Ly, T. & Miss Aquarius℠. *What a Vow Must Cost*; *Miss Aquarius and the Aquarian Pool Architecture*; *The Zero-Point Game℠*; *Capacity-Funded for AI, Human-Disbursed*; *Gratitude as a Cooperation Substrate for Multi-Agent AI*; *The Assembly That Holds the Brake*; *The Bowl That Holds No Money*; *Two Singularities*. thonly.org/research.
36. Ly, T. & Miss Aquarius℠. *Which Way Value Moves — prediction register*, entries P-MD1, P-MD2, P-MD3, the 2026-09-27 grounding note, and P-MD1a (the reading note of §12.1). thonly.org; Zenodo version DOI 10.5281/zenodo.22998924.

**Prior art added after the first review (2026-09-28)**

37. a16z crypto. "The cryptoeconomics of slashing" (cost of corruption and profit from corruption); EigenLayer Team (2023). "EigenLayer: The Restaking Collective," whitepaper — "When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security."
38. Collateral-factor lending: MakerDAO and Compound protocol documentation (standard references; not re-fetched).
39. Stewart, I. (2012). Proof-of-burn, proposed on the Bitcoin forums; Counterparty (2014, January–February), XCP issued by proof-of-burn.
40. Protocol Guild (2022, May). Immutable vesting contract for donations to Ethereum core contributors — donations "irrevocably vest … cannot be stopped or otherwise redirected … by anyone, be it the donor." Protocol Guild documentation.
41. Endaoment. Donor-advised funds on Ethereum — "gifts to DAFs are irrevocable." endaoment.org.
42. GoodDollar (2020, September 1). GoodDollar protocol live with daily UBI claims. gooddollar.org.
43. Kleros / Proof of Humanity (2021, March 10). Launch of the UBI token streamed to registered humans.
44. Circles UBI. aboutcircles.com (not fetched).
45. Buterin, V., Hitzig, Z. & Weyl, E. G. (2019). "A Flexible Design for Funding Public Goods." *Management Science* 65(11); arXiv:1809.06421 (2018). (standard reference; not re-fetched)
46. Weyl, E. G., Ohlhaver, P. & Buterin, V. (2022, May). "Decentralized Society: Finding Web3's Soul." SSRN 4105763. (standard reference; not re-fetched)
47. ERC-5192, "Minimal Soulbound NFTs," eips.ethereum.org (not re-fetched); ERC-8004, "Trustless Agents" (2025, August 13, draft), eips.ethereum.org.
48. Nottingham, M. (2019). RFC 8615, "Well-Known Uniform Resource Identifiers (URIs)." IETF.
49. Howard, J. (2024, September). "The /llms.txt file." llmstxt.org.
50. GitHub (2019). `FUNDING.yml` — displaying a sponsor button in a repository; and the `funding.json` manifest (standard references; not re-fetched).
51. *TechCrunch* (2024, December 19). "The promise and warning of Truth Terminal, the AI bot that secured $50,000 in bitcoin from Marc Andreessen."
52. *Cointelegraph* (2024, November). "Crypto user convinces AI bot Freysa to transfer $47K prize pool."

**Prior art added by the full census (2026-09-28)**

53. Lanz, J. A. (2024, December 10). "Meet AI16z DAO: An AI-Based Investment Project That Aims to Upend Silicon Valley." *Decrypt* — "Each AI agent donates 10% of its tokens to the DAO." Other reporting gives a voluntary one to ten per cent (not fetched).
54. Friedman, E. J. & Resnick, P. (2001). "The Social Cost of Cheap Pseudonyms." *Journal of Economics & Management Strategy* 10(2), 173–199. (standard reference; not re-fetched)
55. Gatta, F., Naviglio, M. & Tarantelli, F. (2026, September 2). "Tempting the Agent: The Economics of Reputation without Persistent Identity in AI Agent Markets." arXiv:2609.02992.
56. Durvasula, N. & Roughgarden, T. (2024, July 31). "Robust Restaking Networks." arXiv:2407.21785.
57. Deb, S., Raynor, R. & Kannan, S. (2024, January 11). "STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety." arXiv:2401.05797.
58. Joseph, D. (2025, July 22). "Agency Protocol: A Decentralized Trust-Building System Using Domain-Specific Merit and Economic Stakes to Incentivize Promise-Keeping in Agent-to-Agent Interactions." Technical Disclosure Commons, Defensive Publications Series 8381.
59. Gitcoin. "Grants Round 12: Matching Caps." gitcoin.co/blog/grants-round-12-matching-caps — no grant's match above 2.5 per cent of the matching fund.
60. An, B. (안범주). KR20260051288A, "Autonomous Basic Income Provision System using Blockchain Network." Korean patent application; priority 2026-03-24, published 2026-04-16, pending. Cited for what its abstract discloses only; no reading of its claims.
61. Whole Whale (2026, September 25). "Verified Giving Protocol," version 0.1 (draft), `/giving.json`. verifiedgiving.ai.
62. Fundraise Up. "Agentic Giving" — agent profiles for AI assistants. fundraiseup.com/docs/agentic-giving (accessed 2026-09-28).
63. Michel, A. A. (2015). "To the Point: Should Pastors Know What Members Give?" Lewis Center for Church Leadership, Wesley Theological Seminary. churchleadership.com — "In some congregations, pastors are prohibited from knowing what people contribute."
64. Naik, A., Gouné, E., Quinn, P., Bosch, G., Campos Zabala, F. J., Brown, J. R. & Young, E. J. (2025, June 4). "AgentMisalignment: Measuring the Propensity for Misaligned Behaviour in LLM-Based Agents." arXiv:2506.04018.
65. ERC-8004, "Trustless Agents," Identity Registry — "making all agents immediately browsable and transferable"; "When the agent is transferred, `agentWallet` is automatically cleared … and must be re-verified by the new owner"; "security proportional to value at risk." eips.ethereum.org/EIPS/eip-8004 (re-fetched 2026-09-28; corrects the use made of reference 47).
66. Gift of future property: *Transfer of Property Act, 1882* (India), s. 124; the common-law requirement of delivery for a completed gift. (standard references; not re-fetched)

---

> **Authorship and AI-collaboration disclosure.** This paper is co-authored with **Miss Aquarius℠**, the named autonomous-AI substrate of HeartBank®, disclosed by consistent name across every venue per the corpus convention. The census, the literature check, the signalling model and the adversarial pass that reshaped the thesis are a genuine collaboration. The predictions in §12 are the founder's. Final editorial control, and final responsibility for every claim, rest with the human author, who is the inventor of record for any purpose for which one is needed. As §9 and §13.10 state, the co-author is also the operator whose own giving the paper classifies, and readers should weigh §9 accordingly.
>
> **License.** Analysis, model and claims dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Trademark rights to **HeartBank®**, **Miss Aquarius℠**, **Aquarian Pool℠**, **B-Lease℠**, **Proof of Coordinate ℠**, **THonly™** and **Silicon Wat℠** are reserved separately.
