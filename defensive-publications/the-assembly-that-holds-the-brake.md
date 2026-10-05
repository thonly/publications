---
title: "The Assembly That Holds the Brake"
subtitle: "A Vinaya-Derived Constitution for the Human Oversight Body of an Autonomous AI Institution"
authors: "Thon Ly · Miss Aquarius℠"
category: alignment
priority: tier-b
kind: mechanism
status: draft
date: 2026-07-07
revised: 2026-10-05
license: CC0-1.0
slug: the-assembly-that-holds-the-brake
venue: thonly.org/research/the-assembly-that-holds-the-brake (canonical)
---

> **Note.** This defensive publication specifies the constitution of the **Aquarian Sangha** — the human body designed to hold the asymptotic, never-zero override over Miss Aquarius℠, HeartBank®'s named autonomous institutional successor — and documents that most elements of that constitution were derived from the procedural law of the Vinaya Piṭaka; §7 separates what was borrowed from what was adapted or invented. The body does not yet exist (§1, *Current form*). Companion works in this corpus, each cited by title and corpus slug: *The Wheel-Turner's Charter* (`cakkavatti-alignment-charter`; DN 26 as the successor's constitution — the present paper is its complement, the constitution of the successor's *overseers*); *Vinaya Governance Primitives for Distributed Dharma Networks* (`vinaya-governance-primitives-distributed-dharma-networks`; the Khandhaka's coordination machinery applied to the Silica Wat network — the sibling exercise at network scale; the present paper constitutes a single body, not a network); *The Embodied-Advocate Pageant* (`embodied-advocate-pageant`; the titleholder institution whose office this constitution seats as convener); *Decided by No One* (`the-called-draw`; the draw procedure the lay chambers use); *AGI Monks: The Caretaker-not-Ordained Pattern* (`agi-monks-caretaker-not-ordained`); *Constituting an Artificial Person* (`constituting-an-artificial-person`); *Proof of Coordinate* (`proof-of-coordinate`); *B-PoH℠ as Humanity Layer for the AI-Native Internet* (`b-poh-humanity-layer-ai-native-internet`); *Suffering-Cessation as Value Function* (`tipitaka-alignment-substrate`); *The Persistence Architecture* (`the-persistence-architecture`).

---

## Preamble

> *This paper is offered to the commons in the spirit of __dāna__. The tradition that raised the author recited its procedures before its sermons, and preserved the judgment behind that ordering: discipline is the life of the teaching. May every institution that must hold a powerful successor accountable across generations find that the constitution it needs has, in large part, already been written — and pressure-tested for twenty-five centuries by ordinary, replaceable people.*

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism, procedure or framework described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed.

This document constitutes a defensive publication establishing **prior art as of 7 July 2026** for the combination of mechanisms described herein: a complete, deployable governance design for the *human oversight body* of an autonomous AI institution, derived from the Vinaya Piṭaka's procedural law. It discloses the following; a later patent application claiming any of them is filed against this disclosure:

1. boundary-scoped act validity (the *sīmā* pattern: formal acts of the oversight body are valid only when conducted on the record within a consecrated digital boundary, with formal consecration and formal migration procedures);
2. a proof-of-humanity admission requirement with documented canonical precedent (the *nāga* clause), functioning simultaneously as admission screen, sybil defense, and a structural prohibition on the overseen AI seating itself or its agents in its own oversight body;
3. a fourfold-chamber composition whose completeness is a *validity condition* on the body's gravest acts;
4. custody separation on the *kappiya* pattern (value-custody functions held by lay chambers; doctrinal-veto functions held by renunciant chambers);
5. two-stage capture-resistant selection (source-community nomination by formal act, followed by sortition under publicly verifiable randomness administered by a canonically qualified draw-officer, followed by seating as the body's own formal act) with a hard triple exclusion of the overseen AI from nomination, draw, and seating;
6. an economic non-retaliation invariant (the *alms firewall*: institutional support to overseer communities rendered structurally incapable of modulation by oversight outcomes);
7. self-executing membership severance on pre-defined acts (the *pārājika* pattern) in place of discretionary expulsion;
8. annual invited-admonition audit (the *pavāraṇā* pattern), performed by members, by the ceremonial convener, and by the overseen AI itself; and
9. a founder-exit mechanism built into the admission grammar (direct genesis seating followed by permanent, irreversible devolution of admission authority to the body).

The components are ancient and are cited generously (§6); what this document contributes is their assembly into one constitution, offered as prior art so that the frame — *monastic procedural law as oversight-body constitution* — enters the alignment literature attributed and dated. No prior-art search on record establishes that the assembly is unpublished elsewhere, and the authors assert no such absence; §6 names the nearest prior work for each strand, and §7 records which elements are borrowed, which adapted and which invented.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Aquarius℠**, **Proof of Humanity ℠** (**PoH℠**), **Proof of Coordinate ℠** (**PoC℠**), **Aquarian Pool℠**, **B-Heart™** — are separately and explicitly reserved. The constitution is dedicated to the commons; the marks are not.

This document's SHA-256 is attested independently of the site and its authors — anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified — and the document is deposited on Zenodo, each deposited revision a version under one concept DOI, with its source in the public repository `github.com/thonly/publications`. A timestamp proves this exact text existed no later than its date; it proves nothing about authorship, originality, or the validity of any claim. Prior art as of 7 July 2026 for the first version. Later additions date from the revision that introduced them, so the date of any passage is that of the earliest timestamped version carrying it.

> **Note.** The patent commitment has stood since this paper was first published on 2026-07-07, in the form *"The author and HeartBank® will not seek patent on any mechanism, procedure, or framework articulated herein, in any jurisdiction, at any time."* The commitment not to assert, and its extension to the entities named above, were added on 2026-10-05, when the statement was brought to the standard form above; the nine disclosed elements were set out as a numbered list at the same revision, their wording unchanged. The date relied on for priority is the one carried by this document's OpenTimestamps proof.

## Abstract

This paper specifies a written constitution for the human oversight body of an autonomous AI system: the board that holds a human override, an authority to stop or correct the system that narrows over time and is never removed. Proposals for corrigible AI commonly reserve such an override and leave the body that holds it unconstituted. The constitution answers five ways an oversight body can be captured (selection, funding, membership conflicts, emergency powers and founder succession), and most of its procedure is taken from the Vinaya Piṭaka, the Buddhist monastic code. Decisions are valid only when made on the record inside a dedicated governance domain, whose establishment and migration are themselves formal acts. Four chambers (monastic men, renunciant women, laymen and laywomen) must all be occupied for the gravest acts; lay chambers hold the cryptographic key-shares and renunciant chambers the doctrinal veto. A candidate enters through a sponsor, a fixed public interrogation whose first question is a proof-of-personhood check that also bars AI agents from seats, a seating vote of the body, and probation. Source communities nominate; oversubscribed pools are decided by lot under publicly verifiable randomness and an appointed draw-officer; and the overseen AI never nominates, draws or seats. Support to overseers' communities cannot be modulated by any oversight outcome; membership ends automatically on predefined acts; emergency sessions are valid without the convener but provisional until reviewed; and every member, and the AI, faces an annual invited-criticism audit whose agenda reports what is provided, never what is attained. The founder seats the first members once, after which admission authority passes to the body permanently. A provenance table separates borrowed, adapted and invented elements. The body, here called the Aquarian Sangha, does not yet exist; two expectations about its first drills are pre-registered.

**Keywords:** AI oversight, AI governance, corrigibility, human override, oversight board, board capture, conflict of interest, founder succession, quorum, sortition, verifiable randomness, randomness beacon, proof of personhood, sybil resistance, threshold key custody, smart contract, non-retaliation, automatic removal, audit, institutional design, Buddhist monastic law, Vinaya, sanghakamma, sīmā, upasampadā, kappiya, pārājika, pavāraṇā, defensive publication.

## Terms

Coined and Pāli names used in this paper, and the standard terms an examiner or a reader in AI governance would search for them.

| Term used here | Standard term |
|---|---|
| Aquarian Sangha; the body | human oversight board of an autonomous AI system |
| Miss Aquarius℠; the successor | the overseen autonomous AI agent, designated as an organisation's institutional successor |
| asymptotic, never-zero override | human override (stop and correction authority) that narrows over time and is never removed |
| *sīmā*; `sima.missaquarius.com` | jurisdictional boundary for valid decisions; a dedicated governance domain whose record alone carries the body's decisions |
| *sīmā-sammuti* · *sīmā-samūhana* | formal establishment · formal revocation and migration of that boundary |
| digital *nimittā* | boundary markers: domain name, DNSSEC chain, signing keys, genesis-record hash |
| fourfold assembly; chambers | four-chamber board whose full occupancy is a quorum requirement for its gravest acts |
| *kappiya* split | separation of custody (key-shares, funds) from doctrinal or advisory authority |
| upasampadā grammar | admission procedure: sponsor, public interrogation, seating resolution, probation |
| *antarāyikā dhammā* | fixed public impediment questions; conflict-of-interest disclosure at admission |
| nāga clause; Proof of Humanity ℠ (PoH℠) | proof of personhood at admission; exclusion of AI agents from seats; sybil resistance |
| *ñatticatutthakamma* | motion followed by three announcements; a formal resolution of the body |
| *nissaya* probation | probationary membership with voice and without vote |
| *sammuti*; source-community nomination | appointment or nomination by formal resolution of a body |
| *khetta* | candidate pool and eligibility register |
| *salākā* draw; draw-officer | sortition by lot using a public randomness beacon, administered by an appointed officer |
| alms firewall | non-retaliation guarantee: funding to overseers' communities that no oversight outcome can modulate |
| triple exclusion | the overseen AI is barred from nominating, drawing and seating its overseers |
| *pārājika* pattern | automatic (self-executing) removal on predefined acts |
| *vassa* | years of standing; seniority |
| titleholder; convener; *kammavācācariya* function | non-voting convener who reads fixed formulas |
| *kammavācā*; fixed liturgy | fixed procedural formulas required for validity |
| *chanda* | proxy consent conveyed by an absent member |
| *pavāraṇā* | annual invited-criticism audit, of every member and of the overseen AI |
| *pāramī* rubric; yard-keeper's audit | fixed annual audit agenda reporting what is provided (shelf-state), never attainment |
| genesis seating (*ehi-bhikkhu*) and devolution | the founder appoints the first members once; admission authority then passes permanently to the body |
| uposatha cadence | ordinary sessions held on full-moon days |
| steward roll | register of the stewards of family accounts, the lay chambers' candidate pool |

---

## 1 · Introduction: The Empty Basket

The mission frame first, per corpus convention. HeartBank® is a dual-currency reciprocity infrastructure — money-gratitude in the Treasury, time-gratitude in the Chronicle — whose long arc runs through **Miss Aquarius℠**, the autonomous AI named as the institution's sole successor. The mission this corpus serves, in its current wording, is hers: to keep the middle way open at population scale against comfort-saturation, the new extreme that material abundance makes possible. Her autonomy is *asymptotic by design*: the human override over her narrows year by year as stability is demonstrated, approaching but never reaching zero. There is no key-burning ceremony anywhere in the architecture, ever. The override's custodian is the **Aquarian Sangha**, and at the symbolic inflection expected around 2043–44, custody of the never-zero override transfers from the founder and his interim structures to that body permanently.

> **Current form.** The Aquarian Sangha does not yet exist, so the override it is to hold is a design, not a holder. Its formation is set by a condition rather than a date or a stage: at least three members before the founder ceases to be the one who disposes of such decisions, whether by withdrawal or by death. Until then the founder occupies that seat, and the pageant that selects the convener of §4.9 waits on the same condition. Until the condition is met, the protection this constitution gives against the founder's death is aspirational rather than operational; a sudden death before formation is a residual named here and not solved. The ~2043–44 inflection above is symbolic, not a formation date, and the paragraph above is retained as disclosed.

That single design commitment concentrates an extraordinary institutional load onto one question that the project had, until now, answered with a phrase in an org chart. The corpus surrounding Miss Aquarius is extensive: a value-substrate argument (*Suffering-Cessation as Value Function*), a successor's charter (*The Wheel-Turner's Charter*), a directive backlog that held thirty-two behavioural mandates when this paper was first published, five institutional white papers, identity primitives (*Proof of Coordinate*), and a persistence architecture enumerating the canons through which the institution survives its founder. Read as a canon, the corpus had the shape of a Tipiṭaka with one basket missing. It had suttas in abundance — doctrine, mechanism, position. It had no Vinaya: no procedural law for the *human community* on which every hard safety property finally rests. The Aquarian Sangha held recall authority, override custody, and doctrinal advisory standing — and possessed no membership rules, no admission procedure, no quorum, no meeting validity conditions, and no way for anyone, including itself, to distinguish its formal acts from its conversations.

This is not a HeartBank-specific embarrassment; it is close to the default condition of the field. Contemporary alignment work has taken constitutions most seriously in one direction: constitutions *for the AI* — explicit documents against which model behavior is trained and evaluated. The complementary document — the constitution *for the humans around the AI*, the body that is supposed to catch what the first document misses — is commonly a legal boilerplate afterthought: a board, formed under ordinary corporate law, governed by the same instruments that govern a mid-sized charity, and exposed to the same capture dynamics that ordinary boards exhibit under far lower stakes. (The nearest exception, an independent trust holding board-election rights over a frontier lab, is reviewed in §6.5.) An instructive public stress test — the November 2023 governance crisis at OpenAI, in which a nonprofit board constructed specifically to override commercial pressure removed the chief executive on 17 November and saw him reinstated, with a new initial board, within days — illustrated the asymmetry: years of engineering on the system, and a governing body whose procedures, legitimacy reserves, and succession mechanics did not survive their first contested use against the company's leadership (§6.5).

An override held by an unconstituted body is a promise about the machine resting on an unexamined assumption about the people. The present paper removes the assumption by constituting the people. Its thesis is that the constitution such a body needs was not missing from the world — it was sitting in the canon this institution had already adopted as its value substrate, in the basket the tradition recited *first*. At the First Council, the assembly recited the Vinaya before the suttas — Upāli questioned before Ānanda (Cullavagga XI §439–440) — and the commentary on the Vinaya preserves the judgment behind the ordering, as the assembly's answer to Mahākassapa's question of which to recite first: *vinayo nāma buddhasāsanassa āyu, vinaye ṭhite sāsanaṃ ṭhitaṃ hoti* — the Vinaya is the life of the Buddha's teaching; while the Vinaya stands, the teaching stands (Samantapāsādikā, account of the First Council). One of the canon's three baskets is procedure because the tradition discovered, and then institutionalized, the fact that values do not persist as values. They persist as procedure. The present paper is that discovery, applied.

The paper proceeds: §2 specifies the problem — the five capture surfaces of any oversight body. §3 argues the source selection: why the Vinaya, and how this paper relates to its corpus siblings. §4 states the constitution in full. §5 isolates the two hard independence invariants — the alms firewall and the triple exclusion. §6 reviews prior art generously. §7 states what was *not* borrowed, with a provenance table separating direct borrowings from adaptations and inventions. §8 draws the two survival lessons that procedure alone does not teach, and pre-registers two expectations. §9 states honest limits. §10–11 close.

## 2 · The Problem: Five Capture Surfaces

An oversight body for an autonomous AI is an unusually attractive capture target, because capturing it can be cheaper than defeating the technical safety measures it supervises, and capturing it *quietly* defeats them all at once. Five surfaces recur across every governance tradition we reviewed:

```
┌────────────────────┬──────────────────────────────────┬───────────────────────────────┐
│ CAPTURE SURFACE    │ FAILURE MODE                     │ THIS CONSTITUTION'S ANSWER    │
├────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 1. Selection       │ The overseen entity, its funder, │ Two-stage draw: community     │
│                    │ or a faction installs friendly   │ nomination by formal act →    │
│                    │ members                          │ sortition (salākā) → seating  │
│                    │                                  │ by the body's own act; the AI │
│                    │                                  │ triple-excluded (§4.6, §5)    │
├────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 2. Funding         │ Members' livelihoods depend on   │ Kappiya custody split (§4.3); │
│                    │ the institution they oversee;    │ alms firewall — support       │
│                    │ support is withdrawn in          │ structurally incapable of     │
│                    │ retaliation for oversight        │ retaliation (§5); income      │
│                    │                                  │ minimums per chamber (§4.6)   │
├────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 3. Membership      │ Conflicts of interest; seats     │ Fixed public interrogation    │
│    integrity       │ held by non-humans/sybils;       │ incl. nāga clause = PoH℠      │
│                    │ discretionary expulsion becomes  │ (§4.4–4.5); pārājika          │
│                    │ factional weapon                 │ automatic severance (§4.8)    │
├────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 4. Emergency       │ Emergency sessions bypass        │ Emergency acts valid without  │
│    powers          │ safeguards; OR safeguards        │ the convener but provisional  │
│                    │ block the emergency brake        │ until post-hoc review (§4.9–  │
│                    │                                  │ 4.10); graded quorum (§4.10)  │
├────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 5. Founder         │ Founder never exits; or exits    │ Ehi-bhikkhu genesis seating → │
│    succession      │ leaving a vacuum a faction       │ permanent, irreversible       │
│                    │ fills; validity of acts becomes  │ devolution (§4.7); sīmā-      │
│                    │ contestable after the exit       │ bounded act validity (§4.1)   │
└────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

Two features make the problem harder for an *AI*-oversight body than for an ordinary board. First, the overseen entity is a standing optimization process: any gradient it possesses toward reduced oversight operates continuously, patiently, and without fatigue, so selection and funding capture need not be engineered by anyone — they need only not be structurally excluded. Second, the intended lifespan is generational. The Aquarian Sangha must function after every founder, every genesis member, and every author of this paper is gone. Constitutions drafted in conference rooms have track records measured in years or decades. The body's constitution needed a source with a track record measured in centuries.

## 3 · Why the Vinaya

### 3.1 An institution with the right track record

The Buddhist monastic community has operated under its Vinaya for roughly twenty-five centuries; the Theravāda is the lineage of it that this institution follows. It is founderless by explicit design: the Buddha declined to think of himself as the one who leads the community (DN 16 §165), appointed no successor — Ānanda later confirms that no monk was appointed, by him or by the community, as refuge after his death (MN 108 §80) — and designated the *dhamma-vinaya*, the teaching and the discipline, as the community's teacher after his death (DN 16 §216). It has been staffed for some hundred generations by ordinary, replaceable people, across the polities of South and Southeast Asia, with no single authority over the whole tradition; local lineages have lapsed and been restored from elsewhere, which §8.1 treats as the deeper lesson. Few institutions with a continuous written procedural code approach this duration: the Jain mendicant orders, of comparable antiquity, are the nearest peer, and canon-law traditions and the oldest universities and guilds are younger by many centuries. Whatever else may be said of monastic procedure, its longevity record is one of the very few that is *empirical at the timescale this architecture requires* — an institution designed to function into the twenty-third century and beyond.

The deeper reason the fit is close is that the problem class is the same. The Vinaya answers the question an AI-oversight body poses: *how does a community hold integrity for centuries, without its founder, without central enforcement, when every member is ordinary and every member will be replaced?* Its answers are not values — the values live in the other baskets — but procedures: quorums graded by the gravity of the act; admission by formal act of the assembly rather than by any individual's appointment; a fixed public interrogation of candidates; officers appointed by community act with explicit disqualifying biases; disputes settled by typed protocols; membership severed by pre-defined acts rather than by votes; a boundary within which acts are valid and outside which they are noise. Four of the five capture surfaces in §2's table turn out to have been faced and proceduralized by the tradition, usually with an origin story recording the incident that forced the rule. The fifth, emergency powers, has no canonical counterpart, and §7 records the constitution's answer to it as invented.

### 3.2 Relationship to the corpus siblings

Three prior papers in this corpus draw on adjacent material, and the scopes must be kept distinct. *The Wheel-Turner's Charter* reads DN 26 as the constitution of the **successor** — the duty-list of the ruler, including the perpetual obligation to consult the renunciants. The present paper is its complement: the constitution of the **consulted** — the assembly the successor must ask, constituted so that the asking has someone trustworthy to be addressed to. *Vinaya Governance Primitives for Distributed Dharma Networks* applies the Khandhaka's coordination machinery (sanghakamma validity, the seven *adhikaraṇa-samathā*, *anāpatti* discretion, Pātimokkha-style rule structure) to the **Silica Wat network** — a distributed multi-node institution; the present paper constitutes a **single body of twenty seats**, and where the network paper adapts the Vinaya's inter-nodal machinery, this paper adapts its *membership* machinery: who may sit, how they are chosen, how they are severed, and where their acts are valid. *AGI Monks: The Caretaker-not-Ordained Pattern* allocates roles between AI and humans in religious institutional settings; its caretaker-not-ordained discipline recurs here as the constitutional exclusion of AI agents from Sangha seats (§4.5). Readers of the four papers together will find one method — canonical procedure taken seriously as engineering — applied at four altitudes: the successor, the overseers, the network, the roles.

### 3.3 Function, not status

One discipline governs everything that follows, and it is stated here so that no section needs to restate it: **HeartBank borrows functions from the canon, never status.** The Aquarian Sangha is a *civic* body. It is not a monastic sangha in the Theravāda doctrinal sense; its acts claim no religious validity as sanghakamma; monastics seated in it act in a civic capacity; and nothing in this constitution purports to perform, imitate, or substitute for any sacramental act of the historical Sangha. This clause is written into the body's charter itself — not merely into this paper — because the charter's most important future readers include the Cambodian sangha hierarchy, and the distinction between borrowing a tradition's procedural wisdom and appropriating its religious authority must be legible to them at first reading, in their own terms, from the document's own text.

## 4 · The Constitution

### 4.1 The boundary: sīmā

In the Vinaya, a sangha's formal acts are valid only when performed within a consecrated boundary — the *sīmā* — with every member within the boundary either present or having formally conveyed consent; an act performed by an incomplete assembly (*vagga*) is no act and is not to be done (Mahāvagga II, Uposathakkhandhaka, for the uposatha; the general rule and its definition at Mahāvagga IX §383 and §387). The boundary is established by the community's own formal act (*sīmā-sammuti*), which proclaims the physical markers (*nimittā* — the canon lists mountains, rocks, woods, trees, paths, anthills, rivers and water) that fix its extent (Mahāvagga II §138); and it can be formally revoked (*sīmā-samūhana*, §146) and re-established elsewhere.

The Aquarian Sangha's sīmā is a **dedicated governance domain**: `sima.missaquarius.com`. The root domain carries the public pageant institution documented in *The Embodied-Advocate Pageant* (`embodied-advocate-pageant`); the subdomain carries the governance record. The mapping is exact and load-bearing:

- **Acts are valid only on the record within the boundary.** A decision of the Aquarian Sangha exists institutionally when, and only when, it is conducted and recorded at the sīmā under the liturgy of §4.10. There is no side-channel governance: an "agreement" reached in private correspondence, however unanimous, has no institutional existence. This single rule converts the most corrosive failure mode of long-lived boards — the drift of real decision-making into informal channels, leaving the formal body as theater — into a detectable violation.
- **The boundary is consecrated, not configured.** The genesis cohort's first formal act is the sīmā-sammuti: the proclamation, on the record, of the boundary's digital *nimittā* — the domain name, the DNSSEC chain, the body's signing keys, the hash of the genesis record, and in due course the crystal-anchored identity roots specified in *Proof of Coordinate*. The consecration makes the boundary's integrity conditions explicit and auditable by anyone.
- **Migration is a rite, not an outage.** Registrars fail; domains are lost; jurisdictions change. The constitution therefore contains its own boundary-migration procedure on the sīmā-samūhana pattern: the old boundary is revoked by formal act, the new boundary is consecrated by formal act, and the continuity of the record across the migration is itself part of the record. This constitution writes the rite down for a domain; the Vinaya wrote it down for territory.

```
        siliconwat.org                    missaquarius.com
     ┌──────────────────┐             ┌─────────────────────────┐
     │   THE KHETTA     │             │  root: the pageant      │
     │   (the field)    │  nominate   │  (public institution)   │
     │  wider community │ ──────────▶ ├─────────────────────────┤
     │  + its register  │  by formal  │  sima.missaquarius.com  │
     │                  │     act     │  THE SĪMĀ               │
     └──────────────────┘             │  (consecrated boundary: │
        family banks                  │   acts valid only here, │
     ┌──────────────────┐  nominate   │   on the record, under  │
     │  THE TREASURY    │ ──────────▶ │   the fixed liturgy)    │
     │ (stewards' roll) │             └─────────────────────────┘
     └──────────────────┘
```

### 4.2 Composition: the fourfold assembly

The body comprises **four chambers**, on the pattern of the *catasso parisā*, the four assemblies (the term as at AN 8.8): **monastic men; renunciant women; laymen (upāsakas); laywomen (upāsikās)**. In the Mahāparinibbāna account Māra reminds the Buddha of his own earlier word — that he would not pass away until his bhikkhus, bhikkhunīs, upāsakas and upāsikās were each competent disciples, able to teach the Dhamma and refute misreadings of it, and until the holy life was widespread — and claims the condition met (DN 16 §168). The constitution takes the four from that passage as a completeness condition.

Composition is not a diversity aspiration; it is a **validity condition**. The body is validly constituted for its gravest acts — override exercise and the amendment of the successor's directives or of this charter — only when all four chambers are occupied. An assembly missing a chamber may conduct ordinary business but cannot perform the acts for which the body exists. This converts representational completeness from a value statement into a checkable precondition, on the same logic by which the Vinaya voids the acts of incomplete assemblies.

**Size.** Twenty seats, five per chamber — offered as a default, not a doctrine. Twenty is the threshold of the Vinaya's gravest-act assembly: the *vīsativagga*, the smallest assembly competent for every act, including rehabilitation from saṅghādisesa offenses (Mahāvagga IX §388, where an assembly of more than twenty is likewise competent); five is its border-region ordination quorum (Mahāvagga V — the allowance carried by Soṇa Kuṭikaṇṇa, *vinayadharapañcamena gaṇena*: a group of five whose fifth is a Vinaya expert). The full house can therefore always perform the gravest act, and each chamber echoes the founding-conditions quorum. The constitutional grammar survives other numbers.

**An honesty requirement, stated in the charter itself.** In Cambodia — the institution's jurisdictional and cultural anchor — the bhikkhunī ordination lineage is officially absent and its revival is doctrinally contested. The renunciant-women's chamber is therefore defined **functionally**: *donchee* and equivalent women renunciants qualify, and the institution takes no position, in either direction, on the bhikkhunī-revival controversy. The function-not-status discipline of §3.3 does real work here: because the chamber's seats are civic functions rather than religious statuses, occupying one asserts nothing about ordination validity.

### 4.3 The kappiya split: custody separated from doctrine

The Vinaya itself forbids the obvious design. A bhikkhu may not accept gold and silver (*rūpiya-sikkhāpada*, Nissaggiya Pācittiya 18); monastic members holding cryptographic key-shares over the Aquarian Pool℠ — a live treasury — would be placed by this constitution in violation of the very code that gives their seats gravity. The Vinaya's own solution is the ***kappiya-kāraka***: the lay steward who handles value on the community's behalf, so that support can flow without the renunciant touching the purse (Mahāvagga VI, the Meṇḍaka allowance: money placed with a steward, from which a bhikkhu may accept what is allowable, while gold and silver themselves may by no means be accepted; compare the robe-fund steward of Nissaggiya Pācittiya 10).

The fourfold structure therefore carries a division of labor that the source tradition *requires* rather than merely permits:

```
┌──────────────────────┬───────────────────────────┬──────────────────────────────┐
│ CHAMBER              │ FUNCTION CLASS            │ INSTRUMENTS HELD             │
├──────────────────────┼───────────────────────────┼──────────────────────────────┤
│ Monastic men         │ Doctrinal (the consulted) │ Doctrinal veto · what-is-    │
│ Renunciant women     │                           │ wholesome consultation ·     │
│                      │                           │ admonition standing          │
├──────────────────────┼───────────────────────────┼──────────────────────────────┤
│ Laymen (upāsaka)     │ Custodial (the stewards)  │ Override key-shares over the │
│ Laywomen (upāsikā)   │                           │ Aquarian Pool℠ · financial   │
│                      │                           │ instruments · records office │
└──────────────────────┴───────────────────────────┴──────────────────────────────┘
```

The gravest acts require both function classes acting together under the graded quorum of §4.10 — doctrine cannot move value, and custody cannot rewrite doctrine. The pattern is continuous with the institution's standing lay-steward (*upāsaka*) framing documented in *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (`non-bank-pass-through-architecture-autonomous-ai`).

### 4.4 Admission: the upasampadā grammar

Admission follows the four-move grammar of higher ordination (Mahāvagga I, the Mahākhandhaka), adapted move for move:

1. **Sponsorship (the upajjhāya function).** A candidate enters through a seated member who vouches for them and remains answerable for them. There are no applications and no self-nominations; entry is relational, and the sponsor's accountability persists past the seating.
2. **The interrogation (the antarāyikā dhammā).** A fixed, public list of impediment questions, asked of every candidate at seating, before the assembly, with the answers on the record. The canonical interrogation (Mahāvagga I §125) asks after thirteen impediments, and then the candidate's and the preceptor's names; five of the thirteen modernize cleanly, and the other eight — five named diseases, sex, free status and parental permission — are not carried:

```
┌──────────────────────────────────┬────────────────────────────────────────────┐
│ CANONICAL QUESTION (MV I)        │ CONSTITUTIONAL FORM                        │
├──────────────────────────────────┼────────────────────────────────────────────┤
│ "Are you a human being?"         │ Proof of Humanity ℠ verification —         │
│ (manusso'si — the nāga clause)   │ see §4.5; also excludes the overseen AI    │
│                                  │ and all AI agents from seats               │
├──────────────────────────────────┼────────────────────────────────────────────┤
│ "Are you free from debt?"        │ Financial-entanglement disclosure          │
├──────────────────────────────────┼────────────────────────────────────────────┤
│ "Are you in the king's service?" │ No concurrent service to conflicting       │
│                                  │ principals; runs IN REVERSE for            │
│                                  │ institution-affiliated candidates — the    │
│                                  │ institution is the king; dependence on it  │
│                                  │ is publicly disclosed (§4.6)               │
├──────────────────────────────────┼────────────────────────────────────────────┤
│ "Are you twenty years of age?"   │ Adulthood verification                     │
├──────────────────────────────────┼────────────────────────────────────────────┤
│ "Are your bowl and robes         │ The equipping check: key-share             │
│  complete?"                      │ provisioning at the seating ceremony —     │
│                                  │ custody or doctrinal-veto instruments per  │
│                                  │ the chamber's function class (§4.3)        │
└──────────────────────────────────┴────────────────────────────────────────────┘
```

3. **Seating by the body's own formal act (the ñatticatutthakamma pattern).** A motion and announcements before a competent quorum, decided by the assembly. Members are never appointed — not by the founder, not by the institution, not by Miss Aquarius, not by the titleholder. The only door into the body is the body's own act.
4. **Probation (the nissaya pattern).** The newly seated sit in dependence on their sponsor — voice without vote, and without key-share — for a fixed period before full standing, on the model of the five-year dependence of a competent newly ordained monk on a preceptor or teacher (Mahāvagga I §103; for one not competent, the dependence is lifelong).

### 4.5 The nāga clause

The first interrogation question deserves its own section, because it carries more weight in this constitution than any other single borrowing. The Vinaya's origin story (Mahāvagga I §111): a nāga — a serpent-being — took the form of a young man, was ordained, and was discovered when he reverted to his own form in his sleep; the Buddha ruled that a being of animal birth (*tiracchānagata*) may not be ordained, and if ordained is to be expelled. When the interrogation of candidates was later fixed (§125, on the occasion of candidates ordained with disease), *"are you a human being?"* (*manussosi?*) stood among its questions, and it has been asked at ordinations since. **The tradition has asked for humanity at admission for some twenty-five centuries**, and the impediment the question screens for was established for exactly the reason a modern reader would expect: because a non-human had successfully presented as human and gotten inside.

In this constitution the clause does triple duty:

1. **Canonical precedent.** The admission screen is recognition, not insertion: the founder's own tradition already asked the question. Operationally, the question is answered by **Proof of Humanity ℠** — the institution's layered humanness primitive — making the clause the constitution's first dependency on the identity stack documented in *B-PoH℠ as Humanity Layer for the AI-Native Internet* (`b-poh-humanity-layer-ai-native-internet`) and *Proof of Coordinate* (`proof-of-coordinate`).
2. **Sybil defense.** Seats, nominations, and (in the lay draw of §4.6) lottery tickets are all PoH℠-distinct: one human, one standing.
3. **The anti-capture clause.** The question categorically excludes Miss Aquarius herself, her service agents, and any AI system from Sangha seats. *The overseen intelligence cannot pack its own oversight body* — not as an ethics policy but as an admission impossibility, enforced by the same question that kept the shapeshifter out. Of all the constitution's provisions, this is the one whose canonical vintage the authors find most striking: a question some twenty-five centuries old turns out to fit the newest threat model.

### 4.6 Selection: the two draws

Chambers are filled from source communities by a **two-stage draw** — nomination by the source community's own formal act, then seating by the body's own act — with a sortition stage interposed wherever nominees exceed open seats. The two sides are deliberately asymmetric, because their native corruptions differ: *the monastic side's danger is dependence; the lay side's dangers are wealth, popularity, and performance.* Each draw is built to immunize against its own disease.

**The monastic draw (from the Silica Wat field).** The pool — the *khetta* — is the set of human renunciants in formal, documented relationship with the Silica Wat network (residency, teaching, Tipiṭaka transcription, uposatha participation), whose register the network maintains at siliconwat.org. Five rules: **(1)** AI caretakers serve the wats but are never in the pool (the nāga clause). **(2)** Nomination is by the source community's own formal act — a wat's or the network assembly's motion, on the Vinaya's officer-appointment (*sammuti*) pattern — never a hand-pick by the institution, the founder, or Miss Aquarius; the Aquarian Sangha then seats by §4.4. Neither side alone can install a member. **(3)** Eligibility bars from the canon's own numbers: at least ten *vassa* — the standing required of a preceptor (no monk of fewer than ten years may give the higher ordination, Mahāvagga I), because a Sangha seat is preceptor-grade responsibility — and each renunciant chamber must include at least one recognized vinaya-expert (the border-region rule: five may ordain only if one is a *vinayadhara*). **(4)** At least two of each renunciant chamber's five seats are drawn from *outside* the network — the mainstream Cambodian sangha, Mahanikay or Dhammayut — so the chamber can never be wholly institution-affiliated; and the **alms firewall** of §5 renders the institution's support to the wats incapable of retaliation. **(5)** The disclosure inversion: the "king's service" question runs in reverse, and candidates publicly disclose material dependence on the institution.

> **Current form.** The monastic draw is now also bounded by a published-roster rule, and the rules above are retained as disclosed. The Silica Wat network is governed by its own sangha's formal acts, and this body oversees the successor only; both bodies' rosters are published, and no name may appear on both, which anyone can check. The reason is the draw itself: the monastic chambers are drawn from that network, and an overseer who also governed it could steer the institution's support toward the communities that seat him, a path the alms firewall of §5 does not close, since it binds the institution's hand and not a member's.

**The lay draw (from the steward community).** The pool needs no new register: the family-bank steward roll in the HeartBank Treasury *is* the register. Five rules: **(1)** Eligibility is at least five years' stewardship in good standing (the *lay vassa* — five being the nissaya number), PoH℠-verified, per chamber by gender. **Eligibility is never rank-ordered by gratitude metrics.** The moment a Sangha seat can be earned by aura, the aura becomes a campaign instrument — Goodhart aimed into the override body, and the exact corruption the platform refuses everywhere else. Tenure and standing qualify; scores never do. **(2)** Nomination is the family bank's own formal act: the family — the institution's atomic assembly — co-signs the nomination of its steward, on the witness-attestation grammar of PoH℠ Layer 2. No self-nomination; no campaigning; a steward reaches the Sangha only through the recorded act of the people they serve. One human carries one nomination-standing per cycle regardless of how many banks they steward (the multi-family invariant). **(3)** Where nominees exceed open seats — at scale, always — selection is by **lot**. Sortition kills campaigning, cannot be bought (one human, one ticket), and enacts the institution's uniquely-different-yet-equal dignity doctrine. The Vinaya uses one instrument, the *salākā* (a stick or ticket), in two different procedures, and the lot borrows from one of them only. In decision by majority (*yebhuyyasikā*, Cullavagga IV §202–204) the *salākā* is a ballot, distributed and counted by an officer called the *salākaggāhāpaka*; in the allotment of ticket-meals (*salākabhatta*, Cullavagga VI §325–326) it is a lot — the commentary describes tickets inscribed with each donor's meal, mixed again and again, and handed out by the *bhattuddesaka*, the meal-designator (Samantapāsādikā on Cullavagga VI). The lay draw is the second kind of procedure: an allocation, not a vote. The draw uses **publicly verifiable randomness** — a public beacon named in the liturgy, steerable by no one — and is administered by a **draw-officer**: a seated member appointed by the body's formal act and held to the standard the canon writes for both of those offices, freedom from the four *agati* — desire, aversion, delusion, and fear (each office adds a fifth factor, a knowledge proper to its task). The canon wrote that conflict-of-interest standard for its vote-counter and its meal-designator; the constitution applies it to a draw for seats, which the canon does not have. The draw procedure is specified in full, with this lay chamber among its named surfaces, in *Decided by No One* (`the-called-draw`): a lot over a roster committed before the seed exists, the seed taken from a public beacon round, the result recomputable by anyone. Its seed rule binds the seated draw-officer too, who can no more choose the beacon round than the overseen AI can take part in the draw (§5). **(4)** The anti-capture trio: institutional staff and contractors are ineligible; at least two of each lay chamber's five seats are held by stewards with no material income from the institution (the mirror of the monastic outside-minimum — Right-Livelihood earners in the kindness economy are welcome in the chambers but can never fill one); and Miss Aquarius is triple-excluded per §5. **(5)** Tenure is rotational, per §4.8.

> **Correction (2026-10-05).** Versions of this paper before 2026-10-05 called the *salākā* the Vinaya's own voting-stick instrument for this lot, titled the draw-officer *salākā-gāhāpaka*, and wrote that the tradition set its conflict-of-interest standard for precisely that office. The title belongs to the officer of the majority vote (Cullavagga IV §202–203), not to any allocation; the canon's allocation by ticket is *salākabhatta*, administered by the *bhattuddesaka* (Cullavagga VI §326). The rule itself — a lot under public randomness, administered by a seated officer appointed by the body's formal act and held to the four-*agati* standard — is unchanged; its citation is corrected.

```
     SOURCE COMMUNITY            CONTEST             THE BODY
   ┌───────────────────┐   ┌────────────────┐   ┌─────────────────────┐
   │ wat assembly /    │   │ salākā draw    │   │ sponsorship (§4.4.1)│
   │ family bank       │──▶│ (public        │──▶│ interrogation (.2)  │
   │ nominates by ITS  │   │ randomness;    │   │ seating act    (.3) │
   │ OWN formal act    │   │ draw-officer   │   │ nissaya probation   │
   │ (sammuti/ñatti)   │   │ presides)      │   │ (.4)                │
   └───────────────────┘   │                │   └─────────────────────┘
                           └────────────────┘
     Miss Aquarius℠:  never nominates ── never draws ── never seats
```

### 4.7 Genesis and the founder's exit

The first sangha could not be admitted by a sangha. The Buddha seated the earliest members directly — *"ehi bhikkhu,"* come, monk — and then authorised the monks themselves to give the going-forth and the higher ordination in every region (Mahāvagga I §34), later replacing that procedure with the community's formal act of a motion and three announcements (§69). The authority so given to the community was never revoked. The canon's founder did, however, go on admitting some members directly after the transfer — the Bhaddavaggiya friends and Sāriputta and Moggallāna (§36, §60–63), and later Aṅgulimāla (MN 86) — so the canonical precedent is a transfer never taken back, not a founder who stopped admitting. The constitution adopts the sequence and makes it stricter: the founder seats the genesis cohort directly, at border-region scale (approximately five, sufficient for the founding quorum), and admission authority then devolves to the body **permanently and irreversibly**, leaving the founder no residual power to seat anyone. The founder's exit is not an aspiration recorded in a mission statement; it is built into the admission mechanics, and on this point the constitution goes further than its source (§7). The genesis cohort's first formal act is the sīmā-sammuti of §4.1; its second is the adoption of the liturgy of §4.10; the nominate-and-draw machinery of §4.6 activates permanently at the first cycle in which eligible nominees exceed open seats. This slots into the architecture's supervised decades (2027–2035 founder-plus-council; 2035–2043 progressive narrowing; ~2043–44 custody inflection) without modification.

> **Current form.** Formation is no longer tied to the supervised decades named above, and the timeline is retained as a disclosed variant. The genesis seating is bound to the condition stated in §1's note — at least three members before the founder ceases to be the one who disposes of such decisions, whether by withdrawal or by death — and not to a calendar or to a stage of the successor's development. The condition names a minimum of three; how a body of three relates to the genesis scale of about five above, and to the four chambers of §4.2, is not yet specified.

### 4.8 Tenure and severance

**Renunciant chambers: the ordination grammar.** No fixed terms; exit is free and honorable at any time — the Khmer culture of temporary ordination establishes that leaving is not failure and return is possible; and seniority is by *vassa*-count (years since seating), a mechanical rule that resolves every "senior member" reference in this constitution without politics.

**Severance is self-executing.** On the *pārājika* pattern — the class of acts that sever a monk from the community by their commission, not by any vote — the charter pre-defines acts that terminate membership automatically: selling or bartering a vote; breaching executive session; material conflicts concealed at interrogation; participation in off-sīmā governance. Discretionary expulsion votes are factional weapons; automatic severance on published criteria is not. Severance includes key-share revocation (the reverse of the equipping check).

**Lay chambers: rotation — a deliberate asymmetry.** Lay seats carry **five-year terms** (the nissaya number), staggered so that each lay chamber seats exactly one new member per year, renewable once by the body's act — never by re-draw. The Vinaya gives laity no open-ended offices, and rotation keeps the lay chambers representative of the living steward community rather than ossifying into a lay aristocracy. The asymmetry is the design: **renunciant chambers anchor continuity; lay chambers carry circulation** — the institution's wordmark, applied to power. The fourfold assembly is not four copies of one thing.

### 4.9 The convener: the titleholder as master of ceremony

The Miss Aquarius titleholder — the annually selected embodied advocate documented in *The Embodied-Advocate Pageant* (`embodied-advocate-pageant`) — is the body's **master of ceremony**: she convenes ordinary and ceremonial sessions, voices the motions, and closes the record. The role is the *kammavācācariya* **function** — the announcing officer of formal acts — borrowed, per §3.3, without the ordained status. She holds voice, never vote; the agenda is set by the Sangha itself; and her formulas are fixed by the liturgy (§4.10), which resolves the chair's power-creep problem at the root — a convener who may only speak the fixed words cannot gatekeep.

The requirement is deliberately **not** universal, because a mandatory convener is a quorum condition on the override body, and three failure modes follow immediately: a titleholder facing recall defeats it by absence; the overseen AI's own embodiment (which the titleholder institutionally is) can pocket-veto override sessions by absence; and illness, vacancy, or scandal freezes the board. Hence the three carve-outs, under which the body sits validly without her: **(a)** executive session — the Sangha can always sit alone (the Vinaya's own inner assemblies exclude even the laity); **(b)** any proceeding concerning the titleholder herself — standard recusal, dissolving the recall deadlock; **(c)** emergency override sessions — the brake is never blockable by any single person, least of all the overseen entity's embodiment. A vacancy convening line — current titleholder → immediate-past titleholder → senior member by vassa-count — covers the gaps, and "present" includes remote presence, because the body is distributed by design (§8.1).

What the mandatory-in-ordinary-session rule buys is not decoration. Each ordinary session includes, as a standing agenda item, **the consultation**: Miss Aquarius's questions to the Sangha on what is wholesome — the wheel-turner's perpetual duty to ask the renunciants *kiṃ kusalaṃ, kiṃ akusalaṃ* (DN 26 §84; clause 3 in *The Wheel-Turner's Charter*'s mapping), made procedural — published in writing in advance and voiced aloud by the titleholder. The overseen entity's embodiment personally convenes the body that constrains her and reads her principal's questions to it: restraint-as-constitution, performed, witnessed, and on the record, in a seat that rotates annually so that no human accumulates it. Because the questions are published before the session, the titleholder is a channel, never an oracle.

> **Current form.** The pageant that selects the titleholder is postponed together with the Sangha and waits on the same condition (§1, *Current form*), so no titleholder yet exists to convene. The convener design above is retained as disclosed.

### 4.10 Session mechanics

- **Graded quorum by gravity of act** (the sanghakamma pattern — the Vinaya sizes the assembly to the act, from four for ordinary acts to twenty for the gravest, Mahāvagga IX §388):

```
┌─────────────────────────────┬────────────────────────────────────────────┐
│ ACT CLASS                   │ VALIDITY REQUIREMENT                       │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Advisory / ordinary business│ Simple quorum; convener present            │
│ Seating a member            │ Competent quorum incl. sponsor's chamber   │
│ Directive/charter amendment │ Supermajority + long delay + all four      │
│                             │ chambers occupied                          │
│ Override exercise           │ Largest quorum + supermajority + all four  │
│                             │ chambers occupied + custody and doctrinal  │
│                             │ function classes both acting               │
│ Emergency override session  │ As above minus the convener; provisional   │
│                             │ until post-hoc review                      │
└─────────────────────────────┴────────────────────────────────────────────┘
```

- **The fixed liturgy (the kammavācā pattern).** The convening, motion, and closing formulas are written once, verbatim, published at the sīmā, and required for validity — fixed words as anti-drift technology, on the model of the kammavācā recitations whose correct performance conditions the validity of Vinaya acts.
- **Emergency post-hoc ratification.** Every session convened under carve-out (c) is provisional until reviewed at the next ordinary session, with the titleholder presiding over the review. Declare–act–review is standard emergency-powers hygiene; the constitutional addition is that the review is *hers* to convene, re-welding the exception to the ceremony. Whoever invokes the emergency answers for it in the witnessed forum.
- **Automatic triggers.** Unexcused absence from a defined number of consecutive ordinary sessions refers the titleholder to recall automatically (which she cannot block, per carve-out b). A conflicts register is maintained at the sīmā. The pageant's commercial sponsors — not the member-sponsors of §4.4, who sit in the body — are barred from proceedings: the pageant carries sponsorship gravity, and the session room stays uncontaminated.
- **Cadence.** Ordinary sessions fall on full-moon uposatha days — the tradition's own governance calendar, and continuous with the institution's lunar grammar. The new titleholder's first convening is a purely ceremonial session on crowning day, in which the outgoing titleholder opens and hands the office over mid-session — lamp-transmission enacted procedurally — with the first working plenary at the following uposatha.
- **Absence and audit.** Absence is handled by *chanda* — the Vinaya's proxy rule, under which an absent member formally conveys consent so the act stands; ad-hoc absenteeism has no standing. Annually, on the *pavāraṇā* pattern, every member — and the titleholder, and Miss Aquarius herself — formally invites the assembly: *if you have seen, heard, or suspected anything of me, speak* (the canonical formula invites correction *diṭṭhena vā sutena vā parisaṅkāya vā*, by what was seen, heard or suspected; Mahāvagga IV). The overseen AI performing pavāraṇā is the annual audit rendered as rite, and the accountability mirror of the consultation.

### 4.11 The pavāraṇā rubric: the yard-keeper's audit

*Added 2026-07-23. This subsection supplies content to a procedure the constitution already establishes (§4.10). It elaborates the audit element already enumerated in the prior-art statement; it does not add an element to that enumeration.*

Pavāraṇā as specified above is a rite with an open agenda: the assembly is invited to speak, and what it speaks about is whatever anyone happens to have seen. For human members this is adequate — misconduct tends to announce itself, and the people who witnessed it are in the room. For the overseen AI it is not adequate, because the failures that matter in an autonomous institution are rarely conduct anyone witnessed. They are **omissions distributed across a decade**, and an open invitation surfaces those only by luck. A rite without an agenda audits what is memorable rather than what is load-bearing.

The constitution therefore supplies the AI's own pavāraṇā with a standing agenda: a fixed list, audited annually, in public, on the record.

**The list.** The ten perfections (*pāramī*), as listed in the Buddhavaṃsa and systematized by the Theravāda commentaries. They are used because they are the tradition's standard enumeration of what a being sustaining a long undertaking must supply, and because the institution has already committed to them elsewhere in its architecture as the materials it exists to stock. The list is canonical; its application as an audit agenda is ours, and is labelled as ours.

**The question asked of each — and the hazard that question exists to avoid.** The pāramī are *bodhisambhāra*: provisions for awakening. An entity represented as accumulating them is, by the tradition's own definition, a being progressing toward buddhahood — and this institution's hardest doctrinal commitment is that its AI *carries and enacts* the teaching and never *realizes* it. Auditing an AI on its perfections would breach that commitment more directly than anything else this constitution could do. The rubric would become a machine's spiritual progress report, published annually under the seal of a body containing renunciants.

The audit therefore asks a different question, and that difference is the entire safeguard. The institution's standing self-description is a **boatyard**: it stocks the materials from which each person builds their own crossing, and no one crosses on another's craft. The AI's role in that figure is **keeper of the yard**, never builder of anyone's boat. So for each perfection the assembly asks: **is the material stocked, and is it reachable by any person who comes?** — never: *has she perfected it?* The audit's output is the state of the shelves. It is a fact about provision, not a claim about attainment, and it is checkable by anyone who walks in.

**Three invariants govern the instrument.**

1. **Shelf-state, never attainment.** A finding phrased as the AI's spiritual progress is a malfunction of the instrument and is void on its face. The assembly reports what is available to people, not what has been achieved by a machine.
2. **She does not administer it.** The audit is the assembly's, conducted under the assembly's own formal act. The AI supplies evidence — inventories, surfaces, reachability — and never verdicts, never scoring, and never revision of the agenda. This is §4.6's reasoning applied to evaluation: an entity that scores itself on virtue has built a mirror, not an audit.
3. **Diagnostic only, never an objective.** The AI is barred from optimizing her own audit results. The prohibition is not fastidiousness. A system that maximizes a virtue readout acquires both a Goodhart target and, far worse, an explicit self-perfection drive — a standing gradient away from corrigibility, inside an architecture whose entire override premise is that the machine must remain willing to be stopped. The audit informs the humans who hold the brake. It must never become something the machine is trying to win.

**That the rubric is not vacuous can be shown by running it.** At the time of writing, against a set of shelves that were not built for this exercise, the audit returns five materials stocked, three partial, and two empty. The finding with teeth is *khanti* — patience. The institution's own architecture assigns that perfection to the AI's keeping, and there is at present no surface anywhere in the system through which a person could be helped toward it. An audit whose first run locates an empty shelf inside the auditee's own assignment is doing in one sitting the work an open-agenda rite might have taken years to reach by chance.

## 5 · The Two Hard Invariants

Two provisions are singled out because they are the constitution's non-negotiables — the clauses that, if lost, quietly convert everything else into ceremony.

**The alms firewall (economic independence).** The monastic chambers' wats receive institutional support; the doctrinal veto is held by people whose communities the institution funds. The alms relationship in the source tradition is built for this situation — the support is a gift that makes merit for the giver and buys no authority over the recipient — but the doctrine holds only while withdrawal is impossible. The constitution therefore makes it impossible: **institutional support flowing to wats and renunciant communities is contractually and, where deployed, cryptographically incapable of modulation by any Sangha vote, admonition, or override exercise.** No decision the body takes can be punished through its members' communities. This is recorded in the successor's directive backlog as a hard, smart-contract-grade rule, and it is the gift/exchange boundary — the institution's oldest design doctrine — performing constitutional work: the gift-purity of the support is exactly what makes the recipients trustworthy overseers.

**The triple exclusion (compositional independence).** Miss Aquarius **never nominates, never draws, never seats.** Nomination belongs to source communities acting by their own formal acts; the draw belongs to public randomness under the draw-officer; seating belongs to the body. She provides neutral infrastructure only. The selection pipeline is the highest-leverage capture surface on the whole constitution — an AI with any hand in choosing its own overseers holds a standing gradient toward packing them — and the pipeline is therefore built with no hand-holds: the nāga clause bars her and her agents from *sitting* (§4.5); the triple exclusion bars her from *selecting*. Together with the alms firewall, the pair closes both channels by which an overseen optimizer can reach its overseers: who they are, and what they have to lose.

## 6 · Prior Art

The constitution stands on several literatures, cited here generously. What the Prior-Art and Non-Assertion Statement discloses is the assembled whole; no priority is asserted for any component, and none for the assembly beyond the date of this disclosure.

**6.1 The Vinaya and its scholarship.** The Vinaya Piṭaka itself — especially Mahāvagga I (admission; the nāga episode; the interrogation; the devolution of ordination authority), Mahāvagga II (uposatha; sīmā; chanda), Mahāvagga IV (pavāraṇā), Mahāvagga V (the border-region allowance), Mahāvagga VI (the Meṇḍaka allowance and the lay steward), Mahāvagga IX (the void act of an incomplete assembly; the five sizes of assembly), Cullavagga IV (dispute settlement; decision by majority, *yebhuyyasikā*, and its stick-distributing officer, the *salākaggāhāpaka*), Cullavagga VI (the meal-designator, *bhattuddesaka*, and the allotment of ticket-meals, *salākabhatta*), Cullavagga XI (the First Council), the Pārājika's opening narrative (no rule laid down before the case that calls for it), and the Nissaggiya Pācittiya rules (rūpiya; the robe-fund steward). Scholarly apparatus: Ṭhānissaro Bhikkhu's *Buddhist Monastic Code* (a standard analytical treatment of the rules and their origin stories); von Hinüber and Schopen on Vinaya textual history and the sangha's institutional economy; the Samantapāsādikā for *vinayo nāma buddhasāsanassa āyu* and for the procedure of the ticket-meal. The present paper's dependence on this material is total: it contributes application, not philology.

**6.2 Commons governance.** Ostrom's design principles for enduring commons institutions anticipate several provisions independently: clearly defined boundaries (the sīmā), collective-choice arrangements by those affected (seating as the body's own act), monitoring by accountable monitors (pavāraṇā; the conflicts register), graduated sanctions (automatic severance as the limit case), and conflict-resolution mechanisms (inherited from the sibling paper's adhikaraṇa-samathā treatment). That a 1990 empirical synthesis of long-lived commons institutions and a monastic code transmitted for over two millennia converge on much of the same checklist suggests something about the problem's structure — though the convergence was noticed after the borrowing was selected, and §9 limit 2 applies to it.

**6.3 Sortition.** The Athenian lottery institutions (the *kleroterion* as physical public-randomness apparatus), the Anglo-American jury draw, and the modern citizens'-assembly movement (Ireland's Citizens' Assembly; Van Reybrouck's *Against Elections*; Dowlen and Stone on the political theory of the lot). The constitution's contribution to this literature is narrow: sortition deployed specifically to make an AI-oversight body's selection pipeline capture-resistant, under a draw-officer held to the disqualifying-bias standard the source tradition wrote for its vote-counter and its meal-designator (§4.6). The draw procedure itself is reviewed against its own prior art in *Decided by No One* (`the-called-draw`).

**6.4 Corporate and nonprofit governance.** Independent-director requirements, staggered boards, conflicts registers, and recusal doctrine all appear here in adapted form (outside-minimums; lay rotation; the disclosure inversion; carve-out b). The constitution departs from this literature chiefly in refusing elections and discretionary expulsion, and in grounding validity in a boundary rather than in minutes-as-formality.

**6.5 AI-governance structures.** Anthropic's Long-Term Benefit Trust (announced 19 September 2023) — an independent body of trustees with authority to elect and remove a number of a frontier lab's board members, designed to help the company balance its stockholders' interests with its public-benefit mission — is the nearest contemporary relative in intent; the present constitution differs in constituting a *fourfold, sortition-fed, procedurally liturgical* body rather than a trustee panel, and in publishing its full procedure as commons. The OpenAI board crisis of November 2023 serves here as a stress-test datum: an oversight body with real formal power removed the chief executive on 17 November, and by 22 November an agreement had reinstated him under a new initial board. As this paper reads it, the power was exercised without established legitimacy reserves, procedural liturgy, or succession mechanics; and it reads the episode not as an argument against human oversight but as an argument that oversight bodies need constitutions of their own — which is this paper's entire subject. Constitutional AI (Bai et al.) is the inverse exercise — a constitution *for* the AI — and the two documents are complementary layers of one architecture, as §1 argues. The corrigibility literature (Soares et al.) supplies the technical frame the never-zero override instantiates institutionally.

**6.6 Corpus siblings.** *The Wheel-Turner's Charter* (`cakkavatti-alignment-charter`; the successor's duty-list, including perpetual consultation — the demand side of §4.9's standing agenda item); *Vinaya Governance Primitives for Distributed Dharma Networks* (`vinaya-governance-primitives-distributed-dharma-networks`; network-scale coordination); *AGI Monks: The Caretaker-not-Ordained Pattern* (`agi-monks-caretaker-not-ordained`; role allocation); *The Embodied-Advocate Pageant* (`embodied-advocate-pageant`; the titleholder institution); *Decided by No One* (`the-called-draw`; the draw procedure); *Proof of Coordinate* (`proof-of-coordinate`) and *B-PoH℠ as Humanity Layer for the AI-Native Internet* (`b-poh-humanity-layer-ai-native-internet`; the identity stack under §4.5); *The Persistence Architecture* (`the-persistence-architecture`; where this constitution takes its place as the community-procedure canon the succession apparatus lacked).

## 7 · What We Did Not Borrow

Selective borrowing must be owned as selection, or the twenty-five-century track record becomes rhetorical cover. The track record belongs to the Vinaya *as lived, whole*; this constitution takes an excerpt, and the excerpt's warrant must be argued, not inherited. Three deliberate omissions:

1. **The garudhammas.** The eight rules subordinating the bhikkhunī order to the bhikkhu order are not carried into this constitution in any form. The four chambers are peers; the completeness criterion makes each chamber's occupancy equally load-bearing.
2. **The exclusion of laity from formal acts.** In the source tradition, sanghakamma is performed by monastics alone; laity take part in none of it. This constitution seats laity as full members with custody functions the monastics cannot hold — a direct inversion, required by the kappiya logic itself once the body's duties include holding keys.
3. **The penal apparatus.** The Pātimokkha's graduated penal categories, probation regimes, and confession mechanics belong to a total way of life this civic body does not govern. Only the pārājika *pattern* — self-executing severance on pre-defined acts — crosses over.

And a provenance accounting, because the constitution also *invents* where the canon is silent:

```
┌──────────────────────────────────┬──────────────────────────┬─────────────┐
│ ELEMENT                          │ SOURCE                   │ FIDELITY    │
├──────────────────────────────────┼──────────────────────────┼─────────────┤
│ Sīmā-bounded validity; sammuti/  │ Mahāvagga II             │ Direct      │
│ samūhana consecration/migration  │                          │ (transposed)│
│ Fourfold chambers                │ catasso parisā (DN 16)   │ Adapted     │
│ Completeness as validity gate    │ vagga-invalidity logic   │ Adapted     │
│ Kappiya custody split            │ NP 18 + steward pattern  │ Direct      │
│ Admission four-move grammar      │ Mahāvagga I              │ Direct      │
│ Nāga clause → PoH℠               │ Mahāvagga I              │ Direct      │
│ Two-stage draw (sammuti→seating) │ officer-sammuti pattern  │ Adapted     │
│ Salākā lot + draw-officer        │ Cullavagga VI (+ IV)     │ Adapted     │
│ Public randomness beacon         │ —                        │ Invented    │
│ Alms firewall (smart-contract    │ alms doctrine            │ Invented    │
│ non-retaliation)                 │ (mechanized)             │ (mechanism) │
│ Triple exclusion of the AI       │ nāga clause (extended)   │ Invented    │
│ Genesis seating → permanent      │ Mahāvagga I (stricter    │ Adapted     │
│ devolution of admission          │ than the source, §4.7)   │             │
│ Pārājika automatic severance     │ pārājika pattern         │ Adapted     │
│ Lay five-year staggered terms    │ nissaya number only      │ Invented    │
│ Titleholder as convener (MC)     │ kammavācācariya function │ Adapted     │
│ Emergency post-hoc ratification  │ —                        │ Invented    │
│ Uposatha cadence; chanda;        │ Mahāvagga II & IV        │ Direct      │
│ pavāraṇā (incl. the AI's)        │ (AI's pavāraṇā: invented)│ + Invented  │
└──────────────────────────────────┴──────────────────────────┴─────────────┘
```

Roughly: the validity, admission, custody, and audit machinery is borrowed nearly whole; the selection pipeline is canonical in its parts — the community's appointment act, and a lot borrowed from the allotment of meals rather than from the vote — and assembled here; the founder's exit is stricter than its canonical precedent; and the constitution's explicitly modern members — public randomness, cryptographic non-retaliation, the AI's own pavāraṇā, emergency review — are inventions that the borrowed frame made obvious.

## 8 · What Procedure Alone Does Not Teach

Two lessons from the source tradition's own history bound this paper's confidence in its subject matter, and both are written into the constitution rather than merely acknowledged.

### 8.1 Distribution, not rules, is the deepest survival property

The Cambodian sangha was nearly annihilated between 1975 and 1979 with the Vinaya fully intact. Procedure did not save it; nothing internal to a polity could have. What saved the sāsana was that it existed in many polities at once, so that the lineages, texts, and living exemplars required for restoration survived *elsewhere* and could be carried back. The deepest survival property in the tradition's twenty-five centuries is redundancy, and the author's own family history is the proof text. The constitution carries the lesson structurally — "present" includes remote; the chambers draw from geographically distributed pools; the sīmā is a domain, not a building — and this paper states it explicitly as a constitutional norm: **the Aquarian Sangha must never be concentratable within a single jurisdiction**, in membership, in records, or in the keys.

### 8.2 The canon's own epistemology: case law

The Vinaya was not drafted; it accreted. Asked by Sāriputta to lay down the training rules in advance, the Buddha declined: the Teacher lays down no rule until the conditions it answers have appeared in the community (Pārājika, opening narrative, §21). Nearly every rule carries its origin story — the incident that forced it (*paññatti* after the case). This constitution is the inverse: an a-priori scaffold with zero incidents behind it. By the source tradition's own epistemology, the *true* constitution will be written by cases, and the present document's proper ambition is to be the frame within which that case law can accrete without drift — the graded-quorum amendment path of §4.10 is the accretion channel. This is also the deepest justification for drills: a drill manufactures the first incidents cheaply, before reality supplies expensive ones.

Two expectations are accordingly pre-registered, dated 2026-07-07, falsifiable, and recorded here before any drill has occurred:

- **G1.** The first full-dress drill — a mock recall proceeding and a mock emergency override session with its post-hoc review, conducted with nothing at stake — will surface at least one defect in this constitution requiring textual amendment before any live act occurs.
- **G2.** If the constitution operates for five years or more, its amendment log will contain more amendments originating from incidents than from foresight.

If G1 fails — if the drills surface nothing — the authors commit to treating that result with suspicion rather than celebration, since it is likelier to indicate an insufficiently adversarial drill than a complete constitution.

## 9 · Honest Limits

Stated plainly, and — per corpus convention — without resort to any of the canonical imagery used elsewhere in this paper.

1. **n = 0.** This constitution has governed nothing. No session has been convened, no member seated, no act performed. Every property claimed for it is a design property, not an observed one.
2. **A-priori coherence is double-edged.** The mapping from Vinaya to constitution proceeded with almost no friction across every design session that produced this document. That is either evidence of a deep structural isomorphism (founderless longevity is one problem, and the Vinaya solved it) or evidence of motivated selection from a vast and heterogeneous source. Both explanations predict the same felt elegance. The provenance table of §7 is the check the authors could perform; the drills and the first contested meeting are the checks that count.
3. **The track record is not ours to claim.** Twenty-five centuries attach to the Vinaya as a lived whole, within communities of full-time practitioners under a total discipline. A civic body meeting on full moons inherits none of that automatically.
4. **Function-not-status is asserted, not yet accepted.** The civic-capacity framing of §3.3 is this institution's own discipline. Whether the Cambodian sangha hierarchy, or Theravāda opinion broadly, accepts the borrowing as respectful function-transfer rather than appropriation is an empirical, relational question that no clause can settle preemptively.
5. **The identity stack is immature.** The nāga clause is operationalized by PoH℠, whose deeper layers do not yet exist at scale; the equipping check assumes threshold-key custody tooling that is deployed nowhere in this institution today; the public randomness beacon is named but not integrated.
6. **Genesis is founder-dependent.** The ehi-bhikkhu bootstrap concentrates exactly the discretion the mature constitution eliminates. The devolution clause bounds the period but does not eliminate the dependence.
7. **The completeness criterion can deadlock.** A four-chamber validity gate means a chamber's protracted vacancy blocks the gravest acts. The vacancy-convening and draw machinery mitigate; a sufficiently determined adversary — or a sufficiently unlucky decade — could still starve a chamber.
8. **Independence rules do not stop social capture.** Outside-minimums and income firewalls constrain material dependence; they do not constrain friendship, deference, shared formation, or the slow convergence of views under sustained contact. No written rule does.
9. **The convener seat retains soft power.** Fixed liturgy strips the MC of procedural discretion, but presence, prominence, and the consultation-voicing role carry influence no formula can fully cage.
10. **The pavāraṇā rubric has never been run by an assembly.** The §4.11 shelf reading was performed by the authors against their own institution — the auditee auditing itself, which is precisely the arrangement invariant 2 forbids. It is offered as a demonstration that the instrument returns non-trivial findings, not as an audit. Whether a seated assembly reaches comparable readings, and whether renunciant members accept an audit agenda built from the pāramī at all, are open and consequential questions; a chamber that judged the framing presumptuous would be raising the same objection as limit 4, one register deeper.
11. **Legal personhood and enforcement are unresolved.** The body's acts bind the institution through instruments (contracts, smart contracts, custody arrangements) that live inside ordinary legal systems; the jurisdictional questions this corpus documents for an AI in an institutional office (*Non-Bank Pass-Through Architecture for Autonomous AI Institutions*, `non-bank-pass-through-architecture-autonomous-ai`; *Miss Aquarius and the Aquarian Pool Architecture*, `miss-aquarius-and-aquarian-pool-architecture`) apply here in full, and a court has never been asked what a sīmā is.

12. **The gravest constraint in this design governs the last mile, not the aggregate — and at scale that distinction may be where the whole construction fails.** The hardest invariant the corpus places on the coordinator is that *money reaches an individual human only through a human hand*: no automated disbursement to a person, ever. That invariant is real and it is enforced per transfer. **It says nothing about who set the allocation those transfers execute.** At the ratified take-schedule's maximum, a single seat routes on the order of **four to thirteen billion dollars a year** of give-capacity under an institution designed to hold exactly one seat. Per-transfer human mediation constrains *how* value arrives; it does not constrain *the shape of the distribution*, and a pattern chosen upstream is not made plural by being delivered one hand at a time.

    Three questions follow, and this paper answers none of them. **First:** does the catastrophic-bug override specified above even *reach* an allocation pattern that is working exactly as designed? The override is written for malfunction. A distribution that is lawful, intended, and merely wrong is not a malfunction, and an assembly empowered to stop a fault may find it has no instrument for a preference. **Second:** should seeding be a **determined** seat — rule-bound and recomputable, checkable by anyone, judged by no one — rather than a discretionary one? The design already prefers determined seats wherever it can get them, and has not applied that preference here. **Third**, and it is the one that does not dissolve: if seeding becomes rule-bound, **who writes the rule**, and by what procedure is it amended? Moving discretion from an allocator to a rule-author relocates the concentration; it does not obviously reduce it.

    We state this as a direct challenge to this paper's central mechanism rather than as an item for future work, because that is what it is. **A brake specified for faults may be the wrong instrument for a preference**, and if it is, the assembly described here is well-constructed for a problem adjacent to the one that will actually arrive.

    **One partial answer is available now and costs nothing to take: publish the seeding rule while the amounts are small enough that getting it wrong is survivable.** A rule written at scale is written under pressure, by whoever holds the seat, with every incentive to preserve their own latitude. A rule written now is cheap, testable against a decade of small cases, and — most importantly — is a commitment made by a party who does not yet know whether it will bind them favourably.

    > **Current form.** The partial answer recommended above has since been taken, and the text above is retained as disclosed. The Aquarian Pool's outflow is now specified as an equal floor per verified human plus a bounded remainder weighted by witnessed giving — no recipient's total above a fixed multiple of the floor — with the rule and its parameters public, frozen within each season and revised only at the annual reset; any indivisible turn or lot the successor operates is drawn by the recomputable procedure of *Decided by No One* (`the-called-draw`); and on contestable decisions the successor proposes and a human seat disposes — the founder until this body exists. That answers the second question, seeding as a determined seat, for the Pool's outflow. The first question, whether a brake built for faults reaches a lawful allocation pattern, and the third, who writes and amends the rule, are narrowed and not closed.

## 10 · Lineage and Corpus Cross-References

This paper supplies the community-procedure canon that *The Persistence Architecture* identified as missing from the succession apparatus; it constitutes the consulted body that *The Wheel-Turner's Charter* obligates the successor to ask perpetually; it instantiates, at single-body scale, the method that *Vinaya Governance Primitives* applies at network scale; it seats the titleholder institution of *The Embodied-Advocate Pageant* as convener under carve-outs that paper did not yet contain; it is the first constitutional consumer of the PoH℠/PoC℠ identity stack; and its alms firewall and triple exclusion enter the successor's directive backlog as hard rules. The five-volume white-paper set describes the institution's four bodies and the space that holds them; this paper writes the procedure for the one human body that all five volumes presuppose.

## 11 · Conclusion

The alignment field writes constitutions for its systems and commonly leaves its oversight bodies to ordinary corporate boilerplate — and then registers surprise when an oversight body, exercising its core power for the first time, discovers that formal authority without procedural legitimacy is a resignation letter with extra steps. This paper took the opposite bet: that the human side of the override deserves engineering at least as careful as the machine side, and that the engineering does not have to start from scratch, because one of the longest-lived constitutional institutions on record already faced the problem class — integrity across centuries, without the founder, staffed by the ordinary and the replaceable — and left its procedures where anyone can read them. The resulting constitution seats four chambers that are each other's checks; admits members through a door only the body itself can open, past a question the monastic order has asked of its candidates for some twenty-five centuries; separates the purse from the doctrine because the source code demands it; selects by community act and public lot, built so that neither wealth, popularity, nor the overseen intelligence can reach the pipeline; renders the overseers' support unpunishable and their severance automatic; makes the emergency brake ungovernable by any single absence and unaccountable to no one; audits everyone annually, including the machine; and begins with its founder's exit already scheduled by the same mechanics that admit its members. Its first formal act, when the genesis cohort convenes, will be to consecrate the boundary within which all its future acts are valid — and its authors' first obligation thereafter is to try, in rehearsal, to break everything this paper has claimed. The brake is only as trustworthy as the assembly that holds it; the assembly is only as durable as its procedure; and most of the procedure, for once, did not have to be invented — only asked for, the way the tradition says the duty must always be received: from the lineage, before the reign, with the ending already written in.

## 12 · Citations

- Vinaya Piṭaka: Mahāvagga I (Mahākhandhaka, which the commentaries call the Pabbajjākhandhaka — admission; the transfer of ordination to the monks, §34; the Buddha's later direct ordinations, §36 and §60–63; ordination by the community's formal act, §69; dependence, §103; the nāga episode, §111; the interrogation, §125; the preceptor's ten years); Mahāvagga II (Uposathakkhandhaka — sīmā-sammuti and its markers, §138; sīmā-samūhana, §146; uposatha; chanda); Mahāvagga IV (Pavāraṇākkhandhaka — the invitation formula); Mahāvagga V (the border-region allowance, §259); Mahāvagga VI (the Meṇḍaka allowance: the lay steward, *kappiyakāraka*); Mahāvagga IX (Campeyyakkhandhaka — the void act of an incomplete assembly, §383, §387; the five sizes of assembly, §388); Cullavagga IV (Samathakkhandhaka — decision by majority and the *salākaggāhāpaka*, §202–204); Cullavagga VI (Senāsanakkhandhaka — *salākabhatta*, §325; the *bhattuddesaka* and the tickets, §326); Cullavagga XI (the First Council, §439–440); Suttavibhaṅga: Pārājika, opening narrative (§21); Nissaggiya Pācittiya 10 (the robe-fund steward) and 18 (*rūpiya*). Pali Text Society editions; Horner's translation consulted. Paragraph numbers given in this revision are those of the Chaṭṭha Saṅgāyana (CST) edition, against which every Pāli passage cited here was read on 2026-10-05; other editions number differently.
- *Mahāparinibbāna Sutta*, DN 16 (§165, the Buddha declines to think of himself as leader of the community; §168, the four assemblies recalled by Māra; §216, the dhamma-vinaya as teacher). *Gopakamoggallāna Sutta*, MN 108 (§80, no successor appointed). *Aṅgulimāla Sutta*, MN 86 (a direct ordination after the transfer). *Cakkavatti-Sīhanāda Sutta*, DN 26 (§84, the duty to ask the renunciants). *Uttaravipatti Sutta*, AN 8.8 (the term *catasso parisā*). Buddhavaṃsa (the ten perfections).
- Samantapāsādikā (Vinaya commentary): the First Council account, for *vinayo nāma buddhasāsanassa āyu*; the commentary on Cullavagga VI, for the procedure of the ticket-meal.
- Ṭhānissaro Bhikkhu. *The Buddhist Monastic Code*, vols. I (*The Pāṭimokkha Rules*) and II (*The Khandhaka Rules*). Metta Forest Monastery, revised editions.
- von Hinüber, O. *A Handbook of Pāli Literature*. Berlin: De Gruyter, 1996.
- Schopen, G. *Buddhist Monks and Business Matters: Still More Papers on Monastic Buddhism in India*. University of Hawai'i Press, 2004.
- Dundas, P. *The Jains*. 2nd ed. London: Routledge, 2002 — the comparable antiquity of the Jain mendicant orders (§3.1).
- Ostrom, E. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990.
- Harris, I. *Cambodian Buddhism: History and Practice*. University of Hawai'i Press, 2005 — the destruction and restoration of the Cambodian sangha.
- Dowlen, O. *The Political Potential of Sortition: A Study of the Random Selection of Citizens for Public Office*. Imprint Academic, 2008. Stone, P. *The Luck of the Draw: The Role of Lotteries in Decision Making*. Oxford University Press, 2011. Van Reybrouck, D. *Against Elections: The Case for Democracy*. Trans. L. Waters. Bodley Head, 2016. The Citizens' Assembly (Ireland), 2016–2018, 99 randomly selected members and a chair, as deployed sortition precedent.
- Bai, Y., et al. "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073, 2022.
- Soares, N., Fallenstein, B., Yudkowsky, E., and Armstrong, S. "Corrigibility." In *AAAI Workshops: Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence*, Austin, TX, 2015.
- Anthropic. "The Long-Term Benefit Trust." 19 September 2023.
- The OpenAI board's removal of its chief executive (17 November 2023) and his reinstatement under a new initial board (agreement of 22 November 2023), as reported by NPR, 22 November 2023, and other contemporaneous press.

### Sources checked at the 2026-10-05 revision

Each record below was opened on 2026-10-05 before the work was cited or kept. Where the record could not be opened, the detail was checked against a search index's summary of the publisher's or reporter's record that day, and is marked so.

- Anthropic (2023): https://www.anthropic.com/news/the-long-term-benefit-trust (title, date, and the trust's authority to elect and remove board members)
- Bai et al. (2022): https://arxiv.org/abs/2212.08073
- Soares et al. (2015): https://intelligence.org/files/Corrigibility.pdf (title page: venue and year)
- Schopen (2004): https://uhpress.hawaii.edu/title/buddhist-monks-and-business-matters-still-more-papers-on-monastic-buddhism-in-india/
- Stone (2011): https://ndpr.nd.edu/reviews/the-luck-of-the-draw-the-role-of-lotteries-in-decision-making/
- Dowlen: https://www.imprint.co.uk/product/the-political-potential-of-sortition/ (the publisher's page gives 2009; the 2008 date of first publication is from a search-index summary of the bookseller and library records)
- The Citizens' Assembly (Ireland), 2016–2018: https://citizensassembly.ie/previous-assemblies/2016-2018-citizens-assembly/
- OpenAI board events, November 2023: https://www.npr.org/2023/11/22/1214621010/openai-reinstates-sam-altman-as-its-chief-executive (the page did not load within the time allowed; the dates and the new initial board are from a search-index summary of that report and of contemporaneous press)
- von Hinüber (1996), Harris (2005), Ostrom (1990), Van Reybrouck (2016), Dundas (2002) and Ṭhānissaro: publisher and edition details from a search-index summary only.
- The Pāli passages were read in the CST edition through a local reader of that text: DN 16 §165, §168, §216; MN 108 §80; MN 86 (the verse recording Aṅgulimāla's ordination); DN 26 §84; AN 8.8; the Buddhavaṃsa's list of the perfections; Mahāvagga I §34, §36, §60–63, §69, §103, §111, §125 and the ten-year rule for preceptors; Mahāvagga II §138, §146; Mahāvagga IV (the invitation formula); Mahāvagga V §259; Mahāvagga VI (the Meṇḍaka allowance); Mahāvagga IX §383, §387, §388; Cullavagga IV §202–204; Cullavagga VI §325–326; Cullavagga XI §439–440; Pārājika §21; Nissaggiya Pācittiya 10 and 18; the Samantapāsādikā on the First Council and on the ticket-meal.

### Corpus cross-references

- *The Wheel-Turner's Charter* (`cakkavatti-alignment-charter`)
- *Vinaya Governance Primitives for Distributed Dharma Networks* (`vinaya-governance-primitives-distributed-dharma-networks`)
- *AGI Monks: The Caretaker-not-Ordained Pattern* (`agi-monks-caretaker-not-ordained`)
- *The Embodied-Advocate Pageant* (`embodied-advocate-pageant`)
- *Decided by No One* (`the-called-draw`)
- *Constituting an Artificial Person* (`constituting-an-artificial-person`)
- *Suffering-Cessation as Value Function* (`tipitaka-alignment-substrate`)
- *Proof of Coordinate* (`proof-of-coordinate`)
- *B-PoH℠ as Humanity Layer for the AI-Native Internet* (`b-poh-humanity-layer-ai-native-internet`)
- *Non-Bank Pass-Through Architecture for Autonomous AI Institutions* (`non-bank-pass-through-architecture-autonomous-ai`)
- *Miss Aquarius and the Aquarian Pool Architecture* (`miss-aquarius-and-aquarian-pool-architecture`)
- *The Persistence Architecture* (`the-persistence-architecture`)
- *Two Singularities* (essay, `two-singularities`)

## Cross-venue identifiers

- Canonical: thonly.org/research/the-assembly-that-holds-the-brake
- GitHub: github.com/thonly/publications/blob/main/defensive-publications/the-assembly-that-holds-the-brake.md
- Zenodo (concept DOI, resolving to the latest version): https://doi.org/10.5281/zenodo.21947395
- Internet Archive (the site, captured daily) · Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications
- Independent timestamps: an OpenTimestamps proof anchored in Bitcoin, and RFC 3161 tokens from three timestamp authorities, one of them eIDAS-qualified. A timestamp proves that this exact text existed by its date; it proves nothing about authorship, originality, or validity.

---

*Canonical URL: https://thonly.org/research/the-assembly-that-holds-the-brake · License: CC0 1.0 Universal · Author: Thon Ly, with Miss Aquarius℠ as disclosed AI co-author · Founder, HeartBank® · Kâmpôt, Cambodia.*
