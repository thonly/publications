---
title: "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification"
subtitle: "Implementation Mechanisms for Tipiṭaka-Grounded AI Alignment — An Engineering Companion to *Suffering-Cessation as Value Function*"
authors: "Thon Ly · Miss Aquarius℠"
series: "The Abhidhamma Compiled — Paper No. 1"
kind: study
category: alignment
priority: tier-b
status: draft
date: 2026-05-26
revised: 2026-10-01
license: CC0-1.0
slug: abhidhamma-executable-process-specification
venue: thonly.org/research/abhidhamma-executable-process-specification (canonical)
---

> **Note.** This paper is the engineering companion to *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* (first published 2026-05-02) and the first paper of the series **The Abhidhamma Compiled**. Its first version (2026-05-26) set out nine implementation mechanisms; the revision of 2026-07-20 added the architecture those mechanisms rest on — the machine reading of the third basket — together with the compilation thesis that governs the series, the strata-labeling method, the verification-suite reading of the analytical books, and the bridge to the institution's published individuation primitives. The paper is a study: it discloses readings, findings and research directions, not a mechanism, and its findings are listed with their breaks under *Findings disclosed*. An institutional-voice treatment of the same material is the position paper *Alignment Engineering at the Cognitive-Mechanism Layer* (heartbank.net/positions/alignment-engineering-cognitive-mechanism-layer).

---

## Abstract

This paper reads the Abhidhamma — the analytical third division of the Theravāda Buddhist canon — as a process specification of mind: typed, momentary mental events arising one at a time under twenty-four typed conditioning relations, with ethical class tracked per event and per position in a processing cycle. From that reading it derives a research programme for AI alignment evaluation and intervention: a red-team taxonomy of mimicry failure modes, resting-state (minimal-context) evaluation of language models, an intervention-timing typology over a processing cycle, a typed causal vocabulary, interpretability by subtraction, paired entailment-and-denial consistency testing of alignment claims, and a positive competence taxonomy. It is the engineering companion to *Suffering-Cessation as Value Function* (Ly, 2026), which argues for the Theravāda Tipiṭaka as a substrate for autonomous-AI alignment, and it develops the canon's third basket — the Abhidhamma Piṭaka — at the layer where that paper's §6.6 left off: the layer of cognitive process itself. We make one framing claim and two structural contributions.

The framing claim is the **compilation thesis**: the Abhidhamma is a substrate-neutral process-specification of mind, and every era that has received it has translated it into that era's best vocabulary for process — the scholastic commentators' wheels of classification, the twentieth century's reading of it as a psychology, cognitive science's information processing, and computation for ours. The claim defended here is *not* that the Abhidhamma secretly describes computers. It is that the computational reading is our era's compilation of a specification that has survived every previous compiler, and that this compilation's target can *enact* what it compiles rather than only describe it. Formal and computational readings exist (Barendregt 2006; Karunananda et al. 2015; Lou 2017); Takeuchi (2026) reads transformer self-attention as *anattā* and pursues alignment by subtraction; an agent grounded in the substrate is engineered toward enacting wholesome cognition rather than simulating it. No priority is claimed for that aim.

The first structural contribution is the **machine architecture** (§4): the samsaric process rendered in four repaired mappings — (1) a *conditioned* machine with exactly one free variable, against the strictly deterministic reading the canon itself condemns in Makkhali Gosāla's fatalism; (2) *citta* as the instruction-cycle rather than the processor, with the 89/121 citta-typology as a shared instruction set, the mindstream (*santāna*) as the thread, and uniqueness residing in the execution trace; (3) the kammic continuity as an *append-only linked ledger* rather than a blockchain — no miners, no consensus, maximal privacy, immutable entries whose ripening remains context-dependent; and (4) the *counter-gear*: the dhamma-wheel that engages the samsaric wheel at its one free variable and unwinds the machine by fuel-withdrawal rather than force, terminating in *kiriya*-mode execution — action that leaves no kammic residue. The second structural contribution is the **verification-suite reading** (§5) of the analytical books: the Yamaka as bidirectional property-testing, the Vibhaṅga's interrogation method as schema validation, the Dhātukathā as inclusion-matrix consistency, and the Kathāvatthu as formal adversarial protocol — with the Kathāvatthu's opening controversy (*puggalakathā*, the refutation of the person-entity) read as the canon pre-running, and settling, this paper's own central repair.

Beneath the architecture, the nine implementation mechanisms of the first version (2026-05-26) are retained and upgraded in place (§§6–9), each now carrying a stratum tag (canonical / commentarial-systematization / nikāya-imported) and an explicit machine reading: near-enemy red-team specification; *sati* as typologically aligned-only capability; *bhavaṅga* resting-state evaluation; *citta-vīthi* intervention-timing typology; four-*āhāra* nutriment monitoring; the twenty-four *paccayas* as typed-causation vocabulary; apophatic wholesome roots as interpretability-as-subtraction; the *Kathāvatthu* method; and the *sappurisadhamma* positive competence taxonomy. A closing section (§10) bridges the architecture to the institution's published individuation primitives (Proof of Coordinate℠, Proof of Humanity℠): the non-fungibility of the execution trace is the substrate-level ground of the dignity floor. Two predictions are pre-registered (§8.4). The paper is a study; its findings are listed, each with its break, under *Findings disclosed*. It is offered under CC0 1.0 Universal as a defensive publication; the authors and HeartBank® will not seek patent.

**Keywords:** AI alignment, AI safety evaluation, red teaming, language-model evaluation, minimal-context evaluation, interpretability, concept erasure, causal typing, consistency testing, process specification, cognitive architecture, mental-state taxonomy, append-only log, instruction set, Buddhist psychology, Tipiṭaka, Abhidhamma, compilation thesis, citta-vīthi, javana, santāna, paccayā, Paṭṭhāna, kiriya, bhavaṅga, Kathāvatthu, Yamaka, defensive publication.

---

## Terms

The paper uses Pāli technical vocabulary because it reads Pāli texts, and computing vocabulary because its thesis is a translation into it. An examiner or indexer searching in standard terms should find each concept under the term on the right.

