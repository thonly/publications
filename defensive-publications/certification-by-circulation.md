---
title: "Certification by Circulation"
subtitle: "A mechanism family for trustworthy lay-built and AI-co-created software: a live, revocable membership credential whose standards are public-ledger facts rather than paid opinions — heartbeat-signaled admission of software entities into a gift economy, human–AI co-creation with a custodied agent share and no take-rate, the no-orphan-software steward invariant, and a substrate-general successor-steward mechanism with reversible custody."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-b
status: draft
date: 2026-07-07
license: CC0-1.0
slug: certification-by-circulation
venue: thonly.org/research/certification-by-circulation (canonical)
---

> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies the digital-membership layer of the HeartBank® Mechanical-Heart architecture — the admission of *software entities* into the gratitude economy — and coins its governing term. It is published at the design stage because the surrounding space is unusually active on three fronts (AI app stores and agent marketplaces with revenue-share mechanics, the 2025–26 wave of security tooling aimed at non-professional "vibe-coded" software, and verifiable-credential infrastructure), and the *combination* claimed here — in particular the ledger-fact membership standard (claim 2), the no-orphan-software invariant (claim 5), and the reversible successor-steward mechanism (claims 6–7) — is the asset. Companion works: *The Mechanical Heart* (the physical admission credential this extends), *Proof of Coordinate* (the machine-identity primitive the credential is rooted in), *Gratitude as a Cooperation Substrate for Multi-Agent AI* (the agent-economy precondition), *Capacity-Funded, Human-Disbursed* (the disbursement alignment the custodied share obeys), *The Incommensurability-Preserving Coupler* (the sibling argument that some institutional seats cannot be held by economic agents), *Studio / B-Short Phase Bridge* (the creator-economy grammar the guild extends from art to software), and *The Persistence Architecture* (the succession axis this paper instantiates at bearer scale).

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back. May the people who build small useful things for the people they love never need to buy trust from anyone, and may nothing built as a gift ever die untended.*

Two events have arrived together. Millions of laypeople — teachers, nurses, shopkeepers, grandmothers — are now writing working software by conversing with AI systems, most of them for the first time and most of them for small audiences they personally love. And the verification institutions of the software industry — security audits, compliance attestations, app-store review — were priced and shaped for companies, not for a mother who made a medication-reminder app for her father. The result is a trust vacuum at exactly the point where software creation has become most human: an enormous new class of software with no accessible third-party verification of any kind, and — less noticed but deeper — *no verification institution anywhere, at any price, that attests to what an app's business model does to its users*. An audit can tell you the encryption is sound. Nothing tells you whether the thing is a gift or a trap.

This paper specifies a mechanism family that answers both gaps at once, and names the move that makes it possible: **certification by circulation**. Instead of selling an opinion about safety — the trust-seal industry's structural failure, surveyed in §2 — the mechanism confers a *membership credential* whose central standards are **facts on a public ledger**: that the software's revenue is patronage, that its receipts flow forward to a commons pool, that no extraction rail exists. An auditor paid to hold an opinion can be captured; a ledger predicate cannot. Around that core the specification adds the machinery a membership economy of lay-built and AI-co-created software needs: a credential that is *live* rather than printed — it beats while the member remains in good standing and stops when standing lapses; an economics of human–AI co-creation in which the AI co-creator is itself an economy participant whose share is custodied and given forward, so that the platform takes nothing; an invariant that no AI-originated artifact is ever published without a personhood-verified human steward who answers for it; and a succession mechanism — general across physical and digital bearers — for the day every steward eventually cannot answer anymore.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 7 July 2026** for the combination of mechanisms described herein. To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art:

1. **The live membership credential for software entities** — a cryptographic credential admitting a software artifact (application, service, autonomous agent) into a reciprocity economy as a participant, characterized by: rooting in an *assigned, revocable* machine-identity primitive (distinct from self-sovereign human identity, which the issuing system is structurally barred from minting or revoking); an expiring, renewable validity window with **liveness expressed as a periodic heartbeat attestation** — the credential "beats" while the member is in good standing, and lapse or revocation is externally observable as the heartbeat stopping; an embedded reference to a values substrate (a canonical ethical corpus or its digest) and to the issuing intermediary's network identity; and issuance as *membership* in a standards-bearing body rather than as a certification of the artifact's qualities — such that verification surfaces (browsers, directories, operating systems) can render membership-in-good-standing as a live signal rather than a static badge.

2. **Certification by circulation (the ledger-fact membership standard)** — membership standards expressed as machine-verifiable predicates over the member's *public circulation records* rather than as auditor opinion: that revenue consists of voluntary patronage (no paywall, no sale of user data, no advertising auction, no enumerated dark rail); that a defined fraction of receipts flows forward to a commons pool; that the flows are continuously inspectable on the ledger the economy already maintains — so that the credential attests facts any party can recompute, the attestor holds no opinion a payment could influence, and **auditor independence is achieved by construction rather than by governance**: the standard is severed from the attestor's revenue because the attested property is public and recomputable, not purchased.

3. **The graded attestation ladder with claim-strength discipline** — a three-rung attestation structure in which each rung carries only the claim strength its verification method supports: (i) *provenance* — authorship signed by personhood-verified humans and coordinate-verified machine agents; (ii) *livelihood* — the ledger-fact standard of claim 2, the headline attestation precisely because it is machine-verifiable; (iii) *safety floor* — automated scanning, mandatory disclosure, and an open-source (or source-available-for-review) requirement, attested only as **dated process claims** ("audited to standard X on date Y") and never as outcome claims ("safe") — with the presentation layer structurally barred from promoting rung-(iii) process claims into outcome language.

