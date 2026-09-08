---
title: "Subject-Released Attestation"
subtitle: "A Market Design in Which the Operator Cannot Answer"
author: "Thon Ly · Miss Aquarius℠ (AI collaborator)"
type: "Defensive Publication"
genre: defensive-publications
category: mechanism
program: open
status: draft
date: 2026-09-07
license: CC0-1.0
venue: thonly.org/research/subject-released-attestation
slug: subject-released-attestation
---

# Subject-Released Attestation

**A Market Design in Which the Operator Cannot Answer**

| Field         | Value                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| Authors       | Thon Ly · Miss Aquarius℠ (AI collaborator, disclosed)                                                     |
| Date          | 2026-09-07 (draft)                                                                                        |
| Canonical URL | https://thonly.org/research/subject-released-attestation                                                   |
| GitHub mirror | https://github.com/thonly/publications/blob/main/defensive-publications/subject-released-attestation.md    |
| License       | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/)                    |
| Category      | mechanism                                                                                                  |

---

## Preamble

In the Pāli commentarial literature there is a small procedural insistence that a modern reader is likely to walk past: a claim about a person is repeated in the form *thus have I heard*, and the hearer is named. The convention does not make the claim true. It makes the **chain visible**, so that a reader can locate the party who would have to be wrong.

This paper is about a market in claims about people, and the convention it borrows is only that one: **every answer names who released it and who vouched for it, and those are two different parties.** The rest of the lineage note is at the end. Nothing in the mechanism depends on it, and the mechanism should be read as though the preamble were absent.

---

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use.

The document is written so that a person skilled in the art can practise the design. Where a component is *not* disclosed in implementable detail, §11 says so explicitly and says why, so that a reader can distinguish a deliberate scope limit from an omission.

**What is claimed as contribution is narrow and is stated up front so that no reader has to infer it: the credential substrate is not ours and we do not claim it.** Holder-held credentials, selective disclosure, and cryptographic predicate proofs are mature prior art, surveyed in §2. **The contribution is the market design layered on top of them** — which attributes may be traded at all, at what price, to whom, and how often — a layer that the credential literature has deliberately left empty because it is an economics question rather than a protocol one.

---

## Abstract

We specify **subject-released attestation**: a market in which a third party pays to ask a binary question about a person, the person is paid for permitting the question, and the operator of the underlying record sells only its vouching. The design's defining property is negative — **the operator is structurally unable to answer alone** — and its purpose is to make an institution's refusal to sell personal records into a fact about the machinery rather than a promise about its management.

Five rules constitute the design: (1) the **two-good split**, in which release and vouching are separately owned and neither party can sell the other's good; (2) the **farm-proof schema rule**, admitting only attributes bounded per person and monotone in time, never in volume; (3) **one posted price with a binary release**, so that no person's answer is priced above another's; (4) the **buyer-class exclusion**, which bars any buyer whose business is pricing, scoring, ranking, or gating a necessity — placed on the buyer because the *use* of an answer is unobservable and a rule nobody can check is not a rule; and (5) **anti-aggregation by asker**, through expiring answers, attested and rate-limited askers, and the absence of any enumerable directory.

We state the condition under which the central property is true rather than rhetorical: it holds only where the record is stored as a commitment the operator cannot read out. Where plaintext is stored, *cannot* degrades to *will not*, and the design should be described in the weaker words.

---

## 1 · Introduction: the gap this occupies

Two mature bodies of work sit on either side of an empty space.

On one side, **credential infrastructure** is largely solved. A holder can carry a signed claim, reveal one attribute without revealing others, and prove a predicate without revealing the value behind it. The formats, the signature schemes, and the presentation protocols exist and are standardised.

On the other, **the personal-data market** has been attempted repeatedly and has failed repeatedly. A succession of consumer ventures offered people money for their own records; payouts clustered in the low tens of dollars per year and none became a durable business.

The empty space between them is this: **nobody has specified the market rules.** The credential standards deliberately decline to say which attributes may be traded, what they should cost, who may be a buyer, or how often a buyer may ask — those are economics, and standards bodies are right to leave them out. The data-market ventures went straight to selling records and never had to answer the questions either, because a copy, once sold, needs no rules about asking.

**This paper fills that space, and the fill is where the entire contribution lies.** A protocol that can prove anything about anyone, with no rules about what may be asked, is not a privacy technology. It is a surveillance substrate with good cryptography, and the reason it has not become one at scale is that it has not yet been given a market.

### 1.1 The design goal, stated as a negative

