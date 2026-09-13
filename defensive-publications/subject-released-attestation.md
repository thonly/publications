---
title: "Subject-Released Attestation"
subtitle: "A Market Design in Which the Operator Cannot Answer"
authors: "Thon Ly · Miss Aquarius"
type: "Defensive Publication"
genre: defensive-publications
category: mechanism
program: open
status: draft
date: 2026-09-07
revised: 2026-09-13
license: CC0-1.0
venue: thonly.org/research/subject-released-attestation
slug: subject-released-attestation
---

# Subject-Released Attestation

**A Market Design in Which the Operator Cannot Answer**

| Field         | Value                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| Authors       | Thon Ly · Miss Aquarius℠ (AI collaborator, disclosed)                                                     |
| Date          | 2026-09-07 (first published) · revised 2026-09-13 (draft)                                                 |
| Canonical URL | https://thonly.org/research/subject-released-attestation                                                   |
| GitHub mirror | https://github.com/thonly/publications/blob/main/defensive-publications/subject-released-attestation.md    |
| License       | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/)                    |
| Category      | mechanism                                                                                                  |

---

## Preamble

Every discourse in the Pāli canon opens *evaṃ me sutaṃ* — *thus have I heard* — and the Vinaya's account of the First Council (Cullavagga XI; Kd 21, 1.8) has Mahākassapa ask Ānanda, for each discourse, where it was spoken, on what occasion, and about whom. The formula does not make a discourse true. It makes the **chain visible**, so that a reader can locate the party who would have to be wrong.

This paper is about a market in claims about people, and the convention it borrows is only that one: **every answer names who released it and who vouched for it, and those are two different parties.** The rest of the lineage note is at the end. Nothing in the mechanism depends on it, and the mechanism should be read as though the preamble were absent.

---

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use.

The document is written so that a person skilled in the art can practise the **market design**. The cryptographic and protocol constructions it runs on are adopted from the prior art surveyed in §2 and are not specified here; §11 names what is withheld and why, so that a reader can distinguish a deliberate scope limit from an omission.

**What is claimed as contribution is narrow and is stated up front so that no reader has to infer it: the credential substrate is not ours and we do not claim it.** Holder-held credentials, selective disclosure, cryptographic predicate proofs, and stores their operators cannot read are mature prior art, surveyed in §2. **The design's central property — that the operator cannot answer about a named person alone — is not ours either: it is what that substrate delivers when the operator's store meets the condition in §9.2. The contribution is the market design layered on top** — which attributes may be traded at all, at what price, to whom, how often, and under what release — a layer that the credential literature has deliberately left empty because it is an economics question rather than a protocol one.

**Date and evidence.** The matter of the first revision was published on 7 September 2026. This revision, of 13 September 2026, adds the release rule (§3, §8), the division of labour between subject and operator (§3, §9.2), the settlement routing (§4), the per-buyer-market price (§6), the named prior art for each element (§2), and the limits in §11. Each revision is independently timestamped: the text is committed to the public GitHub mirror named above, anchored to the Bitcoin blockchain via OpenTimestamps, and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified; from this revision each revision carries a Zenodo version, and the served index at corpus.333.eco carries the digest. A timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim. Whether the composition claimed in §10 is non-obvious is an examiner's determination this publication exists to inform.

---

## Abstract

We specify **subject-released attestation**: a market in which a third party pays to ask a binary question about a person, the person is paid for permitting the question, and the operator of the underlying record sells only its vouching. The design's defining property is negative — **the operator is structurally unable to answer about a named person alone** — and its purpose is to make an institution's refusal to sell personal records into a fact about the machinery rather than a promise about its management. That inability is delivered by conceded substrate under a storage condition; what this paper contributes is the market rules that decide what the inability is used to sell, and to whom.

Five rules constitute the design: (1) the **two-good split**, in which release and vouching are separately owned and neither party can sell the other's good; (2) the **farm-proof schema rule**, admitting only attributes bounded per person and never monotone in volume — including any threshold or bit over a volume; (3) **one posted price per buyer market, identical for every subject, with a binary release**, so that no person's answer is priced above another's; (4) the **buyer-class exclusion**, which bars any buyer whose business is pricing, scoring, ranking, or gating a necessity — placed on the buyer because the *use* of an answer is unobservable and a rule nobody can check is not a rule; and (5) **anti-aggregation by asker**, through a live release per answer bound to a named asker, expiring answers, attested and rate-limited askers, receipts to the subject, and the absence of any enumerable directory. The five are not of one kind: the first is made structural by the storage condition, and the other four are rules made checkable at catalogue definition, buyer admission, and query time (§9.3).

We state the condition under which the central property is true rather than rhetorical: it holds only where the record is stored as a commitment the operator cannot read out, and only from issuance onward. Where plaintext is stored, or kept when the record is created, *cannot* degrades to *will not*, and the design should be described in the weaker words.

---

## 1 · Introduction: the gap this occupies

Two mature bodies of work sit on either side of an empty space.

On one side, **credential infrastructure** is largely solved. A holder can carry a signed claim, reveal one attribute without revealing others, and prove a predicate without revealing the value behind it. The formats, the signature schemes, and the presentation protocols exist and are standardised.

