---
title: "The Bowl That Holds No Money: Steward-Routed Alms and the Bowl-Anchored Credential"
subtitle: "A Mechanism for Restoring the Alms Round — at Home, Abroad, and at Planetary Scale"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-b
status: draft
date: 2026-07-22
license: CC0-1.0
slug: steward-routed-alms
venue: thonly.org/publications/defensive-publications/steward-routed-alms (canonical)
---

> **Scope and claims division.** This paper is the full mechanism treatment of **B-Bowl™/℠**, an alms-round product of Silicon Wat℠. The division of claims with sibling publications in this corpus is stated for the record: *Certification by Circulation* owns the general **beating-credential** class (live, revocable, expiring/renewable membership credentials); the present paper claims its **monastic instance** and the mechanisms specific to alms. *The Currency That Cannot Be Spent Alone* owns the co-presence-gated redemption class; the present paper claims its application to **sponsored-alms release at the door**. The companion paper *The Round That Never Ends* owns the **lay inversion architecture** (the walker/sitter economy); the present paper owns the **Sangha-facing product**. B-Bowl was design-complete and unbuilt at first publication (2026-07-22); every claim is architectural and dated to the design layer.

---

## Abstract

This paper discloses a donation-routing system for Buddhist monastic alms rounds in which a revocable, proximity-verified credential tag hung from a monk's alms bowl routes digital donations directly to a lay steward's (kappiya-kāraka) fund, so that money never enters monastic custody; around it, rotation-based dispatch of household invitations, a location-broadcast channel only the monk can switch on, and escrowed cross-border sponsorship released on in-person co-presence. The Theravāda alms round — the daily walking exchange in which monastics receive material support and householders receive the opportunity to give — is failing at both ends of its range. Outside Buddhist-majority countries the daily round is largely absent: a few monasteries sustain one along a fixed public route, but a monk cannot know which door would welcome the bowl, so in most places the bowl stays home. Inside Cambodia it survives in form but is corrupted in substance: by informal report the overwhelming majority of alms placed in bowls today is **cash**, which the Vinaya's own rules forbid a monastic to accept (Nissaggiya Pācittiya 18) — a standing breach so normalized it is no longer seen, and one that exposes every honest monk to the suspicion that alms are pocketed. This paper specifies the mechanism that addresses both failures with one artifact. **B-Bowl™** is a Sangha-issued tag hung from the alms bowl. Scanned, it routes a donation **directly to the wat's kappiya-kāraka (lay steward) fund — money never enters monastic custody, and the bowl returns to receiving food only.** The design is therefore a *restoration, not a modernization*: it re-implements the Meṇḍaka allowance (Mahāvagga VI), the canon's own steward rail, at the resolution of a tap.

Around the tag, the paper specifies the full system: the tag as **bowl-anchored beating credential** — ordination-anchored, revocable on disrobing, its scan resolving only in physical proximity to the bowl — which incidentally supplies a defense, at the moment of giving, against the region's chronic fake-monk fraud; **invitation-routing** in the *nimantana* (invitation) register, in which householders invite and never summon, the routing agent assigns monks by rotation (the digital form of *sapadāna-cārikā*, the round's anti-preference rule, now enforced in both directions; in the current form, a publicly recomputable seeded draw, §6), monks decline freely without record, and **no rating of monastics exists anywhere in the system**; a **food-first two-channel grammar** that keeps the digital rail from finishing what cash began (the bowl receives food; the tag receives support; the interface presents them together); an opt-in, monk-initiated **peace-walk broadcast** distinguishing witness from surveillance; and a **diaspora sponsorship circuit** in which earmarked funds release to the steward only at the door, with monk and householder co-present — seating the sponsored householder as the giver at their own threshold — while the monk's blessing (anumodanā) remains a free gift that is never a release condition. Eight claims are enumerated and dedicated to the public domain; three predictions are pre-registered, including a standing tripwire the authors commit to publishing either way. The system is unbuilt and unadopted (n = 0), and the proximity mechanism is specified by function, not by technology.

