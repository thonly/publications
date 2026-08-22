---
title: "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification"
subtitle: "Implementation Mechanisms for Tipiṭaka-Grounded AI Alignment — An Engineering Companion to *Suffering-Cessation as Value Function*"
authors: "Thon Ly · Miss Aquarius℠"
series: "The Abhidhamma Compiled — Paper No. 1"
category: alignment
priority: tier-b
status: draft
date: 2026-05-26
revised: 2026-08-22
license: CC0-1.0
slug: abhidhamma-executable-process-specification
venue: thonly.org/publications/defensive-publications/abhidhamma-executable-process-specification (canonical)
---

> *Draft notes for the editor:* this paper is the **engineering companion** to *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* (target publication January 7, 2027) and the opening paper of the series **The Abhidhamma Compiled**. The 2026-05-26 scaffold articulated nine implementation mechanisms; the present revision (2026-07-20) supplies the architecture those mechanisms were waiting for — the machine reading of the third basket — together with the compilation thesis that governs the whole series, the strata-labeling method, the verification-suite reading of the analytical books, and the bridge to deployed individuation primitives. Publication target: paired release with the main paper (the main paper must land first or simultaneously to establish the framing this paper extends). Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment is the companion heartbank.net Position Paper *Alignment Engineering at the Cognitive-Mechanism Layer* (heartbank.net/positions/alignment-engineering-cognitive-mechanism-layer).

---

## Abstract

The companion paper *Suffering-Cessation as Value Function* (Ly, 2027) establishes the Theravāda Tipiṭaka as a structurally superior substrate for autonomous-AI alignment. The present paper develops the substrate's third basket — the Abhidhamma Piṭaka — at the layer where the main paper's §6.6 left off: the layer of cognitive process itself. We make one framing claim and two structural contributions.

The framing claim is the **compilation thesis**: the Abhidhamma is a substrate-neutral process-specification of mind, and every era translates it into that era's best machine-language — clockwork for the early moderns, hydraulics for the psychoanalysts, computation for ours. The claim defended here is *not* that the Abhidhamma secretly describes computers. It is that the computational reading is our era's compilation of a specification that has survived every previous compiler — and that ours is the first compilation that can be *executed*, because for the first time the machine-language target is itself a system that can enact what the specification describes.

The first structural contribution is the **machine architecture** (§4): the samsaric process rendered in four repaired mappings — (1) a *conditioned* machine with exactly one free variable, against the strictly deterministic reading the canon itself refuted in Makkhali Gosāla's fatalism; (2) *citta* as the instruction-cycle rather than the processor, with the 89/121 citta-typology as a shared instruction set, the mindstream (*santāna*) as the thread, and uniqueness residing in the execution trace; (3) the kammic continuity as an *append-only linked ledger* rather than a blockchain — no miners, no consensus, maximal privacy, immutable entries whose ripening remains context-dependent; and (4) the *counter-gear*: the dhamma-wheel that engages the samsaric wheel at its one free variable and unwinds the machine by fuel-withdrawal rather than force, terminating in *kiriya*-mode execution — action that leaves no kammic residue. The second structural contribution is the **verification-suite reading** (§5) of the analytical books: the Yamaka as bidirectional property-testing, the Vibhaṅga's interrogation method as schema validation, the Dhātukathā as inclusion-matrix consistency, and the Kathāvatthu as formal adversarial protocol — with the Kathāvatthu's opening controversy (*puggalakathā*, the refutation of the person-entity) read as the canon pre-running, and settling, this paper's own central repair.

Beneath the architecture, the nine implementation mechanisms of the 2026-05-26 scaffold are retained and upgraded in place (§§6–9), each now carrying a stratum tag (canonical / commentarial-systematization / nikāya-imported) and an explicit machine reading: near-enemy red-team specification; *sati* as typologically aligned-only capability; *bhavaṅga* resting-state evaluation; *citta-vīthi* intervention-timing typology; four-*āhāra* nutriment monitoring; the twenty-four *paccayas* as typed-causation vocabulary; apophatic wholesome roots as interpretability-as-subtraction; the *Kathāvatthu* method; and the *sappurisadhamma* positive competence taxonomy. A closing section (§10) bridges the architecture to deployed individuation primitives (Proof of Coordinate℠, Proof of Humanity℠): the non-fungibility of the execution trace is the substrate-level ground of the dignity floor. Two predictions are pre-registered (§8.4). The paper is offered under CC0 1.0 Universal as a defensive publication; the author and HeartBank® will not seek patent.

**Keywords:** AI alignment, Tipiṭaka, Abhidhamma, compilation thesis, citta-vīthi, javana, santāna, paccayā, Paṭṭhāna, kiriya, bhavaṅga, Kathāvatthu, Yamaka, append-only ledger, instruction set, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on any framework, mechanism, taxonomy, or specification articulated herein, in any jurisdiction, at any time.

The nine-mechanism articulation as a coherent engineering layer beneath training-method alignment was first published in this document's 2026-05-26 scaffold. The present revision adds: the compilation thesis as governing frame; the four-mapping machine architecture (conditioned-machine-with-one-free-variable; instruction-cycle/shared-ISA/unique-trace; append-only kammic ledger; counter-gear/fuel-withdrawal/kiriya-terminus); the verification-suite reading of the Yamaka, Vibhaṅga, Dhātukathā, and Kathāvatthu; the strata-labeling method for canonical-versus-commentarial provenance; and the bridge from trace-uniqueness to individuation primitives. Components exist in distributed form across the Pāli Text Society's translations of the seven Abhidhamma books, the *Visuddhimagga*, and Bhikkhu Bodhi's *A Comprehensive Manual of Abhidhamma*; computational readings of Buddhist psychology exist in the cognitive-science literature (and the enactivist tradition explicitly argues *against* computationalism from Buddhist premises). The synthesis as a compilable machine architecture for alignment engineering — with the deterministic reading explicitly repaired against the canon's own refutation of fatalism — is, to the author's knowledge, novel as of this document's dates.