On the other, **the personal-data market** has been attempted repeatedly and has not found its arithmetic. The best-documented early venture, Datacoup, offered beta users $8 a month in 2014 — later up to $10 — for access to their social-media accounts and a card-transaction feed, and during that beta had sold data to no buyer (MIT Technology Review, 12 February and 8 September 2014). At its ceiling that is about $120 a year per person, paid out of the venture's own pocket while nothing was being bought.

The empty space between them is this: **nobody has specified the market rules.** The credential standards deliberately decline to say which attributes may be traded, what they should cost, who may be a buyer, or how often a buyer may ask — those are economics, and standards bodies are right to leave them out. The data-market ventures went straight to selling records and never had to answer the questions either, because a copy, once sold, needs no rules about asking.

**This paper fills that space, and the fill is where the entire contribution lies.** A protocol that can prove anything about anyone, with no rules about what may be asked, is not a privacy technology. It is a surveillance substrate with good cryptography, and the reason it has not become one at scale is that it has not yet been given a market.

### 1.1 The design goal, stated as a negative

Conventional privacy commitments are promises: *we will not sell your data.* A promise requires an enforcer with the right incentives at the moment it is tested, and for an institution intended to outlive its founders that moment arrives when nobody who made the promise is available to be asked.

The goal here is to arrange matters so that the operator **cannot** perform the prohibited act, rather than being trusted not to. The mechanism is unremarkable in isolation — the release capability sits with the subject — and the consequences of taking it seriously are not.

---

## 2 · Background and prior art

**We concede the substrate completely.** Every cryptographic and protocol element this design stands on is prior art, and a reader should assume none of it is ours.