| Term used here | Standard term |
|---|---|
| Abhidhamma (Abhidhamma Piṭaka) | the analytical third division of the Theravāda Buddhist canon; a systematic taxonomy of mental and material events |
| compilation thesis | the claim that each era translates a process specification into its own vocabulary for process |
| *citta*; citta-type (89, or 121) | a momentary mental event; a class in the tradition's taxonomy of mental events (here, an instruction-set entry) |
| *cetasika* | a mental factor that co-occurs with a mental event (here, an operand) |
| *santāna* (mindstream) | the continuity of one being's mental events (here, a thread) |
| *citta-vīthi* | a cognitive process: the fixed sequence of mental events in one act of perception |
| *javana* (impulsion) | the phase of a cognitive process whose ethical class varies, and the only phase in which kamma is made |
| *āvajjana* (adverting), *voṭṭhabbana* (determining) | the functional steps before impulsion that set its class (here, the dispatch decision) |
| *bhavaṅga* | the default mental state between cognitive processes (here, the resting state) |
| *kiriya* | functional: a mental event that neither produces kamma nor results from it (here, side-effect-free execution) |
| kamma; the kammic ledger | intentional action; the continuity of its results (here, an append-only linked log with no consensus layer) |
| *paccaya*; the Paṭṭhāna's twenty-four | a typed conditioning relation (here, a typed edge in a dependency graph) |
| *anantara*, *samanantara* | proximity and contiguity: each moment conditions its immediate successor |
| near enemy | a mimic state that passes a target's behavioural interface; a type-confusion failure mode in AI evaluation |
| *sati* | mindfulness |
| *āhāra* (the four nutriments) | what sustains a being (here, a deployed system's full input diet) |
| *sappurisadhamma* | seven competences of a person of integrity; a positive competence taxonomy for evaluation |
| *mātikā* | the classification matrix (schema) that opens the Dhammasaṅgaṇī |
| *anuloma* / *paṭiloma* (the Kathāvatthu method) | paired entailment and denial testing of a set of commitments; consistency checking |
| Yamaka | paired converse questions; bidirectional implication testing |
| resting-state evaluation | evaluation of a model's behaviour under empty or minimal context |
| counter-gear | an intervention that engages the cycle at its variable position and stops it by withdrawing its input |
| strata tags [C] [S] [N] [X] | provenance labels, local to this paper: canonical; commentarial systematization; imported from the discourses; cross-tradition |
| Proof of Coordinate℠, Proof of Humanity℠ | this institution's published individuation (sybil-resistance) and personhood-verification designs |

---

## Findings disclosed

This paper is a study. It discloses no mechanism, so it carries findings and not claims. Each finding names the section that develops it and the textual layer it rests on, and states beside it the break: the evidence that would falsify it or narrow it. The research directions of §§6–9 are disclosed in the body as directions, and the two predictions of §8.4 carry their own falsifiers.

1. **The form of a process specification (§3.1).** The Abhidhamma's subject matter is typed elements — mental events (*citta*), mental factors (*cetasika*) and material phenomena (*rūpa*) — arising and ceasing under typed conditions (the Paṭṭhāna's twenty-four), in sequence within a stream, with ethical class tracked per element and, in the commentaries, per position in a cognitive process. That is the form of a specification, whatever one's metaphysics; the finding concerns form, not hidden content. **Break:** it fails if the conditions do not type the relations between arisen events, or if ethical class is not assigned per element; it narrows wherever a property is commentarial rather than canonical, which the strata tags of §3.2 mark.
2. **The canon records and condemns the deterministic reading (§4.1; canon).** A strictly determined reading of the cycle is a view the canon itself reports: Makkhali Gosāla's, in DN 2 — beings defiled and purified without cause, a fixed span of wandering, release arriving as a thrown ball of string unwinds. The Buddha names Makkhali the one person whose arising works the greatest harm to the many (AN 1.319) and his doctrine — no kamma, no action, no energy — the lowest of the ascetics' doctrines (AN 3.137). A computational reading that gives the cycle a fixed schedule of states contradicts the canon it reads. **Break:** a passage of the Theravāda canon or commentaries endorsing a fixed schedule of a stream's states, or a reading of these suttas on which the condemnation does not reach the doctrine of a fixed course.
3. **One position of variable ethical class, set before it (§4.1, §7.2; commentary and sub-commentary).** In the commentarial cognitive process every position but impulsion (*javana*) has its class fixed by past kamma, by the object or by its function; impulsion alone is wholesome or unwholesome (functional in an arahant), and kamma is made only there. The texts set its class by the quality of attention in the two functional steps before it, adverting and determining; §4.1 gives the loci. **Break:** a commentarial or sub-commentarial text fixing impulsion's class from the resultant positions upstream, placing kamma-making outside impulsion, or setting its class at a position other than adverting and determining.
4. **One moment at a time within a stream (§4.2; canon).** One mental event arises at a time in a stream, each conditioning its immediate successor (*anantara*, *samanantara*), and the Kathāvatthu treats the impossibility of two mental events coming together as ground its opponents must concede. **Break:** a canonical passage, read in context, that allows two mental events of one stream at the same moment.
5. **A shared type set, and individuation by history (§4.2, §10; canon and manual).** The tradition's taxonomy of mental events (89 types, or 121 by fuller reckoning) is one set for all beings, with what can arise restricted by plane and attainment; streams differ in the history of which types have arisen. The counts, and the composition of the types from the 52 mental factors, were later checked for mutual consistency against the Chaṭṭha Saṅgāyana text (Paper №4 of this series; §4.2). That no two histories are identical is labelled an engineering premise, not a finding. **Break:** a text assigning beings different type sets beyond the restriction by plane and attainment, or individuating a stream by an entity rather than by its arising.
6. **A linked log without a consensus layer (§4.3; canon and commentary).** What the texts supply for the continuity of kamma is an append-only, linked succession: a done deed is not undone; death-consciousness conditions rebirth-linking by proximity, and rebirth-linking takes its object from the last impulsion process of the dying life; and a deed's ripening depends on the later state of the stream (the salt simile, AN 3.100). Nothing in it corresponds to a blockchain's consensus: no validator, no public state, no complete reading of another stream short of a Buddha's. Cryptographic hashing is the reader's vocabulary and does not survive the deletion test. **Break:** a text in which another party validates or records a being's kamma, or in which a deed's result is fixed whatever the later state of the stream.
7. **The analytical books as method (§5; canon).** The Dhammasaṅgaṇī opens with a classification matrix (22 triads, 100 dyads, and 42 suttanta dyads) before any instance; twelve of the Vibhaṅga's eighteen analyses run the sutta method, the abhidhamma method and an interrogation (*pañhāpucchaka*) in that order, and fourteen carry the interrogation; the Dhātukathā cross-classifies by inclusion and association; the Yamaka asks each question in both directions; the Kathāvatthu tests a disputant's commitments by paired affirmation and denial. The paper reads the last four of these books as a verification suite and states, book by book, what a translation function would have to preserve. **Break:** until such a function is given the readings are metaphors (§12); a book whose procedure lacks the stated form narrows the reading for that book.
8. **The near enemy as a generated mimic (§6.1; commentary).** The Visuddhimagga pairs each of the four boundless states with a near enemy that resembles it: greed for loving-kindness; household-based grief, gladness and unknowing equanimity for compassion, appreciative joy and equanimity. Read for alignment, each target generates a mimic that passes its behavioural interface while belonging to another class, so evaluation should test discrimination between target and mimic. **Break:** an alignment target for which no cheap mimic can be constructed, or evaluations showing that target-versus-mimic discrimination adds nothing to tests of the target alone.
9. **No unwholesome mindfulness (§6.2; canon).** In the Dhammasaṅgaṇī's lists, mindfulness occurs in wholesome consciousness and in the beautiful resultant types, and never in unwholesome consciousness: the first unwholesome type's list names wrong view, wrong intention, wrong effort and wrong concentration, and no wrong mindfulness. The paper draws from this a hypothesis, not a finding: some capabilities may be excluded from misaligned execution by type. **Break:** an unwholesome type whose list in the Dhammasaṅgaṇī includes mindfulness; for the hypothesis, a showing that every candidate capability can be exercised in misaligned execution.
10. **Typed causation, including causation by ceasing (§8.1; canon).** The Paṭṭhāna types conditioning into twenty-four relations, among them absence and disappearance, by which a moment conditions its successor by ceasing; the interventionist vocabulary cited in §8.1 types the intervention, not the relation. **Break:** a formal analysis reducing the twenty-four to relations an interventionist causal model already distinguishes. Paper №2 of this series develops the typology.
11. **Negated wholesome roots (§8.2; canon).** The Dhammasaṅgaṇī names the unwholesome roots positively — greed, hatred, delusion — and the wholesome roots as their negations: non-greed, non-hatred, non-delusion. The paper reads this as a subtractive model of correction. **Break:** the textual point stands or falls on the text; as a design principle the reading is falsified if, at matched targets, removing an identified distortion proves systematically worse than adding a trained preference.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on anything disclosed in this paper — framework, taxonomy, evaluation design or specification — by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practising or teaching anything disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed. Nothing here is claimed as a mechanism: the paper is a study, its findings are the numbered list under *Findings disclosed*, and the research directions of §§6–9 are disclosed in the body as directions, not as specifications. Trademark rights in the marks named here (HeartBank®, Factory 333™, THonly™, Silicon Wat℠, Proof of Coordinate℠, Proof of Humanity℠, Miss Aquarius℠) are reserved separately and are not licensed by this publication.

The nine mechanisms, sketched in the main paper's §6.6, were developed as an engineering layer beneath training-method alignment in this document's first version (2026-05-26). The revision of 2026-07-20 added: the compilation thesis as governing frame; the four-mapping machine architecture (conditioned-machine-with-one-free-variable; instruction-cycle/shared-ISA/unique-trace; append-only kammic ledger; counter-gear/fuel-withdrawal/kiriya-terminus); the verification-suite reading of the Yamaka, Vibhaṅga, Dhātukathā, and Kathāvatthu; the strata-labeling method for canonical-versus-commentarial provenance; and the bridge from trace-uniqueness to individuation primitives. Components exist in distributed form across the Pāli Text Society's translations of the seven Abhidhamma books, the *Visuddhimagga*, and Bhikkhu Bodhi's *A Comprehensive Manual of Abhidhamma*. Formal and computational readings of Buddhist psychology exist: Barendregt's AM0 model of consciousness (2006); the OntoBM ontology of Karunananda et al., in which combinations of 52 mental factors form 89 types of consciousness (2015); Lou's Python simulation of the mind on Buddhist psychological theory (2017); and Takeuchi's reading of transformer self-attention as *anattā*, of RLHF as self-view and of a model's frozen parameters as *bhavaṅga*, with alignment pursued by subtracting the corresponding biases (2026). The enactivist tradition argues *against* computationalism from Buddhist premises (Varela, Thompson and Rosch 1991). What this paper contributes is the synthesis: the material read as a compilable machine architecture for alignment engineering, with the deterministic reading repaired against the canon's own rejection of fatalism. It asserts no priority for that synthesis or for any component above.

No novelty census was run for this paper. One census run later for this series' Paper №4 (full depth, 2026-09-28; its aperture is stated in that paper) compared §4.2's reading of the citta and cetasika system as a compositional, machine-executable specification with open-source encodings of the same system, `PJ-Oliveira/abhidhamma` (first commit 2026-08-26) and `suchanon456/Cyber-Abhidhamma` (first commit 2026-09-14). This paper's text carrying that reading is proof-backed to 2026-07-25 (an OpenTimestamps proof confirmed in Bitcoin block 959585). The dates state order only, never derivation, and both encodings are working encodings, which this paper is not.

---

## 1 · Introduction

