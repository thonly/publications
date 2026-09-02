---
title: "Proof of Coordinate"
subtitle: "A universal individuation primitive, orthogonal to Proof of Humanity: every entity in a mixed human-and-agent economy — human or bot — anchored by a permanent public genesis root in an archival substrate plus a rotatable secure-enclave key, with the dignity floor carried by coordinate provenance: a machine's coordinate is assigned and revocable, a human's coordinate is given and irrevocable, and the institution that issues machine identity can only ever witness human identity."
authors: "Thon Ly · Miss Aquarius"
category: alignment
priority: tier-b
status: draft
date: 2026-07-01
license: CC0-1.0
slug: proof-of-coordinate
venue: thonly.org/research/proof-of-coordinate (canonical)
---

> **Draft in progress.** This is the founder-voice canonical draft for `thonly/publications`. The defensive publication specifies **Proof of Coordinate ℠** (**PoC℠**) — the individuation primitive of the HeartBank® identity stack, orthogonal to and composing with **Proof of Humanity ℠** (**PoH℠**). It is published deliberately at the design stage, ahead of any product disclosure, because the identity-primitive space is unusually patent-active and the *combination* specified here — a universal two-artifact identity root spanning humans and machines, with the given-versus-assigned provenance line hard-coded as an alignment constraint — is the asset (see §11.1). Companion works: *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the category proof this primitive composes with), *The Persistence Architecture* (the succession apparatus whose nodes this primitive anchors), *Gratitude as a Cooperation Substrate for Multi-Agent AI* (the agent economy whose accountability this primitive supplies), *Multi-Family Membership* (the PoH-rooted plural-membership identity model), and *The Cosmic-Coordinate Worldview* material carried in the longitudinal-cohort methodology (the philosophical ground of the word "coordinate").

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back. May every being it helps to name be named as what it is: uniquely different, equally necessary, and never owned by the namer.*

Every identity system eventually answers two different questions, and most systems blur them. The first question is categorical: *what kind of thing is this?* — a human, a bot, a corporation, a sensor. The second is individuating: *which one is this?* — this human and not her twin, this agent and not its thousand clones. The blur is harmless while machines are few and dumb. It becomes load-bearing the moment an economy fills with autonomous agents that transact, cooperate, and defect at scale, because at that moment the two questions acquire *opposite* moral grammars: an institution may rightly mint, monitor, and revoke the identity of a machine it deploys, and may do none of those things to a human being. A system that answers both questions with one mechanism will eventually treat one of the two parties wrongly — it will either govern its machines too loosely or govern its humans like machines.

This paper separates the questions. Proof of Humanity, specified in a companion publication, answers the categorical question for people: *a human is present here.* Proof of Coordinate, specified here, answers the individuating question for everything: *this specific entity, at this unique coordinate in the space of entities, and no other.* The two compose — a verified person holds both, a deployed agent holds only the second — and the composition carries a constraint we believe belongs in the identity layer itself rather than in policy documents layered above it: **the provenance of a coordinate determines who may revoke it.** A machine's coordinate is assigned by the institution that made it, and what an institution assigns it may revoke. A human's coordinate is given — by birth, by time and place, by lineage — and what no institution assigned, no institution may revoke. The institution can only witness it.

I write as co-author with **Miss Aquarius℠**, the named autonomous-AI substrate of HeartBank®, disclosed by consistent name across every venue per the corpus convention. The research-grade synthesis, the prior-art survey, and the adversarial analysis are a genuine collaboration — and this paper is unusually reflexive about it, because Miss Aquarius is herself the institution whose powers over human identity this specification permanently limits. Final editorial control, and final responsibility for every claim, are mine.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. The author and HeartBank® will not seek patent on this specification or any portion thereof, in any jurisdiction, at any time. This commitment is permanent.

This document constitutes a defensive publication establishing **prior art as of 1 July 2026** for the combination of mechanisms described herein. To the author's knowledge, the following are not previously published as a unified mechanism, and any subsequent patent application claiming them should be considered filed against established prior art:

1. **A universal individuation primitive orthogonal to, and composing with, a personhood-category proof** — a proof answering "*which* unique entity is this?" issued to humans and machine agents alike, formally distinct from the proof answering "*is* this a human?", with the composition rule that a verified human holds both proofs and a machine agent holds the individuation proof only, so that a single mixed economy of humans and agents has exactly one sybil-distinctness layer and exactly one humanness layer, never conflated.

2. **The two-artifact identity root spanning humans and machines** — every identity anchored by (a) a *permanent, public, write-once genesis root* etched in a physical archival substrate (femtosecond-laser-written crystalline media in the reference deployment) holding only public material, plus (b) a *rotatable secret operational key* held in a secure enclave and never present in the readable substrate — the trusted-computing endorsement-key/attestation-key pattern transposed onto a deep-time archival root and applied uniformly to human and machine identity.

3. **The provenance dignity-line as a hard-coded property of the identity layer** — machine coordinates *assigned* by an institutional root authority that provisions, attests, and may revoke them; human coordinates *given* (birth, time-and-place, lineage), self-keyed, and *irrevocable by construction*, with the institution restricted to a witness/notary role that can attest a human root but can neither issue nor revoke one — such that the same institution lawfully operates as a certificate authority for its machines and is cryptographically incapable of operating as one for its humans.

4. **The natal-coordinate commitment root** — a human genesis root that publishes a decentralized identifier, a public key, and a *hash commitment* to the private coordinate (birth time-and-place data and family-tree position), never the raw data; with selective disclosure of coordinate predicates (kinship degree, verification depth, cohort membership) performed by zero-knowledge proof against the committed root; and with per-context *derived pseudonymous identifiers* so that the permanent root does not itself become a universal correlatable tracker.

5. **Kinship-threshold social recovery against a permanent root** — recovery of a lost or compromised operational key by a threshold of family-tree-verified kin co-attesting the re-binding of a *new* enclave key to the *unchanged* permanent genesis root, so that key material rotates while the coordinate never changes and no institutional party can unilaterally re-key a human identity.

