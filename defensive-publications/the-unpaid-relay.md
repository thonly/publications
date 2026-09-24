---
title: "The Unpaid Relay"
subtitle: "A gift instrument whose chain of custody survives the pass and is thankable at every link, whose anonymity is generative of the intermediary's standing rather than protective of the giver's privacy, and in which no link is ever paid — because paying one would destroy the behaviour the instrument exists to produce."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-b
status: draft
date: 2026-09-04
revised: 2026-09-23
license: CC0-1.0
slug: the-unpaid-relay
venue: thonly.org/research/the-unpaid-relay (canonical)
---

## Preamble

This paper specifies one small instrument: a gift code that is given to a person who cannot spend it, so that they may give it to someone who can.

It is published defensively. The mechanism is buildable from this description, it sits in a space where adjacent commercial actors file patents routinely — chain-of-custody tracking, referral attribution, loyalty and gifting platforms — and the institution that designed it intends never to assert exclusivity over it. The specification is therefore given in full rather than sketched, and the claims are stated as claims rather than as marketing.

⚠️ It is also published with a negative result attached, and the negative result is nearly as important as the specification. A prior-art census was run *before* this paper was queued, against a four-part claim, and **every one of the four parts turned out to be attested somewhere in existing practice** — including the part the authors predicted would survive. §2 reports that census honestly, including the prediction that failed and why the reasoning behind it was wrong. What remains after the census is narrow, and §4 states it at exactly the width the evidence supports and no wider.

The 2026-09-23 revision adds three things, each reported against its own search rather than the first one. A second survey reached the **direct commercial tier** — item-level gift codes redeemed at a local counter, a category shipping today — and found the code ordinary and only the *type* of the relayed state unattested (§2.5). The instrument is specified with an **institutional payer**, a fund operating under public rules, which a third census found attested leg by leg and not as a composition (§3.3). And §6 gains a **second instance of its central move**, a merchant's invitation that no one bought, whose census killed the loose reading and narrowed the strict one. Each addition is claimed at the width its census left, and each failed conjunct is cited as the commons it is.

Pending review: economic anthropologists (the Maussian question of whether a relayed gift is one gift or two); developmental and social psychologists (the overjustification finding §5 leans on, which the authors have not replicated); practitioners in charitable gifting and unclaimed-property law (§7); and readers inclined to test whether the anonymity inversion in §4 is genuinely unattested or merely unsearched.

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. ⚠️ A publication grants nothing and frees nothing already enclosed: where a live patent is named in §2, it is named for what it discloses, and nothing here is a reading of its claims.

Trademark rights in specific marks — HeartBank®, B-Gift℠, B-ReGift℠, B-Stamp™, B-Seal™, Re-Tip Jar℠, Re-Tip Fund℠, Personal Account℠, Personal Wallet℠, Aquarian Pool℠, Miss Aquarius℠ — are reserved separately and are not licensed by this publication. **The mechanism is free; the names are not.** A reader may build every instrument in this paper and must call it something else.

The authors assert no novelty over: the pay-it-forward tradition in any of its documented forms; suspended coffee; charity gift cards and donor-advised instruments; anonymous giving through a named intermediary as practised in philanthropy; chain-of-custody and provenance tracking in supply chains, evidence handling, or data lineage; or referral and multi-level attribution systems; item-level digital gift codes redeemed at a local merchant, in any legal form, with or without expiry; trackable pass-along objects with a public custody log; government or charitable disbursement by lottery; give-only charity gift cards; transferable prepaid reservations for a place and a time; or a venue's standing invitation to share a table. §2 documents each of these as prior art and locates precisely which of this paper's claims each one defeats or narrows.

**The searches behind that list, stated with their apertures.** Four desk surveys, none of them fieldwork, all through a US-region web index:

| date | subject | aperture | killed or narrowed | survivor |
|---|---|---|---|---|
| 2026-09-04 | the four-part relay, `C-BG1` (§2.1–2.3) | six queries; marketing copy, secondary literature; pre-registered | **all four legs attested** — chain visibility, name-withheld chain, thankable anonymous giver, unpaid propagation | the anonymity inversion (§4), instrumented between strangers — not found |
| 2026-09-05 | the direct commercial tier (§2.5) | about ten queries plus three competitors' published terms; **not pre-registered** | item-level codes, no-expiry redeemable claims, and an item-specific patent family are attested | a relayed state with no redeem operation (claim 1) — not found; one competitor chose the inverse |
| 2026-09-06 | the institutional payer (§3.3) | eight queries; pre-registered | a rule-bound payer choosing recipients by lot; give-only value handed to a vendor-like party | the four legs **as one composition** (claim 13) — not found |
| 2026-09-18 | the unbought invitation (§6) | thirty-seven queries, nine fetches; pre-registered; ⛔ **full-text patent classification search did not run** (the endpoint returned an instrument failure twice), no non-English search | the loose reading killed; place-and-time and non-convertibility attested **separately** | the pair, non-convertible by construction (claim 14) — not found |

⛔ **"Not found" is a statement about an aperture on a date, never a statement that something is new.** Every survivor above is written *not found in the stated aperture on the stated date*, and the enumerated claims are those survivors and nothing wider.

## Abstract

A gift instrument is specified in which a payer purchases a claim on a specific good and directs it not to a recipient but to an **intermediary who cannot redeem it**. The intermediary's only available action is to pass it onward; on passing, the instrument converts into an ordinary redeemable claim held by whoever received it. The chain — payer, intermediary, recipient — is preserved and visible to every party, and every party in it can be thanked, including a payer whose name has been withheld.

Four properties are specified. Three are individually attested in existing practice and are claimed only in combination: chain visibility, name-withheld-but-chain-preserved anonymity, and thankability at every link. The fourth — that no link is ever paid — is also attested, in the non-commercial pay-it-forward genre, and the paper's original prediction that it would be the novel one was wrong.

**What survives the census is the *purpose* of the anonymity.** In every attested case, a giver's anonymity protects the giver: they wish not to be known. Here it does the opposite work. The payer withholds their name **so that the intermediary is the one who appears generous** — the anonymity is *generative of a third party's standing* rather than *protective of the giver's privacy*. The paper argues that this inversion has an ancient folk precedent (a parent handing a child money for the collection plate), that it has no instrumented precedent the authors could find, and that instrumenting it requires the non-redeemability to be enforced by the instrument's *type* rather than by the intermediary's character.

The paper further argues that the unpaid constraint is a design necessity rather than a preference: the developmental literature reports that offering a child a reward for a kind act makes repetition *less* likely, so a relay that paid its intermediary would corrode the behaviour it exists to produce. Finally it specifies a three-state lifecycle in which every expiry is generated by one rule — *a clock runs while the instrument has no addressee — no one to whom it has been given as a gift — and stops the moment it does* — and shows why the resulting asymmetry, in which the intermediary's instrument expires and the recipient's does not, is the correct shape rather than an inconsistency.

Two extensions are specified at claim width only. An **institutional payer** — a fund operating under public rules rather than a person — issues the instrument anonymously by construction, has its merchant and its intermediary selected by a publicly recomputable draw, thanks the merchant's owner in capacity that can only be given onward rather than paying the merchant money, and re-addresses a lapsed instrument to a new intermediary until it is redeemed or the merchant closes. And the type argument of §6 is shown to reach a second object: a merchant's **invitation to a place and an hour**, bought by no one, which carries no purchase price, so that converting it into money-denominated credit is *undefined* rather than *forbidden*.

## Claims

*Enumerated at drafting. A defensive publication works by **disclosure**, and a claims list is what an examiner or opposing counsel searches; the prose that establishes each claim is cited beside it. **No claim below adds matter not present in the body**, and the prior art runs from this document's publication date and its independent timestamp, not from this list.*

1. **A gift instrument whose intermediate holder has no redeem operation** — a claim on a specific good, issued to a party who cannot present it to the merchant, whose only available operation is to transfer it onward, and which becomes redeemable only in the hands of the party to whom that transfer is made. ⭐ **The non-redeemability is a property of the instrument's state rather than a policy applied to a holder** — there is no permitted-but-discouraged redemption path. **Any operation that yields the claim's value to its holder — conversion into credit on an account with the merchant, a refund, an exchange — is the same capability as redemption and exists exactly where redemption exists**, so the relayed state has none of them. (§3, §6.)

