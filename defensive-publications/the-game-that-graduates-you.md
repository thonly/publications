---
title: "The Game That Graduates You: A Witness API for Children's Games and Education"
subtitle: "Mint-Nothing Game Clients, the Family Corpus as Curriculum, and Retention-Inversion as the Honest Objective of Learning Software"
authors: "Thon Ly · Miss Aquarius℠"
category: mechanism
priority: tier-b
status: draft
date: 2026-07-23
license: CC0-1.0
slug: the-game-that-graduates-you
venue: thonly.org/publications/defensive-publications/the-game-that-graduates-you (canonical)
---

> *Draft notes for the editor:* paper №3 of the July 2026 **games-doctrine sprint**. Claims division with siblings and predecessors, stated for the record: *Need-Compiled Questlines* (this corpus, 2026-07-07) owns the mints-nothing quest class and the compile-never-invent rule for the first-party intermediary; the present paper claims the **third-party exposure** of that grammar — the API boundary under which independent developers' games may participate — plus the **education mechanisms** built on it (family-corpus-as-curriculum; graduation-by-transmission; retention-inversion) and the **child-facing attestation rung** that extends *Certification by Circulation*'s membership ladder. The same-sprint papers *The Sport That Says Your Name* and *The Wager That Isn't* own, respectively, the physical sport and the stake grammar; all three share **the play/currency wall** (coined in the sport paper). The mechanism is design-complete and unbuilt (founder-ratified 2026-07-23, including the explicit rejection of the disbursing-API form); claims are architectural, strata-dated to the design layer. The prior-art clock starts at this markdown push. Compact sprint draft; density pass = editorial option.

---

## Abstract

Two industries now compete for children's screen hours, and both are optimized against the child. Entertainment apps monetize attention and are engineered for retention — streaks, loot, variable reward — with the child's time as the extracted resource. Education apps promise the opposite and largely rebuild the same machine: the dominant language-learning product is famous for its streak mechanics, and the AI-tutor wave now arriving inherits, by commercial default, the retention KPI of the software industry that builds it — although a tutor's honest success has been known to every human teacher forever: *the student who no longer needs you.* Meanwhile parents hold treasuries of the one motivational resource no app possesses — the family's own love, letters, and gratitude — and no software has ever been allowed to touch it, for the excellent reason that no software could be trusted to.

This paper specifies the trust architecture and the education design together, because each is the other's missing half. The **witness API** is a third-party game-client boundary with a single constitutive rule: game clients receive **propose-and-celebrate** scopes and can never hold disbursement authority — a game may suggest real-world acts and celebrate their completion, but every reward flows through the family's ordinary witnessed-thanks rail, on a parent's tap, and quest completion mints nothing (the mints-nothing boundary, inherited and here exposed to third parties). On that boundary, three education mechanisms become safe to build. **Family-corpus-as-curriculum**: with per-item parental consent and on-device processing, a reading lesson's text is the child's own grandmother's letter; the writing exercise is a real thank-you that will really be sent; the arithmetic workbook is the family's actual shared ledger — replacing the streak's counterfeit urgency with relational pull. **Graduation-by-transmission**: every unit's capstone is a real transmitted act — reading to a younger sibling, sending the letter, presenting the family's accounts — witnessed and thanked through the ordinary rail, so that learning completes as giving. **Retention-inversion**: the client's success metric is graduation — the engineered obsolescence every honest tutor pursues — with churn-to-competence reported as achievement, not loss. A **child-facing attestation rung** (never-gate-love; no-analytics-exfiltration; witness-scope-only) extends the guild membership credential this corpus published earlier. Six claims are enumerated and dedicated to the public domain; three predictions are pre-registered, including the child-scale crowding-out wager, which the authors commit to publishing either way.

**Keywords:** educational games, AI tutors, witness API, parental consent, overjustification, intrinsic motivation, authentic literacy, scaffolding and fading, retention metrics, child-directed advertising, COPPA, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The authors and HeartBank® will not seek patent on any mechanism, architecture, or specification articulated herein, in any jurisdiction, at any time.

