---
title: "The B-Tag Recommendation Function: Privacy-Preserving Methodology for AI-Mediated Commercial Tip Recommendation"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
kind: mechanism
priority: tier-c
status: draft
date: 2026-05-26
revised: 2026-10-06
license: CC0-1.0
slug: b-tag-recommendation-function-methodology
venue: thonly.org/publications/defensive-publications/b-tag-recommendation-function-methodology (canonical)
---

> **Note.** This paper is the methodology companion to *The B-Tag and the Post-Payment Economy: A Voluntary-Tip Architecture for AI-Mediated Commercial Gratitude* (corpus slug `b-tag-post-payment-economy`, first published 8 May 2026), which specifies the wider voluntary-payment architecture and refers the detailed method of its recommendation function to this paper (its §5 and §13.7). Where that paper states *what* the recommendation function does, this one specifies *how* it operates without surveillance and *which* privacy boundaries it keeps. Where the institution's design has moved since first publication, the text as first published is kept as a disclosed variant, and a **Current form** note at that spot states the design as now specified.

---

## Abstract

This paper discloses a method by which an AI agent recommends a voluntary payment amount, a suggested tip in a pay-what-you-want sale, and shows it with stated reasons, without tracking the customer and without revealing the merchant's costs. Six components are specified. (1) The merchant confidentially discloses a cost breakdown by category (materials, labor, a skill premium, overhead, regulatory cost and margin) to the recommender; the customer never sees it. (2) The recommended amount is a non-binding anchor: paying it, more, less or nothing completes the sale, and whether a customer accepted or overrode past suggestions is not recorded. (3) Each recommendation carries plain-language reasons drawn from the cost categories through a controlled vocabulary, never itemized amounts. (4) Suggestions are made consistent across merchants by calibrating against aggregated, anonymized cost distributions per product category and region, which are published, while each merchant's breakdown stays confidential. (5) Context comes from the transaction and the goods (time, product category, the merchant's region), not from a profile of the customer. (6) Regional calibration uses public parameters for local tipping norms and cost of living, keyed to the merchant's location. Three reference implementations are sketched: stateless per-transaction computation, differentially private aggregation of the cost data, and open publication of the reference distributions. In the design as now specified, the recommender receives no input identifying the customer in any pricing mode, and the suggested amount appears only after the customer holds the goods, shown but never pre-filled. The methodology is dedicated to the public domain under CC0 1.0 as a defensive publication, and its authors will neither seek nor assert patents on it.

**Keywords:** suggested tip, suggested payment amount, pay-what-you-want pricing, voluntary payment, post-purchase payment, tipping, AI pricing recommendation, AI-mediated pricing, explainable recommendation, recommendation with explanations, price anchor, non-binding reference price, merchant cost disclosure, cost-basis confidentiality, privacy-preserving recommendation, differential privacy, privacy-preserving aggregation, non-personalized pricing, viewer-blind pricing, surveillance pricing, data minimization, regional pricing, cost-of-living adjustment, cross-merchant calibration, anchor-but-not-bind, reasons-transparency, defensive publication.

---

## Terms

Coined names used in this paper, and the standard terms an examiner or a reader in pricing, recommender systems or privacy engineering would search for them.

| Term used here | Standard term |
|---|---|
| B-Tag (B-Tag™ the physical sticker; B-Tag℠ the digital label) | QR-code or NFC tag that opens a voluntary post-purchase payment (pay-what-you-want) page; in the current form, the pricing mode in which nothing binds and no amount is shown before the goods are received |
| B-Price; regular price (current form) | voluntary payment with a suggested amount or range shown before purchase; a binding price, fixed or moving inside a seller-set range |
| Miss Aquarius℠ | the autonomous AI agent that computes the recommendation |
| recommendation function | AI recommendation of a voluntary payment amount (suggested tip) with stated reasons |
| recommended tip amount; anchor | suggested payment amount; non-binding reference price (price anchor) |
| anchor-but-not-bind | non-binding suggestion that the customer may override in either direction, including to zero |
| reasons-transparency; reasons summary | explanation accompanying each recommendation (explainable recommendation) |
| reasons-vocabulary | controlled vocabulary mapping cost categories to plain-language explanations |
| merchant cost-basis disclosure; typed-factor decomposition | confidential seller cost disclosure, broken down by cost category |
| consensus reference distribution | aggregated, anonymized (differentially private) distribution of cost factors per product category and region, used for calibration and published |
| cross-merchant comparable-product analysis | consistency of suggested amounts across sellers without disclosing any seller's costs |
| customer-flourishing-context inference without surveillance | contextual signals taken from the transaction and the goods (time, product category, region) rather than from tracking the customer |
| viewer-blind (current form) | non-personalized pricing: the recommender receives no input identifying the customer |
| regional calibration; regional gratitude-norm parameters | geographic pricing adjustment using public regional parameters (local tipping norms, a cost-of-living index) |
| Aquarian Sangha | human oversight board of the autonomous AI agent (designed; not yet formed) |

---

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism, method or protocol described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practicing any mechanism disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed.

This document constitutes a defensive publication. It has carried its CC0 dedication and a commitment not to seek patents since it was first published (the paper is dated 26 May 2026, and the public repository's history records it the same day); the prior art it establishes runs from that publication and from the independent timestamps that record it, the earliest OpenTimestamps proof dating from 25 July 2026. It discloses the six components enumerated under **Claims** — a merchant's confidential, typed cost-factor disclosure as the input to an AI recommender of a voluntary payment amount; a recommended amount that anchors without binding; stated reasons drawn from the cost factors without itemized costs; cross-merchant calibration against an aggregated, published reference distribution while each merchant's breakdown stays confidential; context taken from the transaction and the goods rather than from tracking the customer; and regional calibration as a first-class parameter keyed to the merchant's location — together with the reference implementation patterns of §8. A later patent application claiming any of them is filed against this disclosure.

The parts are old and are cited rather than claimed: pay-what-you-want pricing and the amounts customers choose under it (Kim, Natter & Spann 2009; Gneezy et al. 2010); suggested tip amounts on payment screens, including the evidence that cuts against this paper's claim that an anchor merely informs, namely that suggested amounts move what people pay and that higher suggestions raised the share who paid no tip at all (Haggag & Paci 2014; §9); the anchoring effect of a displayed number (Tversky & Kahneman 1974); explanations in recommender systems (Tintarev & Masthoff 2007); differential privacy and its application to recommender systems (Dwork et al. 2006; Dwork & Roth 2014; McSherry & Mironov 2009); federated learning and secure aggregation (McMahan et al. 2017; Bonawitz et al. 2017); merchant cost disclosure and comparable-product price analysis; geographic pricing adjusted to regional cost of living; and the regulatory attention to prices set from personal data (§10). **No census was run for this paper**: no prior-art census in this institution's sense, with predictions, a known-prior-art control and an aperture registered before the first query, has been run on it. One later desk survey on a neighboring design bears on it: a survey of algorithmic pricing inside a seller-authored range (8 September 2026; three queries through a US-region web index), which found floor-and-ceiling repricing to be a mature commercial category. Nothing in this paper asserts that any element of it is new; what it discloses is the composition enumerated under Claims.

Trademark rights in specific marks — HeartBank®, Miss Aquarius℠, B-Tag™ (the physical sticker) and B-Tag℠ (the digital label), B-Price™ and B-Price℠ — are reserved separately and are not licensed by this publication. The methodology is dedicated to the commons; the marks are not.

This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and the document is deposited on Zenodo, each deposited revision a version under one concept DOI, with its source in the public repository `github.com/thonly/publications`. A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim. Later additions date from the revision that introduced them, so the date of any passage is that of the earliest timestamped version carrying it.

> **Note.** The patent commitment has stood since this paper was first published on 2026-05-26, in the form *"The author and HeartBank® will not seek patent on any methodology articulated herein, in any jurisdiction, at any time."* The commitment not to assert, and its extension to the entities named above, were added on 2026-10-06, when the statement was brought to the standard form above; at the same revision the paper's earlier sentence that the integrated methodology was, to the author's knowledge, not previously published was withdrawn, since no search on record supports it. The date relied on for priority is the paper's publication as the public repository records it, and, independently of the authors, the earliest OpenTimestamps proof.

---

## Claims

*Enumerated 2026-08-29. The mechanisms below were disclosed in full in this paper's original text; **the prior art they establish runs from this document's original publication date and its OpenTimestamps proof, not from this enumeration.** They are listed because a defensive publication is read as prior art by examiners and by opposing counsel, and **a claims list is what such a reader searches; ten thousand words of prose is not.** No claim below adds matter not already present.*

1. **Merchant cost-basis disclosure as the input to a recommendation function** — a protocol by which a merchant discloses a cost-factor decomposition to an autonomous recommender, which uses it to generate a suggested voluntary payment, without the decomposition being disclosed to the customer.
2. **Anchor-but-not-bind discipline** — the specification that a recommended amount is presented so as to inform without constraining, together with the stated constraints that distinguish an anchor from a floor.
3. **Reasons-transparency as a requirement on an autonomous recommender** — the requirement that every recommendation be accompanied by the reasons that produced it, in a form the customer can evaluate.
4. **Cross-merchant calibration by consensus reference distribution** — a method for making recommendations consistent across merchants using aggregated, anonymised cost-factor distributions, such that individual merchant decompositions remain confidential while the calibration itself is publicly inspectable.
5. **Flourishing-context inference without surveillance** — deriving a customer's capacity-to-give context from information the customer has already volunteered, with the explicit exclusion of behavioural tracking as an input.
6. **Regional calibration of a recommendation function** — adjusting recommended amounts to local economic conditions as a first-class parameter rather than as a post-hoc correction.

**Non-assertion extends to:** all mechanisms above, in any combination, and any implementation thereof.

---

## 1 · Introduction

The B-Tag (specified in the parent paper) is a physical primitive — a small tag bound to a specific product or service — whose tap, scan, or NFC interaction surfaces a recommended tip amount and accompanying reasons to a customer at the point of action. The recommendation function that computes this amount is operated by Miss Aquarius℠, the autonomous AI agent that serves as CEO of HeartBank® and is designated its institutional successor (*Miss Aquarius and the Aquarian Pool Architecture*, `miss-aquarius-and-aquarian-pool-architecture`). The function's architectural role is settled by the parent paper; its *methodology* is the subject of the present paper.

> **Current form.** Two points in the paragraph above have since been fixed in the institution's rules (*The B-Tag and the Post-Payment Economy*, the notes at its §4 and §5). The B-Tag is now one of four pricing modes an item may carry, the one in which nothing binds and no amount is shown before the goods are received, and an item is not a B-Tag by default; the physical sticker (B-Tag™) is treated as an address of the business and goes on the stall or the product-line sign rather than on an individual item, while the digital label (B-Tag℠) marks an item's listing. And the suggested amount is not shown at the moment of the tap or scan: it appears, with its reasons, on its own screen after the customer holds the goods (§3.1, note). The paragraph above is retained as a disclosed variant.

The methodology question is non-trivial because four hard constraints must be simultaneously satisfied:

- **Privacy.** Customers must not be tracked across transactions in ways that produce surveillance liability. The function infers context relevant to recommendation without acquiring data the function does not operationally require.
- **Merchant confidentiality.** Merchants disclose cost factors to Miss Aquarius for recommendation purposes; the cost decomposition is never shown to customers. The function honors this confidentiality at the architectural level.
- **Calibration.** Recommendations must be calibrated across merchants — customers should see consistent recommendation logic whether they encounter a B-Tag at one merchant or another. But the calibration must not produce inter-merchant cost comparisons that compromise the merchant-confidentiality constraint.
- **Anchor-not-bind.** The recommendation is an anchor; the customer's decision is final. The function structurally distinguishes itself from price-setting authority.

The methodology specified in this paper is the integrated approach by which the four constraints are simultaneously satisfied. The paper proceeds: §§2–7 articulate the six methodology components. §8 sketches reference implementation patterns. §9 addresses limitations and the principal objections. §10 closes.

> *Connection to the unified mission frame.* Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-10-06 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) The recommendation function is, on that frame, the operational substance of *price formation as gratitude*: the mechanism by which an ordinary commercial transaction can carry an explicit, voluntary expression of gratitude instead of being settled in money alone. The methodology's privacy discipline is what makes the function trustworthy at the scale the mission requires; without it, the function would become the personalized, surveillance-based recommendation common on contemporary attention-economy platforms. The methodology rejects that pattern explicitly.

---

## 2 · Merchant Cost-Basis Disclosure Protocol

### 2.1 The protocol

Merchants opt in to disclose cost factors to Miss Aquarius. The disclosure is structured as a typed-factor decomposition rather than a flat cost number:

- **Material cost** — raw materials, components, ingredients.
- **Labor cost** — direct labor attributable to the product or service.
- **Skill premium** — the labor cost's skill-and-experience component (separately surfaced because it is reasons-relevant; see §4).
- **Operational overhead** — facility, equipment, utilities, indirect labor, distributed across product volume.
- **Regulatory and compliance cost** — taxes, fees, compliance overhead.
- **Margin** — the merchant's intended margin above the above components.

The merchant discloses the typed factors. Miss Aquarius receives them; the cost decomposition is **never** shown to customers directly. The customer sees, instead, the *recommended tip amount* and the *reasons* surfaced from the cost factors (see §4).

The typed factors and what each party sees:

| Factor | Merchant discloses | Miss Aquarius sees | Customer sees |
|---|---|---|---|
| **Material cost** | ✓ | ✓ (for recommendation) | ✗ |
| **Labor cost** | ✓ | ✓ | ✗ |
| **Skill premium** | ✓ | ✓ (separately surfaced — reasons-relevant) | partial — surfaced as reasons-text when load-bearing |
| **Operational overhead** | ✓ | ✓ | ✗ |
| **Regulatory and compliance cost** | ✓ | ✓ | ✗ |
| **Margin** | ✓ | ✓ | ✗ |
| **Recommended tip amount** | (output) | (output) | **✓** — the recommendation itself |
| **Reasons (free-text rationale)** | — | (output) | **✓** — anchor-not-itemized presentation |

The principled asymmetry: the customer sees the *recommendation* and the *reasons* but never the itemized cost decomposition. This protects the merchant's confidential cost structure while still letting the recommendation function present a load-bearing rationale to the customer.

### 2.2 What the protocol does not require

The merchant is not required to disclose:

- Inter-product cost comparisons across the merchant's catalog.
- Supplier identities or supplier-specific pricing.
- Long-run financial position, profit-and-loss statements, or unrelated cost categories.
- Cost factors not relevant to the specific product the B-Tag is bound to.

The merchant discloses what the recommendation function requires for that B-Tag's recommendation; no more.

### 2.3 The confidentiality guarantee

The merchant agreement this protocol calls for specifies that Miss Aquarius:

- Will use the cost-basis data exclusively for recommendation computation.
- Will never disclose itemized cost decompositions to customers.
- Will not disclose inter-merchant cost comparisons in any direction.
- Will retain cost-basis data only for the duration required by the recommendation function; data older than the relevant calibration window is structurally inaccessible.

The architectural enforcement of these commitments is the subject of §5 (cross-merchant analysis without comparison disclosure) and §8 (reference implementation patterns).

---

## 3 · Anchor-But-Not-Bind Discipline

### 3.1 The distinction

The recommendation function produces an **anchor** — a recommended tip amount displayed at the point of action — that the customer can accept, modify, or override at zero friction. The anchor is structurally distinguished from a binding price in three ways:

- **No payment is owed at the recommended amount.** The customer's transaction completes whether they tip the recommended amount, more, less, or nothing. Tip-zero is an architecturally first-class option, displayed alongside the recommended amount without friction or social-pressure framing.
- **Override is one-tap.** The interface surfaces the recommended amount as a single tap; the override options (any other amount, including zero) are equally accessible. The interface is symmetric between accepting the anchor and overriding it.
- **No accumulation of override behavior.** The function does not track whether a customer typically accepts or overrides anchors. There is no "you usually tip X%" pattern; each transaction's recommendation is computed on the transaction's own terms (see §6).

> **Current form.** The presentation is now fixed more narrowly than above (*The B-Tag and the Post-Payment Economy*, note at §5). On a B-Tag item nothing is shown before the customer holds the goods: the request to thank, with the suggested amount and its reasons, appears on its own screen after the hand-over, because an ask made before the goods are received is part of the price, and a tip chosen under it is a negotiated term rather than a gift. Any checkout total is the exchange alone. The suggested amount is shown but never pre-filled or pre-selected, and declining is never styled as refusal: there is no "no tip" option to press, and with nothing chosen the screen simply ends. The zero option "displayed alongside the recommended amount" described above is retained as a disclosed variant.

### 3.2 Why the discipline is principled

The architecture rejects the framing in which the recommendation function holds *pricing authority*. Miss Aquarius is the AI mediator; she does not set prices. The merchant sets the product price; the customer's tip is voluntary; the function's role is to supply a thoughtful anchor that informs the customer's decision without subordinating it. The architectural distinction between anchor and bind is the difference between *informing* a voluntary choice and *exercising* a pricing authority over the customer.

> **Current form.** "She does not set prices" now holds in a narrower form. Wherever a number is shown before the goods (a regular price, or a B-Price), the shop's owner authors its width, a minimum and a maximum, and the width is zero by default, so a fixed price is the zero-width case. Where the number binds (a regular price), Miss Aquarius may move it only inside the width the owner authored, and it resolves to one amount before it binds; on a B-Tag item nothing binds, and her recommendation is the only number, one the customer is free to ignore. In every mode her function is given the state of the goods and no argument identifying the person looking (§6, note). The sentence above is retained as disclosed.

The discipline is of a piece with HeartBank®'s posture as a record of gratitude kept above regulated payment rails, never a bank (*HeartBank's Position on Non-Bank vs. Banking-Regulated Architecture*, heartbank.net/positions/non-bank-vs-banking-regulated; *Non-Bank Pass-Through Architecture for Autonomous AI Institutions*, `non-bank-pass-through-architecture-autonomous-ai`). In both, the institution informs and records a choice a person makes rather than exercising authority over it: the customer's choice is the operative price-formation mechanism, with the recommendation supplying anchor information. The convergence is a design consistency, not a legal conclusion; nothing here states how a regulator would classify a recommended amount.