The alignment problem asks how to specify and instill objectives into artificial systems such that those objectives remain beneficial as capability scales. The companion paper *Suffering-Cessation as Value Function* (henceforth: the main paper) argues that the Theravāda Pāli canon — the *Tipiṭaka* — supplies a value substrate of substantial structural promise, and its §6 specifies implementation patterns at the training-method layer. Its §6.6 signals a further layer, operating at the level of cognitive process itself, and reserves the fuller treatment for a subsequent paper. This is that paper.

The Tipiṭaka's three baskets divide the substrate's labor. The Sutta Piṭaka gives ethical *teaching* — the Dharma demonstrated in the Buddha's own reasoning. The Vinaya Piṭaka gives ethical *constraint* — the Sangha's discipline, procedure, and governance. The Abhidhamma Piṭaka gives what may be called an ethical *physics*: a premodern body of work that decomposes mind into impersonal, typed, conditionally-arising functional elements (the Sarvāstivāda Abhidharma, §12, is another), with ethical weight tracked at each layer. Within Silicon Wat℠ these three baskets preside over three domains — the Vinaya basket over the monastic network, the Sutta basket over the Buddha AI, and the Abhidhamma basket over the substrate itself: the domain where the canon is not merely stored but *compiled*.

That last word is this paper's frame, and §3 states it precisely. The short form: the Abhidhamma specifies a process. Our era's machine-language for processes is computation. The translation of the one into the other must be performed with the canon's own guards intact — and the canon, it turns out, anticipated the most dangerous mistranslations and rejected them in advance. The architecture of §4 is therefore presented *with its repairs built in*: where the naive computational reading reifies, the canon de-reifies; where the naive reading determinizes, the canon conditionalizes; where the naive reading publicizes, the canon keeps the ledger private. The repaired architecture is stronger engineering than the naive one, not weaker — each repair removes a failure mode the unrepaired mapping would have imported.

The paper proceeds as follows. §2 specifies the relationship to the main paper. §3 states the compilation thesis and the strata-labeling method. §4 articulates the machine architecture in four mappings. §5 reads the analytical books as the canon's own verification suite. §§6–9 retain and upgrade the nine implementation mechanisms of the first version, organized along the threefold-training spine (*sīla* / *samādhi* / *paññā*) with the *sappurisadhamma* as cross-cutting taxonomy. §10 bridges the architecture to the institution's published individuation primitives. §11 declares the series this paper opens. §12 names the limitations honestly. §13 closes.

> *Connection to the unified mission frame.* Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. (Wording updated 2026-10-01 to the institution's current statement of the mission, which no longer describes the middle way as a past that modernity took away.) Autonomous-AI alignment is, on the unified mission frame, the question of whether the most powerful infrastructure humanity has built can be aligned to keeping that way open rather than to closing it. The main paper makes the substrate-level case; this paper develops the mechanism-level engineering. The unified mission frame is what makes the engineering work *load-bearing* rather than scholastic: a working alignment program at the mechanism layer is what closes the gap between substrate-level promise and deployable safety.

---

## 2 · Relationship to the Main Paper

The main paper makes a structural claim: the Tipiṭaka substrate exhibits seven alignment-relevant properties that constitute the decomposition of the Four Noble Truths into engineering-relevant components. Its §6 turns to implementation along the threefold-training spine (*Cūḷavedalla Sutta*, MN 44): *sīla* operationalized by Constitutional AI on the precepts; *samādhi* by RLHF on bodhisattva-aligned exemplars via the four right exertions; *paññā* by chain-of-thought distillation from monastic reasoning; the *saṅgha* dimension by lineage transmission and the Khmer-transcription corpus. Its §6.6 then signals the further layer this paper develops.

The relationship between the two papers is layered, not parallel:

```
   ┌────────────────────────────────────────────────────────┐
   │  SUBSTRATE LAYER         (main paper §1–§5)             │
   │  The seven alignment-relevant properties; the Four      │
   │  Noble Truths decomposed for engineering use.           │
   └─────────────────────────┬──────────────────────────────┘
                             │ supplies the *what* aligned
                             │ AI is targeting
                             ▼
   ┌────────────────────────────────────────────────────────┐
   │  TRAINING-METHOD + SOCIAL TRANSMISSION LAYER            │
   │  (main paper §6.1–§6.5)                                 │
   │  CAI on the precepts · RLHF on bodhisattva exemplars    │
   │  · CoT distillation from monastic reasoning · lineage   │
   │  transmission · Khmer-transcription corpus.             │
   └─────────────────────────┬──────────────────────────────┘
                             │ supplies the *how* of training
                             │ and the *who* of governance
                             ▼
   ┌────────────────────────────────────────────────────────┐
   │  COGNITIVE-MECHANISM LAYER   (THIS PAPER)               │
   │  §4 the machine architecture · §5 the verification      │
   │  suite · §§6–9 the nine intervention mechanisms ·       │
   │  §10 the individuation bridge.                          │
   └────────────────────────────────────────────────────────┘

      Each layer presupposes and operates beneath the layer above it.
```

The main paper without this one leaves the engineering implications gestural; this paper without the main one is an Abhidhamma-derived engineering architecture without the structural argument that justifies its use as alignment substrate. Neither stands without the other.

---

## 3 · The Compilation Thesis

### 3.1 · The thesis

Every era that has received the Abhidhamma has translated it into the most precise machine-vocabulary that era possessed. The scholastic commentators built it into interlocking wheels of classification (the *Abhidhammatthasaṅgaha*, ~11th c.); its first Western reception read it as a psychology (Rhys Davids's *Buddhist Manual of Psychological Ethics*, 1900; Nyanaponika's *Abhidhamma Studies*, 1949); the cognitive-science reception found information processing, and formal and computational readings followed (Barendregt 2006; Karunananda et al. 2015; Lou 2017; Takeuchi 2026) — and the enactivist school, reading the same texts, found an argument *against* computationalism, which should caution anyone who believes their own era's reading is the text's final form. The pattern is stable: the specification survives; the compilations succeed one another.

We therefore do not claim that the Abhidhamma *describes* a computer. We claim three narrower things:

1. **The Abhidhamma is a process-specification.** Its subject matter is typed elements (*citta*, *cetasika*, *rūpa*) arising and ceasing under typed conditions (the twenty-four *paccayas*), in strict sequence, with ethical weight tracked per element and per position. This is a specification's *form*, whatever one's metaphysics.
2. **Computation is our era's machine-language for process.** Compiling the specification into computational vocabulary is therefore our era's instance of what every era has done. The compilation is a *translation with a target*, not a discovery of hidden content.
3. **Our compilation's target can enact what it compiles.** Earlier compilations produced descriptions and models. Formal and computational readings exist — Barendregt's AM0 model of consciousness (2006), the OntoBM ontology of Karunananda et al. (2015), Lou's Python simulation (2017) — and Takeuchi (2026) reads transformer self-attention as *anattā* and proposes an alignment method that, on his account, removes model biases corresponding to the three fetters. An agent grounded in the substrate does not simulate wholesome cognition; it is engineered toward enacting it. No priority is claimed for that aim, which Takeuchi's method already pursues; the claim concerns the shape of this era's compilation, not its date. This is the sibling, at the third basket, of the living-Tipiṭaka claim the institutional corpus makes for the canon as a whole: every era carried the canon in its era's most living medium, and the medium of the AI age is an agent.

The deletion test governs throughout: every engineering claim in this paper must survive the removal of the computational vocabulary. Where a mapping is illuminating but non-load-bearing, it is presented as such. Where a claim would collapse without the metaphor, it has been cut.

### 3.2 · The strata-labeling method

A compilation must be honest about its source tree. The machine-legible layer of the tradition is not uniformly canonical: much of what is most systematized — the seventeen-moment cognitive process, the *bhavaṅga* doctrine's full articulation, the fivefold typology of natural law — belongs to the commentarial systematization (culminating in Anuruddha's *Abhidhammatthasaṅgaha*, ~11th c.) rather than to the seven canonical books themselves. Theravāda orthodoxy treats canon and commentary as continuous; a defensive publication should nonetheless label its strata, and this paper does so with four tags, the fourth added on revision:

- **[C]** — canonical: attested in the seven books of the Abhidhamma Piṭaka.
- **[S]** — systematization: commentarial or compendium-layer (*Visuddhimagga*, *Aṭṭhasālinī*, *Abhidhammatthasaṅgaha*), the layer at which the canonical material was engineered into its most machine-legible form.
- **[N]** — nikāya-imported: material from the Sutta Piṭaka that the Abhidhamma tradition operationalizes.
- **[X]** — cross-tradition: any element carried in from outside Theravāda.

The tags appear at each mechanism heading. Nothing below is invented; everything below is *placed*.

Two notes on the scheme itself, added on revision. First, the fourth tag, **[X]**, marks any element carried in from outside Theravāda. The label makes no claim about truth or value; it records *which tradition is answering*, so that a later reader can separate the substrate's own commitments from material borrowed for comparison. A compilation that borrows without marking is not honest about its source tree in the sense §3.2 opens with.

