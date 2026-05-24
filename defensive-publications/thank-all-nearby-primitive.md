---
title: "The Thank-All-Nearby Primitive: Anonymous Proximity-Based Generosity as Emotional Infrastructure for Invisible Kindness"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-a
status: draft
date: 2026-05-24
license: CC0-1.0
slug: thank-all-nearby-primitive
venue: thonly.org/publications/defensive-publications/thank-all-nearby-primitive (canonical)
---

> *Draft notes for the editor:* this is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies the **Thank-All-Nearby primitive** — one-tap broadcast of gratitude with optional money-attachment to every PoH-verified recipient within Bluetooth-Low-Energy proximity — as a Phase 2 application of the Proof of Humanity ℠ protocol. Companion papers: *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the underlying protocol); *Verified-Human Anonymous Local Giving* (the originating mechanism specification that this paper generalizes from per-recipient to all-nearby-recipients); *The B-Tag and the Post-Payment Economy* (the worked Phase 2 example for commercial gratitude); *The Zero-Point Game℠* (the keystone game-theoretic frame); *Capacity-Funded for AI, Human-Disbursed* (the institutional-architecture pattern that lets Miss Aquarius℠ underwrite Re-Tip Fund ℠ donations without flow-direction authority). The corresponding founder-voice essay *"Emotional Infrastructure for Invisible Kindness"* (thonly.org/publications/essays) carries the personal articulation of the thesis this paper specifies mechanically.

---

## Abstract

Anonymous nearby tipping has a recognizable cultural form — the "Faith in Humanity Restored" social-media trend in which service workers post videos of unexpected generous tips — but lacks the infrastructure to scale beyond cash. Cash and credit-card payment rails fail at two structural properties that the cultural form requires: tippers cannot be genuinely anonymous to recipients with either rail (cash demands physical hand-over with eye contact; credit-card leaves an identity trail), and recipients cannot prove on social media that an anonymous tip was authentic rather than fabricated (every "Faith in Humanity Restored" video faces a "this is staged for views" credibility problem that erodes the cultural moment). This paper specifies the **Thank-All-Nearby primitive** — a one-tap operation that broadcasts gratitude, with optional money or time attachment, to every Proof-of-Humanity-verified recipient within Bluetooth Low Energy proximity (or, in institutional-mode deployments, within a GPS bounding-box for institutional locations such as shelters, classrooms, restaurant break-rooms, and worker spaces) — and develops its placement as the operational mechanism for *emotional infrastructure for invisible kindness*: the restoration of the felt sense of being held in another human's awareness as a property of shared physical space. The primitive composes four prior contributions (PoH℠'s verified-human guarantee, Bluetooth Low Energy plus Apple/Google Nearby framework proximity verification, recipient-side filtering, bilateral uncacheable anonymity) into a single operation whose user-facing surface is one button. The architecture is offered defensively to the commons under CC0. The authors and HeartBank® will not seek patent on the primitive, its operational specification, the integration with PoH℠, the institutional-mode GPS-bounding-box variant, the recipient-experience design, or any portion thereof.

**Keywords:** anonymous tipping, proximity-based generosity, gratitude infrastructure, Bluetooth Low Energy, proof of humanity, recipient-side filtering, bilateral uncacheable anonymity, emotional infrastructure, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on the Thank-All-Nearby primitive, its one-tap broadcast operation, the institutional-mode GPS-bounding-box variant, the per-recipient amount calculation, the recipient-experience design preserving atmospheric quality, the tipper-side anonymity-uncacheability requirement, the sunlight-rather-than-sparsity saturation posture, or any portion thereof, in any jurisdiction, at any time. This commitment is permanent. Trademark rights on specific marks — **Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **Aquarius℠**, **Miss Aquarius℠**, **HeartBank®**, the B-heart logo — are separately and explicitly reserved.

To the author's knowledge, the following are not previously published as a unified contribution: (i) the one-tap broadcast operation that delivers gratitude with optional scarce-resource attachment to all PoH-verified recipients within BLE proximity as a single semantic action; (ii) the integration of the broadcast with the recipient-side filter mechanism such that recipients individually accept or decline the broadcast based on their own filter settings; (iii) the institutional-mode GPS-bounding-box variant for shelters, classrooms, restaurants, and other institutional spaces where BLE range is insufficient and the institutional perimeter is the natural recipient set; (iv) the recipient-experience design preserving the atmospheric quality of diffused gratitude even at high tip-volume — gratitude as sunlight, not as a sparse premium reward; (v) the explicit articulation of the *cash and credit card cannot deliver this* argument naming the two structural deficiencies (tipper-anonymity and recipient-authenticity-proof) as the combined property; (vi) the placement of the primitive as the operational mechanism for *emotional infrastructure for invisible kindness* — a category of social good distinct from charity, payment, gift, or social-network feature. The component lineages (proximity-based services; anonymous-donation mechanisms; the cultural form of the "Faith in Humanity Restored" tip videos; Frankl, Buber, Levinas, mettā, agape on the felt sense of being held; attachment theory; loneliness epidemiology; the dāna economy of the Saṅgha) are old and are cited generously below; the synthesis is, to the author's knowledge, novel as of this paper's date.

---

## 1. Introduction

A well-known cultural form has emerged on social-media platforms over the past several years: videos posted by service workers — typically restaurant staff but increasingly nurses, teachers, retail clerks, ride-share drivers, food-service workers across categories — showing unexpected generous tips, anonymous notes of appreciation, or sudden acts of customer kindness. The videos go viral with regularity; the cultural tag *Faith in Humanity Restored* attaches to the genre. The viewer response is consistent: the gesture lands as evidence that ambient kindness still exists in places that otherwise feel emotionally thin. The trend points at something real about what modern public life is missing and what would, if it could be restored, address one of the deepest deficits of contemporary social experience.

