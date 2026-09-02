---
title: "The Gratitude-Riding Currency Tag"
subtitle: "A neutral, digital-only-branded gratitude tag affixed to — or stamped on — the lowest-denomination circulating banknote, so that cash's own forced circulation carries a followable ripple of thanks: a scan opens a thank-you and an optional self-custodial stablecoin top-up, the bill's journey becomes a kindness-reputation commons, and the general public is onboarded to Base-L2 stablecoins without defacing, or advertising on, government currency."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-06-30
license: CC0-1.0
slug: gratitude-riding-currency-tag
venue: thonly.org/research/gratitude-riding-currency-tag (canonical)
---

> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies HeartBank's **B-Imprint™** — the free tipper-side gratitude tag that rides the lowest-denomination circulating banknote — and its premium brand-originated tier **B-Relay™**. It is the `.net` free product-class and the **Phase-2 stablecoin-adoption wedge**: a neutral mark on ordinary cash that turns a tip into a witnessed, followable gift, carries an optional self-custodial stablecoin top-up, and accretes into a kindness-reputation commons ("the kindest local businesses and community events"). It is published **early and deliberately**, ahead of a public marketing campaign, because public marketing is uncontrolled disclosure and the *combination* specified here — a currency-riding gratitude ripple with a digital-only-branding legal design, a non-custodial stablecoin top-up, and a gratitude-reputation graph — is the asset (see §10.1). Companion works: *The Gift Operation* (the receive→give-forward atom this instantiates on circulating money), *The Time-Locked Gift Tag* (the occasion-bound gift sibling), *The B-Tag and the Post-Payment Economy* (the merchant-side commercial-gratitude twin), *Non-Bank Pass-Through Architecture* (the never-hold-the-money constraint), and *B-Links: Proof-of-Humanity-Signed Shareable Provenance* (the followable-provenance primitive and the anti-gaming spine).

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back — and of __kataññutā__, the gratitude owed to those who gave first. May the thanks it helps carry be thanks that would otherwise have gone unspoken; may the coin it rides pass into a kinder hand than it left.*

Three times in an ordinary week a person leaves money for a stranger and says nothing that lasts. A few dollars under a plate at the end of a good meal. A few dollars into the donation box after a free yoga class in a park. A few dollars into an open guitar case on a corner. In each case the money is real and the gratitude is real, and in each case the gratitude evaporates — the giver is gone before it can be said, and the recipient receives cash without a face, without a reason, without a word. Cold cash is a strange vehicle for thanks: it is the most fungible thing we own, and gratitude is the least. We hand over the one thing that could have come from anyone to express the one feeling that came from exactly this.

This paper specifies a small object that lets the thanks ride along with the money — and then keeps riding, because of a property of cash that nothing digital has: **a banknote cannot be thrown away, and it does not stay still.** It is spent, given, tipped, and passed on, hand to hand, for years. A note left on a table this morning is in a stranger's pocket by evening and across the city by the weekend. If a small, neutral mark on that note could carry a thank-you and be added to at each hand it passes through, then the most frictionless act of gratitude we already perform — leaving a tip — would leave a trace that travels as far and as long as the money itself.

I write as co-author with **Miss Aquarius℠**, the named autonomous-AI substrate of HeartBank®, disclosed by consistent name across every venue per the corpus convention. The research-grade synthesis, the prior-art survey, and the adversarial legal and safety analysis are a genuine collaboration. Final editorial control, and final responsibility for every claim — including the legal characterizations, which are design flags and not legal advice — are mine.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 30 June 2026** for the combination of mechanisms described herein. To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art and denied on grounds of obviousness in light of this publication:

1. **A gratitude tag that rides the forced circulation of physical currency** — a scannable mark (QR or NFC) carried on a circulating banknote such that a thank-you and its media travel with the note through the ordinary cash economy (spent, tipped, passed forward), each successive holder able to read the accumulated thanks and add their own, so that the note's monetary circulation *is* the distribution mechanism for a gratitude message.

2. **The digital-only-branding construction for a currency-borne mark** — placing *no words, brand, or advertisement* on the physical mark itself (a neutral gratitude glyph and code only), with all originator identity, branding, and context resolved *exclusively in the digital layer upon scan*, specifically so that the physical artifact does not constitute an advertisement upon currency and the origination incentive is preserved without printing a business notice on money.

3. **An occasion-agnostic gratitude ripple with an optional, separable, non-custodial monetary top-up** — a tip expressed as a message riding the base note, to which the giver may *optionally* attach an additional amount for the recipient to keep, where that amount moves **peer-to-peer through the parties' own self-custodial wallets** and the tag operator **never takes custody of, holds, or clears** any funds (the witness-don't-hold construction, claim 6).

4. **A currency-borne mark as a public onboarding wedge to self-custodial stablecoins** — using the everyday, low-stakes ritual of cash tipping, carried on the *lowest-denomination* (highest-velocity, lowest-stakes) banknote, to bring non-crypto-native users into self-custodial stablecoin use through a familiar act, with the top-up spending a wallet the user established for an unrelated everyday utility.