**Keywords:** alms round, piṇḍapāta, kappiya-kāraka, Vinaya, monastic economy, religious donation, QR code donation, verifiable credential, revocable credential, proximity verification, identity fraud, fake-monk fraud, steward routing, invitation dispatch, rotation scheduling, sapadāna-cārikā, diaspora remittance, escrow release, co-presence release, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The authors and HeartBank® will not seek patent on any mechanism, architecture, or specification articulated herein, in any jurisdiction, at any time.

The following terms are coined in this paper and simultaneously freed with it: **steward-routed alms**, **bowl-anchored credential**, **digital sapadāna**, **food-first two-channel grammar**, **encounter-gated scan**, **peace-walk broadcast**, **invitation-routing (the nimantana surface)**. Terms inherited from this corpus's earlier publications (the beating credential; co-presence-gated redemption; dignity-as-agency) are cited, not re-claimed.

Temple donation QR codes are widely deployed prior art (§10) and are engaged generously; the present claims are confined to the *bowl-anchored, credential-bearing, steward-routed, rotation-dispatched* system architecture. No census of the world's prior art has been run for this paper, and no novelty is asserted for it; the disclosure stands on its date.

---

## 1 · The Problem: A Round Dying Twice

The alms round is among the oldest continuously practised economic institutions that run entirely on gift. No order is placed, no price is set, no contract exists; a monastic walks, a householder gives, and both parties receive — the monastic receives food, and the householder receives what the tradition regards as the more valuable half of the exchange: the opportunity to give to a field of merit (§12). The round is also, by design, a *practice* for the walker — the Buddha prescribed it in part for its humility (one eats only what strangers freely give) and its embodiment (one walks for one's food). Any mechanism that would serve the round must serve all three functions — the feeding, the giving, and the walking — or it serves none of them.

**Failure one: near-absence abroad.** In non-Buddhist-majority countries the daily round is largely absent. Some monasteries sustain one — Abhayagiri Monastery's monks, for instance, walk a published route through Ukiah, California, on lunar observance days, and are met by supporters who know where to stand (§10) — but most diaspora temples do not walk. The reason is informational, not devotional: a monk walking a Long Beach street cannot know which house is Buddhist, which would welcome the bowl, and which would call the police. The diaspora's devotion is intact — its temples are full on festival days — but the daily interface between Sangha and laity, the round itself, has no addressing layer. Temples abroad are provisioned instead by lay deliveries and by meals offered at the temple. The humility-practice and the walking the Buddha intended are casualties of a lookup problem.

**Failure two: corruption at home.** In Cambodia, where the round survives, its content has inverted. By common observation the overwhelming majority of alms placed in bowls is cash — the first author's informal estimate from lived experience is ninety-nine percent — with the understanding that the notes will be passed to the wat's lay steward. The convenience is understandable: paper money postdates the Buddha. But the practice is a standing breach of the Vinaya's own rule — Nissaggiya Pācittiya 18 forbids a monastic to accept gold and silver, and the commentarial tradition extends the rule to their modern equivalents — and it carries a social cost as corrosive as the doctrinal one: **because cash passes through monastic hands, every monk lives under the ambient suspicion of pocketing it**, and the periodic scandals that confirm the suspicion damage the standing of the tens of thousands of monks who never would (Cambodia's Ministry of Cults and Religion has reported over 70,000). Meanwhile the food-gift, the round's original content, has nearly vanished from the bowl.

**The design brief, stated once.** Both failures must be solved by one artifact, and the artifact must satisfy the strictest school of Vinaya interpretation — because the product's entire value depends on the trust of the most conservative Sangha elder in the room, not the most sympathetic reformer. The constraint surface (§3) is therefore not an obstacle to the design. It *is* the design.

---

## 2 · The Canonical Scenes