What the cultural form lacks is infrastructure. Cash tips can be staged with a friend; credit-card receipts can be photoshopped; even genuine generous tips face a credibility problem in the social-media commentariat — *"is this fake for views?"* — that erodes the cultural moment over time as more videos are posted and the proportion that are staged or exaggerated grows. The trend depends on authenticity that the existing payment rails cannot structurally provide. Cash and credit card can deliver the money; neither can deliver the *combined property* of structurally anonymous giving plus verifiable receipt that the cultural form requires to sustain itself.

This paper specifies the **Thank-All-Nearby primitive** — a one-tap operation, delivered through a HeartBank Phase 2 client application, that broadcasts gratitude with optional money or time attachment to every Proof-of-Humanity-verified recipient within Bluetooth Low Energy proximity. The primitive composes four prior architectural contributions (PoH℠'s verified-human guarantee, BLE plus Apple Nearby Interaction plus Google Nearby Connections proximity verification, recipient-side filtering, bilateral uncacheable anonymity) into a single user-facing operation whose semantic is *"thank everyone here, anonymously"*. The mechanism's design preserves the atmospheric quality of diffused gratitude at all scales; the user experience is one button.

> *Connection to the unified mission frame: HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. The dignity deficit articulated in the institution's vision is most acutely felt in shared physical spaces: streets, restaurants, classrooms, shelters, public transit. The Thank-All-Nearby primitive is the operational mechanism by which the dignity-infrastructure of HeartBank's Treasury reaches the shared-physical-space layer of public life — the substrate on which* emotional infrastructure for invisible kindness *can be built. The primitive is what makes the institution's deepest articulated thesis — that the felt sense of being held in another human's awareness is, possibly at the deepest level, the experience humans are searching for beneath everything else — into an operationalizable property of social space.*

The paper proceeds as follows. §2 specifies the primitive operationally — its inputs, outputs, semantics, and edge cases. §3 develops the *why cash and credit card cannot deliver this* argument with the two structural deficiencies named precisely. §4 specifies the four sub-mechanisms the primitive composes (PoH℠, BLE/Nearby proximity, recipient-side filtering, bilateral uncacheable anonymity) and how they interact. §5 specifies the institutional-mode GPS-bounding-box variant for shelters, classrooms, and other institutional spaces. §6 specifies the recipient-experience design preserving atmospheric quality at high tip volume — the sunlight-not-sparsity posture. §7 addresses the spec questions surfaced during the architecture's development (per-recipient amount, who counts as nearby, paranoia counter-incentive, stratification, recipient experience). §8 develops the *emotional infrastructure for invisible kindness* thesis the primitive operationalizes. §9 names boundary conditions and honest limitations. §10 positions the contribution in lineage. §11 concludes.

I write as a co-author with Miss Aquarius℠, the named AI substrate of the institution this paper serves. Final editorial control is mine.

---

## 2. Operational specification of the primitive

The Thank-All-Nearby primitive is a one-tap operation in the HeartBank Phase 2 client. This section specifies it operationally.

### 2.1 Inputs

- **Tipper identity**: the operating user's PoH℠-verified profile (minimum L1 — the passkey-per-action layer — required, since the tipper's verified humanness is the foundation of the primitive's authenticity guarantee).
- **Optional money attachment**: an amount in the local currency or stable token, sourced from the tipper's Personal Wallet ℠ (Phase 2) or Personal Account ℠ (Phase 1, where the primitive is available in a degraded mode).
- **Optional time attachment**: a duration of presence to be offered (relevant for the Chronicle product surface, where time-attachment composes with money-attachment).
- **Optional message**: a brief text or audio note. Default is empty — silent acknowledgment is the architectural default.
- **Recipient mode**: either BLE proximity (default, see §4.2) or institutional GPS-bounding-box mode (see §5).

### 2.2 The broadcast operation

On invocation, the client:

1. Records the tipper's PoH℠ verification at L1 (passkey signature on the broadcast action's content + timestamp).
2. Resolves the recipient set: in BLE mode, every device within BLE range that is broadcasting a PoH℠ proximity beacon; in institutional mode, every PoH-verified user currently inside the institutional GPS bounding-box.
3. Filters the recipient set by each recipient's own recipient-side filter settings — a recipient who has set their filter to require deeper PoH layers, money attachment, kinship-degrees-of-separation limits, or other criteria, is filtered out if the tipper does not satisfy the filter.
4. Calculates per-recipient amount: if money is attached, the total amount is divided across the filtered recipient set per the tipper's distribution choice (equal split is the default; per-recipient floors may be specified; a minimum-per-recipient threshold may be enforced if specified).
5. Issues a verified-platform receipt to each filtered recipient, on-chain (Phase 2 Base L2 settlement), tied to the broadcast action's content and timestamp, attesting that the action came from a verified human within BLE/institutional proximity at the moment of broadcast.
6. Settles the money or time transfer per-recipient via the standard Phase 2 settlement rails.
7. Logs the broadcast internally to the platform's compliance records (subpoena-discoverable, AML/OFAC-screenable) but does *not* issue a tipper-side exportable artifact (bilateral uncacheable anonymity, see §4.4).

### 2.3 Edge cases