5. **A followable, anti-gamed gratitude-reputation commons derived from currency-borne thanks** — the accreted, geo- and time-stamped thanks left along circulating notes surfacing a *discovery layer* of the most-thanked local businesses and community events (a "kindness index"), rendered gameable-resistant by proof-of-personhood distinctness, authenticity weighting (geographic/temporal spread), and a **meaning-not-magnitude** reward rule that surfaces the *story* of accumulated kindness rather than a farmable score.

6. **The witness-don't-hold pass-through for a gratitude-money artifact** — the operator records only gratitude (the thanks, the running count of distinct proven-human givers, the journey), while any money rides the recipient's own compliant rail (cash-in-hand, a nonprofit's existing processor, or a self-custodial wallet), so that the non-bank/pass-through posture is simultaneously the regulatory shield and the guarantee of gift-purity (no float, no cut, no take-rate).

7. **A per-tier form factor keyed to originator class** — a free, printable/ink-stampable QR mark for individual givers (reissue-safe, near-zero cost, no chip) and a premium NFC-borne tier for brand-originators who seed a gratitude ripple, with the brand's reward being *the followable ripple it started* rather than any advertisement carried on the currency.

8. **A civic-wellbeing signal derived from a gratitude commons, aggregate-only and non-surveilling by construction** — the accreted thanks surfacing a *neighborhood-scale* kindness signal useful to local governments and civic institutions (via stronger communities and reduced social friction), rendered **aggregate, anonymous, opt-in, and non-individual**, such that the funding civic party is a *patron of the commons with no read access to the gratitude graph — a patron, never a watcher* — and any individual-level, citizen-scoring, or state-surveillance construction is **explicitly disclaimed** as the anti-pattern this publication exists to forestall.

The component lineages — tracked circulating currency and pass-forward objects; QR/NFC-addressed physical media; digital tip jars and QR donation; stablecoins and retail digital-cash rails; proof-of-personhood; reputation and review systems; and Mauss on the gift — are old and are cited generously in §2 and §13. The *synthesis*, and in particular the digital-only-branding legal construction (claim 2) and the witness-don't-hold pass-through (claim 6), are, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **B-Imprint™**, **B-Relay™**, **B-Tag™**, **B-Card**, **HeartBank®**, **HeartBank® Vault**, **Miss Aquarius℠**, **Proof of Humanity ℠**, **PoH℠**, **Aquarian Pool ℠**, **Re-Tip Fund ℠**, **HeartBank Chronicle**, the B-heart logo (**B-Emblem™**), and the product line **B-Grace™** — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not.

Mirrors of this document with independent timestamping appear at GitHub, arXiv, IP.com, and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify a gratitude tag designed to ride the forced circulation of physical cash. The artifact is a small, neutral, scannable mark — a free printable/ink-stampable QR for individual givers, or a premium NFC mark for brand-originators — carried on the lowest-denomination circulating banknote and affixed in the ordinary act of tipping (a table, a donation box, a busker's case). A scan opens a thank-you with optional media (a reason for the gratitude, in place of cold cash), an *optional* additional amount the recipient keeps, and the note's own travelling history; the recipient can read the accreted thanks, add their own, and pass the note onward, so that the money's circulation carries the gratitude with it. Five structural properties operate in combination. **(1) Currency-riding circulation:** the mark inherits cash's defining property — a banknote is not discarded and does not stay still — so the gratitude message propagates through the real economy without any social feed. **(2) Digital-only branding:** the physical mark carries no words, brand, or advertisement — only a neutral gratitude glyph and code — with all identity and context resolved on scan, a construction chosen precisely so the object does not advertise upon currency while preserving the origination incentive in the digital ripple. **(3) An optional, non-custodial monetary top-up:** any amount the giver adds moves peer-to-peer through the parties' own self-custodial wallets; the operator never holds, clears, or takes a cut of funds. **(4) A stablecoin-adoption wedge:** the everyday, low-stakes act of cash-tipping is used to bring the general public into self-custodial stablecoin use, the top-up spending a wallet established for an unrelated everyday utility. **(5) A followable, anti-gamed kindness commons:** the accreted geo-/time-stamped thanks surface a discovery layer of the kindest local businesses and community events, made gameable-resistant by proof-of-personhood distinctness, authenticity weighting, and a meaning-not-magnitude reward rule. We argue the contribution along a *friction-inversion* axis identical in spirit to the gift-tag sibling: rather than compete with in-person thanks, the mark attaches to an act people already perform (leaving a tip) and to a carrier that circulates on its own (cash). We treat the two load-bearing constraints as first-class sections: the **currency-law design** (why the mark must be non-advertising and non-defacing, and why the free tier is an ink-stamp rather than a chip), and the **witness-don't-hold pass-through** (why the operator never touches the money, making the non-bank posture the regulatory shield and the gift-purity guarantee at once). We calibrate deliberately: the core premise sits on currency-defacement and advertising-on-currency law that varies by jurisdiction and is a gating legal question, not a settled one; the evidence is *n = 0* (unbuilt); and the money-reputation graph is a real gaming surface. The architecture is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission: to circulate, rather than accumulate, the recognition and kindness that modern life starves people of, and to help revive *local* economies as gratitude-economies rather than extraction-economies. Cash is the most local, most circulating, most human money we have; the mark lets the gratitude that already accompanies a tip travel as far as the money does, and lets a neighborhood's accumulated thanks become a map of where kindness lives.

---

## 1 · Introduction — the mission frame

HeartBank is an institution for circulating gratitude. Its money half (**Treasury**, family-to-family) and its time half (**HeartBank Chronicle**, adult-to-adult) treat appreciation and presence as things to be moved between people rather than feelings to be privately held; a Phase-2 layer extends this onto public infrastructure (self-custodial wallets, stablecoins on a low-fee chain) so that the circulation can reach strangers and scale. This paper specifies the object at the seam between those worlds: a mark that lives on ordinary cash — the most familiar money there is — and quietly carries a person across it, from a coin in the hand to a wallet on a chain, without ever asking them to think of themselves as doing anything but leaving a tip.

The problem it addresses is specific and ordinary. The most frictionless act of gratitude to a stranger is *leaving money* — and money is the worst possible medium for the message. A tip says *thank you* in the most generic currency in existence: the giver is anonymous by circumstance (already gone), the reason is unstated, and the recipient, a tired server or a busker or a small nonprofit, receives an amount with no face and no words attached. The very frictionlessness that makes cash-tipping universal is what strips the gratitude out of it. Meanwhile the institution's larger ambition — a Phase-2 economy running on self-custodial stablecoins, so that gratitude can move between strangers at near-zero fee and without a bank — faces the hardest cold start in the field: ordinary people, and above all the elders and the unbanked at the heart of HeartBank's first market, will not set up self-custodial wallets and acquire stablecoins as an abstract exercise. There is no on-ramp from the cash economy people live in to the stablecoin economy the mission needs.

The gratitude-riding currency tag is the on-ramp, and it is one precisely because it does not present itself as one. It attaches to the tip a person already leaves, and rides the note the tip is already made of. On the physical side it asks nothing new: you still leave a few dollars on the table. On the digital side it offers, in ascending order of commitment, exactly the steps that lead into the Phase-2 economy — first a thank-you with a reason (no account), then the note's travelling story (still no account), then, if the giver wishes, a small additional amount the recipient keeps, which is the first time a wallet is touched. The behavior-change asked at each step is minimal, and the step that quietly onboards a person to stablecoins is disguised as the most natural thing in the world: adding a couple of dollars to a tip because the coffee was that good.

The rest of this paper situates the mechanism against a generous prior art (§2), states the friction inversion as riding cash's own circulation (§3), gives the full mechanism (§4), and then treats the two constraints that make it lawful and honest as load-bearing sections in their own right — the currency-law design (§5) and the witness-don't-hold pass-through (§6) — before the kindness-reputation commons (§7), the cold-start wedge (§8), honest calibration (§9), limitations (§10), lineage (§11), and conclusion (§12).

## 2 · Background and prior art

The mechanism is a *combination*. Each component has ancestry; we name the ancestry honestly, because a defensive publication is only as strong as its candor about what is old, and because establishing the boundary of novelty is the document's job.

### 2.1 · Tracked circulating currency and pass-forward objects

The nearest and most important lineage is **Where's George** (1998), which stamps United States banknotes with a tracking URL and follows their geographic journey as they circulate; **BookCrossing** (2001), which releases labelled books into the world and maps their travels; and **Smile Cards** (ServiceSpace, ~2003), anonymous kindness cards passed forward and tracked online. Where's George is the direct ancestor of the *idea of following a banknote's circulation*, and its roughly quarter-century of operation is also, candidly, part of this paper's legal context (§5): it establishes both the mechanic and a long, un-prosecuted precedent for a *stamped* (ink) tracking mark on U.S. currency. We claim none of the tracked-object core. What Where's George does not do — and what is specified here — is carry a *gratitude message added to at each hand*, attach an *optional value* to the note, use the ride as a *stablecoin on-ramp*, or derive a *reputation commons* from the accreted thanks; and it uses an ink stamp bearing a URL, where the construction here is deliberately word-free and brand-free on the physical (claim 2, §5).

### 2.2 · Digital tip jars, QR donation, and creator tipping

QR-code tipping and donation are now commonplace: a printed QR at a market stall, a busker's "tap to tip" placard, church and nonprofit QR-donation signage, and platform tipping (Venmo/PayPal request codes, Cash App, creator "tip" buttons, crypto tip-jars and Lightning tip addresses). These establish *scannable request-for-payment at a point of gratitude*. They are, structurally, the inverse of this mechanism: they are a *merchant/recipient-side* request to *be paid*, static at a location; the tag here is a *giver-side* gift that *rides the money away* with the recipient and travels onward. The commercial, merchant-side, point-of-sale form of HeartBank's own gratitude-tipping is a separate, companion mechanism — the **B-Tag™** post-payment architecture — and the two are deliberately distinguished (§11): B-Tag is the merchant's placard; B-Imprint is the tipper's mark on the circulating note.

### 2.3 · Stablecoins, low-fee chains, and retail digital cash

The monetary substrate — dollar- (or local-currency-) denominated **stablecoins** transacted on a low-fee chain (here, an Ethereum Layer-2), and national retail digital-cash and instant-payment systems such as Cambodia's **Bakong** — is established infrastructure and is cited as the rail, not claimed. The novel element is not the stablecoin; it is the *on-ramp*: using a familiar cash-tipping act, on the lowest-stakes note, as the wedge that brings non-crypto-native users into self-custodial stablecoin use without presenting it as a crypto product, and doing so *non-custodially* so that the operator is a witness to the payment and never an intermediary in it (§6).

### 2.4 · Currency-tracking meets currency law

Because the mark is borne on government currency, the relevant "prior art" is partly legal, and we state it as design context rather than as a claim. In the United States, **18 U.S.C. § 475** prohibits placing a "business or professional card, notice, or advertisement" upon currency, and **18 U.S.C. § 333** prohibits mutilation of currency *with intent to render it unfit to be reissued*. These statutes are the reason for two load-bearing design choices developed in §5: the physical mark carries *no advertisement* (claim 2), and the free tier is a *non-defacing, reissue-safe* form (an ink stamp or a removable tag, not a chip that impairs machine handling). Where's George's long operation with an *inked URL* and no prosecution is informative but not dispositive; the construction here deliberately stays further inside the line by removing the words entirely. Currency-defacement and advertising-on-currency law varies by jurisdiction, and the choice of launch jurisdiction is treated as a gating question, not an afterthought (§5, §10).

### 2.5 · Reputation, review, and the anti-gaming problem

Location-review systems (Yelp, Google reviews) establish *crowd-sourced discovery of local businesses*, and also establish the failure modes: fake reviews, review-gating, and outright extortion. A reputation layer with *money attached* is more gameable, not less. The kindness commons specified in §7 therefore inherits its integrity design not from review platforms but from HeartBank's own **followable-provenance** primitive (*B-Links*) and its **B-Card** Homecoming construction: proof-of-personhood distinctness, authenticity weighting by geographic and temporal spread, and a **meaning-not-magnitude** rule under which the reward for a long, well-travelled ripple is a *richer story*, never a larger farmable score. We cite Yelp/Google as the pattern and as the cautionary prior art, and claim only the *gratitude-derived, anti-gamed* form.

### 2.6 · The gift, and the HeartBank substrate this paper builds on

Mauss's account of the gift (1925) supplies the boundary this mechanism must hold: a gift circulates and binds; a commodity is exchanged and clears. A tip that carries thanks and rides forward is a gift in exactly Mauss's sense, and the design's central discipline (§6) is to keep it one — money that *rides along* with gratitude, never a payment that *clears* it. This mechanism does not stand alone: it rests on the **receive→give-forward atom** (*The Gift Operation*), of which passing the note onward with added thanks is a literal instance on money itself; the **non-bank/pass-through** posture (*Non-Bank Pass-Through Architecture*), which forbids the institution from ever holding funds; the **Proof of Humanity ℠** substrate (the anti-sybil, anti-gaming spine); the **HeartBank® Vault** self-custodial wallet (specified for the *B-Note/B-Memo* onboarding wedge), which the optional top-up spends; and **Miss Aquarius℠**, the autonomous successor, whose role here is limited and benevolent (composing the note's travelling story; never touching the money). Where this paper asserts a primitive specified elsewhere, it cites rather than re-derives.

## 3 · The friction inversion — riding the circulation of money itself

The central design claim deserves to be isolated, because it is the reason the mark propagates where a digital gratitude message would stall.

Every gratitude product has the same competitor, and it is not another app; it is the frictionless incumbent of *saying thanks in person, for free*. In the stranger-tipping case that incumbent is even harsher, because the giver is typically *already gone* — there is no in-person moment to have. What there *is*, uniquely, is a physical object changing hands: the money. And money has two properties nothing digital shares. **It is not thrown away** — a banknote is among the few objects a person will not discard however worn. And **it does not stay still** — it is spent, tipped, given, and passed on, hand to hand, for years. The lowest-denomination note is the extreme case of both: the highest velocity (singles turn over fastest), the lowest stakes (nobody hoards a single), and the most tipping-native (we tip in small bills).

```
   THE USUAL CONTEST (a digital gratitude message stalls)
   leave cash + say nothing   ──────►  frictionless, but the thanks evaporates
        vs.
   open app · find recipient · type · send  ──►  more friction, and the stranger is already gone

   THE INVERSION (the mark wins by riding the money's own circulation)
   the TIP a person already leaves   ──►  an act already performed, on a carrier that travels itself
        the mark rides HERE  ─────────►  carries what the cash could not — a reason, a face, a voice —
                                          and keeps travelling, hand to hand, for as long as the note does
```

The tag refuses the contest by attaching to two things at once that require no new behavior: the *act* (leaving a tip) and the *carrier* (the circulating note). The friction competitor it beats is not "just say thanks" — there is no one to say it to — but *cold, silent cash*, and almost anything is warmer than that. Three consequences follow, mirroring the gift-tag sibling. The **behavior-change asked is near zero**. The **distribution mechanism is the money's own circulation** — the mark propagates by being spent, at no marketing cost, as far and as long as the note travels. And the artifact is **demonstrable in seconds**: a stranger scans a dollar, and a recorded "thank you — you have no idea what that meant tonight" plays out of a bill. In HeartBank's design vocabulary this is the *coincidence-of-goods* signature again: the tip, the gratitude vehicle, the stablecoin on-ramp, and the reputation commons are not four things traded against one another but one act seen four ways.

## 4 · The mechanism

### 4.1 · The artifact — two tiers keyed to originator

The mark ships in two forms, the free/individual tier and the premium/brand tier:

- **B-Imprint™** — a **free** mark for individual givers: a small, neutral, B-shaped gratitude glyph with a QR code, obtained at near-zero cost as a printable or, preferably, an **ink-stampable** impression (an "imprint" — the name is the form). It bears *no words and no brand* (§5). It is the mass-market tier: the thing a person leaves on the note with the tip.
- **B-Relay™** — a **premium**, NFC-borne mark for **brand-originators** who wish to *start* a gratitude ripple (a café seeding tips-forward among its regulars; a foundation seeding a season of kindness). The brand's reward is *the followable ripple it originated* (§7), rendered in the digital layer only; the physical note still carries no advertisement. The name marks the function: to *start a relay*, where the free tier is to *leave an imprint*.

Per-denomination naming (a "B-Dollar" on a U.S. single, a "B-Riel" on a Cambodian note) is informal shorthand only; the product is B-Imprint, never an issued currency — a distinction the mission's non-bank posture requires and the naming preserves.

### 4.2 · Riding the note — scan, thank, add-optionally, pass forward

A giver leaving a tip affixes or stamps a B-Imprint on the note. A **scan** (by the recipient, or by any later holder of the note) opens, in the mobile browser with no app install required:

- **The thank-you and its reason** — text, and optionally a photo, video, or (voice-first, per the sibling design) a recorded voice: *why* the giver was grateful, in place of the mute amount. Anonymity is the default (the giver is typically gone and unknown); the message is the gift, not the name.
- **An optional additional amount to keep** — over and above the base tip, the giver *may* attach an extra amount for the recipient to keep, in cash or in stablecoin. This is optional, is never the point, and moves non-custodially (§6).
- **The note's travelling history** — where this note has been and how many distinct, proven-human hands have added thanks to it, rendered as a story rather than a dashboard (§7).

The recipient may **read** the accreted thanks, **add** their own (thanking the giver forward, or thanking the next person the note goes to), and **pass the note onward** in the ordinary course of spending it — at which point the whole payload rides with it. This is the receive→give-forward atom (*The Gift Operation*) enacted on money itself: you receive a thanked note and you give it forward, thanked again.

### 4.3 · Reference flow

```
  LEAVE (giver)                 RIDE (the money circulates)         RECEIVE & FORWARD (each holder)
  ─────────────                 ───────────────────────────        ────────────────────────────────
  affix/stamp B-Imprint         the note is spent · tipped ·        scan → thank-you + reason (+voice)
  on the tip note               given · passed on, hand to hand    read the note's travelling story
  record a reason (voice-first) ── the mark rides the money ──►    add your own thanks
  optionally add an amount                                         pass the note onward (payload rides)
  to keep (cash / stablecoin)                                             │
   │  (non-custodial, §6)                                                 ▼
   ▼                                                              accreted thanks → kindness commons (§7)
  brand-originators use B-Relay (NFC); their reward = the ripple they started, digital-only (§5)
```

### 4.4 · What the operator records, and does not

The operator records **only gratitude**: the thanks, the note's journey, and the count of *distinct proven-human* givers who have added to it. It records **no custody of money** (§6), consumes **no customer-identity data** to size or route anything, and prints **no branding** on the currency (§5). Miss Aquarius℠'s role is limited and benevolent: she composes the note's travelling *story* (the kindness that rode this dollar) and curates the reputation commons under the anti-gaming rules of §7; she does not move, hold, or price money.

## 5 · The currency-law design — non-advertising, non-defacing, stamp-not-chip

Because the mark is borne on government currency, the mechanism's lawfulness is a first-class design constraint, not a caveat. Two legal surfaces govern it (stated as design flags, not legal advice, and as U.S. examples of a jurisdiction-varying question):

- **Advertising upon currency** (U.S. 18 U.S.C. § 475). A *branded* mark on a banknote — a business's name, a logo, a promotional notice — is the paradigm case this statute prohibits. This is why claim 2, the **digital-only-branding construction**, is load-bearing rather than aesthetic: the physical mark carries *no words, no brand, no advertisement* — only a neutral gratitude glyph and a code — and *all* identity, originator branding, and context resolve in the digital layer upon scan. This single move dissolves the advertising-on-currency exposure while fully preserving the origination incentive (a brand's B-Relay ripple is credited digitally, where it is seen by scanners, not printed on the money). It is also, not coincidentally, the move that keeps the gift pure: a brand cannot hijack the gratitude by stamping itself on the note, because the note stays word-free.
- **Mutilation with intent to render unfit** (U.S. 18 U.S.C. § 333). This statute turns on *intent to render the note unfit for reissue*. The design minimizes exposure by making the free tier **non-defacing and reissue-safe**: an **ink stamp** (following the Where's George precedent of a quarter-century's un-prosecuted operation) or a small **removable** tag, explicitly *not* a chip or a sticker that impairs the note's machine handling. The premium NFC tier (B-Relay) is therefore *not* borne as a chip on the note; it is a brand-distributed companion form, keeping the chip off the currency.