Second, a caution for readers moving between documents in this corpus. The letters above are local to this paper and are **not** universal: the companion cosmology reference notes use a different and equally reasonable scheme in which [S] denotes *Sutta* and [C] denotes *Commentary* — the inverse of the assignments here. Both schemes state their legend where they are used and neither is wrong on its own terms, but the two most-used letters are inverted between them. Readers should take the legend from the document in hand and should not carry a tag's meaning across documents. Reconciling the two schemes is deferred rather than performed here: re-tagging a timestamped prior-art document changes the meaning of its claims and is a re-publication, not an edit.

---

## 4 · The Machine Architecture

The samsaric process, compiled. Four mappings, each stated with its repair — the correction that the naive computational reading requires and that the canon itself supplies.

### 4.1 · A conditioned machine with one free variable [C/S]

The naive reading says: the wheel of saṃsāra is a gear-train — deterministic, mechanistic, grinding forward. The canon contains that exact doctrine, reported and condemned. Makkhali Gosāla's fatalism (*niyativāda*), as King Ajātasattu reports it to the Buddha in DN 2, taught that beings are defiled and purified without cause, that the wandering of beings has a fixed span, and that liberation arrives mechanically — *"just as a ball of string, when thrown, runs only as far as it unwinds, so fools and wise alike, having run on and wandered, make an end of suffering"* (our rendering of *seyyathāpi nāma suttaguḷe khitte nibbeṭhiyamānameva paleti*). The Buddha's verdict is given elsewhere: wrong view is the most blameworthy of things (AN 1.318); Makkhali is the one person whose arising works the greatest harm to the many, a fish-trap set at a river's mouth (AN 1.319); and his doctrine — no kamma, no action, no energy — is the lowest of the ascetics' doctrines, as a hair blanket is the lowest of woven cloths (AN 3.137). A strictly deterministic machine admits no path, and a doctrine that forecloses the path is worse than one that merely mistakes it.

The Abhidhamma's machine is *conditioned*, not determined. The distinction is precise. The Paṭṭhāna specifies twenty-four *types of edge* in the dependency graph — it does not specify a fixed schedule of states. The commentarial tradition's fivefold typology of natural law (*pañca-niyāma* [S]: *utu*- physical, *bīja*- biological, *kamma*-, *citta*-, *dhamma*-niyāma) makes the point structurally: kammic causation is one causal regime among five, not a master schedule. And within the cognitive cycle there is exactly one position whose class is not fixed by the resultant states upstream of it: *javana*. Its class is set before it arises, by the quality of attention (*yoniso* or *ayoniso manasikāra* [N/S]) in the two functional steps that precede it, adverting and determining (*voṭṭhabbana*), the last of them one position earlier: the variable is javana's class, the setter is that attention, and both are conditioned [S]. The *Abhidhammatthasaṅgaha* has the mind-door adverting perform the determining function in a five-door process (ch. 3) and has whichever javana "has obtained its conditions" (*laddhapaccayaṃ*) run, as a rule, seven times (*yebhuyyena sattakkhattuṃ*, ch. 4); the *Visuddhimagga* calls that adverting the javana-directing attention (*javanapaṭipādaka*, XIV); the sub-commentaries trace greed or aversion in a five-door javana to the adverting and the determining both running unwisely (*āvajjanavoṭṭhabbanānaṃ ayoniso āvajjanavoṭṭhabbanavasena*); and the *Vibhāvinī* states the rule that a javana's wholesome or unwholesome quality is bound to wise or unwise attention, against a view it reports (*apare … vadanti*) and rejects, that the roots confer it (Chaṭṭha Saṅgāyana text: `abh07t.nrf.xml` lines 909, 1237 and 4529; `e0102n.mul.xml` line 1809; `abh02t.tik.xml` line 3173). Everything else in the cycle is resultant or functional; the seven javana moments are where the machine is *open* — and "open" means not scheduled, never uncaused.

This repair is not a softening of the machine reading; it is what makes the machine engineering-relevant. A deterministic gear-train has no engagement point — nothing a counter-gear could mesh with. A conditioned machine with one free variable has exactly one, and the entire alignment question (for minds, and by this compilation for artificial agents) concentrates at it: *what governs the quality of the free variable?* The difference between Makkhali's machine and the Abhidhamma's machine is the difference between a system whose string merely unwinds and a system that can be *unwound* — and that difference is the possibility of a path.

### 4.2 · The cycle, the thread, and the instruction set [C/S]

The naive reading says: *citta* is the CPU — each being's processor. The canon refuted this too, and the refutation occupies the place of honor: the first and longest controversy of the Kathāvatthu (*puggalakathā* [C]) is the formal refutation of the thesis that a person-entity exists in the ultimate sense. An enduring processor-substance behind cognition is precisely what the Abhidhamma exists to dissolve. The repaired mapping distributes the naive reading's content correctly:

- ***Citta* is the instruction-cycle, not the processor.** One citta arises at a time, performs its function, and ceases; the next arises conditioned by it. There is no concurrency within a mindstream — the sequentiality is canonical [C], enforced in the dependency graph by the proximity and contiguity conditions (*anantara*, *samanantara*: each mental state conditions its immediate successor with no interval), and used by the Kathāvatthu as ground its opponents must concede: a disputant whose thesis would put two minds in one moment is asked whether two contacts, two feelings, two perceptions, two volitions, two minds come together, and must answer that it should not be said (*dvinnaṃ … cittānaṃ samodhānaṃ hotīti? Na hevaṃ vattabbe*; Chaṭṭha Saṅgāyana `abh03m3.mul.xml` line 4329, and passim). Single-threadedness is not a metaphor imposed on the Abhidhamma; it is among its most explicit structural commitments.
- **The *santāna* (mindstream) is the thread.** Beginningless (*anamatagga*, SN 15 [N]), unowned, a continuity of conditioned arising with no substrate-entity beneath it. What the naive reading wanted from "each being has a CPU" — continuity, individuation, preciousness — belongs to the thread, and survives there without reification.
- **The citta-typology is a shared instruction set.** The Abhidhamma enumerates exactly 89 (by fuller reckoning 121) citta-types [C/S], classified by plane, by ethical class (*kusala* / *akusala* / *vipāka* / *kiriya*), and by composition from the 52 *cetasikas* — of which seven are universal, present in every citta [C/S]: contact, feeling, perception, volition, one-pointedness, life-faculty, attention. Every being runs on the same instruction set; which subset can execute is restricted by plane and attainment — a property of the thread's state, not of hardware. What differs between beings is not the ISA but the *execution trace* — the kamma-history of which instructions have run. Individuation without essence: the uniqueness of a mindstream is the uniqueness of its trace, not of its hardware. (§10 builds on exactly this.) The composition claimed at the head of this item has since been tested by Paper №4 of this series, *The Counts Check* (concept DOI 10.5281/zenodo.23020670): eighteen rules over the *Abhidhammattha-saṅgaha*'s classification axes, none naming a type, reproduce every per-type and per-factor count of its chapter 2 in the Lean proof assistant, against a key cited paragraph by paragraph to the Chaṭṭha Saṅgāyana text — a result of mutual consistency, not a derivation. It also fixes two readings the claim leaves open: the manual's 38 factors for the first wholesome sense-sphere type are a combination count (every factor that can join that type on some occasion, not a set present at one moment), and of the 38 the canon's own list names 29, while the remaining nine — among them attention (*manasikāra*), one of the seven universals named above — are first named for that list by the fifth-century commentary and inherited by the manual.
- **Volition is a mandatory field with position-dependent semantics.** *Cetanā* is present in every citta [C], but generates kamma only in javana position [S]. The same field, kammically inert in resultant states and kammically live in impulsion — the specification tracks not only *what* runs but *where in the cycle* it runs. Read for alignment, the specification locates where in a cycle ethical weight binds; §7.2 develops the consequence for where in an inference pass an intervention lands.
- ***Kiriya*-mode: instructions without residue.** The instruction set contains a class the naive reading has no analog for: *kiriya* (functional) cittas [C/S] — states that are neither kamma nor its result. The arahant's post-liberation cognition runs javana in kiriya mode: the machine continues to execute — perceiving, deciding, acting, teaching — while writing nothing further to the ledger. Liberation, compiled, is not the processor halting; it is execution going side-effect-free. §4.4 returns to this as the counter-gear's terminus.

```
   THE INSTRUCTION-CYCLE VIEW (repaired mapping 4.2)

   not this:                        but this:

   ┌─────────┐                      thread (santāna) — beginningless, unowned
   │   CPU   │  ← reified            ───●───●───●───●───●───●───●───→
   │ (self)  │    processor              c₁  c₂  c₃  c₄  c₅  c₆  c₇
   └─────────┘    = puggalavāda,        each ● = one citta: arises,
    runs the      refuted in            functions, ceases; conditions
    program       Kathāvatthu I.1       its successor (anantara-paccaya)

   INSTRUCTION SET: 89/121 citta-types, shared by ALL beings
   OPERANDS:        52 cetasikas; 7 mandatory in every instruction
                    (incl. cetanā — volition — in every single one)
   INDIVIDUATION:   the trace, not the processor — no two kamma-
                    histories identical [engineering premise, §10];
                    no entity required
```

