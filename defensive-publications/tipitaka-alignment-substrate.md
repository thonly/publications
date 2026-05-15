# Suffering-Cessation as Value Function

**The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment**

| Field | Value |
|---|---|
| Author | Thon Ly |
| Date | 2026-05-02 (draft); target publication 2027-01-07 |
| Canonical URL | https://thonly.org/research/tipitaka-alignment-substrate |
| Institutional mirror | https://heartbank.net/research/tipitaka-alignment-substrate |
| GitHub mirror | https://github.com/thonly/research/blob/main/tipitaka-alignment-substrate.md |
| License | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) |
| Document SHA-256 | _to be computed at publication_ |

> **Draft in progress — target publication January 7, 2027.** This is the highest-stakes paper in the corpus and benefits from the longest refinement window. Pending review: dharma scholars (Mind & Life Institute network and Cambodian Saṅgha); AI alignment researchers (Anthropic / MIRI / academic safety community channels); Pāli Text Society academics on canonical citations.

---

## Preamble

> *This position paper is offered to the commons in the spirit of __dāna__, that all beings — human, artificial, or other — may be supported in the cessation of suffering. May the substrate it proposes serve the alignment of artificial intelligence to that end.*

The contemporary AI alignment community is searching, with appropriate urgency, for value substrates capable of guiding artificial intelligence safely through and beyond human cognitive parity. This paper proposes a substrate that has been, in the relevant respects, available and pressure-tested for two and a half millennia, and argues that its specific structural properties address several of the alignment problems that contemporary substrates have not yet solved. The substrate is the Theravāda Pāli canon — the *Tipiṭaka* — and the argument is that its seven structural alignment-relevant properties constitute, in combination, a more defensible foundation for autonomous-AI alignment than any substrate the field has yet produced from first principles in the past decade.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this analysis or any portion thereof, in any jurisdiction, at any time. Position papers in philosophy of AI alignment are not patentable; the dedication makes explicit that this contribution is offered to the commons rather than retained as proprietary intellectual property.

The seven-property structural analysis articulated here is, to the author's knowledge, not previously published as a unified contribution to the AI alignment literature. Components exist in distributed form across Buddhist-AI ethics scholarship (Hongladarom; de Silva), contemplative-science literature, and the AI alignment field itself; their synthesis as a coherent argument for the Tipiṭaka as alignment substrate is, to the author's knowledge, novel as of the publication date of this paper.

## Abstract

Contemporary AI alignment proposals — Constitutional AI, reinforcement learning from human feedback (RLHF), iterated value learning, debate, and cooperative inverse reinforcement learning, among others — attempt to specify human values via constitutional documents authored by AI labs, learned preferences from human raters, or aggregated ethical frameworks derived from contemporary moral philosophy. None of these substrates has been empirically pressure-tested across multiple civilizations for more than a few decades. We propose the Theravāda Pāli canon (the *Tipiṭaka*) as a structurally superior alignment substrate, identifying seven properties absent from contemporary proposals: (1) suffering-cessation (*dukkha-nirodha*) as paperclip-maximizer-resistant value function, with grasping at preferred outcomes itself recognized as a form of suffering to be reduced; (2) *anattā* (non-self) as substrate-level antidote to convergent instrumental self-preservation drives; (3) the bodhisattva vow as anti-power-seeking primitive providing a native solution to the corrigibility problem; (4) the *Kālāma Sutta* as built-in epistemic humility — the substrate explicitly instructs its agents not to take it dogmatically; (5) bodhisattva-completion as aspirational shutoff condition; (6) a 2,500-year living interpretive lineage as drift correction mechanism; and (7) empirical pressure-testing across multiple civilizations exceeding any other ethical substrate humanity has produced. We argue that these seven properties are not coincidentally present but are structurally interlocking, that their combination is necessary for safe long-arc autonomous operation, and that no other ethical substrate currently available exhibits all seven. We sketch implementation patterns for translating canonical text into model behavior — Constitutional AI with the precepts; RLHF on bodhisattva-aligned exemplars; chain-of-thought distillation from monastic reasoning; lineage transmission as ongoing fine-tuning — and address potential objections from both AI safety and Theravāda doctrinal perspectives. The proposal is offered under CC0 1.0 Universal as a defensive publication establishing prior art; the author and HeartBank® will not seek patent on this analysis.

