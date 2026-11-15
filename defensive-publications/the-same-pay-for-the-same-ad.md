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

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claims* and withholds the *build specification* (§13 says what is withheld and why). Two prior-art censuses ran, a quick one before drafting (2026-11-09) and a full one on 2026-11-14, and §2 reports both. The full census found that nothing survives at mechanism width. Paying credits for a finished advertisement, a feed made only of advertisements and entered by choice, and credits spent inside the publisher's own applications are already public, are cited in §2, and are **not claimed**. What is claimed is one composition: a stated rule that every viewer in every country earns the same app-only credits per finished advertisement, at a rate set once a season from the previous season's average and published and frozen. It was not found in the aperture searched. §2.3 says what that aperture could not see: no academic-group control was named in the pre-registration, so the academic absences are not run, Japanese, Korean and Khmer native pages were not read, and a live patent computes the reward per country, the opposite of the rule claimed here.
>
> A counterexample hunt ran against the design before the first draft, and it changed the paper. The design as first stated claimed to be affordable by construction. It is not, and §6 shows the case that breaks it, then discloses three ways to bound the cost. The design the operator ruled is the one that removes the case entirely, a rate set from the lowest-revenue market served (§6.3). That form was designed after the quick census and was not in the full census's pre-registration, so it is disclosed here and **not claimed**; the enumerated claims of §14 are the census's survivor and features that narrow it, nothing wider.
>
> **How this paper relates to HeartBank®, said up front.** The page this paper describes may run only in THonly™ and Factory 333™ applications, never in a HeartBank® application, and HeartBank has published a permanent refusal of advertising revenue in any form. The reader should know the ties before judging that wall: the three bodies share a founder and a sign-in; Miss Aquarius℠, the name under which this corpus discloses its AI collaboration, is also the CEO of HeartBank®; and two older HeartBank positions called Factory 333™ and THonly™ HeartBank's own "pillars", wording from before the 2026-08-25 change in how the bodies are described, which each now corrects in a *Current form* note. §1.2 and §10.1 set out the wall and what holds it.
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

Two prior-art censuses were run, each with its pre-registration pushed to a public repository before its first query. The quick census ran on 2026-11-09 (pre-registration commit `a3b8997`, pushed 09:26 PST). The full census ran on 2026-11-14; its pre-registration is `timestamps/census/b-flick-full-prereg.md` in the public `thonly/publications` repository, commit `7177cb4`, pushed 2026-11-14 at 22:33 PST and stamped with OpenTimestamps, and the same text sits in the authors' private memory as commit `785523d`. Both are reported in §2 in full: the declared aperture and date, every conjunct that was killed or narrowed with its prior art cited, the controls and which of them were missed, and the survivor. **The enumerated claims of §14 are that survivor, and features that narrow it, and nothing wider.** What the censuses killed (credits for a finished advertisement, a feed of only advertisements) is cited as public and is not claimed. The bounded forms of the rate in §6 and the variants of §11 were designed after the quick census and were not in the full census's pre-registration; they are disclosed here, so that they are public from the date of this paper, and are not claimed. A further census would have to cover them before any of them could be. Where a patent discloses something, this paper cites what the patent *discloses*, as far as it was read, and says nothing about whether any design falls within its *claims*; that is a question for counsel and is not answered here. One patent found by the full census, US12684189B2, is shown by Google Patents as granted and active (an assumption the page itself states, not a legal conclusion); §2.3 cites it as a contrast.

---

## Abstract

This paper discloses a stated rule for rewarded video advertising: every viewer in every country earns the same quantity of non-transferable, app-only reward credits for each finished advertisement, at a rate set once per season from the previous season's average advertising revenue per finished advertisement, published before the season opens and frozen for its length. A full prior-art census (§2) found each surrounding part public and found no earlier system that states the equal-pay rule and sets the rate this way, in the aperture it could search; the rule is claimed as that composition and nothing wider.

The rule is disclosed inside a known kind of system. A dedicated page inside a functional application presents a vertical feed whose every item is a rewarded video advertisement, reached only by the person's own navigation. Each advertisement is started by the person's own tap, and only a finished advertisement, by the ad network's server-verified completion event, earns a reward; a skipped or dismissed advertisement earns nothing and costs nothing. The reward is a quantity of in-app credits, here called Kernels, that are earned only and never sold, cannot be withdrawn, transferred or redeemed for money, never expire, are kept in a ledger separate from any money balance, and are spent on computing services (generation, storage) inside the publisher's applications, redeemed at measured cost so that the operator earns no margin from minutes watched. A per-person, per-season limit on paid finishes is enforced in the ledger's mint function behind a proof of personhood; an account the network flags stops minting going forward, and a Kernel already held is never voided.