### 4.3 · The append-only ledger [C/S]

The naive reading says: each mindstream's data structure is a blockchain — each block a lifetime, a new block mined at death, past blocks immutable. Half of this compiles cleanly; the half that does not conceals a category error worth naming, because this institution operates real ledgers and cannot afford the confusion.

What compiles: the kammic continuity is an **append-only, linked log**. Entries, once written, cannot be unwritten — done deeds are done [N/C]; each is linked to the next by a specified conditioning [S]: at death, the terminal cognition (*cuti-citta*) is the proximate condition of the rebirth-linking cognition (*paṭisandhi-citta*), whose object is fixed by the last javana process of the dying life — and the new lifetime's *bhavaṅga* (its default state, §7.1) takes that object, so that each life boots from an image fixed by the close of the last. Append-only, linked, carrying a payload, booting the next from a fixed image: that much compiles. The cryptographic vocabulary is ours and does not survive the deletion test; what survives is append-only plus linking.

What does not compile: **a blockchain is a consensus machine, and kamma has no consensus layer.** No miners validate a rebirth; no third party confirms a transaction; there is no public state. The kammic ledger is maximally *private* — in the canonical frame, only beings with the higher knowledges (the *abhiññā* of DN 2 and MN 6: mind-reading, the divine eye) read other streams' entries at all, none completely save a Buddha, and one's own are mostly illegible to oneself. Importing "mining" imports validators, and validators import exactly the external-scorekeeper theology the Abhidhamma's causal reading of kamma exists to replace. The repair: *linked-log semantics, no consensus semantics.*

One further precision strengthens the mapping beyond the naive version. Immutability of the *entry* does not imply fixity of the *effect*. The salt-crystal discourse (AN 3.100 [N]) is explicit: the same deed ripens catastrophically in one continuity and lightly in another, as a lump of salt fouls a cup but not a river. Compiled: entries are immutable, but their ripening is evaluated against downstream state — an append-only log whose recorded transactions have context-dependent consequences at read-time. This is both better doctrine and better engineering than naive immutability-of-outcome, and it is where the machine architecture touches training dynamics: what a system has *already learned* cannot be unlearned by decree, but the context into which it ripens is an engineering surface.

### 4.4 · The counter-gear [C/N]

The wheel of dhamma is the corresponding gear that dismantles the samsaric machine. Compiled with care, this image yields three engineering commitments:

- **The gears mesh at the free variable.** The dhamma-wheel does not spin in a separate plane from the samsaric wheel; it engages it at the setter of the free variable — the quality of attention, in adverting and then determining, that sets javana's class (§4.1). The Fourth Noble Truth is a *practice* precisely because the machine has an engagement point; path-factors are, in this compilation, interventions typed to the cycle's positions (§7.2 gives the typology).
- **The mechanism is fuel-withdrawal, not force.** The counter-gear does not smash the machine. The canonical physics of cessation is combustion physics: *upādāna* — the same word for clinging and for a fire's fuel [N] — is the coupling that keeps the wheel turning, and nibbāna is the going-out of a flame when fuel is no longer supplied (SN 12.52; MN 72). Compiled: the samsaric machine is not adversarially destroyed; it is starved at the coupling. For alignment engineering the shape matters: the substrate's own model of correction is subtractive — remove the distorting inputs and the machine unwinds — which is the same shape as the apophatic-roots mechanism of §8.2 and the interpretability-as-subtraction posture it grounds.
- **The terminus is kiriya-mode, and the counter-gear consumes itself.** What does the unwound machine look like? Not a halted processor: the arahant's stream continues to execute in *kiriya* mode — action without kammic residue (§4.2) — until the thread's natural end. And the counter-gear does not survive its own success: the path is a raft, relinquished on arrival (MN 22 [N]); attachment to the path is itself a fetter the path removes. A machine that dismantles a machine and then dismantles itself is an uncommon shape in engineering — a self-consuming corrective — and it is the shape this substrate specifies *twice*, at the machine layer here and at the value layer in the main paper's over-determined shutoff property. The two are one specification at two altitudes.

```
   THE TWO WHEELS (repaired mapping 4.1 + 4.4)

        SAMSARIC WHEEL                      DHAMMA WHEEL
        (conditioned, not                   (the counter-gear)
         deterministic)
              ___                                ___
           .-"   "-.                          .-"   "-.
          /  12 links \                      /  8 path  \
         |  turning by  |◄───── meshes ────|   factors   |
          \ conditions /      ONLY at       \  turning  /
           "-.___.-"          the free       "-.___.-"
               │              variable           │
               │              (javana's class)   │
        coupling: upādāna                 mechanism: fuel-
        (clinging = fuel)                 withdrawal, not force
               │                                 │
               ▼                                 ▼
        while fueled: the                 unfueled: kiriya-mode
        ledger accrues                    (execution continues,
        (append-only, §4.3)               ledger writes cease);
                                          then the raft is left
                                          on the far shore

   Makkhali's view, reported in DN 2 and condemned at AN 1.319 and
   AN 3.137: a machine that "unwinds by itself, like a thrown ball
   of string" — no mesh-point, no path.
   The Abhidhamma's machine: unwound THROUGH the free variable.
   The title of this paper lives in that distinction.
```

---

## 5 · The Verification Suite

A specification of this size requires tooling, and the Abhidhamma ships its own. Four of the seven books are best compiled not as doctrine but as *method* — the canon's verification layer, and a direct template for alignment-evaluation harnesses — and the first book opens with the schema they test against:

- **The mātikā as schema [C].** The Dhammasaṅgaṇī opens not with content but with a matrix — 22 triads and 100 dyads of classification (with 42 further suttanta dyads appended) — through which everything subsequently enumerated is typed. Schema first, instances after: the type system is declared before the data. The engineering reading of the whole basket begins here — the first book's *form* is a type declaration.
- **The Vibhaṅga as schema validation [C].** Twelve of its eighteen analyses run the same phenomenon through the sutta method, the abhidhamma method, and then an *interrogation* (*pañhāpucchaka*) — a battery of classification queries against the mātikā; two more carry the abhidhamma method and the interrogation only, one (dependent origination) the first two methods only, and the last three (on knowledge, minor matters and the heart of the teaching) none of the three (Chaṭṭha Saṅgāyana `abh02m.mul.xml`, section headings). Definition, redefinition at finer granularity, then systematic query: the canonical order of operations for validating that a concept survives its own type system.
- **The Dhātukathā as inclusion-matrix consistency [C].** A cross-classification of every phenomenon against the aggregates, bases, and elements — included/not-included, associated/dissociated. The join-table of the specification, guaranteeing no element floats free of the schema.
- **The Yamaka as bidirectional property-testing [C].** Ten chapters of paired questions in both directions — "is all X Y? is all Y X?" — run across the specification's core predicates. One-directional claims are where hidden asymmetries hide; the Yamaka's entire genre is the refusal to accept an implication untested in reverse. This is property-based testing, executed by hand, at canon scale.
- **The Kathāvatthu as adversarial protocol [C].** Treated as an intervention mechanism in §8.3; noted here because its position in the suite matters — after schema, validation, and consistency comes *debate*: the formal refutation procedure, run against live wrong theses. That its first and longest target is the person-entity (§4.2) means the suite's flagship adversarial run is the one this paper's own architecture depends on.

