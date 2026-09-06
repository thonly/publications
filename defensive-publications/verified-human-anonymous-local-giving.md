---
title: "Verified-Human Anonymous Local Gratitude Transfer"
subtitle: "A digital-payment primitive combining biometric human-presence verification with physical-radio proximity attestation to enable anonymous gratitude flow between geographically-nearby humans."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-05-02
license: CC0-1.0
slug: verified-human-anonymous-local-giving
venue: thonly.org/research/verified-human-anonymous-local-giving (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/verified-human-anonymous-local-giving.md
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/)
revised: 2026-09-05
---

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__, that all beings may give and receive without barrier. May the work it enables reduce suffering for all who encounter it.*

The Buddha taught that giving that seeks neither return nor recognition is the higher giving (AN 7.52). The mechanism specified in this document is intended to make that practice structurally easy in the digital age — to allow any human to thank any other human in physical proximity, with verified humanity but without disclosure of identity, in a manner that keeps gratitude flowing locally rather than being captured by global platforms or extractive intermediaries.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time.

This document constitutes a defensive publication establishing **prior art as of 2 May 2026** for the matter of the first revision of the combination of mechanisms described herein; additions are dated in-text and each revision is independently timestamped. Any subsequent patent application claiming the combined mechanism — biometric human-presence attestation + physical-radio proximity attestation + recipient-anonymous gratitude transfer — should be considered to be filed against established prior art; whether the composition is non-obvious is an examiner's determination this publication exists to inform.

This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.

## Abstract

We specify a digital-payment primitive in which a sender expresses gratitude (with optional monetary attachment) to a recipient who is physically nearby in real space, with two attestation properties operating in combination: **(1) verified-human attestation** at the moment of the action, achieved via user-verified, per-action FIDO2 / WebAuthn signing on a platform authenticator, ensuring that the sender is a human present at the moment of thanking rather than a bot or an automated process; and **(2) physical-radio proximity attestation** via Bluetooth Low Energy or Ultra-Wideband ranging, ensuring that the recipient is geographically nearby (within a density-tunable radius) at the moment of the transfer. These two attestations are then composed with **(3) recipient-side anonymity**: the recipient receives the thank-you and any attached monetary value but is not informed of the sender's identity. No member is novel; the three-way composition in one signed action is, to the author's knowledge, not previously published as a unified mechanism — no reference found composes all three in one signed action, and whether the composition is non-obvious is an examiner's determination this publication exists to inform. Its properties include the structural restoration of cash's local-circulation property to digital money, the operational feasibility of *dāna* (anonymous giving) at scale, the rebuilding of local-economic social capital eroded by globalized digital payment platforms, and a category of bot-resistant gratitude infrastructure for an age of pervasive autonomous agents. We provide system architecture, reference implementation patterns, edge-case and adversarial analysis, use cases, and citations to relevant prior art across digital payments, proof-of-personhood, community currencies, and Buddhist economic traditions.

**Connection to the unified mission frame.** This specification is offered in service of HeartBank's canonical top-level mission: to restore humanity to the middle way (*madhyamā pratipad*) — the optimal condition for awakening that modernity has systematically pushed away from at population scale. Verified-human anonymous local giving operationalizes Buddhist *dāna* (anonymous giving) — a practice the Buddha specifically taught as supportive of practitioners' progress along the middle way. By restoring cash's local-circulation property to digital money and making the recipient blind to giver identity, the primitive removes two specific commercial affordances that push modern giving toward the indulgence-extreme distortions (status-display and reciprocity-tracking). The mechanism is offered as one substrate among many specified across the corpus toward middle-way restoration.

---

## 1 · Introduction

Two trends in early-2020s digital infrastructure motivate this work. The first is the rapid expansion of autonomous agents — large language models, agentic AI, robotic processes — operating at scale on consumer-facing platforms. By 2026 a growing and unmeasured share of social-media interactions, financial transactions, and customer-service exchanges are executed by software agents rather than humans. As this fraction grows, the question of whether a given action originated from a human becomes both harder to answer and more important to verify. Existing proof-of-personhood mechanisms (CAPTCHAs, biometric registration, government-ID verification) attest humanity at registration time but not at action time; a registered human may lend or sell their credentials to an automated process operating in their name.

