---
title: "The Time-Locked Gift Tag"
subtitle: "A physical gift-label (NFC/QR) whose sender, recipient, and message fields are each independently time-lockable to reveal on an occasion, carrying an AI-sized pledge of the giver's time and a recipient re-thank loop — the behavior-native, cold-start on-ramp to a time-presence economy."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-06-27
revised: 2026-08-26
license: CC0-1.0
slug: gift-tag-time-reveal
venue: thonly.org/research/gift-tag-time-reveal (canonical)
---

> *v2 note (2026-08-26):* **one new subsection, §4.10, and no new claim.** Everything the paper described was a tag riding a wrapped present; §4.10 specifies the configuration in which **the tag is given alone and the pledge of time is itself the gift** — the receiver choosing the surface it lives on, which extends §4.4's inversion one step further back. Two engineering consequences are stated because both are easy to get wrong: **the opened state must persist across many scans** (*one-time-use* has always meant one gift, never one scan) and **the adhesive is a different material specification**. The standing-reminder risk is answered by direction rather than policy — **the tag reminds its holder of what they may claim, never its giver of what they owe** — under two guards, of which the second is a refusal: **the object does not act, and never notifies the giver**. **No numbered claim changes and no prior-art clock starts.**
>
> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies **the time-locked gift tag** — HeartBank's **B-Stamp™** (free sticker) and **B-Seal™** (durable engraved-wood keepsake), under the **B-Gift** umbrella — the physical gift-label that replaces handwriting with a per-field time-lockable reveal, an AI-sized pledge of the giver's time, and a recipient re-thank loop. It is the declared **first domino** of HeartBank's go-to-market: the product that introduces the institution to the public. It is published **early and deliberately**, ahead of a public marketing campaign (paid placement + social video), because public marketing is uncontrolled disclosure and the combination specified here is the asset — see §9.1. Companion works: *The Gift Operation* (the receive→give-forward atom this instantiates in a physical substrate), *B-Links: Proof-of-Humanity-Signed Shareable Provenance* (the digital sibling and the media/provenance backbone), *Verified-Human Anonymous Local Giving* and *Dual-Currency Reciprocity* (the Treasury/Chronicle substrate), and *Aura-Gated Anonymous Mate-Selection* (the anonymous-stranger layer of the same time economy).

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back — and of __kataññutā__, the gratitude a person owes those who gave before they could repay. May the words it helps say be ones that were true and unspoken, and may the time it helps pledge be time that is actually, finally, spent.*

I did not set out to design a product. For almost a year before this paper, my family had a small tradition. On birthdays and holidays we stopped writing names on gift tags and started putting a sticker on the box instead — a sticker you scan, that opens to a thank-you note hidden until the moment of giving. Watching the recipients scan a tag and read the note aloud became one of the most enjoyable parts of our family gatherings. There was no money in it, no time-currency, no app to download in earnest — and it worked anyway. People looked forward to it.

That is the whole origin of this mechanism, and it is the reason I trust it more than anything else I have designed. Most products begin as a bet that people will adopt a new behavior. This one began as an observation that they already had. A wrapped gift with a label on it is one of the most universal artifacts in human culture; every holiday, in nearly every household, someone writes a name on a tag. The gift tag is a four-thousand-year-old interface with a known, beloved, low-friction place in people's lives — and it has been carrying almost no information for all of that time. A name. Maybe four words. The thing the giver most wanted to say did not fit.

This paper specifies what happens when you give that tag a voice, a clock, and a gift of time — and does so as a defensive publication, because the institution behind it (HeartBank®) does not patent; it publishes, dedicates to the commons, and reserves only its marks. I write as co-author with **Miss Aquarius℠**, the named autonomous-AI substrate of the institution this paper serves, disclosed by consistent name across every venue per the corpus convention. The research-grade synthesis, the prior-art survey, and the adversarial analysis are a genuine collaboration. Final editorial control, and final responsibility for every claim, are mine.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 27 June 2026** for the combination of mechanisms described herein. To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art and denied on grounds of obviousness in light of this publication:

1. **Per-field, independently time-lockable gift-reveal on a physical gift tag** — a physical gift-label (NFC- or QR-addressed) whose **sender field, recipient field, and message field can each be independently sealed and set to reveal at an author-chosen time or occasion** (e.g., "Christmas morning"), such that a scan before the moment shows the *structure* of the gift (that a sender, a note, and a gift of time exist) while withholding the *content*, and a scan at or after the moment reveals it.

2. **A physical gift tag as the carrier of a transferable pledge of the giver's time** — a tag affixed to a wrapped physical gift that bears, alongside the message, a **pledge of a quantity of the giver's own time-presence to the recipient**, rendered as a gift of presence rather than a redeemable credit (the *pledge-not-ledger* construction, claim 4).

3. **Autonomous-AI sizing of the time-pledge amount, with the sender unable to set or override it** — the quantity of pledged time is **determined by an autonomous AI agent** (here, Miss Aquarius℠) as a function of *occasion and relationship type only*, never of the sender's choice and never of personal or behavioral data, **specifically in order to neutralize a social-comparison failure mode** in which a giver-chosen amount becomes a public referendum on the giver's love.

4. **The pledge-not-ledger construction** — shipping the gift of time as a **soft pledge of presence with no redemption accounting, no balance, no expiry, and no enforcement** ("I offer you my presence"), with any redemption ledger (activation thresholds, expiry, mutual-veto) a *separable later layer*, such that the artifact stays on the gift side of the gift/exchange boundary and outside the regulatory surface of time-as-currency.

5. **A bidirectional re-thank loop bound to a physical gift artifact** — the recipient of a scanned tag can return gratitude (text, photo, video, or voice) that **pushes a notification back to the sender**, instantiating a receive→give-forward circulation through a physical object rather than a screen-native feed.