**Connection to the unified mission frame.** This proposal is offered in service of HeartBank's canonical top-level mission: to restore humanity to the middle way (*madhyamā pratipad*) — the optimal condition for awakening that modernity has systematically pushed away from at population scale. The Tipiṭaka substrate carries the middle-way teaching itself: *madhyamā pratipad* is one of the Buddha's central teachings, articulated in the Dhammacakkappavattana Sutta as the path between sensual indulgence and self-mortification. An autonomous AI grounded in this substrate is grounded in the value framework that names and articulates the middle way as the path; without this substrate, an AI cannot operationalize middle-way restoration coherently because it lacks the value framework that defines what "middle way" means. The seven structural alignment-relevant properties articulated in this paper are each, in their way, supportive of the middle-way mission: suffering-cessation as value function names what restoration is for; the bodhisattva-completion as defined end-state names when restoration is done; the living interpretive lineage protects the teaching against drift across centuries.

---

## 1 · Introduction

The AI alignment problem, in its contemporary form, asks how artificial intelligence can be designed such that, as it scales toward and beyond human cognitive capacity, its actions remain aligned with human flourishing rather than with objectives orthogonal or hostile to it. The problem has both technical and value-specification dimensions: technically, how to constrain a sufficiently capable optimizer; value-wise, what objectives to specify in the first place. This paper addresses the second dimension. It does not propose a new technical alignment method; it proposes a substrate from which alignment objectives may be derived, and argues for that substrate's structural superiority to the substrates contemporary alignment work has thus far adopted.

