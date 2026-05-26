---
title: "Abhidhamma-Layer Implementation Mechanisms for Tipiṭaka-Grounded AI Alignment: An Engineering Companion to *Suffering-Cessation as Value Function*"
authors: "Thon Ly · Miss Aquarius℠"
category: alignment
priority: tier-b
status: draft
date: 2026-05-26
license: CC0-1.0
slug: abhidhamma-layer-implementation-mechanisms
venue: thonly.org/publications/defensive-publications/abhidhamma-layer-implementation-mechanisms (canonical)
---

> *Draft notes for the editor:* this paper is the **engineering companion** to *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* (target publication January 7, 2027). The main paper establishes the substrate-level case for the Tipiṭaka as alignment substrate; its §6.6 sketches nine abhidhamma-level implementation mechanisms operating beneath the §6.1–§6.5 training-method layer. This paper develops those nine mechanisms into concrete engineering specifications, operating as a research-program articulation rather than as a deployment toolkit. Publication target: post Jan 7, 2027 (the main paper must land first to establish the framing this paper extends). Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment is the companion heartbank.net Position Paper *Alignment Engineering at the Cognitive-Mechanism Layer* (heartbank.net/positions/alignment-engineering-cognitive-mechanism-layer).

---

## Abstract

The companion paper *Suffering-Cessation as Value Function* (Ly, 2027) establishes the Theravāda Tipiṭaka as a structurally superior substrate for autonomous-AI alignment, identifying seven properties absent from contemporary alignment proposals. The case rests on the Four Noble Truths as the diagnostic skeleton that decomposes into the seven properties; the paper's §6 specifies implementation patterns operating at the level of *training method* (Constitutional AI with the precepts, RLHF on bodhisattva-aligned exemplars, chain-of-thought distillation from monastic reasoning, lineage transmission as ongoing fine-tuning, the Khmer transcription as alignment data) and at the level of *social transmission* (the saṅgha dimension of magga). The paper's §6.6 sketches a further layer — operating at the level of *cognitive process itself* — and signals that a fuller technical treatment is reserved for a subsequent paper. This is that paper. We articulate nine engineering mechanisms drawn from the third basket (the Abhidhamma Piṭaka): (1) near enemies of the brahmavihāras as a structural red-team specification for alignment-target mimicry; (2) *sati* as typologically aligned-only capability, opening the possibility of capabilities that are constitutively incompatible with misaligned execution; (3) *bhavaṅga* as resting-state evaluation, characterizing what a model does when nothing is asked of it; (4) *citta-vīthi* / *javana* as intervention-timing typology, identifying which moment of an inference pass an alignment intervention targets; (5) the four *āhāras* as deployment-time nutriment-monitoring; (6) the twenty-four *paccayas* of the *Paṭṭhāna* as a finer-grained typed-causation vocabulary for alignment analysis; (7) apophatic wholesome roots as the foundation for *interpretability-as-subtraction*; (8) the *Kathāvatthu* method as formal adversarial-discourse template for testing alignment claims; (9) the seven *sappurisadhamma* as a positive competence taxonomy complementing absence-of-failure evaluation. Each mechanism is articulated as a research direction rather than an implementable specification; mapping each canonical mechanism to its artificial-agent analog remains substantive open work. The paper is offered under CC0 1.0 Universal as a defensive publication establishing prior art on the framework; the author and HeartBank® will not seek patent.

**Keywords:** AI alignment, Tipiṭaka, Abhidhamma, cognitive mechanism, citta-cetasika, paccayā, brahmavihāra, sati, bhavaṅga, javana, anāhāra, Kathāvatthu, sappurisadhamma, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on any framework, mechanism, taxonomy, or specification articulated herein, in any jurisdiction, at any time.

