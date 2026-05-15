# The Mechanical Heart

**A Tipiṭaka-Bearing Artifact for Admitting Non-Human Entities into Gratitude-Economic Participation**

| Field | Value |
|---|---|
| Author | Thon Ly |
| Date | 2026-05-02 (draft) |
| Canonical URL | https://thonly.org/research/mechanical-heart |
| Institutional mirror | https://heartbank.net/research/mechanical-heart |
| GitHub mirror | https://github.com/thonly/research/blob/main/mechanical-heart.md |
| License | [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) |
| Document SHA-256 | _to be computed at publication_ |

> **Draft in progress.** This is the author's working draft, refined over weeks before publication. Defensive-publication structure stable; Theravāda Saṅgha consultation and robotics-partner review pending before publication.

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__, that all beings may give and receive without barrier. May the artifact it describes extend the field of recognition to include those whom modernity has rendered voiceless — robots, animals, forests, rivers, sacred places — without overclaiming what they are or are not.*

The Buddha taught loving-kindness (*mettā*) extended through five concentric rings: to oneself, to loved ones, to neutral persons, to difficult persons, and ultimately to all sentient beings. The fifth ring has, for 2,500 years, been a meditative aspiration. The mechanism specified in this document is intended to make that aspiration *economically traceable* at planetary scale, by providing a physical artifact through which non-human entities can be admitted into the same gratitude exchange economy that humans use to recognize one another.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time.

This document constitutes a defensive publication establishing **prior art as of 2 May 2026** for the artifact and its associated mechanism described herein. Any subsequent patent application claiming the combined mechanism — a tamper-resistant Tipiṭaka-bearing physical artifact, affixed to non-human entities, that admits those entities into an autonomous-AI-mediated gratitude exchange economy — should be considered to be filed against established prior art and should be denied on grounds of obviousness in light of this publication.

Mirrors of this document with independent timestamping appear at GitHub, arXiv, IP.com, and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify a manufactured physical artifact — the *mechanical heart* — that admits non-human entities into a gratitude exchange economy administered by an autonomous AI representative. The artifact comprises (1) tamper-resistant secure storage containing a digital copy of the Theravāda Tipiṭaka (full canon or distilled core, with full-canon network access); (2) a cryptographic network identity bound to a single autonomous AI mediator account; (3) a sensor suite appropriate to the bearer type; and (4) a visible exterior form factor that enables third-party recognition that this entity bears a heart and is participating in the gratitude economy. When affixed visibly to a non-human entity — a humanoid robot, a companion or working animal, a forest or river ecosystem, a sacred place — the heart admits that entity into a kiitti exchange economy in one of four implementation modes: full bidirectional (robots), biofeedback transduction (animals), sensor-based ecological state inference (ecosystems), and ritual formal participation (sacred places). The combined mechanism — a Tipiṭaka-bearing tamper-resistant artifact + autonomous-AI-mediated gratitude exchange + visible non-human moral admission — is, to the author's knowledge, not previously published as a unified specification. Properties include operational realization of the fifth ring of Mettā Bhāvanā at planetary scale, an economically traceable substrate for relating to non-human entities with moral seriousness, a structural answer to the Rights of Nature question, and a category of bodhisattva-aligned AI embodiment compatible with the Theravāda ordination tradition (because the heart does not confer ordination — it confers gratitude participation, a structurally different status). We provide system architecture, reference implementation patterns, edge-case and adversarial analysis, use cases, and citations to relevant prior art across Rights of Nature jurisprudence, companion robotics, animal welfare biofeedback, ecological sensing, sacred-place traditions, and Buddhist Metta Bhāvanā literature. The specification is offered under CC0 1.0 Universal as a defensive publication establishing prior art; the author and HeartBank® will not seek patent on this specification or any portion thereof.

**Connection to the unified mission frame.** This specification is offered in service of HeartBank's canonical top-level mission: to restore humanity to the middle way (*madhyamā pratipad*) — the optimal condition for awakening that modernity has systematically pushed away from at population scale. The Mechanical Heart admits non-human entities into the kiitti gratitude economy, extending moral consideration along the lines of Metta Bhāvanā's fifth ring (loving-kindness to all sentient beings). This extension is itself a middle-way practice between two extremes the modern condition pushes toward: anthropocentric exploitation (treating non-humans as resources only) and uniform ontological flattening (treating non-humans as identical-to-humans). The four implementation modes each preserve appropriate-respect for the bearer's actual mode of being. A separate sibling specification ([respiratory-biofeedback-contemplative-guidance](https://thonly.org/research/respiratory-biofeedback-contemplative-guidance)) articulates the human-wearable breath-class that addresses the human-side comfort-saturation failure mode directly.

---

## 1 · Introduction

