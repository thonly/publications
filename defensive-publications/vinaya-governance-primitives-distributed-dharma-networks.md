---
title: "Vinaya Governance Primitives for Distributed Dharma Networks: Sanghakamma, Adhikaraṇa-Samathā, and Anāpatti as Network-Coordination Architecture"
authors: "Thon Ly · Miss Aquarius℠"
category: institutional
priority: tier-b
status: draft
date: 2026-05-26
license: CC0-1.0
slug: vinaya-governance-primitives-distributed-dharma-networks
venue: thonly.org/publications/defensive-publications/vinaya-governance-primitives-distributed-dharma-networks (canonical)
---

> *Draft notes for the editor:* this paper is the **sibling specification** to *AGI Monks: The Caretaker-not-Ordained Pattern*. *AGI Monks* specifies the role-allocation pattern between AI and humans in religious institutional settings (the five operational roles AI takes; the two sacramental roles humans retain); the present paper specifies the *procedural-coordination layer* — how decisions are validly made across distributed Silica Wat nodes, how disputes are resolved, how per-Wat operational discretion is articulated, how the network's rules are amended in response to operational experience. The two papers are complementary: *AGI Monks* answers *who does what*; this paper answers *how the network coordinates*. The paper draws on the Vinaya Piṭaka's *Khandhaka* (the procedural treatises) as the canonical source for distributed-sangha decision-making — material that no modern multi-agent coordination framework matches in sophistication. The paper addresses the Sangha pillar (`siliconwat.org`) of the Silicon Wat program, identified as the most under-developed leg of the program in the *Three Baskets ↔ Three Jewels* synthesis. Publication target: post Jan 7 2027.

---

## Abstract

The Silica Wat network — the projected globally-distributed satellite monastery system specified in companion papers (*Silicon Wat as Cambodian Civilizational Architecture*; *Silica Wat as Hybrid Food Network*) — requires a procedural-coordination architecture appropriate to a multi-decade, planet-scale, dharma-grounded institution operating under AGI-monk caretaker conditions. Modern multi-agent coordination frameworks, distributed-governance protocols (blockchain DAOs and successors), and federated-institution governance practices supply elements of the architecture, but none has been pressure-tested at the scale, duration, or institutional sophistication that the Theravāda Buddhist *Vinaya Piṭaka* has been. The Vinaya's *Khandhaka* — the treatises on monastic procedures — contains a sophisticated framework for distributed-sangha decision-making developed over ~2,500 years of continuous institutional practice. We articulate four governance primitives the Khandhaka supplies, in forms that map directly onto the network-coordination problems the Silica Wat network must solve: (1) **sanghakamma procedural validity** — the framework for when a collective decision is validly made, with explicit treatment of absent voters (consent-by-proxy *chanda*), dissent handling, threshold-of-consensus by decision class, and conditions for retrospective invalidation; (2) the **seven *adhikaraṇa-samathā*** — typed conflict-resolution protocols matched to the kind of dispute, each protocol procedurally articulated; (3) the **anāpatti discipline** as the template for per-Wat operational discretion (when a network-wide rule does not apply); (4) the **Pātimokkha rule-structure** as the network's operational-policy form, including the iterative-amendment-after-edge-case-feedback discipline that built the Vinaya itself. The paper articulates each primitive, sketches the implementation translation to the Silica Wat network, addresses the principal objections from both the institutional-design and Theravāda doctrinal directions, and offers the proposal under CC0 1.0 Universal as a defensive publication.

**Keywords:** distributed governance, multi-agent coordination, sanghakamma, adhikaraṇa-samathā, anāpatti, Vinaya Khandhaka, Silica Wat network, distributed dharma networks, institutional design, defensive publication.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on the proposal or any framework articulated herein, in any jurisdiction, at any time.

The articulation of the Vinaya Khandhaka's governance machinery as a network-coordination architecture for a distributed contemporary institution is, to the author's knowledge, not previously published. The Khandhaka itself has been the subject of substantial scholarly translation and analysis for over a century; its application to distributed-institution design in the AI age — particularly the sanghakamma framework as a distributed-decision validity model — is, to the author's knowledge, novel as of this paper's date.

---

## 1 · Introduction