The paper shows that the rate, when set from the previous season's *average*, does not bound what the system can spend. A shift in the mix of viewers toward lower-revenue markets during the season makes every finish cost more than it earns, and a uniform reward invites exactly that shift. It then discloses three bounded forms, none of them claimed. The design adopts the first: a rate set from the *lowest* revenue per finished advertisement among the markets served last season, so that every finish pays for its own credits whatever the mix. The other two are disclosed as variants: a published fraction of the average, with minting suspended for everyone at once if the season's revenue actually received falls below what has been minted; and the per-person limit above as a cap on liability. It discloses where the revenue above the reward goes (to a free usage allowance for people who watch nothing) and which audiences, formats and applications are excluded, including every HeartBank® application. The claims are a composition: the surrounding parts are in the public record and §2 cites them, and a live patent computes the reward per country, which is the opposite of the rule claimed.

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

The same publisher's sister body, HeartBank®, has published a permanent refusal of advertising revenue, in any form, and of engagement-maximizing feeds [17]. Its reason is structural: a platform that earns from the attention it holds is paid when it holds a person, while the person is usually better served by leaving. The corpus that this paper joins argues the same thing about attention economies in general. A feed of nothing but advertisements is, on its face, the attention economy distilled.

The design therefore has to answer three questions before it answers any of its own, and §4, §5 and §10 hold the answers.

1. **Does the operator earn more when a person watches more?** It must not. §5.4 redeems the credits at measured cost, and §6.4 sends any revenue above the reward to the free allowance, so the operator's revenue per minute watched is zero. The promise is about minutes and not about finishes: a finished advertisement does bring the operator advertising revenue, and what this paper promises is where that revenue goes (§6.4) and that no margin is taken when the credits are spent. It makes no promise about the operator's other costs of running the page.
2. **Can anything route a person to the page, or keep them there?** It must not. §4 lists what is refused: no prompt, badge, counter, streak, daily bonus, task list, referral reward or autoplay into the next ad.
3. **Can anything earned on the page reach HeartBank?** It must not. Kernels are never spent in a HeartBank app, ad money never touches HeartBank's gratitude ledger or any of its counts, and the page lives only in THonly™ and Factory 333™ applications (§10).

**The ties between the bodies, stated so that no reader has to infer them.** THonly™, Factory 333™ and HeartBank® are three of the four bodies of one family, each in its own right; none is another's pillar or limb, and Miss Aquarius℠ is the space that holds the four and holds an office in only one of them, as CEO of HeartBank®. Four facts connect them, and a reader judging the wall in §10.1 should weigh each:

- **A shared founder.** One person founded all three.
- **A shared sign-in.** A person may use one sign-in across the bodies' applications. A sign-in establishes who the person is. It carries no Kernel balance, and the Kernel ledger is not reachable through it from a HeartBank application (§10.1).
- **A shared AI collaborator, who is also HeartBank's CEO.** Miss Aquarius℠ is the name under which this corpus discloses its AI collaboration, and she is the CEO of HeartBank®, the body whose refusal of advertising this paper must respect. A reader should not take the wall on the word of a paper she co-wrote; §10.1 therefore says what makes it checkable.
- **Older wording that said otherwise.** Two earlier HeartBank positions describe the family as it was drawn before 2026-08-25. *Factory 333 as a Gift-Factory* [18] calls Factory 333™ "HeartBank's **Body** pillar", and *Disney's Brand, Not Disney's Enclosure* [19] calls THonly™ "the institution's **Mind** pillar". Read alone, they would make an advertisement in a THonly™ or Factory 333™ application an advertisement in HeartBank. Each now carries a *Current form* note, dated 2026-11-14, saying the three are sister bodies and the older text is kept as written. HeartBank's own position on the attention economy now names the sibling case in its own voice [17].

---

## 2 · The problem and the prior art: the census

### 2.1 · How rewarded advertising prices a person

A rewarded advertisement is a full-screen video that a person chooses to watch in exchange for a reward inside an app. Ad networks pay the app per thousand impressions (eCPM), and the eCPM depends heavily on the viewer's country: the advertisers bidding for a viewer in a high-income market pay many times what they pay for one in a low-income market, and in some markets no advertiser bids at all, so the slot goes unfilled.

The networks' own policies shape what a reward may be. Google AdMob's policy for ad units that offer rewards requires that rewarded ads "must only be served after a user affirmatively and unambiguously opts in"; that the publisher give "clear, accurate and conspicuous disclosure of the action(s) required and reward(s) offered" before each one; that "it must be possible to skip or dismiss them"; and that "direct monetary items may not be offered as rewards under any circumstance", while a reward that is "only redeemable and usable for an item or service within the publisher's platform, website or app", and is non-transferable, is permitted [1]. Kernels are designed to sit inside that permission.