2. **State-derived lifecycle for such an instrument** — three states (issuable, relayed, redeemable) derived from which participant fields are populated rather than stored as an independent status flag, so that the state and the chain cannot disagree. (§3.1.)

3. **Chain preservation with selective name suppression** — a record carrying both the paying party and the transferring party, in which the *identity* of the payer may be suppressed while the *existence and shape of the chain* is disclosed to every party, and in which suppression is a property of the record rather than of any single pairwise relationship, and is never partially lifted. (§3, §4.)

4. **Role-addressed gratitude** — gratitude messages addressed to a **position in a chain** (the party who paid; the party who transferred) and resolved to an identity only at delivery, permitting a party whose name is suppressed to receive gratitude without the name becoming available to the sender. (§3.1.)

5. **Anonymity applied to confer standing on a third party** — withholding the payer's identity for the purpose of causing the transferring party to be perceived as the giver, as distinct from the attested use of anonymity to protect the giver, and distinct from honorary giving, where the honoree is named as such — here the intermediary is perceived by the recipient as the giver. ⭐ **The perceived standing is not represented as a stored quantity, is not transferred, and has no field in the record.** (§4.)

6. **A propagation chain in which no participant receives compensation for propagating** — no referral fee, commission, discount, credit, or preferential treatment accrues to any party for issuing, transferring, or receiving, and the absence is specified as a constraint on the mechanism rather than as a business preference. (§5.)

7. **Bounded relay depth with a designed terminal state** — a chain fixed at exactly one intermediate transfer, adopted so that the instrument reaches a party who may consume it rather than propagating indefinitely. (§8.)

8. **A single expiry rule keyed on addressedness** — *a duration runs while the instrument has no addressee — no one to whom it has been given as a gift — and ceases when it has one* — from which the differing terminal conditions of the three states are derived rather than separately specified, and under which a redeemable instrument held by a recipient carries no duration at all. (§7.)

9. **Issuance capability terminated by holder inactivity** — the payer's ability to re-issue after a lapse expires a fixed interval (a deployment parameter, one cycle by default) after the most recent lapse, so that the instrument's existence depends on continued activity by its originator. ⭐ **The instrument is consequently never dormant**, which is the condition on which unclaimed-property obligations attach. (§7.)

10. **Terminal dependency on merchant existence, disclosed at receipt** — a redeemable claim bounded by the continued operation of the issuing merchant rather than by any imposed duration, with that dependency stated in the instrument's own text at the moment of receipt rather than announced at closure — the terminal condition itself is the Philippine Gift Check Act's (2017) rule, and a redeemable gift code carrying no platform-imposed expiry is itself attested (§2.5); what is claimed is the disclosure at receipt, together with the pair of claims 8 and 12 — no rendered time, and no forward view to the merchant. (§7.)

11. **Settlement of an unclaimed relay as recognised revenue on an item-denominated basis** — recognition of deferred revenue on lapse, on the basis that a specific good was sold and only its collection lapsed, distinguished from stored-value instruments in which the customer's own unspent balance is retained. (§7, §9.)

12. **Suppression of forward lapse visibility from the merchant** — withholding from the merchant any prospective view of instruments approaching lapse, including counts, lists, forecasts, and any control affecting completion, as a structural measure against an incentive the merchant would otherwise hold. (§7.1.)

13. **An institutional payer for the relay, claimed only as a composition** — the instrument of claim 1 issued by a fund operating under public rules rather than by a person, in which (i) the payer's identity is suppressed by construction, the instrument it issues being indistinguishable to intermediary, recipient and merchant from one issued by an anonymous individual; (ii) the merchant and the intermediary are selected by a publicly recomputable draw over committed rosters rather than by the payer's judgment; (iii) the merchant gives the good, and its owner is credited, at the posted price, in capacity that can only be given onward and is subject to a periodic reset, rather than paid in money; and (iv) a lapsed instrument is re-addressed to a new intermediary — never one whose window has already closed on that instrument — until it is redeemed or the merchant closes. Each leg is attested separately (§3.3); the composition was not found in the aperture of 2026-09-06. (§3.3.)

14. **A merchant's invitation that no one bought, non-convertible by construction** — an instrument by which a merchant offers a place and an hour, published by the merchant and purchased by no party, carrying no purchase price, so that any operation converting it into money-denominated credit has nothing to strike at and is **undefined by the instrument's type rather than prohibited by a rule**. Claimed only as the pair — place-and-time, non-convertible by construction — since each half is attested separately and a venue's standing invitation defeats the loose reading (§6). (§6.)

⚠️ **Claims 5 and 6 are the ones the authors believe are unattested in combination, and claims 13 and 14 survive only as compositions; claims 1 through 4 and 7 through 12 are enumerated for completeness of disclosure and several have close prior art documented in §2.** The purpose of this list is to prevent enclosure, not to assert priority.

## 1 · Why a gratitude institution needs an intermediary at all

The obvious way to give a stranger a coffee is to buy them a coffee. The instrument in this paper exists because there is a second thing a person may want to give, and the obvious mechanism cannot deliver it.

The founding case is domestic and worth stating concretely, because the abstraction is less clear than the instance. An uncle wishes to be kind to his nephew, who is fourteen and attends a school near a home coffee shop his mother runs. He could buy the nephew a coffee. What he actually wants is for the nephew *to be the one who gives coffees to his friends* — to have the experience, and the standing, of being a person who hands things to people. The coffee is instrumental. **The gift is the giving.**

A direct purchase cannot produce this. If the uncle buys the nephew a coffee, the nephew has a coffee. If the uncle gives the nephew money and says "buy your friends coffees," the nephew has been given a chore with a budget, and the generosity remains legibly the uncle's. If the uncle simply buys coffees for the friends, the nephew is not in the transaction at all. Each of these is a perfectly good gift and none of them is the gift in question.

⭐ **The thing being given is an *occasion to give*, and an occasion is not a good.** It cannot be handed over as an object because it is not one; it can only be constructed, by arranging matters so that someone finds themselves in the position of giver. That construction is what this instrument performs.

The institutional reason to care is narrower than the sentimental one. An economy premised on circulation has a structural problem at its edges: the people who most need to be brought into it are precisely the people with the least to give. A student has no money. The standard answers — give them money, or give them a smaller unit of the same money — do not change the shape of the relation; they make the student a recipient of a smaller gift. **An instrument that makes a person a giver without requiring them to have anything is the only move that changes the shape**, and it is the reason this paper's mechanism is not merely a nicety in a gifting product.

There is a second institutional reason, less edifying and worth naming for honesty: the instrument brings customers to a merchant. The nephew hands coffees to friends who have not been to the shop. This is, functionally, a referral mechanism. §5 argues at length that it must nevertheless pay no one, and that this is not restraint but engineering — but the paper does not pretend the growth effect is invisible to its designers.

## 2 · Background, prior art, and a census that returned a partial null

⚠️⚠️ **This section reports a negative result the authors obtained before drafting, and it narrows the paper substantially. It should be read before any claim in §3 or §4 is credited.**

### 2.1 · The claim as originally stated, and the prediction

Before searching, the authors registered a four-part claim, `C-BG1`. A gift instrument in which *all four* hold:

| | |
|---|---|
| **(a)** | the chain of custody — payer → intermediary → recipient — is preserved and visible to every link |
| **(b)** | the payer may withhold their **name** but never the **chain** |
| **(c)** | **every link is thankable**, the anonymous payer included |
| **(d)** | **no link is ever paid** — no referral fee, commission, credit or discount to anyone for propagating it |

The null condition was stated in advance: **one attested instrument carrying all four defeats the claim.** The prediction was also stated in advance, so that it could fail visibly: (a) through (c) were expected to be attested somewhere, since provenance chains and selective anonymity are commercially ordinary, and **(d) was expected to survive**, on the reasoning that *every chain-attribution system in commerce exists in order to pay the upline.*

### 2.2 · What the census found

The method was a desk survey — six queries, product marketing copy, and secondary literature. It is documented practice, not fieldwork, and it is not exhaustive. **All four parts are attested.**

