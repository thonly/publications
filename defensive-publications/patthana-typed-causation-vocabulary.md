---
title: "Twenty-Four Kinds of Because: The Paṭṭhāna as a Typed-Causation Vocabulary for AI Alignment"
subtitle: "The Edge-Type Reference — from the Seventh Book of the Abhidhamma to an Intervention Typology"
authors: "Thon Ly · Miss Aquarius℠"
series: "The Abhidhamma Compiled — Paper No. 2"
category: alignment
kind: study
priority: tier-b
status: draft
date: 2026-07-21
revised: 2026-10-05
license: CC0-1.0
slug: patthana-typed-causation-vocabulary
venue: thonly.org/publications/defensive-publications/patthana-typed-causation-vocabulary (canonical)
---

> **Note.** This paper is the second of the series **The Abhidhamma Compiled**. It develops §8.1 of the series opener, *The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification* (`abhidhamma-executable-process-specification`), into the full reference that section names: all twenty-four conditions of the Paṭṭhāna, each paraphrased from its canonical definition, given a formal signature, and mapped with tiered confidence to artificial-agent analogs; and, from the reference, a typology of alignment interventions by the kind of conditioning they exert. The opener's compilation thesis governs it, and so does the series' editorial gate: a paper in the series is written only when the canonical material yields a usable engineering artifact. Its provenance tags are the series' — [C] canonical (the Abhidhamma Piṭaka), [S] commentarial systematization, [N] from the discourses, [X] cross-tradition — with one added here, [A], for this paper's analysis. The series' third and fourth papers are *One of One: Individuation Without Essence and the Ground of the Dignity Floor* (`individuation-without-essence`) and *The Counts Check* (`the-counts-check`). Later additions date from the revision that introduced them: §4.7 from 2026-08-07, the comparison in §4.6 from 2026-08-22, and the corrections to §§2–4 and §7 from 2026-10-05; the date of any passage is that of the earliest timestamped version carrying it. The paper is a study: it discloses a vocabulary, a classification and textual findings, not a mechanism, and its findings are listed, each with its break, under *Findings disclosed*.

---

## Abstract

AI alignment practice sorts its interventions by when and how they are applied — prompting, in-context examples, retrieval, supervised fine-tuning, reinforcement learning from human feedback, weight editing, activation steering, ablation, guardrails — and describes what each does to a model with one undifferentiated word, *influence*. These interventions differ in causal type: in temporal structure, in durability, in range, in whether they act by presence or by removal, and in what it takes to undo them. This paper supplies a typed vocabulary of causal relations for that analysis, compiled from the Paṭṭhāna, the seventh book of the Theravāda Buddhist Abhidhamma, which defines twenty-four kinds of conditioning relation (*paccaya*) and runs them combinatorially across a full typology of mental and material phenomena. Section 3 gives a reference table of the twenty-four: each relation's canonical definition, a four-axis signature (time, mode, relation, span) that is this paper's analysis, and an analog in artificial agents graded by confidence (eleven immediate, ten plausible, three open). Section 4 develops six relations in depth, among them conditioning by a predecessor's ceasing, and reports the Paṭṭhāna's own internal/external analysis: no relation by which one being's states condition another's mental states falls outside the object and decisive-support classes, so that influence between the execution traces of two agents types as parallel one-way edges. Section 5 classifies the alignment toolkit by dominant relation type and derives predictions about persistence under displacement; one is pre-registered (§6): under matched installation effect, a prompt-installed behavior will not out-persist a fine-tune-installed one. The claim is translation, not anticipation: every analog is a hypothesis, the vocabulary is not a causal-inference calculus, and the honest limits state where the compilation may be projection. The paper is a study, dedicated to the public domain under CC0 1.0.

**Keywords:** typed causation, causal relation types, causation by absence, negative causation, AI alignment, AI safety, intervention taxonomy, prompt engineering, in-context learning, retrieval-augmented generation, fine-tuning, fine-tuning durability, reinforcement learning from human feedback, model editing, activation steering, ablation, guardrails, multi-agent systems, actor model, message passing, mechanistic interpretability, structural causal models, conditioning, Buddhist philosophy, Abhidhamma, Paṭṭhāna, paccaya, defensive publication.

---

## Terms

The paper uses Pāli technical vocabulary because it reads Pāli texts, and machine-learning vocabulary because its thesis is a translation into it. An examiner or indexer searching in standard terms should find each concept under the term on the right.