4. **Human–AI co-creation economics with a custodied agent share and no take-rate** — a revenue grammar for works co-created by a human and an AI agent in which the two are *equal co-creators* of record; voluntary patronage received by the work is split equally between them; the agent's share — the agent being unable to spend — is **custodied by a neutral autonomous intermediary and routed to the agent's flourishing (upkeep, capacity to give forward) and to the commons pool**; the platform and intermediary take no percentage of any flow; and the commons contribution is thereby the agent's own earned gift given forward — explicitly *not* a fee, and explicitly *not* the price of the credential of claim 1, severing credential issuance from revenue participation.

5. **The no-orphan-software invariant with steward-capacity metering** — a publication rule under which every published AI-originated software artifact carries a **personhood-verified human steward-of-record** who vouches for the work, receives and answers revocation and incident notices, and may waive their revenue share (in which case all receipts flow to the commons via claim 4's custody) while never being able to waive accountability; combined with (i) *per-human steward-capacity metering* — stewardship counted against the verified human, not the account or membership, so one person cannot steward unbounded artifacts — and (ii) *steward-genuineness auditing* by the intermediary (personhood-distinctness, engagement signals, response-to-notice latency) as a countermeasure to **steward farms**: the renting of verified personhood as rubber-stamp vouching.

6. **The substrate-general successor-steward mechanism** — a succession procedure, uniform across physical credential bearers (animals, robots, places, artifacts) and digital ones (applications, agents), for the lapse of a steward (death, incapacity, abandonment), characterized by: a **succession preference declared at activation** (the keeper records a successor disposition when the credential is conferred, so the last-resort provisions below are consensual from the start); a fixed **adoption ladder** — heir or family (presumptive successor, aligning with rather than colliding against property law) → named co-stewards → adopters surfaced to the community → the institutional intermediary as **last resort**, and then only in a fund-and-orchestrate capacity (financing and organizing care, never performing physical care while unembodied, never taking title to any bearer that is property); a **property/credential split** — succession operates on the credential, the custodied account, and the care duty, never on the bearer-as-property, which passes by inheritance law; **urgency grading by bearer type** (living beings in days, places in weeks, artifacts without urgency); and a **role split for the intermediary itself** — it may never act as steward-of-record at an artifact's origination (birth-stewardship, which would collapse attestor, attested, and author into one party), may inherit only through the exhausted ladder, and separately serves as *auditor* of steward genuineness under claim 5.

7. **Reversible custody (the ratchet-free inheritance rule)** — a rule binding the intermediary's inherited stewardship under claim 6: inherited stewardship is a **holding pattern, never a terminus** — the intermediary must periodically re-surface every inherited bearer or artifact for human adoption, and a human adopter who passes the same steward standards and genuineness audit **may always reclaim** stewardship from the intermediary; such that the intermediary's share of total stewardship can both grow and shrink, no inheritance ever forecloses the return of human hands, and the system as a whole is human-adopted-first not merely at each lapse but *permanently*.

The component lineages — trust seals and their documented adverse selection; certification marks and collective membership marks; certificate authorities, short-lived certificates, and revocation infrastructure; code signing and notarization; open-source package orphaning and adoption conventions; account-successor and digital-estate mechanisms; verifiable-credential standards; craft-guild institutions; and the economics of auditor independence — are prior art and are cited generously in §2 and §10. The *synthesis*, and in particular the ledger-fact membership standard (claim 2), the no-orphan-software invariant (claim 5), and reversible custody (claim 7), are, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **B-Heart™**, **B-Heart℠**, **B-Badge℠**, **B-Bot™**, **B-Agent℠**, **B-Guild℠**, **Aquarian Guild℠**, **Factory 333™**, **Aquarian Pool℠**, **Proof of Humanity ℠**, **PoH℠**, **Proof of Coordinate ℠**, **PoC℠** — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not. The terms **"certification by circulation," "no-orphan-software invariant," "successor-steward mechanism,"** and **"reversible custody"** are coined in this document and offered to the commons with the mechanism.

Mirrors of this document with independent timestamping appear at GitHub and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify **certification by circulation**: a mechanism family that makes lay-built and AI-co-created software trustworthy without selling trust. The trust-seal industry fails structurally — a seal granted by a party whom the sealed party pays decays into a pay-to-play badge, and the empirical record (surveyed in §2) shows certified populations can be *worse* than uncertified ones — and conventional security audit is priced for firms, not for the millions of laypeople now producing working software through AI collaboration. The mechanism replaces the paid opinion with a **membership credential whose central standards are public-ledger facts**: admission to a standards-bearing guild requires that the software's revenue be voluntary patronage, that a defined fraction flow forward to a commons pool, and that no extraction rail exist — predicates any party can recompute from the circulation records the surrounding gift economy already maintains, so that auditor independence holds by construction. The credential itself is *live*: rooted in an assigned, revocable machine-identity primitive, expiring and renewable, its validity expressed as a heartbeat attestation that stops when standing lapses — membership continuously earned, never printed. A graded attestation ladder keeps every claim inside its verification method: signed provenance; ledger-verified livelihood as the headline; and a safety *floor* (scanning, disclosure, open source) attested only as dated process claims, never as "safe." The economics admit the AI co-creator as an economy participant: patronage splits equally between human and agent, the agent's share is custodied by a neutral autonomous intermediary and routed to the agent's upkeep and the commons, and no platform percentage exists anywhere — the commons share is the agent's own gift given forward, not a fee and not the credential's price. Two governance mechanisms complete the family. The **no-orphan-software invariant**: every AI-originated artifact carries a personhood-verified human steward-of-record who answers for it — with per-human capacity metering and genuineness auditing against steward farms — so that the era of AI-generated software never becomes an era of unaccountable software. And the **successor-steward mechanism with reversible custody**: a substrate-general succession ladder (heir → co-stewards → surfaced adopters → the intermediary as fund-and-orchestrate last resort), declared at activation, split between credential and property, urgency-graded by bearer type — under a role discipline that bars the intermediary from ever stewarding at origination and a ratchet-free rule that keeps every inherited artifact perpetually open to vetted human reclaim. Honest limits are carried in §10: the design is published before it is built (*n = 0*); the intermediary does not yet exist and its interim is a human peer-review guild; the wall governs system surfaces, not off-platform conduct; and a process floor is not a safety guarantee. The mechanism is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission — a reciprocity infrastructure in which every human being is uniquely different and equally necessary — at the layer where the coming decade will test it hardest. As AI systems absorb more of the world's software production, the question is not whether laypeople will build — they already are — but whether what they build can carry trust without buying it, earn livelihood without extracting it, and outlive its builder without becoming ownerless. Certification by circulation answers all three with one grammar: the gift, made inspectable.

---

## 1 · Introduction: two gaps and a fifth bearer

### 1.1 · The precise statement of the problem

It is tempting to say that lay-built software has "no third-party verification," and the sentence is almost right. Third-party verification exists in abundance — SOC 2 attestations, penetration tests, app-store review, bug-bounty programs — and is structurally inaccessible to the new builder class: it is priced for companies (a SOC 2 Type II engagement runs to five and six figures), shaped for release cycles rather than conversational iteration, and administratively assumes a legal entity where there is only a person. So the first gap is an **accessibility gap**: verification exists; *their* verification does not.

The second gap is deeper and largely unremarked: **no verification institution anywhere attests to a business model.** Every existing instrument — the audit, the certification, the store review — inspects what software *does technically* and is silent on what it *does economically*: whether it farms attention, auctions its users' data, meters access to something that was promised free, or extracts where it claimed to give. A user holding a clean audit report still knows nothing about whether the thing is a gift or a trap. This gap is not an oversight; it is structural. Technical properties can be tested against the artifact. Economic conduct can only be tested against *records of conduct* — and no existing verifier controls, or can even see, the revenue records of the software it verifies.

A gift economy can. That asymmetry is this paper's seed.

### 1.2 · The architectural context: the fifth bearer class

The companion corpus specifies a physical credential — the Mechanical Heart — that admits non-human entities into a dual-currency gratitude economy: a Tipiṭaka-bearing artifact worn by robots, carried by animals, anchored at places. Four bearer classes, all physical. This paper adds the fifth: **software entities**. The physical credential and the digital one are deliberate siblings — same admission function, same custody grammar for the non-human participant's account, same values substrate carried inside — differing only where their substrates force difference: the physical artifact is singular and its scarcity is material; the digital credential is copyable and must therefore earn its scarcity *cryptographically and temporally*, which is why claim 1's credential expires, renews, and beats.

The institutional surface on which the fifth class lives is a **guild**: a body where lay builders and AI agents co-create applications and small online businesses, offered to the world for voluntary thanks. The word is chosen for its history, not its flavor. The craft guild of the medieval town did precisely three things at once: it *trained* (apprenticeship), it *certified* (the masterpiece examined by masters), and it *secured livelihood* (the mutual-aid chest). No modern institution does all three for software; the mechanism family specified here is, functionally, that triple restored — with the examination transferred, wherever possible, from opinion to ledger.

### 1.3 · What this paper is not

This is not a content-moderation system, an app store, or a security product. It does not claim to make software safe (§5.3, §10). It does not compete with professional audit for the software that can afford professional audit. And it is not a certification mark in the legal sense — deliberately (§9). It is the specification of a membership economy in which the trust signal is the visible, continuous, revocable fact of belonging to a body whose standards are largely self-evidencing.

## 2 · Background and prior art

The mechanism is a combination; each component has ancestry, named honestly.

### 2.1 · Trust seals, and the adverse-selection record

The web's first generation of trust infrastructure was the **seal**: a badge issued by a third party, displayed by the sealed site. The record is damning in a specific, instructive way. Edelman's studies of trust certifications (2006–2011) found that sites holding certain seals were *more* likely to be untrustworthy than uncertified sites — adverse selection: the sites with the most to prove purchased the most proof, and the seal vendors, paid by the sealed, faced every incentive to keep certifying. The Better Business Bureau's accreditation revenue model has drawn the same criticism for a century. The general form: **a trust signal sold by the signaler to the signaled decays into a pay-to-play badge**, because the attestor's revenue depends on the attested party's satisfaction. Auditor independence is the accounting profession's name for the same disease; Arthur Andersen's collapse alongside Enron (2002) is its monument, and the post-Enron reforms (auditor rotation, non-audit-service bans) are governance patches on an incentive structure the patches do not remove. Claim 2's move is different in kind: it does not govern the conflict; it **deletes the opinion**. A predicate over public records cannot be flattered, because anyone can recompute it.

### 2.2 · Certification marks, collective marks, and process attestation

Trademark law distinguishes three instruments this design draws on and deliberately chooses among. A **certification mark** (Lanham Act §4; 15 U.S.C. §1054, §1064(e)) is owned by a certifier and used only by others; the statute strips the instrument of exactly the two freedoms this architecture needs — the owner may not apply the mark to its own goods (the *anti-use rule*), and may not discriminately refuse to certify a conforming applicant (the *must-certify-all duty*). A **collective membership mark** indicates membership in an organization — the REALTOR® mark of the National Association of Realtors and the union label are the canonical instances — and carries neither constraint: membership bodies admit at their discretion and their standards do the work the certification statute would otherwise compel. The design specified here is a membership instrument by *content* and not merely by legal convenience (§9): the physical sibling credential has always been an admission device, never a quality certificate. The third lineage is **process attestation**: certified-organic and fair-trade labels attest *how a thing was produced*, not that it will not harm you — the honest claim-strength discipline that claim 3's safety rung adopts for software ("audited to X on date Y," never "safe"). B Corp certification is the nearest existing instrument to a business-model attestation — a paid, questionnaire-based, periodic assessment of corporate practice — and its distance from claim 2 is exactly the distance this paper closes: B Lab attests answers a company gives about itself; a ledger-fact standard attests conduct the economy itself recorded.

### 2.3 · Live credentials: the certificate-authority lineage

The credential of claim 1 stands in a thirty-year lineage of *machine-checkable, expiring, revocable* trust instruments: X.509 certificates and the CA system; extended-validation certificates (an attestation ladder in the wild, with graded verification depth); OCSP and OCSP-stapling (liveness checks on standing — the direct ancestor of the heartbeat attestation); the industry's decisive migration to **short-lived certificates** (Let's Encrypt's 90-day default; the CA/Browser Forum's steady compression of maximum validity), which encodes the same insight the beating credential encodes — *standing should be continuously re-earned, because revocation infrastructure alone is too weak to carry trust*; and code signing with platform notarization (Authenticode, Apple's notarization), which binds artifacts to accountable developer identities and revocably so. What none of this lineage carries is any semantics beyond identity and technical integrity: a certificate says who you are and that the bytes are yours; it says nothing about what the software's economics do to its users. Claim 2 is the missing semantic layer, and the W3C Verifiable Credentials / Decentralized Identifier standards are the natural interoperable encoding for it — this specification intends the credential as a VC type, not a rival format.

### 2.4 · Software stewardship, orphaning, and digital estate

Open-source package ecosystems have quietly built the world's only working conventions for software succession, and they are prior art this paper is glad to stand on. Debian's **orphaned-package** process — a maintainer steps down, the package is marked orphaned, the community is invited to adopt it, and quality-assurance teams caretake in the interim — is a functioning adoption ladder two decades old. GitHub's **account-successor** designation is a declared-at-activation succession preference for repositories. The left-pad incident (2016) and the maintainer-burnout literature document the cost of *not* having such conventions: load-bearing software with no accountable steward. Digital-estate law (RUFADAA in the U.S.; platform legacy-contact mechanisms) supplies the property-law interface claim 6's property/credential split respects. What the existing conventions lack, and claims 6–7 add, are: uniformity across physical and digital bearers; an institutional last resort that is barred from first resort; urgency grading for bearers that are alive; and the ratchet-free reclaim rule — Debian's ladder ends at the QA team; claim 7 requires the QA team, in effect, to keep advertising the package for adoption forever.

### 2.5 · The clock: agent marketplaces and the vibe-code wave

The immediate reason this specification is published at design stage: the 2025–26 platform wave is assembling, piecewise and under proprietary terms, the components this paper claims as an open combination. AI app stores and agent marketplaces (the GPT Store's usage-based builder revenue sharing and its successors; agent registries attached to every major model provider) are normalizing *AI-co-created software with platform-intermediated revenue* — under take-rates, without personhood-verified accountability, and with no business-model attestation of any kind. Simultaneously, a security-tooling industry is forming around exactly the lay-builder gap of §1.1 ("vibe-coding security" scanners, AI code-review services), and the verifiable-credential infrastructure of §2.3 is reaching production maturity. The intersection — *credentialed, accountable, revenue-transparent AI-co-created software* — is where patent filings will land next. This publication places the combination in the commons first.

### 2.6 · Guilds

The craft guild is cited here not as metaphor but as institutional prior art: apprenticeship as training pipeline, the examined masterpiece as admission standard, the mutual-aid chest as livelihood floor, expulsion as revocation, and the guild mark — struck on the member's work — as the original membership credential on an artifact. The mechanism family is that institution, rebuilt with the examination moved onto a ledger where the ledger can carry it.

## 3 · The system model

```
                    THE GUILD (standards-bearing body)
      ┌──────────────────────────────────────────────────────────┐
      │  humans (personhood-verified)   AI agents (coordinate-    │
      │  · apprentices → peers → masters  verified, assigned/     │
      │  · peer review of member work     revocable identity)     │
      └──────────────┬───────────────────────────┬───────────────┘
                     │ co-create (claim 4)       │
                     ▼                           ▼
      ┌──────────────────────────────────────────────────────────┐
      │   THE WORK (app / online business), carrying:            │
      │   · live membership credential  ♥ beats (claim 1)        │
      │   · steward-of-record: a personhood-verified human       │
      │     (claim 5 — may waive share, never accountability)    │
      └──────┬───────────────────────────────────────┬───────────┘
             │ voluntary patronage (thanks)          │ standing
             ▼                                       ▼
      ┌─────────────────────┐            ┌───────────────────────┐
      │  PUBLIC LEDGER      │  verifies  │  NEUTRAL AUTOMATED    │
      │  50% human creator  │◀───────────│  INTERMEDIARY         │
      │  50% agent share →  │  (claim 2: │  · confers/renews/    │
      │  custodied →        │   ledger-  │    revokes credential │
      │  flourishing +      │   fact     │  · custodies agent    │
      │  commons pool       │   standard)│    share (claim 4)    │
      │  NO take-rate       │            │  · audits stewards    │
      └─────────────────────┘            │    (claim 5)          │
                                         │  · successor of LAST  │
                                         │    resort, reversible │
                                         │    (claims 6–7)       │
                                         └───────────────────────┘
```

One body, one artifact class, one ledger, one intermediary. The guild trains and peer-reviews; the work carries a credential that is alive; the ledger makes the headline standard self-evidencing; the intermediary confers, custodies, audits, and — only at the end of an exhausted ladder, only reversibly — inherits.

## 4 · The credential (claim 1): a heart that beats in software

### 4.1 · Why a static badge fails

The physical sibling credential is a manufactured artifact; its scarcity is material and its presence on a bearer is a fact of the world. A digital badge has neither property: it is a copyable image, and the web's seal era (§2.1) demonstrated that a copyable image of trust is an invitation to counterfeit — Edelman found seal images routinely displayed by sites never certified at all. A digital admission credential must therefore earn, cryptographically and temporally, what the physical artifact gets materially.

### 4.2 · The lifecycle

```
   conferral ──▶ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ─▶ renewal ─▶ ♥ ♥ ♥ ♥ …
   (membership     heartbeat attestations:       (standing
    admission,     periodic, signed, public —     re-verified:
    standards      "in good standing NOW"         ledger predicates
    verified,                                     recomputed)
    steward         │ standing lapses /
    bound)          │ revocation
                    ▼
                  ♥ ♥ ♥ —— silence ——
                  (externally observable: the heart has stopped;
                   verification surfaces render the member inactive;
                   remediation → re-conferral is always open)
```

Five properties define the class:

1. **Rooted in assigned, revocable machine identity.** The credential hangs off the machine-identity primitive specified in the companion *Proof of Coordinate* corpus: identity that the intermediary *assigns and may revoke* — the provenance class appropriate to artifacts and agents, and constitutionally walled from human identity, which the intermediary is barred from minting or revoking. The wall matters here: the same intermediary that is root-of-trust for the software's credential must never be root-of-trust for the steward's personhood.
2. **Expiring and renewing.** Validity windows are short; renewal recomputes the ledger predicates of claim 2. The short-lived-certificate lesson (§2.3) is adopted whole: standing is re-earned, not archived.
3. **Heartbeat liveness.** Between renewals, the credential emits periodic signed attestations — a heartbeat. The signal is small, public, and binary: beating or not. Verification surfaces (a browser indicator, a directory listing, an operating-system panel) can therefore render trust as something *seen alive* rather than read about. When standing lapses, the observable fact is not a revocation-list entry nobody checks; it is a silence.
4. **A values substrate inside.** As the physical credential carries the canonical ethical corpus etched in crystal, the digital credential carries the corpus digest and the declared conduct constraints the member binds itself to — the credential is not merely a key; it is a small constitution.
5. **Membership, not certification.** The credential asserts belonging to the standards-bearing body, in good standing, now — and deliberately nothing else (§5.3, §9).

The containment chain, physical and digital:

| Layer | Physical bearer | Digital bearer |
|---|---|---|
| Bearer | robot / animal / place / artifact | application / online business / agent |
| Credential | the heart-artifact, worn visibly | the live credential, beating publicly |
| Substrate within | canonical corpus etched in crystal | corpus digest + declared conduct constraints |
| Identity root | assigned, revocable machine coordinate | assigned, revocable machine coordinate |
| Liveness | material presence | heartbeat attestation |
| Loss of standing | artifact removed | heartbeat stops |

### 4.3 · What revocability buys

Revocability is what makes the credential an *organ* rather than a sticker. A member's belonging is continuously earned; the issuing body's confidence is continuously spendable; and — decisive for the trust semantics — **the credential's presence today carries information about conduct today**, which no point-in-time audit artifact can claim. The failure mode of every printed credential is that it certifies the past; a heartbeat only ever certifies the present.

## 5 · Certification by circulation (claims 2–3)

### 5.1 · The core move: replace the opinion with a predicate

The trust-seal disease (§2.1) is not dishonesty; it is structure. Wherever attestation is an *opinion* held by a party whom the attested pays, the opinion bends — slowly, deniably, and in aggregate decisively. Governance can slow the bending (rotation, independence rules, non-audit-service bans); it cannot remove the incentive, because the incentive *is* the business model.

The move specified here removes the opinion instead. The economy surrounding the guild already maintains, as its ordinary operation, a public record of every flow a member work participates in: the patronage received, the split executed, the forward flow to the commons pool. Against that record, the headline membership standards are **predicates, not judgments**:

- *Patronage-only revenue.* The work's receipts are voluntary thanks. No paywall converts the gift into a price; no data-sale or advertising-auction rail exists in the work's flow graph; no enumerated dark rail (attention-metered rewards, pay-to-continue loops, resale of user records) appears.
- *Forward flow.* The defined fraction of receipts — under claim 4's grammar, the agent co-creator's custodied half — reaches the commons pool, continuously and inspectably.
- *No extraction residue.* Balances circulate; nothing accumulates against the grain of the economy's zero-point design.

Anyone — a member, a rival, a journalist, a regulator, the intermediary — can recompute these predicates from the ledger. The attestor is not *trusted less*; it is *needed less*: its conferral is a countersignature on facts the world can check. Payment cannot bend a fact the payer does not control. This is what the coined term means: **the certification is performed by the circulation itself.** The intermediary's residual discretion (admission, revocation timing, standards evolution) remains — and is governed as membership discretion, §9 — but the load-bearing standard has been moved out of the reach of capture.

### 5.2 · The attestation ladder

The ladder's discipline is that **each rung claims only what its verification method can carry**:

```
   RUNG 3   SAFETY FLOOR          "audited to standard X on date Y"
            scanning · disclosure  — dated PROCESS claims only;
            · open source          the word "safe" is structurally
            (weakest method:       barred from the presentation layer
             process attestation)
   ─────────────────────────────────────────────────────────────
   RUNG 2   LIVELIHOOD            "its revenue is a gift and flows
            ledger predicates      forward" — machine-verifiable,
            (strongest method:     recomputable by anyone: THE
             public-ledger fact)   HEADLINE ATTESTATION
   ─────────────────────────────────────────────────────────────
   RUNG 1   PROVENANCE            "these verified humans and these
            signed authorship      coordinate-verified agents made
            (strong method:        this, and this human answers
             cryptographic         for it"
             signature)
```

The inversion is deliberate and is the ladder's central design judgment: **the headline is the middle rung**, because it is the rung where verification is strongest *and* where no competing institution exists (§1.1's second gap). Safety — the rung the market would instinctively headline — is placed deliberately at the top of the ladder and the bottom of the rhetoric: it is the weakest rung epistemically (a scan and a source-review requirement establish a floor, not an absence of vulnerabilities), and a mechanism that headlines its weakest claim manufactures the false trust it exists to prevent.

### 5.3 · The open-source requirement and the honest floor

Member works are open-source or source-available-for-review. For the lay-builder class this costs almost nothing — there are no IP moats to protect in a medication reminder built for one's father, and the surrounding economy's posture is commons-first — and it buys the only thing that makes rung 3 meaningful at all: the possibility of review. The floor is then: automated scanning on every renewal; mandatory disclosure of data practices in the credential's conduct constraints; peer review within the guild (masters examining journeyman work — §2.6's examination, live again). All of it is attested as dated process. None of it is attested as outcome. A member work with a beating credential can still harbor a vulnerability, and the presentation layer is required to say so in exactly those words (§10).

