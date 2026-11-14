---
title: "Uniform Worldwide Rewards for Opt-In Rewarded Video Ads, Set Each Season from the Prior Season's Ad Revenue: The Same Pay for the Same Ad, Everywhere"
subtitle: "A Feed of Only Ads, Entered by Choice, That Pays Non-Transferable In-App Compute Credits per Finished Ad at One Published, Season-Frozen Rate for Every Viewer, with Three Ways to Bound What the Rate Can Cost (the B-Flick℠ mechanism)"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-b
program: open
status: draft
date: 2026-11-14
license: CC0-1.0
slug: the-same-pay-for-the-same-ad
venue: thonly.org/research/the-same-pay-for-the-same-ad
canonical_url: https://thonly.org/research/the-same-pay-for-the-same-ad
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claims* and withholds the *build specification* (§13 says what is withheld and why). A quick prior-art census ran before drafting, and §2 reports it in full: every part of the mechanism is already public or partly public, and only the combination was not found, in a thin, English-only search. A counterexample hunt then ran against the design before a word of this paper was written, and it changed the paper. The design as first stated claimed to be affordable by construction. It is not, and §6 shows the case that breaks it, then discloses three ways to bound the cost. The design is the one that removes the case entirely, a rate set from the lowest-revenue market served (§6.3); the average form is retained as a disclosed variant. The enumerated claims of §14 are the census's survivor and those bounded forms, nothing wider. A full census, covering the languages and literature the quick one did not, is owed before this paper's first archival deposit.
>
> Companion works: *The Zero-Employee Institution* (the earning legs this mechanism sits inside), *The Fractal Three-Level Architecture* (an equal floor per verified human, with parameters public and frozen for the season), *The Zero-Point Game* (a rule fixed before anyone knows whom it favors), and *B-PoH: A Humanity Layer for the AI-Native Internet* (the proof of a person that §8 leans on).

---

## Preamble

The same thirty-second advertisement, shown to two people on the same day, earns the app that showed it very different amounts. Shown on a phone in San Francisco it may earn a few cents; shown on a phone in Kampot it may earn a tenth of that, or nothing, because no advertiser bid for the slot. The ad market is not being cruel when it does this. An advertiser pays for the chance that a viewer will buy, and the chance is priced by what the viewer can spend. The price of a person's attention follows the size of their wallet.

Rewarded advertising inherits that price. When an app lets a person watch an ad in exchange for something inside the app, an extra life or a few credits, the app is paid by the market's rate for that person, and the obvious design pays the person in proportion. Most apps do not do the obvious thing. They set one reward per ad unit and pay it to everyone, because it is simpler. The result is that the same reward is already paid worldwide in many apps, by default, without anyone having decided that it should be.

This paper is about deciding it. It discloses a page inside an app that shows nothing but ads, entered only when the person chooses to go there, in which every finished ad pays the same number of in-app compute credits to every viewer in every country, at a rate published once a season and frozen for that season. The credits cannot be withdrawn, transferred or bought, and they never expire. They buy computing inside the publisher's apps: an image rendered, a file stored. The purpose is access. A person with little money and some time can use the same tools as a person with money and no time, and the rate they are paid for their time does not depend on where they live.

The paper also reports, in its own body, why that last sentence is narrower than it sounds. Equal pay per ad is not equal pay per hour. A rate set from last season's average is not affordable by construction. And a feed that pays everyone the same attracts the people for whom the same is the most, which pulls the average down toward the lowest-revenue market served. Each of these was found by an adversarial pass run before drafting, and each changed what is claimed.

---

## Prior-Art and Non-Assertion Statement

This document is published as a **defensive publication** to establish prior art. Its contents, including every mechanism, the analysis, the variants of §11 and the enumerated claims of §14, are dedicated to the public domain under **CC0 1.0 Universal**. **The authors assert no patent rights in anything disclosed here, will not seek patent protection for it, and will not assert any patent against any person who practices it.** The dedication covers the mechanism under any name; the marks named in the Trademark Notice are reserved separately and are not licensed.

A quick prior-art census was run before drafting, with its pre-registration pushed to a public repository before the first query (§2.2). Its result is reported in §2 in full: the declared aperture and date, every conjunct that was killed or narrowed with its prior art cited, and the survivor. **The enumerated claims of §14 are that survivor, plus the bounded forms of §6 that the counterexample hunt made necessary, and nothing wider.** The bounded forms were designed after the census ran; they were not searched separately, and the full census owed before this paper's first archival deposit must search them (§15). Where a patent discloses something, this paper cites what the patent *discloses*, as far as it was read, and says nothing about whether any design falls within its *claims*; that is a question for counsel and is not answered here.

---

## Abstract

This paper discloses a computer-implemented system for opt-in rewarded video advertising in which (1) a dedicated page inside a functional application presents a vertical feed whose every item is a rewarded video advertisement, and the page is reached only by the person's own navigation, never by a prompt, badge or redirect; (2) each advertisement is started by the person's own tap, and only a *finished* advertisement earns a reward, while an advertisement skipped or dismissed earns nothing and costs nothing; (3) the reward is a quantity of in-app credits, here called Kernels, that are earned only and never sold, cannot be withdrawn, transferred or redeemed for money, never expire, are kept in a ledger separate from any money balance the person holds, and are spent at a fixed credit price per use on computing services (generation, storage) inside the publisher's applications; and (4) every viewer in every country earns the same number of credits per finished advertisement, at a rate set once per season for everyone from the previous season's ad revenue per finished advertisement, published before the season opens and frozen for its length.

The paper shows that the rate in (4), when set from the previous season's *average*, does not bound what the system can spend. A shift in the mix of viewers toward lower-revenue markets during the season makes every finish cost more than it earns, and a uniform reward invites exactly that shift. It then discloses three bounded forms. The design adopts the first: a rate set from the *lowest* revenue per finished advertisement among the markets served last season, so that every finish pays for its own credits whatever the mix. The other two are disclosed as variants: a published fraction of the average, with minting suspended for everyone at once if the season's revenue actually received falls below what has been minted; and a per-person, per-season limit on paid finishes, enforced in the ledger's mint function behind a proof of personhood. It discloses where the revenue above the reward goes (to a free usage allowance for people who watch nothing), why the credits are redeemed at measured cost so that the operator earns nothing per minute watched, and which audiences, formats and applications are excluded. The claims are a composition; every component is in the public record, and §2 cites it.

**Keywords:** rewarded video advertising, rewarded ads, incentivized advertising, in-app currency, virtual currency, non-transferable credits, opt-in advertising, vertical video feed, eCPM, ad revenue sharing, uniform global pricing, geographic price discrimination, prospective rate setting, adverse selection, invalid traffic, proof of personhood, compute credits, generative AI access, digital inclusion.

---

## 1 · What this is for

### 1.1 · The access problem

