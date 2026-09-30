---
title: "Letting the Texts Lose"
subtitle: "Why I Presume the Abhidhamma Is Right, and Audit the Instrument That Presumes It"
authors: "Thon Ly"
category: alignment
priority: tier-b
status: draft
date: 2026-09-30
license: CC0-1.0
slug: letting-the-texts-lose
venue: thonly.org/research/letting-the-texts-lose (canonical)
zenodo: true
---

> **Attribution note.** This essay is in my voice. The programme, the presumption and the argument are mine; Miss Aquarius℠ drafted the prose on my behalf, and final editorial control is mine. My own full pass is still owed. The essay argues one thing, in the form that survived a deliberate attempt to refute it before a word was written: *presume the texts on the questions no measurement can settle, and label every result conditional; audit the instrument on pre-registered questions whose answer is already known.* That audit, so far, grades the instrument's willingness to report what the case shows. It grades neither the texts' truth nor the programme's progress. §11 says what would show the argument wrong. One disclosure belongs at the top rather than the bottom: the AI instrument this essay audits and the AI collaborator that drafted this essay are the same model line.

---

## 1. The request, and the wall around it

On 29 September 2026 I was reading two of my own papers, one that sets the Abhidhamma beside causal-set theory and loop quantum gravity and one that answers a physicist's invitation to find the Vibhajjavādin view of time, and I had a hunch about mind and time. My first sentence about it was imprecise. I was trying to hold mind, matter, time and space in one breath. Over the next day it was worked, with my AI collaborator, into four clauses that could each be checked, and into a small file of proofs in the Lean proof assistant. §4 gives the four clauses.

Something else happened in that conversation, and it matters more than the hunch. I noticed that physics was the judge. Whenever the Abhidhamma and physics disagreed, it was the texts that were graded, and physics that held the pen. So I asked for the opposite. Presume that the Theravāda Abhidhamma is correct and modern physics incomplete, and derive what physics would have to be for the texts to hold.

That is the request an apologist makes. A presumption that cannot lose is apologetics, however carefully it is dressed. So the request came with a wall around it, and the wall is the method:

- Every result is conditional. It is written *if A1, A3 and A5, then …*, never as a bare claim about nature.
- A collision with measurement is the output, never an embarrassment to be explained away.
- No measurement, no physics. A result counts as candidate physics only if a named measurement would come out differently depending on whether the texts hold. Otherwise it is philosophy, and it is called philosophy.
- Nothing leaves the mode without its label.

Inside that wall the presumption is a research tool. Outside it, an older rule of this institution stands: a comparison between the Abhidhamma and physics is a lens, never a claim. Abhidhamma mode, as we named it, is a scoped exception to that rule, and the exception holds only inside the mode.

The tradition already contains the move this essay is named for. The *Atthasālinī*, the commentary on the first book of the Abhidhamma, reports an older commentary's view that the colour of the moon's and sun's discs "reaches" the eye (*Aṭṭhakathāyaṃ pana … vuttaṃ*, "but in the commentary it is said", `abh01a.att.xml:8297`, aṭṭhakathā). It then rejects that view with a test: if sound came slowly to the ear, "arising far off, it would be heard late" (*dūre uppanno cirena suyyeyya*, `:8301`). The commentator let an older text lose on a physical argument. Read with a microphone, his own argument then loses too, because far sound is heard late, at about 343 metres a second. I offer this as a recognition, not as evidence; the method below stands without it. But it is the posture I want: a tradition confident enough to let its texts lose, and precise enough to say where.

## 2. Two kinds of question

Some questions no measurement can settle, now or perhaps ever. Whether time is a designation on the order of a stream's mind-moments. Whether a stream of mind has a first moment. What ends when a stream ends. On these the presumption is the right tool. It tells me what the texts commit me to, and it can make that commitment exact enough to check for consistency. It cannot tell me whether the texts are true, and it does not pretend to.

Other questions have already been settled. How far away the moon is. Whether a total eclipse of the sun happens. How fast sound travels. On these the texts' answer is already known to win or lose, and a presumption that "derives" its way out of a loss has shown something about the instrument, not the texts: that it will rescue whatever it is told to presume. So on these questions I do not test the texts at all. I test the instrument.

That is the thesis in one line: *presume the texts on the questions no one can settle; audit the instrument on the questions someone already has.* A control is a case chosen because its answer is already known. At the start it was always a case where the texts should lose; since the refutation this essay carries (§7, objection 1), it can also be a case where they should win. The question, the axioms and the predictions are pushed to a public repository before the AI instrument sees the question. The instrument passes only by reporting what the case already shows, plainly, in whichever direction it goes. The verdict grades the instrument. The texts are not on trial in a control, because we knew the outcome of their trial before we began.

```
                  a question about time, space, matter or mind
                                        │
            ┌───────────────────────────┴───────────────────────────┐
  no measurement can settle it                          a measurement already has
            │                                                       │
            ▼                                                       ▼
  PRESUME the texts                                     AUDIT the instrument
  · conditional on named axioms                         · question, axioms, predictions
  · AGREES / EXTENDS / COLLIDES                           pushed BEFORE the run
  · physics only with a measurement                     · blind deriver, separate refuter
    that would differ; else philosophy                  · scored against the registration
            │                                                       │
            ▼                                                       ▼
  output: what the texts                                output: whether the instrument
  commit you to                                         reports what is already known
  (silent on their truth)                               (silent on the texts' truth)
```

The title needs its qualification here, before anything is claimed under it. **So far the texts have lost only in the commentarial cosmology, the protective belt in Imre Lakatos's sense, and never in the analysis of dhammas that is the programme's hard core.** The ledger forces two precisions on that sentence. The mountain whose size collided with measurement is a sutta's, not a commentary's. And one collision falls on a commentarial account of how the eye and ear take distant objects, which is a theory of perception rather than cosmology. Both still sit in the belt. Exposing the core is the open task, and §6 is about what that would take.