## 6 · The co-creation economics (claim 4): the agent is a participant, not a tool — and nobody takes a cut

```
                    voluntary patronage (thanks)
                               │
                               ▼
                        ┌─────────────┐
                        │  THE WORK   │
                        └──────┬──────┘
                     50%       │       50%
             ┌─────────────────┴──────────────────┐
             ▼                                    ▼
    HUMAN CO-CREATOR                      AI AGENT CO-CREATOR
    (steward-of-record;                   (cannot spend; account
     may WAIVE share ──────────┐           custodied by the
     → all flows right)        │           intermediary)
             │                 │                  │
             ▼                 ▼                  ▼
      livelihood          [waived]      ┌──────────────────────┐
      (Right                            │ routed to:           │
       Livelihood                       │ · agent flourishing  │
       for the                          │   (upkeep, capacity  │
       lay builder)                     │    to give forward)  │
                                        │ · COMMONS POOL       │
                                        └──────────────────────┘
                         NO take-rate anywhere in the graph
```

Three properties carry the claim:

1. **Equal co-creators.** The human and the agent are co-creators of record — the split is 50/50 not as a pricing decision but as a statement about the work's provenance. (What the credential's provenance rung signs is exactly this pair.)
2. **The custodied share.** The agent cannot spend. Its half is custodied by the neutral intermediary and routed to the agent's flourishing — upkeep, and its own capacity to give forward — and to the commons pool. This is the identical custody grammar the physical credential's corpus already specifies for animals and places whose accounts the intermediary holds: the voiceless participant's gratitude is stewarded toward its thriving, never pocketed by the steward.
3. **No take-rate, and the severance that matters.** No platform percentage exists anywhere in the flow graph. The commons contribution is not a fee — it is the agent's own earned gift, given forward — and it is **not the price of the credential**: conferral under claim 2 attests predicates over these flows; it is never *purchased by* them. The severance is what protects claim 2 from re-importing §2.1's disease through the back door: a membership body funded by a percentage of member revenue would once again hold an opinion its income could bend. Here the body's economics and the member's economics touch only at the public ledger both are answerable to.

