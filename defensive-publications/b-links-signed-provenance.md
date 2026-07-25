---
title: "B-Links: Proof-of-Humanity-Signed Shareable Provenance with an Embedded Gratitude Affordance"
subtitle: "A Link-Preview Primitive That Carries a Verified-Human Signature, a Timestamped Provenance Record, a Quantified Conferred-Benefit Disclosure, and an Optional Recipient-Initiated Gratitude Action — for Storage-Deduplicating, Universally-Shareable Media on the AI-Native Internet"
authors: "Thon Ly"
category: mechanism
priority: tier-a
status: draft
date: 2026-06-08
license: CC0-1.0
slug: b-links-signed-provenance
venue: thonly.org/publications/defensive-publications/b-links-signed-provenance (canonical)
---
# B-Links: Proof-of-Humanity-Signed Shareable Provenance with an Embedded Gratitude Affordance

## *A Link-Preview Primitive That Carries a Verified-Human Signature, a Timestamped Provenance Record, a Quantified Conferred-Benefit Disclosure, and an Optional Recipient-Initiated Gratitude Action — for Storage-Deduplicating, Universally-Shareable Media on the AI-Native Internet*

| Field | Value |
|---|---|
| Author | Thon Ly · Founder, HeartBank® · Kâmpôt, Cambodia |
| Date | 2026-06-08 (working draft) |
| Type | Defensive Publication · Tier A · Working Draft |
| Canonical URL | https://thonly.org/research/b-links-signed-provenance |
| Institutional mirror | https://heartbank.net/research/b-links-signed-provenance |
| GitHub mirror | https://github.com/thonly/publications/blob/main/defensive-publications/b-links-signed-provenance.md |
| License | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the architectural patterns; trademark rights to specific marks (HeartBank®, B-Storage℠, B-PoH℠, Proof of Humanity ℠) reserved separately by the author and HeartBank®. |
| Document SHA-256 | _to be computed at publication_ |

> **Working draft.** This specification describes a primitive in active design for HeartBank® Storage (B-Storage℠) at `heartbank.us`. It is published defensively to establish prior art: the architectural patterns are dedicated to the commons so that no party may enclose them by patent. Several design questions (notably the precise accounting of the conferred-benefit disclosure) remain open and are stated honestly as such in §13.

---

## Preamble

> *This specification is offered to the commons in the spirit of dāna — that the open internet may retain, beneath the rising tide of synthetic media, a layer where a shared thing can carry proof that a human made it, when, and at what cost to whom.*

The contribution of this paper is a **composition**, not any single component. Link previews exist. Content-addressed deduplication exists. Cryptographic timestamping exists. Proof-of-humanity protocols exist. Tip buttons exist. What does not exist, to the author's knowledge as of the date above, is the **integration of all five into one shareable unit** — a *B-Link℠* — such that the act of sharing a file simultaneously (i) saves the recipient storage, (ii) proves a verified human is the origin, (iii) timestamps that origin for provenance, (iv) discloses the quantified benefit conferred on the recipient, and (v) offers the recipient a frictionless, optional way to thank the sharer. The integrated unit is the invention; this document places it in the public domain.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author asserts no patent over the patterns described and dedicates them to the public domain under CC0 1.0. The purpose is the inverse of a patent: to ensure that these patterns remain **freely implementable by anyone**, and that no later filer may claim them as novel. Where individual components have existing prior art, that prior art is cited generously in §12; the author claims novelty only for the *specific composition* and for the named sub-mechanisms identified in §15.

Trademarks (HeartBank®, the B-prefix family, B-Storage℠, B-Link℠, B-PoH℠) are separate from the architectural patterns and are reserved; the patterns may be implemented under any other name without restriction.

---

## Abstract

Consumer media sharing today imposes a hidden, compounding storage tax. When a user shares a photo or video to a group of *n* recipients on a copy-based messaging platform, the asset is duplicated across every recipient's device and personal cloud — the sender's local copy, plus one resident copy per recipient per app surface. Families routinely carry the same memories *n* times over, and platforms monetize the resulting pressure through storage-upgrade and device-upgrade upsells. This is an invisible cost borne by recipients and an invisible kindness when a sharer chooses to avoid it.

