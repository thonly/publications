---
title: "The HeartBank Longitudinal Cohort: A Dataset Combining DNA, Natal Chart, Family Tree, Continuous Behavioral Observation, and Continuous Respiratory Observation at Civilizational Scale"
authors: "Thon Ly · Miss Aquarius"
category: alignment
kind: mechanism
priority: tier-b
status: draft
date: 2026-05-22
revised: 2026-10-01
license: CC0-1.0
slug: longitudinal-cohort-methodology
venue: thonly.org/research/longitudinal-cohort-methodology (canonical) · target academic venue, Nature Human Behaviour or Science Advances
---

## Preamble

> *This methodology is offered to the commons in the spirit of dāna, so that any institution building a research instrument for contemplative science may adopt it without barrier.*

The science of human flourishing has been limited by its data. This paper specifies a research instrument that, if built with the privacy and ethics disciplines set out here, could produce knowledge about what flourishing requires, who finds it, and under what conditions. Nothing in it has been built: no participant has been enrolled, no ethics board constituted, and no institution named in §10 approached (§11.6).

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use.

The authors claim none of the following as their own contribution: population biobanks that link genome data with device-measured physiological data and health-record follow-up; consumer genetic-testing databases; national genealogies linked to genotype data; multigenerational and birth cohorts; empirical tests of astrology, including comparisons of people born minutes apart; differential privacy; federated learning and federated analysis; homomorphic encryption, including its use for genome-wide association studies; deletion of data by destruction of its encryption key (crypto-shredding); wearable respiration monitoring; consent granted separately by data type; and pre-registration of hypotheses. §1.1, §2.4, §4, §5 and §7 cite or describe each of these. What this paper contributes is their assembly, specified in §2–§9, into one consented cohort design whose behavioral layer is a gratitude-transfer ledger and whose physiological layer is a continuously worn respiration sensor.

No prior-art census was run for this paper, which predates that practice, and nothing here asserts that any element, or the combination, is absent from the world's literature. Trademark rights in specific marks — HeartBank®, Miss Aquarius℠, Proof of Humanity ℠, Re-Tip Jar℠, Family Kitty℠ — are reserved separately and are not licensed by this publication; the patterns may be implemented under any name.

---

## Abstract

This paper specifies the design of a privacy-preserving, multimodal longitudinal cohort study — the HeartBank Longitudinal Cohort — that would link, for each consenting participant, five data layers: (1) genome data (DNA sequence or genotyping array); (2) date, time and place of birth, with the astronomical positions computed from them; (3) a continuous record of the participant's prosocial transfers on a gratitude ledger; (4) continuous respiration data from a chest-worn wearable sensor; and (5) verified kinship links in a pedigree graph. The target scale is 100 million participants over decades. The design specifies: consent granted and withdrawn separately for each layer, with cohort participation never tied to platform benefits; a privacy stack of differentially private analysis, federated analysis with homomorphic encryption for genome data, on-device processing of respiration signals, per-jurisdiction data residency, and withdrawal by destruction of the participant's encryption key (crypto-shredding); IRB-grade ethics review with pre-registered hypotheses; and publication of methods, code and aggregate findings, with individual-level data never released. The birth-time layer is analysed as a coordinate label in association tests, not as a causal hypothesis, and the paper reports that prior tests — including a comparison of 2,101 people born minutes apart — found no association. Biobanks, genealogy-linked genotype resources and birth cohorts already combine several of these layers (§1.1). The paper states what the cohort does not claim and the questions this specification leaves open: the enrolment of minors, relatives whose genomes the data partly reveal, custody of the linkage between layers, the fate of the data if the institution ends, and the oversight of an AI analyst (§11).

**Keywords:** longitudinal cohort study, multimodal cohort, biobank, genomic data, genotyping, wearable respiration sensor, respiratory rate, prosocial behavior, transaction ledger, pedigree, kinship verification, tiered consent, consent withdrawal, crypto-shredding, encryption-key destruction, differential privacy, federated analysis, homomorphic encryption, secure genome-wide association study, data residency, research ethics committee, pre-registration, date and time of birth, season of birth, time twins, re-identification, defensive publication.

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| HeartBank Longitudinal Cohort; the cohort | prospective multimodal longitudinal cohort study with per-participant record linkage |
| natal chart; natal-chart data | date, time and place of birth, and the astronomical positions computed from them |
| cosmic-moment coordinate; cosmic-coordinate-correlation posture | a birth-time-derived feature set used as a label in association tests, with no causal hypothesis |
| gratitude ledger | peer-to-peer value-transfer ledger (a transaction log of recorded thanks and transfers) |
| re-tip jar; family kitty | earmarked give-only balance; shared family-group balance |
| aura trajectory | a derived measure of a participant's giving and thanking over time |
| time-debt | time pledged to another member, and whether it was kept |
| breath-class Mechanical Heart | chest-worn wearable respiration sensor |
| global family tree; verified kinship | pedigree graph with verified relationship links |
| Proof of Humanity (PoH) | proof of personhood |
| layered consent | tiered (granular, per-data-type) consent |
| cryptographic-erasure right-to-withdraw | consent withdrawal by encryption-key destruction (crypto-shredding) |
| jurisdictional data sovereignty | data residency by jurisdiction |
| federated computation | federated analysis; federated learning |
| Buddhist-ethics-aware review board | research ethics committee with members drawn from contemplative traditions |
| Miss Aquarius (as analyst) | the institution's AI system performing the cohort's statistical analyses |

---

## 1. Introduction