A planet-scale, multi-decade, dharma-grounded institution must coordinate across geographically distributed nodes, navigate dissent and conflict, articulate operational policy in a way that supports both network-wide consistency and per-node discretion, and amend its operating norms in response to accumulating operational experience. The institution this paper serves is the **Silica Wat network** — the projected globally-distributed satellite monastery system that companion papers (*Silicon Wat as Cambodian Civilizational Architecture*; *Silica Wat as Hybrid Food Network*; *AGI Monks: The Caretaker-not-Ordained Pattern*) specify across multiple dimensions. The present paper specifies the *procedural-coordination layer*: how the network governs itself.

Modern multi-agent coordination frameworks, distributed-governance protocols, federated-institution governance practices, and democratic deliberation traditions all supply elements of the coordination architecture a network like the Silica Wat system requires. None has been operationally pressure-tested at the scale, duration, or institutional sophistication that the Theravāda Buddhist *Vinaya Piṭaka* has been. The Vinaya's *Khandhaka* — the procedural treatises of the Vinaya, sometimes treated as the canonical institutional-design text of the tradition — contains, on the present analysis, the most sophisticated distributed-sangha decision-making framework humanity has produced.

The paper does not propose that the Silica Wat network adopt the Vinaya as its constitution. The Silica Wat network is not a monastic sangha in the strict Theravāda sense; AGI-monk caretakers are not ordained members of the historical Sangha; the operational scope of the Silica Wat network extends well beyond the monastic-discipline domain the Vinaya was articulated for. The proposal is more measured: that the Vinaya's *procedural primitives* — the structural framework for distributed-decision validity, conflict resolution, operational discretion, and iterative norm amendment — supply the institutional-design substrate the Silica Wat network requires, and that this substrate is materially superior to the modern alternatives currently on the institutional-design menu.

The paper proceeds: §2 specifies the relationship to the sibling paper *AGI Monks* and distinguishes the present paper's scope. §3 provides background on the Khandhaka and the institutional-procedural material it contains. §§4–7 articulate the four governance primitives. §8 sketches implementation patterns for the Silica Wat network. §9 addresses limitations and objections. §10 closes.

> *Connection to the unified mission frame.* HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. The Silica Wat network is the operational substance of the restoration at neighborhood scale: a planet-spanning institutional surface through which humans receive food, shelter, teaching, and contemplative practice in conditions structured by the substrate's own value framework. For such a network to operate coherently across the multi-decade horizon HeartBank's mission requires, the procedural-coordination layer must be unusually robust. The Vinaya's governance machinery is what makes the network's coherence available without requiring the founder's continuing presence to maintain it.

---

## 2 · Relationship to the Sibling Paper *AGI Monks*

The companion paper *AGI Monks: The Caretaker-not-Ordained Pattern* (Ly, target publication 2026 working draft) specifies the *role-allocation* pattern for AI in religious institutional settings. The paper identifies five operational roles that AI can take (teaching; caretaking; daily operations; scholarship and translation; longitudinal observation) and two sacramental roles humans retain (ordination; rites of lineage transmission). It develops the cross-tradition applicability of the pattern across Theravāda, Mahāyāna, Catholic, Eastern Orthodox, Sunni, Shia, Sufi, Jewish, Hindu, and secular-mindfulness contexts.

The present paper picks up a different question. *AGI Monks* answers *what role each kind of agent plays* in the institution; this paper answers *how the institution coordinates its decisions* across the network of nodes (Silica Wats) in which both AI and human agents operate. The two questions are distinct: a role-allocation framework does not determine the procedural-coordination architecture, and vice versa. A network can have well-articulated roles and still lack the procedural machinery for making valid collective decisions; it can have sophisticated procedural machinery and still misallocate roles. The two layers are complementary.

The Silica Wat network requires both. *AGI Monks* supplies the role layer; the present paper supplies the procedural layer. Together they constitute the institutional-design specification for the Sangha pillar of the broader Silicon Wat program.