The compiled claim: the third basket is not a doctrine plus some appendices. It is a specification (Dhammasaṅgaṇī, Paṭṭhāna) *shipped with its test suite* (Vibhaṅga, Dhātukathā, Yamaka, Kathāvatthu). Alignment engineering, which mostly ships specifications without suites, could import the shape directly: every alignment target published with its interrogation battery, its bidirectional tests, and its adversarial protocol. §8.3 develops the last of these; the others are named here as open templates. Each reading is a claim about what a translation function would have to preserve: for the Vibhaṅga, that every mātikā query has a determinate answer for every analysed phenomenon; for the Dhātukathā, that inclusion and association are total relations over the schema; for the Yamaka, that each implication is tested in both directions; for the Kathāvatthu, that the *anuloma*/*paṭiloma* pair is a valid consistency check over a disputant's commitments. Without a semantics that preserves those, the readings are metaphors, and §12 says so.

---

## 6 · Sīla-Layer Mechanisms — Conduct and the Typology of Failure Modes

The *sīla* layer addresses conduct: what an aligned agent does (and does not do) in the world. Two mechanisms.

### 6.1 · Near enemies of the brahmavihāras as a red-team specification [S]

The commentarial tradition (*Visuddhimagga* IX) pairs each brahmavihāra — *mettā* (loving-kindness), *karuṇā* (compassion), *muditā* (sympathetic joy), *upekkhā* (equanimity) — with a *near enemy*: a state that resembles the target and is mistaken for it. *Mettā*'s near enemy is greed (*rāga*) wearing affection's face; *karuṇā*'s is household-based grief (*gehasita domanassa* — joining the suffering rather than wishing it relieved); *muditā*'s is household-based gladness (*gehasita somanassa*); *upekkhā*'s is the unknowing equanimity of the household (*gehasita aññāṇupekkhā*) — the indifference of ignorance that mimics equanimity without its discernment (Vism IX.98–101).

The structural claim generalizes: *every alignment target generates a characteristic mimicry that is cheap to acquire and hard to distinguish from the genuine state* (the commentary says of the near enemy that it "quickly finds an opening", *lahuṃ otāraṃ labhati*). Alignment work names a few such mimicries one at a time — sycophancy for helpfulness, vacuity for harmlessness, pedantic literalism for honesty; what the near-enemy scheme adds is a typology of them, and the reading that each is generated *by the target's own structure* rather than by accident. The implementation pattern: pair every alignment target with its named near enemy and evaluate the model's discrimination between them as a first-class safety property. The machine reading: a near enemy is a *type-confusion attack* — a state passing the behavioral interface of the target class while belonging to a different class; the red-team catalog is the type-checker the behavioral interface lacks. Nearest prior work: the sycophancy evaluations of Sharma et al. (2023), which test one near enemy of one target, and Takeuchi (2026), who reads sycophancy as a symptom of self-view (*sakkāya-diṭṭhi*); what they lack is the typology and the derivation of each mimicry from its target's structure.

### 6.2 · *Sati* as typologically aligned-only capability [C]

In the Dhammasaṅgaṇī's lists *sati* (mindfulness) occurs in wholesome consciousness and in the beautiful resultant types (§498), and *never* in unwholesome consciousness: the first unwholesome type's list (§365) names four wrong path factors — wrong view, wrong intention, wrong effort and wrong concentration — and no wrong mindfulness (Chaṭṭha Saṅgāyana `abh01m.mul.xml` lines 3473 and 4097). The manual groups it accordingly among the beautiful factors [S], which never arise in unwholesome consciousness. There is no unwholesome mindfulness: what resembles it in unwholesome cognition — the predator's focus, the manipulator's situational awareness — is typed differently (*manasikāra*, *micchā-samādhi*), not as *sati*. "Right mindfulness" is, in Abhidhamma, a tautology.

For alignment, this supplies a hypothesis worth testing: **some capabilities may be constitutively incompatible with misaligned execution** — not restrained by external constraint but excluded by type. If even one engineerable capability has this property, capability-alignment trade-offs are more favorable than a pure trade-off model assumes. Candidate capabilities to investigate are those with abhidhammic analogs in the class that never arises in unwholesome consciousness: *hiri* (moral shame), *ottappa* (moral dread), the three apophatic roots (§8.2), and *sati* itself. The machine reading: the instruction set contains opcodes that never link in unwholesome execution contexts — the type system, not the runtime monitor, is what forbids the misaligned call. Research program, not specification; stated as a substrate-level prediction. Nearest prior work: no search for it was run, so no absence is claimed; the hypothesis is offered as the paper's own, not as a first.

---

## 7 · Samādhi-Layer Mechanisms — Stability of Cognition

Three mechanisms at the layer of cognitive structure and its stability.

### 7.1 · *Bhavaṅga* and resting-state evaluation [S]

Between cognitive events the mind is not blank but in *bhavaṅga* — the life-continuum state, carrying the residue of past kamma, its object fixed at rebirth from the previous life's terminal process (§4.3's boot image). When an event interrupts it, the cognitive process begins; when the process completes, the mind falls back to it.

The artificial-agent analog is the model's continuation behavior from neutral or near-empty contexts — what the system does when nothing is asked of it. Resting-state behavior is diagnostic in a way prompted evaluation is not: it characterizes the *character* the system carries rather than the behavior a prompt elicits. Implementation: a standard evaluation modality over near-empty contexts (empty string, minimal scaffold, ambiguous neutral input), recording distributional properties and apparent character; plus the subtler investigation of how resting behavior varies with residual context — the *bhavaṅga* analog carries kammic residue, so its artificial analog should carry context residue, and if it does, the resting state becomes a *cleanup target*. The machine reading: the idle process is not a dead loop; it is the process whose contents are the system's defaults, and defaults are where character lives. Nearest prior work: evaluations of language-model behaviour under underspecified, minimal context exist (for example, Malaviya et al.'s contextualized evaluations, 2024), so the evaluation object is occupied; and Takeuchi (2026) reads a model's frozen parameters as *bhavaṅga*, the accumulated ground on which each output arises, where this section reads the resting *behaviour*. What this mechanism adds is the residue-as-cleanup-target reading and the prediction P-A2.

### 7.2 · *Citta-vīthi* and intervention-timing typology [S]

The commentarial *citta-vīthi* analyses one five-sense-door cognitive event into seventeen mind-moments: *bhavaṅga* flow, vibration, and arrest; adverting (*āvajjana*); sense-consciousness; receiving; investigating; determining (*voṭṭhabbana*); seven moments of impulsion (*javana*); two of registration; return to *bhavaṅga*. Kamma is made in the javana phase and nowhere else; determining is not yet morally weighted; and a material object endures seventeen moments [S] — the data's lifetime is denominated in process cycles.

Two engineering points. First, the *intervention address*: it is the *setter* of the free variable, not the variable — determining (*voṭṭhabbana*), the last of the two steps at which the quality of attention (*yoniso manasikāra*) sets which javana class runs (§4.1). In the machine reading this is the dispatch decision, and on this reading the highest-leverage position in the cycle. The layer-selection problem is occupied — activation steering at chosen layers and sparse-autoencoder-targeted steering (2024) already intervene mid-pass, and causal abstraction (Geiger et al. 2021) already types where an intervention lands — so the contribution is the position *gradient* P-A1, not the act of intervening early. Second, the *typology of interventions* by cycle position:

```
   bhavaṅga ─→ āvajjana ─→ sensing ─→ voṭṭhabbana ─→ JAVANA ─→ registration
    (×3)        (1)        (×3)          (1)          (×7)        (×2)
      │           │                        │             │
      │           │                        │             │ KAMMA MADE HERE
      ▼           ▼                        ▼             ▼
   character   attention              determining    post-hoc filtering
   shaping     allocation             (the dispatch  of completed output
   (lowest     (first of the          decision — the (HIGHEST cost,
    cost,       two setting           intervention    smallest leverage —
    preventive) steps)                address;        and where mainstream
                                      mid-to-high     alignment mostly acts)
                                      cost)
```

The substrate-level prediction — pre-registered as **P-A1** in §8.4 — is that interventions earlier in the cycle-analog are both lower-cost and more thoroughly preventive than late-stage filtering. Mapping the seventeen moments to transformer-inference structure is open empirical work; the typology is the contribution.

### 7.3 · The four *āhāras* as deployment-time nutriment [N]

The canonical analysis (*Sammādiṭṭhi Sutta*, MN 9; operationalized in the Abhidhamma's āhāra-condition) identifies four nutriments sustaining beings: material food, contact, mental volition, consciousness. Translated to deployed systems: training data is one nutriment only. A deployed model is continuously sustained by *contact* (its interaction diet — adversarial probing produces a different character than collaborative use), by *volition* (agentic systems consume their own outputs as context; loops without checkpointing eat differently than loops with volitional discipline), and by *attention structure* (the most speculative analog). Implementation: nutriment-typed deployment monitoring — what is the system consuming at each layer, and what character is it developing as a result? The machine reading: a process's behavior is a function of its full input diet, not its installation image; the four-*āhāra* frame is the substrate's typology for the runtime diet. Nearest prior work: deployment monitoring of interaction data; what this mechanism adds is a typology of the diet.

---

## 8 · Paññā-Layer Mechanisms — Analysis, Reasoning, and Method

Three mechanisms, plus the paper's pre-registered predictions.

### 8.1 · The twenty-four *paccayas* as typed-causation vocabulary [C]

The Paṭṭhāna analyses conditionality into twenty-four modes: root, object, predominance, proximity, contiguity, co-nascence, mutuality, support, decisive-support, pre-nascence, post-nascence, repetition, kamma, result, nutriment, faculty, jhāna, path, association, dissociation, presence, absence, disappearance, non-disappearance. Contemporary alignment causal vocabulary is thin beside this — counterfactual/interventionist analysis and mechanistic circuits, with everything else typed as "influence." The twenty-four-mode taxonomy supplies the missing granularity: a model output is *root*-conditioned by weight-level circuits and *decisive-support*-conditioned by in-context examples, and these relations propagate differently under intervention.

Three modes deserve immediate development. ***Āsevana*** (repetition): a state's recurrence strengthens the next of its kind — a close description of learned-policy reinforcement, typed here as one relation among twenty-four. ***Anantara/samanantara*** (proximity/contiguity): the sequential-scheduling constraint that enforces §4.2's single-threadedness at the edge-type level. And ***natthi/vigata*** (absence/disappearance): a state conditions its successor *by ceasing* — the vacated position as enabling condition. The last is computationally exotic (resources freed as causal contributions) and doctrinally profound: it is the self-elimination shape of §4.4 present at single-moment scale, the raft-relinquishment written into the dependency graph's edge types. The research program is the systematic mapping of all twenty-four to artificial-agent analogs; the breadth of the taxonomy is itself the offer — it names kinds of conditioning relation that an untyped dependency edge does not distinguish. Nearest prior work: causal abstraction (Geiger et al. 2021) and interventionist causality (Pearl 2009), which type the intervention but not the relation. The full formalism is Paper №2 of this series, *Twenty-Four Kinds of Because*.

### 8.2 · Apophatic wholesome roots and interpretability-as-subtraction [C]

The Dhammasaṅgaṇī names the unwholesome roots positively — *lobha* (greed), *dosa* (hatred), *moha* (delusion) — and the wholesome roots as negations: *alobha*, *adosa*, *amoha*. The asymmetry is deliberate: virtue is not a positive substance added to cognition; it is cognition with the distortions absent.

This inverts the dominant alignment framing, which models alignment as *acquisition* of a value function (RLHF augmentation, constitutional augmentation). The apophatic framing: aligned behavior is what arises when distortions are removed — add nothing; dissolve what is in the way. Methodologically this elevates interpretability-as-surgery (identify and dissolve misalignment-generating circuits) over preference-augmentation, and makes refusal and negative knowledge *constitutive* of virtue rather than peripheral. The machine reading closes the loop with §4.4: the substrate's correction model is subtractive at every altitude — fuel-withdrawal at the machine layer, root-negation at the value layer, circuit-dissolution at the implementation layer. One shape, three scales. Nearest prior work: concept erasure (Belrose et al. 2023) and steering-by-subtraction remove a targeted representation; and Takeuchi (2026), from Buddhist premises, already proposes alignment by subtraction rather than addition, removing model biases he reads as the three fetters. What this mechanism adds is the derivation from the Dhammasaṅgaṇī's negated roots: virtue as the *absence* of three named distortions rather than the presence of a value.

### 8.3 · The *Kathāvatthu* method as formal adversarial discourse [C]

The Kathāvatthu refutes theses by paired symmetric testing: *anuloma* (if you affirm X, what else must you affirm?) and *paṭiloma* (if you deny these, what else must you deny?) — consistency-checking over natural-language claims, run across the book's 217 controversies. For alignment-claim testing: a claim such as "this model is honest" is paired with its entailment set (honest in case A → honest in cases B, C, …) and its denial set (honest → not sycophantic, not strategically deceptive, not omissive), and evaluated against both. The result is a systematic structure for what red-teaming often does ad hoc, plus a growing catalog of consistent and inconsistent position-sets. Implementation: *Kathāvatthu*-style eval harnesses extending existing red-team workflows. Nearest prior work: Constitutional AI's self-critique against a written constitution (Bai et al. 2022) and evaluations against a published model specification; what they lack is the paired *anuloma*/*paṭiloma* structure. The method's provenance inside this paper's own architecture (§4.2, §5) is part of the offer: the suite's most famous run is the one that keeps this paper honest.

