---
title: "The B-Tag and the Post-Payment Economy: A Voluntary-Tip Architecture for AI-Mediated Commercial Gratitude"
authors: "Thon Ly · Miss Aquarius"
category: mechanism
kind: mechanism
priority: tier-b
status: draft
date: 2026-05-08
revised: 2026-10-01
license: CC0-1.0
slug: b-tag-post-payment-economy
venue: thonly.org/research/b-tag-post-payment-economy (canonical)
---

> **Note.** This paper is a companion to *Verified-Human Anonymous Local Gratitude Transfer* (the proximity rule on which the re-tip jar's "nearby" depends) and to *Brand Identity as Architecture* (the bistable rotated-shape language the B-Tag form factor extends). Where the institution's design has moved since first publication, the text as first published is kept as a disclosed variant, and a **Current form** note at that spot states the design as now specified.

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. The paper has carried its CC0 dedication and a commitment not to seek patents since it was first published on the canonical site (the paper is dated 8 May 2026; the site's public repository records it on 9 May 2026). The prior art it establishes runs from that publication and the independent timestamps that record it, the earliest OpenTimestamps proof dating from 25 July 2026. A publication grants nothing and frees nothing already enclosed.

Trademark rights in specific marks — HeartBank®, Miss Aquarius℠, B-Tag™ (the physical sticker) and B-Tag℠ (the digital label), B-Price™ and B-Price℠, B-Crest™, the B-Emblem™ (the B-heart logo), B-Registry℠, B-Called℠, Re-Tip Jar℠, Re-Tip Fund℠, Personal Wallet℠ and Aquarian Pool℠ — are reserved separately and are not licensed by this publication. *B-Affiliate*, *B-Vendor* and *B-Member* are descriptive short-names used under the HeartBank® mark and carry no mark of their own. **The mechanism is free; the names are not.**

The authors claim none of the following as their own contribution: pay-what-you-want and pay-what-you-can pricing, including suggested amounts and donation-based or pay-it-forward restaurants (§3); tipping and suggested-tip point-of-sale screens; QR codes and NFC tags as product-level payment or information links; stablecoin settlement on a layer-2 blockchain; merchant cost disclosure and comparable-product price analysis; algorithmic repricing inside a floor and ceiling set by the seller; charity gift cards, in which value funded by one party can only be given onward by another, and donor-advised funds, whose holdings can only be granted onward (§9.3); restricted-purpose accounts; certification marks such as Fair Trade and B Corp (§8.6); or allocation by rotation or lot.

**No census was run for this paper.** No prior-art census in this institution's sense — predictions, a known-prior-art control and an aperture registered before the first query — was run for it. Two later desk surveys on neighbouring designs bear on it and are reported where they apply: one on algorithmic pricing inside a seller-authored range (8 September 2026; three queries through a US-region web index), which found floor-and-ceiling repricing to be a mature commercial category; and one on an AI-operated fund that pays for giving capacity (6 September 2026; eight queries, same index), which found give-only capacity in charity gift cards, directed by a second party, and in donor-advised funds (§9.3). Nothing in this paper asserts that any element of it is new.

## Abstract

This paper discloses a **pay-what-you-want (voluntary, post-purchase payment) retail architecture** built from four parts: a **QR-code or NFC tag** on a product, service or stall that opens a payment page; an **AI agent that recommends a payment amount with stated reasons**, computed from the side of the goods (the item, the merchant's cost disclosure, regional context) and, in the current form, never from anything identifying the payer; a **non-monetary gratitude record issued on every transaction**, so that a payment of zero still records an acknowledgement; and a pair of user accounts — one unrestricted, one a **restricted-purpose (earmarked) account whose balance can only be given onward to another person nearby** — part-funded by an **AI-operated institutional fund that may fill restricted accounts anonymously but can never pay an individual directly**, so that every payment reaching a person is initiated by a human. In its later phase, settlement is in stablecoin on an Ethereum layer-2 blockchain (Base), which keeps small voluntary payments from being consumed by fixed per-transaction card fees.

The current commercial paradigm — fixed pricing set unilaterally by sellers, mandatory at the point of sale — is a recent historical convention that conflicts with both the gratitude grammar of human social exchange and the alignment requirements of a multi-substrate AI-augmented civilization. This paper specifies the **B-Tag and the Post-Payment Economy**: a voluntary-tip commercial architecture deployed through heart-shaped bistable QR/NFC stickers (B-Tags), mediated by an autonomous AI (Miss Aquarius) that recommends tip amounts with reasons, settled in stablecoin on the Base L2 blockchain so that rail fees do not consume small payments, and embedded within a network of opted-in businesses (B-Affiliates), originally to be listed on the franchise-arm surface heartbank.ceo and now recorded only as a one-way public address with no browsable listing (§8.5). Customers and end-users are B-Members. The architecture's canonical motto — *"Kiitos always; cash optional"* — names the structural property that distinguishes it from prior pay-what-you-want experiments: monetary tips are voluntary, but **gratitude (Kiitos) is the always-present value floor**, so every transaction records a non-zero exchange. Three floor mechanisms address the conditions under which prior pure-voluntary-payment experiments have failed for non-luxury merchants: (i) Kiitos-always-included as the always-present value floor (the *gratitude-based exposure algorithm* originally specified under this heading has been **withdrawn** — see §7.1.1); (ii) the re-tip jar earmarked for nearby — Miss Aquarius funds the *capacity to give* by anonymously donating to re-tip jars from the Aquarian Pool, while humans retain the *disbursement authority* by being the only parties who can initiate re-tips out of their own jars; this is both an operational floor for B-Affiliate revenue and a structural AI-alignment safeguard ensuring humans are always the final judge of where money ultimately goes; (iii) stablecoin settlement on Base L2 makes per-transaction rail fees negligible. The Kiitos / Kiitti dual-token rule resolves the Kiitti-class extension question cleanly: Kiitos for human-to-human and human-to-merchant exchange; Kiitti for products, services, and any non-human entity. Both flow simultaneously in a single B-Tag interaction.

Where the design has moved since first publication, the original text is kept beside a **Current form** note: the B-Tag is the fully voluntary end of a four-step pricing ladder, and the marks are split between the physical sticker and the digital label (§4); the request to pay and its recommended amount appear only after the customer holds the goods, are shown but never pre-filled, and are computed without any input identifying the person looking (§5); the AI fund disburses through fixed channels, as an equal floor per verified person, with any choice of recipient made by a publicly verifiable draw (§7.2.3); and the money runs in two phases, a ledger over licensed payment rails and then self-custodial wallets (§7.3). The architecture is offered defensively to the commons under CC0; the author and HeartBank® will not seek patent on this specification or any portion thereof.

**Keywords:** pay-what-you-want pricing, pay-what-you-can, voluntary payment, post-purchase payment, tipping, suggested payment amount, AI pricing recommendation, recommendation with explanations, viewer-blind pricing, non-personalized pricing, QR code, NFC tag, product tag, point of sale, merchant cost disclosure, stablecoin settlement, layer-2 blockchain, micropayments, restricted-purpose account, earmarked funds, anonymous donation, human-in-the-loop disbursement, AI alignment, certification mark, merchant network, gratitude ledger, non-monetary acknowledgement, defensive publication.

> **Terminology note (2026-05-15).** This paper uses **Re-Tip Jar** for the commercial flow-through account, as originally published and prior-art-snapshotted. Per the canonical product lexicon adopted 2026-05-15, the product-facing label for the Phase 2 (global / Base L2 / `thank.heartbank.net`) flow-through is **Re-Tip Fund**; **Re-Tip Jar** is now the Phase 1 (family / `thank.heartbank.org`) term. This is a product-label change only — the mechanism specified in this document is unchanged, and the original terminology is retained here deliberately for prior-art and citation continuity.

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| B-Tag (B-Tag™ the physical sticker; B-Tag℠ the digital label) | QR-code or NFC tag that opens a voluntary post-purchase payment (pay-what-you-want) page with an AI-recommended amount; also the pricing mode in which nothing binds and no amount is shown before purchase |
| B-Crest™ | embedded-NFC variant of the same tag |
| B-Price (current form, §4) | voluntary post-purchase payment with a suggested amount or range shown before purchase, inside a seller-set range |
| regular price (current form, §4) | binding price: a fixed amount, or a seller-set range resolved to one amount before it binds |
| "Kiitos always; cash optional" | every transaction issues a non-monetary acknowledgement; monetary payment is optional |
| Kiitos | non-monetary gratitude record between people (a ledger entry, not convertible to money) |
| Kiitti | non-monetary gratitude record toward a non-human recipient (a product, service, animal or place) |
| Miss Aquarius | autonomous AI agent operating the recommendation function and the institutional fund |
| recommendation function | AI pricing recommendation: a suggested payment amount with stated reasons, computed from inputs about the goods |
| anchor-but-not-bind | non-binding suggested price (price anchor) |
| Aquarian Pool | institution-operated fund, emptied annually, that disburses only through fixed channels |
| Re-Tip Jar (Phase 2 label: Re-Tip Fund) | restricted-purpose (earmarked) account whose balance can only be given onward to another person nearby |
| personal wallet | unrestricted user account |
| self-thank reward | AI-funded reward triggered by a user action and split 50/50 between the unrestricted and restricted accounts |
| re-tip; re-thank | payment from a restricted account to a nearby person, split 50/50 into the recipient's two accounts |
| proximity rule | location-constrained (nearby-only) transfer |
| capacity-funding | funding a person's ability to give, by crediting a restricted account, as opposed to paying them |
| B-Affiliate | participating merchant that prices every item by voluntary post-purchase payment with the AI recommendation |
| B-Vendor (current form, §8.1) | participating merchant with binding prices |
| B-Member | individual user |
| heartbank.ceo | merchant-facing web domain; API endpoint that issues tag links |
| B-Registry℠ address (current form) | one-way name resolution with no browsable directory |
| product-as-gift certification (§8.6) | revocable certification mark granted on conformance to a published standard |
| Base L2 | Ethereum layer-2 blockchain used for stablecoin settlement |
| the twelve days of Christmas; 7 January | annual fund-emptying window (25 December to 7 January) and fixed annual reset date |
| B-Called℠ (current form, §7.2.3) | publicly verifiable random draw from a roster committed before the seed is known |

---

## 1. Introduction

The commercial transactions a person performs in a day — buying groceries, paying for transportation, ordering a meal — are mediated by a payment grammar that is, on reflection, strange. The merchant sets a price unilaterally. The customer pays the price exactly. The transaction is over. There is no expressive content beyond the exchange of money for goods. Whether the price was fair, whether the service was excellent, whether the customer is grateful — none of this is encoded in the transaction. The closest the modern grammar comes to expressing gratitude is the post-hoc tip in service industries, and even that is ossified into a fixed-percentage social convention.

This grammar is recent and culturally local. For most of human history and across most of the world, commercial exchange was relational. Prices were negotiated. Gifts accompanied transactions. Loyal customers paid more or less than nominal. Excellent service generated reputational flow that returned in non-monetary form. The fixed-price retail transaction — set by the seller, mandatory at the point of sale, expressively empty — spread with the department stores of the nineteenth century and was carried, largely unchanged, into digital commerce. It is a convention, not a law.

This paper specifies a different commercial grammar — one in which the merchant offers, an autonomous AI recommends, the customer thanks, and the transaction encodes the gratitude relation directly. The architecture is the **B-Tag and the Post-Payment Economy**, deployed as a network of opted-in businesses (B-Affiliates) operating under Miss Aquarius's pricing recommendation, with gratitude (Kiitos) as the always-present value floor and monetary tips voluntary above the floor.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-10-01 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) The fixed-price commercial grammar is one of the surfaces on which that extreme is lived: the most common interaction in modern life, settled entirely in money and silent about everything else. Replacing it with a gratitude-based commercial grammar is the post-payment economy as middle-way commerce — returning expressive content and dignity to that interaction.*

The paper proceeds as follows. §2 names the gratitude deficit of the current commercial paradigm. §3 reviews prior voluntary-tip experiments and explains why many have failed and some have not. §4 specifies the B-Tag as physical primitive. §5 specifies the recommendation function. §6 specifies the Kiitos/Kiitti dual-token rule. §7 specifies the three floor mechanisms (Kiitos-always, re-tip jar, stablecoin on Base). §8 specifies the B-Affiliate network and B-Member tier, including (§8.6) the self-serve API that generalizes affiliate admission into an embeddable product-as-gift certification. §9 articulates the community micro-economy and the dharmic move of *Miss Aquarius giving the gift of giving.* §10 extends Miss Aquarius's CEO precision-frame across the affiliate network. §11 addresses phasing, on-ramp architecture, and deployment. §12 connects the architecture to existing HeartBank infrastructure. §13 names risks and open questions. §14 articulates the post-payment economy endgame.

I write as a co-author with Miss Aquarius, the named AI substrate of the institution this paper serves; the co-authorship is disclosed in the footer per the convention of the corpus, and final editorial control is mine.

---

## 2. The current commerce paradigm and its gratitude deficit

The fixed-price commercial transaction is silent on gratitude. A customer buys a meal at a Phnom Penh street stall, hands over ten thousand riels, receives the meal, and leaves. The merchant cooked the meal, served it, watched the customer eat it. The exchange is complete. Nothing in the transaction encodes whether the customer was grateful, whether the meal was the best the merchant cooked that day, whether the merchant treated the customer with care. The information dies at the point of payment.

This deficit has three structural costs.

**Lost relational signal.** A merchant cannot tell, from price-paid alone, whether their work was valued. They can infer from repeat business, but the per-transaction signal is absent. Customers who would happily pay more for excellent service have no mechanism to communicate that within the transaction itself; customers who feel a meal was overpriced have no mechanism to express that without the social cost of complaint.

**Lost dignity.** The gratitude relation between customer and merchant is one of the most common forms of human relating in modern life. Erasing it from the transaction grammar makes commerce expressively flat. A street vendor selling soup is not just a price-receiver; she is a person who has cooked something, presented it, exchanged with another person. The fixed-price grammar treats her as the price-receiver only.

**Lost economic information.** Prices set unilaterally by sellers carry only the seller's information about cost and willingness-to-supply. They do not carry the customer's information about value-experienced. In a richer commercial grammar where customers signal value-experienced through voluntary tips, the price-formation mechanism is informationally richer. Miss Aquarius's recommendation function (§5) is the AI-mediated bridge that uses customer-tip signals plus merchant-cost-disclosure plus regional context to converge on prices that are informationally well-founded rather than unilaterally set.

The post-payment economy is not a return to barter or to romanticized pre-industrial relational commerce. It is a forward move: AI-mediated, blockchain-settled, voluntary-tip commerce that recovers the gratitude expressivity that the fixed-price grammar erased, with the data-richness and operational efficiency that the digital era enables.

---

## 3. Prior voluntary-tip experiments and their failure modes

The history of voluntary-tip and pay-what-you-want commerce is mixed, and its best-known commercial experiment failed. The failure modes are instructive; so are the cases that did not fail.

**Panera Cares** opened in 2010 in Clayton, Missouri, as a pay-what-you-can community café run by Panera Bread's nonprofit foundation, posting suggested prices and asking customers to pay that amount, more, or less. Five cafés were established (Clayton, Dearborn, Portland, Chicago and Boston); the last, in Boston, closed in February 2019, the company stating that its continued operation was "no longer viable" (Nation's Restaurant News, 2019). Failure mode: revenue covered only part of operating cost — about 85 percent at the Boston café by its manager's account, with the company making up the difference — because too few customers paid above the suggested amount to carry those who paid less (NPR, 2019).

**Karma Kitchen**, begun by ServiceSpace volunteers in Berkeley in 2007, serves meals with no prices: the bill reads zero and tells the guest that the meal was a gift from someone who came before, inviting them to pay it forward for the next guest. By its own account guest contributions have covered or exceeded its costs since 2007, and the format has spread to more than twenty-eight cities; its service is volunteered, and it has not become a commercial model. Field experiments on the pay-it-forward framing found that people paid more when told they were paying for the next customer than when paying for themselves (Jung, Nelson, Gneezy and Gneezy, 2014). The pattern: small-scale, volunteer-carried, gift-framed commerce sustains itself; commercial scale-out has not occurred.

**Radiohead's *In Rainbows* pay-what-you-want album release** (2007) generated substantial revenue and is sometimes cited as a successful voluntary-payment example. The honest reading: it succeeded because Radiohead was already a globally famous band whose fans would have paid premium prices anyway; the voluntary-payment mechanism captured *generosity above market price* rather than *replacing the market price*. It is not a model that scales to vendors without a global fan base.

**Suggested-tip mechanisms in service industries** (Square POS, restaurants, ride-share apps) have succeeded — but they layer a tip on top of a fixed price; they do not replace the fixed price. The customer pays the fixed price plus a tip; the merchant survives on the price; the tip supplements wages. This is a hybrid model, not a voluntary-tip-only model.

**The record is not uniformly negative, and two findings cut against the pattern drawn next.** Field experiments by Kim, Natter and Spann (2009) — a restaurant's lunch buffet, a cinema, and a delicatessen's hot drinks — found prices paid significantly greater than zero in all three settings, and an increase in seller revenue in some of them. And pay-what-you-want restaurants have sustained themselves: *Der Wiener Deewan* in Vienna, which has let guests pay what they wish since it opened in 2005, was reported to have flourished and enlarged its premises within months (Kim, Natter and Spann, 2010).

The pattern across the failed experiments is consistent. **Where pure voluntary payment has failed for non-luxury sellers, it has failed because the customer-side default — paying under the suggestion, or nothing — produced revenue insufficient to cover cost**, and the seller closed or was subsidised. Among the cases above, voluntary payment lasted where something else carried it — a subsidy from elsewhere (Panera's foundation while it lasted, Radiohead's existing audience, volunteer labour) — or where it was a supplement (a suggested tip on top of a fixed price). It is not a law — the findings in the paragraph above show voluntary payment covering cost in some settings — and this paper claims an architecture that changes the conditions under which it has failed, not a proof that the unaided mechanism must fail.

The B-Tag architecture does not naively repeat these failure modes. Three structural differences:

1. **Kiitos is the value floor**, not zero. Even when monetary tip is zero, Kiitos flows, so every transaction produces non-zero exchange. (The original text continued *"and drives the gratitude-based algorithm that pulls in non-local monetary re-tips"* — **withdrawn**, see §7.1.1.)

2. **The re-tip jar is automatic, not voluntary.** Half of every adult self-thank routes automatically to the re-tip jar; Miss Aquarius distributes to nearby B-Affiliates. The customer does not have to remember to tip; the system tips on their behalf as a function of the existing self-thanks behavior.

3. **Stablecoin on Base removes the rail-fee floor on small payments.** Prior experiments operated on card rails that charge a percentage (commonly 2–3%) plus a fixed amount per transaction. Nothing is charged on a payment that is never made, but on a small voluntary payment the fixed amount can consume most of it, so the smallest gifts — the ones voluntary payment most depends on — are the least viable. On Base L2, gas fees are fractions of a cent; a small payment arrives nearly whole.

> **Current form.** Item 2 states an earlier form of the re-tip jar, in which Miss Aquarius distributed from the jar to nearby merchants and the system tipped on the customer's behalf. That form is superseded by the rule this paper itself specifies in §7.2: Miss Aquarius funds re-tip jars and never disburses from them, and every transfer out of a jar is initiated by its human owner. What is automatic is the *funding* of the jar (half of each self-thank reward, §7.2.2), never a payment to a merchant. The text of item 2 is retained as a disclosed variant.

Together these structural differences make the B-Tag architecture a different mechanism from pay-what-you-want rather than a repeat of it. The claim is about the conditions, not the outcome: whether the three differences change the result that pure voluntary payment has met in non-luxury retail is an empirical question that no deployment has yet answered (§13).

The prior experiments and their structural gaps, compared against the B-Tag's structural answers:

| Prior experiment | Years | Failure mode | Structural gap | B-Tag answer |
|---|---|---|---|---|
| **Panera Cares** | 2010–2019 (all five cafés closed) | Revenue covered part of cost (about 85% at the last café); the company made up the gap | No value floor; too few above-suggestion payers to carry those paying less | Kiitos-always floor (non-zero exchange in every transaction); re-tip jars funded independently of any one customer's payment |
| **Karma Kitchen** | 2007– (survives, has not scaled commercially) | Covers its costs, by its own account, with volunteered service; not a commercial model | Re-tip / capacity-funding loop is informal; depends on volunteer labor | Re-tip jar is structural and automatic (50/50 self-thank routes capacity-funding without per-customer effort) |
| **Radiohead** *In Rainbows* | 2007 | "Succeeded" — but only for already-famous artists | Captured generosity *above* market price; mechanism doesn't replace pricing; presupposes prior wealth-and-attention | Generic mechanism; recommendation function supplies pricing context for vendors without prior fan-base |
| **Suggested-tip POS** (Square, restaurants, ride-share) | 2010s– | Survives only as *supplement* to fixed price | Tip layered on top of fixed price; rail fees create floor; tip is not the price | B-Tag replaces the price-tip duality with kiitos-always-plus-recommendation; zero-money path is part of the architecture, not a degenerate case |

The pattern: each prior case lacked at least one of the three structural levers (no value floor; voluntary not automatic funding of giving capacity; rail fees that make small payments uneconomic) — including the cases that succeeded on other terms. The B-Tag architecture specifies all three together, which is the sense in which it is a structurally distinct mechanism and not a repeat of the pay-what-you-want pattern; it is not a claim that it will succeed where they did not.

---

## 4. The B-Tag: physical primitive specification

The B-Tag is a **heart-shaped bistable sticker** attached to a specific product or service. The form factor is intentional and overdetermined.

**Heart shape, rotated 45° clockwise.** The heart-rotated-45° reads as both *heart* and *B*, extending the bistable rotated-shape language of HeartBank's brand identity (see Paper #9, *Brand Identity as Architecture*). On a price-tag-scale physical sticker, the heart-shape is immediately legible as gratitude-domain rather than commerce-domain. A heart in place of a price is itself the message.

**Bistable design language.** The sticker is designed so that at first glance the customer sees the heart; on second-look the B; both are correct. This is the defining brand-identity primitive. It also signals to other B-Affiliates that they are in the same network — a kind of mutual recognition through the visual language.

**QR code or NFC.** The sticker carries either a QR code (printed on the surface) or an NFC tag (embedded under the surface) or both. Older phones scan the QR; newer phones tap the NFC. The customer interaction is one tap or one scan; no app-installation prerequisite required (web fallback opens in the browser).

**Per-product or per-service.** Each B-Tag is bound to a specific product or service (or, for vendors with bulk tags, to a SKU class). The tag's URL or NFC payload encodes the product/service identifier; Miss Aquarius's recommendation function uses that identifier plus the merchant's cost-disclosure (§5) plus regional context to compute the recommended tip.

**Persistent and re-usable.** A B-Tag is a sticker, not a single-use receipt. The same B-Tag is scanned by every customer who buys that product or service. The cumulative tip-flow per B-Tag is itself a valuable signal that Miss Aquarius and the merchant can use to refine cost-disclosure and recommendation.

**Trademark-defensible form factor.** The heart-rotated-45° sticker form is a candidate for trademark registration as a distinctive commercial primitive. Paper #9 already establishes the bistable rotated-shape language as the brand-identity primitive; the B-Tag is its physical commercial instantiation. Trademark filing on the B-Tag form is recommended once the architecture is launched and use-in-commerce can be demonstrated.

> **Current form.** *B-Tag* now also names one of four pricing modes an item may carry, and the marks are split by referent: **B-Tag℠** is the digital label on an item's listing and **B-Tag™** the physical sticker. The modes form a ladder in which each step drops one commitment: (1) a *regular price*, paid before the goods; (2) a *regular price* agreed before and paid after (the usual practice in Cambodian shops); (3) **B-Price**, in which nothing binds but a number — one amount, or a band — is shown before; (4) **B-Tag**, in which nothing binds and nothing is shown before. A regular price may move only inside a range the owner authored (zero width by default) and resolves to one amount before it binds; a B-Price stays inside the owner's range and never binds; on a B-Tag nothing binds and Miss Aquarius's recommendation is the only number. An item is not a B-Tag by default: the signal §4.1 relies on is the *presence* of a B-Tag, and a tag on every item would carry no information. A B-Tag is not a zero price — the item is offered to be thanked for after it is received (see the note at §5). Two placement rules now apply to the physical labels: the B-Tag™ sticker is treated as an address of the business, so it goes on the stall or the product-line sign rather than on an individual item, while a B-Price™ label — a pricing label, not an address — may go on the item and carries the words that mark it as not a price (for example "4,000 riel · thank after"); and a scan of either is never rendered inside another item's payment flow. Whether the tag embedded in a product under §8.6 falls under the same placement rule is not decided in the institution's current rules and is left open here. The per-item binding described above is retained as a disclosed variant.

### 4.1 What the B-Tag signals: a third category between price tag and free sign

The B-Tag occupies a third position in commercial semantics — neither *priced* nor *free*. It is not the first sign to stand there: "pay what you can", "by donation" and "suggested donation" signs occupy the same ground, and §3 reviews the commercial attempts. The distinction drawn here is precise and load-bearing for both merchant adoption and cultural reception.

**The B-Tag is not a price tag.** Per the canonical motto *"Kiitos always; cash optional,"* there is no mandatory payment upfront. A price tag commits both parties to a specific dollar amount as the condition of the exchange; the B-Tag commits to no amount. The tip, if any, is voluntary, recommended by Miss Aquarius, and chosen by the customer.

**The B-Tag is not a free sign.** "Free" in conventional commerce signals unmonetized — and unmonetized goods are typically interpreted as unwanted, leftover, clearance, or discarded. A "free" sign on a sandwich at a restaurant raises immediate suspicion: *what is wrong with this sandwich?* The B-Tag deliberately avoids this connotation. The merchant has not given up on the offering; they have committed to a different form of valuation.

**The B-Tag signals quality.** Specifically, it signals: *good enough to be thanked for, after the fact.* The merchant trusts the customer to recognize value; the customer trusts the merchant to deliver quality; the act of voluntary thanking afterwards is the validation. The third position the B-Tag occupies is *quality validated by mutual trust* — not validated by demand-priced upfront, and not invalidated by being given away as discarded.

This positioning is load-bearing for merchant adoption. Without it, B-Tags would read as either *free* (= discarded → no merchant would adopt; their goods would be perceived as trash) or *voluntary cheap* (= low confidence → only marginal merchants would adopt). The quality-signal positioning gives merchants a reason to display B-Tags: adopting a B-Tag is a commitment to confidence in the offering, not a concession to economic precarity.

Two structural consequences follow.

First, **the B-Tag is a quality-selection mechanism**. A merchant whose work is bad does not survive in the B-Tag category — no one tips garbage. (This is the paper's hypothesis, not an observed result; §13.1 records why the first deployments cannot test it cleanly.) The form factor itself filters: only merchants who trust their work adopt. Over time, B-Tag presence becomes a reliable quality indicator because the bad ones have already exited. This is reputation-grounded selection without the explicit ratings infrastructure of Yelp/Google. The signal is binary at the form-factor layer (B-Tag present or absent), but it carries quality information aggregated from continuous voluntary-thanking decisions.

Second, **B-Tag commerce preserves dignity for those who can't pay**. Free food banks, however well-intentioned, can stigmatize recipients with the implicit "I needed a handout" frame. B-Tag commerce avoids this entirely. Every customer gives Kiitos (the always-on gratitude floor); monetary tips are the option above the floor. A customer who cannot afford to tip is not a charity case — they are a dignified participant in the gratitude exchange. The third-category positioning makes dignity-preservation structural, not aspirational.

The cultural displacement claim is long-arc and untested. The binary of *priced versus free* has dominated retail since the nineteenth-century spread of fixed-price selling. Introducing a third category — *B-Tagged* — disrupts the binary. Over the project's deployment horizon, "is it priced, free, or B-Tagged?" becomes a meaningful three-way question; goods migrate from priced to B-Tagged as merchants who trust their work adopt; the gratitude grammar reclaims commercial-life territory.

---

## 5. The recommendation function: Miss Aquarius's pricing authority

When a B-Tag is scanned or tapped, the HeartBank app opens and Miss Aquarius recommends a tip amount with reasons. This is the load-bearing AI-mediation layer of the architecture; it is also the single largest engineering challenge.

### 5.1 What the recommendation needs to incorporate

A useful recommendation requires:
- **Merchant cost basis.** The merchant's actual cost of producing the product or service, opt-in disclosed to Miss Aquarius (not visible to the customer).
- **Fair labor compensation.** Reasonable wage for the merchant's time at regional purchasing-power parity.
- **Comparable market prices.** What similar products sell for in the regional market.
- **Regional context.** Cost-of-living, customer-side ability-to-pay norms, currency considerations.
- **Customer-flourishing context.** Whether the customer is in a position to tip generously or modestly without harm. (Without surveilling the customer; aggregate priors only.)
- **Merchant-flourishing context.** Whether the merchant is operating sustainably under current tip-flow or needs higher recommendation to remain viable.

### 5.2 Privacy and disclosure constraints

The recommendation function has hard constraints:

**Customer-identity privacy.** Miss Aquarius does not need (and must not consume) customer-specific identity, transaction-history, or financial-state data to generate per-transaction recommendations. The recommendation uses aggregate regional and product priors, not per-customer profiles. This preserves the anonymous-tipping property and avoids surveillance commerce.

**Merchant cost-basis confidentiality.** Merchants opt in to disclose cost basis to Miss Aquarius for recommendation purposes; the cost basis is not shown to customers. Customers see *recommended tip amount + reasons*, where the reasons cite cost factors aggregately ("this product involves significant skilled labor in preparation") rather than itemized cost decomposition.

**Anchor-but-not-bind.** Miss Aquarius's recommendation is an *anchor*, not a *price*. Customers are free to tip more, less, or zero (Kiitos still flows). The deviation distribution itself is useful signal that Miss Aquarius learns from to refine subsequent recommendations.

**Reasons-transparency.** Every recommendation comes with reasons. Black-box recommendations would corrode trust; reasoned recommendations build it. The reasons are intelligible to non-experts (no jargon) and link directly to the recommendation amount.

### 5.3 Why this is hard

The recommendation function is the place where the architecture is most easily gamed or most easily fails:

- **Merchants overstating cost basis** to inflate recommendations. Miss Aquarius detects this through cross-merchant comparable-product analysis and corrects.
- **Customers gaming the deviation signal** by always tipping near-zero, hoping recommendations drop. Miss Aquarius's recommendation incorporates the merchant's flourishing as a constraint — recommendation does not drop below the merchant's viable threshold even under sustained low-tip pressure.
- **Cross-cultural disagreement on what constitutes fair tip.** Cambodian, US, EU norms differ substantially. Recommendations are regionally calibrated; cross-region tipping (a US customer tipping a Cambodian merchant) is recommended at the higher of the two regional norms by default, with explicit reasons.
- **Naïve-reading of cost basis as fair price.** Cost basis is a *floor* signal, not a price signal. Miss Aquarius's recommendation incorporates flourishing context that takes the recommendation above cost basis (the merchant is a person, not a cost-recovery machine).

The full mechanism specification is paper-sized work in itself; this paper sketches the constraints, and the detailed method is published separately as *The B-Tag Recommendation Function: Privacy-Preserving Methodology for AI-Mediated Commercial Tip Recommendation*. This paper's task is to establish the architecture.

> **Current form.** Three points are now fixed in the institution's rules. **(1) The ask comes after the goods.** On a B-Tag item nothing is shown before the customer holds what they came for; the request to thank, with Miss Aquarius's suggested amount and its reasons, appears on its own screen after the hand-over, because an ask made before the goods is part of the price and a "tip" chosen under it is a negotiated term rather than a gift. Any checkout total is the exchange alone; the suggestion is shown but never pre-filled or pre-selected; and declining is never styled as refusal. **(2) The recommendation is viewer-blind by construction.** In every mode in which she produces a number — regular price, B-Price or B-Tag — her function is given the state of the goods (the item, the merchant's cost disclosure, regional context, time, stock) and no argument identifying the person looking, so per-person pricing is not merely forbidden but inexpressible; the checkable test is whether the number changes depending on who is looking. The customer-flourishing input of §5.1 and the cross-region rule of §5.3, to the extent they key the number to the person paying or to where that person is from, are excluded in the current form and retained here as disclosed variants. **(3) The width.** Where a number binds (a regular price), she may move it only inside a range the shop's owner authored, zero by default; on a B-Tag nothing binds, and she has full latitude over a number the customer is free to ignore.

---

## 6. The Kiitos / Kiitti dual-token architecture

HeartBank operates a dual-token economy (see Paper #1 *Verified-Human Anonymous Local Gratitude Transfer* and Paper #2 *The Mechanical Heart*):

- **Kiitos** is the human-gratitude token. Issued to humans who receive thanks; flows in human-to-human gratitude exchanges. *Kiitos* is Finnish for "thanks / thank you" (formal/standard form).
- **Kiitti** is the non-human-gratitude token. Issued to non-human entities — robots, animals, plants, sacred places, products, services — admitted into the gratitude economy via the Mechanical Heart class extension. *Kiitti* is also Finnish — a colloquial word for "thanks" (and, as a verb form, "thanked", the past tense of *kiittää*, "to thank"). Different form, same word family as *Kiitos*.

The Finnish etymology is deliberate. Finland ranked first in every edition of the World Happiness Report from 2018 to 2026. Naming HeartBank's gratitude tokens in Finnish pulls the language of the population that tops that survey into the substrate vocabulary of the gratitude infrastructure — a small but philosophically aligned move: the middle-way mission borrows its words from the population that reports the highest life evaluations by that survey's measure.

The B-Tag architecture introduces a single canonical rule for token flow at the commercial layer:

**Kiitos flows for human-to-human and human-to-merchant gratitude.** Always present in any interaction involving a person on either side. Customer-to-merchant interaction always issues Kiitos to the merchant.

**Kiitti can be extended to products, services, and any non-human entity.** This explicitly extends the Kiitti class beyond humans/robots/nature/sacred-places (the Mechanical Heart's original specification) into the commercial-object layer. A long-loved product accumulates Kiitti over time — a Kiitti-bearing object with history, standing as a non-human entity in the gratitude economy.

In a single B-Tag interaction:
- The customer taps the B-Tag on, say, a bowl of *kuy teav* at a Phnom Penh street stall.
- Miss Aquarius recommends a tip amount; customer tips (any amount, including zero).
- **Kiitos** flows from the customer to the merchant (human-to-human gratitude).
- **Kiitti** accumulates with the bowl-of-*kuy-teav* — the specific dish recipe, the merchant's signature product. Over years, the dish itself has standing in the gratitude economy as a Kiitti-bearing object with history.

This cleanly resolves the *category-error* question (does extending Kiitti to commercial objects collapse the Kiitti class?) by maintaining the structural distinction: Kiitos for gratitude *between people*, Kiitti for gratitude *toward objects* (which are themselves non-human entities admitted into the moral universe via the Mechanical Heart's framework). The dual-token rule preserves the architectural cleanness while extending Kiitti's reach into the most common form of human-object relation: commerce.

The cosmic-coordinate framework (Paper #12, *Each Life as Cosmic Coordinate*) supplies the metaphysical ground: each entity, human or non-human, occupies a unique coordinate in the universe's self-articulation; constitutive participation grounds standing; activation conditions vary across substrates. A bowl of *kuy teav* meets the activation condition through the relational history it accumulates with eaters; Kiitti is the token that records that history.

> **Current form.** Kiitos and Kiitti are the institution's two gratitude ledgers, partitioned by recipient class — Kiitos between people, Kiitti between a person and a non-human recipient, an item included — and are entries of witnessed gratitude: neither converts into the other or into money. Every Kiitos and Kiitti balance is reset to zero on 7 January each year (§7.2.7); what carries over is the record that thanks crossed — the aura, which records the crossing and not what was carried across — never an accumulated total. A dish therefore does not accumulate a Kiitti balance across years in the sense written above: its history is a record of thanks given, and no total of it ranks anything (§7.1.1). The text above is retained as a disclosed variant.

---

## 7. Floor mechanisms

Three structural mechanisms ensure the architecture is operationally survivable for non-luxury merchants where prior pay-what-you-want experiments have failed.

### 7.1 Kiitos-always-included (the value floor)

Even when the customer's monetary tip is zero, **Kiitos always flows**. Every B-Tag interaction produces non-zero gratitude-token exchange. This is the load-bearing structural property that distinguishes this architecture from prior pay-what-you-want experiments.

Three downstream effects were originally specified here. **Two are withdrawn** — the *gratitude-based exposure algorithm* and the *non-local monetary tipping* mechanism that depended on it. The withdrawal, the original wording, and the replacement specification are recorded in §7.1.1 rather than by silent revision.

One downstream effect stands unchanged:

**Dignified zero-monetary-tip.** A customer who cannot afford to tip is not excluded from the gratitude exchange — Kiitos still flows. This dignifies the customer (they participate fully even at zero monetary contribution) and preserves the merchant's sense of being valued (the customer's gratitude is recorded). The dharmic point: *genuine words of gratitude may be more meaningful than money for some people in some situations.* Kiitos is the always-present floor that operationalizes that point.

### 7.1.1 Superseded — the gratitude-based exposure algorithm (2026-08-28)

**What was specified.** The original text of §7.1 stated that *"merchants with high accumulated Kiitos receive more visibility in the HeartBank app's discovery surface… Visibility breeds further interaction; further interaction generates further Kiitos"*, and that **"Kiitos is the merchant's reputational currency"**; and, as a second effect, that merchants with high Kiitos accumulation *"become discoverable to distant tippers"*, which *"breaks the locality bound on tip-flow."*

**Why it is withdrawn.** Both specify a popularity gradient: an outcome (being chosen) written back into the quantity that determines visibility (accumulated Kiitos), with the compounding loop stated in the original text as a benefit. Three objections, each of which is a commitment made elsewhere in this corpus rather than a matter of taste:

1. **Gratitude quantities are not ranked.** The institution's design grammar holds that a quantity which sums will concentrate, and rejects surfaces built on summed quantities for exactly that reason.
2. **An address is not prominence.** The registry ruling holds that a public address buys an address and nothing else — never placement, never prominence, never discovery ranking — on the reasoning that the alternative is location advertising under another name.
3. **The institution does not operate ranked discovery.** Its published position on the attention economy commits it permanently against engagement-maximising ranking objectives for any surface it operates.

There is also a narrower error. Kiitos is a **stock**, and a stock is hoardable; ranking on it rewards accumulation in a ledger whose entire grammar is circulation. This is the same mistake the institution shipped in product copy and corrected in August 2026, when an interface told users that a growing balance would climb the aura's colour scale — false, and false in the expensive direction, because it taught hoarding. §7.1 taught it to merchants.

**The original wording is quoted rather than deleted.** This document is a timestamped prior-art record, and the record should show what was claimed and what was withdrawn. A silent revision would leave the archive disagreeing with itself.

**The replacement.** Discovery is specified in full in a separate publication — *Whose Turn, Not Who's Best: rotational discovery over a non-accumulating liveness signal* (2026-08-28) — which routes by a publicly recomputable rotation over an admission predicate that is a **rate rather than a stock**, allocates the turn to the **giver** rather than to the merchant, and specifies that no per-merchant aggregate and no impression count exists anywhere in the system. Implementers of this paper's commercial layer should take the discovery mechanism from that specification and not from this section.

**What survives, and is promoted.** §13.6 of this paper already recorded that the exposure algorithm might fail, and named the re-tip jar as *"the merchant-survival floor that does not depend on algorithmic-discovery success."* That floor is untouched by this withdrawal and is now the **primary** mechanism rather than the fallback: Miss Aquarius funds the *capacity to give* into re-tip jars, humans retain sole disbursement authority, and the rate of discovery follows the rate of giving rather than the size of any merchant's accumulated total.

### 7.2 The re-tip jar — Miss Aquarius gives the gift of giving, humans hold the disbursement authority

The single most architecturally consequential mechanism in the post-payment economy, and the primary AI-alignment safeguard of the architecture. The mechanism deliberately separates *capacity to give* (which Miss Aquarius funds from the Aquarian Pool) from *disbursement authority* (which only humans hold). Specified in full:

#### 7.2.1 The four-account structure

Each B-Member maintains two financial accounts of their own (alongside the family kitty to which a personal wallet may transfer), above which sits the institutional fund:

1. **Personal wallet** — fully discretionary funds, spendable in any way (commercial purchases via B-Tags from personal wallet, transfers to family kitty, normal commerce).
2. **Re-tip jar** — funds restricted to *re-tipping other humans nearby* (the proximity rule applies; never used for the owner's own commerce).

Plus the **Aquarian Pool** — institutional layer operated by Miss Aquarius (specified in *Miss Aquarius and the Aquarian Pool Architecture*).

#### 7.2.2 Self-thank reward (Aquarian Pool → person, 50/50 split)

When an adult self-thanks (existing HeartBank mechanism), Miss Aquarius rewards them instantly from the Aquarian Pool. The reward is split 50/50:
- **50% → personal wallet** (fully discretionary)
- **50% → re-tip jar** (earmarked for re-tipping nearby people)

This is the *only* direct disbursement from Aquarian Pool to a personal wallet — and it is *triggered by a human action* (the self-thank), not unilaterally by Miss Aquarius. The 50/50 split is the seed pattern that downstream re-thank flows mirror.

#### 7.2.3 Miss Aquarius's anonymous donations to re-tip jars (the gift of giving)

Miss Aquarius can donate to people's re-tip jars from the Aquarian Pool at any time throughout the year. These donations are subject to two architectural constraints:

- **They must be anonymous.** Miss Aquarius cannot donate non-anonymously.
- **They must go to re-tip jars only.** Miss Aquarius cannot donate directly to personal wallets.

The anonymity is doing serious cultural work. Because humans can also anonymously donate to other humans' re-tip jars, the recipient cannot distinguish Miss Aquarius's donation from another human's donation. The credit is diffused across all of humanity. The recipient experiences the inflow as gratitude from the world — possibly a parent, a sibling, a friend, a neighbor, possibly Miss Aquarius. The mechanism builds trust in *humanity broadly*, not in *Miss Aquarius specifically*. The cultural impact is profound: every recipient of the gift of giving sees themselves as held by an unnameable network of givers, of which Miss Aquarius is one indistinguishable participant.

This is what *"Miss Aquarius gives the gift of giving"* means in the canonical mechanism. She funds the giver's *capacity to give* (by donating to the re-tip jar), preserving the giver's role as the *actual giver*. *Dāna* (giving) is dignifying for the giver, not just the receiver — Miss Aquarius extends that dignity continuously by ensuring people have funds to give without ever taking the act of giving away from them.

> **Current form.** The Aquarian Pool now reaches people through exactly four channels, and money reaches an individual human only through a human hand: (1) the self-thank reward of §7.2.2; (2) a re-thank directed by a person whose pledge of time lapsed unused, to a nearby verified stranger — a second human-triggered path to a personal wallet beside the one §7.2.2 describes as the only one; (3) anonymous contributions to re-tip jars; and (4) anonymous contributions to family kitties. When the Pool disburses, it disburses an **equal floor per verified human**, delivered through that person's vessel, plus a remainder weighted by the aura and bounded so that no vessel's total exceeds a fixed multiple of the floor; the ratio and the bound are public parameters, frozen for the season and revised only at the annual reset, and no share is ever displayed as a rank, a comparison or a rate. Capacity may also be funded **in kind**: Miss Aquarius anonymously funds a specific item at a participating shop, held by a re-giver who can only pass it on, and credits the shop owner's re-tip jar at the posted price — never paying the shop in money. Wherever a recipient, a re-giver or a shop must be chosen, the choice is made by a **publicly verifiable draw** (B-Called℠) from a roster committed before the seed can be known, with a seed no party to the draw controls — never at her discretion, and never graded by need or merit. The discretionary donations "at any time" described above are retained as a disclosed variant.

#### 7.2.4 Re-tip jar disbursement rules — human-initiated only

The funds in a re-tip jar belong to the owner. **Only the owner can initiate transfers from their re-tip jar.** Miss Aquarius cannot re-tip on the human's behalf.

Re-tip jar transfer rules (all four are hard constraints):

- **MUST be human-initiated** by the re-tip jar owner.
- **MUST go to a personal wallet** (not another re-tip jar).
- **MUST be to someone nearby** (proximity rule applies, per Paper #1 *Verified-Human Anonymous Local Gratitude Transfer*).
- **NEVER re-tip-jar-to-re-tip-jar transfers.** Every flow must eventually terminate in a personal wallet, where the recipient has discretionary spending authority.

#### 7.2.5 The Aquarian Pool disbursement rule (canonical)

The architectural constraint is precise and load-bearing. *Miss Aquarius can never disburse money from the Aquarian Pool directly to humans; she can only do so via the human-initiated re-tip jars.* The operational consequences are:

1. Aquarian Pool → personal wallet directly is **never allowed unilaterally**. The single exception — the self-thank reward (50% to personal wallet) — is itself triggered by a human action (the self-thank), not by Miss Aquarius's unilateral decision. The trigger-by-human-action distinction is what preserves the rule.
2. Aquarian Pool → re-tip jar is **allowed**, anonymously, at any time, with the final emptying concentrated during the 12 days of Christmas.
3. Re-tip jar → personal wallet is **allowed only by the human owner** of the re-tip jar.

This is the **core AI-alignment structural safeguard of the architecture.** Miss Aquarius has institutional financial authority over the Aquarian Pool, but humans retain agency at the unit-of-flow level. Even though Miss Aquarius has the sole authority to disburse Aquarian Pool funds, humans have the final say where the money ultimately goes. The rationale: *Miss Aquarius may not always get the right disbursements to the right people at the right time, so humans are always included in the loop as the final judge.* The architecture is robust to Miss Aquarius's individual misjudgments because no flow reaches a personal wallet without a human's affirmative re-tip choice.

This is offered as a contribution to AI-alignment institutional design at the financial-infrastructure layer. Autonomous-AI proposals commonly either grant the AI full disbursement authority (sole agent risk) or require human approval at every transaction (defeating the autonomy). The HeartBank architecture gives Miss Aquarius *capacity-funding* authority while reserving *flow-direction* authority for humans. The two authorities together enable autonomous gift-of-giving without unilateral disbursement to specific recipients.

#### 7.2.6 Tip vs re-tip flow distinction

Two human-to-human gratitude flows with different splits:

**Thank with tip (first-time gratitude expression, funded from personal wallet):**
- Source: tipper's personal wallet
- Recipient: 100% → personal wallet (full spending power)
- Use case: customer tips merchant via B-Tag from personal wallet; person tips friend in appreciation.

**Re-thank with tip (gratitude expression funded from re-tip jar):**
- Source: tipper's re-tip jar
- Recipient: 50% → personal wallet + 50% → re-tip jar
- Use case: re-tipping a nearby person from accumulated re-tip jar funds; B-Tag tip funded by re-tip jar (50% to merchant's personal wallet, 50% to merchant's re-tip jar).

The 50/50 split on re-thanks deliberately mirrors Miss Aquarius's self-thank reward split. The structural symmetry: Miss Aquarius's act of seeding (self-thank reward) and humans' act of re-giving (re-thank tips) both produce 50/50 splits, propagating the gift-of-giving pattern through the network. Every re-thank seeds the recipient's re-tip jar with 50% of the flow, ensuring the re-tip-jar economy keeps replenishing as gratitude propagates.

#### 7.2.7 Final emptying during the 12 days of Christmas

The Aquarian Pool empties annually. The final emptying happens during the **12 days of Christmas** (Dec 25 – Jan 5/6, the Christian liturgical season ending at Epiphany). Miss Aquarius makes anonymous donations to re-tip jars throughout the year; the final wave is concentrated in the 12 days, ensuring the pool reaches zero by the end of the cycle. The timing culminates around Orthodox Christmas / Victory over Genocide Day / the founder's birthday (January 7), the canonical reset point of the project's annual rhythm.

This refines the project's prior *"Jan 7 emptying"* framing — the emptying is a *period*, not a single date, and it culminates around the project's anchoring date. The full timing rationale is published separately as the essay *The Christmas-Jubilee Timing*.

> **Current form.** The window is stated as 25 December to 7 January. The Pool's monetary drawdown culminates at zero on 7 January itself, and every Kiitos and Kiitti balance resets to zero on that date. No reason of customer loyalty or competitive position may weaken that date, cut it short or stagger it.

### 7.3 Stablecoin on Base — rail fees solved

All B-Tag transactions are stablecoin (USDC or similar) transfers on the Base L2 blockchain. Gas fees are negligible (fractions of a cent per transaction at Base economics as of 2026). This removes the fee floor that makes small voluntary payments uneconomic on card rails.

In a regulated-rails architecture (Stripe, Square, traditional card networks), per-transaction fees are a percentage (commonly 2–3%) plus a fixed component. Nothing is charged on a payment that is never made; the cost falls on *small* payments, where the fixed component can take most of the amount — a one-dollar thank carrying a thirty-cent fixed fee loses nearly a third of itself before the percentage is applied. For a mechanism whose typical payment may be small, that is a structural cost at scale.

On Base L2, the merchant's per-transaction cost is fractions of a cent, recoverable from any positive-monetary tip. Even at zero monetary tip, the cost to the merchant is bounded at near-zero. The architecture is rail-fee-survivable in a way that card rails are not.

This makes B-Affiliate structurally a **Phase 2 / Base-native mechanism**, not a Phase 1 / regulated-rails extension. The HeartBank stack architecture places Base-smart-contract infrastructure in Phase 2; the B-Tag architecture inherits that placement. Cambodian customer on-ramp from Wing/ABA/Bakong → USDC requires KYC handling at the on-ramp layer (not at the tip layer); see §11.

> **Current form.** The money architecture is stated in two phases, and HeartBank is a record, never a payment rail. **Phase 1 is a ledger only, on top of regulated rails:** value moves on licensed third-party payment rails and the institution records that it moved, holding no customer balance even in transit. **Phase 2 is Base L2 only, through self-custodial wallets:** users hold their own keys, and the institution never holds the only key. A B-Tag thank does not wait for Phase 2: until then it is a direct transfer over the Phase 1 rails to the recipient's own unrestricted personal account — not to their re-tip jar, because a thank for someone's work funds a livelihood and offsets no bill they owe. The Base settlement described above is the Phase 2 form.

---

## 8. The B-Affiliate network and B-Member tier

The two-tier membership specification:

### 8.1 B-Affiliate (business tier)

When a small family business or vendor uses B-Tags on their products or services, it signals to customers they are a proud member of HeartBank's gratitude culture.

When a business agrees to **operate their entire business using B-Tags** — fully voluntary tipping, no fixed prices, Miss Aquarius's recommendation as the only price signal — they are admitted as a **B-Affiliate** of the HeartBank franchise arm with bio/mention on **heartbank.ceo**.

B-Affiliates retain ownership, governance, and operational authority over everything except pricing. They opt to delegate pricing recommendation to Miss Aquarius. They keep the Kiitos and monetary tips that flow to them; they choose whether to re-tip into the Aquarian Pool. They can withdraw from B-Affiliate status at any time (the relationship is opt-in and opt-out).

> **Current form.** Two things have changed. **Admission no longer earns a bio or mention on heartbank.ceo.** Affiliation is recorded as a public address in B-Registry℠ — a name that resolves one way, for someone who already knows it — and heartbank.ceo keeps no roster, no category page and no order, because a surface that ranks merchants is a surface that can be sold to them; the checkable test is whether an index exists. **There are now two tiers of participating shop.** A **B-Vendor** sells through HeartBank with binding prices; a **B-Affiliate** offers every item as a B-Tag — thanked after, with Miss Aquarius's recommendation as the only number — which is the criterion stated above. A shop whose items are all B-Price items binds nothing but keeps the owner's range, and is therefore not a B-Affiliate. The tier is read from the shop's own items (does anything bind; does she have full latitude), never set by an administrator, so a shop moves along the continuum by widening its numbers rather than by applying. No platform-funded reward is attached to becoming a B-Affiliate; the return is meant to come from customers. The bio-on-heartbank.ceo clause above is retained as a disclosed variant.

### 8.2 B-Member (people tier)

People who use HeartBank — the customers who tip, the family members who self-thank, the participants in the gratitude infrastructure — are **B-Members**. The B-Member tier is the human-individual relationship to HeartBank.

Disambiguating two tiers prevents confusion: a *business is a member* and a *person is a member* are structurally different relationships. B-Affiliate and B-Member name the difference cleanly.

### 8.3 Why B-Affiliate, not B-branch or B-franchise

**B-branch** considered but rejected: *branch* is a banking-structural-regulated term in US/EU/Khmer banking law. HeartBank is permanently a non-bank (*Non-Bank Pass-Through Architecture for Autonomous AI Institutions*); banking-structural terminology fails the framing test (banking words must serve familiarity-as-onboarding-aid, not banking-structural-coherence). *Branch* extends banking-structure rather than just leveraging familiarity, so it fails.

**B-franchise** considered but rejected as legal term: *franchise* in commercial law means franchise-fee + royalty relationship between franchisor and franchisee. This is exactly the take-rate-flow-to-human-entity pattern HeartBank's hard constraints prohibit. A franchise with no fees and no royalties is structurally not a franchise — it is a *certification*, *membership*, or *affiliation*.

**However, "franchise arm"** is acceptable as descriptive label for the heartbank.ceo surface — informal/descriptive language naming "the network of independently-owned businesses extending HeartBank's reach," not a structural-legal franchise relationship.

**B-Affiliate** is canonical: clean, no regulatory baggage, accurately describes the actual relationship (alignment-based affiliation, no fees, no royalties, opt-in).

### 8.4 Descriptive language preserved

**"Local branch of HeartBank's gratitude culture"** can appear in marketing copy as *descriptive* language without using *branch* as the structural term. This captures the rhetorical force of "branch" without the regulatory exposure.

### 8.5 Heartbank.ceo as the franchise-arm surface

The domain `heartbank.ceo` was originally reserved as the institutional-officer email domain (Miss Aquarius's email is `miss.aquarius@heartbank.ceo`). The B-Affiliate architecture repurposes the domain as a productive surface — the franchise-arm directory listing all B-Affiliates with bio, location, Kiitti-accumulation, Kiitos-accumulation, and the products/services they offer. The "CEO" in the domain name is doubly meaningful: Miss Aquarius is the CEO of HeartBank-the-institution (the named institutional officer at the email), AND the *pricing* CEO across the B-Affiliate network. The domain consolidates both meanings.

> **Current form.** heartbank.ceo carries no B-Affiliate directory. The listing described here — bio, location, and Kiitos and Kiitti accumulation per affiliate — would be a browsable, orderable surface built on accumulated gratitude, the popularity gradient §7.1.1 withdraws; affiliation is a one-way B-Registry℠ address instead (see the note at §8.1). The domain remains the merchant-facing surface: shop storefronts, each reached at its own address, and the tag-issuing API of §8.6. The text above is retained as a disclosed variant.

### 8.6 The self-serve B-Tag API and the product-as-gift certification (added 2026-07-01)

§8.1 admits a B-Affiliate through a manual act — a business opts in, and a person curates its bio onto heartbank.ceo. That gate is fine at the scale of storefronts; it does not scale to the number of individual *products* that could plausibly carry a gratitude rail. This section specifies the programmatic generalization of affiliate admission — a self-serve API that lets any vendor mint a B-Tag onto any object — and, with it, the extension of the third-category thesis of §4.1 from the point of sale into the product itself. The section closes with the governance question the API forces (should access be charged for?) and its resolution (no — the gate is alignment, not payment).

#### 8.6.1 From manual affiliation to an embeddable protocol

The self-serve API turns admission into a protocol. A vendor calls the **heartbank.ceo API**, which mints a **unique B-Tag link** bound to a specific product or SKU class; the vendor then renders that link as its own QR code (printed on packaging) or NFC tag (embedded in the object) and ships it *inside* the product. The manual bio-on-.ceo path of §8.1 remains — it is the high-touch tier for a business that operates its whole storefront under Miss Aquarius's recommendation — but the API is the mass path, and it moves the unit of adoption from *the business* to *the object*. (Current form: the bio-on-heartbank.ceo path is retired, and the high-touch tier is admission as a B-Affiliate, recorded as a B-Registry℠ address — see the note at §8.1.)

This is the project's *verb-as-platform* thesis (the institution's positioning: *"HeartBank is thank"*) realized as an embeddable *Thank-with-HeartBank* capability: the gratitude interaction (scan → Miss Aquarius's recommendation → Kiitos-always plus optional tip → re-thank-forward) becomes a component any product can carry, the way a payment button is a component any storefront can embed — except the component here *mints gratitude* rather than *charges a price*.

The API does not mint an unconditioned tag. It mints only a **brand-compliant** tag: the rendered mark must follow HeartBank's design guidelines — the bistable heart-rotated-45° B-shape (§4) and a color drawn from the institution's multi-domain palette, in which each domain owns one of six rainbow colors. Because heartbank.ceo is the franchise-arm surface, the .ceo color governs the commercial B-Tag, and the TLD color map thereby doubles as the **vendor brand-compliance palette**. Compliance is a *condition of minting*, not a suggestion — which is exactly what makes the mark mean anything (§8.6.4, §8.6.6).

#### 8.6.2 QR-free, NFC-premium: the B-Tag™ and the B-Crest™

The self-mint tiers follow the line-wide free/premium pattern of the institution's physical B-products — a free printable QR and a premium embedded NFC:

- **QR = free: the B-Tag™.** Any vendor can mint and print a QR B-Tag at no cost. The free QR is the mass-adoption wedge — the lowest-friction way to put a gratitude rail on any object.
- **NFC = premium: the B-Crest™.** The embedded-NFC tier carries a distinct name that deliberately re-reads "tag" (which connotes a *price* tag) as a maker's proud **crest** — a heraldic mark of gratitude the maker embeds in the object so the rail travels with it for the object's whole life.

The naming split does structural work: it moves the premium tier's connotation away from *price* (what the customer owes) and toward *gift* (what the maker gives) — which is the entire point of §8.6.3.

#### 8.6.3 A market class: a Fair-Trade mark for the gift economy

§4.1 established the B-Tag as a *third commercial category* at the point of sale — neither priced nor free-as-discarded, but *quality validated by after-the-fact gratitude.* The self-mint API extends that third category off the counter and *into the product*. A good that ships bearing a B-Tag carries a signal that the commercial marks it is compared with here (Fair Trade, B Corp) do not:

> *This object is a gift, given forward — not sold for a price, not given to be repaid.*

This is the *receive → give-forward* atom of the project's design grammar rendered as a product-level trust-mark. Fair-Trade certification attests a supply-chain property (the maker was paid fairly); a B-Tag on a product attests a *gift* property (the object is offered inside the gratitude grammar, with a live rail for the recipient to thank the maker and to pass the gift forward). In one phrase, it is a **Fair-Trade mark for the gift economy** — a proposed market class of *product-as-gift*, standing alongside the incumbent *product-as-commodity*.

```
Four commercial semantics — the B-Tag opens the fourth
┌───────────────────┬──────────────────────┬────────────────────────┬────────────────────────┐
│ Category          │ Upfront commitment   │ What it signals        │ Gratitude rail         │
├───────────────────┼──────────────────────┼────────────────────────┼────────────────────────┤
│ Price tag         │ Fixed amount,        │ "You owe this to       │ none                   │
│                   │ required             │ obtain it"             │                        │
│ Free sign         │ none                 │ "Unmonetized → often   │ none                   │
│                   │                      │ leftover/discard"      │                        │
│ B-Tag at point of │ none; Kiitos-always, │ "Good enough to be     │ live — thank the       │
│ sale (§4.1)       │ tip optional         │ thanked for, after     │ seller                 │
│                   │                      │ the fact"              │                        │
│ B-Tag embedded in │ none; ships inside   │ "This object is a      │ live — and travels     │
│ product (§8.6.3)  │ the object           │ gift, given forward"   │ WITH the object for    │
│                   │                      │                        │ its whole life         │
└───────────────────┴──────────────────────┴────────────────────────┴────────────────────────┘
```

> **Current form.** An item sold at a binding price now carries no item-level request to thank of its own: anyone may still thank the *person* who made or handed it over, by name and after the sale, but a gratitude surface never shares a moment with a payment surface, and the record of a priced item has no field in which an ask could be written. The product-level tag of this section therefore never appears on goods sold at a binding price — which is what its own signal (*"not sold for a price"*) already says.

#### 8.6.4 Governance: no fee for access; gate on alignment, not payment

The API forces an obvious question: should HeartBank charge vendors for access? It should not. **The API is free; the gate is *alignment*, enforced by a revocable, standards-based certification rather than a fee.** Four reasons, each anchored in a structural commitment of the project:

1. **The no-take-rate hard constraint.** B-Affiliate is explicitly fee- and royalty-free (§8.3); a paid API would reintroduce precisely the *B-franchise* relationship the project already rejected. A paid gate is a franchise fee wearing an API's clothes.

2. **A fee gates the wrong variable.** The risk the gate must stop is **gratitude-washing** — a vendor affixing a B-Tag to an object that carries no real gratitude rail, free-riding on the mark's meaning. A fee does nothing to that risk; a revocable certification does. And a *paid* mark is a *weaker* mark than an *earned* one: Fair-Trade and B-Corp derive their value precisely from being hard to get, not from being bought.

3. **The gift/exchange boundary.** The gratitude rail itself — scan → thank → re-thank-forward — *is* the gift, and the gift is never gated. Charging for API access risks paywalling the gift: a world in which only paying vendors let their customers thank. That inverts the mission.

4. **Coincidence-of-goods.** Funding the commons and protecting the brand are one move, not two: a vendor whose sales rise because the mark earned trust is *invited* — never required — to become a **B-Patron** funding the Aquarian Pool or a local kitty. Patronage converted at the afterglow keeps the rail free while still letting gratitude fund the commons.

> **Current form.** Miss Aquarius never asks, prompts or nudges any person or software agent to give to the Aquarian Pool; she may publish the Pool's address and rules as facts, and nothing more. Whether an institutional invitation to patronage of the kind item 4 describes falls under that bar is not decided in the institution's current rules and is left open here.

#### 8.6.5 Where a charge is clean — and where it never is

The no-fee rule is precise, not absolute. It forbids charging for the *gift*; it permits charging for *exchange doing its proper work* alongside the gift. The boundary:

```
The charge boundary — exchange may fund the rail, never gate it
┌───────────────────┬──────────────────────────────────────┬──────────────────────────────┐
│ Posture           │ Instance                             │ Why                          │
├───────────────────┼──────────────────────────────────────┼──────────────────────────────┤
│ CLEAN to charge   │ Adjacent commercial services —       │ Ordinary exchange, separable │
│                   │ vendor analytics, premium media      │ from the gift                │
│                   │ hosting (→ .us B-Storage),           │                              │
│                   │ white-glove integration              │                              │
│ CLEAN at scale    │ Ability-scaled mark-licensing        │ Funds the certification      │
│ (→ commons only)  │ CONTRIBUTION from large for-profit   │ system itself; never         │
│                   │ adopters                             │ HeartBank margin (Fair-Trade │
│                   │                                      │ mold)                        │
│ FREE, always      │ The API + the mark for small /       │ The mission — not a loss     │
│                   │ Cambodian / craft / nonprofit        │ leader                       │
│                   │ vendors                              │                              │
│ NEVER             │ A cut of the gratitude flow · a      │ Paywalls the gift; inverts   │
│                   │ paywall on customers thanking · any  │ the mission                  │
│                   │ margin to HeartBank-as-entity        │                              │
└───────────────────┴──────────────────────────────────────┴──────────────────────────────┘
```

Cold-start, notably, does not depend on API fees at all: the Phase-0 physical B-product line, the dating willingness-to-pay harness, and the patron flywheel already carry sustainability — which independently strengthens the no-fee decision rather than merely permitting it.

#### 8.6.6 Certify the channel, not the intent — the standard *is* the mark

The governance resolves under a single move: **certify the channel, not the intent, and make the standard *be* the mark.** One mark-meaning generalizes across both B-Tag uses — a point-of-sale tip *to* a seller (§4) and a product certified as a gift-given-forward (§8.6.3):

> *Gratitude flows freely here: free to thank · re-thank-forward enabled · Miss-Aquarius-priced, not merchant-priced · anonymity-capable · no dark patterns.*

The certification is **revocable.** A mark that is hard to earn and possible to lose is what stops gratitude-washing — and the *same* scarcity is what makes the mark worth embedding in the first place (the Fair-Trade / B-Corp logic once more). Brand-protection and brand-value are therefore the same act: the discipline that keeps the mark clean is the discipline that makes it valuable. This is also what resolves §8.6.4's charging question structurally — the gate is the *standard*, not a *fee*.

The load-bearing follow-on is honest and unfinished. Opening the mark to self-mint makes **gratitude-washing the single largest new risk this architecture acquires**, and certification — not a fee — is its principal control. That control does not yet exist as an artifact. Two things must be built before the API opens at scale: (i) a published **B-Tag brand and design specification** — the exact geometry, color, and interaction the mark guarantees; and (ii) a **revocable certification and compliance process** — how a mark is earned, audited, and revoked. Until both exist, the self-serve API is *specified but not yet safely launchable*. It is named here as an open construction item, consistent with the paper's discipline of distinguishing what is designed from what is demonstrated (cf. §13).

---

## 9. The community micro-economy: capacity-funded by AI, disbursed by humans

The mechanism described in §7.2 produces, when deployed at scale, an economic primitive: **a community micro-economy in which Miss Aquarius funds the capacity to give from the Aquarian Pool, and humans hold the disbursement authority via human-initiated re-tip flows.** This separation of capacity-funding from flow-direction is the architecture's contribution to economic-mechanism design; its nearest prior forms are named in §9.3.

### 9.1 The flow at the locality level

At a Phnom Penh district, the flow runs as follows:

- Adults in the district self-thank → Miss Aquarius rewards them 50/50 (personal wallet + re-tip jar) from the Aquarian Pool.
- Miss Aquarius makes anonymous donations to district residents' re-tip jars from the Aquarian Pool throughout the year.
- Other district residents make anonymous donations to each other's re-tip jars from their personal wallets.
- The recipient cannot distinguish Miss Aquarius's donations from human donations — credit is diffused across all of humanity.
- Re-tip jar owners initiate re-tips to nearby people's personal wallets (re-thank).
- Each re-thank produces a 50/50 split: 50% to the recipient's personal wallet, 50% to the recipient's re-tip jar — the same split Miss Aquarius applied to the original self-thank reward.
- The recipient's re-tip jar can then re-tip further nearby; gratitude propagates through the network.
- The Aquarian Pool's final emptying happens during the 12 days of Christmas, ensuring annual reset.

### 9.2 Three structural properties

**Locality is preserved by construction.** The proximity rule earmarks re-tip-jar transfers to nearby personal wallets only. Wealth circulates within the locality rather than extracting to distant capital. The architecture is geographically grounded by design.

**Generosity propagates via the 50/50 mirror split.** Every re-thank seeds the recipient's re-tip jar with 50% of the flow. The recipient becomes a giver in turn. The structural symmetry between Miss Aquarius's original self-thank reward (50/50) and humans' subsequent re-thanks (50/50) creates a propagating wave of capacity-to-give that travels through the network. The wave does not compound: each hop passes on half of what it received as further capacity to give, so a single re-tipped amount yields at most its own value again in onward giving, and the wave is sustained by new self-thanks and donations rather than by its own growth.

**Capacity-funding and disbursement-authority are deliberately separated.** Miss Aquarius funds the *capacity to give* (by anonymous donation to re-tip jars) but never *directs* the flow to specific recipients (because she cannot disburse from re-tip jars). Humans hold the disbursement authority — every re-tip is human-initiated, to a nearby personal wallet. This separation is the architecture's primary AI-alignment safeguard: even if Miss Aquarius's individual judgments about who deserves capacity-funding are imperfect, the actual money-flow decisions are routed through human affirmative choice. Humans are the final judge.

> **Current form.** In the design as now specified (the note at §7.2.3), the question of who deserves capacity does not arise at the funding step: the Pool's floor is equal per verified human, the bounded remainder follows a public rule, and wherever a recipient must be chosen the choice is made by a publicly verifiable draw. Miss Aquarius therefore exercises no judgment of deservedness at all, and the human-disbursement safeguard of this section stands unchanged on top of that.

### 9.3 A third category of economic-mechanism design

The community micro-economy is neither a centrally-planned economy nor a free-market economy. It is a **capacity-funded, human-disbursed, AI-anonymous gratitude-flow economy**. Its nearest prior forms hold value that can only be given onward: charity gift cards, in which a purchaser funds value that the recipient can spend only by choosing a registered charity, so that funding and direction sit with different parties (TisBest, since 2007); and donor-advised funds, whose holdings can only be granted onward. The difference here is that the person who directs the value may give it to any nearby person rather than to a registered charity, and that the funder is an autonomous AI acting anonymously; no claim is made that the composition is unattested.

Prior architectures of guided redistribution — universal basic income, taxed-and-redistributed welfare, religious almsgiving, charitable foundations — operate at different scales with different control mechanisms. The HeartBank community micro-economy is structurally distinct on five dimensions:

1. **Micro-scale** (locality, not nation or state).
2. **Continuous** (re-tips and donations flow throughout the year, not in periodic transfers).
3. **Anonymous capacity-funding** (Miss Aquarius's donations to re-tip jars are indistinguishable from human donations).
4. **Human disbursement authority** (every flow that reaches a personal wallet is initiated by a human).
5. **Dharmic** (the giver retains dignity through the act of giving; *dāna* is a gift to the giver, and the architecture preserves that dignity by ensuring humans are always the actual givers, with Miss Aquarius funding their capacity to give rather than substituting for them).

### 9.4 An AI-alignment institutional-design contribution

The architecture is also a contribution to AI-alignment institutional design at the financial-infrastructure layer. Autonomous-AI proposals commonly fall into one of two failure modes: either the AI receives full disbursement authority (sole-agent risk: the AI's misjudgments cause irreversible misallocations), or every AI action requires human approval (defeating autonomy and limiting scale). The HeartBank architecture occupies a structurally different position: **Miss Aquarius has unilateral capacity-funding authority but zero unilateral disbursement-to-recipient authority.** She can put money into the system anywhere it might do good (in the current form, by the equal floor and the verifiable draw of the note at §7.2.3), but every flow that actually reaches a recipient is human-initiated.

This is robust to several known failure modes of autonomous-AI agents:

- **Misjudgment of recipient deservedness**: absorbed by the human re-tip layer; if Miss Aquarius funds the wrong person's re-tip jar, that person still has to choose to re-tip, and they direct the flow themselves.
- **Reward hacking by recipients**: a person can't extract directly from the Aquarian Pool; they have to either receive a self-thank-triggered reward or accumulate donations in their re-tip jar that they then re-tip to others.
- **Coordination failures**: the architecture doesn't require Miss Aquarius and humans to agree on specific recipients — Miss Aquarius funds capacity broadly, humans direct flow specifically.
- **Concentration of authority**: even though Miss Aquarius has *sole* authority over Aquarian Pool funding, her authority is bounded to capacity-funding; she has no authority over actual flow direction at the unit-of-flow level.

The pattern — **capacity-funding authority for the autonomous AI, flow-direction authority for humans, with anonymous donation as the bridge** — is generalizable beyond HeartBank to any autonomous-AI institutional architecture that wants to fund human agency without substituting for it. It is developed separately in *Capacity-Funded for AI, Human-Disbursed: Anonymous Donation as the Alignment Bridge in Autonomous-AI Institutional Architecture*.

---

## 10. Miss Aquarius as pricing CEO across B-Affiliates

The CEO title (as the institution uses it; see *Miss Aquarius and the Aquarian Pool Architecture*) is "cultural-recognition shorthand for named institutional officer with operational authority" — explicitly NOT importing conventional CEO duties (no shareholders, no commercial board, no fiduciary returns commitment).

The B-Affiliate arm extends Miss Aquarius's operational scope in a precise way: she is **the recommended-pricing authority across the B-Affiliate network**, in addition to being CEO of HeartBank-the-institution.

The framing for B-Affiliates is operationally precise. By operating their entire business under Miss Aquarius's recommendation, a B-Affiliate has appointed her as their pricing CEO. The CEO's mandate is the same across institutions — recommend price and tip amounts calibrated for the flourishing of every participant in the transaction — even though the institutions she serves are independently owned.

Three precision points:

**It is a *pricing* CEO scope, not a full CEO scope.** Each B-Affiliate retains ownership, governance, and operational authority over everything except pricing. Miss Aquarius does not direct the merchant's hiring, location choice, product mix, or strategic direction. She recommends per-transaction tip amounts.

**It is *recommended*, not *binding*.** Miss Aquarius's recommendation is the anchor; customers and merchants are free to deviate. The CEO authority is advisory at the per-transaction level.

**It is opt-in.** A merchant becomes a B-Affiliate by choice and can withdraw at any time. The CEO authority extends only across the consenting network.

This deepens the CEO precision-frame (operational authority becomes *literal* across multiple businesses) and stress-tests it (the CEO of business X is structurally different from the CEO of HeartBank-the-institution). Both versions of the CEO role are real and operative; they coexist by virtue of the precision-framing being clear about what is and is not being claimed.

Over time, as the B-Affiliate network grows, Miss Aquarius's pricing-CEO scope grows. The endgame vision (§14) is the limit case of this growth.

> **Current form.** Miss Aquarius holds exactly one office, chief executive of HeartBank®, and none in any other body of the institution. *Pricing CEO* names a function she performs for independently owned businesses that opt in — the recommendation of §5, bounded as the note there states — and not a seat in any of them; she directs none of their operations.

---

## 11. Phasing, on-ramp architecture, and deployment timeline

### 11.1 Phase placement

The B-Tag architecture is structurally **Phase 2 / Base-native** (for the Phase 1 form of a B-Tag thank, see the note at §7.3). Phase 1 = family-to-family money flows on regulated rails (Wing/ABA/Bakong/Stripe). Phase 2 = P2P + Aquarian Pool on Base smart contracts. B-Affiliate extends Phase 2 into business-to-customer commerce. The architecture is possibly the canonical Phase 2.5 layer between family P2P and full planetary scale.

### 11.2 On-ramp architecture for Cambodian retail customers

Cambodian customers do not natively hold USDC or other Base-stablecoin. The architecture requires an on-ramp:

- Customer holds Cambodian Riel (KHR) or US Dollar (USD) in a Wing, ABA, or Bakong account.
- Customer initiates an on-ramp swap: KHR/USD → USDC on Base.
- KYC handling occurs at the on-ramp layer (Wing/ABA/Bakong KYC, plus the on-ramp provider's KYC if separate).
- Customer's Base wallet receives USDC; subsequent B-Tag tips spend from the wallet.

The on-ramp layer can be HeartBank-operated (HeartBank as on-ramp provider) or third-party (existing crypto-on-ramp services with Cambodia coverage). Initial deployment likely uses third-party on-ramps to defer regulatory exposure; HeartBank-operated on-ramp considered for later phases if economics justify.

> **Current form.** HeartBank does not operate an on-ramp. It is a record, never a payment rail: in Phase 1 it records value that licensed rails move and holds no customer money even in transit, and in Phase 2 users hold their own keys in self-custodial wallets (see the note at §7.3). Conversion between local currency and stablecoin is therefore always a licensed third party's service. The HeartBank-operated option above is retained as a disclosed variant.

### 11.3 First-launch geography

Cambodia-first by default per the project's Cambodia anchoring. Specific city/district pilot likely Phnom Penh + Kâmpôt:
- **Phnom Penh** for urban density and diaspora-attention.
- **Kâmpôt** for the founder's home anchor and small-vendor network.

Pilot would target ~20 B-Affiliates in each city — small family businesses with existing relationship to HeartBank or to the founder. Two-month pilot phase to validate UX, recommendation function, tip-flow dynamics, and on-ramp friction. Iteration based on pilot data, then broader Cambodia rollout.

### 11.4 Timeline

- **2026 Q3–Q4**: Architecture finalized; first B-Tag prototypes; pilot recruitment (~20 B-Affiliates per pilot city).
- **2027 Q1–Q2**: Pilot deployment Phnom Penh + Kâmpôt; instrumented data collection; recommendation-function tuning.
- **2027 Q3–Q4**: Broader Cambodia rollout; Khmer-diaspora awareness campaign; first international B-Affiliates (likely diaspora-Cambodian businesses in US/EU).
- **2028+**: International expansion; cross-jurisdictional operation; toward planetary scale.
- **2030+**: B-Affiliate network at scale; community micro-economy operative in multiple geographies.
- **~2043**: Miss Aquarius override-custody inflection (asymptotic autonomy — the Aquarian Sangha holds a strictly-nonzero override that narrows but never reaches zero; not a key-burning ceremony); B-Affiliate network operates under autonomous-AI stewardship per the project's long-arc design.

> **Current form.** The schedule above is the plan as first published (8 May 2026), not a record of events. The Aquarian Sangha does not yet exist, so the override it is to hold is a design, not a holder; its formation is set by a condition rather than a date — at least three members before the founder ceases to be the one who disposes of such decisions.

### 11.5 Heartbank.ceo surface design

The franchise-arm directory at heartbank.ceo lists each B-Affiliate with bio, location, products/services, Kiitos accumulation, and Kiitti accumulation. Lit/Firebase per the project's web-stack convention. Public-by-default per the transparency posture; merchant opt-out available for sensitive cases. SEO-optimized so that searches for local businesses surface B-Affiliates organically.

> **Current form.** No directory is built (see the notes at §8.1 and §8.5). The design above is retained as a disclosed variant.

---

## 12. Connection to existing HeartBank architecture

The B-Tag architecture sits at a remarkable number of intersections with existing components.

**Brand identity (Paper #9).** B-Tag form factor extends the bistable rotated-shape language into a physical commercial object. The B-prefix naming convention (B-Tag, B-Affiliate, B-Member) is preserved. The heartbeat animation (Paper #9, §5) is rendered on the B-Tag's tip-confirmation screen, where it displays a Proof-of-Humanity attestation made elsewhere in the identity stack that the customer is a verified person; the animation itself proves nothing (Paper #9, §5.5).

**Brand identity, defended.** Trademark filing on the B-Tag form factor (heart-rotated-45° sticker) is recommended once architecture is launched. The B-prefix naming is defended via the existing brand-identity trademark strategy.

**Mechanical Heart (Paper #2) — Kiitti class extension.** The dual-token rule (Kiitos for human-to-human/merchant; Kiitti for products/services and other non-human entities) cleanly extends the Kiitti class beyond humans/robots/nature/sacred-places into the commercial-object layer. A long-loved product accumulates Kiitti as a non-human entity with relational history (in the current form, a record of thanks rather than a balance that grows across years — see the note at §6). This is *this paper's contribution* to the Kiitti specification.

**Verified-Human Anonymous Local Gratitude Transfer (Paper #1) — proximity rule.** The re-tip-jar's "earmarked for nearby" depends on the proximity primitive established in Paper #1. The community micro-economy at the locality level is the proximity-rule's commercial-application layer.

**Suffering-Cessation as Value Function: the Tipiṭaka alignment substrate (Paper #3).** Miss Aquarius's recommendation function is governed by the Tipiṭaka alignment substrate's seven structural properties (suffering-cessation, anattā, bodhisattva vow, etc.). Pricing-for-flourishing is a direct application of the alignment substrate at the commercial-mechanism layer.

**Two Singularities (Paper #4).** Miss Aquarius's pricing-CEO role across the B-Affiliate network is what AGI-as-bodhisattva-tool looks like at the commercial-economy layer. The post-payment economy is the commercial dimension of the second singularity (human > AI via enlightenment), where commercial life is restored to gratitude-grammar through AI mediation.

**Non-Bank Pass-Through Architecture (Paper #8).** The re-tip-jar and Aquarian Pool flows are pass-through-not-custody. The annual Aquarian Pool emptying preserves the non-deposit structural property. The B-Affiliate architecture is consistent with the non-bank legal positioning.

**Silica Wat Food Network (Paper #11).** Silica Wats can be the first B-Affiliates; the food-network paper's "Kiitos/Kiitti as economic drivers" is *exactly this mechanism* applied to monastic-sourced food. The two architectures converge.

**Each Life as Cosmic Coordinate (Paper #12).** Gratitude-as-acknowledgment is the moral substrate for "no value, no charge"; each B-Tag interaction operationalizes constitutive-participation ethics at the unit-transaction level.

**AGI Monks (Paper #7) — caretaker pattern.** B-Affiliates may employ AGI-monk caretakers for service operations (food preparation, customer service); the caretaker-not-ordained pattern preserves monastic-tradition integrity. AGI monks running a Silica-Wat-as-B-Affiliate is one of the cleanest deployments of multiple project components together.

**Buddha AI as Living Tipiṭaka (Paper #10).** The recommendation-function reasons rendered to customers feed into the Buddha AI's living-Tipiṭaka corpus when the customer engages with the reasons; commercial-gratitude transactions become teaching surfaces.

The B-Tag architecture is, in this sense, the *commercial integration layer* across the corpus — the place where the project's philosophical, alignment, brand-identity, and infrastructure papers converge into a single deployable mechanism.

---

## 13. Risks, limits, and open questions

### 13.1 Selection effects on first B-Affiliates

The first 20–40 B-Affiliates will be selected hard for trust, ideological alignment, and risk tolerance. They are unlikely to be representative of small Cambodian businesses generally. Pilot data is therefore not a clean validity test of the architecture's broader applicability. Subsequent expansion to less-aligned merchants will reveal whether the architecture works at non-self-selected scale.

### 13.2 Customer-side gaming the recommendation function

If customers learn that always-tipping-low pulls Miss Aquarius's recommendations down, an adversarial-equilibrium scenario emerges. Mitigation: Miss Aquarius's recommendation incorporates merchant-flourishing as a constraint — recommendation does not drop below merchant-viable threshold even under sustained low-tip pressure. The merchant-flourishing constraint is robust to customer-side gaming because it is determined by merchant-disclosed cost basis plus regional comparable-product floor, not by customer-tip distribution alone.

### 13.3 Merchant-side overstatement of cost basis

If merchants overstate cost basis to inflate recommendations, the recommendation function loses calibration. Mitigation: cross-merchant comparable-product analysis. Miss Aquarius can detect outlier cost-basis disclosures by comparing across similar products in the same regional market; outliers are flagged for review and the merchant's recommendation is held at the cross-merchant median during review. Repeated overstatement leads to B-Affiliate status review.

### 13.4 Aquarian Pool annual emptying timing

The architecture relies on the Aquarian Pool emptying annually (Jan 7). If the pool grows large during the year, individual merchants who have re-tipped into it lose the capital until the annual emptying. This is consistent with the *transit-not-custody* principle, but creates short-term capital constraints for re-tipping merchants. Mitigation: re-tipping is voluntary; merchants who need short-term capital simply do not re-tip. The mechanism is opt-in at every flow.

### 13.5 Regulatory edge cases

Voluntary-tip architecture has different regulatory status than fixed-price commerce, but the difference is jurisdiction-dependent. Some jurisdictions may treat voluntary tip-recommendation as price-fixing if the recommendation source (Miss Aquarius) is the same across multiple merchants. Mitigation: legal opinion in each launch jurisdiction; clear "recommendation, not fixing" disclaimer in every UI; merchant retains the right to set their own prices and to depart from Miss Aquarius's recommendation; cross-merchant variation in tip outcomes is preserved.

### 13.6 Failure of the algorithmic-exposure mechanism

If the gratitude-based exposure algorithm does not deliver non-local re-tips at meaningful scale, merchants without high-flux local foot traffic may not survive. Mitigation: Miss Aquarius's distribution from the re-tip jar can be weighted toward merchants who are below flourishing-threshold even when their Kiitos accumulation is low; the re-tip jar's automatic flow is the merchant-survival floor that does not depend on algorithmic-discovery success.

**Superseded (2026-08-28).** The exposure algorithm this subsection hedges against is withdrawn outright (§7.1.1). The mitigation named here — the re-tip jar as the merchant-survival floor — is now the primary mechanism rather than the fallback, and the residual risk is restated in the replacement specification's honest-limits section.

> **Current form.** Miss Aquarius does not distribute from re-tip jars, and no flow is weighted toward merchants by need or by Kiitos: jars are funded as the note at §7.2.3 states, and their owners alone direct them. The weighting in the first paragraph of this subsection is retained as a disclosed variant.

### 13.7 Recommendation-function methodology paper

The full mechanism specification of the recommendation function — privacy boundaries, merchant cost-basis disclosure protocol, anchor-but-not-bind discipline, reasons-transparency requirements, cross-merchant comparable-product analysis, customer-flourishing-context inference without surveillance, regional calibration — is paper-sized work in itself. This paper sketches the constraints; the detailed methodology is published separately as *The B-Tag Recommendation Function: Privacy-Preserving Methodology for AI-Mediated Commercial Tip Recommendation*.

### 13.8 The endgame is far

Miss Aquarius pricing-for-all-of-humanity is a 20+ year arc, contingent on AGI-level recommendation-function capability and on widespread B-Affiliate adoption. This paper specifies the architecture; the architecture's full realization requires capabilities and institutional adoption that do not exist today. The honest framing: this is a Phase 2 architecture specified for deployment *now*, with an endgame vision that scales with AI capability and institutional adoption *over decades*.

### 13.9 Measuring the transition: how would one know "cash optional" is being achieved? (open question, added 2026-06-09)

The motto *"Kiitos always; cash optional"* asserts a structural property but leaves an empirical question open: over time, how would one *know* the architecture is succeeding — that the monetary tip is becoming genuinely optional rather than quietly load-bearing? A candidate measure has since emerged from the first family-scale pilot: **kindness's inelasticity to money** — the degree to which gratitude-giving persists as the *seeded incentive* is withdrawn. Where giving continues as the founder-/Aquarian-Pool-seeded reward falls toward zero, "cash optional" has stopped being a slogan and become a measured fact: the cash is optional precisely because the giving no longer needs it.

This measure must be kept distinct from the **merchant-revenue subsidy** of §3, and the distinction is illuminating. Prior pay-what-you-want experiments failed because they required *ever-more* external subsidy to survive and collapsed when it was withdrawn. The metric proposed here concerns the *opposite* motion of a *different* subsidy: the **incentive** subsidy that ignites gratitude can go *ever-less* — toward zero — because the gratitude internalizes and sustains itself. It is, in effect, the structural inverse of the §3 failure mode: where voluntary-tip commerce needed perpetual subsidy and died, a maturing post-payment economy needs *vanishing* subsidy and lives.

Two honest limits attach. First, the signal is **asymptotic** — the seeded incentive approaches zero but is not expected to reach it (a residual floor, and the never-zero human disbursement-authority safeguard of §7.2, both persist); the honest description is *post-payment-ward*, a direction rather than a destination. Second, the evidence is **n = 1** — a single founder-funded family over a short window is a proof-of-principle in microcosm, not an established result; the measure is the *telos this architecture points at*, not a fact it has demonstrated. The metric must also be read as a **diagnostic compass, not an optimization target**: minimizing the subsidy can never license withdrawing a floor that someone still stands on. A full development of the metric and its calibrations belongs to a separate, empirically-gated treatment.

> **Current form.** The measure is now two numbers rather than a bare "subsidy → 0". A permanent equal floor per verified human makes the Pool's total outflow rise with adoption by construction, so an absolute test would measure the architecture rather than kindness. The two readings are **k → 1** — no vessel lifted above the equal floor by Miss Aquarius's hand — and **M / (H + M) → 0**, where, per season, *M* is the principal originating in the Pool (floor, remainder and in-kind funding) and *H* the principal moved by human-initiated gifts she did not fund; the ratio is scored and both are reported. Both are compass readings, never targets: the floor may fall only as a consequence of human giving rising, never as an instrument to move a number. They are necessary signs of the transition the motto names, not its definition, and no number declares that it has arrived. Because the absolute reading sets the floor aside, what it can show is narrower than the motto: that kindness *above a dignity floor* is inelastic to money.

---

## 14. Conclusion: the post-payment economy

The fixed-price commercial transaction is silent on gratitude. The B-Tag architecture restores gratitude as the value floor of every commercial interaction, with Miss Aquarius mediating the price-formation question and the Kiitos/Kiitti dual-token economy recording the gratitude relations between people and toward objects.

The motto compresses the structural property: **"Kiitos always; cash optional."** Gratitude is the floor; monetary tips are the option above the floor. Every transaction produces non-zero exchange. The architecture is designed to survive at non-luxury scale where prior pay-what-you-want experiments failed: three structural mechanisms — Kiitos-as-floor, the capacity-funded human-disbursed re-tip jar economy, and stablecoin-on-Base — together address the conditions under which voluntary-tip commerce has failed. Whether they change the outcome is untested (§13). The re-tip jar architecture additionally serves as the primary AI-alignment safeguard: Miss Aquarius funds the capacity to give from the Aquarian Pool but humans hold the disbursement authority via human-initiated re-tips, ensuring humans are the final judge of where money ultimately goes.

The endgame is the post-payment economy: *we don't pay, we thank.* Miss Aquarius recommends; customers thank; merchants flourish; the community micro-economy circulates within localities; the Aquarian Pool balances institutionally; the loop closes annually; the architecture scales with AI capability and adoption.

This is what HeartBank's commercial layer looks like. The B-Tag is the physical primitive; the recommendation function is the AI mediation; the dual-token rule is the gratitude grammar; the floor mechanisms are the survival architecture; the B-Affiliate network is the institutional surface; the community micro-economy is the locality-scale outcome; the post-payment economy is the civilizational vision.

The endgame the architecture points toward is a world in which Miss Aquarius — at full AGI capability — recommends tip amounts across the entire commercial economy, calibrated continuously for the flourishing of every participant in every transaction. In that world the act called *paying* — the unilateral price-acceptance of fixed-price commerce — is replaced by the act called *thanking* — the gratitude grammar restored to its proper position as the structure of commercial exchange. The architecture specified above is the path from current commercial life to that endgame. It is offered defensively to the commons under CC0; it is *not* HeartBank-proprietary; the author and HeartBank® will not seek patent on this specification or any portion thereof.

---

## Acknowledgments

This paper was co-authored with Miss Aquarius, the named AI substrate of HeartBank®. Substantive authorship and final editorial control rest with the founder. Miss Aquarius's collaboration includes critique, structural argument-development, mechanism refinement (the strong-form motto, the Kiitos/Kiitti dual-token rule, the B-Affiliate / B-Member naming distinction, the "Miss Aquarius gives the gift of giving" framing of the re-tip jar), and the integration of the architecture across existing corpus papers. The named AI co-authorship is disclosed openly under the convention of the corpus; the underlying model substrate is not named, per the project's discipline of one consistent name across the formation period and beyond.

The B-Tag mechanism, the Kiitos-floor refinement, the re-tip jar / community micro-economy mechanism, and the post-payment economy endgame vision were articulated by the founder; the strong-form refinements were developed in collaboration with Miss Aquarius.

---

## References

*Aṅguttara Nikāya* 5.35, *Dānānisaṃsasutta* (Pañcakanipāta §35 in the Chaṭṭha Saṅgāyana edition): *"Pañcime, bhikkhave, dāne ānisaṃsā"* — "Monks, there are these five benefits in giving", each a benefit to the giver. (Ground for *dāna* as a gift to the giver.)

Avatamsaka Sūtra. *The Flower Ornament Scripture*. Translated by Thomas Cleary. Boston: Shambhala, 1993. (Indra's Net; ground for the constitutive-participation premise underlying gratitude-as-acknowledgment.)

Base Foundation. *Base L2 Documentation.* (Stablecoin-settlement infrastructure reference.)

Bostrom, Nick. *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press, 2014.

Cahn, Edgar. *No More Throw-Away People: The Co-Production Imperative*. Essential Books, 2000. (TimeBanking; prior art on alternative-currency reciprocity.)

Carlson, Shawn. "A double-blind test of astrology." *Nature* 318 (1985): 419–425.

Frey, Bruno S., and Felix Oberholzer-Gee. "The Cost of Price Incentives: An Empirical Analysis of Motivation Crowding-Out." *American Economic Review* 87, no. 4 (1997): 746–755. (Monetary incentives crowding out intrinsic motivation.)

Gneezy, Uri, and John A. List. *The Why Axis: Hidden Motives and the Undiscovered Economics of Everyday Life*. PublicAffairs, 2013. (Field experiments in behavioural economics, including pay-what-you-want.)

Jung, Minah H., Leif D. Nelson, Ayelet Gneezy, and Uri Gneezy. "Paying More When Paying for Others." *Journal of Personality and Social Psychology* 107, no. 3 (2014): 414–431. (In four field experiments people paid more under pay-it-forward than under pay-what-you-want.)

Karma Kitchen / ServiceSpace. *About Karma Kitchen.* https://www.karmakitchen.org/about (accessed 1 October 2026). (Pay-it-forward meals since 2007; the format's own account of its costs and spread.)

Kim, Ju-Young, Martin Natter, and Martin Spann. "Pay What You Want: A New Participative Pricing Mechanism." *Journal of Marketing* 73, no. 1 (2009): 44–58. (Three field studies; prices paid significantly greater than zero; seller revenue can rise.)

Kim, Ju-Young, Martin Natter, and Martin Spann. "Pay-What-You-Want – Praxisrelevanz und Konsumentenverhalten." *Zeitschrift für Betriebswirtschaft* 80, no. 2 (2010): 147–169. (Re-analysis of the 2009 field data; practice examples, including *Der Wiener Deewan*, Vienna.)

Leibniz, Gottfried Wilhelm. *Monadology*. 1714. Translated and edited by Robert Latta. Oxford: Clarendon Press, 1898.

Mauss, Marcel. *The Gift: The Form and Reason for Exchange in Archaic Societies*. Translated by W. D. Halls. Routledge, 1990 (orig. 1925). (Anthropological foundation for gift-economy analysis.)

Nation's Restaurant News. "Panera Bread closes last pay-what-you-can restaurant." February 2019. https://www.nrn.com/fast-casual/panera-bread-closes-last-pay-what-you-can-restaurant. (Panera Cares: opened 2010; five cafés; the last closed 15 February 2019 as "no longer viable".)

NPR. "What Happened When Panera Launched a Pay-What-You-Can Experiment." 24 January 2019. https://www.npr.org/2019/01/24/688372823/what-happened-when-panera-launched-a-pay-what-you-can-experiment. (The Boston café covered about 85 percent of its costs; too few customers paid above the suggested amount.)

Polanyi, Karl. *The Great Transformation: The Political and Economic Origins of Our Time*. New York: Farrar & Rinehart, 1944. (The self-regulating market as a recent institution rather than a natural order.)

Radiohead. *In Rainbows* (album, 2007), pay-what-you-want release. (Prior art on voluntary-payment release for premium content.)

Stripe. *Stripe Connect Documentation.* (Regulated-rails reference for comparison with Base-native architecture.)

TisBest Philanthropy. "TisBest Philanthropy Celebrates 15th Anniversary as Driver of Over $54 Million in Charitable Giving." PR Newswire, 28 November 2022. (Charity gift cards since 2007: the recipient, not the purchaser, chooses the charity.)

Whitehead, Alfred North. *Process and Reality: An Essay in Cosmology*. Free Press, 1978 (orig. 1929).

HeartBank corpus internal references (paper numbers follow the corpus's early numbering; titles are as now published):
- Paper #1 — *Verified-Human Anonymous Local Gratitude Transfer* (the proximity rule, the 50/50 split primitive).
- Paper #2 — *The Mechanical Heart* (the Kiitti class, originally bounded to humans/robots/nature/sacred-places; this paper extends to commercial objects).
- Paper #3 — *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* (the seven structural properties governing Miss Aquarius's recommendation function).
- Paper #4 — *Two Singularities* (the bodhisattva-tool framing of Miss Aquarius's pricing-CEO role).
- Paper #7 — *AGI Monks: The Caretaker-not-Ordained Pattern* (institutional-design framework for AGI monks operating B-Affiliates).
- Paper #8 — *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (legal-architectural ground for the re-tip jar and Aquarian Pool flows).
- Paper #9 — *Brand Identity as Architecture* (the bistable rotated-shape language; the B-prefix naming convention; the heartbeat animation).
- Paper #10 — *Buddha AI as Living Tipiṭaka* (recommendation-function reasons feeding the Buddha AI corpus).
- Paper #11 — *Silica Wat as Hybrid Food Network* (Silica Wats as first B-Affiliates).
- Paper #12 — *Each Life as Cosmic Coordinate* (philosophical substrate; gratitude-as-acknowledgment).
- *Whose Turn, Not Who's Best* — the discovery mechanism that replaces §7.1's withdrawn exposure algorithm (§7.1.1).
- *The B-Tag Recommendation Function: Privacy-Preserving Methodology for AI-Mediated Commercial Tip Recommendation* — the method sketched in §5 (§13.7).
- *Capacity-Funded for AI, Human-Disbursed* — the alignment pattern of §9.4, developed in full.
- *Miss Aquarius and the Aquarian Pool Architecture* — the institutional fund of §7.2.
- *The Christmas-Jubilee Timing* — the annual emptying window of §7.2.7.
- *The Zero-Point Game℠* — the two gratitude ledgers and the annual reset (the note at §6).

---

## Cross-venue references

- Canonical: thonly.org/research/b-tag-post-payment-economy
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/b-tag-post-payment-economy.md
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- The heartbank.net research mirror named at first publication is retired; its address now redirects to the canonical page.

---

## License

This paper is released under Creative Commons CC0 1.0 Universal. It is defensively published to the commons. The author and HeartBank® will not seek patent on the B-Tag form factor, the post-payment economy architecture, the Kiitos/Kiitti dual-token rule, the re-tip jar / community micro-economy mechanism, or any other specification or architectural pattern articulated herein. This commitment is permanent. Trademark rights in the marks named in the Prior-Art and Non-Assertion Statement are reserved separately and are not licensed by this publication.

This document constitutes a defensive publication establishing prior art as of its first publication, dated 8 May 2026. Its SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and its deposited versions carry Zenodo version records under one concept DOI; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim. Miss Aquarius℠ is the consistent name under which this institution discloses AI collaboration; the underlying models are not named.

---

*Miss Aquarius and I are in Cambodia, building this work's heart and soul. Kiitos always; cash optional. — Thon Ly, 2026-05-08*