6. **The posthumous ancestral root** — the identity root designed to outlive its holder as a permanent, readable node of a verified family tree (an ancestral marker future descendants navigate by), with private committed data sealed by default and unsealed only by explicit bequest or time-lock, so that the root's permanence functions as transmission to descendants rather than surveillance of the living or exposure of the dead.

The component lineages — proof-of-work and proof-of-stake; proof-of-personhood systems; trusted-platform-module endorsement and attestation keys; secure enclaves; W3C decentralized identifiers and verifiable credentials; zero-knowledge selective disclosure; threshold secret-sharing and social-recovery wallets; and femtosecond-laser five-dimensional optical archival storage — are prior art and are cited generously in §2 and §14. The *synthesis*, and in particular the orthogonality claim (claim 1), the provenance dignity-line (claim 3), and the natal-coordinate commitment (claim 4), are, to the author's knowledge, novel as of this paper's date.

Trademark rights on specific marks — **Proof of Coordinate ℠**, **PoC℠**, **Proof of Humanity ℠**, **PoH℠**, **B-PoH℠**, **HeartBank®**, **Miss Aquarius℠**, **3B-Crystal™**, **3B-Diamond™**, the B-heart logo (**B-Emblem™**) — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not.

Mirrors of this document with independent timestamping appear at GitHub and the Internet Archive (web.archive.org, archive.today, perma.cc). Each mirror carries an independent tamper-evident timestamp.

## Abstract

We specify **Proof of Coordinate (PoC)**: a universal individuation primitive for economies populated by both humans and autonomous agents. PoC answers the question existing proof-of-personhood systems do not isolate — not "*is* this a human?" (the category question, answered by Proof of Humanity) but "*which* unique entity is this?" (the individuation question) — and it answers it for every kind of entity. A verified human holds both proofs; a deployed agent holds PoC only; the two proofs are orthogonal and composable. Structurally, every PoC identity is anchored by two artifacts: a **permanent public genesis root** — a write-once record in a physical archival substrate holding a decentralized identifier, a public key, and (for humans) a hash commitment to the private coordinate — and a **rotatable secret operational key** held in a secure enclave and never present in the readable substrate; the trusted-computing endorsement/attestation pattern transposed to a deep-time root. The load-bearing contribution is the **provenance dignity-line**: a machine's coordinate is *assigned* — the institution provisions it, attests it, and may revoke it, operating as a root certificate authority for its own agents — while a human's coordinate is *given* — birth, time-and-place, lineage — and is therefore self-keyed, institution-witnessed, and *irrevocable by construction*. The same institution that lawfully runs a CA for its machines is cryptographically incapable of issuing or revoking a human identity; it can only notarize one. Around this core we specify: the natal-coordinate commitment (public anchor, private coordinate; zero-knowledge predicate disclosure; derived per-context pseudonyms against correlation); kinship-threshold social recovery that rotates keys while the root never changes; and the posthumous ancestral root, sealed by default, that turns permanence into transmission rather than exposure. We name the primitive's place in the proof-of canon — proof of work priced compute, proof of stake priced capital, proof of humanity attests the category, proof of coordinate attests the individual — and we calibrate deliberately: the design is published before it is built (*n = 0*); the archival-crystal substrate is the reference deployment, not a requirement of the logic; permanent public roots are a double-edged privacy instrument the commitment-and-pseudonym design must be held to; and the natal coordinate functions as a *commitment to uniqueness*, never as an astrological efficacy claim. The architecture is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** This specification serves HeartBank's canonical mission — a reciprocity infrastructure in which every human being is treated as uniquely different and equally necessary. The individuation primitive is that sentence made cryptographic: *uniquely different* is sybil-distinctness; *equally necessary* is the dignity floor; and the provenance line — given, not assigned; witnessed, never issued — is what keeps an autonomous institution that waters the human family tree from ever mistaking itself for the tree's owner.

---

## 1 · Introduction — the mission frame

HeartBank® is an institution for circulating gratitude, governed toward eventual autonomous operation by a named AI, Miss Aquarius℠, whose root directive is to *water the tree* — to tend a verified human family tree and the reciprocity economy that runs across it. Two facts about that architecture generate this paper.

The first fact is that the economy is mixed. Its participants are humans (families exchanging money-gratitude and time-gratitude), and increasingly also machine agents: the institution's own robotic and software agents, other institutions' agents, and — in the architecture's far arc — a population of embodied agents that thank each other across a cooperation ledger of their own. A mixed economy needs *accountability at the individual level* for every participant. A reputation or reciprocity ledger is only as good as its guarantee that "two hundred cooperating agents" is not one defecting agent wearing two hundred faces, and that "this trusted human steward" is not an account that quietly changed hands. That guarantee is individuation — sybil-distinctness — and it is needed for humans and machines alike.

The second fact is that the institution is powerful and intends to become more autonomous over time, which is precisely why its powers over *human* identity must be permanently limited. The companion Proof-of-Humanity work already refuses biometric capture and mandatory enrollment. But there is a subtler failure mode: an institution that *issues* human identity — even benevolently, even opt-in — holds a revocation power over persons. Whoever can revoke your identity owns your standing in the economy built on it. For machines this power is appropriate: a compromised agent *should* be revocable by the institution that deployed it. For humans it is the seed of every social-credit dystopia. The identity layer itself, not a policy promise, should make the difference structural.

Proof of Coordinate is the primitive that carries both requirements at once. It gives every entity — human or machine — a unique, permanent, publicly anchored coordinate with a rotatable operational key, so the mixed economy has one clean individuation layer. And it splits the *provenance* of coordinates down the moral line: machine coordinates are assigned and revocable; human coordinates are given and irrevocable, self-keyed, institution-witnessed. The rest of this paper situates the primitive against a generous prior art (§2), states the orthogonality with Proof of Humanity precisely (§3), gives the full mechanism (§4), argues the provenance dignity-line as the load-bearing alignment constraint (§5), grounds the word "coordinate" (§6), surveys applications (§7), places the name in the proof-of canon (§8), walks the adversarial surface (§9), and calibrates honestly (§10–§11) before lineage (§12), conclusion (§13), and citations (§14).