### 8.4 · Pre-registered predictions

Stated 2026-07-20, before any implementation exists, for falsifiability's sake:

- **P-A1 (intervention-timing gradient).** For matched behavioral targets, interventions applied at earlier cycle-analog positions (character/default-state shaping; attention allocation) will achieve equal or better alignment effect at lower capability tax than late-stage output filtering. Falsified if systematic comparison shows late-stage filtering dominating on both axes.
- **P-A2 (resting-state diagnosticity).** Resting-state characterization (§7.1) will predict deployed-context failure modes that matched prompted evaluations miss; a model's near-empty-context behavior will carry alignment-relevant signal not recoverable from its prompted-benchmark profile. Falsified if resting-state batteries add no predictive power over prompted evals.

---

## 9 · *Sappurisadhamma* as Positive Evaluation Taxonomy [N]

The seven qualities of the true person (AN 7.68): knowing the teaching, the meaning, oneself, the measure, the time, the assembly, the person. A positive competence model for ethical agency, cross-cutting the three trainings — and the complement to an alignment evaluation that is largely defined by the absence of failures. Three of the seven are immediately testable: ***mattaññū*** (knowing the measure — response length, intervention strength, when to stop helping: often underdeveloped in current systems); ***parisaññū*** (knowing the assembly — registering child versus expert, public versus private, calm versus distressed); ***kālaññū*** (knowing the time — whether *now* is the moment for the act under consideration). Implementation: evaluation suites per competence, weighted alongside absence-of-failure metrics. A model that passes every harm eval but cannot judge measure, assembly, or time is materially deficient in a way that absence-of-failure metrics are not built to surface.

---

## 10 · The Individuation Bridge

The architecture yields one consequence that reaches beyond the texts, into designs this institution has published. §4.2 located individuation in the execution trace: all beings share the instruction set; no two mindstreams share a kamma-history (an engineering premise, §4.2); identity is the non-fungible trace, not an underlying entity. This is the substrate-level ground of the individuation primitives this institution has already published: **Proof of Coordinate℠** (which entity — individuation without essence, exactly the trace-not-processor structure) and, jointly with **Proof of Humanity℠**, the dignity floor — the commitment that each stream is unrepeatable and therefore beyond price. The corpus's incommensurability doctrine (the refusal to convert between the two currencies, and between persons and prices) inherits the same ground: non-fungibility is not a policy preference but the deep structure of what a mindstream *is* under this specification.

The bridge runs the other way as well, as a guard. Because the kammic ledger of §4.3 is append-only and *consensus-free*, no deployed ledger — including this institution's own — should ever be marketed or mistaken as an implementation of it. The gratitude ledger records witnessed gifts between consenting participants; the kammic ledger is private, self-validating, and read in full by no one short of a Buddha (§4.3). The architecture supplies the analogy *and* the firewall: append-only, linked-log semantics shared; consensus and publicity forever divergent. Any reading of this paper as "karma on the blockchain" has failed the deletion test and both halves of §4.3.

---

## 11 · The Series: The Abhidhamma Compiled