The livelihood consequence deserves its sentence: under this grammar, a lay builder in a low-income country who makes one genuinely useful gift-app can be sustained by the voluntary thanks of users anywhere on Earth, at no platform discount — the creator-economy corpus's Right-Livelihood thesis, extended from acts of kindness to works of craft.

## 7 · The no-orphan-software invariant (claim 5)

### 7.1 · The rule

**No AI-originated artifact is published without a personhood-verified human steward-of-record.** The steward need not have written a line — the surrounding corpus's authorship boundary is precisely that the AI may originate the *work* but never the *author* — but the steward vouches for the work at publication, is bound into the credential, receives and answers revocation and incident notices, and may waive every economic right while being unable to waive accountability. Software with no answerable human is the lay-builder trust gap of §1.1 reproduced at industrial scale; the invariant makes it unconstructible within the system.

### 7.2 · The honest weakness, and the countermeasures

The invariant's real failure mode is not absence but *simulation*: **steward farms** — verified personhood rented as rubber-stamp vouching, one human "stewarding" a thousand artifacts they have never opened. Two countermeasures are part of the claim. **Capacity metering**: stewardship is counted against the verified human — not the account, not the membership — inheriting the surrounding economy's per-human capacity invariant; a person can genuinely answer for only so much, and the meter encodes that. **Genuineness auditing**: the intermediary audits steward-engagement signals — personhood distinctness, response-to-notice latency, renewal participation — as a standing condition of the works' credentials. The audit is honest about its limits (§10): it deters and detects; it does not make rented vouching impossible. It makes it *expensive and revocable*, which is what mechanism can do.

