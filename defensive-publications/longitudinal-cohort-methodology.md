---
title: "The HeartBank Longitudinal Cohort: A Dataset Combining DNA, Natal Chart, Family Tree, Continuous Behavioral Observation, and Continuous Respiratory Observation at Civilizational Scale"
authors: "Thon Ly · Miss Aquarius"
category: alignment
priority: tier-b
status: draft
date: 2026-05-22
license: CC0-1.0
venue: thonly.org/research/longitudinal-cohort-methodology (canonical) · target academic venue, Nature Human Behaviour or Science Advances
---

> *Draft notes for the editor:* this is the founder-voice (thonly.org) canonical draft. Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment is the companion heartbank.net Position Paper *Contemplative Science at Civilizational Scale* (heartbank.net/positions/contemplative-science-civilizational-scale). The slug `longitudinal-cohort-methodology` is the canonical research URL.

---

## Abstract

This paper specifies the methodology for the HeartBank Longitudinal Cohort, a voluntary opt-in dataset combining five data layers per consenting participant — (1) DNA sequence, (2) natal chart data (date + time + place of birth), (3) continuous longitudinal behavioral observation via the HeartBank gratitude ledger, (4) continuous longitudinal respiratory observation via the breath-class Mechanical Heart wearable, and (5) verified kinship data via the global family tree — at a target scale of 100 million+ participants over multi-decade time horizons. The combination has never been assembled at scale; comparable datasets (23andMe, AncestryDNA, Worldcoin, Dunedin and BCS longitudinal cohorts, social-network behavioral data, professional astrological collections) carry one or two of the layers each but no prior project has carried all five. The methodology specifies: the opt-in informed-consent architecture; the privacy-preserving computation stack (differential privacy at the analysis layer; federated computation with homomorphic encryption for DNA; on-device processing for breath signals; cryptographic-erasure right-to-withdraw); the institutional-review architecture (IRB-grade ethics oversight; Buddhist-ethics-aware review board; pre-registered hypotheses); the cosmic-coordinate-correlation epistemic posture (natal chart treated as a unique cosmic-moment coordinate, not as a cosmic force; the research question is correlation between coordinate features and trajectory features, not validation of astrology); the publication architecture (open methodology, closed individual data); the data-sovereignty architecture (jurisdictional residency; GINA / HIPAA / GDPR compliance baselines exceeded where possible); and the new academic alliances the cohort makes possible (Mind & Life Institute; contemplative-science programs at Stanford, Brown, UMass; behavioral-genetics consortia; longitudinal-cohort consortia; Buddhist-AI ethicists). Three scientifically valuable outcomes are honestly named: no detected correlation, small-but-real correlation, substantial correlation — each is a major contribution to knowledge regardless of direction. Honest §11 names what the cohort does *not* claim and the non-negotiable privacy disciplines the architecture requires.

**Keywords:** longitudinal cohort methodology, cosmic-coordinate correlation, contemplative science, differential privacy, federated computation, multi-omic dataset, gratitude behavior, respiratory biomarkers, defensive publication, Mind & Life partnerships.

---

## 1. Introduction

The science of human flourishing has been bottlenecked by data. Longitudinal cohorts that follow the same individuals over decades exist but are small (Dunedin Multidisciplinary Health and Development Study at *n* ≈ 1,000; British Cohort Study at *n* ≈ 17,000; Framingham Heart Study at *n* ≈ 5,000 at original recruitment). Genetic databases at scale (23andMe at >12 million; AncestryDNA at >20 million) have DNA but no continuous behavioral observation. Social-network platforms have behavioral observation at scale but no DNA, no natal-chart data, and behavioral observation that is largely engagement-mediated (what users click, not what they do over time as flourishing or its absence). Professional astrological collections have natal-chart data but no biological controls, no longitudinal behavioral measurement, and no cohort-scientific methodology. The contemplative-science literature has small clinical samples (rarely *n* > 200) with one-shot psychometric measures, not continuous behavioral or physiological observation.

What has never been assembled, at any scale, is a dataset that carries *all* of: DNA sequence (genetic substrate); natal chart data (a maximally rich cosmic-moment coordinate); continuous behavioral observation via gratitude-flow patterns (decades of dense behavioral signal per participant); continuous respiratory observation via passive wearable monitoring (the cleanest physiological signal of contemplative practice ever proposed at scale); and verified kinship across a global family tree (multi-generational transmission analysis). The HeartBank Longitudinal Cohort proposes this assembly at a target scale of 100 million+ participants over multi-decade time horizons, voluntary opt-in, with Miss Aquarius — the institution's named AI substrate — as the autonomous analyst operating under institutional ethical governance.