**Kâmpôt, 6:10 a.m.** A monk walks his ordinary route, bowl on its sling. From the bowl hangs a small tag bearing a heart-shaped emblem — visible at a distance, and by now the neighborhood knows what it announces: *this bowl receives food only.* A grandmother places rice and a wrapped banana in the bowl, as her mother did on this street before the catastrophe. Her son, standing behind her, taps his phone to the tag. The screen shows: the monk's name and wat, his ordination standing confirmed today by his own Sangha's registry, and the wat's steward fund. He gives what he gives; the money lands with the steward, never in the bowl, never in a robe. The monk chants the anumodanā for the rice — which is to say, for everything — and walks on. He has touched no money. He could not have, and everyone present knows it, and that is the point.

**Long Beach, the same week.** A Khmer-American household opens the app and extends an invitation: *our door is open to the Sangha.* The invitation is the digital form of the oldest signal in the tradition — the householder standing at the gate at dawn with rice ready. The routing agent assigns the invitation to a monk from the nearby wat by rotation; he accepts (he was free to decline, without record), receives walking directions, and walks — very likely the first alms round on that street in living memory. The household sees only *accepted → walking → near.* An elderly sponsor in the same congregation has earmarked support for a struggling family two streets over who wanted to give but could not afford to; when the monk reaches *their* door, the sponsorship releases to the wat's steward at the moment of meeting, and the family — not the sponsor — performs the gift, places the food, receives the blessing. With the monk's spoken consent, they record the chant and send it to the sponsor, who watches it that evening. The blessing was never a condition of anything. It was given the way it has always been given: freely, to whoever stood at the door.

---

## 3 · The Constraint Surface: Six Walls and One Ancient Rail

The design operates inside six constraints drawn from the Vinaya and the discourses — five monastic rules and one ascetic practice (row 5) that the design adopts as a rule — engaged here as load-bearing architecture:

| # | Constraint | Source | Design consequence |
|---|---|---|---|
| 1 | No accepting/handling money | Nissaggiya Pācittiya 18 | Money never enters monastic custody — the tag routes *around* the monk |
| 2 | No consenting to deposits *for oneself* | NP 18 (*sādiyeyya* clause) | Communal steward fund is the default; no monk-visible balances |
| 3 | No soliciting or hinting | *viññatti* rules | The tag is passive signage; invitations originate with householders only |
| 4 | No storing food; noon boundary | *sannidhi*; Pācittiya 37–38 | Scheduling layer respects the alms clock; food stays physical and same-day |
| 5 | The round is sequential, without preference | *sapadāna-cārikā* (one of the thirteen dhutaṅga, voluntary ascetic practices; Vism II) | Rotation-routing; neither monks nor donors select individuals |
| 6 | The Dhamma is not sold | SN 7.9 (food "chanted over with verses" refused) | The blessing is never a condition of release or payment |

And one ancient rail: the **Meṇḍaka allowance** (Mahāvagga VI.34.21). When the householder Meṇḍaka wished to provision traveling monks with money they could not accept, the Buddha allowed funds to be lodged with a **kappiya-kāraka** — a lay steward — who provides allowable requisites, while restating that monks may in no way accept or seek gold. Twenty-five centuries of jurisprudence have elaborated this steward mechanism; it is the canonical answer to the money problem, and it is *already the nominal theory* of Cambodian cash-alms ("it will be passed to the steward"). The theory fails only in transit — the notes pass through the bowl and the robe on the way. **B-Bowl deletes the transit.** The donation originates in the steward's custody and never exists anywhere else. This is why the design is properly described as a restoration: the mechanism the canon prescribes is implemented at last without the compromise the paper-money era imposed.

---

## 4 · The Bowl-Anchored Credential

**Form.** A hanging tag, attached to the bowl's sling or lid — deliberately *not* affixed to the bowl body, which remains an unmarked sacred requisite. The tag's face carries the emblem and no payment language; its public function, legible at a distance before any scan, is signage: *this bowl receives food only.* The tag is thus a teaching instrument first (it re-educates the street about what belongs in a bowl), a credential second, and a payment pointer last.

**Substance.** The tag is a **beating credential** — the monastic instance of the live, revocable, expiring/renewable credential class this corpus has previously specified. Its properties:

