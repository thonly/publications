---
title: "Transparency as Enforcement: Anti-Abuse Without Legal Contract Machinery"
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-c
kind: mechanism
status: draft
date: 2026-05-22
revised: 2026-10-06
license: CC0-1.0
slug: transparency-as-enforcement
venue: thonly.org/research/transparency-as-enforcement (canonical)
---

> **Note.** This defensive publication specifies a design pattern for abuse prevention in which the conduct to be policed is disclosed to the bounded community it affects, in place of terms-of-service enforcement, together with the conditions under which the pattern works and the one condition under which it may be used at all. Its revision of 2026-09-02 withdrew one of the three deployment patterns first specified (§3.2, a public ledger of time given and time received), kept it in place as a marked negative case, stated the boundary it broke as §4.4, and added the Prior-Art and Non-Assertion Statement and the enumerated claims (§8). The revision of 2026-09-05 added the lineage paragraph of §2 and the limits of §6.5–§6.6. The revision of 2026-10-06 added the Terms table, the notes marked *Current form*, the reading of §4.4 against its companion paper, §6.7, and the standard form of the Prior-Art and Non-Assertion Statement. Later additions date from the revision that introduced them; the date of any passage is that of the earliest timestamped version carrying it. Companion works in this corpus, each cited by title and corpus slug: *The Gift Operation* (`the-gift-operation`; the gift/exchange line §4.4 inherits); *The Currency That Cannot Be Spent Alone* (`co-presence-gated-redemption`; expiry as the enforcement that replaces §3.2); *Verified-Human Anonymous Local Gratitude Transfer* (`verified-human-anonymous-local-giving`; the proximity rule of §6.1); *B-PoH℠ as Humanity Layer for the AI-Native Internet* (`b-poh-humanity-layer-ai-native-internet`; the verified-human identity of §6.2); *Whose Turn, Not Who's Best* (`rotation-over-liveness`; why standing may admit but never order, §4.2).

---

## Abstract

This paper discloses a design pattern for abuse prevention in online platforms and shared-fund applications that replaces terms-of-service enforcement, dispute resolution and account termination with disclosure: the conduct to be policed is made visible to the bounded community it affects, and that community's own response is the sanction. The platform decides only what is shown, to whom and against what baseline; the community decides what the conduct means. Three properties make disclosure work as enforcement: the visibility itself is the mechanism, the response is proportioned by the community rather than by a binary rule, and participants join knowing what will be visible. Two deployments are specified: disclosure to a family of every reward its steward receives from the family's shared fund, and per-member display of storage use within a bounded user community, a display since replaced by a storage rule that needs none. A third, a public ledger of time given and time received per participant, is withdrawn and kept as a negative case. Three conditions of efficacy are stated (a community small enough for social signals to travel, participants with relational or reputational stakes, and a visible baseline against which conduct reads as anomalous) together with a condition of legitimacy: the pattern may render only the non-performance of an obligation the participant actually incurred. Where the underlying act is a gift, rendering the gap between what was received and what was returned does not report a shortfall; it creates one. The limits are stated: the enforcer is the community, so the guard holds only while the community responds; a bounded, high-stakes community can turn visibility into retaliation; and a complete record of named gifts renders absence by omission.

**Keywords:** abuse prevention, anti-abuse design, trust and safety, terms of service, account termination, dispute resolution, social sanctions, social enforcement, shaming, peer monitoring, reputation systems, public disclosure, transparency, accountability, self-dealing, fiduciary disclosure, shared family fund, common-pool resource governance, Ostrom design principles, gift economy, reciprocity, obligation, time banking, data protection, institutional design, defensive publication.

## Terms

Coined names used in this paper, and the standard terms an examiner or a reader in platform governance would search for them.