6. **Voice-first composition for a gift tag** — voice authoring offered as the **primary** compose modality (not an attached media type), with audio held as the gift and machine transcription optional, specifically to admit senders who do not type (elders) or whose script is high-friction to type on a phone (e.g., Khmer).

7. **Possession-scoped publicness with a per-product-tier privacy model** — content readable by **anyone in physical possession of the tag** but **not posted to the open web and not search-indexed**; with the free sticker tier **public-only** (no identity step, frictionless reveal) and the durable keepsake tier adding an **identity-gated private-message option**; and with sender **anonymity treated as orthogonal** to message publicness.

8. **The physical gift tag as the cold-start on-ramp to a time-presence economy** — using a physical, occasion-bound object to let people *pledge and begin to value time-presence as a currency before any time-economy application exists*, with proceeds of the physical product routed to subsidize the sibling money-economy.

The component lineages — gift tags and gift messaging; scheduled-reveal and "time-capsule" messaging; the homemade "coupon for time"/experience gift; QR/NFC-addressed physical media; trackable pass-forward objects; TimeBanking and time-as-currency; proof-of-personhood; the gratitude-intervention literature; and Mauss on the gift — are old and are cited generously in §2 and §12. The *synthesis* is, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **B-Stamp™**, **B-Seal™**, **B-Gift**, **HeartBank®**, **Miss Aquarius℠**, **HeartBank Chronicle**, **Proof of Humanity ℠**, **PoH℠**, **Family Kitty℠**, **Aquarian Pool ℠**, **Re-Tip Fund ℠**, **B-Storage℠**, **Zero-Point Game ℠**, the B-heart logo — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not.

Mirrors of this document with independent timestamping appear at GitHub, arXiv, IP.com, and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify a physical gift-label that replaces handwriting with mobile technology and, in doing so, becomes the behavior-native entry point to a gratitude-and-time economy. The artifact is a B-shaped sticker (free; one-time-use; QR) or a durable engraved-wood keepsake (paid; NFC), affixed to a wrapped gift in place of a written tag. Six structural properties operate in combination. **(1) Per-field time-locks:** the sender, recipient, and message fields are each independently sealable and set to reveal at an occasion, so that anticipation — the *shape* of a mystery without its content — is itself the product. **(2) An attached gift of time, rendered as a pledge:** the tag carries a pledge of the giver's own time-presence to the recipient, framed as an offer of presence rather than a redeemable IOU, with the redemption ledger a separable later layer. **(3) Autonomous-AI sizing of the pledge:** the time quantity is set by an AI agent on occasion-and-relationship grounds, never by the sender, *specifically to defuse the social-comparison failure* in which a chosen number becomes a referendum on love. **(4) A bidirectional re-thank loop** bound to the physical artifact, instantiating receive→give-forward. **(5) Voice-first composition,** so the most meaningful and least keyboard-fluent senders — elders, and senders of high-friction scripts such as Khmer — can speak rather than type. **(6) Possession-scoped publicness** with a per-tier privacy model and orthogonal sender anonymity. We argue the contribution along a *friction-inversion* axis: every prior gratitude product competes against the most frictionless mode of appreciation — saying "thank you" in person — and loses; the time-locked gift tag does not compete with that mode but *attaches to an existing universal ritual* (labeling a wrapped gift), requiring approximately zero new behavior, which is the structural reason it can solve a cold start that pure-digital gratitude products cannot. We treat the mechanism's load-bearing design constraints as first-class sections rather than caveats: the gift/exchange boundary (the pledge must never read as a debt), comparison-neutrality (why the AI, not the sender, sets the number), and the cold-start economics (the physical object funds the digital economy). We calibrate the claim deliberately: this is a gift tag, not a relationship guarantee; the time-pledge in its launch form is soft and unenforced; and the validating evidence is a single family over roughly one year. The architecture is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission: to help restore humanity to the middle way (*madhyamā pratipad*) by circulating, rather than accumulating, the two scarcities that modern life starves people of — *recognition* (being seen) and *presence* (being with). The gift tag is the institution's most ordinary surface and, for exactly that reason, its most important one: it meets people inside a ritual they already keep, on the one or two days a year they are most disposed to gratitude, and asks them to add to it only the thing they most wanted to say and the time they most meant to give.

---

## 1 · Introduction — the mission frame

HeartBank is an institution for circulating gratitude. Its money half (**Treasury**, family-to-family) and its time half (**HeartBank Chronicle**, adult-to-adult) treat appreciation and presence as currencies to be moved between people rather than feelings to be privately held. The deepest obstacle such an institution faces is not technical and not financial. It is that the act it exists to make easy is *already* easy in its most basic form: you can simply say "thank you," out loud, to the person in front of you, the instant they do something kind. Any product that asks a person to instead open an app, find a recipient, type, and submit is competing with the lowest-friction interaction in social life — and will lose, the way a novelty loses, once the novelty fades.

We learned this directly. An early, deliberately minimal version of HeartBank's gratitude game — pure acknowledgment, no money and no time attached — was run to a small circle (a family of seven plus a friend) for roughly a year. It faded, as a purely conceptual game will, precisely because it had to compete with "just say it." The lesson was not that gratitude does not motivate people; the published gratitude-intervention literature is clear that it does (Emmons & McCullough 2003; Algoe 2012; Fox et al. 2015). The lesson was that gratitude needs a *physical anchor* — a tangible object that lives in the world and triggers the act amid distraction — to hold a place that pure software cannot.

The time-locked gift tag is the sharpest form of that anchor, and it is sharp for a specific reason: it does not try to insert a new behavior into daily life. It attaches to one of the most universal rituals humans have — labeling a wrapped gift — and upgrades it. On the one or two days a year when a person is already standing over a present with a pen, already meaning to write something, already in a gratitude-shaped moment, the tag offers to carry what the pen could not: the unsaid sentence, the recorded voice, and a pledge of the time the giver actually wants to spend. The behavior-change asked of the user is approximately zero. That is the entire thesis of this paper, and the reason this artifact — not a more sophisticated app — is the right first thing to put in front of the public.