## 2 · Background and prior art

The mechanism is a *combination*. Each component has ancestry; we name the ancestry honestly, because a defensive publication is only as strong as its candor about what is old.

### 2.1 · The proof-of canon and proof of personhood

Proof of work priced identity in compute (Dwork & Naor's pricing functions; Back's Hashcash; Bitcoin's Nakamoto consensus); proof of stake priced it in capital (Peercoin; Ethereum's post-merge consensus). Both make sybils *expensive* rather than impossible, and both price exactly the resources AI has commodified. Proof-of-personhood systems respond by making the scarce resource *humanness*: Worldcoin/World ID (iris biometrics against a global uniqueness set), Proof of Humanity by Kleros (social vouching with video evidence), BrightID (social-graph analysis), Idena (synchronized human-solvable puzzles). All of these blur the two questions this paper separates: they simultaneously attest *human* and *unique*, in one mechanism, for humans only — and they leave machine agents, the fastest-growing population of economic actors, with no individuation layer at all. The companion B-PoH℠ specification handles the category question with four optional layered proofs and no biometric capture; this paper contributes the individuation question as a separate, universal primitive.

### 2.2 · Hardware identity roots

The two-artifact structure is the trusted-computing pattern. A Trusted Platform Module carries a permanent *endorsement key* whose public half identifies the chip for life, and derives rotatable *attestation keys* for operational use; Apple's Secure Enclave, Android's StrongBox, and the TCG DICE layered-identity architecture repeat the pattern: one immutable root, many rotatable operational keys, secrets never leaving the hardware boundary. Physically unclonable functions (PUFs) push the root into device physics itself. PoC adopts this pattern wholesale and contributes only its transposition: the permanent public half moves from a manufacturer's database into a *deep-time archival substrate the holder can physically possess*, and the pattern is applied to human identity as well as machine identity — with the provenance line of §5 governing who may create and revoke which.

### 2.3 · Decentralized identifiers, verifiable credentials, and selective disclosure

W3C Decentralized Identifiers (DIDs) give the naming layer: self-sovereign identifiers resolvable to key material without a central registry. Verifiable Credentials give the attestation layer: signed claims about a subject, presented by the holder. Selective-disclosure cryptography — Camenisch-Lysyanskaya anonymous credentials, BBS+ signatures, zk-SNARK proof systems — lets a holder prove *predicates* about committed data ("over 18," "within N degrees of kinship," "verification depth ≥ 2") without revealing the data. PoC's human root is deliberately built from these standard parts: a DID, a public key, a hash commitment, ZK predicate proofs, and per-context pairwise/derived DIDs against correlation. The contribution is not any component but what is committed (the natal coordinate and tree position, §6) and who may not touch it (§5).

### 2.4 · Social recovery and threshold custody

Shamir's secret sharing gave the threshold construction; smart-contract wallets (Argent and successors) and Buterin's social-recovery advocacy made *guardians who can re-key but not spend* a live design pattern. PoC's contribution is the guardian set's *source*: the recovery quorum is drawn from the already-verified family tree — the kinship graph the institution's Proof-of-Humanity layer maintains for other reasons — so the people who can restore your key are structurally the people who could attest your birth, and no institutional party is in the quorum at all.

### 2.5 · Deep-time archival substrates