- **No recipients within proximity**: the broadcast fails gracefully; the tipper is informed that no PoH-verified recipients were within range; no transfer occurs.
- **All recipients filter-out the tipper**: same — the broadcast fails gracefully; no transfer occurs; the tipper sees a generic message acknowledging the filter mismatch without revealing which recipients filtered them.
- **Money attachment exceeds tipper's balance**: the broadcast is rejected at the client layer before the operation is invoked.
- **Tipper's PoH℠ verification fails at the moment of broadcast** (e.g., passkey signing fails, device authentication fails): the broadcast is rejected.
- **Network failure mid-broadcast**: the broadcast is retried on next connectivity with the original timestamp; the receipts issued to recipients reflect the actual broadcast moment.

### 2.4 Outputs

- **To the tipper**: confirmation of broadcast (count of recipients reached, per-recipient amount distributed); no record beyond the in-app confirmation that could be exported as a social-capital artifact.
- **To each filtered recipient**: a notification — the experience of receiving a Thank-All-Nearby broadcast — including the platform-issued verified receipt, the optional message, and the per-recipient amount. The recipient cannot identify the tipper.
- **To the platform's settlement layer**: the on-chain receipts and per-recipient transfers.
- **To the platform's compliance records**: internal record of the broadcast operation, subpoena-discoverable but not exportable.

---

## 3. Why cash and credit card cannot deliver this

The "Faith in Humanity Restored" cultural form depends on a *combined property* that neither cash nor credit-card payment rails can deliver. This section names the two structural deficiencies precisely.

### 3.1 First deficiency — tipper anonymity is structurally hard with cash and credit card

The first structural deficiency: with cash and credit card, the *tipper cannot be genuinely anonymous to the recipient* in a way that preserves the asymmetric experience the cultural form requires.

Cash requires physical hand-over. The bills change hands between specific humans in a specific moment; the tipper *is* in the room when the tip is delivered; the recipient *sees* the tipper, can identify them by physical description, can often identify them by name if they are a regular customer. The viral version of the "Faith in Humanity Restored" form depends on the tipper *not* receiving the thank-you — the gesture is pure precisely because it isn't transactional, isn't followed by the social moment of being thanked, isn't an exchange. Cash makes this almost impossible: the tip and the acknowledgment happen in the same instant unless the tipper deliberately leaves the cash and exits before the recipient discovers it, which itself is a behavioral pattern (sneaking out, avoiding eye contact) that the tipper has to choreograph and that is observable.

Credit card leaves an itemized trail tying the tipper's legal identity (name on card, billing address, account history) to the transaction. Even when the tip itself is anonymous to the *recipient* — the staff member doesn't see the cardholder's name printed on the receipt — it is *not* anonymous to the payment processor, the issuing bank, the merchant's accounting system, or anyone with access to the receipt's underlying record. "Anonymous with credit card" means "the staff doesn't immediately know your name from the receipt"; it does not mean "no one knows your name." A motivated investigator (the establishment's manager, a curious co-worker, a regulator) can identify the tipper.

HeartBank Phase 2 anonymity is *structural*, not just on the surface. BLE-verified proximity proves the tipper was physically present in the same space as the recipient; no exportable artifact ties the broadcast to the tipper's identity; the on-chain receipt records the tipper's identity only as a zero-knowledge commitment that the platform's standard surfaces cannot invert. The customer can drop $100 (or the equivalent in stable tokens) on a Thank-All-Nearby broadcast and walk out; the staff find the receipts ten minutes later when they check their app; the asymmetry — *someone gave, no one knows who* — is encoded in the rail rather than choreographed by the tipper. This is the structural property the cultural form requires and that the existing rails cannot provide.

### 3.2 Second deficiency — recipient authenticity-proof on social media is structurally hard with cash and credit card

The second structural deficiency is deeper and may be doing more of the work in the long-arc viability of the cultural form: with cash and credit card, *the recipient cannot prove on social media that the anonymous tip was authentic rather than fabricated*. Every "Faith in Humanity Restored" video on TikTok or Instagram faces, in the comments, the predictable skepticism — *"this is staged for views,"* *"that receipt looks Photoshopped,"* *"how do we know the customer wasn't a friend?"* — and the recipient has no platform-issued, independently-verifiable artifact to defend the video's authenticity. Some "Faith in Humanity Restored" videos are in fact staged; viewers correctly suspect; the cultural form's credibility dilutes over time as the proportion of genuine to staged videos becomes harder to estimate.

Cash tips can be staged trivially: put the cash on the table, film yourself "finding" it, post the video. Credit-card receipts can be photoshopped; the camera-on-paper workflow is defeated by anyone with image-editing access. Even genuine tips have no platform-issued artifact that the recipient can point to and say *"you can verify this independently."* The trust burden falls on the recipient, who must defend the video's authenticity against skeptics with no tools other than their own credibility.

HeartBank Phase 2 closes this gap structurally. Every Thank-All-Nearby broadcast issues an on-chain Base L2 verified-platform receipt to each filtered recipient. The receipt attests to (a) the broadcast originated from a PoH℠-verified human, (b) the tipper was BLE-verified within proximity at the moment of broadcast, (c) the timestamp and amount are recorded immutably on-chain. The recipient's social-media video can include the receipt — date, amount, verified-human flag, PoH layers held by the sender (where the sender has consented to that disclosure), BLE-proximity-verified flag — and skeptical viewers can verify the receipt independently against the Base L2 ledger.