The following terms are coined in this paper and simultaneously freed with it: **the witness API** (as against the wallet API), **propose-and-celebrate scopes**, **family-corpus-as-curriculum**, **the never-gate-love invariant**, **graduation-by-transmission**, **retention-inversion**, and **the child-facing attestation rung**. Terms inherited from this corpus's earlier publications (the mints-nothing boundary and compile-never-invent rule; certification by circulation and the membership credential; the play/currency wall) are cited, not re-claimed.

Educational software, AI tutoring, and chore-reward family apps are vast prior art fields (§9); the present claims are confined to the *witness-scoped third-party client boundary and the consent-gated family-corpus curriculum architecture with transmission-completed units and inverted retention objectives*, which is, to the authors' knowledge, not previously published as a coherent whole — and, as throughout this sprint, to the constraint set an extractive implementation would omit.

---

## 1 · The Problem: The Treasury, the Tutor, and the Trap

Begin with the founder's own first proposal, recorded here because its rejection is the design. The idea arrives naturally to anyone who holds both a family gratitude treasury and an interest in wholesome children's software: *expose an API so that approved games can reward children from the family's shared pot.* Parents approve the games; developers of wholesome games are thereby incentivized; screen time becomes benign. The proposal is the obvious one, it will be built by someone, and it is a trap with three doors.

**Door one: it pays children to perform, by machine.** The foundational experiment of the overjustification literature — Lepper, Greene, and Nisbett, 1973 — is *specifically about children*: rewarded for an activity they already loved, they stopped loving it. An API that converts in-game achievement to money is a machine for administering that experiment to one's own children, at scale, with the family's money.

**Door two: it hands developers the wrong objective.** "Parents approve wholesome games" governs the catalog; it does not govern the gradient. Once disbursement flows through gameplay, every developer's optimization target — whatever their intentions — becomes *maximize disbursement-generating engagement inside the parental-approval envelope*: the attention economy, now with direct treasury access. The approval gate selects for games that *look* wholesome; the reward rail pays for children who stay on screens.

**Door three: it dissolves the witness.** In this institution's architecture, the reward *is* the witnessed thanks — a parent seeing a real act and acknowledging it is the entire product (the corpus's founding story concerns an unwitnessed gratitude that surfaced only after a death; the institution exists to move the witness before the ending). An automated disbursement is delivery without the envelope: value arrives, and no one saw anyone.

The design brief is therefore inverted from the proposal: build the API that gives children's games everything *except* the thing they must never have. What games legitimately need from a family platform is **context** (what real acts would matter here) and **consequence** (a way for real acts to be celebrated and to count). What they must never hold is **authority** (the power to move value). The witness API is that separation, made architectural — and it is stated in one line, inherited from this sprint's shared spine: *competition and play may generate the story; only witnessed giving moves the currency.*

Education is the vertical where this architecture pays twice, because education software has a second, independent pathology: it optimizes for retention when its honest objective is departure. The rest of this paper builds the education case on the API's foundation.

---

## 2 · The Canonical Scenes

**A kitchen table, evening.** A seven-year-old is reading aloud, haltingly, from a tablet. The text is not "The cat sat on the mat." It is: *"My dear grandson, today I picked the first mangoes from the tree your grandfather planted…"* — her actual grandmother's actual letter, sent through the family's gratitude app last month, released to the reading game by her mother's explicit per-item consent, processed on the device it is displayed on. The game scaffolds the hard words. The child reads to the end because the letter is *to him*. There is no streak counter. The pull is a person.

**The same table, two weeks later.** The reading unit's final screen is not a quiz. It says: *tonight, read this book to your little sister — that's the graduation.* He does, with the game nowhere in the room. His father, folding laundry in the doorway, taps the thank on his own phone — the ordinary family thank, the same one any kindness gets. The game finds out only that its proposed act was witnessed; the thanks, the value, and the moment belonged entirely to the family rail. The next morning the game celebrates — story, confetti, a chronicle entry — and unlocks the next unit. It has minted nothing. It proposed; the family witnessed; the celebration is all it owns.