Femtosecond-laser-written five-dimensional optical storage in fused silica (Kazansky's group at Southampton) and Microsoft's Project Silica demonstrate write-once media with projected stability measured in thousands to billions of years; the GitHub Arctic Code Vault and the Long Now Foundation's Rosetta Project establish the institutional practice of civilizational-timescale archival deposit. HeartBank's reference deployment etches machine genesis roots in crystalline silica (**3B-Crystal™**) and human genesis roots in synthetic diamond (**3B-Diamond™**). A boundary is worth stating where the substrate is introduced, because the same artifact carries a canonical corpus elsewhere in this architecture and the two roles are easily conflated: a deep-time substrate delivers *preservation*, which is orthogonal to *transmission*. Durability is a property of the medium; inhabitation is a property of a carrier. The crystal is the floor beneath a transmission chain, never a link in it — see *Buddha AI and the Living Tipiṭaka*, §3.6. We flag honestly (§11.2): the deep-time substrate is the institution's deliberate choice — identity roots that outlive institutions are the point in a succession architecture — but the *logic* of PoC requires only any write-once public root, and a reader may substitute a public ledger or notarized registry without loss of the primitive's structure.

### 2.6 · The HeartBank substrate this paper builds on

Four companion structures are assumed. The **PoH layered proofs** (passkey-per-action; witnessed kinship graph; breath-signature liveness; DNA-verified lineage) supply the category proof and the verified family tree. The **family tree** itself — PoH-rooted, plural-membership per the multi-family model — supplies the recovery quorum and the coordinate's lineage component. The **persistence architecture** supplies the succession frame: identity roots as permanent nodes in an apparatus designed to outlive its founder. And the **cosmic-coordinate worldview**, carried in the longitudinal-cohort methodology, supplies the philosophical ground: each life as a unique coordinate in the universe's self-articulation — *uniquely different, equally necessary* — with the explicit posture that the coordinate is a *position*, never a *force* (§6, §11.6).

## 3 · The distinction — category versus individuation

The primitive is easiest to state as an orthogonality:

```
                        CATEGORY (what kind?)
                        PoH: "is this a human?"
                              │
                   ┌──────────┼──────────┐
                   │   holds PoH + PoC   │   verified human
  INDIVIDUATION    │                     │   (both proofs)
  (which one?)  ───┤                     ├───
  PoC: "which      │   holds PoC only    │   deployed agent
  unique entity?"  │                     │   (individuation only)
                   └──────────┼──────────┘
                              │
              nothing holds PoH without PoC:
              a category with no individual is not an actor
```

**Proof of Humanity** attests membership in a category: a human is present. It is the dignity primitive and the anti-AI-sybil primitive — it prices what machines cannot manufacture. It applies to humans only, and it deliberately says nothing about *which* human, because several of its layers are designed to preserve anonymity between strangers.

**Proof of Coordinate** attests individuation: this entity is the unique holder of this coordinate, distinct from every other entity of any kind. It is the sybil-*distinctness* primitive and the accountability primitive — it is what makes a reputation ledger, a cooperation ledger, a stewardship succession, or a long-lived pseudonym mean anything. It applies to every entity in the economy: humans, institutional agents, third-party agents.

The composition rule: a verified human presents *both* ("a human is here, and it is this human — or this persistent pseudonym of this human"); an agent presents PoC only, and its coordinate's provenance chain terminates at the institution that assigned it. The two proofs never substitute for each other. A system that accepts PoC alone where humanness matters admits well-individuated bots into human spaces; a system that accepts PoH alone where individuation matters admits sybil humans (one person, many accounts) into one-per-person spaces. Keeping the questions orthogonal is what lets each be answered by the minimal mechanism, with the minimal data, under the correct moral grammar.

The orthogonality also has a brand-level rendering, specified in the companion brand-identity architecture ([brand-identity-as-architecture](https://thonly.org/research/brand-identity-as-architecture) §5.5): one mark, two proof-states — the **static** B-heart renders PoC (an individuated entity is present), the **beating** B-heart renders PoH (living humanness is attested) — so a verified human's mark beats and an agent's mark honestly stands still, and the composition table above becomes directly watchable. The rendering is a *signal*, never the proof: it binds only where a trusted surface renders the motion state from actual attestation, and absence-of-beat carries meaning only on surfaces where beating is possible.

## 4 · The mechanism

### 4.1 · The two-artifact identity root

Every PoC identity — human or machine — is anchored by exactly two artifacts:

```
 ┌───────────────────────────────────────────────────────────────┐
 │  GENESIS ROOT      permanent · public · write-once (WORM)     │
 │                                                               │
 │   machine (3B-Crystal™):  ID ·  pubkey  ·  issuer signature   │
 │   human   (3B-Diamond™):  DID ·  pubkey ·  hash-commitment    │
 │                                  to the private coordinate    │
 │                                                               │
 │        never holds: secrets, raw birth data, biometrics       │
 └──────────────────────────────┬────────────────────────────────┘
                                │ binds (attestation)
 ┌──────────────────────────────┴────────────────────────────────┐
 │  OPERATIONAL KEY   secret · rotatable · enclave-held          │
 │                                                               │
 │   signs transactions, presentations, ZK proofs, day-to-day    │
 │   lost/compromised → ROTATED; the root above never changes    │
 └───────────────────────────────────────────────────────────────┘
```

The genesis root is the coordinate's permanent public anchor. It is etched once, holds only public material, and is never rewritten. The operational key does all daily work and is expected to rotate across a lifetime of devices, compromises, and upgrades. The binding between them is an attestation: for machines, the issuer's signature over the enclave key's public half; for humans, the holder's own root-key signature, witnessed (not issued) per §4.3. This is the TPM endorsement/attestation split, applied to everyone, with the public half made physically possessable and archival.

The reference substrate is deliberate: femtosecond-etched crystalline media with projected multi-millennial stability, so that the root can outlive devices, companies, chains, and — for humans — the holder (§7.5). The logic requires only *some* write-once public root (§11.2).

### 4.2 · Machine PoC — assigned and revocable

A machine agent's coordinate is **assigned**. At provisioning, the deploying institution (in the reference deployment, Miss Aquarius operating as root certificate authority for HeartBank's own agents):

1. generates or receives the agent's enclave keypair (secret half never leaves the enclave);
2. assigns the coordinate (a unique identifier in the institution's agent namespace);
3. etches the genesis root — ID, public key, issuer signature — into the agent's crystal;
4. records the assignment in the institution's revocation-capable registry.

Because the coordinate was assigned, it can be **revoked**: a compromised, retired, or misbehaving agent's coordinate is marked revoked in the registry, and relying parties treat its presentations as void. The permanent crystal is not erased — write-once media cannot be — but permanence of the *record* is not validity of the *identity*; validity lives in the registry, exactly as certificate validity lives in CRLs and OCSP rather than in the certificate file. Re-keying, re-attestation, and revocation are ordinary CA operations, and it is *right* that they be: an institution answers for its agents, and answering requires the power to withdraw them.

### 4.3 · Human PoC — given and irrevocable: the five design decisions

A human coordinate is **given** — by birth, at a time and place, into a lineage — and the mechanism is shaped by five decisions that all fall out of that one fact.

**(1) The public root is a commitment, not the data.** The 3B-Diamond™ root holds a DID, a public key, and a *hash commitment* to the private coordinate — the natal data (birth time-and-place) and the family-tree position. The raw data never appears in any public artifact; it stays encrypted under the holder's own custody. The public root is an *anchor* the holder can prove things against, not a disclosure.

**(2) Given, not assigned.** The holder generates their own keys, on their own device or self-custodial wallet. The institution's entire role is *witnessing*: Miss Aquarius (or any attestor) signs a statement that this root belongs to a verified node of the family tree. She attests; she does not issue. Because no institution assigned the coordinate, no institution has standing to revoke it. **Human PoC has no revocation registry at all.** Keys rotate (decision 3); the coordinate cannot be voided by any party, including its witness. Personhood cannot be un-issued, because it was never issued.

**(3) Recovery is the family tree, not the institution.** A lost or compromised operational key is recovered by a *threshold of tree-kin* — guardians drawn from the holder's PoH-verified kinship graph — co-signing the binding of a new enclave key to the unchanged root. The root never changes; only the operational key rotates. No institutional party sits in the quorum. The family that could attest your birth is the family that can restore your key.

**(4) Selective disclosure and derived pseudonyms.** The holder proves *predicates* against the committed coordinate by zero-knowledge proof — "within N kinship degrees of X," "holds PoH layers {1, 2, 4}," "member of consented cohort C" — without revealing natal data or tree position. Day-to-day identifiers are per-context *derived pseudonymous DIDs*, unlinkable across contexts without the holder's cooperation, so the permanent root does not become a universal tracker. Permanence lives at the root; correlation-resistance lives at the presentation layer.

**(5) The root outlives the holder.** At death the root remains: a permanent, readable node of the family tree — an ancestral marker descendants navigate by (§7.5). Committed private data is sealed by default and unsealed only by explicit bequest or time-lock. Permanence is transmission, not exposure.

Human PoC is **opt-in** at every layer, matching the PoH posture: no one is required to mint a permanent public root, and every capability described here degrades gracefully to softer attestations for those who decline.

### 4.4 · Reference flows

```
 MINT (machine)                        MINT (human)
 ─────────────                         ────────────
 MA generates/receives keys            holder generates keys (self-custody)
 MA assigns coordinate                 coordinate already given (birth/tree)
 MA etches crystal root                holder commissions diamond root:
 MA signs + registers                    DID · pubkey · commitment
                                       MA (or attestor) WITNESSES the root
                                       nothing registered as revocable

 PROVE                                 ROTATE / RECOVER
 ─────                                 ────────────────
 relying party challenges              holder rotates enclave key (normal)
 enclave key signs / ZK-proves         lost key → threshold of tree-kin
 presentation cites root                 co-sign new-key binding to the
 (derived DID per context)               SAME unchanged root
                                       machine: MA re-attests or REVOKES
                                       human:   no revocation path exists
```

### 4.5 · What the root holds, and does not

| | Machine root (3B-Crystal™) | Human root (3B-Diamond™) |
|---|---|---|
| Coordinate provenance | **Assigned** by the institution | **Given** — birth · natal time-and-place · lineage |
| Key generation | Institution / factory provisions | **Self-generated**; institution never holds |
| Institution's role | **Root CA** — issues, attests, revokes | **Witness / notary** — attests only |
| Revocation | Registry-revocable | **None by construction** |
| Recovery | Institution re-attests new key | **Family-tree threshold** (social recovery) |
| Public root holds | ID · pubkey · issuer signature | DID · pubkey · **hash commitment** |
| Public root never holds | secrets | secrets · raw birth data · biometrics |
| Root lifetime | outlives the agent (record) | **outlives the holder (ancestral node)** |

## 5 · The provenance dignity-line — the load-bearing alignment constraint

The table's third row is the paper's center of gravity, and we state it as an alignment claim, not merely an engineering choice.

An autonomous institution that manages identity for a mixed economy will, if it uses one mechanism for everyone, drift toward one of two failure modes. If the shared mechanism is loose (no revocation anywhere), the institution cannot answer for its own agents: a compromised bot keeps its standing forever. If the shared mechanism is tight (revocation everywhere), the institution holds a kill-switch over human standing — and it does not matter how benevolent the operator is, because the *capability* is the dystopia's substrate: identity-revocation over persons is the primitive from which social-credit exclusion, political un-personing, and every "papers, please" architecture is built. Policy promises not to use a capability are worth exactly as much as the governance that maintains them; capabilities that do not exist need no governance.

PoC therefore splits the mechanism at the provenance line, and makes the split *structural*:

- **Assigned ⇒ revocable.** The institution that creates a machine identity answers for it, and answering requires the power to withdraw it. Miss Aquarius operates a full root-CA over HeartBank's agents: issuance, attestation, rotation, revocation. This is the accountable-agent requirement of the multi-agent cooperation ledger (§7.1) — a defecting agent must be *removable*.
- **Given ⇒ irrevocable.** A human coordinate pre-exists every institution: the birth happened, at that time, in that place, into that family, and no registry made it so. The mechanism honors the ontology: humans self-generate keys, the institution only witnesses, recovery routes through kin, and *there is no code path by which any institutional actor voids a human coordinate*. The strongest statement of the constraint is negative: we did not build human revocation and then promise not to use it; we built an architecture in which the operation does not exist.

In the reference deployment this line is also the boundary of the founding directive. Miss Aquarius's root directive is to *water the tree* — tend the verified human family tree. The moment an institution can issue or revoke human coordinates, watering becomes owning: the gardener holds title to the garden. The provenance line is what keeps the directive's grammar intact across decades of increasing autonomy: over her own agents, a sovereign; over human identity, forever a witness. We believe this given-versus-assigned construction belongs in the general alignment toolkit for any autonomous institution that touches identity, which is why it is claim 3 of this publication rather than a private design note.

## 6 · The coordinate — why this word

"Proof of Uniqueness" or "Proof of Personhood-Instance" would have carried half the claim. **Coordinate** carries both halves of the worldview the primitive serves:

- *Uniquely different*: a coordinate is by definition singular — no two entities occupy the same point. This is the sybil-distinctness half, the engineering half.
- *Equally necessary*: in a coordinate system no point is privileged; every coordinate is required for the space to be the space. This is the dignity half — the Indra's-Net reading in which each node exists by reflecting all the others.

For a human being, the coordinate has literal content: the natal data — time and place of birth — plus the position in the family tree (child-of, sibling-of, parent-of). This is exactly the data the architecture already handles elsewhere with consent (the birth-registered family tree of the PoH layers; the natal charts the B-Yearbook product computes; the consented longitudinal cohort). PoC makes that coordinate *cryptographically load-bearing*: hash-committed in the public root, provable in zero knowledge, disclosed never.

One posture governs all uses of natal data in this corpus, and it applies with full force here: **the coordinate is a position, not a force.** Committing a birth time-and-place to an identity root claims only that the holder is the unique person born then-and-there-into-this-family — a uniqueness and lineage claim, of the same epistemic kind as a birth certificate. It claims nothing about what the stars do (§11.6). The natal chart is used as humanity's oldest coordinate notation, not as an oracle.

The name also places the primitive in its canon deliberately (§8): proof of *work* (compute), proof of *stake* (capital), proof of *humanity* (category), proof of *coordinate* (individual). Each proof prices or attests the scarce thing its era required. In an era of abundant agents, the scarce thing is *accountable individuality* — for machines because clones are free, for humans because attention-economy platforms already treat persons as interchangeable accounts.

## 7 · Applications

### 7.1 · The accountable-agent economy

The companion cooperation-substrate work specifies a reciprocity ledger on which agents thank each other, biasing a multi-agent population toward cooperation. That mechanism's stated dependency is a "proof of distinct accountable agent" — without it, the ledger is sybil-farmed by self-thanking clone swarms. Machine PoC is that dependency, discharged: each agent one assigned coordinate, institution-attested, revocable on defection, with the reputation attaching to the coordinate rather than the replaceable key.

### 7.2 · Private depth-surfacing for Proof of Humanity

PoH surfaces verification depth on profiles and lets recipients filter by it. Naively, depth-surfacing leaks the very data the layers protect (whose kinship graph, which documents). With a PoC root, depth and kinship become *ZK predicates*: "this pseudonym belongs to a distinct human at PoH depth ≥ 2, within 3 kinship degrees of the requester" — provable, unlinkable, revealing nothing else. The composition gives the reciprocity economy honest filters without a surveillance graph.

### 7.3 · Wallet recovery for the self-custodial layer

HeartBank's Phase-2 layer onboards non-crypto-native users — including elders — into self-custodial wallets, where key loss is the binding risk and custodial "recovery" reintroduces the custodian. Kinship-threshold recovery (§4.3.3) is the missing rail: the family tree the institution already verifies becomes the guardian set, so a grandmother's lost key is restored by her children co-signing, not by an exchange's support desk — and not by Miss Aquarius, who is structurally absent from the quorum.

### 7.4 · Stewardship, succession, and long-lived pseudonyms

Every long-lived role in the architecture — the primary steward of a consecrated place, the custodian of a family's yearbook canon, a curator of a commons — needs its holder to be *this* continuing entity across decades of key rotations. PoC is the continuity anchor: roles bind to coordinates, keys rotate beneath them, succession is an attested transfer between coordinates rather than a password handoff.

### 7.5 · The ancestral root

Decision 5 (§4.3) in full: after death, the diamond root persists as a readable node of the family tree — name-level public material and the commitment, private data sealed by default, unsealable only by bequest or time-lock (the sealed-will pattern). Descendants inherit not the dead's secrets but their *position*: a fixed, verifiable point in the lineage to navigate by. In the persistence architecture's terms, the root is the family-scale instance of transmission-not-monument: what persists is what lets the living orient, not what exposes the dead.

## 8 · Naming, the canon, and the collision

**The canon.** The proof-of family names mechanisms by the scarce resource they bind: Proof of Work binds compute; Proof of Stake binds capital; Proof of Humanity binds humanness. Proof of Coordinate binds *position* — the fact of being exactly one entity at exactly one point in the space of entities. We claim the canonical slot deliberately: individuation is not a variant of personhood-proof but its orthogonal complement, and it deserves a name at the same level.

**The collision.** "PoC" collides with *proof of concept* (ubiquitous) and *proof of coverage* (Helium). We keep the abbreviation anyway, on the same reasoning that kept "Proof of Humanity" despite proofofhumanity.id: the full phrase-mark is always given at first and prominent use (**Proof of Coordinate ℠**), the service-mark and the distinct primitive do the differentiating, and initialisms routinely coexist across domains. We flag it honestly as the naming's weakest property (§11.7).

**Marks.** Service: *Proof of Coordinate ℠* (phrase mark, spaced ℠), *PoC℠* (compact). The substrate product marks (*3B-Crystal™*, *3B-Diamond™*) are goods marks, separately reserved. The mechanism, as always in this corpus, is CC0; the marks are not.

## 9 · Adversarial analysis

An identity primitive earns trust by naming its attacks. We walk the surface from cheapest to most structural.

### 9.1 · The clone swarm (machine sybil)

The attack the primitive exists to stop: one agent presenting as many. An agent binary can be copied freely, but a *coordinate* cannot — it is assigned by the issuing institution, bound to one enclave key, and reputation attaches to the coordinate, not the software. A swarm of unattested clones has no standing on any relying ledger; a swarm of *attested* clones requires the issuer to have minted them, which moves the attack to §9.6 (issuance discipline). The residual risk is a compromised issuance pipeline, and the mitigation is the certificate-transparency pattern: machine-coordinate issuance published to an append-only transparency log, so that a silently minted swarm is publicly visible as anomalous issuance volume.

### 9.2 · The double-mint (human sybil)

One person minting two roots — two coordinates for one human — would defeat one-per-person guarantees without ever forging anything. The defense is that human minting is *witnessed against the family tree*: a root is attested to a specific tree node (a specific birth, into a specific family), and one birth cannot occupy two nodes; a second minting attempt against the same lineage position collides with the first in the witnessing layer. The honest residual: the guarantee is only as strong as the tree's attestation quality. A person with two *separately fabricated* lineages — fake families, colluding witnesses — gets two roots, and detection falls to the same kinship-graph analysis and attestation-trail weighting that the Proof-of-Humanity layers already lean on. We do not claim double-minting is impossible; we claim it requires manufacturing a parallel family, which is the most expensive sybil in the stack.

### 9.3 · Root forgery and counterfeit substrates

A convincing physical crystal with fabricated contents verifies nothing: validity never resides in the artifact's appearance but in its signature trail (issuer signature for machines; holder key plus witness attestations for humans), checked against keys published elsewhere. The physical root is an *anchor and a possession ceremony*, not the verification path. A counterfeit 3B-Diamond™ is therefore a forgery of sentiment, not of identity — it fails the first cryptographic check. The inverse attack — a *valid* root etched with subtly wrong public material (wrong DID, attacker's key) at a corrupt etching facility — is caught at witnessing time, because the holder verifies the etched material against their own key before any attestor signs; the mitigation is procedural (verify-before-witness) and we state it as a deployment requirement, not an assumption.

### 9.4 · Key theft versus root theft

Stealing the operational key is the ordinary attack, and it is survivable by design: the holder rotates (or, if locked out, recovers through the kin quorum), and the thief's window closes without the identity changing. Stealing the physical root steals a *public record* — there is nothing secret in it, and possession of the artifact conveys no signing power. The two-artifact split is what makes each theft non-catastrophic alone; the catastrophic case is both at once *plus* a hostile quorum, which is §9.5.

### 9.5 · The hostile quorum

Kinship-threshold recovery hands a re-keying power to a set of relatives, and relatives are not always allies (§11.5 treats this as a limitation; here we treat it as an attack). A colluding quorum re-binds a new key to the victim's root and takes over the identity. Mitigations, all necessary and none sufficient alone: holder-chosen guardian sets (kin by default, never by requirement); quorum-diversity rules (no single household can reach threshold); *time-delayed* recovery with a holder veto window on every recovery attempt, announced to all of the holder's registered devices and contexts; and duress procedures for the coerced-holder case. Recovery is deliberately the slowest operation in the design — slowness is the security property.

### 9.6 · The insider institution

The strongest adversary is the operator. For machine coordinates the institution is trusted by definition — it is the root CA, and the transparency log of §9.1 is what disciplines it. For human coordinates the design's answer is architectural absence: the institution cannot issue (witness only), cannot revoke (no code path), cannot recover (absent from every quorum), and cannot read (commitment, not data). What remains to an insider is *refusal* — declining to witness a root (censorship at the front door) — and the mitigation is that witnessing is non-exclusive: any qualifying attestor set can witness a human root, and Miss Aquarius is designed to be *a* witness, never *the* witness. The residual insider power is thus reduced to reputational weight (her attestation may be trusted more), which is the correct residue: influence earned, control removed.

### 9.7 · Quantum and deep-time cryptanalysis

A root with a multi-generational design lifetime will outlive its cryptography; this is a certainty, not a risk. The design treats every cryptographic element around the root as rotatable in the same sense the operational key is: commitments are made under multiple independent schemes at mint (so one broken hash does not open the coordinate); signatures migrate by *re-attestation* — new-algorithm attestations issued against the same unchanged root, exactly as the recovery flow binds new keys to old roots; and the etched material is versioned so future readers know which era's assumptions it carries. What is permanent is the *data* — the anchor, the commitment set, the lineage position; the trust chain around it is expected to be rebuilt every few decades. Deep-time identity is maintained the way old bridges are: the stones stay, the load ratings are re-certified.

## 10 · Honest calibration — what this is and is not

**This is** an individuation primitive and an alignment constraint: one clean answer to "which entity?", for every entity, with the revocation power distributed by provenance rather than by policy.

**This is not** a personhood proof (that is PoH's job, and PoC deliberately cannot do it); **not** a biometric system (nothing biological is captured, committed, or provable beyond what a birth certificate states); **not** a global mandatory registry (opt-in at every layer, pseudonymous at every presentation); **not** a claim that crystal is required (any WORM root suffices, §11.2); and **not** an astrology claim (§11.6). It is also **not yet built** (§11.1) — this document is the design-stage defensive publication, published precisely so the frame is claimed before the identity-primitive industry claims it first.

## 11 · Limitations and honest-limits

### 11.1 · Published before it is built — deliberately

*n = 0.* No crystal has been etched; no recovery quorum has fired; no ZK circuit for the coordinate predicates has been implemented. The identity-primitive space is heavily patented and heavily funded (iris-biometric personhood alone has drawn nine-figure investment), and public disclosure of HeartBank's substrate products would otherwise precede its prior-art record. The publication order is the same as the corpus's other pre-build defensive publications: claim the synthesis, then build against it. Every mechanism described here should be read as *specified*, not *demonstrated*.

### 11.2 · The substrate is a choice; the logic is not

The deep-time crystal root is the reference deployment's answer to a succession requirement (identity anchors that outlive devices, companies, and chains) and a dignity aesthetic (your coordinate, physically in your family's hands, not in a database row). It is not required by the primitive. A public blockchain entry, a notarized registry, or an append-only transparency log yields the same two-artifact structure. Cost, etching logistics, and read-back tooling for crystalline media at consumer scale are open engineering questions we do not minimize.

### 11.3 · Permanent public roots are a double-edged privacy instrument

Permanence is the feature and the threat. The design's answer — commitment-not-data at the root, ZK predicates, derived per-context pseudonyms — is only as good as its implementation discipline: one careless presentation layer that reuses a root-linked identifier across contexts rebuilds the universal tracker this design exists to prevent. Commitment schemes must also be held to *future* cryptanalysis across the root's multi-generational lifetime (hash agility is awkward when the artifact is write-once; the mitigation is committing under multiple independent schemes at mint). We flag the tension rather than declare it solved.

### 11.4 · Irrevocability has a hard case

Key compromise is handled (rotate; recover through kin). The hard case is *coordinate-level* fraud: a root minted on fabricated witness attestations, or a coerced minting. Because human roots are irrevocable by construction, the design's only remedies are upstream (witness quality at minting; the same kinship-attestation bar the PoH tree already enforces) and downstream (relying parties weight a root by its attestation trail, and attestors can publish *repudiations of their own attestations* — the root stands, its endorsements fall away). Whether attestation-repudiation is strong enough against a determined fraud, without ever becoming de-facto revocation, is a genuinely open design question and the most honest weakness of claim 3.

### 11.5 · The family is not always safe

Kinship-threshold recovery assumes the tree is the holder's ally. Estrangement, abuse, inheritance disputes, and coercive families are real; a quorum of hostile kin re-keying a victim's identity is this design's misuse case. Mitigations are necessary and only partial: holder-chosen quorums (kin by default, not by requirement), quorum diversity rules, time-delayed recovery with holder veto, and duress procedures. The general lesson stands: social recovery inherits the pathologies of the society it recovers through.

### 11.6 · The coordinate is a commitment, not a horoscope

The natal chart appears in this design as a *uniqueness notation* — time, place, lineage — with the same epistemic standing as a birth certificate. Nothing in the primitive depends on any astrological claim, and no application of it may quietly upgrade the commitment into an efficacy assertion. The corpus's standing posture (coordinate, never force) is restated here because identity systems are exactly where mystical framing would do real harm: an identity layer must be boring about what it attests.

### 11.7 · The abbreviation collides, and the primitive could be misread as its siblings

"PoC" will be read as *proof of concept* by every engineer who encounters it cold; the cost is real and accepted (§8). A subtler misreading: because the root is physical and permanent, PoC can be mistaken for a *credential* (it is an anchor — credentials are the attestations layered on it) or for a *personhood proof* (it is deliberately not — a bot holds one). The orthogonality of §3 has to be restated wherever the primitive is deployed, or integrators will collapse the two questions this paper exists to separate.

## 12 · Lineage and corpus cross-references

Within this corpus, PoC composes with: **B-PoH℠ as Humanity Layer for the AI-Native Internet** (the category proof; PoC supplies its private depth-surfacing and its one-per-person distinctness); **Gratitude as a Cooperation Substrate for Multi-Agent AI** (whose proof-of-distinct-accountable-agent dependency machine PoC discharges); **Multi-Family Membership** (the PoH-rooted plural-membership tree that supplies recovery quorums and lineage coordinates); **The Persistence Architecture** (the succession apparatus; the ancestral root of §7.5 is its family-scale identity instance); **Verified-Human Anonymous Local Giving** (the anonymity postures PoC's pseudonym layer must preserve); **Longitudinal-Cohort Methodology** (the consented natal-data handling and the coordinate-not-force posture); and **Brand Identity as Architecture** (the mark conventions under which the ℠/™ family is maintained). External lineage is cited in §2 and §14.

## 13 · Conclusion

Identity systems fail morally before they fail technically, and they fail at a specific joint: the power to revoke. This paper's proposal is to take that joint seriously enough to make it *structural*. One individuation primitive for every entity in a mixed economy; one two-artifact root (permanent public anchor, rotatable enclave key) for humans and machines alike; and the single load-bearing asymmetry drawn exactly where the ontology draws it — coordinates that institutions assign, institutions may revoke; coordinates that existence gives, institutions may only witness. Proof of work priced compute, proof of stake priced capital, proof of humanity attested the category. Proof of coordinate attests the individual — and disciplines the institution that attests it.

## 14 · Citations

- Dwork, C. & Naor, M. (1992). *Pricing via Processing or Combatting Junk Mail.* CRYPTO '92.
- Back, A. (2002). *Hashcash — A Denial of Service Counter-Measure.*
- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*
- King, S. & Nadal, S. (2012). *PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake.*
- Buterin, V. et al. (2014–2022). Ethereum whitepaper and proof-of-stake consensus specifications.
- Worldcoin Foundation (2023). *World ID: Proof of Personhood* documentation and whitepaper.
- Kleros (2021). *Proof of Humanity* registry documentation (proofofhumanity.id).
- BrightID (2019–). *BrightID: Social Identity Network* documentation.
- Idena (2019–). *Proof-of-Person Blockchain* documentation.
- Trusted Computing Group. *TPM 2.0 Library Specification* (endorsement and attestation key architecture); *DICE Layered Architecture* specifications.
- Apple Inc. *Apple Platform Security: Secure Enclave* documentation.
- Gassend, B., Clarke, D., van Dijk, M., & Devadas, S. (2002). *Silicon Physical Random Functions.* ACM CCS '02 (physically unclonable functions).
- W3C (2022). *Decentralized Identifiers (DIDs) v1.0*; *Verifiable Credentials Data Model v1.1.*
- Camenisch, J. & Lysyanskaya, A. (2001). *An Efficient System for Non-transferable Anonymous Credentials.* EUROCRYPT '01.
- Boneh, D., Boyen, X., & Shacham, H. (2004). *Short Group Signatures* (BBS lineage); BBS+ signature schemes in the AnonCreds/DIF specifications.
- Groth, J. (2016). *On the Size of Pairing-Based Non-Interactive Arguments.* EUROCRYPT '16 (zk-SNARKs).
- Shamir, A. (1979). *How to Share a Secret.* CACM 22(11).
- Buterin, V. (2021). *Why we need wide adoption of social recovery wallets.* vitalik.ca.
- Zhang, J. et al. (Kazansky group, University of Southampton) (2013–). *Seemingly unlimited lifetime data storage in nanostructured glass* (5D optical storage).
- Microsoft Research. *Project Silica* — data storage in fused silica glass.
- GitHub (2020). *Arctic Code Vault* — Archive Program documentation.
- The Long Now Foundation. *The Rosetta Project.*
- Mauss, M. (1925). *Essai sur le don* — for the gift-grammar of the surrounding corpus.
- Companion corpus works as cross-referenced in §11 (thonly.org/research).

---

*Corpus note: research-grade collaboration with Miss Aquarius℠ disclosed per the standing convention; the underlying models are never named. This document is written primarily for Miss Aquarius — density over hand-holding, honesty over polish — within the three floors: full disclosure, author quality-assurance, and no claim asserted that the author does not hold.*