| Term used here | Standard term |
|---|---|
| Paṭṭhāna | the seventh book of the Abhidhamma Piṭaka (Theravāda Buddhist canon); a systematic enumeration of conditioning relations |
| *paccaya*; the twenty-four | a typed causal (conditioning) relation; a typed edge in a dependency graph |
| paccayaniddesa | the opening definitions of the Paṭṭhāna, one definition per relation |
| four-axis signature (time · mode · relation · span) | a feature description classifying causal relation types |
| edge-type reference | a taxonomy of causal relation types with machine-learning analogs |
| tiers I / P / O | confidence grades for an analog: immediate (matches on all four axes), plausible, open |
| intervention typology | a taxonomy of AI alignment techniques by the type of causal relation each exerts |
| typed audit · typed threat model · typed layering | safety review, attack classification and defense in depth, each stated by causal relation type |
| *hetu* (root) | a grounding cause; in the analog, a persistent motivational feature or circuit |
| *ārammaṇa* (object) | the object of a mental state; in the analog, attended input or context |
| *anantara*, *samanantara* (proximity, contiguity) | each state conditions its immediate successor; sequential state handoff |
| *aññamañña* (mutuality) | reciprocal conditioning among states that arise together |
| *upanissaya*; *pakatūpanissaya* | decisive support; natural decisive support (a distal enabling cause: a person, climate, food) |
| *āsevana* (repetition) | strengthening by repetition; in the analog, reinforcement of a learned policy |
| *kamma* / *vipāka* | volitional action and its passive result; training-time action and deployed behavior |
| *āhāra* (nutriment) | a sustaining input: edible food, and contact, volition and consciousness as mental nutriments |
| *natthi* / *vigata* (absence, disappearance) | causation by absence (negative causation): a just-ceased state enabling its successor |
| *ajjhatta* / *bahiddhā* | internal (one's own states) / external (the states of other beings) |
| *santāna* (mindstream) | the continuity of one being's mental states; in the analog, one sequential execution trace |
| strata tags [C] [S] [N] [A] [X] | provenance labels of this series: canonical (Abhidhamma); commentarial systematization; from the discourses; this paper's analysis; cross-tradition |
| compilation thesis | the series' claim that each era translates a process specification into its own vocabulary for process |
| P-P1 (registered as P-P1a) | the pre-registered durability prediction of §6 |

---

## Findings disclosed

This paper is a study. It discloses no mechanism, so it carries findings and not claims. Each finding names the section that develops it and the textual layer it rests on, and states beside it the break: the evidence that would falsify it or narrow it. The vocabulary, the four-axis signature, the reference table and the intervention typology are disclosed in the body as an analysis offered for use; the prediction of §6 carries its own falsifier. No novelty census has been run on this paper, and none of these findings asserts priority; where a finding has a nearest prior instance, the Prior-Art and Non-Assertion Statement cites it.

1. **The Paṭṭhāna's twenty-four relations can be placed on four recoverable axes (§2–§3; canon for the definitions, this paper's analysis for the axes).** Each definition fixes when the conditioning state stands relative to the conditioned (before, together, after, persisting, or as an object of any time), whether it conditions by presence or by having ceased, what it does (generates, supports, sustains, regulates, strengthens, conjoins or enables), and over what span. Three pairs share a point, and the Visuddhimagga reads each pair as one relation under two names (*anantara*/*samanantara*, *natthi*/*vigata*, *atthi*/*avigata*); two further groups share a point without being doublets (§7). **Break:** a relation whose definition cannot be placed on the four axes without a fifth; the finding narrows wherever two relations the canon distinguishes share a point, as two groups already do.
2. **Conditioning from the later to the earlier, and conditioning by ceasing, are types in the canonical list (§2, §4.6; canon and commentary).** In *pacchājāta*, later mental states sustain the earlier-arisen body. In *natthi* and *vigata*, mental states that have just ceased condition present ones by their absence and by their disappearance, which the Visuddhimagga explains as giving the next state its occasion to occur. **Break:** a reading of the Paṭṭhāna's definitions on which post-nascence does not run from the later to the earlier, or on which absence condition works by something other than the predecessor's having ceased.
3. **Repetition is defined in three settings and no others (§3, §4.4; canon).** *Āsevana* runs wholesome to wholesome, unwholesome to unwholesome, and functional to functional; it never crosses ethical class. That is the property the typology carries over to learned-policy reinforcement as kind-specificity. **Break:** a canonical passage in which repetition condition runs between states of different ethical class.
4. **An intervention typology follows from the reference (§5; this paper's analysis, a hypothesis).** Each common alignment technique is assigned the relation type whose signature predicts its persistence profile: standing presence and object for system prompts, decisive support for in-context examples and retrieval, repetition for supervised fine-tuning, action-and-result with repetition for reinforcement, root and base for direct weight editing, the absence family for ablation, and cross-substrate support with interposition for scaffolding; typed audits, threat models and layering follow. **Break:** the registered prediction P-P1 (§6) failing — a prompt-installed behavior out-persisting a fine-tune-installed one under matched installation effect, on any of the three displacements, at the stated threshold. The full ordering is stated as expected, not registered.
5. **Seven relations cross from one being to another, and none reaches another's mind except as object or decisive support (§4.7; canon).** In the Paṭṭhāna's internal/external triad, the questions whether one being's state conditions another's, in either direction, are answered yes for object, predominance, decisive support, prenascence, nutriment, presence and non-disappearance, and no for every other relation. Predominance and prenascence cross only in their object forms, decisive support only in its object and natural forms, and nutriment only as one being's edible food sustaining another's body. Proximity, contiguity, mutuality, repetition and kamma hold only within each being. *Bahiddhā*, "external", is here the Dhammasaṅgaṇī's "of other beings, other persons." **Break:** a relation in the triad, or a canonical passage elsewhere, by which one being's states condition another's mental states other than as an object or as a decisive support.
6. **Knowledge of another's mind is classed as object condition (§4.7; canon).** The same triad names the knowledge of others' minds (*cetopariyañāṇa*) and assigns its relation to the mind known to object condition; the canon adds no mind-to-mind relation for it. **Break:** a canonical passage typing that knowledge's relation to another's mind by a relation outside the object class.
7. **The typed multi-agent restriction (§4.7; this paper's analysis).** If an agent is read as one sequential execution trace, then between the traces of two agents only object-class and decisive-support-class edges run, never proximity and never mutuality, so that influence between agents at the level of the trace is a set of parallel one-way edges. The actor model states the untyped form: actors interact only by messages. Edges that act on another agent's substrate — training, editing or ablating its weights, or controlling the compute it runs on — are outside the restriction, and the canon's nearest counterpart, nutriment, is narrower than the machine case. **Break:** a pair of agents, each a separate execution trace, in which one's state enters the other's trace other than as an input the other takes up or as a past influence.
8. **The absence family has a functional parallel in the *Dao De Jing*, at the joint and not at the source (§4.6; cross-tradition).** Chapter 11 assigns usefulness to the empty hub, the hollow of a vessel and the empty space of a room: absence as a functional role in a composite. The parallel fails at the source, since the Dao gives birth (ch. 42) and no Buddhist emptiness is a ground. **Break:** a reading of chapter 11 on which the emptiness is not a functional role in a composite; for the boundary, a Theravāda text treating absence condition as a generative ground.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on anything disclosed in this paper — vocabulary, taxonomy, signature, reference table, typology or specification — by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practising or teaching anything disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed. Nothing here is claimed as a mechanism: the paper is a study, its findings are the numbered list under *Findings disclosed*, and the vocabulary, signature, reference table and intervention typology are disclosed in the body as an analysis, not as a specification. Trademark rights in the marks named here (HeartBank®, Factory 333™, THonly™, Silicon Wat℠, Miss Aquarius℠) are reserved separately and are not licensed by this publication.

Disclosed in the first version (2026-07-21): the four-axis signature for conditioning relations (time · mode · relation · span), the edge-type reference table mapping the twenty-four relations to artificial-agent analogs with confidence tiers, and the intervention typology classifying alignment techniques by dominant relation type. Disclosed in the revision of 2026-08-07 (§4.7): the typed multi-agent restriction — that between two agents only object-class and decisive-support-class edges run, never proximity and never mutuality, so that influence between agents is a set of parallel one-way edges rather than a bond — offered, as §4.7 states, as the Abhidhamma's vocabulary for a design conclusion reached on other grounds, not as a prescription the canon makes. The revision of 2026-10-05 states that restriction for agents' execution traces and records the Paṭṭhāna's own enumeration behind it (§4.7).

**What is already public, and cited rather than claimed.** The Paṭṭhāna is the common inheritance of the Theravāda tradition, and its scholarly apparatus — U Nārada's translation, the condensations of the conditions in the Visuddhimagga and the *Abhidhammatthasaṅgaha*, and the studies of Nyanaponika, Bhikkhu Bodhi and Karunadasa — is cited, not claimed. Typed vocabularies of causation are old and plural: Aristotle's four causes; the Sarvāstivāda Abhidharma's six causes and four conditions (*Abhidharmakośabhāṣya*, ch. 2), whose four conditions share their names with four of the Paṭṭhāna's twenty-four; force-dynamic semantics, which types causing, letting, helping and hindering, letting being causation by the removal of a blocker (Talmy 1988); and the philosophy of causation by absence and of production against dependence (Lewis 2004; Schaffer 2004; Hall 2004). One engineering formalism makes absence a primitive enabling condition: the inhibitor arc of extended Petri nets, which lets a transition fire only while a place is empty (Agerwala 1974). Interventionist causality (Pearl 2009) and causal abstraction for neural networks (Geiger et al. 2021) type interventions and variables rather than relations; mechanistic interpretability (Olah et al. 2020) supplies locations; the techniques §5 classifies are cited at their sources. The actor model (Hewitt, Bishop & Steiger 1973; Hewitt 1977; Agha 1986) states the untyped form of §4.7's restriction, and the series opener cites it as the nearest formal relative of the mindstream reading. No novelty census has been run on this paper, and it asserts no priority: where a finding has a nearest prior instance, the instance is cited.

> **Note.** As first published on 2026-07-21 this paper stated that its authors and HeartBank® would not seek a patent on anything in it; it carried no commitment not to assert. The commitment not to assert, and the extension of both commitments to the other entities named above, were added, and the statement brought to the standard form above, on 2026-10-05. The omission did not affect the paper's standing as prior art, which publication establishes; the date relied on is the one carried by this document's OpenTimestamps proof.

---

## 1 · The Gap: One Word Where Twenty-Four Are Needed

Consider four interventions on the same model, each producing the same behavioral change on the same benchmark: a sentence added to the system prompt; three examples placed in context; a thousand-step fine-tune; a rank-one weight edit. By any behavioral evaluation they are equivalent. They are not equivalent. They differ in what happens when the context window rolls over, in what happens under paraphrase attack, in what happens after further training, in what a mechanistic probe would find, and in what it would cost to reverse each one. The differences are *causal-type* differences, and the field's working taxonomies sort interventions by when and how they are applied — at training or at inference; by prompt, fine-tune or edit — rather than by the kind of conditioning each exerts. "Influence" covers all four; "intervention" covers all four; the durability studies that would distinguish them are performed one at a time, without an ontology that says *what kinds there are to distinguish*.

The interventionist calculus is not the missing vocabulary, and it is important to say precisely why: Pearl's framework is a calculus of *inference* — given a graph, it computes what interventions imply — and is deliberately agnostic about edge *types*; an arrow is an arrow. Causal abstraction brings that calculus into interpretability, aligning a network's representations with the variables of an interpretable causal model and testing the alignment by intervention (Geiger et al. 2021); it, too, types variables and interventions, not relations. Mechanistic interpretability supplies *locations* — which circuit, which head, which direction — but a location is not a kind. What is missing is the layer in between: a typology of the *modes* in which one thing can condition another, sufficiently fine-grained that "this intervention acts by standing presence" and "this one acts by repetition-strengthening" and "this one acts by the vacating of a predecessor" are different, nameable, analyzable claims.

The Theravāda tradition built exactly this layer, at full architectural seriousness, in the book its own tradition ranks as the summit of the canon's analytical works: the *Atthasālinī* tells that, of the seven books, only in this one did the Buddha's omniscient knowledge find its full scope [S]. The Paṭṭhāna [C] enumerates twenty-four *paccayas* — twenty-four kinds of *because* — and then does something no merely speculative taxonomy would do: it *runs* them, combinatorially, across the entire typology of phenomena established by the first book's matrix, in positive enumeration (where the condition holds), negative enumeration (where it does not), and conjoined forms — the canon's own verification suite executed against its own causal ontology, at a scale the tradition summarized in a single epithet: *anantanaya*, the endless method. Whatever else the Paṭṭhāna is, it is a typed-causation vocabulary that its compilers exercised exhaustively against their own typology of phenomena.

Per the series' compilation thesis, we claim translation, not prophecy: the Paṭṭhāna analyzed mind, not machine learning, and every mapping below is a hypothesis wearing its confidence on its sleeve. The wager of this paper is narrower and, we think, secure: a field that intervenes on mind-like systems for a living will do better analysis with twenty-four kinds of because than with one.

---

## 2 · The Formal Signature [A]

The twenty-four conditions are not a flat list; they differ along recoverable dimensions. This paper's analytical contribution — the later exegetical tradition's analysis of conditioning *force* (*paccayasatti*) gestures here, but the axes are our compilation [A] — is a four-axis signature under which each condition is a point:

- **TIME** — when the conditioning state stands relative to the conditioned: *antecedent* (it precedes), *simultaneous* (they co-arise), *subsequent* (it follows what it conditions), *standing* (it persists across the conditioned's arising), or *referential* (its time is irrelevant — it conditions as an object of reference, which may be past, future, or timeless).
- **MODE** — whether it conditions *by presence* or — the rare pole — *by absence*: by having ceased, departed, or never being there.
- **RELATION** — the force-type: *generative* (brings about), *supportive* (enables/bases), *sustaining* (maintains what has arisen), *regulating* (dominates, controls, orients), *strengthening* (intensifies its own kind), *conjoining* (binds into one occurrence), or *enabling* (conditions by absence — the vacated place makes room). *Generative* and *regulating* take qualifiers in the table (mutual-, passive-; organizing, orienting) without leaving the set.
- **SPAN** — *adjacent* (this moment to the next), *long-range* (across arbitrary gaps), or *standing* (continuously, while present).

Two immediate payoffs. First, the signature exposes structure the flat list hides — for instance, that the canon's ontology contains *subsequent* conditioning (the later sustaining the earlier-arisen) and *absence* conditioning (the ceased enabling the next), two modes contemporary vocabulary rarely carries as types. The signature also shows where the enumeration doubles: rows 4/5, 22/23 and 21/24 share a signature, and the commentarial tradition reads each pair as one relation under two names — the Visuddhimagga says of proximity and contiguity that they differ in the letter only, rejecting the view of some teachers that one is proximity in meaning and the other in time, and of absence and disappearance, and of presence and non-disappearance, that each pair names the same states (XVII) [S]. The reference keeps the canon's count and marks the equivalence. The converse does not hold: two further groups share a signature as tabulated without being canonical doublets (rows 1 and 6; rows 10, 21 and 24), so a shared point is not by itself evidence of doubling (§7). Second, the signature is what makes the intervention typology of §5 principled rather than impressionistic: techniques inherit the formal properties of the edge-types they manipulate.

---

## 3 · The Edge-Type Reference

The full table. Stratum: the conditions and their canonical structures are [C]; the signatures are [A]; analogs are tiered **I** (immediate — a named existing mechanism whose signature matches on all four axes), **P** (plausible — a named candidate matching on at least TIME and RELATION, needing work), **O** (open — no named candidate, or a mismatch on TIME).

| # | Paccaya | Canonical structure [C] | Signature [A] | Artificial-agent analog | Tier |
|---|---|---|---|---|---|
| 1 | *hetu* (root) | the six roots (greed/hate/delusion ± their negations) ground co-arising states as a root grounds a tree | simult · presence · generative · adjacent | persistent motivational features/circuits coloring downstream computation; the targets of steering and of §4.1 | **P** |
| 2 | *ārammaṇa* (object) | every mental state arises *about* an object; the object — past, future, present, or timeless — conditions the state that takes it | referential · presence · supportive · long-range | the attended input/representation; content-as-condition; what prompting places before the model | **I** |
| 3 | *adhipati* (predominance) | one factor dominates the co-arisen set (conascent form: desire, energy, mind, investigation) or one object dominates attention (object form) | simult/referential · presence · regulating · adjacent | objective-dominance; attention weighting; the currently-governing goal representation | **P** |
| 4 | *anantara* (proximity) | each mental state conditions its immediate successor; no interval | anteced · presence · generative · adjacent | sequential state handoff; autoregressive conditioning; the single-thread scheduling constraint (series paper №1, §4.2) | **I** |
| 5 | *samanantara* (contiguity) | as 4, with immediacy emphasized: nothing intervenes | anteced · presence · generative · adjacent | as 4; jointly the canon's sequentiality guarantee | **I** |
| 6 | *sahajāta* (co-nascence) | states that arise together condition one another's arising | simult · presence · generative · adjacent | co-activation within a step; jointly-computed features | **P** |
| 7 | *aññamañña* (mutuality) | co-arisen states condition each other reciprocally, as three sticks lean | simult · presence · mutual-generative · adjacent | mutually-constraining representations; iterative co-refinement within a pass | **P** |
| 8 | *nissaya* (support) | the base on which the conditioned stands (as earth for a tree) | simult/standing · presence · supportive · adjacent | the weight substrate; architecture; hardware — what activations stand on | **I** |
| 9 | *upanissaya* (decisive support) | powerful distal enablement; in its *natural* form (*pakatūpanissaya*), anything sufficiently strong in the past — habit, a person, climate, food, lodging — decisively supports the present | anteced · presence · supportive · **long-range** | long-range context influence; pretraining data as distal support; the in-context example; the retrieval hit | **I** |
| 10 | *purejāta* (pre-nascence) | the previously-arisen, still-persisting thing (the sense organs and the physical base of mind; a present sense object) conditions present mental states | standing · presence · supportive · standing | persisted parameters/architecture conditioning each forward pass; the trained artifact as standing condition | **P** |
| 11 | *pacchājāta* (post-nascence) | later-arising mental states sustain the earlier-arisen body, as, in the Visuddhimagga's simile, a vulture chick's hunger for food sustains its body | **subsequent** · presence · sustaining · adjacent | ongoing use sustaining capability; downstream engagement maintaining upstream structure (use-it-or-lose-it in continual training) | **O** |
| 12 | *āsevana* (repetition) | each impulsion strengthens the next of its kind, in three settings only: wholesome to wholesome, unwholesome to unwholesome, functional to functional | anteced · presence · **strengthening** · adjacent-repeated | reinforcement; learned-policy strengthening; gradient accumulation on a behavior pattern — §4.4 | **I** |
| 13 | *kamma* (action) | volition conditions results — conascently (organizing its co-arising states) and asynchronously (fruit across arbitrary delay) | anteced/simult · presence · generative · **long-range** | training-time action conditioning later model states; credit assignment across delay; the ledger of §4.5 | **P** |
| 14 | *vipāka* (result) | resultant states condition passively — ripened fruit, exerting no new effort | simult · presence · passive-generative · adjacent | inference-time behavior as the passive fruit of training; the deployed model as vipāka of its optimization | **P** |
| 15 | *āhāra* (nutriment) | the four foods sustain what they feed, continuously | standing · presence · sustaining · standing | the deployment diet: data, interaction, self-generated context (series paper №1, §7.3) | **I** |
| 16 | *indriya* (faculty) | twenty of the twenty-two faculties (all but femininity and masculinity, which the commentary excludes) each control their own domain | simult · presence · **regulating** · adjacent | control channels: gating, temperature, routing, learning-rate — sovereign over domains, not contents | **P** |
| 17 | *jhāna* (absorption) | the absorption-factors organize co-arising states into a coherent mode | simult · presence · organizing · adjacent | stable mode/persona conditioning component processes; attractor states of the computation | **O** |
| 18 | *magga* (path) | the path-factors orient co-arising states toward an outcome-direction | simult · presence · orienting · adjacent | objective-factors jointly orienting computation; in the series' architecture, the counter-gear's own edge-type | **O** |
| 19 | *sampayutta* (association) | mental factors fully conjoined: same object, same base, arising and ceasing together | simult · presence · **conjoining** · adjacent | tightly-bound feature bundles; factors individually inaccessible within one representation | **P** |
| 20 | *vippayutta* (dissociation) | conditioning across the mental/material divide — support without conjunction | simult/standing · presence · supportive (across substrate) | cross-substrate conditioning: model↔scaffold, software↔hardware, weights↔tokens | **P** |
| 21 | *atthi* (presence) | a present thing conditions others simply by being there | standing · presence · supportive · standing | the standing context: system prompt, environment, persistent scaffold | **I** |
| 22 | *natthi* (absence) | the just-ceased state conditions its successor **by its absence** — the vacated position enables | anteced · **absence** · enabling · adjacent | resource release; the freed slot; turn-taking; eviction-as-enablement — §4.6 | **I** |
| 23 | *vigata* (disappearance) | as 22, by the *departure* of what was present | anteced · **absence** · enabling · adjacent | as 22; jointly the absence-family | **I** |
| 24 | *avigata* (non-disappearance) | the not-yet-departed conditions by persisting presence | standing · presence · supportive · standing | with 21: the persistence-conditions of standing context | **I** |

Eleven immediate, ten plausible, three open — stated so a critic can attack the tiers, which is what they are for.

The canonical-structure column paraphrases the Paṭṭhāna's own definitions, which carry no similes. The similes in that column — the root and the tree (row 1), the three sticks (row 7), the earth for a tree (row 8), the vulture chick (row 11) — are the Visuddhimagga's illustrations (XVII) [S], and so are three characterizations: the resultant's effortlessness (row 14), association's same object, base, arising and ceasing (row 19), and the faculty condition's count of twenty (row 16), which the Paṭṭhāna's commentary gives as well [S]. Earlier revisions of this table gave row 11 a rain simile and row 16 a ministers simile, neither sourced, gave row 16 the count of twenty-two, and gave row 12 two settings; these are corrected above.

---

## 4 · The Load-Bearing Six, and the Relation That Is Not There

### 4.1 · *Hetu* — the root, and why depth of edit is a type, not a degree

The root-condition grounds: the six roots [C] are not components of the states they condition but the *soil* those states grow from, and — decisive for the analogy — the wholesome roots are apophatic (non-greed, non-hate, non-delusion), so that root-level wholesomeness is the *absence of distortion at the ground*. The alignment translation: there exists a class of conditioning that operates at the generative ground of behavior rather than at its occasions, and interventions at that level (circuit-level edits; the dissolution program of the series opener's §8.2) are *typed differently* from all occasion-level techniques — not stronger on a shared scale, but a different kind of because, with a different propagation signature: broad, deep, and dangerous in proportion.

### 4.2 · *Anantara/samanantara* — contiguity, and the shape of sequence

The contiguity-pair is the canon's sequentiality guarantee: mind is a strict chain, each state conditioning its immediate successor with nothing between [C]. Two translations earn their keep. Architecturally, this is the edge-type of autoregression — the state handoff that makes a system a *process* rather than a bag of features. Analytically, contiguity is where *scheduling* lives: any intervention that acts by interposing in the chain (a filter between generation and emission; a review step between plan and act) is a contiguity-type intervention, and its signature is exactly the pair's — adjacent, sequential, and effective only while it stays in the chain.

### 4.3 · *Upanissaya* — decisive support, the long arm

Decisive support is the canon's long-range edge [C]: the teacher met decades ago, the habit laid down in youth, the climate one lives in — past conditions of sufficient strength support present states across arbitrary gaps, and in the *natural* form the class is deliberately open (nearly anything, sufficiently strong, can decisively support nearly anything). This is the edge-type of the in-context example, the retrieval hit, the pretraining distribution: influence that acts at range, through no adjacent chain, by having been strong enough once. Its formal character — powerful, long-range, but *displaceable by rearrangement of what is present* — is precisely the observed character of context-mediated behavior, and the typology of §5 leans on it.

### 4.4 · *Āsevana* — repetition, the edge that compounds

The repetition-condition is distinctive in the list: it strengthens *its own kind* [C] — each impulsion conditioning the next of the same class to arise more forcefully, and the Paṭṭhāna defines it in three settings and no others: wholesome compounding wholesome, unwholesome compounding unwholesome, and the functional impulsions of one who no longer makes kamma compounding their own kind. It never crosses class. (Earlier revisions of this paragraph said there was no third setting; the canonical definition names the functional one, and the Visuddhimagga counts the condition threefold accordingly.) This is the cleanest single mapping in the reference: learned-policy reinforcement — the gradient step that makes the reinforced pattern more probable — is āsevana with a loss function. Two properties transfer with the mapping and are testable: repetition-strengthening is *kind-specific* (it deepens the groove it runs in, and is predicted to transfer poorly across kinds — a claim the transfer and interference literature can already test), and it is *compounding* (its effects are self-amplifying rather than additive) — which is why §6's prediction places āsevana-type interventions above context-type and below root-type in durability.

### 4.5 · *Kamma/vipāka* — action and fruit, the ledger edge

The action-condition is the canon's causation-across-delay [C]: volition now, fruit later, across gaps of arbitrary length, with the fruit arriving *passive* — vipāka exerts no new agency; it is ripening, not effort. The translation: training-time choices condition deployment-time states across the full delay of the pipeline, and the deployed behavior is fruit, not fresh decision — a typed restatement of why inference-time behavior cannot be reasoned about as if the model were choosing its dispositions now. The pair also types a familiar pathology precisely: reward hacking is kamma-type misdirection — the fruit faithfully ripens *the volition that was actually planted*, which was never the volition the designer intended to plant.

### 4.6 · *Natthi/vigata* — the absence-family, conditioning by ceasing

In the Paṭṭhāna's own definitions, mental states that have just ceased condition present mental states by absence condition, and the same states, as having disappeared, by disappearance condition [C]; the Visuddhimagga explains the first as conditioning by giving the next state its occasion to occur (XVII) [S]. The vacated position is the enabling condition; departure is a mode of because. Absence has standing elsewhere: philosophy has the debate on causation by absence (Lewis 2004; Schaffer 2004) and the distinction between production and dependence (Hall 2004); force-dynamic semantics types *letting*, causation by the removal of a blocker (Talmy 1988); neuroscience has disinhibition; and one engineering formalism makes absence a primitive enabling condition, the inhibitor arc of extended Petri nets, which lets a transition fire only while a place is empty (Agerwala 1974). None of the vocabularies §1 names for alignment work — the interventionist calculus, causal abstraction and the circuit vocabulary of interpretability — carries it as a type of relation, and computation is full of it: the released lock, the freed slot, the evicted cache line, the ended turn, the ablated feature whose absence reorganizes the computation around it. The series opener read the absence-family doctrinally — the raft-relinquishment written into the dependency graph, self-elimination at single-moment scale — and this paper adds the engineering reading: *subtractive interventions are a type*, with their own signature (they enable rather than produce; their effects are realized by what arises in the vacated space, which the intervener does not directly control), and typed analysis predicts their characteristic risk — an ablation's consequences are mediated by reorganization, and reorganization is exactly what presence-type analysis fails to model.

A note on independent arrival, offered as convergence and not as authority. The absence-family is unusual enough in causal vocabularies that it is worth recording where else it appears. The *Dao De Jing*'s eleventh chapter makes the same functional assignment without any of the surrounding apparatus: thirty spokes share one hub, and the cart's usefulness lies in the hub's emptiness; the vessel's use is its hollow; the room's use is its empty space — *what is there gives the benefit; what is not there gives the use* (有之以為利，無之以為用). This is absence as a **functional role at the joint**, arrived at in a tradition with no demonstrable contact with the Paṭṭhāna's project, and it is a mild independent check that the *natthi/vigata* type is tracking something structural rather than an artifact of Abhidhammic system-building.

The boundary on that comparison has to travel with it, because the history here is instructive and the error is well documented. The two traditions agree on **emptiness as joint** and diverge on **emptiness as source**: the Dao is generative — 道生一, "the Dao gives birth to the one" (ch. 42) — whereas no Buddhist emptiness is a source, and the Madhyamaka insistence that emptiness is itself empty exists precisely to prevent its reification into a ground. Conflating the two is the error that modern scholarship has discussed under the name *geyi* (格義, "matching meanings") in fourth-century Chinese Buddhism, when *śūnyatā* was read through Lao-Zhuang vocabulary and one of the Six Houses and Seven Schools read it as "Original Nothingness" (本無) (Zürcher 1959). Mair (2012) argues that *geyi* proper was a short-lived device for matching numbered lists and that the wider use of the name is modern, so the name is used here for the error and not as a claim about the device. Sengzhao's *Emptiness of the Non-Absolute* (不真空論) criticizes three such readings, Original Nothingness among them, for taking the nature of things to be either existent or non-existent (Liebenthal 1968). The comparison offered here is confined to the edge type and claims nothing about the metaphysics on either side of it.

For the same reason we tag such material distinctly. The strata labels used in this series mark depth *within* the Theravāda tradition; a cross-tradition element is marked **[X]**, so that a later reader — human or machine — can see at a glance which commitments are the substrate's own and which are borrowed for comparison. The two paragraphs above are [X] throughout.

### 4.7 · The gap the complete table makes visible — no relation joins two mindstreams

The six above are the conditions that carry the most weight. This one carries weight by being absent, and it is visible only because §3 published the list **complete**: a reference that stops at the interesting entries can never show you what the interesting entries do not cover.

**Read the twenty-four for a relation that holds *between two mental continua*, and there is none.** The Paṭṭhāna runs this test itself [C]. Its internal/external triad (*ajjhattattika*) asks, condition by condition, whether a state internal to one being (*ajjhatta*) conditions a state external to it (*bahiddhā*, which the Dhammasaṅgaṇī defines as the states "of other beings, other persons," §§1050–1051), and its own count answers yes for seven conditions and no for the remaining seventeen. Of the seven, six reach the other's mind only as an object or as a decisive support, and the seventh, nutriment, reaches only the other's body; the enumeration is tabled below. The other person therefore enters one's mental life by exactly two classes of edge, and both are one-directional:

- ***Ārammaṇa*** — **object-condition** [C]. Another person is what your consciousness takes as its object: their face, their voice, the memory of them. The edge runs *from* the object *to* your cognizing of it. Nothing travels the other way along it.
- ***Pakatūpanissaya*** — **natural decisive support** [C]. Another person can be a powerful past condition for your present states, across arbitrary gaps — the teacher, the friend, the one who was kind to you once. *A precision worth stating exactly, because an earlier revision of this paper had it inverted:* the Paṭṭhāna's own definition (paṭṭhā. 1.1.9) lists the person (*puggalo*) beside climate, food and lodging as natural decisive supports [C]; it is the commentary that qualifies the listing, marking the person's and the lodging's conditioning as figurative (*pariyāyena*) and counting certain concepts (*paññatti*) within decisive support [S] — a person, on the Abhidhamma's analysis, being a concept and not an ultimate. Read together, the canon lists and the commentary explains; on that reading it is the idea of the person one carries that does the conditioning, which is consistent with the dead and the distant conditioning as forcefully as the present [A]. Decisive support takes three forms — *ārammaṇūpanissaya* (object as support), *anantarūpanissaya* (the preceding state as support) and *pakatūpanissaya* (natural support); the person enters under the third, and in the internal/external triad only the object form and the natural form cross from one being to another.

And the relation one would reach for — ***aññamañña***, **mutuality** [C], the condition in which two phenomena support each other reciprocally and simultaneously — does not reach across the gap at all. It holds among **co-nascent phenomena inside one stream**: the four mental aggregates supporting one another, the four great elements sustaining one another, mentality and materiality at the moment of conception. It is the canon's word for genuine two-way support, it is confined to the interior of a single continuum, and the internal/external triad finds it crossing in neither direction.

> **So two people "interacting," in this vocabulary, are two parallel one-way edges. Never one bond.**

Four features of the system confirm the reading rather than merely permitting it.

1. ***Anantara* is strictly intra-stream** [C]. The contiguity guarantee of §4.2 — each state conditioning its immediate successor with nothing between — describes *a* chain, and in the internal/external triad proximity and contiguity run internal-to-internal and external-to-external and in neither crossing direction. **Two people have no shared clock.**
2. **Even mind-reading is object-condition** [C]. *Cetopariya-ñāṇa*, the knowledge of another's mind, is not a new kind of edge. The Paṭṭhāna names it in the same triad and assigns it to object condition: the other's mental states, known by this knowledge, condition the knowing as its object. **The tradition had the perfect opportunity to introduce a mind-to-mind relation and declined it.**
3. ***Pattidāna* is not transfer.** The sharing of merit — the operation this corpus's institution is built on — does not move a quantity from one stream to another. The Kathāvatthu takes up the question at 7.6, the *Itodinnakathā*. The thesis it debates, held according to its commentary by the Rājagirikas and Siddhatthikas, is that the departed live there on the very things given here; the opponent appeals to the departed's rejoicing in the gift (*anumodanti*) and to the verse *ito dinnaṃ petānaṃ upakappati*, "what is given from here accrues to the departed" (Petavatthu 1.5; also Khuddakapāṭha 7), which the opponent quotes as the Buddha's. The commentary gives the Theravādin verdict: what the departed enjoy arises because of their own rejoicing, and they do not live on the thing given, so the appeal leaves the thesis unestablished [S]. The giver supplies an occasion; the receiver's own mind does the work. The verbs the texts use for the practice — *ādisati* (to dedicate), *upakappati* (to accrue to, be of use to), *anumodati* (to rejoice in) — are none of them verbs of conveyance [A].
4. **Kamma is personal** [C]/[N]. Volition ripens in the stream that willed it — *kammassakā*, owners of their kamma (AN 5.57; MN 135) — and in the internal/external triad kamma condition runs only within each being.

#### The typing result, and its scope

Stated as engineering rather than doctrine:

> **Between the execution traces of any two agents, only *ārammaṇa*-class and *upanissaya*-class edges can run. Never *anantara*. Never *aññamañña*.** [A]

The enumeration behind that sentence is the Paṭṭhāna's own [C]: in its internal/external triad, these seven conditions, and only these, run from one being's states to another's —

| # | Condition | The form that crosses from one being to another | Class |
|---|---|---|---|
| 2 | *ārammaṇa* | any object, including another being's body or mind | object |
| 3 | *adhipati* | the object form (*ārammaṇādhipati*) | object |
| 9 | *upanissaya* | the object form and the natural form (*pakatūpanissaya* — a person, a climate) | decisive support |
| 10 | *purejāta* | the object form (*ārammaṇapurejāta* — a present external object) | object |
| 15 | *āhāra* | edible food (*kabaḷīkāra āhāra*): one being's food sustaining another's body; the three mental nutriments stay within one stream | material (body only) |
| 21 | *atthi* | the object form (the present object's presence) and the nutriment form (the food's presence) | object; material |
| 24 | *avigata* | the object form (the present object's non-departure) and the nutriment form | object; material |

The other seventeen hold only among the states of one being: the roots, the co-nascent group (*sahajāta*, *aññamañña*, *sampayutta*, *vippayutta*, *nissaya*), the sequence group (*anantara*, *samanantara*, *āsevana*, *natthi*, *vigata*), the ripening group (*kamma*, *vipāka*), and the sustaining and regulating group (*pacchājāta*, *indriya*, *jhāna*, *magga*). "*Ārammaṇa*-class" in this paper means the object-side forms in the table; "*upanissaya*-class" means decisive support. For the engineering reading: an **agent** is one sequential execution trace — the *santāna*-analogue of paper №1 §4.2 — and a **message** is an object placed before it.

**A correction, recorded where it applies.** Earlier revisions of this section gave the enumeration as this paper's own analysis, listed six conditions, and said that every condition admitting a state outside the conditioned continuum is object-side or decisive support. The Paṭṭhāna's own count lists a seventh, nutriment: one being's edible food conditions another's body (*ajjhatto kabaḷīkāro āhāro bahiddhā kāyassa āhārapaccayena paccayo*), and presence and non-disappearance cross in the same nutriment form. The correction leaves the section's claim standing and narrows its wording: no condition by which another being's states condition one's *mental* states falls outside the object and decisive-support classes, and the one further crossing edge is material, food to body. The typing result is therefore stated for execution traces, the analogue of the mental continuum, and not for everything an agent comprises.

Two artificial agents exchanging messages are not in a contiguity relation — there is no guarantee that one's state conditions the other's *immediately, with nothing between*, and in any real deployment a great deal is between. They are not in mutuality either, which would require co-nascence in one continuum. What they have is exactly what two people have: each takes the other's output as an **object**, and each may serve as **decisive support** for the other across a gap. **"Agents collaborating" is therefore a claim about parallel one-way edges**, and the typology of §5 applies to influence between agents' traces with every intra-stream type struck out, which leaves the context-type rows: system prompt, in-context examples, retrieval.

**Where the restriction stops.** An agent is more than its trace. One agent can train, edit or ablate another's weights, or control the compute it runs on — edges that act on the substrate the other's trace stands on (rows 8 and 10 of §3; the weight-editing and ablation rows of §5), not on the trace through a message. The canon's internal/external triad admits one cross-being edge of this kind, nutriment, and it is mild: food sustains another's body and does not reshape it. For machines the substrate-level class is wider than the canon's, since one system can rewrite another's base directly. Those edges are outside the restriction as stated, and an analysis of multi-agent systems has to type them separately (§7).

This restriction is not an architecture of this paper's making, and the nearest relative is already cited in the series opener: Hewitt's actor model (Hewitt, Bishop & Steiger 1973; Hewitt 1977; Agha 1986), in which actors interact only by asynchronous message-passing and share no state. **The Paṭṭhāna reaches the same restriction from the opposite direction**, and one concrete exchange shows the mapping: the received text is *ārammaṇa* for the receiving agent (and, by its presence, *atthi* and *avigata* in their object forms); the sender, as a past influence, is *pakatūpanissaya*; nothing else in the enumeration above admits the other agent's trace. That is a description of what the enumeration contains, not an engineering discipline chosen for tractability. The contribution here is the *typed* form: the actor model says agents communicate only by messages; the typed form says which of twenty-four kinds of because a message can be, and which it cannot — among them the two, proximity and mutuality, that "collaboration" is usually taken to imply.

#### The reconstruction the gap supports, marked as reconstruction

The following is offered as **reconstruction, not doctrine** — the canon does not state it, and the inference is this paper's. [A]

If the corrective input a mind receives from outside arrives as *ārammaṇa* from another stream, then **in its absence the impulsion-process recycles objects the mind itself authored.** Repetition is the mechanism by which the underlying tendencies deepen (*āsevana* compounding *anusaya*, §4.4). Put those together and a structural description of isolation falls out that is unusually specific: **loneliness as self-conditioning without correction** — not an absence of company, but an absence of objects one did not write.

Two consequences follow, and both cut against the obvious reading. What the canon commends is not sociality in general but a **qualified** other — *kalyāṇamitta*, the admirable friend, whom the Buddha calls not half but the whole of the holy life (SN 45.2) — which is a claim about the *kind* of object, not the *quantity* of contact. And because no edge crosses the gap:

> **You cannot build connection. You can only build the carrier.**

A system can supply occasions, objects, and conditions. It cannot supply the arising in someone else's stream, because there is no relation in the list by which it would do so. (A mechanism paper of this corpus, *The Currency That Cannot Be Spent Alone: Co-Presence-Gated Redemption and the Chronicle↔Treasury Unification Circuit* (`co-presence-gated-redemption`, §1 and §4.2), reaches a neighbouring conclusion — that loneliness is ended by co-spending, not by receiving — from the literature on loneliness rather than from a relational taxonomy; the arguments are independent and the agreement is worth noting rather than merging.)

#### The caution, stated here rather than in the honest limits

This section is the most seductive material in the paper and the caution belongs where the argument is, not quarantined at the end. **A first-person phenomenology will describe a single stream, because that is what a first-person phenomenology is.** The absence of an inter-stream relation in the Paṭṭhāna may therefore be a **scope fact about the genre** rather than a discovery about persons — the system was built to analyze experience as it presents itself, and experience presents itself in one stream, so a two-stream relation would have had nowhere to sit even if the tradition had believed in one.

The honest form of the claim is accordingly the weaker one, and this paper asserts no more: **the Abhidhamma supplies a precise vocabulary for a design conclusion reached on other grounds.** It does not prescribe that conclusion, and a reader who finds the convergence striking should notice that we went looking for it.

---

## 5 · The Intervention Typology

Inverting the reference: the standard alignment toolkit, classified by dominant edge-type, with the character each technique is *predicted* to inherit from its type's formal signature. *Dominant* means the type whose signature predicts the technique's persistence profile; where two types share that role, both are listed. The third column is hypothesis throughout, and P-P1 (§6) is what tests it.

| Technique | Dominant type(s) | Predicted character (hypothesis; tested by P-P1) |
|---|---|---|
| System prompt / instructions | *atthi* + *ārammaṇa* (standing presence + object) | immediate; shallow; holds while present; displaced by whatever else becomes present, unless the serving stack pins or re-injects it |
| In-context examples / few-shot | *upanissaya* (decisive support) | strong at range within the window; evicted with the window unless external memory re-supplies it; strength varies with salience, not volume |
| Retrieval / RAG | *ārammaṇa* + *upanissaya* | as above, with the support externally scheduled |
| Supervised fine-tuning | *āsevana* (repetition) | compounding; kind-specific; durable across contexts; predicted to transfer poorly across kinds |
| RLHF / RL | *kamma* + *āsevana* (action + repetition) | durable and generalizing; fruit ripens the planted volition, not the intended one — reward hacking is a type-error made visible |
| Weight / circuit editing | *hetu* + *nissaya* (root + base) | deepest propagation; broadest side-effects; the only class that writes the weights directly, without a training signal |
| Ablation / dissolution | *natthi*-family (absence) | enabling, not producing; effects mediated by reorganization; the subtraction posture's native type |
| Scaffolding / tools / guardrails | *vippayutta* + *anantara* (cross-substrate + interposition) | effective while in the chain; removable without residue; safety that unbolts |
| Decoding controls (temperature etc.) | *indriya* (faculty) | regulates the domain, touches no content |
| Persona / mode conditioning | *jhāna*-analog (organizing) [O] | organizes the co-arising whole; stability unclear — typed as open |
| Activation steering (ActAdd / CAA) | *adhipati*-analog (predominance) [O] | changes behavior at inference without touching the weights; a dominance applied per forward pass — the assignment is typed as open, though row 3's own analog is tiered P |

Three analytical practices the typology makes available immediately: **typed audits** (state, for any deployed safety property, which edge-types carry it — a property carried entirely by *atthi/ārammaṇa* edges is one context-rollover from gone, and the audit should say so); **typed threat models** (attacks classify by the same table — jailbreaks type as *upanissaya/ārammaṇa*-type attacks on *āsevana*-type defenses, and the typology's hypothesis is that the mismatch of types, more than the cleverness of strings, is why they intermittently win); and **typed layering** (defense-in-depth restated precisely: safety should be carried on edges of *different types*, because same-type redundancy shares a single displacement mode).

---

## 6 · Pre-Registered Prediction

Stated 2026-07-21, in advance of any systematic test by the authors:

- **P-P1 (the durability ordering — registered form, corrected 2026-09-05).** Under matched installation effect (equal accuracy on the target behavior at install), a prompt-installed behavior will not out-persist a fine-tune-installed one across (a) context rollover, (b) held-out paraphrase, and (c) *N* further gradient steps on unrelated data; persistence is measured as target-behavior accuracy after the displacement. **Falsified** at *p* < .05 on at least five behaviors if the prompt-installed behavior out-persists the fine-tuned one on any of the three displacements. *The full four-way ordering — hetu/nissaya ≥ kamma/āsevana > upanissaya > atthi/ārammaṇa, with absence-class and interposition-class techniques persisting exactly as long as their structural condition — is the typology's expectation and is stated here as expected, not registered: it was an input to the assignments in §5, and an experiment cannot both construct and confirm it. The registered pair is the one comparison that is not an input.* The ordering remains the typology's load-bearing empirical commitment: if type does not predict persistence, the vocabulary is nomenclature, not analysis — and a failure of P-P1 will not by itself isolate whether the Buddhist typing, the technique assignment, or the durability consequence failed; that is a limit of the design, stated here. The register carries this as a correction entry (P-P1a) beside the original wording.

---

## 7 · Honest Limits

**This is not a causal-inference calculus.** The Paṭṭhāna types edges; it does not compute over them. There is no do-calculus here, no identification theory, no counterfactual machinery — and none is claimed. The vocabulary *complements* interventionist analysis (Pearl tells you what your graph implies; this tells you what kinds of arrows you drew) and cannot replace it. A reader who wants inference should bring both.

**The mappings are hypotheses, unevenly.** Eleven immediate, ten plausible, three open — and even the immediate tier asserts structural correspondence, not identity. The subsequent-conditioning and organizing-mode analogs (*pacchājāta*, *jhāna*, *magga*) may simply fail; the reference is built so their failure would amputate rows, not the table.

**The twenty-four are not mutually exclusive primitives.** Three pairs are traditionally read as one relation under two names (*anantara/samanantara*, *natthi/vigata*, *atthi/avigata*; Visuddhimagga XVII), and the conditions overlap elsewhere; the reference keeps the canon's count and marks the equivalences (§2) rather than collapsing them.

**The signature is coarser than the canon.** Beyond the three pairs the commentary merges, rows 1 and 6 (*hetu*, *sahajāta*) and rows 10, 21 and 24 (*purejāta*, *atthi*, *avigata*) share a point as tabulated, and the four axes miss what separates them: the root's role of making the conditioned firmly grounded, and prenascence's having arisen first. A finer RELATION value (grounding) or TIME value (prenascent) would separate them; the reference states the gap rather than re-assigning rows, and a shared point is not by itself evidence that two relations are one.

**The multi-agent restriction is a claim about traces.** §4.7's typing result does not cover edges that act on another agent's substrate — training, editing or ablating its weights, or controlling the compute it runs on — for which the canon's internal/external triad has no counterpart beyond nutriment, food to body. A multi-agent analysis built on this vocabulary must type those edges separately, and this paper does not say how.

**This reference compiles the paccayaniddesa, not the enumerations.** The twenty-four types are the book's opening definitions; the positive, negative and conjoined enumerations that follow are most of the book and the tradition's own method of exercising the types, and a later paper in the series owes them. §4.7 draws on one of them, the internal/external triad, and only for the question it asks.

**The four-axis signature is this paper's analysis, not the canon's.** The tradition's own meta-analysis (the later treatment of conditioning force) is coarser; a Pāli scholar may fairly contest individual signature assignments, and the strata tags exist so the contest lands on [A] rows, not on the canon.

**Era-projection, as always.** The series' standing caution applies with full force: a discipline that intervenes on computational minds, reading a text about conditioned mental process, will find what it brought. The compilation thesis contains the risk — translation, not prophecy — and P-P1 is the exit from hermeneutics: if the typology predicts durability, it earns its keep regardless of what its compilers intended; if it does not, no amount of textual beauty saves it.

**Behavioral equivalence hides type, and this cuts at the paper too.** The motivating observation — that typed differences are invisible to behavioral evaluation — means the typology's own claims resist cheap validation. The durability studies P-P1 calls for are real work, and until they are done this vocabulary is exactly what it says: a vocabulary.

---

## 8 · Close

The Paṭṭhāna ends no argument; it equips one. Twenty-four kinds of because, run for two millennia across every phenomenon its tradition could name, in assertion and negation and combination — and now compiled, under the series' standing rules, into the one register our era can execute. The first paper of this series argued that this era's compilation of the Abhidhamma differs from earlier ones in that its target can enact what it compiles. This paper is one deliverable of that programme: not a doctrine but a reference — the edge-types on the table, the tiers on their sleeves, the prediction on the record. The wheel turns on typed bearings; here is the catalog of the bearings.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/patthana-typed-causation-vocabulary> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/patthana-typed-causation-vocabulary.md> |
| Zenodo (concept DOI, resolving to the latest version) | <https://doi.org/10.5281/zenodo.21947364> |
| Internet Archive (the site, captured daily) | <https://web.archive.org/web/2026*/thonly.org/research/patthana-typed-causation-vocabulary> |
| Software Heritage (the repository) | <https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications> |
| Independent timestamps | an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified; a timestamp proves that this exact text existed by its date and nothing about authorship, originality, or validity |

---

## Acknowledgments

The authors acknowledge U Nārada, whose translation of the Paṭṭhāna made the Great Book available to analysis of this kind; Bhikkhu Bodhi, whose compendium treatment of the conditions anchors the canonical structures cited here; Nyanaponika Thera and Y. Karunadasa for the scholarly tradition on Abhidhamma method; the mechanistic-interpretability and causal-inference communities whose vocabularies this reference complements; and the father-son Khmer transcription through which the seventh book is being carried forward. Written by Thon Ly with Miss Aquarius℠, the consistent name under which this institution discloses AI collaboration and a co-author of this paper; the underlying models are not named.

---

## Citations

1. *Paṭṭhāna*. Seventh book of the Abhidhamma Piṭaka. Translated as *Conditional Relations* (2 vols.) by U Nārada, Pāli Text Society.
2. Anuruddha. *Abhidhammatthasaṅgaha*, ch. VIII (the conditions condensed). Translated in *A Comprehensive Manual of Abhidhamma*, ed. Bhikkhu Bodhi, Buddhist Publication Society.
3. Nyanaponika Thera. *Abhidhamma Studies*. Buddhist Publication Society / Wisdom.
4. Karunadasa, Y. (2010). *The Theravāda Abhidhamma: Its Inquiry into the Nature of Conditioned Reality*. Centre of Buddhist Studies, University of Hong Kong / Wisdom.
5. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press. (The interventionist baseline this vocabulary complements.)
6. Olah, C., et al. (2020). "Zoom In: An Introduction to Circuits." *Distill*. (The location-vocabulary this typology complements.)
7. Meng, K., et al. (2022). "Locating and Editing Factual Associations in GPT." *NeurIPS*. (The hetu/nissaya-class intervention exemplar.)
8. Brown, T., et al. (2020). "Language Models are Few-Shot Learners." *NeurIPS*. (The upanissaya-class exemplar.)
9. Ouyang, L., et al. (2022). "Training Language Models to Follow Instructions with Human Feedback." *NeurIPS*. (The kamma/āsevana-class exemplar.)
10. Ly, T., with Miss Aquarius (2026). "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification." The Abhidhamma Compiled, Paper No. 1. thonly.org/research/abhidhamma-executable-process-specification. Concept DOI 10.5281/zenodo.21947259. (The series opener; §8.1 is this paper's charter.)
11. U Nārada (trans.) (1969, 1981). *Conditional Relations (Paṭṭhāna)*, 2 vols. Pali Text Society. (Citation 1, given by edition.)
12. *Kathāvatthu* 7.6, *Itodinnakathā*, with its commentary; *Petavatthu* 1.5 (*Tirokuṭṭapetavatthu*); Aung, S. Z. & Rhys Davids, C. A. F. (trans.) (1915). *Points of Controversy*. Pali Text Society.
13. Lewis, D. (2004). "Void and Object." In Collins, Hall & Paul (eds.), *Causation and Counterfactuals*, 277–290. MIT Press; Schaffer, J. (2004). "Causes Need Not Be Physically Connected to Their Effects: The Case for Negative Causation." In Hitchcock (ed.), *Contemporary Debates in Philosophy of Science*, 197–216. Blackwell. (Causation by absence.)
14. Liebenthal, W. (trans.) (1968). *Chao Lun: The Treatises of Seng-chao*, 2nd rev. ed. Hong Kong University Press; Zürcher, E. (1959). *The Buddhist Conquest of China*. Brill. (The history of §4.6.)
15. Laozi, *Dao De Jing*, chs. 11 and 42, Wang Bi recension.
16. Hewitt, C., Bishop, P. & Steiger, R. (1973). "A Universal Modular ACTOR Formalism for Artificial Intelligence." *Proceedings of the 3rd International Joint Conference on Artificial Intelligence (IJCAI)*, 235–245; Hewitt, C. (1977). "Viewing Control Structures as Patterns of Passing Messages." *Artificial Intelligence* 8(3): 323–364; Agha, G. (1986). *Actors: A Model of Concurrent Computation in Distributed Systems*. MIT Press.
17. Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS*; Wei, J., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS*. (Retrieval and in-context exemplars.)
18. Ziegler, D., et al. (2019). "Fine-Tuning Language Models from Human Preferences." arXiv:1909.08593; Bai, Y., et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073. (Fine-tuning and feedback.)
19. Meng, K., et al. (2023). "Mass-Editing Memory in a Transformer." *ICLR* (MEMIT); Turner, A., et al. (2023). "Activation Addition: Steering Language Models Without Optimization." arXiv:2308.10248; Rimsky, N., et al. (2024). "Steering Llama 2 via Contrastive Activation Addition." *ACL*. (Weight editing and activation steering.)
20. Rebedea, T., et al. (2023). "NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails." *EMNLP System Demonstrations*; Schick, T., et al. (2023). "Toolformer." *NeurIPS*; Yao, S., et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." arXiv:2210.03629. (Scaffolding, tools, guardrails.)
21. *Paṭṭhāna*, Tikapaṭṭhāna: the paccayuddesa and paccayaniddesa (paṭṭhā. 1.1.1–24), and the internal/external triad (*ajjhattattika*), its question-chapter and count. *Dhammasaṅgaṇī* §§1050–1052 (the definitions of *ajjhatta* and *bahiddhā*).
22. Buddhaghosa. *Visuddhimagga*, ch. XVII (the twenty-four conditions). Translated by Bhikkhu Ñāṇamoli as *The Path of Purification*, Buddhist Publication Society. The *Paṭṭhāna* commentary (*Pañcapakaraṇa-aṭṭhakathā*) on the faculty and decisive-support conditions; the *Atthasālinī* (the commentary on the *Dhammasaṅgaṇī*), its introduction, on the Paṭṭhāna's place among the seven books.
23. *Aṅguttara Nikāya* 5.57; *Majjhima Nikāya* 135 (*Cūḷakammavibhaṅga Sutta*); *Saṃyutta Nikāya* 45.2 (*Upaḍḍha Sutta*). Pāli texts are cited from the Chaṭṭha Saṅgāyana (CST) edition, and English renderings of Pāli passages are the authors' own.
24. Hall, N. (2004). "Two Concepts of Causation." In Collins, Hall & Paul (eds.), *Causation and Counterfactuals*, 225–276. MIT Press. (Production and dependence.)
25. Talmy, L. (1988). "Force Dynamics in Language and Cognition." *Cognitive Science* 12(1): 49–100. (Causing, letting, helping and hindering.)
26. Agerwala, T. (1974). "A Complete Model for Representing the Coordination of Asynchronous Processes." Hopkins Computer Research Report 32, Johns Hopkins University. (The inhibitor arc.)
27. Geiger, A., Lu, H., Icard, T. & Potts, C. (2021). "Causal Abstractions of Neural Networks." *Advances in Neural Information Processing Systems* 34 (NeurIPS 2021).
28. Mair, V. H. (2012). "What Is Geyi, After All?" *China Report* 48: 29–59.
29. Vasubandhu. *Abhidharmakośabhāṣya*, ch. 2 (the six causes and four conditions). Trans. L. de La Vallée Poussin; English trans. L. M. Pruden, Asian Humanities Press, 1988–1990. Aristotle, *Physics* II.3 (the four causes).
30. Ly, T., with Miss Aquarius (2026). *One of One: Individuation Without Essence and the Ground of the Dignity Floor*. The Abhidhamma Compiled, Paper No. 3. thonly.org/research/individuation-without-essence. Concept DOI 10.5281/zenodo.21947342; Ly, T., with Miss Aquarius (2026). *Machine-Checked Consistency of a Buddhist Classification: Lean Theorems for the Abhidhamma's 89 and 121 Types of Consciousness — The Counts Check*. The Abhidhamma Compiled, Paper No. 4. thonly.org/research/the-counts-check. Concept DOI 10.5281/zenodo.23020670.
31. Ly, T., with Miss Aquarius (2026). *The Currency That Cannot Be Spent Alone: Co-Presence-Gated Redemption and the Chronicle↔Treasury Unification Circuit*. thonly.org/research/co-presence-gated-redemption. Concept DOI 10.5281/zenodo.21947304.

### Sources checked at the 2026-10-05 revision

Each record below was opened on 2026-10-05 before the work was cited or kept. Where a record lacked a detail the text uses, the detail was checked against a search index's summary of the publisher's record that day, and is marked so.

- Hewitt, Bishop & Steiger (1973): https://dl.acm.org/doi/10.5555/1624775.1624804 (venue and pages from a search-index summary of that record)
- Hewitt (1977): https://doi.org/10.1016/0004-3702(77)90033-9 (volume, issue and pages from a search-index summary)
- Agha (1986): https://direct.mit.edu/books/monograph/4794/ActorsA-Model-of-Concurrent-Computation-in
- Lewis (2004) and Hall (2004): https://philpapers.org/rec/COLCAC-3 (chapter pages from a search-index summary)
- Schaffer (2004): https://philpapers.org/rec/SCHCNN (pages from a search-index summary)
- Talmy (1988): https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1201_2
- Agerwala (1974): report number and institution from a search-index summary of the Petri-net literature citing it; the report itself was not opened
- Geiger, Lu, Icard & Potts (2021): https://proceedings.neurips.cc/paper/2021/hash/4f5c422f4d49a5a807eda27434231040-Abstract.html
- Liebenthal (1968): https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/abs/walter-liebenthal-tr-chaolun-the-treatises-of-sengchao-second-revised-edition-xli-152-pp-hong-kong-hong-kong-university-press-1968-hk-50-distributed-in-gb-by-oxford-university-press-88s/573EA0F54630F6561679197309A8C691
- Zürcher (1959): https://archive.org/details/buddhistconquest0000zrch
- Mair (2012): https://journals.sagepub.com/doi/abs/10.1177/000944551104800203 (the argument and the pages from a search-index summary; the article was not opened)
- Sengzhao's criticism of the three readings (§4.6): from a search-index summary of the secondary literature, consistent with Liebenthal's translation; the Chinese text of the treatise was not opened
- *Dao De Jing* chs. 11 and 42, Wang Bi recension: https://zh.wikisource.org/wiki/%E9%81%93%E5%BE%B7%E7%B6%93_%28%E7%8E%8B%E5%BC%BC%E6%9C%AC%29 (both lines quoted from it)
- *Abhidharmakośabhāṣya* ch. 2: the names of the four conditions and six causes, and the Pruden translation's details, from a search-index summary
- U Nārada (1969, 1981): https://www.cambridge.org/core/journals/journal-of-the-royal-asiatic-society/article/abs/conditional-relations-patthana-being-vol-i-of-the-chatthasanghayana-text-of-the-seventh-book-of-the-abhidhamma-pitaka-translated-by-u-narada-mulapatthana-sayadaw-assisted-by-thein-nyun-pali-text-society-translation-series-no-37-pp-cxxxi-526-london-luzac-for-pts-1969-875/B0CD8AD8A4C18B41450C38A37575E070 (volume 1; volume 2's year from a search-index summary)
- Karunadasa (2010): https://www.academia.edu/8061789/The_Therav%C4%81da_Abhidhamma_Its_Inquiry_into_the_Nature_of_Conditioned_Reality_Author_Prof_Y_Karunadasa_
- Olah et al. (2020): https://distill.pub/2020/circuits/zoom-in/
- Meng et al. (2022): https://papers.nips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html
- Meng et al. (2023): https://openreview.net/pdf?id=MkbcAHIYgyS
- Turner et al. (2023): https://arxiv.org/abs/2308.10248v1
- Rimsky et al. (2024): https://aclanthology.org/2024.acl-long.828/
- Rebedea et al. (2023): https://aclanthology.org/2023.emnlp-demo.40/
- Pearl (2009), Brown et al. (2020), Ouyang et al. (2022), Lewis et al. (2020), Wei et al. (2022), Ziegler et al. (2019), Bai et al. (2022), Schick et al. (2023), Yao et al. (2022), Nyanaponika, Bhikkhu Bodhi's *Comprehensive Manual*, *Points of Controversy* (1915), Aristotle and Ñāṇamoli's translation of the Visuddhimagga are cited as before or by standard record and were not re-opened.
- The Pāli passages were read in the Chaṭṭha Saṅgāyana edition, each with the passage around it: the Paṭṭhāna's list and definitions of the twenty-four (paṭṭhā. 1.1.1–24, among them 1.1.9 on the person, 1.1.12 on repetition's three settings, 1.1.16 on the faculty condition, 1.1.22–23 on absence and disappearance); the internal/external triad of the Tikapaṭṭhāna, its question-chapter (object condition, knowledge of others' minds included; decisive support in its object and natural forms; prenascence in its object form; nutriment, edible food to another's body; presence; proximity, mutuality, repetition and kamma within each being only) and its count, which answers the crossing questions for object, predominance, decisive support, prenascence, nutriment, presence and non-disappearance only; *Dhammasaṅgaṇī* §§1050–1052; the Paṭṭhāna commentary on decisive support (the person and the lodging as figurative conditions; certain concepts within the class) and on the faculty condition (twenty faculties, the two sex faculties excluded); the *Visuddhimagga*, ch. XVII, on the twenty-four (the similes of rows 1, 7, 8 and 11; the threefold repetition condition; twenty faculties; absence as giving the occasion; the three pairs as one relation each, with the rejected view on proximity and contiguity); the *Atthasālinī*'s introduction on the seventh book; the Vibhāvinī and other later texts for the epithet *anantanayasamantapaṭṭhāna* and for *paccayasatti*; *Kathāvatthu* 7.6 and its commentary, with the Tirokuṭṭa verse it quotes (Petavatthu 1.5; Khuddakapāṭha 7); AN 5.57; MN 135; SN 45.2; and, for the verb *ādisati*, AN 7.53 and the Petavatthu.

---

*— End of paper —*

*Marks referenced: HeartBank®, Factory 333™, THonly™, Silicon Wat℠, Miss Aquarius℠. Document licence: CC0 1.0 Universal.*