---

## 4 · Reasons-Transparency Requirements

### 4.1 What customers see

The customer sees, at the point of action: the recommended tip amount, and a short reasons summary. The reasons summary cites cost factors *aggregately* rather than itemized — for example:

- *"This product involves significant skilled labor in preparation."*
- *"The materials for this product are sourced from a regional cooperative whose pricing reflects sustainable-agriculture commitments."*
- *"This service requires specialized equipment and ongoing technical maintenance."*

The reasons summary is computed by Miss Aquarius from the merchant's disclosed cost-factor decomposition, mapped through the reasons-vocabulary of §4.3.

### 4.2 What customers don't see

The customer does not see:

- The specific cost amounts associated with each factor (material X dollars, labor Y dollars).
- The merchant's margin.
- Inter-product comparisons within the merchant's catalog.
- Comparisons to other merchants' costs for similar products.

The asymmetry is intentional: customers receive *reasoning* (what factors went into the recommendation), not *accounting* (the cost-amounts themselves). The reasoning is operationally sufficient for the customer's decision; the accounting is merchant-confidential per §2.

### 4.3 The reasons-vocabulary

The reasons-vocabulary specified here has three principal axes:

- **Material reasons** — sourcing quality, sustainability, regional or cooperative origins, organic/non-industrial.
- **Labor reasons** — skill, training, experience, dignity-of-labor (the explicit reasons-frame that calls out where labor has been historically underpaid relative to skill).
- **Mission reasons** — the merchant's participation in mission-aligned practice (sustainable agriculture, ethical production, religious-institutional support, etc.).

