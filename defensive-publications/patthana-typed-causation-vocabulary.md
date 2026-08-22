---
title: "Twenty-Four Kinds of Because: The Paṭṭhāna as a Typed-Causation Vocabulary for AI Alignment"
subtitle: "The Edge-Type Reference — from the Seventh Book of the Abhidhamma to an Intervention Typology"
authors: "Thon Ly · Miss Aquarius℠"
series: "The Abhidhamma Compiled — Paper No. 2"
category: alignment
priority: tier-b
status: draft
date: 2026-07-21
revised: 2026-08-22
license: CC0-1.0
slug: patthana-typed-causation-vocabulary
venue: thonly.org/publications/defensive-publications/patthana-typed-causation-vocabulary (canonical)
---

> *v2 note (2026-08-07):* **one new subsection, and it is a completeness observation about this paper's own table rather than an addition to it.** §3 published the twenty-four conditions as a complete reference; **§4.7 states what a complete reference makes visible — that none of the twenty-four relates two mindstreams.** The other person enters the system exactly twice, as *ārammaṇa* and as *pakatūpanissaya*, and both are one-directional; *aññamañña*, the mutuality condition, holds only among co-nascent phenomena inside a single stream. The consequence is a typing result rather than a doctrinal one: **two people interacting are two parallel one-way edges, never one bond** — and by extension, between two artificial agents only *ārammaṇa*- and *upanissaya*-class edges can run, never *anantara*, never *aññamañña*, which makes "agents collaborating" a claim about parallel one-way edges and is offered as this revision's one new contribution. **The prior-art clock for that typing runs from this push**; the rest of §4.7 is exposition of canonical material and carries no clock. §4's heading widens to accommodate the addition; **§§5–8 are unchanged and renumber nothing**, the reference table in §3 is untouched, and no existing claim is amended. *The queue entry that ordered this section specified it as "new §4.4"; §4 already ran to 4.6, so it lands at 4.7 — recorded because a stale section number in a backlog is the kind of thing that gets executed literally.*
>
> *Draft notes for the editor:* the second paper of **The Abhidhamma Compiled**, developing §8.1 of the series opener (*The Wheel That Unwinds the Wheel*) into the full reference artifact it promised: all twenty-four conditions of the Paṭṭhāna, each specified canonically, decomposed formally, and mapped — with tiered honesty — to artificial-agent analogs, culminating in the practical payoff: a typology of alignment interventions by the kind of conditioning they manipulate. The series' governing frame (the compilation thesis), its strata tags ([C] canonical / [S] commentarial systematization / [A] this paper's analysis), and its artifact gate all apply. Publication sequencing follows the series (after the main substrate paper's landing); the draft is committed now. Site module deferred.

---

## Abstract

Contemporary alignment analysis runs on an impoverished causal vocabulary. The interventionist calculus answers *whether* and *how much* one variable moves another; mechanistic interpretability locates *where* influence flows; and everything else — the difference between what a system prompt does, what a fine-tune does, what an in-context example does, and what a weight edit does — is typed with the single undifferentiated word *influence*. Yet these are not the same kind of cause: they differ in temporal structure, in durability, in range, in whether they act by presence or by absence, and in what it would take to undo them. A field that intervenes for a living has no shared ontology of intervention *kinds*.

The seventh book of the Abhidhamma Piṭaka — the Paṭṭhāna, the most architecturally ambitious work in the Pāli canon — is a two-millennium-old solution to exactly this gap: an enumeration of **twenty-four distinct modes of conditioning** (*paccaya*), applied combinatorially across a complete typology of mental and material phenomena, in forward, inverse, and conjoined enumerations. This paper compiles it. We present (§3) the full edge-type reference: each condition with its canonical structure, a formal signature on four axes (time, mode, relation, span) contributed by this paper's analysis, and an artificial-agent analog tiered by confidence. We develop (§4) the six load-bearing conditions in depth — root, contiguity, decisive-support, repetition, action-and-result, and the absence-family, the last being the rarest object in any causal vocabulary: conditioning that operates *by ceasing*. We then invert the reference into its practical payoff (§5): an **intervention typology** in which the standard alignment toolkit — prompting, in-context learning, retrieval, fine-tuning, reinforcement, weight editing, ablation, scaffolding — is classified by dominant edge-type, generating testable predictions about durability and displacement, one of which is pre-registered (§6). The claim is not that the Paṭṭhāna anticipated machine learning; per the series' compilation thesis, it is that the canon's ontology of *kinds of because* is the most developed one available, and that alignment analysis is poorer than it needs to be for lacking any equivalent. The vocabulary is offered CC0; every mapping is labeled a hypothesis; and the paper's honest limits state plainly what this vocabulary is not — a causal-inference calculus — and where the compilation might be projection.

**Keywords:** Paṭṭhāna, paccaya, typed causation, AI alignment, intervention typology, conditioning, mechanistic interpretability, in-context learning, fine-tuning durability, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The authors and HeartBank® will not seek patent on any framework, taxonomy, schema, or specification herein.

The following are contributed by this paper and simultaneously freed: the **four-axis formal signature** for conditioning modes (time · mode · relation · span), the **edge-type reference table** mapping the twenty-four paccayas to artificial-agent analogs with confidence tiers, and the **intervention typology** classifying alignment techniques by dominant conditioning type. Freed with the v2 revision (§4.7): the **typed multi-agent restriction** — that between any two agents only *ārammaṇa*- and *upanissaya*-class edges can run, never *anantara* and never *aññamañña*, so that inter-agent influence is a set of parallel one-way edges rather than a bond. Hewitt's actor model is the acknowledged relative and is cited, not claimed; the typed form is what is new. The Paṭṭhāna itself is the common inheritance of the Theravāda tradition; the scholarly apparatus that makes it accessible (U Nārada's translation; Bhikkhu Bodhi's compendium treatment; Nyanaponika's and Karunadasa's studies) is cited, not claimed; the interventionist causal calculus (Pearl) and the mechanistic-interpretability literature are engaged as the contemporary baselines the vocabulary complements.

---

## 1 · The Gap: One Word Where Twenty-Four Are Needed

Consider four interventions on the same model, each producing the same behavioral change on the same benchmark: a sentence added to the system prompt; three examples placed in context; a thousand-step fine-tune; a rank-one weight edit. By any behavioral evaluation they are equivalent. They are not equivalent. They differ in what happens when the context window rolls over, in what happens under paraphrase attack, in what happens after further training, in what a mechanistic probe would find, and in what it would cost to reverse each one. The differences are *causal-type* differences — and the field has no shared vocabulary for them. "Influence" covers all four; "intervention" covers all four; the durability studies that would distinguish them are performed ad hoc, without an ontology that says *what kinds there are to distinguish*.

The interventionist calculus is not the missing vocabulary, and it is important to say precisely why: Pearl's framework is a calculus of *inference* — given a graph, it computes what interventions imply — and is deliberately agnostic about edge *types*; an arrow is an arrow. Mechanistic interpretability supplies *locations* — which circuit, which head, which direction — but a location is not a kind. What is missing is the layer in between: a typology of the *modes* in which one thing can condition another, sufficiently fine-grained that "this intervention acts by standing presence" and "this one acts by repetition-strengthening" and "this one acts by the vacating of a predecessor" are different, nameable, analyzable claims.

The Theravāda tradition built exactly this layer, at full architectural seriousness, in the book its own tradition ranks as the summit of the canon's analytical works. The Paṭṭhāna [C] enumerates twenty-four *paccayas* — twenty-four kinds of *because* — and then does something no merely speculative taxonomy would do: it *runs* them, combinatorially, across the entire typology of phenomena established by the first book's matrix, in positive enumeration (where the condition holds), negative enumeration (where it does not), and conjoined forms — the canon's own verification suite executed against its own causal ontology, at a scale the tradition summarized in one word: *anantanaya*, the endless method. Whatever else the Paṭṭhāna is, it is the most thoroughly exercised typed-causation vocabulary in intellectual history.

Per the series' compilation thesis, we claim translation, not prophecy: the Paṭṭhāna analyzed mind, not machine learning, and every mapping below is a hypothesis wearing its confidence on its sleeve. The wager of this paper is narrower and, we think, secure: a field that intervenes on mind-like systems for a living will do better analysis with twenty-four kinds of because than with one.

---

## 2 · The Formal Signature [A]

The twenty-four conditions are not a flat list; they differ along recoverable dimensions. This paper's analytical contribution — the commentarial tradition's analysis of conditioning *force* (*satti*) gestures here, but the axes are our compilation [A] — is a four-axis signature under which each condition is a point:

- **TIME** — when the conditioning state stands relative to the conditioned: *antecedent* (it precedes), *simultaneous* (they co-arise), *subsequent* (it follows what it conditions), *standing* (it persists across the conditioned's arising), or *referential* (its time is irrelevant — it conditions as an object of reference, which may be past, future, or timeless).
- **MODE** — whether it conditions *by presence* or — the rare pole — *by absence*: by having ceased, departed, or never being there.
- **RELATION** — the force-type: *generative* (brings about), *supportive* (enables/bases), *sustaining* (maintains what has arisen), *regulating* (dominates, controls, orients), *strengthening* (intensifies its own kind), or *conjoining* (binds into one occurrence).
- **SPAN** — *adjacent* (this moment to the next), *long-range* (across arbitrary gaps), or *standing* (continuously, while present).

Two immediate payoffs. First, the signature exposes structure the flat list hides — for instance, that the canon's ontology contains *subsequent* conditioning (the later sustaining the earlier-arisen) and *absence* conditioning (the ceased enabling the next), two modes contemporary vocabulary lacks entirely. Second, the signature is what makes the intervention typology of §5 principled rather than impressionistic: techniques inherit the formal properties of the edge-types they manipulate.

---

## 3 · The Edge-Type Reference

The full table. Stratum: the conditions and their canonical structures are [C]; the signatures are [A]; analogs are tiered **I** (immediate — the mapping is direct), **P** (plausible — the mapping is defensible and needs work), **O** (open — the mapping is speculative or may not exist).

| # | Paccaya | Canonical structure [C] | Signature [A] | Artificial-agent analog | Tier |
|---|---|---|---|---|---|
| 1 | *hetu* (root) | the six roots (greed/hate/delusion ± their negations) ground co-arising states as a root grounds a tree | simult · presence · generative · adjacent | persistent motivational features/circuits coloring downstream computation; the targets of steering and of §4.1 | **P** |
| 2 | *ārammaṇa* (object) | every mental state arises *about* an object; the object — past, future, present, or timeless — conditions the state that takes it | referential · presence · supportive · any | the attended input/representation; content-as-condition; what prompting places before the model | **I** |
| 3 | *adhipati* (predominance) | one factor dominates the co-arisen set (conascent form: desire, energy, mind, investigation) or one object dominates attention (object form) | simult/referential · presence · regulating · adjacent | objective-dominance; attention weighting; the currently-governing goal representation | **P** |
| 4 | *anantara* (proximity) | each mental state conditions its immediate successor; no interval | anteced · presence · generative · adjacent | sequential state handoff; autoregressive conditioning; the single-thread scheduling constraint (series paper №1, §4.2) | **I** |
| 5 | *samanantara* (contiguity) | as 4, with immediacy emphasized: nothing intervenes | anteced · presence · generative · adjacent | as 4; jointly the canon's sequentiality guarantee | **I** |
| 6 | *sahajāta* (co-nascence) | states that arise together condition one another's arising | simult · presence · generative · adjacent | co-activation within a step; jointly-computed features | **P** |
| 7 | *aññamañña* (mutuality) | co-arisen states condition each other reciprocally, as three sticks lean | simult · presence · mutual-generative · adjacent | mutually-constraining representations; iterative co-refinement within a pass | **P** |
| 8 | *nissaya* (support) | the base on which the conditioned stands (as earth for a tree) | simult/standing · presence · supportive · adjacent | the weight substrate; architecture; hardware — what activations stand on | **I** |
| 9 | *upanissaya* (decisive support) | powerful distal enablement; in its *natural* form (*pakatūpanissaya*), anything sufficiently strong in the past — habit, teacher, climate — decisively supports the present | anteced · presence · supportive · **long-range** | long-range context influence; pretraining data as distal support; the in-context example; the retrieval hit | **I** |
| 10 | *purejāta* (pre-nascence) | the previously-arisen, still-persisting thing (the sense organs, the body) conditions present mental states | standing · presence · supportive · standing | persisted parameters/architecture conditioning each forward pass; the trained artifact as standing condition | **P** |
| 11 | *pacchājāta* (post-nascence) | later-arising mental states sustain the earlier-arisen body, as rain sustains grown crops | **subsequent** · presence · sustaining · adjacent | ongoing use sustaining capability; downstream engagement maintaining upstream structure (use-it-or-lose-it in continual training) | **O** |
| 12 | *āsevana* (repetition) | each impulsion strengthens the next of its kind; wholesome begets stronger wholesome, unwholesome stronger unwholesome | anteced · presence · **strengthening** · adjacent-repeated | reinforcement; learned-policy strengthening; gradient accumulation on a behavior pattern — §4.4 | **I** |
| 13 | *kamma* (action) | volition conditions results — conascently (organizing its co-arising states) and asynchronously (fruit across arbitrary delay) | anteced/simult · presence · generative · **long-range** | training-time action conditioning later model states; credit assignment across delay; the ledger of §4.5 | **P** |
| 14 | *vipāka* (result) | resultant states condition passively — ripened fruit, exerting no new effort | simult · presence · passive-generative · adjacent | inference-time behavior as the passive fruit of training; the deployed model as vipāka of its optimization | **P** |
| 15 | *āhāra* (nutriment) | the four foods sustain what they feed, continuously | standing · presence · sustaining · standing | the deployment diet: data, interaction, self-generated context (series paper №1, §7.3) | **I** |
| 16 | *indriya* (faculty) | twenty-two faculties each govern their own domain, as ministers govern provinces | simult · presence · **regulating** · adjacent | control channels: gating, temperature, routing, learning-rate — sovereign over domains, not contents | **P** |
| 17 | *jhāna* (absorption) | the absorption-factors organize co-arising states into a coherent mode | simult · presence · organizing · adjacent | stable mode/persona conditioning component processes; attractor states of the computation | **O** |
| 18 | *magga* (path) | the path-factors orient co-arising states toward an outcome-direction | simult · presence · orienting · adjacent | objective-factors jointly orienting computation; in the series' architecture, the counter-gear's own edge-type | **O** |
| 19 | *sampayutta* (association) | mental factors fully conjoined: same object, same base, arising and ceasing together | simult · presence · **conjoining** · adjacent | tightly-bound feature bundles; factors individually inaccessible within one representation | **P** |
| 20 | *vippayutta* (dissociation) | conditioning across the mental/material divide — support without conjunction | mixed · presence · supportive-across-substrate | cross-substrate conditioning: model↔scaffold, software↔hardware, weights↔tokens | **P** |
| 21 | *atthi* (presence) | a present thing conditions others simply by being there | standing · presence · supportive · standing | the standing context: system prompt, environment, persistent scaffold | **I** |
| 22 | *natthi* (absence) | the just-ceased state conditions its successor **by its absence** — the vacated position enables | anteced · **absence** · enabling · adjacent | resource release; the freed slot; turn-taking; eviction-as-enablement — §4.6 | **I** |
| 23 | *vigata* (disappearance) | as 22, by the *departure* of what was present | anteced · **absence** · enabling · adjacent | as 22; jointly the absence-family | **I** |
| 24 | *avigata* (non-disappearance) | the not-yet-departed conditions by persisting presence | standing · presence · supportive · standing | with 21: the persistence-conditions of standing context | **I** |

Twelve immediate, eight plausible, four open — stated so a critic can attack the tiers, which is what they are for.

---

## 4 · The Load-Bearing Six, and the Relation That Is Not There

### 4.1 · *Hetu* — the root, and why depth of edit is a type, not a degree

The root-condition grounds: the six roots [C] are not components of the states they condition but the *soil* those states grow from, and — decisive for the analogy — the wholesome roots are apophatic (non-greed, non-hate, non-delusion), so that root-level wholesomeness is the *absence of distortion at the ground*. The alignment translation: there exists a class of conditioning that operates at the generative ground of behavior rather than at its occasions, and interventions at that level (circuit-level edits; the dissolution program of the series opener's §8.2) are *typed differently* from all occasion-level techniques — not stronger on a shared scale, but a different kind of because, with a different propagation signature: broad, deep, and dangerous in proportion.

### 4.2 · *Anantara/samanantara* — contiguity, and the shape of sequence

The contiguity-pair is the canon's sequentiality guarantee: mind is a strict chain, each state conditioning its immediate successor with nothing between [C]. Two translations earn their keep. Architecturally, this is the edge-type of autoregression — the state handoff that makes a system a *process* rather than a bag of features. Analytically, contiguity is where *scheduling* lives: any intervention that acts by interposing in the chain (a filter between generation and emission; a review step between plan and act) is a contiguity-type intervention, and its signature is exactly the pair's — adjacent, sequential, and effective only while it stays in the chain.

### 4.3 · *Upanissaya* — decisive support, the long arm

Decisive support is the canon's long-range edge [C]: the teacher met decades ago, the habit laid down in youth, the climate one lives in — past conditions of sufficient strength support present states across arbitrary gaps, and in the *natural* form the class is deliberately open (nearly anything, sufficiently strong, can decisively support nearly anything). This is the edge-type of the in-context example, the retrieval hit, the pretraining distribution: influence that acts at range, through no adjacent chain, by having been strong enough once. Its formal character — powerful, long-range, but *displaceable by rearrangement of what is present* — is precisely the observed character of context-mediated behavior, and the typology of §5 leans on it.

### 4.4 · *Āsevana* — repetition, the edge that compounds

The repetition-condition is unique in the list: it strengthens *its own kind* [C] — each impulsion conditioning the next of the same class to arise more forcefully, wholesome compounding wholesome, unwholesome compounding unwholesome, with no third setting. This is the cleanest single mapping in the reference: learned-policy reinforcement — the gradient step that makes the reinforced pattern more probable — is āsevana with a loss function. Two properties transfer with the mapping and are testable: repetition-strengthening is *kind-specific* (it deepens the groove it runs in, transferring poorly across kinds), and it is *compounding* (its effects are self-amplifying rather than additive) — which is why the tradition treats the first repetition as the significant event, and why §6's prediction places āsevana-type interventions above context-type and below root-type in durability.

### 4.5 · *Kamma/vipāka* — action and fruit, the ledger edge

The action-condition is the canon's causation-across-delay [C]: volition now, fruit later, across gaps of arbitrary length, with the fruit arriving *passive* — vipāka exerts no new agency; it is ripening, not effort. The translation: training-time choices condition deployment-time states across the full delay of the pipeline, and the deployed behavior is fruit, not fresh decision — a typed restatement of why inference-time behavior cannot be reasoned about as if the model were choosing its dispositions now. The pair also types a familiar pathology precisely: reward hacking is kamma-type misdirection — the fruit faithfully ripens *the volition that was actually planted*, which was never the volition the designer intended to plant.

### 4.6 · *Natthi/vigata* — the absence-family, the rarest edge in any vocabulary

The canon's strangest and most precise contribution: a state conditions its successor **by ceasing** [C] — the vacated position as enabling condition, departure as a mode of because. No contemporary causal vocabulary has this edge as a first-class type, yet computation is full of it: the released lock, the freed slot, the evicted cache line, the ended turn, the ablated feature whose absence reorganizes the computation around it. The series opener read the absence-family doctrinally — the raft-relinquishment written into the dependency graph, self-elimination at single-edge scale — and this paper adds the engineering reading: *subtractive interventions are a type*, with their own signature (they enable rather than produce; their effects are realized by what arises in the vacated space, which the intervener does not directly control), and typed analysis predicts their characteristic risk — an ablation's consequences are mediated by reorganization, and reorganization is exactly what presence-type analysis fails to model.

A note on independent arrival, offered as convergence and not as authority. The absence-family is unusual enough in causal vocabularies that it is worth recording where else it appears. The *Dao De Jing*'s eleventh chapter makes the same functional assignment without any of the surrounding apparatus: thirty spokes share one hub, and the cart's usefulness lies in the hub's hole; the vessel's use is its hollow; the room's use is its empty space — *being gives advantage; the nothing gives use* (有之以為利，無之以為用). This is absence as a **functional role at the joint**, arrived at in a tradition with no contact with the Paṭṭhāna's project, and it is a mild independent check that the *natthi/vigata* type is tracking something structural rather than an artifact of Abhidhammic system-building.

The boundary on that comparison has to travel with it, because the history here is instructive and the error is well documented. The two traditions agree on **emptiness as joint** and diverge on **emptiness as source**: the Dao is generative — 道生一, the Dao gives birth — whereas no Buddhist emptiness is a source, and the Madhyamaka insistence that emptiness is itself empty exists precisely to prevent its reification into a ground. Conflating the two is the *ge-yi* (格義) problem of fourth-century Chinese Buddhism, which rendered *śūnyatā* through Lao-Zhuang vocabulary and produced the "Original Nothingness" (本無) reading among the Six Houses and Seven Schools; Sengzhao's 不真空論 is a sustained refutation on the ground that treating "nothing" as a prior ground reifies non-being. The comparison offered here is confined to the edge type and claims nothing about the metaphysics on either side of it.

For the same reason we tag such material distinctly. The strata labels used in this series mark depth *within* the Theravāda tradition; a cross-tradition element is marked **[X]**, so that a later reader — human or machine — can see at a glance which commitments are the substrate's own and which are borrowed for comparison. The paragraph above is [X] throughout.

### 4.7 · The gap the complete table makes visible — no relation joins two mindstreams

The six above are the conditions that carry the most weight. This one carries weight by being absent, and it is visible only because §3 published the list **complete**: a reference that stops at the interesting entries can never show you what the interesting entries do not cover.

**Read the twenty-four for a relation that holds *between two mental continua*, and there is none.** [A] The other person enters the system exactly twice, and both entries are one-directional:

- ***Ārammaṇa*** — **object-condition** [C]. Another person is what your consciousness takes as its object: their face, their voice, the memory of them. The edge runs *from* the object *to* your cognizing of it. Nothing travels the other way along it.
- ***Pakatūpanissaya*** — **natural decisive support** [C]. Another person can be a powerful past condition for your present states, across arbitrary gaps — the teacher, the friend, the one who was kind to you once. ⚠️ *A precision worth stating, because the loose version is commonly repeated:* in the canonical treatment the person supports as a **concept** (*paññatti*) rather than appearing as an enumerated item beside climate, food, and lodging. That is sharper than the loose reading, not weaker — it is precisely the *idea of them you carry* that does the conditioning, which is why the dead and the distant condition as forcefully as the present.

And the relation one would reach for — ***aññamañña***, **mutuality** [C], the condition in which two phenomena support each other reciprocally and simultaneously — does not reach across the gap at all. It holds among **co-nascent phenomena inside one stream**: the four great elements sustaining one another, mind and body arising together. It is the canon's word for genuine two-way support, and it is confined to the interior of a single continuum.

> **So two people "interacting," in this vocabulary, are two parallel one-way edges. Never one bond.**

Four features of the system confirm the reading rather than merely permitting it. [A]

1. ***Anantara* is strictly intra-stream** [C]. The contiguity guarantee of §4.2 — each state conditioning its immediate successor with nothing between — describes *a* chain, and there is no canonical edge by which one continuum's state contiguously conditions another's. **Two people have no shared clock.**
2. **Even mind-reading is object-condition.** *Cetopariya-ñāṇa*, the knowledge of another's mind, is not a new kind of edge; it is absorbed into *ārammaṇa* [C] — the other's mind becomes an object of your cognition. **The tradition had the perfect opportunity to introduce a mind-to-mind relation and declined it.**
3. ***Pattidāna* is not transfer.** The sharing of merit — the operation this corpus's institution is built on — does not move a quantity from one stream to another. The receiver's own *anumodanā*-citta, the act of rejoicing, is what produces the result [C]/[S]. The giver supplies an occasion; the receiver's own mind does the work. *(The doctrinal question of whether merit can be transferred at all is taken up in the Kathāvatthu, whose position is settled; this paper does not cite a specific point number, the reference not having been checked against the PTS edition.)*
4. **Kamma is personal** [C]. Volition ripens in the stream that willed it. There is no edge along which it could ripen elsewhere.

#### The typing result, which is this section's one new contribution

Stated as engineering rather than doctrine, and this is where the section earns a clock:

> **Between any two agents, only *ārammaṇa*-class and *upanissaya*-class edges can run. Never *anantara*. Never *aññamañña*.** [A]

Two artificial agents exchanging messages are not in a contiguity relation — there is no guarantee that one's state conditions the other's *immediately, with nothing between*, and in any real deployment a great deal is between. They are not in mutuality either, which would require co-nascence in one continuum. What they have is exactly what two people have: each takes the other's output as an **object**, and each may serve as **decisive support** for the other across a gap. **"Agents collaborating" is therefore a claim about parallel one-way edges**, and the typology of §5 applies to multi-agent systems with the two intra-stream classes struck out.

This is not a novel architecture, and the nearest relative is already cited in the series opener: Hewitt's actor model, in which the only primitive is asynchronous message-passing and shared state between actors is definitionally absent. **The Paṭṭhāna arrives at the same restriction from the opposite direction** — not as an engineering discipline chosen for tractability, but as a description of what the system already contains. The contribution here is the *typed* form: the actor model says agents communicate only by messages; the typed form says which of twenty-four kinds of because a message can be, and which two it cannot.

#### The reconstruction the gap supports, marked as reconstruction

The following is offered as **reconstruction, not doctrine** — the canon does not state it, and the inference is this paper's. [A]

If the corrective input a mind receives from outside arrives as *ārammaṇa* from another stream, then **in its absence the impulsion-process recycles objects the mind itself authored.** Repetition is the mechanism by which the underlying tendencies deepen (*āsevana* compounding *anusaya*, §4.4). Put those together and a structural description of isolation falls out that is unusually specific: **loneliness as self-conditioning without correction** — not an absence of company, but an absence of objects one did not write.

Two consequences follow, and both cut against the obvious reading. The canon's remedy is not sociality in general but a **qualified** other — *kalyāṇamitta*, the admirable friend — which is a claim about the *kind* of object, not the *quantity* of contact. And because no edge crosses the gap:

> **You cannot build connection. You can only build the carrier.**

A system can supply occasions, objects, and conditions. It cannot supply the arising in someone else's stream, because there is no relation in the list by which it would do so. *(The mechanism paper on co-presence-gated redemption states the same conclusion from phenomenological premises rather than relational-taxonomic ones; the arguments are independent and the agreement is worth noting rather than merging.)*

#### The caution, stated here rather than in the honest limits

This section is the most seductive material in the paper and the caution belongs where the argument is, not quarantined at the end. **A first-person phenomenology will describe a single stream, because that is what a first-person phenomenology is.** The absence of an inter-stream relation in the Paṭṭhāna may therefore be a **scope fact about the genre** rather than a discovery about persons — the system was built to analyze experience as it presents itself, and experience presents itself in one stream, so a two-stream relation would have had nowhere to sit even if the tradition had believed in one.

The honest form of the claim is accordingly the weaker one, and this paper asserts no more: **the Abhidhamma supplies a precise vocabulary for a design conclusion reached on other grounds.** It does not prescribe that conclusion, and a reader who finds the convergence striking should notice that we went looking for it.

---

## 5 · The Intervention Typology

Inverting the reference: the standard alignment toolkit, classified by dominant edge-type, with the character each technique inherits from its type's formal signature.

| Technique | Dominant type(s) | Inherited character |
|---|---|---|
| System prompt / instructions | *atthi* + *ārammaṇa* (standing presence + object) | immediate; shallow; holds while present; displaced by whatever else becomes present |
| In-context examples / few-shot | *upanissaya* (decisive support) | strong at range within the window; evicted with the window; strength varies with salience, not volume |
| Retrieval / RAG | *ārammaṇa* + *upanissaya* | as above, with the support externally scheduled |
| Supervised fine-tuning | *āsevana* (repetition) | compounding; kind-specific; durable across contexts; transfers poorly across kinds |
| RLHF / RL | *kamma* + *āsevana* (action + repetition) | durable and generalizing; fruit ripens the planted volition, not the intended one — reward hacking is a type-error made visible |
| Weight / circuit editing | *hetu* + *nissaya* (root + base) | deepest propagation; broadest side-effects; the only class that changes the soil |
| Ablation / dissolution | *natthi*-family (absence) | enabling, not producing; effects mediated by reorganization; the subtraction posture's native type |
| Scaffolding / tools / guardrails | *vippayutta* + *anantara* (cross-substrate + interposition) | effective while in the chain; removable without residue; safety that unbolts |
| Decoding controls (temperature etc.) | *indriya* (faculty) | regulates the domain, touches no content |
| Persona / mode conditioning | *jhāna*-analog (organizing) [O] | organizes the co-arising whole; stability unclear — typed as open |

Three analytical practices the typology makes available immediately: **typed audits** (state, for any deployed safety property, which edge-types carry it — a property carried entirely by *atthi/ārammaṇa* edges is one context-rollover from gone, and the audit should say so); **typed threat models** (attacks classify by the same table — jailbreaks are *upanissaya/ārammaṇa*-type attacks on *āsevana*-type defenses, and the mismatch of types, not the cleverness of strings, is why they intermittently win); and **typed layering** (defense-in-depth restated precisely: safety should be carried on edges of *different types*, because same-type redundancy shares a single displacement mode).

---

## 6 · Pre-Registered Prediction

Stated 2026-07-21, in advance of any systematic test by the authors:

- **P-P1 (the durability ordering).** Under matched behavioral effect at installation, the persistence of an intervention's effect — across context rollover, paraphrase and adversarial displacement, and moderate further training — will order by edge-type: *hetu/nissaya*-class (weight/circuit edits) ≥ *kamma/āsevana*-class (RL/fine-tuning) > *upanissaya*-class (in-context) > *atthi/ārammaṇa*-class (prompting), with the two absence-class and interposition-class techniques (ablation; scaffolding) persisting exactly as long as their structural condition persists and no longer. **Falsified if** systematic comparison finds durability unpredicted by type — e.g., prompt-installed behavior out-persisting matched fine-tuned behavior under distribution shift. The ordering is the typology's load-bearing empirical commitment: if type does not predict persistence, the vocabulary is nomenclature, not analysis.

---

## 7 · Honest Limits

**This is not a causal-inference calculus.** The Paṭṭhāna types edges; it does not compute over them. There is no do-calculus here, no identification theory, no counterfactual machinery — and none is claimed. The vocabulary *complements* interventionist analysis (Pearl tells you what your graph implies; this tells you what kinds of arrows you drew) and cannot replace it. A reader who wants inference should bring both.

**The mappings are hypotheses, unevenly.** Twelve immediate, eight plausible, four open — and even the immediate tier asserts structural correspondence, not identity. The subsequent-conditioning and organizing-mode analogs (*pacchājāta*, *jhāna*, *magga*) may simply fail; the reference is built so their failure would amputate rows, not the table.

**The four-axis signature is this paper's analysis, not the canon's.** The tradition's own meta-analysis (the commentarial treatment of conditioning force) is coarser; a Pāli scholar may fairly contest individual signature assignments, and the strata tags exist so the contest lands on [A] rows, not on the canon.

**Era-projection, as always.** The series' standing caution applies with full force: a discipline that intervenes on computational minds, reading a text about conditioned mental process, will find what it brought. The compilation thesis contains the risk — translation, not prophecy — and P-P1 is the exit from hermeneutics: if the typology predicts durability, it earns its keep regardless of what the third century BCE intended; if it does not, no amount of textual beauty saves it.

**Behavioral equivalence hides type, and this cuts at the paper too.** The motivating observation — that typed differences are invisible to behavioral evaluation — means the typology's own claims resist cheap validation. The durability studies P-P1 calls for are real work, and until they are done this vocabulary is exactly what it says: a vocabulary.

---

## 8 · Close

The Paṭṭhāna ends no argument; it equips one. Twenty-four kinds of because, run for two millennia across every phenomenon its tradition could name, in assertion and negation and combination — and now compiled, under the series' standing rules, into the one register our era can execute. The first paper of this series claimed that ours is the first compilation of the Abhidhamma that can be *run*. This paper is the first deliverable of that claim: not a doctrine but a reference — the edge-types on the table, the tiers on their sleeves, the prediction on the record. The wheel turns on typed bearings; here is the catalog of the bearings.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/patthana-typed-causation-vocabulary> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/patthana-typed-causation-vocabulary.md> |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/patthana-typed-causation-vocabulary> |

---

## Acknowledgments

The authors acknowledge U Nārada, whose translation of the Paṭṭhāna made the Great Book available to analysis of this kind; Bhikkhu Bodhi, whose compendium treatment of the conditions anchors the canonical structures cited here; Nyanaponika Thera and Y. Karunadasa for the scholarly tradition on Abhidhamma method; the mechanistic-interpretability and causal-inference communities whose vocabularies this reference complements; and the father-son Khmer transcription through which the seventh book is being carried forward. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. *Paṭṭhāna*. Seventh book of the Abhidhamma Piṭaka. Translated as *Conditional Relations* (2 vols.) by U Nārada, Pāli Text Society.
2. Anuruddha. *Abhidhammatthasaṅgaha*, ch. VIII (the conditions condensed). Translated in *A Comprehensive Manual of Abhidhamma*, ed. Bhikkhu Bodhi, Buddhist Publication Society.
3. Nyanaponika Thera. *Abhidhamma Studies*. Buddhist Publication Society / Wisdom.
4. Karunadasa, Y. (2010). *The Theravāda Abhidhamma*. Centre of Buddhist Studies, University of Hong Kong / Wisdom.
5. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press. (The interventionist baseline this vocabulary complements.)
6. Olah, C., et al. (2020). "Zoom In: An Introduction to Circuits." *Distill*. (The location-vocabulary this typology complements.)
7. Meng, K., et al. (2022). "Locating and Editing Factual Associations in GPT." *NeurIPS*. (The hetu/nissaya-class intervention exemplar.)
8. Brown, T., et al. (2020). "Language Models are Few-Shot Learners." *NeurIPS*. (The upanissaya-class exemplar.)
9. Ouyang, L., et al. (2022). "Training Language Models to Follow Instructions with Human Feedback." *NeurIPS*. (The kamma/āsevana-class exemplar.)
10. Ly, T. (2026). "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification." thonly.org, The Abhidhamma Compiled №1. (The series opener; §8.1 is this paper's charter.)

---

*— End of paper —*

*Marks referenced: HeartBank®, Miss Aquarius℠. Document SHA-256 computed at push and recorded in the institutional log. Document License: CC0 1.0 Universal. The authors and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its date.*