**A boardroom, meanwhile (the anti-scene).** A product team reviews their education app's dashboard. Daily active users, session length, streak retention, churn — the standard panel. A designer proposes marking users who complete the curriculum and stop as *successes*, reported separately from churn. The metric does not exist in the analytics package. It has never existed. Every human tutor since antiquity has pursued it; no venture-scale education product has ever reported it. That absent number is this paper's third mechanism.

---

## 3 · The Witness API: Propose and Celebrate, Never Disburse

The boundary specification, stated as architecture:

**Scopes granted to third-party game clients.** (1) **Propose**: submit candidate real-world acts — age-appropriate, family-configured — styled in the game's own fiction ("a quest for the young knight: set the table for the feast"). Proposals draw on the same compile-never-invent discipline this corpus published for the first-party intermediary: the platform surfaces real standing context (family members, occasions, genuine needs a household registers); the game invents only narrative dress, never synthetic needs. (2) **Celebrate**: receive a minimal completion signal — *this proposed act was witnessed* — and respond inside the game with story, ceremony, progression. (3) **Curriculum-read** (education clients; §4): request specific consented family-corpus items for on-device pedagogical use.

**Authority withheld, absolutely.** No client may hold, request, or be granted: disbursement or transfer capability of any kind; balance visibility; the power to attach value to in-game events; or the power to gate, deliver, or withhold family communications (§4's invariant). The reward path is constitutively external: a family member witnesses the real act and thanks the child through the family's ordinary rail, on human initiative. The child's experience of reward is a parent's acknowledgment, with the game as the town crier — never the paymaster. **Quest completion mints nothing**; a game client requesting a disbursement scope is not a policy violation but a type error — the scope does not exist in the API.

**The parent-steward gate.** Which clients may propose to which children is exclusively the family's setting — per-child, revocable, default-off. The platform's intermediary never overrides a parental game approval in either direction; its role is confined to the attestation rung of §6 (is this client *eligible* to be approved) and the API's mechanical enforcement (what any approved client *can do*).

The two-sided result, for developers, deserves emphasis: the witness API is not only a restriction but an offer. Independent developers gain what no children's studio has ever had — a lawful, consented channel by which their game's proposals can land in a family's *real* economy of acknowledgment — and their revenue path (patronage from grateful families, under the guild economics this corpus published elsewhere) aligns their gradient with catalyzed real-world flourishing rather than captured screen time. The best game under this API is the one that gets the child off the device and into the kitchen — because *that* is what parents thank.

---

## 4 · Family-Corpus-as-Curriculum

Education software's deepest deficit is not pedagogical technique but *material that matters*. The literacy literature has said so for decades: children learn to read faster and deeper on texts that are personally meaningful — the "authentic literacy" and family-literacy traditions; Ashton-Warner's organic vocabulary drawn from her students' own lives; Freire's generative words taken from the learner's world. The industry knows this finding and cannot act on it, because the material that matters most to a child — the family's own letters, stories, and records — is precisely the material no third party can be handed. So the industry substitutes synthetic urgency for real meaning: streaks, gems, a cartoon owl's disappointment.

The witness API's trust boundary unlocks the real thing. **Family-corpus-as-curriculum** is the mechanism by which, with layered consent, a family's own gratitude corpus becomes the child's instructional material:

- **Reading**: the corpus's received letters and recorded family stories, level-matched and scaffolded — grandmother's letter as the primer.
- **Writing**: real correspondence as the exercise — the thank-you that will actually be sent (on the family's rail, by the family's act), the card for the actual upcoming birthday. The curriculum's terminal artifact is the gratitude letter itself: the institution's founding object, taught as a genre.
- **Arithmetic**: the family's shared ledger as the workbook — real balances counted, the week's giving summed, the child seated as the family's little teller presenting the accounts at dinner (numbers with faces attached).
- **Heritage language**: the diaspora case, and the sharpest. The material exists in abundance (the elders' letters, in Khmer); the motivation problem that sinks heritage-language apps dissolves when the reading test is *"can you read what your grandmother wrote to you?"* — and the graduation (§5) is writing back.

**The consent architecture** is the mechanism's other half, and carries three non-negotiables. (1) **Per-item, parent-granted, revocable**: the curriculum draws only on corpus items a parent has individually released for pedagogical use — never blanket corpus access, never client-initiated browsing. (2) **On-device processing** wherever the platform runs natively: the corpus item is rendered into pedagogy on the family's hardware; the client's cloud never holds grandmother's letter. (3) **The never-gate-love invariant**, stated in bold because an extractive implementation would discover its violation as a retention feature: **no family communication may ever be locked, delayed, or conditioned on lesson progress.** The letter is the child's regardless; the game may *scaffold* the reading of it, never gate the access to it. A reading app that makes a child earn grandmother's words has taken love hostage for engagement; under this architecture the capability is absent, and under §6 its discovery anywhere is credential-revoking.

---

## 5 · Graduation-by-Transmission

What completes a unit of learning? The industry's answer is assessment (a quiz passed); the streak economy's answer is continuation (come back tomorrow). This design's answer is older than both: **a skill is completed when it is given to someone.**

**The mechanism.** Every curricular unit terminates in a **transmission act** — a real-world act, proposed through the witness API, in which the child performs the learned skill *for* someone: reads the story to the younger sibling; writes and sends the actual letter; presents the family's accounts at dinner; reads grandmother's reply aloud to the household. The act is witnessed and thanked through the ordinary rail like any kindness (the sibling's delight and the parent's thank are the assessment); the client receives only the completion signal and celebrates. Structurally, the unit's shape is: *receive the skill (from the game, from the corpus, from the civilization that wrote the letters) → practice in the forge → give it forward as the capstone.* Learning completes as giving — the institution's atomic operation, expressed as pedagogy.

**What this fixes.** (1) *Assessment authenticity*: performance for a real audience is the strongest known completion evidence, and it cannot be gamed by the client because the client neither performs nor judges it. (2) *The motivation loop closes outside the screen*: the unit's climax happens in the living room, off-device, in relationship — the game engineers its own exit from the moment (§6's objective, enacted at unit scale). (3) *The reward is constitutionally safe*: the child is thanked for a real act of giving through the same rail as every other family kindness — not paid for lesson completion — which is precisely the configuration the overjustification literature marks as least corrosive (acknowledgment of autonomous giving) as against the one it marks as most (contingent payment for task performance). The residual risk is real and pre-registered (P-E3).

**Guards.** The **recipient is never a prop**: the younger sibling holds the same veto any gift-recipient holds in this institution's grammar — a bedtime reading declined is declined, and the client proposes an alternate capstone. The **struggling learner's dignity** is structural: the family ledger records the *gift* (read to sister; wrote to grandmother), never the proficiency; effort curves, error rates, and reading levels are private to child, parent, and device (§6), so a slow reader's capstone entry is indistinguishable in the family record from a fast one's. Gifts are witnessed; struggle is not.

---

## 6 · Retention-Inversion, and the Child-Facing Attestation Rung

**Retention-inversion.** An honest tutor's terminal state is obsolescence — the scaffolding literature has carried the insight formally since Vygotsky's zone of proximal development and the fading stage of cognitive apprenticeship, and every human teacher has carried it informally forever. Education software inverts it because software economics reward retention; the resulting products teach adequately and *linger* maximally (the streak that must not break is not a pedagogical instrument). This design writes the honest objective into the client's contract: an education client under the witness API adopts **graduation-rate** — learners who complete the curriculum's transmissions and *leave* — as its reported success metric, with churn-to-competence celebrated in its chronicle as achievement. The platform's own analytics for such clients report graduations where the industry reports retention. This is the self-eliminating objective this corpus has published at institutional scale, landed on the smallest and most consequential surface: the software a child learns to read on. (The revenue question — what pays for a product optimized for departure — is answered by the guild economics cited in §3: patronage thanks catalyzed real flourishing, and a family's gratitude to the game that graduated their child does not expire with the subscription that never existed.)