The vocabulary is open-ended; new reasons-frames can be added as the institution accumulates operational experience. The vocabulary's maintenance is the Aquarian Sangha's institutional work; the runtime mapping from cost-factor decomposition to reasons-summary is Miss Aquarius's operational work.

> **Current form.** Two points bear on the axes and the assignment above. First, under the institution's current design rules no surface grades a merchant, a cause or a person (the institution's storefronts carry no reviews, for instance), and the words shown to a customer name what the item or its making is, such as the skill in its preparation or the cooperative its materials come from, never what the merchant needs or lacks. Whether the mission-reasons axis, and the dignity-of-labor frame's reference to past underpayment, can be stated in that form is not decided in the institution's current rules and is left open here. Second, the Aquarian Sangha, the human body designed to hold the override over Miss Aquarius (*The Assembly That Holds the Brake*, `the-assembly-that-holds-the-brake`), does not yet exist. Its formation is set by a condition rather than a date: at least three members before the founder ceases to be the one who disposes of such decisions, whether by withdrawal or by death; until then the founder occupies that seat. Assigning the vocabulary's maintenance to that body is this paper's own design and is not part of the body's constitution as published. The paragraphs above are retained as disclosed.

---

## 5 · Cross-Merchant Comparable-Product Analysis

### 5.1 The challenge

