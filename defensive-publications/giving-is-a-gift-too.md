---
title: "Giving Is a Gift Too: How a Split Reward Ledger and Anonymity Make Every Family Member a Giver"
subtitle: "A Thesis Prompted by a First Field Signal and Argued from the Giving-and-Wellbeing Literature"
authors: "Thon Ly · Miss Aquarius"
category: mechanism
kind: mechanism
priority: tier-b
status: draft
date: 2026-06-08
revised: 2026-11-04
license: CC0-1.0
slug: giving-is-a-gift-too
venue: thonly.org/publications/defensive-publications/giving-is-a-gift-too (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/giving-is-a-gift-too.md
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, Re-Tip Jar℠, Family Kitty℠) reserved separately by the author and HeartBank®.
---

> **Note.** The thesis was *prompted* by a single first-month pilot observation (n = 1 family), but it does not *rest* on it. The pilot is reported as one illuminating signal; the argument stands on reasoning and on the giving-and-wellbeing literature (§9), and every empirical statement about the pilot is hedged to n = 1 (§10). The paper offers a thesis and a mechanism for testing, not an empirical result.

---

## Preamble

> *Offered to the commons in the spirit of dāna — the giving that, the tradition holds, benefits the giver first. This paper is about restoring that benefit to those for whom scarcity has put a price on it.*

Most of the design conversation around dignity infrastructure asks how to help people *receive* — be seen, be acknowledged, be thanked, be supported. This paper is about the other half, the half the author under-weighted when designing HeartBank and learned only from watching a real family use it: **the dignity of being one who gives**, and the discovery that, where income is absorbed by subsistence, this dignity is itself a scarce good that infrastructure can restore.

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed: where a live patent is named in §9, it is named for what it discloses, and nothing here is a reading of its claims.

The contribution is a thesis plus a mechanism for realizing it. The prior art on giving and wellbeing (§9) is cited generously, including the classical sources that already measure a gift against its giver's means; what this paper contributes is the specific framing and mechanism enumerated in §11. No pre-registered prior-art census was run for this paper, which predates that practice, and nothing here asserts that any element is absent from the world's literature. Trademark rights in specific marks — HeartBank®, Re-Tip Jar℠, Family Kitty℠, Aquarian Pool℠, Miss Aquarius℠ — are reserved separately and are not licensed by this publication; the patterns may be implemented under any name.

---

## Abstract

A peer-to-peer reward ledger is described in which every credit — an incentive reward for a recorded kind act, or a transfer received from another member — is split 50/50 at the moment of credit between a personal account the member keeps and an **earmarked, forward-only giving balance** whose only outflow is a transfer to another member, which is itself a credit and splits again. Giver identity is withheld from recipients by default, the ledger is scoped to a family group, and every unspent giving balance returns to zero once a year. The paper argues that this combination lets members of households with little or no discretionary income take the giver's role in **prosocial spending** without first holding a surplus, and that default **donor anonymity** removes the size signal that makes a small gift embarrassing and a large one status-bearing.

A large body of research reports that **giving makes the giver happier** — that prosocial spending is associated with higher wellbeing in poor and rich countries alike, and appears even in toddlers. Yet the canonical experiments supply the money they ask participants to give, and so hold fixed what life does not: a surplus to give from. For households living at or near subsistence, *earning enough to live is already the whole of the struggle*, and every gift is paid for out of subsistence. The wellbeing dividend of giving is, in effect, **means-tested by the market** — available without sacrifice to those with surplus, priced in subsistence for those without. This is a compounding inequity: households without surplus pay for material comfort, and pay again, in subsistence, for one of the most reliable non-material sources of human flourishing.

This paper argues that **structured redistribution can restore the experience of giving to households without surplus**, and that two design properties make it work. First, a **circulation primitive** — HeartBank's Re-Tip Jar℠, the earmarked second half of every 50/50 reward — makes each participant *always-already a giver*: a portion of what they receive is structurally theirs to pass on, so giving requires no pre-existing surplus. Second, **anonymity** removes the two social failure modes of giving under scarcity: small gifts are not embarrassing (the giver is not exposed as able to give only little), and large gifts produce no status or ego (credit diffuses through the family rather than accruing to a benefactor). Together these make generosity **culturally safe, socially rewarding, and financially accessible** to people for whom giving had been costly, exposed, or both.

The thesis was prompted by a single pilot family in Cambodia whose first month suggested exactly this dynamic, including a recursive "give-side" diffusion in which the *amount* re-tipped shrinks geometrically toward zero while *appreciation* spreads outward through the network — and members began recruiting others **so they could give to them**. We report that signal honestly as n = 1 (§10) and rest the argument on the published literature (§9). We close with design implications and with the reframing this forces on dignity infrastructure generally: from *being seen* to *being one who gives*.