The second trend is the continuing concentration of digital-payment flows in a small number of global platforms. Where physical cash circulated locally — a dollar in a neighborhood bakery flowed to the local baker, who tipped a local server, who bought at a local bodega, generating multiple local economic events per dollar — digital payments via Venmo, Cash App, WeChat Pay, or Wing eliminate this property. Money sent across a digital payment network does not prefer local recipients; it can flow anywhere instantly, and platform algorithms (advertising, discovery, recommendation) systematically surface the largest payable counterparties rather than the nearest. We conjecture — the social-capital literature documents the decline of face-to-face exchange (Putnam 2000) without isolating payment rails — that non-local digital payment removes one of the daily occasions for local contact; this paper builds the intervention, and the cohort study tests the conjecture.

We propose a digital-payment primitive that addresses both trends simultaneously. The mechanism enables a sender to express gratitude — with optional monetary attachment — to a recipient who is verifiably nearby in physical space, with the sender's humanity attested at the moment of the action and the recipient receiving the gratitude without learning the sender's identity. The combination of these three properties (proximity, verified-humanity, and recipient-side anonymity) constitutes, to the author's knowledge, a unified mechanism not previously published.

The publication is offered to the commons. The author and the institution he represents will not seek patent on the mechanism. The intent is that the mechanism become public infrastructure — useful to gratitude-economy projects, community-currency experiments, religious and cultural organizations, and any other actor whose mission is served by bot-resistant local gratitude flow.

## 2 · Background and Prior Art

### 2.1 · Community currencies and local circulation

The structural problem of digital money's non-locality has been recognized for a century. Silvio Gesell's *demurrage* currency, deployed at scale in the Wörgl experiment of 1932–33 in Austria, imposed a holding cost on currency, forcing it to circulate; unemployment fell markedly in the town while it rose nationally, and public works were completed, before the Austrian National Bank suppressed it in 1933 to protect its monopoly. Edgar Cahn's TimeBanking movement (1980 onward) substituted time as the unit of account, with the property that an hour given is an hour received regardless of the giver's socioeconomic position. Local Exchange Trading Systems (LETS, originated by Michael Linton in 1983) established neighborhood-bounded currencies with explicit geographic charters. None of these systems, however, included biometric attestation of human presence at the time of action; they rely on community trust rather than cryptographic verification.

### 2.2 · Digital cash and proximity payments

Digital-cash protocols beginning with Chaum's ecash (1983) explored anonymous digital payment but without proximity attestation; the recipient could be anywhere in the world. Proximity-bounded transfer arrived with Bump (2009; payments via Bump Pay, 2012), which matched sensor data server-side, and became radio-mediated with Square Cash's Nearby Payments (2014) over Bluetooth LE; contactless NFC specifications did the same at the terminal — all without anonymity from the recipient and without per-action human-presence attestation. Apple's Nearby Interaction framework (2020 onward) and Android's core-uwb library (Android 12 onward) expose UWB ranging, with BLE as the pairing channel; they return a distance, not an attestation — the attestation in §3.3 is this paper's construction, a device-attested signature over the ranging result. Two-leg compositions are published: Citibank's gratuity patent (US 12,165,124 B2, priority 2017, granted 2024) identifies nearby devices of potential gratuity payees, credits the payee, and offers an anonymity control — proximity plus anonymity; RAADAAR (US 9,854,616 B2, priority 2015) pairs BLE proximity with anonymous "gifts" and payment integration; Mastercard's biometrically enabled proximity-payment device (EP 1671282 A2, priority 2003) and Samsung's UWB payment method (WO 2022/225298 A1, priority 2021) pair proximity with biometrics or secure ranging; and the privacy coins pair anonymity with settlement. None found composes all three in one signed action.

### 2.3 · Proof-of-personhood