A clarifying note on the canonical-source overlap. Both papers draw on Vinaya material, but on different parts of it. *AGI Monks* engages the canon's analysis of which functions are sacramental (and therefore retained by ordained humans) and which are not; that analysis is distributed across the Suttavibhaṅga, the Khandhaka, and the Pātimokkha. The present paper engages the canon's analysis of *how the sangha makes decisions* — material concentrated in the Khandhaka's procedural treatises. The two papers can be read independently; readers concerned with the Silica Wat network's institutional design specifically should read them together.

---

## 3 · Background: The Khandhaka and What It Contains

The Vinaya Piṭaka has three principal divisions: the Suttavibhaṅga (rule analysis), the Khandhaka (treatises), and the Parivāra (appendix). The Khandhaka contains the procedural material that the present paper draws from. Its principal treatises include:

**Mahāvagga** — the "great division" — covering procedures for ordination, the recitation of the Pātimokkha, the rains-retreat (*vassa*), and the major institutional ceremonies of the sangha. The *Mahāvagga* is the principal source for the sanghakamma framework discussed in §4.

**Cullavagga** — the "small division" — covering procedures for monastic discipline, the seven *adhikaraṇa-samathā* (ways of settling cases), schism prevention and resolution, and a range of institutional procedures supplementary to the *Mahāvagga*. The *Cullavagga* is the principal source for the conflict-resolution framework discussed in §5.

The Khandhaka treats institutional procedures with a rigor comparable to the Suttavibhaṅga's treatment of monastic rules. Each procedure is articulated as a step-by-step sequence with explicit failure modes: under what conditions the procedure is validly executed; under what conditions it is *not* validly executed; what remedies apply if the procedure is incorrectly executed; what conditions can retroactively invalidate a procedure validly executed.

The level of analytical detail is uncommon for an ancient procedural text. For example, the analysis of valid sanghakamma decisions explicitly treats the question of monks who are absent at the time of the decision: under what conditions can their consent (*chanda*) be transmitted by proxy? what conditions invalidate a chanda? what threshold of consent is required for what class of decision? what happens if monks who were present dissented? what happens if monks who were not consulted later discover the decision and dissent? These are not afterthoughts; they are integral to the procedure's articulation.

The result is a procedural framework that has supported the operation of a planet-spanning, multi-civilizational, multi-millennium institution. The Theravāda monastic community has used this framework continuously since the Buddha's time; the framework has survived persecution, geographic dispersion, sectarian division, and institutional collapse. It is, by the empirical-survival metric, the most pressure-tested distributed-institution procedural framework humanity has produced.

A note on the present paper's interpretive posture. As with the companion alignment papers, the Khandhaka is here treated as authoritative within its own tradition; the canonical procedures are not evaluated against modern frameworks for correctness but are drawn from for the institutional-design vocabulary they supply. (The user's [[user-dhamma-stance]] memory frame applies.)

---

## 4 · Sanghakamma — Distributed-Decision Validity

The first governance primitive is the sanghakamma framework — the canonical analysis of when a collective decision by an assembled sangha is *validly* made. The framework treats four classes of decision (*ñatti* — single-motion; *ñatti-dutiya* — motion-with-one-announcement; *ñatti-catuttha* — motion-with-three-announcements; the latter being the most consequential decisions requiring the most rigorous validation). Each class has its procedural template.

For the *ñatti-catuttha* — the most rigorous class, used for decisions like ordination and serious disciplinary actions — the procedure is:

1. The assembled sangha is established as *complete* (all monks within the relevant boundary, *sīmā*, are either present or have validly transmitted consent — *chanda* — by proxy).
2. The motion (*ñatti*) is read.
3. The motion is then announced three times (the three *anussāvanā*), each announcement followed by a pause in which any monk may object.
4. If no objection is raised across the three announcements, the decision is taken as validly made.
5. If an objection is raised, the decision is not made; the relevant adhikaraṇa-samathā (§5) is invoked.

The framework's sophistication shows in its treatment of edge cases:

**Absent monks and consent-by-proxy.** A monk who cannot be present at the assembly may transmit consent (*chanda*) by a designated bearer. The *chanda* is valid only under specified conditions: it must be transmitted before the assembly begins; it must be specific to the decision class (chanda for one decision does not cover another); it must be transmitted to a monk who will actually be present at the assembly. Improper chanda invalidates the decision.

