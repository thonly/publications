---
title: "The Unpaid Relay"
subtitle: "A gift instrument whose chain of custody survives the pass and is thankable at every link, whose anonymity is generative of the intermediary's standing rather than protective of the giver's privacy, and in which no link is ever paid — because paying one would destroy the behaviour the instrument exists to produce."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-b
status: draft
date: 2026-09-04
revised: 2026-09-05
license: CC0-1.0
slug: the-unpaid-relay
venue: thonly.org/research/the-unpaid-relay (canonical)
---

## Preamble

This paper specifies one small instrument: a gift code that is given to a person who cannot spend it, so that they may give it to someone who can.

It is published defensively. The mechanism is buildable from this description, it sits in a space where adjacent commercial actors file patents routinely — chain-of-custody tracking, referral attribution, loyalty and gifting platforms — and the institution that designed it intends never to assert exclusivity over it. The specification is therefore given in full rather than sketched, and the claims are stated as claims rather than as marketing.

⚠️ It is also published with a negative result attached, and the negative result is nearly as important as the specification. A prior-art census was run *before* this paper was queued, against a four-part claim, and **every one of the four parts turned out to be attested somewhere in existing practice** — including the part the authors predicted would survive. §2 reports that census honestly, including the prediction that failed and why the reasoning behind it was wrong. What remains after the census is narrow, and §4 states it at exactly the width the evidence supports and no wider.

Pending review: economic anthropologists (the Maussian question of whether a relayed gift is one gift or two); developmental and social psychologists (the overjustification finding §5 leans on, which the authors have not replicated); practitioners in charitable gifting and unclaimed-property law (§7); and readers inclined to test whether the anonymity inversion in §4 is genuinely unattested or merely unsearched.

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it cannot later be enclosed. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control.

Trademark rights in specific marks — HeartBank®, B-Gift℠, B-ReGift℠, B-Stamp™, B-Seal™, Re-Tip Jar℠, Re-Tip Fund℠, Personal Account℠, Personal Wallet℠, Aquarian Pool℠, Miss Aquarius℠ — are reserved separately and are not licensed by this publication. **The mechanism is free; the names are not.** A reader may build every instrument in this paper and must call it something else.

The authors assert no novelty over: the pay-it-forward tradition in any of its documented forms; suspended coffee; charity gift cards and donor-advised instruments; anonymous giving through a named intermediary as practised in philanthropy; chain-of-custody and provenance tracking in supply chains, evidence handling, or data lineage; or referral and multi-level attribution systems. §2 documents each of these as prior art and locates precisely which of this paper's four claims each one defeats.

## Abstract

A gift instrument is specified in which a payer purchases a claim on a specific good and directs it not to a recipient but to an **intermediary who cannot redeem it**. The intermediary's only available action is to pass it onward; on passing, the instrument converts into an ordinary redeemable claim held by whoever received it. The chain — payer, intermediary, recipient — is preserved and visible to every party, and every party in it can be thanked, including a payer whose name has been withheld.

Four properties are specified. Three are individually attested in existing practice and are claimed only in combination: chain visibility, name-withheld-but-chain-preserved anonymity, and thankability at every link. The fourth — that no link is ever paid — is also attested, in the non-commercial pay-it-forward genre, and the paper's original prediction that it would be the novel one was wrong.

**What survives the census is the *purpose* of the anonymity.** In every attested case, a giver's anonymity protects the giver: they wish not to be known. Here it does the opposite work. The payer withholds their name **so that the intermediary is the one who appears generous** — the anonymity is *generative of a third party's standing* rather than *protective of the giver's privacy*. The paper argues that this inversion has an ancient folk precedent (a parent handing a child money for the collection plate), that it has no instrumented precedent the authors could find, and that instrumenting it requires the non-redeemability to be enforced by the instrument's *type* rather than by the intermediary's character.