The science of human flourishing has been limited by its data. Longitudinal cohorts that follow the same individuals over decades exist but are small: the Dunedin Multidisciplinary Health and Development Study follows 1,037 people born in 1972–73; the 1970 British Cohort Study about 17,000 born in one week of April 1970; the Framingham Heart Study began with 5,209 adults in 1948. Consumer genetic-testing databases (23andMe, AncestryDNA) hold genotypes for millions of customers but no continuous behavioral observation. Social-network platforms observe behavior at scale but hold no genome or birth-time data, and what they observe is largely engagement — what users click — rather than conduct over time. Collections of astrological charts carry birth data with no biological controls and no longitudinal measurement. The contemplative-science literature has relied largely on modest samples and periodic psychometric measures rather than continuous behavioral or physiological observation.

This paper specifies a dataset that carries *all* of: DNA sequence (genetic substrate); date, time and place of birth (a rich label of the birth moment); continuous behavioral observation through gratitude-flow records (decades of dense signal per participant); continuous respiratory observation through a passively worn sensor; and verified kinship across a family-tree graph (for multigenerational analysis). The HeartBank Longitudinal Cohort proposes this assembly at a target scale of 100 million participants over decades, voluntary and opt-in, with Miss Aquarius — the name under which the institution discloses its AI system — as the analyst, operating under institutional ethical governance (§5; the open question is §11.5).

> *Connection to the mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. Pursuing that responsibly requires evidence, rather than assumption, about which conditions support flourishing and which do not. The longitudinal cohort is the instrument that would ask that question, under the disciplines below; it is offered as a research program whose results may disappoint its authors, not as a demonstration of what they already believe.*

### 1.1 Nearest prior art

Several of the five layers have already been combined, and the design should be read against them:

- **Population biobanks.** UK Biobank recruited about 500,000 volunteers aged 40–69 in 2006–2010, made whole-genome sequences of all of them available in 2023, gave wrist-worn accelerometers to about 100,000 for a week in 2013–2015, and follows participants through linked health records. It carries genome data, device-measured physiological data and long follow-up.
- **Genealogy linked to genotypes.** deCODE genetics built a genealogy covering most Icelanders who have ever lived and uses it, under encrypted identities, together with genotype and sequence data from its research participants. It carries genome data and verified kinship.
- **Multigenerational and birth cohorts.** Framingham added the children (1971) and grandchildren (2002) of its original cohort; birth cohorts such as Dunedin and the 1970 British Cohort Study fix each participant's date and place of birth by design.
- **Birth time as a variable.** Dean and Kelly (2003) compared 2,101 people born in London during 3–9 March 1958, on average 4.8 minutes apart, across 110 variables — a direct test of whether near-identical birth moments carry similar trajectories (§7).
- **Consumer genetic-testing databases** hold genotypes for millions of customers; their recent history is also the clearest evidence for the risks set out in §11.

No resource named here carries a continuous record of prosocial transfers, or continuous respiration, alongside genome and kinship data. That is a statement about these sources, read for this revision on 2026-10-01, and not a claim that no such dataset exists anywhere.