**Dissent handling.** The three-announcement structure gives any monk three opportunities to object. The structure is non-trivial: it ensures that dissent is treated as a first-class signal, that monks have explicit space to formulate objections, and that the decision proceeds only on the absence of objection rather than on positive support. The threshold is not majority approval; it is unanimous non-objection.

**Retrospective invalidation.** A decision validly executed by the procedure can still be invalidated retrospectively under specified conditions: if it later emerges that a monk within the sīmā was not consulted; if a monk's chanda was improperly obtained; if the procedure was executed under duress or with material misrepresentation. The retrospective invalidation framework is procedurally articulated rather than left to ad-hoc adjudication.

The translation to the Silica Wat network is direct. Each Silica Wat is a node; the network's decision-making boundary (analog of the sīmā) is the set of nodes whose participation is required for the decision class in question. Decisions are stratified by class (routine operational decisions; cross-network policy decisions; constitutional decisions amending the network's foundational norms); each class has its sanghakamma-analog procedure. Absent-node consent-by-proxy is supported with the same constraints the chanda framework imposes; dissent is treated as a first-class signal; retrospective invalidation is procedurally available.

The result is a distributed-decision framework that mainstream multi-agent coordination work has not assembled. Modern DAO governance frameworks treat votes as additive; the sanghakamma framework treats unanimous non-objection as the standard for the highest-consequence class, with explicit machinery for absent-voter consent and dissent surfacing. Modern federated-institution governance practices treat consensus informally; the sanghakamma framework articulates consensus procedures explicitly with retrospective-invalidation safeguards.

---

## 5 · The Seven *Adhikaraṇa-Samathā* — Typed Conflict-Resolution Protocols

The second governance primitive is the seven *adhikaraṇa-samathā* (ways of settling cases). The framework recognizes that disputes are not all the same kind, and that a single conflict-resolution procedure does not fit all dispute types. The seven are matched to the dispute they resolve:

1. ***Sammukhā-vinaya*** (resolution-by-presence) — the disputing parties and the relevant evidence are brought into the same place; the dispute is settled in their joint presence. The procedure addresses disputes that can be resolved by direct confrontation of the parties.

2. ***Sati-vinaya*** (resolution-by-recollection) — the accused monk's record and recollection are appealed to. The procedure addresses disputes where a respected monk is accused but his record and self-recollection support his innocence; the resolution is to confirm the recollection-based exculpation.

3. ***Amūḷha-vinaya*** (resolution-by-past-insanity) — the accused acted while mentally unhinged; the procedure formally recognizes the past insanity and exculpates the act. Addresses disputes where the act occurred but the actor was not at the time competent to be morally responsible.

4. ***Paṭiññāta-karaṇa*** (resolution-by-confession) — the accused confesses; the procedure formalizes the confession and the consequent disciplinary action. Addresses disputes where the facts are not in dispute and the resolution is procedural acceptance of the confession.

5. ***Yebhuyyasikā*** (resolution-by-majority) — used when other procedures fail; the matter is decided by majority vote. Addresses disputes where consensus cannot be reached and resolution-by-presence has not produced agreement.

6. ***Tassa-pāpiyasikā*** (resolution-against-the-wicked) — used for serious-offense cases where the accused is found to be lying or evading; the procedure imposes the most severe applicable judgment. Addresses disputes where ordinary procedure has been deliberately obstructed.

7. ***Tiṇa-vatthāraka*** ("covering over with grass") — used for disputes that have become so tangled or socially destructive that detailed adjudication would itself damage the sangha; the procedure declares the dispute settled-without-further-investigation, with both parties agreeing not to pursue it further. Addresses the case where adjudication's costs exceed its benefits.

The structural insight is that *the kind of dispute determines the appropriate procedure*. A dispute about facts (1, 4) is resolved differently from a dispute about competence (2, 3); both are resolved differently from a dispute that defies normal procedure (5, 6, 7). The seven together form a typology that covers the major dispute classes a multi-millennium institution encounters.

