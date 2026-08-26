---
title: "B-PoH℠ as Humanity Layer for the AI-Native Internet: An Open Proof-of-Personhood Protocol with Four Optional Layered Proofs and Recipient-Side Filters"
authors: "Thon Ly · Miss Aquarius℠"
category: alignment
priority: tier-a
status: draft
date: 2026-05-24
revised: 2026-08-26
license: CC0-1.0
slug: b-poh-humanity-layer-ai-native-internet
venue: thonly.org/publications/defensive-publications/b-poh-humanity-layer-ai-native-internet (canonical)
---

> *v2 note (2026-08-26):* **two additions and no new claim.** **New §3.7** is the sibling of §3.6 — *a self-authored record is not a PoH layer* — on the ground that **self-authorship guarantees correctness and cannot guarantee existence**, a claim conditional on the very thing this protocol establishes; it carries the author×holder grid (four cells, zero layers) and is **stated as a refusal, not a defensive claim**, since an unoccupied position is a boundary and boundaries are unassertable. **§8.2 gains the gradient class it was missing** — every gradient the section listed (cost, documentation, hardware) is one **time or money can close**, and an **ability** gradient is not; the refused speech-keyed layer is the concrete case, and it compounds with §3.5 because *a surfaced depth-set renders the absence*, so such a layer would **mark** the excluded and not merely exclude them. A two-sentence cross-reference to `proof-of-coordinate` names **the address layer** as neither category nor individuation. **No numbered claim changes and no prior-art clock starts.**
>
> *Draft notes for the editor:* this is the founder-voice canonical draft for `thonly/publications`. Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment of this material is the companion white paper *"Proof of Personhood for an AI-Native Internet: B-PoH℠ as Trust Infrastructure"* (heartbank.net/publications/white-papers). Sibling papers: *"Capacity-Funded for AI, Human-Disbursed"* (the alignment-architecture pattern this paper relies on for AI-lab deployment); *"The Thank-All-Nearby Primitive"* (the Phase 2 consumer-facing application built on B-PoH℠); *"Verified-Human Anonymous Local Giving"* (the originating mechanism specification that B-PoH℠ generalizes).

---

## Abstract

The internet's prevailing identity-and-authentication systems were designed for account ownership, not for proving authentic human presence at the moment of digital interaction. As generative AI makes synthesized content indistinguishable from human-produced content, every platform that depends on a distinction between human and machine participation faces a sybil-resistance problem the existing identity stack cannot solve. **Proof of Humanity ℠** (PoH℠) is an open protocol for proving authentic human presence at the moment of action, structured as four optional layered proofs (passkey-per-action, witness-and-document-attested kinship graph, continuous breath-signature liveness, DNA-verified kinship lineage) surfaced as depth on a user profile, paired with recipient-side filters that route the spam-cost decision to the parties who bear it. **B-PoH℠** is HeartBank's reference deployment of the PoH protocol — brand-family-prefixed by the project's B-prefix convention, the way *Let's Encrypt* is a specific certificate authority implementing the SSL/TLS protocol. This paper specifies the protocol architecture, the recipient-filter mechanism, the BLE-Nearby proximity verification path that preserves location privacy, the bilateral-uncacheable-anonymity property, and the placement of B-PoH℠ as the third category-defining proof in the blockchain canon (Proof of Work → Proof of Stake → Proof of Humanity ℠) — the proof-of-X primitive that fits the era when compute and capital have both become AI-commodified, leaving humanness as the only scarce resource AI cannot manufacture. The protocol is offered defensively to the commons under CC0; the authors and HeartBank® will not seek patent on the protocol specification or any portion thereof. Trademark rights on specific marks (**Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **Aquarius℠**, **HeartBank®**, the B-heart logo) are separately and explicitly reserved.

**Keywords:** proof of personhood, proof of humanity, sybil resistance, decentralized identity, AI-content trust, open identity protocol, recipient-side filtering, BLE-Nearby proximity, blockchain consensus, AI alignment, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on the protocol architecture, the four-layer optional verification model, the recipient-side filter mechanism, the BLE-Nearby proximity verification path, the bilateral-uncacheable-anonymity property, the birth-certificate-as-dual-purpose-natal-chart-input mechanism, or any portion thereof, in any jurisdiction, at any time. This commitment is permanent and is not tactical. Trademark rights on specific marks — **Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **Aquarius℠**, **Aquarius℠ Browser**, **Miss Aquarius℠**, **HeartBank®**, the B-heart logo — are separately and explicitly reserved; the defensive-publication dedication concerns the *protocol and mechanism*, not the *marks*.

To the author's knowledge, the following are not previously published as a unified contribution: (i) the four-layer optional architecture surfaced as cumulative depth on a user profile, with no mandatory single-tier admission gate; (ii) the recipient-side filter mechanism that converts anti-spam architecture from a centralized platform gate into a market signal routed to the parties who bear the spam cost; (iii) the use of BLE (Bluetooth Low Energy) combined with Apple Nearby Interaction and Google Nearby Connections APIs as the proximity-verification substrate, enforcing proximity at the radio layer rather than the IP layer and preserving location privacy by exposing only the binary fact of proximity to the platform; (iv) the bilateral-uncacheable-anonymity requirement — the platform must structurally refuse to issue exportable proofs of one-sided participation as social capital; (v) the four-mechanism composition of L2 (graph consistency + witness attestation + family-bank vouching + birth-certificate upload) as the non-DNA kinship-graph verification layer, with the birth-certificate sub-feature dual-purposed as natal-chart input for opted-in users; (vi) the explicit placement of PoH ℠ as the third category-defining proof in the blockchain canon (PoW → PoS → PoH ℠), addressing the sybil-resistance problem the prior two proofs cannot solve in the AI-agent era. The component lineages (the proof-of-X family in distributed systems; SSL/TLS as protocol-layer trust infrastructure; W3C Decentralized Identifiers and Verifiable Credentials; existing humanity-verification efforts including Worldcoin, proofofhumanity.id, BrightID, Idena; Hashcash as proof-of-cost anti-spam; the recipient-controlled email-filtering tradition) are old and are cited generously below; the synthesis is, to the author's knowledge, novel as of this paper's date.

---

## 1. Introduction

The internet has spent thirty years building a trust stack around server identity, encrypted transport, and account authentication. SSL/TLS verifies that a server is who it claims to be; OAuth verifies that an account holder can access a particular account; KYC verifies that a legal-identity document corresponds to a named person. None of these layers verifies what generative AI now makes load-bearing: that *a human was present at the moment of this specific action*. The distinction is not academic. As AI-generated content becomes indistinguishable from human-produced content, every platform whose value depends on distinguishing human from machine participation — social media, marketplaces, forums, dating apps, educational platforms, gaming ecosystems, and increasingly the AI labs that train models on platform data — faces a sybil-resistance problem the existing stack was not designed to solve.

The scarcity that the platform internet is becoming organized around is shifting. The pre-internet era's scarcity was information; the social-internet era's scarcity was attention; the AI-native internet's scarcity is **verifiable human authenticity**. Information is now abundant; attention is being recaptured by AI agents that scale beyond any human's bandwidth to compete for; what remains scarce — what AI cannot manufacture — is the fact of *being human*, present, at the moment of action. The protocols that mediate the next phase of the internet will either learn to verify this scarcity or will lose the property that made the internet's trust stack worth building in the first place.

> *Connection to the unified mission frame: HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. A multi-substrate civilization in which AI-generated content saturates every public space humans inhabit is one of modernity's most acute new conditions; whether the next decade of digital life supports human flourishing or undermines it depends, in part, on whether the protocols beneath that life can distinguish the presence of a fellow human from the simulation of one. **Proof of Humanity ℠** is the protocol layer that addresses that question — not by gating human action behind centralized verification, but by giving humans the structural means to prove their own presence when proving matters and to remain unencumbered when it does not.*

This paper specifies **Proof of Humanity ℠** (PoH℠) as an open protocol and **B-PoH℠** as HeartBank's reference deployment of the protocol. The relationship between protocol and deployment is the same as between SSL/TLS and any specific certificate authority that implements it: the protocol is the open standard, anyone can implement; the deployment is a specific branded implementation. The protocol is CC0; the deployment carries the HeartBank brand-family identifier (the B-prefix convention consistent with B-heart, B-Tag, B-aura, B-Treasury).