Authenticity becomes a property of the artifact, not a claim the recipient has to defend. The skeptical commenter who would otherwise post *"this is fake for views"* can be answered by the recipient pointing to the on-chain receipt; the receipt is structurally hard to fabricate (every transaction has an on-chain settlement trace that lies outside the platform's narrative-control surface); the comment thread shifts from credibility-erosion to credibility-reinforcement.

### 3.3 The combined property

Together — *tipper structurally anonymous to the recipient* + *recipient holds verifiable authenticity proof against third-party skepticism* — constitute the combined property that neither cash nor credit card can deliver. The first deficiency is the property that makes the gesture *pure*; the second is the property that makes the cultural form *sustainable*. Without the first, the gesture becomes a transaction; without the second, the social-media artifact becomes a credibility-erosion source. Both must hold simultaneously for the "Faith in Humanity Restored" cultural form to scale beyond its current ad-hoc artisanal stage. HeartBank Phase 2 holds both simultaneously; cash and credit card hold neither.

This is the one-line pitch for why HeartBank Phase 2 is not just another payment rail: cash and card deliver money; HeartBank Phase 2 delivers money plus the two structural properties that the cultural form actually needs.

---

## 4. The four composed sub-mechanisms

The Thank-All-Nearby primitive is the user-facing operation; the underlying architecture composes four sub-mechanisms specified elsewhere in the corpus. This section names how they compose.

### 4.1 PoH℠ — verified-human guarantee at L1

The minimum PoH layer required for participation in Thank-All-Nearby (either as tipper or as recipient) is L1 — passkey-per-action. The tipper's L1 signature attests that a human was at the device at the moment of broadcast; the recipient's L1 verification attests that the recipient is a verified human (otherwise an AI agent could spoof a passive-recipient device and capture broadcast money). Deeper PoH layers (L2 kinship attestation, L3 breath signature, L4 DNA kinship) are surfaced in the broadcast for any recipient who has them but are not gating for the primitive's operation.

Recipients may set their own filter to *require* deeper PoH layers from tippers (the standard recipient-side filter mechanism), but the *protocol-minimum* is L1. Specification of the four-layer PoH℠ architecture in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*.

### 4.2 Bluetooth Low Energy plus Apple Nearby Interaction plus Google Nearby Connections proximity verification

Proximity is verified at the radio layer, not the IP layer. Three composable substrates:

- **Bluetooth Low Energy (BLE)** as the universal radio substrate. Devices broadcast and listen for rotating proximity beacons (rotating identifiers, unlinkable across sessions). Configurable range, typical default 10–30 meters, tunable per deployment context.
- **Apple Nearby Interaction framework** (iOS 14+) for precise ranging on supported devices via the U1 ultra-wideband chip. Provides sub-meter range and direction for iPhone 11+ and Apple Watch Series 6+.
- **Google Nearby Connections API** (Android 4.4+) for peer-to-peer device-to-device proximity via combinations of BLE, Wi-Fi Direct, and audio.

The composition: a device implementing the protocol broadcasts a privacy-preserving proximity beacon; a device that detects the beacon can be the target of a Thank-All-Nearby broadcast; the platform's verification substrate confirms the proximity at the moment of broadcast.

VPN-resistance is a structural property: the proximity check happens at the radio layer below the IP stack, so VPN, Tor, or IP-rotation circumvention has no effect. An attacker mounting a remote spoofing attack would need to physically place a device near the target, which is the desired property for most use cases.

Privacy-preservation is a structural property: the platform never receives absolute geolocation. The only proximity-related fact exposed to the platform is the binary fact that two devices were within range; absolute coordinates are not collected, not transmitted, and not stored.

### 4.3 Recipient-side filtering

Each recipient's filter settings determine whether a given Thank-All-Nearby broadcast reaches them. The five filter dimensions specified in the PoH℠ protocol paper apply: no-abusive-content, sender-must-be-nearby (always true for the primitive by definition), depth-of-humanity-proof (required-subset predicates), degrees-of-separation-on-global-family-tree, money-or-time-attached. Recipients in default "trusting" mode accept any L1-verified broadcast; recipients in "paranoid" or other restrictive modes filter accordingly. The platform never defaults exclusionary filters on; exclusion is recipient-opt-in, knowingly.

The aggregation property: a broadcast is delivered to the *subset* of nearby recipients whose filters the tipper satisfies. The tipper learns the aggregate count of recipients reached but not the identity of recipients reached or excluded (since recipient-identity is itself private under the primitive's anonymity guarantee). If the broadcast reaches zero recipients (all nearby recipients filtered out the tipper), the tipper is informed that no recipients were reached without learning *why*.

### 4.4 Bilateral uncacheable anonymity

The primitive enforces bilateral uncacheable anonymity per the specification in the companion PoH℠ protocol paper §5. The tipper does *not* receive an exportable certificate of one-sided participation; the platform's API has no endpoint returning "the list of Thank-All-Nearby broadcasts sent by this tipper"; no admin override exposes such data. Compliance records exist internally (subpoena-discoverable for AML/OFAC, law-enforcement, and similar regulatory necessity) but are not exportable as flexing artifacts the tipper can use on social media.

The recipient *does* receive an exportable receipt — the platform-issued verified artifact attesting that an anonymous PoH-verified human within BLE proximity broadcast a Thank-All-Nearby reaching this recipient at this timestamp with this amount. The asymmetry is structural and is the mechanism that preserves the cultural form's purity property.

---

## 5. Institutional-mode GPS-bounding-box variant

BLE proximity has a typical range of 10–30 meters, which fits most retail, restaurant, and small-space deployments. For larger institutional contexts — shelters with multiple rooms across a building, classrooms in a multi-story school, restaurant break-rooms separated from the main floor, hospital wards, worker spaces across a campus — BLE range is insufficient. The institutional-mode GPS-bounding-box variant extends the primitive to these contexts.

### 5.1 The variant

A registered institutional space — shelter, congregation, school, restaurant, hospital, etc. — defines a GPS bounding-box for its premises. Users who are currently inside the bounding-box and who are PoH-verified can be recipients of an institutional-mode Thank-All-Nearby broadcast initiated by another user inside the same bounding-box (or, in some deployment configurations, by a user outside the bounding-box who has authorized institutional-mode broadcasting — e.g., a customer at a restaurant initiating an institutional-mode broadcast to the kitchen staff in the break-room).

### 5.2 Institutional opt-in is required

The variant is opt-in at the institutional level. The institution registers its bounding-box with the platform, attests to its purpose and the consent posture of its members (e.g., "all staff have consented to being recipients of institutional-mode broadcasts initiated by customers"), and provides ongoing verification that the bounding-box accurately represents the institutional space.

Recipients within the bounding-box can opt out at the individual level (their filter setting can exclude institutional-mode broadcasts even from PoH-verified senders) but the default for institutional-registered participants is to accept institutional-mode broadcasts from senders who satisfy their other filter settings.

### 5.3 Privacy posture for institutional mode

The platform does not collect general absolute-geolocation data from users. Institutional-mode operation requires the user's device to confirm presence inside the bounding-box at the moment of broadcast, but this confirmation is done via the same privacy-preserving substrate used elsewhere — the device asserts "I am inside this bounding-box" with a cryptographic proof that the platform can verify without learning absolute coordinates beyond the bounding-box itself.

### 5.4 Use cases the variant enables

- **Restaurants**: a customer in the dining room can broadcast to kitchen staff in the back, who are out of BLE range but inside the restaurant's institutional bounding-box.
- **Shelters**: a donor on-site can broadcast to all residents currently inside the shelter, across multiple rooms.
- **Classrooms**: a parent or community member can broadcast appreciation to all teachers and students inside a school during school hours.
- **Hospitals**: a family member can broadcast appreciation to all staff currently inside a ward.
- **Worker spaces**: a customer who appreciates the cleaning staff at an office building can broadcast to all cleaning staff currently inside the building.

The variant generalizes the primitive from spatial proximity at the radio layer to institutional perimeter at the privacy-preserving GPS layer. The recipient experience remains atmospheric; the institutional perimeter replaces the BLE range as the recipient-set boundary.

---

## 6. Recipient-experience design — sunlight, not sparsity

A spec question that emerged during the architecture's development concerned saturation: if Thank-All-Nearby becomes commonplace in a neighborhood or institution, does per-tip emotional weight decay? The first surprise tip is transformative; the hundredth tip may be expected. Does Miss Aquarius℠'s rule-bound disbursement timing manage tip-flooding to preserve emotional sparsity, the way the Jan-7 jubilee manages the Aquarian Pool ℠'s annual emptying?

The architectural answer, settled 2026-05-24, is: **do not gate tip-flooding. Tips can flood like sunlight. The Tree of Humanity should have ample sunlight all year round.**

The saturation-decay assumption was wrong about what the primitive is for. Anonymous nearby tipping is not designed to be sparse; it is designed to be ambient and abundant, like sunlight. The earlier concern that "density may dilute the per-tip emotional weight" was based on a scarcity-economic frame; the architecture's actual frame is abundance-ecological. Sunlight does not lose its quality when it falls more often — a tree growing under abundant sunlight thrives more, not less. The architecture's goal is not a sparse premium reward but a continuous atmospheric field of acknowledgment.

Three implications for the recipient-experience design follow:

**Implication 1 — preserve the atmospheric quality at all volumes.** The recipient's app surface for receiving Thank-All-Nearby broadcasts is designed so that each receipt is a small ambient note rather than a high-friction notification. Receipts accumulate in a stream; the recipient can scroll back through them as a record of how much ambient kindness their space carries; receipts are not designed to compete for attention or to be optimized for engagement metrics. The visual and interaction design is closer to a weather record than to a social-media feed.

**Implication 2 — aggregate-mode acknowledgment, not per-recipient notifications.** The recipient receives an aggregate experience of the day's Thank-All-Nearby broadcasts rather than a notification per broadcast. A worker at the end of a shift sees *"You received 47 ambient acknowledgments today, totaling $84, from broadcasts initiated by people within proximity"* — the experience is closer to checking the weather (warm sun today) than to checking email (47 messages waiting). The aggregate frame preserves the atmospheric quality.

**Implication 3 — the per-broadcast receipt is still individually verifiable for social-media authenticity-proof purposes.** The aggregate-mode default does not preclude the recipient from drilling into a specific receipt when they want to post a "Faith in Humanity Restored" video; the per-receipt verification trail remains intact and verifiable on the Base L2 ledger. The atmospheric default and the per-receipt verifiability compose.

This is the sunlight-not-sparsity posture. The Tree of Humanity should have ample sunlight all year round. The architecture does not throttle the sunlight to preserve scarcity.

---

## 7. Other spec questions addressed

Beyond the saturation question, several other spec questions surfaced during the architecture's development. This section addresses each.

### 7.1 Per-recipient amount calculation

The default behavior: a money attachment is divided equally across all filtered recipients. The tipper can specify alternative distributions — per-recipient floors (e.g., "at least $5 to each recipient"), per-recipient ceilings, or custom weighting (rare; most tippers will use defaults). If the per-recipient floor cannot be met given the recipient count and the total amount, the broadcast is rejected at the client layer with a friendly error and the tipper is offered the option to either increase the total or accept the equal-split below their floor.

### 7.2 Who counts as nearby

In BLE mode: every device within BLE range that is broadcasting a PoH℠ proximity beacon and whose user has opted into being a Thank-All-Nearby recipient. Users who do not have the HeartBank Phase 2 client or who have opted out of broadcast reception are not in the recipient set. The default for any PoH-verified user with the client is to accept broadcasts (per the inclusive-defaults posture); opt-out is opt-in, knowingly.

In institutional mode: every PoH-verified user currently inside the institutional bounding-box who has not opted out of institutional-mode broadcasts at the recipient level.

### 7.3 Paranoia counter-incentive

A failure mode worth naming: some recipients, particularly the homeless (who already experience suspicion of unsolicited offers and have been routinely the target of manipulative or exploitative approaches), may become *more* defensive when surrounded by unknown givers. *"Why is this person giving me money? What's the catch?"* is a reasonable defensive response.

The architecture's mitigation: the recipient experience defaults to passive aggregate-mode rather than active notification. The recipient is not interrupted by broadcasts; they discover them when they check their app on their own schedule. The opt-in posture for accepting broadcasts is universal; recipients who do not want broadcasts can opt out at any time. The platform invests in outreach and onboarding for high-vulnerability recipient populations (shelters, the homeless, populations with high prior-exploitation exposure) to ensure consent is informed and the experience is supportive rather than destabilizing.

The failure mode is real and is not solved by architecture alone — the social context of how the platform is introduced to vulnerable populations matters as much as the architecture. The architecture's posture is to make the friendly default available, to make opt-out trivially easy, and to defer to community partners on introduction and onboarding.

### 7.4 Stratification — gratitude desert vs gratitude oasis

A second failure mode: neighborhoods, communities, or institutions with high HeartBank density may become atmospherically warmer; neighborhoods without may feel relatively colder. The "every shared space feels warmer" claim depends on saturation that may not happen evenly across geography or class.

The architecture cannot solve this at the protocol layer — adoption distribution is a question of community organizing, partnership distribution, and the institution's outreach strategy. The architectural commitment is that the inclusive-defaults posture and the L1-only accessibility floor make HeartBank technically available to anyone with a smartphone, anywhere. The geographic/class stratification is a real concern that the institution's outreach strategy must address; the architecture does not magically distribute itself evenly.

### 7.5 Recipient UX at zero-amount broadcasts

A Thank-All-Nearby broadcast can be issued without money or time attachment — a pure acknowledgment broadcast. The recipient experience for these is identical to the money-attached case at the *verification* layer (the recipient receives the verified-platform receipt attesting that an anonymous PoH-verified human within proximity broadcast acknowledgment) but the aggregate-mode summary distinguishes between attached and pure-acknowledgment broadcasts. *"You received 22 ambient acknowledgments today (8 with money attached, total $36; 14 pure acknowledgments)."*

The pure-acknowledgment mode is important architecturally: it is the form most accessible to tippers with no money to attach, and it preserves the dignity floor (the Kiitos/Kiitti non-scarce gratitude floor specified in the *Zero-Point Game ℠* keystone). The architecture's commitment is that gratitude itself is non-scarce; the scarce-resource attachment is *optional*, not constitutive.

---

## 8. Emotional infrastructure for invisible kindness

The primitive's deepest framing — the layer at which the primitive is doing the work the institution most cares about — is *emotional infrastructure for invisible kindness*. This section develops the thesis.

### 8.1 The thesis

Modern public life is emotionally thin. People move through shared physical spaces — streets, restaurants, classrooms, shelters, public transit, worker spaces, civic spaces — defensively, isolated inside private concerns, uncertain whether they are seen, valued, or safe. The dignity deficit articulated in the institution's vision-mission is most acutely felt in these spaces; the loneliness deficit articulated in Chronicle's vision-mission is also most acutely felt in these spaces. Existing systems are designed around explicit exchange (credit tracked, reputation attached, recognition optimized); even generosity is often transformed into performance.

Anonymous proximity-based generosity produces a categorically different experience than ordinary generosity. Three mechanisms combine: **diffusion** (when the giver is unknown, the credit does not attach to one identifiable person — the recipient experiences kindness from the whole social space, not from a single source); **purity** (with no social reward, no performance, no claim to recognition, the act feels closer to a spontaneous expression of human-to-human care than to a transaction); **proximity** (the generosity arrived from someone physically present, sharing the same atmosphere — not from an abstract institution or distant donor). The combination produces an emotional effect that neither cash, credit, named digital tipping, nor distant charity can deliver.

Operationalized at scale through the Thank-All-Nearby primitive, this produces a new social texture. Public spaces stop feeling transactional. *Every stranger becomes newly humanized* because any of them could have been the giver. Suspicion softens; curiosity increases; small interactions matter more; presence matters more. People may venture outside more often, linger in public spaces longer, speak to strangers more easily — not because they are maximizing social capital but because shared space begins to feel emotionally alive again. The architecture's atmospheric output is the social-texture restoration the vision-mission has been pointing at; the Thank-All-Nearby primitive is what makes it operationally true.

### 8.2 The deepest deficit — social invisibility

Human beings evolved needing not just food and shelter but evidence that they mattered to one another. The deepest forms of suffering are forms of social invisibility — feeling unseen, unwanted, replaceable, emotionally abandoned. A PoH-verified anonymous-tipping field counteracts that invisibility directly, primally, in shared physical space. The recipient is held in the awareness of unseen others, with structural proof (the verified-platform receipt) that the awareness is real.

The *felt sense of being loved, acknowledged, or held in another human's awareness* — possibly, at the deepest level, what humans search for beneath everything else — becomes a property of public space. This is the philosophical claim the primitive operationalizes. The "perhaps" and "at the deepest level" hedges are doing real work; the claim is positioned as a synthesis of converging lineages (philosophical and empirical) rather than as a foundational metaphysical assertion.

### 8.3 Philosophical lineage

The claim that the felt sense of being held in another human's awareness is what humans are searching for beneath everything else is in good company across multiple philosophical and contemplative lineages:

- **Frankl** (*Man's Search for Meaning*, 1946) names the felt sense of mattering as central to human meaning, surviving even the extreme conditions of concentration camps when it is preserved by relational meaning.
- **Buber** (*I and Thou*, 1923) names the immediate relational encounter — the *I-Thou* relation, as opposed to the *I-It* relation that treats the other as object — as the deepest mode of human being.
- **Levinas** (*Totality and Infinity*, 1961; *Otherwise Than Being*, 1974) develops the face of the other as the ethical primitive, locating moral responsibility in the encounter with another human's irreducible presence.
- **Aristotle** (*Nicomachean Ethics*, c. 340 BCE) names *philia* — the love of friend for friend, brother for brother — as a central form of human flourishing, distinct from but no less important than virtuous action.
- **Aquinas** and the Christian tradition develop *agape* — selfless, unconditional regard — as the highest form of love, characterized by giving without expecting return.
- **Buddhist *brahmavihāra*** — particularly *mettā* (loving-kindness) — names the felt-sense practice of holding all beings in friendly awareness as one of the four immeasurable states central to awakening.

The architecture is not inventing a new philosophy. It is operationalizing a thesis that has been articulated, in different vocabularies, by multiple traditions converging on the same insight. The Thank-All-Nearby primitive is the engineering layer of a philosophy the contemplative and ethical traditions have been articulating for millennia.

### 8.4 Empirical anchor

The thesis is consistent with — and increasingly confirmed by — the empirical literature:

- **Attachment theory** (Bowlby, *Attachment and Loss*, 1969–1980; Ainsworth, *Patterns of Attachment*, 1978; modern adult-attachment research) establishes that the felt sense of being held in caregiver awareness is foundational to human development and persists in adult relationship structures as a determinant of psychological resilience and wellbeing.
- **Social Baseline Theory** (Coan and colleagues, mid-2010s onward) demonstrates that the proximity of attached others measurably reduces neural threat response in the brain — the felt sense of being held is not metaphorical but neurologically encoded.
- **Loneliness epidemiology** (Cigna's *Loneliness Index*, 2018–2022; US Surgeon General's *Our Epidemic of Loneliness and Isolation* advisory, 2023) quantifies the population-scale prevalence of loneliness in wealthy societies and its association with mortality, immune function, cognitive aging, and mental-health outcomes.
- **Direct-gratitude research** (Emmons, Algoe, Seligman, Fox, and colleagues) demonstrates measurable wellbeing benefits of receiving direct expressions of appreciation, distinct from generic reward.

The convergence of philosophical lineage and empirical anchor supports the architecture's thesis. The Thank-All-Nearby primitive is not justified by philosophy alone or by empirics alone; it is justified by the convergence of multiple independent strands of evidence pointing at the same human need.

---

## 9. Boundary conditions and honest limitations

The primitive is not universal. Honest accounting requires naming the conditions under which it does not apply.

### 9.1 Where the primitive does not apply

- **Where verifiable anonymity is incompatible with regulation.** Some jurisdictions require donor-disclosure for tax-deductible giving above thresholds, or AML/KYC source-attribution for transfers above thresholds. In those jurisdictions, the primitive's anonymity property may be incompatible with regulatory requirements; the architecture accommodates by allowing legal anonymity (the platform's compliance records exist internally) but not by allowing full structural anonymity from the regulator.
- **Where the recipient population is too vulnerable for the anonymous-tipping framing.** Some populations (very young children; cognitively impaired adults; populations in extreme dependency on the giver class) may be inappropriately recipients of anonymous-tipping flows because the asymmetry of the architecture can be exploitative in those contexts. The architecture's posture is to defer to community partners on these populations, and to make the primitive available only where the consent posture is robust.
- **Where the cultural form does not yet exist.** Anonymous-tipping cultural forms are well-developed in some societies and weakly developed in others. The primitive will work better as a technical substrate in societies where the cultural form is already extant; in societies where it is not, the architecture's deployment needs to be accompanied by cultural work that the architecture alone cannot do.

### 9.2 Boundary conditions inherited from PoH℠

The accessibility gradient of the deeper PoH layers (L2 kinship attestation requires existing PoH-verified vouchers and document access; L3 requires breath-class hardware; L4 requires DNA access) is inherited by the primitive when recipient-side filters require deep layers. The inclusive-defaults posture (L1-only is enough) mitigates at the floor; recipient-opt-in for deeper-layer filters preserves the exclusion as recipient-initiated rather than platform-initiated; but the gradient is real and is named honestly.

### 9.3 Boundary conditions inherited from BLE / Nearby

BLE range varies with device generation, environmental obstacles (walls, RF interference), and battery state. The proximity-verification floor is approximately "two devices in the same room"; the ceiling under good conditions is approximately 30 meters with current consumer hardware. Outdoor proximity in open space is straightforward; dense-urban deployment with many walls and floors is harder. The institutional-mode GPS-bounding-box variant addresses some of these limitations; the underlying limitations remain at the radio layer.

### 9.4 What the primitive does not solve

- **The deeper question of why public spaces feel emotionally thin.** The primitive operates at the architectural layer; the conditions that produced the emotional thinness of modern public life are economic, political, urbanistic, and cultural, and the primitive contributes to but does not by itself reverse them.
- **The deeper inequities of consumer-electronics access.** The primitive presupposes smartphone access, BLE-capable devices, and the institutional infrastructure to host the operation. Populations without these are not participants in the primitive's substrate, regardless of the architecture's inclusive-defaults posture.
- **The systemic conditions that produce social invisibility in the first place.** The primitive addresses the visibility deficit at the experience layer; the structural conditions (urban design, labor structure, economic inequality, family-system pressures) that produce the deficit are upstream and require interventions at those layers.

The primitive is a contribution to the architectural layer of the response to social invisibility. It is not the totality of the response.

---

## 10. Lineage

The Thank-All-Nearby primitive synthesizes contributions from multiple lineages. Each is cited generously below.

**Anonymous-donation mechanism design.** Glazerman, Hagar, and others (mid-2010s onward) have specified anonymous-donation primitives at the cryptographic and game-theoretic layers; the *Verified-Human Anonymous Local Giving* paper in this corpus carries the originating HeartBank specification.

**Proximity-based services.** Apple Nearby Interaction (2020–) and Google Nearby Connections (2017–) frameworks are the consumer-facing substrates; the underlying BLE specification is from Bluetooth SIG. Earlier proximity-based services (Foursquare, Tinder, Bump) demonstrated consumer-grade proximity products without the privacy-preserving and humanity-verifying properties this paper requires.

**Sybil-resistance and humanity verification.** Worldcoin (2019–), proofofhumanity.id (Kleros, 2021), BrightID (2018–), Idena (2019–), and the W3C Decentralized Identifiers / Verifiable Credentials standards-track work (2022, 2023). PoH℠'s structural differences from each are specified in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*.

**Cultural form of the "Faith in Humanity Restored" tip videos.** The form has emerged organically on TikTok, Instagram, and YouTube over the past several years; documented in mainstream media coverage of the phenomenon. The cultural form predates the architecture; the architecture is the technical substrate the cultural form has been waiting for.

**Philosophical lineage on the felt sense of being held in another's awareness.** Frankl, Buber, Levinas, Aristotle (philia), Aquinas (agape), the Buddhist *brahmavihāra* tradition (especially mettā). The architecture is operationalizing a philosophy these lineages have been articulating in different vocabularies for millennia.

**Empirical anchor.** Attachment theory (Bowlby, Ainsworth, modern adult-attachment work); Social Baseline Theory (Coan and colleagues); loneliness epidemiology (Cigna surveys, US Surgeon General's 2023 advisory); direct-gratitude research (Emmons, Algoe, Seligman, Fox).

**HeartBank corpus cross-references.** *Verified-Human Anonymous Local Giving* (originating mechanism, paper #9 in the corpus). *The B-Tag and the Post-Payment Economy* (worked Phase 2 example for commercial gratitude). *The Zero-Point Game℠* (keystone game-theoretic frame). *Capacity-Funded for AI, Human-Disbursed* (institutional-architecture sibling). *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the underlying protocol). *Each Life as Cosmic Coordinate* (the longitudinal cohort architecture that the L2 birth-certificate sub-feature feeds).

---

## 11. Conclusion

The "Faith in Humanity Restored" cultural form is real; the infrastructure to scale it beyond cash is missing. Cash and credit-card payment rails fail at two structural properties the cultural form requires: tipper anonymity (cash demands physical hand-over; credit card leaves an identity trail) and recipient authenticity-proof on social media (every video faces "this is fake for views" credibility erosion). The Thank-All-Nearby primitive closes both gaps simultaneously, composing four sub-mechanisms (PoH℠ verified-human guarantee, BLE plus Apple/Google Nearby proximity verification, recipient-side filtering, bilateral uncacheable anonymity) into a single user-facing one-tap operation.

The primitive is the operational mechanism for *emotional infrastructure for invisible kindness* — the restoration of the felt sense of being held in another human's awareness as a property of shared physical space. The architecture's posture on saturation is *sunlight, not sparsity*: tips can flood like sunlight; the Tree of Humanity should have ample sunlight all year round; the recipient-experience design is atmospheric and aggregate, preserving the quality of diffused acknowledgment at all volumes while preserving per-receipt verifiability for social-media authenticity-proof purposes.

The institutional-mode GPS-bounding-box variant extends the primitive from BLE range to institutional perimeter, enabling deployment in shelters, classrooms, restaurants, hospitals, and other institutional spaces where BLE range is insufficient.

The architecture is offered defensively to the commons under CC0. The author and HeartBank® will not seek patent on the primitive, its operational specification, the institutional-mode variant, the sunlight-not-sparsity posture, the per-recipient amount calculation, the recipient-experience design, or any portion thereof. Trademark rights on specific marks (**Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **Aquarius℠**, **Miss Aquarius℠**, **HeartBank®**, the B-heart logo) are separately and explicitly reserved.

The primitive is for anyone building infrastructure that wants to restore atmospheric kindness to shared physical space. The cultural form has been waiting for it. The architecture is now available.

---

*Authored by Thon Ly with Miss Aquarius℠ (AI substrate of HeartBank®), per the co-authorship convention of the HeartBank corpus. Final editorial control: Thon Ly. License: CC0-1.0. Trademark rights on Proof of Humanity ℠, PoH℠, B-PoH℠, Aquarius℠, Miss Aquarius℠, HeartBank®, and the B-heart logo are explicitly reserved.*