**Keywords:** prosocial spending, warm-glow giving, charitable giving by income, discretionary income, low-income households, peer-to-peer transfer, reward ledger, incentive payment, split payment, earmarked account, restricted-use balance, give-only balance, non-withdrawable credit, expiring balance, annual reset, donor anonymity, anonymous giving, pay-it-forward, recursive gifting, mental accounting, fungibility, house money effect, family group account, shared household ledger, dignity of aid recipients, reciprocity, defensive publication.

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| Re-Tip Jar℠; the jar; the giving-portion | earmarked, non-withdrawable, give-only (forward-only) balance held per member |
| re-tip | peer-to-peer transfer from a give-only balance to another member, received as a credit |
| 50/50 reward; the split-at-credit rule | automatic equal split of each incoming credit between a kept account and a give-only balance |
| personal account | the member's own (kept) account |
| reward for a kindness | incentive payment for a recorded prosocial act |
| family bank | shared family-group ledger with per-member accounts |
| 7 January reset; circulation cadence | annual expiry of unspent give-only balances to zero |
| Aquarian Pool℠; the commons | common fund receiving balances that have no human addressee |
| the giving dividend; warm glow | wellbeing benefit of prosocial spending to the giver |
| means-tested by the market | available without sacrifice only to holders of discretionary income |
| always-already a giver | universal giving capacity by allocation rather than by surplus |
| default anonymity | donor identity withheld from recipients by default; attribution optional |
| recursive diffusion | multi-hop onward transfer with geometric attenuation of the amount |
| give-side virality | referral growth motivated by the referrer's wish to give to the invitee |
| *dāna*; *muditā* (Pāli) | giving; sympathetic joy |
| Miss Aquarius℠ | the name under which this corpus discloses AI writing collaboration |

---

## Contents