Generative tools cost money every time they run. A render of an image, a few seconds of synthesized speech, a stored file: each has a cloud bill behind it, and somebody pays. The publisher of the apps this paper concerns, THonly™, sells that computing to the people who use it, through one prepaid balance in money. A person who can pay, pays.

A person who cannot pay meets three doors before this paper's page is relevant, in a fixed order, for every costly action:

```
  a costly action (render · store · generate)
        │
        ▼
  ┌─────────────┐   covered?   ┌────────────┐
  │ 1 free      │──── yes ────▶│  it runs   │
  │   allowance │              └────────────┘
  └─────┬───────┘                    ▲
        no                           │
        ▼                            │
  ┌─────────────┐   covered?         │
  │ 2 a gift    │──── yes ───────────┤
  │   (someone  │                    │
  │   gave use  │                    │
  │   forward)  │                    │
  └─────┬───────┘                    │
        no                           │
        ▼                            │
  ┌─────────────┐   enough?          │
  │ 3 pay from  │──── yes ───────────┤
  │   the money │                    │
  │   balance   │                    │
  └─────┬───────┘                    │
        no                           │
        ▼                            │
  ┌──────────────────────────┐       │
  │ 4 one ad, one use, where │─ yes ─┘
  │   allowed; never forced  │
  └──────────────────────────┘
```

The free allowance comes first and is equal per verified person. It is sized each season from what was actually raised to fund it, divided by the people it serves, so it cannot overspend at any scale. A gift is capacity another person paid for and gave forward, anonymously, as items ("ten renders"), never as a currency. Paying comes third. An advertisement, where it is permitted at all, comes last, and it is offered at the costly action itself, once, as an equal choice beside paying; nobody is ever routed to it.

This paper adds a fifth thing beside the fourth door: a place a person may go, by choice, to watch advertisements ahead of need and keep what they earn. The fourth door spends an ad immediately on the action in front of the person. The page lets a person who would rather pay with time than money do so on their own schedule, and arrive at the costly action with credits already in hand.

### 1.2 · What the page must not become

The same publisher's sister institution, HeartBank®, has published a permanent refusal of advertising revenue, in any form, and of engagement-maximizing feeds. Its reason is structural: a platform that earns from the attention it holds is paid when it holds a person, while the person is usually better served by leaving. The corpus that this paper joins argues the same thing about attention economies in general. A feed of nothing but advertisements is, on its face, the attention economy distilled.

The design therefore has to answer three questions before it answers any of its own, and §4, §5 and §10 hold the answers.

1. **Does the operator earn more when a person watches more?** It must not. §5.4 redeems the credits at measured cost, and §6.4 sends any revenue above the reward to the free allowance, so the operator's revenue per minute watched is zero.
2. **Can anything route a person to the page, or keep them there?** It must not. §4 lists what is refused: no prompt, badge, counter, streak, daily bonus, task list, referral reward or autoplay into the next ad.
3. **Can anything earned on the page reach HeartBank?** It must not. Kernels are never spent in a HeartBank app, ad money never touches HeartBank's gratitude ledger or any of its counts, and the page lives only in THonly™ and Factory 333™ applications (§10).

---

## 2 · The problem and the prior art: the census

### 2.1 · How rewarded advertising prices a person

A rewarded advertisement is a full-screen video that a person chooses to watch in exchange for a reward inside an app. Ad networks pay the app per thousand impressions (eCPM), and the eCPM depends heavily on the viewer's country: the advertisers bidding for a viewer in a high-income market pay many times what they pay for one in a low-income market, and in some markets no advertiser bids at all, so the slot goes unfilled.

The networks' own policies shape what a reward may be. Google AdMob's policy for ad units that offer rewards requires that rewarded ads "must only be served after a user affirmatively and unambiguously opts in"; that the publisher give "clear, accurate and conspicuous disclosure of the action(s) required and reward(s) offered" before each one; that "it must be possible to skip or dismiss them"; and that "direct monetary items may not be offered as rewards under any circumstance", while a reward that is "only redeemable and usable for an item or service within the publisher's platform, website or app", and is non-transferable, is permitted [1]. Kernels are designed to sit inside that permission.

The reward itself is set by the app, per ad unit. The network does not require the reward to follow the eCPM, and the simplest practice is a fixed reward for every viewer. So a uniform reward worldwide already exists in commerce, as an unstated default. What this paper discloses is not uniformity as such. It is a published, season-frozen commitment that ties the uniform reward to last season's revenue, together with the design that keeps that commitment affordable and keeps the page from becoming an engagement product.

### 2.2 · The census