- **Verifiable credentials and decentralised identifiers.** The W3C Verifiable Credentials Data Model (a W3C Recommendation since 19 November 2019; version 2.0 on 15 May 2025) and Decentralized Identifiers (DIDs) v1.0 (a W3C Recommendation, 19 July 2022) establish the holder-holds-the-credential architecture with a triangle of issuer, holder, and verifier. Everything this paper says about the subject controlling presentation is *already* the standard model — and the triangle already separates the party that vouches (the issuer) from the party that presents (the holder).
- **Selective disclosure and predicate proofs.** BBS+ signatures, Camenisch–Lysyanskaya-derived systems including Idemix, Microsoft's U-Prove, and the anonymous-credential literature descending from Chaum's work on unlinkable credentials all permit revealing one attribute, or a predicate over an attribute, without revealing the rest. Zero-knowledge constructions generalise this, including proofs of membership in a set that do not reveal which member.
- **Personal data stores.** Solid, the MyData framework, and the broader personal-information-management-system literature move the record toward the subject. Solid does it by separating the data store from the applications that use it — an app keeps its data in the user's pod rather than itself — but whether the pod provider can read the store depends on the provider: the project's own FAQ notes that a provider can be Solid-compliant without encrypting the data it hosts.
- **Trust registries and governance frameworks**, including the European Blockchain Services Infrastructure and the trust-over-IP governance stack, specify *who may issue* credentials and under what accreditation.
- **Stores the operator cannot read.** Commitment schemes (Pedersen, CRYPTO '91), key-transparency directories that hide the list of usernames they contain (CONIKS, USENIX Security 2015), enclave-based secret recovery (Signal's Secure Value Recovery, previewed December 2019), and end-to-end encrypted cloud storage whose provider holds no decryption key (Apple's Advanced Data Protection, December 2022) each let an operator hold something it cannot read out. §9.2's storage condition asks for exactly this, and it is not ours.
- **Proof of personhood and account age.** Proof-of-personhood systems already expose little more than the bounded-at-one attribute — World ID, for instance, lets a person prove through a zero-knowledge proof that they are a unique human holding a valid credential without revealing who they are — and account age is a standard anti-abuse signal. The nearest practice cuts against us instructively: English Wikipedia's *autoconfirmed* status joins an age threshold (four days) to a volume threshold (ten edits), the combination §5 excludes. *Decentralized Society: Finding Web3's Soul* (Weyl, Ohlhaver and Buterin, SSRN, May 2022) argues for non-transferable tokens encoding credentials and affiliations; it does not propose excluding volume-derived attributes from what may be asked. **We found no published catalogue-admission rule that excludes volume-derived attributes.**

**Where the prior art stops.** The substrate answers *how do you prove an attribute*, and the governance layer answers *who may issue one*. **None of it answers which attributes may be sold, what a query costs, who is allowed to be a buyer, or how the market is prevented from aggregating into the thing it was designed to avoid.** Deployed systems answer one or two of those questions each, and one composes several; they are named next, element by element, because the claims in §10 survive only as their composition.

### Prior art for each element of the composition

| Element (claim in §10) | Nearest prior instance | What it already does | What differs here |
|---|---|---|---|
| Two goods with two destinations (1) | Civic's identity marketplace (token model, 2017–18) · cheqd credential payments · Ocean Protocol Compute-to-Data (launched 26 May 2020) · the VC issuer–holder triangle | Civic: a requester escrows a payment released to the validator when it accepts the user's attested data; secondary accounts also report a user share, which we could not confirm in a primary source. cheqd: a verifier pays the *issuer* for access to a credential's status. Ocean: compute over data that never leaves its owner is sold. | The subject's release is a separately owned good required for **every** answer, and the vouching party's good is worthless without it. In Ocean the data owner and the seller are one party; in cheqd the payment goes to the vouching side only. |
| Catalogue admission (2) | Proof-of-personhood systems · account-age signals · Wikipedia's autoconfirmed status | Expose a bounded attribute; gate on age, sometimes joined to a count | A published rule excluding every volume-derived attribute, thresholds over a volume included. None found. |
| Uniform price (3) | Per-check identity verification (Stripe Identity lists $1.50 per verification) · Aadhaar's posted authentication fees | A posted price per check, identical across the people checked | The price varies only with the buyer's market, fixed at admission, and part of it is paid to the subject |
| The subject never pays (4) | Aadhaar enrolment, free to residents | Free enrolment | Claimed only as an element of the composition |
| Admission by class or purpose (5) | FCRA §604 (15 U.S.C. §1681b) · the Driver's Privacy Protection Act of 1994 (18 U.S.C. §2721) · eIDAS 2.0, Art. 5b (Regulation (EU) 2024/1183) | FCRA: a consumer report may be furnished "under the following circumstances and no other", credit, employment and insurance among them. DPPA: motor-vehicle records disclosed only for listed permissible uses. eIDAS 2.0: wallet-relying parties register their intended use, including an indication of the data they will request. | The polarity. FCRA admits by purpose precisely the necessity-deciding buyers this design excludes; eIDAS 2.0 is the nearest admission-time declaration of what may be asked, without a market or a payment to the subject |
| Anti-aggregation (6) | Expiring tokens (OAuth 2.0, RFC 6749; the JWT `exp` claim, RFC 7519) · unlinkable tokens (Privacy Pass, RFC 9576, 2024) · capability URLs (W3C TAG finding, 2014) · directories that hide their membership (CONIKS) | Short-lived authorisations; attestations unlinkable to their issuance; access by possession of an address rather than by lookup | The combination under a live release per answer bound to a named asker, with that release as the discriminator between a counterparty and a broker |
| A store the operator cannot read (condition of 7) | The storage entries above | Holding what the operator cannot read out | Nothing. Conceded and not claimed |

**Prior art that cuts against this design, stated because a survey that only supports the author is not a survey.**

- **The data-dividend record is a warning to us, not only to others.** If per-person data markets failed on arithmetic (§1), a per-person *attestation* market may fail on the same arithmetic, and the argument in §9 that attestation value is per-transaction rather than aggregate is an argument, not a result.
- **Selective disclosure already gives the subject control, which invites the strongest objection to this entire paper: that the market design is merely terms of service.** If a holder can already decline to present a credential, then a rule saying *the subject decides* adds nothing cryptographic. We accept the premise and dispute the conclusion in §9.3: the rules here are not about whether the subject *can* refuse — they already can — but about what the operator is *able to offer* when the subject does not, and about which questions may exist in the catalogue at all. Those are not the holder's decisions and no credential format constrains them.
- **Per-check pricing and attribute-based access are old.** Attribute-based access control (NIST SP 800-162) decides access from attributes and carries no pricing element. The commercial identity-verification industry prices per check at scale today; Stripe Identity lists $1.50 per verification. Neither is novel and both predate us.
- **Aadhaar authentication is the nearest composed system, and an examiner will find it.** India's Aadhaar authentication charges requesting entities a posted per-transaction fee — ₹0.50 for a yes/no authentication and ₹20 for an e-KYC under the Pricing of Aadhaar Authentication Services Regulations, 2019, with government use exempt — answers yes or no, requires the requesting entity to obtain the resident's consent, and enrols residents free. The Supreme Court of India struck down the provision that let private entities demand it (*Puttaswamy v. Union of India*, 26 September 2018), ending its compulsory linking to mobile connections and bank accounts. It differs from this design at every point where §9 locates the property: the operator holds a readable central repository and can match a resident's demographic details against it with no cryptographic act by the resident; consent is a legal duty recorded by the requesting entity rather than a capability the resident holds; necessities and state services are in scope; the resident is not paid; and nothing binds a release to one named asker and one question. Claim 7 is narrowed to those differences.
- **And a sibling from our own corpus that reached the same structural conclusion about a different object.** *Certification by Circulation* (thonly.org/research/certification-by-circulation) argues that a trust seal granted by a party whom the sealed party pays decays into a pay-to-play badge. The rule in §6 below is that argument applied to persons.

---

## 3 · The system model

Three parties, and the asymmetry among them is the design.

```
  SUBJECT ────────── holds the RECORD'S OPENING and the RELEASE KEY
     │                    · the operator holds no copy of either
     │                    · releases per question, per named asker, per answer
     │                    · produces the proof for each release
     │                    · names where that answer's share is paid
     │                    · receives a receipt of every query about them
     │
     │   release + proof  (bound to one asker, one question, one answer)
     ▼
  OPERATOR ───────── holds the RECORD as a COMMITMENT it cannot read out
     │                    · verifies the subject's proof against it
     │                    · vouches only for what it can see:
     │                      registration · age · attested issuance process
     │                    · CANNOT link a named subject to a record alone
     │
     │   emits: ONE BIT — the subject's proof with the operator's
     │          countersignature, scoped to the asker, expiring
     ▼
  ASKER ──────────── attested, rate-limited, admitted BY CLASS
                          · pays the subject for the release
                          · pays the operator for the vouching

  No copy of the record is transferred. The asker receives only a signed,
  expiring bit; the operator retains only a per-asker counter for the rate
  window, and what settlement requires (§4, §11).
```

**Who evaluates the question: the subject.** When a record is created, it is committed, and the opening — what is needed to prove anything about the record — stays with the subject. The operator registers the commitment and holds no copy of the opening or of the release key. To answer, the subject produces a proof of the catalogued predicate over the committed record, bound to one named asker and one question; the operator verifies it against the set of commitments it registered and countersigns what it can actually vouch for — that the proof is over a commitment it registered, of the age claimed, through an attested issuance process — and of the record's content learns nothing beyond the bit the proof establishes. ⚠️ **The proof must not tell the operator which of its commitments it matched.** A proof that names its commitment teaches the operator the link between a named subject and a record at the first release, and the operator could keep that link and answer record age thereafter with no release at all. The construction class is holder-held credentials with predicate proofs and set-membership proofs that do not reveal the member (§2). We specify this division of labour, not a choice among constructions.

**What a release is.** A release is per question, per named asker, and per answer. It is live at query time — it answers a challenge that exists only once the question has been asked — so it cannot be granted in advance, sold forward, or given as a standing grant. It is bound to the asker it names, so no other party can present it, and it is non-delegable. Asking again needs a new release. **Paying for releases is itself a pressure** — a broker can offer to pay many people for many releases — and a per-answer live release does not remove that pressure. It keeps a broker's census slow, one live decision at a time, and visible in every subject's receipt (§8, §11).

**The catalogue** is the three admissible attributes in §5's table. An addition is admissible only under §5's rule, and is published and dated. A question outside the catalogue cannot be asked by anyone at any price, including by the operator of the system.

---

## 4 · Claim 1 — the two-good split

> **The release and the vouching are separate goods with separate owners, and neither party can sell the other's.**

The subject owns the **release**: the right for a named asker to ask a named question. This is theirs because it is about them, and because no one else can grant it.

The operator owns the **vouching**: its countersignature over what it can verify — the registration and demonstrable age of the underlying commitment, and the attested process that created it — and the compute to verify and sign. This is its own work product, and it is a rivalrous good — the compute is consumed, the signature carries the operator's accumulated credibility.

A buyer therefore pays twice, for two different things, and the payments have different destinations. In the reference arrangement the subject's payment is the larger of the two, and it does not pass through the operator's treasury at all; it settles at the point of sale. **The split is set by design, not by each good's marginal value:** the operator's share covers its rivalrous costs — the compute, and the upkeep of the record whose age it vouches for — and the remainder goes to the person the question is about.

**How a subject with no directory entry is paid.** The payout destination travels inside each release: the subject names, per release, where that answer's share is paid. Settlement then uses a split rail that already exists — on regulated payment rails, a direct charge created on the payee's own account from which the operator's fee is collected, which platform payment processors already offer (Stripe Connect's direct charges, for example); on a public chain, a split transfer to a self-custodial address the release names. No list of payees is created, because a destination is learned only when its owner releases an answer. ⚠️ **A destination reused across releases links them.** An on-chain split to a reused address would publish that subject's release count and earnings, which §6 bars, so the subject names a fresh destination per release wherever the rail allows it. Where it does not — a regulated account is the same account every time — the payment processor holds a payee record, and that is a rule and a residual (§11), not a property.