Conventional privacy commitments are promises: *we will not sell your data.* A promise requires an enforcer with the right incentives at the moment it is tested, and for an institution intended to outlive its founders that moment arrives when nobody who made the promise is available to be asked.

The goal here is to arrange matters so that the operator **cannot** perform the prohibited act, rather than being trusted not to. The mechanism is unremarkable in isolation — the release capability sits with the subject — and the consequences of taking it seriously are not.

---

## 2 · Background and prior art

**We concede the substrate completely.** Every cryptographic and protocol element this design stands on is prior art, and a reader should assume none of it is ours.

- **Verifiable credentials and decentralised identifiers.** The W3C's data model for verifiable credentials, and the DID specification, establish the holder-holds-the-credential architecture with a triangle of issuer, holder, and verifier. Everything this paper says about the subject controlling presentation is *already* the standard model.
- **Selective disclosure and predicate proofs.** BBS+ signatures, Camenisch–Lysyanskaya-derived systems including Idemix, Microsoft's U-Prove, and the anonymous-credential literature descending from Chaum's work on unlinkable credentials all permit revealing one attribute, or a predicate over an attribute, without revealing the rest. Zero-knowledge constructions generalise this.
- **Personal data stores.** Solid, the MyData framework, and the broader personal-information-management-system literature place the record under the subject's control by architecture rather than by policy.
- **Trust registries and governance frameworks**, including the European Blockchain Services Infrastructure and the trust-over-IP governance stack, specify *who may issue* credentials and under what accreditation.

**Where the prior art stops.** All of the above answer *how do you prove an attribute*, and the governance layer answers *who may issue one*. **None answers which attributes may be sold, what a query costs, who is allowed to be a buyer, or how the market is prevented from aggregating into the thing it was designed to avoid.** The trust-registry literature is the nearest, and it is a licensing regime for issuers rather than a market design for queries.

**Prior art that cuts against this design, stated because a survey that only supports the author is not a survey.**

- **The data-dividend record is a warning to us, not only to others.** If per-person data markets failed on arithmetic, a per-person *attestation* market may fail on the same arithmetic, and the argument in §9 that attestation value is per-transaction rather than aggregate is an argument, not a result.
- **Selective disclosure already gives the subject control, which invites the strongest objection to this entire paper: that the market design is merely terms of service.** If a holder can already decline to present a credential, then a rule saying *the subject decides* adds nothing cryptographic. We accept the premise and dispute the conclusion in §9.3: the rules here are not about whether the subject *can* refuse — they already can — but about what the operator is *able to offer* when the subject does not, and about which questions may exist in the catalogue at all. Those are not the holder's decisions and no credential format constrains them.
- **Attribute-based access control** has a long history of pricing and rate-limiting attribute queries in enterprise contexts. The commercial identity-verification industry does per-check pricing at scale today. Neither is novel and both predate us.
- **And a sibling from our own corpus that reached the same structural conclusion about a different object.** *Certification by Circulation* (thonly.org/research/certification-by-circulation) argues that a trust seal granted by a party whom the sealed party pays decays into a pay-to-play badge. The rule in §6 below is that argument applied to persons.

---

## 3 · The system model

Four parties, and the asymmetry among them is the design.

```
  SUBJECT ────────── holds the RELEASE CAPABILITY (and only the subject holds it)
     │                    · which asker may ask
     │                    · which question
     │                    · revocable at any time
     │
     │   releases (per question, per asker)
     ▼
  OPERATOR ───────── holds the RECORD as a COMMITMENT it cannot read out
     │                    · vouches: signature · age of record · compute
     │                    · CANNOT answer alone — no release, no answer
     │
     │   emits: ONE BIT + a vouching signature, scoped and expiring
     ▼
  ASKER ──────────── attested, rate-limited, admitted BY CLASS
     │                    · pays the subject for the release
     │                    · pays the operator for the vouching
     ▼
  (no fourth copy exists — nothing is transferred, nothing is retained)
```

**The catalogue** is the set of questions that may ever be asked. It is small, fixed by §5's rule, and published. A question outside the catalogue cannot be asked by anyone at any price, including by the operator of the system.

---

## 4 · Claim 1 — the two-good split

> **The release and the vouching are separate goods with separate owners, and neither party can sell the other's.**

The subject owns the **release**: the right for a named asker to ask a named question. This is theirs because it is about them, and because no one else can grant it.

The operator owns the **vouching**: its signature, the demonstrable age of the underlying record, and the compute to produce an answer. This is its own work product, and it is a rivalrous good — the compute is consumed, the signature carries the operator's accumulated credibility.