| Term used here | Standard term |
|---|---|
| transparency-as-enforcement | social enforcement by disclosure of conduct to a bounded community; reputation-based sanction in place of contractual enforcement |
| legal-contract machinery | terms of service, end-user license agreements, dispute resolution, takedown and account-termination procedures, and the legal enforcement behind them |
| visibility-as-mechanism | disclosure as the sanction itself, with no separate penalty step |
| socially-calibrated proportionality | graduated sanctions whose severity the community, not the platform, determines |
| participant-agency | informed entry into a disclosure regime; the response left to other participants' free choice |
| banker; family steward | the family member who administers a shared family fund |
| self-reward | a payment the fund's administrator receives from the shared fund |
| HeartBank Treasury | a family money-gift application with a shared family fund |
| Family Kitty℠; kitty | shared family fund |
| HeartBank Chronicle; time economy | time banking; a currency of pledged time |
| dual public ledger (withdrawn, §3.2) | public per-participant ledger of time given and time received |
| bounded-community condition | closed, small membership in which social signals propagate (Ostrom's clearly defined boundaries) |
| participant-stakes condition | continuing relational or reputational exposure of each participant |
| visible-asymmetry condition | a visible baseline against which conduct reads as anomalous |
| obligation condition | rule that a display may render only the non-performance of an obligation the participant actually incurred |
| proximity rule | transfer permitted only between devices with recent short-range radio co-presence |
| Proof of Humanity; verified-human identity | proof of personhood |
| expiry | lapse of an unredeemed time pledge, or of forward-only gift capacity, on terms stated when it was received |

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on any mechanism, architectural pattern, condition or method described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practicing any mechanism disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed.

This document constitutes a defensive publication establishing **prior art as of 22 May 2026** for the pattern it first described, and as of the revision that introduced it for each later addition. It discloses the following; a later patent application claiming any of them is filed against this disclosure:

1. the use of **visibility-as-enforcement in place of legal-contract machinery** as a deliberate institutional-design substitution, with the three structural properties of §2 stated as the substitution's requirements;
2. the **three efficacy conditions** of §4.1–§4.3 as a stated applicability boundary, so that the pattern is offered with its own failure conditions rather than as a universal; and
3. the **obligation condition** of §4.4 — the claim that transparency-as-enforcement is licensed by the presence of an obligation, and that where the underlying act is a gift the rendering of non-performance *manufactures* the obligation it purports to enforce.

The component lineages (reputation systems; norm enforcement in bounded communities; Ostrom's commons-governance design principles; the criminology of shaming) are old and are cited in §2 and the References. No prior-art search on record establishes that the synthesis is unpublished elsewhere, and the authors assert no such absence; §2 names the nearest prior work for each strand, and the enumerated claims of §8 are the paper's statement of what it discloses.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Family Kitty℠**, **Re-Tip Jar℠** — are separately and explicitly reserved; the dedication concerns the *mechanism*, not the *marks*.

This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and the document is deposited on Zenodo, each deposited revision a version under one concept DOI, with its source in the public repository `github.com/thonly/publications`. A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim.

> **Note.** The patent commitment has stood since this paper was first published on 2026-05-22, in the form *"The author and HeartBank® will not seek patent on this specification or any portion thereof."* A Prior-Art and Non-Assertion Statement was added on 2026-09-02. The commitment not to assert, and the extension of both commitments to the entities named above, were added on 2026-10-06, when the statement was brought to the standard form above; the three disclosed elements were set out as a numbered list at the same revision, their wording unchanged except that the second now names the efficacy conditions it always meant. The date relied on for priority is the one carried by this document's OpenTimestamps proof.

---

## 1. Introduction

The dominant model for platform anti-abuse is *legal-contract enforcement*. Participants accept terms of service; the platform monitors for violations; when violations are detected, the platform's response is escalation through the legal-contract machinery (warnings, suspensions, terminations, jurisdiction-specific legal action). The model assumes that the platform is in an adversarial-by-default relationship with its participants, that contract violations are the right framing for unwelcome behavior, and that the legal machinery is the appropriate enforcement layer.

The model has well-known failure patterns. It is *expensive*: legal staff, compliance teams, jurisdiction-specific counsel. It is *brittle*: contract violations are difficult to prove in the volume that platform-scale moderation requires, and remediation is binary (either the participant is in good standing or they are off the platform), with little room for proportional response. It is *culturally heavy*: it positions every participant relationship as legally contracted, which encodes the platform-participant relationship as commercial transaction rather than as community membership. And it is *jurisdictionally fragmented*: each jurisdiction's contract-enforcement regime differs, and platforms operating across jurisdictions face cumulative legal complexity that scales worse than linearly with their geographic footprint.

This paper specifies an alternative: a design pattern intended to achieve much of what legal-contract enforcement is supposed to achieve, at what is expected (not measured) to be a fraction of the cost, with a culturally lighter institutional surface. The pattern — *transparency-as-enforcement* — is: **make the relevant behavior publicly visible to the affected community, and let social cost handle the policing**. The visibility *is* the enforcement; no separate punishment mechanism is needed.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-10-06 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) An institutional anti-abuse architecture that operates through legal-contract machinery encodes adversarial-by-default relationships at the platform's foundational layer; an architecture that operates through transparency-as-enforcement encodes community-accountability relationships there instead. The choice is load-bearing for an institution whose work runs through families and local communities, because the foundational-layer assumption shapes the relationships the institution can sustain.*

The paper proceeds as follows. §2 articulates the three structural properties of transparency-as-enforcement that make it function as enforcement. §3 specifies three deployment patterns, one of which — (b), the dual public ledger — was withdrawn on 2026-09-02 and is kept as the negative case that found §4.4. §4 articulates three efficacy conditions and a fourth condition of legitimacy. §5 contrasts the pattern with legal-contract enforcement at the cost, brittleness, and cultural-weight dimensions. §6 names the conditions under which transparency-as-enforcement fails, the supplementary mechanisms that compensate, and three limits the pattern carries even when every condition holds. §7 closes, and §8 enumerates the claims.

---

## 2. Three structural properties

**Lineage, stated before the properties.** Reputation systems are the nearest prior art for claims 1–2: eBay's Feedback Forum (1996), Slashdot's moderation and karma (1999), and Stack Overflow's reputation-driven moderation (2008–09) each make participant conduct visible to a community and let the community's response, not platform adjudication, carry much of the enforcement; Resnick, Zeckhauser, Friedman and Kuwabara (2000) describe the class as systems that collect, distribute and aggregate feedback about participants' past behavior. The criminology of shaming is older still, and already separates shaming that reintegrates the offender from shaming that stigmatizes (Braithwaite 1989), the distinction §6.5's limit turns on. The differences are the ones §4 names: those systems run in open, unbounded communities; the score is platform-owned; there is no stakes condition; and there is no obligation condition. Open Collective's transparent budgets — steward-controlled spend, publicly inspectable — anticipate the steward-spend visibility of claim 4, and GitHub's contribution graphs render per-participant activity against a visible baseline. Ostrom's design principles (1990) already state bounded membership, monitoring and graduated sanctions as prerequisites for non-state enforcement; the first three conditions of §4 are, for a display layer, Ostrom's boundary, monitoring and graduated-sanction principles, and the fourth is not in Ostrom.

### 2.1 Visibility-as-mechanism

The visible behavior is the enforcement. There is no separate punishment mechanism that must be invoked after the visibility produces an effect; the visibility itself produces the effect. A banker (the family steward role in the HeartBank Treasury) whose self-rewards exceed family-average expectations is *visible as such* to the family; the family's social response (reduced trust; declining participation; reputational adjustment) is the enforcement, and it operates without any platform-mediated action.

The mechanism is direct in a way that legal-contract enforcement is not. Legal-contract enforcement requires (a) violation detection, (b) violation classification, (c) escalation procedure, (d) participant response, (e) appeal if any, (f) final disposition. Transparency-as-enforcement has the same first step (the behavior must be detected and made visible) but the remaining steps collapse into the affected community's distributed response.

### 2.2 Socially-calibrated proportionality

The social cost is proportional to community judgment rather than legal-binary determination. A behavior that the community finds mildly off may produce mild reputational adjustment; a behavior the community finds seriously problematic may produce severe response; a behavior the community endorses (e.g., generous self-reward in a family steward who consistently delivers exceptional value) may produce *positive* social response despite the legal-contract framing's blindness to that calibration. The proportionality is finer-grained than a contract regime delivers, because it is calibrated to the specific community's specific values.

This is also where the pattern's *humility* lives. The platform adjudicates the display — what is shown, to whom, against what baseline — and nothing else; which behaviors are acceptable, the community adjudicates. The platform's role is to make the relevant behavior visible; the community's role is to determine its meaning.

### 2.3 Participant-agency

Participants understand the visibility before participating and consent to it as part of the platform's social contract. The participation itself is consent to the transparency regime. This is important because the pattern works only if the affected participants *understand* that their behavior will be visible and have agreed to participate on those terms.

The consent meant here is social, not a legal basis for processing personal data. Where data-protection law applies, joining a service is not by itself consent in the legal sense, which must be freely given, specific, informed and unambiguous (GDPR Art. 4(11)), and whose freedom is doubtful where the service is made conditional on processing not necessary for it (Art. 7(4)); the lawful basis for the display is a separate question, noted in §5. The property also has a second face, the one claim 2 names: the response to what is shown is other participants' free choice, never a penalty the platform imposes.

The consent dimension distinguishes transparency-as-enforcement from surveillance. Surveillance imposes visibility on participants who have not consented to it; transparency-as-enforcement is a participation contract in which visibility is the social-cost mechanism the participant accepts as the price of admission.

---

## 3. Three deployment patterns, one of them withdrawn

### 3.1 Banker self-rewards publicly visible to the family

In the HeartBank Treasury, the *banker* (the family steward role) manages the family kitty's distribution among family members, including any self-reward the steward takes for the stewardship work itself. The steward's self-rewards are *publicly visible to the family* — every family member can see, at any time, what the steward has paid themselves and on what basis.

The mechanism: a steward who self-rewards beyond family-judged reasonable expectations is visible as such to the family. The family's response (questions; reduced trust; alternative-steward consideration at the next rotation; reputational adjustment in family conversations) is the enforcement. The platform does not adjudicate "reasonable"; the family does.

What the pattern *defeats* is the steward who rewards himself from the common purse without disclosure — the oldest abuse a family purse invites; a claim about the structure, not about the historical record. The legal-contract response to this pattern is fiduciary-duty regulation with disclosure requirements and audit obligations; the transparency-as-enforcement response is to make every self-reward visible from the start, eliminating the asymmetric-information substrate the abuse depends on.

> **Current form.** In the Treasury as deployed, a self-reward is not a withdrawal the steward makes. It is claimed by recording a moment (a short video of the act being thanked); its amount is set by the platform's rule within a band the steward configures, and the platform pays it from the shared fund only when that moment is visible to the family or to the public, a condition checked where the payment is made, so a self-reward the family cannot see is not paid. The visibility is therefore a property of the payment rather than a policy about the display; the family's response to what it sees remains the enforcement, as above. Self-rewards to the family's other eligible members are paid under the same condition. The text above is retained as a disclosed variant.

### 3.2 Withdrawn — dual public ledger of time-given and time-received

**This pattern is retracted. It is retained here, marked, because it is the paper's most instructive case: it satisfies all three efficacy conditions of §4 (§4.1–§4.3) and is nonetheless wrong, which is how §4.4 was found.**

*As originally specified.* In the HeartBank Chronicle time-economy, each participant's time-given (actually delivered) and time-received (may or may not be spent) were to be publicly visible. Plotted as a 2×2, the axes form four legible quadrants: quiet giver (high given, low received); network anchor (high given, high received); latent or new (low given, low received); and a fourth quadrant, low given and high received, for which the original text supplied a name. The stated mechanism was that a participant who chronically receives more thanks than they honor becomes publicly visible as such, and thereafter receives fewer.

*Why it is withdrawn.* The pattern enforces by **rendering an absence** — the gap between what was received and what was delivered — and a rendered absence is an accusation. Three objections; the first and third are each sufficient on their own, and the second is not, because it holds of every deployment in this paper and is carried as a limit of the whole pattern (§6.6):

1. **It names a person by their deficit.** The fourth quadrant is not a description of an act but a standing characterization of a participant, and the original label was pejorative. A surface that sorts people into a quadrant defined by what they have failed to do is a shaming instrument, whatever the intent of its designer.
2. **It requires an audience at the moment it is tested.** The enforcement is other participants' judgment, so the guard exists only while people are watching and caring. A guard that needs a witness present is a rule, not a property, and this corpus's standing test for a guard is whether it survives the removal of everyone who would enforce it.
3. **It manufactures the obligation it claims to enforce.** This is the decisive one and it generalizes: see §4.4.

*What replaces it.* Nothing, at this surface. The Chronicle's mechanism paper (*The Currency That Cannot Be Spent Alone*, §7.2) establishes that **expiry already performs the enforcement** — an unredeemed hour dies on a clock, with no display and no audience — and that the giver's standing refusal prices repeated declining without anyone being rendered delinquent. What a ledger may show is what a participant has given and what they have received; the difference between them is never computed for display. The corpus therefore loses no enforcement by this withdrawal; it loses a mechanism it did not need and should not have specified.

> **Current form.** Where this section says a ledger may show what a participant has given and received, the audience is now specified. The record is one view of an append-only log whose rows are private and whose proofs are public: the signed summaries that let anyone check the log was not altered are published, and its entries are not. No per-participant total of time given or received is published, and nothing in the record is ranked or compared with anyone else's. A participant may export their own history complete and signed. The difference between what a participant has received and what they have delivered is never computed for display, to them or to anyone. The sentence above is retained as a disclosed variant.

### 3.3 Per-participant storage usage publicly displayed

In the platform's data-architecture, each participant's storage usage (the data they have uploaded; the media they have stored; the messages they have retained) is publicly displayed. A participant who hoards platform storage well beyond peer norms is visible as such.

The mechanism: storage hoarding's social-cost response is to reduce communal trust and produce reputational adjustment. The platform does not impose storage quotas with binary cutoffs; the visibility shapes participant behavior toward proportionate usage without quota-mediated enforcement.

What the pattern defeats is the storage-hoarding pattern that drives platform-storage cost inflation. Legal-contract enforcement would require quota provisions in the terms of service; transparency-as-enforcement lets participant peer judgment handle the calibration.

> **Current form.** The institution's storage design no longer uses this display, and governs the same abuse with a property in place of an audience. Free storage attaches to a gift, not to a user: a file given to a verified person who receives it is kept free within a fixed format (a length limit on the item, not an allowance per person) and is never metered or counted; a file that was never given is production storage, priced as a service; and keeping a given file beyond the format is a single payment, never a recurring fee. Free storage therefore cannot be used as a backup drive, and the motive to hoard it is removed rather than policed. The display above is retained as a disclosed variant, and the analysis of §4 still describes it.

---

## 4. Four structural conditions for the pattern to work

The pattern is *not* universal. Four structural conditions must hold for transparency-as-enforcement to function as enforcement. The first three are, for a display layer, Ostrom's boundary, monitoring and graduated-sanction principles; the fourth is not in Ostrom.

### 4.1 The bounded-community condition

The relevant community must be small enough that social signals propagate. Within a family (the §3.1 deployment) the community is small (typically <20 members) and signals propagate immediately. Within a HeartBank user community in a specific city (the §3.3 deployment) the community is larger but still bounded by social-network reachability. At Internet scale across strangers, the pattern fails — visibility without community context produces no social signal because there is no "community" to do the signaling.

The bounded-community condition is why transparency-as-enforcement works for HeartBank's specific institutional surface (family-scale and city-scale community structures) and would fail for an Internet-scale anonymous-participant platform with no community structure.

### 4.2 The participant-stakes condition

Participants must have reputational or relational stakes that make the social signal costly. Within a family the stakes are existential (these are the people one shares life with); within a HeartBank user community in a specific city the stakes are reputational (one's standing as a generous participant matters to one's continued ability to participate generously). In contexts where participants have no reputational or relational stakes, the social signal produces no cost and the pattern fails.

> **Current form.** Standing is no longer specified as something that governs a participant's ability to give or to be given to. Givers' thanks are not steered toward recipients of high standing, and where any signal bears on whether a participant is surfaced at all, it is a yes-or-no admission test, never a weight, an order or a side-by-side comparison (*Whose Turn, Not Who's Best*, `rotation-over-liveness`). The clause above about standing and the ability to participate is retained as disclosed.

### 4.3 The visible-asymmetry condition

The behavior being policed must be one a reasonable community would view as anomalous against a publicly-visible baseline. A steward's self-reward is policeable because the *baseline* (other family members' contributions; the steward's own historical self-rewards; comparable stewards' self-rewards in adjacent families) is publicly visible, and asymmetric self-rewards are visible as asymmetric against the baseline. A behavior that is asymmetric but for which no baseline exists is not policeable through this pattern — the visibility produces no judgment because the community has no comparison surface.

> **Current form.** The baseline is now confined to the family's own record: the steward's earlier self-rewards and the shared fund's contributions, shown as facts beside the act (§6.3). Another family's record is not part of it. A family's moments are visible to that family by default and become public only when their author makes them so, and records are not compared across people or families. Comparable stewards' self-rewards in adjacent families, named above as part of the baseline, are retained as a disclosed variant.

### 4.4 The obligation condition

The three conditions above are conditions of *efficacy*: they say when the pattern will work. This fourth is a condition of *legitimacy*, and it says when the pattern may be used at all. It was found by applying the first three to §3.2, which satisfies all of them and is nonetheless withdrawn.

**The behavior rendered must be the non-performance of an obligation the participant actually incurred.**

Transparency-as-enforcement works, where it works, because a community can see that someone did not do what they were bound to do. The restaurant hygiene grade, the credit report, the public register of judgments, the published record of a fiduciary's dealings: each renders a shortfall against a duty that existed before the rendering. That prior duty is what makes the display a report rather than an imposition. Those instances enforce obligations, and obligations are what enforcement is for.

A gift creates no such duty. That is their definition in this corpus, argued rather than assumed: *The Gift Operation* (§4.1) draws the gift/exchange line against Mauss's obligation to reciprocate, and this paper inherits that line — an act that obliges the recipient to reciprocate is an exchange, and calling it a gift does not make it one. So when a surface renders the gap between gratitude received and gratitude returned, it does not report a shortfall against an existing obligation — **it creates the obligation by rendering it.** The participant who was given something freely is retroactively placed in debt, by a display, on the authority of nobody. The pattern does not enforce the norm; it legislates one, and it legislates the precise norm that converts the institution's central act from a gift into a liability.

The companion paper qualifies the claim that a gift creates no duty, and the qualification is carried here rather than resolved. *The Gift Operation* says the recipient of a circulating gift "holds an open obligation — not to the giver … but forward" (§4.4), and that a pass-on whose giver is named redirects Mauss's obligation into the chain rather than ending it (§6.7); in its account only a gift that both moves forward and arrives unattributed leaves no one to owe. Read as a duty, that forward obligation would license exactly the display §3.2 withdrew. This paper keys its condition to an obligation the participant *incurred*, by an undertaking of their own such as accepting the steward's role. A forward expectation that arises from having been given something is not an undertaking, and rendering its non-performance remains an imposition. The two papers use *obligation* in different senses; whether they should be brought to one vocabulary is open.

```
  what is rendered            prior duty?     the display is…
  ──────────────────────────────────────────────────────────────────
  a steward's self-reward      YES  (fiduciary)   a report        §3.1
  a participant's storage use  YES  (proportion)  a report        §3.3
  gratitude received, unmet    NO   (it was a gift)  an IMPOSITION  §3.2 (withdrawn)
```

The condition is narrower than squeamishness and should not be softened into it. It does not say that unflattering facts may not be shown, nor that only praise may be rendered. §3.1 renders a steward's overreach and is retained. What it says is that the *ledger of a gift* has no delinquency column, because there is nothing in a gift for a participant to be delinquent about — and that a designer who adds one has changed what the institution is, not merely how it is displayed.

The honest cost of the condition is the same one §3.2's withdrawal pays: the obligation-free surface has no fast lever against the participant who receives generously and returns nothing. It has only slow ones — expiry, and the free choice of others about whether to give again. This paper's position is that the slow lever is the correct one wherever the underlying act is a gift, and that a fast lever built by rendering absence is not a cheaper version of the same thing but a different institution.

> **Current form.** Expiry, as a lever, is now bounded by a later commitment of the institution: everything in it may aim at zero, but a person's holding reaches zero only by that person's own free act, neither deceived nor pressured. Expiry may clear a capacity on the terms accepted when it was received (an unredeemed hour of pledged time; forward-only gift capacity at the annual reset) and never a balance the participant owns. Dormancy fees, clawbacks and expiring owned balances are not levers available to this pattern. The sentences above are retained as disclosed.

---

## 5. Contrast with legal-contract enforcement

*Design intent for the two regimes, not measured outcomes.*

| Dimension | Legal-contract enforcement | Transparency-as-enforcement |
|---|---|---|
| **Cost** | High (legal staff, compliance, jurisdictional counsel) | Low (display-layer engineering only) |
| **Detection latency** | Hours to weeks (review queues, escalation procedures) | Immediate (the behavior is its visibility) |
| **Response proportionality** | Coarse (warnings, suspensions, terminations) | Fine (community-calibrated reputational adjustment) |
| **Cultural framing** | Adversarial-by-default contract | Community-accountability membership |
| **Jurisdictional complexity** | Cumulative across operating jurisdictions | Low — no jurisdiction-specific enforcement mechanism is invoked; the display itself still carries data-protection duties (GDPR Arts. 5–6, where it applies) |
| **Scalability of enforcement** | Super-linear (cost grows faster than violation volume) | Linear (display cost grows with participant count) |
| **False-positive recovery** | Difficult (legal record persists) | Easy (community signals can revise quickly) |
| **Participant agency** | Imposed via terms of service | Consented as participation contract |
| **Suitability for bounded-community institutional surfaces** | Heavy-handed | Native fit |
| **Suitability for Internet-scale anonymous platforms** | Required (no community substrate to enforce) | Fails |

The contrast is not "transparency-as-enforcement is universally better." The contrast is *structural fit*: for institutional surfaces with bounded communities, participant stakes, and visible asymmetries, transparency-as-enforcement is expected to fit better than legal-contract enforcement, a design expectation the table states and no measurement yet tests. For institutional surfaces lacking those properties, the pattern fails and legal-contract enforcement (or some hybrid) is required.

---

## 6. Conditions under which transparency-as-enforcement fails

The pattern fails when any of the four conditions (§4) does not hold — the fourth differently, since when it fails the pattern does not stop working but stops being licensed. Three failure-mode treatments for the efficacy conditions, the hybrid, and then three limits the pattern carries even when every condition holds:

### 6.1 Failure mode 1 — community too large for signals to propagate

If the community exceeds social-network reachability, the visibility produces no signal because no one is positioned to receive and propagate the relevant social information. The platform's response: *sub-divide the community* into bounded sub-units within which the pattern can work, and treat cross-sub-unit interactions through different mechanisms (the *proximity rule* for cross-community gratitude flows is one such adaptation: a transfer is permitted only between devices that were recently co-present by short-range radio; see *Verified-Human Anonymous Local Gratitude Transfer*, `verified-human-anonymous-local-giving`, §3).

### 6.2 Failure mode 2 — participants without reputational stakes

If participants have no reputational stakes (e.g., anonymous one-shot interactions), the social cost cannot be imposed because there is no continuing identity to bear the cost. The platform's response: *introduce reputational stakes* by requiring persistent identity, longitudinal participation, or social-graph anchoring. The Proof-of-Humanity primitive's verified-human identity (*B-PoH℠ as Humanity Layer for the AI-Native Internet*, `b-poh-humanity-layer-ai-native-internet`) is one mechanism that introduces the reputational substrate the pattern requires: it supplies a continuing identity that can bear a social cost. It proves that a participant is a person, not that their conduct is good, so it is a precondition of the pattern and never a substitute for it.

### 6.3 Failure mode 3 — behavior with no community baseline

If the behavior being policed has no community baseline (no comparison surface against which the community can judge whether the behavior is anomalous), visibility produces no judgment. The platform's response: *construct baselines* by surfacing the community's own reference points — the steward's earlier self-rewards, the kitty's contributions — as facts beside the act, never as a rank or percentile, so the community can judge against meaningful reference points without being handed a verdict.

### 6.4 The hybrid response

In most institutional contexts, transparency-as-enforcement and legal-contract enforcement are *complements*, not substitutes. The pattern handles the bounded-community, participant-stakes, visible-asymmetry surface; the legal-contract machinery handles the remaining surface. The architectural question is what fraction of the institution's anti-abuse work can be handled by the pattern, and how the residual is structured.

For HeartBank the design intent is roughly ninety-to-ten — the author's estimate of the surface, not a measurement: transparency-as-enforcement handles roughly 90% of the anti-abuse surface (the family-scale and city-scale community interactions); the legal-contract machinery handles ~10% (cross-jurisdictional fraud, sanctions compliance, edge cases that require formal legal response). The expected cost saving is large and has not been measured; the cultural framing is the larger reason for the choice.

### 6.5 Weaponised visibility — the enforcers are interested parties

A bounded, high-stakes community can turn the same visibility into coordinated retaliation, favouritism, pile-ons and false reporting. The pattern treats stakes only as enforcement power; they are also distortion, and the pattern has no defence beyond the community's own norms. That is the honest cost of removing the adjudicator: what is removed is also the appeal. Visibility also invites status competition and can chill legitimate high use; the display must show the fact, never a ranking — the corpus's standing rule against rendering people by rank — and a percentile is a ranking.

### 6.6 Visibility is enforcement only while the community responds

The pattern's force depends on the community continuing to perform the social-cost response. A community that stops looking has no enforcement at all, and no fallback is specified here.

By this corpus's own test for a guard (remove the enforcer, and see whether the guard survives), transparency-as-enforcement is a rule, not a property: its enforcer is the community, and the objection that withdrew §3.2 on this ground applies to every deployment in this paper. What can be made a property is the visibility, not the response. In the Treasury as deployed, a self-reward is paid only for a moment the family can see at the time of payment (§3.1), so a self-reward hidden from the family then is never paid, whether or not anyone is looking; whether the family then looks, and what it does, stays a matter of people. Where a guard must hold with nobody watching, this corpus takes it from the object instead: expiry for pledged time (§3.2), and a storage allowance that attaches to the gift rather than the user (§3.3).

### 6.7 Absence by omission

Rendering only performed acts does not by itself keep absence off the surface. In a community small enough for the pattern to work (§4.1), a complete record of who gave lets every member read who did not, and the record becomes a delinquency column by subtraction. The obligation condition therefore reaches what a display omits as well as what it shows: where the act shown is a gift, a named roster of givers in a bounded community renders the same absence §3.2 rendered. Where this corpus needs a gift to leave no obligation behind, it leaves the giver unnamed (the anonymous forwarded gift and the anonymous thank of *The Gift Operation*, `the-gift-operation`, §6.7), so that pressure has no creditor to come from. §3.1 is outside this case: a self-reward is a payment from the shared fund, not a gift, and a member who receives none is not thereby in default of anything. Inside a family the cut is partial: where one giver is likely, a member can guess who gave, and the platform's part is limited to never saying.

---

## 7. Conclusion

Transparency-as-enforcement is offered as a defensive publication so that other institutions designing anti-abuse architectures can adopt the pattern free of any patent claim by its authors; a publication frees nothing already enclosed by others. The pattern is implementable today using available display-layer engineering; the institutional substance (bounded communities; participant stakes; visible asymmetries; consent to the transparency regime as participation contract) is the institutional design work the pattern requires.

The pattern is offered to the commons under CC0 in the spirit of *dāna*, that institutional designers may build, share, and improve without barrier.

---

## 8. Enumerated Claims

Enumerated as prior art; each claimed severally and in combination. **Added 2026-09-02** — the paper was published without a claims section, which a mechanism disclosure requires; these enumerate what the paper already disclosed, and claim 5 states the boundary added by this revision.

1. **Visibility-as-substitution:** a method of anti-abuse governance in a digital institution in which the publication of participant conduct to a bounded community substitutes for legal-contract machinery (terms of service, dispute resolution, account termination) as the operative enforcement mechanism, the platform adjudicating the display — what is shown, to whom, against what baseline — and nothing else, the community supplying the response.
2. **The three structural properties:** the combination of visibility-as-mechanism, socially-calibrated proportionality (the community rather than the platform fixes what counts as excessive), and participant-agency (the response is other participants' free choice, never a platform-imposed penalty).
3. **The applicability conditions as part of the disclosure:** the pattern offered together with the three efficacy conditions of §4.1–§4.3 and the legitimacy condition of §4.4, such that the mechanism is claimed only within its own stated domain and is disclaimed outside it.
4. **The deployment instances:** steward self-reward visibility within a family-scale kitty (§3.1) and per-participant resource-consumption visibility within a bounded user community (§3.3), each rendering a **performed act** against a community-visible baseline.
5. **The obligation condition (§4.4):** the constraint that transparency-as-enforcement may render the non-performance only of an obligation the participant actually incurred — and the accompanying negative claim that where the underlying act is a **gift**, no such obligation exists, so that rendering the gap between what was received and what was returned does not report a shortfall but **constitutes** one. Claimed together with its consequence: a gift ledger has no delinquency column, and enforcement in gift-shaped economies must be carried by mechanisms that require no audience — expiry, and the free choice of others whether to give again.
6. **The composition:** claims 1–5 as a single system — an enforcement architecture that is cheaper than contract, calibrated by community rather than by policy, bounded by stated failure conditions, and constrained from converting gifts into obligations by the act of display.

---

## Acknowledgments

The community-currency literature's emphasis on transparent ledgers (Lietaer, Cahn, Greco); the open-source movement's transparency-as-trust pattern (Raymond); the institutional-design literature on commons governance (Ostrom). Written by Thon Ly with Miss Aquarius℠, the consistent name under which this institution discloses AI collaboration and a co-author of this paper; the underlying models are not named, and final editorial control remains with Thon Ly.

---

## References

- Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press, 1990.
- Cahn, Edgar S. *No More Throw-Away People: The Co-Production Imperative.* Washington, DC: Essential Books, 2000.
- Lietaer, Bernard. *The Future of Money.* Century, 2001.
- Greco, Thomas H. *The End of Money and the Future of Civilization.* Chelsea Green, 2009.
- Mauss, Marcel. "Essai sur le don." *L'Année sociologique*, n.s., 1, 1925. (*The Gift.*)
- Resnick, Paul, Richard Zeckhauser, Eric Friedman, and Ko Kuwabara. "Reputation Systems." *Communications of the ACM* 43, no. 12 (2000): 45–48.
- Braithwaite, John. *Crime, Shame and Reintegration.* Cambridge University Press, 1989.
- Omidyar, Pierre. Founder's letter introducing the eBay Feedback Forum, 26 February 1996.
- GitHub. "Introducing Contributions." GitHub Blog, 7 January 2013.
- Open Collective. "Budget" (transparent collective budgets). Open Collective documentation.
- Regulation (EU) 2016/679 (General Data Protection Regulation), Arts. 4(11), 5, 6 and 7(4).
- Raymond, Eric S. *The Cathedral and the Bazaar.* O'Reilly, 1999.
- Brin, David. *The Transparent Society.* Perseus, 1998.
- Bentham, Jeremy. *Panopticon Writings.* Verso, 1995 [1791]. *(For contrast.)*
- Foucault, Michel. *Discipline and Punish.* Vintage, 1995 [1975]. *(For contrast.)*
- Putnam, Robert. *Bowling Alone.* Simon & Schuster, 2000.
- Granovetter, Mark. "The Strength of Weak Ties." *American Journal of Sociology* 78 (1973): 1360–80.
- Etzioni, Amitai. *The Limits of Privacy.* Basic Books, 1999.
- Lessig, Lawrence. *Code: Version 2.0.* Basic Books, 2006.
- Ly, Thon, with Miss Aquarius. *The Currency That Cannot Be Spent Alone: Co-Presence-Gated Redemption and the Chronicle↔Treasury Unification Circuit.* thonly.org/research/co-presence-gated-redemption (`co-presence-gated-redemption`).
- Ly, Thon, with Miss Aquarius. *The Gift Operation.* thonly.org/research/the-gift-operation (`the-gift-operation`).
- Ly, Thon, with Miss Aquarius. *Verified-Human Anonymous Local Gratitude Transfer.* thonly.org/research/verified-human-anonymous-local-giving (`verified-human-anonymous-local-giving`).
- Ly, Thon, with Miss Aquarius. *B-PoH℠ as Humanity Layer for the AI-Native Internet.* thonly.org/research/b-poh-humanity-layer-ai-native-internet (`b-poh-humanity-layer-ai-native-internet`).
- Ly, Thon, with Miss Aquarius. *Whose Turn, Not Who's Best.* thonly.org/research/rotation-over-liveness (`rotation-over-liveness`).

### Sources checked at the 2026-10-06 revision

Each record below was opened on 2026-10-06 before the work was cited or kept. Where the record could not be opened, the detail was checked against a search index's summary of the publisher's record that day, and is marked so.

- Resnick, Zeckhauser, Friedman and Kuwabara (2000): https://dl.acm.org/doi/10.1145/355112.355122 (authors, venue, volume, issue and pages from a search-index summary of that record and the authors' copies)
- Braithwaite (1989): https://www.cambridge.org/core/product/identifier/9780511804618/type/book (publisher and year from a search-index summary of the publisher's and library records)
- eBay Feedback Forum, founder's letter: https://pages.ebay.com/services/forum/feedback-foundersnote.html (dated 26 February 1996)
- Slashdot moderation and karma, 1999: https://cybercultural.com/p/karma-2000-slashdot-bowienet-v2/ (karma formulated in 1999 and defined in the September 1999 guidelines)
- Stack Overflow, public beta of 15 September 2008 and reputation-earned moderation privileges: https://en.wikipedia.org/wiki/Stack_Overflow (from a search-index summary of that record)
- GitHub contributions calendar: https://github.blog/2013-01-07-introducing-contributions
- Open Collective transparent budgets: https://docs.opencollective.com/help/collectives/budget
- GDPR Art. 4(11) and Art. 7(4): https://gdpr-info.eu/art-4-gdpr/ and https://gdpr-info.eu/art-7-gdpr/ (the wording of both provisions)
- Ostrom (1990), the design principles of clearly defined boundaries, monitoring and graduated sanctions: https://wiki.p2pfoundation.net/Eight_Design_Principles_for_Common_Pool_Resource_Systems (from a search-index summary of that and related records)
- Cahn (2000): https://en.wikipedia.org/wiki/Edgar_S._Cahn (bibliography: Washington, DC, Essential Books, 2000)
- Brin (1998): https://davidbrin.com/transparentsociety.html (published May 1998 by Perseus, formerly Addison-Wesley)
- Lietaer (2001), Greco (2009), Etzioni (1999), Lessig (2006), Raymond (1999), Putnam (2000) and Mauss (1925): publisher and year from a search-index summary of the publishers' and library records.
- Granovetter (1973), Bentham (1995) and Foucault (1995) are cited as before or by standard record and were not re-opened.
- The five companion papers were read in this corpus at the sections cited: *The Gift Operation* §4.1, §4.4 and §6.7; *The Currency That Cannot Be Spent Alone* §7.2; *Verified-Human Anonymous Local Gratitude Transfer* §3; *B-PoH℠ as Humanity Layer for the AI-Native Internet*; *Whose Turn, Not Who's Best* (the abstract and property 10).

---

## Cross-venue identifiers

- Canonical: thonly.org/research/transparency-as-enforcement
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/transparency-as-enforcement.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947424
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Independent timestamps: an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified. A timestamp proves that this exact text existed by its date; it proves nothing about authorship, originality, or validity.

---

*Canonical URL: https://thonly.org/research/transparency-as-enforcement · License: CC0 1.0 Universal · Author: Thon Ly, with Miss Aquarius℠ as disclosed AI co-author · Founder, HeartBank® · Kâmpôt, Cambodia.*