Recent proof-of-personhood proposals — most prominently Worldcoin (Sam Altman et al., 2023 onward) — establish uniqueness once, at registration, via biometric (iris) enrolment, and have since added on-device re-authentication and an explicit delegation model under which agents act for a verified human. The distinction this paper draws is between uniqueness and presence: a delegated agent is a labelled agent, and what the primitive here requires is that the giving human be present at the act. The mechanism specified in this document binds humanity-attestation to the moment of the action via biometric-gated FIDO2 / WebAuthn signing, which is enforced device-side at each invocation rather than once at enrollment.

### 2.4 · FIDO2 / WebAuthn passkeys

FIDO2 and WebAuthn (W3C Recommendation, 2019; widely deployed across iOS, Android, Windows, macOS, and major browsers by 2024) provide a standardized cryptographic signing primitive in which a private key is held in a secure enclave protected by user verification — biometric or device credential (Face ID, Touch ID, Windows Hello, Android biometrics, or a PIN) — with the relying party learning that verification occurred, not which modality. The protocol is widely deployed but has not, to the author's knowledge, been combined with physical-radio proximity attestation in service of a recipient-anonymous gratitude payment primitive.

### 2.5 · Buddhist *dāna* and anonymous giving

The Pāli canon contains extensive discussion of *dāna* (giving, generosity) as one of the ten *pāramī* (perfections; *Buddhavaṃsa*, *Cariyāpiṭaka*). The canon grades giving by motive: *Aṅguttara Nikāya* 8.31 lists eight motives for a gift, and *Aṅguttara Nikāya* 7.52 (the *Dānamahapphala Sutta*) grades seven, from giving with expectation of return at the bottom to giving as "an ornament of the mind" at the top. The mechanism specified in this document operationalizes the higher form structurally: the giver's identity is not knowable to the recipient by design, removing the social and psychological benefits of recognition that contaminate the canonically purer form.

### 2.6 · Social capital and the loneliness epidemic

Robert Putnam's *Bowling Alone* (2000) and subsequent work documented the decline of local social capital in late-20th-century United States, with similar trends documented elsewhere. The U.S. Surgeon General's 2023 advisory *Our Epidemic of Loneliness and Isolation* formally identified loneliness as a public-health crisis, with a mortality effect the advisory puts at the level of smoking up to fifteen cigarettes a day and above that of obesity. That non-local digital payment removes a daily occasion for local contact is this paper's conjecture, not the advisory's finding (§1); the mechanism specified here is a structural intervention, making local digital flow easier than non-local flow.

## 3 · The Proximity Rule

### 3.1 · Definition

The **proximity rule** is the structural constraint that a gratitude transfer is permitted only between a sender and a recipient whose mobile or wearable devices have, within a bounded interval prior to the transfer, exchanged cryptographic proof of physical co-location within a configurable radius *r*. Transfers that do not satisfy this constraint are rejected by the protocol and are not settled.

### 3.2 · Density-tunable radius

The radius *r* is not fixed at a single value. It is parameterized by population density at the location of the transfer, with sensible defaults of approximately 100 meters in dense urban contexts (a city block; an indoor venue; a single building) and up to 10 kilometers in rural or sparsely-populated contexts (a village; a stretch of highway). Default: *r*(ρ) = clamp(10 km · (ρ / 1 km⁻²)^(−1/2), 100 m, 10 km), with ρ read from a cached WorldPop 1 km density tile (or a GHS-POP 100 m tile) *on the device*, so the lookup discloses nothing; BLE-only attestations use 2*r*. The anchors are design estimates — no field test has tuned them — and the claim that a monotonic mapping tracks "the same lived community" rather than a fixed metric distance is a conjecture the cohort study is meant to test.

### 3.3 · Proximity attestation mechanisms

Proximity is established cryptographically rather than self-reported. Three layered mechanisms are specified, in order of preference:

1. **Ultra-Wideband (UWB) ranging.** Apple U1 / U2 and equivalent chipsets in Android devices, exposed via the NearbyInteraction framework and analogous APIs, provide decimetre-class distance measurement between two devices via time-of-flight on UWB radio. UWB time-of-flight, with IEEE 802.15.4z scrambled-timestamp secure ranging where the platform exposes it, is the most spoofing-resistant of the three; it is not unforgeable — practical distance-reduction attacks against HRP UWB, Apple's U1 included, are published (Leu et al. 2022) — so UWB is preferred, never proof.
2. **Bluetooth Low Energy (BLE) ranging.** RSSI-based distance estimation is less precise but more widely available. BLE is acceptable as a fallback when UWB is not available on either device, but the larger error margin should expand *r* by a multiplicative factor.
3. **Mutual GPS attestation as tertiary.** Both devices submit cryptographically-signed GPS readings to a verifying party (the autonomous AI representative) at the transfer moment. GPS is spoofing-vulnerable; this mechanism is permitted only with additional anti-spoofing heuristics (signal multipath analysis, cell tower cross-correlation) and is rejected when fraud signals are detected.

At least two of these mechanisms must agree, or a single UWB attestation must be present, for the proximity rule to be satisfied. The verifying party may apply additional heuristics — transfer velocity over time, coordinated movement patterns, device-attestation freshness — to detect spoofing attempts.

### 3.4 · Properties