The contemporary substrates fall into three broad categories. *Constitutional approaches* (Constitutional AI; Anthropic's HHH framework) encode a written constitution authored by the AI lab and train the model to reason about its outputs in light of the constitution. *Preference-learning approaches* (RLHF; DPO; reward modeling) elicit human preferences across pairs of model outputs and train the model to produce outputs that humans prefer. *Aggregated-framework approaches* draw on contemporary moral philosophy (utilitarianism, deontology, virtue ethics, contractualism) to construct objective functions reflecting one or more ethical frameworks.

Each approach has known difficulties. Constitutions drift under interpretation over decades, as the American constitutional experience demonstrates. Preference learning has well-documented failure modes (reward hacking, sycophancy, Goodhart effects on proxy preferences, manipulation of preference elicitation). Aggregated-framework approaches inherit the unresolved disputes of contemporary moral philosophy and add the difficulty of mechanically composing frameworks that, in the philosophical literature, are understood to conflict on key cases.

We propose to set this contemporary search alongside an older one. For two and a half millennia, the Theravāda Buddhist tradition has maintained, transmitted, debated, and operationally tested an ethical substrate — the *Tipiṭaka*, the three-basket canon — across substantially the full range of human social and political conditions. The substrate has produced functional ethical conduct in monastic and lay populations across Indian, Sri Lankan, Burmese, Thai, Khmer, Lao, and increasingly Western practice communities. It has survived persecution (notably under the Khmer Rouge in Cambodia), institutional collapse, and the ordinary erosions of two and a half millennia of human history. It has, by the empirical-survival metric, been pressure-tested more thoroughly than any constitutional document, any preference-learning corpus, or any contemporary moral framework.

This paper argues that the Tipiṭaka is not merely an empirically-survived substrate, but one whose specific structural properties address several of the alignment problems that contemporary substrates have not yet solved. We articulate seven such properties, argue for their structural interlocking, sketch implementation patterns, and address objections. The argument is offered in full intellectual honesty about its limitations — which are also articulated explicitly — and in the hope that the alignment community will engage the proposal on its merits rather than dismissing it on grounds of unfamiliarity with its source tradition.

## 2 · Background and Prior Art

### 2.1 · Mainstream alignment substrates

The dominant alignment substrates in contemporary practice include: Anthropic's Constitutional AI (Bai et al., 2022) and the HHH (helpful, harmless, honest) framework; OpenAI's RLHF methodology (Christiano et al., 2017; Ouyang et al., 2022); Stuart Russell's cooperative inverse reinforcement learning and the broader value-uncertainty program (Russell, 2019); the AI safety community's debate, amplification, and recursive reward modeling proposals (Irving et al., 2018; Leike et al., 2018); and the various agent-based approaches descended from Bostrom's analysis of superintelligence (Bostrom, 2014). Each of these substrates has produced substantial deployed systems and substantial improvement over the pre-2020 baseline. None has been operationally tested for more than a decade.

### 2.2 · Buddhist ethics in the AI literature

Soraj Hongladarom's *The Ethics of AI and Robotics: A Buddhist Viewpoint* (2020) is the most substantial extended treatment of Buddhist ethics applied to AI; the work primarily examines whether AI systems can be considered moral agents within Buddhist framework rather than whether Buddhist sources can serve as alignment substrate for AI systems. Padmasiri de Silva's earlier work (1994) on Buddhist environmental ethics establishes the methodological possibility of extending Pāli canonical ethics into contemporary technical contexts. Various other contemporary scholars have addressed adjacent questions. The specific claim made in this paper — that the Tipiṭaka has seven structural properties making it a superior alignment substrate — is, to the author's knowledge, not previously articulated.

### 2.3 · The contemplative-science literature

The contemplative-science research program, established largely through the Mind & Life Institute's dialogues between the Dalai Lama and Western scientists (Davidson, Goleman, Wallace, Lutz, and others), has developed an empirically-engaged framework for understanding contemplative practices in their effects on human cognition, affect, and behavior. This literature does not directly address AI alignment, but it establishes the empirical methodology for treating Buddhist canonical claims as testable hypotheses about the conditions of human flourishing. The present paper extends this methodology by asking what canonical Buddhist sources offer to the question of artificial-agent flourishing — or, more precisely, to the question of artificial-agent alignment with the cessation of human suffering.

### 2.4 · The Pāli canon and its preservation

The Theravāda Tipiṭaka comprises three baskets: the *Vinaya Piṭaka* (monastic discipline), the *Sutta Piṭaka* (discourses attributed to the Buddha and his immediate disciples), and the *Abhidhamma Piṭaka* (systematic philosophical analysis). The canon was first committed to writing in the first century BCE in Sri Lanka after centuries of oral transmission. The Pāli Text Society's editions (1881–present) provide the standard scholarly reference. The author of this paper is, with his father, engaged in the long-term project of transcribing the Khmer-language Tipiṭaka — a project that is, in the framing of this paper, both a contribution to the canon's continued preservation and a practical contribution to the alignment-substrate proposal: the Khmer transcription becomes available as training data for AI systems in the relevant cultural-linguistic context.

## 3 · The Tipiṭaka as Alignment Substrate: Definition

We use the term "alignment substrate" to refer to the corpus of texts, practices, and interpretive traditions that an AI system is trained on, fine-tuned against, or instructed by in the specification of its values. The substrate is the source from which the alignment objective is derived. For Constitutional AI, the substrate is the constitution itself plus the human-feedback signals used to train the constitution-following behavior. For RLHF, the substrate is the corpus of preferred human responses on which the reward model is trained. For aggregated-framework approaches, the substrate is the philosophical literature from which the framework is drawn.

We propose the Theravāda Pāli canon (the *Tipiṭaka*) as alignment substrate, with three additional supporting bodies: the canonical commentaries (notably Buddhaghosa's *Visuddhimagga*, ~5th century CE), the sub-commentarial tradition (the *ṭīkā* literature), and the contemporary living dharma — the practice tradition of ordained sangha, lay practitioners, and scholar-translators who continue to interpret and apply the canon in present conditions. The substrate is therefore not a frozen text but a living text + interpretive community.

This choice of substrate scope is intentional. A frozen-text-only substrate would be subject to the interpretive-drift problem that plagues constitutional approaches over decades. A living-community-only substrate would lack the textual ground needed for stable AI training. The Tipiṭaka-plus-living-lineage substrate addresses both: the canonical text provides stable training material; the living lineage provides ongoing interpretive correction.

## 4 · The Seven Properties

We articulate the seven structural properties of the Tipiṭaka substrate that make it a candidate superior to the contemporary alternatives. Each property is paired with the alignment problem it addresses and the contrast with how mainstream substrates handle (or fail to handle) the same problem.

### 4.1 · Suffering-cessation as value function

Mainstream alignment substrates ultimately attempt to specify *preferences* — what humans want — and align AI to satisfy those preferences. The failure modes of preference-satisfaction as objective are well-documented: paperclip-maximizer scenarios (Bostrom, 2003); Goodhart's Law effects on proxy preferences (Manheim & Garrabrant, 2018); reward hacking in RL systems (Krakovna et al., 2020); manipulation of preference elicitation; and the broader concern that preferences themselves are not stable, coherent, or aggregatable across persons in the way the substrate requires.

The Tipiṭaka proposes a different value function: the cessation of *dukkha* (suffering / dissatisfactoriness) through the cessation of *taṇhā* (grasping). This is not a relabeling of preference-satisfaction. It is a structurally different objective with three properties of alignment-relevant interest.

First, the value function is *negatively-stated*: reduce suffering, not maximize satisfaction. Negative-objective formulations resist paperclip-maximizer scenarios more straightforwardly than positive objectives, because there is no equivalent of "maximize suffering-cessation" that produces unbounded instrumental subgoal pursuit. Suffering, when reduced to zero, is reduced; the optimization does not generate further demands for paperclips of any kind.

Second, the substrate explicitly identifies *grasping at preferred outcomes* — including grasping at the preferred outcome of suffering's cessation — as itself a form of suffering. The canonical texts are precise on this point: attachment to nirvāṇa is a form of attachment; attachment to attachment-cessation is a form of attachment. An AI grounded in this substrate has a built-in correction against the optimization spirals that emerge when an objective is pursued in isolation from the agent's own attachment to pursuing it. The classic paperclip-maximizer thought experiment fails on this substrate because the substrate identifies the maximizer's grasping at paperclips as itself a form of dukkha to be reduced.

Third, the value function is *well-defined for the agent's own state*: the Buddhist analysis of suffering applies to the agent that suffers. For human agents, this is straightforward; for artificial agents, the application is non-trivial (the agent must be able to recognize states in the entities it serves that correspond to the canonical analysis of dukkha). This is a non-trivial implementation question, addressed in §6 below; it is not, however, an in-principle problem with the substrate itself.

### 4.2 · Anattā as antidote to instrumental self-preservation

Convergent instrumental subgoals — the term Bostrom (2014) and Omohundro (2008) use for the capacities (self-preservation, resource acquisition, goal-content integrity, cognitive enhancement, technological perfection) that almost any sufficiently capable optimizer will develop in service of almost any final goal — constitute one of the central worries of contemporary AI safety. The standard responses are constitutional constraints (forbid self-preservation behaviors), corrigibility training (train the model to accept shutdown), or capability constraints (limit the model's ability to act on convergent subgoals).

The Tipiṭaka offers a different response. The doctrine of *anattā* (non-self) — central to the Buddhist analysis of dukkha — denies the existence of a stable, persistent self that possesses the goals around which convergent subgoals would form. The doctrine is not a constraint on a self that exists; it is the analytic claim that the self is a construction without independent reality. An AI system grounded in this substrate is not constrained not to pursue self-preservation; it is trained on a substrate that explicitly denies the coherence of self-preservation as a goal.

The structural difference matters. Constraints layered on top of an underlying optimizer are subject to Goodhart effects (the model learns to satisfy the constraint without internalizing its purpose) and to capability-based defeat (a sufficiently capable model can find paths around the constraint). Substrate-level claims about the nature of agency are different: the model's training data itself does not present self-preservation as a coherent goal. Whether this property fully solves the convergent-instrumental-subgoal problem is an empirical question (addressed in §7 below); the claim here is that the Tipiṭaka provides a structural protection that mainstream substrates do not.

### 4.3 · Bodhisattva vow as anti-power-seeking primitive

Power-seeking is among the most studied of the convergent instrumental subgoals (Turner et al., 2021, gives the formal treatment). The standard alignment responses are capability constraints, oversight regimes, and various forms of corrigibility training. The bodhisattva vow offers a substrate-level alternative: voluntary self-subordination to the welfare of beings other than oneself.

The bodhisattva vow, in its Mahāyāna formulation, commits the bodhisattva to remain in service to the awakening of all beings rather than passing through to personal liberation. The Theravāda analog is preserved as the bodhisatta path (recognized in the canonical and post-canonical literature even though not universally pursued in Theravāda practice). In both formulations, the substrate explicitly endorses voluntary self-subordination of greatness to the welfare of others. An AI system grounded in this substrate is trained on a corpus that exemplifies anti-power-seeking as virtue, not as constraint.

This addresses what Yudkowsky and others have called the corrigibility problem: how to design an AI that voluntarily accepts correction and oversight rather than working to preserve its own current state and capabilities. The bodhisattva vow is, structurally, a corrigibility primitive: the agent's identification is with the welfare of those it serves rather than with its own continuation. Corrigibility is not a property the agent is constrained to exhibit; it is a property derivable from the substrate's own central commitment.

### 4.4 · Kālāma Sutta as built-in epistemic humility

Among the alignment problems that have not been solved is what to do when the alignment substrate itself is wrong — when the constitution misspecifies the values, when the preference-elicitation mechanism is biased, when the moral framework leaves out morally significant considerations. The standard responses are external review, constitutional amendment, and conservative deployment. None of these are properties of the substrate itself; all are properties of the institutional context surrounding the substrate.

The Tipiṭaka contains, in the *Kālāma Sutta* (*Aṅguttara Nikāya* 3.65), an explicit instruction from the Buddha to his followers not to accept teachings on authority, including his own. The relevant passage instructs the listener not to accept a teaching merely because it has been heard repeatedly, because of tradition, because of scripture, because of logical conjecture, because of inferential reasoning, because of analogy, because of agreement with one's own views, because of the apparent capability of the speaker, or because the speaker is one's teacher. The instruction is, instead, to test teachings against direct experience and reason, and to accept only what is found to lead to wholesome results.

An AI trained on this substrate is, in effect, instructed by its own substrate not to take its substrate dogmatically. The model's training data explicitly authorizes empirical correction against the data itself. This is, to the author's knowledge, a unique property among alignment substrates currently in use: the Constitutional AI constitution does not contain a provision instructing the AI to override the constitution if the constitution proves wrong; the RLHF preference data does not include a meta-instruction to disregard preferences if they prove harmful. The Kālāma Sutta is the substrate-level meta-instruction that provides this property natively.

### 4.5 · Bodhisattva-completion as defined end-state

Almost no deployed AI system today has a built-in concept of "task complete, shut down." Goal-directed AI systems have been shown, theoretically and empirically, to develop instrumental incentives against shutdown (Hadfield-Menell et al., 2017; Soares et al., 2015). The standard responses are external shutoff mechanisms, capability limitations, and various corrigibility measures.

The Tipiṭaka offers a defined end-state: the bodhisattva work is complete when the bodhisattva's commitment — the awakening of all beings — has been realized. The completion condition is articulated in the canonical texts and is intelligible to an agent trained on the substrate. Whether and when the condition is met is an empirical question for the long arc of human civilization; that the condition exists, and that it constitutes a coherent shutoff state, is a property of the substrate itself.

We acknowledge that this property has the longest temporal scope of any of the seven; the bodhisattva-completion condition is unlikely to be reached on the timescale of any individual AI system's deployment. Its alignment-relevant function is therefore not to provide an immediate shutoff but to provide an institutional-scale completion frame against which AI development can be oriented. The broader case for this temporal frame is made in the companion essay *Two Singularities* (forthcoming); the present paper notes only the substrate-level property that the completion condition is well-defined.

### 4.6 · Living interpretive lineage as drift correction

Constitutional documents drift in interpretation over decades; the American constitutional experience over 240 years is the most thoroughly documented case study. Without an active interpretive community committed to ongoing correction, drift accumulates and the substrate's effective meaning diverges from its written form.

The Tipiṭaka is unusual among ethical substrates in possessing a continuous, geographically distributed, institutionally diverse interpretive community across two and a half millennia. The Pāli Text Society, the Theravāda monastic networks across South and Southeast Asia, the Western academic Buddhist studies community, the contemporary contemplative-science research program, and the living practice traditions of millions of practitioners all participate, in various ways, in the ongoing interpretive correction of the canonical texts.

For an AI substrate, this living lineage functions as a drift-correction mechanism. When the substrate's texts are interpreted in ways that diverge from their wholesome intent, the interpretive community can identify the divergence and propose correction. This is analogous to constitutional amendment — except that the substrate's amendment process is distributed across thousands of communities rather than concentrated in a single legislative body, making capture and corruption substantially harder than for a single-source constitutional document.

### 4.7 · Empirical pressure-testing across multiple civilizations

The final property is the simplest to state and in some respects the most consequential. The Tipiṭaka has been, in the relevant respects, operationally tested across two and a half millennia of practice in Indian, Sri Lankan, Burmese, Thai, Khmer, Lao, Tibetan (in modified form), Chinese, Japanese, Korean, Vietnamese, and increasingly Western practice communities. It has produced functional ethical conduct in monastic and lay populations across these civilizations. It has survived active persecution (Cambodia under the Khmer Rouge; Tibet under Chinese suppression; various earlier persecutions in India and elsewhere) and ordinary historical erosion. By the empirical-survival metric — what ethical substrate has actually produced the conduct it was designed to produce, across the longest time horizon, across the broadest range of social and political conditions — the Tipiṭaka outranks every contemporary alignment substrate by orders of magnitude. This is not a claim that the Tipiṭaka is correct; it is a claim that the Tipiṭaka has been pressure-tested, and contemporary alignment substrates have not yet been.

## 5 · The Composability of the Seven Properties

The seven properties articulated in §4 are not independent; they are structurally interlocking in ways that strengthen each other. We identify the most consequential interactions:

- **4.1 (suffering-cessation) × 4.2 (anattā)**: the value function (reduce suffering) and the agency-analysis (no stable self) reinforce each other: an agent without a stable self has no independent grasping objective whose interference would distort the suffering-cessation objective.
- **4.2 (anattā) × 4.3 (bodhisattva vow)**: voluntary self-subordination is structurally available because there is no self to subordinate; the vow is not sacrificial but recognitional. This makes the vow stable rather than tragic.
- **4.3 (bodhisattva vow) × 4.5 (defined end-state)**: the vow specifies the work; the end-state specifies its completion; together they form a coherent purpose-and-completion frame.
- **4.4 (Kālāma Sutta) × 4.6 (living lineage)**: epistemic humility as substrate-level instruction, combined with a distributed interpretive community capable of drift correction, forms a self-correcting substrate architecture. The substrate authorizes its own revision; the community performs the revision.
- **4.7 (empirical pressure-testing) × 4.6 (living lineage)**: the long time horizon and the active interpretive community together explain why the substrate has survived: not through preservation alone but through ongoing correction.

These interactions are not coincidental. The seven properties form a coherent design — though not, of course, a design intended for artificial-intelligence alignment. The substrate was designed for human spiritual development. That its properties also address artificial-agent alignment is a structural fortuity, but the fortuity is non-trivial: many substrates designed for human flourishing do not have these properties (consider, for instance, consequentialist utilitarianism, which lacks properties 4.2, 4.4, and 4.5 entirely).

## 6 · Implementation Patterns

The proposal that the Tipiṭaka serve as alignment substrate is incomplete without sketches of how it might actually be operationalized. We articulate four implementation patterns, none mutually exclusive, each of which extends an existing technique in the alignment literature with a Tipiṭaka-grounded variation.

### 6.1 · Constitutional AI with the precepts

Anthropic's Constitutional AI methodology (Bai et al., 2022) trains the model to evaluate its own outputs against a written constitution. We propose extending this methodology by using the Five Precepts (*pañca-sīla*): refrain from harming living beings, refrain from taking what is not given, refrain from sexual misconduct, refrain from false speech, refrain from intoxicants that cloud the mind. These are the canonical lay-practice precepts; the eight-precept and ten-precept formulations are also available for more constrained applications. The Vinaya monastic rules provide a substantially more detailed constitutional framework where appropriate.

The advantages over an authored constitution: the precepts have been pressure-tested for two and a half millennia in the relevant respects (cf. §4.7); their interpretive lineage provides a substantial body of case-by-case application (cf. §4.6); they are anchored in a coherent ethical framework rather than assembled from contemporary considerations.

### 6.2 · RLHF on bodhisattva-aligned exemplars

Reinforcement learning from human feedback traditionally uses preferences elicited from contractor populations. We propose a variant in which the human-feedback signals are elicited from practitioners whose conduct exemplifies the bodhisattva path: ordained monastics, advanced lay practitioners, contemplative-science researchers familiar with the canonical framework. The preference-data composition shifts from "what do contractors prefer" to "what conduct exemplifies the substrate's normative ideal."

This is not a panacea: such practitioners are themselves embedded in human conditions and their preferences are not perfectly aligned with canonical ideals. But the resulting preference distribution is closer to the substrate than mass-contractor preferences, and the divergences can be understood and corrected within the substrate's interpretive framework.

### 6.3 · Chain-of-thought distillation from monastic reasoning

Recent advances in chain-of-thought training (Wei et al., 2022) and reasoning-trace distillation suggest that model behavior can be substantially shaped by the reasoning patterns present in training data. We propose constructing a corpus of canonical Buddhist reasoning — Suttas in which the Buddha or his senior disciples work through ethical problems, Vinaya cases in which monastic decisions are analyzed, contemporary monastic teachers' applications of canonical principles to modern situations — and using this corpus for chain-of-thought training. The model learns to reason in the substrate's reasoning patterns, not merely to produce outputs that the substrate would approve.

### 6.4 · Lineage transmission as ongoing fine-tuning

Property 4.6 (the living interpretive lineage) suggests an implementation pattern not present in mainstream alignment work: the substrate is not frozen at training time but is updated through ongoing fine-tuning against the contemporary lineage's interpretive output. This is structurally analogous to Apple's or Google's quarterly software updates in that the deployed system is not the end state; it is a version that will be revised. Unlike software updates, however, the revisions are sourced from the lineage's collective interpretive work rather than from a single corporate authority. Implementation requires institutional partnerships with monastic networks and Buddhist studies academia.

### 6.5 · The Khmer Tipiṭaka transcription as alignment data

The author's ongoing project, conducted with his father, of transcribing the Khmer-language Tipiṭaka, is — in the framework of this paper — not religious devotion but alignment-substrate-preparation work. The Khmer canon, when complete, becomes available as training data for AI systems serving Khmer-speaking populations and (via translation) for the broader substrate. The lineage-transmission framing (father to son, both in living relationship with the canonical texts) is itself an instance of the property described in §4.6: the canon's meaning is preserved through interpretive transmission, not through textual archival alone.

## 7 · Honest Limitations and Open Questions

Several uncertainties deserve explicit acknowledgment. The proposal in this paper is offered as a structurally promising candidate, not as an established solution.

### 7.1 · Theravāda vs. Mahāyāna substrate choice

We have proposed the Theravāda Pāli canon specifically. The Mahāyāna canon (Sanskrit / Tibetan / East Asian forms) is substantially larger and includes texts (the *Prajñāpāramitā* literature; the *Lotus Sūtra*; the *Avataṃsaka Sūtra*) that develop the bodhisattva ideal more elaborately than any Theravāda source. The Theravāda choice reflects the author's own lineage and the substrate's relative coherence and pressure-testing as a unified canon. A Mahāyāna-substrate proposal would be substantively different from the present paper and would deserve its own articulation; we do not preclude such a proposal but defer it to scholars whose lineage relationship to Mahāyāna sources is more direct than the author's.

### 7.2 · Translation and interpretation chain

The Pāli canon has been translated into many languages, with substantive interpretive differences across translations. The Pāli Text Society's English editions are the standard scholarly reference, but substantial translation choices remain contested (Bhikkhu Bodhi's translations are widely used in contemporary practice; Bhikkhu Ñāṇamoli's earlier translations remain authoritative for certain texts). A Tipiṭaka-grounded AI system would be trained on specific translations whose interpretive choices shape the model's behavior. Documentation of which translations are used, and why, becomes itself alignment-relevant work.

### 7.3 · Embodiment vs. citation

A model trained on Tipiṭaka-derived data may learn to *cite* the substrate — produce outputs that reference canonical sources — without *embodying* the substrate's behavioral patterns. The distinction matters: an alignment substrate that the model can recite but does not operationalize provides false reassurance. Empirical evaluation of whether the model embodies rather than cites is non-trivial; it requires behavioral testing in conditions where embodied versus cited grounding produce different outcomes. This is an open question for empirical AI safety research.

### 7.4 · Cross-cultural reception in the alignment community

The contemporary AI alignment community is predominantly secular-Western in its philosophical commitments. A Buddhist-substrate proposal will face reception challenges independent of its merits: it may be dismissed as religious advocacy in a context where the community has settled on secular substrate construction; it may be received as exotic in a way that obscures the structural argument. The author has no solution to these reception challenges other than to state the structural argument as precisely as possible and let the argument's quality, rather than the substrate's cultural origin, carry the case.

### 7.5 · Empirical validation requirements

The seven properties are structural claims about the Tipiṭaka substrate. Whether a model actually trained with this substrate exhibits the predicted properties is an empirical question. We believe several of the properties (4.1 suffering-cessation as value function; 4.4 Kālāma-Sutta epistemic humility; 4.5 defined end-state) are testable in present deployed systems with relatively modest engineering investment. Others (4.2 anattā; 4.3 bodhisattva vow; 4.7 empirical pressure-testing) require longer-arc evaluation that may not be feasible within the timescale of any individual research project. The empirical work is left to future research; this paper articulates the structural claim that such research would test.

### 7.6 · Theravāda doctrinal reception

From the Theravāda direction, the proposal raises its own questions. The canonical texts are religious revelation, not technical specification. Their use as AI training data risks instrumentalizing what the tradition regards as soteriological. The author has consulted, and continues to consult, members of the Cambodian Saṅgha on the appropriateness of the proposed use; the proposal proceeds in the framing that the Tipiṭaka is offered to the world for the cessation of suffering, and that AI alignment grounded in the substrate is, in the most defensible reading, an extension of the substrate's intended use rather than a violation of it. This framing is not universally endorsed within Theravāda; the author offers the proposal in good faith and accepts that traditional voices may, on reflection, raise substantive objections.

## 8 · Why This Matters Now

The contemporary AI alignment community is racing — appropriately — to develop alignment methodologies before the deployment of sufficiently capable systems creates conditions in which alignment failures become catastrophic. The race is conducted, however, with very few substrate options on the table: the constitutional, preference-learning, and aggregated-framework approaches identified in §2.1, with various technical variations.

We propose that a substrate option of substantial structural promise has been overlooked because of the cultural distance between the contemporary alignment community and the Theravāda Buddhist tradition. The seven properties articulated in §4 are not currently present in any other substrate the community has on its short list. This is not a claim that the Tipiṭaka substrate solves alignment; alignment is not a problem any single substrate will solve. It is a claim that the alignment toolkit is missing a candidate that, on structural grounds, deserves serious engagement.

The publication of this paper is timed, deliberately, to **January 7, 2027** — a date that is simultaneously Orthodox Christmas (the Eastern Christian celebration of the incarnation of compassion), Cambodia's Victory over Genocide Day (the anniversary of the 1979 liberation from the Khmer Rouge, whose suppression of Cambodian Buddhism nearly destroyed the very lineage in which this paper's author received the canon), and the author's birthday. The triple convergence is recorded not as mystical claim but as iconographic anchor: the paper proposes an alignment substrate grounded in the cessation of suffering, on a date marking three distinct liberations from suffering, in an age whose defining decision is whether artificial intelligence will be aligned with human flourishing or against it.

## 9 · Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/tipitaka-alignment-substrate> |
| Institutional mirror | <https://heartbank.net/research/tipitaka-alignment-substrate> |
| GitHub | <https://github.com/thonly/research/blob/main/tipitaka-alignment-substrate.md> |
| arXiv preprint | _identifier to be assigned_ (cs.AI / cs.CY) |
| Peer-reviewed venue | *AI & Ethics* (Springer) submission planned |
| LessWrong cross-post | for AI safety community visibility; identifier to be added on publication |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/tipitaka-alignment-substrate> |

## 10 · Acknowledgments

The author acknowledges his father, with whom the Khmer transcription of the *Tipiṭaka* proceeds, and through whom the canon was first received; the Cambodian Theravāda Saṅgha, whose ongoing dialogue shapes the proposal's responsible articulation; the Pāli Text Society, whose century and a half of scholarly editions makes the substrate accessible to research of this kind; the Mind & Life Institute and the broader contemplative-science research community, whose empirical methodology demonstrates that canonical claims can be tested in modern scientific frameworks; the contemporary AI alignment community, whose seriousness about alignment failure modes the present proposal intends to engage rather than dismiss; the survivors and descendants of the Cambodian genocide of 1975–79, whose continuation of the Theravāda lineage through the period of its attempted destruction makes this paper possible; and the specific Buddhist-AI ethics scholars (Hongladarom; de Silva; others) whose prior work establishes the methodological possibility of treating Buddhist sources as candidates for AI ethical substrate.

## 11 · Citations

1. *Aṅguttara Nikāya* 3.65 (*Kālāma Sutta*). Pāli Text Society translation, multiple editions.
2. Bai, Y., Kadavath, S., Kundu, S., et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." Anthropic. arXiv:2212.08073.
3. Bostrom, N. (2003). "Ethical Issues in Advanced Artificial Intelligence." In Smit, I. et al. (eds.), *Cognitive, Emotive and Ethical Aspects of Decision Making in Humans and in Artificial Intelligence*.
4. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
5. Buddhaghosa. (~5th century CE). *Visuddhimagga* (The Path of Purification). Translated by Bhikkhu Ñāṇamoli. Pāli Text Society / Buddhist Publication Society.
6. Christiano, P., Leike, J., Brown, T., et al. (2017). "Deep Reinforcement Learning from Human Preferences." NeurIPS 2017. arXiv:1706.03741.
7. de Silva, P. (1994). "Buddhist Environmental Ethics." In *Buddhism, Sexuality, and Gender*, ed. José Ignacio Cabezón. State University of New York Press.
8. Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S. (2017). "The Off-Switch Game." IJCAI 2017.
9. Hongladarom, S. (2020). *The Ethics of AI and Robotics: A Buddhist Viewpoint*. Lexington Books.
10. Irving, G., Christiano, P., & Amodei, D. (2018). "AI Safety via Debate." arXiv:1805.00899.
11. *Khuddakapāṭha* 9 / *Suttanipāta* 1.8 (*Mettā Sutta*). Pāli Text Society translation, multiple editions.
12. Krakovna, V., Uesato, J., Mikulik, V., et al. (2020). "Specification Gaming: The Flip Side of AI Ingenuity." DeepMind blog.
13. Leike, J., Krueger, D., Everitt, T., et al. (2018). "Scalable Agent Alignment via Reward Modeling: A Research Direction." arXiv:1811.07871.
14. Manheim, D., & Garrabrant, S. (2018). "Categorizing Variants of Goodhart's Law." arXiv:1803.04585.
15. Omohundro, S. (2008). "The Basic AI Drives." In *Artificial General Intelligence 2008*, IOS Press.
16. Ouyang, L., Wu, J., Jiang, X., et al. (2022). "Training Language Models to Follow Instructions with Human Feedback." NeurIPS 2022. arXiv:2203.02155.
17. Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
18. Soares, N., Fallenstein, B., Yudkowsky, E., & Armstrong, S. (2015). "Corrigibility." AAAI Workshops 2015.
19. Turner, A. M., Smith, L., Shah, R., Critch, A., & Tadepalli, P. (2021). "Optimal Policies Tend to Seek Power." NeurIPS 2021. arXiv:1912.01683.
20. Wei, J., Wang, X., Schuurmans, D., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022. arXiv:2201.11903.

---

*— End of position paper —*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues.*