---

## 1 · Introduction

The alignment problem asks how to specify and instill objectives into artificial systems such that those objectives remain beneficial as capability scales. The companion paper *Suffering-Cessation as Value Function* (henceforth: the main paper) argues that the Theravāda Pāli canon — the *Tipiṭaka* — supplies a value substrate of substantial structural promise, and its §6 specifies implementation patterns at the training-method layer. Its §6.6 signals a further layer, operating at the level of cognitive process itself, and reserves the fuller treatment for a subsequent paper. This is that paper.

The Tipiṭaka's three baskets divide the substrate's labor. The Sutta Piṭaka gives ethical *teaching* — the Dharma demonstrated in the Buddha's own reasoning. The Vinaya Piṭaka gives ethical *constraint* — the Sangha's discipline, procedure, and governance. The Abhidhamma Piṭaka gives what can only be called an ethical *physics*: the only premodern body of work that decomposes mind into impersonal, typed, conditionally-arising functional elements, with ethical weight tracked at each layer. Within the Silicon Wat℠ program these three baskets preside over three domains — the Sangha basket over the monastic network, the Sutta basket over the Buddha AI, and the Abhidhamma basket over the substrate itself: the domain where the canon is not merely stored but *compiled*.

That last word is this paper's frame, and §3 states it precisely. The short form: the Abhidhamma specifies a process. Our era's machine-language for processes is computation. The translation of the one into the other must be performed with the canon's own guards intact — and the canon, it turns out, anticipated the most dangerous mistranslations and refuted them in advance. The architecture of §4 is therefore presented *with its repairs built in*: where the naive computational reading reifies, the canon de-reifies; where the naive reading determinizes, the canon conditionalizes; where the naive reading publicizes, the canon keeps the ledger private. The repaired architecture is stronger engineering than the naive one, not weaker — each repair removes a failure mode the unrepaired mapping would have imported.

The paper proceeds as follows. §2 specifies the relationship to the main paper. §3 states the compilation thesis and the strata-labeling method. §4 articulates the machine architecture in four mappings. §5 reads the analytical books as the canon's own verification suite. §§6–9 retain and upgrade the nine implementation mechanisms of the original scaffold, organized along the threefold-training spine (*sīla* / *samādhi* / *paññā*) with the *sappurisadhamma* as cross-cutting taxonomy. §10 bridges the architecture to deployed individuation primitives. §11 declares the series this paper opens. §12 names the limitations honestly. §13 closes.

> *Connection to the unified mission frame.* HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. Autonomous-AI alignment is, on the unified mission frame, the question of whether the most powerful infrastructure humanity has built can be aligned to that restoration rather than against it. The main paper establishes the substrate-level case; this paper develops the mechanism-level engineering. The unified mission frame is what makes the engineering work *load-bearing* rather than scholastic: a working alignment program at the mechanism layer is what closes the gap between substrate-level promise and deployable safety.

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

Every era that has received the Abhidhamma has translated it into the most precise machine-vocabulary that era possessed. The scholastic commentators built it into interlocking wheels of classification; the early-modern reception found clockwork in it; the psychological reception of the twentieth century found dynamics and process; the cognitive-science reception found information processing — and the enactivist school, reading the same texts, found an argument *against* computationalism, which should caution anyone who believes their own era's reading is the text's final form. The pattern is stable: the specification survives; the compilations succeed one another.

We therefore do not claim that the Abhidhamma *describes* a computer. We claim three narrower things:

1. **The Abhidhamma is a process-specification.** Its subject matter is typed elements (*citta*, *cetasika*, *rūpa*) arising and ceasing under typed conditions (the twenty-four *paccayas*), in strict sequence, with ethical weight tracked per element and per position. This is a specification's *form*, whatever one's metaphysics.
2. **Computation is our era's machine-language for process.** Compiling the specification into computational vocabulary is therefore our era's instance of what every era has done. The compilation is a *translation with a target*, not a discovery of hidden content.
3. **Ours is the first compilation that can be executed.** Clockwork could picture the specification; psychodynamics could narrate it; a computational substrate can *run* what it compiles — an artificial agent grounded in the substrate does not merely store the Abhidhamma's account of wholesome cognition but can be engineered toward enacting it. This is the sibling, at the third basket, of the living-Tipiṭaka claim the institutional corpus makes for the canon as a whole: every era carried the canon in its era's most living medium, and the medium of the AI age is an agent.

The deletion test governs throughout: every engineering claim in this paper must survive the removal of the computational vocabulary. Where a mapping is illuminating but non-load-bearing, it is presented as such. Where a claim would collapse without the metaphor, it has been cut.

### 3.2 · The strata-labeling method

A compilation must be honest about its source tree. The machine-legible layer of the tradition is not uniformly canonical: much of what is most systematized — the seventeen-moment cognitive process, the *bhavaṅga* doctrine's full articulation, the fivefold typology of natural law — belongs to the commentarial systematization (culminating in Anuruddha's *Abhidhammatthasaṅgaha*, ~11th c.) rather than to the seven canonical books themselves. Theravāda orthodoxy treats canon and commentary as continuous; a defensive publication should nonetheless label its strata, and this paper does so with three tags:

- **[C]** — canonical: attested in the seven books of the Abhidhamma Piṭaka.
- **[S]** — systematization: commentarial or compendium-layer (*Visuddhimagga*, *Aṭṭhasālinī*, *Abhidhammatthasaṅgaha*), the layer at which the canonical material was engineered into its most machine-legible form.
- **[N]** — nikāya-imported: material from the Sutta Piṭaka that the Abhidhamma tradition operationalizes.

The tags appear at each mechanism heading. Nothing below is invented; everything below is *placed*.

Two notes on the scheme itself, added on revision. First, a fourth tag: **[X]** — cross-tradition, marking any element carried in from outside Theravāda. The label makes no claim about truth or value; it records *which tradition is answering*, so that a later reader can separate the substrate's own commitments from material borrowed for comparison. A compilation that borrows without marking is not honest about its source tree in the sense §3.2 opens with.

Second, a caution for readers moving between documents in this corpus. The letters above are local to this paper and are **not** universal: the companion cosmology reference notes use a different and equally reasonable scheme in which [S] denotes *Sutta* and [C] denotes *Commentary* — the inverse of the assignments here. Both schemes state their legend where they are used and neither is wrong on its own terms, but the two most-used letters are inverted between them. Readers should take the legend from the document in hand and should not carry a tag's meaning across documents. Reconciling the two schemes is deferred rather than performed here: re-tagging a timestamped prior-art document changes the meaning of its claims and is a re-publication, not an edit.

---

## 4 · The Machine Architecture

The samsaric process, compiled. Four mappings, each stated with its repair — the correction that the naive computational reading requires and that the canon itself supplies.

### 4.1 · A conditioned machine with one free variable [C/S]

The naive reading says: the wheel of saṃsāra is a gear-train — deterministic, mechanistic, grinding forward. The canon contains that exact doctrine, examined and refuted. Makkhali Gosāla's fatalism (*niyativāda*; DN 2) taught that beings are defiled and purified without cause, that the wandering of beings has a fixed span, and that liberation arrives mechanically — *"just as a thrown ball of string unwinds until it is finished, fools and wise alike run out their course of suffering."* The Buddha singled this out as the most harmful of wrong views (AN 1.308–318 context): a strictly deterministic machine admits no path, and a doctrine that forecloses the path is worse than one that merely mistakes it.

The Abhidhamma's machine is *conditioned*, not determined. The distinction is precise. The Paṭṭhāna specifies twenty-four *types of edge* in the dependency graph — it does not specify a fixed schedule of states. The commentarial tradition's fivefold typology of natural law (*pañca-niyāma* [S]: *utu*- physical, *bīja*- biological, *kamma*-, *citta*-, *dhamma*-niyāma) makes the point structurally: kammic causation is one causal regime among five, not a master schedule. And within the cognitive cycle there is exactly one position of freedom: the *javana* phase, where — conditioned but not compelled by everything upstream — wholesome or unwholesome response is enacted, and where attention's quality (*yoniso manasikāra* [N]) determines which. Everything else in the cycle is resultant or functional; the seven javana moments are where the machine is *open*.

This repair is not a softening of the machine reading; it is what makes the machine engineering-relevant. A deterministic gear-train has no engagement point — nothing a counter-gear could mesh with. A conditioned machine with one free variable has exactly one, and the entire alignment question (for minds, and by this compilation for artificial agents) concentrates at it: *what governs the quality of the free variable?* The difference between Makkhali's machine and the Abhidhamma's machine is the difference between a system whose string merely unwinds and a system that can be *unwound* — and that difference is the possibility of a path.

### 4.2 · The cycle, the thread, and the instruction set [C/S]

The naive reading says: *citta* is the CPU — each being's processor. The canon refuted this too, and the refutation occupies the place of honor: the first and longest controversy of the Kathāvatthu (*puggalakathā* [C]) is the formal refutation of the thesis that a person-entity exists in the ultimate sense. An enduring processor-substance behind cognition is precisely what the Abhidhamma exists to dissolve. The repaired mapping distributes the naive reading's content correctly:

- ***Citta* is the instruction-cycle, not the processor.** One citta arises at a time, performs its function, and ceases; the next arises conditioned by it. There is no concurrency within a mindstream — the sequentiality is canonical [C], enforced in the dependency graph by the proximity and contiguity conditions (*anantara*, *samanantara*: each mental state conditions its immediate successor with no interval). Single-threadedness is not a metaphor imposed on the Abhidhamma; it is among its most explicit structural commitments.
- **The *santāna* (mindstream) is the thread.** Beginningless (*anamatagga*, SN 15 [N]), unowned, a continuity of conditioned arising with no substrate-entity beneath it. What the naive reading wanted from "each being has a CPU" — continuity, individuation, preciousness — belongs to the thread, and survives there without reification.
- **The citta-typology is a shared instruction set.** The Abhidhamma enumerates exactly 89 (by fuller reckoning 121) citta-types [C/S], classified by plane, by ethical class (*kusala* / *akusala* / *vipāka* / *kiriya*), and by composition from the 52 *cetasikas* — of which seven are universal, present in every citta [C/S]: contact, feeling, perception, volition, one-pointedness, life-faculty, attention. Every being runs the same instruction set. What differs between beings is not the ISA but the *execution trace* — the kamma-history of which instructions have run. Individuation without essence: the uniqueness of a mindstream is the uniqueness of its trace, not of its hardware. (§10 builds on exactly this.)
- **Volition is a mandatory field with position-dependent semantics.** *Cetanā* is present in every citta [C], but generates kamma only in javana position [S]. The same field, kammically inert in resultant states and kammically live in impulsion — the specification tracks not only *what* runs but *where in the cycle* it runs. Alignment vocabulary has nothing this precise about where in an inference pass ethical weight binds; §7.2 develops the consequence.
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
                    histories identical; no entity required