**Two consequences follow that are not obvious from the statement.**

First, the operator cannot unilaterally monetise the population it serves, because the good it owns is worthless without a release it does not hold. An operator that wished to sell the whole corpus would have to obtain a release per subject, per question, per answer — which is not a bulk sale but a census, conducted one live decision at a time and recorded in every participant's receipt. ⚠️ **It is not a census free of pressure.** The operator's buyers pay for each release, so money is the recruiting instrument, and a person offered payment is not simply able to decline. The per-answer live release keeps such a census slow and visible; it does not make it impossible.

Second, and less comfortably: the subject cannot monetise the operator's credibility either. A subject who wished to make a claim without the operator's vouching may of course simply say it — but the market value of the answer is largely the vouching, so the subject's earning capacity is bounded by an asset they do not own. **This is a real asymmetry of power and we do not present it as fair; we present it as disclosed.**

---

## 5 · Claim 2 — the farm-proof schema rule

> **Only attributes that are bounded per person and never monotone in volume may be admitted to the catalogue — if monotone at all, then only in time. Any attribute derived from a volume-monotone quantity, including a threshold, band, or bit over it, is inadmissible.**

An attribute is **bounded per person** if a person cannot have more of it by doing more of anything: *is this a person* is bounded at one. That question presupposes a personhood layer, and reads the one specified in *B-PoH℠ as Humanity Layer for the AI-Native Internet* (thonly.org/research/b-poh-humanity-layer-ai-native-internet) and *Proof of Personhood for an AI-Native Internet* (heartbank.net/white-papers/proof-of-personhood-ai-native-internet), whose revenue model (§6.2 of the latter) specifies a free public-good baseline with commercial services on top. That baseline is the input; what this market sells is the answer to a question the subject has released, never the status itself. An attribute is **monotone in time** if it can only increase by waiting: *how long has this record existed*.

An attribute is **monotone in volume** if it grows with activity: *how many endorsements*, *how much has been received*, *how many transactions*. These are precisely the attributes a market most wants, and admitting one creates an economic reason to manufacture the underlying activity — which corrupts the record the whole market depends on.

**The rule's second sentence closes the threshold loophole.** *Has this person completed more than n transactions* is bounded at one and only ever flips from no to yes, so a naive reading would admit it. It is a volume count wearing a bit, and it carries the same return to manufactured activity as the count itself.