The paper further argues that the unpaid constraint is a design necessity rather than a preference: the developmental literature reports that offering a child a reward for a kind act makes repetition *less* likely, so a relay that paid its intermediary would corrode the behaviour it exists to produce. Finally it specifies a three-state lifecycle in which every expiry is generated by one rule — *a clock runs while the instrument has no addressee — no one to whom it has been given as a gift — and stops the moment it does* — and shows why the resulting asymmetry, in which the intermediary's instrument expires and the recipient's does not, is the correct shape rather than an inconsistency.

## Claims

*Enumerated at drafting. A defensive publication works by **disclosure**, and a claims list is what an examiner or opposing counsel searches; the prose that establishes each claim is cited beside it. **No claim below adds matter not present in the body**, and the prior art runs from this document's publication date and its independent timestamp, not from this list.*

1. **A gift instrument whose intermediate holder has no redeem operation** — a claim on a specific good, issued to a party who cannot present it to the merchant, whose only available operation is to transfer it onward, and which becomes redeemable only in the hands of the party to whom that transfer is made. ⭐ **The non-redeemability is a property of the instrument's state rather than a policy applied to a holder** — there is no permitted-but-discouraged redemption path. (§3, §6.)

2. **State-derived lifecycle for such an instrument** — three states (issuable, relayed, redeemable) derived from which participant fields are populated rather than stored as an independent status flag, so that the state and the chain cannot disagree. (§3.1.)

3. **Chain preservation with selective name suppression** — a record carrying both the paying party and the transferring party, in which the *identity* of the payer may be suppressed while the *existence and shape of the chain* is disclosed to every party, and in which suppression is a property of the record rather than of any single pairwise relationship, and is never partially lifted. (§3, §4.)

4. **Role-addressed gratitude** — gratitude messages addressed to a **position in a chain** (the party who paid; the party who transferred) and resolved to an identity only at delivery, permitting a party whose name is suppressed to receive gratitude without the name becoming available to the sender. (§3.1.)

5. **Anonymity applied to confer standing on a third party** — withholding the payer's identity for the purpose of causing the transferring party to be perceived as the giver, as distinct from the attested use of anonymity to protect the giver, and distinct from honorary giving, where the honoree is named as such — here the intermediary is perceived by the recipient as the giver. ⭐ **The perceived standing is not represented as a stored quantity, is not transferred, and has no field in the record.** (§4.)

6. **A propagation chain in which no participant receives compensation for propagating** — no referral fee, commission, discount, credit, or preferential treatment accrues to any party for issuing, transferring, or receiving, and the absence is specified as a constraint on the mechanism rather than as a business preference. (§5.)

7. **Bounded relay depth with a designed terminal state** — a chain fixed at exactly one intermediate transfer, adopted so that the instrument reaches a party who may consume it rather than propagating indefinitely. (§8.)

8. **A single expiry rule keyed on addressedness** — *a duration runs while the instrument has no addressee — no one to whom it has been given as a gift — and ceases when it has one* — from which the differing terminal conditions of the three states are derived rather than separately specified, and under which a redeemable instrument held by a recipient carries no duration at all. (§7.)

9. **Issuance capability terminated by holder inactivity** — the payer's ability to re-issue after a lapse expires a fixed interval (a deployment parameter, one cycle by default) after the most recent lapse, so that the instrument's existence depends on continued activity by its originator. ⭐ **The instrument is consequently never dormant**, which is the condition on which unclaimed-property obligations attach. (§7.)

10. **Terminal dependency on merchant existence, disclosed at receipt** — a redeemable claim bounded by the continued operation of the issuing merchant rather than by any imposed duration, with that dependency stated in the instrument's own text at the moment of receipt rather than announced at closure — the terminal condition itself is the Philippine Gift Check Act's (2017) rule; the disclosure at receipt is what is claimed. (§7.)

11. **Settlement of an unclaimed relay as recognised revenue on an item-denominated basis** — recognition of deferred revenue on lapse, on the basis that a specific good was sold and only its collection lapsed, distinguished from stored-value instruments in which the customer's own unspent balance is retained. (§7, §9.)