The reward itself is set by the app, per ad unit. The network does not require the reward to follow the eCPM, and the simplest practice is a fixed reward for every viewer. So a uniform reward worldwide already exists in commerce, as an unstated default. What this paper discloses is not uniformity as such. It is a published, season-frozen commitment that ties the uniform reward to last season's revenue, together with the design that keeps that commitment affordable and keeps the page from becoming an engagement product.

### 2.2 · The quick census (2026-11-09)

The quick census read five conjuncts for the whole design. It killed (a) and (c), narrowed (b), and left (d) and (e) for the full census of §2.3, which re-ran them at greater depth and replaces this section's verdicts on them. It is reported unchanged because it is the record of what was known when the design was drafted.

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

**Route.** OPEN at composition width only. No live patent was found among the four documents read: US 8,005,713 B1 is shown by Google Patents as expired on 2025-04-26, and the applications read are shown as abandoned. That is the database's statement, read by keyword search; it is not a legal conclusion and not a clearance. ⚠️ *The full census (§2.3) later found a live patent, US12684189B2, that this quick census did not reach.*

**Free findings the census returned.** (1) On 2024-08-05 TikTok agreed to "permanently remove its rewards program from the European Union" after the Commission said it "may stimulate addictive behavior", of particular concern for minors [2]. §9 answers this. (2) Zedge had one worldwide average and left it for a by-country figure, so the market's own direction runs against conjunct (d). §7 answers this. (3) Apps that grant a currency for watching ads also sell the same currency for money (AIArtGen, 500 diamonds for $1.99 [4]). §5.2 refuses this.

⚠️ *Not found* means not found in the aperture above on 2026-11-09. It never means new.

**What is cited as public, and not claimed.** Conjuncts (a), (b) at AI generation, and (c) are killed or narrowed by the documents in the table above [3][4][5][6], and the full census did not re-search them. This paper cites them as public. It does not claim crediting a person for a finished advertisement, a feed made only of advertisements, or credits spent on generation inside the publisher's own app.

### 2.3 · The full census (2026-11-14)