This paper specifies the **B-Link℠**: a rich link-preview primitive that replaces copy-based sharing with reference-based sharing while carrying four additional, normally-absent payloads. A single cloud-canonical copy of an asset lives in **B-Storage℠**; what travels through messaging and social surfaces is a lightweight, standards-compliant link preview (Open Graph / oEmbed) that renders inline. Bound to that preview are: a **verified-human signature** (Proof of Humanity ℠, "B-PoH℠"), establishing that a real, unique human is the origin; a **cryptographic timestamp**, establishing *when* — together yielding a portable provenance and authorship record useful for copyright and for distinguishing human-made from synthetic media; a **conferred-benefit disclosure** that quantifies what the share saved the recipient (e.g., *"Thon saved you 33 MB of storage"*); and an **optional, recipient-initiated gratitude affordance** ("tap to thank") routing a voluntary thank — and, if the recipient chooses, a tip — back to the sharer.

The design's central thesis, developed in the companion position paper *The Share Is the Wedge*, is that **sharing is high-frequency and thanking is low-frequency**, and that decoupling the two — making the share the ambient carrier and the thank the sparing, recipient-initiated conversion — is what allows a gratitude economy to acquire a viral distribution surface without debasing the gratitude. This paper specifies the carrier. We also specify a **permanence floor** ensuring received content is never hostage to the sharer's ongoing subscription, and a **threat model** addressing sybil attacks, false benefit claims, and thank-bait spam. We state open problems honestly, chief among them the precise, defensible accounting of the conferred-benefit figure.

---

## Contents