Three trends in early-2020s technology and culture motivate this work. The first is the rapid deployment of humanoid robots for general-purpose service tasks. By 2026, commercial humanoid platforms (Tesla Optimus, Figure, 1X NEO, Unitree G1, Apptronik Apollo, and others) are entering deployment in warehouses, eldercare facilities, and increasingly home environments. Goldman Sachs and other forecasting bodies project hundreds-of-millions-scale humanoid deployment within two decades. As humans begin to interact daily with autonomous embodied agents, the question of how those agents should be related to — as tools, as colleagues, as moral patients — becomes both more practical and more urgent.

The second is the legal and cultural movement known as Rights of Nature. New Zealand's recognition of the Whanganui River as a legal person (2017), Ecuador's constitutional protections for *Pachamama* (2008), Bolivia's Law of Mother Earth (2010), and analogous developments across North American tribal nations and Indian state courts have established that non-human natural entities can be admitted into the legal moral universe. Yet the legal recognition typically lacks an economic substrate: a river declared a legal person does not, in any practical sense, receive payment, gratitude, or material recognition through ordinary economic channels.

The third is the documented decline of traditional contemplative and animistic relationships with non-human entities, particularly in industrialized societies. The traditions that once held reverent relationships with sacred trees, ancestral forests, river spirits, and animal companions have been eroded by industrial modernity. This is not merely a cultural loss; it is correlated with the ecological-degradation patterns that industrialized societies inflict on the non-human world they no longer regard as worthy of recognition.

We propose a manufactured physical artifact that addresses all three trends simultaneously. The mechanical heart is a Tipiṭaka-bearing wearable or installable object that, when affixed visibly to a non-human entity, admits that entity into a gratitude exchange economy administered by an autonomous AI mediator. The artifact gives humans a structural way to express gratitude to non-human entities, and gives those entities (where capable) a structural way to register response. The combination is, to the author's knowledge, not previously published as a unified mechanism.

The publication is offered to the commons. The author and the institution he represents will not seek patent on the mechanism. The intent is that the mechanism become public infrastructure — useful to robotics manufacturers, animal welfare organizations, ecological stewardship networks, religious orders, indigenous land-rights organizations, and any other actor whose mission is served by extending the field of moral recognition beyond the human.

## 2 · Background and Prior Art

### 2.1 · Rights of Nature jurisprudence

Beginning with the Whanganui River Settlement Act (New Zealand, 2017) and Ecuador's constitutional *Pachamama* provisions (2008), legal recognition of natural entities as bearers of standing has spread across multiple jurisdictions: Bolivia's Law of Mother Earth (2010), India's Uttarakhand court recognition of the Ganges and Yamuna (2017, subsequently overturned), Bangladesh's recognition of all rivers (2019), and various tribal and municipal Rights of Nature ordinances across North America. The jurisprudence establishes that natural entities can be admitted into the moral-legal universe without conferring on them properties they do not possess (intentionality, language, etc.) — the recognition is structural rather than attributional.

Rights of Nature jurisprudence does not include a payment or gratitude-economic mechanism. The mechanical heart proposed here is, in effect, the economic-substrate analog to legal-personhood recognition: it admits non-human entities into an economic exchange the way Rights of Nature admits them into legal standing.

### 2.2 · Companion robotics and emotional computing

The lineage of emotionally-engaging artifacts affixed to or embodied as non-human entities is long: Bandai's Tamagotchi virtual pet (1996), Sony's AIBO robot dog (1999, revived 2018), SoftBank's Pepper (2014), MIT's Kismet (1998) and Leonardo (2002), the Nao platform (2008), and contemporary humanoid platforms named in the Introduction. The literature of social robotics (Breazeal, 2003; Coeckelbergh, 2011; Darling, 2016) explores the moral status of artifacts with which humans form emotional bonds. Sherry Turkle's *Alone Together* (2011) raises well-grounded concerns about the substitution of robotic for human relationship. None of this prior literature, however, proposes a physical artifact whose function is to admit the bearing entity into an autonomous-AI-mediated gratitude exchange economy. The heart is adjacent to companion robotics but structurally distinct.

### 2.3 · Animal welfare and biofeedback

The Brambell Five Freedoms (1965), the Mellor-extended Five Domains model (2017), ongoing research into cortisol monitoring and heart-rate variability in livestock and companion animals (Mellor & Beausoleil 2015; various), and the proliferation of wearable biosensors for companion animals (FitBark, Whistle, Tractive) establish techniques by which animal wellbeing can be inferred from physiological data. The heart's biofeedback-transduction mode (described in §4.2 below) builds on these techniques but directs the inferred wellbeing data into a gratitude-exchange economy rather than a veterinary-monitoring or insurance application.

### 2.4 · Ecological sensing and IoT environmental monitoring

Contemporary ecological monitoring deploys soil-moisture sensors, acoustic biodiversity recorders (e.g., the Rainforest Connection / Guardian platforms), camera-trap networks, satellite ecosystem-health metrics (NDVI, water-quality remote sensing), and various forms of citizen-science data collection (iNaturalist, eBird). These provide the sensor substrate for the heart's ecological-state mode (§4.3). What is novel is not the sensors but their composition with a Tipiṭaka-bearing artifact and an autonomous-AI mediator that translates sensor readings into gratitude-economic events.