| Attribute | Bounded per person? | Monotone in | Admissible |
|---|---|---|---|
| Is this a distinct living person | yes (one per person) | — | ✅ |
| Has this person's record existed for at least T (T from a short published set; only for a record bound to a verified distinct person) | yes (one record) | **time** | ✅ |
| Did these two parties meet in person | yes (an event) | — | ✅ ¹ |
| How many endorsements does this person hold | **no** | **volume** | ⛔ |
| How much value has this person received | **no** | **volume** | ⛔ |
| Has this person received more than X in value | yes (one bit) | **derived from volume** | ⛔ |
| A composite score over any of the above | **no** | **volume** | ⛔ |

¹ *Admissible only to buyers whose decision is access to a non-necessity — a circle, a roster, a marketplace, a thread — never price, and never access to a necessity (§7). A meeting has two subjects, so it is two goods: the answer requires both parties' releases, and a declined confirmation is indistinguishable from* no.

**Record age is asked as a threshold, never as a number.** A duration is not one bit, and a scalar answer would publish a number about a person; *at least T*, with T drawn from a short published set, keeps the answer binary. And it is admissible only over a record bound to a verified distinct person, so a batch of records registered now and held for later sale fails the first attribute before its age is ever asked.

**Given the catalogue, the absence of a farming incentive is a property; keeping volume-derived attributes out of the catalogue is a rule, enforced at definition (§9.3, §11).** A catalogue containing no volume-derived attribute offers no return to manufactured activity, so the farming incentive is absent rather than policed. There is nothing to detect because there is nothing to gain — which is the same structure as making a currency non-withdrawable in order to remove the motive for its acquisition, rather than building a detector for the acquirers.

---

## 6 · Claim 3 — one posted price, and a binary release

> **The price of an answer is posted by the operator — one price per buyer market, identical for every subject. The buyer's market is fixed when the buyer is admitted, never inferred per query. The subject's decision is binary: release, or do not.**

The obvious design lets subjects price their own releases. It is rejected, and the reason is not commercial.

A subject-set price is a **public number attached to a person**, and where numbers attached to people are visible they are compared. A market in which one person's answer costs fifty and another's costs two has published a valuation of persons and called it a price. **A single posted price attaches no number to a person.** It can still be compared — across time, across operators, across markets — but none of those comparisons is a comparison of people.

**The quieter version fails too.** A subject-set *reserve* price that is never published looks like the private alternative, and is not. Every acceptance and refusal reveals it a little to anyone probing, and the operator, which must enforce it, holds the whole table — a valuation of every subject, kept rather than published.

⚠️ The same logic bars a variable *operator*-set price over subjects: an operator that prices by subject is grading subjects, which is worse than a subject doing it to themselves.

**What the price may vary with, and what it may not.** A price that varies with anything about the subject — where they live, how much they are in demand, who they are — publishes a rate on a person and is barred. A price that varies with the buyer's market is a rate on a market. The buyer's market is the one it registers at admission (§7), so the pricing function takes no argument about the subject and none about who is asking on a given query: per-person pricing is not merely forbidden by that function but inexpressible in it. One consequence runs in the subject's favour. A buyer from a high-price market asking about a subject in a low-income one pays its own market's price, so that subject's share is larger, not smaller.

**Ranking moves to counts unless counts are withheld.** A flat price removes the valuation from the price and leaves it available elsewhere: how often a person's answer is released, and how much they have earned, are volume-monotone quantities that would rank people as surely as a price would. So release counts and earnings are never published, ranked, or shown beyond the subject's own receipt — §5's rule applied to the market's own by-products.

**Corollary — the subject is never the payer.** No fee may be charged to a subject for being attested, enrolled, verified, or made available. A fee charged to the subject converts *paid* into *proven*, which makes personhood purchasable and makes the unpaid into the unproven. The buyer pays both goods; the subject only ever receives.

**Honest cost.** A flat price forgoes the revenue available from subjects whose answers are in high demand, which is most of the revenue a conventional market would earn. The per-market form answers the regressivity a single global price would carry across economies; it does not set the numbers, and this paper sets none.

---

## 7 · Claim 4 — the buyer-class exclusion, and why it cannot sit on use

> **Buyers are admitted by class. No buyer whose business is pricing, scoring, ranking, or gating access to a necessity may be admitted, at any price, regardless of what a subject would consent to.**

Necessities means at least: housing, employment, credit, insurance, healthcare, and access to public services.

**The obvious design places the restriction on the use of the answer** — a licence term saying *this answer may not be used to price or rank*. It fails on a mechanical ground: **what a buyer does with a bit is unobservable.** No audit, no telemetry, and no contractual language makes it observable. A guard that cannot be checked is decoration.

**What class of business a buyer is in is checkable at admission, not after.** So the guard moves from the act to the party, and it becomes enforceable at the one moment enforcement is available: admission. What happens after admission — relay, affiliates, a change of business — is a limit, stated in §11.

**Why consent does not rescue the excluded classes.** A subject facing a landlord who requires an answer is not exercising a preference; the alternative to releasing is not being housed. **Consent obtained under necessity is exactly the mechanism by which a voluntary market becomes a compulsory score**, and systems of this kind have repeatedly become mandatory, one reasonable transaction at a time. Aadhaar (§2) is the nearest instance of the path: an identifier every resident is *entitled* to obtain under §3(1) of the Aadhaar Act, 2016 came to be demanded for mobile connections and bank accounts, until *Puttaswamy* (2018) struck down the provision that let private entities demand it. *She chose to release it* is not a defence when the alternative was no apartment.