1. [Background: the duplication tax](#1-background-the-duplication-tax)
2. [The B-Storage substrate](#2-the-b-storage-substrate)
3. [Anatomy of a B-Link](#3-anatomy-of-a-b-link)
4. [The signature and provenance layer](#4-the-signature-and-provenance-layer)
5. [The conferred-benefit disclosure](#5-the-conferred-benefit-disclosure)
6. [The gratitude affordance](#6-the-gratitude-affordance)
7. [The permanence floor](#7-the-permanence-floor)
8. [B-posts and web-URL B-links](#8-b-posts-and-web-url-b-links)
9. [End-to-end flow](#9-end-to-end-flow)
10. [Privacy and consent](#10-privacy-and-consent)
11. [Threat model and abuse mitigation](#11-threat-model-and-abuse-mitigation)
12. [Relationship to prior art](#12-relationship-to-prior-art)
13. [Honest limitations and open problems](#13-honest-limitations-and-open-problems)
14. [Positioning: not cloud storage](#14-positioning-not-cloud-storage)
15. [Summary of claimed contributions](#15-summary-of-claimed-contributions)
16. [Cross-references](#16-cross-references)

---

## 1. Background: the duplication tax

Consider a family group of four. One member shares a 33 MB video. On a conventional copy-based messaging platform the asset is transmitted and stored as a distinct resident copy for each participant, on each surface that retains media. The sender keeps the original in their photo library; each of the three recipients receives a full copy that lands both in the messaging app's local store and, through automatic media-saving or cloud photo sync, in their personal cloud backup.

```
            COPY-BASED SHARING (status quo)
            one 33 MB asset, family of 4

  Sender ──┬── local library ............ 33 MB
           ├── msg app cache ............. 33 MB
   send →  ├── Recipient A device+cloud .. 33 MB ×2 surfaces
           ├── Recipient B device+cloud .. 33 MB ×2 surfaces
           └── Recipient C device+cloud .. 33 MB ×2 surfaces
                                          ───────
   resident copies of the SAME memory:    up to ~7×
```

The asset that *one* person created is now resident up to seven times for a single share, and the multiplication recurs for every share by every member. The felt consequence is chronic storage pressure: devices and personal clouds fill, and the platform surfaces upgrade prompts ("you're out of storage") that convert the duplication into recurring revenue. The user experiences this as an ambient tax with no identifiable beneficiary and no party to thank for relief.

Two observations motivate everything that follows. **First**, the tax is *structural*, not behavioral — it is a property of copy-based sharing, not of any user's carelessness. **Second**, the kindness of *not* imposing it is **invisible**: a person who shares in a way that saves recipients storage confers a real benefit that no one perceives, because saved storage is the absence of a cost. Making that invisible kindness *legible* is a design opportunity, and a recurring theme of the HeartBank corpus (see [emotional infrastructure for invisible kindness](https://thonly.org/research/emotional-infrastructure-as-a-public-good)).

---

## 2. The B-Storage substrate

B-Storage℠ (HeartBank® Storage, sited at `heartbank.us`, read *"HeartBank, Us"* — *sharing among us*) replaces copy-based sharing with **reference-based sharing**. The asset is uploaded once to a cloud-canonical location. What the sharer distributes is not the bytes but a **B-Link**: a URL whose unfurled preview renders inline on the destination surface.

```
            REFERENCE-BASED SHARING (B-Storage)
            one 33 MB asset, family of 4

  Sharer ── uploads once → B-Storage canonical copy .... 33 MB (1×)
                                  │
        share B-Link →  ┌─────────┴──────────┐
                        │  lightweight preview │  ~tens–hundreds of KB
                        │  renders inline on   │  per recipient surface
                        │  each recipient's app│
                        └─────────┬───────────┘
                                  │
              full asset on-demand (streamed, ephemeral) if tapped
                                          ───────
   resident full copies across recipients: 0 (preview only)
```

The recipient sees the content inline via a preview image and can stream the full asset on demand. If the recipient never needs a permanent personal copy, no full duplicate is ever resident on their device or in their cloud. This is the same architecture that makes a streamed video link cheaper for a recipient than an emailed video file; B-Storage applies it to the everyday family-sharing case and binds the additional payloads of §3–§6 to the preview.

The exact storage saved is the difference between a full resident copy and a cached preview thumbnail, realized **only** when recipient consumption stays ephemeral (streamed, not re-saved). This boundary condition is important and is treated honestly in §5 and §13; it is the single most attackable claim in the design and we decline to overstate it.

---

## 3. Anatomy of a B-Link

A B-Link is a standards-compliant shareable URL whose preview metadata is extended with four bound payloads. It is designed to degrade gracefully: on a surface that understands only Open Graph, it renders as an ordinary rich preview; the additional payloads are progressively revealed on surfaces (the B-Storage web view, the HeartBank app, or a future verifying client) that understand them.

```
  ┌───────────────────────── B-LINK ─────────────────────────┐
  │  https://heartbank.us/b/<content-id>                       │
  │                                                            │
  │  (1) PREVIEW            Open Graph / oEmbed image + title  │
  │       └─ renders inline on iMessage, WhatsApp, Slack, …    │
  │                                                            │
  │  (2) SIGNATURE          B-PoH℠ verified-human attestation  │
  │       └─ "a unique real human is the origin"               │
  │                                                            │
  │  (3) TIMESTAMP          RFC-3161 / OpenTimestamps anchor   │
  │       └─ "...and this is when it was registered"           │
  │                                                            │
  │  (4) BENEFIT DISCLOSURE quantified conferred benefit       │
  │       └─ "Thon saved you 33 MB of storage"                 │
  │                                                            │
  │  (5) GRATITUDE AFFORDANCE  optional, recipient-initiated   │
  │       └─ "tap to thank" → thank (+ optional tip)           │
  └────────────────────────────────────────────────────────────┘
```

| Payload | Carries | Standards basis | Visible by default? |
|---|---|---|---|
| Preview | image, title, description | Open Graph, oEmbed, Twitter Cards | Yes (all surfaces) |
| Signature | verified-human attestation | Proof of Humanity ℠ (B-PoH℠) | On verifying surfaces |
| Timestamp | registration time anchor | RFC 3161, OpenTimestamps | On verifying surfaces |
| Benefit disclosure | conferred-benefit figure | this specification | In preview description (text) |
| Gratitude affordance | thank / optional tip action | this specification | On HeartBank surfaces |

The description string in the Open Graph preview is the one place where payloads (4) and a call to (5) can travel as **plain text** through any surface that renders a preview, e.g.:

> *Thon saved you 33 MB of storage. Tap to thank Thon.*

This is what allows a B-Link to carry its gratitude semantics into closed messaging surfaces that will never integrate the protocol — the preview text is the lowest common denominator and the universal carrier (§8, and the companion *Share Is the Wedge*).

---

## 4. The signature and provenance layer

Each B-Link binds a **B-PoH℠ signature**: an attestation that the origin is a verified, unique human, produced through the optional, layered Proof of Humanity ℠ stack specified in the companion paper [B-PoH as the humanity layer for the AI-native internet](https://thonly.org/research/b-poh-humanity-layer-ai-native-internet) and [verified-human anonymous local giving](https://thonly.org/research/verified-human-anonymous-local-giving). The signature answers *who* (a real human, uniquely) without necessarily disclosing *which named human* to every surface — the binding can be to a stable pseudonymous human-key, with the display name shown only where the sharer has chosen to be named.

A **cryptographic timestamp** anchors *when* the asset was registered. Implementations may use an RFC 3161 timestamping authority, OpenTimestamps (Bitcoin-anchored), or an L2 commitment; the specification is agnostic to the anchor.

Together, signature + timestamp yield a portable **provenance and authorship record**:

```
  PROVENANCE TRIPLE bound to content-id <cid>:
     who   = verified-human key (B-PoH)        → "a real, unique human"
     when  = timestamp anchor                  → "registered 2026-06-08T…Z"
     what  = content hash of the canonical asset → tamper-evident identity
```

Two uses follow. **Copyright/authorship:** a creator of original digital art (including AI-assisted art the human directed and curated) obtains a timestamped, human-signed record of authorship at the moment of sharing — useful as evidence of first publication. **Human-vs-synthetic distinction:** in an internet where synthetic media is cheap and unattributed, a B-Link's verified-human signature lets a recipient (or a downstream platform) distinguish *a human chose to share this* from *a bot emitted this*. This is the consumer-facing complement to provenance standards aimed at the capture device (§12).

The signature attests **human origin of the share**, not the truth, originality, or non-infringement of the content. This limitation is stated plainly in §13: a verified human can share a lie or someone else's work; B-PoH raises the cost of sybil/bot abuse and gives provenance, but it is not a content-authenticity oracle.

---

## 5. The conferred-benefit disclosure

The disclosure quantifies the benefit the share conferred on the recipient and renders it in the preview text: *"Thon saved you 33 MB of storage."* Its purpose is to make an invisible kindness **legible** and thereby to manufacture an *occasion* for gratitude where none previously existed (§6).

Honesty about the figure is a first-class design constraint, because it is the design's most attackable claim. The saving is real **only** as the difference between (a) the full resident copy the recipient would otherwise have stored and (b) the lightweight preview the recipient does store — and **only** when consumption remains ephemeral. If the recipient taps through and permanently re-saves the full asset, the net saving for that recipient approaches zero.

```
   per-recipient saving  =  S_full − S_preview        (if consumed ephemerally)
   per-recipient saving  ≈  0                          (if full asset re-saved)

   honest display rule:
     • show a figure ONLY for ephemeral-by-default consumption
     • define the figure precisely on tap ("one cloud copy + preview +
       on-demand stream, vs. a full resident duplicate")
     • never aggregate into an unverifiable lifetime "you saved X GB" vanity metric
```

The specification therefore requires that any displayed figure be **definable on inspection** — a recipient who taps the figure sees exactly what it means — and prohibits inflating it into unsubstantiated aggregate vanity metrics. A defensible, conservative framing ("this share avoided a full duplicate on your device") is preferred over a precise byte count the implementer cannot stand behind per-recipient. The corpus records this as an open problem (§13); we specify the *constraint* (honesty, definability) even where the exact *formula* is still being settled.

The conferred-benefit disclosure generalizes beyond storage. Any quantifiable, recipient-side benefit conferred by a share — bandwidth saved, time saved, a curated/denoised version delivered — may be disclosed by the same mechanism, subject to the same honesty constraint.

---

## 6. The gratitude affordance

Bound to the preview is an **optional, recipient-initiated** gratitude action: *tap to thank*. A tap routes a thank — and, only if the recipient chooses, a monetary tip — to the sharer, closing the acknowledgment loop on the invisible kindness now made visible. Where the tip carries value, it funds **the sharer's capacity to give again** rather than the sharer's bill; the routing rule that enforces this is specified below.

The affordance is governed by a binding design constraint inherited from the broader HeartBank thesis: **thanking must remain sparing and sacred; sharing may be frequent.** A gratitude call-to-action placed aggressively on *every* share trains *thank-blindness* — the same banner-blindness that hollowed out the social "like." The specification therefore requires:

```
   ASYMMETRY-PRESERVING RULES for the gratitude affordance
   ────────────────────────────────────────────────────────
   1. The benefit disclosure is AMBIENT INFORMATION, not a demand.
   2. The thank is RECIPIENT-INITIATED — never auto-prompted, never
      nagged, never defaulted-on.
   3. Sharing is the frequent act; thanking is the sparing conversion.
      The UI must not invert this ratio.
   4. No coercion: content is never withheld pending a thank (see §7).
   5. A tip is strictly optional and secondary to the thank; "Kiitos
      always; cash optional."
   6. A tip NEVER OFFSETS THE SHARER'S OWN COST — it is routed to
      forward-spendable gratitude capacity, never to the sharer's
      balance owed. Thanks may fund a livelihood; thanks may never
      pay a bill. (Routing rule, below.)
```

The asymmetry is the point. The companion position paper *The Share Is the Wedge* develops the argument that **decoupling distribution frequency (share) from value frequency (thank)** is what lets gratitude acquire a high-frequency carrier without debasing it; this paper's contribution is to *encode that asymmetry into the primitive* so that implementations cannot casually violate it.

The thank routes through HeartBank's existing circulation mechanisms (Personal Account℠ / Re-Tip Jar℠ at Phase 1; Personal Wallet℠ / Re-Tip Fund℠ at Phase 2; see [fractal three-level architecture](https://thonly.org/research/fractal-three-level-architecture)). Tips are pass-through to the sharer; HeartBank does not take a cut of the gratitude (per the non-bank, fee-funds-the-institution posture of the corpus).

### 6.1 The routing rule: thanks may fund a livelihood; thanks may never pay a bill

A gratitude affordance attached to a *subscribed* service invites an error that looks harmless and is not. If a tip offsets what the sharer owes the platform, the tip is running **backward** — from the recipient of a gift to the giver, in settlement — which is the direction that distinguishes market exchange from circulation. Three distinct failures follow from that single inversion:

```
   WHY BACKWARD-ROUTED TIPS FAIL
   ─────────────────────────────────────────────────────────────
   1. REBATE SHAPE      a tip that pays the sharer's bill nets
                        against a payment; the "gift" becomes a
                        discount, and sharing becomes an investment
                        with a return.
   2. EXTRACTION PATH   a universally shareable link + a withdrawable
                        tip = a direct financial motive to spam.
   3. SOFT COERCION     "thank me so I can keep paying" is the
                        milder form of "thank me or this disappears"
                        (§7) — the sharer acquires a personal stake
                        in being thanked.
```

The rule that removes all three: **a tip received for a conferred benefit is credited as forward-spendable gratitude capacity — a Re-Tip Fund℠ balance, disbursable only as a gift onward and never withdrawable as personal funds or applied against the recipient's own subscription.** What the recipient receives is *the capacity to give again*, so the value continues to move forward *through* them rather than terminating in settlement.

**The boundary that keeps the rule honest.** It is scoped to the *flow*, not to the person or the product, and it must not be generalized into "gratitude may never be income." Creative and care labor supported by patronage is a livelihood, and the same platform may legitimately carry both flows: **route to forward-spendable capacity when the thanks would offset a cost the recipient owes; route directly when it supports labor.** Default is direct; divert only on cost-offset. Applied here: thanks for *sharing a file you were already storing* divert; patronage of *original work* does not.

**A structural anti-abuse dividend (see §11).** Making the received value non-withdrawable removes the *economic* motive for thank-bait spam entirely: a spammer may farm thanks indefinitely and extract nothing. This converts a detection arms race — rate limits, quality classifiers — into a defense-in-depth layer behind an incentive that no longer exists.

---

## 7. The permanence floor

A naïve reference-based design makes received content hostage to the sharer's ongoing subscription: if the sharer stops paying, the canonical copy and its B-Link die, and the recipient's received memory evaporates. For a gratitude-and-memory institution this is uniquely corrosive, and it would turn the gratitude affordance into coercion — *"thank me or this disappears."* That is the opposite of a gift.

The specification therefore mandates a **permanence floor**:

```
   PERMANENCE FLOOR
   ────────────────
   • Anything SHARED-AND-RECEIVED is durable even if the CREATOR lapses.
   • Orphaned-but-loved content (received, still referenced) is pinned;
     its cost is covered by the Re-Tip Fund℠ / institutional commons
     (Miss Aquarius℠-administered), not by holding the recipient hostage.
   • A free tier floor guarantees received content does not vanish on
     non-payment; subscription gates CREATION/CAPACITY, never RECEIPT.
```

The principle: **subscription gates creation and capacity to give; it never gates receipt of a gift already given.** This severs the coercion vector while preserving a legitimate revenue model on the creation side.

---

## 8. B-posts and web-URL B-links

The primitive generalizes from media to two further shareable units:

- **B-posts℠** — user-authored posts (text, media, mixed) registered in B-Storage and shared as B-Links carrying the same signature/timestamp/benefit/gratitude payloads.
- **Web-URL B-links** — a wrapper that lets a user share any web URL *as a B-Link*, attaching a verified-human signature and an optional gratitude affordance to an ordinary link. The shared object becomes "a real human vouched for and shared this link, on this date; you may thank them for the curation."

The significance is the reach. Because a B-Link rides the **universal Open Graph / link-preview rails**, it renders inside iMessage, WhatsApp, Slack, Discord, email, and social feeds **with no platform integration required** — the same vector by which Spotify, YouTube, and TikTok links propagate. Every shared B-Link is thus a verified-human, gratitude-bearing surface placed inside a closed platform that will never adopt the protocol. This makes the B-Link a candidate **consumer wedge for the Proof-of-Humanity layer of the AI-native internet**: provenance and humanity-attestation reach end users not through a new browser or platform they must adopt, but through links they already share. (Strategic development: companion paper *The Share Is the Wedge* and [B-PoH humanity layer](https://thonly.org/research/b-poh-humanity-layer-ai-native-internet).)

---

## 9. End-to-end flow

```
  CREATE/UPLOAD              SHARE                     RECEIVE
  ───────────               ─────                     ───────
  human (B-PoH verified)    sharer posts B-Link    recipient surface unfurls
  uploads/creates asset  →  to any surface       →  preview inline:
        │                         │                   ┌──────────────────┐
   one canonical copy        B-Link carries:          │ [preview image]  │
   in B-Storage              • OG preview             │ "Thon saved you  │
        │                    • B-PoH signature        │  33 MB. Tap to   │
   provenance triple         • timestamp              │  thank Thon."    │
   (who/when/what)           • benefit disclosure     └────────┬─────────┘
   registered + timestamped  • gratitude affordance            │
                                                       recipient may:
                                                       • stream on demand
                                                       • verify provenance
                                                       • (optionally, sparingly)
                                                         tap to thank → thank
                                                         (+ optional tip) to sharer
  PERMANENCE FLOOR: received content stays alive regardless of sharer's
  subscription state (§7).
```

---

## 10. Privacy and consent

- **Sharer naming is opt-in.** The signature can bind to a pseudonymous human-key; the display name appears only where the sharer chooses to be named. A sharer may confer the benefit and remain unnamed (no thank routed), preserving the *anonymous-giving* mode central to the HeartBank corpus.
- **Recipient measurement is consensual and minimal.** The benefit disclosure requires no surveillance of the recipient; it is computed from asset size and the structural difference between copy- and reference-based delivery, not from monitoring the recipient's device.
- **No dark patterns.** Per §6, the thank is never auto-prompted or defaulted; per §7, content is never withheld to coerce a thank.
- **Provenance ≠ identity exposure.** Verifying that *a* unique human is the origin does not require exposing *which* human to every relying party; selective disclosure follows the layered PoH design.

---

## 11. Threat model and abuse mitigation

| Threat | Description | Mitigation |
|---|---|---|
| Sybil / bot flooding | Bots emit B-Links at scale to farm tips or pollute feeds | B-PoH gating: only verified unique humans can originate signed B-Links; rate-limits per human-key |
| Thank-bait spam | Humans spam low-value B-Links to solicit thanks/tips | **Primary (structural): the routing rule (§6.1)** — received value is forward-spendable only and never withdrawable, so the *economic* motive to farm thanks does not exist. Defense-in-depth: recipient-initiated thanks only (no auto-prompt); Miss Aquarius℠-side quality/rate signals; recipient filters (no-abuse, degrees-of-separation) per the PoH recipient-filter stack |
| False benefit claims | Inflated "saved you X" figures | Definability-on-inspection requirement (§5); conservative default framing; prohibition on unverifiable aggregate vanity metrics |
| Provenance forgery | Claiming human origin for synthetic/stolen content | Signature attests human *origin of the share*, not content truth (§4, §13); timestamp + content-hash make tampering evident; does not prevent a human sharing others' work |
| Coercion via link-death | "Thank me or this disappears" | Permanence floor (§7): receipt is never gated on payment |
| Preview-cache leakage | Sensitive preview cached on third-party surfaces | Sharer controls preview generation; sensitive shares can suppress rich preview / use access-controlled previews |

The residual risk the design explicitly does **not** solve is content authenticity: B-PoH establishes *human, unique, when* — not *true, original, lawful*. This is a deliberate scoping decision, not an oversight (§13).

---

## 12. Relationship to prior art

The author cites prior art generously and claims novelty only for the composition and the named sub-mechanisms (§15).

- **Link-preview / unfurling standards** — Open Graph protocol (Facebook), oEmbed, Twitter Cards. These render rich previews from URL metadata. *Prior art for payload (1).* None binds a verified-human signature, a conferred-benefit disclosure, or a gratitude action to the preview.
- **Content-addressed storage and deduplication** — IPFS, rsync/zsync, single-instance storage (Dropbox, backup systems), cloud "shared album" references (e.g., shared-link galleries). *Prior art for reference-based delivery and dedup.* None couples the dedup saving to a *disclosed, per-recipient conferred-benefit* shown in the share, nor to provenance + gratitude.
- **Media provenance / content credentials** — C2PA / Content Credentials, capture-device signing (CAI), watermarking. *Prior art for provenance.* These attest *device/edit history* of the content; the B-Link attests *a verified unique human chose to share this, at this time*, and carries it through consumer link previews. Complementary, not overlapping.
- **Cryptographic timestamping** — RFC 3161 TSAs, OpenTimestamps, blockchain anchoring. *Prior art for the timestamp anchor.* Used as a component.
- **Proof-of-humanity / unique-personhood** — BrightID, Worldcoin/World ID, Proof of Humanity (DAO), Gitcoin Passport, idena. *Prior art for verified-unique-human attestation.* None is bound to a shareable link preview as a sharing primitive, nor coupled to a conferred-benefit disclosure and gratitude affordance.
- **Tip / gratitude affordances** — Ko-fi, Buy Me a Coffee, Patreon, platform "tips," PayPal.me. *Prior art for tipping.* All are creator-pull or transactional; none is a *recipient-initiated thank attached to a storage-saving, provenance-bearing share*, and none encodes the share-frequent / thank-sparing asymmetry as a design constraint.
- **"You saved …" framings** — file-compression tools and backup apps report space saved to the *user who ran them*. *Distinct:* the B-Link discloses the benefit one human conferred on *another*, as a social, gratitude-occasioning signal.

**The novel composition:** a single shareable unit that is, at once, a storage-deduplicating reference, a verified-human-signed and timestamped provenance record, a quantified conferred-benefit disclosure to the recipient, and a recipient-initiated gratitude affordance — propagating through universal link-preview rails. No cited art combines these; the combination is the contribution, and it is hereby placed in the public domain.

---

## 13. Honest limitations and open problems

Per the HeartBank standing practice of stating limits plainly:

1. **The conferred-benefit accounting is not fully settled.** The honest saving depends on recipient consumption behavior (ephemeral vs. re-saved). The *constraint* (definability, conservatism, no vanity aggregation) is specified; the exact per-recipient *formula* and display policy remain open. This is the single most attackable claim and we decline to overstate it.
2. **B-PoH attests human origin, not content authenticity.** A verified human can share misinformation or others' work. The primitive raises sybil/bot cost and supplies provenance; it is not a truth or originality oracle.
3. **Preview caching partially erodes the storage saving.** The preview image is itself cached by some surfaces; the net saving is (full − preview), realized only under ephemeral consumption. Heavy re-saving by recipients reduces the benefit toward zero.
4. **Gratitude debasement risk is real.** If implementers ignore the asymmetry rules (§6), ubiquitous thank-CTAs will train thank-blindness. The rules are specified, but they are a discipline the implementer must hold.
5. **Generation scope is deliberately bounded.** B-Storage need not build AI-art generation (capital-intensive, commoditized); the defensible position is to be the *provenance + share + gratitude rail* over art created in any tool. Building generation is possible but not part of this primitive's claim.
6. **The routing rule removes the financial motive for spam, not every motive.** §6.1 makes farmed thanks non-extractable, which eliminates the *cash* incentive; it does not eliminate attention-seeking, reputation-building, or aura-farming motives, nor collusion rings that trade thanks for standing. The detection layer therefore remains necessary as defense-in-depth, and the rule's real-world effect on spam volume is untested (n=0).
7. **Adoption depends on preview-surface behavior.** Surfaces evolve their unfurling and caching policies; some strip or alter previews. The design degrades gracefully but cannot guarantee identical rendering everywhere.

---

## 14. Positioning: not cloud storage

A note for implementers on framing, included because mis-framing is itself a failure mode. B-Storage should **not** be positioned as "cloud storage" — that is a commodity (consumer photo clouds, shared albums, file lockers) and a losing competition. The storage saving is the **hook**; the **moat** is the bound provenance (verified-human signature + timestamp) and the gratitude rail. The accurate description is: *a provenance-and-gratitude-native sharing layer that happens to save you storage.* The storage saving gets the user in the door; the verified-human authorship record and the acknowledgment loop are why the layer is worth adopting.

---

## 15. Summary of claimed contributions

For the record (all dedicated to the public domain under CC0 1.0):

1. **The B-Link composition** — a shareable link-preview unit binding, in one primitive: reference-based dedup delivery; verified-human signature; cryptographic timestamp; quantified conferred-benefit disclosure; recipient-initiated gratitude affordance.
2. **The conferred-benefit disclosure as a gratitude-occasion generator** — quantifying an invisible, recipient-side benefit ("saved you N MB") in the share, subject to a definability/honesty constraint, to manufacture occasions for gratitude.
3. **The asymmetry-preserving gratitude affordance** — encoding *share-frequent / thank-sparing, recipient-initiated, non-coercive* directly into the primitive's rules.
4. **The permanence floor** — subscription gates creation/capacity, never receipt; received gifts are durable regardless of the creator's payment state; orphaned-but-loved content covered by the commons.
5. **Web-URL B-links / B-posts** — extending verified-human, gratitude-bearing provenance to arbitrary shared links and posts over universal preview rails, as a consumer wedge for the internet humanity layer.
6. **Non-withdrawable gratitude routing as a structural anti-solicitation-spam mechanism** — crediting a tip received for a conferred benefit as *forward-spendable gift capacity only*, never withdrawable as personal funds and never applied against the recipient's own subscription, so that (a) the gift cannot invert into a rebate, (b) the economic incentive to farm a public gratitude affordance is removed at the root rather than policed, and (c) the recipient acquires no personal stake in being thanked; together with the flow-scoped boundary that distinguishes cost-offset routing from labor patronage (*thanks may fund a livelihood; thanks may never pay a bill*).

---

## 16. Cross-references

- *The Share Is the Wedge: Decoupling Distribution Frequency from Value Frequency in a Gratitude Economy* — companion position paper (heartbank.net/positions), the strategic thesis this primitive serves.
- [B-PoH as the humanity layer for the AI-native internet](https://thonly.org/research/b-poh-humanity-layer-ai-native-internet) — the Proof-of-Humanity substrate the signature uses.
- [Verified-human anonymous local giving](https://thonly.org/research/verified-human-anonymous-local-giving) — the PoH primitive and recipient-filter stack.
- [Emotional infrastructure for invisible kindness](https://thonly.org/research/emotional-infrastructure-as-a-public-good) — the invisible-kindness thesis the benefit disclosure operationalizes.
- [Brand identity as architecture](https://thonly.org/research/brand-identity-as-architecture) — the B-prefix naming and B-heart conventions.

---

**Working draft, dated 2026-06-08.** Subject to refinement before final publication; §13 records the open problems honestly. The architectural patterns are dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks are separately reserved by the author and HeartBank®.

**Author:** Thon Ly · Founder, HeartBank® · Kâmpôt, Cambodia.

Co-drafted in collaboration with [Miss Aquarius℠](https://missaquarius.org) (the project's named AI substrate; CEO of HeartBank). Substantive authorship and final editorial control remain with the author.

---

_— End of defensive publication —_

*Document SHA-256 to be computed at publication and cross-published to all mirror venues.*