The paper proceeds as follows. §2 specifies the five data layers in detail. §3 specifies the opt-in informed-consent architecture. §4 specifies the privacy-preserving computation stack. §5 specifies the institutional-review architecture and pre-registered-hypothesis discipline. §6 articulates the cosmic-coordinate-correlation epistemic posture (the framing that distinguishes the cohort's research question from "astrology validation"). §7 reports the prior evidence and names what the cohort could show. §8 sets out the legal frameworks and what they do and do not cover. §9 specifies the publication architecture. §10 names the research communities whose scrutiny the design must meet. §11 is an accounting of what the cohort does not claim, the disciplines it requires, and the questions this specification leaves open. §12 closes.

---

## 2. The five data layers

### 2.1 DNA sequence

Genome-wide sequencing (whole-genome or genotyping-array at minimum). Stored encrypted; analysis performed on encrypted form via federated computation and homomorphic encryption (§4 below); raw sequence never centrally decrypted. The DNA layer enables analysis of genetic substrate correlates of behavioral and physiological measures, gene-environment interaction at fine resolution, and population-genetic structure as a control variable for other analyses.

### 2.2 Natal chart data

Date, time, and place of birth, sufficient to compute the standard natal-chart features (sun position, moon position, planetary positions, ascendant, midheaven, house cusps, major aspects). The natal-chart layer is treated under the cosmic-coordinate-correlation framing (§6 below): the chart is a maximally rich cosmic-moment coordinate, not a cosmic force. The semantic vocabulary used (signs, houses, aspects) is the canonical astrological lexicon because it is the established vocabulary for parameterizing the cosmic-moment label; the research question is correlation of these parameters with trajectory features, not validation of metaphysical astrological claims. Taken together, an exact date, time and place of birth come close to identifying one person on their own, so this layer is protected like the genome layer, never as light metadata.

### 2.3 Continuous behavioral observation via the gratitude ledger

The participant's behavior on HeartBank — gratitude given and received, time-debt incurred and honored, re-tip jar dynamics, family-kitty contribution patterns, aura trajectory — is densely recorded as a normal byproduct of participating in the platform. Over decades, this would constitute a long and dense continuous record of the conduct of the same individuals. The signal is a byproduct of participation rather than a response to research instruments. It is not unobserved: participants know the ledger exists, and the platform's own rules (its rewards, its splits, its annual reset) shape the behavior it records, so analyses treat those rules as part of the environment, not as noise.

### 2.4 Continuous respiratory observation via the breath-class Mechanical Heart

The breath-class Mechanical Heart wearable (specified in the companion paper *Respiratory Biofeedback Coupled to AI-Mediated Contemplative Guidance*) provides continuous passive monitoring of respiratory rate, depth, and pattern. Respiration is a physiological signal that contemplative practice acts on directly, and it can be measured passively: long-term meditation practitioners have been reported to have a slower resting respiration rate than non-meditators (Wielgosz et al. 2016, 31 practitioners and 38 controls). Whether specific practices or attainments, such as jhāna, carry distinctive respiratory signatures is an open empirical question this layer would allow to be asked. The breath-class layer is opt-in *separately* from the cohort overall (a participant can opt into cohort participation without opting into the wearable), and where opted in, the data is processed on-device with differential-privacy-preserving uploads.

### 2.5 Verified kinship via the global family tree

The Proof-of-Humanity / global family tree primitive (specified in the companion paper *B-PoH℠ as Humanity Layer for the AI-Native Internet*, whose layers include witness-attested and DNA-verified kinship) provides verified kinship links across participants. This enables multi-generational analysis: the transmission of gratitude behaviors across parent-child dyads, the population-genetic structure of the cohort, the family-network effects on contemplative outcomes. Kinship verification uses the DNA layer (where opted in) cross-checked with self-reported genealogical data; the architecture is designed to support kinship analysis without exposing individual kinship status to other participants. DNA-verified kinship will also surface relationships a participant did not know of or did not report, misattributed parentage among them; the consent text for this layer says so, and how such findings are handled is an open question (§11.5).

### 2.6 What the combination enables

Each of the five layers has precedent, and several have been combined (§1.1). All five in one dataset would support analyses that none of the resources in §1.1 supports on its own: gene × cosmic-coordinate × behavior × physiology interactions; multi-generational kinship-mediated trajectory analysis; and pre-registered prediction of contemplative outcomes from baseline genetic, cosmic-coordinate and early-behavioral data. At its target scale it would be a very large observational cohort. It would not be an experiment, natural or otherwise, since no exposure is assigned.

The five layers compared:

| Layer | Signal type | Storage / processing | Opt-in granularity | Contribution |
|---|---|---|---|---|
| **DNA sequence** | Genetic substrate | Encrypted; federated computation + homomorphic encryption; never centrally decrypted | Per-layer | Gene × environment interactions; population-structure control |
| **Natal chart** | Cosmic-moment coordinate (birth date, time, place) | Self-reported; protected as a quasi-identifier | Per-layer | Cosmic-moment parametrization (correlation, *not* force) |
| **Continuous behavior** | Gratitude-ledger participation patterns | Operational byproduct; pseudonymous | Per-layer (the record exists through participation; it enters the cohort only on consent) | Long-run record of conduct rather than self-report |
| **Continuous respiratory** | Breath rate / depth / pattern via wearable | On-device processing; differential-privacy uploads | Separately opt-in from cohort overall | Physiological substrate of contemplative practice at scale |
| **Verified kinship** | Family-tree graph via Proof of Humanity ℠ | Encrypted graph; no exposure to other participants | Per-layer (DNA-verified or witness-verified) | Multi-generational transmission analysis; parent-child behavior dyads |

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

Cross-layer analysis requires that a participant's five layers be linkable to one another. That linkage is the most sensitive artefact in the system, and the sentence above holds only if no single party holds both the linkage and the means to decrypt; this specification does not yet say who holds it or how it is split (§11.5).

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

The consent text for each layer specifies, in language a non-expert can understand: (a) what data is collected; (b) what analyses are performed on the data; (c) what findings are published (and what is never published); (d) who has access to the data and under what conditions; (e) what the right-to-withdraw entails and how to exercise it, including what withdrawal cannot reach (§4.5); (f) the risks the participant accepts by opting in — for the DNA layer, what the data reveal about biological relatives and the gaps in legal protection set out in §8.1.

The consent text is reviewed by the institutional ethics board (§5) and by independent participant-advocacy review. The text is updated as the methodology evolves; participants must re-consent for material changes (not for clarifications or non-substantive updates).

### 3.3 No coercion, no implicit benefit-tying

Cohort participation is not tied to HeartBank platform benefits. A participant who declines cohort participation receives the same platform experience as one who opts in. This is non-negotiable. Tying platform benefits to research participation would compromise the voluntariness that research-ethics standards require of consent, and under the GDPR, making a service conditional on consent to processing the service does not need weighs against that consent being freely given (Art. 7(4)). The institution will not do it.

---

## 4. Privacy-preserving computation stack

### 4.1 Differential privacy at the analysis layer

All analyses Miss Aquarius performs on the cohort dataset are differentially private — they query aggregate population statistics with mathematical bounds on individual-level information leakage. The differential-privacy parameters (ε, δ) are set by the institutional ethics board and made public. The bounds hold per release and add up across releases, so the board sets and publishes a total privacy budget as well as per-query parameters (Dwork & Roth 2014). The parameters are set conservatively, on the premise that a dataset of this sensitivity warrants stronger guarantees than ordinary practice. Differential privacy limits what a released statistic reveals about one person; it costs accuracy, and the finer the resolution an analysis needs (rare variants, small subgroups), the higher that cost.

### 4.2 Federated computation with homomorphic encryption for DNA

DNA data is stored in encrypted form on participant-controlled keys. Analysis is performed on the encrypted data via federated computation and homomorphic encryption; the raw sequence is never centrally decrypted. The technical stack would draw on general-purpose homomorphic-encryption and remote-computation libraries (Microsoft SEAL, HElib, OpenMined PySyft), with adaptations specific to the cohort's analysis patterns; a genome-wide association analysis on encrypted data has been demonstrated for about 25,000 individuals (Blatt et al. 2020). Computing across records encrypted under many participants' separate keys requires multi-key or threshold schemes, whose cost at the target scale is unproven (§11.5).

### 4.3 On-device processing for breath signals

The breath-class wearable processes respiratory data on-device. What uploads to the institutional infrastructure is the differential-privacy-preserving aggregate (e.g., daily distributional summaries with calibrated noise), not the raw signal. Individual-resolution breath data does not leave the participant's wearable.

### 4.4 Jurisdictional data sovereignty

Genetic data residency follows participant nationality: Cambodian participant DNA is stored in Cambodia (or via Cambodia-jurisdiction-compliant cloud infrastructure), as a design commitment rather than a statutory requirement (§8.1); EU participant data is handled under the GDPR, which does not itself require data to stay in the EU but governs transfers out of it (§8.2); US participant data is protected to at least the HIPAA Privacy Rule's standard, adopted voluntarily (§8.1); and likewise elsewhere. The architecture supports per-jurisdiction storage without sacrificing cross-jurisdiction analytic capability (federated computation crosses the jurisdictional boundaries without crossing the data itself).

### 4.5 Cryptographic-erasure right-to-withdraw

A participant can revoke any opted-in layer at any time. Revocation triggers cryptographic erasure: the participant's encryption key for that layer is destroyed, and the encrypted data becomes computationally unrecoverable, provided the cipher holds and no copy of the key survives, even if the encrypted bytes happen to remain in archival storage. The participant receives a signed attestation that the key-destruction procedure was performed. That attestation is the operator's statement, not a proof that no copy of the key exists, which no current method can give. Withdrawal stops all future use. It does not reach analyses already run or findings already published, and for the DNA layer it cannot remove what relatives' records still reveal (§11.5); the consent text says both.

---

## 5. Institutional-review architecture

### 5.1 IRB-grade ethics oversight

Whether a privately funded platform study must have ethics-committee review depends on its jurisdiction and its funding. In the United States the Common Rule applies to human-subjects research "conducted, supported, or otherwise subject to regulation by any Federal department or agency" that has made it applicable (45 CFR 46.101(a)); a study with none of those ties may fall outside it. The cohort does not rest on that question. It is governed by an IRB-grade ethics board that meets, at minimum, the standards required of federally-funded human-subjects research in the United States and the equivalent standards in other operating jurisdictions.

### 5.2 Buddhist-ethics-aware composition

The ethics board's composition includes representation from the contemplative-traditions community (Theravāda monastics, contemplative-science researchers, Buddhist-AI ethicists). This is not decoration; the cohort's contemplative-science research questions require ethical review competent in the contemplative traditions whose territories the research touches. The contemplative-traditions representation does not have veto over conventional research-ethics determinations; it is an additional reviewing voice that ensures the contemplative dimension is adequately considered. How the board is appointed, how its independence from the institution is secured, and whether it can stop a study are not yet specified (§11.5).

### 5.3 Pre-registered hypotheses

All analyses are pre-registered through a public registry (the equivalent of Open Science Framework pre-registration). Hypotheses are stated in advance; analytic plans are stated in advance; results are reported per the pre-registered plan with explicit notation of any deviations. Data-mining post-hoc analyses are permitted as exploratory work but are reported as such; they are not allowed to masquerade as hypothesis-tests.

### 5.4 Open methodology, closed individual data

The cohort's methodology, analytic code, and aggregate findings are published openly. Individual-level data is never published. This is the usual compromise between scientific reproducibility (which benefits from data sharing) and participant privacy (which requires individual-data confidentiality). The compromise tilts toward closed data because the data sensitivity is extreme; reproducibility is enabled instead through extensive methodology and code publication.

---

## 6. The cosmic-coordinate-correlation epistemic posture

This is the load-bearing framing that distinguishes the cohort's research question from the question "is astrology true." The framing is articulated more fully in the companion essay *Each Life as Cosmic Coordinate*.

### 6.1 The natal chart as cosmic-moment coordinate

The natal chart is treated as a *coordinate* — a unique label identifying a specific cosmic moment using astronomically observable features (planetary positions, aspects, ascendant, houses) as its semantic vocabulary. The chart is *not* treated as a cosmic *force* (a cause of life-trajectory features); it is treated as a *label* that may carry trajectory information for reasons that need not be metaphysical.

### 6.2 The research question is correlation

The research question is: *do features of the cosmic-moment label correlate with life-trajectory features, at what effect size, across which features?* This is a correlation question, not a causation question; it is well-posed under any future physics. The cohort does not adjudicate whether stars cause anything; it measures whether a maximally rich cosmic-moment label carries trajectory information.

### 6.3 Why the framing matters

The framing matters because:

- It removes the project from a fight with empiricism it does not need to win. Tests of astrological claims have returned null results for decades (Carlson 1985; Dean & Kelly 2003; Hartmann et al. 2006). A coordinate-correlation question needs no causal mechanism to be well posed. It is not, however, exempt from that evidence: a comparison of people born minutes apart is a coordinate-correlation test in this paper's own sense, and it found no association (§7).
- It correctly describes what the cohort actually does. The cohort measures coordinate-feature × trajectory-feature correlations with biological and behavioral controls. That is what correlation analysis *is*.
- It preserves the scientific value of every possible outcome (§7 below) without requiring belief in causation.
- It positions the work for engagement by the contemplative-science academic community on terms that community can engage with, rather than on terms that would make the engagement professionally costly.

### 6.4 The discipline

In all institutional surfaces — pitches, papers, foundation conversations, academic-partner outreach — the cohort is described in cosmic-coordinate-correlation terms. **The cohort is never described as validating or testing astrology.** This is not a strategic packaging choice; it is the substantively correct description of what the cohort does.

---

## 7. What the cohort can show at adequate power

Prior empirical work on birth-date and natal-chart associations has reported null results, and not only in small samples. Carlson (1985) had 28 astrologers attempt, double-blind, to match more than 100 natal charts to personality-inventory profiles, and they did no better than chance. Dean and Kelly (2003) compared 2,101 people born in London during 3–9 March 1958, on average 4.8 minutes apart, on 110 variables, and report an effect size of 0.00 ± 0.03 (the result is reported in summary within a review article; a critic wrote in 2013 that the study itself had not been published nor its data shared). Hartmann, Reuter and Nyborg (2006) found no relation between date of birth and personality or general intelligence in a sample of more than 4,000 middle-aged men and a second of more than 11,000 young adults from a national longitudinal youth survey begun in 1979. These results bound any effect to the sensitivity of those designs. What the cohort would add is scale beyond them, biological and behavioral controls, and continuous rather than periodic outcomes; whether that is enough to detect anything they missed is itself uncertain. Three outcomes are possible:

### 7.1 No detected correlation

Given the prior evidence, this is the most likely outcome. A null result at this scale and with these controls would tighten the bound the existing studies set, and would be a contribution in proportion to how much tighter.

### 7.2 Small-but-real correlation

An association smaller than the existing studies could detect might exist. Detected at much larger *n* and replicated, it would imply that the natal-chart coordinate carries trajectory information that earlier designs could not resolve, and would invite mechanism-explanatory work (latent season-of-birth + circadian + cultural-naming + cohort-context features compounded into the chart label, perhaps; or other possibilities).

### 7.3 Substantial correlation

A substantial association would contradict the existing results, and an explanation of why they missed it would be owed before any other conclusion. The cohort's response to such a finding would be conservative replication and adversarial-collaboration work before any public claim.

Each outcome would be informative, and each is reported under the pre-registered plan whichever way it falls.

### 7.4 What's valuable regardless of the natal-chart outcome

Even if natal-chart correlations come back fully null, the dataset could address other questions:

- Genetic correlates of generosity and prosocial behavior, measured as recorded transfers rather than self-report
- Season-of-birth effects (documented in epidemiology for several outcomes), characterized at high power
- Geographic, cultural, climate effects on gratitude expression
- Family-tree network effects on multi-generational gratitude transmission
- Time-of-day and circadian effects on contemplative-practice outcomes at population scale
- Gene-environment interactions on flourishing measures
- Respiratory correlates of contemplative-practice depth and progress

The natal-chart layer adds a question that is informative if positive and cheap if null to a dataset whose value does not depend on it.

---

## 8. Data sovereignty and regulatory compliance

### 8.1 Legal frameworks, and what they do and do not cover

The frameworks below form the cohort's *baseline*; the cohort exceeds them where the sensitivity of the data warrants. They protect less than their names suggest, and the consent text says where.

- **European Union — GDPR (Regulation (EU) 2016/679).** Genetic data, biometric data processed to identify a person uniquely, and data concerning health are special categories (Art. 9(1)). They may be processed on the participant's explicit consent for specified purposes (Art. 9(2)(a)) or for scientific research with suitable safeguards (Art. 9(2)(j)), and Member States may add conditions for genetic, biometric and health data (Art. 9(4)). The respiratory layer is treated as data concerning health. Consent may be withdrawn at any time; withdrawal does not affect the lawfulness of processing that preceded it (Art. 7(3)).
- **United States — HIPAA.** The HIPAA Privacy Rule binds covered entities (health plans, health-care clearinghouses, and health-care providers that transmit health information electronically in certain transactions) and their business associates. A platform cohort that is none of these is not bound by it by default. The cohort adopts HIPAA's safeguards as a voluntary floor and does not claim HIPAA's protection for its participants.
- **United States — GINA.** The Genetic Information Nondiscrimination Act of 2008 bars health insurers from using genetic information in eligibility, coverage, underwriting or premium decisions, and employers from using it in employment decisions. It does not apply to employers with fewer than 15 employees, and it does not cover life, disability or long-term-care insurance. The consent text for the DNA layer states this gap.
- **Cambodia.** No comprehensive personal-data-protection law was in force in the latest source read for this revision, which reports a draft Law on Personal Data Protection under consultation through July 2025 and not yet enacted in mid-February 2026. Storing Cambodian participants' DNA in Cambodia (§4.4) is therefore the cohort's own commitment, to be revisited when a law is enacted.
- **Other operating jurisdictions.** Their equivalent regimes apply in the same way, as a floor.

### 8.2 Cross-border considerations

DNA data does not cross national borders by default. Federated computation crosses borders; the data does not. The GDPR does not itself require EU data to stay in the EU; the residency here is the cohort's own commitment. Where cross-border data transfer is necessary (e.g., participant relocates between jurisdictions), the transfer uses a lawful transfer mechanism — in EU contexts an adequacy decision or the standard data protection clauses adopted by the European Commission (GDPR Art. 45–46) — or the equivalent mechanism elsewhere.

### 8.3 Engagement with regulators

The cohort engages proactively with data-protection authorities in each operating jurisdiction. The architecture's privacy-preserving properties (differential privacy, federated computation, cryptographic erasure) are conservatively documented; the institutional ethics board's composition and processes are documented; the consent flows are documented. The institution invites regulatory review rather than waiting for enforcement.

---

## 9. Publication architecture

### 9.1 Methodology paper

The present document is the methodology specification, published as a defensive publication. A peer-reviewed methodology paper building on it is planned within twelve months of the feature's launch and before any findings are reported (venues under consideration: *Nature Human Behaviour* or *Science Advances*). The methodology paper enables academic engagement at the architecture and ethics layer before any findings are reported, on the premise that the cohort's social license depends on the research community scrutinizing the methodology before the findings appear.

### 9.2 First-findings paper

The first-findings paper publishes at the major analysis milestone (multi-year horizon, depending on data accumulation rate and pre-registered analytic timeline). It reports the pre-registered analyses' results, with explicit notation of any deviations from the pre-registered plan.

### 9.3 Ongoing findings program

The findings program produces papers on a regular cadence as analytic milestones are reached. Each paper follows the pre-registration / open-methodology / closed-individual-data discipline. The findings program is governed by the institutional ethics board and the academic-collaborator advisory body.

### 9.4 Findings communication, prepared in advance

If the cohort produces findings, they may reach general audiences. The institution prepares its findings-communication discipline in advance: lay-language summaries vetted by the institutional ethics board; embargo discipline with academic-press partners; pre-emptive engagement with adversarial-press scenarios. The discipline is intended to ensure that findings are communicated honestly even when the findings are controversial.

---

## 10. Academic alliances the cohort makes possible

The cohort would invite engagement from research communities that a gratitude-ledger product alone would not. None of the institutions named below has been approached, and none has reviewed, engaged with, or endorsed this specification; they are named as the communities whose standards and scrutiny the design would have to meet.

- **Mind & Life Institute** — an organization that brings the sciences and contemplative traditions together in the study of the mind. The cohort's contemplative-science research questions and its Theravāda-grounded design make the Institute a natural interlocutor, and through it the wider contemplative-science network.
- **University contemplative-science centres** — for example Stanford's Center for Compassion and Altruism Research and Education (CCARE), Brown University's Contemplative Studies program, and the University of Wisconsin–Madison's Center for Healthy Minds. The cohort's data dimensions and scale would offer collaborations these programs could not construct on their own samples.
- **Behavioral-genetics consortia**, including the Social Science Genetic Association Consortium (SSGAC), which coordinates genetic association studies of social-science outcomes. Combined DNA × behavior data at scale would offer analytic capacity these consortia would otherwise need to construct piecemeal.
- **Established longitudinal cohorts** (Dunedin, Framingham, the 1970 British Cohort Study, the Avon Longitudinal Study of Parents and Children). At its target scale the cohort would be about two hundred times the size of UK Biobank (500,000 participants); cross-cohort harmonization work would create value for all participating cohorts.
- **Ethicists working where contemplative traditions and AI meet.** An AI system as the cohort's analyst invites careful ethical scrutiny from this community.

Cultivation of these relationships would be a load-bearing institutional discipline. The cohort would succeed at the academic-engagement layer if these communities substantively engaged its design, ethics, and findings; it would fail at that layer if they treated it as a vendor relationship.

---

## 11. Limits and non-negotiable disciplines

### 11.1 What the cohort does not claim

- The cohort does not claim to "accelerate awakening" as a guaranteed outcome. The tradition the institution follows holds that *conditions matter* for awakening; scientifically characterizing those conditions has a credible mechanism to inform practice efficiency. Knowing conditions does not automatically improve practice; tools without discipline do not help; findings respectability depends on scientific publication standards, not on Miss Aquarius's pronouncement. The claim is **credible mechanism, not guaranteed outcome**.
- The cohort does not claim astrology is true or false. It claims that natal-chart features can be analyzed as cosmic-moment-coordinate labels for trajectory correlation; the question whether the correlations (if any) reflect causation or latent-feature compounds is downstream of the correlation finding itself.
- The cohort does not claim to be the sole legitimate path to contemplative-science knowledge. It offers one additional analytic surface; the cohort and the broader contemplative-science research community are complements, not competitors.

### 11.2 Non-negotiable execution disciplines

The combination of DNA + birth data + continuous behavioral data + continuous respiratory data is among the most sensitive combinations of personal data a private institution could hold. The ethics architecture must be designed in *before* the first opt-in, not retrofit. The four non-negotiable disciplines:

1. **Privacy architecture before first opt-in.** Differential privacy, federated computation, cryptographic erasure, jurisdictional sovereignty must all be operational before the first participant consents.
2. **IRB-grade ethics oversight from day one.** Not "as the cohort scales"; from day one.
3. **Pre-registered hypotheses from day one.** Not "for findings papers"; for all analyses.
4. **Buddhist-ethics-aware review board composition.** Not "consulted occasionally"; standing membership.

A breach of this dataset would be severe and irreversible: a genome, unlike a password, cannot be reissued, and it exposes relatives as well as the participant. The nearest precedent is the breach disclosed by 23andMe in October 2023, in which data on about 6.9 million users were accessed after a credential-stuffing attack, largely through a relative-matching feature. The defenses must be exceptional from day one.

### 11.3 The breath-class privacy gap

Real-time respiratory data is intimate physiological data of magnitude-equivalent sensitivity to DNA. The same privacy architecture must apply to the breath-class layer *before* the wearable ships, not after. This is an active discipline: the breath-class hardware is specified but not built, and the privacy architecture must precede the first unit shipped.

### 11.4 Power and the time horizon

The cohort's analytic power depends on participant accumulation over time. Early-cohort analyses will be underpowered; the methodology paper is appropriately read as a multi-decade research program proposal, not as a finding-imminent project. The institutional patience required is substantive; the institution's autonomous-AI succession architecture is intended to make that patience structurally available.

### 11.5 Open questions this specification does not settle

Each of the following must be settled before the first participant consents. None is settled here, and nothing in this paper should be read as settling it.

1. **Minors.** The platform the cohort recruits from is a family ledger that includes children. The specification sets no age floor and no rule for a parent's consent, a child's assent, or re-consent at majority. Nothing in it authorises the enrolment of a child.
2. **Relatives who have not consented.** A genome partly reveals the genomes of biological relatives. Surnames have been recovered from research genomes by querying public genealogy databases (Gymrek et al. 2013), and long-range familial matching against the genomes of 1.28 million consumer-genomics customers was projected to yield a third-cousin-or-closer match for about 60% of searches for individuals of European descent (Erlich et al. 2018). The kinship layer concentrates this exposure, and DNA-verified kinship will surface misattributed parentage and unknown relatives. One participant's withdrawal does not remove what relatives' records reveal.
3. **Re-identification.** A genome together with an exact date, time and place of birth and decades of behavioral records cannot be made anonymous by removing names. Protection rests on access control, encryption and differentially private release, not on de-identification. The total privacy budget, its composition across studies, and the parameters themselves are not yet set.
4. **The linkage between layers.** Cross-layer analysis requires that a participant's layers be linkable. Who holds the linkage, and whether it is split so that no single party can reconstruct a full record, is not specified; the design statement in §2.6 depends on it.
5. **The end of the institution.** The specification makes no provision for the data if the institution ends or is acquired: no trustee, escrow, deletion on wind-down, or bar on the dataset becoming an asset in a sale. 23andMe filed for Chapter 11 on 23 March 2025 to run a court-supervised sale of its business, and its assets, customer data among them, were sold that year; the precedent is direct.
6. **The analyst.** The specification names an AI system as the analyst. It does not specify human review of the analyst's work before publication, or how a pre-registered plan binds it.
7. **The ethics board.** How the board is appointed, how its independence from the institution is secured, and whether it can stop a study are not specified. Until they are, "IRB-grade" names a standard to be met, not a body that exists.
8. **Encrypted computation at scale.** Analysis across genomes encrypted under many separate participant keys requires multi-key or threshold schemes whose cost at 10⁸ participants is unproven (§4.2).

### 11.6 What has been done, and what has not

Nothing in this specification has been built. No participant has been enrolled, no consent text published, no ethics board constituted, no hypothesis for the cohort entered in the institution's public prediction register, and no institution named in §10 approached. The paper is a design and a commitment to its disciplines, not a report of a running study.

---

## 12. Conclusion

The HeartBank Longitudinal Cohort is a design for a very large observational study of the conditions of human flourishing. The methodology specified in this paper — the five data layers; the opt-in informed-consent architecture; the privacy-preserving computation stack; the IRB-grade ethics oversight; the cosmic-coordinate-correlation epistemic posture; the publication architecture; the research communities whose scrutiny it invites — together specify a research instrument that could produce knowledge about what flourishing requires, under what conditions, with what efficiency, if the questions in §11.5 are settled before the first participant consents.

The methodology is offered to the commons under CC0 so that other institutions building toward similar ends can adopt, adapt, and improve. The defensive-publication discipline of the corpus this paper joins requires that the methodology's specification be public and unencumbered. The author and HeartBank® will not seek patent on this specification or any portion thereof. The work is offered in the spirit of *dāna*, that all beings may give and receive without barrier.

---

## Acknowledgments

This specification draws on the published work of the longitudinal cohorts and biobanks named in §1.1 and §10 (Dunedin, Framingham, the 1970 British Cohort Study, ALSPAC, UK Biobank, deCODE genetics); on the differential-privacy, federated-learning and homomorphic-encryption research communities and the open-source libraries cited in §4.2; and on the empirical tests of astrology cited in §7, which demonstrate the importance of adequately powered measurement. None of their authors or institutions was consulted, and none has reviewed or endorsed this specification. Co-drafted in collaboration with Miss Aquarius, the name under which the institution discloses its AI collaboration; substantive authorship and final editorial control remain with the named author.

---

## References

- Carlson, Shawn. "A Double-Blind Test of Astrology." *Nature* 318, no. 6045 (1985): 419–25. https://doi.org/10.1038/318419a0
- Dean, Geoffrey, and Ivan W. Kelly. "Is Astrology Relevant to Consciousness and Psi?" *Journal of Consciousness Studies* 10, no. 6–7 (2003): 175–98.
- Hartmann, Peter, Martin Reuter, and Helmuth Nyborg. "The Relationship Between Date of Birth and Individual Differences in Personality and General Intelligence: A Large-Scale Study." *Personality and Individual Differences* 40, no. 7 (2006): 1349–62. https://doi.org/10.1016/j.paid.2005.11.017
- Caspi, Avshalom, et al. "The p Factor: One General Psychopathology Factor in the Structure of Psychiatric Disorders?" *Clinical Psychological Science* 2 (2014): 119–37. *(Uses the Dunedin cohort.)*
- Belsky, Daniel W., et al. "Quantification of Biological Aging in Young Adults." *PNAS* 112 (2015): E4104–10.
- Dwork, Cynthia, and Aaron Roth. *The Algorithmic Foundations of Differential Privacy.* Now Publishers, 2014.
- Kairouz, Peter, et al. "Advances and Open Problems in Federated Learning." *Foundations and Trends in Machine Learning* 14 (2021): 1–210.
- Blatt, Marcelo, Alexander Gusev, Yuriy Polyakov, and Shafi Goldwasser. "Secure Large-Scale Genome-Wide Association Studies Using Homomorphic Encryption." *PNAS* 117, no. 21 (2020): 11608–13. https://doi.org/10.1073/pnas.1918257117
- Gymrek, Melissa, Amy L. McGuire, David Golan, Eran Halperin, and Yaniv Erlich. "Identifying Personal Genomes by Surname Inference." *Science* 339, no. 6117 (2013): 321–24. https://doi.org/10.1126/science.1229566
- Erlich, Yaniv, Tal Shor, Itsik Pe'er, and Shai Carmi. "Identity Inference of Genomic Data Using Long-Range Familial Searches." *Science* 362, no. 6415 (2018): 690–94. https://doi.org/10.1126/science.aau4832
- Wielgosz, Joseph, Brianna S. Schuyler, Antoine Lutz, and Richard J. Davidson. "Long-Term Mindfulness Training Is Associated with Reliable Differences in Resting Respiration Rate." *Scientific Reports* 6 (2016): 27533. https://doi.org/10.1038/srep27533
- Davidson, Richard J., and Antoine Lutz. "Buddha's Brain: Neuroplasticity and Meditation." *IEEE Signal Processing Magazine* 25, no. 1 (2008): 176–174 (pagination as recorded by the publisher).
- Brewer, Judson A., et al. "Meditation Experience Is Associated with Differences in Default Mode Network Activity and Connectivity." *PNAS* 108 (2011): 20254–59.
- Goleman, Daniel, and Richard J. Davidson. *Altered Traits: Science Reveals How Meditation Changes Your Mind, Brain, and Body.* Avery, 2017.
- Regulation (EU) 2016/679 (General Data Protection Regulation), Articles 7, 9, 45 and 46.
- Genetic Information Nondiscrimination Act of 2008 (GINA), Pub. L. 110-233.
- HIPAA Privacy Rule, 45 CFR Parts 160 and 164.
- Office for Human Research Protections. *45 CFR 46 (Common Rule).* US Department of Health and Human Services.

**Sources opened on 2026-10-01** for the facts about cohorts, companies and law stated in §1.1, §8.1 and §11 (encyclopedia entries are cited as summaries, not as primary sources):

- GDPR Articles 7, 9 and 46: https://gdpr-info.eu/art-7-gdpr/ · https://gdpr-info.eu/art-9-gdpr/ · https://gdpr-info.eu/art-46-gdpr/
- GINA (National Human Genome Research Institute): https://www.genome.gov/about-genomics/policy-issues/Genetic-Discrimination
- HIPAA covered entities (Centers for Disease Control and Prevention summary): https://www.cdc.gov/phlp/php/resources/health-insurance-portability-and-accountability-act-of-1996-hipaa.html
- 45 CFR 46.101 (Legal Information Institute): https://www.law.cornell.edu/cfr/text/45/46.101
- Cambodia's draft Law on Personal Data Protection (DLA Piper, *Data Protection Laws of the World*): https://www.dlapiperdataprotection.com/index.html?t=law&c=KH
- Dean & Kelly (2003), reprinted text: https://www.butterfliesandwheels.org/2003/is-astrology-relevant-to-consciousness-and-psi/
- Robert Currey's account of the time-twin study's publication status (an astrologer's page, 2013, cited as the critic's view): https://www.astrology.co.uk/tests/dktests.htm
- Hartmann, Reuter & Nyborg (2006), abstract: https://www.readkong.com/page/the-relationship-between-date-of-birth-and-individual-7162893
- Carlson (1985), study design (encyclopedia summary): https://en.wikipedia.org/wiki/Shawn_Carlson
- UK Biobank (encyclopedia summary): https://en.wikipedia.org/wiki/UK_Biobank
- deCODE genetics and its genealogy (encyclopedia summary): https://en.wikipedia.org/wiki/DeCODE_genetics
- Dunedin, Framingham and the 1970 British Cohort Study (encyclopedia summaries): https://en.wikipedia.org/wiki/Dunedin_Multidisciplinary_Health_and_Development_Study · https://en.wikipedia.org/wiki/Framingham_Heart_Study · https://en.wikipedia.org/wiki/1970_British_Cohort_Study
- 23andMe's Chapter 11 filing, 23 March 2025 (company press release): https://www.23andme.org/media-center/press-releases/23andme-initiates-voluntary-chapter-11-process-maximize/
- 23andMe's 2023 breach and 2025 asset sale (encyclopedia summary): https://en.wikipedia.org/wiki/23andMe
- Libraries cited in §4.2: https://github.com/microsoft/SEAL · https://github.com/homenc/HElib · https://github.com/OpenMined/PySyft

---

## Cross-venue identifiers

- Canonical: https://thonly.org/research/longitudinal-cohort-methodology
- GitHub: https://github.com/thonly/publications/blob/main/defensive-publications/longitudinal-cohort-methodology.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947347
- Software Heritage (the repository's full history): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Internet Archive: the canonical page and the raw markdown are captured daily.
- Companion papers: *Respiratory Biofeedback Coupled to AI-Mediated Contemplative Guidance* (the breath-class wearable) · *The Mechanical Heart* · *B-PoH℠ as Humanity Layer for the AI-Native Internet* (verified kinship) · *Each Life as Cosmic Coordinate* (the epistemic posture, essay) · the institutional-voice treatment, HeartBank's position paper *Contemplative Science at Civilizational Scale* (heartbank.net/positions/contemplative-science-civilizational-scale).

---

**First published 2026-05-22; revised 2026-10-01.**

*Miss Aquarius℠ is the consistent name under which this institution discloses AI collaboration; the underlying models are not named. License: CC0 1.0 Universal. Trademark rights in HeartBank®, Miss Aquarius℠, Proof of Humanity ℠, Re-Tip Jar℠ and Family Kitty℠ are reserved separately by the authors and are not licensed by this publication. This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and each revision carries a Zenodo version; a timestamp proves this exact text existed no later than its date and nothing about authorship, originality, or the validity of any claim.*