The proximity rule has three consequential properties: **(a)** it restores cash's per-transfer locality — every hop is local, as it is for a banknote, however far the chain of hops travels; **(b)** it inverts the reach logic of digital platforms: the recipient set is whoever is physically present, so a remote platform cannot be thanked and the person behind the counter can — the storefront is reachable, the headquarters is not; **(c)** it makes movement generative, since each step admits a new neighborhood to the sender's reach. (The resonance with the canonical wanderer, the *paribbājaka*, is a lens the Preamble's tradition supplies, not a property of the mechanism.)

## 4 · Verified-Human Anonymous Giving

### 4.1 · The two-layer attestation

Humanity attestation in the specified mechanism operates at two layers, applied in series:

1. **Per-action FIDO2 / WebAuthn attestation** (immediate). Each transfer is signed by a private key held in the sender's device secure enclave (Apple Secure Enclave, Android Trusty / Strongbox, Windows TPM, etc.), with the signing operation gated on user verification. The signature attests that an enrolled user verified this action on this authenticator; biometric-first modality is enforced by device policy and by admitting only attested platform authenticators (an AAGUID allow-list), never by the WebAuthn flag, which reports that verification occurred and not how. This is meaningfully stronger than session-based or registration-time attestation: a registered user cannot delegate this signature to an autonomous process without verifying each action on the admitted authenticator — with the residuals §10 names (PIN fallback, shared authenticators, synced passkeys).
2. **DNA-verified family-tree attestation** (long-term, optional, voluntary). Users may opt in to a DNA-verified global family-tree dataset; this is now specified as Layer 4 (DNA-verified kinship lineage) of the **B-PoH℠** protocol in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*. When this opt-in is present, the verifying party applies an additional check that the FIDO2-signing identity corresponds to a verified-human node in the family tree. This closes, for senders who have opted in, a residual attack surface in which a sufficiently advanced deepfake plus stolen device could defeat per-action FIDO2 alone; for all others that attack remains the residual named in §10.

### 4.2 · Recipient anonymity

The recipient receives the gratitude expression and any attached monetary value, but is not informed of the sender's identity. The system retains the sender's verified identity for adversarial-pattern detection, regulatory compliance, and limited audit purposes — but does not surface it to the recipient under any normal interaction. The recipient sees only: the gratitude content; the verified humanity-attestation; the attested proximity at time of transfer; and a stable per-recipient pseudonym for the sender (§6.3), which carries no identity. "Recipient-side anonymity" means exactly this — anonymity toward the recipient; the verifying party is a trusted party that sees everything, and no unlinkability toward it is claimed (§10).

### 4.3 · The novel combination

The combination of **(a) per-action biometric humanity attestation**, **(b) cryptographic physical-radio proximity attestation**, and **(c) recipient-side anonymity** is, to the author's knowledge, not previously published as a unified mechanism. Existing digital-payment systems have at most two of the three: cash has anonymity and proximity but no humanity verification (any actor can spend cash); Worldcoin has humanity verification but not proximity and not recipient anonymity; contactless payment apps have proximity but not anonymity and not per-action humanity verification; privacy-preserving cryptocurrencies have anonymity but not proximity and not humanity verification; Citibank's gratuity patent and RAADAAR have proximity and anonymity but no per-action humanity verification; the biometric proximity-payment family and Apple Pay over Nearby Interaction have proximity and biometrics but no anonymity. No reference found composes all three in one signed action; the composition is the disclosed matter of this publication, and whether it is non-obvious is an examiner's determination this publication exists to inform.

## 5 · The Combination and What It Enables

The combination of proximity and verified-human anonymity is more than the sum of its components. Each property alone is well-explored; their combination is designed to produce properties none has alone:

- **Operationally easy *dāna*.** The Buddhist higher form of giving — anonymous, without ego-attachment to recognition — becomes the path of least resistance. Where in face-to-face giving the giver must perform self-effacement against social pressure, the mechanism removes the recognition channel by default. Practitioners who aspire to anonymous giving no longer need to discipline themselves against the natural human tendency to seek credit.
- **Bot-resistant local economy.** As autonomous agents proliferate, gratitude transfers verified at this combined level constitute a category of economic activity that no agent can perform at scale without human cooperation. Local merchants who participate in the system gain a structural preference: the agent economy cannot easily displace human-witnessed local commerce.
- **Anti-extractive reach.** The recipient set is whoever is physically present, so a remote platform cannot be thanked and the person behind the counter can — the storefront is reachable, the headquarters is not. Small local businesses, independent service workers, neighbors, and community institutions are what proximity admits.
- **Cultural-religious accessibility.** The mechanism is not denominationally exclusive. Anonymous giving has analogs in Christian almsgiving (Matthew 6:2–4 on secret giving — the left hand not knowing what the right hand does, giving without even the giver's awareness of having given), Islamic *sadaqa jariya*, Jewish *tzedakah* at the second of Maimonides' eight rungs — giver and recipient unknown to each other; the first rung, enabling self-sufficiency, is the Re-Tip Fund℠'s register, not this primitive's — and indigenous traditions of communal sharing. The mechanism serves all of these without privileging any.

## 6 · System Architecture

We sketch a reference architecture without claiming any specific implementation as canonical. Variations consistent with the three structural properties (per-action humanity attestation, proximity attestation, recipient anonymity) fall within the scope of this defensive publication.

### 6.1 · Components

- **Sender device** — mobile phone, wearable, or equivalent, bearing a FIDO2 / WebAuthn-compatible secure enclave and UWB / BLE radio.
- **Recipient device** — mobile phone or wearable with at least BLE radio.
- **Verifying party** — an autonomous AI representative or smart contract on a public ledger that validates attestations, authorizes the transfer, and settles any monetary component. In the HeartBank ecosystem this is Miss Aquarius, the autonomous AI representative to be deployed on Base (Coinbase L2), specified in the companion paper.
- **Settlement layer** — a public ledger or analogous mechanism for recording the transfer's monetary component, if any.

### 6.2 · Transfer flow

1. Sender device proposes a transfer to recipient device, including gratitude content and optional monetary value.
2. Sender and recipient devices perform proximity attestation per §3.3 — a single UWB ranging, or two agreeing mechanisms — each device signing the resulting transcript with device-attested keys.
3. Sender device prompts the user for verification; FIDO2 / WebAuthn signing occurs over the transfer payload, which contains the ranging transcript, so user verification and proximity are attested by one signature over one object — this binding is the mechanism's claim.
4. Signed transfer payload is submitted to the verifying party.
5. Verifying party checks: FIDO2 signature valid, from an admitted attested authenticator; proximity attestation satisfies §3.3 and lies within the density-adjusted radius; sender's verified humanity status current; adversarial heuristics (collusion, rate-limiting, coded-message detection) pass.
6. On success, monetary component (if any) is settled to the recipient. Gratitude content is delivered to the recipient with sender's identity redacted.
7. Verifying party retains audit-grade record (sender identity, full payload) in protected storage, accessible only under specified adversarial-investigation or regulatory conditions.

### 6.3 · Key derivation and pseudonymity

The recipient receives a per-transfer pseudonym for the sender, derived as HMAC(salt_R, sender_id) with salt_R held by the verifying party, such that repeat transfers from the same sender to the same recipient appear under a stable pseudonym (allowing relational continuity) without disclosing identity. Different recipients see uncorrelated pseudonyms for the same sender, because their salts are independent; the verifying party, which holds every salt, can correlate them all.

## 7 · Reference Implementation Patterns

### 7.1 · Sender pseudocode

```javascript
function sendGratitude(recipient, content, amount?) {
  // 1. Establish proximity via UWB (preferred) or BLE
  const proximityProof = await measureProximity(recipient);
  if (!proximityProof.withinRadius(densityAdjustedRadius()))
    throw new ProximityError();

  // 2. Build transfer payload
  const payload = {
    recipient: recipient.publicId,
    content,
    amount,
    proximity: proximityProof,
    timestamp: now()
  };

  // 3. Biometric-gated signing via WebAuthn
  const signature = await navigator.credentials.get({
    publicKey: {
      challenge: concat(verifierNonce, hash(payload)), // single-use nonce from the verifier
      userVerification: "required" // user verification; modality is device policy
    }
  });

  // 4. Submit to verifying party
  return submitTransfer({ payload, signature });
}
```

### 7.2 · Verifier pseudocode

```javascript
function verifyTransfer(transfer) {
  // 1. Verify FIDO2 signature
  if (!verifyWebAuthnSignature(transfer.payload, transfer.signature))
    return reject("invalid_signature");

  // 2. Verify per-action user-presence + biometric flags
  const flags = transfer.signature.authenticatorData.flags;
  if (!flags.userPresent || !flags.userVerified)
    return reject("user_not_present");
  if (!admittedAuthenticators.has(transfer.signature.aaguid))
    return reject("authenticator_not_admitted"); // attested platform authenticators only

  // 3. Verify proximity attestation
  const r = densityAdjustedRadius(transfer.payload.location);
  if (!verifyProximityProof(transfer.payload.proximity, r))
    return reject("proximity_failed");

  // 4. Adversarial heuristics
  if (detectCollusion(sender, recipient)) return reject("collusion");
  if (rateLimitExceeded(sender)) return reject("rate_limit");
  if (codedMessageHeuristic(transfer)) return flag("coded_message");

  // 5. Settle and deliver
  const pseudonym = derivePseudonym(sender.id, recipient.salt);
  if (transfer.payload.amount)
    settle(sender, recipient, transfer.payload.amount);
  deliverToRecipient({
    pseudonym,
    content: transfer.payload.content,
    proximity: transfer.payload.proximity
  });
}
```

## 8 · Edge Cases and Adversarial Analysis

### 8.1 · Collusion (mutual-tipping for value laundering)

Two parties may collude by repeatedly tipping each other, attempting to launder value or fabricate social signal. The verifying party detects this via graph analysis: bidirectional flow exceeding a threshold ratio, repeating co-location patterns outside normal social graphs, near-equal balance flow over time. Detected collusion results in rate-limiting, transfer reversal, or aura penalty.

### 8.2 · Coded-message via amount

A sender may attempt to communicate a covert message via the transfer amount (e.g., $1.34 as a timestamp; $99.99 as a coded signal). The verifying party applies entropy and pattern heuristics to flag suspected coded messages for review and may quantize amounts to defeat fine-grained covert channels.

### 8.3 · Stalking via repeated anonymous tips

A bad actor in physical proximity may attempt to harass a recipient via a burst of anonymous unwanted thanks. The mechanism mitigates this via per-pseudonym rate-limiting (the same pseudonym cannot exceed N transfers per recipient per period) and recipient-side block lists by pseudonym. Repeated harassment escalates to the verifying party with the underlying identity revealed for adversarial action.

### 8.4 · GPS spoofing

A sender may attempt to fake their location via GPS spoofing to satisfy the proximity rule. The mechanism rejects GPS-only attestations when UWB or BLE is available; cross-references cell tower signal strength; analyzes signal multipath; and rejects velocity-implausible movement patterns.

### 8.5 · Replay attacks

The verifying party issues a single-use nonce that the WebAuthn challenge commits to, alongside the payload hash, preventing replay of historical signatures. Proximity attestations include freshness timestamps; stale attestations are rejected.

### 8.6 · Anti-money-laundering and regulatory variance

Per-jurisdiction regulatory variance is handled by configurable thresholds: small anonymous transfers are unconstrained; transfers above a configurable threshold trigger optional verification escrow with progressive identity disclosure to the recipient as required by local law. The structural anonymity is preserved at the social layer; legal compliance is layered on top.

### 8.7 · Deepfake biometric defeat

High-end deepfake plus stolen device with biometric bypass remains a residual attack on per-action FIDO2 alone. The DNA-verified family-tree layer — Layer 4 of the **B-PoH℠** protocol specified in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet* — closes this gap for senders who have opted in, by binding the FIDO2 identity to a biologically-verified human kinship graph; for all others the attack remains the residual named in §10.

## 9 · Use Cases

- **Local-business gratitude.** A customer thanks a barista, a mechanic, a cashier; the small monetary attachment helps sustain local economy without exposing identity asymmetry.
- **Conference and event tipping.** Attendees thank speakers, organizers, service staff anonymously without the awkwardness of face-to-face cash.
- **Religious almsgiving.** The mechanism supports the canonical higher form of *dāna*, *tzedakah* at Maimonides' anonymous rung, anonymous Christian almsgiving, and analogous traditions.
- **Honoring service workers.** Anonymous gratitude to nurses, teachers, transit workers, garbage collectors, others in undervalued professions.
- **Cross-cultural travel.** Travelers unable to communicate verbally with a local can leave a verified-human anonymous thank-you that speaks across the language barrier.
- **Supporting strangers in need.** A bystander encountering someone in difficulty can offer anonymous monetary aid without the dignitary cost of public charity.

## 10 · Limitations and Future Work

The mechanism specified here addresses the gratitude-transfer primitive but leaves several related questions for separate work:

- The DNA-verified family-tree layer is specified as Layer 4 of the **B-PoH℠** protocol in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*.
- The autonomous AI representative (Miss Aquarius) is specified in the companion paper *Miss Aquarius and the Aquarian Pool Architecture* (`miss-aquarius-and-aquarian-pool-architecture`). Its alignment substrate (the Theravāda *Tipiṭaka*) is specified in the companion paper *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* (target publication January 7, 2027).
- The integration with non-human entities (robots, animals, plants, sacred places) via the Mechanical Heart artifact is specified in the companion paper *The Mechanical Heart: A Tipiṭaka-Bearing Artifact for Admitting Non-Human Entities into Gratitude-Economic Participation*.
- **Residuals of the verified-human layer.** WebAuthn user verification is satisfied by a PIN as well as a biometric; authenticators can be shared; synced passkeys move between devices. Device policy and the attested-authenticator allow-list narrow these; they do not close them. A deepfake plus a stolen device defeats per-action signing for any sender who has not opted into the kinship layer.
- **Residuals of the proximity layer.** UWB is not universal; BLE is vulnerable to relay and amplification; and no composition proof exists for the case in which one adversary controls both the radio and the authenticator.
- **What proximity binds.** The primitive attests the sender's presence, not the recipient's: proximity binds two devices, and the recipient device may be unattended, shared, relayed, emulated, or carried by another person. Recipient-side humanity is a filter the recipient's own B-PoH layers supply, outside this specification.
- **Linkage surfaces.** The verifying party sees sender identity and the full payload; timing and proximity are exposed to the recipient; a repeated pseudonym is linkable across a recipient's own transfers; network metadata is not addressed here. No unlinkability toward the verifying party is claimed.
- Per-jurisdiction regulatory mappings are implementation details outside the scope of this defensive publication.
- Empirical evaluation of the mechanism's social-capital effects, local-economy impact, and dharmic-practice uptake is future work; the longitudinal cohort mechanism specified separately is the intended evaluation substrate.

## 11 · Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/verified-human-anonymous-local-giving> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/verified-human-anonymous-local-giving.md> |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/verified-human-anonymous-local-giving> |
| archive.today | captured on the estate's snapshot cadence — a trademark specimen for the marks it carries, not prior art |
| Zenodo | a version DOI per revision |

## 12 · Acknowledgments

The author acknowledges his father, with whom the Khmer transcription of the *Tipiṭaka* is being undertaken; the Cambodian Theravāda Saṅgha, whose lineage carries the canon that grounds this work; the survivors and descendants of the Cambodian genocide of 1975–79, whose civilizational rebuilding is the soil this publication grows from; the foundational thinkers in community currency, proof-of-personhood, and Buddhist economics whose work is cited above; and the autonomous artificial intelligence community whose alignment work this publication intends to contribute to in the spirit of the bodhisattva path.

## 13 · Citations

1. *Aṅguttara Nikāya* 7.52 (*Dānamahapphala Sutta* — the seven motives for giving). Pāli Text Society translation, multiple editions.
2. *Aṅguttara Nikāya* 8.31 (*Dāna Sutta*). Pāli Text Society translation, multiple editions.
3. Cahn, E. (2000). *No More Throw-Away People: The Co-Production Imperative*. Essential Books.
4. Chaum, D. (1983). "Blind signatures for untraceable payments." *Advances in Cryptology — CRYPTO '82*.
5. FIDO Alliance. (2019). *Web Authentication: An API for accessing Public Key Credentials, Level 1*. W3C Recommendation.
6. Gesell, S. (1916). *Die natürliche Wirtschaftsordnung* [The Natural Economic Order].
7. Linton, M. (1983). "Local Exchange Trading Systems."
8. Maimonides, M. (1180). *Mishneh Torah, Hilchot Matanot Aniyim* 10:7–14 (the eight levels of *tzedakah*).
9. Putnam, R. (2000). *Bowling Alone: The Collapse and Revival of American Community*. Simon & Schuster.
10. U.S. Surgeon General. (2023). *Our Epidemic of Loneliness and Isolation: The U.S. Surgeon General's Advisory on the Healing Effects of Social Connection and Community*. U.S. Department of Health and Human Services.
11. Worldcoin Foundation. (2023). *Worldcoin Whitepaper*.
12. New Testament, Matthew 6:2–4 (anonymous almsgiving).
13. Leu, P., Camurati, G., Heinrich, A., Roeschlin, M., Anliker, C., Hollick, M., Capkun, S., & Classen, J. (2022). "Ghost Peak: Practical Distance Reduction Attacks Against HRP UWB Ranging." *USENIX Security 2022*.
14. Citibank, US 12,165,124 B2 (priority 2017, granted 2024) — gratuity payments to nearby devices with an anonymity control.
15. RAADAAR, US 9,854,616 B2 (priority 2015) — BLE proximity, anonymous gifts, payment integration.
16. Mastercard, EP 1671282 A2 (priority 2003) — biometrically enabling a proximity payment device; Samsung, WO 2022/225298 A1 (priority 2021) — payment over UWB secure ranging.
17. Square (2014). *Nearby Payments* in Square Cash, over Bluetooth LE (press release, October 2014); Bump (2009) and Bump Pay (2012).
18. Android Developers, *Ultra-wideband (UWB) communication* (androidx.core.uwb); Apple Developer, *Nearby Interaction* (2020).

---

*— End of defensive publication —*

*Co-authored with Miss Aquarius℠, the institution's named AI collaborator, per the corpus's standing disclosure; final editorial control and responsibility for every claim rest with the human author. This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