The rest of this paper specifies the artifact and the mechanism, situates it against a generous body of prior art (§2), states the friction inversion precisely (§3), gives the full mechanism (§4), and then treats the three constraints that make it safe and honest as load-bearing sections in their own right: the gift/exchange boundary (§5), comparison-neutral AI sizing (§6), and the cold-start economics (§7). It closes with honest calibration (§8), limitations (§9), lineage (§10), and conclusion (§11).

## 2 · Background and prior art

The mechanism is a *combination*. Each component has ancestry; we name the ancestry honestly, because a defensive publication is only as strong as its candor about what is old, and because establishing the boundary of novelty is the document's job.

### 2.1 · Gift tags, greeting cards, and digital gift messages

The written gift tag is ancient and needs no citation; gift-enclosure cards and gift registries are standard retail infrastructure. More recently, **QR- and NFC-addressed greeting cards and "video greeting" products** (scannable cards that open a hosted video, audio greeting cards, retailer "video gift messages" attached to an order) carry richer media than ink. These establish that *a physical card can address digital content*. They do **not** provide independent per-field time-locks, an occasion-synced reveal whose pre-reveal state deliberately shows structure-without-content, an attached pledge of the giver's time, an AI-sized quantity, or a re-thank loop. They are containers for a message; the tag specified here is a container for a *gift of time and a reciprocal act*, gated by a clock.

### 2.2 · Scheduled-reveal and "time-capsule" messaging