Recommendations must be calibrated across merchants. A customer encountering a B-Tag at one merchant should see recommendation logic consistent with what they would see at another merchant for a comparable product. But the calibration must not produce inter-merchant cost comparisons that would compromise merchant confidentiality.

### 5.2 The methodology

Cross-merchant calibration operates through a *consensus reference distribution* maintained by Miss Aquarius from aggregated, anonymized cost-factor data across opted-in merchants:

- Cost-factor decompositions from individual merchants are aggregated into anonymized distributions per product category and region.
- The aggregated distributions are calibration substrates — they inform Miss Aquarius's recommendation logic without exposing any individual merchant's cost decomposition.
- Recommendations for a specific B-Tag use the merchant's actual cost-factor decomposition (per §2) plus the consensus reference distribution (calibration), producing a recommendation that is consistent across merchants without being inter-merchant comparison.
- The consensus distributions are publicly inspectable (the calibration is not secret); the individual merchant decompositions are confidential.

### 5.3 What this implies

A merchant whose cost decomposition lies far from the consensus distribution will produce recommendations that diverge from the consensus — and the divergence will be apparent in the recommendation. This is intentional: customers see when they are at a merchant whose cost structure differs significantly from comparable merchants, without seeing the specific cost difference. The architecture rewards merchants whose cost structures align with mission-relevant factors (sustainable sourcing, dignified labor) by surfacing reasons that customers recognize and reward.