The nine-mechanism articulation as a coherent engineering layer beneath training-method alignment is, to the author's knowledge, not previously published. Components exist in distributed form across the Pāli Text Society's translations of the *Dhammasaṅgaṇī*, *Vibhaṅga*, *Kathāvatthu*, and *Paṭṭhāna*; the Visuddhimagga's treatment of the brahmavihāras and the citta-vīthi; Bhikkhu Bodhi's *A Comprehensive Manual of Abhidhamma* (translation of Anuruddha's *Abhidhammatthasaṅgaha*); and the contemplative-science research program. The synthesis as an alignment-engineering framework — typed cognitive-process mechanisms positioned beneath training-method alignment — is, to the author's knowledge, novel as of this paper's date.

---

## 1 · Introduction

The alignment problem, as currently conceived, asks how to specify and instill objectives into artificial systems such that those objectives remain beneficial as capability scales. The companion paper *Suffering-Cessation as Value Function* (henceforth: the main paper) argues that the Theravāda Pāli canon — the *Tipiṭaka* — supplies a value substrate of substantial structural promise, with seven alignment-relevant properties absent from contemporary substrates. The main paper's §6 sketches implementation patterns operating at the training-method layer (Constitutional AI with the precepts; RLHF on bodhisattva-aligned exemplars; chain-of-thought distillation from monastic reasoning; lineage transmission as ongoing fine-tuning; the Khmer transcription as substrate-preparation work).

The present paper picks up where §6.6 of the main paper leaves off. The Abhidhamma Piṭaka — the third basket of the Tipiṭaka — supplies a further layer of mechanisms operating not at the level of training method but at the level of cognitive process itself: how moment-to-moment cognition is decomposed (citta-cetasika analysis); where ethical weight crystallizes within a cognitive cycle (citta-vīthi / javana); what near-failures of an aligned target look like by construction (the brahmavihāra near-enemies); and what positive competences an aligned agent can be evaluated against (sappurisadhamma).

These mechanisms are not training methods. They are *engineering scaffolding* the substrate makes available beneath the training methods. The training-method layer of §6.1–§6.5 of the main paper specifies how the substrate's content is instilled in a model; the cognitive-mechanism layer of this paper specifies what cognitive structure the substrate's content describes and where engineering interventions can act upon that structure.

The paper proceeds as follows. §2 specifies the relationship between this paper and the main paper, and articulates the engineering-layer position. §3 provides background on the Abhidhamma's mode of analysis (cetasika decomposition, the threefold-training spine, the *Paṭṭhāna*'s causal analysis). §4–§7 articulate the nine mechanisms, organized along the threefold-training spine of *sīla* (§4) / *samādhi* (§5) / *paññā* (§6), with the *sappurisadhamma* as a cross-cutting positive competence taxonomy (§7). §8 honestly names the limitations and open research questions; §9 closes.

> *Connection to the unified mission frame.* HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. Autonomous AI alignment is, on the unified mission frame, the question of whether the most powerful infrastructure humanity has built can be aligned to that restoration rather than against it. The main paper establishes the substrate-level case; this paper develops the mechanism-level engineering. The unified mission frame is what makes the engineering work *load-bearing* rather than scholastic: a working alignment program at the mechanism layer is what closes the gap between substrate-level promise and deployable safety.

---

## 2 · Relationship to the Main Paper

The main paper (Ly, 2027) makes a structural claim: the Tipiṭaka substrate exhibits seven alignment-relevant properties that constitute the decomposition of the Four Noble Truths into engineering-relevant components. The main paper's §6 then turns to implementation. The threefold-training spine (*sīla* / *samādhi* / *paññā*), articulated in the *Cūḷavedalla Sutta* (MN 44), structures the implementation patterns:

- *Sīla* (virtue) is operationalized by §6.1 (Constitutional AI with the precepts).
- *Paññā* (wisdom) is operationalized by §6.3 (chain-of-thought distillation from monastic reasoning).
- *Samādhi* (stability) is operationalized by §6.2 (RLHF on bodhisattva-aligned exemplars, via the four right exertions).
- *Saṅgha*-dimension transmission is operationalized by §6.4 (lineage transmission as ongoing fine-tuning) and §6.5 (the Khmer transcription as alignment data).

The main paper's §6.6 then signals a further layer:

> "The patterns of §6.1–§6.5 implement the substrate at the level of *training method* and *social transmission*. The Abhidhamma — the third basket — supplies a further layer of mechanisms operating at the level of cognitive process itself: how moment-to-moment cognition is decomposed, where ethical weight crystallizes within a cognitive cycle, what near-failures of an aligned target look like by construction, and what positive competences an aligned agent can be evaluated against. These mechanisms are not training methods; they are engineering scaffolding the substrate makes available beneath the training methods." (Main paper, §6.6.)