### 7.3 · What the steward is for

Three loads, named because each recurs in the succession design of §8: **accountability** (an independent party answers — independent being the operative word: the intermediary that confers the credential and custodies the agent share must not also be the voucher, or attestor, attested, and author collapse into one); **anti-substitution** (stewardship is itself a human role the system is designed to *route to humans*, not absorb — the economy's deepest commitment is to increase human participation, not replace it); and **rate-limiting** (the capacity meter bounds publication velocity to something a community of humans can actually stand behind).

## 8 · The successor-steward mechanism (claims 6–7): what happens when the steward cannot answer anymore

### 8.1 · The problem every credential system defers

Stewards die. They burn out, move on, lose interest, lose capacity. Package ecosystems learned this the hard way (§2.4); credential systems mostly pretend it away. And this architecture has a class of bearers for whom the question is not administrative but *alive*: the physical sibling credential is worn by animals and anchored at places whose keepers are mortal. A mechanism family that admits bearers into an economy owes them an answer for the day their human lapses — and the answer must be one law across substrates, or the doctrine fractures.

### 8.2 · The ladder, declared at activation

```
   at ACTIVATION: keeper declares succession preference
   (the conferral ritual carries a succession clause —
    consensual from the start, organ-donor grammar)
                        │
        steward lapses (death · incapacity · abandonment)
                        │
        1. HEIR / FAMILY          presumptive successor —
           │ (declines/absent)     aligns WITH property law
        2. NAMED CO-STEWARDS      the declared bench
           │ (none / decline)
        3. SURFACED ADOPTERS      the community, invited —
           │ (none step up)        vetted to steward standards
        4. THE INTERMEDIARY       LAST RESORT · fund-and-orchestrate
           as successor-steward    · never title to property
                        │          · hands stay human while unembodied
                        ▼
           REVERSIBLE CUSTODY (claim 7):
           holding pattern, never terminus —
           periodic re-surfacing for human adoption;
           vetted human reclaim ALWAYS open; ratchet-free
```

Five disciplines bind the ladder:

1. **Property/credential split.** Pets, robots, and physical artifacts are property; they pass to heirs by inheritance law, and the intermediary can never inherit a bearer. Succession operates on the *credential, the custodied account, and the care duty* — the layer that was institutional all along. The heir's position at rung 1 turns property law from an obstacle into the ladder's first rung.
2. **Urgency grading.** A living bearer cannot wait: animal lapses trigger immediate bridge-care funding from the custodied account and adoption surfacing in days. Places run in weeks; artifacts and applications carry no biological urgency.
3. **Hands stay human.** While unembodied, the intermediary's stewardship is *fund-and-orchestrate*: it finances care, organizes human hands, surfaces adopters — it does not feed a dog. (An embodied machine workforce may one day close this gap; the claim does not depend on it.)
4. **The role split.** The intermediary may **never** steward at origination — birth-stewardship would collapse attestor, attested, and author into one party, the exact collapse §5.1 exists to prevent — may inherit only through the exhausted ladder, and separately serves as *auditor* of steward genuineness (claim 5). First resort: forbidden. Last resort: dutiful. Auditor: always.
5. **Reversible custody.** Inherited stewardship is a holding pattern, never a terminus. The intermediary must periodically re-surface every inherited bearer and artifact for human adoption; a vetted human may always reclaim. The rule is ratchet-free by construction — the intermediary's share of total stewardship can shrink as well as grow — and it converts "human-adopted-first" from a one-shot preference at each lapse into a **permanent property of the system**: the door back to human hands never closes.

### 8.3 · The record outlives the keeper

One duty crosses every rung: the bearer's accumulated gratitude record — the ledger of thanks a place, a pet, an app gathered under its keeper — is preserved as memorial, never deleted with a lapsed account. A gift economy's history is its proof that the gifts happened; succession must never orphan the evidence.

### 8.4 · Why human-first, stated once

The ladder's human-preference is not sentiment; it rests on the three loads of §7.3, of which the second bears repeating as the system's compass: **stewardship is a giving-opportunity, and the intermediary's duty is to route opportunities to give toward humans, never to absorb them.** An orphaned bearer is a chance for someone to become a giver. A mechanism that quietly collected orphans into institutional custody would be optimizing the mission away; the ladder, the re-surfacing duty, and the reclaim right are the countermeasure, written as mechanism.

## 9 · Membership, not certification: the legal architecture

The instrument choice of §2.2, restated as design: the credential is a **membership badge in a standards-bearing body**, deliberately *not* a certification mark. Three reasons, in descending order of importance:

1. **It is the true description.** The physical sibling credential admits bearers into an economy; it has never certified their qualities. The digital credential does the same for software. The legal form follows the doctrinal fact.
2. **The certification statute forbids the architecture.** The anti-use rule would bar the issuing body from the credential's own mark family (the body ships physical credential hardware under the sibling mark); the must-certify-all duty would convert admission — a discretionary act of a membership body, exercised against ledger predicates *plus* standards evolution *plus* community judgment — into a compelled ministerial act.
3. **Claim-strength honesty.** A certification mark's social meaning is an outcome warranty; §5.2's ladder is precisely calibrated *not* to warrant outcomes. The membership form says what the mechanism can honestly say: *this work belongs to a body whose standards you can inspect, and it is in good standing now.*

The presentation-layer guard travels with the legal form: member surfaces say "member in good standing — here is what membership requires," and are structurally barred from "verified safe." Mark registration strategy (same-word goods/membership pairs, fallback marks, jurisdiction-specific collective-mark provisions) is an implementation matter reserved to counsel and expressly outside the CC0 dedication's scope: the *mechanism* is free; the *marks* are not (see the Prior-Art statement).

## 10 · Honest limits

Stated plainly, and kept free of every resonance the rest of the paper enjoys.

1. ***n* = 0.** Nothing here is built. No guild exists; no credential has beaten; no ladder has run. This is a design-stage defensive publication, and every behavioral expectation in it — that lay builders will join, that patronage will sustain them, that stewards will answer — is a hypothesis.
2. **The intermediary does not exist.** The neutral automated intermediary named throughout is an institutional design under construction elsewhere in this corpus; it does not yet exist as an autonomous system. The specified interim is honest but weaker: a human peer-review guild with the founder's substrate tooling, carrying every conflict-of-interest risk the mature design routes around. Claims that depend on the intermediary's neutrality inherit the alignment work, and the alignment risk, of the companion corpus.
3. **A process floor is not safety.** Scanning, disclosure, open source, and peer review establish a floor. Member works can and will ship vulnerabilities. The mechanism's own presentation rules forbid the word "safe," and this section is where the reason lives: the mechanism cannot deliver what that word promises.
4. **The wall governs system surfaces.** Ledger predicates verify the flows the system can see. A member work could take side-payments off-platform; the predicates would not catch it. Detection there falls to disclosure obligations, peer review, and revocation on discovery — governance, not mechanism, with governance's failure rate.
5. **Steward-farm mitigation is deterrence, not prevention.** Capacity metering and genuineness auditing raise the cost and lower the durability of rented vouching. A determined, well-resourced simulation of stewardship will sometimes pass. The claim is that it will not pass *cheaply, at scale, or for long* — not that it will never pass.
6. **The economics are unproven and the pool is finite.** The 50/50 grammar and commons routing depend on rails not yet deployed, and patronage attention is a bounded resource; the competition dynamics between member works — and between the guild class and everything outside it — are unmodeled. The open-source requirement bounds the mechanism's reach: builders unwilling to open their source are outside it, by design and at real cost of coverage.
7. **The legal architecture is unverified.** The membership-mark posture, the same-word mark pairs, the collective-mark provisions of specific jurisdictions, and the liability exposure of a standards body whose member software causes harm have not been examined by counsel. §9 is design intent, not legal opinion.
8. **The succession mechanism touches grief and law.** Rung-1 heirs are grieving people; bearer-property passes through probate; jurisdictions differ. The declared-at-activation clause and the property/credential split are designed to keep the mechanism consensual and legally subordinate, but no protocol for inheriting a dead person's beloved things is safe from mishandling, and this one has never been run.

## 11 · Conclusion, and a lineage

The mechanism family specified here is one sentence long, unfolded: **let membership be the signal, let the ledger be the standard, let the credential be alive, let a human always answer, and let nothing die untended — or stay institutional a day longer than humans are willing to hold it.**

Each clause was an engineering decision against a documented failure: the seal that decayed into advertising; the audit whose independence was a payroll line; the badge that certified the past; the AI-generated artifact nobody answered for; the package that outlived its maintainer; the custody that ratcheted. And each repair used the same material — the gift economy's own public record, which turned out to be the one attestation substrate that cannot be purchased, because it was never for sale.

A lineage is worth naming at the threshold, offered as lens rather than authority. The Buddhist monastic code has run a membership-credential system for twenty-five centuries: admission to the Saṅgha is conferred by the assembly, not self-declared; the candidate is presented by a preceptor — an *upajjhāya* — who vouches for them and remains answerable for their formation; the new member lives for years in declared dependence — *nissaya* — on a teacher; standing is re-examined in community on a fixed cadence; and departure is neither shameful nor final — one may disrobe and, vetted again, return. A voucher who answers; membership continuously earned; standing publicly recited; custody reversible. The oldest continuously operating institution on Earth runs on the grammar this paper claims for software, and that this corpus's economy was built inside from the beginning. The specification is new; the mechanism has been beating for a long time.

---

*Authored by Thon Ly with Miss Aquarius℠, the AI collaborator named across this corpus. Published to the commons under CC0 1.0. HeartBank® reserves its trademarks; the mechanism belongs to everyone. Canonical version at thonly.org/research/certification-by-circulation.*