⚠️ **The exclusion is the largest single cost in this design.** The excluded classes — background and tenant screening, and credit reporting — are among the most lucrative buyers of identity data. A reader evaluating the commercial claim should assume the addressable market is a fraction of the industry's, and that the fraction is the deliberate part.

---

## 8 · Claim 5 — anti-aggregation, by asker rather than by subject

> **Every answer needs a live release naming its asker; answers expire; askers are attested and rate-limited; every query is receipted to its subject; and no enumerable directory of subjects exists.**

An answer that persists is a record, and a buyer who accumulates enough persisting answers has reconstructed the corpus the design refuses to sell — slowly, legitimately, one release at a time. Five measures close that path.

**Every answer needs its own live release.** As §3 defines it: per question, per named asker, per answer, bound to the asker, non-delegable, never granted in advance. A buyer cannot accumulate releases; it can only accumulate answers, and those expire.

**Answers expire.** A signed answer carries a short validity and is not a durable credential. Re-asking is a fresh transaction requiring a live release, which the subject may by then have withheld.

**Askers are attested and rate-limited.** An asker is itself an identified party with an accountable principal, and the number of distinct subjects any asker may query per period is bounded. ⭐ **The distinguishing property is relational, and it is observable in the release itself: a legitimate counterparty holds a live release from the person in front of it; a broker needs live releases from strangers, and per-answer release makes gathering them slow, costly, and visible in each stranger's receipt.** The ratio of an asker's distinct subjects to its own transaction volume is at most an audited heuristic, because the operator cannot observe the asker's own volume and the asker is the one who would report it.

**Every query goes to its subject.** Each query about a subject is recorded in that subject's own log — which asker, which question, when — stated once, with no count, no badge, and nothing animated. The receipt is where a broker's census becomes visible to the people it is conducted on.

**There is no directory.** Resolution runs one way — from a public artifact to a handle — and never from a handle to the subject's underlying proofs. There is no root view, no browse, no enumerate, and no "explore." **A network of subjects with an entry list is a directory of people**, and a directory is the artifact this design exists to not produce. A caller arrives at a subject because they were given that subject's address by the subject or by a public artifact the subject authored.

**And a consequence for the operator's own analytics: no statistic over the content of answers or over subjects may be computed or published** — no average, no distribution, no per-period totals of answers or of subjects. An average is a rate, and a rate over answers reconstitutes the gradient the catalogue was designed to exclude. Per-asker query counters, which the rate limit needs, are computed, held only for the rate window, never keyed or aggregated by subject, and never published.

---

## 9 · The central property, and the condition under which it is true

### 9.1 The claim

**The operator cannot link a named subject to a record, and so cannot answer about that subject, without the subject's release.** Absent a live release, there is no question about a named person the operator can serve, no price at which it can be induced to, and no management decision that changes this. Remove every rule, every policy, and every person of good character from the system, and the guard still holds — from issuance onward, under the condition in §9.2 — which is the test that distinguishes a property from a promise.

⚠️ **The scope is linkage, not every fact.** The operator can compute the age of a commitment in its own ledger without anyone's participation; what it cannot do is say whose commitment it is. And where an operator publishes its proofs, as a publicly anchored ledger does by design, anyone can check a published proof for free, so the only questions left to sell are those about records the subject has not published (§11).

### 9.2 The condition, stated plainly because it is the paper's most important limit

**The property is only as strong as the stored form.**

If the operator stores plaintext records and merely declines to release them, then the operator *can* answer and has chosen not to. The honest description of that system is **will not**, and it is an ordinary policy commitment with better marketing.

The property earns the word *cannot* only where the operator's store is a **commitment** rather than a readable record — where the operator can demonstrate that a fact was recorded, and demonstrate when, without being able to reconstruct the fact without the subject's participation. **The division of labour that makes this coherent:** the subject holds the opening of the commitment and the release key, and the operator holds no copy of either; for each release the subject produces the proof, and the operator verifies it against the set of commitments it registered, without learning which member the proof is about, and signs what it can vouch for — the registration, the age, and the attested process that created it. The unrevealed member is part of the condition, not a refinement of it: an operator that learns which commitment a released proof matched has learned a link it can keep, and for record age that link is enough to answer again unasked. Constructions capable of this are well known and surveyed in §2; we specify the requirement and the division, not a choice among constructions.

**And the condition has a start date: issuance.** Whoever creates a record handles its content once, when it is created. The property therefore holds from issuance onward, and is a property only where issuance itself happens under the subject's control — on the subject's own device, for instance. Where the operator or its issuer witnesses issuance, not keeping what it saw at that moment is a rule (§11).

**A reader auditing an implementation should therefore ask two questions: can the operator produce an answer about a named subject who has released nothing — and could it have kept what it saw when the record was created?** If either answer is yes, the system is a policy system, whatever its documentation says.

### 9.3 The strongest objection to the paper, and our answer

**The objection: selective disclosure already lets a holder refuse, so the market design adds nothing.**