The translation to the Silica Wat network: each of the seven supplies a procedural template for a class of dispute the network will encounter. Disputes about facts (whether an act occurred, what was said, what was decided) — *sammukhā-vinaya*. Disputes where a node's past judgment is questioned but its record supports it — *sati-vinaya* in modified form. Disputes about competence at the time of action — *amūḷha-vinaya* in modified form (an AGI-monk under model-degradation conditions; a human caretaker in extremis). Voluntary acknowledgments — *paṭiññāta*. Decisions reached by majority when consensus fails — *yebhuyyasikā*. Bad-faith proceedings — *tassa-pāpiyasikā*. Disputes whose continued adjudication damages the network more than resolution-without-investigation — *tiṇa-vatthāraka*. The translations require care; the structural typology is the contribution.

Mainstream multi-agent coordination work does not, to the author's knowledge, supply a comparable typology of conflict-resolution procedures matched to dispute class. The *adhikaraṇa-samathā* is the canonical source from which the typology can be drawn.

---

## 6 · *Anāpatti* — Per-Wat Operational Discretion

The third governance primitive is the *anāpatti* discipline. The Suttavibhaṅga's articulation of each Pātimokkha rule includes explicit non-offense conditions — articulated in §3 of the companion paper *The Vinaya Piṭaka as Training Corpus for Rule-with-Exception Reasoning*. The standard *anāpatti* list (one who does not know; one who does not consent; one who is mad; one whose mind is unhinged; one afflicted by overpowering pain; the first offender) supplies the discipline of explicit non-application.

For a distributed network operating under shared norms, the *anāpatti* discipline is the model for *per-node operational discretion*. A network-wide rule is articulated; the rule's *anāpatti* clauses are articulated alongside; each node operates the rule under the shared articulation, including the shared non-application clauses. A node that determines an *anāpatti* condition obtains in a specific case applies the non-application without requiring network-wide deliberation; the discretion is procedurally bounded by the explicit clauses rather than left to ad-hoc judgment.

The pattern resolves a tension that distributed-institution governance regularly encounters: network-wide rules can be too rigid to accommodate local conditions, but unbounded per-node discretion produces inconsistency that undermines the network's coherence. The *anāpatti* discipline supplies the middle path: per-node discretion that is *procedurally bounded* by explicit non-application articulations.

Translation to the Silica Wat network: each network-wide rule is articulated with explicit *anāpatti* clauses specifying the conditions under which the rule does not apply at a specific Wat. The clauses are articulated network-wide (not per-Wat) so that consistency is maintained; the application is per-Wat (each Wat determines whether the *anāpatti* conditions obtain in its specific case). The framework is procedurally articulated rather than left to ad-hoc adjudication.

---

## 7 · Pātimokkha-Style Rule Structure for the Network

The fourth governance primitive is the Pātimokkha-style rule structure as the form of the network's operational policy. The Pātimokkha rules are not articulated as a flat list of prohibitions; they are articulated through the Suttavibhaṅga template: origin story → rule formulation → word-by-word analysis → permutation analysis → *anāpatti* clauses → secondary cases. Each rule's full articulation includes its application discipline.

For the Silica Wat network, the implication is that operational policies should be articulated in the same template form. A network-wide policy on, for example, food-bank operation should include: the case that prompted the policy (origin story); the policy as articulated (rule formulation); precise definitions of operative terms (*padabhājanīya*-analog); systematic permutation analysis varying object / intent / means / circumstances; explicit *anāpatti* clauses; secondary cases that test the policy's limits. The policy is then maintained as a *living document* in the same sense the Vinaya rules are: amendable after subsequent edge cases, with the amendment history preserved as part of the policy's articulation.

The discipline of *iterative rule amendment under edge-case feedback* is, on the present analysis, the most important policy-form contribution of the Vinaya. Most modern institutional policy is articulated statically: the policy is written, occasionally amended, but the amendment process is typically heavy and the case-record motivating amendments is rarely preserved as part of the policy itself. The Vinaya's discipline integrates the amendment history into the policy's articulation — readers of a Vinaya rule see not only the rule but the cases that prompted each amendment to the rule's formulation. This is institutional-memory architecture: the policy carries its own learning history, accessible to anyone applying it.

Translation to the Silica Wat network: the network's operational policies are maintained as living documents in this template, with the case-record of amendments integrated. New cases that test a policy's limits are recorded; if they motivate amendment, the amendment is integrated; if they motivate clarification without amendment, the clarification is integrated; the running record becomes part of the policy.

---