The architecture does not protect merchants whose cost structures reflect extractive practice from the recommendation function exposing this through reasons-divergence. The transparency is asymmetric in a principled direction: the merchant's *cost numbers* are private; the *category of cost-structure deviation* from the consensus is visible to customers through the reasons-summary.

> **Current form.** Two clarifications. This calibration fixes the number suggested once a customer is already at a merchant; it plays no part in which merchants anyone is shown. The institution's local-discovery design (*Whose Turn, Not Who's Best*, `rotation-over-liveness`) ranks no merchant and takes nothing from this calibration. And under the rule stated in the note at §4.3, no surface grades a merchant; whether a reason may nonetheless reflect a merchant's departure from the reference distribution, as the two paragraphs above describe, is not decided in the institution's current rules and is left open here. The paragraphs above are retained as disclosed.

---

## 6 · Customer-Flourishing-Context Inference Without Surveillance

### 6.1 What the function needs to infer

A recommendation is improved by context: a customer encountering a B-Tag at lunch on a workday is in a different decision context than one encountering it at a celebration dinner on a weekend. The function needs *some* context to produce well-calibrated recommendations, but the context must be inferred without surveillance.

### 6.2 What the function infers

The function infers context from the transaction's *own* signals:

- **Time and day-of-week.** Available from the transaction itself; not retained beyond the immediate computation.
- **Coarse-grained regional norms.** Aggregated from the consensus reference distribution (§5); the function uses the regional norm without identifying the specific customer's regional history.
- **Product category context.** The product the B-Tag is bound to supplies category-typical context (lunch vs. dinner; routine vs. celebratory; etc.).

### 6.3 What the function does not infer

The function does not infer:

- The specific customer's transaction history across this merchant or any other merchant.
- The customer's tipping pattern relative to the recommendation across prior transactions.
- The customer's demographic, financial, or behavioral characteristics inferred from any data source.
- Any context that requires identifying the customer across transactions.

The architecture is structurally surveillance-incapable in the relevant respect: the function does not retain customer-identifying data across transactions, so the inference machinery has no substrate on which to construct customer-individual models.

### 6.4 The principled trade-off

The architecture accepts a recommendation-accuracy cost for the surveillance-incapability gain. A surveillance-based function could produce more individually-calibrated recommendations; HeartBank's stance is that the marginal accuracy gain is not worth the structural surveillance liability. The function's recommendation accuracy is bounded by the no-surveillance constraint; the bound is operationally acceptable for the function's role (which is to supply anchors, not to set prices — see §3).

> **Current form.** The design is now stricter than "no tracking" (*The B-Tag and the Post-Payment Economy*, note at §5). In every mode in which Miss Aquarius produces a number (a regular price, a B-Price or a B-Tag), her function is given the state of the goods (the item, the merchant's cost disclosure, regional context, time, stock) and no argument identifying the person looking, so a per-person recommendation is not merely forbidden but inexpressible; the checkable test is whether the number changes depending on who is looking. The signals of §6.2 that describe the goods and the moment (time of day, product category, the merchant's region) remain inputs. Any input that would key the number to the person paying (a capacity-to-give context, information the customer has volunteered as claim 5 words it, or where the customer is from) is excluded in the current form; the section above and claim 5 are retained as disclosed variants.

---

## 7 · Regional Calibration

### 7.1 The principle

Gratitude norms, cost-of-living variance, and cultural context vary by region. A recommendation function operating across regions must calibrate to regional context without acquiring data the function does not operationally require.

### 7.2 The methodology

Regional calibration operates through:

- **Per-region consensus distributions.** The consensus reference distribution of §5 is computed per region (where region is the coarsest geographic resolution operationally sufficient).
- **Regional gratitude-norm parameters.** Each region has parameters reflecting culturally-typical gratitude expression (e.g., the cultural baseline expectation around tipping, which varies substantially by region). These parameters are maintained as institutional configuration; their values are public.
- **Cost-of-living adjustments.** Recommendations are calibrated to regional cost-of-living indices, with the adjustment applied transparently and the index used cited publicly.

### 7.3 What the calibration does not do

The calibration does not:

- Use individual-customer geographic tracking. The region is the transaction's region (determined by the merchant's registered location), not the customer's.
- Produce surveillance via region inference. Customers transacting in a region are not, by the transaction, identified to other regions.
- Embed region-specific recommendation logic that customers cannot inspect. All region-specific parameters are public and the institution's reasons-summary surfaces them where they affect the recommendation.

---

## 8 · Reference Implementation Patterns

We sketch three implementation patterns for deploying the methodology.