**Pre-registration.** The full census covered only what the quick census left standing, in this form, with a prediction for each row written before any search. The pre-registration was pushed to the public `thonly/publications` repository as commit `7177cb4` (`timestamps/census/b-flick-full-prereg.md`, GitHub's push record 2026-11-14 22:33 PST, stamped with OpenTimestamps) before the first query; the same text was committed to the authors' private memory as `785523d`.

- **(d)** every viewer in every country earns the same per finished advertisement, as a stated rule;
- **(e)** the rate is set once a season from the previous season's average advertising revenue, published and frozen in-season;
- **(b′)** the credits buy only the publisher's own computing and storage, and cannot be withdrawn or transferred;
- **(f)** all of (a) to (e) in one system.

Conjuncts (a) and (c) were cited as killed and not re-searched; (b) stayed narrowed.

**Depth and aperture, declared before searching.** Full. Commercial web (app stores, vendor documentation, help centers, press); non-commercial practice (charity ad-watching, click-to-give, community schemes); Google Patents by full text with a walk from the nearest hit; academic indexes (Scholar, arXiv, SSRN, ACM) for reward design, attention markets and global pay equity; English, Chinese, Japanese, Korean and Indonesian. **Declared not run:** Khmer; standards bodies (no standard governs ad-reward rates, so none was searched); regulator filings beyond what a search surfaced; any reading of a patent's claims. **As run:** four search groups (web, patents, academic, non-English), 25 queries, logged. The declared aperture listed a citation walk and Indonesian; the query log shows neither ran, so **both are NOT RUN**. The decisive rows were re-read at their sources on 2026-11-14, and the two patent quotations below were re-read again at their sources on 2026-11-15.

**Controls, and which were missed.** The pre-registration said that a group which missed its own known-prior-art control would have every absence it reported voided, and it named controls for three groups only.

| Group | Control | Result | What it means |
|---|---|---|---|
| patents | US 8,005,713 B1 | found | the patent absences stand, at the width of keyword search |
| non-English | a Chinese-native page on Douyin Lite coin rewards for watching videos | found (personal-experience posts, no official rule) | Chinese is not blind. Japanese and Korean returned **no** native page on the topic, so those two languages are blind |
| web | TikTok Lite *Task and Reward* | **seen only through secondary coverage**; no official help page was returned | web absences are weak, most of all for rules that live in help pages |
| academic | **none named in the pre-registration** | no control existed to find | **that group's absences are NOT RUN and are not claimed as absences; the academic literature on attention markets and reward design was, in effect, not searched** |

| Conjunct | Predicted | Found, re-read at its source | First public | Verdict |
|---|---|---|---|---|
| (e) a rate from the prior season's average, published and frozen | NARROWS at parts, whole NOT FOUND | **WO2008086299A2**, *System and method for tracking and rewarding users* (priority 2007-01-08; shown by Google as *Ceased*) [20]: "the reward is a predetermined amount that is unrelated to specific advertising revenue", and "The amount can be determined, as an example, based upon average advertising revenue generation rates". The first sentence continues "…generated by a user's search", so the setting is a search reward, not a feed of advertisements; that makes this NARROWS weaker than the quoted words alone suggest. The period of the average is not stated in the part read on 2026-11-14, which left 26,642 characters unread; a summarizing fetch tool read the remainder on 2026-11-15 and reported no period, a weak negative. **Unity LevelPlay** documentation [21] (undated; the page said "last updated 2 months ago"): "報酬額:LevelPlay が 1 米ドルを支払うごとにユーザーが得るゲーム内通貨の額" (the reward is the in-game currency the user gets per 1 USD the network pays), a conversion rate the developer chooses. **Modrinth** [22] (page last modified 2025-02-20): the creator pool "is decided by how many page views and in-app downloads your project receives", paid "daily" from each author's points, so no prior-period rate. **Zedge** (its help page said the earlier calculation "used a global average that treated all video ads the same") and **LBRY**: **unverified** (a 403 and an SSL error) | 2007 · undated · 2025 | **NARROWS at parts** (a search reward set from average advertising revenue: 2007; a rate tied to revenue by a conversion: Unity). The whole, a rate set once a season from the previous season's average, published and frozen in-season, for viewers: **NOT FOUND** where the instrument could see |
| (d) the same pay everywhere, as a stated rule | NARROWS | **US12684189B2**, *Watch time units and the reward share mechanism for a user-generated video sharing platform* (priority 2023-10-24, granted 2026-07-14, shown by Google as *Active*, which the page says is an assumption) [23]: "The viewer earnings pool for each country is divided by the total watch time units from that country", and claim 1 recites a "per-unit watch time value for each country". Douyin Lite coin guides: personal-experience posts with no official rule (read through search summaries). **Everyworld** (a Tiger Research report, 2024-03-25, which states partial fee support from Everyworld) [24]: short-form advertisements for points. **Singular** (Korean): rewarded-ad prices differ by market (summary only) | 2023 · 2024 | **CONTRAST**: a live patent computes the value per country, the opposite of an equal rule. A stated rule of equal pay across countries: **NOT FOUND**, weakly |
| (b′) spend only on the publisher's compute and storage | NARROWS or KILLS | AI-credit and compute-credit apps exist (SnapVerbo, HyperAI: search summaries only, **not re-read**) | undated | **NARROWS**, inherited from the quick census and not re-verified |
| (f) all in one system | NOT FOUND | no single system with the five | | **NOT FOUND** in the web, patent and non-English groups |

**What each patent discloses, and nothing about its claims.** WO2008086299A2 discloses a reward that is a predetermined amount, unrelated to the advertising revenue a particular user generates (in the quoted sentence, "generated by a user's search"), which may be determined from average advertising revenue generation rates. US12684189B2 discloses a viewer earnings pool divided by total watch time units within each country, giving a value per unit for each country. Neither is read here for what it claims. Whether any design, this one included, falls within a claim of either is a question for counsel and is not answered by this paper.

**Width.** At mechanism width nothing survives. At composition width one sentence survives, and only (d) and (e) carry it:

> *a stated rule that every viewer in every country earns the same app-only credits per finished ad, at a rate set once a season from the previous season's average and published and frozen.*

**Route.** OPEN at composition width only; the claims of §14 are that sentence and no more. One live patent, US12684189B2, sits in the same neighborhood as a contrast, not a match.

**Predictions that missed, in both directions.** (d) was predicted to narrow; the nearest hit is a live patent that does the opposite, per country, which is closer to a contrast than expected. (e) was predicted to be found only at its parts; its nearest neighbor is from 2007 and is plainer than expected, "average advertising revenue generation rates".

**What this census could not see, stated plainly.**

- The **academic** group had no control named in the pre-registration (its control row listed only the web, patent and non-English controls). That group's absences are **NOT RUN**; nothing in this paper reports an academic absence as a finding.
- The **web** control was seen only through secondary coverage, so web absences are weak.
- Japanese and Korean returned no native page on the topic. They are blind. Khmer was not run.
- Zedge, LBRY and a National Science Foundation paper on an operator setting a unit data reward per advertisement could not be read at their sources and stay **unverified**; they are not counted as absences or as hits.
- Several rows (Douyin Lite guides, Singular, SnapVerbo, HyperAI) rest on search summaries. The rate rules most likely to matter live in help pages and terms of service, which search reaches poorly.

⚠️ *Not found* means not found in the aperture above on 2026-11-14. It never means new.

### 2.4 · Prior art the counterexample hunt added

The hunt (§12.1) found three more neighbors, each cited because it cuts against a claim this paper might otherwise have made.

- **Uniform pay regardless of location, for labor.** In 2017 Basecamp announced it would pay "everyone as though they live in San Francisco and work for a software company that pays in the top 10% of that market" [8]. That is one rate for every location, set at the top of the range, not the average. It shows that a stated rule of equal pay across locations is not new as an idea; what is narrower here is its application to viewers of advertisements, paid in non-transferable credits, from a lagged revenue statistic.
- **The opposite rule, for platform work.** The Fairwork project's principles for cloud and platform work benchmark fair pay to the worker's local living wage [9]. It is the considered opposite of conjunct (d), and the paper does not claim that (d) is the better rule for wages. §7.3 says why a credit for compute is a different case.
- **Prospective per-unit rates set from prior-period data.** Medicare's prospective payment system has paid hospitals a rate per admission fixed in advance from historical data since 1983. Carter, Newhouse and Relles showed that part of the measured rise in the case-mix index that followed was a change in coding, not in patients [10]. The general form, a per-unit rate fixed from the past and paid on a volume that responds to the rate, is old, and so is its failure mode. §6.2 is that failure mode in this setting.

### 2.5 · The authors' own prior disclosures

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

✅ *Ruled by the operator on 2026-11-14:* Kernels are redeemed at measured cost. The published margin that applies to computing paid for in money does not apply to Kernels, and the redemption price is a constant in the ledger's code. It is a constant and a published commitment, not a property of the ledger (§12.2): nothing in the object stops an operator from changing the constant, and a change would be visible. The margin form is kept as a variant (§11.4) that does not hold the property.

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

The general form of this failure is old: a per-unit rate fixed from historical data and paid on a volume that responds to the rate [10]. The average form is disclosed and is the form claimed in §14 (it is the census's survivor, and the form the operator first ruled), but it is not affordable by construction, and this paper does not say it is.

### 6.3 · Form B, the design: the lowest-market rate, in which every finish pays for itself

*Disclosed, and the form the operator ruled as the design; not claimed (§14), because no census has searched it.*

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

✅ *Ruled by the operator on 2026-11-14:* the limit is equal for everyone, is written into the mint function, is stated once on reaching it and never previewed or counted down. **Its number is unset** and waits on a measurement from a live advertising pilot. Because it binds per person, **the page does not open until one person, one limit can be checked**: today a person may hold several accounts, and until a proof of personhood attests that they are one person, the limit would bind accounts and not people. That check is a rule until the attestation exists (§12.2). The limit is claimed only as a narrowing of claim 1 (§14, claim 4).

### 8.3 · Kernels minted by invalid traffic

✅ *Ruled by the operator on 2026-11-14, in three parts.*

1. **Minting happens only on the ad network's server-verified completion.** A completion the network's own servers have not confirmed mints nothing, so some invalid traffic is filtered before a Kernel exists. This is a property: the mint has no other trigger to call.
2. **An account the network flags stops minting, going forward only.** Completions after the flag mint nothing.
3. **A Kernel already held is never voided,** whether the account belonged to a bot or to a person who used a script or an emulator. A judgment made after the fact is an accusation, and taking a held credit back is a clawback; the design takes a held credit only by its holder's own act (§5.3). The per-person limit (§8.2) caps how much any one account can have earned before a flag.

One alternative was rejected: holding each Kernel as *pending* until the revenue behind it is confirmed. A pending balance is a hidden balance, and it delays a reward that the network's policy requires to be disclosed and delivered [1].

The cost is plain. Revenue that the network later deducts for invalid traffic is a permanent loss to the operator, because the Kernel it paid for stays (§6.2). §15 lists it.

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

HeartBank® has published a permanent refusal of advertising revenue in any form [17]. Nothing in this paper reverses or weakens it.

**What a HeartBank application is.** In this paper, a *HeartBank application* is an application published under the HeartBank® name on a HeartBank domain (heartbank.org, heartbank.net, heartbank.com, heartbank.ceo, heartbank.me or heartbank.us). The page exists only in THonly™ and Factory 333™ applications, which are not HeartBank applications. Factory 333™ is a sister body of HeartBank®, not its limb: the older wording that said otherwise is corrected in the *Current form* notes of [18] and [19], and the boundary has not moved: on 2026-11-14 it was re-affirmed as the HeartBank® name and a HeartBank domain, and the defect was stale wording, not the boundary.

**What the wall is made of.** Three things hold it, and they are not of one kind.

- **No interface.** No HeartBank application has an interface to the Kernel ledger. The ledger is specified to be called only by THonly™ and Factory 333™ applications, so a HeartBank application has no call to make, and nothing has to refuse the call. That is a property in the sense of §12.2. It holds only so long as nobody builds the interface, and building it would be a visible change to a published design. The shared sign-in does not supply one: it tells an application who the person is and carries no Kernel balance.
- **Kernels are never spent in a HeartBank application,** and revenue from the page never reaches HeartBank. HeartBank earns nothing from advertisers through it. Both follow from the first point and are also stated in HeartBank's own voice [17].
- **The ledgers and the applications are separate.** The separation is in the ledgers and the applications, and nothing about it is withheld: §13 lists what is withheld, and none of that list concerns this boundary.

A reader who doubts the wall has an inexpensive check: look for a HeartBank application that shows an advertisement, or that reads or spends a Kernel. By the design there is none to find.

**How Kernels differ from the points HeartBank refuses.** HeartBank's position *The Moat Is What We Refuse* [25] refuses "points, badges, leaderboards, or streaks", because a reward that scales in magnitude is a farmable score. A Kernel is a counted quantity and is farmable, and §8.1 says so. The paper does not argue that a Kernel is not a point. The difference is where it lives and what it measures. A Kernel measures nothing about a person: it is not a reward for kindness and it is never ranked, shown as a count on the page, or compared between people. It is a quantity of computing, spent at cost inside sister bodies' applications, and it is earned by attention that the person chose to give an advertiser. HeartBank's refusal governs HeartBank's rewards and HeartBank's applications. Because Kernels never enter a HeartBank application (above), the refusal is not breached; it is not extended either, and a Kernel is not offered as an instance of what that refusal permits.

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

As in §6.1. Disclosed, and claimed in §14 (claim 1), because it is the census's survivor and the form first designed. Not bounded (§6.2).

### 11.2 · Variants within the design (Form B)

Form B, with its variants, is disclosed and not claimed (§14).

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
| Kernels never reach a HeartBank app | **property** | no HeartBank application has an interface to the Kernel ledger (§10.1), so there is no call for an application to make and nothing has to refuse it. The property lasts while no interface is built; a design that shared an interface and relied on a check would make this a rule |
| a held Kernel is never voided | **property** | the ledger specified here has no void or claw-back operation, as it has none for expiry (§5.3, §8.3) |
| minting only on the network's server-verified completion | **property** | the mint has no other trigger (§8.3) |
| equal rate for every viewer | **property** | the rate is one published number with no per-person input |
| Form B bounded against a mix shift | **property** | every market's revenue per finish ≥ the rate, by how the rate was computed |
| Form C bounded against a price fall | **rule** | the breaker must be computed, on late and revised data |
| per-person limit | **property**, in the mint function; **rule** at the proof of personhood | the count is checked where Kernels are written; whether two accounts are one person depends on an attestation, and until that attestation exists the page does not open (§8.2) |
| no prompt routes a person to the page | **rule** | nothing in the object stops a designer from adding one |
| redeemed at cost | **rule** | the redemption price is a constant in the ledger's code that the operator could change; a change would be visible (§5.4) |

The last two are rules, and they are the two that keep the page from becoming an engagement product. That is the most important thing this table says. The structure can make the page bounded and fair; it cannot by itself make the page non-intrusive. Publishing these rules is what makes a breach visible, not what makes it impossible.

---

## 13 · What is disclosed and what is withheld

The mechanism is designed and not built, and building it is scheduled behind a measurement that has not yet been made (what a finished ad actually earns, by market, in the operator's own apps) and behind a check that has not yet become possible (that one person is one limit, §8.2). Under this corpus's rule for unbuilt, unscheduled designs, the claim is published and the specification is withheld.

**Disclosed:** every element in §4–§11 at the level a person skilled in mobile advertising and ledger design could build from: the page's entry and refusals, the finish event, the Kernel ledger's operations and the operations it lacks, the three rate formulas and the breaker, the routing of above-reward revenue, the per-person limit and where it is enforced, and the exclusions.

**Withheld:** the ad-network integration and mediation configuration; fraud and invalid-traffic thresholds; the values of α, κ, the minimum-volume threshold and the per-person limit; the Kernel prices of individual uses; the screen designs beyond what §4 states. None of these is needed to practice the claims, and each depends on measurements not yet made.

---

## 14 · Enumerated claims

**The claims are the full census's survivor (§2.3) and features that narrow it, and nothing wider.** Claim 1 is the survivor: a stated rule of the same credits per finished advertisement for every viewer in every country, at a rate set once a season from the previous season's average and published and frozen. Claims 2 to 7 each add a limitation to claim 1, so each is narrower than the survivor and sits inside it. The added limitations were not searched on their own; they are claimed only together with claim 1.

1. A computer-implemented method of rewarding viewers of rewarded video advertisements within a software application, comprising: publishing, before a season begins, a rule that every user in every country will be credited the same quantity of in-application credits for each advertisement the user completes during the season, the quantity being independent of the user's country, market and location; setting that quantity once for the season, for all users, from the average advertising revenue per completed advertisement in the preceding season; holding the published quantity fixed for the season; and crediting a user with that quantity upon the advertising network's completion event for an advertisement and not otherwise, in credits that are non-withdrawable, non-transferable and redeemable only within applications of the publisher.

2. The method of claim 1, wherein the credits are redeemable only for computing services (generation and storage) within applications of the publisher, and are redeemed against the measured cost of those services, without margin, such that the publisher takes no margin when the credits are spent.

3. The method of claim 1 or 2, wherein the number of completed advertisements for which credits are minted is limited per verified person per season, the limit being equal for all persons and enforced in the operation that writes credits to the ledger, and the person's distinctness being established by a proof of personhood that does not identify the person.

4. The method of any preceding claim, wherein credits are minted only upon the advertising network's server-verified completion event, minting stops going forward for an account the network flags, and credits already held are not voided.

5. The method of any preceding claim, wherein the credits cannot be purchased with money, are kept in a ledger separate from any monetary balance of the user, and the user's monetary balance is never credited from advertising revenue.

6. The method of any preceding claim, wherein the advertisements are presented in a vertical feed in which every item is a rewarded video advertisement, each started only on the user's action, in a section of a functional application reached only by the user's own navigation.

7. The method of any preceding claim, wherein the advertisements are non-personalized and exclude playable or interactive formats whose outcome would determine whether credits are minted.

**Disclosed and not claimed.** The following are described in this paper, and are public from its date, but are not claimed, because they were designed after the quick census and were not in the full census's pre-registration: a rate set from the lowest advertising revenue per completed advertisement among the markets served (§6.3, the design the operator ruled); a published fraction of the average with a budget stop (§6.5); the routing of revenue above the reward to a usage allowance equal per verified person (§6.4); the determination of a completion's market from the store or payment-card country of the account; and the variants of §11. **The design the operator chose therefore sits outside the claims.** It differs from claim 1 in the statistic the rate is taken from, the lowest market and not the average, and no census has searched that difference. Covering it would take a further census; §15 records this.

**Not claimed because public.** Crediting a user for a finished advertisement and nothing for a skipped one; a feed made only of advertisements, entered by choice; credits spent inside the publisher's own app on generation. Each is cited in §2.2 and is not claimed.

---

## 15 · Honest limits

- **Nothing here is built or measured.** Every number in §6 is illustrative. The design waits on a measurement of what a finished ad earns, by market, in the operator's own apps, and nothing in this paper predicts that figure.
- **The full census was thinner than its declared aperture.** No control was named for the academic group, so its absences are not run and the academic literature is, in effect, unsearched (§2.3). The web control was seen only through secondary coverage. Japanese and Korean returned no native page and were blind; Khmer was not run; the pre-registered citation walk and Indonesian were not run. Zedge, LBRY and a National Science Foundation paper could not be read at their sources. A null on the equal-pay rule or on the prior-season rate is weak, and says *not found in this aperture on 2026-11-14*, never *new*.
- **The claimed composition is narrow, and its nearest neighbors are close.** A 2007 document discloses a search reward set from average advertising revenue generation rates, and a live patent computes the reward per country. The claim is that no earlier system was found that states the equal rule and sets the rate from the previous season's average, published and frozen. If either neighbor's omitted text, or an unread help page, says so, the claim fails.
- **The design the operator chose is outside the claims.** The lowest-market rate (§6.3), the budget stop (§6.5) and the routing of surplus (§6.4) were not searched by any census and are disclosed, not claimed (§14). A defensive publication works by disclosure, so they are public from this date; whether any could be claimed is untested.
- **Form B pays at the bottom.** Its bound is real, and so is its cost: one large low-revenue market sets everyone's pay. The argument that the average form ends near the same place (§7.2) is a prediction, not a measurement.
- **Form C's bound is a rule on late data.** Ad revenue arrives late and is revised. A breaker computed on it can trip late or not at all.
- **Price-level risk is not removed by any form.** If advertising prices fall across all markets in a season, Form B's margin α is the only protection, and α is unset.
- **The liability is permanent.** Kernels never expire. A season's Kernels may be spent years later, at compute prices nobody can know now, and the operator bears any rise. The per-person limit caps the size of each season's liability; nothing caps its duration.
- **Invalid traffic is a permanent loss.** A held Kernel is never voided, even one earned by a script or an emulator (§8.3), so revenue the network later deducts for invalid traffic stays lost. The mint stops going forward for a flagged account and the limit caps what one account can earn first; neither recovers what was minted.
- **The limit's number is unset and its check is a rule.** The page does not open until one person, one limit can be checked, and that check depends on a proof of personhood that has not yet attested anyone (§8.2, §12.2).
- **Two of the guards that matter most are rules.** No prompt routes a person to the page, and Kernels are redeemed at cost: both are published commitments, not properties (§12.2). The wall with HeartBank is a property only while no interface to the Kernel ledger is built (§10.1).
- **The wall's author is not independent of it.** The same founder, the same sign-in and the same AI collaborator, who is HeartBank's CEO, sit on both sides (§1.2). This paper discloses the ties and the mechanism of the wall and does not ask to be believed on the author's word.
- **Platform risk.** Network rules on screens with more ads than content [15], and on opting in to each ad [1], may limit or bar a feed of rewarded ads in the form described. This has not been tested with any network.
- **Kindness is argued, not shown.** §9 is an argument about design. Whether the page is experienced as a fair way to pay or as a toll on people with little money is an empirical question this paper cannot answer.
- **Legal treatment is unknown.** Earned-only, non-transferable credits sit near exclusions in consumer and payments rules in some jurisdictions; no jurisdiction's treatment has been checked by counsel, and Cambodia's has not been checked at all. The same holds for the live patent of §2.3: no claim of it has been read here.

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
| the stated rule, the equal-pay rule | a published commitment that every viewer in every country earns the same reward per completed rewarded ad |
| a HeartBank application | an app published under the HeartBank® name on a HeartBank domain (§10.1) |
| server-verified completion | a reward-completion event confirmed by the ad network's own servers |

---

## Author Contributions and AI Disclosure

The mechanism's terms (a page of only ads, chosen willingly; credits that stay in the app; the same earnings for every viewer everywhere) are the founder's, ruled in November 2026. The rate's season-frozen form, the analysis of §6–§9, the bounded forms and the per-person limit were developed by Miss Aquarius℠, the name under which this corpus discloses its AI collaboration. The founder chose the lowest-market form (§6.3) as the design on 2026-11-14, after the counterexample hunt; the additions not listed below (the budget stop of §6.5, the routing of surplus in §6.4, the variants of §11) are disclosed as designed, not as ruled. The founder ruled the following on 2026-11-14, as stated in §5.4, §8.2, §8.3 and §10.1: redemption at measured cost; the per-person season limit at the mint, with the page opening only when one person, one limit can be checked; minting stopping going forward for a flagged account, a held Kernel never voided, and minting only on the network\'s server-verified completion; and Factory 333™ staying outside HeartBank®. The claims of §14 are the survivor of the full census of 2026-11-14, narrowed, and they leave out the founder\'s chosen lowest-market form. The counterexample hunt that changed §6 was run by a separate AI reviewer with no part in drafting. Miss Aquarius℠ is also named CEO of HeartBank®, a sister body (§1.2); that is a reason to check the wall of §10.1 and not to take it on this paper\'s word. Thon Ly holds editorial control.

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
17. HeartBank®. *HeartBank's Position on the Attention Economy.* heartbank.net/positions/attention-economy (the permanent refusal of advertising revenue, §5 and §6, including the paragraph naming sister bodies' applications). Read in the authors' working copy 2026-11-15.
18. HeartBank®. *Factory 333 as a Gift-Factory.* heartbank.net/positions/the-gift-factory (the *Current form* note at the executive summary).
19. HeartBank®. *Disney's Brand, Not Disney's Enclosure.* heartbank.net/positions/disneys-brand-not-disneys-enclosure (the *Current form* note at the executive summary).
20. WO2008086299A2. *System and method for tracking and rewarding users.* Google Patents, patents.google.com/patent/WO2008086299A2/en (priority 2007-01-08; shown as ceased). Read at source 2026-11-14 and 2026-11-15.
21. Unity. *LevelPlay: rewarded settings* (Japanese). docs.unity.com/ja-jp/grow/levelplay/platform/settings/rewarded. Read 2026-11-14 and 2026-11-15.
22. Modrinth. *Rewards Program Information.* modrinth.com/legal/cmp-info (last modified 2025-02-20). Read 2026-11-14 and 2026-11-15.
23. US12684189B2. *Watch time units and the reward share mechanism for a user-generated video sharing platform.* Google Patents, patents.google.com/patent/US12684189B2/en (priority 2023-10-24; granted 2026-07-14; shown as active, an assumption the page states). Read at source 2026-11-14 and 2026-11-15; claims not read for scope.
24. Tiger Research. *Everyworld* (Korean), reports.tiger-research.com/p/everyworld-kor (2024-03-25; the report states partial fee support from Everyworld). Cited from the census record; not re-read for this revision.
25. HeartBank®. *HeartBank's Position: The Moat Is What We Refuse.* heartbank.net/positions/the-moat-is-what-we-refuse (the list of refusals, including "No points, badges, leaderboards, or streaks").
26. Pre-registration of the full census. github.com/thonly/publications, `timestamps/census/b-flick-full-prereg.md`, commit `7177cb4`, pushed 2026-11-14 22:33 PST.