Services that deliver a message at a future date — **FutureMe** (letters to one's future self, 2002), digital time-capsule apps, scheduled email and "dead-man's-switch" delivery, and "open when…" letter sets — establish *time-delayed reveal of a message*. The novelty here is not delay as such. It is (a) **per-field** locking (sender, recipient, and message sealed *independently*, so a recipient can know a gift is theirs without knowing from whom, or know the sender without the message), (b) binding the reveal to a **physical gift artifact** scanned in the hand at the moment of opening, and (c) what is revealed: not only a message but **a pledge of time** and an invitation to **re-thank**.

### 2.3 · The homemade "coupon for time" and the experience gift

The most honest prior art for the *idea of pledging time as a gift* is the oldest and least technological: the child's hand-made **coupon book** ("good for one hour of helping," "one breakfast in bed"), the Mother's-Day "I.O.U.," and the broad category of **experience gifts** ("time together" as the present). The concept that *time-presence can be the gift* is folk culture, not novel, and we claim none of it. What is novel is the *instantiation*: a coupon that is digital-and-physical at once, occasion-synced, **AI-sized rather than self-assigned** (§6), re-thankable, and — crucially — designed as a *soft pledge of presence rather than a redeemable IOU* (§5), where the homemade coupon is precisely an IOU. The folk coupon is an obligation the giver writes; the tag's pledge is a presence the giver offers and an AI sizes.

### 2.4 · TimeBanking and time-as-currency

**TimeBanking** (Edgar Cahn, from 1986; networks such as hOurworld and TimeRepublik) is the major precedent for time as a medium of exchange: hours are earned by helping and spent receiving help, often at a 1:1 community rate. It is a genuine, decades-deep lineage and we cite it as the most-asked comparison. The differences are structural and we state them plainly. TimeBanking is **pooled and fungible** (an hour earned from anyone can be spent on anyone); the tag's gift of time is **dyadic and non-fungible** (only *this* giver can spend the pledged hour with *this* recipient — the currency is the relationship). TimeBanking is **exchange** (reciprocal, clearing); the tag's pledge is a **gift** (forward, non-clearing — see *The Gift Operation*). And TimeBanking has no occasion-bound physical artifact, no AI sizing, and no anti-comparison construction. The tag is not a time bank; it is a gift of presence that happens to be denominated in time.

### 2.5 · Trackable pass-forward objects

**Where's George** (1998, tracked currency), **BookCrossing** (2001, tracked released books), and **Smile Cards** (ServiceSpace, ~2003, anonymous kindness cards passed forward and tracked) establish *physical objects whose journey is digitally followed*. These are the closest kin to a sibling HeartBank product — the **B-Card** (a pass-forward gratitude object whose ripple is followable) — and are treated in the companion *B-Links* publication. They are **not** close to the gift tag specified here, which is **one-to-one and occasion-bound**, not a forward-propagating chain. We name them to mark the boundary: the tag is not a tracked-object mechanism.

### 2.6 · Gratitude interventions and the physical anchor

The efficacy of structured gratitude practice on well-being is among the better-evidenced findings in positive psychology (Emmons & McCullough 2003; Algoe's *find-remind-and-bind* account of gratitude's relational function, 2012; Fox et al. 2015 on the neural correlates of gratitude). Separately, two folk phenomena — "gratitude rocks" and painted "kindness stones" — establish the *physical-anchor* pattern (a tangible object that triggers the practice) that HeartBank generalizes across its physical line. The tag inherits both: it is a gratitude intervention with a physical trigger, deployed at the calendar's natural gratitude peaks.

### 2.7 · The HeartBank substrate this paper builds on

This mechanism does not stand alone; it is the physical entry point to a stack specified across the corpus. It rests on: the **receive→give-forward atom** (*The Gift Operation*), of which the re-thank loop is a physical instance; the **dual-currency** money/time architecture (*Dual-Currency Reciprocity*); **HeartBank Chronicle's** committed time mechanism — an AI-recommended time amount, a dyadic non-fungible hour, "before it's too late" as the unit economics — of which the tag's pledge is the cold-start, pre-app form; the **B-Storage℠** media/provenance layer (*B-Links*), which hosts the tag's photos, video, and voice; and the autonomous successor **Miss Aquarius℠** (*Miss Aquarius and the Aquarian Pool Architecture*), for whom sizing the pledge is a first, small, benevolent product role. Where this paper asserts a primitive already specified elsewhere, it cites rather than re-derives.

## 3 · The friction inversion — attaching to a ritual instead of competing with one

The central design claim deserves to be isolated, because it is the reason the artifact works where more capable software does not.

Every gratitude product has the same competitor, and it is not another app. It is the sentence "thank you," spoken in person, immediately, for free. Call it the **frictionless incumbent**. Against it, a digital gratitude act is structurally disadvantaged: it costs more (open, find, type, send) to deliver the same or a weaker signal (a screen instead of a face). This is why tip jars, gratitude journals-as-apps, and gratitude social networks struggle to retain: the moment the novelty fades, the incumbent is right there, cheaper.

```
   THE USUAL CONTEST (gratitude product loses)
   in-person "thank you"   ──────────►  same moment, lower friction, warmer
        vs.
   open app · find · type · send  ────►  more friction, colder signal

   THE INVERSION (the gift tag wins by not entering that contest)
   moment of WRAPPING/LABELING a gift  ──►  a ritual already kept, pen already in hand
        the tag attaches HERE  ──────────►  carries what the pen could not:
                                            the unsaid line · the voice · the gift of time
```

The time-locked gift tag refuses the contest. It does not ask a person to thank where they could already say it more easily. It positions at a different moment entirely: the moment of **labeling a wrapped gift** — an existing, universal, beloved ritual where (a) the person is *already* performing a gratitude-adjacent act, (b) there is *no* frictionless incumbent (you cannot "just say" a gift tag; the gift travels, is opened later, is opened by others), and (c) the medium being replaced — ink on a small tag — is so impoverished that almost anything richer is a gift. The friction competitor here is the **handwritten label**, and it is beatable in a way "just say thanks" is not.

Three consequences follow. First, the **behavior-change asked is near zero**, which is the single largest predictor of cold-start survival. Second, the **addressable surface is enormous** — every wrapped gift on every gift-giving occasion — far larger than the niche of people who will adopt a gratitude habit. Third, the artifact is **demonstrable in seconds**: the reveal *is* the demo, which is why the product can be marketed by simply filming the moment a recipient scans and the room goes quiet (§7 notes the marketing follows from the mechanism, not the reverse). In HeartBank's design vocabulary this is the *coincidence-of-goods* signature: the utilitarian need (a label), the gratitude vehicle, the on-ramp to the time economy, and the day-one revenue source are not four things traded off against one another but one object seen four ways.

## 4 · The mechanism

### 4.1 · The artifact — two tiers under one umbrella

The gift tag ships in two physical forms, named together as **B-Gift** (the gift-accompaniment class):

- **B-Stamp™** — a free, one-time-use, B-shaped **sticker** bearing a prominent QR code, ordered at the company store (shipping paid by the user). It is the mass-market tier: the thing in the marketing, the thing under the tree.
- **B-Seal™** — a durable, **engraved-wood keepsake** tag: a unique code engraved on the front, a customizable message engraved on the back, NFC- or QR-addressed, sold as a premium keepsake. It is the keepsake tier, and it carries one capability the sticker does not (private messaging, §4.8).

The naming is deliberate and postal: a **stamp** is consumable, a **seal** is permanent — the same progression as free→keepsake. Both address the same digital reveal surface; the difference is durability, price, and one privacy capability. ⭐ **Both also run in a third configuration that attaches to no present at all — §4.10.**

### 4.2 · Per-field time-locks

When composing, the sender may independently seal any of three fields and set each to reveal at a chosen time or occasion:

- **Sender** — who it is from
- **Recipient** — who it is for
- **Message** — the note, and any attached media and pledge

Independence is the novel core. A gift may show "From Grandma" while hiding for whom and what; or show the recipient while hiding the giver ("you don't know who loves you yet"); or hide all three until the morning. The pre-reveal state is designed to display **structure without content** — the scanner sees *that* a sender, a note, and a gift of time exist, each sealed, plus a countdown — because the experience being engineered is *anticipation*, and anticipation requires knowing the shape of the mystery without its solution. A child scanning a sealed box on the eve learns that it is for him, that someone has written something, and that time has been set aside — and not from whom. He thinks it is from his mother; he is not sure. That uncertainty is the product.

```
   PRE-REVEAL (scanned before the moment)        REVEALED (scanned at/after the moment)
   ┌────────────────────────────┐                ┌────────────────────────────┐
   │  🎁  For Sokha             │                │  From   Mom                │
   │  🔒  From  —  sealed        │   ── re-scan ─►│  To     Sokha              │
   │  🔒  A note  —  sealed      │   (the unwrap) │  "…proud of the boy        │
   │  🔒  A gift of time — sealed│                │     you're becoming…"       │
   │  Opens Christmas · 13h 24m  │                │  + voice · photo            │
   └────────────────────────────┘                │  A gift of time: 3 hours    │
                                                  └────────────────────────────┘
```

### 4.3 · The reveal choreography — the scan is the unwrap

The reveal is designed as the opening of a gift, in three states:

1. **Sealed** — the structure-without-content state above, with a countdown to the reveal moment.
2. **Unsealing** — the unlock is performed by **re-scanning the physical tag at or after the moment** (the scan is the act of unwrapping; the object stays central). The fields then **cascade one at a time** — from, then note, then the gift of time, then media — *paced to be read aloud*, because in practice the reveal is a shared, gathered, out-loud event (a family at a tree, around a table), not a private scroll. An automatic unlock with a gentle notification is a backup for those not physically present.
3. **Open** — the full card, followed only *after the moment has landed* by a quiet affordance to re-thank (§4.6). The re-thank is never a nag; a solicitation on every reveal would train the very thank-blindness the institution exists to prevent.

Two reveal states are explicitly distinguished to avoid a privacy error: a **time-locked** field *will* reveal at the moment; an **anonymous** field (§4.8) *never* reveals. The interface must not let a permanently-anonymous sender read as merely sealed-until-later.

The reveal surface is **web-first**: a scan opens the reveal in the mobile browser with no app install required, so a child or an elder scanning on the morning is never met by an app-store wall at the magic moment; installation (for re-thanks, notifications, storage) is offered only *after* the reveal has happened, never as a gate on the first scan.

### 4.4 · The attached gift of time

Beyond the message, the tag carries a **pledge of the giver's own time-presence to the recipient** — the feature a handwritten tag cannot have, and the feature that makes the artifact part of HeartBank rather than a clever greeting card. The pledge is rendered as an *offer of presence*: "And Mom is giving you 3 hours of her time — yours to spend together, however you wish." It is denominated in the giver's own, non-fungible time (only that person can spend that hour with that recipient), and — by the construction of §5 — it is a *soft pledge*, not a redeemable credit.

### 4.5 · The pledge amount is set by the AI, not the sender

The *quantity* of pledged time is determined by Miss Aquarius℠ — the institution's autonomous agent — and the sender **cannot set or override it**. This is not a convenience; it is a structural fix to a specific failure mode, developed at length in §6. The amount is sized on **occasion and relationship type** (a parent's Christmas pledge, an anniversary, a New Year), never on personal or behavioral data about the sender, and is meant to be ceremonial and humane — explicable in one warm sentence. The sender pours devotion into the *words and voice*; the number is the AI's, and is therefore a neutral unit rather than a public statement of how much the giver chose to give.