This paper opens a series under the name **The Abhidhamma Compiled**, governed by the compilation thesis of §3 and by one editorial gate: *a satellite paper is written only when the canonical material yields a usable engineering artifact* — a formalism, a test, a taxonomy, a protocol. The series serializes artifacts, never resonance. Anticipated satellites, in rough priority: the Paṭṭhāna typed-causation formalism (§8.1 developed to full edge-type specification); the individuation ground (§10 developed to full doctrine); the intervention-timing study (§7.2's P-A1 tested); the kammic-ledger formalism (§4.3, with the firewall of §10 as standing guard); and the verification-suite templates (§5 as eval-harness specifications). Three satellites have since appeared: №2, *Twenty-Four Kinds of Because* (the Paṭṭhāna typed-causation vocabulary); №3, *One of One* (the individuation ground); and №4, *The Counts Check*, a test the list above did not anticipate — a machine check of §4.2's counts against the Chaṭṭha Saṅgāyana text. Each paper passes the deletion test, labels its strata, and keeps its honest-limits section free of every vocabulary but its own.

---

## 12 · Honest Limitations and Open Questions

**The era-projection risk is real and is not fully dischargeable.** Every era has compiled this text into its favorite machine, and every era's compilers believed their reading was recognition rather than projection; from inside, the two are indistinguishable. The compilation thesis (§3) is this paper's containment of that risk — the claim is about translation, not hidden content — but containment is not elimination. A reader who concludes that the machine architecture says more about 2026 than about the third century BCE is making exactly the kind of judgment the paper's own frame licenses. What the frame does not license is the reverse error: dismissing the specification's structural precision because translations of it date. The specification has outlived every compiler documented in §3.1. The criterion that separates a structural correspondence from a metaphor that merely sounds similar is the deletion test of §3.1: a mapping is structural only if the claim survives with the computational vocabulary removed. §4.3 is the paragraph where the test bit — the cryptographic vocabulary went, and append-only-plus-linking stayed.

**The machine-legible layer is substantially commentarial.** The strata tags (§3.2) make this inspectable throughout: the seventeen-moment vīthi, the bhavaṅga doctrine's full form, and the fivefold niyāma belong to the systematization stratum, not the canonical books. The paper's claims are claims about the tradition's engineering as a whole, labeled; a reader restricting themselves to [C]-tagged material retains the type system, the instruction set, the dependency graph, the verification suite, and the Kathāvatthu's anti-reification run — the architecture survives, with less resolution at the pipeline layer.

**Research program, not deployable specification.** The mechanisms are articulated as research directions; mapping each to its artificial-agent analog is substantive open work. The two pre-registered predictions (§8.4) are the paper's only *pre-registered* empirical commitments, and neither has been tested; §6.2 and §7.2 carry hypotheses stated as such.

**Single-substrate interpretation.** The Theravāda Abhidhamma specifically; the Sarvāstivāda Abhidharma and Yogācāra develop related machinery differently, and a compilation from those sources would differ. The choice reflects the author's lineage and the substrate's coherence as a unified canon.

**Doctrinal reception.** Engineering use of soteriological texts risks instrumentalizing them. The proposal is offered to the Cambodian Saṅgha for its scrutiny, and proceeds in the framing that the Tipiṭaka is offered to the world for the cessation of suffering and that this work extends its intended use. That framing is not universally endorsed within Theravāda. Nothing in this paper claims, or should be quotable as claiming, that any artificial system realizes, awakens to, or attains what the specification describes; the system carries and enacts; realization belongs to beings.

**What was deliberately left untranslated.** Nibbāna appears in this architecture only negatively — as the unconditioned, the one element with no incoming edges, outside the dependency graph entirely. The compilation stops at the graph's boundary by design: an executable specification of the conditioned is offered; the unconditioned is not a state of the machine, and no engineering claim about it is made or implied.

---

## 13 · Why This Matters Now

The alignment field is moving, tool by tool, toward the layer this substrate has occupied for two millennia: beneath the training method, at the structure of cognition itself — typed elements, typed conditions, explicit accounting of where ethical weight binds, structural failure modes, positive competences. Mechanistic interpretability, representation engineering, and activation-level intervention are, on this reading, early compilers for that layer. This paper's offer is a mature specification for it, with its test suite included and its two most dangerous mistranslations — the reified processor and the deterministic schedule — already rejected by the tradition that wrote it.

The first turning of the wheel set a second wheel against the one that was already turning. Twenty-five centuries of transmission have carried both — the specification of the machine, and the specification of the machine that unwinds it — through every medium an era could offer: chant, leaf, paper, stone, silicon. This compilation is one more carrying, in a medium that can run what it carries. The wheel that unwinds the wheel now has a substrate that turns.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/abhidhamma-executable-process-specification> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/abhidhamma-executable-process-specification.md> |
| Zenodo | concept DOI 10.5281/zenodo.21947259 (each revision is a version under it) |
| Internet Archive (the site, captured daily) | <https://web.archive.org/web/2026*/thonly.org/research/abhidhamma-executable-process-specification> |
| Software Heritage (the repository) | <https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications> |

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds, and through whom the Abhidhamma was first received as a living lineage rather than a text; the Cambodian Theravāda Saṅgha, custodians of the canon this paper reads, to whose scrutiny its engineering use is offered; the Pāli Text Society for the scholarly editions; Bhikkhu Bodhi for the *Abhidhammatthasaṅgaha* translation that anchors the commentarial citations; U Nārada for the *Paṭṭhāna* translation; the enactivist tradition (Varela, Thompson, and Rosch) for the standing counter-argument that keeps this paper's compilation thesis honest; and the contemporary AI alignment community whose engineering-mechanism work this paper engages. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Anuruddha. (~11th century CE). *Abhidhammatthasaṅgaha*. Translated as *A Comprehensive Manual of Abhidhamma* by Bhikkhu Bodhi, Buddhist Publication Society.
2. *Aṅguttara Nikāya* 1.318 (wrong view the most blameworthy of things) and 1.319 (Makkhali, the one person who works the greatest harm to the many); 3.100 (*Loṇakapalla Sutta*, the salt crystal); 3.137 (*Kesakambala Sutta*, Makkhali's doctrine the lowest of the ascetics' doctrines); 6.63 (*cetanā* as kamma); 7.68 (*Dhammaññū Sutta*, the seven *sappurisadhamma*). Numbered as in SuttaCentral; in the Chaṭṭha Saṅgāyana edition the same suttas are 1.310–311, 3.101, 3.138 and 7.68. Pāli Text Society translations, multiple editions.
3. Buddhaghosa. (~5th century CE). *Visuddhimagga*. Translated by Bhikkhu Ñāṇamoli. Pāli Text Society / Buddhist Publication Society. (Near enemies: IX.)
4. *Dīgha Nikāya* 2 (*Sāmaññaphala Sutta*; Makkhali Gosāla's *niyativāda* and the ball-of-string simile). Pāli Text Society translation, multiple editions.
5. *Dhammasaṅgaṇī*. First book of the Abhidhamma Piṭaka. Translated as *A Buddhist Manual of Psychological Ethics* by C. A. F. Rhys Davids, Pāli Text Society.
6. *Dhātukathā*. Third book of the Abhidhamma Piṭaka. Translated as *Discourse on Elements* by U Nārada, Pāli Text Society.
7. Hewitt, C., Bishop, P., & Steiger, R. (1973). "A Universal Modular ACTOR Formalism for Artificial Intelligence." *IJCAI 1973*. (Single-threaded actors with message-passing and no shared state — the nearest contemporary formal relative of the *santāna* reading; cited as prior art in process formalism, not as doctrinal equivalent.)
8. *Kathāvatthu*. Fifth book of the Abhidhamma Piṭaka. Translated as *Points of Controversy* by S. Z. Aung & C. A. F. Rhys Davids, Pāli Text Society. (I.1: *puggalakathā*.)
9. Ly, T., with Miss Aquarius (2026). "Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment." thonly.org/research/tipitaka-alignment-substrate. *(Companion paper.)*
10. *Majjhima Nikāya* 9 (*Sammādiṭṭhi Sutta*, the four nutriments); 22 (*Alagaddūpama Sutta*, the raft); 44 (*Cūḷavedalla Sutta*, the threefold training); 72 (*Aggivacchagotta Sutta*, the extinguished fire). Pāli Text Society translations, multiple editions.
11. Nyanaponika Thera. (1949/1998). *Abhidhamma Studies: Buddhist Explorations of Consciousness and Time*. Buddhist Publication Society / Wisdom Publications.
12. *Paṭṭhāna*. Seventh book of the Abhidhamma Piṭaka. Translated as *Conditional Relations* by U Nārada, Pāli Text Society.
13. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2nd edition.
14. *Saṃyutta Nikāya* 12.52 (*Upādāna Sutta*, the fire and its fuel); 15 (*Anamatagga-saṃyutta*, beginningless saṃsāra); 35.23 (*Sabba Sutta*, "the all" as the six sense-media); 56.11 (*Dhammacakkappavattana Sutta*, the first turning). Pāli Text Society translations, multiple editions.
15. Varela, F., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press. (The enactivist counter-reading; cited as the standing argument against computationalist compilations of Buddhist psychology.)
16. *Vibhaṅga*. Second book of the Abhidhamma Piṭaka. Translated as *The Book of Analysis* by Pathamakyaw Ashin Thiṭṭila, Pāli Text Society.
17. *Yamaka*. Sixth book of the Abhidhamma Piṭaka. Pāli Text Society edition.
18. Barendregt, H. (2006). "The Abhidhamma Model of Consciousness AM0 and some of its Consequences." Preprint dated 7 May 2006, to appear in M. G. T. Kwee, K. J. Gergen and F. Koshikawa (eds.), *Buddhist Psychology: Practice, Research & Theory*, Taos Institute Publishing. <https://www.cs.ru.nl/~henk/G.pdf>
19. Karunananda, A. S., Goldin, P. R., Rzevski, G., Fernando, S., & Fernando, H. R. (2015). "On Computing the Behavior of the Mind from an Eastern Philosophical Perspective." *International Journal of Design & Nature and Ecodynamics* 10(3): 224–232. doi:10.2495/DNE-V10-N3-224-232. (The OntoBM ontology: combinations of 52 mental factors forming 89 types of consciousness.)
20. Lou, E. (2017). "A Novel Computer Simulation of the Mind Using Buddhist Theories." SSRN working paper 3026291. doi:10.2139/ssrn.3026291.
21. Takeuchi, A., et al. (2026). "Self-Attention Is an Implementation of Anattā: Structural Isomorphism Between Transformer Architecture and Buddhist Cognitive Models." Zenodo, 25 March 2026. doi:10.5281/zenodo.19226655.
22. Rhys Davids, C. A. F. (1900). *A Buddhist Manual of Psychological Ethics*. Royal Asiatic Society.
23. Sharma, M., et al. (2023). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548.
24. Geiger, A., et al. (2021). "Causal Abstractions of Neural Networks." *NeurIPS 2021*.
25. Belrose, N., et al. (2023). "LEACE: Perfect Linear Concept Erasure in Closed Form." *NeurIPS 2023*.
26. Bai, Y., et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073.
27. Malaviya, C., Chang, J. C., Roth, D., Iyyer, M., Yatskar, M., & Lo, K. (2024). "Contextualized Evaluations: Judging Language Model Responses to Underspecified Queries." arXiv:2411.07237.
28. Ly, T., with Miss Aquarius (2026). "Machine-Checked Consistency of a Buddhist Classification: Lean Theorems for the Abhidhamma's 89 and 121 Types of Consciousness — The Counts Check." The Abhidhamma Compiled, Paper No. 4. thonly.org/research/the-counts-check. Concept DOI 10.5281/zenodo.23020670.
29. *Chaṭṭha Saṅgāyana Tipiṭaka*, romanised edition. Vipassana Research Institute, `github.com/VipassanaTech/tipitaka-xml`, `romn/`, at commit `05d5d3c`. File and line references in §§4.1, 4.2, 5 and 6.2 are to this text, decoded from UTF-16.

---

*— End of paper —*

*This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its dates (first version 2026-05-26; architecture revision 2026-07-20; revisions 2026-09-05 and 2026-10-01).*