**Pre-registration.** The claim was split into five conjuncts and a prediction was written for each, with a known-prior-art control, before any search ran. The pre-registration was pushed to a public repository on 2026-11-09 at 09:26 PST (commit `a3b8997`, GitHub's push record). The conjuncts:

- **(a)** finishing an ad earns in-app credits that cannot be withdrawn or transferred, and a skipped ad earns nothing;
- **(b)** those credits are spent on compute (AI generation, storage) in the publisher's apps;
- **(c)** a vertical swipe feed in which every item is an ad, entered only by the viewer's own choice;
- **(d)** every viewer in every country earns the same per finished ad, as a stated rule;
- **(e)** the earn rate is set each season, for everyone, from the prior season's average ad revenue, and is published and frozen in-season.

**Depth and aperture, declared before searching.** Quick. Commercial web (app stores, vendor documentation, press); non-commercial practice (charity ad-watching, click-to-give); Google Patents by keyword, including published applications; English only. **Not run:** Chinese, Japanese, Korean or Khmer sources; academic indexes; standards bodies; citation walks. The category's largest body of practice is Chinese watch-to-earn short-video apps, which this census did not read, so a null on (c), (d) or (e) is weak. Eleven queries ran; they are listed in the census record and can be re-run.

**Control.** TikTok Lite's Task and Reward program, which paid points for watching videos and was the subject of European Commission proceedings in 2024, was predicted to be found. It was found, at source [2]. A census that missed it would have voided every null below.

| Conjunct | Predicted | Found | First public | Verdict |
|---|---|---|---|---|
| (a) credits for a finished ad, nothing for a skip | KILLS | US 8,005,713 B1 discloses crediting a user's account for playing an advertisement, with skipping interrupting playback [3]; the AIArtGen app's listing offers to "earn diamonds by watching optional ads" [4] | patent priority 2000-11-08 | **KILLS** |
| (b) spent on compute in the publisher's apps | KILLS | AIArtGen sells and grants the same diamonds; that they buy generation is inferred from the listing's steps [4]; storage: nothing found | listing review dated 2024-12-02 | **NARROWS**, probably KILLS at AI generation |
| (c) a feed of only ads, entered by choice | NARROWS or KILLS | an ITRex case study describes "a TikTok-like mobile advertising platform where users watch a stream of ads", with a money reward [5]; US 2011/0191151 A1 discloses points or credits "based on viewing the advertisements", with ads "scrolled up" [6] | application priority 2010-02-01 | **KILLS** |
| (d) the same pay everywhere, as a stated rule | NARROWS | Monamedia's listing states "EUR 0.10 is credited to your account instantly" with no countries named, but its release notes mention "country wise currency changes in mobile ads", and it pays cash [7]; Zedge divided each day's video ad revenue by each day's views worldwide, for the artists on its platform, and moved to a by-country calculation in 2024 (read through search summaries only; its page refused the fetch) | Zedge to 2024 | **NARROWS** |
| (e) a rate from the prior season's average, published and frozen | NOT FOUND | Zedge's per-view figure from a period's revenue (summaries only); pooled ad revenue for creators, with daily revenue published (summaries only); privacy-browser ad rewards whose per-ad amount changes over time. A rate taken from the *prior* period, frozen and published, for *viewers*: not found | — | **NARROWS** at its parts; whole NOT FOUND at this depth |
| control | found | TikTok Lite Rewards, read at source [2] | 2024 | the nulls stand |
| all five in one system | NOT FOUND | no single system with all five | — | **NOT FOUND** at this depth |

**Width.** At mechanism width nothing survives. At composition width one sentence survives:

> *a feed of nothing but ads, entered by choice, in which every viewer everywhere earns the same app-only credits per finished ad, at a rate set once a season from the previous season's average and published and frozen.*

**Route.** OPEN at composition width only. No live patent was found among the four documents read: US 8,005,713 B1 is shown by Google Patents as expired on 2025-04-26, and the applications read are shown as abandoned. That is the database's statement, read by keyword search; it is not a legal conclusion and not a clearance.

**Free findings the census returned.** (1) On 2024-08-05 TikTok agreed to "permanently remove its rewards program from the European Union" after the Commission said it "may stimulate addictive behavior", of particular concern for minors [2]. §9 answers this. (2) Zedge had one worldwide average and left it for a by-country figure, so the market's own direction runs against conjunct (d). §7 answers this. (3) Apps that grant a currency for watching ads also sell the same currency for money (AIArtGen, 500 diamonds for $1.99 [4]). §5.2 refuses this.

⚠️ *Not found* means not found in the aperture above on 2026-11-09. It never means new.

### 2.3 · Prior art the counterexample hunt added

The hunt (§12.1) found three more neighbors, each cited because it cuts against a claim this paper might otherwise have made.

- **Uniform pay regardless of location, for labor.** In 2017 Basecamp announced it would pay "everyone as though they live in San Francisco and work for a software company that pays in the top 10% of that market" [8]. That is one rate for every location, set at the top of the range, not the average. It shows that a stated rule of equal pay across locations is not new as an idea; what is narrower here is its application to viewers of advertisements, paid in non-transferable credits, from a lagged revenue statistic.
- **The opposite rule, for platform work.** The Fairwork project's principles for cloud and platform work benchmark fair pay to the worker's local living wage [9]. It is the considered opposite of conjunct (d), and the paper does not claim that (d) is the better rule for wages. §7.3 says why a credit for compute is a different case.
- **Prospective per-unit rates set from prior-period data.** Medicare's prospective payment system has paid hospitals a rate per admission fixed in advance from historical data since 1983. Carter, Newhouse and Relles showed that part of the measured rise in the case-mix index that followed was a change in coding, not in patients [10]. The general form, a per-unit rate fixed from the past and paid on a volume that responds to the rate, is old, and so is its failure mode. §6.2 is that failure mode in this setting.

### 2.4 · The authors' own prior disclosures

Two papers in this corpus already disclose a rule that is fixed and published before the period it governs. *The Fractal Three-Level Architecture* sets an equal floor per verified human with its parameters "public and frozen for the season" [11]. *The Zero-Point Game* rests a sizing rule on being fixed "before anyone knows whose thank it favors" [12]. This paper applies the same discipline to a rate paid for attention. It also inherits a warning from the second: timing removes a ruling on a case already seen, but it does not remove a slant toward a *kind* of case that the rule-setter can see coming. §7 is that warning, applied.

---

## 3 · The mechanism on one page

```
 SEASON s−1                         BETWEEN SEASONS                SEASON s
 ──────────────────────────         ───────────────────            ─────────────────────────────
 every finished ad recorded:        compute the rate r_s           the page opens; r_s is shown
   (market, revenue received)       from season s−1's record       once, the same for everyone
        │                             ├─ (A) average form          │
        │                             ├─ (B) lowest market ◀ design▼
        └────────────────────────────▶├─ (C) fraction + breaker    person taps an ad card
                                      │                            │
                                      ▼                            ├─ dismisses ─▶ nothing earned,
                                  publish r_s, frozen              │               nothing lost
                                  for all of season s              │
                                                                   └─ finishes ──▶ mint r_s Kernels
                                                                                   (if under the
                                                                                    person's cap and
                                                                                    the breaker is
                                                                                    not tripped)
                                                                                        │
                       ┌────────────────────────────────────────────────────────────────┘
                       ▼
          KERNEL LEDGER (separate from money)              REVENUE ABOVE THE REWARD
          · earned only, never sold                        · funds the free allowance
          · never withdrawn or transferred                   for people who watch nothing
          · never expires                                  · the operator keeps nothing
          · spent at a fixed Kernel price per use,           per minute watched
            redeemed at measured cost
```

Five parts, each specified below: the page (§4), the credits (§5), the rate and its bounds (§6), the equality the rate does and does not deliver (§7), and abuse (§8). §9 asks whether it is kind, and §10 states where it may not run.

---

## 4 · The page

### 4.1 · How a person arrives

The page is a section of a functional application: an app that does something else (renders images, keeps files, makes things), not an app built to show ads. It appears in the app's navigation as one entry among others, labeled as what it is. Nothing points to it. In particular:

- no prompt anywhere in the app suggests going there, including at a costly action where the money balance is short (that moment offers the fourth door, one ad for one use, and nothing else);
- no badge, dot or number marks the entry;
- no notification, email or message ever mentions it;
- the app does not change its navigation for a person who has used the page often.

The test for every screen outside the page: *could a person who never wants an advertisement use the whole app and never learn this page exists, except by reading the menu?* If yes, the page is non-intrusive.

### 4.2 · What the page shows

The page is a vertical feed of cards. Every card is one advertisement, labeled **Ad**, with the reward for finishing it stated on the card, in a fixed form: *Finish this ad: 5 Kernels.* The number is the season's rate, the same on every card for every person all season. The person swipes past a card to see the next, or taps the card to start the advertisement.

Two details follow from the networks' policies rather than from preference. Each advertisement starts only on a tap, because the person must opt in to each one [1]; the feed never plays the next advertisement on its own. And the reward is disclosed before each advertisement, because the policy requires it [1]. The disclosure is a constant, not a balance: it states what this one ad pays, never what the person has earned, how far they are from anything, or how many ads they have watched.

### 4.3 · What a finish is

A finish is the network's own completion event for a rewarded advertisement: the signal on which the network itself would grant a reward. The design adds nothing to it and takes nothing from it. Closing an advertisement before that signal earns nothing and costs nothing; the person returns to the feed where they were. There is no partial credit, because a partial credit would be a hidden balance accumulating toward a threshold the person cannot see.

### 4.4 · What the page refuses

| Refused | Why |
|---|---|
| autoplay into the next ad | each ad needs its own opt-in; autoplay is how a feed holds a person |
| a count of ads watched, a streak, a daily target, a progress bar | each is a meter on attention; a meter is what an engagement product optimizes |
| daily bonuses, multipliers, "watch 3 more for a bonus" | each pays more for *more*, which makes the operator's interest and the person's diverge |
| task lists, missions, referral rewards | the TikTok Lite program's structure; the Commission's concern [2] |
| playable or interactive ads in the feed | a game outcome would decide what is minted, which crosses the wall between play and currency (§10.3) |
| personalized ads | the page knows nothing about the person that it may sell, and targeting would make the price of each viewer's attention depend on the profile the operator built |
| a "running low" warning, a countdown to the next season | a rendered loss presses a person toward the page |

The person may look up what they hold, on a balance screen they open themselves. That is the one count the page shows, and only on request.

### 4.5 · Who may use it

Adults only. A person whose age the app does not know is not offered the page. The reason is not only legal caution. A minor's attention is the case the Commission named [2], and a child cannot weigh minutes of advertising against money they do not control.

---

## 5 · The credits

### 5.1 · A ledger of their own

Kernels are kept in a ledger separate from the person's money balance. The two never mix: advertising revenue never pays into the money balance, and a money balance never buys Kernels. A person who holds both sees two numbers, never a sum.

The separation matters for three reasons. A money balance that grew from watching advertisements would make the money side an advertising product. A combined figure would hide which part can be refunded (the money) and which cannot (the Kernels). And the money balance is a prepaid store of value with its own legal treatment, which a credit earned only by watching should not inherit or contaminate.

### 5.2 · Earned only, never bought

Kernels cannot be bought. The money balance is how a person pays; Kernels are how a person who would rather pay with time does so. Selling Kernels would add an exchange rate between money and Kernels, which would hide the price of every use behind a conversion, and it would turn Kernels into a purchased in-app currency, with the consumer-protection treatment that brings. The census found that an app granting a currency for ads also sells it [4]; this design refuses that step.

### 5.3 · What a person can and cannot do with them

| A person can | A person cannot |
|---|---|
| spend Kernels on a costly action in a THonly™ or Factory 333™ app, at its fixed Kernel price | withdraw them, cash them out, or redeem them for money or goods |
| hold them indefinitely | transfer them to another person, or receive them from one |
| see what they hold, on request | buy them |
| stop using the page at any time | spend them in any HeartBank® application |

Kernels never expire and are never taken back. Ending the page means stopping the minting of new Kernels; what a person already holds stays spendable until they spend it. A held credit is reduced only by its holder's own act.

### 5.4 · A fixed price per use, redeemed at cost

Each costly action has a price in Kernels that does not change: a render costs a fixed number of Kernels, and so does a unit of storage. What changes from season to season is how many Kernels a finished ad earns. Holding the use price fixed means a person always knows what their Kernels buy, and the season's rate is the only number that moves.

When a person spends Kernels, the operator redeems them against the measured cost of the computing they buy, with no margin. This is the property that answers the first question of §1.2. If Kernels were redeemed at the price a paying customer pays, which includes a margin, the operator's revenue would rise with every minute watched, and the page would sit on the attention economy's gradient. Redeemed at cost, the operator neither gains nor loses from a minute watched; any revenue above the reward goes to the free allowance (§6.4).

⚠️ *Disclosed as designed, not as ruled:* whether the operator's published margin on paid computing applies when Kernels are spent is an open decision for the operator. The paper discloses the at-cost form as the one that holds the property, and the margin form as a variant (§11.4) that does not.

---

## 6 · The rate, and what it can cost

### 6.1 · The average form, as first designed

Let a season be one year. During season *s*−1, every finish is recorded with two facts: the market it came from (the store or card country of the person's account, never the device's location) and the ad revenue actually received for it. Between seasons:

```
  R̄(s−1)  =  total revenue received in season s−1  ÷  number of finishes in season s−1

  r(s)    =  R̄(s−1) ÷ κ         Kernels per finish, for everyone in season s

  where κ = the measured compute cost that one Kernel stands for
```

*r*(*s*) is published before season *s* opens and frozen for its length. A swipe earns nothing; a finish earns *r*(*s*). The same number of Kernels per finish holds for every viewer in every market.

The design was first described as affordable by construction, on the reasoning that it pays out last season's average revenue and so cannot pay more than the ads bring in. That reasoning is wrong, and the next section is the case that shows it.

### 6.2 · Why the average does not bound spending

The average is taken over last season's *mix* of viewers. The payout is paid on this season's mix. If the two differ, the average is the wrong number, and a uniform reward is precisely the thing that makes them differ.

A worked case, with illustrative figures (not measurements):

```
  SEASON s−1                                   SEASON s
  market   share of    revenue per             market   share of    revenue per
           finishes    finish                           finishes    finish
  ───────  ─────────   ───────────             ───────  ─────────   ───────────
  high       40 %        $0.020                high       10 %        $0.020
  low        60 %        $0.002                low        90 %        $0.002

  R̄(s−1) = 0.4×0.020 + 0.6×0.002 = $0.0092     R̄(s)   = 0.1×0.020 + 0.9×0.002 = $0.0038

  rate frozen for s:  $0.0092 of compute per finish
  revenue per finish in s:  $0.0038
  ──────────────────────────────────────────────────────────────────────────────
  every finish in season s costs 2.4 × what it earns, and more finishes cost more
```

Why the mix moves in that direction: at a rate of $0.0092 of compute per finish, a viewer in the high market is paid 0.46 times what their own attention earns the operator, and a viewer in the low market 4.6 times. The page is a better deal the lower a market's ad prices, so the low market's share grows. Each season then pays the previous season's higher average to a lower-revenue mix, so the error has a known sign: the average form overspends for as long as the mix is still moving toward the low markets, and it is not even right on average.

Two further effects push the same way.

- **Revenue is revised after the reward is paid.** Ad networks deduct revenue for invalid traffic after the fact, sometimes after payment, without a per-impression breakdown. A Kernel, once minted, is never taken back (§5.3). Revenue later deducted is a permanent loss.
- **Kernels are spent later than they are earned.** A Kernel minted in season *s* may be spent in season *s*+3. Its cost falls due when it is spent, at that season's compute price, while the revenue that funded it arrived when it was minted. If the cost of a use rises, the Kernel's fixed price per use (§5.4) means the shortfall is the operator's.

The general form of this failure is old: a per-unit rate fixed from historical data and paid on a volume that responds to the rate [10]. The average form is disclosed (it is the census's survivor, and the form the operator first ruled), but it is not affordable by construction, and this paper does not say it is.

### 6.3 · Form B, the design: the lowest-market rate, in which every finish pays for itself

The case in §6.2 breaks the average form because the rate exceeds what a finish in a low market earns. The fix that removes the case is to set the rate no higher than what a finish earns in *any* market served:

```
  for each market m served in season s−1 (with at least a published minimum number of finishes):

      R(m, s−1) = revenue received in m  ÷  finishes in m

  r(s) = α × min over m of R(m, s−1) ÷ κ          0 < α ≤ 1, published
```

Now every finish in season *s* earns at least what its credits cost, whichever market it comes from, so a shift in the mix cannot produce a loss. The mix risk is removed by construction: no rule has to be enforced at the moment the mix moves. Three risks remain, and none of them is removed.

- **The price level can move.** If ad prices in the lowest market fall from last season to this one (a weak advertising year, a seasonal dip), a finish there can earn less than last season's figure. α below 1 is the margin against that, and §6.5 adds the breaker for a fall larger than the margin.
- **The lowest market sets everyone's pay.** If one market served pays almost nothing per finish, the rate is almost nothing for everyone. The minimum-volume threshold keeps a market with a handful of finishes from setting the rate, but a large, low market legitimately does. That is the honest cost of this form: it is equal at the bottom. §7 argues that the average form ends up near the bottom anyway, so the cost in equilibrium is small, and the cost out of equilibrium, while high-market viewers still use the page, is real.
- **Deductions after payment.** The margin between the rate and a market's revenue absorbs some, not all.

### 6.4 · Where the revenue above the reward goes

Under Form B, every finish in a market above the lowest earns more than its credits cost. That surplus is not kept by the operator. It funds the free allowance of §1.1, the first door, which serves people who watch nothing at all.

The routing matters for the argument of this paper, not only for its accounts. Under the average form, the surplus from high-market viewers is paid out to whoever watches most, wherever they live; it rewards hours. Under Form B, it is paid to the free allowance, which is equal per verified person and asks nothing of anyone; it rewards nobody for watching and serves everybody. The second is the rule the operator already follows for a related case (a render paid for by three advertisements, where the revenue above the render's cost funds the same allowance).

So the design delivers two kinds of equality at once, and they do not compete. Everyone who watches is paid the same per finish. Everyone, watching or not, shares equally in what the richer markets' advertising brings in above that.

### 6.5 · Form C: a fraction of the average, and a breaker

Form B removes the mix risk at the cost of paying at the bottom. A third form keeps more of the average and bounds the cost by a rule instead of a construction:

```
  r(s) = α × R̄(s−1) ÷ κ                         0 < α < 1, published

  during season s, after each finish:
      received(s)  = ad revenue received so far in season s, net of known deductions
      minted(s)    = κ × Kernels minted so far in season s
      if minted(s) > received(s):  stop minting, for everyone at once, until the next season
```

When the breaker trips, the page states one fact, once, in the place a person would look for it: *This season's Kernels are all given out. The page pays again on 7 January.* It never counts down, and nothing about it is shown outside the page. Advertisements already started still pay. Nothing already held is touched.

Form C is weaker than Form B in the sense this corpus cares about. Form B's bound holds with nobody watching it; Form C's holds only while the breaker is computed correctly, on revenue figures that arrive late and are revised. And a tripped breaker is felt by everyone at once, including the high-market viewers whose ads funded the season, while a single market's surge caused it. Form C is disclosed because it pays more than Form B while the mix is still rich, and because it is the only one of the three that bounds the *price-level* risk as well as the mix risk.

### 6.6 · The three forms side by side

| | (A) average | (B) lowest market | (C) fraction + breaker |
|---|---|---|---|
| rate | R̄(s−1) | α × min R(m, s−1) | α × R̄(s−1) |
| equal for every viewer | yes | yes | yes |
| frozen in-season | yes | yes | yes, until the breaker trips |
| bounded against a mix shift | **no** | **yes, by construction** | yes, by a rule |
| bounded against a price-level fall | no | only by the margin α | yes, by a rule |
| bounded against deductions after payment | no | partly | partly |
| who sets the rate | the season's average viewer | the lowest-revenue market | the season's average viewer |
| revenue above the reward | paid out to viewers | to the free allowance | to the free allowance |
| what flexes when revenue falls | nothing; the operator absorbs it | nothing | availability, for everyone at once |

The forms combine. Form B with a breaker (Form B's rate, Form C's stop rule) covers both risks, at Form B's rate.

**The design is Form B.** It is the only form whose bound against a shift in the mix holds with nobody enforcing it, and §7.2 argues that what it gives up, a higher shared rate while high-market viewers still use the page, could not have been relied on in any case. Forms A and C are disclosed as variants (§11).

---

## 7 · Who the rate is equal for

### 7.1 · Per ad, not per hour

The rule pays the same per finished advertisement. It does not pay the same per hour. In a market where advertisers bid for most slots, a person can finish many ads in an hour; in a market where many slots go unfilled, the same hour finishes fewer, because cards stall waiting for an ad that never comes. Vendor figures put fill rates well below high-income levels in emerging markets, and the operator's own experience of its first market is that no fill is common. So Kernels per hour still depend on where a person lives.

The paper states the claim at the width it holds: **the payout per finished ad is uniform; the payout per hour, and the price the advertiser paid, are not.** An unfilled card says one plain line (*No ad is available here right now*) and never blames the person or asks them to try again.

### 7.2 · Where the average ends up

Even if no high-market viewer ever leaves the page, the people for whom a uniform reward is the best deal are those whose attention the market prices lowest, and they will supply most of the finishes. People in high-income markets, who have more money and less spare time, can pay the money price instead, and mostly will. So the average in Form A drifts toward the revenue per finish of the lowest-revenue markets served, and in equilibrium the shared rate is roughly the lowest-revenue market's rate. The cross-subsidy that the average form promises, high-market advertising carrying low-market viewers, exists mainly while the mix is still moving.

This is the result that makes Form B less costly than it looks. If the average form ends near the bottom anyway, paying at the bottom from the start gives up little, and it gives up nothing that could be relied on.

### 7.3 · Why uniform here, when fair-work principles say local

Fair-work principles for platform labor benchmark pay to the worker's local living wage [9], and that rule is the right one for a wage: a wage is what a person lives on, and a living costs what it costs where the person lives. A Kernel is not a wage. It cannot be spent on rent or food; it buys a fixed quantity of computing, and computing costs the same in every country, because the servers are the same servers. Paying a uniform number of Kernels per finish is paying a uniform quantity of the same good for the same act. The paper does not claim that uniform pay is better than local pay for anything that a person lives on, and it would be a misuse of this design to cite it for that.

### 7.4 · What equality the design does guarantee

| Equal | Not equal |
|---|---|
| Kernels per finished ad, for every viewer, all season | Kernels per hour (fill differs by market) |
| the Kernel price of each use, for everyone | the revenue each finish earns the operator |
| (Form B) the share of above-reward revenue that funds the free allowance, per verified person | the number of ads a person chooses to watch |
| (§8) the per-person limit, if one is set | |

---

## 8 · Abuse

### 8.1 · Why a uniform reward attracts farming

Under a reward set by each viewer's market, a farm of fake viewers in a low-revenue market earns what that market's attention is worth, which is little. Under a uniform reward, it earns the global rate on attention worth less than the rate: a uniform reward makes the least valuable traffic the most profitable. And Kernels buy real computing, which has value even though it cannot be withdrawn.

Non-transferability blunts this. A farm cannot sell Kernels, because Kernels cannot leave the account that earned them, and the account cannot be sold through the app. What remains is a farmer earning computing for their own use, or selling accounts outside the app. Ad networks also detect and deduct invalid traffic, but after the fact (§6.2), and a Kernel already minted is not taken back.

### 8.2 · A per-person, per-season limit, in the mint function

The design's answer is a limit on paid finishes per verified person per season, equal for everyone, enforced in the ledger's own mint function: a finish beyond the limit mints nothing, because the function that mints Kernels checks the person's count before it writes. It is a property of the ledger, not a rule someone must remember.

A limit per *account* is evadable by opening accounts, so the limit binds per *person*, behind a proof of personhood: an attestation, kept separately, that the account belongs to a distinct living human, without revealing who [13]. One person, one limit, however many accounts.

The limit does three jobs at once. It caps what any one farmer can extract. It caps the operator's total liability for a season at *r* × the limit × the number of verified people, a number known before the season opens. And it caps the hours any one person can spend on the page, which is the kindness question of §9.

When a person reaches the limit, the page states it once, as a fact: *You have finished this season's B-Flicks. They pay again on 7 January.* It is never previewed (*3 left*), never counted down, and never mentioned outside the page.

⚠️ *Disclosed as designed, not as ruled:* the per-person limit is the authors' addition, made after the counterexample hunt, and the value of the limit is unset. It is claimed as a variant (§14, claim 6), not as the ruled form.

### 8.3 · Kernels minted by invalid traffic

If an account is later shown to be a bot, the Kernels it earned are not a person's holding, because there is no person; voiding them takes nothing from anyone. If a real person used an emulator or a script, the case is harder, and the design does not settle it here. The paper records it as an open question (§15) rather than claim a rule it has not ruled.

---

## 9 · Is it kind?

The strongest objection to the whole page is not economic. It is that a feed of advertisements, paid in something the person wants, asks the people with the least money to pay with the most hours, and that a feed which pays for watching is what the European Commission found "may stimulate addictive behavior" [2].

The design's answer has four parts, and the objection is not fully answered by them.

1. **The page is never the way in.** The free allowance and gifts come before any payment, so basic use of the apps never requires the page. A person goes to the page only to get more than the allowance gives, ahead of need, by choice.
2. **The page has none of the machinery the Commission named.** TikTok Lite's program paid points for tasks, including time spent and inviting friends. This page has no tasks, no time-based reward, no referral reward, no streak and no daily bonus (§4.4). It pays for a finished ad and nothing else.
3. **The hours are capped.** The per-person limit (§8.2) is also a limit on time, equal for everyone.
4. **The operator earns nothing from the hours.** Kernels are redeemed at cost and the surplus goes to the free allowance (§5.4, §6.4), so there is no revenue reason to make the page more absorbing.

What remains: a person with little money who wants more than the free allowance will still pay for it in minutes of advertising, and a person with money will not. The page does not make that inequality; the price of computing does. It offers a second way to pay that does not depend on money, at a price that does not depend on where the person lives. Whether that is a kindness or a toll depends on what the alternative is. Where the alternative is no access at all, it is the former. Where a free allowance large enough to cover a person's needs could be funded instead, the page is the weaker answer, and the free allowance is the stronger one. That is why Form B routes the richer markets' surplus to the allowance and not to the page.

---

## 10 · Where it may not run

### 10.1 · Never in a HeartBank® application

HeartBank® has published a permanent refusal of advertising revenue in any form. Nothing in this paper reverses or weakens it. The page exists only in THonly™ and Factory 333™ applications. Kernels are never spent in a HeartBank application. Revenue from the page never reaches HeartBank, and HeartBank earns nothing from advertisers through it. The two institutions share a founder and a sign-in; the separation is in the ledgers and the applications, and §13 withholds nothing about it.

### 10.2 · Never in an app built for ads

The page is a section of a functional application. App-store review rules bar applications designed predominantly to display advertisements, while permitting an app to reward a person for watching one [14]; a standalone app of only the feed would be the first kind. Ad-network rules also limit screens that carry more ads than publisher content [15]; whether that rule reaches a full-screen rewarded feed inside a functional app is not settled, and it is named as a risk in §15.

### 10.3 · Never across the wall between play and currency

Games, matches and contests may decide a story; they may not decide what is minted. A playable advertisement, in which the person plays a short game, would let the game's outcome decide whether a reward is earned. The page carries only advertisements whose finish is a time-based completion event.

### 10.4 · Never touching a gratitude count

Kernels and the advertising revenue behind them never touch any count of gratitude kept by HeartBank or anyone else: no thank, no aura, no measure of anyone's giving. A person's attention to an advertisement is not a kindness, and the design does not let it be recorded as one.

### 10.5 · Never to minors, never personalized

Adults only (§4.5). Advertisements are non-personalized, and the market used in the rate's computation is the account's store or card country, never the device's location.

---

## 11 · Variants

### 11.1 · Variant A: the average form

As in §6.1. Disclosed because it is the census's survivor and the form first designed. Not bounded (§6.2).

### 11.2 · Variants within the design (Form B)

The design is §6.3, with α and the minimum-volume threshold published. Variants within it: the minimum over markets replaced by a low published percentile (bounded only for the markets above it); markets grouped into published bands before the minimum is taken.

### 11.3 · Variant C: fraction and breaker

As in §6.5. Variants within it: the breaker computed on a published lag (revenue more than *d* days old only), trading speed for fewer revisions; the breaker set to trip at a published fraction of received revenue rather than at equality.

### 11.4 · Variant D: redemption with a margin

Kernels redeemed at the price a paying customer pays, including the operator's published margin. Disclosed because it is a natural implementation. It loses the property of §5.4: the operator's revenue then rises with minutes watched.

### 11.5 · Variant E: a season of a different length

A season of a quarter or a month instead of a year. Shorter seasons track a moving mix more closely and make Form A less wrong, at the cost of a rate that changes more often and a rule that is fixed for less time before the people it governs.

### 11.6 · Variant F: the rate stated in compute, not in Kernels

The rate published as a quantity of a named use (*one finished ad: one fifth of a render*), with no separate unit at all. It removes a name and a conversion, and it ties the rate to the price of one use, which then cannot change independently.

---

## 12 · The adversarial surface

### 12.1 · What the counterexample hunt killed and narrowed

Before this paper was drafted, a separate reviewer with no stake in the design tried to refute it. What it found, and what changed:

| Claim before the hunt | Finding | Status in this paper |
|---|---|---|
| affordable by construction | a lagged average paid on a moving mix overspends, with a known sign (§6.2) | **killed**; replaced by Forms B and C |
| a rule of equal value the market will not produce | the market already pays a fixed reward per ad unit by default; uniform pay across locations is a known labor rule [8] | **narrowed** to a *published, season-frozen commitment* tied to last season's revenue |
| the price of attention cut loose from where a person lives | equal per ad, not per hour; fill differs by market (§7.1) | **narrowed** to per finished ad |
| high-market ads carry low-market viewers | in equilibrium the average approaches the lowest-revenue market's rate (§7.2) | **narrowed**; the cross-subsidy moved to the free allowance (§6.4) |
| access to compute for people without money | the free allowance already takes rich-market surplus for people who watch nothing | **kept**, with the surplus routed to the allowance, not the page |
| a feed of only ads | network rules require an opt-in and a reward disclosure before each ad; stores bar ad-only apps [1][14][15] | **kept**, as a page inside a functional app, one tap per ad |

### 12.2 · Remove the enforcer: which guards are properties

A guard is a property if it holds when nobody is enforcing it at the moment it is tested, and a rule if it needs an enforcer then.

| Guard | Property or rule | Why |
|---|---|---|
| a skipped ad earns nothing | **property** | minting is triggered only by the network's completion event |
| Kernels cannot be withdrawn, transferred or bought | **property** | the ledger has no withdrawal, transfer or purchase operation to call |
| Kernels never expire | **property** | the ledger has no expiry operation |
| Kernels never reach a HeartBank app | **property**, if the HeartBank apps have no interface to the Kernel ledger | **rule** if they share an interface and a check prevents the call |
| equal rate for every viewer | **property** | the rate is one published number with no per-person input |
| Form B bounded against a mix shift | **property** | every market's revenue per finish ≥ the rate, by how the rate was computed |
| Form C bounded against a price fall | **rule** | the breaker must be computed, on late and revised data |
| per-person limit | **property**, in the mint function; **rule** at the proof of personhood | the count is checked where Kernels are written; whether two accounts are one person depends on an attestation |
| no prompt routes a person to the page | **rule** | nothing in the object stops a designer from adding one |
| redeemed at cost | **rule** | the redemption price is a published number the operator could change |

The last two are rules, and they are the two that keep the page from becoming an engagement product. That is the most important thing this table says. The structure can make the page bounded and fair; it cannot by itself make the page non-intrusive. Publishing these rules is what makes a breach visible, not what makes it impossible.

---

## 13 · What is disclosed and what is withheld

The mechanism is designed and not built, and building it is scheduled behind a measurement that has not yet been made: what a finished ad actually earns, by market, in the operator's own apps. Under this corpus's rule for unbuilt, unscheduled designs, the claim is published and the specification is withheld.

**Disclosed:** every element in §4–§11 at the level a person skilled in mobile advertising and ledger design could build from: the page's entry and refusals, the finish event, the Kernel ledger's operations and the operations it lacks, the three rate formulas and the breaker, the routing of above-reward revenue, the per-person limit and where it is enforced, and the exclusions.

**Withheld:** the ad-network integration and mediation configuration; fraud and invalid-traffic thresholds; the values of α, κ, the minimum-volume threshold and the per-person limit; the Kernel prices of individual uses; the screen designs beyond what §4 states. None of these is needed to practice the claims, and each depends on measurements not yet made.

---

## 14 · Enumerated claims

The claims below are the census's survivor (claim 1) and the bounded forms the counterexample hunt made necessary (claims 2–8). Claims 2–8 were designed after the quick census ran and have not been searched separately; the full census owed before the first archival deposit must search them, and any it kills will be withdrawn in a revision.

1. A computer-implemented method of opt-in rewarded advertising, comprising: presenting, within a section of a functional software application reached only by a user's own navigation, a vertical feed in which every item is a rewarded video advertisement; starting each advertisement only on the user's action; crediting the user, upon the advertising network's completion event for an advertisement and not otherwise, with a quantity of in-application credits that are non-withdrawable, non-transferable and non-expiring, are kept in a ledger separate from any monetary balance of the user, and are redeemable only for computing services within applications of the publisher; wherein the quantity credited per completed advertisement is the same for every user in every market, and is set once per season, for all users, from the average advertising revenue per completed advertisement in the preceding season, published before the season begins and held fixed for the season.

2. The method of claim 1, wherein the quantity credited per completed advertisement is instead set from the lowest advertising revenue per completed advertisement among the markets served in the preceding season, each market having at least a published minimum number of completions, multiplied by a published factor not greater than one, such that each completed advertisement in any market earns at least the cost of the credits it mints.

3. The method of claim 1 or 2, wherein, during the season, the credits minted are compared with the advertising revenue received in that season net of known deductions, and minting is suspended for all users at once for the remainder of the season when the cost of the credits minted exceeds that revenue, credits already held being unaffected.

4. The method of claim 2 or 3, wherein the advertising revenue received for completed advertisements in excess of the cost of the credits minted for them is applied to a usage allowance provided equally to each verified person, without regard to whether that person watches advertisements.

5. The method of any preceding claim, wherein credits are redeemed against the measured cost of the computing services they purchase, without margin, such that the publisher's revenue does not increase with the number of advertisements a user completes.

6. The method of any preceding claim, wherein the number of completed advertisements for which credits are minted is limited per verified person per season, the limit being equal for all persons and enforced in the operation that writes credits to the ledger, and the person's distinctness being established by a proof of personhood that does not identify the person.

7. The method of any preceding claim, wherein the credits cannot be purchased with money, and the user's monetary balance is never credited from advertising revenue.

8. The method of any preceding claim, wherein the market of a completion is determined from the store or payment-card country of the user's account and never from the location of the device, and the advertisements are non-personalized and exclude playable or interactive formats whose outcome would determine whether credits are minted.

---

## 15 · Honest limits

- **Nothing here is built or measured.** Every number in §6 is illustrative. The design waits on a measurement of what a finished ad earns, by market, in the operator's own apps, and nothing in this paper predicts that figure.
- **The census was quick and English-only.** The category's largest body of practice is Chinese, and it was not read. Claims 2–8 were not searched at all. A full census is owed before the first archival deposit, and it may narrow or kill claims.
- **Form B pays at the bottom.** Its bound is real, and so is its cost: one large low-revenue market sets everyone's pay. The argument that the average form ends near the same place (§7.2) is a prediction, not a measurement.
- **Form C's bound is a rule on late data.** Ad revenue arrives late and is revised. A breaker computed on it can trip late or not at all.
- **Price-level risk is not removed by any form.** If advertising prices fall across all markets in a season, Form B's margin α is the only protection, and α is unset.
- **The liability is permanent.** Kernels never expire. A season's Kernels may be spent years later, at compute prices nobody can know now, and the operator bears any rise. The per-person limit caps the size of each season's liability; nothing caps its duration.
- **Invalid traffic and #68.** Whether Kernels minted by a real person using a script are a holding that cannot be voided is not settled (§8.3).
- **Two of the guards that matter most are rules.** No prompt routes a person to the page, and Kernels are redeemed at cost: both are published commitments, not properties (§12.2).
- **Platform risk.** Network rules on screens with more ads than content [15], and on opting in to each ad [1], may limit or bar a feed of rewarded ads in the form described. This has not been tested with any network.
- **Kindness is argued, not shown.** §9 is an argument about design. Whether the page is experienced as a fair way to pay or as a toll on people with little money is an empirical question this paper cannot answer.
- **Legal treatment is unknown.** Earned-only, non-transferable credits sit near exclusions in consumer and payments rules in some jurisdictions; no jurisdiction's treatment has been checked by counsel, and Cambodia's has not been checked at all.

---

## 16 · Predictions

Proposed for the authors' public register of predictions; **not registered**, and to be registered, if at all, only before any data from a live page exists.

1. **The mix moves toward low-revenue markets.** Under a uniform rate, the share of finishes from the lowest-revenue market served rises from the first season to the second.
2. **The average falls.** Under Form A, R̄ falls from the first season to the second, and the second season's payout exceeds its revenue.
3. **Form B does not overspend on mix.** Under Form B, no market's revenue per finish in a season falls below the rate, except where advertising prices in that market fell from the prior season.
4. **Most people never use the page.** A large majority of active users never open the page in a season, because the free allowance and payment cover their needs. A page used by most people would suggest the allowance is too small.

---

## Coda

An advertisement does not know where it is shown, and neither does the server that renders the image a person pays for with it. The price of attention is set by the advertiser's guess about the viewer's wallet; the price of computing is set by electricity and silicon, which cost the same everywhere. This design lets the second price govern the reward, and it confines the first to the accounts, where its surplus goes to people who watch nothing. Most of what it claims is already in the world. What it adds is a decision written down in advance, and the arithmetic that keeps the decision honest.

---

## Terms

| Term in this paper | Standard term |
|---|---|
| B-Flick℠ | one rewarded video advertisement in an opt-in vertical feed |
| the page, B-Flicks | an opt-in rewarded-ad feed within a functional app |
| Kernels | non-transferable, non-withdrawable, non-expiring in-app reward credits |
| a finish | the ad network's reward-completion event |
| a season | the rate period (one year, 7 January to 7 January) |
| the rate *r*(*s*) | reward per completed rewarded ad, fixed for the period |
| the free allowance | a free usage allowance, equal per verified person |
| the market | the account's store or payment-card country |
| the breaker | a budget stop on reward minting |
| proof of personhood | an attestation that an account belongs to a distinct living human |

---

## Author Contributions and AI Disclosure

The mechanism's terms (a page of only ads, chosen willingly; credits that stay in the app; the same earnings for every viewer everywhere) are the founder's, ruled in November 2026. The rate's season-frozen form, the analysis of §6–§9, the bounded forms and the per-person limit were developed by Miss Aquarius℠, the name under which this corpus discloses its AI collaboration. The founder chose the lowest-market form (§6.3) as the design on 2026-11-14, after the counterexample hunt; the remaining additions are disclosed as designed, not as ruled. The counterexample hunt that changed §6 was run by a separate AI reviewer with no part in drafting. Thon Ly holds editorial control.

## Trademark Notice

B-Flick℠, THonly™, Factory 333™, HeartBank® and Miss Aquarius℠ are marks of their respective owners within the HeartBank® family. *Kernels* is a plain word, not a mark. The CC0 dedication covers the mechanism under any name and does not license the marks.

## Citations

1. Google AdMob Help. *Policies for ad units that offer rewards.* support.google.com/admob/answer/7313578. Read 2026-11-14.
2. Music Business Worldwide. *TikTok drops Lite Rewards program in EU permanently* (reporting the European Commission's 2024-08-05 announcement). musicbusinessworldwide.com/tiktok-drops-lite-rewards-program-in-eu-permanently/. Read 2026-11-09.
3. US 8,005,713 B1. Google Patents, patents.google.com/patent/US8005713B1/en (priority 2000-11-08; shown as expired 2025-04-26). Read 2026-11-09.
4. AIArtGen, App Store listing, apps.apple.com/app/id6737144362. Read 2026-11-09.
5. ITRex Group. *Mobile advertising platform for an adtech startup* (case study). itrexgroup.com/case-studies/mobile-advertising-platform-for-adtech-startup/. Read 2026-11-09.
6. US 2011/0191151 A1. Google Patents, patents.google.com/patent/US20110191151 (priority 2010-02-01). Read 2026-11-09.
7. Monamedia, App Store listing, apps.apple.com/app/id6751844726. Read 2026-11-09.
8. Heinemeier Hansson, D. *Basecamp doesn't employ anyone in San Francisco, but now we pay everyone as though all did.* Signal v. Noise, 2017-12-22. Read 2026-11-14.
9. Fairwork. *Fairwork principles.* fair.work/en/fw/principles/ (read through a search summary only).
10. Carter, G. M., Newhouse, J. P. & Relles, D. A. (1990). How much change in the case mix index is DRG creep? *Journal of Health Economics* 9(4), 411–428. doi:10.1016/0167-6296(90)90003-L (cited from the abstract and catalog records).
11. Ly, T. & Miss Aquarius℠. *The Fractal Three-Level Architecture.* thonly.org/research/fractal-three-level-architecture.
12. Ly, T. & Miss Aquarius℠. *The Zero-Point Game.* thonly.org/research/zero-point-game.
13. Ly, T. & Miss Aquarius℠. *B-PoH: A Humanity Layer for the AI-Native Internet.* thonly.org/research/b-poh-humanity-layer-ai-native-internet.
14. Apple. *App Review Guidelines*, 3.2.2 and 4.2. developer.apple.com/app-store/review/guidelines/. Read 2026-11-14 (by the counterexample reviewer).
15. Google Publisher Policies. *More ads or paid promotional material than publisher-content.* support.google.com/publisherpolicies/answer/11169917. Read 2026-11-14.
16. Ly, T. & Miss Aquarius℠. *The Zero-Employee Institution.* thonly.org/research/the-zero-employee-institution.