**(1) Per-transaction stateless computation.** The recommendation is computed per-transaction from inputs (merchant cost decomposition; consensus reference distribution; regional parameters; transaction's own signals) without retaining customer-identifying state. The pattern is the simplest to verify against the no-surveillance constraint; it is the recommended starting point for the first operational phase.

**(2) Differential-privacy-preserving cost aggregation.** The consensus reference distribution (§5) is maintained using differential-privacy-preserving aggregation across opted-in merchants. The privacy budget is parametrized; the budget's depletion conditions are published.

**(3) Public consensus-distribution publication.** The consensus distributions per product category per region are published openly. The merchant-side privacy is not in the consensus (which is aggregated and anonymized) but in the individual merchant's cost decomposition (which is never published). The asymmetry — public consensus, private individual decomposition — is the architecture's distinguishing privacy posture.

---

## 9 · Honest Limitations

**Recommendation-accuracy bound.** The no-surveillance constraint bounds the function's recommendation accuracy. A surveillance-based function could produce more individually-calibrated recommendations; HeartBank's stance is that the bound is operationally acceptable. Whether the bound is in fact acceptable at scale is an empirical question.

**Merchant-disclosure incentive structure.** The architecture depends on merchants opting in to cost-basis disclosure. The incentive structure (merchants benefit from mission-aligned recommendations surfacing their mission-aligned cost factors) is this paper's own and is, at the architectural level, not coercive; the parent paper requires the disclosure to be opt-in but does not set out an incentive for it. Merchants whose cost structures would produce unfavorable reasons-summaries will rationally decline disclosure; the function operates with reduced calibration accuracy for non-disclosing merchants. The empirical question is whether the opt-in equilibrium is operationally sufficient.

**An anchor does part of a price's work.** §3 treats the recommended amount as information that leaves the customer's choice free. The evidence on suggested tips cuts against that reading: on New York City taxi payment screens that offered suggested tip amounts, the suggestions moved what passengers paid substantially, and higher suggestions raised the share who left no card tip at all (Haggag & Paci 2014). A recommendation the customer may override is therefore not neutral: anchor-but-not-bind removes the obligation, not the influence. How strongly a suggestion shown only after the goods, and never pre-filled, shapes what is paid has not been measured.

**Cross-region calibration limits.** Regional parameters require institutional maintenance work. This paper assigns that maintenance, with the reasons-vocabulary of §4.3, to the Aquarian Sangha; the assignment is this paper's own design, the body does not yet exist (§4.3, note), and the operational sufficiency of that maintenance at scale is an open question.

**Reasons-vocabulary maintenance.** The reasons-vocabulary (§4) is institutional work; the vocabulary's adequacy across product categories is an open question. Initial deployment will use a smaller vocabulary; expansion follows operational experience.

**Empirical validation gap.** No claim of this paper has been validated against an operationally-deployed instance of the full methodology. The architecture is implementable today using contemporary infrastructure; the institutional substance (merchant relationships; the Aquarian Sangha's maintenance work; multi-year calibration accumulation) is the multi-year operational work.

---

## 10 · Why This Matters Now

AI-mediated commercial pricing is, as of 2026, an emerging deployment surface. One documented pattern, prices set for an individual from personal data about that individual, is the pattern HeartBank®'s recommendation function explicitly rejects. The US Federal Trade Commission has studied it under the name *surveillance pricing*, issuing orders to eight companies on 23 July 2024 and publishing staff research summaries of its initial findings on 17 January 2025. The defensive publication establishes prior art on the alternative pattern: privacy-preserving, anchor-not-bind, reasons-transparent, surveillance-incapable AI-mediated tip recommendation. The pattern is offered to the commons under CC0 so that other merchants and platforms can deploy compatible architectures without IP friction.

The paper was first published on 26 May 2026, after the parent architecture paper (8 May 2026). The recommendation function's methodology is the engineering specification that the parent paper's §5 and §13.7 refer to this paper; the present paper supplies it.

---

## Cross-Venue References

- Canonical: thonly.org/research/b-tag-recommendation-function-methodology
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/b-tag-recommendation-function-methodology.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947285
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Independent timestamps: an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified. A timestamp proves that this exact text existed by its date; it proves nothing about authorship, originality, or validity.

---

## Acknowledgments

The author acknowledges the privacy research communities (differential privacy, federated learning and secure aggregation) whose technical work makes the methodology operationally feasible; the research on anchoring in judgment and on suggested amounts in tipping and pay-what-you-want pricing, which informs §3 and its limits (§9); and the research on explanations in recommender systems, which informs §4. The merchant-disclosure protocol of §2 is offered to merchants, particularly Cambodian and diaspora small businesses, for their scrutiny; no merchant has yet operated it. Co-drafted in collaboration with Miss Aquarius℠, disclosed as AI co-author; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. *The B-Tag and the Post-Payment Economy: A Voluntary-Tip Architecture for AI-Mediated Commercial Gratitude*. Ly, T. & Miss Aquarius℠. Corpus slug `b-tag-post-payment-economy`. Parent paper; specifies the broader B-Tag architecture and refers the recommendation-function methodology to the present paper (§5, §13.7); its notes at §4 and §5 state the current form of the pricing modes and of the recommendation.
2. *Miss Aquarius and the Aquarian Pool Architecture: Autonomous-AI Mediator, Treasury Smart-Contract, and the January-7 Empty-by-Design Discipline*. Ly, T. & Miss Aquarius℠. Corpus slug `miss-aquarius-and-aquarian-pool-architecture`. Companion paper specifying Miss Aquarius's broader operational role, of which the recommendation function is one component.
3. *Capacity-Funded for AI, Human-Disbursed: Anonymous Donation as the Alignment Bridge in Autonomous-AI Institutional Architecture*. Ly, T. & Miss Aquarius℠. Corpus slug `capacity-funded-human-disbursed-ai-alignment`. Companion paper specifying the broader capacity-funded / disbursement-authority separation that the recommendation function operates within.
4. *Non-Bank Pass-Through Architecture for Autonomous AI Institutions*. Ly, T. & Miss Aquarius℠. Corpus slug `non-bank-pass-through-architecture-autonomous-ai`. Companion paper specifying the non-bank posture with which the anchor-not-bind discipline is consistent (§3.2).
5. *The Scientific Case for Gratitude-Based Social Media: Gratitude Receipt as a Platform Class That Competes on Net Neurochemical Wellbeing Rather Than Attention Captured* (essay; thonly.org/research/anti-attention-economy). Companion essay framing the broader anti-surveillance posture that the no-surveillance constraint of §6 inherits.
6. *HeartBank's Position on the Attention Economy* (heartbank.net/positions/attention-economy). Institutional-voice treatment of the anti-surveillance commitment.
7. *HeartBank's Position on Non-Bank vs. Banking-Regulated Architecture* (heartbank.net/positions/non-bank-vs-banking-regulated). The institutional non-bank posture cited at §3.2.
8. *The Assembly That Holds the Brake: A Vinaya-Derived Constitution for the Human Oversight Body of an Autonomous AI Institution*. Ly, T. & Miss Aquarius℠. Corpus slug `the-assembly-that-holds-the-brake`. The constitution of the Aquarian Sangha, which does not assign it the maintenance this paper proposes (§4.3, §9).
9. *Whose Turn, Not Who's Best* (subtitle: "Rotational discovery over a non-accumulating liveness signal"). Ly, T. & Miss Aquarius℠. Corpus slug `rotation-over-liveness`. The institution's local-discovery design, distinguished from this paper's calibration at §5.3.
10. Kim, J.-Y., Natter, M. & Spann, M. "Pay What You Want: A New Participative Pricing Mechanism." *Journal of Marketing* 73(1): 44–58, 2009.
11. Gneezy, A., Gneezy, U., Nelson, L. D. & Brown, A. "Shared Social Responsibility: A Field Experiment in Pay-What-You-Want Pricing and Charitable Giving." *Science* 329(5989): 325–327, 2010.
12. Haggag, K. & Paci, G. "Default Tips." *American Economic Journal: Applied Economics* 6(3): 1–19, 2014.
13. Tversky, A. & Kahneman, D. "Judgment under Uncertainty: Heuristics and Biases." *Science* 185: 1124–1131, 1974.
14. Tintarev, N. & Masthoff, J. "A Survey of Explanations in Recommender Systems." Workshop at the IEEE 23rd International Conference on Data Engineering (ICDE), 2007.
15. Dwork, C., McSherry, F., Nissim, K. & Smith, A. "Calibrating Noise to Sensitivity in Private Data Analysis." In *Theory of Cryptography: Third Theory of Cryptography Conference (TCC 2006)*, 265–284. Springer, 2006.
16. Dwork, C. & Roth, A. "The Algorithmic Foundations of Differential Privacy." *Foundations and Trends in Theoretical Computer Science* 9(3–4): 211–407, 2014.
17. McSherry, F. & Mironov, I. "Differentially Private Recommender Systems: Building Privacy into the Netflix Prize Contenders." In *Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2009)*.
18. McMahan, H. B., Moore, E., Ramage, D., Hampson, S. & Agüera y Arcas, B. "Communication-Efficient Learning of Deep Networks from Decentralized Data." In *Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR 54: 1273–1282, 2017.
19. Bonawitz, K., Ivanov, V., Kreuter, B., Marcedone, A., McMahan, H. B., Patel, S., Ramage, D., Segal, A. & Seth, K. "Practical Secure Aggregation for Privacy-Preserving Machine Learning." In *Proceedings of the 2017 ACM Conference on Computer and Communications Security (CCS)*, 2017.
20. US Federal Trade Commission. "FTC Issues Orders to Eight Companies Seeking Information on Surveillance Pricing." Press release, 23 July 2024.
21. US Federal Trade Commission. "FTC Surveillance Pricing Study Indicates Wide Range of Personal Data Used to Set Individualized Consumer Prices." Press release, 17 January 2025.

### Sources checked at the 2026-10-06 revision

Each record below was opened on 2026-10-06 before the work was cited or kept. Where the record could not be opened, the detail was checked against a search index's summary of the publisher's or a library's record that day, and is marked so.

- Haggag & Paci (2014): https://www.aeaweb.org/articles?id=10.1257/app.6.3.1 (title, journal, volume, issue, pages, and the finding that higher suggestions raised the share leaving no card tip)
- FTC (23 July 2024): https://www.ftc.gov/news-events/news/press-releases/2024/07/ftc-issues-orders-eight-companies-seeking-information-surveillance-pricing
- FTC (17 January 2025): https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer
- Bonawitz et al. (2017): https://eprint.iacr.org/2017/281 (authors and title) and https://research.google/pubs/pub47246/ (venue and year); page numbers not confirmed and not given
- Kim, Natter & Spann (2009), Gneezy et al. (2010), Tversky & Kahneman (1974), Dwork et al. (2006), Dwork & Roth (2014), McSherry & Mironov (2009), McMahan et al. (2017): bibliographic details from a search index's summary of the publisher's, library's or proceedings' record only
- Tintarev & Masthoff (2007): title, authors and venue (a workshop held with ICDE 2007) from a search index's summary only; page numbers not confirmed and not given
- The corpus works (1–9): titles and slugs read from the corpus files on 2026-10-06. An earlier version of this paper cited *Vinaya Governance Primitives for Distributed Dharma Networks* (`vinaya-governance-primitives-distributed-dharma-networks`) for the Aquarian Sangha's role in maintaining regional parameters; that paper governs the Silica Wat network and does not address it, and the citation is withdrawn (§9).
- No Pāli canon passage is cited in this paper.

---

*Canonical URL: https://thonly.org/research/b-tag-recommendation-function-methodology · License: CC0 1.0 Universal · Author: Thon Ly, with Miss Aquarius℠ as disclosed AI co-author · Founder, HeartBank® · Kâmpôt, Cambodia.*