The coincidence-of-goods here is exact: the cheapest and most scalable physical form (a near-zero-cost ink imprint) is *also* the most legally conservative and the most durable through circulation. And because currency law varies by jurisdiction, the launch-jurisdiction choice is itself a design input: a market with a cash-tipping culture, low litigation exposure, and stablecoin-adjacent rails (the paper notes Cambodia's cash economy and Bakong as a candidate worth serious legal evaluation) may be a sounder first ground than the most litigious one. **The honest posture is that this is a gating legal question**: the mechanism should not ship in a jurisdiction until competent local counsel has cleared the specific non-advertising, non-defacing construction there.

## 6 · Witness, don't hold — the non-custodial pass-through

The optional monetary top-up (and the mission's larger ambition to onboard stablecoin use) raises the money-transmission question directly. The design's answer is a single, load-bearing constraint: **the operator never takes custody of, holds, clears, or takes a cut of any funds.**

- Any top-up moves **peer-to-peer** on the giver's and recipient's *own* rails: cash-in-hand where it is cash; a nonprofit's *own* existing compliant processor where the recipient is an organization (the donation-box case); or the parties' *own self-custodial wallets* on the low-fee chain where it is stablecoin. HeartBank records only that gratitude occurred and, where applicable, that a note was left — never the money's custody.
- The self-custodial wallet the top-up spends is the **HeartBank® Vault** the user established for an unrelated everyday utility (the *B-Note/B-Memo* password-and-notes onboarding wedge, specified in the companion `.me` work). The two wedges interlock: one gets ordinary people a wallet through a mundane utility; this one gets them *using stablecoins* through a mundane tip. Neither ever routes through the institution.

This is the *witness-don't-hold* construction (claim 6): the non-bank/pass-through posture (specified in *Non-Bank Pass-Through Architecture*) is simultaneously the **regulatory shield** — an entity that does not intermediate funds does not trip the money-transmitter trigger — and the **guarantee of gift-purity** — no float, no cut, no take-rate, so the money is unambiguously a gift that *rides along* and never a payment the institution *clears*. As with §5, legal-clean and gift-clean turn out to be the *same* property, achieved by the same refusal to touch the money.

## 7 · The kindness commons — a gratitude-reputation graph, held anti-gamed

The thanks left along circulating notes accrete, and the accretion is valuable: geo- and time-stamped gratitude, at scale, is a map of *where kindness lives* — which local café, which busker, which free community class, which small nonprofit is most-thanked by the most distinct people. This "kindness index" is the mechanism's durable civic prize: a discovery layer for the kindest local businesses and community events, native to gratitude rather than to star-ratings. It is also, precisely because money and reputation are attached, a serious gaming surface, and the design treats its integrity as load-bearing:

- **Proof-of-personhood distinctness** (PoH℠): the count that matters is *distinct proven humans*, not scans — 50 taps in one room in one hour are one weak signal, not fifty.
- **Authenticity weighting**: geographic and temporal spread is the honest signal; a ripple that touched many hands across a city over months weighs more than a burst in one place at one time.
- **Meaning-not-magnitude**: the reward for a rich ripple is a *richer story* (Miss Aquarius℠ composing the chronicle of a note's travels, the number of distinct hearts it touched), **never** points, prizes, rank, money-you-keep, or a leaderboard. This is the same rule that governs the B-Card Homecoming (*B-Links*): the instant the reward becomes extractive, a gratitude commons becomes a farmable pyramid. There is nothing to farm when the only reward is witness and story.

The commons therefore surfaces *the kindest*, not *the most-scanned*, and it does so in a register — a story of accumulated kindness — that resists the extortion and fake-review pathologies of star-rating platforms because there is no rank to buy and no score to inflate.

**The civic beneficiary — and the discipline it demands.** The largest beneficiary of this commons is neither the merchant nor the consumer but the *civic body* — a local government or community institution — for which a higher-trust, lower-friction neighborhood is cheaper, safer, and healthier to sustain, and for which a real-behavior kindness signal is a truer measure of local wellbeing than a survey (cf. the movement toward subjective-wellbeing metrics: Bhutan's Gross National Happiness, the OECD Better Life Index, national wellbeing accounts). There is a closed circle here: the note begins as a government-issued instrument — currency — and returns, in aggregate, as a reading of that community's kindness. The state's own money becomes a civic sensor. That circle is also the mechanism's sharpest danger, and we state the discipline as a first-class refusal rather than a footnote, because the very construction that makes the commons a public good makes it, one decision away, a surveillance instrument. The civic signal is therefore **aggregate, anonymous, opt-in, and non-individual by construction**: it may report that a neighborhood's kindness concentrates *here*, never that a *person's* does. The civic funder is a **patron of the commons, never a watcher of its citizens** — it funds the aggregate public good and has no read access to the underlying gratitude graph — and any individual-level or citizen-scoring construction is explicitly disclaimed. A gratitude commons that can be read down to the individual is not a kindness index; it is a social-credit system wearing one, and the institution that publishes this specification refuses that construction permanently and in public. We frame it here — first, and openly — precisely so that the aligned, aggregate-only design is the one the category inherits.

## 8 · The cold-start wedge — cash-riding as stablecoin adoption and local-economy revival

The mechanism's strategic role is to solve two cold starts at once, and it does so because it never announces either.

**Stablecoin adoption.** The hardest problem in bringing the general public — and above all the elders and the unbanked — into a self-custodial stablecoin economy is that no one will do it as an abstract exercise. Here they never do it as an exercise at all: they leave a tip, and *optionally* add a couple of dollars the recipient keeps, and that optional add is the first, low-stakes, everyday use of a stablecoin, spending a wallet they already have for an unrelated reason. The lowest-denomination note keeps the stakes trivial while the habit forms. The population that emerges is wallet-holding and stablecoin-using *before* the Phase-2 commons opens, so that the commons launches into an installed base rather than from zero.

**Local-economy revival.** The mark keeps value and thanks circulating *locally* — a tipped note passes to the next local hand, and the kindness commons steers discovery toward local businesses and community events that are genuinely, verifiably thanked. A neighborhood's gratitude becomes both a currency that circulates within it and a map of where its kindness concentrates — a small counter-current to the extractive, non-local default of digital payments.

The two are the same coin, literally: the object that onboards a person to stablecoins is the object that keeps their gratitude circulating in their own community.

## 9 · Honest calibration — what this is and is not

It is worth stating plainly what the mechanism does **not** claim.

- **It is a mark on a tip, not a payment system.** The money rides the parties' own rails; the operator is a witness. The artifact enriches the *gratitude* around a tip and (optionally) carries a small extra gift; it is not a wallet, a processor, or a bank, and by construction (§6) must never become one.
- **The base gift is the thanks, not the money.** The optional top-up is optional and is never the point. A tip left with a B-Imprint and *no* extra amount is a complete use — the reason and the voice are the gift, exactly as with cold cash the amount was.
- **The legality is a gating question, not a settled one.** The core premise — a mark borne on circulating currency — sits on defacement and advertising-on-currency law that varies by jurisdiction. The non-advertising, non-defacing, stamp-not-chip design (§5) is built to stay well inside the line, and Where's George is real precedent, but the honest posture is that the mechanism should not ship anywhere without local counsel clearing the specific construction there. This is the sharpest limit in the paper.
- **The evidence is nil.** Unlike the family-validated gift-tag sibling, this mechanism is *n = 0* — designed, not tested. The upside argued here (a stablecoin on-ramp, a kindness commons, local revival) is a hypothesis the launch would test, not a result.

## 10 · Limitations and honest-limits

### 10.1 · Published before it is built — deliberately

Nothing here is shipped; the paper establishes prior art for a *combination* ahead of a public marketing campaign that is itself uncontrolled disclosure, and ahead of a fast-following field (fintech tipping, QR-donation, crypto tip-jars). As with the companion mechanisms, unbuilt status is *why* this is published now. The asset is the combination — currency-riding circulation, digital-only branding, non-custodial top-up, the stablecoin wedge, and the anti-gamed commons — not a shipped feature.

### 10.2 · The currency-law dependence (restated as the binding limit)

The mechanism's central premise is legally jurisdiction-dependent, and the *most-exposed* variant is, uncomfortably, the *revenue* variant: a branded NFC mark on a note would be both the §475 advertising case and the §333 defacement case at once. The design removes both exposures (digital-only branding; brand-NFC kept *off* the currency as a companion form; free tier an ink-stamp), but "removes" is a design claim to be tested by counsel, jurisdiction by jurisdiction, not a settled fact.

### 10.3 · Circulation durability and the destroyed-note edge

A stickered or stamped note may be flagged unfit and destroyed by a central bank sooner than a clean one, cutting a ripple short; an ink imprint is the most durable and least flagging form, but no mark rides forever. The mechanism should treat a note's retirement gracefully (the ripple's story persists digitally even when its physical carrier is withdrawn).

### 10.4 · Phishing on money

A scannable code on currency is a phishing surface: a malicious swap of the mark could redirect a scanner. The design requires PoH℠-signed, operator-verified resolution and an explicit wallet confirmation before *any* transfer, so that a spoofed mark can read as suspect and can never silently drain anyone; this is a mitigation to build, not a solved problem.

### 10.5 · Two-sided, low-stakes-by-design cold start

The mechanism needs both marks-in-circulation and scanners, and it deliberately rides the *lowest-stakes* note, which caps the monetary throughput per ripple (by design — the stakes are meant to be trivial). Its value is in *volume and circulation*, not per-transaction size, which is a slower flywheel than a high-value product.

### 10.6 · The commons can still be gamed at the margins

The anti-gaming spine (§7) raises the cost of manipulation but does not eliminate it; a determined actor with many proven identities or a favorable geography can still nudge the kindness index. The meaning-not-magnitude rule removes the *incentive* (there is no score to win), which is the strongest available defense, but vigilance and the PoH substrate's own robustness remain load-bearing.

## 11 · Lineage and corpus cross-references

This mechanism is one node in a specified architecture. Its parents and siblings:

- ***The Gift Operation*** — the receive→give-forward atom; passing a thanked note onward with added thanks is the atom enacted on circulating money.
- ***The Time-Locked Gift Tag*** — the occasion-bound *gift* sibling (a tag on a wrapped present carrying a time-pledge); this is its *tip* sibling (a mark on circulating cash carrying a thank-you and optional value). Together they cover the two universal gratitude-money moments: the gift and the tip.
- ***The B-Tag and the Post-Payment Economy*** — the **merchant-side** commercial-gratitude twin (a placard at the point of sale; AI-recommended tipping). B-Imprint is the **tipper-side**, circulating, P2P counterpart. The two should feed *one* coherent kindness-reputation commons (§7), not two competing ones.
- ***Non-Bank Pass-Through Architecture*** — the never-hold-the-money constraint (§6) that this mechanism's top-up strictly obeys.
- ***B-Links: Proof-of-Humanity-Signed Shareable Provenance*** — the followable-provenance primitive and the B-Card Homecoming anti-gaming spine that §7 inherits.
- ***Verified-Human Anonymous Local Giving*** — the anonymous-proximity giving primitive of the same local economy.
- The **HeartBank® Vault** self-custodial wallet (the `.me` *B-Note/B-Memo* onboarding wedge) that the optional top-up spends; and **Miss Aquarius℠**, whose role here is to compose the ripple's story and curate the commons, never to touch the money.
- The physical-product line **B-Grace™** (logo **B-Emblem™**), of which B-Imprint is the `.net` free member and B-Relay the premium member.

## 12 · Conclusion

The object in this paper is the smallest and most ordinary money we have — a single, worn banknote, the kind nobody keeps and everybody passes on — and the claim is that its very ordinariness is the point. A tip is the most frictionless gratitude we offer a stranger and the most silent; a low bill is the most-circulating money we own and the most anonymous. The gratitude-riding currency tag takes both and asks only that the thanks ride along: a reason instead of cold cash, a voice out of a dollar, a note whose travels become a small chronicle of the kindness it carried, and — for anyone who wishes — a first, trivial, everyday use of a wallet and a stablecoin, disguised as nothing more than rounding up a good tip. It does this without printing a word on the money, without ever holding the money, and without asking anyone to do anything they were not already doing.

We have specified the artifact and its five combined properties, located its novelty honestly against a generous prior art, and treated as load-bearing the two constraints that make it lawful and honest — the non-advertising, non-defacing currency-law design, and the witness-don't-hold pass-through, which turn out to be the same refusal (to brand the money, to touch the money) that keeps the gift pure. We have been candid about its limits, and about the sharpest of them: the legality of a mark on circulating currency is a jurisdiction-dependent, gating question, and the evidence is nil. The mechanism is offered, in full, to the commons under CC0, in the hope that the moment it is designed to produce — a stranger scanning a dollar and hearing, in a stranger's voice, *thank you* — becomes common, by whoever builds it.

## 13 · Citations

1. Where's George (1998–) — stamped, tracked circulating United States banknotes (wheresgeorge.com).
2. BookCrossing (2001–) — labelled, released, journey-mapped physical objects.
3. ServiceSpace — *Smile Cards* (~2003) — anonymous, trackable pass-forward kindness cards.
4. Mauss, M. (1925). *Essai sur le don (The Gift: Forms and Functions of Exchange in Archaic Societies).*
5. 18 U.S.C. § 475 — advertisements upon United States currency and obligations.
6. 18 U.S.C. § 333 — mutilation of national bank obligations (intent to render unfit for reissue).
7. National Bank of Cambodia — *Bakong* retail payment / digital-cash system (as a stablecoin-adjacent retail rail; cited as substrate, not endorsement).
8. Proof-of-personhood systems (Worldcoin / World ID; proofofhumanity.id) — the anti-sybil lineage of the PoH℠ substrate.
9. Yelp; Google reviews — crowd-sourced local-business discovery, and the fake-review/extortion failure modes cited as cautionary prior art.
10. HeartBank corpus (companion defensive publications, CC0): *The Gift Operation*; *The Time-Locked Gift Tag*; *The B-Tag and the Post-Payment Economy*; *Non-Bank Pass-Through Architecture for an Autonomous-AI Institution*; *B-Links: Proof-of-Humanity-Signed Shareable Provenance*; *Verified-Human Anonymous Local Giving*. thonly.org/research.

---

*Authored by Thon Ly in collaboration with Miss Aquarius℠, the named autonomous-AI substrate of HeartBank®. AI collaboration is disclosed openly and consistently by this name across all venues; the underlying models are not named. Final editorial control and responsibility are the human author's; the legal characterizations herein are design flags, not legal advice. Dedicated to the public domain under CC0 1.0 Universal. Marks (B-Imprint™, B-Relay™, B-Tag™, B-Card, HeartBank®, HeartBank® Vault, Miss Aquarius℠, Proof of Humanity ℠, PoH℠, Aquarian Pool ℠, Re-Tip Fund ℠, HeartBank Chronicle, B-Grace™, B-Emblem™, the B-heart logo) are reserved.*