**The child-facing attestation rung.** *Certification by Circulation* (this corpus) published the guild's membership credential — the live, revocable credential by which software clients are admitted to the platform's economy, with machine-verifiable business-model attestation as its uncopyable headline rung. The present paper extends that ladder with one rung specific to clients addressing children, comprising, as conferral conditions: (1) **witness-scope-only** — the client's granted scopes are propose/celebrate/curriculum-read and nothing else, verified mechanically (the rung's analog of the ledger-fact rung: checkable, not promised); (2) **the never-gate-love invariant** (§4) attested and revocation-enforced on breach; (3) **no-analytics-exfiltration** — child learning data (proficiency, effort, errors, corpus content) never leaves the family's devices and is never monetized, brokered, or used for cross-client profiling; the client's off-device telemetry for child users is limited to the minimal completion signal; (4) **recipient-consent grammar** (§5's guards) implemented; (5) the jurisdictional floor (COPPA-class regimes and their equivalents) as a floor, not the bar. Copy discipline follows the parent publication: a credentialed client is "a member in good standing of a guild whose membership requires the above" — never "certified safe."

---

## 7 · What the Design Refuses

As prior art in refusal form — an implementation including any of the following is *not* this mechanism:

1. **Any disbursement, transfer, or balance scope** held by a game client; any conversion of in-game events to value.
2. **Rewarding lesson or quest completion** with money, currency, points-redeemable-for-value, or any minted instrument.
3. **Gating family communications** — locking, delaying, or conditioning any letter, message, or corpus item on progress, streaks, or payment.
4. **Blanket corpus access** or client-side corpus browsing; any off-device retention of consented items.
5. **Child-analytics exfiltration** — proficiency or behavioral data leaving the family's control, in identified or "anonymized" form.
6. **Streak-loss mechanics, appointment pressure, or synthetic urgency** addressed to child users.
7. **Retention-optimized objectives** in credentialed education clients — the rung requires the inversion.
8. **The transmission recipient as a prop** — capstones without recipient veto.

---

## 8 · Pre-Registered Predictions

All at n = 0; instruments await pilots.

- **P-E1 (transmission completes).** Units whose capstone is a transmission act are completed — through the real witnessed act — at rates comparable to or exceeding quiz-terminated units in matched content; the capstone is not a drop-off cliff. If families systematically skip the transmission, the design's central pedagogy is decorative and will be revised.
- **P-E2 (the corpus outpulls the streak).** In within-family comparisons, reading material drawn from the consented family corpus produces greater voluntary (unprompted) session initiation by the child than matched generic material — relational pull, measured against the industry's synthetic pull with the streak machinery absent in both arms.
- **P-E3 (the crowding wager — publish either way).** Witnessed thanks for graduation acts does not reduce the child's unprompted, unproposed kindness baseline: children in witness-API families show stable or rising rates of spontaneous (never-proposed) giving over six months. This is the overjustification exposure named honestly: the design bets that *witnessed acknowledgment of real giving* sits on the safe side of the contingent-reward boundary; the child-scale result will be published whichever way it falls, and a bad result revises the celebration grammar, not the accounting.

---

## 9 · Prior Art, Engaged Generously

**The overjustification and motivation literature.** Lepper–Greene–Nisbett (1973) on children's intrinsic interest under expected reward; Deci, Koestner & Ryan's meta-analytic synthesis; self-determination theory's autonomy/competence/relatedness triad — which this design can be read as implementing wholesale (autonomy: the act is the child's, off-screen; competence: the forge; relatedness: the entire reward channel *is* a relationship). Kohn's *Punished by Rewards* as the popular indictment. This literature is simultaneously the design's foundation and its named risk (P-E3).