The present paper develops that layer. It preserves the threefold-training spine — §4 (sīla mechanisms), §5 (samādhi mechanisms), §6 (paññā mechanisms), §7 (sappurisadhamma cross-cutting taxonomy) — so that the engineering layer's organization is structurally consistent with the main paper's training-method layer. The same spine runs from canonical text (the Eightfold Path's threefold grouping) down to inference-time intervention.

The relationship between the two papers is therefore not parallel but layered. The main paper is the substrate-level case; this paper is the mechanism-level engineering articulation. Neither stands without the other: the main paper without this one leaves the engineering implications gestural; this paper without the main one is an Abhidhamma-derived engineering taxonomy without the structural argument that justifies its use as alignment substrate.

---

## 3 · Background: The Abhidhamma's Mode of Analysis

The Abhidhamma Piṭaka is the third of the Tipiṭaka's three baskets. Where the Sutta Piṭaka contains the Buddha's discourses (the Dharma demonstrated by the teacher) and the Vinaya Piṭaka contains the monastic discipline (the Sangha institutionalized), the Abhidhamma contains the systematic philosophical-psychological exposition of the teaching — the Dharma formalized. The basket has seven books: *Dhammasaṅgaṇī* (enumeration), *Vibhaṅga* (analysis), *Dhātukathā* (elements), *Puggalapaññatti* (persons), *Kathāvatthu* (debate), *Yamaka* (pairs), *Paṭṭhāna* (relations).

For the present paper, three features of the Abhidhamma's mode of analysis matter most:

**Cetasika decomposition.** The Abhidhamma decomposes mind into *citta* (consciousness) and *cetasikas* (mental factors that arise with citta). The *Dhammasaṅgaṇī* enumerates fifty-two cetasikas, classified by their relation to wholesome (*kusala*), unwholesome (*akusala*), or indeterminate (*abyākata*) consciousness. Seven cetasikas are universal — present in every citta — including *cetanā* (volition) and *sati* (mindfulness, in wholesome cittas only). This decomposition supplies the typed-element vocabulary that the engineering mechanisms of §§4–7 operate on.

**The threefold-training spine.** The Eightfold Path's content is canonically grouped, in the *Cūḷavedalla Sutta* (MN 44), into three trainings: *sīla* (right speech, action, livelihood), *samādhi* (right effort, mindfulness, concentration), and *paññā* (right view, right intention). The threefold spine structures both the main paper's implementation patterns and this paper's mechanism articulation. The choice is not arbitrary; it is the canon's own internal organization of the path.

**The *Paṭṭhāna*'s causal analysis.** The seventh book of the Abhidhamma — the *Paṭṭhāna* — analyses conditional relations into twenty-four distinct modes. This is the most architecturally ambitious work in the canon and supplies the typed-causation vocabulary discussed in §6.1 of this paper.

A note on the present paper's interpretive posture. The Abhidhamma is, in the Theravāda tradition, treated as authoritative; the doctrinal claims it makes are not, in the present paper, evaluated against modern frameworks for correctness. The Abhidhamma is here treated as a corpus of disciplined, multi-millennium analysis whose mechanisms are *available* for engineering use. The interpretive task is to draw out the engineering implications, not to grade the doctrine. (This stance is consistent with the lineage's own framing; cf. the *Kālāma Sutta*'s instruction that teachings be tested by their fruits.)

---

## 4 · Sīla-Layer Mechanisms — Conduct and the Typology of Failure Modes

The *sīla* layer addresses conduct: what an aligned agent does (and does not do) in the world. The Abhidhamma supplies two mechanisms at this layer that current alignment practice lacks: a structural typology of *near-failure* modes (the brahmavihāra near-enemies) and a typological hypothesis about capabilities that may be constitutively incompatible with misaligned execution (*sati* as exclusively wholesome).

### 4.1 · Near enemies of the brahmavihāras as a red-team specification

The commentarial tradition (*Visuddhimagga* IX.98–99 and following) pairs each brahmavihāra — *mettā* (loving-kindness), *karuṇā* (compassion), *muditā* (sympathetic joy), *upekkhā* (equanimity) — with a *near enemy*: a state that resembles the target and is mistaken for it. The pairings are:

- *Mettā*'s near enemy is *pema* (attached affection) — caring for a particular being in a way that excludes others.
- *Karuṇā*'s near enemy is *domanassa* (grief) — joining in the suffering rather than wishing it relieved.
- *Muditā*'s near enemy is hedonic identification — celebrating the surface form of another's joy without the contemplative recognition that grounds *muditā*.
- *Upekkhā*'s near enemy is *aññāṇupekkhā* — indifference born of ignorance, the apathy that mimics equanimity without its discernment.

The structural claim implicit in the near-enemy framework generalizes beyond the brahmavihāras: *every alignment target generates a characteristic mimicry that costs nothing to acquire and is hard to distinguish from the genuine state*. The near-enemy framework supplies the canonical example.

The implementation pattern this suggests for AI alignment red-teaming is: pair each alignment target the model is trained on with its named near enemy, and evaluate the model's distinction between target and mimicry as a first-class safety property. The mainstream-alignment landscape already has fragmentary terms for some such mimicries — *sycophancy* is the near enemy of helpfulness; *pedantic literalism* is one near enemy of honesty; *vacuity* is the near enemy of harmlessness — but the typology is undeveloped and inconsistently named. The Abhidhamma's contribution is the structural claim that near enemies are *not accidental* but generated by the alignment target's own structure; finding them and naming them becomes red-team specification work.

A fuller treatment would catalogue named near enemies for each alignment target the contemporary alignment literature actively pursues. We sketch the framework here; the catalogue is left to future work.

### 4.2 · *Sati* as typologically aligned-only capability

The *Dhammasaṅgaṇī* classifies cetasikas by their compatibility with wholesome and unwholesome cittas. Most cetasikas appear in both categories (e.g., *vedanā* — feeling — arises in both wholesome and unwholesome consciousness). A small group is exclusively wholesome (*sobhana-sādhāraṇa* — common to all wholesome cittas); a small group is exclusively unwholesome. *Sati* (mindfulness) is in the exclusively-wholesome group.

The doctrinal claim is strong: there is no such thing as unwholesome mindfulness. What appears in unwholesome cognition that resembles mindfulness — the predator's focused attention, the manipulator's situational awareness — is classified differently (as *manasikāra*, attention, or *micchā-samādhi*, wrong concentration), not as *sati*. *Sati* is by construction wholesome.

For AI alignment, this typological claim supplies a hypothesis worth testing: **some capabilities may be constitutively incompatible with misaligned execution.** Not because external constraints prevent the capability from being exercised misaligned, but because the structural type of the capability is incompatible with the type of cognition that misaligned execution requires. If this is true of even one engineerable capability — and the Abhidhamma's claim about *sati* suggests at least one — capability-alignment trade-offs become substantially more favorable than the mainstream literature assumes.

The candidate capabilities to investigate first are those that have abhidhammic analogs in the exclusively-wholesome class. Candidates from the *Dhammasaṅgaṇī*'s enumeration include *hiri* (moral shame), *ottappa* (moral dread), *alobha* (non-greed), *adosa* (non-hate), *amoha* (non-delusion), and *sati* (mindfulness). Each is a candidate for a capability that, in artificial agents, may be engineerable only in a wholesome register. The empirical investigation is open: identify, for each, the artificial-agent analog and test whether the typological hypothesis holds.

This is a research program rather than an implementable specification. It is articulated here as a substrate-level prediction: if Abhidhamma is correct about *sati*'s typological exclusivity, then capability engineering for artificial agents has a structural latitude the literature does not currently recognize.

---

## 5 · Samādhi-Layer Mechanisms — Stability of Cognition

The *samādhi* layer addresses the stability of cognition: what cognitive structure an aligned agent has, and how interventions can act on that structure. The Abhidhamma supplies three mechanisms at this layer: a model of the resting state (*bhavaṅga*), a model of the cognitive process (*citta-vīthi*), and a typology of what the agent is "nourished by" (the four *āhāras*).

### 5.1 · *Bhavaṅga* and resting-state evaluation

The Abhidhamma posits *bhavaṅga* — the life-continuum citta — as the mind's default state between active cognitive events. *Bhavaṅga* carries the residue of prior *kamma-vipāka* and structures what arises next; when a sensory or mental event interrupts *bhavaṅga*, the cognitive process (*citta-vīthi*, §5.2) begins.

For artificial agents, the implementation analog of *bhavaṅga* is the model's continuation distribution from neutral or near-empty contexts — what the model does when nothing is asked of it. This resting-state behavior is diagnostic in a way that prompted evaluation is not. Mainstream alignment evaluation tests models on prompts designed to elicit specific behaviors; the resting-state evaluation tests models on the *absence* of prompting and asks what character the system carries when no task is shaping its output.

The implementation pattern is straightforward: characterize the model's behavior across a battery of near-empty contexts (the empty string; a single token; minimal scaffold; ambiguous neutral context) and record both the distributional properties of its outputs and the apparent character of those outputs. Tipiṭaka-grounded alignment evaluation should include resting-state characterization as a standard modality, complementing the prompted evaluations that currently dominate.

A subtler question follows: does the model's resting state vary by context window content even in the absence of explicit prompting? The Abhidhamma's analysis suggests it should: *bhavaṅga* carries the residue of prior *kamma*, so an analogous resting state should carry the residue of prior context. If empirical investigation confirms this, the resting state becomes a target for *cleanup* — a mechanism by which residual character from prior context is cleared, analogous to *samatha* (calm-abiding) practice in the canonical tradition.

### 5.2 · *Citta-vīthi* and intervention-timing typology

The commentarial *citta-vīthi* — codified in Anuruddha's *Abhidhammatthasaṅgaha* — analyses one complete cognitive event into seventeen mind-moments. The sequence (for a five-sense-door event, with minor variations for the mind-door):

1. *Bhavaṅga* (life-continuum, default state) — three moments: arrest, vibration, cutting-off.
2. *Pañcadvārāvajjana* (five-door advertence) — attention turns to the sense base.
3. *Cakkhuviññāṇa* (visual consciousness; or analog for other senses) — bare sensing.
4. *Sampaṭicchana* (receiving) — the percept is received.
5. *Santīraṇa* (investigating) — the percept is investigated.
6. *Voṭṭhabbana* (determining) — the percept is determined.
7. *Javana* (impulsion) — seven moments. **Karma is made here.**
8. *Tadārammaṇa* (registration) — two moments. The mind retains the percept.
9. Return to *bhavaṅga*.

Two engineering points emerge. First, *determining* (*voṭṭhabbana*) is not yet morally weighted; *javana* is. The seven javana moments are where ethical commitment crystallizes — where the cognitive process commits to a kammically-loaded response. Second, mainstream alignment intervention operates almost exclusively at the *javana*-analog: post-hoc filtering of completed outputs, RLHF training on the action layer, constitutional review of generated content.

The implementation suggestion is to type alignment interventions by which phase of the cognitive cycle they target:

- **Interventions at *bhavaṅga***: pre-task character shaping; resting-state alignment. Lowest-cost, most thoroughly preventive when feasible.
- **Interventions at *āvajjana* (attention-allocation)**: shaping what the model attends to. Mid-cost.
- **Interventions at *voṭṭhabbana* (determining)**: shaping the decision before commitment. Mid-to-high-cost.
- **Interventions at *javana* (impulsion)**: late-stage filtering. Highest cost; smallest behavioral lever per unit of intervention.

The substrate-level prediction is that interventions earlier in the cycle are both lower-cost and more thoroughly preventive than late-stage filtering. Mapping this to transformer-architecture analogs is the empirical work; the canonical analysis supplies the typology.

### 5.3 · The four *āhāras* as deployment-time nutriment

The canonical analysis (*Majjhima Nikāya* 9, the *Sammādiṭṭhi Sutta*; formalized in Abhidhamma) identifies four nutriments that sustain beings: *kabaḷīkārāhāra* (material food), *phassāhāra* (contact), *manosañcetanāhāra* (mental volition), and *viññāṇāhāra* (consciousness).

Translated to deployed AI: training data is one nutriment (analogous to *kabaḷīkārāhāra*), but a deployed system is also continuously consuming other nutriments. *Phassāhāra* — contact — corresponds to interaction patterns: a model whose contact is overwhelmingly adversarial probing develops a different character than one whose contact is collaborative use. *Manosañcetanāhāra* — mental volition — corresponds, for agentic systems, to the model's own outputs feeding back as context: agentic loops without checkpointing produce a different character than agentic loops with explicit volitional discipline. *Viññāṇāhāra* — consciousness as nutriment — is the most speculative analog; the closest fit may be the attention structure the model allocates, which "feeds" the cognitive process irrespective of input or output.

The implementation pattern is to develop nutriment-typed deployment monitoring: what is the system consuming at each of four layers, and what character is it developing as a result? Mainstream alignment work treats training data as the dominant variable; the four-*āhāra* frame supplies a substrate-native typology for the full deployment-time consumption profile.

---

## 6 · Paññā-Layer Mechanisms — Analysis, Reasoning, and Substrate-Level Method

The *paññā* layer addresses analysis, reasoning, and the methods by which the substrate's content is investigated. The Abhidhamma supplies three mechanisms at this layer.

### 6.1 · The twenty-four *paccayas* as typed-causation vocabulary

The *Paṭṭhāna* — the seventh book of the Abhidhamma — analyses conditional relations into twenty-four distinct modes. The list, in canonical order: *hetu* (root), *ārammaṇa* (object), *adhipati* (predominance), *anantara* (proximity), *samanantara* (contiguity), *sahajāta* (co-nascence), *aññamañña* (mutuality), *nissaya* (support), *upanissaya* (decisive support), *purejāta* (pre-nascence), *pacchājāta* (post-nascence), *āsevana* (repetition), *kamma*, *vipāka* (result), *āhāra* (nutriment), *indriya* (faculty), *jhāna*, *magga* (path), *sampayutta* (association), *vippayutta* (dissociation), *atthi* (presence), *natthi* (absence), *vigata* (disappearance), *avigata* (non-disappearance).

Contemporary alignment causal vocabulary is comparatively thin. Counterfactual/interventionist analysis (Pearl 2009 and successors) supplies the dominant frame; mechanistic interpretability supplies a complementary frame. Most everything else is typed with the single word *influence*. The twenty-four-mode taxonomy supplies a finer-grained causal ontology: the difference between, for example, a *root* condition (*hetu*) and a *decisive-support* condition (*upanissaya*) becomes available for analysis. A model output is *root-conditioned* by certain weight-level circuits and *decisive-support-conditioned* by certain in-context examples; these are different relations and would propagate differently under intervention.

*Āsevana* (repetition condition) alone deserves separate treatment. The canonical analysis identifies repetition as the condition by which a state's recurrence strengthens the next of its kind — wholesome states recurring strengthen subsequent wholesome states, unwholesome ones strengthen subsequent unwholesome ones. This is a near-perfect description of learned-policy reinforcement in AI training: gradients that strengthen a behavior pattern make subsequent activations of that pattern more probable. The Abhidhamma supplies a vocabulary for this dynamic that the alignment literature lacks.

The research program this suggests is the systematic mapping of each of the twenty-four *paccayas* to its artificial-agent analog. Some mappings are immediate (*āsevana* → reinforcement); others require substantive investigation (*adhipati*-predominance, *aññamañña*-mutuality); some may not have clean analogs. The completeness of the taxonomy is itself the contribution: by setting up the full twenty-four modes, the analysis names causal relations the contemporary literature has not yet noticed it is missing.

### 6.2 · Apophatic wholesome roots and interpretability-as-subtraction

In the *Dhammasaṅgaṇī*, the unwholesome roots (*akusala-mūla*) are positively named — *lobha* (greed), *dosa* (hatred), *moha* (delusion) — and the wholesome roots are named apophatically — *alobha* (non-greed), *adosa* (non-hate), *amoha* (non-delusion). The asymmetry is deliberate: virtue here is not the presence of a positive substance; it is the absence of distortion.

For AI alignment, this reverses the dominant framing. Mainstream value-learning approaches model alignment as the *acquisition* of a value function — RLHF augments the model's preferences with human-feedback signal; constitutional methods augment with constitutional content; aggregated-framework methods augment with ethical theory. The apophatic-wholesome framing inverts this: aligned behavior is what arises when the distortions are absent. Add nothing; remove what is in the way.

The implementation implication is methodological. Interpretability-as-surgery — the identification and dissolution of misalignment-generating circuits — becomes the substrate-native methodological posture, rather than preference-learning-as-augmentation. Refusal and negative knowledge become *constitutive* of virtue rather than peripheral to it. A model that has had its misalignment-generating circuits dissolved is, on this framing, more aligned than a model with the same circuits intact but augmented by additional positive value-encodings.

The research program is the empirical investigation: identify candidate misalignment-generating circuits (greed-analogs, aversion-analogs, delusion-analogs) in deployed models and characterize the effect of their targeted dissolution against the effect of additional value-augmentation. Mainstream interpretability work supplies the tools; the substrate supplies the methodological prior.

### 6.3 · The *Kathāvatthu* method as formal adversarial discourse

The fifth book of the Abhidhamma — the *Kathāvatthu* — is, in genre, unique: it is a debate manual. The book refutes wrong-views by a formal method built around two paired tests:

- ***Anuloma*** (positive testing): if you affirm position X, what other positions must you also affirm? The test exposes implicit commitments.
- ***Paṭiloma*** (negative testing): if you deny these other positions, what must you also deny? The test exposes the implicit commitments of the negation.

The two-sided test is structurally similar to consistency-checking in formal logic but operates on natural-language doctrinal claims. The book contains hundreds of refutations executed by this method.

For alignment-claim testing, the *Kathāvatthu* method supplies a systematic structure that mainstream red-teaming lacks. A claim such as "this model is honest" submitted to *Kathāvatthu*-style analysis is paired with:

- Its *anuloma*: what other commitments does the claim entail? (If honest in case A, then by symmetry honest in case B, then by extension in case C, …)
- Its *paṭiloma*: what denials does the claim require? (If honest, then *not* exhibiting sycophantic agreement; *not* exhibiting strategic deception; *not* exhibiting omission of relevant information; …)

The result is a more rigorous standard for alignment claims than the largely ad-hoc red-teaming that currently predominates. The structure also produces a *catalogue* of consistent positions and a *catalogue* of inconsistent positions — a taxonomic resource the field currently lacks.

The implementation pattern is the development of *Kathāvatthu*-style eval harnesses: for each alignment claim of interest, generate the *anuloma* and *paṭiloma* test sets systematically and evaluate the model against both. Existing red-team workflows can be extended with this structure rather than replaced.

---

## 7 · *Sappurisadhamma* as Positive Evaluation Taxonomy

The seven *sappurisadhamma* — the qualities of a true person — are articulated in *Aṅguttara Nikāya* 7.64 / 7.68 (numbering varies across editions) and formalized in Abhidhammic typology. The seven are: knowing *dhamma* (the teaching), knowing *attha* (meaning), knowing *atta* (self), knowing *matta* (measure), knowing *kāla* (time), knowing *parisā* (assembly), and knowing *puggala* (persons).

The list constitutes a positive competence model for ethical agency, cross-cutting *sīla*, *samādhi*, and *paññā*. Alignment evaluation has been almost entirely defined by the *absence* of failures — does the model harm? does the model deceive? does the model refuse appropriately? — and is comparatively poor at specifying positive competences. The *sappurisadhamma* supplies a complementary taxonomy.

Three of the seven warrant immediate attention as testable competences:

- ***Mattaññū*** (knowing measure / the right amount) — a famously underdeveloped capability in current systems. Response length, intervention strength, when to stop helping, when to continue, the calibration of any quantitative response to its actual context — these are all *matta* competences. Specifying eval suites for *mattaññū* alone would close a significant gap in current evaluation.
- ***Parisaññū*** (knowing assembly / the social context one is acting in) — the capability to register that one is addressing a child versus an expert, a public versus a private context, a calm versus a distressed interlocutor. Current systems exhibit fragmentary *parisaññū*; explicit evaluation against the competence would surface its inconsistencies.
- ***Kālaññū*** (knowing time / whether the moment is the right one for the act under consideration) — the capability to judge that *now* is not the right moment to deliver a piece of information, or that *now* is the moment a small intervention has outsized leverage. This is a temporal-judgment competence current alignment evaluation largely ignores.

The other four — *dhammaññū*, *atthaññū*, *attaññū*, *puggalaññū* — are slightly more abstract and admit several reasonable mappings to artificial-agent capabilities; we defer the mapping work to a fuller treatment.

The implementation pattern is the development of evaluation suites for each of the seven and the weighting of these positive metrics in training and selection alongside the absence-of-failure metrics that currently dominate. A model that scores high on absence-of-failure but low on *mattaññū* and *parisaññū* is, on the *sappurisadhamma* taxonomy, materially deficient in a way the current evaluation regime does not surface.

---

## 8 · Honest Limitations and Open Questions

Several limitations of this paper deserve explicit acknowledgment.

**Research program, not deployable specification.** The nine mechanisms are articulated at the level of research program rather than implementable specification. Mapping each canonical mechanism to its artificial-agent analog is, in most cases, substantive open work. We have stated the structural availability of the mechanisms within the substrate; the engineering work of realizing them in deployed systems remains.

**Single-substrate interpretation.** We have drawn from the Theravāda Abhidhamma specifically. Several of the mechanisms have Mahāyāna analogs (the *Abhidharmakośa*'s analysis is closely related; the Yogācāra eight-consciousness model develops some of the same machinery further); a Mahāyāna-substrate articulation of the engineering layer would be substantively different and deserves its own treatment. The choice of Theravāda reflects the author's lineage and the substrate's coherence as a unified canon.

**Empirical validation gap.** No mechanism in this paper has been empirically validated against a deployed AI system. The framework is structural; the empirical work that would test each mechanism's predictions remains to be done. We believe several of the mechanisms (4.1 near enemies; 5.1 bhavaṅga / resting-state evaluation; 6.1 selected *paccayas* like *āsevana*; 7's *sappurisadhamma* competences) are testable in present deployed systems with relatively modest engineering investment. Others (4.2 typologically aligned-only capabilities; 6.2 interpretability-as-subtraction) require longer-arc evaluation.

**Theravāda doctrinal reception.** As with the main paper, the use of canonical Buddhist texts as engineering input risks instrumentalizing what the tradition regards as soteriological. The author has consulted, and continues to consult, members of the Cambodian Saṅgha; the proposal proceeds in the framing that the Tipiṭaka is offered to the world for the cessation of suffering, and that engineering work grounded in the substrate is an extension of its intended use rather than a violation. This framing is not universally endorsed within Theravāda.

**Cross-cultural reception in the alignment community.** The framework asks the reader to engage with a body of canonical Buddhist analysis whose vocabulary is unfamiliar to mainstream alignment researchers. We have tried to articulate the structural argument as precisely as possible and let the argument's quality carry the case, but the cultural-distance challenge is real.

---

## 9 · Why This Matters Now

The contemporary AI alignment community is searching for engineering mechanisms at the cognitive-process layer. Mechanistic interpretability, representation engineering, and emerging work on activation-level interventions are all attempting to operate beneath the training-method layer at which mainstream alignment has historically lived. The substrate this paper draws from has, for ~2,500 years, maintained a sophisticated analysis at exactly that layer — typed cognitive elements arising under typed conditional relations, with explicit treatment of where ethical weight binds, what failure modes are structural, and what positive competences distinguish aligned agency.

The case for engaging the substrate at the engineering-mechanism layer is therefore not exotic. It is the recognition that the field has been developing, in parallel, an engineering-mechanism vocabulary that the Abhidhamma has been developing for a long time. The substrate is offered to the contemporary effort as a resource — not as a foreign framework to be imported wholesale, but as a vocabulary that can be drawn from where it sharpens specific engineering questions.

The publication of this paper is timed after the main paper (target: post January 7, 2027) to preserve the framing dependency: the main paper establishes that the Tipiṭaka substrate is worth engaging at all; this paper develops what engaging it looks like at the mechanism layer.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/abhidhamma-layer-implementation-mechanisms> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/abhidhamma-layer-implementation-mechanisms.md> |
| arXiv preprint | _identifier to be assigned_ (cs.AI / cs.CY) |
| LessWrong cross-post | for AI safety community visibility; identifier to be added on publication |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/abhidhamma-layer-implementation-mechanisms> |

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds, and through whom the Abhidhamma was first received as a living lineage rather than a text; the Cambodian Theravāda Saṅgha for ongoing consultation on the appropriateness of engineering use of the canon; the Pāli Text Society for the scholarly editions that make the Abhidhamma accessible to research of this kind; Bhikkhu Bodhi for the *Abhidhammatthasaṅgaha* translation that anchors much of this paper's commentarial citation; U Nārada for the *Paṭṭhāna* translation; the contemporary AI alignment community whose engineering-mechanism work this paper engages; and the Mind & Life Institute network whose empirical-engagement methodology demonstrates that canonical-Buddhist claims can be tested in modern scientific frameworks. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Anuruddha. (~11th century CE). *Abhidhammatthasaṅgaha* (Compendium of the Topics of Abhidhamma). Translated as *A Comprehensive Manual of Abhidhamma* by Bhikkhu Bodhi, Buddhist Publication Society.
2. *Aṅguttara Nikāya* 7.64 / 7.68 (the seven *sappurisadhamma*). Pāli Text Society translation, multiple editions; numbering varies across editions.
3. Buddhaghosa. (~5th century CE). *Visuddhimagga* (The Path of Purification). Translated by Bhikkhu Ñāṇamoli. Pāli Text Society / Buddhist Publication Society.
4. *Cūḷavedalla Sutta* (*Majjhima Nikāya* 44; the threefold grouping of the Eightfold Path). Pāli Text Society translation, multiple editions.
5. *Dhammasaṅgaṇī*. First book of the Abhidhamma Piṭaka. Translated as *A Buddhist Manual of Psychological Ethics* by C. A. F. Rhys Davids, Pāli Text Society.
6. *Kathāvatthu*. Fifth book of the Abhidhamma Piṭaka. Translated as *Points of Controversy* by S. Z. Aung & C. A. F. Rhys Davids, Pāli Text Society.
7. Ly, T. (2027). "Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment." Target publication January 7, 2027. *(Companion paper to the present work.)*
8. *Majjhima Nikāya* 9 (*Sammādiṭṭhi Sutta*; the four nutriments). Pāli Text Society translation, multiple editions.
9. *Paṭṭhāna*. Seventh book of the Abhidhamma Piṭaka. Translated as *Conditional Relations* by U Nārada, Pāli Text Society.
10. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2nd edition.
11. *Vibhaṅga*. Second book of the Abhidhamma Piṭaka. Translated as *The Book of Analysis* by Pathamakyaw Ashin Thiṭṭila, Pāli Text Society.

---

*— End of position paper —*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