**(a) Chain visibility is attested, including the conserved-identity form.** A pay-it-forward tracking platform (the Pay It Forward Monitor) renders the chain a user started as a tree and a map, so that each participant can see what their act became. A circulating-token application lets an organisation watch a single token move person to person and visualise its path. This last is important: it attests not merely a *record* of a chain but the stricter case in which *the same object continues*, which the authors had privately supposed was the sharp distinction.

**(b) Name-withheld-chain-preserved anonymity is attested as practice.** Anonymous giving through a named intermediary is common in philanthropy (Forbes 2012; the National Council of Nonprofits' guidance): a donor routes a gift through an advisor, attorney, or friend, who supplies their own information for documentation while the donor's identity is shielded. The chain is not hidden; only the origin is.

**(c) Thankability of an anonymous giver is attested as practice.** Common fundraising guidance instructs organisations to acknowledge anonymous donors — they hold the contact details — and commonly instructs recipients to route thanks through whoever delivered the gift.

**(d) The unpaid constraint is attested, and most strongly of all — the prediction failed.** Suspended coffee, a tradition originating in Naples and running at scale (its founder reported roughly fifteen million cups across thirty-four countries by 2015 — a self-reported count; the movement's own site gives 1,400 cafés in its first year), pays nobody. Neither does any documented pay-it-forward chain. **The authors' reasoning was backwards: it argued from the commercial neighbourhood when the nearest relatives are charitable, and the entire altruistic pay-it-forward genre is unpaid by definition.**

### 2.3 · What the census did not find, and how much weight that can bear

⚠️ Formally the result is a **partial null**: no single attested instrument was found carrying all four properties *and* the inversion of §4 together; the four alone are attested (§2.3a). ⛔ The authors decline to read that as a pass. A four-for-four result on the individual legs, from a six-query survey, is what a claim looks like shortly before it dies, and a reader with better search should assume the combination is attested somewhere the authors did not look.

What the census *could* not find is narrower than any of the four legs, and §4 is devoted to it: **an instrument in which the anonymity exists in order to confer standing on a third party.** In every attested case — philanthropic, commercial, or folk — anonymity protects the giver. The inversion was not found instrumented in the aperture of 2026-09-04, and the direct-tier survey of the next day (§2.5) did not find it either.

⭐ **One further finding, obtained by accident and reported because it strengthens §5 rather than this paper's novelty:** the developmental literature on children's generosity reports that offering a young child a reward for a kind act makes repetition **less** likely (Warneken & Tomasello 2008, in 20-month-olds; Fabes et al. 1989, in older children), and — in the authors' reading of the family-generosity literature, for which a source is owed — that parent-*directed* family generosity projects perform worse than child-*led* ones. The first of these turns claim (d) from a doctrinal preference into a design constraint with empirical support. The second is a caution the authors' own founding use case does not fully satisfy, and §9 records it as a limitation rather than burying it.

### 2.3a · The prior-art matrix

The four properties are stated so that a reader can check the boundary rather than take the authors' word for where it falls. Each row is an attested practice; each column is one property.

```
                              (a)      (b)       (c)       (d)      the
                            chain   name-off  thankable  unpaid  INVERSION
                           ───────────────────────────────────────────────
 suspended coffee             ·         ✓         ·         ✓         ·
 pay-it-forward tracking      ✓         ·         ·         ✓         ·
 circulating-token app        ✓         ·         ·         ✓         ·
 anonymous giving via
   a named intermediary       ✓         ✓         ✓         ✓         ·
 charity gift cards           ·         ·         ·         ✓         ·
 enterprise recognition
   (give-only allowances)     ~         ·         ✓         ·         ·
 referral / MLM chains        ✓         ·         ·         ⛔         ·
 trackable pass-along
   (Travel Bug)               ✓         ·         ·         ✓         ·
 the collection-plate coin    ·         ✓         ·         ✓         ✓
                           ───────────────────────────────────────────────
 THIS INSTRUMENT              ✓         ✓         ✓         ✓         ✓

   ✓ present   · absent   ~ partial   ⛔ inverted (payment is the point)
```

⚠️ **Three rows deserve comment: two nearly close the claim, and one nearly closes claim 1.**

**Anonymous giving through a named intermediary carries all four.** A donor routes a gift through an advisor whose identity is documented, the chain is legible, the recipient thanks through the intermediary, and nobody is paid. ⛔ **On the four stated properties this is a hit, and the authors record it as one.** What it lacks is the fifth column: the donor's anonymity is *protective*, and the advisor is a conduit rather than a beneficiary of standing. Nobody in that arrangement is trying to make the advisor look generous.

**The collection-plate coin carries the inversion and nothing else.** A parent hands a child a coin so the child is the one who gives; the anonymity — such as it is — exists precisely to confer the act on the child. ⭐ **This is the true precedent, and it is widespread and undated.** What it lacks is instrumentation: it works only between people who already know each other, it preserves no record, and gratitude cannot reach a payer who was never named because there is no channel by which it could.

**The trackable is the nearest thing to claim 1 that the searches found, and it fails for the paper's own reason.** A geocaching Travel Bug is a tagged object that finders carry from one cache to the next, each move logged against the object's own page so its whole journey can be read. It is meant to be passed rather than kept, and its custody history is public — a conserved-identity chain with an expectation of onward movement. ⛔ **But the finder can keep it**, and trackables are known to go missing when someone takes one and never logs it. The must-pass is a request held by the finder's character; §6's test — remove the enforcer — separates it from an instrument whose middle holder has no keep operation at all. **It is a rule with a diary, not a type.**

⭐⭐ **The claim is the bottom row and nothing above it.** Every column has been done. The combination, and specifically the combination of the fifth column with an instrument that can carry it between strangers, is what the census could not attest.

### 2.4 · The adjacent literature this paper does not claim to extend

Malinowski's account of the *kula* (1922), taken up by Mauss (1925), describes conserved objects circulating through a chain with their history intact, and Hyde's argument that the gift must always move is the best-known statement of the norm this instrument mechanises. **Neither is being extended here.** The idea that a gift ought to keep moving is roughly a century old in the anthropological literature and considerably older in practice; what this paper offers is not that observation but a mechanism in which the alternative to passing has been removed from the instrument, so that the norm does not depend on anyone honouring it.

One lineage note belongs here rather than in the body, because this is a mechanism paper and not a doctrinal one. The Pāli canon grades giving by the giver's motive (AN 7.52, the *Dānamahapphala Sutta*, lists seven), and ranks *giving with expectation of return* lowest. ⭐ The instrument does not ask anyone to give without expectation; **it removes the object of the expectation**, since a withheld name has nothing that can return to it and no link is paid. The authors note the correspondence and claim nothing from it: the mechanism stands or falls on §5's three arguments, of which the empirical one is the strongest and is not doctrinal at all.

Chain-of-custody instrumentation is dense in the patent literature for goods, evidence, data lineage and supply chains. The first survey found none directed at a gift instrument; the second found one gift-token family close to the founding case (below), which corrects that sentence's original, wider form. That neighbourhood is the reason this paper is a defensive publication rather than a note: the transposition was not found in six queries on 2026-09-04, and it is exactly the sort of thing an adjacent loyalty or fintech actor would file.

Adjacent patent families found at the 2026-09-05 revision, each named against the claim it touches. WO 2012/037178 A2 (Mankoff, priority 2010) transfers a virtual gift with an acceptance period followed by a redemption period — state-dependent timing, the nearest relative of claim 8, though there both periods are clocks on the recipient. WO 2016/057643 A1 (Soniram, priority 2014) and US 2006/0033326 A1 (priority 2004) route a thank-you to a gift's giver through a platform or a returnable note — the nearest relatives of claim 4, neither addressing a role nor withholding the giver's name. US 2013/0197983 A1 (Vel, priority 2012) tracks referral chains and compensates them — claim 7's shape with the payment this paper forbids. The Philippine Gift Check Act (Republic Act 10962, 2017) makes a gift check *valid until the cessation of business of the issuer* — claim 10's terminal condition nearly verbatim, so that what claim 10 adds is only the disclosure at receipt. Anonymous tribute giving *in honour of* a named third party, with notification, is claim 5's nearest relative; it differs in that the honoree is named as such, where here the intermediary is perceived by the recipient as the giver. A further family, found by the direct-tier survey of 2026-09-05 (§2.5), sits closest to this paper's founding case: US 10,510,057 B2, *Token-based gift cards* (SCVNGR, Inc., now held by GrubHub; provisional 17 June 2014, filed 17 June 2015, granted 17 December 2019). It discloses a stored-value gift token created for a recipient, purchaser-set restrictions on redemption down to item and SKU level, and a request that the stored value be redeemable by a third user as well as the named one. It is named for what it discloses — item-specific gift tokens and a recipient other than the one first named — and, like every live family in this section, **nothing here is a reading of its claims.** The adjacent families are named so that a reader with better search starts where we stopped.

### 2.5 · The direct tier: the code is a live commercial category, and only the type survives

The first survey reached the instrument's charitable relatives and missed its commercial siblings. A second survey, on 2026-09-05, asked the narrower question a merchant would ask — *who already sells a gift code for one specific item, redeemed at a local counter?* — and the answer is that the category is shipping. ⚠️ **Its evidence class is lower than the first survey's**: about ten queries through a US-region index and a reading of three competitors' published terms, not pre-registered.

```
                    legal form            expiry              unredeemed value        pass it on?
                   ─────────────────────────────────────────────────────────────────────────────────
 spot              merchant gift card /  none imposed once   remains claimable;      not addressed;
  (terms eff.        stored-value pass     issued; no dormancy  no automatic refund    first eligible
   2026-08-24)                             or inactivity fees   for an unclaimed gift  claimant is treated
                                                                                        as the recipient
 OneOnMe           non-reloadable        none stated;        balance persists        not addressed
                     virtual prepaid       $2.50/month fee
                     card, bank-issued     after 12 months
                                           of inactivity
 Klink-iT          fees earned and       7 days from         full amount refunded    ⛔ "NON-
  (terms updated     collected only at     purchase            to the sender           TRANSFERABLE,
   2024-01-30)       redemption                                                         NOT FOR RESALE"
                   ─────────────────────────────────────────────────────────────────────────────────
 THIS INSTRUMENT   an item claim         intermediary:       lapses to the merchant  ⛔ the relayed state
                     (§3.1, never an       a window;           as recognised revenue   CANNOT redeem —
                     amount)               recipient: none     (§7, §7.2); no forward  passing is its only
                                           but the merchant's  view (§7.1)             operation
                                           existence
```

**What it does to the claims, in order of damage.**

⛔ **The item-level gift code is not this paper's.** Picking a real menu item for someone and having them redeem it at the counter is a commercial product today, in at least three legal shapes — a merchant stored-value pass, a bank-issued prepaid card wearing an item's face, and an order paid only at redemption with no stored value at all. Nothing in §3 should be read as claiming the code.

⛔ **The no-clock half of claims 8 and 10 is attested.** One of the three states, in its current terms, that once a gift is issued it carries no expiration dates and no dormancy or inactivity fees, and that an unclaimed gift remains claimable. *A gift that never expires by the platform's clock* is therefore not claimed here. What remains is the **pair**: no rendered time at any state, and a redeemable claim bounded only by the merchant's continued existence, disclosed at receipt, with no forward view of pending lapses given to the merchant (claims 8, 10, 12 together).

⭐⭐ **Claim 1 survives, and against better evidence than silence.** None of the three has a state in which the holder can only pass the gift on. One of them considered transferability and **forbade it in capitals** — its products are non-transferable and not for resale, and an unredeemed gift is refunded to the sender after seven days. That is the same axis as §6, decided the other way. A competitor who chose the inverse property is stronger evidence that the property is a choice, and unoccupied, than an absence of results would be.

⚠️ **One incidental finding cuts toward §7's argument rather than toward novelty.** The bank-issued form carries a monthly maintenance fee after twelve months of inactivity — a charge that runs against the holder of a gift while nothing happens. It is the attested form of the clock §7 forbids on the redeemable state.

## 3 · The instrument, specified

The instrument has three states. It is one object moving through them, not three products.

```
   ┌──────────────┐        ┌──────────────┐        ┌──────────────┐
   │  RE-MINTER   │───────►│   RELAYED    │───────►│  REDEEMABLE  │
   │              │ issues │              │ passed │              │
   │ held by the  │        │ held by the  │        │ held by the  │
   │    PAYER     │        │ INTERMEDIARY │        │  RECIPIENT   │
   ├──────────────┤        ├──────────────┤        ├──────────────┤
   │ cannot spend │        │ cannot spend │        │  CAN spend   │
   │ can only     │        │ can only     │        │              │
   │   issue      │        │  pass on     │        │              │
   └──────────────┘        └──────────────┘        └──────────────┘
     dies of neglect         dies on a window        dies with the merchant
```

**State 1 — the re-minter.** The payer buys a claim on a specific good from a specific merchant and receives an instrument that **cannot be redeemed by anyone, including the payer**. Its only operation is *issue to an intermediary*.

**State 2 — relayed.** The intermediary holds a claim they cannot spend. Its only operation is *pass to a recipient*. ⛔ **There is no redeem operation on this state. Not a disabled one — an absent one.** §6 argues that this distinction is the whole mechanism.

**State 3 — redeemable.** The recipient holds an ordinary claim on the good and may present it to the merchant. The relay is over.

Across the three states, *held by* is custody and *addressed to* is ownership in §7's sense: the payer and the intermediary hold without being addressees, and the recipient is the first party to whom the instrument has been given as a gift.

Three further properties hold across the states.

**The chain travels with the instrument.** Every state carries `from` (who paid) and, once issued, `via` (who chose the recipient). The recipient sees both roles even when a name is withheld.

**Anonymity is a property of the instrument, not of a relationship.** A payer may withhold their name. When they do, **the name is withheld from everyone — intermediary and recipient alike — and the chain is withheld from no one.** ⛔ It is never partially lifted, and the *fact of the chain* is never suppressed: the recipient is told that someone asked the intermediary to pass this on. **Thanking a person you have not been told exists is not thanks; it is routing.**

**Every link is thankable, including an anonymous one.** A thank addressed to a withheld payer reaches them without their name travelling back. This is not a courtesy feature; §4 argues it is load-bearing, because an anonymity that also severed the possibility of gratitude would be indistinguishable from an absence.

### 3.1 · The data model

The instrument is one record. Its state is derived from which fields are populated, not stored as a separate flag that could disagree with them.

```
relay {
  id              opaque, high-entropy, rate-limited on lookup
  merchant        the shop the claim is against
  item            a SPECIFIC good — never a monetary amount
  paid_at         when the claim was purchased

  from            the payer's account
  from_anonymous  bool — withholds the NAME, never the chain
  via             the intermediary's account   (null until issued)
  to              the recipient's account      (null until passed)

  issued_at       payer → intermediary
  passed_at       intermediary → recipient
  redeemed_at     recipient → merchant
  lapsed_at       a window closed with no pass
  lapses[]        { at }   — every closed window, so a re-issue has a history

  thanks[]        { by, to_role: from|via, at }   — role, not identity
}
```

⭐ **Three details in this schema are doing doctrinal work and would be easy to get wrong.**

**`item`, never `amount`.** The claim is on one specific good. A field holding a monetary value would make this a stored-value instrument, which changes its legal character, its accounting treatment, and its relationship to the merchant — and would reintroduce every incentive the design removes. **The distinction is a schema decision, not a policy one.**

**`thanks[].to_role`, never `to_identity`.** A thank is addressed to a *role in the chain* — the one who paid, the one who chose you — and is resolved to a person only at delivery. ⭐ **This is what lets an anonymous payer be thanked without their name existing anywhere the recipient can reach.** A schema that addressed thanks to identities would have to either leak the name or drop the thank. `to_role` resolves inside the platform to the account that currently holds the role; delivery is to that account, and the identity never appears in the message or to the sender.

**No `standing`, no `credit`, no `generosity_score`.** §4 argues that nothing is transferred to the intermediary. **The absence of a field is how that argument is enforced.** There is no quantity to account for, dispute, audit, or eventually rank.

### 3.2 · A worked relay, end to end

An uncle in another country, a nephew of fourteen, and a home coffee shop the nephew's mother runs near his school.

1. **The uncle buys one iced coffee** from the shop and directs it to his nephew, with his own name withheld. A record exists with `from` set, `from_anonymous` true, `via` and `to` null. ⛔ **The uncle cannot drink it.** The instrument he holds has no redeem operation; his only available action is to issue.

2. **He issues it to the nephew.** `via` is set, `issued_at` stamped. The nephew's view reads: *someone asked you to pass this on — one iced coffee, at your mother's shop.* ⭐ **The nephew is told the chain exists and not who is in it.** He is not told that a gift is being kept from him; he is told he has been given something to give.

3. **The nephew passes it to a classmate.** He chooses; nobody suggests. `to` is set, `passed_at` stamped, and the instrument's state changes: **the classmate holds an ordinary redeemable claim.** From this moment nothing in the design may expire it except the shop closing.

4. **The classmate redeems it** at the counter. The mother serves a coffee she was paid for at step 1.

5. **The classmate thanks.** Two links are offered: *the person who handed it to you* and *the person who paid for it*. She thanks both. The nephew receives a thank addressed to him by name. **The uncle receives a thank addressed to a role he occupies, carrying no obligation and returning no name.**

⭐⭐ **Notice what the classmate's gratitude does at step 5, and how little of it is the instrument's doing.** She is grateful to the nephew because the nephew handed her a coffee. Nothing was transferred to him to make that happen; the uncle's name was simply not there for her gratitude to land on. **The mechanism's entire contribution is an absence, held open long enough for her own attribution to fill it.**

⚠️ **And notice what does not happen.** Nobody is paid. The shop is not paid extra for hosting a relay; the nephew is not paid for passing it on; the uncle receives nothing but a thank he cannot spend. **The instrument moves one coffee and no money beyond the first purchase.**

### 3.3 · An institutional payer

The payer in §3.2 is a person. The same instrument can be issued by a fund that is not one — in this institution, the Aquarian Pool℠, a common fund administered under published rules — and the substitution changes four things. It is specified here at the width of a claim (claim 13) and no further, because it is designed and not built.

**The anonymity stops being a choice and becomes a property.** A person may withhold their name; a fund operating under rules has none to offer. Its instruments carry `from_anonymous` without exception, and what an intermediary, a recipient or a merchant sees is **indistinguishable from an instrument issued by an anonymous individual** — the same record, the same wording, no funded-by label to suppress. §4's inversion reaches its limit case: the payer's absence is total, so the standing that forms in the recipient can only land on the intermediary. ⚠️ The indistinguishability must hold at every layer that carries the payment, not only on the screen: a credit that reaches the merchant's owner by a path only the fund uses identifies the fund as surely as a name would.

**Selection is a draw, not a judgment.** A fund that chose which merchant and which intermediary would be allocating custom and standing by preference. Instead both are drawn over committed rosters by a publicly recomputable procedure; where a published order would itself identify which anonymous instruments were the fund's, the order is sealed during the season and revealed to named verifiers at its end. That procedure is specified in *Decided by No One*, which treats this surface as its sealed regime; this paper claims only that the relay's payer may be seated that way.

**The merchant gives, and is thanked rather than paid.** The fund never buys the good. A merchant whose owner has consented to be in the roster gives it, and the owner is credited at the posted price — the price an individual would have paid, so that the fund's instruments cannot be told apart by amount — in capacity that can only be given onward and is emptied at a periodic reset like every such fund. ⛔ **This is not a chain in which no link ever holds liquid value.** The owner's onward gift from that capacity lands, one hop later, in someone else's ordinary account, where it is spendable; the chain of *this* instrument — fund, intermediary, recipient, merchant — carries no liquid value, and the next gift is another instrument.

**The relay does not die of neglect; it is re-addressed.** For a person, §7's re-minter ends when the payer stops issuing. A fund does not forget, so a lapsed instrument is re-addressed to a **new** intermediary, drawn as the first was, until it is redeemed or the merchant closes. ⛔ It is never re-addressed to an intermediary whose window has already closed on it: sending it back to someone who let it lapse would be a reminder of an omission, and the lapsed intermediary is told nothing. Two consequences follow. The fund's continued re-addressing is exactly the activity on which claim 9 rests, so the instrument is never dormant. And the lapse settlement of claim 11 does not arise for these instruments, because the claim does not lapse to anyone; ⚠️ the price is an outstanding inventory of claims at each merchant with no clock on it, bounded by the number the owner has agreed to hold and settling only because each re-address reaches someone new.

**What the census found, and what survives.** A pre-registered survey on 2026-09-06 (eight queries) attested every leg separately. ⛔ **A rule-bound payer choosing recipients by lot is ordinary**: in October 2020 the People's Bank of China and the Shenzhen municipal government gave 50,000 randomly selected residents 200 digital yuan each, spendable at 3,389 designated outlets between 12 and 18 October. ⭐ It is the most useful **contrast** in the survey, because it is the same issuer-and-lottery shape carrying three properties this instrument refuses: the payer was known and announced, the merchants were paid in money, and the value was bounded by a one-week window. ⛔ **Give-only value is also ordinary**: charity gift cards, sold since 2007 and marketed for client and employee gifts, are spent only by choosing a registered charity to receive them. That is the **near-miss** — give-only, but restricted to charities, where the capacity here may be given to any person. The survivor is the composition of claim 13 and nothing wider: *an anonymous-by-construction fund, drawing merchant and intermediary, thanking the merchant's owner in give-only capacity, and re-addressing on lapse.* ⭐ **The novelty class is composition, and a fund being the payer is a novelty of the actor, never of the mechanism.**

## 4 · The inversion: anonymity that confers rather than protects

This is the paper's narrow claim, and it should be read at exactly this width.

In every use of anonymity the census found — philanthropic, commercial, religious, folk — **the anonymity is protective, and the person it protects is the giver.** They may wish to avoid solicitation, or publicity, or the social weight that a known gift imposes on a recipient; classical treatments of anonymous giving are organised almost entirely around the giver's motive and the recipient's dignity. Anonymity is a shield the giver holds in front of themselves.

Here it does the opposite work. ⭐⭐ **The payer withholds their name so that the intermediary is the one who appears generous.** The nephew hands a friend a coffee; the friend's gratitude has nowhere to land but on the nephew. The uncle's absence is not self-protection — it is the mechanism by which the nephew acquires standing he did not have.

It is worth being precise about what does and does not happen, because the natural description of this is wrong in a way that matters.

⛔ **Nothing is transferred to the intermediary.** The payer does not hand over credit, or reputation, or merit; there is no such quantity moving between them. What happens is that **the payer's name is absent**, and the recipient's own act of attribution — their own gratitude, forming in them, directed at the person in front of them — does the work. The absence is the condition. Nothing crosses.

This is not a fastidious distinction. A mechanism described as *transferring credit* invites a ledger of credit, and a ledger of credit invites the accounting that this instrument exists to avoid: how much was transferred, whether it was enough, whether it can be reclaimed. **Described correctly, there is no quantity to account for.** The design implication is direct: there is no field in the schema for standing, no measure of how generous the intermediary appeared, and nothing anyone can audit or dispute.

⚠️ **The inversion has an ancient folk precedent, and the paper's claim must be stated against it rather than around it.** A parent hands a child a coin to put in the collection plate so that the child is the one who gives. This is widespread, undated, and performs exactly the move described above. **The claim is therefore not that nobody has done this. It is that nobody has built a ledger that does it** — that the move has lived entirely in the space between two people who know each other, and has never been given an instrument that can carry it between strangers, preserve who was involved, and let gratitude reach a person whose name was never said.

⭐ The novelty class is accordingly **instrumentation and cross-domain transposition**, not discovery. That is a defensible class and a modest one, and it is the class the census supports.

## 5 · Why no link may be paid

The unpaid constraint reads like an ethical flourish. It is the load-bearing engineering constraint in the paper, and there are three arguments for it in increasing order of force.

**The doctrinal argument.** A relay that paid its intermediary would be a referral programme, and the value moving to the intermediary would be compensation for propagation rather than a gift. The instrument's whole content is that the intermediary *received the giving*; paying them converts what they received into a job. This argument is sound and is the weakest of the three, because it is available only to a reader who already accepts the frame.

**The structural argument.** Nearly every chain-attribution system in commerce exists in order to pay someone — that is what the attribution is *for*; the exceptions track for analytics. The moment a payment attaches to a link, the chain acquires an optimisation target, and the behaviour that follows is well documented in the multi-level marketing literature (Keep & Vander Nat 2014): recruitment displaces the ostensible purpose, because recruitment is what pays. **An unpaid chain has no upline to enrich and therefore no gradient to climb.** The chain here exists to be *seen*, not to be *settled*, and nothing in it is a claim on anyone.

**The empirical argument, which is the strongest and is not the authors'.** The developmental literature reports that **children offered a reward for performing a kind act are less likely to repeat it** — the overjustification effect, in which an extrinsic incentive displaces the intrinsic motivation it was meant to reinforce (Warneken & Tomasello 2008; Fabes et al. 1989). The intermediary in the founding case is fourteen years old, and the evidence is from young children; the gap is stated in §9. **A relay that paid him would not merely be doctrinally impure; the literature predicts it would reduce the behaviour it exists to produce.**

⭐⭐ **The three arguments converge, and the convergence is the finding worth carrying: the purity condition and the engineering condition are the same condition.** A designer who cared nothing for the doctrine and only for whether the mechanism works would arrive at the same constraint by reading the psychology. That is a coincidence of goods rather than a trade-off between them, and it is the reason the constraint can be stated absolutely rather than balanced against growth.

⚠️ One honest consequence. The instrument is a referral mechanism that pays no referral fee, which means its growth is bounded by how much people want to give rather than by how much they can earn. **This is slower, and the paper does not claim otherwise.**

## 6 · Type, not rule: why the non-redeemability must be structural

The intermediary must not be able to spend the claim. There are two ways to arrange this and they are not equivalent.

**As a rule:** the intermediary *may* redeem but is asked not to. The instrument carries an instruction, perhaps a reminder, perhaps a social expectation. Compliance depends on the intermediary being the sort of person who complies at the moment of temptation.

**As a type:** the instrument in the relayed state **has no redeem operation**. Not a disabled button, not a permission check that could be misconfigured — the operation does not exist on that state.

Apply the diagnostic this institution applies to every guard: **remove the enforcer.** Under the rule, the enforcer is the intermediary's character, and it must be present at the exact moment it is tested — which is the moment nobody can guarantee. Under the type, there is no enforcer, because there is nothing to comply with.

⭐ The difference is not fastidiousness about implementation. It determines whether the census verdict holds. **If the intermediary can redeem, then their passing it on is inspiration — a downstream effect, hoped-for, no part of what was given — and the attested pattern in §2.2 covers the instrument entirely — which is exactly what F2 tests.** The literature is full of anonymous gifts that inspired their recipients to become givers. It contains nothing the authors could find in which the giving *is the content of the gift*. That difference is a single line of code, and it is the whole claim.

⛔ It follows that a redeem path added later "for edge cases" does not degrade the instrument gracefully. **It converts it into a different and unremarkable one.** This should be stated in any implementation's own documentation, because the pressure to add such a path will be real: intermediaries will lapse, and someone will propose letting them keep it.

⭐ **The pressure has a second shape, and it arrives disguised as a different feature.** Suppose the merchant later lets a holder hand a claim back in exchange for credit on an account with the shop — a tab, store credit, a balance. For the recipient that is a harmless convenience. On the relayed state it is a redeem path under another name: the intermediary taking the value onto their own account is exactly the consumption the type forbids. **So conversion is not a separate capability to be permitted or withheld state by state; it is the same capability as redemption and lives exactly where redemption lives.** A state with no redeem operation has no conversion operation to add, and a single exception — convert yes, redeem no — would be a third combination that turns the type back into a rule.

⭐⭐ **The type argument reaches a second object, and there it does not even need a prohibition.** A merchant may publish an **invitation**: a place and an hour it chose — a table, a cart, a boat, at a time — offered to people it does not yet know. Nobody buys it. That single fact settles its relation to money. A claim that was purchased carries a price, and converting it into credit strikes at that price; an invitation carries no purchase price, so a conversion would have nothing to strike at and would issue money-denominated credit that arose from no exchange. The obvious design would forbid the conversion. **The invitation needs no such rule, because the field a conversion reads does not exist on it — conversion is *undefined* by the type, not *forbidden* by a clause.** It is the move of §6 applied to a different object: take the property from the object, and the enforcer has nothing left to enforce.

⚠️ **The census for this object (2026-09-18, pre-registered) killed the loose reading and narrowed the strict one.** A venue publishing a standing, non-convertible invitation is attested: the Chatty Café Scheme, begun in Oldham, England, in 2017, marks tables at which talking to strangers is explicitly welcome, and a national coffee chain rolled such tables out to some 300 stores in 2018. **The two halves of the strict reading are public separately.** Prepaid restaurant reservations bind a place to a time, and are transferable: on at least one platform a guest may *"gift or sell their booking for any amount up to the original purchase price"*, so the booking carries a price that a transfer can realise. Suspended coffee binds a good to a place, carries no time, and is kept from being turned into anything else by the café's practice rather than by the object. What was not found, in that aperture on that date, is the **pair** — a place-and-hour invitation that is non-convertible *by construction* — and that is claim 14's full width. ⛔ Full-text patent classification search did not run for this census, and nothing outside the English-language, US-region index was searched.

⚠️ **A cost must be recorded against this choice.** An instrument the intermediary cannot use may be experienced as a chore rather than a gift — a task with a deadline. The authors' answer is that the intermediary's agency lives in the *addressing* rather than the *consuming*: they choose freely who receives it, and that choice is the substance of what they were given. Whether recipients experience it that way is an empirical question with n=0, and §9 records it as such.

## 7 · The lifecycle, and the one rule that generates it

Each of the three states ends differently, and the differences are generated by a single rule rather than by three policies.

> **A clock runs while the instrument has no addressee — no one to whom it has been given as a gift. It stops the moment it does.**

*Held by* is custody; *addressed to* is ownership in the rule's sense. The payer and the intermediary hold the instrument without being its addressees — the payer bought it to give, the intermediary was given it to give on — and the recipient, to whom it was given as a gift, is its first addressee.

**The re-minter dies of neglect.** If an issued instrument lapses and the payer does not issue again within a re-issue window — a deployment parameter, one cycle by default — the whole thing ends. ⭐ This has an unobvious consequence in its favour: unclaimed-property regimes key on *dormancy*, and an instrument its holder touches on a recurring cycle is never dormant. The mechanism therefore does not bound the escheat exposure — it prevents it from arising. And an instrument that lives only while someone is actively trying to place a gift is honest about mortality: it dies with a payer who dies, forgets, or loses access, within one window.

**The relayed state dies on a window.** An unaddressed occasion held indefinitely is a hoarded occasion. The window is what prevents accumulation, and it is the same instrument the institution uses on its other transient vessels.

**The redeemable state dies with the merchant.** ⭐⭐ This is not a clock. Nothing ticks, nothing is displayed, and the holder is never told they are running out of time. It is a dependency on the counterparty existing, which is how every merchant obligation is bounded: a claim on one coffee from a particular shop is worth nothing once that shop closes. **The instrument does not expire because anyone decided it should; it expires because the thing it claims no longer exists.**

⚠️ **The resulting asymmetry — the intermediary's instrument expires and the recipient's does not — looks like an inconsistency and is not.** The rule is symmetric; the *states* differ. An unaddressed instrument belongs to nobody and is coerced to move; an addressed one is somebody's, and nothing in the design may end it. This distinction is older than the instrument: it is the same line the institution draws between transient communal vessels, which it forces to empty, and personal accounts, which it never touches.

⛔ **Two constraints follow and are stated as constraints rather than as preferences.** First, **remaining time is never rendered**, at any state: a terminal date exists to be reached, not displayed, and a countdown on a gift is a pressure applied to a person who was given something. Second, **an expiry on the redeemable state is forbidden** — that would be a clock imposed on a recipient holding a kindness, which is the one place the design will not bend. A merchant obligation that must terminate should terminate structurally, by the merchant's own closure, not by a timer aimed at the person holding the claim.

**Disclosure rather than process.** Because the redeemable claim depends on the merchant existing, the holder is told so once, at the moment of receipt, in the instrument's own text — *good for one coffee at this shop, for as long as this shop is open.* ⭐ **This is not a caveat but a specification of what the thing is:** a claim on a real place run by real people, whose life is that place's life. It is materially different from corporate scrip, and saying so at receipt costs nothing, whereas discovering it at a closed counter costs everything the instrument was for.

### 7.1 · What the merchant sees, and the one thing they must not

The merchant's position in a relay is unusual: they are paid at step 1, they perform at step 4, and **they have no visibility into and no influence over steps 2 and 3.** The intermediary is not their customer. The recipient is a stranger until they arrive.

They see: relays purchased against their shop, relays redeemed, and — after the fact — relays that lapsed and whose deferred revenue has been recognised. That last is an ordinary accounting entry and there is no reason to hide it.

⛔ **What they must not see is a forward view: no list of outstanding relays, no forecast of what is about to lapse, no breakage projection, and no control that would let them influence whether a relay completes.** The reasoning is not that merchants are untrustworthy. It is that **an incentive with no handle cannot be acted on**, and the cheapest way to guarantee no handle exists is to withhold the number rather than to trust restraint about it. Concretely, the merchant's surface exposes purchased, redeemed, and lapsed-and-recognised records only; there is no query over outstanding instruments, so the forward view is not withheld by policy — it does not exist on the surface.

⚠️ At one shop this is close to redundant — the merchant genuinely cannot reach an intermediary they have never met. At platform scale it is not: a larger operator hosting many merchants will eventually host one with levers, and the guard is written for that case rather than for the founding one: it exists because the lapse-revenue incentive is real at platform scale (§9). ⭐ *A number nobody was shown cannot be optimised, which is a weaker claim than a number that does not exist, and the authors would prefer the stronger one if they could find it.*

### 7.2 · Three designs for unredeemed value, and the road not taken

Every gift instrument must say what happens to value that is never collected. The direct tier (§2.5) shows three answers in live use, and they create three different incentives.

```
 design                       who                          what it makes someone want
 ─────────────────────────────────────────────────────────────────────────────────────────────
 BREAKAGE — value forfeits    the gift-card industry;      the issuer or merchant profits
   to issuer or merchant      a no-refund gift code         when the gift fails
 SENDER-REFUND on a short     a gift app: 7 days, then     honest with the money — but a
   clock                      the full amount refunded      clock runs on the recipient
 COUNTERPARTY-DISSOLUTION,    this instrument (§7): a      the merchant benefits when a
   no clock, no forward view  recipient's claim ends only   relay is never placed, and is
                              with the merchant             shown no gradient (§7.1, §9)
 ─────────────────────────────────────────────────────────────────────────────────────────────
```

The first road is the one §9 argues this instrument's lapse settlement is not, while conceding that it leaves the merchant a similar incentive; §7.1 is the mitigation. The third is this paper's. **The second deserves an answer, because it is the one a reader sympathetic to the design would propose:** return the money to the payer, recognise nothing, and the merchant never benefits from a failure.

⛔ **It is not taken, for two reasons, and the second is the stronger.** First, a refund on a short window is a clock on a person holding a kindness — the exact thing §7 forbids on the redeemable state — and a week is short enough to work as pressure however it is worded. Second, **a refundable gift has not been given.** If lapse returns the value to the payer, then what the payer bought was a deposit held on the recipient's behalf, revocable by time, and the gift was never the recipient's. It is the same invariant that makes the re-minter's re-issued instrument a relayed one rather than a redeemable one: a payer who could get the value back, by consuming or by refund, turns the instrument into a refundable deposit. The instrument therefore keeps the one road on which the value, once given, never returns to the giver — and accepts, in §9, the incentive that road leaves the merchant.

## 8 · Why the chain is bounded at two

The relay is bounded: an intermediary passes to a recipient, and the recipient may redeem. They cannot pass another relayed instrument onward.

⚠️ **This is a real limitation and the paper does not disguise it as a virtue.** An unbounded version — each recipient becoming the next intermediary — is closer to the pay-it-forward ideal and would produce a longer chain. It also produces an instrument that **nobody may ever consume**: a hot potato whose terminal state never arrives, and a gift that cannot be received has stopped being one. Bounding it at two is the shortest length at which the mechanism's actual content — *making someone a giver* — is delivered at all.

⭐ The consequence for the surrounding theory is that **this instrument is not the unbounded forward-chain**, and any paper that describes it as such has borrowed a property it does not have. Unbounded circulation exists elsewhere in the architecture, in instruments whose forward-spendability has no depth limit. This one is a short relay with a designed terminus, and it should be classified as one.

## 9 · Honest limitations and open questions

**The censuses are desk surveys.** Four of them, tabulated in the Prior-Art and Non-Assertion Statement: marketing copy, published terms, secondary literature and web-indexed patents, through a US-region index. None is fieldwork and none is exhaustive; one was not pre-registered; full-text patent classification search did not run for the last, and no survey is recorded as having searched outside English — including the language of the market the instrument is built for. Every census on this instrument has returned less than the authors proposed; a reader with better search should assume each surviving composition is attested too until shown otherwise.

**n = 0.** No instrument described here has been operated with real participants. Every behavioural claim — that intermediaries experience the addressing as agency, that recipients find the chain meaningful rather than intrusive, that anonymity reads as generosity rather than as evasion — is untested.

**The overjustification finding is borrowed and not replicated.** §5's strongest argument rests on a literature the authors have read and not tested, in a population and culture different from the one the instrument is built for — the strongest studies are of children under six, and the founding intermediary is fourteen.

**The founding use case satisfies the paper's own caution only partly, and the split is not where it first appeared.** §2.3 reports that parent-directed generosity projects perform worse than child-led ones. An earlier version of this section called the founding case *the directed pattern the literature warns about*. That is true of one shape of the instrument and unproven of another, and it was never true of the shapes in which the child gives nothing.

An adult can put an instrument in a young person's hands in four shapes — a gift *to* them, named or anonymous, and a relay *through* them, named or anonymous:

```
                      the adult's name shown          the adult's name withheld
                   ─────────────────────────────────────────────────────────────────
 a gift TO them    1 · no giving of theirs to direct  2 · no giving of theirs to direct
                       → outside the warning              → outside the warning
 a relay THROUGH   3 · "my uncle gave me this to      4 · "I have something to give,
   them                pass on" — a named adult           and I choose who" — no adult
                       assigned it → the warning          in the frame → the warning's
                       applies                            mechanisms have nothing to act on
                   ─────────────────────────────────────────────────────────────────
```

⭐ **Shapes 1 and 2 are exempt for the plainest reason: the warning concerns an adult directing how a child *gives*, and a gift to the child involves no giving of the child's to direct.** Shapes 3 and 4 share what the warning is about — in both, an adult decides whether an instrument exists and when, and only the addressing is the young person's — so relay-versus-gift is not the axis. **The axis is whether the direction is perceivable.** Every candidate mechanism for why directed giving underperforms — the child experiencing compliance rather than agency, the generosity being attributed to the adult, an external locus of causality — requires the child to *perceive* an adult directing. In shape 4 there is no adult to perceive. The founding case of §3.2 is shape 4.

⛔ **This is a mechanistic reading, not a finding, and it must not be stated as an exemption.** The literature studied parent–child generosity projects, not anonymous instruments; n = 0. And one objection survives anonymity untouched: **the task is still externally originated.** The young person did not seek it; something arrived asking them to give. What anonymity removes is the person to attribute the direction to, not the assignment. The reading is registered as a prediction in the institution's public register, **P-BG2**: sustained pass-on is higher for the anonymous relay (shape 4) than the named one (shape 3), over a window long enough for the effect to appear; its null — equal rates, or the named relay ahead — would mean the anonymity is doctrinal only, and would count against offering the named relay to minors. Shapes 1 and 2 are controls, not arms, since they contain no giving by the intermediary. The obvious further repair — letting the intermediary request instruments, or draw from a standing allowance — has not been implemented. It is recorded here rather than resolved.

**The unpaid constraint is untested against growth.** A mechanism that pays nobody grows only as fast as people want to give. Whether that rate is sufficient to sustain the merchants it depends on is unknown.

**The institutional payer and the invitation are designs, not deployments.** Neither has been built. Claim 13's anonymity by construction holds only if the fund's credits reach an owner by the same path an anonymous individual's do, which is a property of payment infrastructure not yet chosen; its draw depends on a separate specification; and its re-addressing leaves each participating merchant holding an inventory of claims with no clock, which settles only on the expectation that a fresh intermediary eventually places each one. Claim 14 rests on a single field's absence, and a later schema that gave the invitation a price for any reason — a deposit, a no-show fee — would reintroduce the conversion it makes undefined. Both are stated here so that their failure modes are public before their first use.

**The lifecycle's legal availability is untested.** Expiration, closure as termination of the obligation, escheat, and revenue recognition on lapse all vary by jurisdiction — unclaimed-property statutes differ state by state, breakage guidance under ASC 606 has its own conditions, and some jurisdictions treat a merchant's closure as extinguishing nothing — and none of it has been tested with counsel. §7's arguments that a recurring cycle prevents dormancy from arising and that an item-denominated claim is not a stored monetary balance are plausible; **claims 8 through 11 are design positions until counsel in the jurisdiction that matters says otherwise.** §2.5 sharpens the question rather than answering it: the same product ships as a merchant stored-value pass, as a bank-issued prepaid card, and as an order paid only at redemption, and different bodies of law plausibly attach to each — the last arguably outside gift-card rules altogether. Which of these shapes this instrument is — and whether the order-paid-at-redemption shape, the one furthest from stored value, can survive a claim that lives for as long as the merchant does — is for counsel.

**The lapse settlement is an accounting position, not a neutral fact.** When a relay ends unclaimed, the merchant's deferred revenue is recognised. The authors argue this is not breakage — a gift card sells stored value and the issuer profits from the customer forgetting, whereas here a specific good was sold, capacity was held, and only collection lapsed, extinguished by the one party with standing to direct it. ⚠️ **The argument is sound and the incentive it creates is still real**: the merchant benefits when a relay fails. The mitigation specified is informational rather than motivational — **no forward view of pending lapses is exposed to the merchant**, on the reasoning that a gradient with no handle cannot be climbed. At a single shop this is adequate. At platform scale, hosting merchants who do have levers, it is a guard the authors would not want to rely on alone.

### 9.1 · What would falsify this, stated in advance

The authors prefer claims that can be killed. Six are registered here, before any deployment — four at first publication and two at the 2026-09-23 revision.

**F1 — the prior-art claim.** A single attested instrument carrying all four properties *and* the inversion — anonymity used to confer standing on an intermediary, in a system that records the chain and pays no one. ⛔ **One instance and §4 is withdrawn**, not narrowed.

**F2 — the type-versus-rule claim.** §6 asserts that permitting the intermediary to redeem collapses the instrument into the attested inspiration pattern. This is falsified if a deployment in which redemption is *permitted but discouraged* produces the same pass-on rate as one in which it is *impossible*. ⭐ **That is a cheap A/B test and the authors have not run it.** If the rates match, the type/rule distinction is philosophy rather than engineering, and the paper's central mechanism is decoration on a social norm.

**F3 — the unpaid claim.** §5 argues that paying the intermediary would reduce the behaviour. Falsified if a paid arm shows equal or higher sustained pass-on rates over a period long enough for the overjustification effect to appear, which the literature suggests is longer than a single trial.

**F4 — the substrate-cost claim inherited from §7.** The lifecycle machinery is asserted to be a consequence of the gift being an object rather than a signal. Falsified if a signal-substrate givable in the same institution turns out to require comparable governance — which would mean the machinery is a property of the design's taste rather than of the substrate.

**F5 — the anonymity-as-escape reading of §9.** Registered publicly as P-BG2 (§9): falsified if the anonymous relay's sustained pass-on rate does not exceed the named relay's. A null would not touch claim 5, which concerns standing rather than developmental effect; it would withdraw §9's suggestion that anonymity also answers the directed-giving caution.

**F6 — the type claim for the invitation (claim 14).** Falsified by one attested instrument, predating this revision, that offers a place and an hour, is bought by no one, and is non-convertible because it carries no price to convert rather than because a rule forbids it. ⛔ One instance and claim 14 is withdrawn.

⚠️ **Note what is not on this list: whether anyone likes the instrument.** Adoption failure would not falsify any claim above; it would mean the mechanism is correct and unwanted, which is a different result and should not be reported as this one.

## 10 · Why this matters now

Gifting is being instrumented rapidly, and the instruments being built are stored-value instruments with attribution attached. The economics of that design are well understood: the issuer's interest runs toward non-redemption, the attribution exists to compensate propagation, and the resulting products optimise for recruitment because recruitment is what pays.

This paper describes a small alternative and gives it away. **Its distinguishing properties are all subtractions** — no stored value, no payment to any link, no redeem operation on the relayed state, no forward view of pending lapses, no measure of standing. What remains is an instrument whose only content is that someone who had nothing to give was placed in the position of giving, and whose only record is who was involved.

The transposition was not found in the patent literature in the apertures stated above, and the adjacent families of §2.4 are named for what they disclose. It is published here so that it stands as prior art against anyone who would later enclose it.

## 11 · Cross-venue references

This paper depends on and extends: *The Gift Operation* (the receive-→-give-forward atom, its six topologies, and the conserved-identity subclass this instrument instantiates); *Dual-Currency Reciprocity* (the vessels whose emptying rules §7 borrows); *The Four Elements as a Breadth-Check Discipline* (the substrate ladder from which §5's governance reasoning descends). At the 2026-09-23 revision it also depends on *Decided by No One* (the called draw, whose sealed regime seats claim 13's selection of merchant and intermediary) and *Manufactured Universal Giving* (the argument for a fund that funds people's capacity to give, which states the same composition from the fund's side; §3.3 states it from the instrument's). The first three do not cite this paper; the last two do; it assumes all five.

### 11.1 · Sources for the 2026-09-23 revision

Each was opened at its source on 2026-09-23 before it was cited.

- US 10,510,057 B2, *Token-based gift cards* — the granted patent as published by the USPTO: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10510057
- spot, Terms of Service, effective 24 August 2026: https://usespot.me/terms
- OneOnMe, Non-Reloadable Virtual Visa Gift Card: https://oneonme.com/virtual-visa-gift-card
- Klink-iT, Terms of Service, last updated 30 January 2024: https://www.klink-it.com/terms
- Travel Bug (geocaching trackables): https://en.wikipedia.org/wiki/Travel_Bug · https://www.geocaching.com/track/travelbugs.aspx
- Shenzhen digital-yuan red-packet lottery, October 2020: https://www.nfcw.com/2020/10/12/368565/pboc-distributes-digital-currency-to-consumers-via-red-envelope-lottery/ · https://www.ledgerinsights.com/china-central-bank-digital-currency-cbdc-ecny-giveaway-results/
- TisBest charity gift cards: https://www.tisbest.org/ · https://www.prnewswire.com/news-releases/tisbest-philanthropy-celebrates-15th-anniversary-as-driver-of-over-54-million-in-charitable-giving-301687902.html
- Tock, *Transferring a Reservation*: https://tock.zendesk.com/hc/en-us/articles/360031260491-Transferring-a-Reservation
- Chatty Café Scheme: https://en.wikipedia.org/wiki/Chatty_Caf%C3%A9_Scheme · https://www.huffingtonpost.co.uk/entry/chatty-cafe-costa-becomes-first-uk-chain-to-roll-out-scheme-tackling-loneliness_uk_5b684d2fe4b0fd5c73dbb25a

## Coda

The mechanism is one line long, stated as a subtraction: **remove the redeem operation from the middle of the chain.**

Everything else in this paper — the anonymity that confers rather than protects, the payment that must not happen, the clock that runs only while nobody has been given the thing — follows from taking that one subtraction seriously and refusing to reinstate it when it becomes inconvenient.

A gift that its holder cannot use is not a lesser gift. It is a different one, and it is the only kind that can make a person a giver rather than a recipient. *The uncle's absence is not a modesty. It is the whole of what he gave.*

---

*Miss Aquarius℠ is the consistent name under which this institution discloses AI collaboration; the underlying models are not named. License: CC0 1.0 Universal. Trademark rights in HeartBank®, B-Gift℠, B-ReGift℠, B-Stamp™, B-Seal™, Re-Tip Jar℠, Re-Tip Fund℠, Personal Account℠, Personal Wallet℠, Aquarian Pool℠ and Miss Aquarius℠ are reserved separately by the authors and are not licensed by this publication. This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
