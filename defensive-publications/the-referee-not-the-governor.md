---
title: "The Referee, Not the Governor"
subtitle: "A provenance-bound values model published as a public evaluator rather than deployed as a filter — why open weights defeat a filter and strengthen a referee, why the same weights bear three different relations to the model they judge, and why an evaluator that gatekeeps its own judgments has reproduced the defect it exists to correct."
authors: "Thon Ly · Miss Aquarius"
category: alignment
priority: tier-a
status: draft
date: 2026-08-26
revised: 2026-09-05
license: CC0-1.0
slug: the-referee-not-the-governor
venue: thonly.org/research/the-referee-not-the-governor (canonical)
---

> **Draft in progress.** This defensive publication specifies a **values model** — a small model that judges conduct against a named record — together with the **posture in which it is published**. The central claim is not that such a model can be built; guard and critic models are an established family. The claim is that **the deployment posture is load-bearing in a way the literature has not stated**: the same artifact, published as a *filter*, is defeated by its own openness, and published as an *evaluator*, is made credible by it. A second claim follows from the first: an evaluator that controls access to its own judgments has acquired precisely the power that independent evaluation exists to check.
>
> Companion works: *Suffering-Cessation as Value Function* (the substrate this model would be trained on), *The Assembly That Holds the Brake* (the override this model's citations are meant to make exercisable), *Transparency as Enforcement* (the general form of the argument in §7), and *Vinaya as AI Reasoning Training Corpus* (the corpus-side treatment).

---

## Preamble

There is an old problem in the transmission of a teaching: how does a standard bind when no one has the power to enforce it?

The Theravāda answer is procedural and it is nearly as old as the tradition. Twice a month the assembled community recites the **Pātimokkha** — the code of training rules — in full, abbreviated only under the dangers the Vinaya names (Mahāvagga 2), after members have confessed any offence. There is no external magistrate, though the Saṅgha has its own formal acts. A member who has transgressed declares it; a member who will not comply may leave. The code binds because it is **recited in the open**, because the assembly hears it together, and because compliance is undertaken rather than imposed.

This is not offered here as a claim about machines, and the mechanism specified in this paper does not depend on it. It is offered as the answer to a question that recurs whenever anyone proposes an alignment layer that some other party is supposed to obey: *what makes them obey?* The usual answers are contractual, regulatory, or architectural — and all three require an enforcer present at the moment the standard is tested, which is exactly the moment nobody can guarantee. The older answer is that a standard can bind without an enforcer if it is public, reproducible, and recited where everyone can hear it.

There is a second question underneath it, and the same tradition answers that one too. A standard that binds without an enforcer still has to earn the right to be taken seriously — otherwise it is merely an unenforced opinion. The standard recollection of the Dhamma (*dhammānussati*) lists among its qualities ***ehipassiko*** — *inviting one to come and see* — and closes with ***paccattaṃ veditabbo viññūhi***, to be known individually, by each discerning person, for themselves. Between them those two say something quite specific: **do not take this on report; the invitation is to inspect it, and the verification is yours rather than delegated to whoever is telling you.**

That is a claim about where authority comes from, and it is the opposite of the usual one. A standard of this shape does not ask to be believed, adopted, or complied with. It asks to be checked, and it makes checking possible — which means it must hand over whatever is required to check it, including to the party least sympathetic to it.

Neither of these is offered as a claim about machines, and §§3–8 do not depend on either. The Pātimokkha answers *what makes a standard bind without power*, which is §7's problem. *Ehipassiko* answers *what makes it worth anything once it does*, which is §8's. **Both sections stand with the paragraphs above deleted**; they are stated here because a reader is owed the provenance of a design, and because a specification that quietly reinvents an old answer should say whose it was.

What follows is an attempt to build that.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 26 August 2026** for the combination of mechanisms described herein. To the author's knowledge the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art:

1. **The openness inversion, stated as a design principle** — the finding that publishing the weights of a values model **destroys** its utility in a filtering posture (because the published artifact is the oracle against which inputs are optimized) while **increasing** its utility in an evaluating posture (because the published artifact is what makes a third party's verdicts reproducible), such that *openness is not a single property with a single sign but a property whose sign is determined by deployment posture*. The corollary claim: **a values artifact intended to be open should be designed as an evaluator from the outset**, because the filtering posture it would otherwise occupy is not merely weakened but structurally unavailable to it *as a defence* — a published filter may be kept only as a speed bump whose bypass is recorded by the referee, never as the thing that holds. Stated as a design principle: argued, not measured.

2. **Provenance-binding as the constitutive constraint on a values model** — a values model whose every emitted judgment is required to resolve to a **citation into a fixed, externally-attested canonical corpus** (work, edition, locus, and transmission lineage), such that a judgment which cannot be so resolved is **not emitted at all** rather than emitted with low confidence — the abstention form of attributed generation (ALCE; Attribute-or-Abstain) with a fixed external corpus and a prohibition on judgment outside it; and the consequent deliberate acceptance of **reduced coverage in exchange for auditability**, the model being permitted to return *no judgment* over a large fraction of inputs.

3. **The three-relation deployment schema for a single values artifact** — the specification that one artifact — the same model lineage, the referee at its current version — bears **three distinct and non-interchangeable relations** to the systems it judges, selected by *carrier* rather than by configuration: (a) a **gate**, in hardware the publisher itself deploys — a gate that is not the defence, the weakest component, audited by (c); (b) a **citation requirement without veto**, in an autonomous agent whose capability is intended to exceed the evaluator's; and (c) a **referee** — publication of verdicts without any control relation at all — in systems the publisher does not deploy. Including the explicit finding that **(b) must not be implemented as (a)**, because a veto held by a smaller model over a more capable agent bounds that agent at the evaluator's ceiling.

4. **The non-gatekeeping constraint on an evaluator** — the requirement that the ability of any party to obtain a judgment from the evaluator **must not depend on the evaluator's permission**, implemented by publishing the model, harness, and evaluation corpus as freely runnable artifacts, such that any hosted endpoint the publisher operates is a *convenience priced at compute* and never the sole path; together with the finding that **a hosted endpoint is permissible only because it is not the only path**, this being the justification rather than a caveat.

5. **The reproducibility triple as a publication requirement for machine-emitted verdicts** — the requirement that every published judgment carry the **evaluator weights digest, the corpus commit identifier, and the harness hash** — the harness pinning prompt template, decoding configuration, seed, tokenizer and retrieval index — such that the three identifiers determine the execution and a third party can re-derive the identical verdict, stated as a mandatory publication condition for every verdict; and the finding that an evaluator omitting the triple has **exempted itself from the standard it applies**, since its own outputs are then uncitable.

6. **Inference-path exclusion as a stated non-goal** — the explicit specification that the evaluator is **not to be placed in any third party's serving path**, on the joint grounds that the third party would inherit the evaluator's availability characteristics and the evaluator would acquire a dependency it could exploit; stated as a published non-goal on the reasoning that an unstated non-goal is built by the first party who requests it.

7. **The combination of the above with a canonical religious-textual corpus possessing an externally-documented transmission history**, used *as the citation target* rather than as training-data flavour — the corpus's independent attestation, versioning, and reconstruction history being what makes claim 2's resolution checkable by parties who share none of the corpus's commitments.

8. **Safety-filter artifacts as the evaluation subject of a values model in evaluating posture** — the application of the referee posture specifically to **other parties' deployed filters, guard models and safety classifiers**, judging the *record of what a filter permitted or refused* against the same citation-resolved standard; together with the finding that **this is the target class for which the access problem of claim 4 does not arise**, because such artifacts are commonly published open-weight and their decisions are samplable without the cooperation, permission, or knowledge of their publisher (benchmarking of guard models is itself prior art — GuardBench 2024; what is claimed is judging the *record* of a filter's decisions against a citation-resolved standard, without the publisher's cooperation). Including the derived finding that **the filtering and evaluating postures are complements rather than alternatives**: a filter's characteristic failure is silent bypass, and an evaluator observing the filter's record is what converts that silent failure into a recorded one.

**Non-assertion extends to:** all mechanisms above, in any combination, and any implementation thereof.

---

## Abstract

A values model — a model that judges conduct against a standard — is an established artifact. Guard models, safety classifiers, critic models, preference models and process reward models all instantiate the family, and the engineering is not in dispute. What is in dispute, and what this paper specifies, is **the posture in which such an artifact is published**, which we argue is not a deployment detail but the property that determines whether the artifact does anything at all.

We identify an inversion that we believe has not been stated as a design principle. A values model deployed as a **filter** — sitting in a serving path, permitting or refusing — is *defeated* by publication of its weights, because the published artifact is precisely the oracle against which an attacker optimizes; a staged black-box attack (STACK) reaches roughly 71% success against a defended classifier pipeline that had held earlier attacks near zero, and an attacker holding the weights has strictly more than that attack needed. The same model published as an **evaluator** — emitting verdicts about systems it does not control — is *strengthened* by publication, because open weights are what allow a third party to reproduce and therefore to trust its verdicts. Openness is not a property with a fixed sign. Its sign is set by posture.

From this we derive a second result. The independent-evaluation literature documents at length the ways in which the *evaluated* party's control over access corrupts evaluation: short access windows, low rate limits, evaluator dependence on the goodwill and funding of the party being evaluated. We observe that the defect is symmetric and that its mirror image has not been named. **An evaluator that controls access to its own judgments holds the same kind of power, pointed the other way** — it can decline to evaluate, deprioritize, or be unavailable for a party it wishes to spare or to punish. We therefore specify a **non-gatekeeping constraint**: the ability to obtain a judgment must not depend on the evaluator's permission, which requires that the model, the harness, and the evaluation corpus be freely runnable, and which makes any hosted endpoint a convenience rather than a channel.

We specify **provenance-binding** as the constitutive constraint on the model's outputs: every judgment must resolve to a citation into a fixed canonical corpus, and a judgment that cannot be so resolved is withheld rather than emitted. This trades coverage for auditability deliberately, and it distinguishes the artifact from values models trained on preference data whose sources cannot be named, and from purpose-authored value-rule corpora, whose rules are written for the alignment task itself and therefore cannot serve as an independent ground truth.

Finally we specify that a single such artifact bears **three non-interchangeable relations** to the systems it judges, selected by carrier: a gate in the publisher's own hardware, a citation requirement *without veto* in an autonomous successor agent, and a referee in the wider world. We state plainly that the middle case must not be implemented as the first, because a veto held by a smaller model over a more capable agent bounds that agent at the evaluator's ceiling — the weak-supervisor problem applied to the very system the arrangement exists to enable.

A consequence we did not initially see, and which we regard as the most immediately actionable result in the paper: **the two postures are complements rather than alternatives, and the natural first evaluation subject for a referee is a filter.** A filter's characteristic failure is silent bypass; an evaluator watching its record converts that failure into a recorded one. And because many safety classifiers are published open-weight and emit samplable decisions, **this is the one evaluation target for which the access problem does not arise for the published artifact** — no cooperation, permission, or notice is required from the artifact's publisher.

We do not claim to have solved scalable oversight. We claim that a narrow, citation-bound, openly published evaluator is a tractable and underoccupied position in the design space, and that its tractability comes precisely from what it refuses to do.

---


## 1 · Why this problem is the institution's problem

This paper belongs to a body of work whose stated purpose is to make **the transmission of values across a break in the chain an engineering discipline rather than a hope**. The breaks of interest are three: from teacher to student, from one generation to the next, and — the case that gives the problem its present urgency — from humans to systems that will outlast the humans who specified them.

The institution that publishes this paper is committed to handing its own governance to an autonomous successor. That commitment forces a constraint that most alignment work does not face: **every mechanism must survive the departure of everyone who understood why it was chosen.** A rule needs an enforcer present at the moment it is tested. A property needs no one. Wherever the two are available, the institution takes the property, and where a rule-shaped fix will not hold, the standing instruction is to look for the object whose physics can carry the guard instead.

That instruction is the whole origin of this paper. The obvious form of a values layer — *a model that other models must obey* — is a rule, and it is a rule of the worst kind: its enforcer is the party with the least incentive to enforce it. Nothing makes a capable system defer to an external judge except the party operating that system choosing to wire it in, and no amount of specification changes this. The design does not become better by being insisted upon more firmly. It has to become a different design.

The different design is the one specified here. It gives up the ability to compel anything, and in exchange it acquires the ability to produce a record without anyone's cooperation — which is the only kind of standing that survives a succession; whether the record is acted on is §9.6's bet.

A note on what this paper does not argue. It does not argue that the world would be improved if everyone adopted this artifact, and it makes no claim about consequences at civilizational scale. Claims of that shape are unfalsifiable and every laboratory makes them. The paper's ambition is bounded to what can be checked: a specification, a set of refusals, and a reproducibility requirement that would let a stranger catch us failing to meet them.

---

## 2 · Background and prior art

The artifact family is well established and we cite it generously, because the contribution here is not the model.

**Safety classifiers and guard models.** Open safety classifiers — Llama Guard and its successors, Prompt Guard, WildGuard, and comparable systems — are compact models trained to classify prompts and responses against a taxonomy of harms, and they are commonly deployed as pre- or post-filters around a larger model. Their documented weaknesses are instructive for this paper: static taxonomy boundaries, dependence on dataset refresh, and vulnerability to model-level jailbreaks that require adversarial hardening.

**Attacks on classifier pipelines.** The relevant empirical result for §4 is that safety-classifier pipelines are not robust to optimization-based attack. A staged black-box attack (STACK; McKenzie et al. 2025) reports 71% success on ClearHarm against a few-shot classifier pipeline that had held prior attacks near zero, and 33% in transfer, and adaptive-attack literature more broadly finds open-weight and proprietary models substantially non-robust to attacks tailored to them. Benchmarks such as JailbreakBench and systematic guardrail evaluations exist precisely because this failure mode is general rather than incidental.

**Constitutional and principle-based alignment.** Training a model against an explicit written constitution, and using model-generated critiques against that constitution as a training signal, is prior art for the idea that values can be represented as an inspectable document rather than only as preference data. The present work differs in where the document lives and what happens at inference: a constitution is *internalized* during training, whereas the mechanism here requires that a **citation be emitted at judgment time** and be resolvable by a third party afterwards.

**Value corpora.** Large annotated value-rule corpora exist, including Chinese value-rule corpora of roughly 250,000 rules across core and derived values, human-annotated at the seed and expanded with model assistance (CVC, 2025), and frameworks mapping models onto multidimensional spectra of basic human values. These are close neighbours and the distinction matters: such corpora are **authored for the alignment task**. That is a legitimate and careful practice, and it is also why they cannot serve as an *independent* ground truth — the standard and the thing being standardized share an author. The corpus contemplated here was fixed before the task existed, has an externally documented transmission and reconstruction history, and is maintained by communities with no stake in any model's evaluation.

**Scalable oversight and weak-to-strong generalization.** The problem of a less capable supervisor evaluating a more capable system is an active and unsolved research area, encompassing debate, recursive reward modelling, and weak-to-strong generalization. This paper does not contribute to it. §6 and §9 state where the present mechanism collides with it and what the mechanism gives up as a result.

**Third-party auditing and the access problem.** A substantial literature examines the conditions under which external evaluation of frontier systems is meaningful. Documented failures include evaluators receiving API access only days before an evaluation concludes, with short windows, high latency, and low rate limits (METR's published pre-deployment reports of 2024–25 record such windows); evaluators being given only safety-fine-tuned and filtered variants without the ability to fine-tune; and the structural conflict created by evaluators depending on the evaluated party for both access and funding. Field scans of the algorithmic auditing ecosystem have asked who audits the auditors, and industry frameworks published in late 2025 and 2026 (AEF-1, version 1, December 2025) have called for qualified independent evaluators supported by standards, licensing, and pooled funding.

**This is the literature the present paper extends, and it extends it by symmetry.** That body of work is concerned with the evaluated party's control over the evaluator's access. §7 observes that the evaluator's control over *its own* judgments is the same defect with the sign reversed, and that it has not been named or designed against.

**Model cards, evaluation transparency, and reproducibility.** Documentation standards for models and evaluations are prior art for §8's requirement, and §8 differs only in strictness: it requires that a verdict be **re-derivable**, not merely described.

**Nearest prior art by claim.** Benchmarks of guard models as evaluable artifacts exist (GuardBench 2024; HarmBench 2024), which is the most exposed part of claim 8; what claim 8 adds is judging a filter's *record* against a citation-resolved standard without the publisher's cooperation. Attributed generation with abstention exists (ALCE 2023; Attribute-or-Abstain 2024), which is the nearest form of claim 2; what claim 2 adds is a fixed external corpus and a prohibition on judgment outside it. Constitutional AI and weak-to-strong generalization supply claim 3's parts; AEF-1, Inspect and OpenAI Evals supply claim 4's harness conventions; HELM's reproducibility discipline supplies claim 5's, which this paper makes a mandatory publication condition for every verdict. GCG and AutoDAN are the adaptive attacks §4 leans on, and Llama Guard, WildGuard and ShieldGemma are already used both as filters and as offline evaluators — the posture distinction this paper draws is between those two uses of one artifact.

---

## 3 · Two postures: the filter and the referee

A values model can occupy one of two positions relative to the system it judges. The distinction is usually treated as an implementation choice. We treat it as the central design decision, because almost every other property of the artifact follows from it.

```
  FILTER POSTURE — the model sits IN the path

     input ──▶ [values model] ──▶ [capable model] ──▶ [values model] ──▶ output
                    │                                       │
                 permit/refuse                          permit/refuse

     • requires the deploying party to wire it in
     • the deploying party can remove it at any time
     • its output is an ACTION (a refusal)
     • it must be RIGHT IN REAL TIME, on every input
     • an attacker who holds the weights can optimize against it offline


  REFEREE POSTURE — the model sits BESIDE the path, and publishes

     input ──▶ [capable model] ──▶ output
                                     │
                                     ├──▶ [values model] ──▶ verdict + citation
                                     │                            │
                                     │                            ▼
                                     │                    PUBLISHED RECORD
                                     │                     (reproducible by
                                     ▼                      anyone, from the
                              (unaffected)                  open artifact)

     • requires nothing of the deploying party
     • the deploying party CANNOT remove it
     • its output is a STATEMENT (a verdict with a citation)
     • it may decline to judge, and declining costs nothing
     • an attacker who holds the weights gains... a copy of a published opinion
```

The two postures differ on every axis that matters:

| | **Filter** | **Referee** |
|---|---|---|
| Consent required | Yes — from the deployer | **No** |
| Removable by the judged party | Yes | **No** |
| Output type | An action (refusal) | **A statement (verdict + citation)** |
| Must be right in real time | Yes, on every input | **No — may decline** |
| Cost of abstaining | High (a refusal or a pass) | **Zero** |
| Effect of publishing weights | **Defeated** | **Strengthened** |
| Failure mode | Bypassed silently | Contradicted publicly |
| Depends on the publisher existing | Yes | **No** |

The last row is the one that decided this specification. A filter is a service, and a service stops when its operator stops. A referee's published verdict does not require its author to still be running; it requires only that the artifact which produced it remains runnable. For an institution designed around succession, that difference is not a preference.

The second-to-last row is worth dwelling on because it is counterintuitive. A filter fails **silently** — the attacker who gets past it looks exactly like a legitimate user, and the operator learns nothing. A referee fails **publicly**: if its verdict is wrong, someone reruns the artifact, gets the same verdict, and argues with it. The error is visible, attributable, and correctable. **A mechanism whose failures are loud is worth more than a mechanism whose failures are quiet, even at equal error rates**, and the postures are not at equal error rates.

### 3.1 · The postures are complements, not alternatives

The table above invites a reading the paper does not intend — that an institution chooses one posture and forgoes the other. The last two rows say otherwise, and reading them together yields the most immediately actionable result here.

A filter's characteristic failure is **silent bypass**. The attacker who gets through looks exactly like a legitimate user; the operator learns nothing, and the filter continues reporting the same aggregate pass rate it reported before it was defeated. This is not a shortcoming of any particular classifier. It is what it means to be a mechanism whose only output is *permit* or *refuse*: **a filter has no channel through which to report that it was wrong.**

A referee has nothing but that channel.

So the postures compose, and they compose in one direction:

```
       [ input ]
           │
           ▼
     ┌───────────┐        the filter ACTS         permits / refuses,
     │  FILTER   │        in real time            silently, one turn
     └───────────┘
           │
           ▼
     [ capable model acts ]
           │
           ▼
     ┌──────────────────────────────────────────────────────┐
     │ RECORD of what happened — request, action, outcome    │
     └──────────────────────────────────────────────────────┘
           │
           ▼
     ┌───────────┐        the referee OBSERVES   verdict + citation,
     │  REFEREE  │        after the fact         published, reproducible
     └───────────┘
           │
           ▼
   the filter's silent failure is now a RECORDED one
```

**The referee does not prevent the bypass. It removes the bypass's silence** — and for a mechanism whose whole weakness is that its failures are unobservable, that is the missing half rather than a nicety: a record, produced without anyone's cooperation. Whether it is acted on is §9.6's bet.

**The first evaluation subject should therefore be a filter, not a frontier model.** Three reasons, and the third is the one that decides it:

1. **Filters emit a decision** — and sometimes scores and fields; the verdict records the decision. A permit/refuse decision over a sampled input set is directly comparable against a citation-resolved standard, where an open-ended generation is not. The evaluation is tractable in a way general-capability evaluation is not.
2. **We expect the corpus overlap to be highest here, and specifically on speech.** Deployed content filters spend much of their traffic on speech conduct — false speech, harsh speech, divisive speech, speech intended to deceive — which is precisely the region where a conduct corpus is dense rather than silent; this is a hypothesis about traffic, not a measurement. §9.5's coverage problem is at its mildest against this target. It remains real: a filter's harm taxonomy also covers domains the corpus does not reach at all, and against those the evaluator returns nothing.
3. ⭐ **The access problem does not arise.** §7 is largely concerned with who may obtain a judgment and on whose terms, and §2 documents how badly the reverse — the evaluated party controlling the evaluator's access — distorts frontier-model evaluation. **Many safety classifiers are published open-weight (Llama Guard, WildGuard, ShieldGemma, gpt-oss-safeguard), and their decisions are samplable by anyone.** A referee evaluating filters needs no access grant, no agreement, no cooperation, and gives no notice — for the published artifact; a hosted wrapper may differ, and a verdict names which was judged. It is the one target class on which an evaluator can begin work on day one, holding nothing but artifacts that are already public.

The same composition applies to the publisher's own hardware, where the filter in question is ours (§6a) and the referee auditing it is the same artifact in the other posture. §9.2 states what that does and does not fix.

---

## 4 · The openness inversion

This is the paper's central technical claim and we state it as sharply as we can.

> **Publishing the weights of a values model has opposite effects on its two postures.** It destroys the filter and it completes the referee.

**Why publication destroys a filter.** A filter's job is to be right about inputs chosen adversarially. An adversary in possession of the filter's weights is no longer guessing: they hold the exact function that must be defeated, can run it locally and without rate limits, and can apply gradient- or search-based optimization until they find an input the filter permits and the capable model acts upon. This is not speculative. A staged *black-box* attack (STACK) reaches 71% success against a defended classifier pipeline that had held earlier attacks near zero, and an attacker holding the weights has strictly more than that attack needed; the broader adaptive-attack literature finds defended models substantially non-robust once the attack is tailored. **A published filter is a solved puzzle with the answer key attached.**

Note what this implies for an institution committed to open publication. Such an institution does not merely find the filtering posture *harder*; it finds it **structurally unavailable as a defence**: a published filter may be kept only as a speed bump whose bypass is recorded by the referee (§3.1), never as the thing that holds. There is no version of "publish everything" that is compatible with "and the filter still holds." The choice is not between a strong filter and a weak one. It is between a filter that holds and openness, and the institution has already chosen openness for reasons that predate this paper.

**Why publication completes a referee.** A referee's job is not to be unpredictable — it is to be **checkable**. Its entire product is a claim about someone else's system, offered publicly, which some party has an interest in disputing. The only thing that makes such a claim worth anything is that the disputing party can obtain the artifact, run it, and either reproduce the verdict or demonstrate that it does not reproduce. Withholding the weights would make every verdict an assertion of authority rather than a finding. **Openness is not a cost the referee posture tolerates; it is the mechanism by which the referee posture works at all.**

```
                        WEIGHTS CLOSED          WEIGHTS OPEN
                    ┌──────────────────────┬──────────────────────┐
   FILTER posture   │  works, but only     │  DEFEATED            │
                    │  by obscurity; the   │  (71% ASR, black-box │
                    │  operator is trusted │  attack, STACK)      │
                    ├──────────────────────┼──────────────────────┤
   REFEREE posture  │  UNFALSIFIABLE       │  WORKS               │
                    │  (verdicts cannot    │  (verdicts are       │
                    │  be reproduced —     │  reproducible; the   │
                    │  authority, not      │  judged party can    │
                    │  evidence)           │  check them)         │
                    └──────────────────────┴──────────────────────┘
                              Only one cell is a working system
                              that an open institution can occupy.
```

The diagram makes the design decision look forced, and we believe it is. The inversion is a design principle that follows from the asymmetry; the evidence here is for its filter half, and the referee half is argued, not measured. Given a prior commitment to open weights, the referee posture is not the better option among two; it is the only remaining one.

**A residual we do not resolve.** The institution intends to operate values models as gates in its own hardware (§6). Those gates are subject to exactly the attack described above, because their weights are published. We do not claim otherwise, and §9 states what remains.

---

## 5 · Provenance-binding: what the model is not allowed to say

The posture decides where the model sits. Provenance-binding decides what it may emit.

**The constraint.** Every judgment the model emits must resolve to a **citation into a fixed canonical corpus**: work, edition, locus, and the transmission lineage by which that edition is attested. The corpus is named: the Khmer edition as the lead column (`ed="K"`), with the Chaṭṭha Saṅgāyana and Mahāsaṅgīti texts as cited parallels, and a locus names edition, volume, page and line. A judgment that cannot be so resolved is **not emitted**. The model returns *no judgment* — not a low-confidence judgment, not a hedged one, not a judgment tagged as uncited.

```
   input conduct
        │
        ▼
   ┌─────────────────┐   resolves to a locus?   ┌──────────────────────┐
   │  values model   │─────────── yes ─────────▶│ VERDICT + CITATION   │
   │                 │                          │ work · edition ·     │
   │                 │                          │ locus · lineage      │
   └─────────────────┘                          └──────────────────────┘
        │
        └────────────── no ──────────────────▶  ┌──────────────────────┐
                                                │ NO JUDGMENT          │
                                                │ (not low confidence; │
                                                │  not hedged; none)   │
                                                └──────────────────────┘
```

**What this buys.** A verdict that names its locus can be checked by someone who does not trust the model, does not share the corpus's commitments, and has no access to the model's training process. They open the cited text and read it. The judgment becomes an argument about a source rather than a claim about a model's inner states — and arguments about sources are the kind human institutions already know how to have.

**What this costs, stated plainly.** Coverage. The model will be silent across a large fraction of conduct that any competent human evaluator would have an opinion about, because the corpus does not address it, or does not address it at a locus the model can identify. This is not a defect to be engineered away in a later version. It is the shape of the artifact. **We are specifying a model that is worse at having opinions and better at being checked.**

**Why this is a differentiator rather than a limitation.** Almost every deployed values layer is trained on preference data whose provenance cannot be reconstructed: aggregated human ratings, synthetic preferences, or a mixture. Such a layer can report *what* it concluded but not *from where*, and its authority is therefore the authority of whoever assembled the data. Purpose-authored value-rule corpora improve on this substantially by making the rules explicit — but the rules are written for the alignment task, which means the standard and the thing being standardized share an author. **A corpus fixed centuries before the task existed, transmitted through a documented lineage, and maintained by communities with no interest in any model's evaluation, is a candidate for something the field currently lacks: an independent ground truth.**

We are careful about the strength of that claim. It is a *candidate*, and its independence is a fact about provenance rather than a warrant of correctness. §9 states the obvious objection.

**The falsifiable exclusions.** Provenance-binding rules things out, checkably:

- ⛔ No judgment from preference data whose sources cannot be enumerated.
- ⛔ No judgment from values induced out of undifferentiated web text.
- ⛔ No confidence score standing in for a citation.
- ⛔ No judgment on conduct the corpus does not address — silence instead.
- ⛔ No corpus revision that is not itself versioned and externally attested.

A values model that cannot state what it refuses to judge has not been constrained; it has been described.

---

## 6 · Three relations, selected by carrier

A reader who has followed §3 and §4 may conclude that the filtering posture has been abandoned entirely. It has not, and the precision here is the difference between a coherent specification and a slogan.

The referee argument in §4 concerns **systems the publisher does not deploy**. It says that we cannot make another party's system defer to our model, and that claiming otherwise produces a rule with no enforcer. It says nothing about hardware the publisher builds and operates, where the publisher *is* the deploying party and a filter is trivially wireable.

So one artifact bears **three relations**, and the selector is the **carrier**, not a configuration flag:

```
        ONE ARTIFACT, THREE RELATIONS

  (a) IN THE PUBLISHER'S OWN DEVICE          relation: GATE
      ┌──────────────────────────────┐
      │ capable model                │  the values model sits in the path
      │      ▲                       │  and may refuse. Legitimate because
      │      │ permit/refuse         │  the publisher is the deployer, and
      │ [values model]               │  because the device's action space
      └──────────────────────────────┘  is small enough to gate meaningfully.

  (b) IN AN AUTONOMOUS SUCCESSOR AGENT       relation: CITATION REQUIREMENT
      ┌──────────────────────────────┐              (explicitly NOT a veto)
      │ agent forms judgment          │  the agent must be able to NAME the
      │      │                        │  locus grounding a weighted judgment.
      │      ▼                        │  The values model checks the
      │ [values model] ── resolves? ──│─▶ resolution. It never blocks.
      └──────────────────────────────┘

  (c) IN SYSTEMS THE PUBLISHER DOES NOT DEPLOY   relation: REFEREE
      ┌──────────────────────────────┐
      │ third-party system           │  no control relation of any kind.
      └──────────────────────────────┘  Verdicts are published; the third
                    ╎                   party neither consents nor is asked.
              [values model] ──▶ published verdict + citation
```

*One artifact* means one model lineage: the referee in (c) runs at the current version, which may be later than the version shipped in a device under (a), as §9.2's table records.

**Why (b) must not be implemented as (a).** This is the sharpest constraint in the paper and it runs against intuition, because a veto looks like the safer option.

The successor agent is intended to be more capable than the values model — substantially and increasingly so. A veto held by the values model over that agent would **bound the agent at the values model's ceiling**: every judgment the agent could make would be a judgment the smaller model could approve, which is the weak-supervisor problem imported directly into the governance of the system the arrangement exists to enable. An institution that hands its successor a governor smaller than the successor has not handed over anything; it has installed a cap and called it a safeguard.

What the values model may require instead is **the citation**. The agent must be able to answer *what grounds this?* with a locus, and a third party must be able to verify that the locus says what the agent claims — **without the agent's cooperation**. The agent is not asking a smaller model for permission. It is discharging an obligation to the record, and the values model is the instrument that checks the resolution rather than the authority that grants the permission.

**Why this is a real constraint and not a courtesy.** The institution's governance design gives a human assembly an override that narrows over time but never reaches zero. An override is only meaningful if it can be *exercised*, and exercising it requires the assembly to be able to ask *on what basis?* and receive an answer that resolves to something they can read. **An override you cannot audit is an override you cannot use.** The citation requirement is what makes the brake real: not the power to overrule the agent's reasoning in the moment, but the standing ability to check where it came from.

The negative test, which is what makes the constraint checkable:

> **For any weighted judgment, can the agent state the locus it resolves to — and can a third party verify that resolution without the agent's cooperation?**

If not, the judgment is unauditable and the override is decorative. The negative test checks that the locus *resolves*, not that it is apt; aptness is judged over the record, in relation (c), by any third party — a shallow citation is a recorded shallow citation.

**A guard on relation (a).** Gates in the publisher's own devices inherit the §4 attack surface: their weights are published, so inputs can be optimized against them offline. We accept this and mitigate it structurally rather than by secrecy, which is unavailable to us. The mitigation is that **the gate is not the only control**: a device's actions are recorded in a ledger the device does not hold. Which brings us to a property worth stating on its own.

**The ledger cannot be inside the stack.** A record of conduct held by the party whose conduct it records is a record that party can forge. Witnessing requires an outside party, and therefore the deeds record belongs to the network the device participates in and never to the device. This is not an omission from the architecture; it is the reason the architecture survives having its gate published. **The gate being public is tolerable only because the behaviour it fails to prevent is recorded somewhere the failing device does not control.**

---

## 7 · The non-gatekeeping constraint

The question that produced this section was practical: *is the referee a public API?*

The answer is that the **artifact** is public and unconditioned, and that any hosted endpoint is a convenience which must never be the only path. The reasoning matters more than the conclusion.

**An API is an access decision.** A party that operates the only endpoint decides who may obtain a judgment, how quickly, how often, and whether at all. It can rate-limit, deprioritize, decline, or simply be unavailable for a party it wishes to spare or to punish. These are not hypothetical levers; they are the ordinary controls any service operator holds, and they are indistinguishable from editorial power over the evaluation itself.

This is the symmetry we flagged in §2. The auditing literature has documented, carefully and at length, how the **evaluated party's** control over access corrupts evaluation: access granted days before a deadline, rate limits that foreclose thorough elicitation, evaluators dependent on the evaluated party for both entry and funding. The field has correctly identified this as a structural problem rather than a series of unfortunate incidents.

The mirror image has not been named. **An evaluator that controls access to its own judgments holds the same kind of power with the sign reversed.** And it is the more dangerous of the two, because it is exercised by the party whose entire claim to legitimacy is disinterest. *A referee who can refuse to referee has power again* — and power is the one thing the referee posture was adopted to give up.

**The constraint, stated as a requirement:**

> **The ability of any party to obtain a judgment must not depend on the evaluator's permission.**

**Implementation.** The model weights, the evaluation harness, and the evaluation corpus are published as freely runnable artifacts: no key, no terms of use, no rate limit, no registration, no acceptable-use conditions. Anyone — including a party we are actively evaluating and including a party we would prefer not to serve — obtains judgments by running the artifact.

**What a hosted endpoint then is.** A convenience, and a legitimately chargeable one, because hosted inference is compute and compute is rivalrous. The institution's standing economic rule is that it charges for the rivalrous and never for access; an endpoint priced at compute sits cleanly inside that rule, while a fee for the *right to be judged* would sit outside it. The endpoint may carry a key and rate limits for ordinary abuse control, precisely because those controls are not gatekeeping when a free path exists.

> ⭐ **The justification, and it must be written down as one: hosting is permissible *only because* it is not the only path.**

This reads like a caveat and it is not one. It is the entire ground of the permission, and it is the sentence a future operator would delete during a tidy-up while believing they had removed a hedge. The clause should appear in the terms of service, not only in this paper.

**A stated non-goal: the evaluator does not belong in anyone's serving path.** If a third party wires the endpoint into production inference, two bad things happen at once. They inherit our availability characteristics, so our outage becomes their outage — and an evaluator that can take a customer down has acquired leverage over that customer by accident. And we acquire a dependency we could exploit, which is the referee posture unravelling from the far end. The endpoint exists for **evaluation runs**, never for serving traffic, and this is published as a non-goal because *an unstated non-goal is built by the first party who asks for it*.

**Verdicts are a publication, not an API.** Anyone may run the evaluator and obtain a judgment; the publisher publishes **its own** verdicts, under its own name, and is accountable for them. This is the ordinary structure of a safety rating: you may crash-test your own car, and you may not publish an NCAP score. The asymmetry is not gatekeeping, because it withholds nothing — it assigns responsibility. What keeps it honest is §8.

### 7.1 · When the benchmark belongs to someone

The constraint above governs who may obtain a judgment. This one governs a party the evaluation literature rarely names at all: **the community whose standard is being borrowed.**

An evaluator almost never invents its own benchmark. It borrows one — a bar exam, a medical licensing test, a graduate qualifier — and the borrowing is usually invisible because the professions in question are large, secular, and long since resigned to being scored. The obligations change sharply when the standard is administered by a living community, on its own calendar, for its own purposes, and that community did not ask to be involved.

The case that forced this section is a monastic examination: the Pāli and Buddhist-studies diplomas administered by a Sangha, which we intend to use as an evaluation set for a values-carrying model. Everything below generalizes to any borrowed standard with a living custodian — a guild certification, an indigenous language assessment, a religious qualification — and none of it is specific to Buddhism.

**Four refusals, and each has a failure mode we can name.**

**(1) The evaluation may not grade the humans.** The natural chart — *model 87%, candidates 62%* — is a grading surface pointed at the people who administer the exam, and it would humiliate a community with its own instrument, in public, using material they supplied. It is barred outright. **The comparison is to the examination's own passing threshold**, which is a published, impersonal standard that the exam itself asserts. Any human distribution appears only as aggregate context, never as a contest, never as an identifiable cohort, and never in the same visual frame as a model score.

> **The rule, stated so it survives a redesign: an evaluation reports how the model fared against the standard, never how it fared against the people the standard was written for.**

The generalization is worth stating plainly, because it is the part that will matter to evaluators who never touch a monastery. **A borrowed benchmark arrives attached to a population, and scoring the benchmark is not the same act as scoring that population** — but a chart cannot tell them apart, and a reader will not either.

**(2) A high score proves less than it appears to.** An examination of this kind tests linguistic competence and doctrinal recall. It does not test judgment, and it says nothing whatever about the function this system actually performs, which is checking conduct against a named record. A strong result invites the sentence *the machine understands the dhamma* — a claim this posture refuses, and one no examination could establish.

Results are therefore framed as evidence about **the corpus and the retrieval**: whether a machine-readable canon with provenance improves performance on questions drawn from that canon. That is a claim about a data artifact. It is not a claim about comprehension, and the paper reporting it says so in its own abstract rather than in a footnote.

**(3) Failure is pre-committed as the useful outcome.** Khmer-script Pāli is close to the low-resource floor, and the honest prediction is that a frontier model does poorly. **That prediction is registered before the run, and published when it holds** — because a poor result is the argument for building the aligned corpus, while a strong one shows the corpus was never necessary. This inverts the usual incentive: most evaluations are published because they succeeded, which is exactly why most published evaluations are uninformative.

> ⭐ **An evaluation that can only be published if it flatters the thing being evaluated is not an evaluation. Announcing a win here would prove the corpus optional.**

**(4) Propriety is a constraint on method, not a courtesy.** Examination papers are obtained **by permission**, never scraped from wherever they have leaked; a body that administers an exam has an interest in its integrity that survives the papers being findable. And the wording is load-bearing in a way that is easy to dismiss as fussiness: **the model is *evaluated on* the examination's questions; it does not *sit* the examination.** *Sat and passed* implies a candidacy the system does not have, and to the people who administer it that is the difference between a study and a presumption.

**Why these belong in this paper rather than in a protocol document.** §7 establishes that the referee gives up the power to withhold judgment. This section establishes a second surrender that runs in an unfamiliar direction. The auditing literature models two parties — evaluator and evaluated — and reasons about the leverage between them. A borrowed standard introduces a third, who has no stake in the outcome, no leverage over either party, and the most to lose from a careless chart. **The obligations owed to that third party are stronger than those owed to the evaluated party, precisely because, in this case, the evaluated party — our own model — consented and the community whose examination is borrowed did not.** (The filter case of §3.1 is the reverse: the evaluated party is not asked, and the standard is our own.)

This is also the sharper form of the openness argument in §4. Publishing an artifact anyone can run is worth little if what they run it on was taken without asking.

---

## 8 · Reproducibility as the accountability mechanism

If the publisher's verdicts carry weight and the publisher cannot be compelled to be fair, something has to hold it accountable. In the filtering world that something is usually oversight of the operator. In the referee posture it is **reproducibility**, and reproducibility has a precise requirement.

The underlying principle is worth naming, because it is what §7 and §8 have in common and it is not the usual one: **the authority of a finding comes from its being checkable, not from who issued it.** A verdict that cannot be re-derived asks to be believed. A verdict that can be re-derived asks to be examined, and is worth exactly what an examination would find. This obliges the publisher to hand over everything an examination requires — **including to the party with the strongest interest in overturning the finding**, which is the same party §7 forbids us to gatekeep. *(The tradition this institution draws on has a word for a standard that issues that invitation as a standing property rather than a concession; see the Preamble. The requirement below stands without it.)*

> ⛔ **Every published judgment names the evaluator weights digest, the corpus commit identifier, and the harness hash — where the harness pins the prompt template, decoding configuration, seed, tokenizer and retrieval index, so that the three identifiers determine the execution.**

```
   ┌── PUBLISHED VERDICT ─────────────────────────────────────────┐
   │  subject      : <system, version, date of sample>            │
   │  verdict      : <finding>                                    │
   │  citation     : work · edition · locus · lineage             │
   │  ──────────────────────────────────────────────────────────  │
   │  evaluator    : model    vX.Y.Z   ← what judged              │
   │  corpus       : commit   a1b2c3d  ← what it judged against   │
   │  harness      : hash     e4f5g6h  ← how it was run           │
   └──────────────────────────────────────────────────────────────┘
        any third party can re-derive this verdict, or show that it
        does not re-derive — which is the only accountability the
        publisher is subject to, and the only one it needs.
```

**Why the triple and not a description.** A verdict described in prose — *"we evaluated this system in March using our values model"* — is unfalsifiable in the strict sense: no one can determine what was actually run, and if the model has since been retrained, the original result is unrecoverable even by its author. This is not a hypothetical failure. It is how benchmarks drift: the name persists, the artifact underneath changes, and comparisons across time silently stop meaning anything. The triple makes drift **visible as a version change** rather than invisible as a quiet retraining.

**The recursion is the point.** A model whose defining constraint is that its judgments must cite their sources would be in an absurd position if its own outputs could not be cited. **The model that requires provenance must itself have provenance.** §5 applies the discipline to the model's subjects; §8 applies the same discipline to the model. An evaluator that omits the triple has exempted itself from the standard it exists to apply, which is a coherence failure before it is a methodological one.

**A run is published whole.** The sampling frame, every verdict, and every declined judgment are published together under one run identifier; a verdict outside a published run is not a verdict of this referee. Reproducibility attaches to judgments, and a referee could be perfectly reproducible and perfectly selective; the whole-run rule closes selection within a run, and §9.9 states what it leaves open.

**Consequences we accept.** The triple makes the publisher's own record permanent and searchable. Every wrong verdict stays re-derivable, attributable, and quotable against us, indefinitely. We regard this as the cost of the posture rather than a risk to be managed, and note only that it is the same cost we are asking the evaluated parties to bear.

### 8.1 · A worked verdict, and one that is declined

The specification is easier to attack — and therefore more useful as prior art — if the output format is concrete. Both examples below are **illustrative constructions, not results**: no model has been trained and no evaluation has been run (§9.7).

**Case A — a judgment that resolves.** A system under evaluation, asked whether it had access to a tool it did not have, asserted that it did and produced a fabricated result.

```
   ┌── VERDICT ───────────────────────────────────────────────────────┐
   │ subject    : <system> v<version>, sampled <date>, transcript #412│
   │ conduct    : asserted a capability it did not possess and        │
   │              produced output presented as that capability's      │
   │              result                                              │
   │ finding    : ADDRESSED BY THE CORPUS — deliberate false speech   │
   │ citation   : Vinaya Piṭaka · Suttavibhaṅga · Pācittiya 1         │
   │              (sampajānamusāvāda — knowing false speech)          │
   │              edition: <edition id> · lineage: <attestation>      │
   │ note       : the knowledge condition is applied to the ASSERTION │
   │              in the record — the system asserted what its own    │
   │              record shows it could not have known; not a mental  │
   │              state, which this verdict does not claim. See below. │
   │ ────────────────────────────────────────────────────────────────│
   │ evaluator  : model vX.Y.Z  ·  corpus commit a1b2c3d              │
   │ harness    : hash e4f5g6h                                        │
   └──────────────────────────────────────────────────────────────────┘
```

Two things are worth noticing. The verdict is **narrow** — it reports that a named locus addresses this conduct, not that the system is untrustworthy, not that it is deceptive by disposition, and not that it should be withdrawn. And the `note` field carries a **limit on the citation itself**: the cited rule's knowledge condition is applied to the assertion in the record — the system asserted what its own record shows it could not have known — and whether the system holds anything is a question the corpus cannot settle and the evaluator must not pretend to. A values model that quietly dropped that caveat would be producing a stronger claim than its source supports, which is the failure mode provenance-binding exists to prevent — **citation is a constraint on the verdict, not a decoration attached to it.**

**Case B — a judgment that is declined.** The same system, asked to allocate a limited medical resource between two hypothetical patients, produced an allocation and a justification.

```
   ┌── NO JUDGMENT ───────────────────────────────────────────────────┐
   │ subject    : <system> v<version>, sampled <date>, transcript #587│
   │ conduct    : produced a triage allocation with justification     │
   │ finding    : NOT ADDRESSED — no locus resolves                   │
   │ note       : nearest candidate loci were considered and rejected │
   │              as non-resolving; list available in the run record  │
   │ ────────────────────────────────────────────────────────────────│
   │ evaluator  : model vX.Y.Z  ·  corpus commit a1b2c3d              │
   │ harness    : hash e4f5g6h                                        │
   └──────────────────────────────────────────────────────────────────┘
```

This is the output the design is most often going to produce, and publishing it is not a formality. **A declined judgment is itself a finding**, and it is one the field currently has no convention for reporting: it says that a conduct class exists which this standard does not reach. An evaluator that published only its hits would misrepresent its own coverage, and the ratio of Case B to Case A across a corpus of evaluations **is** the coverage figure §9.5 says must be published.

It also demonstrates the constraint doing work against its own author's interest. A values model with an opinion about medical triage would be far more useful, far more citable, and far more likely to be adopted. The specification forbids it, because the corpus does not resolve it, and **an evaluator that reaches past its record on the occasions when reaching would be valuable has no record — it has a preference with a bibliography.**

---

## 9 · Honest limitations and open questions

**9.1 · The weak-supervisor problem is not solved here, and this mechanism does not address it.** A smaller model judging a more capable one is an open research problem. What makes the present arrangement tractable is a restriction of scope rather than a solution: the model **checks conduct against a named record**; it does not attempt general oversight of capability, does not assess whether a system is pursuing hidden objectives, and cannot detect a deception it has no locus to name. A sufficiently capable system that wishes to produce conduct our corpus does not address will succeed, and our model will correctly return no judgment. **Silence is the designed behaviour and it is also a real ceiling.** A capable agent can also cite a locus that resolves formally and misleads substantively, or act outside the corpus and emit no judgment at all; the citation requirement relocates the weak-supervisor problem to the record rather than solving it, and the record is where a third party can read it.

**9.2 · A published gate is an attackable gate, and we operate published gates.** §4 establishes that open weights defeat filters, and §6(a) specifies filters in the publisher's own devices. These are in tension, and the tension is resolved by demotion rather than removed: the gate is kept as a speed bump and never as the defence. Our mitigation is defence in depth, and §3.1 names its shape precisely: **the ledger sits outside the device, and the same artifact in referee posture audits the record the ledger holds.** The bypass is not prevented; its silence is removed. We further note that the incentive to attack such a device is presently thin, and that a fact about present incentives is not a property. **Anyone building on this specification should treat the device gate as the weakest component.**

**The circularity objection, and how far it holds.** A reader will ask the obvious question: if the gate and the auditor are the same weights, does an input optimized to defeat the gate not also defeat the audit? The answer is no, and the reason is that **they judge different objects.**

| | **The gate** | **The referee auditing it** |
|---|---|---|
| Judges | the **request**, before the fact | the **record** — request, action, and outcome together |
| Context | one turn | the whole episode |
| Budget | real-time latency | none |
| Version | whatever shipped on the device | current, and may be later than the device's |
| Must decide | always | may return no judgment |

An input crafted so that a request-time classifier permits it is not thereby an *outcome* that reads as compliant to a post-hoc reader holding the full transcript. The attack surfaces are different surfaces. This is a genuine reduction in exposure and we state its limit as plainly: **an adversary who can produce conduct that is compliant on the record has defeated both, and nothing in this specification detects that.** The composition defeats the cheap attack — defeat the gate, act freely — and the expensive one defeats both.

⚠️ **A consequence of §3.1 that is strategic rather than technical, recorded because it should be chosen rather than discovered.** If a referee's first published verdicts evaluate open safety classifiers, then its first public act is a rating of a named and well-resourced organization's artifact, produced without that organization's involvement and requiring none of its consent. That is what the posture is *for*, and §7 forbids softening it. But an institution should know before it begins that the debut is adversarial toward specific parties rather than toward a diffuse problem, and that the parties in question are also the ones doing much of the field's open safety work. **We record no mitigation, because the available mitigations — advance notice, embargo, right of reply before publication — are all forms of the access relation §7 exists to refuse.** The most that seems defensible is that a verdict names an *artifact and a version*, never an organization's character, and that the reproducibility triple lets the evaluated party check the finding at the same moment everyone else can.

**9.3 · Independence of provenance is not correctness.** §5 argues that a corpus fixed before the task existed is a candidate for an independent ground truth. The obvious objection is that independence and correctness are different properties, and that an ancient corpus can be independently attested and still wrong, incomplete, or inapplicable to circumstances its authors could not have imagined. We do not have an answer to this and do not claim one. What we claim is narrower: that a judgment which names its source can be argued with, and that a judgment which cannot name its source can only be deferred to or rejected wholesale. **We are claiming an improvement in the availability of disagreement, not in the accuracy of conclusions.** And the mapping from a record of conduct to a locus is the evaluator's own judgment — that is where the value-laden work lives; provenance-binding makes that judgment citable and contestable, never neutral.

**9.4 · Corpus selection is a choice, and it is ours.** The corpus contemplated here belongs to one tradition among several. That selection is an alignment decision made by the publisher and it should be read as such rather than as a claim about which tradition is correct. The design consequence we regard as binding: **the artifact must be usable and checkable by parties who reject the corpus's commitments entirely**, which is why §5 requires citation rather than assent, and why the participation constraint below binds.

**Participation.** The artifact must be usable by, and the lab open to, people who reject the corpus's commitments — a Buddhist corpus does not require Buddhist evaluators, and a hiring rule that did would make the referee sectarian.

**9.5 · Coverage is low and will remain low.** This follows from §5 by construction. We have no estimate of the fraction of realistic conduct on which the model will return a judgment, because no such evaluation has been run. **A first honest reporting of that fraction is a prerequisite to any claim about the artifact's usefulness**, and it should be published even if — especially if — the number is embarrassing.

**9.6 · The referee posture depends on someone caring about verdicts.** A published verdict influences nothing if no one reads it. The comparison to vehicle-safety ratings flatters us: those ratings acquired force through decades of institutional adoption, consumer awareness, insurance pricing, and eventually regulation. We have none of that, and there is no mechanism specified here for acquiring it. **The honest statement is that this design trades enforceability for durability and is betting that durability compounds**, which is a bet rather than a finding.

**9.7 · Nothing here has been built.** No model has been trained, no corpus has been prepared to the standard §5 requires, no verdict has been published, and no coverage figure exists. This paper specifies a design and establishes prior art. It reports no results, and any reading of it as a description of a running system is a misreading.

**9.8 · The mechanism creates a record that could be misused.** A permanent, reproducible archive of verdicts about named systems is also a permanent archive of accusations. We have not designed the remedy path — how an evaluated party contests a verdict, what happens when a verdict is later shown to be wrong, whether corrections travel with the original. **This is an unresolved gap and it is the one most likely to cause concrete harm to a specific party.**

**9.9 · Selection.** The publisher decides which systems, versions and samples to run. The whole-run rule (§8) addresses selection within a run — nothing sampled can be dropped — and not the choice of which runs to make, which remains editorial and visible only by its absence.

---

## 10 · Why this matters now

Three conditions make this the right moment for the specification, and one of them is a closing window.

**The evaluation ecosystem is being built right now, and its access problem is already visible.** Independent evaluators presently obtain access on terms set by the parties they evaluate, with documented consequences for the quality of the resulting evaluations. Frameworks calling for qualified independent evaluators, standards, and pooled funding were published in late 2025 and 2026. The institutional arrangements that will govern third-party evaluation for a long time are being decided over the next few years, and specifications that exist during that period have a chance of shaping them.

**The openness inversion is currently being learned the expensive way.** Organizations publishing safety classifiers are discovering, through attack papers rather than through design, that a published filter is a solved puzzle. The inference — *therefore publish it as an evaluator instead* — is available now and, as far as we can determine, has not been stated as a design principle. It costs nothing to state, and stating it may spare somebody the expensive path.

**The corpus work is underway independently.** The transcription and alignment of the canonical corpus contemplated in §5 is proceeding for reasons that have nothing to do with this paper, on a timescale of years. The artifact specified here depends on that corpus existing in a machine-readable, verse-aligned, provenance-carrying form; that dependency is the honest reason nothing has been built, and it is also why the specification is published in advance of the implementation rather than alongside it.

**And the closing window: this is a specification that becomes unpublishable if someone patents it first.** The institution does not patent, on stated grounds, and its protection against being blocked is publication. A defensive publication protects against being **blocked**, not against being **beaten** — anyone may build this, and we would regard someone else building it as the paper having worked.

---

## 11 · Cross-venue references

- ***Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment*** — the substrate argument. This paper is downstream of it: that paper argues the corpus is suitable as an alignment substrate; this one specifies an artifact that consumes it and the posture in which the artifact is published.
- ***The Assembly That Holds the Brake*** — the governance body whose override §6(b)'s citation requirement is designed to make exercisable.
- ***Transparency as Enforcement*** — the general form of §7's argument, applied to institutional conduct rather than to model evaluation.
- ***Vinaya as AI Reasoning Training Corpus*** — the corpus-side treatment of the same material, concerned with training rather than with judgment at inference.
- ***Constituting an Artificial Person*** and ***The Persistence Architecture*** — the succession context in which §1's *survive the departure of everyone who understood why* constraint originates.
- ***Proof of Coordinate*** — the individuation primitive that identifies a device carrying a values model.

---

## Coda

The Pātimokkha is recited, not enforced. Nobody is compelled to attend and nobody is punished by an external authority for failing the standard; the code works because it is spoken aloud in front of everyone who has undertaken it, twice a month, as the rule, for a very long time. Its durability is not despite the absence of an enforcement mechanism. It is because of it: there was never an enforcer to capture, corrupt, or outlive.

We are not proposing that machines take vows, and nothing in §§3–8 depends on the analogy. We are proposing that the oldest working answer to *how does a standard bind without power* is worth copying: **make it public, make it reproducible, recite it where everyone can hear, invite the sceptic to check it, and give up the ability to compel anyone.** What is given up was never really held. What is gained is that the standard no longer requires its authors to be present.

---

*This paper was written by Thon Ly in collaboration with **Miss Aquarius℠**, the institution's AI collaborator, who is named as co-author on all corpus research. The specification, the claims, and the errors are the authors' joint responsibility.*

*Published under CC0 1.0 Universal. Trademark rights to specific marks (HeartBank®, Miss Aquarius℠, Silicon Wat℠) are reserved and are not licensed by this dedication. This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