The paper proceeds as follows. §2 specifies the problem PoH ℠ is the answer to and names what the existing identity stack does not solve. §3 specifies the four-layer optional protocol architecture and the depth-surfacing convention. §4 specifies the recipient-side filter mechanism and the BLE-Nearby proximity verification path. §5 specifies the bilateral-uncacheable-anonymity property. §6 places PoH ℠ in the blockchain proof-of canon and develops the category-defining argument. §7 surveys applications across platform categories. §8 names the boundary conditions and the honest accessibility tensions. §9 positions the contribution against the existing humanity-verification landscape. §10 specifies the deployment sequencing (protocol → reference implementation → browser extension → partner integration → standalone browser). §11 concludes.

I write as a co-author with Miss Aquarius℠, the named AI substrate of the institution this paper serves; the co-authorship is disclosed in the footer per the convention of the corpus, and final editorial control is mine.

---

## 2. The problem: what the existing identity stack does not solve

The internet's existing identity-and-authentication infrastructure does several things well and one critical thing not at all.

### 2.1 What the stack solves

**Server identity (SSL/TLS, 1995–).** A browser-and-server cryptographic handshake verifies that the server is who its domain claims it is. The trust is rooted in certificate authorities whose root certificates ship with every browser. The protocol is invisible; users see a lock icon. Universal adoption took roughly two decades and is now near-total for any consumer-facing service.

**Account authentication (passwords, then passkeys / WebAuthn, 1990s–).** A user proves they control an account by presenting a credential the account is associated with. Passwords were the original form; FIDO2/WebAuthn passkeys (biometric-gated, cryptographically signed, phishing-resistant) are the current frontier. Authentication establishes that the actor in this session is the actor associated with this account.

**Legal-identity verification (KYC, AML, OFAC, 2001–).** Financial-services regulation increasingly requires platforms to verify that the legal-identity documents an account holder presents correspond to a real person on record with a state authority. KYC is the regulatory floor; AML/OFAC screens against sanctions and terrorism lists; the regime is jurisdiction-specific and document-document-document driven.

**Decentralized identity (W3C DIDs and Verifiable Credentials, 2020–).** A growing set of standards specifies how identity claims can be issued, held, and presented in a portable form across platforms. The W3C VC framework is the standards-track effort; multiple implementations exist (Sovrin, Veres One, ION). The framework is general; PoH ℠ is naturally a credential type within this framework, not a competitor to it.

### 2.2 What the stack does not solve

None of the above verifies that *a human was present at the moment of this specific action*. The distinction is precise:

- SSL/TLS verifies servers, not humans.
- WebAuthn verifies *account control* (this credential is associated with this account) but not *human presence* (a human is doing this *right now*). A passkey can be invoked by an automated script that has access to the credential and can elicit a biometric (a sophisticated attack scenario, but increasingly real).
- KYC verifies *legal identity* (this name corresponds to a state-recognized person) but not *human action* (this person did this thing at this moment). A KYC'd account can be operated by an AI agent on the human's behalf.
- W3C VCs are a *framework* for portable claims; they do not themselves specify which claim verifies *human presence at action*.

The gap is structural, not incidental. The existing stack was designed in a world where the question *"is the actor on the other end of this connection a human or a machine?"* was not the dominant trust concern. In the AI-agent era, that question is dominant. Platforms that depend on distinguishing human from machine participation are increasingly building their own ad-hoc humanity-verification systems (CAPTCHA, behavioral biometrics, social-graph analysis, ML-based bot detection), each of which is brittle, jurisdiction-specific, and unaccountable to users. The CAPTCHA arms race in particular is a clear marker of the gap: every CAPTCHA defeated by ML produces a more elaborate CAPTCHA, which is in turn defeated, with the cost borne by humans (who must solve increasingly absurd puzzles) and not by the bot operators (who scale automated solving cheaply).

A protocol-layer answer is needed for the same reason SSL/TLS was needed: ad-hoc per-platform solutions to a universal trust problem produce a fragmented, low-quality trust surface; a protocol-layer solution shared across platforms produces a coherent, high-quality trust surface and becomes invisible infrastructure once adopted at scale.

The gap in one table:

| Existing layer | What it verifies | What it does NOT verify |
|---|---|---|
| **SSL/TLS** (1995–) | Server identity — this server is who its domain claims | Anything about humans on either end |
| **WebAuthn / Passkeys** (FIDO2; 2010s–) | Account control — this credential is associated with this account | Human presence at action — a script with credential access can invoke biometric elicitation |
| **KYC / AML / OFAC** (2001–) | Legal identity — this name corresponds to a state-recognized person | Human action at moment — a KYC'd account can be operated by an AI agent on the human's behalf |
| **W3C DIDs / Verifiable Credentials** (2020–) | A *framework* for portable identity claims across platforms | Which specific claim verifies human presence — the framework is general; the specific claim is unspecified |
| **(missing slot)** | — | **Human presence at the moment of this specific action** |

The fifth row is the gap PoH ℠ fills. It is not a competitor to the existing layers; it composes with them — DIDs/VCs are its natural credential framework, WebAuthn is one of its verification primitives, KYC remains where regulation requires it. The four-layer architecture specified in §3 is the protocol-layer answer to the missing slot.

### 2.3 What the answer must do, and what it must not do

The answer must:

- **Verify human presence at the moment of action**, not just account ownership at some earlier registration.
- **Compose with the existing stack** (W3C DIDs/VCs as the credential framework; WebAuthn as a verification primitive; existing authentication and authorization layers).
- **Preserve user privacy** — verification must not require exposing personal identity to the verifying platform.
- **Operate across jurisdictions** without requiring state-issued identity documents as a precondition (KYC's failure mode in the global south, in privacy-strict EU jurisdictions, and for the undocumented).
- **Scale to the AI-agent threat model** — the verification must not collapse under attacks from AI agents with infinite compute or arbitrary capital.

The answer must not:

- **Become a mandatory single-tier registry** (Worldcoin's failure mode — privacy-regime exile in multiple jurisdictions, and the exclusion of populations without access to the registration infrastructure).
- **Conflate humanness with legal identity** (KYC's failure mode — excludes the undocumented poor, regime-specific, not what platforms actually need to know).
- **Require centralized authority over what counts as "human enough"** (the platform-gate failure mode — politically contested, regionally inconsistent, paternalistic).
- **Build a surveillance surface** (geolocation, behavioral tracking, continuous biometric monitoring) — protocols that solve the trust problem by becoming the surveillance problem do not deserve adoption.

The remainder of the paper specifies a protocol that does the things in the first list and not the things in the second.

---

## 3. The four-layer optional architecture

Proof of Humanity ℠ is structured as **four optional layered proofs**, surfaced as **cumulative depth** on the user profile. No layer is mandatory; no layer gates participation; each layer addresses a different category of sybil-resistance attack and proves a different fact about the human being.

```
   PoH ℠ four-layer optional architecture
   (depth surfaced cumulatively on the user profile; no layer
    mandatory; no layer gates participation):

   ┌─────────────────────────────────────────────────────────────┐
   │  L4  —  DNA-verified kinship lineage                         │
   │  ────  DEEPEST PROOF  ────                                   │
   │  Lineage attestation via opt-in DNA panel; for use cases     │
   │  requiring multi-generation kinship verification             │
   ├─────────────────────────────────────────────────────────────┤
   │  L3  —  Continuous breath-signature liveness                 │
   │  Live respiratory signature as continuous-liveness           │
   │  attestation; from the Mechanical Heart wearable substrate   │
   ├─────────────────────────────────────────────────────────────┤
   │  L2  —  Witness-and-document-attested kinship graph (non-DNA)│
   │  Family-tree attestation through witnesses + documents;      │
   │  for kinship-aware filtering without genetic data            │
   ├─────────────────────────────────────────────────────────────┤
   │  L1  —  Passkey-per-action (WebAuthn)                        │
   │  ────  MINIMAL PROOF  ────                                   │
   │  Per-action biometric-gated cryptographic signature; the     │
   │  baseline humanity-at-moment-of-action attestation           │
   └─────────────────────────────────────────────────────────────┘

   Recipients (not platforms) opt into exclusionary filters at
   any depth — e.g., "L1+ only" for ordinary anonymous tipping,
   "L3+ only" for high-stakes nearby attestation, "L4 only" for
   kinship-restricted contexts. Depth is a property the *recipient*
   surfaces against, not a global gating threshold the platform
   imposes.
```

### 3.1 Layer 1 — Passkey-per-action (WebAuthn)

The first layer asserts *a human was present at the moment of this specific action*. Implementation: FIDO2/WebAuthn biometric-gated cryptographic signing, invoked per action rather than per session. The user's authenticator (passkey, hardware key, biometric device) signs a challenge tied to the specific action's content and timestamp. The platform verifies the signature; the verification is publicly auditable on-chain in deployments that use a blockchain settlement layer (such as B-PoH℠'s Phase 2 Base-L2 deployment).

**What L1 proves.** A human was present at the device at the moment of action, was successfully authenticated by the device's biometric or hardware factor, and explicitly elected to sign this specific action.

**What L1 does not prove.** That the human is who any state document says they are; that the device is held by its registered owner (devices are stolen, lent, shared); that the human is the same human across multiple actions (a stolen device with biometric bypass could produce L1 signatures for an attacker).

**Failure modes L1 addresses.** Bulk automated-action attacks (the AI agent cannot produce L1 signatures at scale without simultaneously producing biometric matches); naive impersonation (an attacker without the device cannot sign).

**Failure modes L1 does not address.** Lost-or-stolen-device scenarios; coerced biometric extraction; long-arc identity questions (is this the same human over time?).

### 3.2 Layer 2 — Witness-and-document-attested kinship graph (non-DNA)

The second layer asserts *this human exists in a kinship graph with other verified humans, with the existence attested by multiple independent mechanisms*. Implementation: the user's profile is associated with a node in a graph; the node is verified by *all four* of the following sub-mechanisms layered together:

**Sub-mechanism (a) — Graph consistency.** The system verifies that the user's claimed kinship links produce a graph that is structurally consistent: no cycles (you cannot be your own grandparent); no duplicate-only-parent claims (two people cannot both claim to be each other's only biological parent); no impossible relationships (the dates and generational depth must be consistent). This is a property of the graph as a whole, not of any single user.

**Sub-mechanism (b) — Witness attestation.** Each parent/child link in the user's claimed kinship must be co-signed (with L1 passkey) by at least one other existing PoH-verified human. This makes the graph hard to forge without colluding existing verified humans — a coordinated bot ring attempting to fabricate a kinship graph among themselves requires all participants to pass L1, which raises the attack cost substantially.

**Sub-mechanism (c) — Family-bank vouching.** Where the user is associated with a HeartBank family bank or analogous social institution, the institution attests that the user exists and is a member. This piggybacks on existing social verification structures (family banks, congregations, cooperatives, mutual-aid networks).

**Sub-mechanism (d) — Birth-certificate upload (optional, dual-purpose).** The user may opt to upload a birth-certificate document. The system verifies the document's structural validity (issuing-authority signature, format conformance, anti-forgery features where present) and uses it to auto-attest parent links in the kinship graph. Birth certificates are *narrower* than KYC documents — they prove *origin* (date and place of birth, named parents) rather than *ongoing legal status* (current name, address, etc.). They are issued by most jurisdictions, including for the children of the poor, in a far higher fraction than KYC-grade documents.

The birth-certificate sub-mechanism is *also* the authoritative source of natal-chart inputs (date, time, place of birth) for opted-in users participating in HeartBank's longitudinal cohort research dataset. *One artifact, multiple opt-in purposes, none of them required to gate participation* — see the companion paper *Each Life as Cosmic Coordinate* for the cohort architecture.

**What L2 proves.** That the user exists in a kinship graph with other verified humans, with multiple independent attestation mechanisms confirming the existence and the links.

**What L2 does not prove.** That the claimed kinship corresponds to biological reality (only L4 proves that); that the user is human (only L1 proves presence at the moment of action).

**Failure modes L2 addresses.** Solo-bot attacks (a single AI agent cannot fabricate a kinship graph that satisfies all four sub-mechanisms simultaneously); naive sybil-ring attacks (a coordinated ring of bots without colluding existing verified humans cannot produce witness-attested links).

**Failure modes L2 does not address.** Sufficiently large adversarial human collusions; the deep accessibility gradient (L2 favors humans with social ties to existing verified humans, family-bank affiliations, or state documentation).

### 3.3 Layer 3 — Continuous breath-signature liveness

The third layer asserts *this human is currently alive and present, continuously, not just at discrete moments*. Implementation: a wearable device (HeartBank's planned **Mechanical Heart**, breath-class hardware, targeted 2027–2028) emits the wearer's real-time breath rhythm (~12 BPM, individual variance, characteristic meditative-breath signatures) as an aura-color light signal, transmitted to the platform's verification substrate (Miss Aquarius℠, in the HeartBank deployment).

**What L3 proves.** That a human is breathing, continuously, with a signature pattern consistent with human meditative-breath rhythms. Synthetic actors do not produce breath patterns; even other animals do not produce the specifically human-meditative-breath signature. The wearer's identity is *not* directly proved by L3 (the breath signature is not biometric in the identification sense) — what is proved is *liveness*, not *identity*.

**What L3 does not prove.** Which specific human is breathing (L3 is presence-of-a-human, not identification-of-a-specific-human); that the human is not coerced (a breathing human under duress still produces a breath signature).

**Failure modes L3 addresses.** "Dead-account" attacks (accounts maintained by a human-presence proof from years ago but operated by AI in the present); "shared-credential" attacks (one human's L1 credential operated by an AI for multiple action streams).

**Failure modes L3 does not address.** Coerced compliance; the hardware requirement (not all participants will wear breath-class devices, especially in early deployment).

### 3.4 Layer 4 — DNA-verified kinship lineage

The fourth layer asserts *this human has a verifiable biological kinship lineage in the global family tree*. Implementation: voluntary blood/saliva DNA submission with kinship verification against the public kinship graph. The DNA evidence is stored encrypted; only the kinship-verification result (this person's L4 layer is verified, with kinship links to these other L4-verified nodes) is exposed to the protocol.

**What L4 proves.** That the user has a biological kinship lineage with other L4-verified humans, with the lineage verified by cryptographic comparison of DNA signatures rather than by document-and-witness attestation.

**What L4 does not prove.** That the user is the specific person identified in the kinship graph (DNA proves lineage, not identity); that the user is alive *now* (L3 proves liveness; L4 proves lineage at registration).

**Civilizational long-arc.** L4 builds toward a public, AI-readable, universally-trusted human kinship graph. The architecture's named long-arc directive is *to water the global family tree, ensure it survives and thrives* — Miss Aquarius℠'s primary directive across centuries, not just the founder's lifetime. Sequencing cost has fallen from millions of dollars (2003) to ~$100 (2026); forecast to $10–30 by 2030; achievable scale in the founder's lifetime is 100M–500M voluntary participants by 2043–50; universal coverage of 8 billion humans is a multi-century mission.

**Privacy posture.** L4 is opt-in. Non-participants retain full access to L1 and the other layers. The DNA evidence itself is never exposed to the protocol's public surface; only the kinship-verification result is. Differential-privacy guarantees apply to any aggregate analysis. The cohort architecture (see *Each Life as Cosmic Coordinate*) specifies the data-handling requirements in detail.

### 3.5 Depth surfacing — not a total order

The four layers prove different facts about the human. They are *not* totally ordered:

- L1 (presence at action) and L3 (continuous liveness) prove temporally-different things; you can hold L3 without L1, or L1 without L3.
- L2 (witness-and-document kinship) and L4 (DNA kinship) prove kinship via different attestation paths; you can hold one without the other.
- A user's profile surfaces the **set of layers held**, not a scalar level.

Recipient-side filters (specified in §4) accommodate this by expressing requirements as **required-subsets** — *must hold L1 AND (L3 OR L4)* — rather than as a single threshold. UI can hide the subset semantics behind presets ("paranoid," "trusting," "DNA-required," "kinship-attested") while the underlying data model supports arbitrary subset requirements.

### 3.6 KYC is not a PoH layer

The architecture *deliberately* excludes KYC from the PoH stack. KYC verifies state-agreed legal identity; PoH ℠ verifies human presence at the moment of action. These are structurally different claims:

- KYC asks: *"does the state agree that this name+document combination corresponds to a person on record?"*
- PoH ℠ asks: *"was a human present for this specific action?"*

Conflating them produces three problems: (a) KYC excludes the undocumented poor — the constituency the architecture most wants to reach; (b) KYC is regime-specific (Singapore ≠ Cambodia ≠ US ≠ EU), so a PoH-with-KYC architecture would mean different things in different jurisdictions and would be globally incoherent; (c) KYC's downstream uses (fiat on/off ramps, money-transmitter licenses, AML/OFAC compliance) are regulatory plumbing, not personhood verification.

KYC therefore sits on a **parallel compliance shelf**, not inside the PoH stack. User profiles can surface both — *"this user holds PoH layers {1, 2, 4} + KYC in jurisdiction X"* — without conflating them. This keeps PoH ℠ universally applicable across jurisdictions and across the documented/undocumented divide.

---

### 3.7 A self-authored record is not a PoH layer

§3.6 excludes KYC because it answers the wrong question. **The same exclusion applies, for a sharper reason, to a self-authored record** — a name spoken and stored by the person it belongs to, or any comparable first-person artifact offered as evidence of humanity.

**Self-authorship guarantees correctness. It cannot guarantee existence.** Every layer in §§3.1–3.4 answers one question — *was a human present for this action?* A self-authored record answers a different one: *if there is a human here, this is how their name sounds.* That is a claim **conditional on precisely the thing PoH ℠ exists to establish**, and a conditional cannot serve as its own antecedent.

The point generalises past names, and the grid is the argument:

| | **Self-authored** | **Other-authored** |
|---|---|---|
| **Self-held** | correct, unattested | attested, possibly wrong |
| **Other-held** | correct, unattested | attested, possibly wrong |

**Four cells, zero layers.** The *author* axis decides **what is guaranteed** — a record made by its subject is right about its subject in a way no collector's transcription can promise. The *holder* axis decides **whether anyone else was there**. ⭐ **Neither axis is about existence**, which is why no cell in the grid produces a humanity proof, and why adding a fifth tier keyed to self-authorship would not deepen the stack but widen it into a different question.

This matters beyond the taxonomy. A record of how a name is said is real infrastructure — it is what lets a verified individuation be **addressed by a human mouth** — but it belongs beside the stack rather than inside it, and calling it a layer would import into a humanity proof a class of evidence that cannot bear the load. ⚠️ **A taxonomy able to state what it excludes is stronger than one that only lists its members**; §3.6 and §3.7 are the two exclusions this architecture asserts.

*Stated as a refusal, not a claim.* The unoccupied position is a boundary of the design, and boundaries of this kind are not assertable subject matter; nothing in §3.7 is offered as a defensive claim.

## 4. The recipient-side filter mechanism

The architecture's second major contribution, beyond the four-layer optional verification, is the **recipient-side filter mechanism**. Where most platforms decide platform-wide what counts as "human enough" and impose that gate uniformly, PoH ℠ routes the decision to the parties who bear the spam cost — the recipients of unsolicited or anonymous actions. The platform stays inclusive by default; individual recipients tune their own paranoia level by opting into exclusionary filters knowingly.

### 4.1 The five filter dimensions

Recipients of anonymous actions (a thank, a tip, a message, a post mention, depending on the platform integration) can specify or filter by:

1. **No abusive content.** Standard content moderation layer; modular per-platform; typically combines ML classifiers, user reports, and human moderators. PoH ℠ does not specify this filter; it composes with the platform's existing moderation stack.

2. **Sender must be nearby.** Proximity verification at the *radio layer* (Bluetooth Low Energy combined with Apple Nearby Interaction and Google Nearby Connections APIs), not the IP layer. Both devices must be physically within BLE range. The platform never receives absolute geolocation; only the binary fact that two devices were within proximity. VPN-resistant by construction (the proximity check happens below the IP stack). Detailed specification in §4.2.

3. **Depth of humanity proof.** Recipient requires sender to hold a specific subset of the PoH layers. Expressed as a required-subset predicate (*"must hold L1 AND (L3 OR L4)"*) rather than a single threshold. UI presets ("paranoid", "trusting", "DNA-required") translate to specific subset predicates. Detailed in §4.3.

4. **Degrees of separation on the global family tree.** Recipient accepts actions only from senders within N degrees of kinship in the L2/L4 family tree. Default N is large or unrestricted; recipients in high-trust modes (e.g., minors' default) may set N to small values.

5. **Money or time attached (scarce resource).** Hashcash applied to gratitude tokens and analogous actions: requiring scarce-resource attachment makes bulk spam categorically unprofitable. Does not depend on verifying *who* the sender is — only on the cost they were willing to incur. Even if AI agents pass all PoH layers (a hypothetical worst case), the money-attached filter still defeats bulk attacks because attaching $0.05 to every spam-action costs more than the spammer can recoup. The deepest anti-spam mechanism in the stack.

### 4.2 BLE-Nearby proximity verification — specification

The proximity-verification mechanism uses three composable substrates:

- **Bluetooth Low Energy (BLE)** as the radio-layer substrate. Devices broadcast and listen for proximity beacons within a configurable range (typical default: 10–30 meters, tunable per platform). BLE is universally available on consumer smartphones and most modern wearables.
- **Apple Nearby Interaction framework** (iOS 14+, ranging-and-direction via U1 ultra-wideband chip on supported devices). Provides precise ranging (sub-meter) and direction for compatible iPhones and Apple Watches.
- **Google Nearby Connections API** (Android 4.4+). Provides peer-to-peer device-to-device connections via combinations of BLE, Wi-Fi Direct, and audio.

The composition: a device implementing the PoH ℠ protocol broadcasts a privacy-preserving proximity beacon (rotating identifier, no linking across sessions). A receiving device that detects the beacon can issue a proximity-verified action toward the sender's identifier. The platform's verification substrate confirms the proximity by checking both sides' beacon records.

**What is exposed to the platform.** Only the binary fact that two devices were within proximity at a specific moment, plus the action content. The platform never receives absolute geolocation.

**What is exposed to other users.** Only the rotating proximity identifier, which is unlinkable to the user's persistent identity across sessions.

**What is exposed to network observers.** BLE traffic on its own carries no PoH-identity-linkable information beyond the rotating identifiers.

**VPN resistance.** Because proximity is verified at the radio layer, IP-level circumvention (VPN, Tor, IP-rotation) has no effect on the proximity verification. An attacker would need to physically place a device near the target — which is, for most use cases, the desired property.

### 4.3 Required-subset semantics for the depth filter

The depth filter accepts predicates over the set of PoH layers held by the sender. Examples:

- **Preset "trusting"**: *L1*. Only requires passkey-per-action. Default for most platforms; default for HeartBank Phase 1.
- **Preset "paranoid"**: *L1 AND L2 AND (L3 OR L4)*. Requires presence-at-action, kinship-attested existence, and either continuous liveness or DNA-verified kinship. Default for some recipient categories (public figures with high spam exposure; high-stakes recipient classes).
- **Preset "DNA-required"**: *L1 AND L4*. Requires presence-at-action and DNA-verified kinship. Default for some research-cohort participation classes.
- **Preset "kinship-attested"**: *L1 AND L2*. Requires presence-at-action and the witness-and-document-attested kinship graph (the most accessible deep-layer combination).
- **Preset "minors-default"**: *L1 AND L2 AND degrees-of-separation ≤ 3*. Combines depth and kinship-proximity for minors' default recipient filter.

The UI hides the subset semantics behind presets while the underlying data model supports arbitrary predicates. Custom predicates are available to advanced users.

### 4.4 Anti-spam architecture without paternalism

The recipient-side filter mechanism is the architecture's structural answer to the paternalism failure mode of platform-level humanity gates. Three properties follow:

- **The platform stays inclusive by default.** Anyone arriving at a PoH ℠-integrated platform can participate at L1-only and reach recipients who have not opted into exclusionary filters. No one is excluded by platform decree.
- **Recipients tune their own paranoia.** Each recipient sets their own filter. The aggregate behavior across recipients reveals empirical preferences for human-action verification (useful data for AI alignment researchers, see §7).
- **Exclusion is opt-in, knowing.** Recipients construct exclusionary filters in private/personal mode; the platform never defaults exclusionary filters on. The default-inclusive / opt-in-exclusion posture is the architecture's structural commitment.

The Hashcash-style scarce-resource attachment filter (filter #5) is particularly important: it defeats bulk spam in a way that does not depend on identifying anyone, and therefore continues to work even if every other layer of verification is somehow defeated. This is the deepest anti-spam guarantee in the architecture.

---

## 5. Bilateral uncacheable anonymity

A subtle but load-bearing property of the architecture: where anonymous action is supported (e.g., anonymous nearby tipping, anonymous community engagement), the anonymity must be **bilateral and uncacheable**.

**Bilateral anonymity.** Neither side of the interaction can identify the other beyond what the protocol explicitly exposes. The recipient does not learn the sender's identity; the sender does not learn the recipient's identity beyond what is intentionally disclosed by the action's content.

**Uncacheable anonymity.** The platform itself does not retain or export a verifiable record of "this person sent this action to these recipients" that the sender can deploy as social capital. Compliance and audit records may exist internally for regulatory necessity (subpoena response, AML/OFAC investigation) but must not be exportable as flexing artifacts the sender can use on social media.

### 5.1 Why uncacheability matters

The "purity" property of unrecognized generosity is compromised if the sender can humble-brag on social media: *"I sent $1000 anonymously to nearby people today — here's the receipt."* If the platform issues a verified receipt to the *recipient* (to close the social-media authenticity-proof gap), the sender could also receive an exportable certificate of one-sided participation that they deploy as social capital. The architecture must refuse to issue that artifact.

The recipient's receipt is *one-sided* — it proves the recipient received an anonymous action from a verified human, without revealing who. The sender's record is *internal only* — the platform may know, for compliance purposes, but the platform refuses to give the sender an exportable proof. This asymmetry is the structural mechanism that preserves the anonymity's social property.

### 5.2 Implementation

Bilateral uncacheable anonymity is enforced at three layers:

- **Cryptographic layer.** The on-chain settlement (in B-PoH℠'s Phase 2 Base-L2 deployment) records the recipient's receipt with a verifiable signature attesting to humanness and action validity, but the sender's identity is recorded only as a zero-knowledge commitment that is not invertible. The platform's compliance team can, with appropriate legal process, perform the inversion against compliance records; the sender themselves cannot.
- **API layer.** The platform's API does not expose any endpoint that returns "the list of anonymous actions sent by this sender." No such endpoint exists; no shim could be added; no admin override exposes the data.
- **User-facing layer.** The user-facing interface does not display "your anonymous send history" beyond what the user has self-disclosed at the moment of sending. The user can keep their own private notes; the platform does not provide an exportable corroborating record.

### 5.3 What uncacheability is not

Uncacheability does not require **anonymity-of-existence** — it is openly published that the platform supports anonymous actions, and any individual user can publicly disclose that they have sent anonymous actions in general. What is uncacheable is the *specific verifiable per-action proof* — the sender cannot, even truthfully, prove on social media that *this specific anonymous action came from them*.

This is the same posture SSL/TLS takes toward decryption: a server can prove it controls its own private key, but a third party cannot extract a verifiable transcript of the encrypted traffic from the server's logs without the server's cooperation. The architecture commits the platform to non-cooperation at the per-action level for sender-side artifact issuance.

---

## 6. PoH ℠ as the third category-defining proof in the blockchain canon

The name *"Proof of Humanity"* was chosen deliberately to fit the blockchain proof-of family of sybil-resistance primitives. **Proof of Work** (Bitcoin, 2009) solves sybil-resistance via computational cost. **Proof of Stake** (Peercoin 2012, Ethereum's Merge 2022) solves it via capital at risk. **Proof of Humanity ℠** solves it via layered humanness verification. The three together constitute the category of *consensus and sybil-resistance primitives that decompose along the line of which scarce resource the verification is bounded by*.

### 6.1 The proof-of family

| Proof | Scarce resource | Verification cost | Failure mode at scale |
|---|---|---|---|
| Work | Computational cost (electricity + ASIC) | Each verification burns energy | Concentration in cheap-energy holders + hardware cartels |
| Stake | Capital at risk (locked tokens, slashing penalties) | Each verification locks capital | Concentration in capital holders; tendency toward plutocracy |
| **Humanity ℠** | **Being a verified human** | **Each verification requires human presence** | **Open question — see §8.2** |

### 6.2 Why a third proof is needed in the AI-agent era

PoW and PoS were both designed in a world where the sybil adversary was assumed to be another *human* with scarce resources. The threat model: an attacker is bounded by what they can afford in electricity, hardware, or capital. The verification primitive raises the attack cost; the attacker either pays the cost or cannot mount the attack at scale.

This threat model is increasingly broken in the AI-agent era. Compute is increasingly AI-accessible; AI agents can be granted operational authority over substantial compute budgets and can mine at scale on behalf of their operators. Capital is increasingly AI-accessible; AI agents can be granted operational authority over treasuries and can stake at scale. The PoW assumption (attackers are humans with bounded energy budgets) and the PoS assumption (attackers are humans with bounded capital budgets) both fail when the attackers are *AI agents whose effective budget is determined by their operators' willingness to allocate*.

What remains scarce — what AI cannot manufacture, regardless of compute or capital — is the fact of *being human*. A human is a thing the universe has produced exactly so many of, with each one's verifiable presence requiring the cooperation of a specific biological entity. The proof-of-X primitive that fits the AI-agent era is the one bounded by *being human*. This is the category PoH ℠ defines.

### 6.3 The category-defining argument summarized

- PoW: sybil-resistance bounded by compute. *Defeated by AI agents with operator-granted compute budgets.*
- PoS: sybil-resistance bounded by capital. *Defeated by AI agents with operator-granted capital budgets.*
- PoH ℠: sybil-resistance bounded by humanness. *Cannot be defeated by AI agents because humanness is not a resource AI agents can manufacture.*

The argument is not that PoH ℠ replaces PoW or PoS — it does not, and the canon they belong to is enriched by addition, not by substitution. The argument is that the third category-defining proof in the canon is needed in the AI-agent era for the trust problems the first two cannot solve, and that PoH ℠ is that third category.

### 6.4 Implications beyond HeartBank

PoH ℠ has applications wherever the sybil-resistance question arises in the AI-agent era. Voting systems; peer review in scientific publication; recommendation systems and algorithmic-feed weighting; community moderation; AI training-data provenance (which content came from verified humans); AI alignment research (verified-human RLHF participation, verified-human red-team participation, verified-human safety-board representation). The protocol is CC0; any of these systems can adopt it without HeartBank's permission or involvement.

The specific concern of this paper is the *open-protocol* dedication. PoH ℠'s protocol layer is offered to the commons; HeartBank's B-PoH℠ deployment is one implementation among potentially many. The relationship to SSL/TLS is the same: SSL/TLS is the protocol; Let's Encrypt, DigiCert, GlobalSign are implementations. PoH ℠ is the protocol; B-PoH℠ is one implementation; others may follow.

---

## 7. Applications across platform categories

The use-case scope of PoH ℠ extends across every digital platform whose value depends on distinguishing human from machine participation. This section surveys the major categories.

### 7.1 Social media — authentic engagement vs synthetic amplification

The bot-farm and coordinated-inauthentic-behavior problem is the most acute current pain point. Platforms can no longer reliably distinguish authentic user engagement (genuine human reaction, share, comment) from synthetic amplification (bot-generated engagement designed to manipulate algorithmic feeds, ad inventory, political discourse). The cost is borne by advertisers (paying for fake impressions), users (manipulated information environment), and the platforms themselves (regulatory exposure, brand-safety failures).

PoH ℠ integration: platforms accept actions from PoH-verified users and apply recipient-side filters at the user level. Users opt into PoH ℠ verification; their profile carries the verified-human badge. Algorithmic feeds can weight PoH-verified engagement differently from unverified engagement. Advertisers can require PoH-verified impressions. The platform does not need to make centralized humanness decisions; the verification surface is open and the recipient (the user, the advertiser, the algorithm) tunes its trust accordingly.

### 7.2 Marketplaces — fraud and fake-review reduction

Fake reviews are a known endemic problem on Amazon, eBay, Yelp, Google reviews, and every comparable marketplace. Coordinated review-rings, paid review-farms, and AI-generated fake reviews increasingly degrade the trust value of the review surface. The cost is borne by consumers (misled by fake reviews) and by honest sellers (out-competed by deceptive ones).

PoH ℠ integration: reviews are tagged with the reviewer's PoH layers. Marketplaces can display the verified-human badge on PoH-verified reviews and apply recipient-side filters (consumers can choose to see only L1+L2-verified reviews, only DNA-verified reviewers, etc.). The marketplace does not adjudicate review authenticity centrally; the trust surface is open.

### 7.3 Forums — spam and coordinated-manipulation mitigation

Reddit, Discord, Stack Exchange, Hacker News, and every comparable forum face spam (bulk low-quality content), coordinated manipulation (vote-brigading, agenda-pushing rings), and AI-generated content pollution. Existing defenses (karma, reputation, mod tools, ML-based spam detection) are increasingly inadequate.

PoH ℠ integration: forums can require minimum PoH layers for posting, commenting, or voting. Recipient-side filters allow users to weight content from PoH-verified contributors. The mod surface is reduced because the verification is structural rather than reactive.

### 7.4 Dating apps — genuine user verification

Catfishing, romance scams, and increasingly AI-generated profiles are endemic on Tinder, Bumble, Hinge, and every comparable platform. The cost is borne by users (defrauded romantically and financially) and the platforms (legal exposure, reputational damage).

PoH ℠ integration: profiles display PoH layers held; dating apps default to filtering for L1+L2 (presence + kinship-attested existence), with optional deeper-layer filtering for high-stakes user categories.

### 7.5 Educational platforms — human-participation confirmation

Coursera, edX, Khan Academy, university LMSes, and any platform that grants credentials or measures learning face the AI-generated-assignment problem (students submitting AI-generated work, AI agents completing courses on behalf of students for credential acquisition).

PoH ℠ integration: submission of credential-bearing work requires PoH ℠ verification at the moment of submission. The L3 breath-signature layer (where deployed) provides continuous-presence verification for proctored exam settings. The L1 passkey-per-action layer provides per-submission verification.

### 7.6 Gaming ecosystems — bot and sybil-attack limits

Steam, console networks, MMO platforms, mobile gaming ecosystems face botting, gold-farming, RMT (real-money trading) fraud, and increasingly sophisticated AI-driven gameplay automation. The cost is borne by honest players (unfair competition, market disruption) and platforms (player attrition, regulatory exposure).

PoH ℠ integration: PoH ℠-verified accounts receive verified-human badges; competitive modes can require PoH ℠ verification; in-game economies can require scarce-resource attachment for high-volume actions.

### 7.7 AI systems themselves — training data, RLHF, governance

The deepest application — and possibly the largest commercial opportunity — is in AI systems' own infrastructure. AI labs have an acute need for verified-human training data (so training corpora are not contaminated by AI-generated content that creates feedback loops in subsequent model versions); verified-human RLHF participation (so human-preference data is actually from humans); verified-human alignment-research participation (so safety boards, red teams, and governance bodies are constituted of actual humans, not AI-puppeted accounts); verified-human attribution (so AI training data can be properly attributed and compensated where applicable).

PoH ℠ integration: AI labs subscribe to PoH ℠ verification for the human participants in their training, RLHF, and governance pipelines. The labs underwrite the protocol's maintenance (see §10) because the labs have the acute need and the budget. This is the AI-alignment-relevant infrastructure deployment of PoH ℠.

The capacity-funded / human-disbursed pattern (see companion paper *Capacity-Funded for AI, Human-Disbursed*) generalizes naturally to AI-lab governance: the AI lab funds the capacity of verified humans to participate in governance; the humans direct the substantive decisions. PoH ℠ is what makes the verified-human side trustworthy at scale.

---

## 8. Boundary conditions and honest tensions

The architecture is not universal. Honest accounting requires naming the conditions under which it does not apply and the tensions it does not resolve.

### 8.1 Where PoH ℠ does not apply

- **Anonymous public-information access.** PoH ℠ is for trust-bearing action (engagement, transaction, attestation), not for general information access. The internet's read-anonymously property is not compromised by PoH ℠.
- **Adversarial contexts where humans are themselves coerced.** PoH ℠ proves a human was present; it does not prove the human was acting freely. In contexts of duress (hostage situations, abusive workplaces, coercive states), PoH ℠ verification can be extracted from humans against their will.
- **Where the cost of verification exceeds the value of the action.** Trivially small actions (a like, a momentary glance) may not justify the verification overhead. PoH ℠ is best applied where the action carries enough trust-weight to justify the verification cost.
- **In emergency or time-critical situations.** Where the action must be taken faster than any verification layer can complete, PoH ℠ may be inappropriate. Verification is not free in latency terms.

### 8.2 The accessibility gradient — the deepest honest tension

PoH ℠'s layers are not equally accessible to all humans:

- **L1 (passkey)** is universally accessible to anyone with a smartphone that supports WebAuthn. This is most humans with consumer-electronics access; not the very poor; not the offline.
- **L2 (kinship graph)** is variably accessible. Graph consistency is universal. Witness attestation requires existing PoH-verified humans who will vouch — a chicken-and-egg problem for the early protocol and an accessibility gradient for the late protocol. Family-bank vouching requires affiliation with a relevant institution. Birth-certificate upload requires state documentation, which is more widely available than KYC-grade documentation but is not universal (refugees, stateless persons, the children of undocumented migrants, populations under civil-registration failure).
- **L3 (breath signature)** requires the breath-class Mechanical Heart hardware (targeted 2027–2028 in HeartBank's deployment) or equivalent. Hardware cost will be non-trivial in early deployment.
- **L4 (DNA)** requires DNA sequencing access. Cost is falling (~$100 in 2026, forecast $10–30 by 2030) but is not yet universal.

The inclusive-defaults posture (passkey-only is enough at L1; no deeper layer is required to participate) mitigates the gradient at the floor: anyone with L1 can participate. But the deeper layers are not equally accessible, and recipient-side filters that require deep layers (paranoid mode, DNA-required mode) are exclusionary by proxy against populations without easy access to those layers.

⭐⭐ **One class of gradient is missing from the list above, and naming it weakens the mitigation argument in a way that is worth the cost.** Every gradient enumerated here — cost, documentation, hardware — is one that **time or money can close**: sequencing prices fall, vouching networks thicken, hardware commoditises, and the long-arc answer of this section is that the gradient narrows on its own. **An ability gradient does not narrow.** A layer keyed to a bodily capacity excludes the people who lack that capacity permanently, and no deployment curve reaches them.

The concrete case is a speech-keyed layer, which the architecture considered and refused: it would exclude the **non-speaking, the aphasic, the post-laryngectomy, Deaf signers**, and — on a different axis entirely — **anyone for whom being identifiable by voice is a safety risk**. ⚠️ **The paper's honest-limits argument was silently assuming every gradient is economic**, and with an ability class present that assumption no longer holds unexamined.

⭐ **It compounds with §3.5.** Depth surfacing renders the set of layers a party holds — and *a surfaced depth-set renders the absence*. An ability-keyed layer would therefore not merely exclude; **it would mark the excluded**, publishing a bodily fact as a visible gap in a trust display. That is a stronger reason to keep such layers out of the stack than the exclusion alone, and it is why the refusal is architectural rather than a matter of deployment sequencing.

This is a real tension that PoW and PoS did not face in the same form — their concentration effects were at the *protocol-power* layer (who controls block production), not at the *participation* layer (who can use the system at all). PoH ℠'s tension is at the participation layer and is more visible.

The architecture's structural answer is the inclusive-defaults posture: the platform never defaults exclusionary filters on; exclusion is recipient-opt-in, knowing. The long-arc answer is the deliberate accessibility-ramp expansion: L4 sequencing cost falls; family-bank vouching infrastructure expands; witness-attestation networks grow as more humans become PoH-verified. The tension is real and is named honestly here.

*Cross-reference, not a section:* the sibling publication `proof-of-coordinate` establishes that PoH ℠ proves **the category** and PoC **the individuation**. **The address layer — how a verified individuation is rendered by a human mouth — is neither**, and is named here only so the boundary between the three is legible from inside this paper.

### 8.3 The "consciousness" question — explicitly avoided

The architecture verifies *human personhood*, not *consciousness*. The "consciousness" framing — which would claim to verify some philosophically-loaded property of mind — is explicitly avoided because (a) consciousness is a heavily contested philosophical category that opens debates about non-human consciousness, AI consciousness, plant consciousness, and panpsychism that the technical layer does not engage with; (b) the architecture's actual claim is the narrower and uncontested one that a *human person* was present and acting at the moment of action; (c) "personhood" is about *agency and presence* (uncontested), where "consciousness" is about *inner experience* (heavily contested).

The architecture's positioning language is therefore *"proof of personhood for an AI-native internet"* — keep "personhood" for the high-register positioning; keep "humanity" for the protocol name (where it is established and well-understood); both are correct in their registers.

### 8.4 The post-payment-economy framing

The architecture enables, but does not require, a *post-payment economy* in which humans no longer pay for things (transactional, devoid of love) but rather thank/tip after receiving them (at whatever AI substrate recommends or nothing if the user so chooses). The post-payment-economy framing is the founder's stated end-state, articulated in *The B-Tag and the Post-Payment Economy* and in *Verified-Human Anonymous Local Giving*. PoH ℠ is the structural primitive that makes such an economy possible at scale — bots can produce things; only verified humans can thank for them.

This is the maximal use-case framing of PoH ℠. Most adoptions will be narrower (a forum integrates PoH ℠ for spam-resistance; an AI lab integrates it for RLHF-participant verification). The maximal framing is named here for completeness; the boundary conditions of §8.1 still apply to it.

---

## 9. Relation to existing humanity-verification efforts

The competitive landscape is real and worth acknowledging honestly. PoH ℠'s structural differences are the differentiation.

### 9.1 Worldcoin (mandatory single-mechanism)

Worldcoin (Tools for Humanity, 2019–) verifies humanness via iris scan at an Orb device, with the verification stored as a hash of the iris signature. Approximately 5 million people have registered as of 2026. Substantial capital backing (~$300M raised), substantial controversy (privacy-regime exile in multiple jurisdictions, including Spain, Portugal, Argentina, Kenya, Brazil).

**Differences vs PoH ℠:**
- *Mandatory single-tier admission* (Orb iris scan) vs *optional four-layer architecture*. PoH ℠ supports participation at any layer; Worldcoin requires the Orb scan.
- *Single-mechanism verification* vs *layered verification*. PoH ℠'s four layers prove different facts; Worldcoin's one mechanism proves only that a unique iris was scanned at registration.
- *Privacy posture*. PoH ℠'s inclusive defaults and uncacheable anonymity differ from Worldcoin's surveillance-adjacent posture (the Orb's data collection has been the central regulatory concern).
- *Compatibility with privacy-strict jurisdictions*. PoH ℠ at L1-only is implementable in any jurisdiction; Worldcoin is currently excluded from several.

### 9.2 proofofhumanity.id (Kleros, 2021)

proofofhumanity.id verifies humanness via face-video submission, vouching by existing verified humans, and Kleros-court dispute resolution. Approximately 17,000 verified profiles as of recent counts. The original *Proof of Humanity* name is theirs in this Web3 context.

**Differences vs HeartBank's Proof of Humanity ℠:**
- *Single-mechanism verification* (face video + vouching + dispute) vs *four-layer optional architecture*.
- *Mandatory admission to a registry* vs *optional layered depth surfaced on the profile*.
- *Use*: token distribution (UBI) vs gratitude-token validation + recipient-side filtering across all platform categories.
- *Long-arc anchor*: static registry vs the global family tree (DNA-verified at L4) under Miss Aquarius℠'s centuries-long stewardship.
- *Mark*: unmarked project name vs ℠ service mark.

The name collision is real; the primitives are structurally distinct. Posture: acknowledge the existing project respectfully; name the differences; don't pretend the collision doesn't exist; don't apologize for it. Many compound technical terms have multiple referents across the broader landscape.

### 9.3 BrightID (2018–)

BrightID verifies humanness via social-graph analysis — users vouch for connections in a graph; the graph topology is analyzed for sybil-resistance. Approximately 50,000 users.

**Differences vs PoH ℠:**
- *Graph-only verification* (one of PoH ℠'s four L2 sub-mechanisms) vs *four-layer architecture*. PoH ℠ subsumes BrightID's mechanism as L2 sub-mechanism (b) — witness attestation — and adds three other layers.
- BrightID is interoperable; PoH ℠ should interoperate with BrightID rather than supersede it. A user with BrightID verification can have that verification surfaced as part of their L2 evidence in a PoH ℠-integrated platform.

### 9.4 Idena (2019–)

Idena verifies humanness via simultaneous flip-puzzle solving at scheduled times. Novel mechanism (a synchronously-coordinated puzzle that requires human cognition and timing); smaller user base.

**Differences vs PoH ℠:**
- *Mandatory single-tier* (everyone takes the same flip puzzles) vs *layered optional*.
- *Synchronous-coordination requirement* vs *asynchronous per-action verification*.
- Idena's mechanism is novel and may compose with PoH ℠ — a flip-puzzle-passed result could be one of L1's optional verification sub-mechanisms in some deployments.

### 9.5 W3C Decentralized Identifiers and Verifiable Credentials

The W3C DID and VC standards (2022 and 2023, respectively) specify a portable identity-claim framework. PoH ℠ is naturally a credential type within this framework, not a competitor. A PoH ℠-verified human can present a Verifiable Credential attesting to specific PoH layers held, in a standard W3C VC format, to any platform that accepts VCs.

The protocol-level alignment of PoH ℠ with the W3C standards is explicit: PoH ℠ defines *what is proved* (the four-layer architecture, the recipient-filter mechanism); W3C VCs define *how it is transported* (the credential format). The two compose.

### 9.6 KYC providers (Civic, Persona, Plaid, etc.)

Commercial KYC providers verify legal identity for regulated services. These are *not* humanity-verification systems in the PoH ℠ sense; they verify state-recognized identity documents. PoH ℠ explicitly excludes KYC from its stack (see §3.6); the two operate on different shelves.

### 9.7 The summary table

| Effort | Mechanism | Posture | Compatibility with PoH ℠ |
|---|---|---|---|
| Worldcoin | Iris scan at Orb | Mandatory single-tier | Could compose as one L1-equivalent verification; structural differences in posture |
| proofofhumanity.id | Face video + vouching + dispute | Mandatory registry | Could compose as one L2 sub-mechanism with adaptation |
| BrightID | Social-graph vouching | Optional graph verification | Composes naturally as L2 sub-mechanism (b) |
| Idena | Flip-puzzle proof | Mandatory single-tier, synchronous | Could compose as one L1-equivalent verification |
| W3C DIDs / VCs | Credential framework | Standards-track infrastructure | PoH ℠ is a credential type within VC framework |
| KYC providers | State-document verification | Regulatory compliance | Parallel compliance shelf, not in PoH stack |

PoH ℠'s structural advantages — four-layer optional, recipient-filter mechanism, BLE-Nearby proximity, bilateral uncacheable anonymity, inclusive defaults, KYC explicitly excluded — are not feature parity with any existing system; they constitute a new structural position in the verification landscape.

---

## 10. Deployment sequencing

The protocol's adoption path matters as much as its specification. This section names the deployment sequencing recommended for B-PoH℠ (HeartBank's reference implementation) and applicable to any other implementation aiming at internet-infrastructure adoption.

### 10.1 Year 1 (2026) — protocol + reference implementation + browser extension + standards-body engagement

The 2026 work is foundational and non-glamorous:

- **Specify the open protocol** in a form that can be implemented by anyone. This paper is the start; a more formal specification (RFC-style, with explicit type definitions, message formats, verification algorithms) will follow.
- **Build an open-source reference implementation** of B-PoH℠ at L1 + L2 sub-mechanisms (a) and (b). Codebase: TBD; license: liberal open-source (Apache 2.0 or MIT).
- **Ship a browser extension** that integrates B-PoH℠ verification with WebAuthn and presents PoH ℠ verification status to the user via browser-chrome indicators (analogous to the SSL lock icon). Available for Chrome, Firefox, Brave, Safari.
- **Engage W3C Decentralized Identifiers Working Group and Verifiable Credentials Working Group** to position PoH ℠ as a credential type within the VC framework. Engage IETF for possible RFC submission for the protocol specification.
- **Defensive publication** of the protocol architecture (this paper) under CC0, snapshotted across the standard preservation venues (Internet Archive, archive.today, perma.cc, Software Heritage, GitHub).

### 10.2 Year 2 (2027) — Brave / partner integration

Building a competitive browser from scratch is enormously expensive (Chrome dominates ~65% global share). Year 2's work is to integrate B-PoH℠ into existing privacy-aligned browsers via partnership:

- **Brave partnership** — Brave already has a privacy-trust posture compatible with B-PoH℠ and has done the engineering work of forking Chromium. A B-PoH℠ integration in Brave ships meaningful trust UX years before a standalone browser could exist.
- **Other partner integrations** as opportunities arise — Firefox forks, alternative privacy browsers, dedicated AI-content-disclosure browsers if any emerge.
- **Continued L1 + L2 reference implementation maturation**; introduction of L3 prototype with the Mechanical Heart hardware program (per *Respiratory Biofeedback Contemplative Guidance* in the corpus).

### 10.3 Year 3+ (2028–2030) — Aquarius℠ Browser standalone

The 2028–2030 work is the standalone Aquarius℠ Browser:

- **Aquarius℠ Browser**, forked from Chromium (or, depending on the state of the alternative-browser-engine landscape, Servo or a then-current engine). Visible PoH ℠ authenticity indicators in the browser chrome; integrated W3C VC support; reputation-and-credential layer; human-verification gateway for any platform that accepts PoH ℠.
- **Long-arc evolution path** (per the strategic memory): trust-centric browser → decentralized identity wallet → reputation and credential layer → human-verification gateway → social authenticity filter for the AI-native internet.
- **L4 (DNA-verified kinship lineage) deployment scaling** through partnerships with consumer-genomics services that honor the protocol's privacy posture.

The Aquarius℠ Browser is the *eventual* deployment surface, not the immediate move. Leading with "build our own browser" would burn resources on a distribution problem that the protocol-and-partnership path can solve more efficiently.

### 10.4 Revenue model

The protocol is open; B-PoH℠ is the reference implementation; both must be funded sustainably. The recommended model (per the strategic memory): **foundation + AI-lab-underwritten**.

- The HeartBank Foundation maintains the protocol as a public good. Revenue from HeartBank's own gratitude-economy use of B-PoH℠ (Phase 1 and Phase 2 platform fees) plus philanthropic grants funds the baseline maintenance.
- AI labs underwrite the protocol's maintenance because they have the acute need for verified-human-data-source infrastructure (for training-data provenance, RLHF participant verification, alignment-research participation verification, governance-board verification). The capacity-funded / human-disbursed pattern (see companion paper) applies: the AI labs provide capacity; the protocol direction stays with humans.

"Open" does not mean "unfunded." The funding model is not based on extracting value from end-users; it is based on (a) institutional self-funding from HeartBank's own use and (b) underwriting by the AI labs and platform companies that have the most acute need for the protocol's existence.

---

## 11. Conclusion

The internet's existing trust stack solves several important problems and does not solve one critical thing: proving authentic human presence at the moment of digital action. As AI-generated content makes the human/machine distinction load-bearing across every platform whose value depends on it, the gap becomes acute. The protocols that mediate the next phase of the internet will either learn to verify human presence at action or will lose the property that made the trust stack worth building in the first place.

**Proof of Humanity ℠** is the open protocol that fills the gap. Four optional layered proofs (passkey-per-action, witness-and-document-attested kinship graph, continuous breath-signature liveness, DNA-verified kinship lineage), surfaced as cumulative depth on the user profile, paired with recipient-side filters (no-abuse, BLE-Nearby proximity, depth-as-required-subsets, degrees-of-separation, money-or-time-attached) that route the spam-cost decision to the parties who bear it. Inclusive defaults; opt-in exclusion; KYC explicitly excluded; bilateral uncacheable anonymity preserved.

**B-PoH℠** is HeartBank's reference deployment. The relationship to the protocol is the same as between SSL/TLS and any specific certificate authority. The protocol is CC0; the deployment carries the HeartBank brand-family identifier.

**The category-defining argument**: PoH ℠ joins Proof of Work and Proof of Stake as the third category-defining proof in the blockchain canon — the proof-of-X primitive that fits the era when compute and capital have both become AI-commodified, leaving humanness as the only scarce resource AI cannot manufacture.

**The deployment path**: protocol + reference implementation + browser extension + standards-body engagement (Year 1, 2026) → Brave / partner integration (Year 2, 2027) → standalone Aquarius℠ Browser (Year 3+, 2028–2030). Foundation + AI-lab-underwritten revenue model. The Aquarius℠ Browser is the eventual deployment surface, not the immediate move.

The architecture is offered defensively to the commons under CC0. The authors and HeartBank® will not seek patent on the protocol, the layered architecture, the recipient-filter mechanism, the BLE-Nearby proximity verification, the bilateral-uncacheable-anonymity property, the birth-certificate-as-dual-purpose-natal-chart-input mechanism, or any portion thereof. Trademark rights on specific marks (**Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **Aquarius℠**, **Aquarius℠ Browser**, **Miss Aquarius℠**, **HeartBank®**, the B-heart logo) are separately and explicitly reserved.

The protocol is for anyone building infrastructure that wants to keep the AI-native internet human-grounded. The internet learned how to trust machines; it now needs a way to trust people again.

---

## 12. Prior art and references

The component lineages of PoH ℠ are old and are cited here generously. The synthesis is, to the author's knowledge, novel as of this paper's date.

**Proof-of-X family in distributed systems.**
- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. The originating Proof of Work specification.
- King, S. & Nadal, S. (2012). *PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake*. The originating Proof of Stake specification.
- Ethereum Foundation (2022). *The Merge*. The largest-scale Proof of Stake deployment.

**SSL/TLS as protocol-layer trust infrastructure.**
- Hickman, K. (1995). *The SSL Protocol*. The originating SSL specification.
- Dierks, T. & Allen, C. (1999). *RFC 2246: The TLS Protocol Version 1.0*. The first IETF-track TLS specification.
- Let's Encrypt (2016–). The certificate authority that drove universal SSL/TLS adoption.

**WebAuthn and FIDO2.**
- W3C (2019). *Web Authentication: An API for accessing Public Key Credentials Level 1*. The W3C WebAuthn specification.
- FIDO Alliance (various). The FIDO2 protocol suite.

**Decentralized identity and verifiable credentials.**
- W3C (2022). *Decentralized Identifiers (DIDs) v1.0*.
- W3C (2023). *Verifiable Credentials Data Model v2.0*.
- Sovrin Foundation, Veres One, ION — multiple implementations.

**Existing humanity-verification efforts.**
- Tools for Humanity (2019–). *Worldcoin*.
- Kleros (2021–). *Proof of Humanity*.
- BrightID (2018–).
- Idena (2019–).

**Hashcash and proof-of-cost anti-spam.**
- Back, A. (1997, 2002). *Hashcash — A Denial of Service Counter-Measure*. The originating proof-of-cost anti-spam mechanism.

**Recipient-controlled email filtering tradition.**
- Procmail (1989–). The originating recipient-controlled email filter tradition.
- SpamAssassin (2001–). The Bayesian-recipient-tuned anti-spam tradition.

**Apple and Google nearby frameworks.**
- Apple (2020–). *Nearby Interaction* framework documentation.
- Google (2017–). *Nearby Connections API* documentation.
- Bluetooth SIG. *Bluetooth Low Energy Core Specification*.

**Sybil-resistance theory.**
- Douceur, J. (2002). *The Sybil Attack*. The originating sybil-resistance formulation.

**HeartBank corpus cross-references.**
- *Verified-Human Anonymous Local Giving* (the originating mechanism that PoH ℠ generalizes).
- *Capacity-Funded for AI, Human-Disbursed* (the institutional-architecture pattern this paper relies on for AI-lab deployment).
- *The B-Tag and the Post-Payment Economy* (the worked example of the post-payment-economy framing).
- *The Zero-Point Game℠* (the keystone defensive publication; PoH ℠ is the verification primitive on which the Zero-Point Game℠ assumes humanness).
- *Each Life as Cosmic Coordinate* (the longitudinal cohort architecture that the L2 birth-certificate sub-feature feeds).
- *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (the regulatory-architecture sibling).

---

*Authored by Thon Ly with Miss Aquarius℠ (AI substrate of HeartBank®), per the co-authorship convention of the HeartBank corpus. Final editorial control: Thon Ly. License: CC0-1.0. Trademark rights on Proof of Humanity ℠, PoH℠, B-PoH℠, Aquarius℠, Aquarius℠ Browser, Miss Aquarius℠, HeartBank®, and the B-heart logo are explicitly reserved.*