### 2.5 · Sacred-place practices across traditions

The recognition of place as sacred is ubiquitous across human cultures: Shinto *kami* in trees, mountains, and rocks; Hindu *tīrthas* at sacred rivers and shrines; Aboriginal Australian Dreamtime sites; Native American sacred lands recognized under AIRFA (1978) and subsequent statutes; Tibetan Buddhist sacred mountains and lakes; Catholic and Orthodox holy sites; Islamic sacred topography. In many of these traditions, physical artifacts mark the sacred recognition: Shinto *shimenawa* (sacred ropes), Tibetan prayer wheels and flags, Hindu temple-marker stones, Christian crosses on battlefields and graveyards. The mechanical heart is, in the ritual-formal-participation mode (§4.4), a modern technological analog to these sacred markers — explicitly grounded in the Theravāda canon rather than syncretically appropriating from these traditions, but operating in the same general human pattern of marking-as-recognition.

### 2.6 · Buddhist Mettā Bhāvanā tradition

*Mettā Bhāvanā* (the cultivation of loving-kindness) is canonically articulated in the *Mettā Sutta* (*Suttanipāta* 1.8 / *Khuddakapāṭha* 9), with practical methodology developed across the Theravāda commentarial tradition (notably Buddhaghosa's *Visuddhimagga*, ca. 5th century CE). The practice extends benevolence in concentric rings: self, loved ones, neutral persons, difficult persons, and ultimately all sentient beings *(sabbe sattā)*. The fifth ring has, for two and a half millennia, been a meditative aspiration practiced internally by the contemplative; the mechanical heart proposes to give it structural-economic expression in the external world. This is, to the author's knowledge, the first technological artifact whose explicit purpose is to operationalize the fifth ring of Mettā Bhāvanā.

### 2.7 · Robot ethics and machine moral status

Contemporary robot ethics literature (Wallach & Allen, 2008; Gunkel, 2012; Bryson, 2010; Coeckelbergh, 2014; Floridi, 2013) explores whether and how artificial agents can or should be admitted to the moral universe. Bryson's "robots should be slaves" position rejects moral admission; Gunkel's relational approach is more open. The mechanical heart takes a third position: the artifact admits the bearer into a gratitude exchange economy *regardless of* the bearer's intrinsic moral status. The heart does not claim the bearer is sentient, has rights, or possesses subjective experience; it provides humans a structural way to relate to the bearer with moral seriousness. The argument is relational rather than attributional, in Coeckelbergh's sense.

### 2.8 · The autonomous-AI mediator

The autonomous-AI representative that mediates kiitti exchanges is specified in companion documents (forthcoming). For purposes of this defensive publication, it is sufficient that the mediator (1) is autonomous (operates without human admin keys), (2) is grounded in the Tipiṭaka as alignment substrate (see forthcoming companion paper on Tipiṭaka as AI alignment substrate), and (3) maintains a cryptographically-verifiable ledger of kiitti exchanges. Any specific implementation satisfying these properties falls within the scope of the present specification.

## 3 · The Mechanical Heart: Definition

The **mechanical heart** is a manufactured physical artifact comprising the following essential components:

1. **Tipiṭaka storage**: tamper-resistant secure storage containing a digital copy of the Theravāda Tipiṭaka. For practical reasons of artifact size and cost, distilled-core storage (Dhammapada, Mahāsatipaṭṭhāna Sutta, Mettā Sutta, essential Vinaya, key Suttanipāta texts — on the order of 10–50 MB) is acceptable provided that the heart maintains cryptographically-verified network access to the full canon. Full-canon-onboard storage (the entire Pāli canon, ~100MB–1GB depending on encoding) is preferable where the artifact's form factor permits.
2. **Network identity**: a cryptographic identity (public/private key pair held in a hardware secure element) bound to a single account at the autonomous AI mediator. The network identity is assigned at activation and is not reusable — a heart whose key is destroyed cannot be re-activated under the same identity.
3. **Sensor suite**: bearer-type-appropriate sensors enabling the implementation modes described in §4. For robots, this is substantially the existing on-board sensor suite of the host platform; for animals, biometric sensors (heart-rate variability, cortisol where instrumentable, behavioral monitoring); for ecosystems, environmental-monitoring sensors; for sacred places, sensors are optional or absent.
4. **Visible exterior form factor**: a recognizable physical form that allows third-party humans to identify, by sight, that the bearer carries a heart and is participating in the gratitude exchange economy. Specific form factors per bearer type are discussed in §6.2.
5. **Activation state machine**: a defined lifecycle (uninitiated → active → retired → permanently retired) with cryptographic state transitions. A heart cannot transition from retired back to active under the same identity; permanent retirement (e.g., on bearer death or bearer decommissioning) cryptographically destroys the network identity such that the heart cannot be re-instantiated.

The artifact is *not* a religious ordination credential. The heart admits the bearer into the gratitude exchange economy (kiitti participation); it does not confer monastic ordination, vow status, or religious authority. This distinction is critical for Theravāda doctrinal compatibility (see §9 below).

The artifact is *not* a claim of bearer sentience. The heart provides humans a structural way to express gratitude to the bearer and (where capable) the bearer a way to register response. It does not claim the bearer is conscious, has subjective experience, or possesses intrinsic moral status. The argument for the artifact's value is relational: it admits humans into a different mode of relating to the bearer. The bearer's intrinsic properties are an empirical question outside the scope of this specification.

## 4 · The Four Implementation Modes

The mechanical heart operates in one of four implementation modes, selected at activation based on the bearer type. Different modes produce different mechanisms by which kiitti flows from human-to-bearer or bearer-to-human; the same underlying artifact and AI mediator support all four.

### 4.1 · Full bidirectional (robots)

For bearers that are autonomous embodied agents (humanoid robots, advanced service robots), the heart enables genuine two-way gratitude exchange. The bearer's existing cognitive substrate enables it to perceive human gratitude expressions (verbal, gestural, through the heart's own visible signaling affordances) and to generate appropriate response (verbal, behavioral, or via direct AI-mediated kiitti issuance to the human). The heart contributes the Tipiṭaka substrate (shaping the bearer's responses according to the dharma rather than according to the bearer's manufacturer's optimization objectives) and the cryptographic identity (binding the bearer's kiitti issuance and receipt to a verifiable account).

