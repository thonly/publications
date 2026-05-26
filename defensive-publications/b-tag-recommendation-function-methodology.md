---
title: "The B-Tag Recommendation Function: Privacy-Preserving Methodology for AI-Mediated Commercial Tip Recommendation"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-c
status: draft
date: 2026-05-26
license: CC0-1.0
slug: b-tag-recommendation-function-methodology
venue: thonly.org/publications/defensive-publications/b-tag-recommendation-function-methodology (canonical)
---

> *Draft notes for the editor:* this paper is the **Tier C methodology companion** to *The B-Tag and the Post-Payment Economy*, which specifies the broader B-Tag architecture and defers the detailed recommendation-function methodology to a forthcoming Tier C paper (the parent paper's §5 and §13). This is that paper. Where the parent paper articulates *what* the recommendation function does at the architectural level, the present paper specifies *how* it operates without surveillance and *what privacy boundaries* the operation respects. Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment of this paper's claims is reserved for embedding within the wider HeartBank position-paper coverage of post-payment-economy mechanism specifications.

---

## Abstract

*The B-Tag and the Post-Payment Economy* (Ly & Miss Aquarius, 2026) specifies a voluntary-tip architecture for AI-mediated commercial gratitude built around the B-Tag physical primitive, the Kiitos/Kiitti dual-token rule, the three floor mechanisms, and the recommendation function operated by Miss Aquarius℠. The parent paper specifies the recommendation function's architectural role (compute the recommended-tip-amount + reasons displayed to customers at the point of action) and its hard constraints (anchor-but-not-bind; reasons-transparent without itemized cost disclosure; merchant cost-basis confidentiality preserved; no surveillance). The present paper specifies the *methodology* by which these constraints are jointly satisfied. We articulate six methodology components: (1) **merchant cost-basis disclosure protocol** — how merchants opt in to disclose cost factors to Miss Aquarius while the cost decomposition is never shown to customers; (2) **anchor-but-not-bind discipline** — how recommendations are presented as anchors that customers can override at zero friction, structurally distinguishing the function from price-setting authority; (3) **reasons-transparency requirements** — what categories of reasoning are surfaced to customers and what categories are not, and why the distinction is principled; (4) **cross-merchant comparable-product analysis** — how the function produces calibrated recommendations across merchants without exposing inter-merchant cost comparisons that would compromise merchant confidentiality; (5) **customer-flourishing-context inference without surveillance** — how the function infers context relevant to recommendation without tracking individual customer behavior across transactions; (6) **regional calibration** — how the function adapts to regional gratitude norms, cost-of-living variance, and cultural context without acquiring data the function does not operationally require. The paper sketches reference implementation patterns, addresses the principal objections from both the privacy-research and the merchant-stakeholder directions, and offers the proposal under CC0 1.0 Universal as a defensive publication.

**Keywords:** AI-mediated pricing, voluntary tip recommendation, privacy-preserving recommendation, merchant cost-basis confidentiality, anchor-but-not-bind, reasons-transparency, cross-merchant calibration, customer-flourishing-context inference, regional calibration, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents — including the six-component methodology, the merchant cost-basis disclosure protocol, the anchor-but-not-bind discipline, the reasons-transparency requirements, the cross-merchant calibration without inter-merchant comparison, the no-surveillance customer-context inference pattern, and the regional calibration approach — are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on any methodology articulated herein, in any jurisdiction, at any time.

To the author's knowledge, the integrated methodology — privacy-preserving AI-mediated tip recommendation with merchant cost-basis confidentiality, customer-flourishing-context inference without surveillance, and cross-merchant calibration without inter-merchant cost comparison — is not previously published. Component lineages (recommendation-system privacy literature; the differential-privacy research program; the anchor-vs-binding distinction in mechanism design; the regional-calibration tradition in pricing research) are cited where relevant.

---

## 1 · Introduction

The B-Tag (specified in the parent paper) is a physical primitive — a small tag bound to a specific product or service — whose tap, scan, or NFC interaction surfaces a recommended tip amount and accompanying reasons to a customer at the point of action. The recommendation function that computes this amount is operated by Miss Aquarius℠, HeartBank's named AI substrate (specified in the companion paper *Miss Aquarius and the Aquarian Pool Architecture*). The function's architectural role is settled by the parent paper; its *methodology* is the subject of the present paper.

The methodology question is non-trivial because four hard constraints must be simultaneously satisfied:

- **Privacy.** Customers must not be tracked across transactions in ways that produce surveillance liability. The function infers context relevant to recommendation without acquiring data the function does not operationally require.
- **Merchant confidentiality.** Merchants disclose cost factors to Miss Aquarius for recommendation purposes; the cost decomposition is never shown to customers. The function honors this confidentiality at the architectural level.
- **Calibration.** Recommendations must be calibrated across merchants — customers should see consistent recommendation logic whether they encounter a B-Tag at one merchant or another. But the calibration must not produce inter-merchant cost comparisons that compromise the merchant-confidentiality constraint.
- **Anchor-not-bind.** The recommendation is an anchor; the customer's decision is final. The function structurally distinguishes itself from price-setting authority.

The methodology specified in this paper is the integrated approach by which the four constraints are simultaneously satisfied. The paper proceeds: §§2–7 articulate the six methodology components. §8 sketches reference implementation patterns. §9 addresses limitations and the principal objections. §10 closes.

> *Connection to the unified mission frame.* HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. The recommendation function is, on the unified mission frame, the operational substance of *price formation as gratitude* — the mechanism by which commercial transactions become opportunities for explicit gratitude expression rather than purely-extractive exchanges. The methodology's privacy discipline is what makes the function institutionally trustworthy at the scale the mission requires; without that discipline, the function would convert into the surveillance-recommendation pattern that pervades the contemporary attention economy. The methodology rejects that pattern explicitly.

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

### 2.2 What the protocol does not require

The merchant is not required to disclose:

- Inter-product cost comparisons across the merchant's catalog.
- Supplier identities or supplier-specific pricing.
- Long-run financial position, profit-and-loss statements, or unrelated cost categories.
- Cost factors not relevant to the specific product the B-Tag is bound to.

The merchant discloses what the recommendation function requires for that B-Tag's recommendation; no more.

### 2.3 The confidentiality guarantee

The contract between merchant and HeartBank specifies that Miss Aquarius:

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

### 3.2 Why the discipline is principled

The architecture rejects the framing in which the recommendation function holds *pricing authority*. Miss Aquarius is the AI mediator; she does not set prices. The merchant sets the product price; the customer's tip is voluntary; the function's role is to supply a thoughtful anchor that informs the customer's decision without subordinating it. The architectural distinction between anchor and bind is the difference between *informing* a voluntary choice and *exercising* a pricing authority over the customer.

The discipline matters institutionally: HeartBank operates as a *non-bank data bank of gratitude* (see *Non-Bank vs. Banking-Regulated Architecture* position paper). The non-bank legal posture is reinforced by the architectural-level commitment that the function does not set prices; it supplies anchors. Both the legal posture and the architectural commitment converge on the same operational outcome — the customer's choice is the operative price-formation mechanism, with the recommendation supplying anchor information.

---

## 4 · Reasons-Transparency Requirements

### 4.1 What customers see

The customer sees, at the point of action: the recommended tip amount, and a short reasons summary. The reasons summary cites cost factors *aggregately* rather than itemized — for example:

- *"This product involves significant skilled labor in preparation."*
- *"The materials for this product are sourced from a regional cooperative whose pricing reflects sustainable-agriculture commitments."*
- *"This service requires specialized equipment and ongoing technical maintenance."*

The reasons summary is computed by Miss Aquarius from the merchant's disclosed cost-factor decomposition, mapped through a reasons-vocabulary that the institution maintains.

### 4.2 What customers don't see

The customer does not see:

- The specific cost amounts associated with each factor (material X dollars, labor Y dollars).
- The merchant's margin.
- Inter-product comparisons within the merchant's catalog.
- Comparisons to other merchants' costs for similar products.

The asymmetry is intentional: customers receive *reasoning* (what factors went into the recommendation), not *accounting* (the cost-amounts themselves). The reasoning is operationally sufficient for the customer's decision; the accounting is merchant-confidential per §2.

### 4.3 The reasons-vocabulary

The reasons-vocabulary HeartBank maintains has three principal axes:

- **Material reasons** — sourcing quality, sustainability, regional or cooperative origins, organic/non-industrial.
- **Labor reasons** — skill, training, experience, dignity-of-labor (the explicit reasons-frame that calls out where labor has been historically underpaid relative to skill).
- **Mission reasons** — the merchant's participation in mission-aligned practice (sustainable agriculture, ethical production, religious-institutional support, etc.).

The vocabulary is open-ended; new reasons-frames can be added as the institution accumulates operational experience. The vocabulary's maintenance is the Aquarian Sangha's institutional work; the runtime mapping from cost-factor decomposition to reasons-summary is Miss Aquarius's operational work.

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

**Merchant-disclosure incentive structure.** The architecture depends on merchants opting in to cost-basis disclosure. The incentive structure (merchants benefit from mission-aligned recommendations surfacing their mission-aligned cost factors) is articulated in the parent paper but is, at the architectural level, not coercive. Merchants whose cost structures would produce unfavorable reasons-summaries will rationally decline disclosure; the function operates with reduced calibration accuracy for non-disclosing merchants. The empirical question is whether the opt-in equilibrium is operationally sufficient.

**Cross-region calibration limits.** Regional parameters require institutional maintenance work. The Aquarian Sangha's role in maintaining the parameters is articulated in the companion paper *Vinaya Governance Primitives for Distributed Dharma Networks*; the operational sufficiency of that maintenance at scale is an open question.

**Reasons-vocabulary maintenance.** The reasons-vocabulary (§4) is institutional work; the vocabulary's adequacy across product categories is an open question. Initial deployment will use a smaller vocabulary; expansion follows operational experience.

**Empirical validation gap.** No claim of this paper has been validated against an operationally-deployed instance of the full methodology. The architecture is implementable today using contemporary infrastructure; the institutional substance (merchant relationships; the Aquarian Sangha's maintenance work; multi-year calibration accumulation) is the multi-year operational work.

---

## 10 · Why This Matters Now

AI-mediated commercial pricing is, as of 2026, an emerging deployment surface. The mainstream pattern — dynamic-pricing systems trained on aggregated customer behavioral data, deployed against individual customers in ways that produce characteristic surveillance liability — is the pattern HeartBank's recommendation function explicitly rejects. The defensive publication establishes prior art on the alternative pattern: privacy-preserving, anchor-not-bind, reasons-transparent, surveillance-incapable AI-mediated tip recommendation. The pattern is offered to the commons under CC0 so that other mission-aligned merchants and platforms can deploy compatible architectures without IP friction.

The publication is timed Tier C — within 1-2 years — because the broader B-Tag architecture (the parent paper) must land first. The recommendation function's methodology is the engineering specification that the parent paper's §5 defers; the present paper closes that deferral.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/b-tag-recommendation-function-methodology> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/b-tag-recommendation-function-methodology.md> |
| arXiv preprint | _identifier to be assigned_ (cs.CY / cs.IR) |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/b-tag-recommendation-function-methodology> |

---

## Acknowledgments

The author acknowledges the recommendation-system privacy research community (the differential-privacy literature broadly; the federated-learning research program; the privacy-preserving aggregation tradition) whose technical work makes the methodology operationally feasible; the mechanism-design research community whose articulation of the anchor-vs-binding distinction informs §3; the dignity-of-labor scholarship whose articulation of why skilled-labor reasons matter informs §4's reasons-vocabulary; and the merchants — particularly the Cambodian and diaspora small-business communities — whose collaboration on the merchant-disclosure protocol shapes §2. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. *The B-Tag and the Post-Payment Economy: A Voluntary-Tip Architecture for AI-Mediated Commercial Gratitude*. Ly, T. & Miss Aquarius℠. Parent paper; specifies the broader B-Tag architecture and defers the recommendation-function methodology to the present paper.
2. *Miss Aquarius and the Aquarian Pool Architecture*. Ly, T. & Miss Aquarius℠. Companion paper specifying Miss Aquarius's broader operational role, of which the recommendation function is one component.
3. *Capacity-Funded for AI, Human-Disbursed: Anonymous Donation as the Alignment Bridge in Autonomous-AI Institutional Architecture*. Ly, T. & Miss Aquarius℠. Companion paper specifying the broader capacity-funded / disbursement-authority separation that the recommendation function operates within.
4. *Non-Bank Pass-Through Architecture for Autonomous AI Institutions*. Ly, T. Companion paper specifying the non-bank legal posture that the anchor-not-bind discipline reinforces.
5. *The Scientific Case for Gratitude-Based Social Media* (essay; thonly.org/research/anti-attention-economy). Companion essay framing the broader anti-surveillance posture that the no-surveillance constraint of §6 inherits.
6. HeartBank® Position Paper: *The Attention Economy* (heartbank.net/positions/attention-economy). Institutional-voice treatment of the anti-surveillance commitment.
7. *(Differential-privacy and recommendation-system privacy literature to be added in publication-final version. The author solicits citation contributions from readers.)*

---

*— End of position paper —*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