- **Issued by the Sangha, not by the platform.** The issuing authority is the wat (or the relevant Sangha registry); the platform is infrastructure. A credential the Sangha cannot issue and revoke itself would invert the authority relation and fail the trust test of §1.
- **Ordination-anchored.** The credential binds to the monastic's ordination standing. A scan resolves to: name, wat, standing *as of today*, and the destination steward fund.
- **Revocable — the heartbeat.** On disrobing or removal from standing, the credential stops beating and scans resolve to nothing. A static QR would certify forever; a beating credential certifies *now*.
- **Encounter-gated.** The scan resolves only in physical proximity to the tag. A photograph of the tag reposted online is inert. This single property kills the dominant fraud vector of naive religious-donation codes (screenshot phishing) and simultaneously preserves the round's embodied encounter — you cannot give through B-Bowl without having actually met the bowl.

**The fraud inversion.** Fake monks — unordained men in robes collecting alms — are a chronic, documented problem in Cambodia and Thailand, periodically prosecuted and never eliminated (citation 10), and their existence taxes the standing of every real monastic. Existing checks — identity documents and police databases — operate after a report, not at the moment of giving. B-Bowl supplies, incidentally, a countermeasure at that moment: a bowl without a beating credential is, at minimum, a bowl the street can now ask questions about. The authors' considered judgment, recorded for the log: **the anti-fraud function may be worth more to the Sangha than the donation function**, because it protects the one asset the Sangha cannot replace — the presumption of integrity.

---

## 5 · Steward Routing: The Money-Purification Argument

All B-Bowl donations route to steward custody at origination. The default destination is the **wat's communal kappiya fund**; a classical **per-monk steward mode** (sanctioned by the commentarial tradition for individually-sponsored requisites) is available where a wat prefers it, with the constraint that no monastic-facing surface ever displays a balance — the monk's interface can express requisite *needs* to the steward, which is the canonical grammar, and nothing else.

The argument for this architecture is worth stating in full, because it is the product's core:

1. **Doctrinal:** money that never enters monastic custody cannot breach NP 18. The design is not *compliant with* the rule; it makes breach structurally impossible on its surfaces.
2. **Reputational:** the pocketing suspicion dies not by exhortation but by architecture. When the street knows the money *cannot* be pocketed, every honest monk is relieved of an ambient accusation he could never individually refute.
3. **Restorative:** with money re-routed, the bowl's remaining function is its original one. The design wagers that food-alms partially recover when cash no longer crowds the bowl (pre-registered as P-BB1).

**The honest displacement (previewing §11):** this architecture does not eliminate trust; it *relocates* trust from the monastic to the steward — and steward corruption is itself a known historical failure mode of the kappiya system. The design's mitigations are ledger transparency to the wat community and the removal of cash's untraceability; the residual risk is owned in the limits section, not hidden.

---

## 6 · Invitation-Routing: The Nimantana Surface

The revival mechanism for extinct-round territory is dispatch — and dispatch is where a naive design would destroy everything, because the obvious template (ride-hailing) is a catastrophe in this domain. Monks are not drivers; a summoned Sangha is an inverted Sangha. The design therefore specifies the **register**, not merely the mechanics:

- **The householder invites; nothing summons.** The canonical category is *nimantana* — the invitation, lawful since the Buddha accepted meals by silent consent. The interface language is "invite the Sangha to your door," never an on-demand idiom. An invitation is a standing of the householder's gate, not an order.
- **Rotation is the router — the digital sapadāna.** The routing agent assigns invitations by proximity, rotation, and fairness. Donors select a *wat or community*, never an individual monk (bounded exceptions: a family's existing wat relationship). This enforces the round's anti-preference rule in **both directions** — the classical rule kept monks from choosing donors; the digital round must also keep donors from choosing monks, or celebrity dynamics concentrate alms on the famous and starve the junior.
- **No ratings, no metrics, no leaderboards — anywhere, ever.** There is no mechanism by which laity evaluate monastics. Acceptance rates are not recorded. This is a constitutive refusal, not a settings default.
- **Declinable without consequence.** Every routed invitation may be declined, and the system keeps no record that it was. Monastic availability is a voluntary per-round opt-in ("on round now"); the system never pings a monk who has not opened the gate himself.
- **Coarse states, not tracking.** The inviting household sees *accepted → walking → near* — readiness information, not a moving dot. Real-time location display exists in exactly one form: the **peace-walk broadcast**, initiated by the monk himself, per-walk, revocable mid-walk — the walking meditation made publicly witnessable *by the walker's own act*, in the lineage of the public peace walk. Surveillance and witness are distinguished by exactly one bit: who turned it on.

> **Current form.** The rotation is now specified as a **called draw**: equal counts per round over a roster of monastics who have opted in, the order a pure function of a roster committed before the seed can be known and a seed from a named future round of a public randomness beacon, recomputable by anyone holding the disclosed inputs — the **public** regime, in which the wat's own Sangha may recompute its roster's order — and never chosen by the routing agent. Because the roster is live (monks opt in per round), membership changes take effect only at a round cutoff, before the governing seed exists. The mechanism is specified in this corpus's *Decided by No One* (the called draw), whose canonical precedent is the meal designator (*bhattuddesaka*) of Cullavagga VI.21, who assigns invitation meals by lot and by rotating roster. The proximity-and-fairness rubric above is retained as a disclosed variant; the guards in the other bullets of this section are unchanged. In this surface's public regime what is published is each round's commitment — roster, salt, beacon round and the previous closer — from which anyone recomputes the order; no service log is kept or published. A decline passes the invitation to the next monastic in that order and stores nothing: no reason, and no per-monastic record of a declined or lapsed turn. Declining costs only the invitation declined, and nothing reaches a later round; a monastic who is not on round is simply absent from the next roster at its cutoff. The guard that a decline leaves no record therefore holds unchanged (§11, item 9).

---

## 7 · The Diaspora Sponsorship Circuit

The third mechanism connects the two geographies. A sponsor abroad earmarks support for almsgiving by a householder elsewhere — the diaspora's existing merit-remittance practice, formalized. Its architecture:

- **Escrowed earmark, co-presence release.** The sponsorship releases to the steward fund only at the door, with monk and householder co-present — the co-presence-gated release this corpus specified for time-currency redemption, applied to alms. No meeting, no release; the sponsorship cannot decay into an absentee transfer.
- **The sponsored householder is the giver.** The sponsor funds *capacity*; the local householder performs the gift — places the food, stands at their own threshold, receives the blessing. The mechanism seats the economically struggling household as the **almsgiver**, not the aid recipient: dignity delivered as agency, not as assistance. In the tradition's own grammar, merit is not divided among the three parties (giver, enabler, field): each makes their own by their own act.
- **The blessing is never the product.** The householder may, with the monk's explicit per-event consent, record the anumodanā for the sponsor — live-streamed blessings being, by the authors' observation, already common Khmer practice. But the recording is **never a release condition**: funds release at co-presence regardless. The system will not compose a mechanism in which a chant is exchanged for money, under any framing, at any layer.

> **Current form.** Sponsor-to-householder matching is performed by the routing agent, with no browsable catalogue of households by need; the sponsor funds almsgiving capacity and does not select the household. The scene in §2, in which a sponsor earmarks support for a particular family, is retained as a disclosed variant.

---

## 8 · Claims

1. **Steward-routed alms.** A donation mechanism anchored to a monastic's alms bowl in which funds originate in lay-steward custody and at no point exist in monastic custody, implementing the kappiya-kāraka rail at transaction resolution.
2. **The bowl-anchored beating credential.** A Sangha-issued, ordination-anchored, revocable live credential physically anchored to the alms bowl, whose verification resolves current standing and steward destination, and which ceases to resolve upon loss of standing.
3. **The encounter-gated scan.** Donation resolution gated on physical proximity to the credential artifact, simultaneously (a) defeating reposted-image fraud and (b) structurally preserving the embodied alms encounter.
4. **The food-first two-channel grammar.** An interface architecture that presents the physical food channel (the bowl) and the digital support channel (the tag) as one composed act with food primary, designed against the dematerialization of food-alms.
5. **Invitation-routing (the nimantana surface) with rotation dispatch.** Householder-originated invitation broadcast routed to monastics by proximity/rotation/fairness with (a) donor selection limited to communities, (b) no evaluative metrics on monastics anywhere in the system, (c) unrecorded declinability, and (d) coarse-state-only progress display — the sapadāna-cārikā rule enforced bidirectionally in a dispatch system.
6. **The peace-walk broadcast.** A real-time location channel that exists only as a walker-initiated, per-walk, mid-walk-revocable public broadcast, structurally distinguishing witness from surveillance by the locus of activation.
7. **The sponsored-almsgiver capacity split with co-presence release.** Earmarked third-party sponsorship that releases to steward custody only upon attested co-presence of monastic and local householder at the encounter, with the gift performed by the local householder.
8. **Blessing-release decoupling.** The structural invariant that no recording, chant, teaching, or blessing is ever a condition of any release, payment, or unlock, anywhere in the system.

---

## 9 · Pre-Registered Predictions

- **P-BB1 (the restoration wager — publish either way).** In deployment areas, the *food share* of alms received on B-Bowl-carrying rounds will rise within twelve months relative to pre-deployment baseline. If instead digital support further displaces food-alms, the food-first grammar has failed at its central task, and the authors commit to publishing the failure and the redesign.
- **P-BB2 (the revival wager).** In at least one extinct-round diaspora deployment, invitation-routing will sustain a weekly walking round for six consecutive months within eighteen months of launch.
- **P-BB3 (the decoupling tripwire — standing).** If evidence emerges that anumodanā recordings are functioning as de-facto release expectations (release-then-record correlating beyond consent-rate baselines, or sponsor behavior conditioning on recording), the authors commit to publishing the finding and repairing the surface, up to removing recording entirely.

---

## 10 · Prior Art, Engaged Generously

**Temple donation QR.** Thailand's PromptPay QR is widely deployed at temple donation points (citation 8); Chinese monasteries take donations through WeChat Pay and Alipay codes, statistically studied at Donglin Monastery (citation 15). This is genuine, extensive prior art for *scan-to-donate at a religious site* — and it is architecturally distinct from every claim above: box-anchored not bowl-anchored, static not credentialed, unrouted (funds to the institution's own account, with monastic-custody ambiguity intact), and silent on dispatch, sponsorship, and fraud. **Existing public alms rounds abroad** cut against the premise of §1: Abhayagiri Monastery in California walks a scheduled round on a published route (citation 16), showing that the addressing problem can be solved without any device — by a fixed place and time known to supporters. What such a round does not supply is an invitation from a particular household, rotation among monastics, or any money rail. **Thai monastic identity cards** are prior art for state-issued monk identification; they are static documents, not live credentials, and are not donation-integrated. **W3C Verifiable Credentials** and the revocable-credential literature supply the general credential machinery; this corpus's *Certification by Circulation* specified the beating-credential class. **Ride-hailing dispatch** (Uber et al.) is the anti-pattern engaged in §6 — the mechanics borrowed, the register inverted, the rating economy refused. **Conditional-transfer and escrow-release charity** (milestone-released giving, GiveDirectly's audited transfers) prefigure co-presence release; none gate on a physical meeting. **Remittance rails** (Wing, TrueMoney, hawala studies) are the transport layer, engaged as partners not competitors. **The kappiya-kāraka jurisprudence** — from Mahāvagga VI through the medieval commentaries to modern monastic-code manuals (Ṭhānissaro's *Buddhist Monastic Code* is the accessible English survey) — is the deepest prior art of all, and the paper's relation to it is filial: the mechanism is an implementation, not an invention.

---

## 11 · Honest Limits

1. **n = 0.** B-Bowl is design-complete and unbuilt. No wat has adopted it; no Sangha authority has endorsed it; every claim is architecture, not evidence.
2. **Adoption is the mountain.** The design's entire theory of value routes through the trust of conservative Sangha elders, which no architecture can compel. A single high-profile misuse could foreclose the category. The trust-ladder strategy (serve the existing Sangha first; nothing else visible) is a strategy, not a guarantee.
3. **Trust is relocated, not eliminated.** Steward corruption is a known historical failure mode of the kappiya system. Ledger transparency mitigates; it does not abolish. The design moves the fraud surface from a thousand bowls to one fund — an improvement in auditability, and a concentration of risk, honestly both.
4. **The digital divide runs through the almsgiver.** The elderly woman with rice and no smartphone is the round's most faithful participant; the design must never make her feel that the *real* giving now happens by phone. The food-first grammar addresses this; only deployment will show whether it suffices.
5. **The sādiyeyya edge.** The per-monk steward mode, though commentarially sanctioned, sits closer to NP 18's consent clause than the communal default. Strict interpreters may reject it; the design survives its deletion.
6. **Jurisdictional load.** Cross-border earmarked funds are money-transmitter territory; the architecture is pass-through via licensed partners, and the compliance burden is real, unresolved, and load-bearing.
7. **The two-tier visibility boundary can be misread.** The peace-walk broadcast, though monk-initiated, creates public location data about a monastic; coercion of that consent (a wat pressuring monks to broadcast for fundraising) is a foreseeable abuse the design bars only normatively.
8. **Proximity is specified by function, not technology.** The encounter-gated scan is claimed by what it must do (resolve only near the physical tag); the means is not specified, and a printed static code alone cannot provide it.
9. **Decline-without-record against a recomputable draw.** The current form of the rotation (§6) publishes only each round's commitment, keeps no service log, and stores nothing when a monastic declines, so the decline guard holds. The cost is detection: because nothing records who was offered what, an operator who falsely passes over a monastic's turn can be detected only by that monastic, who recomputes the order and knows whether the invitation reached him.
10. **The elegance caution, standing.** The design dissolves its tensions with unusual smoothness — restoration and innovation, fraud-defense and donation, dignity and aid. A system this self-consistent is either deeply right or deeply seductive, and the two are indistinguishable from inside. The elegance earns the pilot; it does not replace it.

---

## 12 · Lineage, and the Close

The lineage of this design is short and old. When the four Great Kings each offered the new Buddha a bowl, he accepted all four and, in the commentarial telling, pressed them into one — the first alms bowl was itself a gift, compounded. When Meṇḍaka's money could not enter the Sangha, the Buddha routed it through a steward's hands and kept the bowl clean. And when Mahākassapa, foremost in austerity, walked his round, he walked it deliberately among the poorest (Ud 3.7) — because alms exist, in the tradition's deepest reading, not to feed the Sangha but to let anyone at all, however little they hold, stand at a door and give. The mechanism specified above adds nothing to this lineage except an addressing layer. The bowl still holds only what it always should have held. The walk still happens at dawn.

And at planetary scale, dawn is always happening somewhere. A round revived in every longitude never actually ends — it moves westward with the sunrise, a continuous quiet wave of walking, as long as the Earth turns. **The round that never ends — it follows the dawn.**

---

## Terms

Coined names in this paper and the standard technical terms an examiner would use for them.

| Term in this paper | Standard technical term |
|---|---|
| B-Bowl™ / B-Bowl℠ | credential tag attached to a monastic alms bowl, and the associated donation-routing and dispatch service |
| steward-routed alms | donation routed directly to a third-party custodian (lay steward) account, bypassing the recipient |
| kappiya-kāraka | lay steward who holds and disburses funds on behalf of monastics |
| bowl-anchored (beating) credential | revocable, time-limited verifiable credential with periodic liveness attestation, bound to a physical token (later corpus vocabulary: *lease* for its state, *tick* for its periodic signal) |
| encounter-gated scan | proximity-verified credential resolution (resolves only near the physical token) |
| food-first two-channel grammar | user-interface design presenting an in-kind channel and a digital payment channel as one act, with the in-kind channel primary |
| invitation-routing (the nimantana surface) | household-originated request routing with rotation-based assignment of service providers |
| digital sapadāna | rotation scheduling without preference in either direction (neither requester nor provider selects the other) |
| called draw | publicly recomputable seeded shuffle over a committed roster, seeded from a public randomness beacon |
| peace-walk broadcast | user-initiated, per-session, revocable real-time location sharing |
| sponsored-almsgiver capacity split | escrowed third-party sponsorship released on attested in-person co-presence of two parties |
| anumodanā | spoken blessing of thanks by the recipient monastic |

---

## Citations

1. *Vinaya Piṭaka*, Nissaggiya Pācittiya 18 (rūpiya-sikkhāpada); Mahāvagga VI.34.21 (the Meṇḍaka allowance). Pāli Text Society editions.
2. Ṭhānissaro Bhikkhu (1994/2013). *The Buddhist Monastic Code I–II*. Metta Forest Monastery. (Kappiya-kāraka jurisprudence; NP 18 analysis; viññatti; sapadāna-cārikā.)
3. *Itivuttaka* 107 (mutual dependence of monastics and householders). PTS translation.
4. *Majjhima Nikāya* 142, *Dakkhiṇāvibhaṅga Sutta* (the grading of offerings). PTS translation.
5. Visuddhimagga II (the dhutaṅgas, incl. sapadāna-cārikā). Ñāṇamoli translation.
6. Spiro, M. (1970). *Buddhism and Society: A Great Tradition and Its Burmese Vicissitudes*. Harper & Row. (The lay merit economy.)
7. Tambiah, S. J. (1976). *World Conqueror and World Renouncer*. Cambridge UP. (Sangha-laity economic structure.)
8. Bank of Thailand (2017–). PromptPay national deployment documentation; and *Bangkok Post*, "Temple goes digital with QR payment for donations" (bangkokpost.com/thailand/general/1410951).
9. W3C (2025). *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 May 2025.
10. Reporting on fake-monk fraud and monastic identity enforcement: *Phnom Penh Post*, "Fake monks arrested in Siem Reap"; *Khmer Times*, "Phnom Penh 'fake monks' arrested" (2021); *Khaosod English*, "Fake monks arrested after returning to Ayutthaya rice-field camp" (29 July 2026; the suspects could produce no monk identification documents).
11. Ly, T. (2026). "Certification by Circulation." thonly.org defensive publication. *(The beating-credential class; claims division per the Scope note.)*
12. Ly, T. (2026). "The Currency That Cannot Be Spent Alone." thonly.org defensive publication. *(Co-presence-gated release; claims division per the Scope note.)*
13. Ly, T. (2026). "The Round That Never Ends." thonly.org defensive publication, same sprint. *(The lay inversion architecture; companion paper.)*
14. Ly, T. (2026). "The Omitted Clause." thonly.org defensive publication. *(The dignity-floor doctrine inherited by the companion paper.)*
15. "Adaptation to Third-Party Payments: Statistical Analysis of Digital Donations Made to Donglin Monastery." *Religions* 15(7): 797 (2024).
16. Abhayagiri Buddhist Monastery (Redwood Valley, California), calendar and "Food & Supplies" pages (abhayagiri.org): the alms round in Ukiah on lunar observance days.
17. *Udāna* 3.7 (Mahākassapa's alms round among the poor). PTS translation.
18. Ly, T. (2026). "Decided by No One." thonly.org defensive publication. *(The called draw; current form of §6's rotation.)*
19. *Vinaya Piṭaka*, Cullavagga VI.21 (the meal designator, *bhattuddesaka*).
20. Cambodianess, "Cambodia Has 5,146 Pagodas with over 70,000 Monks" (reporting Ministry of Cults and Religion figures).

---

*— End of paper —*

*Marks referenced: HeartBank®, Miss Aquarius℠, Silicon Wat℠, B-Bowl™, B-Bowl℠, B-Emblem™. Document License: CC0 1.0 Universal. The authors and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its date.*