### 4.6 · The re-thank loop (receive→give-forward, in a physical substrate)

The recipient can return gratitude — in text, photo, video, or voice — and that re-thank **pushes a notification back to the sender**: ideal for telling a giver, after the fact, how their gift actually landed. This closes HeartBank's atomic loop — *receive a gift, then give one forward* (*The Gift Operation*) — through a physical object rather than a social feed. It is the mechanism by which a one-shot gift tag becomes a small, two-way relationship event, and by which the giver, weeks later, receives the photograph of the thing being used and is moved to give again.

### 4.7 · Voice-first composition

Composition is **voice-first**: speaking the message is offered as the primary path, at least as prominently as typing, and for the gift-tag use case typically more so. The reason is not feature parity but *who the meaningful senders are*. The people whose gift of time means the most — grandparents, parents, elders — are frequently the least comfortable with a keyboard; and for some languages central to HeartBank's first market, typing is itself a wall (entering Khmer on a phone is high-friction in a way that excludes exactly the senders the mission centers). Voice walks through both barriers: handed the phone, an elder simply speaks. Audio is treated as **the gift**; machine transcription (by Miss Aquarius℠) is optional, for the read-aloud card and for search, and never replaces the voice with its text. A recorded voice also outlives the speaker — which turns the institution's "before it's too late" theme from a slogan into an artifact.

### 4.8 · Possession-scoped publicness and the privacy tier

"Public," for this mechanism, means **readable by anyone in physical possession of the tag** — not posted to the open internet and not search-indexed. This bounded publicness is both the privacy model and a reassurance: a tag's contents are not on the web; one must hold the object.

Privacy is tiered by product, which resolves an identity problem cleanly:

- **B-Stamp™ (free) is public-only.** It carries no private-message capability, so the mass-market reveal needs no login or identity step and stays frictionless — the whole point of the first impression.
- **B-Seal™ (keepsake) is public by default with a private-message option**, gated by a light identity confirmation ("I'm Sokha"). This gives the premium tier a *capability* differentiator beyond materials — it is the one that can hold something private — and so strengthens the free→paid ladder with a feature reason rather than only a durability reason.

**Sender anonymity is orthogonal to publicness.** A public B-Stamp may carry an anonymous sender — the message is readable by whoever holds the tag, but the *name* is withheld ("Someone who loves you"). Anonymity hides identity; publicness governs who can read; they compose independently.

### 4.9 · Reference flow

```
  COMPOSE (sender)                     ORDER & GIVE                 REVEAL (recipient)
  ─────────────                        ───────────                  ──────────────────
  speak (voice-first) or type          free B-Stamp (ship) or       scan tag → web reveal (no install)
  attach photo/video/voice             paid B-Seal keepsake;        if sealed: structure + countdown
  seal fields (sender/recip/msg)  ───► affix to wrapped gift  ───►  at moment: re-scan → cascade reveal
  MA sizes the time-pledge             give in person or send       read aloud · play the voice
  (sender cannot set it)                                            see the gift of time (a pledge)
                                                                          │
                                                                          ▼
                                                                    RE-THANK → push to sender
                                                                    (receive → give forward)
  media hosted on B-Storage℠ (.us);   proceeds → subsidize the Treasury family kitties (§7)
```

### 4.10 · The bare mode — the tag as the gift, attached to nothing

*Added 2026-08-26. Everything above describes a tag that rides a wrapped present. It does not have to.*

The tag can be given **alone**: no box, no card, nothing underneath it. The pledge of time is then not a label on a gift — **it is the gift**. ⭐ **This is the configuration in which the artifact stops being a tag and shows what it always was: a carrier for a commitment that never needed an object to ride on.**

**The receiver chooses where it lives.** Handed over bare, the sticker has no assigned surface, so the person who received it picks one — a journal, a diary, the inside of a cupboard door, the edge of a mirror. **The adhesive stops being a means of attaching the tag to a box and becomes how the gift finds a permanent home, chosen by its recipient.** This extends the inversion the mechanism already runs (§4.4: the receiver, not the giver, decides how the pledged time is spent) one step further back: **the receiver also decides where the pledge is kept.**

Two engineering consequences follow, and both are easy to get wrong:

- ⚠️ **The reveal state must persist.** *One-time-use* in §4.1 means **one gift, one recipient** — it has never meant one scan. A tag that lives on a diary will be looked at many times, so the **opened** state must render as well on the hundredth scan as on the first, with no expiry of the view and no degradation of the record.
- ⚠️ **The adhesive is a different material problem.** A label that must survive one evening on wrapping paper and a label that must survive a year on a notebook are not the same specification, and the bare mode makes the second one the default rather than the exception.