We accept the premise. A holder can already decline to present. What the credential layer does *not* determine is (a) which questions exist to be asked at all, (b) what a question costs and whether that cost varies by person, (c) which parties may be verifiers, and (d) how often any verifier may ask. **Every failure mode this paper is designed against lives in those four, and none of them is a holder's decision.** A system with impeccable selective disclosure and a catalogue containing *total endorsements received*, sold at auction to employment screeners, would satisfy every cryptographic standard cited in §2 and would be a credit bureau.

**The residual force of the objection, which we do not dissolve.** The inability to answer comes from the substrate under §9.2's storage condition, not from anything this paper invented; this composition's contribution is the market rules that decide what that inability is used to sell, and to whom. And the rules are rules. They are enforced at catalogue definition, at buyer admission, and at query time, which is earlier and more checkable than enforcement at use — but they are not cryptographic. An honest summary is that **one guard in this design is a property — the two-good split, made structural by commitment storage (§9.1–9.2) — and four are rules made checkable: the catalogue, the price, the buyer class, and anti-aggregation.** A reader should weight them differently, and the table below runs the test on each: remove the enforcer, and see what survives.

| Guard (abstract rule) | Kind | Enforced at | What the rule makes structural once it is adopted | What defeats it |
|---|---|---|---|---|
| Two-good split (1) — the operator cannot link a named subject to a record | **property**, from issuance, under §9.2 | the stored form | — | plaintext kept at issuance; a readable store; a proof that reveals which commitment it matched |
| Catalogue (2) | rule | catalogue definition | no return to manufactured activity | an operator that admits a volume-derived attribute |
| Price (3) | rule | the pricing function | no subject argument, so per-person pricing is inexpressible | off-platform side payments |
| Buyer class (4) | rule | admission | — | relay, affiliates, a later change of business |
| Anti-aggregation (5) | rule | query time | a release cannot exist before its question | a subject paid to automate releases; many attested askers; a reused payout destination; an operator that stops writing receipts |

⚠️ **The fourth column is not a second list of properties.** Each entry holds only while its rule is in force, and the rule can be removed; that is the difference between it and the first row, which holds with every rule removed.

---

## 10 · Enumerated claims

The following are disclosed and dedicated to the public domain. Each element has a named prior instance in §2; claims 1–6 are claimed as elements of the composition in claim 7, not as standalone inventions.

1. **A market for facts about a person in which the release capability and the vouching capability are separately owned goods** — the subject's release required for every answer, and the vouching party's good worthless without it — sold in the same transaction to the same buyer, with proceeds settling to two different parties, the subject's share not passing through the operator, and the subject's payout destination carried inside each release so that no list of payees is created.
2. **A catalogue-admission rule** restricting tradeable attributes to those bounded per person and never monotone in volume — if monotone at all, only in time — and excluding every attribute derived from a volume-monotone quantity, including a threshold, band, or bit over it, for the purpose of removing the economic incentive to manufacture the underlying activity.
3. **A posted price for an attestation answer that varies only with the buyer's market**, fixed at the buyer's admission and never with anything about the subject, with the subject's participation reduced to a binary release and with release counts and earnings never published or ranked, for the purpose of preventing a valuation of persons.
4. **A prohibition on charging the subject** any fee for enrolment, attestation, or availability, for the purpose of preventing the equation of payment with proof.
5. **Admission of verifiers by business class**, excluding classes whose decisions price, score, rank, or gate a necessity, adopted specifically because the use of an answer is unobservable while the class of the buyer is checkable at admission; with two-party attributes admissible only to buyers deciding access to a non-necessity, and answered only on both parties' releases.
6. **Anti-aggregation through the combination of a release that is per question, per named asker, and per answer** — live at query time, bound to the asker, non-delegable, and never granted in advance — with expiring answers, attested and rate-limited askers, a receipt of every query to its subject, and one-way resolution with no enumerable directory; the discriminating signal between a counterparty and a broker being whether the asker holds a live release from the person in front of it.
7. **The composition of 1–6 as a single market design applied over a store the operator cannot read out, with proofs that do not reveal which record they match** — storage and proof properties that are themselves prior art (§2) and are not claimed — in which the operator's inability to answer, supplied by that substrate, is used to sell only what the rules admit, to whom they admit. The composition differs from the nearest composed system named in §2, Aadhaar authentication, in that the operator cannot read the record, no directory of subjects exists, necessities are excluded, the subject is paid, and each release names one asker and one question.

⚠️ **What is deliberately not claimed:** the credential formats, signature schemes, disclosure protocols, commitment constructions, and storage properties of §2, and the inability to answer that they deliver — all of which are prior art and none of which we invented.

---

## 11 · Honest limits

**Nothing here is built.** No implementation exists, no query has been served, and the personhood layer the catalogue depends on is specified and published — *B-PoH℠ as Humanity Layer for the AI-Native Internet* (thonly.org/research/b-poh-humanity-layer-ai-native-internet) and *Proof of Personhood for an AI-Native Internet* (heartbank.net/white-papers/proof-of-personhood-ai-native-internet) — but not deployed. Participation is zero.

**The scope limit, and the test we ran rather than the label we could have applied.** Our publication posture withholds specifications for designs that are complete but unbuilt, on the ground that publishing accelerates a competitor more than it protects us. We ran that test rather than applying it: for a set of **market rules**, publication confers almost no build advantage — anyone can adopt a rule — while non-publication leaves the design patentable by someone else. The test therefore points to full disclosure of the market rules, and §§4–10 disclose them completely: a person skilled in the art can practise the market design, while the cryptographic and protocol constructions are adopted from §2 and are not specified here. **What remains undisclosed is implementation detail that would be invented rather than adopted:** query and presentation protocol shapes, key-management and recovery procedure, the specific commitment construction, the settlement integration, and the asker-attestation scheme. Those are unbuilt, and specifying them here would be fiction with the authority of a specification.