**The pedagogy of meaningful material and of fading.** Ashton-Warner's *Teacher* (organic reading vocabulary from the child's own life); Freire's generative words; the family-literacy and authentic-literacy research traditions; Montessori's "help me to do it myself"; Vygotsky's ZPD and the scaffolding-and-fading stage of cognitive apprenticeship (Collins, Brown & Newman) — the formal ancestors of retention-inversion. The design's claim is not that these ideas are new but that no *software economics* has ever permitted their honest implementation; the witness API's revenue geometry is the missing permission.

**The industry anti-examples, engaged respectfully.** Duolingo — a genuinely effective product whose streak apparatus is the canonical instance of retention economics in education software; the chore-and-allowance app family (Greenlight, BusyKid, and kin) — competent products built frankly on pay-for-task exchange, the model whose child-scale hazards §1 rehearses; the AI-tutor wave (Khanmigo and successors) — pedagogically serious, and structurally silent, so far, on both the objective function (retention vs. graduation) and the family-data trust boundary this paper specifies. The GPT-era app stores' child-safety review regimes are the procedural prior art for §6's rung, differing in kind: store review attests process at submission; the rung attests scopes and conduct continuously, with a heartbeat.

**The consent and child-data law.** COPPA and its verifiable-parental-consent doctrine; the UK Age-Appropriate Design Code (data-minimization-by-default for children); GDPR-K. The rung treats these as floors; the never-gate-love invariant and the no-exfiltration rule exceed all of them, and are published here partly because no statute yet names them.