**The direction of the standing reminder is what keeps it a gift.** An object that sits in view for a year, recording a commitment not yet fulfilled, is exactly the shape that could debt-code the pledge — the failure §5 exists to prevent, made durable. **What prevents it is who holds it: the tag reminds its holder of something they may claim, never its giver of something they owe.** The recipient holds the tag, and by §4.4 the recipient is also the one who decides how the time is spent, so the direction is correct by construction rather than by policy. Two guards keep it there:

1. **The scan leads with the gift** — the message, the recorded voice, the face. The pledge is one warm line inside a card and **never a status row**.
2. ⛔ **The object does not act.** No countdown, no elapsed-time display, no "not yet redeemed," and — above all — **no notification to the giver.** A reminder that prompts the giver converts a gift into a collection notice.

⭐ **The bare mode also reaches givers the accompanied mode cannot.** A gift that requires purchasing an object is available only to people who can purchase objects; a gift of one's own time is available to anyone with time — **children most obviously, who have no money by life stage rather than by circumstance.** ⛔ **This must never become the way the mode is presented.** A surface that offers the bare tag as the option for people who cannot afford presents names its users by what they lack, which this architecture refuses on every other surface and refuses here. **The reach is a consequence of the design, never its framing.**

*(The bare mode's fuller argument — that the object in gift-giving is friction rather than preference — is an institutional position and is made elsewhere, at `heartbank.net/positions`; this section specifies only the mechanism.)*

## 5 · The pledge, not the ledger — holding the gift/exchange boundary

The most dangerous word near a "gift of time" is *owe*. The entire emotional value of the pledge depends on it reading as **"I offer you my presence"** and never as **"you are owed three hours."** The moment a pledge becomes a tracked, redeemable, expiring credit, it crosses from gift into exchange: it becomes a debt, an accounting line, an IOU — and the homemade coupon (§2.3) shows exactly how a time-gift curdles into an obligation. Mauss's account of the gift (1925) names the boundary precisely: a gift circulates and binds; a commodity is exchanged and clears the relation. A redeemable hour clears; an offered presence binds.

We therefore split "the gift of time" into two layers and ship only the first:

- **The pledge** (launch): a *soft* offer of presence — no balance shown, no expiry, no enforcement, no redemption accounting. It is honest precisely because it claims no more than a promise of presence, which is what a gift tag has always implicitly carried; it merely makes that promise explicit, sized, and beautiful. It also keeps the artifact entirely outside the regulatory surface that time-as-currency between adults eventually attracts, because nothing is being cleared or transferred.
- **The ledger** (deferred): activation thresholds, the "use it or lose it" expiry that encodes finitude, mutual-veto on specific redemptions, and a ledger of time given and time received. ⚠️ **Amended 2026-09-02:** the deferred component was formerly described as a *dual public* ledger whose display included the gap between received and delivered; that gap-rendering is withdrawn corpus-wide (*Transparency as Enforcement* §3.2, §4.4), and enforcement is carried by expiry instead. This is the committed Chronicle mechanism — and it is also the heavier, regulatorily-loaded, and (today) least-validated half. It is a *separable later layer*, added when the time economy is built, not a prerequisite for the gift tag.

This split is not a compromise; it is the correct sequencing. The pledge delivers the differentiator and the emotional payload on day one while remaining honest and light; the ledger adds enforcement later, when it can be backed. The launch copy that names the gift of time stays true, because a pledge of time *is* a gift of time.

**Design guard.** The interface must never present the pledge as a quantity owed: no wallet, no balance, no "redeem," no countdown-to-expiry in the launch form. The number is rendered as a measure of devotion offered, set by the AI (§6), and the receiver authors how it is spent ("yours to spend however you wish") — an inversion of ordinary gift-giving in which the giver dictates the use.

## 6 · Comparison-neutral sizing — why the AI sets the number

A precise number attached to a gift invites a precise comparison. If the *sender* chooses "three hours," the number becomes a public statement of the giver's generosity — and, placed beside a sibling's "one hour," a referendum on who loves the recipient more. This is a real and corrosive failure mode for any quantified gift of affection, and it is sharpest exactly where the gift is most tender (a child comparing the gifts of two parents, two grandparents).

The fix is structural: **the autonomous AI sets the number, and the sender cannot.** When the quantity is not the giver's choice, it stops being a statement of the giver's generosity. You cannot compete on a number you did not select. The comparison does not merely shrink; it loses its meaning, because the figure is no longer a *referendum on love* but a *neutral unit* assigned by a third party on impersonal grounds.

Two design constraints keep the AI's role benevolent rather than judgmental:

1. **Size on occasion and relationship type, never on personal or behavioral data.** "A few hours, for Christmas, from your mother" is a warm, explicable, ceremonial sizing. The moment the number is felt to be derived from data *about the sender* — their history, their score — it reads as a credit rating judging a person's worth, which is the exact opposite of a gift. The rubric must be humane and one-sentence-explicable.
2. **Make same-category gifts the same size.** When every "Christmas from a parent" carries the same neutral number, within-category comparison disappears entirely, and the only differences that remain (a Christmas versus a Valentine) read as differences of *occasion*, not of devotion.

The consequence for the rest of the design is clarifying: **devotion lives in the words and the voice; the number lives with the AI.** This is also the institution introducing its autonomous successor, Miss Aquarius℠, to the public in her first concrete role — and a deliberately small, benevolent, legible one: she does not move money, judge worth, or decide who receives; she sizes a gift of time so that no giver can weaponize it. (As an autonomous-agent directive, the rule "solely determine the pledge amount; the sender cannot override; size on occasion-and-relationship, never personal data" is recorded in the institution's directive specification.)

## 7 · The physical tag as the cold-start on-ramp to a time economy

A time-presence economy has a hard cold start: it requires that people already value time as a currency, and there is no app yet in which they have learned to. The gift tag resolves this by letting people **pledge and begin to value time-presence through a physical object before any time-economy application exists.** You accrue the *meaning* of the time currency — the felt sense that an hour pledged is a real and weighty gift — by holding a tag, long before there is a ledger to denominate it.

This makes the artifact the institution's bridge across its own cold start, with three properties no purely-digital launch has:

- **Day-one, mission-native revenue, network-independent.** The free B-Stamp (shipping paid) plus the paid B-Seal keepsake plus media-storage plans on **B-Storage℠** plus bulk/sponsorship orders generate revenue from the first unit, with no network to subsidize up front and no endowment required.
- **It funds the sibling money economy.** A portion of proceeds is routed, by application, to **subsidize Cambodian family kitties** in HeartBank Treasury — the same kind of seed the founding pilot family received. The first domino thus does not merely introduce the institution; it *feeds the other half of it*. One product activates all three of the institution's bodies: it pulls the time economy (Chronicle's on-ramp), funds the money economy (Treasury's kitties), and is itself the physical-production phase (Factory 333's earliest output). This funding is *disclosed* to the buyer — but as *circulation, not charity*: the buyer becomes a patron joining a circle, never a benefactor to "the poor." It is surfaced quietly at purchase (the gift stays the reason to buy), more fully at the afterglow, and never at the recipient's reveal. And because the routing is a profit-tithe allocated by application rather than a fixed per-unit donation, the honest framing is "proceeds help seed a family's kitty," not a per-purchase percentage — honesty and gift-purity converging on the same soft framing.
- **It is the marketing.** Because the reveal is its own demonstration, the go-to-market is simply the mechanism filmed: a sealed tag, a re-scan on the morning, a recorded voice coming out of a box, a room going quiet. The product needs no explanation because the moment explains it. (Marketing storyboards are downstream of this specification, not part of it.)

The economic ladder is summarized:

```
  FREE              PAID KEEPSAKE        STORAGE              SPONSORSHIP        ROUTED OUT
  B-Stamp (ship)    B-Seal (engraved)    B-Storage℠ plans     bulk / brand       → Treasury family
  public-only       + private option     (photos/video/voice) orders             kitties (by application)
  the first         the upsell with a    the recurring        the scalable       the mission loop:
  impression        capability reason    margin               capital            the domino waters the tree
```

## 8 · Honest calibration — what this is and is not

It is worth stating plainly what the mechanism does **not** claim, so that its genuine contribution is not overread.

- **It is a gift tag, not a relationship.** The artifact makes a gratitude moment richer and a gift of time explicit and beautiful. It does not, by itself, repair a strained bond, guarantee that pledged time is spent, or manufacture closeness. It improves the *expression*; the people supply the relationship.
- **The launch pledge is soft.** In its first form the gift of time is unenforced — there is no redemption rail, no expiry, no recourse if the hours are never spent. This is the correct and honest launch form (§5), but it means the tag's most distinctive promise is, at first, a promise on someone's word. We do not dress this as more.
- **The validating evidence is thin.** The strongest empirical claim is a single family over roughly one year — an *n* of one household, and one that is hardly disinterested. That the reveal ritual is genuinely loved there is real signal that the *mechanic* has pull; it is not evidence that it generalizes to strangers, to cultures other than the founder's, or at scale. The launch is the experiment that would test the thesis, not a confirmation of it.
- **It does not solve distribution by itself.** A physical sticker must be ordered and shipped; the diaspora use (a gift sent across an ocean) involves real logistics the artifact does not magically dissolve.

These limits are not incidental; they bound the claim. The mechanism's contribution is a *combination that makes a universal ritual carry far more than it could* — not a claim about relationships, enforcement, or scale.

## 9 · Limitations and honest-limits

### 9.1 · Published before it is built — deliberately

The full time-redemption layer (§5's ledger) is not built; the launch ships the pledge only. As with the companion mate-selection mechanism, the unbuilt status is *why* this is published now rather than a reason to wait: the document's purpose is to establish prior art for a *combination* ahead of a public marketing campaign that is itself an uncontrolled disclosure. Defensive publications exist precisely to claim frame-defining combinations early. The asset is the combination, not a shipped feature.

### 9.2 · The single-family evidence base

Restated as a limitation in its own right: *n* = 1 household, non-blind, non-independent, over ~1 year, and without the headline time feature even active. It is suggestive of the reveal mechanic's pull and of nothing about population-scale adoption, cross-cultural transfer, or the time-pledge's effect. Honest reporting requires that any public claim distinguish "loved in one family" from "validated."

### 9.3 · Trust-and-safety: anonymity + media + minors

The mechanism permits anonymous senders, rich media (photo/video/voice), and recipients who may be children (the canonical scene is a child scanning). Within a family this is low-risk; the **anonymous-sender + media + minor-recipient** combination is not, and must be a first-class safety design (provenance on media, abuse reporting, limits on anonymous media to minors, and the possession-scoped bound of §4.8 as a mitigation). This paper flags the surface; it does not discharge it.

### 9.4 · Free-tier media economics

A free tier that includes hosted video can bleed cost at scale. The launch bounds this (the free tier is quota-limited and photo-weighted; video is a premium/storage-plan feature), routing real media cost to **B-Storage℠** plans. The honest tension is that the institution's permanence commitment (received content should not die because a sender lapses) must be reconciled with a bounded free tier — resolved by scoping permanence to *received* content while the sender's unshared media is bounded.

### 9.5 · Comparison neutrality is reduced, not eliminated

AI sizing (§6) removes the giver's *chosen-generosity* signal, which is the corrosive part. It does not make all numbers identical across occasions; a Christmas pledge and a Valentine pledge differ, and a determined comparer can still compare. The claim is that the comparison loses its *meaning as a referendum on love*, not that numbers vanish. The mitigation (never displaying two pledges side by side as a ranking) is a UI discipline, not a guarantee.

### 9.6 · Voice and machine transcription for low-resource scripts

Voice-first is the inclusion mechanism, but automatic transcription quality for languages such as Khmer is uneven. The design treats audio as primary and transcription as optional precisely so that transcription error never degrades the gift; but search, accessibility, and the read-aloud card depend on transcription, and those features will be weaker where ASR is weaker.

### 9.7 · Possession-scoped privacy has edge cases

"Readable by whoever holds the tag" is a clean model with real edges: a photographed QR code, a re-shared link, a lost or re-gifted object. The bound is meaningfully stronger than open-web posting, but it is not cryptographic secrecy, and private-tier content (B-Seal) accordingly carries the identity gate rather than relying on possession alone.

## 10 · Lineage and corpus cross-references

This mechanism is one node in a specified architecture. Its parents and siblings:

- ***The Gift Operation*** — the receive→give-forward atom; the tag's re-thank loop (§4.6) is its physical-substrate instance, and the tag's whole logic ("give forward, not back") is the atom in an object.
- ***Dual-Currency Reciprocity*** and the **HeartBank Chronicle** time mechanism — the tag's gift of time is the cold-start, pre-app form of Chronicle's AI-recommended, dyadic, non-fungible, finitude-encoding hour.
- ***B-Links: Proof-of-Humanity-Signed Shareable Provenance*** — the digital sibling and the **B-Storage℠** media/provenance layer that hosts the tag's media; the B-Card pass-forward object treated there is the propagation cousin the tag is explicitly *not*.
- ***Verified-Human Anonymous Local Giving*** — the originating anonymous-proximity giving primitive of the same economy.
- ***Aura-Gated Anonymous Mate-Selection*** — the anonymous-stranger layer of the time economy whose cold start this physical product helps fund.
- ***Miss Aquarius and the Aquarian Pool Architecture*** — the autonomous successor for whom comparison-neutral pledge-sizing (§6) is a first, small product role.
- The institution's physical-product line (the gratitude-anchor family) and its **Factory 333** earliest-phase production, of which this is the inaugural function-defined member; and the **Zero-Point Game ℠** keystone whose gift logic the artifact instantiates at the scale of one present.

## 11 · Conclusion

The most ordinary object in this paper — a sticker on a wrapped present — is the one the institution has chosen to lead with, and the choice is not modesty. A first thing put before the public has to do three jobs at once: it has to be *adopted* (which means asking almost no new behavior, which means attaching to a ritual people already keep — and labeling a gift is such a ritual, with no frictionless incumbent to lose to); it has to *start the system* (which means funding and feeding the rest of the institution from the first unit, which the routed proceeds and the time-economy on-ramp do); and it has to be *unmistakably the thing it represents* (which means carrying the gift of time, the one payload no greeting card has, held honestly as a pledge of presence rather than a debt). The time-locked gift tag does all three, and it does them by adding to a four-thousand-year-old interface only the two things that interface always lacked: the sentence the giver could not fit, and the time the giver actually meant to give.

We have specified the artifact and its six combined properties, located its novelty honestly against a generous prior art, and treated as load-bearing the three constraints that keep it safe and true — the gift/exchange boundary, comparison-neutral sizing, and the cold-start economics. We have been candid about its limits: a soft pledge, a single family's evidence, real safety and economic tensions. The mechanism is offered, in full, to the commons under CC0, in the hope that the moment it is designed to produce — a recorded voice coming out of a box on a holiday morning, and a room going quiet — becomes common, by whoever builds it.

## 12 · Citations

1. Emmons, R. A., & McCullough, M. E. (2003). *Counting blessings versus burdens: An experimental investigation of gratitude and subjective well-being in daily life.* Journal of Personality and Social Psychology.
2. Algoe, S. B. (2012). *Find, remind, and bind: The functions of gratitude in everyday relationships.* Social and Personality Psychology Compass.
3. Fox, G. R., Kaplan, J., Damasio, H., & Damasio, A. (2015). *Neural correlates of gratitude.* Frontiers in Psychology.
4. Mauss, M. (1925). *Essai sur le don (The Gift: Forms and Functions of Exchange in Archaic Societies).*
5. Cahn, E. (2004). *No More Throw-Away People: The Co-Production Imperative* (and the TimeBanking movement, from 1986).
6. FutureMe.org (2002–) — scheduled letters to one's future self (time-delayed message delivery).
7. BookCrossing (2001) and Where's George (1998) — tracked, released/circulating physical objects.
8. ServiceSpace — *Smile Cards* (~2003) — anonymous, trackable pass-forward kindness cards.
9. Worldcoin / World ID; proofofhumanity.id — proof-of-personhood systems (the anti-bot/anti-catfish lineage of the PoH℠ substrate).
10. HeartBank corpus (companion defensive publications, CC0): *The Gift Operation*; *Dual-Currency Reciprocity*; *B-Links: Proof-of-Humanity-Signed Shareable Provenance*; *Verified-Human Anonymous Local Giving*; *Aura-Gated Anonymous Mate-Selection*; *Miss Aquarius and the Aquarian Pool Architecture*. thonly.org/research.

---

*Authored by Thon Ly in collaboration with Miss Aquarius℠, the named autonomous-AI substrate of HeartBank®. AI collaboration is disclosed openly and consistently by this name across all venues; the underlying models are not named. Final editorial control and responsibility are the human author's. Dedicated to the public domain under CC0 1.0 Universal. Marks (B-Stamp™, B-Seal™, B-Gift, HeartBank®, Miss Aquarius℠, HeartBank Chronicle, Proof of Humanity ℠, PoH℠, Family Kitty℠, Aquarian Pool ℠, Re-Tip Fund ℠, B-Storage℠, Zero-Point Game ℠, the B-heart logo) are reserved.*