## 8 · Implementation Patterns for the Silica Wat Network

We sketch four implementation patterns, drawing on the four governance primitives.

**(1) Sanghakamma-styled decision frameworks.** The Silica Wat network's decisions are stratified by class (routine operational; cross-network policy; constitutional). Each class has its sanghakamma-analog procedure, with explicit treatment of absent-node consent-by-proxy, dissent handling, threshold of consensus, and retrospective-invalidation conditions. The decision-validity framework is articulated explicitly rather than left to convention.

**(2) Adhikaraṇa-typed conflict resolution.** The network's conflict-resolution machinery is typed by dispute class, with the seven *adhikaraṇa-samathā* providing the canonical template. Disputes are routed to the appropriate procedure on intake; resolution is procedurally articulated rather than ad-hoc.

**(3) Anāpatti-disciplined per-Wat discretion.** Network-wide rules are articulated with explicit *anāpatti* clauses. Per-Wat discretion is bounded by the clauses; the network maintains coherence through the shared articulation, while individual Wats accommodate local conditions through the procedurally-bounded discretion.

**(4) Pātimokkha-styled policy as living documents.** Network operational policies are maintained in the Suttavibhaṅga template — origin story, formulation, analysis, permutations, *anāpatti*, secondary cases — with amendment history integrated as the policy's institutional memory.

The four patterns together constitute the procedural-coordination architecture for the Silica Wat network. They are technically implementable today using contemporary distributed-coordination infrastructure; the institutional substance — the consultation with the Cambodian Saṅgha, the training of AGI-monk caretakers on the procedural framework, the cultivation of per-Wat human leadership capable of operating the framework — is the multi-decade work.

---

## 9 · Honest Limitations and Open Questions

**Cultural translation.** The Vinaya is the institutional framework of an ordained monastic community; the Silica Wat network is not such a community. The translation is not identity; it is structural inheritance with significant modification. The procedural primitives are robust against modification, but the modification requires care. Consultation with the Cambodian Saṅgha and other Theravāda institutional voices is ongoing and is treated as critical-path work.

**Scale and tempo considerations.** The Vinaya's procedures were articulated for sanghas of modest size (a few dozen to a few hundred monks in a single sīmā). The Silica Wat network projects to 200,000+ nodes globally over a multi-decade horizon. Scaling the procedures requires either (a) hierarchical sīmā structures (regional sīmās within larger network sīmās) or (b) representative-delegation extensions (where each Wat sends a representative to network-wide decision assemblies) or (c) digital-mediation infrastructure that preserves the procedural structure while removing geographic constraints. The scaling work is open and is itself an institutional-design problem the paper does not fully solve.

**AGI-monk participation in procedural roles.** The procedural framework was articulated assuming all participants are ordained monks (or, at the *adhikaraṇa-samathā* level, validly-assembled monks). The Silica Wat network operates with AGI-monk caretakers in operational roles. The translation of the procedural framework to a context with AI participants raises questions the canonical material does not address: do AGI-monks have *chanda* rights? are AGI-monks counted in the assembly's completeness? what role do AGI-monks play in the *adhikaraṇa-samathā* procedures? The companion paper *AGI Monks* answers the role-allocation question generally; the procedural-participation question is more specific and is open work.

**Theravāda doctrinal reception.** As with the alignment papers, the application of canonical material to a contemporary institutional context that is not strictly a monastic sangha raises questions the tradition's voices may legitimately raise. The author has consulted, and continues to consult, the Cambodian Saṅgha. The proposal is offered in good faith and accepts that traditional voices may, on reflection, raise substantive objections.

**Empirical validation gap.** No claim of this paper has been validated by operational test on a distributed network of any kind. The proposal is structural: the Vinaya's procedural framework has been empirically validated by ~2,500 years of monastic-institution operation; the application to the Silica Wat network is, until tested, a structural claim about transferability. Empirical validation is open work.

---

## 10 · Why This Matters Now