A buyer therefore pays twice, for two different things, and the payments have different destinations. In the reference arrangement the subject's payment is the larger of the two, and it does not pass through the operator's treasury at all; it settles at the point of sale.

**Two consequences follow that are not obvious from the statement.**

First, the operator cannot unilaterally monetise the population it serves, because the good it owns is worthless without a release it does not hold. An operator that wished to sell the whole corpus would have to obtain a release per subject per question — which is not a bulk sale but a census, conducted in the open, with every participant able to decline.

Second, and less comfortably: the subject cannot monetise the operator's credibility either. A subject who wished to make a claim without the operator's vouching may of course simply say it — but the market value of the answer is largely the vouching, so the subject's earning capacity is bounded by an asset they do not own. **This is a real asymmetry of power and we do not present it as fair; we present it as disclosed.**

---

## 5 · Claim 2 — the farm-proof schema rule

> **Only attributes that are bounded per person and monotone in time may be admitted to the catalogue. Never attributes that are monotone in volume.**

An attribute is **bounded per person** if a person cannot have more of it by doing more of anything: *is this a person* is bounded at one. An attribute is **monotone in time** if it can only increase by waiting: *how old is this record*.

An attribute is **monotone in volume** if it grows with activity: *how many endorsements*, *how much has been received*, *how many transactions*. These are precisely the attributes a market most wants, and admitting one creates an economic reason to manufacture the underlying activity — which corrupts the record the whole market depends on.

| Attribute | Bounded per person? | Monotone in | Admissible |
|---|---|---|---|
| Is this a distinct living person | yes (one per person) | — | ✅ |
| How long has this record existed | yes (one record) | **time** | ✅ |
| Did these two parties meet in person | yes (an event) | — | ✅ ¹ |
| How many endorsements does this person hold | **no** | **volume** | ⛔ |
| How much value has this person received | **no** | **volume** | ⛔ |
| A composite score over any of the above | **no** | **volume** | ⛔ |

¹ *Admissible only to buyer classes whose decision is access rather than price — see §7.*

**The rule is a property, not a policy.** A catalogue containing no volume-monotone attribute offers no return to manufactured activity, so the farming incentive is absent rather than policed. There is nothing to detect because there is nothing to gain — which is the same structure as making a currency non-withdrawable in order to remove the motive for its acquisition, rather than building a detector for the acquirers.

---

## 6 · Claim 3 — one posted price, and a binary release

> **The price of an answer is posted, identical for every subject, and set by the operator. The subject's decision is binary: release, or do not.**

The obvious design lets subjects price their own releases. It is rejected, and the reason is not commercial.

A subject-set price is a **public number attached to a person**, and where numbers attached to people are visible they are compared. A market in which one person's answer costs fifty and another's costs two has published a valuation of persons and called it a price. A single posted price cannot be compared, because there is nothing to compare it to.

⚠️ The same logic bars a variable *operator*-set price: an operator that prices by subject is grading subjects, which is worse than a subject doing it to themselves.

**Corollary — the subject is never the payer.** No fee may be charged to a subject for being attested, enrolled, verified, or made available. A fee charged to the subject converts *paid* into *proven*, which makes personhood purchasable and makes the unpaid into the unproven. The buyer pays both goods; the subject only ever receives.

**Honest cost.** A flat price forgoes the revenue available from subjects whose answers are in high demand, which is most of the revenue a conventional market would earn. It also raises a genuine open question this paper does not settle: whether a single global price is regressive across economies, and whether a per-region posted price — a rate attached to a *market*, not to a *person* — is admissible where a per-person price is not. We believe it is, and have not implemented it.

---

## 7 · Claim 4 — the buyer-class exclusion, and why it cannot sit on use

> **Buyers are admitted by class. No buyer whose business is pricing, scoring, ranking, or gating access to a necessity may be admitted, at any price, regardless of what a subject would consent to.**

Necessities means at least: housing, employment, credit, insurance, healthcare, and access to public services.

**The obvious design places the restriction on the use of the answer** — a licence term saying *this answer may not be used to price or rank*. It fails on a mechanical ground: **what a buyer does with a bit is unobservable.** No audit, no telemetry, and no contractual language makes it observable. A guard that cannot be checked is decoration.

**What class of business a buyer is in is observable**, and stays observable. So the guard moves from the act to the party, and it becomes enforceable at the only moment it can be: admission.