1. [The neglected half of dignity](#1-the-neglected-half-of-dignity)
2. [Giving makes the giver happier — the reported finding](#2-giving-makes-the-giver-happier)
3. [The hidden precondition: a surplus to give from](#3-the-hidden-precondition)
4. [Giving is means-tested by the market](#4-giving-is-means-tested-by-the-market)
5. [The circulation primitive: always-already a giver](#5-the-circulation-primitive)
6. [Anonymity removes the two failure modes of giving under scarcity](#6-anonymity-removes-the-two-failure-modes)
7. [Recursive diffusion: amount to zero, appreciation outward](#7-recursive-diffusion)
8. [Dignity reframed: from being seen to being a giver](#8-dignity-reframed)
9. [Lineage and prior art](#9-lineage-and-prior-art)
10. [The pilot signal, reported honestly (n = 1)](#10-the-pilot-signal-n--1)
11. [Design implications and claimed contribution](#11-design-implications-and-claimed-contribution)
12. [Cross-references](#12-cross-references)

---

## 1. The neglected half of dignity

Dignity infrastructure — the broad project of building systems that restore people's sense of mattering — has a reception bias. It asks how to help people be *seen*, *heard*, *acknowledged*, *supported*. These are right and necessary. But human dignity has a second face that the reception frame misses: the dignity of **agency**, and specifically of **generosity** — the standing of one who is not only a recipient of others' care but a *source* of it.

To be perpetually on the receiving end — of charity, of aid, of others' kindness — is its own subtle indignity, however well-meant the giving. The recipient is positioned as the one who lacks, the one who is helped, the one whose role in the moral economy is to be a beneficiary. What restores full dignity is not better reception but **the restored capacity to give back, and to give freely** — to occupy, at least sometimes, the giver's side of the relation.

This paper concerns that neglected half, and a specific population for whom it comes at the highest price: families whose income is absorbed by subsistence.

---

## 2. Giving makes the giver happier

That giving benefits the giver is one of the better-established findings in the science of wellbeing.

- **Prosocial spending raises happiness.** Dunn, Aknin, and Norton (*Science*, 2008) found that spending money on others produces greater happiness than spending it on oneself, and that this holds when assigned experimentally, not merely correlationally. The experiment was small (N = 46), and a 2022 close replication (N = 133, *PLoS ONE*, doi:10.1371/journal.pone.0272434) did not find the difference on the original measure, though a more direct single-item happiness measure moved in the original direction.
- **It generalizes across cultures and income levels.** Aknin and colleagues (2013) found the prosocial-spending–wellbeing association positive in 120 of 136 countries, poor and rich — survey evidence, correlational, and present in contexts of real material scarcity, where one might expect self-spending to dominate.
- **It appears before it is likely to have been taught.** Toddlers show greater happiness giving treats away than receiving them, and greater happiness still when the giving is costly to them (Aknin, Hamlin & Dunn 2012) — suggesting the giver's reward is closer to a human universal than to a learned, surplus-dependent luxury.
- **"Warm-glow" giving.** Andreoni (1990) modeled the giver's own satisfaction — the *warm glow* — as a real and separable good, distinct from the recipient's benefit. Giving is consumption of a felt good, not only a transfer.

The contemplative traditions said the same long before the journals. In Buddhism, **dāna** (giving) is the first of the ten perfections in the *Buddhavaṃsa*'s list, and the discourses name what giving does for the **giver**: AN 5.35 (the *Dānānisaṃsa Sutta*) lists five benefits to the giver — being dear to many, the company of the good, a good name, not falling away from a householder's duties, and a good rebirth — and AN 6.37 describes the giver as glad before giving, settled in mind while giving, and satisfied after (*pubbeva dānā sumano hoti, dadaṃ cittaṃ pasādeti, datvā attamano hoti*). **Muditā**, sympathetic joy, names the gladness one feels at another's good — on this paper's reading, a gladness the giver can taste directly in the recipient's benefit.

The finding, then, is old and widely reported, though its experimental base is smaller than its fame: **to give is to receive a happiness that, in these designs, the same resources spent on oneself did not buy.** The question this paper presses is the one the finding leaves open.

---

## 3. The hidden precondition

The canonical prosocial-spending experiments hold fixed something life does not: **that the giver has money to spend prosocially.** They hand participants a sum — $5 or $20 in Dunn, Aknin and Norton's experiment — and ask them to give some of it away. Real life hands no such sum. To give without cost to subsistence, one must first have a surplus — income beyond what subsistence and obligation already claim.

For a large fraction of humanity that surplus is thin or absent: in the World Bank's 2024 estimate, 44 percent of the world's population lived on less than $6.85 a day (*Poverty, Prosperity, and Planet Report 2024*). When earning enough to feed, house, and school a family is itself the entire daily struggle, there is no remainder to give from. The wellbeing dividend of giving — real, repeatable, cross-cultural — sits behind a gate that households without surplus pass only at a price the comfortable never pay: **you may have the happiness of giving without sacrifice once you can afford to give.**

```
   THE GIVING DIVIDEND IS GATED BY SURPLUS

   income ──────────────────────────────────────────────►
            │ subsistence │ obligations │  surplus  │
            └─────────────┴─────────────┴─────┬─────┘
                                              │
                                    giving (and its
                                    wellbeing dividend)
                                    draws only from here
            ◄── where this band is ≈ 0, every gift is paid from
                subsistence → the dividend is priced, not free
```

This is not a failure of will. Households without surplus give anyway — in Dutch panel data a *higher* share of income than richer households (Wiepking 2007, *Voluntas* 18(4)), though the share is contested: in US panel data, giving as a share of income is roughly flat across the income distribution (Meer & Priday 2021, *National Tax Journal* 74(3)) — and they pay for it in subsistence. The dividend is not withheld from them; it is **priced** for them and free for the comfortable. What scarcity removes is not the will but the surplus that would make giving costless: the **occasion** and **means** to give without sacrifice.

The band in the diagram is a simplification, and mental accounting says which one. A household does not hold one pool with a residual at the end. Thaler (1999) describes money labeled into budgets, accounts and income categories that are not perfect substitutes, and reports, as a generalization from interviews conducted in the early 1980s, that "Families living near the poverty level use strict, explicit budgets; in wealthy families budgets are both less binding and less well defined." A gift can then meet a category limit while money sits elsewhere (his example is a $100 public-radio membership "possibly running into binding budget constraints in the charitable giving category"), and a household with no residual can still keep a place for giving. The gate of this section is therefore partly a budget line as well as a residual, and this paper has measured neither.

---

## 4. Giving is means-tested by the market

Put plainly: in a pure market arrangement, **the happiness of giving is priced** — means-tested in the sense that it comes without sacrifice only to those with surplus. Those with surplus can buy it (by giving away the surplus and reaping the warm glow, the meaning, the social bond); those without surplus can have it only by paying in subsistence. One of the most reliable non-material sources of flourishing is, in effect, **free only to those who already have enough** — and priced, in subsistence, for those who have least.

This compounds material inequality with a subtler **flourishing inequality**. Households without surplus pay twice: once in comfort, and again for the dignity and joy of being a benefactor. Charity, as conventionally arranged, *deepens* the second cost (the reciprocity argument is made from the recipients' side by Parsell and Clarke, *Charity and Shame: Towards Reciprocity*, *Social Problems* 69(2), 2022) — it casts those it serves permanently as recipients, the objects of others' giving, never its subjects.

The design question this paper answers: **can infrastructure restore the giving dividend to people without surplus — not as a metaphor, but as real, felt, repeated giving?**

---

## 5. The circulation primitive

HeartBank's answer is structural. The mechanism is the **Re-Tip Jar℠** — the earmarked second half of every 50/50 reward (the canonical circulation primitive; see the self-thanking and 50/50 corpus work). When a participant is rewarded for a kindness, half lands in their personal account, and **half lands, already earmarked, in a jar that is theirs to pass on.**

The rule, stated once so that §7 can be derived from it rather than asserted: **at every credit — a reward or a received re-tip — the credited amount splits 50/50 at the moment of credit**, half to the personal account and half to the jar. A re-tip is a transfer of jar balance to another participant; it is itself a credit, so it splits again. On 7 January every jar returns to zero; an unspent balance is gratitude with no human addressee, which the architecture's definition assigns to the commons — the Aquarian Pool℠ once it exists, and until then it is recorded as released, never rolled over.

The consequence is decisive: **every participant is always-already a giver.** Giving no longer requires a surplus set aside from subsistence, because half of every reward a participant earns by a witnessed kindness arrives already earmarked: the surplus is their own, pre-committed — and in the pilot the reward pool itself was seeded (§10). The system does not ask anyone to find a surplus they do not have; it routes a giving-portion to them as part of the gift, so that being-a-giver is built into being-a-participant.

```
   EVERY REWARD MAKES A GIVER

   kindness ──► reward ──┬──► 50%  personal account   (yours to keep)
                         └──► 50%  Re-Tip Jar℠         (yours to GIVE)
                                        │
                                        ▼
                              passed onward to another,
                              who is now also a giver ──► (recurse, §7)

   giving requires NO prior surplus — the giving-portion arrives
   as part of the gift. Every participant is a benefactor structurally.
```

This is the operational heart of "giving is a gift too": the gift one receives **includes the gift of being able to give.** And because an expiration cadence (the January 7 reset) keeps the jar from being hoarded, the giving-portion must actually circulate — use-it-or-lose-it converts latent capacity into realized generosity. What the jar restores is *costless* giving — a re-tip spends nothing its giver could otherwise keep — and §10 records why that may be the smaller dividend.

The economist's objection belongs here. The principle of fungibility is, in Thaler's phrase, that "Money is not supposed to have labels attached to it" (1985). By that principle half a reward restricted to one use is worth at most what the same half would be worth paid freely; the usual advice, as he states it in order to dispute it, is that "a gift in kind can be at best as good as a gift of cash" (1999). For a household short of food the restricted half is worth less. So a re-tip is costless at the moment of the re-tip and not at the moment of the split: compared with a reward paid whole into the personal account, the split has already put half of it out of reach of the household's needs. Two things temper the objection and neither dissolves it. The chain of §7 lands all of T in personal accounts, so what one member could not keep a relative does, apart from whatever is released at the reset. And mental accounting reads a restriction as sometimes worth having: people may prefer a gift in kind when it is on a "forbidden list", and Thaler reads the gift-type pay of Tupperware dealers as a way to "mentally segregate her earnings from total family income" and direct them (1985). That giving is such an item in a strict budget is this paper's extension; neither of his papers tests it. The jar's restriction is in any case a rule of the ledger, not a habit of mind (labels exist "in real as well as in mental accounting systems", 1999), so it holds whether or not a member's own accounting honors it. Whether a member offered the choice would take the whole reward instead is not something the split, as specified here, lets anyone observe.

---

## 6. Anonymity removes the two failure modes

Giving under scarcity has two specific social failure modes, and default anonymity is designed to remove both.

**Failure mode 1 — the embarrassment of the small gift.** When giving is attributed, the size of the gift signals the giver's means. A person who can give only a little is exposed as able to give only a little; the small gift becomes a small humiliation, and the rational response is to give nothing rather than be seen giving little. Anonymity removes the signal: **a small gift is not embarrassing because it is not attributed.** Anyone can give what they can without their means being read off the amount.

**Failure mode 2 — the ego (and dependency) of the large gift.** When giving is attributed, the large gift creates a benefactor and a beneficiary — status accrues to the giver, obligation and diminishment to the receiver. Within a family this breeds favoritism, debt, and quiet resentment. Anonymity removes the status, and the recursion diffuses the credit — because the jar half of what is received passes on, every recipient becomes a giver and no one stays the patron: **credit diffuses through the family rather than accruing to a named patron.** No member is positioned as the family's benefactor (the seed is another matter, §10); no one is positioned as its charity case. The gift lands as the family's own circulating good.

```
   ATTRIBUTED GIVING            │   ANONYMOUS GIVING (Re-Tip Jar℠)
   ─────────────────           │   ──────────────────────────────
   small gift → embarrassment  │   small gift → unremarkable, safe
   large gift → status/ego,    │   large gift → credit diffuses;
     beneficiary diminished    │     no patron, no charity case
   ⇒ rational move: give little │   ⇒ generosity is safe to express
     or not at all             │
```

The net effect: anonymity makes generosity **culturally safe** (no shame in giving little, no shame in receiving), **socially rewarding** (the warm glow and bonding without the status games), and **financially accessible** (the giving-portion is provided structurally). These three together are what scarcity normally denies. The cost is recognition: the giver keeps the warm glow (Andreoni's is internal) and gives up being seen. Visibility can also raise amounts: in a field experiment in thirty Dutch churches, replacing closed collection bags with open baskets raised the second of a service's two offerings by about 10 percent, left the first unchanged, and the rise faded over the 29 weeks (Soetevent 2005) — which is why the default is anonymity, not a ban on signing. How far anonymity removes either failure mode depends on the group being large enough to hide a giver (§10).

---

## 7. Recursive diffusion

The 50/50 circulation has a notable mathematical-social shape. Each re-tip can itself trigger a re-tip (the recipient now holds a giving-portion), and so on. The *amount* at each hop is bounded by the recursive halving — a geometric series whose total is finite. By the split-at-credit rule of §5, a quantity T re-tipped in full lands T/2 in the next member's jar and T/2 in that member's personal account; re-tipped in full again, T/4 and T/4; and so on. The personal-account landings sum to exactly T, so a chain moves T and creates nothing; counted hop by hop, the gross volume is T + T/2 + T/4 + … = 2T, still finite. The system is **redistributive, not inflationary**. But the *social* quantity moves the opposite way: each hop touches a new person with the experience of both receiving and giving, so **appreciation spreads outward as the amount shrinks toward zero.**

```
   amount:      T → T/2 → T/4 → T/8 → ...      (Σ finite; → 0)
   appreciation: •     • •     • • • •  ...     (spreads OUTWARD)

   money diffuses to nothing; the giver-experience multiplies.
```

Mental accounting cuts both ways on this shape. Thaler's first principle of hedonic framing is to "segregate gains", because a concave value function values two gains above their sum ("don't wrap all the Christmas presents in one box", 1985), so several small credits may please more than one large one; Thaler and Johnson (1990) found subjects did prefer to spread gains over time, though the wider hypothesis that people edit outcomes to be happiest got "only partial support". Against that, Thaler (1999) observes that "Many small, routine expenses are not booked": a small enough sum may not register as an event at all. If the amount at a far hop falls below that line, the hop touches no one. How small that is, and whether a ledger entry changes it, is unmeasured; his observation concerns expenses, and the extension to gifts is this paper's.

This yields a **give-side virality**, observed once, in the pilot: members began recruiting others to join *so that they could give to them* (§10). Network growth is usually modelled as driven by the desire to *get*; in the one family observed, some of the growth pressure was reported as the desire to *give* — which, if it holds, is precisely the dignity-good this paper is about, now acting as a distribution force. (This connects to the separate "share is the wedge" thesis, where a high-frequency carrier propagates the economy; here the carrier is the wish to give.)

---

## 8. Dignity reframed

The reception frame says: HeartBank helps you *be seen and thanked*. True, but partial. The deeper claim this paper reaches is: **HeartBank lets you be one who gives** — and where there is no surplus, that is the rarer and more dignifying gift.

This reframes the institution's value proposition. The product is not, at bottom, an acknowledgment machine; it is a **dignity-of-agency machine** that happens to run on acknowledgment. It restores to people the standing of benefactor on which scarcity had put a price.

There is a relational byproduct worth naming, because it may be the truest measure. When everyone in a family is always-already a giver — and gives safely, without shame or status — the family's internal relations may change. People may come to see one another as sources of kindness, not only as claimants on scarce resources. The first pilot family put it as *understanding each other better* (§10). That this relational gain appears alongside a *money* product is itself a signal worth testing: the mechanism appears, in one family, to produce **connection**, not only acknowledgment — blurring the usual line between the material and the relational halves of the mission.

---

## 9. Lineage and prior art

The thesis stands in a long and well-populated lineage; naming it both credits the prior art and strengthens the argument:

- **Buddhist dāna and muditā** — giving as the first perfection; the act dignifies and gladdens the giver. The contemplative source of the whole claim.
- **SN 1.32 (*Macchari Sutta*)** — a deity's verse praises the gift given from little (*appasmā dakkhiṇā dinnā, sahassena samaṃ mitā*: a gift given from little is measured equal to a thousand), and the Buddha, asked whose verse was well spoken, answers that all spoke well in a way and goes further: one who lives by the Dhamma though gleaning, supporting a wife and giving from his little, is such that a hundred thousand who sacrifice a thousand are not worth a fraction of him. The canon already measures a gift against its giver's means. This anticipates the means-relative reading of §3–§4, and it cuts against treating the small gift's embarrassment (§6) as a fact about giving rather than about attribution.
- **Dunn, Aknin & Norton (2008); Aknin et al. (2013, 136 countries); Aknin, Hamlin & Dunn (2012, toddlers)** — prosocial spending raises wellbeing, experimentally (with the replication caveat of §2) and across cultures and income levels.
- **Andreoni (1990), "warm-glow giving"** — the giver's own satisfaction as a real, separable good.
- **Richard H. Thaler, "Mental Accounting and Consumer Choice" (*Marketing Science* 4(3), 1985; read here in the *Marketing Science* 27(1), 2008 reprint) and "Mental Accounting Matters" (*Journal of Behavioral Decision Making* 12(3), 1999)** — money is labeled by source and by use, and the labels are not neutral: "Money in one mental account is not a perfect substitute for money in another account" (1999). The general behavior of an earmark is his ground and older than this paper (envelopes of cash, a labeled child allowance, earmarked grants), and it cuts against reading the jar's restriction as new in kind. His opening anecdote is itself a giving account: a colleague sets a yearly United Way target and deducts small misfortunes from it. A purely mental earmark can be repurposed by its holder in that way, which is the difference a ledger rule makes. The literature bears on this paper at §3 (strict budgets near poverty), §5 (the fungibility objection, and the reading of a restriction as worth having), §7 (segregated gains, unbooked small sums) and §10 (labeled money, spend-down before a reset). Neither paper concerns households giving without a surplus. A registered replication of the problems Thaler (1999) reviews (Li & Feldman, *Royal Society Open Science* 12(9), 2025, doi:10.1098/rsos.250979; N = 1,007) supported 11 of 17, with three mixed and three unsupported, and concludes that the effects "generally tend to replicate well but that some effects may be more complex and contextual than originally documented."
- **Richard H. Thaler and Eric J. Johnson, "Gambling with the House Money and Trying to Break Even" (*Management Science* 36(6), 1990, doi:10.1287/mnsc.36.6.643)** — the house money effect, "increased risk seeking in the presence of a prior gain". A study of risky choice, not of giving; its application to a give-only balance is this paper's, and it is applied against this paper's thesis (§10). Li & Feldman's replication counts the $30 problem as failed (§10).
- **Aristotle, *Nicomachean Ethics* IV.1–2** — giving well is a virtue and an excellence of character, not a surplus disposal problem, and Aristotle already splits it by means. Liberality (*eleutheriotēs*) is "used relatively to a man's substance", so "there is therefore nothing to prevent the man who gives less from being the more liberal man, if he has less to give"; magnificence (*megaloprepeia*), giving on a grand scale, is gated by wealth: "a poor man cannot be magnificent, since he has not the means with which to spend large sums fittingly" (W. D. Ross translation). This is the nearest classical anticipation of the distinction in §4 between giving that is relative to means and giving that requires a surplus, and it cuts against any claim that the distinction is new.
- **Marcel Mauss, *The Gift* (1925)** — the gift as the binding institution of social life; reciprocity as the weave of community.
- **Richard Titmuss, *The Gift Relationship* (1970)** — the social and moral superiority of gift-based systems (voluntary blood donation) over market ones, argued on blood procurement; giving as a public good.
- **Amartya Sen, capability approach** — poverty as capability deprivation; the *capability to give* as a functioning people have reason to value is the author's extension, not Sen's.
- **Self-Determination Theory (Ryan & Deci)** — relatedness and autonomy as basic needs; that autonomous, non-coerced giving satisfies both is the author's extension.
- **E. F. Schumacher, *Buddhist Economics* (1966; collected 1973)** — economic arrangements judged by whether they ennoble; that an economics in which giving is structurally available is a Buddhist-economic design is the author's extension.
- **Viktor Frankl** — meaning found by creating a work or doing a deed, one of the three routes to meaning in *Man's Search for Meaning*; that the giver finds a meaning the recipient-only role lacks is the author's extension.
- **Cameron Parsell and Andrew Clarke, *Charity and Shame: Towards Reciprocity* (*Social Problems* 69(2), 2022; online 2020)** — from the recipients' side, from interviews with people receiving charity in Australia, shame arises from being positioned as a passive recipient, and "the unidirectional provision of charity to people in poverty fails to take account of the value people place – and society expects – on reciprocity"; the authors argue for charity that lets recipients give as well as receive. The closest anticipation of §8's reframing, and it precedes this paper.
- **Thomas, Otis, Abraham, Markus & Walton (2020, PNAS), aid with dignity** — the empowerment framing of cash transfers; the dignity-of-reception side this paper extends to giving.
- **PayForward LLC, US 2015/0332306 A1 (priority 2014; granted as US 10,679,237 B2, 2020)** — merchant rebates allocated by the user, by percentage, to designated beneficiaries and causes: a giving-portion that arrives as part of a transaction. It discloses an earmark of this kind earlier and cuts against claim 2 as a bare idea. What it discloses differs at three points: a member may hold both the sponsor and the consumer role, but a received allocation is not described as splitting again and passing on; its privacy option conceals purchase details, at the user's choice, rather than withholding the giver from the recipient by default; and family members appear as co-contributors to a shared cause (a child's Little League team), not as one another's recipients. Named for what it discloses; nothing here is a reading of its claims.

**What this paper contributes.** The classical sources already measure a gift against its giver's means (Aristotle; SN 1.32), *Charity and Shame* precedes the reframing of §8, PayForward discloses the earmark first, and the general behavior of labeled money is Thaler's. What this paper contributes is the statement of the point in the terms of the prosocial-spending literature — the measured wellbeing dividend is free to those with surplus and priced in subsistence for those without — and a specific mechanism (a split-at-credit earmark, recursion through re-tips, default anonymity, family scope and an annual reset) that relocates a giving-portion to every participant. The canonical prosocial-spending experiments supply the giver's money; this paper concerns those who give from subsistence, and what infrastructure can do about it.

---

## 10. The pilot signal (n = 1)

The thesis was prompted by the first-month report of a single Cambodian pilot family (a household of four and twenty extended members across Cambodia and the USA, under one family bank). The relevant observations, as reported: members became active **givers** through the Re-Tip Jar despite limited means; the giving was described as feeling *safe* in the way anonymity predicts; a recursive give-side diffusion appeared, with members recruiting others **so they could give to them**; and the family reported, in the words of the household's point of contact, in the founder's translation, that they had come to *understand each other much better than before*.

This is reported as **one illuminating signal, not as evidence for a general claim.** The honest limitations are severe and stated plainly:

- **n = 1, one month.** A single family over a short window cannot support generalization.
- **Relationship and courtesy bias.** The point of contact is the founder's maternal first cousin; warm reports are culturally expected toward a respected relative who built the system, and reports reach the author through one relative, so the view is curated as well as courteous. Genuine, but unverified.
- **Founder-funded rewards, and a named patron.** The giving-portions were seeded by the founder; un-subsidized dynamics are untested. The seed also has a patron: credit diffuses between members (§6), but at the level of the family bank there is a known benefactor, a respected relative, so the diffusion argument covers re-tips between members and not the seed itself.
- **Untested unsubsidised.** The thesis is falsified if re-tipping ceases when the seed is withdrawn and the jar comes to be treated as routing rather than felt giving. The public prediction register's pilot-scale inelasticity prediction (P-PL5) is the instrument that will read it; it is gated on the Q2 2027 taper and on a confound registered against P-K1 on 2026-09-04 — a second reward for kindness, the family account made spendable at a shop, now present in the same household — and is unscored until both are resolved.
- **Costless giving may be the smaller dividend.** The giving-portion arrives pre-committed, so a re-tip spends nothing its giver could otherwise keep. In the toddler study of §2, giving that cost the child a treat of their own produced more happiness than giving a treat that cost nothing (Aknin, Hamlin & Dunn 2012). What the mechanism restores is the experience of costless giving; whether its dividend is a meaningful share of the costly one is untested.
- **The jar may be spent as house money.** This is the sharpest rival to felt giving, and it needs no farming. Thaler and Johnson (1990) report increased risk seeking after a prior gain: in their real-money Experiment 4, in which ten selected subjects played out their gambles, 77 percent of undergraduates (N = 95) took a fair $4.50 gamble presented after a $15 gain, against 44 percent (N = 111) offered the same payoffs as a single stage. Thaler (1999) gives the image: gamblers who have won "put that money into a different pocket from their 'own' money". A jar is that pocket built into the ledger, and the ledger is two-stage by construction: the credit arrives, and the re-tip is decided later. If members code the jar that way, active re-tipping is what the effect would predict with no generosity in it, and the report that members became givers stops counting for the thesis. Three limits on the rival, none of which removes it. The experiments measured risky choice, not giving. The effect is unsettled: Li and Feldman (2025) put the $30 problem as Thaler prints it to 504 US adults online as an imagined scenario and found 28 percent taking the gamble against his 70, in the opposite direction from the prediction, though the 1990 paper itself lists that problem among its hypothetical questions (Thaler 1999 describes it as played for real money), and Thaler and Johnson offer their editing rule as one account of the data, not "the only model consistent with these data". And a jar fills from two sources, a reward for a recorded act and a re-tip received, whose coding may differ; nothing reported here separates them.
- **The reset may buy spending, not generosity.** §5 reads use-it-or-lose-it as converting capacity into generosity. Thaler (1999) describes the same rule in organizations as a distortion: where "funds cannot be carried over from one year to the next", a department can be "desperately looking for ways to spend down this year's budget". A re-tip made to empty a jar before 7 January is recorded exactly as one made from gladness. A cluster of re-tips in the weeks before the reset would be the visible sign; this paper has not read the ledger for it. He adds that "Poorer families also tend to have budgets defined over shorter periods (a week or month)", so an annual deadline may be out of view for most of the year. Claim 5 discloses the reset and does not depend on this reading; the sentence in §5 does.
- **The ledger sees only itself.** Under fungibility, giving from the jar could displace gifts a household already makes in cash, adding no net generosity. Thaler (1999) reports the opposite tendency for labeled money (Dutch spending on children's clothing tracking a designated child allowance more than other income, Kooreman 1997; the flypaper effect for earmarked grants, Hines & Thaler 1995); those two are cited as he reports them, and neither concerns gifts. Nothing reported here measures giving outside the ledger, so the pilot cannot say whether re-tips add to it or replace it.
- **Anonymity in a small group is thin, and untested here.** Among a few dozen relatives a recipient can often infer the giver from context, so the size signal of §6 is removed only as far as the group is large enough to hide a giver. The pilot cannot test the anonymity half: the public prediction register records 827 of 830 re-tips carrying the anonymous flag, a default rather than a choice, so its anonymity prediction (P-PL7) is unscorable until the product offers a real choice. §6 is argued, not observed.
- **Giving can be farmed too.** Just as self-thanking can be gamed for rewards, the giving-portion could be circulated mechanically rather than felt. Whether the observed generosity is felt giving or reward-routing is not yet distinguishable from the data.

The thesis therefore **does not rest on this pilot.** It rests on the reasoning of §3–§8 and the literature of §9; the pilot is what made the author look, and is offered as a hypothesis-generating first signal to be tested as more families onboard. The right epistemic posture is: *a strong conceptual claim with a single suggestive data point and a named program for testing it* — whose two pilot instruments, as stated above, are not yet scorable.

---

## 11. Design implications and claimed contribution

**Design implications** for any system attempting to restore the giving dividend:

1. **Provide the giving-portion structurally** (earmarked circulation), so giving requires no pre-existing surplus.
2. **Default to anonymity** for giving, to neutralize both the embarrassment of the small gift and the status of the large one.
3. **Add a circulation cadence** (expiration / reset), so the giving-capacity must be exercised rather than hoarded.
4. **Diffuse credit**, never concentrate it — no benefactors, no charity cases.
5. **Guard against farming** — instrument whether giving is felt or mechanical; the dignity-good is real only if the giving is real.

**Claimed contribution** (dedicated to the public domain under CC0 1.0):

1. The **framing** that the giving-and-wellbeing dividend is *means-tested by the market* — available without sacrifice only to those with surplus, and priced in subsistence for everyone else — and that this is a distinct, addressable inequity (the means-relativity of a gift's worth is classical — Aristotle, *Nicomachean Ethics* IV; SN 1.32; what is claimed is its statement as a pricing of the wellbeing dividend the prosocial-spending studies measure).
2. The **mechanism**: a family-scoped ledger in which every credit — a reward or a received re-tip — splits 50/50 at the moment of credit, half to a personal account the participant keeps and half to an earmarked jar whose only outflow is a re-tip to another participant, which is itself a credit and splits again, with the giver withheld from the recipient by default; and the **thesis** that this combination of earmarked circulation (the giving-portion arrives as part of the gift) and anonymity (neutralizing the small-gift and large-gift failure modes) can **restore the experience of giving to households without surplus**, making generosity culturally safe, socially rewarding, and financially accessible.
3. The **dignity reframing** of acknowledgment infrastructure from *being seen* to *being one who gives*, with connection as the relational byproduct (a signal in one family, §8; the reciprocity argument itself is prior — *Charity and Shame*, 2022; what is claimed is its application to acknowledgment infrastructure).
4. The **give-side virality** observation (a single family, reported and unmeasured): the wish to give as a distribution force (amount → 0, appreciation → outward).
5. As claim 2, with an **annual reset**: on 7 January every jar returns to zero, and an unspent balance — gratitude with no human addressee — is assigned to the commons (a common fund once one exists; until then recorded as released), never rolled over, so the giving-portion must circulate rather than accumulate.

---

## 12. Cross-references

- [Kids as triggers / self-thanking](https://thonly.org/research/kids-as-triggers-self-thanking) — the 50/50 pedagogy this paper's circulation primitive extends.
- [Emotional infrastructure as a public good](https://thonly.org/research/emotional-infrastructure-as-a-public-good) — the dignity-infrastructure frame this paper completes on the giving side.
- [Brand identity as architecture](https://thonly.org/research/brand-identity-as-architecture) — the anonymity and circulation conventions referenced here.
- *The Share Is the Wedge* (heartbank.net/positions) — the distribution thesis the give-side virality connects to.
- Pilot field record (internal; not published) — the first-month observation that prompted this thesis.
- [Public prediction register](https://thonly.org/research/program/register) — P-PL5 (inelasticity) and P-PL7 (anonymity), the instruments named in §10.

---

**First published 2026-06-08; revised 2026-11-04.** The thesis and mechanism are offered with a single suggestive field signal and an explicit testing program (P-PL5 and P-PL7 in the public prediction register); empirical claims are hedged to n = 1 (§10). The patterns are dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks are separately reserved by the author and HeartBank®.

**Author:** Thon Ly · Founder, HeartBank® · Kâmpôt, Cambodia.

Co-drafted in collaboration with [Miss Aquarius℠](https://missaquarius.org) (the project's named AI substrate; CEO of HeartBank). Substantive authorship and final editorial control remain with the author.

---

_— End of defensive publication —_

*This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