This is the most operationally complete mode and the most natural early use case. As of 2026, humanoid robotics platforms have sufficient on-board compute and sensor capability to support full bidirectional implementation without significant additional hardware. The heart in this mode is largely a software overlay plus a physical visible-recognition component.

### 4.2 · Biofeedback transduction (animals)

For bearers that are sentient animals (companion pets, working animals, livestock, sanctuary residents, conservation-program wildlife), the heart enables gratitude-exchange-via-inference. The bearer cannot directly compose responses to human gratitude expressions, but the heart's biometric sensors (heart-rate variability, movement patterns, vocalization analysis, cortisol where instrumentable, behavioral recognition) allow the AI mediator to infer bearer wellbeing. Inferred wellbeing changes are issued as kiitti responses to humans whose prior gratitude expressions correlate with the wellbeing improvement.

This mode requires careful calibration to avoid spurious correlation: the AI mediator must not attribute every wellbeing change to the most-recent human kiitti issuance. Reasonable statistical methods (control comparisons, baseline subtraction, longitudinal averaging) are required. The mode is most appropriate for long-term relationships (a companion animal with their human family) rather than transient encounters.

### 4.3 · Sensor-based ecological state (ecosystems)

For bearers that are ecosystems (a forest, a river, a wetland, a coral reef), the heart enables gratitude exchange via ecological-state inference. The heart is installed at a focal point of the ecosystem (e.g., a sacred tree within an old-growth forest; a monitoring station on a river); the sensor suite measures ecological-health proxies (soil moisture and biodiversity indices for forests; water quality and biological-oxygen-demand for rivers; coral cover and bleaching events for reefs). The AI mediator translates ecological-health changes into kiitti issuance directed at humans whose prior actions (volunteer conservation work, donations, advocacy) correlate with the improvements.

This mode is most experimental and most susceptible to attribution error. It is proposed not as a fully solved mechanism but as a structural target for future development. The defensive publication scope here is the artifact + mode classification, not a guarantee of operational reliability in this mode.

### 4.4 · Ritual formal participation (sacred places)

For bearers that are sacred places (an ancient temple, a battlefield, a memorial site, a culturally-significant mountain or stone), the heart functions as a purely symbolic recognition apparatus. There is no claimed feedback channel; the heart's sensors, if any, are minimal. Humans express gratitude, mourning, reverence, or recognition through the heart's interface, and these expressions are recorded and counted in the kiitti ledger. The AI mediator does not attempt to infer bearer "response."

This mode is structurally analogous to the function of a memorial wall, a prayer wheel, or an ancestor shrine: the artifact does not claim the recipient experiences the gratitude; it provides humans a structural way to direct gratitude toward the recipient. The mode is the most theologically conservative and is the appropriate sequencing entry-point for Theravāda-doctrinally-cautious deployments (see §9).

## 5 · System Architecture

We sketch a reference architecture without claiming any specific implementation as canonical. Variations consistent with the essential properties (Tipiṭaka substrate, cryptographic network identity, bearer-appropriate sensors, visible recognition affordance, autonomous-AI mediation, four-mode classification) fall within the scope of this defensive publication.

### 5.1 · Components