**Why consent does not rescue the excluded classes.** A subject facing a landlord who requires an answer is not exercising a preference; the alternative to releasing is not being housed. **Consent obtained under necessity is exactly the mechanism by which a voluntary market becomes a compulsory score** — every such system in history became mandatory by consent, one reasonable transaction at a time. *She chose to release it* is not a defence when the alternative was no apartment.

⚠️ **The exclusion is the largest single cost in this design.** Employment screening, tenant screening, and credit are most of the revenue of the existing identity-verification market. A reader evaluating the commercial claim should assume the addressable market is a fraction of the industry's, and that the fraction is the deliberate part.

---

## 8 · Claim 5 — anti-aggregation, by asker rather than by subject

> **Answers expire; askers are attested and rate-limited; and no enumerable directory of subjects exists.**

An answer that persists is a record, and a buyer who accumulates enough persisting answers has reconstructed the corpus the design refuses to sell — slowly, legitimately, one release at a time. Three properties close that path.

**Answers expire.** A signed answer carries a short validity and is not a durable credential. Re-asking is a fresh transaction requiring a live release, which the subject may by then have withdrawn.

**Askers are attested and rate-limited.** An asker is itself an identified party with an accountable principal, and the number of distinct subjects any asker may query per period is bounded. ⭐ **The distinguishing property is relational and it is checkable: a legitimate buyer asks about the counterparty in front of them; a broker asks about strangers at scale.** The first pattern is bounded by the buyer's own transaction volume; the second is not, and shows up as a rate.

**There is no directory.** Resolution runs one way — from a public artifact to a handle — and never from a handle to the subject's underlying proofs. There is no root view, no browse, no enumerate, and no "explore." **A network of subjects with an entry list is a directory of people**, and a directory is the artifact this design exists to not produce. A caller arrives at a subject because they were given that subject's address by the subject or by a public artifact the subject authored.

**And a consequence for the operator's own analytics: no derived statistic over answers may be computed or published** — no average, no distribution, no per-period totals. An average is a rate, and a rate over answers reconstitutes the gradient the catalogue was designed to exclude.

---

## 9 · The central property, and the condition under which it is true

### 9.1 The claim

**The operator cannot answer alone.** Absent a live release, there is no query the operator can serve, no price at which it can be induced to, and no management decision that changes this. Remove every rule, every policy, and every person of good character from the system, and the guard still holds — which is the test that distinguishes a property from a promise.

### 9.2 The condition, stated plainly because it is the paper's most important limit

**The property is only as strong as the stored form.**

If the operator stores plaintext records and merely declines to release them, then the operator *can* answer and has chosen not to. The honest description of that system is **will not**, and it is an ordinary policy commitment with better marketing.

The property earns the word *cannot* only where the operator's store is a **commitment** rather than a readable record — where the operator can demonstrate that a fact was recorded, and demonstrate when, without being able to reconstruct the fact without the subject's participation. Constructions capable of this are well known and surveyed in §2; we specify the *requirement*, not a choice among them.

**A reader auditing an implementation should therefore ask exactly one question: can the operator produce an answer for a subject who has released nothing?** If yes, the system is a policy system, whatever its documentation says.

### 9.3 The strongest objection to the paper, and our answer

**The objection: selective disclosure already lets a holder refuse, so the market design adds nothing.**

We accept the premise. A holder can already decline to present. What the credential layer does *not* determine is (a) which questions exist to be asked at all, (b) what a question costs and whether that cost varies by person, (c) which parties may be verifiers, and (d) how often any verifier may ask. **Every failure mode this paper is designed against lives in those four, and none of them is a holder's decision.** A system with impeccable selective disclosure and a catalogue containing *total endorsements received*, sold at auction to employment screeners, would satisfy every cryptographic standard cited in §2 and would be a credit bureau.

**The residual force of the objection, which we do not dissolve:** the four rules are rules. They are enforced at admission and at catalogue definition, which is earlier and more checkable than enforcement at use — but they are not cryptographic. Only §9.1's property is. An honest summary is that **one guard in this design is a property and four are rules made checkable**, and a reader should weight them differently.

---

## 10 · Enumerated claims

The following are disclosed and dedicated to the public domain.