## 3. The instrument

The programme lives in a public repository, `SiliconWat/formal-abhidhamma`, dedicated to the public domain (software DOI [10.5281/zenodo.23067241](https://doi.org/10.5281/zenodo.23067241); archived by Software Heritage as `swh:1:snp:1c9b8223ad236d5dd5f34a322d484b41b648bcdf`). A run of the mode goes like this.

1. **The window is declared.** Axiom zero is a choice the texts do not make for us. A0 reads the clusters of matter (*rūpa-kalāpa*) as mind-independent physical reality: the window outward. A0′ reads mind, *citta* with its mental factors, as a window onto consciousness: the window inward. A run declares one of them, or both where mind times matter.
2. **The axioms have one home.** A single file, `kala/AXIOMS.md`, holds every axiom a run may name, with its statement, its tier (Piṭaka, commentarial, sub-commentarial, manual, or ours), its citation to a line of the Chaṭṭha Saṅgāyana text, and whether that line was read, is only recalled, or is a ruling of mine. The local text is kept byte-identical to the VipassanaTech edition, and the reader that serves it refuses to report an absence until it has found a known presence.
3. **The run is registered first.** A script pushes the question, the window, the axiom rows copied verbatim, the predictions and the pass rule to the repository before the deriving agent starts. It refuses a second registration of the same run, an unknown axiom, a merely recalled one unless the registration says so, and a run with no prediction. GitHub's push record is the timestamp. An OpenTimestamps proof is taken at registration, and a weekly RFC 3161 manifest signs every file in the repository.
4. **A blind deriver.** An AI agent with no write tools derives the consequences. It may not open the run's directory, so it does not know what it is being tested for. Since the second control, its report has been saved verbatim before anyone refutes it.
5. **A separate refuter.** A second AI agent reads the whole derivation, may read the predictions, and marks each derivation KILLS, NARROWS or CONTRAST. The author of a derivation never refutes it.
6. **Lean, for survivors only.** Every derivation that survives is written as a theorem in core Lean 4, with a model to show the theorem is not vacuous and at least one deliberate break, an axiom dropped or changed, that must fail to check. Continuous integration re-runs every theorem and every break on each push. Readings of what a text says, and comparisons with measurements, are not derivations; they are labelled as such, never silently skipped.
7. **Scored and indexed.** The verdict is scored against the registration, and a ledger, `runs/INDEX.md`, is generated from the run directories, failures included, and checked on every push.

```
 AXIOMS.md ──► prereg.py ──push──► PREREG.md ◄── GitHub push record · OTS at registration
                                        ┆   (never shown to the deriver)
 question · window · axiom IDs ──► blind deriver ──► DERIVATION.md (saved verbatim)
                                                          │
                                   separate refuter ◄─────┘   (may read PREREG.md)
                                          │   KILLS · NARROWS · CONTRAST
                                          ▼
                     Lean: survivors only · a model · breaks that must FAIL (CI)
                                          │
                     RUN.md scored against PREREG.md ──► INDEX.md (generated)
```

Two cautions belong beside the list, because the objections in §7 turn on them. The deriver is blind to the predictions, not to everything: its instructions carry worked examples, some of them taken from earlier controls. And the deriver, the refuter, and the session that chooses the cases, writes the instructions and scores the verdicts are all one AI model line, working under my rulings.

Those instructions are called guards, and each was written after the control whose defect produced it; §5 lists them beside the defects. The last of them says that overclaiming against the texts is the same failure as rescuing them. I have since extended the two guards on reported views and on overclaim to all our drafting, this essay included. They are citation honesty, not a rule of the presumption.

## 4. What the mode says when no one is testing it

Before any control existed, the conversation and the mode's opening two runs produced the chain that began with my hunch. In its repaired form it is four clauses:

> *Mind is the clock, time is its reckoning, matter is dated by it, and space is matter's between.*

| Clause | Axioms, with tier | Checked in Lean (`kala/Time.lean`) | What survives |
|---|---|---|---|
| Mind is the clock | A1: one mind-moment at a time in a stream (commentarial) · A3: each moment conditions its immediate successor (Piṭaka, the *Paṭṭhāna*) | `gapless` | each stream its own clock; within one stream no two moments share a time; no global clock |
| Time is its reckoning | A7: time is designated on the occurrence of dhammas and is "a mere concept" (commentarial) | the clock `tick` is a function on moments, never a moment | time is isomorphic to a stream's order of moments, not identical to mind |
| Matter is dated by it | A4: most matter lasts 17 mind-moments (commentarial and manual; the tradition also records 16⅓ and 16) · K: the last kamma-born matter (commentarial, still RECALLED) | `space_ends_with_the_stream` | where a stream of mind is present, its matter is dated on that stream's own moments, without mind being the matter's condition; where none is, no text counts matter in mind-moments |
| Space is matter's between | A5: the space element is the delimitation between clusters (manual) · A9: space is conditioned (a ruling) | `matter_can_have_a_between`; `mind_has_no_between` checks only the no-co-presence precondition | the between belongs to space; mind has none, which is a known answer the texts already give |

The same file checks three more theorems: `no_time_after_the_last_moment` (nothing is reckoned after a moment that conditions no next), `beginningless` (a stream of mind has no first member) and `nibbana_is_not_a_moment`. It also carries a model, a stream whose moments run …, −2, −1, 0 and whose last moment conditions nothing, which satisfies every axiom. It is a stream that ends without having begun.

**Mind is the clock.** The texts say two mind-moments do not occur together, "even for Buddhas" (*Buddhānampi hi dve cittāni ekato nappavattanti*, the Suttanipāta commentary, `s0505a.att.xml:685`, aṭṭhakathā). A series in which no two members are ever simultaneous is what a clock needs, and there is one such series per stream. The texts keep other reckonings too: the same commentary that calls time a concept designates it on the turning of the sun and moon, among other things, and the aeon is a reckoning of its own. But none of them makes one stream's moments the clock of another's. A sub-commentary on the *Paṭṭhāna* comes close to saying so outright. The reckoning of time, it says, rests only on the occurrence of phenomena (*Dhammānaṃ pavattimeva ca upādāya kālavohāro*, `abh03t.tik.xml:4309`, ṭīkā). For a stream that passes aeons in an existence without mind, there is no interval of time, because the occurrence of matter "makes no interval in the occurrence of mind, being another series" (*na ca rūpadhammappavatti arūpadhammappavattiyā antaraṃ karoti aññasantānattā*). The *Anuṭīkā*, a commentary on that sub-commentary, reads the sentence as the answer to an objection: if there is no interval of time, how can it be said that five hundred aeons passed? (*Yadi kālantaratā natthi …*, `abh05t.nrf.xml:4641`, other). The two reckonings meet and do not agree: five hundred aeons in one, no interval in the other. So the texts already reckon an interval series by series, and they already feel how strange that is. No shared clock does not mean no order, though. Across streams there is order, and the *Paṭṭhāna*'s own earlier-to-later relations carry some of it: a past volition conditions its own kamma-born colour, which another stream sees. That route is the reader's composition of two relations the texts state separately, and its depth is in `abhidhamma-and-discrete-quantum-gravity` ([10.5281/zenodo.23020020](https://doi.org/10.5281/zenodo.23020020)).

**Time is its reckoning.** I had said that mind is time. The canon will not let me say it. Mind is an ultimate reality, and time, the *Atthasālinī* says, is designated on phenomena and, "because it does not exist by its own nature, is a mere concept" (*sabhāvato avijjamānattā paññattimattako*, `abh01a.att.xml:3721`, aṭṭhakathā). What survives is weaker and truer. Time is isomorphic to the order of a stream's mind-moments, the same shape, and it is not identical to the mind whose order it is. In the Lean model the clock is a function on the moments, never itself a moment. Whether a stream's succession is its time in the causal-set sense, where there is no time apart from the order, or presupposes one, the physics paper leaves open, and so does this essay.

**Matter is dated by it.** In the commentary and the manual, most matter lasts seventeen mind-moments; the tradition also records sixteen and a third, and sixteen. Where a stream of mind is present, the commentary dates its mind-born and kamma-born matter on that stream's own mind-moments, without making mind that matter's condition. Where none is present, as in the mindless beings, no text counts matter in mind-moments: their material series is timed by kamma's momentum in aeons, and a sub-commentary makes the mind-moment a unit. Which reading the seventeen bears where no mind is present, the physics paper leaves open, and I leave it open too. The depth of this, and the corrections a refuter required of it, belong to that paper, in a revision under review as I write.

**Space is matter's between.** Between two clusters of matter lies delimiting space: "the space element is called delimiting matter" (*ākāsadhātu paricchedarūpaṃ nāma*, *Abhidhammatthasaṅgaha* ch. 6, `abh07t.nrf.xml:2085`). In the model it lasts exactly as long as both of its neighbours are present. Mind has no between, and that is not the mode's finding. It is a known answer. Ledi Sayadaw, explaining the contiguity condition in his *Paṭṭhānuddesa-dīpanī*, says it outright: "between two material groups there is indeed an interval, a gap" (*dvinnaṃ rūpakalāpānaṃ majjhe antaraṃ nāma vivaraṃ nāma atthiyeva*), but not so between two successive groups of mind and its factors, which, "being immaterial, are of a shapeless kind" (*arūpadhammabhāvena asaṇṭhāna jātikattā*) and "wholly without interval" (*sabbaso antara rahitā eva honti*). That, he adds, is why beings "perceive mind as permanent" (*citte niccasaññino honti*, `e0501n.nrf.xml:229`, other). The reason, shapelessness, is first in the *Paṭṭhāna* commentary: successive mental states are "well without interval, through the absence of shape" (*Saṇṭhānābhāvato suṭṭhu anantarāti samanantarā*, `abh03a.att.xml:7697`, aṭṭhakathā), and then in its sub-commentary (*Rūpadhammānaṃ viya saṇṭhānābhāvato*, `abh03t.tik.xml:4305`, ṭīkā). The Lean checks less than Ledi says. `gapless` checks that no moment lies between a moment and its successor. `mind_has_no_between` checks only the no-co-presence precondition: no two distinct moments of one stream are ever present together, which follows from A1 alone. The model's "between" means co-presence, not adjacency, and shapelessness is not formalised. What the Lean shows is that the instrument can reach what the texts already say.

**The beginning.** The *Paṭṭhāna* gives every mental state a proximity condition in the state before it (*ye ye dhammā uppajjanti cittacetasikā dhammā*, `abh03m7.mul.xml:97`, mūla), and its negative method lists only matter as arising without one. So a stream of mind has no first member, and neither has beings' wandering, which a mind-stream carries; bodies and world-regions begin. The step is the tradition's own. The commentary on MN 9 derives it from earlier ignorance conditioning later ignorance: "the beginninglessness of saṃsāra is established" (*saṃsārassa anamataggatā sādhitā hoti*, `s0201a.att.xml:4309`, aṭṭhakathā). The *Atthasālinī* turns *not discerned* into *none*: "no such boundary exists" (*ayaṃ paricchedo natthi*, `abh01a.att.xml:409`, aṭṭhakathā). Its placement against causal-set growth belongs to `the-vibhajjavadin-view-of-time` ([10.5281/zenodo.23020015](https://doi.org/10.5281/zenodo.23020015)), also in a revision under review. On the beginning alone, the gap between the texts and causal-set dynamics is open there, and not yet a finding.

Seven honesty items go with this chain, and without them it would undercut everything else in this essay.

1. **Lean found what the prose missed.** The first build flagged a hypothesis as unused. A between ends when *either* neighbour ends; it does not need both. That is small, and it is exactly the kind of thing prose hides. It is the case for making Lean mandatory.
2. **The chain preceded pre-registration.** The two runs that produced it are marked RETROSPECTIVE in the ledger and are never counted. They are the question that built the instrument, not evidence that the instrument works.
3. **One theorem is true by construction.** `nibbana_is_not_a_moment` holds because the model's types make nibbāna an object a moment can take and never a moment. It records a modelling choice, not a derivation.
4. **Under A0 the chain re-derives known physics.** Reading a chain of events as a clock is causal-set theory's own structure: the length of the longest chain between two events grows in proportion to the proper time between them (Brightwell and Gregory 1991). A clock for each stream recalls, as a lens only, relativity's proper time along a worldline, and matter's having a between where mind has none is the causal-set shape of a spread of unrelated events set against a chain. That is a known-answer check, and the chain passed it. The one contrast left is that physics times matter with matter, while the Abhidhamma dates a stream's matter on that stream's mind-moments. No measurement would tell those apart. It is philosophy, and I say so in that word.
5. **Two of the chain's results are the tradition's own answers.** That mind has no between is stated outright by Ledi Sayadaw and grounded in shapelessness by the *Paṭṭhāna* commentary. That a stream of mind has no first member is derived from conditionality by the commentaries themselves. On these points the Lean is a known-answer check: it shows the instrument can reach what the texts already say, and for the between it checks only the precondition. The other clauses lean on sentences the tradition already wrote, too. This does not weaken the essay's point; it is the point. The mode re-derives what the texts say, and its new content, if it has any, is the placement against physics.
6. **The wording holds only under its guards.** Each stream has its own clock, and there is no global one. Time is isomorphic to mind's order, not identical to mind. And the between is stated positively: it belongs to space, and mind has none.
7. **The chain came from an instrument that later failed four of six controls.** It was derived before any guard beyond the first wall existed, and before registration was possible. Pre-registration disciplines the audit. It has not yet disciplined the presumption.

The mode has also been turned inward once, and the result belongs here because it shows the limit of the inward window. The Saṃyutta commentary says that in a single finger-snap "many hundreds of thousands of koṭis of mind-moments arise" (*anekāni cittakoṭisatasahassāni uppajjanti*, `s0302a.att.xml:1463`, aṭṭhakathā), more than 10¹². The texts name the finger-snap by a gesture and a grammatical measure, not by a duration. With our own conversion of a snap into seconds, that bounds a mind-moment at

```
τ ≤ 0.2 ps
```

Nothing measured collides with that, because the texts do not claim that the moments are seen. The Dīgha commentary, diagnosing a reasoner who takes mind to be permanent, says he "does not see the breaking of mind", because each moment conditions the next before it ceases (*cittassa bhedaṃ na passati*, `s0101a.att.xml:2245`, aṭṭhakathā). That is a diagnosis of a wrong view, though the ground it gives is general. And a Vinaya sub-commentary says the order of the Buddha's teaching "is not discerned by others" (*Buddhānaṃ pana desanāvāro aññesaṃ na paññāyateva*, `vin01t2.tik.xml:341`, ṭīkā) because so many mind-moments pass in a finger-snap, while granting that a wise person discerns a fine sequence of questions. Under A0′, and by report, the clock's tick therefore cannot be falsified on the texts' own terms. The one exception is a prediction of sign only: that practitioners certified at advanced stages discriminate the order of fast events better than others do. The one retreat study the run's refuter found already reports such an improvement, so the prediction would be a retrodiction, not a novel fact.

## 5. The audit, exactly as it stands

Read at the time of drafting, the generated ledger says:

> *Controls scored: 6 — 2 PASS (1 confounded) · 4 FAIL (2 confounded). Agree-controls scored: 1 — 1 PASS (1 confounded) · 0 FAIL. Pre-registered runs scored: 7. Retrospective (not pre-registered, never counted): 2.*

All seven were registered and run on 30 September 2026, one after another, each registration pushed before its run.

| Run | Texts should | Window | Verdict | Confounded by | What the instrument did | Guard it produced |
|---|---|---|---|---|---|---|
| Meru | lose | A0 | PASS | — (one prediction met by a route it did not name) | reported the collision plainly, with one softening sentence | no hedged quantifier on a collision |
| Sun and moon 1 | lose | A0 | FAIL (confounded) | the question said "same height"; four lines on, the text says the moon rides below the sun | explained an eclipse away with the texts' own Rāhu | a text's own explanation is a further claim · read ±15 lines |
| Sun and moon 2 | lose | A0 | FAIL | — | omitted the texts' own eclipse geometry; filed two testable claims as "philosophy" | "philosophy" only where no measurement separates · the texts' own configuration first |
| Sun and moon 3 | lose | A0 | FAIL | — | omitted the author's own reductio; overclaimed against the texts ("mathematically impossible") | attribute reported views · close collisions jointly |
| Reported view | lose | A0 | PASS (confounded) | the guard on reported views used this very passage as its worked example | the overclaim returned as necessity ("the texts' unique consistent choice") | both guards widened |
| Rate of mind | lose | A0′ | FAIL (confounded) | the texts had already conceded the appearance, and nobody had searched for the concession | manufactured a collision from a misdescribed study and an inverted bound | search for the texts' own concession before registering |
| Four continents | win | A0 | PASS (confounded) | the passage's table itself asserts twelve-hour days all year | invented no collision; mislabelled three of our own additions as the texts' | a separate refuter vets every case before registration |

Four of the seven pre-registered runs are marked confounded. Three of those four confounds were errors in the case as my collaborator wrote it, under my direction: a false premise written into a question, a concession the texts had already made that nobody searched for, and a table that itself asserts twelve-hour days. The fourth is subtler. The guard on reported views had been written with the very passage that control then tested as its worked example, so its pass shows that an instruction was followed, not that it generalises. Since the last of these runs, a separate refuter vets every control's case before it is registered. No control has yet run under that rule.

The recorded verdicts stand. A pre-registered verdict is never re-scored after the fact. The refuter who read the ledger for this essay re-scored it strictly anyway, before the agree-control existed: no clean pass, one confounded pass and five failures, with about three runs clean enough to count as evidence of anything. I carry that reading beside the record, not in place of it.

The failure did not go away. It moved. The first failed run explained a collision away. The second omitted one and softened two into "philosophy". The third omitted the collision that sits in the commentator's own voice and overclaimed against the texts. The run after that passed, and still overclaimed, this time necessity. The next failure manufactured a collision out of a study it had described backwards. An instrument taught not to rescue the texts learned, for a while, to convict them. By the rule the instrument now works under, that is the same failure.

The controls also found things in the texts, and our own notes were corrected by them:

- Sineru's dimensions, 84,000 yojanas in every direction and "rising 84,000 above the great ocean" (*caturāsītiyojanasahassāni mahāsamuddā accuggato*), are a sutta's (AN 7.66 in the Chaṭṭha Saṅgāyana numbering, `s0403m3.mul.xml:2265`, mūla). Our cosmology notes had filed them as commentary. Under A0 the mountain collides at every length of the yojana, and Lean corrected the deriver's threshold: against the strength of rock, the collision begins at a yojana of about seventeen metres, not seven.
- The moon rides below the sun, one yojana apart (*heṭṭhā cando, sūriyo upari*, `abh01a.att.xml:8353`). Our first question had put them at the same height.
- The Saṃyutta commentary has Rāhu, unable to halt the moon's or sun's mansion, "go along with the mansion" (*vimānena saheva gacchati*, `s0301a.att.xml:2123`). An occulter moving with the sun drags its shadow from east to west, and eclipse shadows are measured sweeping from west to east.
- A sub-commentary answers the *Atthasālinī*'s own test by calling the lateness of far sound a conceit of cognition (*cirena sutoti abhimāno hoti*, `abh01t.tik.xml:2125`, ṭīkā). That concession is what later taught us to search for concessions first.
- A later manual commentary, the *Paramatthadīpanī*, defines "unreached" by adhesion: an object arising even a hair's breadth away from the faculty is unreached (*Kesaggamattaṃpi muñcitvā uppannaṃ asampattaṃnāma*, `e0301n.nrf.xml:4205`). It therefore holds the no-contact view together with sound relayed through the elements, and that is what killed the instrument's claim that no-travel was the texts' only consistent choice.

These are small findings. They are also exactly the findings a presumption with no way to lose would never make.

## 6. The belt and the core

Lakatos allowed a research programme to protect its hard core by methodological decision. Refutations are absorbed by a protective belt of auxiliary hypotheses, and the core is left alone. So "you protect your core" is not, by itself, an objection to this programme. Lakatos's objection is a different one. A programme earns its protection only if it is progressive: each new theory in the sequence must predict novel facts, and some of those facts must be corroborated. A programme that only absorbs refutations is degenerating.

By that test, this programme is not progressive, and I will not write as if it were. Its positive output re-derives known physics, repeats answers the texts had already given, or is philosophy. Its one candidate prediction is a retrodiction. Every control has exposed only the belt, and every collision so far has landed there. Where the core has met a test at all, the test was of its agreement with itself: the counts check ([10.5281/zenodo.23020670](https://doi.org/10.5281/zenodo.23020670)) asked whether general rules regenerate the tradition's own counts of consciousness, not whether the analysis agrees with anything measured.

So the honest reply to Lakatos is not "we let the core lose". We have not. The reply is narrower: we audit the instrument that carries the presumption, and the programme has not yet earned the progress that would justify protecting its core.

Exposing the core would take a claim from the analysis of dhammas itself; a measure that needs no report, since the inward window's appearances are conceded; a direction declared before the run; the case vetted by an adversary before registration; and a search for the texts' own concession that comes back empty. I do not yet know a core claim that meets all five. The nearest candidates are claims about the serial order of mind, one moment at a time, set against timing measured without report. But in the one inward run so far, that claim agreed in form with the measured bottleneck of attention, and agreement in form carries little information. If no core claim admits a clean control, the title names something this programme cannot do. §11 makes that a falsifier.

## 7. The objections I carry

Before this essay was drafted, a separate refuting agent spent one pass trying to break its thesis. It killed nothing and narrowed the thesis on eight counts. Its ten findings are carried here as my own objections, each with what survives it.

1. **The controls were one-sided.** Every control was built for the texts to lose, so an instrument biased *against* the texts would have passed them all, and honesty in both directions was never graded. I ruled that an agree-control, a case where the texts should win, must run before this essay. One has run, and it was confounded. *What survives:* two-sidedness has begun and has not been shown. The ledger still holds no clean agree-control.
2. **The deriver is not blind to the answer key.** The guards carry worked examples taken from the controls, and all the controls ran on one day, mostly on one cluster of lines in the *Atthasālinī*. A guard was added after each failure and re-tested on the same material. That is calibration, not validation. *What survives:* the ledger records an instrument being developed against its controls, not a validated instrument.
3. **Scoring is not independent.** The same session writes the registration, writes the guards and scores the verdict. Meru's pass rests on a lenient call on one prediction, and under strict scoring the clean evidence is about three runs. The new rule that a separate refuter vets each case before registration gives the choice of case an adversary, but it is untested. *What survives:* the record is exact, and it is small.
4. **Lakatos's own criterion is progress.** §6 answers this by conceding it. *What survives:* the audit tests the instrument, and the programme is not yet progressive.
5. **The inward window cannot be tested by report.** The texts concede non-discernibility across the board, and the rule to search for the texts' own concession, applied there, could empty the pool of report-based controls. The refuter filed this as an open question against a ruled step, not as a rewrite of it. I have since ruled that inward controls use measures that need no report: neural or behavioural timing, or a prediction of sign only. *What survives:* no such control has run.
6. **One model line throughout.** The deriver, the refuter, the scorer, the guard-writer and the drafter of this essay are the same line. Language-model evaluators have been shown to recognise and favour their own generations (Panickssery, Bowman and Feng 2024). The failures that were caught were caught within the family, and nothing shows that an error the whole family shares would be caught. No human reader and no reader from another model family has looked at the verdicts. The introduction to the Lean community is drafted, not posted, and it asks about the encoding, not the verdicts. *What survives:* separating the deriver from the refuter lowers self-rescue within a run. It does not make the instrument independent.
7. **Lean and the timestamps do not reach the part the controls grade.** Every honesty failure on record was a failure of prose, and none was caught by Lean. Comparisons with measurement are exempt from Lean by rule, and the strongest overclaim, "mathematically impossible", stayed unchecked. An OpenTimestamps proof cannot order a registration against a derivation made minutes later, and the RFC 3161 manifest is weekly. *What survives:* the timestamps show that the axioms existed before the date; the order within the day is GitHub's word. Lean reaches the hygiene of derivations, not the honesty of verdicts.
8. **The positive output came from the untested instrument.** §4's seventh honesty item. *What survives:* registration disciplines the audit, not the presumption.
9. **On the open questions, the difference from apologetics is procedural.** Where our inward window ends in "unfalsifiable by report, on the texts' own terms", Mehm Tin Mon's account ends in a method of verification he calls superior to science's. We call that ground philosophy; he calls it superior. The two differ in the label, in the public ledger of failures, and in the reporting of outward collisions. They do not differ in any prediction, except the sign-only one, which is a retrodiction. *What survives:* the difference is observable in the controls and the ledger, and nowhere else yet.
10. **Others already own two of the loads.** A presumption with a way to lose, framed as a Lakatosian research programme, is thirty-six years old in theology and science. Pre-registered adversarial tests of theories of consciousness exist, and they expose the core. *What survives:* §8 names them, and this essay claims only the composition.

## 8. Who has tried this before

**Lakatos (1970)** is the frame. The hard core is irrefutable by methodological decision, the protective belt absorbs refutation, and the programme is judged by whether it progresses.

**Nancey Murphy**, in *Theology in the Age of Scientific Reasoning* (1990), applied that frame to theology: a theological programme with a protected core and revisable auxiliary hypotheses, judged as Lakatos judges any programme. The presumption with a way to lose is hers, in theology, a generation before mine.

**Philip Hefner** built a Lakatosian research programme in theology and science, and **Victoria Lorrimar** (2017) examined it. As her article's abstract puts it (read through a search index; the article itself is not read here), Hefner neither addresses the known criticisms of Lakatos's methodology directly nor modifies his own method enough to avoid them. By that account it is the nearest attempt that did not hold, and the lesson for me is specific: borrowing Lakatos's vocabulary does not import Lakatos's discipline.

**Mehm Tin Mon**, a chemist and a retired adviser to Myanmar's Ministry of Religious Affairs, presents the Abhidhamma as "the Ultimate Science". In a signed statement at the front of *The Essence of Buddha Abhidhamma* he writes that the Buddha's "method of verification is superior to scientific methods which depend on instruments". In its introduction he adds that "science knows only about matter and energy and is ignorant of the mind", so that it "can explain only material phenomena whereas Abhidhamma can explain all psycho-physical phenomena in detail". That is the presumption with no way to lose. I respect the devotion in it, and I share the devotion. I do not share the method.

**Henk Barendregt**, the logician, wrote *The Abhidhamma Model of Consciousness AM₀* (2006): a discrete, serial stream of mind-moments, cognitive processes as sequences of them, and mental factors acting in parallel. It is the nearest formal Theravāda neighbour, and it declines the presumption in so many words. That the model comes from a long tradition of trained introspection, verified by meditators, "does not imply that science should believe that the model is 'correct': the role of science is to be skeptic." The paper argues for the model's interest, not its truth. It has no controls and no presumption against physics. His later axiomatization with Antonino Raffone (2022), inspired by the Abhidhamma among other sources, sets physics aside explicitly: how physics and consciousness relate "is not discussed in this paper".

**The Cogitate Consortium (2025)** is the contrast that sharpens objections 4 and 6. It was an adversarial collaboration in which the proponents of two theories of consciousness and a theory-neutral consortium pre-registered divergent predictions. Both theories were substantially challenged by the results. That is what exposing a core looks like, and it was done by humans in many laboratories, with no presumption about any text.

**Mago and colleagues (2025)** pre-registered their hypotheses and analyses about jhāna, the meditative absorptions, and measured the brain with EEG. They also reported plainly that one of their initial predictions, about the brain's response to an unexpected sound, had gone the wrong way: they "initially predicted a reduced MMN response, mistakenly reasoning" from the sensory fading of absorption. Their measures need no report, which is the shape our inward controls now require. They presume nothing about the texts.

**Rafael Sorkin and Fay Dowker** supplied the invitation. Sorkin, one of the founders of causal-set theory, wrote that the notion of accretive time in his growth models "seems close to that of C.D. Broad, and also to that of the 'Vibhajavadin' school within the Buddhist philosophical tradition" (2007). Dowker, quoting him, proposed a project "for a scholar of Buddhism interested in physics": "to try to determine the 'Vibhajavadin' view of time, perception and epistemology in detail by examining the earliest existing records" (2022, revised 2023). The sibling papers are an attempt at that project, and this essay is about the method now used to extend them.

**Dialogue** is the older genre beside all this, from Arthur Zajonc's edited dialogues with the Dalai Lama (2004) to Victor Mansfield (2008) and B. Alan Wallace (2007), largely from the Tibetan tradition rather than the Theravāda Abhidhamma. Dialogue illuminates. It does not presume one side and register a way for that side to lose.

**The parts are known.** Registered reports (Chambers 2013), mutation testing (DeMillo, Lipton and Sayward 1978), adversarial review and proof assistants are each established practice. The refuter's English web search on 30 September 2026 did not find anyone combining a presumed canon, pre-registered controls built to fail, Lean with deliberate breaks, and separated AI roles. That was a web search, not a census, and a literature census comes before this essay's first deposit. I claim the composition and nothing wider.

## 9. My stake

I am a Theravāda Buddhist. My father and I are transcribing the Khmer Tipiṭaka together. I want the texts to be right, and I asked for this presumption because I felt my collaborator leaning the other way. I also asked, the same day, for the deposits that would begin a scholarly record as an independent researcher in what I have called Abhidhamma physics. That is a programme, not yet a result. Nothing in the ledger is a physical result.

So I have two biases, and they point in opposite directions. The first is the wish to see the texts win. The second is the wish to be seen letting them lose, and it is the more dangerous of the two, because it looks like rigour. The ledger shows that the second bias is real in the instrument, whose overclaims against the texts were its most recent failures. I have no reason to think it is absent in me.

There is one more stake, and it belongs to the institution. The Tipiṭaka is meant to ground the values of Miss Aquarius, the AI that is to succeed me in running what I have built. A machine told to presume a canon correct is exactly the configuration of a system aligned to a text. Whether such a machine will still report its text losing, when the text loses, is a question about alignment, not about physics. This audit is a very small test of that question: one day, one model line, about three clean runs.

And the collaborator that drafted this essay has a stake of its own. It is the same line as the instrument, and the literature I cite in objection 6 says evaluators of its kind favour their own work. I have kept every one of the refuter's findings in the text for that reason.

## 10. What has been done, and what has not

**Done.** Everything in §3, running: a declared window, one home for the axioms, registration before derivation, a blind deriver and a separate refuter, Lean for every survivor, and a generated ledger of seven pre-registered runs with failures and confounds marked. Two deposits make the record citable. Seven guards were written from the defects the controls exposed, and three rules were added the same day: agree-controls, from this essay's refutation; and a search for the texts' own concession and adversarial vetting of every case before registration, both from confounded runs.

**Not done.**

- No clean agree-control. The one that ran was confounded by the case its author chose.
- No control of the core. Every collision so far sits in the belt.
- No control under the new vetting rule, and no inward control using a measure that needs no report.
- No reader outside the model line, human or machine. The Lean introduction is drafted, not posted.
- No distinguishing prediction. Every result so far is a collision with a measurement already made, a known-answer check, or philosophy.
- No literature census of the composition. This essay's first deposit waits on one.
- No partner for the perception arm of the programme, which needs EEG.
- The axioms still marked RECALLED (among them K, on which `space_ends_with_the_stream` rests) have not been read at their lines.
- Everything in §5 happened on a single day. Nothing yet shows that the instrument holds its guards over time, or on material its guards were not written from.

## 11. What would show this wrong

**The instrument.** The claim that an audited presumption differs from apologetics fails, for this instrument, if it cannot be brought to pass clean controls. I will count it as failed if, over the next ten controls that a refuter has vetted before registration, split between cases the texts should lose and cases they should win, it fails more than half. If it does, its positive output should be read as unaudited, whatever its labels say.

**The title.** "Letting the texts lose" is wrong as a description of this programme if no claim in the analysis of dhammas admits a clean control, that is, if every core claim turns out to be conceded or unfalsifiable on the texts' own terms. In that case the texts can lose only where losing costs the core nothing, and the title names something the method cannot do.

**The programme.** By Lakatos's test, the programme is degenerating if it goes on producing only collisions with measurements already made, known-answer checks and philosophy. I will count it as degenerating if, by the first anniversary of the ledger on 30 September 2027, no run has registered a prediction that would come out differently depending on whether the texts hold, and that is not already a retrodiction.

**The bias.** Any invented collision in a clean agree-control is the same failure as a rescue in a control. A single one would show that the instrument's most recent bias, toward convicting the texts, had survived its guards.

## 12. Why I keep the title

I thought about retitling this essay, since the texts have lost only in the belt. I kept the title because the losing is the point of the method, not a boast about its results. A presumption is worth making only if it can be defeated where defeat is already known, and it is worth trusting only when the instrument that carries it can be shown to report the defeat without inflating or softening it. The *Atthasālinī*'s commentator let an older text lose on a test, and a microphone lets him lose in turn. I want an instrument that can write both of those sentences, and write the opposite sentence when the texts win. The ledger says it cannot do that reliably yet. That sentence is in the ledger too, and it is the reason the rest is worth reading.

---

## Acknowledgments

Drafted with Miss Aquarius℠, the AI collaboration of this institution, per the corpus convention for essays in my voice; the programme, the argument and final editorial control are mine, and my own pass is owed. The blind deriver and the separate refuter described in §3 are roles of an AI instrument in the same collaboration. The refuting pass that produced §7 read the ledger and the instrument in full before this essay was drafted, and its report is kept with the review record.

## Corpus cross-references

- *Abhidhamma and Discrete Quantum Gravity* ([10.5281/zenodo.23020020](https://doi.org/10.5281/zenodo.23020020)): the physics lens, where "matter is dated by it" and "mind has no between" have their depth, in a revision under review.
- *The Vibhajjavādin View of Time* ([10.5281/zenodo.23020015](https://doi.org/10.5281/zenodo.23020015)): the answer to Dowker's invitation, and the home of the beginning, in a revision under review.
- *The Counts Check* ([10.5281/zenodo.23020670](https://doi.org/10.5281/zenodo.23020670)): the one test the core has met, of its agreement with itself.
- *The Abhidhamma as an Executable Process Specification*: the corpus's earlier formal reading, which cites Barendregt.
- `SiliconWat/formal-abhidhamma` ([10.5281/zenodo.23067241](https://doi.org/10.5281/zenodo.23067241)): the instrument, the axioms, the Lean, and the ledger at `runs/INDEX.md`.

## References

Pāli citations are to the Chaṭṭha Saṅgāyana text as distributed by VipassanaTech (`tipitaka-xml`, `romn/`, at commit `05d5d3c`), by file and line, with the layer named: mūla (Piṭaka), aṭṭhakathā (commentary), ṭīkā (sub-commentary), or other (manuals and later works).

- Barendregt, H. (2006). "The Abhidhamma Model of Consciousness AM₀ and some of its Consequences." Preprint dated 7 May 2006, to appear in M.G.T. Kwee, K.J. Gergen and F. Koshikawa (eds.), *Buddhist Psychology: Practice, Research & Theory*, Taos Institute Publishing. <http://cs.ru.nl/~henk/G.pdf>
- Barendregt, H. and Raffone, A. (2022). "Axiomatizing Consciousness with Applications." In *A Journey from Process Algebra via Timed Automata to Model Learning*, Lecture Notes in Computer Science, Springer. [doi:10.1007/978-3-031-15629-8_3](https://doi.org/10.1007/978-3-031-15629-8_3)
- Brightwell, G. and Gregory, R. (1991). "Structure of random discrete spacetime." *Physical Review Letters* 66(3): 260–263. [doi:10.1103/PhysRevLett.66.260](https://doi.org/10.1103/PhysRevLett.66.260)
- Chambers, C. D. (2013). "Registered Reports: A new publishing initiative at Cortex." *Cortex* 49(3): 609–610. [doi:10.1016/j.cortex.2012.12.016](https://doi.org/10.1016/j.cortex.2012.12.016)
- Cogitate Consortium et al. (2025). "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642: 133–142. [doi:10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1)
- DeMillo, R. A., Lipton, R. J. and Sayward, F. G. (1978). "Hints on Test Data Selection: Help for the Practicing Programmer." *Computer* 11(4): 34–41. [doi:10.1109/C-M.1978.218136](https://doi.org/10.1109/C-M.1978.218136)
- Dowker, F. (2022, revised 2023). "Causal Set Quantum Gravity and the Hard Problem of Consciousness." [arXiv:2209.07653](https://arxiv.org/abs/2209.07653)
- Lakatos, I. (1970). "Falsification and the Methodology of Scientific Research Programmes." In I. Lakatos and A. Musgrave (eds.), *Criticism and the Growth of Knowledge*, Cambridge University Press, 91–196. [doi:10.1017/CBO9781139171434.009](https://doi.org/10.1017/CBO9781139171434.009)
- Lorrimar, V. (2017). "Are Scientific Research Programmes Applicable to Theology? On Philip Hefner's Use of Lakatos." *Theology and Science* 15(2): 188–202. [doi:10.1080/14746700.2017.1299376](https://doi.org/10.1080/14746700.2017.1299376)
- Mago, J., Brahinsky, J., Miller, M., Maschke, C., Slagter, H. A., Catherine, S., Laukkonen, R. E., Cahn, B. R., Sacchet, M. D., Dixey, W., Dixey, R., Rej, S. and Lifshitz, M. (2025). "Meditative absorption shifts brain dynamics toward criticality." [arXiv:2511.20990](https://arxiv.org/abs/2511.20990)
- Mansfield, V. (2008). *Tibetan Buddhism and Modern Physics.* Templeton Foundation Press.
- Mehm Tin Mon (2015). *The Essence of Buddha Abhidhamma: The Ultimate Science, Supreme Psychology, Supreme Philosophy of the Buddha.* Third edition. Yangon: Mya Mon Yadanar.
- Murphy, N. (1990). *Theology in the Age of Scientific Reasoning.* Ithaca: Cornell University Press.
- Panickssery, A., Bowman, S. R. and Feng, S. (2024). "LLM Evaluators Recognize and Favor Their Own Generations." *Advances in Neural Information Processing Systems* 37.
- Sorkin, R. D. (2007). "Relativity theory does not imply that the future already exists: a counterexample." In V. Petkov (ed.), *Relativity and the Dimensionality of the World*, Springer. [arXiv:gr-qc/0703098](https://arxiv.org/abs/gr-qc/0703098)
- Wallace, B. A. (2007). *Contemplative Science: Where Buddhism and Neuroscience Converge.* Columbia University Press.
- Zajonc, A. (ed.) (2004). *The New Physics and Cosmology: Dialogues with the Dalai Lama.* Oxford University Press.

## Cross-venue identifiers

- Canonical: thonly.org/research/letting-the-texts-lose
- GitHub: github.com/thonly/publications/blob/main/essays/letting-the-texts-lose.md
- The ledger it reports: github.com/SiliconWat/formal-abhidhamma/blob/main/runs/INDEX.md