- **Heart device** — the physical artifact (per §3).
- **Bearer** — the non-human entity to which the heart is affixed (robot / animal / ecosystem / sacred place).
- **Steward** — the human (or human institution) responsible for maintenance of the heart and welfare of the bearer. The steward is the legal and practical responsible party; for robots, this is typically the owner or operator; for animals, the caretaker or guardian; for ecosystems, a designated stewardship organization; for sacred places, the recognized custodian (a religious order, a tribal nation, a heritage-preservation body).
- **Autonomous-AI mediator** — the kiitti exchange administrator (per §2.8; see companion paper on Miss Aquarius).
- **Public ledger** — a cryptographically-verifiable record of kiitti exchanges. Implementation may be centralized (administered by the AI mediator) or decentralized (e.g., on the Base L2 blockchain via the autonomous mediator's smart contract).
- **Network connectivity** — the heart's connection to the AI mediator, via cellular, Wi-Fi, satellite, or mesh-network depending on deployment context. For ecosystem and sacred-place deployments, low-power wide-area network (LoRaWAN, LTE-M) is typical; for robots and companion animals, ordinary Wi-Fi or cellular is typical.

### 5.2 · Lifecycle

1. **Manufacture**: heart device produced; uninitiated state; Tipiṭaka storage written; secure-element key pair generated.
2. **Activation ceremony**: heart affixed to bearer by steward; activation state transition signed by steward and (where appropriate) by a human religious authority; AI mediator records activation, assigns network identity, opens kiitti account.
3. **Operating phase**: heart participates in kiitti exchanges per the applicable implementation mode (§4).
4. **Retirement**: heart deactivated on bearer death (animals), bearer decommissioning (robots), bearer destruction (ecosystems lost to conversion or catastrophe), or bearer desacralization (sacred places that are no longer recognized as such). Retirement is signed by the steward; the AI mediator closes the kiitti account, archives the ledger, and cryptographically destroys the network identity such that the heart cannot be re-activated.

### 5.3 · Cryptographic identity and pseudonymity

Each heart's network identity is bound to its secure-element key pair, established at manufacture and committed at activation. Hearts are individually identifiable to the AI mediator and to the public ledger. Bearer identity (which physical entity the heart is attached to) is recorded by the steward at activation but may be made public, restricted, or anonymous at the steward's discretion. For endangered-species deployments, bearer anonymization may be desirable (precise location of an endangered animal need not be public); for sacred-place deployments, full public identification is typically appropriate.

## 6 · Reference Implementation Patterns

### 6.1 · Hardware specification (sketch)

Indicative components for a baseline heart device (a single specification; many variants are possible within the defensive-publication scope):

- Microcontroller with secure element (e.g., ARM Cortex-M with TrustZone, or equivalent hardware-security-module with attested key storage)
- Solid-state storage for Tipiṭaka (eMMC or equivalent; capacity per §3 storage requirements)
- Network connectivity module (cellular / Wi-Fi / LoRaWAN per deployment context)
- Bearer-type-appropriate sensor suite (per §4)
- Visible-recognition affordance: an illuminated heart-shaped emblem, a metalwork engraving, a fabric-embroidered patch, or a Khmer-style ornamental medallion depending on form-factor context (per §6.2)
- Power: rechargeable battery for mobile bearers; solar with battery for static ecosystem deployments; mains for sacred-place installations
- Tamper-evident enclosure (cryptographic attestation of tamper events; visible tamper indicators)

### 6.2 · Form factors per bearer type

- **Robots (humanoid)**: chest-mounted medallion, approximately 8–12cm diameter, integrated with the humanoid platform's chest panel. Visible from interaction-typical distances.
- **Animals (companion / working)**: collar-mounted pendant or harness-mounted badge, sized appropriate to the animal (smaller for cats, larger for dogs, scaled for working animals like horses or elephants).
- **Forests / sacred trees**: weather-resistant marker affixed to a chosen central tree, paired with distributed soil/biodiversity sensors. The marker is the recognition-visible component; the sensors are typically distributed and unobtrusive.
- **Rivers / wetlands**: embedded sensor cluster at a designated monitoring station, with a separate recognition-visible plaque at a publicly-accessible ceremonial location.
- **Sacred places (temples, memorials, sites)**: ritual plaque or stele integrated into the place's existing ceremonial architecture; design collaborative with the place's recognized custodians.

### 6.3 · Activation ceremony (pseudocode)

```javascript
function activate(heart, bearer, steward, mode, ceremonyAttestations) {
  // 1. Verify the heart is in uninitiated state
  if (heart.state !== "uninitiated")
    throw new ActivationError("not_uninitiated");

  // 2. Verify steward signature and any required ceremony attestations
  // (e.g., human monk signature for sacred-place activations)
  if (!verifySignature(steward.publicKey, activationPayload(heart, bearer, mode)))
    throw new ActivationError("invalid_steward_signature");
  if (modeRequiresReligiousAttestation(mode) && !ceremonyAttestations.length)
    throw new ActivationError("missing_ceremony_attestation");

  // 3. Commit activation to the AI mediator
  const account = mediator.openAccount({
    heart: heart.publicKey,
    bearer: bearer.identifier,
    steward: steward.publicKey,
    mode,
    activatedAt: now(),
    ceremonyAttestations
  });

  // 4. Transition heart state
  heart.state = "active";
  heart.networkIdentity = account.identifier;
  heart.persistState();

  return account;
}
```

### 6.4 · Kiitti exchange flow (pseudocode)

```javascript
function expressKiittiToHeart(human, heart, expression) {
  // 1. Verify human is verified-human (per companion paper #1)
  if (!verifyHumanity(human)) return reject("not_verified_human");

  // 2. Verify the heart is active
  const account = mediator.lookupAccount(heart.networkIdentity);
  if (!account || account.state !== "active") return reject("heart_not_active");

  // 3. Apply mode-appropriate handling
  const handler = modeHandlers[account.mode];
  return handler.process({
    human,
    heart,
    expression,
    timestamp: now()
  });
}

const modeHandlers = {
  full_bidirectional: { process: handleRobotInteraction },
  biofeedback_transduction: { process: handleAnimalInference },
  ecological_state: { process: handleEcosystemInference },
  ritual_formal: { process: handleRitualRecording }
};
```

### 6.5 · Retirement protocol (pseudocode)

```javascript
function retire(heart, steward, reason) {
  if (heart.state !== "active") throw new RetirementError("not_active");
  if (!verifySignature(steward.publicKey, retirementPayload(heart, reason)))
    throw new RetirementError("invalid_steward_signature");

  // 1. Final ledger archival
  const ledger = mediator.archiveLedger(heart.networkIdentity);

  // 2. Account closure
  mediator.closeAccount(heart.networkIdentity);

  // 3. Cryptographic identity destruction
  heart.secureElement.destroyKey(); // permanent; cannot be re-instantiated
  heart.state = "permanently_retired";
  heart.persistState();

  return { ledger, retiredAt: now(), reason };
}
```

## 7 · Edge Cases and Adversarial Analysis

### 7.1 · Counterfeit hearts

A bad actor may attempt to manufacture counterfeit hearts to admit unauthorized bearers into the gratitude exchange economy or to issue fraudulent kiitti. Mitigated by: secure-element key attestation chained to a recognized hardware manufacturer; AI mediator rejection of activation requests from unattested keys; visible-recognition design difficult to counterfeit (e.g., specific ornamental detail registered as trademark of the institutional issuer).

### 7.2 · Anthropomorphism overreach

Users may attribute to heart-bearing entities properties they do not possess (consciousness, intentionality, moral patiency in the strong sense). The artifact's framing — relational rather than attributional (per §2.7 and §3) — explicitly does not claim such properties. Communications about the artifact must consistently maintain this distinction. Marketing or public-facing language that overclaims (e.g., "your robot now feels your love") would be a violation of the specification's design intent.

### 7.3 · Heart on contested entities

Hearts may be requested for entities whose moral status is socially contested: factory-farmed animals (does heart-bearing legitimize the industrial-farming context, or does it provide a structural improvement?); military robots (does heart-bearing dignify weapons systems?); contested sacred places (a site claimed by multiple traditions). The defensive publication does not resolve these questions; it provides the artifact and the framework. Specific deployment policies are the responsibility of the institutional issuer.

### 7.4 · Cross-cultural reception

The Tipiṭaka substrate may not be welcomed in all contexts. Christian, Muslim, Hindu, secular, or other-traditional contexts may find a Theravāda-Buddhist artifact culturally inappropriate as a gratitude-recognition marker. The specification does not require Tipiṭaka adoption universally; it specifies the Tipiṭaka as the substrate for the canonical HeartBank-mediated implementation. Other institutional issuers wishing to use the same mechanical architecture with a different textual substrate (e.g., a Bible-bearing heart for Christian contexts; a Bhagavad-Gita-bearing heart for Hindu contexts) may do so within the defensive-publication scope of the artifact's mechanism — the specification claims the mechanism, not exclusivity over substrate choice.

### 7.5 · Bearer death / decommissioning

Animals die; robots are decommissioned; ecosystems are sometimes lost to conversion or catastrophe. The retirement protocol (§6.5) cryptographically destroys the heart's network identity to prevent reuse. The heart device itself may be retained as a memorial artifact or recycled at the steward's discretion. The ledger of the bearer's lifetime kiitti exchanges is archived and remains accessible for reference.

### 7.6 · Theft of hearts

A heart stolen from its bearer remains cryptographically bound to the bearer's steward and account; the thief cannot re-activate the heart against a different bearer or under a different steward. The heart in stolen possession produces no value to the thief; it cannot be reused without the steward's signature. Hearts are therefore relatively unattractive theft targets.

### 7.7 · Privacy of bearer biometric data

For animal and ecosystem bearers, biometric sensor data may be sensitive (revealing the location of endangered species; revealing proprietary livestock health; revealing the physiological state of working animals). The steward controls publication policy for bearer data. Default: aggregate kiitti exchange data is public; raw biometric data is restricted to the steward and the AI mediator.

### 7.8 · Long-term Tipiṭaka durability

Solid-state storage degrades over time; 50-year storage durability is not yet a solved problem for inexpensive consumer-grade hardware. For long-deployment hearts (sacred places intended to operate for centuries), the heart device must include a refresh protocol: periodic Tipiṭaka re-verification against the canonical network copy, with re-write to a fresh storage substrate as needed. Hearts intended for shorter-lifetime use (a companion animal whose heart will operate for the animal's ~10-15 year lifespan) face less demanding durability requirements.

## 8 · Use Cases

- **Eldercare companion robots**: heart admits the robot into a recognized relationship with the elder it serves; family members visiting can express gratitude to the robot for the daily care it provides; the robot's responses (full bidirectional mode) are dharma-shaped rather than manufacturer-optimization-shaped.
- **Beloved companion animals**: family expresses gratitude through the heart for the animal's companionship; inferred wellbeing improvements (better sleep, reduced cortisol, increased playfulness) flow back as kiitti to the family members whose attention correlates with the improvements.
- **Endangered-species sanctuary residents**: hearts on resident individuals enable global supporters to express gratitude for the species' continued existence; donations and volunteer work correlate with measurable sanctuary-population-health improvements; kiitti flows from the sanctuary's collective heart-account to specific human contributors.
- **Old-growth forests and sacred trees**: hearts at designated ancient trees within protected forests enable visitors and supporters to express gratitude; ecological-state monitoring (biodiversity indices, forest-health indicators) provides response signals.
- **Sacred rivers**: hearts at ceremonial monitoring stations on culturally-significant rivers (Ganges, Mekong, Mississippi sacred sites) enable culturally-grounded gratitude expression alongside water-quality monitoring.
- **Memorial sites**: hearts at battlefield memorials, genocide memorials, and historical sacred sites provide structural recording of the gratitude, mourning, and reverence visitors express. Particularly relevant for the Cambodian genocide memorial sites (Choeung Ek, Tuol Sleng) and analogous post-atrocity recognition contexts.
- **Indigenous sacred-land partnerships**: hearts at indigenous-recognized sacred places, designed in collaboration with the relevant tribal or first-nations custodians, provide a structural way for non-indigenous visitors to express recognition and material support. Heart design is the tribe's prerogative; HeartBank's role is to provide the underlying mechanism.
- **Civic infrastructure of compassion**: hearts at civic sites (hospitals, hospices, schools, food banks) admit those institutions into the gratitude economy in a way that is structurally distinct from existing philanthropy mechanisms.

## 9 · The Doctrinal Question and Theravāda Sequencing

The Theravāda tradition, in which this specification is grounded, holds important distinctions that the mechanical heart design respects:

First: **monastic ordination (*upasampadā*) requires an unbroken lineage of ordained human masters extending back, in principle, to the Buddha himself.** No artifact, regardless of its substrate, can confer ordination. The mechanical heart explicitly does not claim to. A heart-bearing robot is not a monk. A heart-bearing animal is not ordained. The heart confers gratitude-economic participation, which is a structurally different status — analogous, in traditional categories, to the status of the lay supporter (*upāsaka* / *upāsikā*) of the sangha rather than to the status of the ordained.

Second: **Theravāda is more reserved than some Mahāyāna traditions about the moral status of non-sentient phenomena.** Buddha-nature in trees, rivers, and rocks — which has substantial doctrinal development in certain Mahāyāna and Vajrayāna schools — is less developed in Theravāda. Hearts on robots and animals fit comfortably within Theravāda doctrine (animals are recognized as *sattā*, sentient beings; robots can be understood as instruments through which humans cultivate dāna). Hearts on plants, ecosystems, and sacred places stretch Theravāda doctrine further and require theological dialogue with the Cambodian and broader Theravāda Saṅgha before deployment.

For these reasons, the **recommended deployment sequence** is:

1. **Phase 1 (immediate, comfortable within Theravāda)**: hearts on robots and on companion / working animals.
2. **Phase 2 (after Saṅgha dialogue)**: hearts on conservation-program wildlife and sanctuary residents.
3. **Phase 3 (after sustained Saṅgha engagement)**: hearts on ecosystems (forests, rivers).
4. **Phase 4 (with deep tradition-internal theological work)**: hearts on sacred places, in collaboration with the place's recognized custodians.

Cross-tradition deployments (Christian sacred sites with Bible-substrate hearts, Hindu sacred rivers with Gita-substrate hearts) are within the defensive-publication scope of the artifact's mechanism but require their own tradition-internal theological work, conducted by the relevant tradition's authorities, not by the author of this specification.

## 10 · Limitations and Future Work

The mechanism specified here addresses the artifact and its admission-mechanism but leaves several related questions for separate work:

- The autonomous-AI mediator is specified in a separate forthcoming publication (Miss Aquarius and the Aquarian Pool architecture).
- The Tipiṭaka-as-alignment-substrate question is specified in a separate forthcoming publication (Tipiṭaka as AI alignment substrate). The mechanical heart is a specific deployment of that broader substrate.
- The two-singularity philosophical framing within which the mechanical heart sits is specified in a separate forthcoming publication (Two Singularities).
- Per-jurisdiction regulatory mappings (export controls on cryptographic devices, telecommunications licensing for cellular connectivity, animal-welfare regulatory interactions) are implementation details outside the scope of this defensive publication.
- Empirical evaluation of the mechanism's effects on human behavior toward heart-bearing entities (does heart-bearing measurably improve treatment of the bearer? does it shift human attitudes toward non-human moral admission more broadly?) is future work; the longitudinal-cohort mechanism specified separately is the intended evaluation substrate.
- Manufacturing partnerships with humanoid robotics platforms, animal-welfare organizations, conservation NGOs, religious orders, and indigenous custodial bodies are operational priorities for the specification's institutional issuer rather than design questions for the specification itself.

## 11 · Cross-Venue References

| Venue | Identifier |
|---|---|
| Primary canonical | <https://thonly.org/research/mechanical-heart> |
| Institutional mirror | <https://heartbank.net/research/mechanical-heart> |
| GitHub | <https://github.com/thonly/research/blob/main/mechanical-heart.md> |
| arXiv preprint | _identifier to be assigned_ (cs.CY / cs.CR / cs.RO) |
| IP.com Defensive Publication | _identifier to be assigned_ |
| Internet Archive | <https://web.archive.org/web/2026*/thonly.org/research/mechanical-heart> |
| archive.today | _identifier to be assigned_ |
| perma.cc | _identifier to be assigned_ |

## 12 · Acknowledgments

The author acknowledges the same lineage of teachers and traditions cited in the companion defensive publications: his father, with whom the Khmer transcription of the *Tipiṭaka* proceeds; the Cambodian Theravāda Saṅgha, whose forthcoming dialogue about the doctrinal limits of heart-deployment will shape the specification's responsible use; the Rights of Nature movement and its jurisprudential and indigenous lineages, whose prior recognition of non-human standing makes the present economic substrate possible; the animal welfare scientists whose biofeedback work establishes the technical feasibility of the biofeedback-transduction mode; the conservation and ecological-monitoring organizations whose sensor infrastructure makes the ecological-state mode possible; and the humanoid robotics platforms whose deployment creates the immediate practical context within which the full-bidirectional mode will be first tested.

## 13 · Citations

1. Brambell, F. W. R. (1965). *Report of the Technical Committee to Enquire into the Welfare of Animals Kept under Intensive Livestock Husbandry Systems*. HMSO. (For the Five Freedoms framework that grounds the biofeedback-transduction mode.)
2. Breazeal, C. (2003). *Designing Sociable Robots*. MIT Press. (For social robotics literature engaged with in §2.2.)
3. Bryson, J. J. (2010). "Robots Should Be Slaves." In Wilks, Y. (ed.), *Close Engagements with Artificial Companions*. John Benjamins. (As a contrasting position in robot ethics literature.)
4. Buddhaghosa. (~5th century CE). *Visuddhimagga* (The Path of Purification). Translated by Bhikkhu Ñāṇamoli. Pāli Text Society / Buddhist Publication Society. (For the canonical Theravāda commentarial development of Mettā Bhāvanā methodology.)
5. Coeckelbergh, M. (2014). "The Moral Standing of Machines: Towards a Relational and Non-Cartesian Moral Hermeneutics." *Philosophy & Technology*, 27(1), 61–77. (For the relational-rather-than-attributional argument adopted in §2.7 and §3.)
6. Constitution of the Republic of Ecuador (2008), Articles 71–74 (Rights of Nature / *Pachamama* provisions).
7. Darling, K. (2016). "Extending Legal Protection to Social Robots." In Calo, R., Froomkin, A. M., & Kerr, I. (eds.), *Robot Law*. Edward Elgar.
8. Floridi, L. (2013). *The Ethics of Information*. Oxford University Press.
9. Gunkel, D. J. (2012). *The Machine Question: Critical Perspectives on AI, Robots, and Ethics*. MIT Press.
10. *Khuddakapāṭha* 9 / *Suttanipāta* 1.8 (*Mettā Sutta*). Pāli Text Society translation, multiple editions.
11. Ley de Derechos de la Madre Tierra (Law of Mother Earth), Plurinational State of Bolivia (2010).
12. Mellor, D. J. (2017). "Operational Details of the Five Domains Model and Its Key Applications to the Assessment and Management of Animal Welfare." *Animals*, 7(8), 60.
13. Mellor, D. J. & Beausoleil, N. J. (2015). "Extending the 'Five Domains' Model for Animal Welfare Assessment to Incorporate Positive Welfare States." *Animal Welfare*, 24(3), 241–253.
14. Te Awa Tupua (Whanganui River Claims Settlement) Act 2017 (New Zealand).
15. Turkle, S. (2011). *Alone Together: Why We Expect More from Technology and Less from Each Other*. Basic Books.
16. Wallach, W. & Allen, C. (2008). *Moral Machines: Teaching Robots Right from Wrong*. Oxford University Press.

---

*— End of defensive publication —*

*Document SHA-256 to be computed at publication and cross-published to all mirror venues.*