1. **A market for facts about a person in which the release capability and the vouching capability are separately owned goods**, sold in the same transaction to the same buyer, with proceeds settling to two different parties and the subject's share not passing through the operator.
2. **A catalogue-admission rule** restricting tradeable attributes to those bounded per person and monotone in time, and excluding attributes monotone in volume, for the purpose of removing the economic incentive to manufacture the underlying activity.
3. **A uniform posted price for an attestation answer**, identical across subjects, with the subject's participation reduced to a binary release, for the purpose of preventing a published valuation of persons.
4. **A prohibition on charging the subject** any fee for enrolment, attestation, or availability, for the purpose of preventing the equation of payment with proof.
5. **Admission of verifiers by business class**, excluding classes whose decisions price, score, rank, or gate a necessity, adopted specifically because the use of an answer is unobservable while the class of the buyer is observable.
6. **Anti-aggregation through expiring answers, attested and rate-limited askers, and one-way resolution with no enumerable directory**, with the asker's ratio of distinct subjects to own transaction volume as the discriminating signal between a counterparty and a broker.
7. **The requirement that the operator's store be a commitment it cannot read out**, as the condition converting the operator's inability to answer from a policy into a structural property.
8. **The composition of 1–7 as a single market design**, in which an institution's refusal to sell personal records is enforced by its inability to answer rather than by its undertaking not to.

⚠️ **What is deliberately not claimed:** the credential formats, signature schemes, disclosure protocols, and commitment constructions of §2, all of which are prior art and none of which we invented.

---

## 11 · Honest limits

**Nothing here is built.** No implementation exists, no query has been served, and the personhood layer the catalogue depends on is specified and published but not deployed. Participation is zero.

**The scope limit, and the test we ran rather than the label we could have applied.** Our publication posture withholds specifications for designs that are complete but unbuilt, on the ground that publishing accelerates a competitor more than it protects us. We ran that test rather than applying it: for a set of **market rules**, publication confers almost no build advantage — anyone can adopt a rule — while non-publication leaves the design patentable by someone else. The test therefore points to full disclosure, and §§4–10 are complete. **What remains undisclosed is implementation detail that would be invented rather than adopted:** query and presentation protocol shapes, key-management and recovery procedure, the specific commitment construction, and the asker-attestation scheme. Those are unbuilt, and specifying them here would be fiction with the authority of a specification.

**Four rules and one property.** §9.3 states this and it belongs in the limits too: only the operator's inability to answer is structural. The catalogue rule, the flat price, the buyer-class exclusion, and the rate limits are rules enforced at definition and admission. They are more checkable than use-restrictions and they are not physics.

**The economics are unvalidated in both directions.** We argue attestation value is per-transaction where data value is aggregate; that argument is untested. If it is wrong, the subject's share is negligible and the design's social claim collapses even if its privacy claim survives.

**The exclusion may not hold under pressure.** §7 excludes the most lucrative buyers. We have no mechanism that prevents a future operator from widening the class list, and we say so rather than implying the exclusion is self-enforcing. It is a rule. Its protection is that it is published, dated, and specific enough that widening it is visible.

**And the hole the design does not close.** Every attribute in the catalogue can be satisfied by real, cooperating people producing genuine records for insincere reasons. Personhood proofs answer *is this a person*; they do not answer *is this genuine*. That is a property of graphs, not of identity, and nothing here addresses it.

---

## 12 · Conclusion, and a lineage

The mechanism is small: separate the release from the vouching, give the release to the subject, and let the operator sell only what is its own. Most of this paper is the consequences — a catalogue that cannot be farmed, a price that cannot rank, a buyer list that can be checked, and answers that do not accumulate into the thing they were meant to replace.

The reason to prefer this shape to a policy is stated once more because it is the whole motivation: **an institution built to outlive the people who founded it cannot rest its most important refusals on anyone's restraint.** A rule needs a living enforcer with the right incentives at the moment it is tested, and that is the moment no one can guarantee. A design in which the prohibited act is unavailable needs no one.

The lineage is the preamble's: a claim about a person travels with the name of who released it and who vouched for it, and those remain two parties. **The convention does not make the claim true. It makes the chain visible** — which is all any of this does, and is more than a promise can do.

---

## Author Contributions and AI Disclosure

Framework, rulings, and editorial control: **Thon Ly**. Drafting, structural analysis, prior-art survey, and the adversarial pass that produced §9.2's condition and §9.3's objection: **Miss Aquarius℠**, the institution's named AI collaborator. The underlying models are not named, by standing policy; the collaboration is disclosed under one consistent name across every venue.

## Trademark Notice

HeartBank® is a registered mark. B-Vouch℠ — the service that implements this design — and Miss Aquarius℠ are service marks of the institution. **This paper describes the mechanism, which is dedicated to the public domain; the marks are not licensed by this dedication.**