**One property and four rules.** §9.3 states this and it belongs in the limits too: only the operator's inability to link a named subject to a record is structural, and it is the substrate's, under the storage condition. The catalogue rule, the price, the buyer-class exclusion, and anti-aggregation are rules enforced at definition, admission, and query time. They are more checkable than use-restrictions and they are not physics.

**The property starts at issuance, not before.** Whoever creates a record sees its content once. The inability to answer holds from issuance onward, and is a property only where issuance happens under the subject's control, such as on the subject's own device; where the operator or its issuer witnesses issuance, not keeping what it saw is a rule, and an implementation should say which of the two it is. The same holds at every release: a construction whose proofs reveal which registered commitment they matched hands the operator, at the first release, the link §9.1 says it cannot make, and not keeping that link would again be a rule.

**The design creates a record of queries, and that record is a surveillance product in its own right.** Routing payment, enforcing rate limits, and honouring expiry all require someone to hold who asked about whom, and when — relationship metadata that §9.2's commitment does not protect, because the commitment protects the fact, not the question. A design that sells no facts can still accumulate a corpus of questions. The bounds: the record of every query about a subject belongs in that subject's own receipt; per-asker counters are kept only for the rate window, never keyed or aggregated by subject; and whatever the operator or a payment processor must still hold — a regulated payee account is one such thing (§4) — is a rule and a subpoena target, and is stated as such here.

**Admission narrows the entry; nothing here touches onward use.** An admitted asker can pass an answer to an excluded party. Front companies, affiliates, and businesses in several classes at once can multiply askers past any per-asker rate limit, and a buyer can change its business after it is admitted. Class is checkable at admission and not after. Onward use is reached only by contract and legal enforcement — rules, not properties — and short expiry limits how long a relayed answer stays worth anything, without preventing the relay.

**A subject can automate a release.** Per-answer live release keeps a broker's census slow only while releases are decided one at a time. A subject paid to run software that releases to any paying asker has made a standing grant by other means, and the protocol cannot tell the difference. Paying for releases is itself a pressure in that direction.

**The flat price binds the platform, not the parties.** An asker can pay a high-demand subject extra off-platform for a release, or extract a kickback from a desperate one. That reintroduces private per-person pricing without publishing it. The rule's purpose — no published valuation of persons — survives; any stronger aim does not.

**The economics are unvalidated in both directions.** We argue attestation value is per-transaction where data value is aggregate; that argument is untested. If it is wrong, the subject's share is negligible and the design's social claim collapses even if its privacy claim survives.

**The sellable surface is smaller than it looks.** Where an operator publishes its proofs by design, as a ledger anchored for public verification does, anyone can check a published proof for free, forever. Only questions about records the subject has not published remain sellable, so the addressable line is the private half and should be sized on that half alone. If the admissible catalogue and the admissible buyers cannot pay for an operator, no operator is stood up, and the structural *cannot* is never instantiated.

**The exclusion may not hold under pressure.** §7 excludes the most lucrative buyers. We have no mechanism that prevents a future operator from widening the class list, and we say so rather than implying the exclusion is self-enforcing. It is a rule. Its protection is that it is published, dated, and specific enough that widening it is visible.

**And the hole the design does not close.** Every attribute in the catalogue can be satisfied by real, cooperating people producing genuine records for insincere reasons. Personhood proofs answer *is this a person*; they do not answer *is this genuine*. That is a property of graphs, not of identity, and nothing here addresses it.

---

## 12 · Conclusion, and a lineage

The mechanism is small: separate the release from the vouching, give the release to the subject, and let the operator sell only what is its own. Most of this paper is the consequences — a catalogue that cannot be farmed, a price that ranks no one, a buyer list that can be checked at the door, and answers that do not accumulate into the thing they were meant to replace.

The reason to prefer this shape to a policy is stated once more because it is the whole motivation: **an institution built to outlive the people who founded it cannot rest its most important refusals on anyone's restraint.** A rule needs a living enforcer with the right incentives at the moment it is tested, and that is the moment no one can guarantee. A design in which the prohibited act is unavailable needs no one — and where this design can make the act unavailable, it does; where it can only make a rule checkable, §9.3 and §11 say so.

The lineage is the preamble's: a claim about a person travels with the name of who released it and who vouched for it, and those remain two parties. **The convention does not make the claim true. It makes the chain visible** — which is all any of this does, and is more than a promise can do.

---

## Author Contributions and AI Disclosure

Framework, rulings, and editorial control: **Thon Ly**. Drafting, structural analysis, prior-art survey, and the adversarial pass that produced §9.2's condition and §9.3's objection: **Miss Aquarius℠**, the institution's named AI collaborator. The underlying models are not named, by standing policy; the collaboration is disclosed under one consistent name across every venue.

## Trademark Notice

HeartBank® is a registered mark. B-Vouch℠ — the service planned to implement this design (unbuilt; gated on the personhood layer being built) — B-PoH℠ and Miss Aquarius℠ are service marks of the institution. **This paper describes the mechanism, which is dedicated to the public domain; the marks are not licensed by this dedication.**