12. **Suppression of forward lapse visibility from the merchant** — withholding from the merchant any prospective view of instruments approaching lapse, including counts, lists, forecasts, and any control affecting completion, as a structural measure against an incentive the merchant would otherwise hold. (§7.1.)

⚠️ **Claims 5 and 6 are the ones the authors believe are unattested in combination; claims 1 through 4 and 7 through 12 are enumerated for completeness of disclosure and several have close prior art documented in §2.** The purpose of this list is to prevent enclosure, not to assert priority.

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

What the census *could* not find is narrower than any of the four legs, and §4 is devoted to it: **an instrument in which the anonymity exists in order to confer standing on a third party.** In every attested case — philanthropic, commercial, or folk — anonymity protects the giver. The inversion appears not to be instrumented.

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
 the collection-plate coin    ·         ✓         ·         ✓         ✓
                           ───────────────────────────────────────────────
 THIS INSTRUMENT              ✓         ✓         ✓         ✓         ✓

   ✓ present   · absent   ~ partial   ⛔ inverted (payment is the point)
```

⚠️ **Two rows deserve comment because they are the ones that nearly close the claim.**

**Anonymous giving through a named intermediary carries all four.** A donor routes a gift through an advisor whose identity is documented, the chain is legible, the recipient thanks through the intermediary, and nobody is paid. ⛔ **On the four stated properties this is a hit, and the authors record it as one.** What it lacks is the fifth column: the donor's anonymity is *protective*, and the advisor is a conduit rather than a beneficiary of standing. Nobody in that arrangement is trying to make the advisor look generous.

**The collection-plate coin carries the inversion and nothing else.** A parent hands a child a coin so the child is the one who gives; the anonymity — such as it is — exists precisely to confer the act on the child. ⭐ **This is the true precedent, and it is widespread and undated.** What it lacks is instrumentation: it works only between people who already know each other, it preserves no record, and gratitude cannot reach a payer who was never named because there is no channel by which it could.

⭐⭐ **The claim is the bottom row and nothing above it.** Every column has been done. The combination, and specifically the combination of the fifth column with an instrument that can carry it between strangers, is what the census could not attest.

### 2.4 · The adjacent literature this paper does not claim to extend

Malinowski's account of the *kula* (1922), taken up by Mauss (1925), describes conserved objects circulating through a chain with their history intact, and Hyde's argument that the gift must always move is the best-known statement of the norm this instrument mechanises. **Neither is being extended here.** The idea that a gift ought to keep moving is roughly a century old in the anthropological literature and considerably older in practice; what this paper offers is not that observation but a mechanism in which the alternative to passing has been removed from the instrument, so that the norm does not depend on anyone honouring it.

One lineage note belongs here rather than in the body, because this is a mechanism paper and not a doctrinal one. The Pāli canon grades giving by the giver's motive (AN 7.52, the *Dānamahapphala Sutta*, lists seven), and ranks *giving with expectation of return* lowest. ⭐ The instrument does not ask anyone to give without expectation; **it removes the object of the expectation**, since a withheld name has nothing that can return to it and no link is paid. The authors note the correspondence and claim nothing from it: the mechanism stands or falls on §5's three arguments, of which the empirical one is the strongest and is not doctrinal at all.

Chain-of-custody instrumentation is dense in the patent literature for goods, evidence, data lineage and supply chains. The authors found none directed at a gift instrument. That gap is the reason this paper is a defensive publication rather than a note: the transposition is unclaimed so far as six queries show, and is exactly the sort of thing an adjacent loyalty or fintech actor would file.

Adjacent patent families found at the 2026-09-05 revision, each named against the claim it touches. WO 2012/037178 A2 (Mankoff, priority 2010) transfers a virtual gift with an acceptance period followed by a redemption period — state-dependent timing, the nearest relative of claim 8, though there both periods are clocks on the recipient. WO 2016/057643 A1 (Soniram, priority 2014) and US 2006/0033326 A1 (priority 2004) route a thank-you to a gift's giver through a platform or a returnable note — the nearest relatives of claim 4, neither addressing a role nor withholding the giver's name. US 2013/0197983 A1 (Vel, priority 2012) tracks referral chains and compensates them — claim 7's shape with the payment this paper forbids. The Philippine Gift Check Act (Republic Act 10962, 2017) makes a gift check *valid until the cessation of business of the issuer* — claim 10's terminal condition nearly verbatim, so that what claim 10 adds is only the disclosure at receipt. Anonymous tribute giving *in honour of* a named third party, with notification, is claim 5's nearest relative; it differs in that the honoree is named as such, where here the intermediary is perceived by the recipient as the giver. The adjacent families are named so that a reader with better search starts where we stopped.

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

## 8 · Why the chain is bounded at two

The relay is bounded: an intermediary passes to a recipient, and the recipient may redeem. They cannot pass another relayed instrument onward.

⚠️ **This is a real limitation and the paper does not disguise it as a virtue.** An unbounded version — each recipient becoming the next intermediary — is closer to the pay-it-forward ideal and would produce a longer chain. It also produces an instrument that **nobody may ever consume**: a hot potato whose terminal state never arrives, and a gift that cannot be received has stopped being one. Bounding it at two is the shortest length at which the mechanism's actual content — *making someone a giver* — is delivered at all.

⭐ The consequence for the surrounding theory is that **this instrument is not the unbounded forward-chain**, and any paper that describes it as such has borrowed a property it does not have. Unbounded circulation exists elsewhere in the architecture, in instruments whose forward-spendability has no depth limit. This one is a short relay with a designed terminus, and it should be classified as one.

## 9 · Honest limitations and open questions

**The census is a desk survey.** Six queries, marketing copy, secondary literature. It is not fieldwork and it is not exhaustive. Four of four legs came back attested; a reader with better search should assume the combination is attested too until shown otherwise.

**n = 0.** No instrument described here has been operated with real participants. Every behavioural claim — that intermediaries experience the addressing as agency, that recipients find the chain meaningful rather than intrusive, that anonymity reads as generosity rather than as evasion — is untested.

**The overjustification finding is borrowed and not replicated.** §5's strongest argument rests on a literature the authors have read and not tested, in a population and culture different from the one the instrument is built for — the strongest studies are of children under six, and the founding intermediary is fourteen.

**The founding use case does not fully satisfy the paper's own caution.** §2.3 reports that parent-directed generosity projects perform worse than child-led ones. In the founding case the payer decides when instruments are issued and how many; only the addressing is the intermediary's. **This is the directed pattern the literature warns about**, and the obvious repair — letting the intermediary request instruments, or draw from a standing allowance — has not been implemented. It is recorded here rather than resolved.

**The unpaid constraint is untested against growth.** A mechanism that pays nobody grows only as fast as people want to give. Whether that rate is sufficient to sustain the merchants it depends on is unknown.

**The lifecycle's legal availability is untested.** Expiration, closure as termination of the obligation, escheat, and revenue recognition on lapse all vary by jurisdiction — unclaimed-property statutes differ state by state, breakage guidance under ASC 606 has its own conditions, and some jurisdictions treat a merchant's closure as extinguishing nothing — and none of it has been tested with counsel. §7's arguments that a recurring cycle prevents dormancy from arising and that an item-denominated claim is not a stored monetary balance are plausible; **claims 8 through 11 are design positions until counsel in the jurisdiction that matters says otherwise.**

**The lapse settlement is an accounting position, not a neutral fact.** When a relay ends unclaimed, the merchant's deferred revenue is recognised. The authors argue this is not breakage — a gift card sells stored value and the issuer profits from the customer forgetting, whereas here a specific good was sold, capacity was held, and only collection lapsed, extinguished by the one party with standing to direct it. ⚠️ **The argument is sound and the incentive it creates is still real**: the merchant benefits when a relay fails. The mitigation specified is informational rather than motivational — **no forward view of pending lapses is exposed to the merchant**, on the reasoning that a gradient with no handle cannot be climbed. At a single shop this is adequate. At platform scale, hosting merchants who do have levers, it is a guard the authors would not want to rely on alone.

### 9.1 · What would falsify this, stated in advance

The authors prefer claims that can be killed. Four are registered here, before any deployment.

**F1 — the prior-art claim.** A single attested instrument carrying all four properties *and* the inversion — anonymity used to confer standing on an intermediary, in a system that records the chain and pays no one. ⛔ **One instance and §4 is withdrawn**, not narrowed.

**F2 — the type-versus-rule claim.** §6 asserts that permitting the intermediary to redeem collapses the instrument into the attested inspiration pattern. This is falsified if a deployment in which redemption is *permitted but discouraged* produces the same pass-on rate as one in which it is *impossible*. ⭐ **That is a cheap A/B test and the authors have not run it.** If the rates match, the type/rule distinction is philosophy rather than engineering, and the paper's central mechanism is decoration on a social norm.

**F3 — the unpaid claim.** §5 argues that paying the intermediary would reduce the behaviour. Falsified if a paid arm shows equal or higher sustained pass-on rates over a period long enough for the overjustification effect to appear, which the literature suggests is longer than a single trial.

**F4 — the substrate-cost claim inherited from §7.** The lifecycle machinery is asserted to be a consequence of the gift being an object rather than a signal. Falsified if a signal-substrate givable in the same institution turns out to require comparable governance — which would mean the machinery is a property of the design's taste rather than of the substrate.

⚠️ **Note what is not on this list: whether anyone likes the instrument.** Adoption failure would not falsify any claim above; it would mean the mechanism is correct and unwanted, which is a different result and should not be reported as this one.

## 10 · Why this matters now

Gifting is being instrumented rapidly, and the instruments being built are stored-value instruments with attribution attached. The economics of that design are well understood: the issuer's interest runs toward non-redemption, the attribution exists to compensate propagation, and the resulting products optimise for recruitment because recruitment is what pays.

This paper describes a small alternative and gives it away. **Its distinguishing properties are all subtractions** — no stored value, no payment to any link, no redeem operation on the relayed state, no forward view of pending lapses, no measure of standing. What remains is an instrument whose only content is that someone who had nothing to give was placed in the position of giving, and whose only record is who was involved.

The transposition is unclaimed in the patent literature so far as six queries and the adjacent families of §2.4 show. It is published here so that it remains so.

## 11 · Cross-venue references

This paper depends on and extends: *The Gift Operation* (the receive-→-give-forward atom, its six topologies, and the conserved-identity subclass this instrument instantiates); *Dual-Currency Reciprocity* (the vessels whose emptying rules §7 borrows); *The Four Elements as a Breadth-Check Discipline* (the substrate ladder from which §5's governance reasoning descends). It is cited by neither and assumes both.

## Coda

The mechanism is one line long, stated as a subtraction: **remove the redeem operation from the middle of the chain.**

Everything else in this paper — the anonymity that confers rather than protects, the payment that must not happen, the clock that runs only while nobody owns the thing — follows from taking that one subtraction seriously and refusing to reinstate it when it becomes inconvenient.

A gift that its holder cannot use is not a lesser gift. It is a different one, and it is the only kind that can make a person a giver rather than a recipient. *The uncle's absence is not a modesty. It is the whole of what he gave.*

---

*Miss Aquarius℠ is the consistent name under which this institution discloses AI collaboration; the underlying models are not named. License: CC0 1.0 Universal. Trademark rights in HeartBank®, B-Gift℠, B-ReGift℠, B-Stamp™, B-Seal™, Re-Tip Jar℠, Re-Tip Fund℠, Personal Account℠, Personal Wallet℠, Aquarian Pool℠ and Miss Aquarius℠ are reserved separately by the authors and are not licensed by this publication. This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