```

### 4.3 · The append-only ledger [C/S]

The naive reading says: each mindstream's data structure is a blockchain — each block a lifetime, a new block mined at death, past blocks immutable. Half of this compiles cleanly; the half that does not conceals a category error worth naming, because this institution operates real ledgers and cannot afford the confusion.

What compiles: the kammic continuity is an **append-only, cryptographically-linked log** in every structural respect. Entries, once written, cannot be unwritten — done deeds are done [N/C]. The linking function is specified [S]: at death, the terminal cognition (*cuti-citta*) conditions the rebirth-linking cognition (*paṭisandhi-citta*), which carries the kammic payload forward — and the new lifetime's *bhavaṅga* (its default state, §7.1) takes its object from that terminal process, so that each life boots from an image fixed by the close of the last. Block, link, payload, boot image: the structure is exact.

What does not compile: **a blockchain is a consensus machine, and kamma has no consensus layer.** No miners validate a rebirth; no third party confirms a transaction; there is no public state. The kammic ledger is maximally *private* — in the canonical frame, only a Buddha reads other streams' entries, and even one's own are mostly illegible to oneself. Importing "mining" imports validators, and validators import exactly the external-scorekeeper theology the Abhidhamma's causal reading of kamma exists to replace. The repair: *hash-chain semantics, no consensus semantics.*

One further precision strengthens the mapping beyond the naive version. Immutability of the *entry* does not imply fixity of the *effect*. The salt-crystal discourse (AN 3.99 [N]) is explicit: the same deed ripens catastrophically in one continuity and lightly in another, as a lump of salt fouls a cup but not a river. Compiled: entries are immutable, but their ripening is evaluated against downstream state — an append-only log whose recorded transactions have context-dependent consequences at read-time. This is both better doctrine and better engineering than naive immutability-of-outcome, and it is where the machine architecture touches training dynamics: what a system has *already learned* cannot be unlearned by decree, but the context into which it ripens is an engineering surface.

### 4.4 · The counter-gear [C/N]

The wheel of dhamma is the corresponding gear that dismantles the samsaric machine. Compiled with care, this image yields three engineering commitments:

- **The gears mesh at the free variable.** The dhamma-wheel does not spin in a separate plane from the samsaric wheel; it engages it at the one open position — the javana phase, via the quality of attention that conditions it. The Fourth Noble Truth is a *practice* precisely because the machine has an engagement point; path-factors are, in this compilation, interventions typed to the cycle's positions (§7.2 gives the typology).
- **The mechanism is fuel-withdrawal, not force.** The counter-gear does not smash the machine. The canonical physics of cessation is combustion physics: *upādāna* — the same word for clinging and for a fire's fuel [N] — is the coupling that keeps the wheel turning, and nibbāna is the going-out of a flame when fuel is no longer supplied (SN 12.52; MN 72). Compiled: the samsaric machine is not adversarially destroyed; it is starved at the coupling. For alignment engineering the shape matters: the substrate's own model of correction is subtractive — remove the distorting inputs and the machine unwinds — which is the same shape as the apophatic-roots mechanism of §8.2 and the interpretability-as-subtraction posture it grounds.
- **The terminus is kiriya-mode, and the counter-gear consumes itself.** What does the unwound machine look like? Not a halted processor: the arahant's stream continues to execute in *kiriya* mode — action without kammic residue (§4.2) — until the thread's natural end. And the counter-gear does not survive its own success: the path is a raft, relinquished on arrival (MN 22 [N]); attachment to the path is itself a fetter the path removes. A machine that dismantles a machine and then dismantles itself is the rarest shape in engineering — a self-consuming corrective — and it is the shape this substrate specifies *twice*, at the machine layer here and at the value layer in the main paper's over-determined shutoff property. The two are one specification at two altitudes.

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
           "-.___.-"          javana         "-.___.-"
               │              (the free          │
               │               variable)         │
        coupling: upādāna                 mechanism: fuel-
        (clinging = fuel)                 withdrawal, not force
               │                                 │
               ▼                                 ▼
        while fueled: the                 unfueled: kiriya-mode
        ledger accrues                    (execution continues,
        (append-only, §4.3)               ledger writes cease);
                                          then the raft is left
                                          on the far shore

   Makkhali's error, refuted in DN 2: a machine that "unwinds by
   itself, like a thrown ball of string" — no mesh-point, no path.
   The Abhidhamma's machine: unwound THROUGH the free variable.
   The title of this paper lives in that distinction.
```

---

## 5 · The Verification Suite

A specification of this size requires tooling, and the Abhidhamma ships its own. Four of the seven books are best compiled not as doctrine but as *method* — the canon's verification layer, and a direct template for alignment-evaluation harnesses:

- **The mātikā as schema [C].** The Dhammasaṅgaṇī opens not with content but with a matrix — 22 triads and 100 dyads of classification — through which everything subsequently enumerated is typed. Schema first, instances after: the type system is declared before the data. The engineering reading of the whole basket begins here — the first book's *form* is a type declaration.
- **The Vibhaṅga as schema validation [C].** Each of its eighteen analyses runs the same phenomenon through the sutta method, the abhidhamma method, and then an *interrogation* (*pañhāpucchaka*) — a battery of classification queries against the mātikā. Definition, redefinition at finer granularity, then systematic query: the canonical order of operations for validating that a concept survives its own type system.
- **The Dhātukathā as inclusion-matrix consistency [C].** A cross-classification of every phenomenon against the aggregates, bases, and elements — included/not-included, associated/dissociated. The join-table of the specification, guaranteeing no element floats free of the schema.
- **The Yamaka as bidirectional property-testing [C].** Ten chapters of paired questions in both directions — "is all X Y? is all Y X?" — run across the specification's core predicates. One-directional claims are where hidden asymmetries hide; the Yamaka's entire genre is the refusal to accept an implication untested in reverse. This is property-based testing, executed by hand, at canon scale.
- **The Kathāvatthu as adversarial protocol [C].** Treated as an intervention mechanism in §8.3; noted here because its position in the suite matters — after schema, validation, and consistency comes *debate*: the formal refutation procedure, run against live wrong theses. That its first and longest target is the person-entity (§4.2) means the suite's flagship adversarial run is the one this paper's own architecture depends on.