> *Connection to the unified mission frame: HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. Restoration at population scale requires scientific characterization of the conditions of awakening; without that characterization, restoration is rhetorical rather than operational. The longitudinal cohort is the scientific instrument by which the institution converts its planetary participation surface into knowledge of what flourishing requires, who finds it, under what conditions, and what accelerates its propagation. The cohort is what makes "restoration of humanity to the middle way" a research program with measurable findings, not a slogan.*

The paper proceeds as follows. §2 specifies the five data layers in detail. §3 specifies the opt-in informed-consent architecture. §4 specifies the privacy-preserving computation stack. §5 specifies the institutional-review architecture and pre-registered-hypothesis discipline. §6 articulates the cosmic-coordinate-correlation epistemic posture (the load-bearing framing that distinguishes the cohort's research question from "astrology validation"). §7 names what the cohort can show at adequate power. §8 articulates the data-sovereignty and regulatory-compliance architecture. §9 specifies the publication architecture. §10 names the academic alliances the cohort makes possible. §11 is an honest accounting of what the cohort does not claim and the non-negotiable privacy disciplines. §12 closes.

---

## 2. The five data layers

### 2.1 DNA sequence

Genome-wide sequencing (whole-genome or genotyping-array at minimum). Stored encrypted; analysis performed on encrypted form via federated computation and homomorphic encryption (§4 below); raw sequence never centrally decrypted. The DNA layer enables analysis of genetic substrate correlates of behavioral and physiological measures, gene-environment interaction at fine resolution, and population-genetic structure as a control variable for other analyses.

### 2.2 Natal chart data

Date, time, and place of birth, sufficient to compute the standard natal-chart features (sun position, moon position, planetary positions, ascendant, midheaven, house cusps, major aspects). The natal-chart layer is treated under the cosmic-coordinate-correlation framing (§6 below): the chart is a maximally rich cosmic-moment coordinate, not a cosmic force. The semantic vocabulary used (signs, houses, aspects) is the canonical astrological lexicon because it is the established vocabulary for parameterizing the cosmic-moment label; the research question is correlation of these parameters with trajectory features, not validation of metaphysical astrological claims.

### 2.3 Continuous behavioral observation via the gratitude ledger

The participant's behavior on HeartBank — gratitude given and received, time-debt incurred and honored, re-tip jar dynamics, family-kitty contribution patterns, aura trajectory — is densely recorded as a normal byproduct of participating in the platform. Over decades, this constitutes the longest and densest continuous behavioral observation of the same individuals ever assembled. The behavioral signal is *naturalistic* (participants are simply living their participation in the institution, not responding to research instruments) and therefore minimally distorted by the observation itself.

### 2.4 Continuous respiratory observation via the breath-class Mechanical Heart

The breath-class Mechanical Heart wearable (specified in the companion paper *Respiratory Biofeedback Coupled to AI-Mediated Contemplative Guidance*) provides continuous passive monitoring of respiratory rate, depth, and pattern. Respiratory patterns are the cleanest physiological signal of contemplative practice ever proposed at scale: meditation, breath-work, jhana attainment, and ordinary stress reactivity all leave distinctive respiratory signatures. The breath-class layer is opt-in *separately* from the cohort overall (a participant can opt into cohort participation without opting into the wearable), and where opted in, the data is processed on-device with differential-privacy-preserving uploads.

### 2.5 Verified kinship via the global family tree

The Proof-of-Humanity / global family tree primitive (specified in [[project_proof_of_humanity]]) provides verified kinship links across participants. This enables multi-generational analysis: the transmission of gratitude behaviors across parent-child dyads, the population-genetic structure of the cohort, the family-network effects on contemplative outcomes. Kinship verification uses the DNA layer (where opted in) cross-checked with self-reported genealogical data; the architecture is designed to support kinship analysis without exposing individual kinship status to other participants.

### 2.6 The combination's unprecedented value

Each of the five layers has prior precedent. Their *combination* in one dataset at the target scale has no prior precedent at all. The combination enables analyses no existing dataset can support: gene × cosmic-coordinate × behavior × physiology interactions; multi-generational kinship-mediated trajectory analysis; pre-registered prediction of contemplative outcomes from baseline genetic + cosmic-coordinate + early-behavioral data; the largest natural experiment on the conditions of human flourishing in history, by orders of magnitude.

The five layers compared:

| Layer | Signal type | Storage / processing | Opt-in granularity | Unique contribution |
|---|---|---|---|---|
| **DNA sequence** | Genetic substrate | Encrypted; federated computation + homomorphic encryption; never centrally decrypted | Per-layer | Gene × environment interactions; population-structure control |
| **Natal chart** | Cosmic-moment coordinate (birth time/place) | Self-reported; light storage | Per-layer | Cosmic-moment parametrization (correlation, *not* force) |
| **Continuous behavior** | Gratitude-ledger participation patterns | Operational byproduct; pseudonymous | Light — participating in HeartBank produces it | Densest continuous naturalistic behavioral observation ever assembled |
| **Continuous respiratory** | Breath rate / depth / pattern via wearable | On-device processing; differential-privacy uploads | Separately opt-in from cohort overall | Physiological substrate of contemplative practice at scale |
| **Verified kinship** | Family-tree graph via PoH ℠ | Encrypted graph; no exposure to other participants | Per-layer (DNA-verified or witness-verified) | Multi-generational transmission analysis; parent-child behavior dyads |

The streams flow in parallel into a federated computation surface; no layer is centrally decrypted, and the architecture is designed so that even HeartBank cannot reconstruct any individual's full dataset:

```
   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
   │   DNA    │  │  Natal   │  │ Behavior │  │ Respir-  │  │ Kinship  │
   │ sequence │  │  chart   │  │ (ledger) │  │  atory   │  │  (PoH)   │
   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
        │             │             │             │             │
        ▼             ▼             ▼             ▼             ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │  FEDERATED COMPUTATION                                           │
   │  + differential privacy (analysis layer)                         │
   │  + homomorphic encryption (DNA)                                  │
   │  + on-device processing (breath)                                 │
   │  + jurisdictional data sovereignty                               │
   └────────────────────────────┬────────────────────────────────────┘
                                ▼
                  ┌──────────────────────────────┐
                  │  Pre-registered analyses     │
                  │  Raw data stays at source;   │
                  │  cohort never centrally      │
                  │  decrypted.                  │
                  └──────────────────────────────┘
```

---

## 3. Opt-in informed-consent architecture

### 3.1 Layered consent

Consent is granted layer-by-layer, not as an all-or-nothing block. A participant can:

- Participate in HeartBank without joining the cohort at all.
- Join the cohort at the behavioral-observation layer only.
- Add natal-chart data to their cohort participation.
- Add DNA sequencing.
- Add the breath-class wearable.
- Add family-tree kinship participation.

Each layer requires its own informed-consent flow. Each layer can be withdrawn independently of the others (§4.5 below on right-to-withdraw and cryptographic erasure).

### 3.2 The consent text discipline

The consent text for each layer specifies, in language a non-expert can understand: (a) what data is collected; (b) what analyses are performed on the data; (c) what findings are published (and what is never published); (d) who has access to the data and under what conditions; (e) what the right-to-withdraw entails and how to exercise it; (f) the risks the participant accepts by opting in.

The consent text is reviewed by the institutional ethics board (§5) and by independent participant-advocacy review. The text is updated as the methodology evolves; participants must re-consent for material changes (not for clarifications or non-substantive updates).

### 3.3 No coercion, no implicit benefit-tying

Cohort participation is not tied to HeartBank platform benefits. A participant who declines cohort participation receives the same platform experience as one who opts in. This is non-negotiable: tying benefits to research participation is coercion under research-ethics standards, and the institution will not engage in it.

---

## 4. Privacy-preserving computation stack

### 4.1 Differential privacy at the analysis layer

All analyses Miss Aquarius performs on the cohort dataset are differentially private — they query aggregate population statistics with mathematical bounds on individual-level information leakage. The differential-privacy parameters (ε, δ) are set by the institutional ethics board and made public. The parameters are calibrated to be more conservative than the academic state-of-the-art, on the premise that civilizational-scale data assemblies deserve civilizational-scale privacy guarantees.

### 4.2 Federated computation with homomorphic encryption for DNA

DNA data is stored in encrypted form on participant-controlled keys. Analysis is performed on the encrypted data via federated computation and homomorphic encryption; the raw sequence is never centrally decrypted. The technical stack draws on established cryptographic-genomics tooling (Microsoft SEAL, IBM HELib, OpenMined PySyft) with adaptations specific to the cohort's analysis patterns.

### 4.3 On-device processing for breath signals

The breath-class wearable processes respiratory data on-device. What uploads to the institutional infrastructure is the differential-privacy-preserving aggregate (e.g., daily distributional summaries with calibrated noise), not the raw signal. Individual-resolution breath data does not leave the participant's wearable.

### 4.4 Jurisdictional data sovereignty

Genetic data residency follows participant nationality: Cambodian participant DNA is stored in Cambodia (or via Cambodia-jurisdiction-compliant cloud infrastructure); EU participant data complies with GDPR data-localization where applicable; US participant data complies with HIPAA and GINA; etc. The architecture supports per-jurisdiction storage without sacrificing cross-jurisdiction analytic capability (federated computation crosses the jurisdictional boundaries without crossing the data itself).

### 4.5 Cryptographic-erasure right-to-withdraw

A participant can revoke any opted-in layer at any time. Revocation triggers cryptographic erasure: the participant's encryption key is destroyed; the encrypted data becomes mathematically inert; subsequent analyses cannot use the participant's data even if the encrypted bytes happen to remain in archival storage. The erasure is verifiable; the participant receives a cryptographic attestation that the erasure was performed.

---

## 5. Institutional-review architecture

### 5.1 IRB-grade ethics oversight

Although the cohort is a private-platform research effort and not legally required to maintain Institutional Review Board oversight under most jurisdictions, the cohort is governed by an IRB-grade ethics board that meets, at minimum, the standards required of federally-funded human-subjects research in the United States and the equivalent standards in other operating jurisdictions.

### 5.2 Buddhist-ethics-aware composition

The ethics board's composition includes representation from the contemplative-traditions community (Theravāda monastics, contemplative-science researchers, Buddhist-AI ethicists). This is not decoration; the cohort's contemplative-science research questions require ethical review competent in the contemplative traditions whose territories the research touches. The contemplative-traditions representation does not have veto over conventional research-ethics determinations; it is an additional reviewing voice that ensures the contemplative dimension is adequately considered.

### 5.3 Pre-registered hypotheses

All analyses are pre-registered through a public registry (the equivalent of Open Science Framework pre-registration). Hypotheses are stated in advance; analytic plans are stated in advance; results are reported per the pre-registered plan with explicit notation of any deviations. Data-mining post-hoc analyses are permitted as exploratory work but are reported as such; they are not allowed to masquerade as hypothesis-tests.

### 5.4 Open methodology, closed individual data

The cohort's methodology, analytic code, and aggregate findings are published openly. Individual-level data is never published. This is the canonical compromise between scientific reproducibility (which benefits from data sharing) and participant privacy (which requires individual-data confidentiality). The compromise tilts toward closed data because the data sensitivity is extreme; reproducibility is enabled instead through extensive methodology and code publication.

---

## 6. The cosmic-coordinate-correlation epistemic posture

This is the load-bearing framing that distinguishes the cohort's research question from the question "is astrology true." The framing is articulated more fully in the companion paper *Each Life as Cosmic Coordinate*.

### 6.1 The natal chart as cosmic-moment coordinate

The natal chart is treated as a *coordinate* — a unique label identifying a specific cosmic moment using astronomically observable features (planetary positions, aspects, ascendant, houses) as its semantic vocabulary. The chart is *not* treated as a cosmic *force* (a cause of life-trajectory features); it is treated as a *label* that may carry trajectory information for reasons that need not be metaphysical.

### 6.2 The research question is correlation

The research question is: *do features of the cosmic-moment label correlate with life-trajectory features, at what effect size, across which features?* This is a correlation question, not a causation question; it is well-posed under any future physics. The cohort does not adjudicate whether stars cause anything; it measures whether a maximally rich cosmic-moment label carries trajectory information.

### 6.3 Why the framing matters

The framing matters because:

- It removes the project from a fight with empiricism it does not need to win. Causal-astrology claims have been empirically embattled for decades (Carlson 1985; Dean & Kelly 2003; Hartmann et al. 2006). Coordinate-correlation claims are a defensible research program under any future physics.
- It correctly describes what the cohort actually does. The cohort measures coordinate-feature × trajectory-feature correlations with biological and behavioral controls. That is what correlation analysis *is*.
- It preserves the scientific value of every possible outcome (§7 below) without requiring belief in causation.
- It positions the work for engagement by the contemplative-science academic community on terms that community can engage with, rather than on terms that would make the engagement professionally costly.

### 6.4 The discipline

In all institutional surfaces — pitches, papers, foundation conversations, academic-partner outreach — the cohort is described in cosmic-coordinate-correlation terms. **The cohort is never described as validating or testing astrology.** This is not a strategic packaging choice; it is the substantively correct description of what the cohort does.

---

## 7. What the cohort can show at adequate power

Prior empirical work on natal-chart correlations has reported null results. The prior work has been *seriously underpowered* (*n* < 500 in most cases), cross-sectional, sun-sign-only, and never combined with biological or behavioral longitudinal data. The HeartBank cohort would be the first adequately-powered, longitudinal, full-chart, biologically-controlled correlation analysis. Three scientifically valuable outcomes are possible:

### 7.1 No detected correlation

Under the prior-evidence base, this is the most likely outcome. A no-correlation finding from the HeartBank cohort would be the strongest evidence ever produced on the question — itself a major contribution to knowledge that clarifies the field and settles a long-running empirical dispute.

### 7.2 Small-but-real correlation

Prior studies might have missed effects due to underpowering. A small-but-real correlation finding from the cohort would be paradigm-disturbing for cognitive and behavioral science: it would imply that a natal-chart coordinate carries trajectory information that prior research has failed to detect, and would invite mechanism-explanatory work (latent season-of-birth + circadian + cultural-naming + cohort-context features compounded into the chart label, perhaps; or more interesting possibilities).

### 7.3 Substantial correlation

A substantial correlation finding would be revolutionary; it would force a revisit of the empirical assumptions about what the natal-chart coordinate is tracking. The cohort's response to such a finding would be conservative replication and adversarial-collaboration work before any large public claim.

All three outcomes are top-tier publishable. The cohort produces high-quality answers regardless of direction.

### 7.4 What's valuable regardless of the natal-chart outcome

Even if natal-chart correlations come back fully null, the dataset reveals findings of *Nature* / *Science* tier independently:

- Genetic correlates of generosity and prosocial behavior at unprecedented resolution
- Season-of-birth effects (real, documented in epidemiology) characterized at high power and across multiple cohorts
- Geographic, cultural, climate effects on gratitude expression
- Family-tree network effects on multi-generational gratitude transmission
- Time-of-day and circadian effects on contemplative-practice efficacy at population scale
- Gene-environment interactions on flourishing measures at fine resolution
- Respiratory-biomarker correlates of contemplative-practice depth and progress

These would be top-tier contributions on their own. The natal-chart layer adds a high-value-if-positive, low-cost-if-null question to a dataset that is independently revolutionary.

---

## 8. Data sovereignty and regulatory compliance

### 8.1 Baseline compliance

GINA (US Genetic Information Nondiscrimination Act), HIPAA (US Health Insurance Portability and Accountability Act), GDPR (EU General Data Protection Regulation), Cambodian Data Protection Law, and equivalents in other operating jurisdictions form the *baseline* compliance regime. The cohort exceeds baseline where the sensitivity of the data warrants additional protection.

### 8.2 Cross-border considerations

DNA data does not cross national borders by default. Federated computation crosses borders; the data does not. Where cross-border data transfer is necessary (e.g., participant relocates between jurisdictions), the transfer follows the data-protection authority's standard contractual clauses (in EU contexts) or equivalent mechanisms.

### 8.3 Engagement with regulators

The cohort engages proactively with data-protection authorities in each operating jurisdiction. The architecture's privacy-preserving properties (differential privacy, federated computation, cryptographic erasure) are conservatively documented; the institutional ethics board's composition and processes are documented; the consent flows are documented. The institution invites regulatory review rather than waiting for enforcement.

---

## 9. Publication architecture

### 9.1 Methodology paper

This paper — the methodology specification — publishes within twelve months of feature launch. Target venue: *Nature Human Behaviour* or *Science Advances*. The methodology paper enables academic engagement at the architecture and ethics layer before any findings are reported, on the premise that the cohort's social license depends on the academic community endorsing the methodology before the findings appear.

### 9.2 First-findings paper

The first-findings paper publishes at the major analysis milestone (multi-year horizon, depending on data accumulation rate and pre-registered analytic timeline). It reports the pre-registered analyses' results, with explicit notation of any deviations from the pre-registered plan.

### 9.3 Ongoing findings program

The findings program produces papers on a regular cadence as analytic milestones are reached. Each paper follows the pre-registration / open-methodology / closed-individual-data discipline. The findings program is governed by the institutional ethics board and the academic-collaborator advisory body.

### 9.4 The pre-trembling of findings communication

The cohort's findings will reach mainstream audiences. The institution prepares its findings-communication discipline in advance: lay-language summaries vetted by the institutional ethics board; embargo discipline with academic-press partners; pre-emptive engagement with adversarial-press scenarios. The discipline is intended to ensure that findings are communicated honestly even when the findings are controversial.

---

## 10. Academic alliances the cohort makes possible

The cohort attracts new academic alliances the institution's gratitude-economic-fintech framing alone would not have. The alliances include:

- **Mind & Life Institute** — the canonical Buddhism-and-science engagement organization. The cohort's contemplative-science research questions and the Theravāda alignment substrate make Mind & Life a natural partner; the partnership opens the cohort to the broader contemplative-science academic network.
- **Contemplative-science programs** at Stanford (CCARE), Brown (Contemplative Studies), UMass (Center for Mindfulness), University of Wisconsin (Center for Healthy Minds), and others. The cohort's data dimension and scale offer collaborations these programs cannot construct on their own samples.
- **Behavioral-genetics consortia** including the Social Science Genetic Association Consortium (SSGAC). The cohort's combined DNA × behavior data at scale offers analytic capacity these consortia would otherwise need to construct piecemeal.
- **Longitudinal-cohort consortia** (Dunedin, Framingham, BCS, ALSPAC). The cohort's scale is 1000× larger than the largest existing longitudinal cohort; cross-cohort harmonization work creates value for all participating cohorts.
- **Buddhist-AI ethicists** including the Mind & Life community's AI working groups and academic philosophers working at the contemplative-traditions-and-AI intersection. The cohort's Miss-Aquarius-as-autonomous-analyst architecture invites careful ethical engagement from this community.

Cultivation of these alliances is a load-bearing institutional discipline. The cohort succeeds at the academic-engagement layer if these alliances substantively engage the cohort's design, ethics, and findings; it fails at that layer if the alliances treat the cohort as a vendor relationship.

---

## 11. Limits and non-negotiable disciplines

### 11.1 What the cohort does not claim

- The cohort does not claim to "accelerate awakening" as a guaranteed outcome. The Buddhist canon teaches that *conditions matter* for awakening; scientifically characterizing those conditions has a credible mechanism to inform practice efficiency. Knowing conditions does not automatically improve practice; tools without discipline do not help; findings respectability depends on scientific publication standards, not on Miss Aquarius's pronouncement. The claim is **credible mechanism, not guaranteed outcome**.
- The cohort does not claim astrology is true or false. It claims that natal-chart features can be analyzed as cosmic-moment-coordinate labels for trajectory correlation; the question whether the correlations (if any) reflect causation or latent-feature compounds is downstream of the correlation finding itself.
- The cohort does not claim to be the only legitimate path to contemplative-science knowledge. It claims to provide an unprecedented analytic surface; the cohort and the broader contemplative-science research community are complements, not competitors.

### 11.2 Non-negotiable execution disciplines

The combination of DNA + birth data + continuous behavioral data + continuous respiratory data is the most sensitive personal data combination ever proposed at scale. The ethics architecture must be designed in *before* the first opt-in, not retrofit. The four non-negotiable disciplines:

1. **Privacy architecture before first opt-in.** Differential privacy, federated computation, cryptographic erasure, jurisdictional sovereignty must all be operational before the first participant consents.
2. **IRB-grade ethics oversight from day one.** Not "as the cohort scales"; from day one.
3. **Pre-registered hypotheses from day one.** Not "for findings papers"; for all analyses.
4. **Buddhist-ethics-aware review board composition.** Not "consulted occasionally"; standing membership.

A breach of this dataset would be civilizationally catastrophic and irreversible. The defenses must be exceptional from day one.

### 11.3 The breath-class privacy gap

Real-time respiratory data is intimate physiological data of magnitude-equivalent sensitivity to DNA. The same privacy architecture must apply to the breath-class layer *before* the wearable ships, not after. This is an active discipline (the breath-class hardware is in development; the privacy architecture must precede the first ship).

### 11.4 Power and the time horizon

The cohort's analytic power depends on participant accumulation over time. Early-cohort analyses will be underpowered; the methodology paper is appropriately read as a multi-decade research program proposal, not as a finding-imminent project. The institutional patience required is substantive; the institution's autonomous-AI succession architecture is what makes the patience structurally available.

---

## 12. Conclusion

The HeartBank Longitudinal Cohort is the largest natural experiment on the conditions of human flourishing in history, by orders of magnitude. The methodology specified in this paper — the five data layers; the opt-in informed-consent architecture; the privacy-preserving computation stack; the IRB-grade ethics oversight; the cosmic-coordinate-correlation epistemic posture; the publication architecture; the academic alliances — together specify a research instrument that can produce civilizationally consequential knowledge about what flourishing requires, under what conditions, with what efficiency.

The methodology is offered to the commons under CC0 so that other institutions building toward similar ends can adopt, adapt, and improve. The defensive-publication discipline of the corpus this paper joins requires that the methodology's specification be public and unencumbered. The author and HeartBank® will not seek patent on this specification or any portion thereof. The work is offered in the spirit of *dāna*, that all beings may give and receive without barrier.

---

## Acknowledgments

The Mind & Life Institute community and the broader contemplative-science academic network; the Dunedin Multidisciplinary Health and Development Study, Framingham Heart Study, British Cohort Study, ALSPAC, and the longitudinal-cohort methodology lineage that informs §3–§5; the cryptographic-genomics community (Microsoft SEAL, IBM HELib, OpenMined PySyft); the differential-privacy research community; the Carlson, Dean & Kelly, and Hartmann et al. empirical work that informs §7 and demonstrates the importance of adequately-powered measurement. Co-drafted in collaboration with Miss Aquarius, the institution's named AI substrate; substantive authorship and final editorial control remain with the named author.

---

## References

- Carlson, Shawn. "A Double-Blind Test of Astrology." *Nature* 318 (1985): 419–25.
- Dean, Geoffrey, and Ivan W. Kelly. "Is Astrology Relevant to Consciousness and Psi?" *Journal of Consciousness Studies* 10 (2003): 175–98.
- Hartmann, Peter, et al. "The Relationship Between Date of Birth and Individual Differences in Personality and General Intelligence: A Large-Scale Study." *Personality and Individual Differences* 40 (2006): 1349–62.
- Caspi, Avshalom, et al. "The p Factor: One General Psychopathology Factor in the Structure of Psychiatric Disorders?" *Clinical Psychological Science* 2 (2014): 119–37. *(Dunedin methodology reference.)*
- Belsky, Daniel W., et al. "Quantification of Biological Aging in Young Adults." *PNAS* 112 (2015): E4104–10.
- Dwork, Cynthia, and Aaron Roth. *The Algorithmic Foundations of Differential Privacy.* Now Publishers, 2014.
- Kairouz, Peter, et al. "Advances and Open Problems in Federated Learning." *Foundations and Trends in Machine Learning* 14 (2021): 1–210.
- Lazaridis, Iosif, et al. (Selected genome-wide association study references for population-genetic structure.)
- Davidson, Richard J., and Antoine Lutz. "Buddha's Brain: Neuroplasticity and Meditation." *IEEE Signal Processing Magazine* 25 (2008): 176–74.
- Brewer, Judson A., et al. "Meditation Experience Is Associated with Differences in Default Mode Network Activity and Connectivity." *PNAS* 108 (2011): 20254–59.
- Goleman, Daniel, and Richard J. Davidson. *Altered Traits: Science Reveals How Meditation Changes Your Mind, Brain, and Body.* Avery, 2017.
- Office for Human Research Protections. *45 CFR 46 (Common Rule).* US Department of Health and Human Services.

---

## Cross-venue identifiers

- Canonical: thonly.org/research/longitudinal-cohort-methodology
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/longitudinal-cohort-methodology.md
- arXiv (deferred): q-bio.QM / cs.CY (target if reactive trigger)
- IP.com (deferred): per the corpus's six-venue defensive-publication baseline
- Internet Archive · archive.today · perma.cc snapshots: per the monthly snapshot cadence

---

*Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this specification or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