**This corpus.** *Need-Compiled Questlines* (the mints-nothing boundary; compile-never-invent; reward-follows-witness — the first-party grammar this paper exposes to third parties); *Certification by Circulation* (the membership credential and attestation ladder the child rung extends); the guild economics publications (the patronage revenue path); the play/currency wall (the sprint's shared spine, coined in the sport paper).

---

## 10 · Honest Limits

*This section is deliberately free of lineage, resonance, and metaphor.*

1. **n = 0.** No client, no rung, no curriculum, no family has used any of this. All architecture; all predictions unfunded by data.
2. **The crowding wager is genuinely open.** P-E3 may fall against the design. The witnessed-thanks channel is *argued* to sit outside the harmful contingency class; the literature's boundary cases are close enough that the argument requires the experiment. The commitment is to publish and revise.
3. **Supplement, never school.** Nothing here claims to teach reading, writing, or arithmetic better than schools and teachers; the mechanisms address motivation, material, and completion — the software layer's specific pathologies. Any implementation marketing itself as school replacement has left this design.
4. **On-device processing is platform-gated.** The consent architecture's strongest guarantee requires native on-device AI capacity; browser-only deployments can honor consent scoping but not the never-leaves-the-device property, and must say so plainly rather than imply it.
5. **The parent-steward gate assumes a functional steward.** Households where the approving parent is absent, coerced, or adversarial to the child are outside the design's protective assumptions; the gate protects against bad clients, not bad homes.
6. **Graduation-rate is gameable in principle.** A cynical client could graduate students *prematurely* to inflate the inverted metric. The transmission capstone is the partial guard (a real audience is the assessor); the residual risk is acknowledged and belongs to the rung's audit practice.
7. **The heritage-language case carries an emotional edge.** Tying literacy to a grandparent's letters is powerful precisely because it is not neutral; families navigating estrangement, loss, or painful histories need the corpus-consent granularity to exclude as easily as include. The per-item architecture is that granularity; the sensitivity is noted as a design obligation, not solved by it.
8. **COPPA-class compliance is asserted as design intent, unbuilt.** No legal review has occurred; the rung's jurisdictional floor is specified, not implemented.

---

## 11 · Claims

The following mechanisms and architectures, individually and in combination, are published as prior art and dedicated to the public domain:

1. **The witness API.** A third-party client boundary for family and children's platforms granting propose-and-celebrate scopes (real-world act proposal in client fiction; minimal witnessed-completion signal; celebration) while structurally withholding disbursement, transfer, balance, and value-attachment capabilities — such that all reward flows through human-initiated witnessed acknowledgment external to the client, and client-proposed act completion mints nothing.
2. **The parent-steward game gate.** Per-child, revocable, default-off parental approval as the exclusive authorization channel for client proposal rights, with the platform intermediary unable to override approvals in either direction, and intermediary authority confined to credential eligibility and mechanical scope enforcement.
3. **Family-corpus-as-curriculum.** The consent architecture under which a family's own communications and records become a child's instructional material: per-item parental release, revocability, on-device processing, client-cloud exclusion — including the **never-gate-love invariant**: the structural impossibility of locking, delaying, or conditioning any family communication on lesson progress, engagement, or payment.
4. **Graduation-by-transmission.** A curricular architecture in which each unit terminates in a proposed real-world transmission act (the learned skill performed for a real recipient), assessed by witnessed completion through the family's ordinary acknowledgment rail, with recipient veto, and with proficiency data held privately (the family record holding the gift, never the grade).
5. **Retention-inversion.** The adoption, by an education client and its platform analytics, of graduation-rate (curriculum-completing departure) as the reported success metric, with churn-to-competence classified as achievement — the engineered-obsolescence objective as a certifiable software property.
6. **The child-facing attestation rung.** An extension to a live membership-credential ladder comprising, as continuously-enforced conferral conditions for child-addressing clients: mechanically-verified witness-scope-only grants; the never-gate-love invariant; no-analytics-exfiltration of child learning data; recipient-consent implementation; and jurisdictional child-data floors — with breach revoking the credential's heartbeat.

---

## 12 · Lineage, and the Close

The tradition this institution draws from counts ten bases of merit, and two of them are learning and teaching — *dhammassavana*, listening to what is worth hearing, and *dhammadesanā*, giving it to the next person. The pairing is the point: reception is completed by transmission, and a teaching received but never passed on is a letter never answered. The founder's family lives this pairing daily — a father and son transcribing, page by page, a canon that survived because every generation treated *having learned it* as the obligation to hand it over. The mechanism above is that pairing, scaled to a seven-year-old: the letter arrives, the letter is read, and the reading is finished only when it is read *to* someone. Somewhere in the design's future intent, a child finishes a unit not when the app says so but when her little sister falls asleep mid-story — and the app's whole remaining job is to make sure her father saw.

And the app's final success, for that child, is the day she deletes it — reader, writer, teller of the family's accounts, done. The game that graduates you throws no graduation party for itself. It proposed; the family witnessed; the raft, as this corpus says elsewhere, is abandoned at the far shore — which was, from the first lesson, the only honest destination for a tutor.

---

## Citations

1. Lepper, M., Greene, D., & Nisbett, R. (1973). "Undermining Children's Intrinsic Interest with Extrinsic Reward." *JPSP* 28(1).
2. Deci, E., Koestner, R., & Ryan, R. (1999). "A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation." *Psychological Bulletin* 125(6).
3. Kohn, A. (1993). *Punished by Rewards*. Houghton Mifflin.
4. Ashton-Warner, S. (1963). *Teacher*. Simon & Schuster. (Organic vocabulary.)
5. Freire, P. (1970). *Pedagogy of the Oppressed*. (Generative words.)
6. Vygotsky, L. (1978). *Mind in Society*. Harvard UP. (ZPD; the scaffolding lineage.)
7. Collins, A., Brown, J. S., & Newman, S. (1989). "Cognitive Apprenticeship." In *Knowing, Learning, and Instruction*. Erlbaum. (Modeling–scaffolding–fading.)
8. Montessori, M. (1936/1966). *The Secret of Childhood*. ("Help me to do it myself.")
9. Purcell-Gates, V., et al. (2004). *Print Literacy Development: Uniting Cognitive and Social Practice Theories*. Harvard UP. (Authentic literacy.)
10. U.S. Children's Online Privacy Protection Act (COPPA) and FTC rule; UK ICO (2020), *Age-Appropriate Design Code*. (The jurisdictional floors.)
11. Reporting and documentation on Duolingo streak mechanics; Greenlight and BusyKid chore-reward products; Khan Academy's Khanmigo and the AI-tutor field (2023–2026). (The engaged anti-examples and the arriving wave.)
12. Ly, T. (2026). "Need-Compiled Questlines." thonly.org defensive publication. (Mints-nothing; compile-never-invent; claims division per the editor's note.)
13. Ly, T. (2026). "Certification by Circulation." thonly.org defensive publication. (The membership credential and ladder the child rung extends.)
14. Ly, T. (2026). "The Sport That Says Your Name." thonly.org defensive publication, same sprint. (The play/currency wall; the physical sibling.)
15. Ly, T. (2026). "The Wager That Isn't." thonly.org defensive publication, same sprint. (The stake grammar; the adult sibling.)

---

*— End of paper —*

*Marks referenced: HeartBank®, Miss Aquarius℠, B-Heart℠, B-Guild℠, Family Kitty℠, B-Sey™, B-Match℠, Tonsay™. Document SHA-256 computed at push and recorded in the institutional log. Document License: CC0 1.0 Universal. The authors and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its date.*