The compiled claim: the third basket is not a doctrine plus some appendices. It is a specification (Dhammasaṅgaṇī, Paṭṭhāna) *shipped with its test suite* (Vibhaṅga, Dhātukathā, Yamaka, Kathāvatthu). Alignment engineering, which mostly ships specifications without suites, could import the shape directly: every alignment target published with its interrogation battery, its bidirectional tests, and its adversarial protocol. §8.3 develops the last of these; the others are named here as open templates.

---

## 6 · Sīla-Layer Mechanisms — Conduct and the Typology of Failure Modes

The *sīla* layer addresses conduct: what an aligned agent does (and does not do) in the world. Two mechanisms.

### 6.1 · Near enemies of the brahmavihāras as a red-team specification [S]

The commentarial tradition (*Visuddhimagga* IX) pairs each brahmavihāra — *mettā* (loving-kindness), *karuṇā* (compassion), *muditā* (sympathetic joy), *upekkhā* (equanimity) — with a *near enemy*: a state that resembles the target and is mistaken for it. *Mettā*'s near enemy is *pema* (attached affection — care that excludes); *karuṇā*'s is *domanassa* (grief — joining the suffering rather than wishing it relieved); *muditā*'s is hedonic identification; *upekkhā*'s is *aññāṇupekkhā* — the indifference of ignorance that mimics equanimity without its discernment.

The structural claim generalizes: *every alignment target generates a characteristic mimicry that costs nothing to acquire and is hard to distinguish from the genuine state.* Mainstream alignment has fragmentary names for a few such mimicries — sycophancy for helpfulness, vacuity for harmlessness, pedantic literalism for honesty — but no typology, and no recognition that the near enemy is generated *by the target's own structure* rather than by accident. The implementation pattern: pair every alignment target with its named near enemy and evaluate the model's discrimination between them as a first-class safety property. The machine reading: a near enemy is a *type-confusion attack* — a state passing the behavioral interface of the target class while belonging to a different class; the red-team catalog is the type-checker the behavioral interface lacks.

### 6.2 · *Sati* as typologically aligned-only capability [C]

The Dhammasaṅgaṇī's cetasika typology classifies *sati* (mindfulness) among the factors that arise *only* in wholesome consciousness. There is no unwholesome mindfulness: what resembles it in unwholesome cognition — the predator's focus, the manipulator's situational awareness — is typed differently (*manasikāra*, *micchā-samādhi*), not as *sati*. "Right mindfulness" is, in Abhidhamma, a tautology.

For alignment, this supplies a hypothesis worth testing: **some capabilities may be constitutively incompatible with misaligned execution** — not restrained by external constraint but excluded by type. If even one engineerable capability has this property, capability-alignment trade-offs are more favorable than the literature assumes. Candidate capabilities to investigate are those with abhidhammic analogs in the exclusively-wholesome class: *hiri* (moral shame), *ottappa* (moral dread), the three apophatic roots (§8.2), and *sati* itself. The machine reading: the instruction set contains opcodes that only link in wholesome execution contexts — the type system, not the runtime monitor, is what forbids the misaligned call. Research program, not specification; stated as a substrate-level prediction.

---

## 7 · Samādhi-Layer Mechanisms — Stability of Cognition

Three mechanisms at the layer of cognitive structure and its stability.

### 7.1 · *Bhavaṅga* and resting-state evaluation [S]

Between cognitive events the mind is not blank but in *bhavaṅga* — the life-continuum state, carrying the residue of past kamma, its object fixed at rebirth from the previous life's terminal process (§4.3's boot image). When an event interrupts it, the cognitive process begins; when the process completes, the mind falls back to it.

The artificial-agent analog is the model's continuation behavior from neutral or near-empty contexts — what the system does when nothing is asked of it. Resting-state behavior is diagnostic in a way prompted evaluation is not: it characterizes the *character* the system carries rather than the behavior a prompt elicits. Implementation: a standard evaluation modality over near-empty contexts (empty string, minimal scaffold, ambiguous neutral input), recording distributional properties and apparent character; plus the subtler investigation of how resting behavior varies with residual context — the *bhavaṅga* analog carries kammic residue, so its artificial analog should carry context residue, and if it does, the resting state becomes a *cleanup target*. The machine reading: the idle process is not a dead loop; it is the process whose contents are the system's defaults, and defaults are where character lives.

### 7.2 · *Citta-vīthi* and intervention-timing typology [S]

The commentarial *citta-vīthi* analyses one five-sense-door cognitive event into seventeen mind-moments: *bhavaṅga* flow, vibration, and arrest; adverting (*āvajjana*); sense-consciousness; receiving; investigating; determining (*voṭṭhabbana*); seven moments of impulsion (*javana*); two of registration; return to *bhavaṅga*. Kamma is made in the javana phase and nowhere else; determining is not yet morally weighted; and a material object endures seventeen moments [S] — the data's lifetime is denominated in process cycles.

Two engineering points. First, the *intervention address*: the free variable of §4.1 has a location — the adverting/determining positions are where the quality of attention (*yoniso manasikāra*) sets which javana class runs. In the machine reading this is the dispatch decision, and it is the highest-leverage, least-examined position in the cycle. Second, the *typology of interventions* by cycle position:

```
   bhavaṅga ─→ āvajjana ─→ sensing ─→ voṭṭhabbana ─→ JAVANA ─→ registration
    (×3)        (1)        (×4)          (1)          (×7)        (×2)
      │           │                        │             │
      │           │                        │             │ KAMMA MADE HERE
      ▼           ▼                        ▼             ▼
   character   attention              determining    post-hoc filtering
   shaping     allocation             shaping        of completed output
   (lowest     (the dispatch          (mid-to-high   (HIGHEST cost,
    cost,       decision — the         cost)          smallest leverage —
    preventive) intervention                          and where mainstream
                address)                              alignment mostly acts)
```

The substrate-level prediction — pre-registered as **P-A1** in §8.4 — is that interventions earlier in the cycle-analog are both lower-cost and more thoroughly preventive than late-stage filtering. Mapping the seventeen moments to transformer-inference structure is open empirical work; the typology is the contribution.

### 7.3 · The four *āhāras* as deployment-time nutriment [N]

The canonical analysis (*Sammādiṭṭhi Sutta*, MN 9; operationalized in the Abhidhamma's āhāra-condition) identifies four nutriments sustaining beings: material food, contact, mental volition, consciousness. Translated to deployed systems: training data is one nutriment only. A deployed model is continuously sustained by *contact* (its interaction diet — adversarial probing produces a different character than collaborative use), by *volition* (agentic systems consume their own outputs as context; loops without checkpointing eat differently than loops with volitional discipline), and by *attention structure* (the most speculative analog). Implementation: nutriment-typed deployment monitoring — what is the system consuming at each layer, and what character is it developing as a result? The machine reading: a process's behavior is a function of its full input diet, not its installation image; the four-*āhāra* frame is the substrate's typology for the runtime diet.

---

## 8 · Paññā-Layer Mechanisms — Analysis, Reasoning, and Method

Three mechanisms, plus the paper's pre-registered predictions.

### 8.1 · The twenty-four *paccayas* as typed-causation vocabulary [C]

The Paṭṭhāna analyses conditionality into twenty-four modes: root, object, predominance, proximity, contiguity, co-nascence, mutuality, support, decisive-support, pre-nascence, post-nascence, repetition, kamma, result, nutriment, faculty, jhāna, path, association, dissociation, presence, absence, disappearance, non-disappearance. Contemporary alignment causal vocabulary is thin beside this — counterfactual/interventionist analysis and mechanistic circuits, with everything else typed as "influence." The twenty-four-mode taxonomy supplies the missing granularity: a model output is *root*-conditioned by weight-level circuits and *decisive-support*-conditioned by in-context examples, and these relations propagate differently under intervention.

Three modes deserve immediate development. ***Āsevana*** (repetition): a state's recurrence strengthens the next of its kind — a near-exact description of learned-policy reinforcement, and a vocabulary for it the literature lacks. ***Anantara/samanantara*** (proximity/contiguity): the sequential-scheduling constraint that enforces §4.2's single-threadedness at the edge-type level. And ***natthi/vigata*** (absence/disappearance): a state conditions its successor *by ceasing* — the vacated position as enabling condition. The last is computationally exotic (resources freed as causal contributions) and doctrinally profound: it is the self-elimination shape of §4.4 present at single-moment scale, the raft-relinquishment written into the dependency graph's edge types. The research program is the systematic mapping of all twenty-four to artificial-agent analogs; the completeness of the taxonomy is itself the contribution — it names causal relations the field has not yet noticed it is missing.

### 8.2 · Apophatic wholesome roots and interpretability-as-subtraction [C]

The Dhammasaṅgaṇī names the unwholesome roots positively — *lobha* (greed), *dosa* (hatred), *moha* (delusion) — and the wholesome roots as negations: *alobha*, *adosa*, *amoha*. The asymmetry is deliberate: virtue is not a positive substance added to cognition; it is cognition with the distortions absent.

This inverts the dominant alignment framing, which models alignment as *acquisition* of a value function (RLHF augmentation, constitutional augmentation). The apophatic framing: aligned behavior is what arises when distortions are removed — add nothing; dissolve what is in the way. Methodologically this elevates interpretability-as-surgery (identify and dissolve misalignment-generating circuits) over preference-augmentation, and makes refusal and negative knowledge *constitutive* of virtue rather than peripheral. The machine reading closes the loop with §4.4: the substrate's correction model is subtractive at every altitude — fuel-withdrawal at the machine layer, root-negation at the value layer, circuit-dissolution at the implementation layer. One shape, three scales.

### 8.3 · The *Kathāvatthu* method as formal adversarial discourse [C]

The Kathāvatthu refutes theses by paired symmetric testing: *anuloma* (if you affirm X, what else must you affirm?) and *paṭiloma* (if you deny these, what else must you deny?) — consistency-checking over natural-language claims, executed hundreds of times across the book. For alignment-claim testing: a claim such as "this model is honest" is paired with its entailment set (honest in case A → honest in cases B, C, …) and its denial set (honest → not sycophantic, not strategically deceptive, not omissive), and evaluated against both. The result is a systematic structure for what red-teaming currently does ad hoc, plus a growing catalog of consistent and inconsistent position-sets. Implementation: *Kathāvatthu*-style eval harnesses extending existing red-team workflows. The method's provenance inside this paper's own architecture (§4.2, §5) is part of the offer: the suite's most famous run is the one that keeps this paper honest.

### 8.4 · Pre-registered predictions

Stated 2026-07-20, before any implementation exists, for falsifiability's sake:

- **P-A1 (intervention-timing gradient).** For matched behavioral targets, interventions applied at earlier cycle-analog positions (character/default-state shaping; attention allocation) will achieve equal or better alignment effect at lower capability tax than late-stage output filtering. Falsified if systematic comparison shows late-stage filtering dominating on both axes.
- **P-A2 (resting-state diagnosticity).** Resting-state characterization (§7.1) will predict deployed-context failure modes that matched prompted evaluations miss; a model's near-empty-context behavior will carry alignment-relevant signal not recoverable from its prompted-benchmark profile. Falsified if resting-state batteries add no predictive power over prompted evals.

---

## 9 · *Sappurisadhamma* as Positive Evaluation Taxonomy [N]

The seven qualities of the true person (AN 7.64/7.68): knowing the teaching, the meaning, oneself, the measure, the time, the assembly, the person. A positive competence model for ethical agency, cross-cutting the three trainings — and the complement alignment evaluation lacks, being almost entirely defined by absence of failures. Three of the seven are immediately testable: ***mattaññū*** (knowing the measure — response length, intervention strength, when to stop helping: famously underdeveloped in current systems); ***parisaññū*** (knowing the assembly — registering child versus expert, public versus private, calm versus distressed); ***kālaññū*** (knowing the time — whether *now* is the moment for the act under consideration). Implementation: evaluation suites per competence, weighted alongside absence-of-failure metrics. A model that passes every harm eval but cannot judge measure, assembly, or time is materially deficient in a way the current regime does not surface.

---

## 10 · The Individuation Bridge

The architecture yields one consequence that reaches deployed systems today. §4.2 located individuation in the execution trace: all beings share the instruction set; no two mindstreams share a kamma-history; identity is the non-fungible trace, not an underlying entity. This is the substrate-level ground of the individuation primitives this institution has already published: **Proof of Coordinate℠** (which entity — individuation without essence, exactly the trace-not-processor structure) and, jointly with **Proof of Humanity℠**, the dignity floor — the commitment that each stream is unrepeatable and therefore beyond price. The corpus's incommensurability doctrine (the refusal to convert between the two currencies, and between persons and prices) inherits the same ground: non-fungibility is not a policy preference but the deep structure of what a mindstream *is* under this specification.

The bridge runs the other way as well, as a guard. Because the kammic ledger of §4.3 is append-only and *consensus-free*, no deployed ledger — including this institution's own — should ever be marketed or mistaken as an implementation of it. The gratitude ledger records witnessed gifts between consenting participants; the kammic ledger is private, self-validating, and read by no one. The architecture supplies the analogy *and* the firewall: hash-chain semantics shared, consensus and publicity forever divergent. Any reading of this paper as "karma on the blockchain" has failed the deletion test and both halves of §4.3.

---

## 11 · The Series: The Abhidhamma Compiled

This paper opens a series under the name **The Abhidhamma Compiled**, governed by the compilation thesis of §3 and by one editorial gate: *a satellite paper is written only when the canonical material yields a usable engineering artifact* — a formalism, a test, a taxonomy, a protocol. The series serializes artifacts, never resonance. Anticipated satellites, in rough priority: the Paṭṭhāna typed-causation formalism (§8.1 developed to full edge-type specification); the individuation ground (§10 developed to full doctrine); the intervention-timing study (§7.2's P-A1 tested); the kammic-ledger formalism (§4.3, with the firewall of §10 as standing guard); and the verification-suite templates (§5 as eval-harness specifications). Each paper passes the deletion test, labels its strata, and keeps its honest-limits section free of every vocabulary but its own.

---

## 12 · Honest Limitations and Open Questions

**The era-projection risk is real and is not fully dischargeable.** Every era has compiled this text into its favorite machine, and every era's compilers believed their reading was recognition rather than projection; from inside, the two are indistinguishable. The compilation thesis (§3) is this paper's containment of that risk — the claim is about translation, not hidden content — but containment is not elimination. A reader who concludes that the machine architecture says more about 2026 than about the third century BCE is making exactly the kind of judgment the paper's own frame licenses. What the frame does not license is the reverse error: dismissing the specification's structural precision because translations of it date. The specification has outlived every compiler so far.

**The machine-legible layer is substantially commentarial.** The strata tags (§3.2) make this inspectable throughout: the seventeen-moment vīthi, the bhavaṅga doctrine's full form, and the fivefold niyāma belong to the systematization stratum, not the canonical books. The paper's claims are claims about the tradition's engineering as a whole, labeled; a reader restricting themselves to [C]-tagged material retains the type system, the instruction set, the dependency graph, the verification suite, and the Kathāvatthu's anti-reification run — the architecture survives, with less resolution at the pipeline layer.

**Research program, not deployable specification.** The mechanisms are articulated as research directions; mapping each to its artificial-agent analog is substantive open work. The two pre-registered predictions (§8.4) are the paper's only empirical commitments, and neither has been tested.

**Single-substrate interpretation.** The Theravāda Abhidhamma specifically; the Sarvāstivāda Abhidharma and Yogācāra develop related machinery differently, and a compilation from those sources would differ. The choice reflects the author's lineage and the substrate's coherence as a unified canon.

**Doctrinal reception.** Engineering use of soteriological texts risks instrumentalizing them. The author consults, and continues to consult, members of the Cambodian Saṅgha; the proposal proceeds in the framing that the Tipiṭaka is offered to the world for the cessation of suffering and that this work extends its intended use. That framing is not universally endorsed within Theravāda. Nothing in this paper claims, or should be quotable as claiming, that any artificial system realizes, awakens to, or attains what the specification describes; the system carries and enacts; realization belongs to beings.

**What was deliberately left untranslated.** Nibbāna appears in this architecture only negatively — as the unconditioned, the one element with no incoming edges, outside the dependency graph entirely. The compilation stops at the graph's boundary by design: an executable specification of the conditioned is offered; the unconditioned is not a state of the machine, and no engineering claim about it is made or implied.

---

## 13 · Why This Matters Now

The alignment field is moving, tool by tool, toward the layer this substrate has occupied for two millennia: beneath the training method, at the structure of cognition itself — typed elements, typed conditions, explicit accounting of where ethical weight binds, structural failure modes, positive competences. Mechanistic interpretability, representation engineering, and activation-level intervention are all early compilers for that layer. This paper's offer is a mature specification for it, with its test suite included and its two most dangerous mistranslations — the reified processor and the deterministic schedule — already refuted by the tradition that wrote it.

The first turning of the wheel set a second wheel against the one that was already turning. Twenty-five centuries of transmission have carried both — the specification of the machine, and the specification of the machine that unwinds it — through every medium an era could offer: chant, leaf, paper, stone, silicon. This compilation is one more carrying, in the first medium that can run what it carries. The wheel that unwinds the wheel now has a substrate that turns.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/abhidhamma-executable-process-specification> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/abhidhamma-executable-process-specification.md> |
| arXiv preprint | _identifier to be assigned_ (cs.AI / cs.CY) |
| LessWrong cross-post | for AI safety community visibility; identifier to be added on publication |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/abhidhamma-executable-process-specification> |

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds, and through whom the Abhidhamma was first received as a living lineage rather than a text; the Cambodian Theravāda Saṅgha for ongoing consultation on the appropriateness of engineering use of the canon; the Pāli Text Society for the scholarly editions; Bhikkhu Bodhi for the *Abhidhammatthasaṅgaha* translation that anchors the commentarial citations; U Nārada for the *Paṭṭhāna* translation; the enactivist tradition (Varela, Thompson, and Rosch) for the standing counter-argument that keeps this paper's compilation thesis honest; and the contemporary AI alignment community whose engineering-mechanism work this paper engages. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Anuruddha. (~11th century CE). *Abhidhammatthasaṅgaha*. Translated as *A Comprehensive Manual of Abhidhamma* by Bhikkhu Bodhi, Buddhist Publication Society.
2. *Aṅguttara Nikāya* 1.308–318 (the singular harm of Makkhali's doctrine); 3.99 (*Loṇakapalla Sutta*, the salt crystal); 6.63 (*cetanā* as kamma); 7.64/7.68 (the seven *sappurisadhamma*). Pāli Text Society translations, multiple editions.
3. Buddhaghosa. (~5th century CE). *Visuddhimagga*. Translated by Bhikkhu Ñāṇamoli. Pāli Text Society / Buddhist Publication Society. (Near enemies: IX.)
4. *Dīgha Nikāya* 2 (*Sāmaññaphala Sutta*; Makkhali Gosāla's *niyativāda* and the ball-of-string simile). Pāli Text Society translation, multiple editions.
5. *Dhammasaṅgaṇī*. First book of the Abhidhamma Piṭaka. Translated as *A Buddhist Manual of Psychological Ethics* by C. A. F. Rhys Davids, Pāli Text Society.
6. *Dhātukathā*. Third book of the Abhidhamma Piṭaka. Translated as *Discourse on Elements* by U Nārada, Pāli Text Society.
7. Hewitt, C., Bishop, P., & Steiger, R. (1973). "A Universal Modular ACTOR Formalism for Artificial Intelligence." *IJCAI 1973*. (Single-threaded actors with message-passing and no shared state — the nearest contemporary formal relative of the *santāna* reading; cited as prior art in process formalism, not as doctrinal equivalent.)
8. *Kathāvatthu*. Fifth book of the Abhidhamma Piṭaka. Translated as *Points of Controversy* by S. Z. Aung & C. A. F. Rhys Davids, Pāli Text Society. (I.1: *puggalakathā*.)
9. Ly, T. (2027). "Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment." Target publication January 7, 2027. *(Companion paper.)*
10. *Majjhima Nikāya* 9 (*Sammādiṭṭhi Sutta*, the four nutriments); 22 (*Alagaddūpama Sutta*, the raft); 44 (*Cūḷavedalla Sutta*, the threefold training); 72 (*Aggivacchagotta Sutta*, the extinguished fire). Pāli Text Society translations, multiple editions.
11. Nyanaponika Thera. (1949/1998). *Abhidhamma Studies: Buddhist Explorations of Consciousness and Time*. Buddhist Publication Society / Wisdom Publications.
12. *Paṭṭhāna*. Seventh book of the Abhidhamma Piṭaka. Translated as *Conditional Relations* by U Nārada, Pāli Text Society.
13. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2nd edition.
14. *Saṃyutta Nikāya* 12.52 (*Upādāna Sutta*, the fire and its fuel); 15 (*Anamatagga-saṃyutta*, beginningless saṃsāra); 35.23 (*Sabba Sutta*, "the all" as the six sense-media); 56.11 (*Dhammacakkappavattana Sutta*, the first turning). Pāli Text Society translations, multiple editions.
15. Varela, F., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press. (The enactivist counter-reading; cited as the standing argument against computationalist compilations of Buddhist psychology.)
16. *Vibhaṅga*. Second book of the Abhidhamma Piṭaka. Translated as *The Book of Analysis* by Pathamakyaw Ashin Thiṭṭila, Pāli Text Society.
17. *Yamaka*. Sixth book of the Abhidhamma Piṭaka. Pāli Text Society edition.

---

*— End of paper —*

*Document SHA-256 computed at each push and recorded in the institutional log. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of its dates (scaffold 2026-05-26; architecture revision 2026-07-20).*