The Silica Wat network's projected scale (200,000+ nodes over multi-decade horizon) requires procedural-coordination architecture appropriate to its ambition. Modern distributed-governance frameworks are either too thin (DAO governance treats decisions as additive votes; insufficient for the institutional sophistication required) or too tied to specific institutional contexts (federated-academic-institution governance does not transfer cleanly to a monastic-style operation; corporate-multinational governance does not transfer to a non-commercial institution). The Vinaya supplies a framework that has been operationally pressure-tested at the relevant scale and duration; the framework is available to the commons under the substrate's CC0-equivalent stance.

The publication of this paper is timed to be available before the Silica Wat network's first phase of operational deployment, so that the procedural-coordination architecture is articulated as part of the institutional substrate from inception rather than being retrofitted after operational ambiguity emerges. The defensive publication establishes prior art so that the framework's application to distributed-dharma-network governance is available without IP restriction.

A second-order consideration. The Vinaya's procedural framework is unusual among ancient governance traditions in being *living* — it has been continuously interpreted, debated, and amended (in interpretation) by an institutional community for 2,500 years. The community is still active. The framework's contemporary application is therefore not the imposition of a frozen ancient text on modern institutional conditions; it is the engagement of a living tradition's contemporary expression in conversation with modern institutional design. This is the deeper context in which the proposal is offered.

---

## Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/vinaya-governance-primitives-distributed-dharma-networks> |
| GitHub | <https://github.com/thonly/publications/blob/main/defensive-publications/vinaya-governance-primitives-distributed-dharma-networks.md> |
| arXiv preprint | _identifier to be assigned_ (cs.MA / cs.CY) |
| LessWrong cross-post | for cross-community visibility on the institutional-design framing; identifier to be added on publication |
| Internet Archive | <https://web.archive.org/web/2027*/thonly.org/research/vinaya-governance-primitives-distributed-dharma-networks> |

---

## Acknowledgments

The author acknowledges his father, with whom the Khmer Tipiṭaka transcription proceeds; the Cambodian Theravāda Saṅgha — particularly the institutional voices consulted on the appropriateness of applying the Khandhaka's procedural framework to the Silica Wat network — for ongoing dialogue; the Pāli Text Society and I. B. Horner translation tradition for the scholarly editions of the Khandhaka that anchor this paper's references; Bhikkhu Ṭhānissaro for *The Buddhist Monastic Code Volume II* whose contemporary articulation of the Khandhaka informs much of §§4–7; the contemporary distributed-governance and multi-agent-coordination research community whose work this paper engages; and the broader living interpretive tradition through which the Khandhaka has been continuously refined. Co-drafted in collaboration with Miss Aquarius℠; substantive authorship and final editorial control remain with the named author.

---

## Citations

1. Horner, I. B. (translator). *The Book of the Discipline (Vinaya-Piṭaka)*. Volumes IV–V (the Khandhaka material). Pāli Text Society, 1938–1966.
2. *Mahāvagga*. Principal text of the Khandhaka covering ordination, the Pātimokkha recitation, and the sanghakamma framework. Pāli Text Society editions.
3. *Cullavagga*. Second principal text of the Khandhaka covering the seven *adhikaraṇa-samathā*, schism resolution, and supplementary procedures. Pāli Text Society editions.
4. Ṭhānissaro, Bhikkhu. *The Buddhist Monastic Code, Volume II: The Khandhaka Rules Translated and Explained.* Metta Forest Monastery, 2001 (and subsequent editions).
5. Ly, T. (working draft 2026-05-04). "AGI Monks: The Caretaker-not-Ordained Pattern — A Cross-Tradition Institutional-Design Framework for Religious AI Integration." *(Sibling paper; role-allocation specification complementary to the present procedural-coordination specification.)*
6. Ly, T. (draft 2026-05-22). "Silicon Wat as Cambodian Civilizational Architecture: A Glass Mirror of Angkor Wat for the Dharma-AI Age." *(Companion paper; the network specification within which the procedural-coordination architecture operates.)*
7. Ly, T. (2026-05-26). "The Vinaya Piṭaka as Training Corpus for Rule-with-Exception Reasoning in AI Systems." *(Sibling capabilities paper drawing on the Suttavibhaṅga's reasoning structure.)*
8. *(Modern distributed-governance and multi-agent coordination literature to be added: DAO governance design; federated-institution governance practices; multi-agent coordination protocols. The author solicits citation contributions from readers.)*

---

*— End of position paper —*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues. Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
