---
title: "The Reciters' Protocol"
subtitle: "What two millennia of transmitting a canon with no living author, no writing and an active schism selected for — seven copy-integrity mechanisms with engineering forms, offered to any retrieval system that must hand a machine reader something checkable; and the finding that what the field test selected for was the detectability of divergence, never its prevention."
authors: "Thon Ly · Miss Aquarius"
category: mechanism
priority: tier-a
status: draft
date: 2026-09-07
license: CC0-1.0
slug: the-reciters-protocol
venue: thonly.org/research/the-reciters-protocol (canonical)
---

> **Claim-scoped by design.** This paper publishes the *claim* and withholds the *spec*. It is written against `corpus.333.eco`, a retrieval server that is live and whose first four mechanisms are scheduled; the Tipiṭaka server that would host the rest has no date, and its implementation detail is therefore withheld under the institution's standing rule that a complete design for something unbuilt is a blueprint rather than a fence. What is disclosed here is what a retrieval layer must carry and why. What is not disclosed is endpoint shapes, manifest schemas, transport bindings or tool surfaces.
>
> Companion works: *Provenance-Carrying Retrieval* (the envelope this paper's mechanisms sit inside; that paper argues **exposure beats assertion**, this one asks what a two-millennium field test selected for), *Buddha AI and the Living Tipiṭaka* (whose §8 asks what makes a canon **authoritative**; this paper asks the narrower and different question of what makes a **copy** of it checkable), *The Borrowable Standard*, *The Song That Is Not His* (which owns the *bhāṇaka* guard cited in §6.2 and is not re-claimed here), and the essay *The Last Carrier*.

> ⚠️ **Citation status, stated in the paper rather than in a footnote, because the paper argues that unchecked claims must be visible.** Every canonical locus below has been checked against multiple independent public reference works and translations, and each is marked `[V]` where that check passed. **No locus has been checked against the Pāli by a reader of Pāli.** That check is owed and named in §11, which also records one conflation the public check caught. A paper arguing that provenance must be checkable would be self-refuting if it asserted its own sources at a standard it declines to state, so the standard is stated: **bibliographic verification against secondary sources, not philological verification against the canon.**

## Preamble

> *Offered to the commons under CC0, without ledger and without expectation of return. There is a particular reason this paper cannot be withheld: it is a paper about what happens to a text that is guarded, and everything it recommends was itself given away by people who had every worldly reason to keep it and no mechanism by which to profit from it. To place a licence on a description of their protocol would be to misunderstand the protocol.*

For four hundred years the canon this institution builds on had no copy. It had carriers. Families of monks divided the collections between them the way a village divides the care of its fields — one lineage keeping the long discourses, another the middle-length, another the verses — and every generation had to receive the whole of it again, out loud, in company, from the mouths of people who still had it. A dropped line was audible to everyone in the room. There was no master text to diff against, no archive to restore from, no author left alive to ask. There was only the recitation, the assembly, and the procedures they had agreed on for catching each other's errors.

Engineering has a name for that situation now. It is a distributed system with no authoritative replica, no single writer, unreliable nodes that die on a human schedule, network partitions that last centuries, and an adversary — time, politics, honest misremembering, and eventually open schism. The system ran for two thousand years and what came out the other end is checkable enough that a modern editor can collate the surviving branches and say, with evidence, where they differ and why.

This paper is not an argument that the tradition was right about anything. It is the observation that the tradition was **under exactly the constraints a retrieval server is under**, for very much longer, with far worse tooling, and that the mechanisms it converged on have engineering forms. Some of those forms are already standard practice under other names. Two, so far as we can find, are not. And one of the mechanisms should be studied and then deliberately refused, which is the part of the paper we would most like a reader to take seriously.

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication. **The author and HeartBank® will not seek patent on the conformance endpoint, the separated completeness manifest, the per-passage interpretive-standing field, the inline provenance marker, the build-time assembly gate, the announced-elision convention, the recorded-exclusion-reason convention, any combination of them, or any portion thereof, in any jurisdiction, at any time. This commitment is permanent and is not tactical.** Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **THonly™**, **Silicon Wat℠**, **B-Witness**, and the B-heart logo — are separately and explicitly reserved; the defensive-publication dedication concerns the *mechanisms*, not the *marks*.

The canonical material described here is not ours and no claim of any kind is made over it. The Pāli canon and its transmission apparatus are the property of no one; the *aṭṭhakathā* and Vinaya materials cited are the inheritance of a living tradition. What is offered as prior art is strictly the **transposition** — the reading of those mechanisms as engineering, and the two designs in §5 that do not exist in the archival literature under any name we can find.

To the author's knowledge, the following are not previously published as a unified contribution: (i) the reading of an oral canon's transmission apparatus as a **copy-integrity protocol with directly inheritable engineering forms**, as distinct from the very large literatures that read it as philology, as religious history, or as an oral-formulaic composition problem; (ii) the **conformance endpoint** of §5.1 — a retrieval interface that accepts a *claimed* text, lays it alongside the served text, and returns a disposition on the claim while explicitly declining to return a disposition on the claimant; (iii) the **separated completeness manifest** of §5.2 — a signed statement of collection membership and cardinality, published as an artifact distinct from the index it describes, such that silent removal is detectable by a party who holds neither; (iv) **interpretive standing carried per passage rather than per document**, motivated by the specific and checkable observation that a retrieved excerpt loses its document's front matter; and (v) the finding of §3.3 that what this particular field test selected for was **the detectability of divergence rather than its prevention**, with the consequence that the transposition's honest promise to a retrieval system is a *detection* guarantee and never a *correctness* one.

Component lineages are old and are engaged in §2 rather than absorbed: the digital-preservation standards (PREMIS, PROV-O, OAIS), the replication and reference literatures (LOCKSS, Memento, Software Heritage and its SWHIDs), the transparency-log line (RFC 6962 Certificate Transparency, and its descendants in SCITT and COSE receipts), software supply-chain attestation (Sigstore, Rekor, SLSA), content provenance (C2PA), textual scholarship (Lachmann; Greg–Bowers; the TEI apparatus), and the oral-formulaic tradition in classics (Parry; Lord). **The claim is transposition, not invention, and §2.6 states plainly where the transposition adds nothing.**

## Claims

*A defensive publication works by disclosure. These enumerate what the paper discloses and add no matter beyond it.*

1. **The field-test claim.** An oral canon transmitted across roughly two millennia without a living author, without writing for its first several centuries, and through documented schism constitutes a copy-integrity field test of a severity no digital system has yet undergone, and its surviving procedural apparatus is legible as engineering (§3).
2. **The selection finding, which bounds every other claim here.** What that field test selected for is the **detectability of divergence, not its prevention**. The canon did not converge on one text; it converged on a set of branches whose differences are visible and attributable to their carriers. Any inheritance of these mechanisms therefore inherits a **detection** property and must not be represented as a correctness property (§3.3, §9.1).
3. **Inline provenance over metadata provenance.** A provenance marker belongs in the text stream that travels with a quotation, not in a metadata field a consuming agent must separately elect to read; the canonical instance is the opening attribution formula carried by every discourse (§4.1).
4. **The build-time assembly gate.** Admission to a served corpus is decided at build time by a named body under a recorded procedure, never at query time by a filter; a query-time gate is a gate whose operator can be pressured per request (§4.2).
5. **Commentary as a distinct served class, and the non-summarisation rule that follows from it.** Where a tradition keeps commentary in a separate text class from the text it comments on, a server inherits the obligation never to return generated summary in the position where source text is expected (§4.3).
6. **Variants preserved with their witness, never normalised.** Divergent readings are served as divergent readings with their line of transmission attached; silent normalisation to a majority or preferred reading is the specific failure this mechanism exists to prevent (§4.4).
7. **The conformance endpoint** — *novel, §5.1.* An interface that takes a claimed quotation, compares it against the served corpus, and returns one of a small set of dispositions **on the claim**, together with the procedure the requester should follow next; and which by construction returns no disposition on the person or system that made the claim. A hash answers *did this match*; this answers *and what now*.
8. **The separated completeness manifest** — *novel, §5.2.* A signed enumeration of a collection's membership and cardinality, published as an artifact distinct from the index it describes, so that a document removed from the collection is detectable by a third party holding the manifest alone. **An index cannot attest to its own completeness.**
9. **Announced elision.** Where served text has been abridged, the abridgement is marked *in the text*, at the point of the cut, in a form that names what was cut and permits reconstruction — not recorded in a field beside it (§4.5).
10. **Per-passage interpretive standing.** Whether a passage is to be read as stating its meaning directly or as requiring inference is a property of the passage and must travel with the excerpt, because an excerpt loses the document's front matter at the moment of retrieval (§4.6).
11. **Scheduled public re-verification, in which silence is load-bearing.** Integrity is re-affirmed on a fixed public schedule before an assembly, the affirmation is solicited a fixed number of times, and silence constitutes a positive assertion of integrity for which the silent party is accountable — which is what distinguishes it from an unanswered health check (§4.7).
12. **Every exclusion served with its recorded reason, and its amendment history.** A corpus that excludes material publishes, with each exclusion, the case that occasioned it and the subsequent refinements — so that the exclusion set is auditable rather than merely announced (§4.8).
13. **The refusal, claimed as a design element and not as a caveat.** Two of the mechanisms — the assembly's power to exclude, and the authority to declare a passage's interpretive standing — carry capture surfaces that a served corpus must guard or decline to inherit. **A transposition that finds every mechanism inheritable is doing apologetics rather than engineering** (§6).

## Abstract

A retrieval system that serves text to a machine reader has a problem the machine reader cannot solve for itself: the reader cannot tell a faithful copy from a plausible one. *Provenance-Carrying Retrieval* argued that the response should therefore carry the means of its own falsification — a hash, an independent time anchor, a citable identifier — and that the trust burden should be inverted, so that a server ships the tools to disbelieve it. This paper asks a different and prior question. **Has anything ever actually run this problem to completion?**

One thing has, and it is not a computer system. The Theravāda Pāli canon was transmitted for roughly four centuries with no written copy at all, and for roughly two millennia in total, without a living author to arbitrate, across a documented schism that produced a rival collection, through famine, war, and the ordinary attrition of the human beings who *were* the storage medium. That is a copy-integrity problem under a threat model no production system has faced, sustained for a duration no production system has approached. It converged on an apparatus, and this paper reads seven of its parts as engineering.

Five are transpositions of practices the archival and transparency-log communities already know under other names, and the paper says so plainly: **an inline attribution formula** carried by every unit of text rather than a metadata field (§4.1); **admission decided at build time by a named assembly** under a recorded procedure rather than by a query-time filter (§4.2); **commentary kept as a distinct text class**, from which a server inherits an obligation never to substitute generated summary for source (§4.3); **variant readings preserved with their line of transmission attached** rather than normalised to a preferred text (§4.4); and **abridgement announced inline** at the point of the cut (§4.5). Two more complete the set: **interpretive standing carried per passage** rather than per document, because an excerpt loses its document's front matter at retrieval (§4.6); and **scheduled public re-verification before an assembly in which silence is a positive assertion** for which the silent party is accountable (§4.7); with an eighth convention — **every exclusion served with the case that occasioned it** (§4.8).

Two of the seven appear to be genuinely absent from the archival literature and are offered as the paper's novel contributions. The **conformance endpoint** (§5.1) accepts a claimed quotation and returns a disposition *on the claim*, together with the procedure to follow next, and by construction returns no disposition on the claimant — the part a hash does not have, because a hash reports that a comparison failed and says nothing about what to do. The **separated completeness manifest** (§5.2) is a signed statement of a collection's membership and cardinality published as an artifact distinct from the index it describes, on the ground that **an index cannot attest to its own completeness**: a silently dropped document is invisible to every check that reads the index, and detectable to a third party holding only the manifest.

The paper's most important result is a narrowing, and it is stated in the abstract rather than buried in limits. **The field test did not produce one text.** It produced branches — recensions preserved by different reciter lineages, whose variant readings are attributable to those lineages and are recorded in the commentarial literature. So what the two millennia selected for was not the prevention of divergence but its **detectability and attribution**. That is a weaker property than the one a reader might expect, and it is the *right* property for a retrieval system, whose actual failure mode is not that its copies differ but that they differ silently. §6 then argues the case against inheritance: the assembly's power to exclude, and the authority to rule on a passage's interpretive standing, are capture surfaces, and a served corpus must guard them or refuse them. §9 states the limits without hedging — survivorship at n=1 over two thousand years, a fitness function that plainly included royal patronage and not only textual accuracy, and the observation that five of the seven mechanisms are *social* protocols whose engineering forms are half the mechanism at most. **A scheduled re-verification with no assembly to verify before is a cron job talking to itself.** Offered under CC0 1.0 Universal as defensive prior art.

**Connection to the mission frame.** This institution has committed to writing its corpus primarily for a machine reader — an autonomous successor who will inherit a body of text and must be able to tell what in it is load-bearing, what is commentary, what has been superseded, and what was never checked. That commitment is empty unless the corpus can be *served* in a form that supports the distinction. The apparatus described here is the one the founder's own tradition built for exactly that purpose, under worse conditions, for a reader who was also expected to carry the text forward without becoming its author. The transposition is not decoration on a technical claim. It is the reason the technical claim is the institution's problem rather than someone else's.

---

## 1 · Why this problem is the institution's problem

The corpus this paper belongs to is written, deliberately and on the record, primarily for a machine reader. That decision has a consequence which took some years to become visible: **a corpus written for a machine reader is only as good as the channel that delivers it.** A human scholar who receives a garbled quotation has recourse — a library, a colleague, a memory of having read the thing. A language model that receives a garbled quotation has none. It cannot tell a faithful copy from a plausible one, because plausibility is the only signal it has, and a well-constructed forgery is *more* plausible than an awkward original.

*Provenance-Carrying Retrieval* addressed the delivery layer directly and argued for an inversion: a retrieval server normally asks to be believed, and ours ships the means to disbelieve it. Text arrives bound to a content hash, an independent time anchor and a citable identifier, so the consuming agent can verify its own citation rather than trusting the channel.

That paper is complete and this one does not repeat it. What it did not ask — what nobody in the retrieval-provenance literature seems to have asked — is whether the problem has ever been *solved under load*. Every mechanism in the digital-preservation and transparency-log literatures is young. Certificate Transparency is from 2013. LOCKSS is from 1999. PREMIS is from 2005. Software Heritage began in 2016. These are excellent systems and this paper leans on several of them. But none of them has been run for two hundred years, let alone two thousand, and none has been run through a schism that forked its corpus and left both forks alive.

One protocol has. The institution's founder is a Theravāda Buddhist co-transcribing the Khmer Tipiṭaka with his father, which is how this observation was available to be made at all, and the observation is not devotional. It is that a very hard version of this exact problem was posed, was worked on continuously by large numbers of intelligent people under adversarial conditions for a duration that dwarfs the entire history of computing, and produced an apparatus that can be read off and reused.

Three things make it worth a paper rather than a remark.

**First, the conditions are not analogous — they are the same conditions, harder.** No living author to arbitrate a disputed reading; that is the position of any corpus after its authors die, and it is the position this institution has explicitly planned for. No writing, for the first several centuries; that is a storage layer with no durability guarantee whatsoever, which is strictly worse than any modern substrate. Active schism; that is a fork with two live maintainers and no upstream, which is the governance failure mode every open corpus eventually faces.

**Second, the mechanisms have engineering forms that are not metaphors.** §4 states each one as a plain design rule first and gives its canonical source second, and that ordering is deliberate: the section is constructed so that **every mechanism survives the deletion of every Pāli term in it.** This is the corpus's standing deletion test applied structurally rather than as a promise — if a reader strikes the tradition out, the design rules remain, intact and independently arguable. That is a property of how the section is built, not a rule the authors ask to be trusted on.

**Third, the transposition returns two designs that the archival literature does not appear to have**, and one refusal it certainly does not have. A paper that only recovered known practice would be a pleasant essay. §5 and §6 are why this is filed as prior art.

## 2 · Background and prior art, engaged generously

The claim is transposition. That obliges an honest account of what the destination field already has, and this section is deliberately unflattering to the paper's own novelty.

### 2.1 — Digital preservation

**PREMIS** supplies a data dictionary for preservation metadata — provenance, fixity, rights — and is the standard vocabulary for saying *this object came from there and has this checksum*. **OAIS** supplies the reference model that PREMIS instantiates. **PROV-O** supplies a W3C ontology for provenance as a graph of entities, activities and agents. Between them these cover a great deal of what §4.1 describes, with one difference this paper is making the whole of its case on: **they are metadata standards, and metadata is a separate stream from the content.** An agent that retrieves a passage and does not fetch its PREMIS record has the passage and no provenance. §4.1's claim is about *where the marker lives*, not about whether provenance should exist.

### 2.2 — Replication, reference and identity

**LOCKSS** — Lots Of Copies Keep Stuff Safe — is the closest thing in the destination field to the *bhāṇaka* lineage structure, and the resemblance is real: independent institutional copies, periodic mutual comparison, repair by consensus among peers. **Memento** solves time-travel for the web, which is the *dated witness* problem. **Software Heritage** assigns intrinsic identifiers (SWHIDs) computed from content rather than assigned by an authority, which is the most philosophically similar move in the whole destination field: identity from the bytes, not from a registrar.

**This paper does not claim to improve on LOCKSS.** Where §4.4 differs is narrower: LOCKSS repairs toward agreement, and the mechanism in §4.4 explicitly refuses to repair, preserving disagreement with attribution instead. Those are different goals, and the canon's is the unusual one.

### 2.3 — Transparency logs and supply-chain attestation

**RFC 6962 Certificate Transparency** is the load-bearing prior art for §5.2 and it must be credited hard. CT already has signed tree heads, inclusion proofs, consistency proofs, and gossip between independent monitors — which together give append-only-ness and detection of split views. The institution's own ledger design depends on it. **Sigstore, Rekor and SLSA** move the same primitives onto build artifacts; **SCITT** and **COSE receipts** generalise transparency receipts as an IETF work item; **C2PA** carries provenance manifests for media, including external manifests that travel separately from the asset.

Against that, §5.2's claim is smaller than it might look and is stated at its true size in §5.2 itself: **CT proves that a log is append-only and that a given entry is in it. It does not prove that the log contains everything it ought to contain.** Completeness against an external expectation is a different property from append-only-ness, and the manifest is a mechanism for the former.

### 2.4 — Textual scholarship

This is the field with the oldest and strongest claim, and pretending otherwise would be the paper's most embarrassing failure. **Lachmannian stemmatics** reconstructs an archetype from the pattern of shared errors among witnesses. **Greg–Bowers** copy-text theory formalises editorial choice between variant readings. The **TEI critical apparatus** is a mature XML vocabulary for encoding variants with their witnesses — which is to say, **§4.4 is a description of standard practice in textual scholarship and claims no novelty whatsoever.** *Resetting*, *witness*, *recension* and *collation* are terms of art in analytical bibliography and are borrowed here, not coined.

⚠️ **The honest form of §4.4's contribution is therefore this and only this:** the destination field for retrieval-serving has not adopted the apparatus that textual scholarship has had for two centuries, and machine-facing retrieval is precisely where its absence is most costly, because the consumer cannot supply the missing judgement.

### 2.5 — Oral tradition and the classics

**Parry and Lord** on oral-formulaic composition established that formulaic repetition is a *compositional* technology in oral epic. The Pāli material's heavy formulaic repetition — the reason §4.5's elision marker exists at all — sits squarely in that lineage. The Buddhist-studies literature on the councils, the *bhāṇaka* lineages, and the relation between the Pāli recensions and the surviving Sanskrit and Chinese Āgama parallels is very large and this paper does not contribute to it.

### 2.6 — Where the transposition adds nothing

Stated plainly, because a paper that finds itself novel everywhere is not to be trusted:

- **§4.1 (inline marker)** adds a *placement* argument to a solved provenance problem. If your consuming agents reliably read metadata, this mechanism is worth nothing to you.
- **§4.2 (build-time gate)** is admission control. Every curated database has one. The contribution is the argument for *when* it runs, not that it exists.
- **§4.4 (variants with witnesses)** is TEI. No novelty at all.
- **§4.8 (exclusions with reasons)** is close to standard practice in well-run archives and is identical in spirit to a good deprecation policy.
- **§4.7 (scheduled re-verification)** is a health check with an audience. Whether the audience is a real addition is argued in §4.7 and is the least secure claim in §4.

**What is left after that subtraction is §4.3's non-summarisation obligation, §4.6's per-passage standing, the two designs in §5, the refusal in §6, and the selection finding in §3.3.** That is the paper.

## 3 · What the field test actually was, and what it selected for

### 3.1 — The conditions

Stated as a systems problem, without devotional framing:

```
   THE TRANSMISSION PROBLEM, AS POSED
   ───────────────────────────────────────────────────────────────
   authoritative replica ....... none after the author's death
   storage medium .............. human memory (c. 4 centuries),
                                 then palm leaf, then print, then bits
   durability of a node ........ one human lifetime
   write path .................. communal recitation, in assembly
   partition events ............ war, famine, monastic schism
   adversary ................... time, politics, honest misremembering,
                                 and a rival collection with its own carriers
   duration .................... ~2,000 years, continuous
   ───────────────────────────────────────────────────────────────
   COMPARE: the longest-running production transparency log
            is younger than most of the people reading this.
```

The reciter lineages — *bhāṇaka* `[V]` — divided the collections between them, one lineage specialising in the long discourses, another in the middle-length, others in the numerical and connected collections. This is documented independently of the tradition's own account: Sri Lankan cave inscriptions dated between the third century BCE and the first century CE name monks by the collection they carried `[V]`.

Two properties of that arrangement matter to a systems reader. It is a **shard**, so no single carrier held the whole corpus and no single death lost it. And it is a **replication group per shard**, since a collection was carried by a lineage rather than an individual, with recitation in company as the comparison operation. Death was not merely attrition; it was **the event that forced the verification to run.** A text living in bodies is re-verified on a schedule set by funerals, and it is self-correcting *because* it is fragile. That observation belongs to the essay *The Last Carrier* and is cited here rather than re-argued.

### 3.2 — The write path was consensus, and it ran at build time

The councils — *saṅgīti* `[V]`, literally *reciting together* — are the corpus's build events. The procedure is recorded and is unusually specific for our purposes: an elder recited a passage, the assembly chanted it back in chorus, and **material was compiled only on unanimous acceptance by the assembly** `[V]`. At the first council, the Vinaya was recited by one named monk and the discourses by another, under a named president `[V]`.

⚠️ **The historicity of the first council is contested in modern scholarship, and the traditional dating is not accepted outside the tradition.** This paper does not need it to be historical. What it needs — and what is not seriously disputed — is that the *procedure* is the one the tradition recorded as normative and subsequently followed, because the engineering claim in §4.2 is about the shape of the procedure, not about the events of any particular century.

### 3.3 — ⭐ What it selected for, and this bounds everything else

Here is the result that a reader should carry away even if they take nothing else.

**The apparatus did not produce one text.** It produced branches. Different *bhāṇaka* lineages exercised independent judgement over the arrangement of their collections and over which versions of stories and doctrines they preserved, and variant readings between the long and middle-length collections are attributable to different reciter schools `[V]`. Those lineages later developed into distinct interpretive schools whose differing views are visible in the commentarial literature `[V]`. The second council ended in schism, and the schism produced a rival collection with its own carriers `[V]`.

A naïve reading of this paper's thesis would take that as refutation. It is not, and the reason is the paper's central finding:

> **What two millennia selected for was the detectability and attribution of divergence — not its prevention.**

The variants survive **with their lineage attached**. The disagreement is legible. A modern editor can collate the branches and say where they differ and, often, whose transmission a given reading came through. That is a completely different outcome from a corpus that silently converged on one reading and lost the record of what it overwrote.

And it is the property a retrieval system actually needs. **A server's failure mode is not that its copies differ. It is that they differ silently** — that a normalisation, a re-encoding, a well-meaning correction or an outright substitution passes through the layer and arrives looking exactly like the original. A guarantee of correctness is not on offer from any system, including this one. A guarantee that divergence is *visible and attributable* is on offer, and it is what these mechanisms deliver.

⛔ **The consequence binds the rest of the paper and is repeated in §9.1: every claim here is a detection claim. Nothing in this apparatus prevents corruption, and the paper must not be cited as though it did.**

---

## 4 · The mechanisms, stated as design rules first

⭐ **Every subsection below states the engineering rule before naming its canonical source, and the rule is written to stand without the source.** Strike every Pāli term from this section and the design survives entire. That is the corpus's deletion test satisfied by the section's construction rather than by the authors' assurance — a property, not a promise.

```
   MECHANISM                       ENGINEERING FORM              NOVEL?
   ─────────────────────────────────────────────────────────────────────
 1 opening attribution formula →   provenance inline in the       no
                                   text stream, not in metadata   (placement arg.)
 2 assembly recitation         →   admission decided at BUILD     no
                                   time by a named body           (timing arg.)
 3 commentary as a text class  →   never return summary where     partly
                                   source is expected
 4 recensions kept distinct    →   variants served with their     no — this is TEI
                                   witness; never normalise
 5 announced abridgement       →   elision marked inline, at      no
                                   the cut, and recoverable
 6 interpretive standing       →   standing per PASSAGE, since    partly
                                   an excerpt loses front matter
 7 scheduled re-verification   →   public, before an assembly,    weakest claim
                                   silence load-bearing           in the set
   ─────────────────────────────────────────────────────────────────────
 + recorded exclusion reasons  →   every exclusion published      no
                                   with its occasioning case
   ─────────────────────────────────────────────────────────────────────
   AND SEPARATELY, §5:  the conformance endpoint   ·   the separated
                        completeness manifest       — both believed novel
```

### 4.1 — Provenance travels *in* the text

**The rule.** A unit of served text carries its attribution as part of the text itself, at its head, so that any excerpt of it that survives a copy-paste, a context window, a summarisation or a quotation still carries the attribution. Provenance recorded only in an accompanying field is provenance that a consumer may decline to fetch, and machine consumers decline constantly — not maliciously, but because the field was not in the retrieved span.

**The canonical instance.** Every discourse in the collection opens with the same attribution formula, conventionally rendered *thus have I heard*, followed by the setting and the occasion. It is not a header. It is the first sentence of the text, in the same voice, and it is preserved through every recitation and every copy because removing it would be removing text.

**Against §2.1.** PREMIS, PROV-O and OAIS all solve provenance *representation* better than this does. The narrow claim is placement, and the argument for it is the one in §3.3: a metadata record that the consumer did not fetch does not fail loudly. It fails by absence, and absence is the failure mode this whole paper is about.

**Sig-9 check — property or rule?** Inline is a **property**: the marker survives excerpting because of where it sits, with no enforcer. A metadata field is a **rule**: it survives because something remembered to fetch it. This is the clearest instance in the paper of the institution's own take-the-fix-from-the-object test, and it is why §4.1 leads.

### 4.2 — Admission is decided at build time, by a named body, under a recorded procedure

**The rule.** What is in the corpus is settled when the corpus is assembled, by an identified group following a procedure that is written down, and the decision is recorded. It is not settled at query time by a filter. A query-time gate has an operator, and an operator can be leaned on per request; a build-time gate produces an artifact that either contains a document or does not, and the containing is checkable by anyone.

**The canonical instance.** The councils, whose procedure §3.2 describes: recitation by an elder, chorus by the assembly, compilation **only on unanimous acceptance** `[V]`.

**What this is not.** It is not a claim that assemblies produce correct results. §6.1 argues the opposite risk at length. It is a claim about *where the decision sits* and therefore about what can be audited afterward.

**Relation to our own corpus.** *Buddha AI and the Living Tipiṭaka* §8 addresses the adjacent question of who may canonise *new* material and specifies a tiered workflow and periodic councils for it. That is a different question from this one: §8 asks what may enter a canon, this asks how a *served copy* of an existing one is assembled. Both are cited; neither absorbs the other.

### 4.3 — Commentary is a distinct class, and the server therefore never summarises

**The rule.** If a corpus distinguishes primary text from commentary on it, a retrieval layer over that corpus must serve them as distinct classes and must never return generated prose in the position where primary text is expected. A summary is not a shorter version of a text. It is a *different text*, of unknown provenance, and it cannot be hash-verified against anything.

**The canonical instance.** The commentarial layer — *aṭṭhakathā* — is a separate class of literature with its own transmission and its own standing, never merged into the discourses it explains.

**Why this is partly novel.** The non-summarisation obligation is stated in *Provenance-Carrying Retrieval* as a consequence of hashability. What the canonical structure adds is a stronger and independent reason: **the tradition maintained the separation even though merging would have been enormously convenient**, precisely because a reader needs to know which layer they are standing on. The convenience argument for merging is exactly the argument for returning a summary, and it was declined for two thousand years by people with better reasons than ours.

### 4.4 — Variants are served with their witness, never normalised

**The rule.** Where the corpus has divergent readings, serve them as divergent, each with the line of transmission it came through. Do not silently pick one. Do not merge them into a smoothed text. A consumer that receives a normalised reading has been told a lie of omission that it has no way to detect.

**The canonical instance.** The recensions preserved by different reciter lineages, whose variant readings are attributable to those lineages `[V]`, and whose differences the commentarial literature records rather than resolves `[V]`.

⚠️ **Novelty: none.** This is the TEI critical apparatus, and before it Lachmann and Greg–Bowers. §2.4 says so. The only contribution is the observation that machine-facing retrieval has not adopted it and is the setting where its absence costs most — because a human reader of a smoothed text can suspect smoothing, and a model cannot.

### 4.5 — Abridgement is announced inline, and is recoverable

**The rule.** When served text is abridged, mark the cut *at the cut*, in the text, in a form that identifies what was removed well enough to reconstruct it. Do not record the abridgement in a field. Do not abridge silently, ever.

**The canonical instance.** The elision marker — *peyyāla*, abbreviated in practice to a short particle `[V]` — which stands in the text where a formulaic passage recurs, indicating that the passage is to be supplied. ⭐ **The precision matters and this paper states it rather than glossing over it:** the marker does not signal *arbitrary omission*. It signals a *recoverable repetition*, and its usefulness depends entirely on that. An elision marker that says only "something was here" is decoration; one that says "the passage you already have, repeated" is a compression scheme with an integrity property.

**The engineering form is therefore narrower than "announce elisions"**: announce them in-band, at the point of the cut, with sufficient information to restore. That is a real constraint and most truncation in retrieval systems fails it.

### 4.6 — Interpretive standing is carried per passage

**The rule.** Whether a passage should be read as stating its meaning directly, or as requiring inference, is a property of the passage. It must travel with the passage. Document-level front matter does not survive retrieval: a system that returns an excerpt has, by construction, dropped the document's `status`, `revised` and genre fields, and the excerpt now reads as though it carried the document's authority.

**The canonical instance.** The distinction between a statement whose meaning is drawn out — *nītattha* — and one whose meaning is to be inferred — *neyyattha* `[V]`. The tradition treats the *misclassification* as the serious error in both directions: explaining an inference-requiring statement as though it were direct, or a direct statement as though it required inference, is characterised in the same passage as a misrepresentation of the teacher `[V]`.

⭐ **That symmetry is the useful part and it is not obvious.** The engineering instinct is to worry only about over-claiming — treating a hedged passage as settled. The canonical rule says the *other* direction is an equal error: treating a settled passage as open to inference is also a misrepresentation. Transposed, that forbids a retrieval layer from marking everything provisional as a defensive posture. **Blanket hedging is a correctness failure, not a safe default.**

**Locus note.** The passage pair is cited in this corpus as AN 2.24–25; enumeration of this collection's early books differs between editions and a reader may encounter it under another number. See §11.

### 4.7 — Scheduled public re-verification, in which silence is load-bearing

**The rule.** Integrity is re-affirmed on a fixed, public, predictable schedule, before an assembled audience rather than to a log. The affirmation is solicited a set number of times. **Silence constitutes a positive assertion of integrity, and the silent party is accountable for it.**

**The canonical instance.** The fortnightly recitation of the disciplinary code — *pāṭimokkha* — before the assembled community on the full and new moon `[V]`. The community is told that one who has committed an offence should declare it and one who has not should remain silent, and that *from your silence I shall understand that you are pure* `[V]`. The question is put three times, and **failing to declare a remembered offence after the third asking is itself an offence** `[V]`.

⭐⭐ **That last clause is what makes the mechanism more than a health check, and it is the reason this subsection exists.** An unanswered health check is ambiguous: the service may be fine, or unreachable, or lying. Here silence is *defined* as an assertion and is *penalised* if false, which converts an absence into a signal with a cost attached. A monitoring system that treated "no response" as "healthy" would be badly designed; a monitoring system in which "no response" is a *signed* claim of health is a different thing entirely.

⚠️ **This is the weakest claim in §4 and the paper marks it as such.** The engineering form — periodic signed attestations of integrity, published, with liability for a false attestation — exists in the transparency-log world already, and the addition of *an assembly* is precisely the part §9.3 argues may not transpose at all.

### 4.8 — Every exclusion is served with its recorded reason

**The rule.** A corpus that excludes material publishes, alongside each exclusion, the case that occasioned it — and the subsequent amendments and exceptions, so the exclusion set has a history rather than a state. An exclusion list is an assertion; an exclusion list with reasons is auditable.

**The canonical instance.** Each disciplinary rule is preceded by its origin story — the specific incident that prompted it — and followed by the amendments the rule accumulated as new situations arose, together with exceptions marking what is *not* a violation `[V]`. Further cases function as judicial precedent `[V]`.

⭐ **The amendment history is the part the destination field usually drops.** Archives commonly publish a takedown policy; they rarely publish, per removed item, the case that caused the rule to exist and the successive refinements to it. That is the difference between a policy and a case law, and a corpus that will outlive its curators wants the latter.

---

## 5 · The two designs that are not transpositions

§2.6 subtracted the paper down to what is left. These two are the substance of it.

### 5.1 — ⭐ The conformance endpoint

**The problem a hash does not solve.** A machine reader that verifies a quotation against a content hash learns exactly one bit: matched, or did not. That bit is nearly useless in the case that actually occurs. A model quotes a passage it half-remembers, or a user pastes a quotation from a third-party site, or an agent carries a citation forward from a prior turn. The hash fails. And now what? The failure is indistinguishable between *the quotation is fabricated*, *the quotation is real but from a different recension*, *the quotation is real and this corpus has been tampered with*, and *the quotation is a faithful paraphrase that was never a quotation at all.* **A hash reports that a comparison failed. It says nothing about what to do next, and it therefore cannot prevent the single most common downstream behaviour, which is to shrug and use the text anyway.**

**The mechanism.** An interface that accepts a *claimed* text — not a hash of it, the text — lays it alongside the served corpus, and returns a **disposition on the claim** together with the procedure the requester should follow. The disposition set is small and closed, and the point of the design is that each member names a different next action:

```
   CLAIMED TEXT ──▶ [ conformance ] ──▶ disposition + next action
                          │
                          ├─ CONFORMS ............ served text; cite it
                          ├─ CONFORMS, VARIANT ... served text + the witness
                          │                        this reading came through
                          ├─ NOT FOUND ........... this corpus does not
                          │                        contain it; do not
                          │                        attribute it here
                          └─ CONFLICTS ........... a text of this identity
                                                   exists and differs; here
                                                   is the difference
   ⛔ NOT IN THE DISPOSITION SET, BY CONSTRUCTION:
      any statement about the party that made the claim.
```

**The canonical source, and it is unusually exact.** The four great references — *mahāpadesa*, given in the account of the teacher's last days and again in the numerical collection `[V]` — instruct that when someone claims to have received a teaching, the words are to be neither approved nor rejected on the spot, but **carefully learned and laid alongside the discourses and the discipline** `[V]`. If they do not accord, the conclusion to be drawn is stated — and the striking part, verified directly against the passage, is *what* the conclusion is about. The disposition is that **the claim has been misunderstood and is to be discarded**; the text prescribes no judgement of, and no penalty on, the person who brought it `[V]`.

⭐⭐ **That separation is the design.** A verification interface that returns a verdict on the *claimant* creates an incentive not to submit claims, which destroys the mechanism's coverage exactly where coverage matters. A verification interface that returns a verdict only on the *claim* is safe to use, and therefore gets used. It is a small distinction and it is the entire difference between a conformance service and a reputation service.

**Why it is offered as novel.** We can find no retrieval, archival or attestation system that exposes this. Hash verification is universal. Text similarity search is universal. Neither returns a *disposition with a prescribed next action*, and neither draws the claim/claimant line as a structural property of the response schema. C2PA comes closest in spirit — its validation reports say what could and could not be verified — but it validates an asset's own manifest rather than adjudicating a third party's claim about a corpus.

**Sig-9 check.** The claim/claimant separation is a **property** if the disposition set has no member that can carry a verdict on a person, and a **rule** if the operator is merely asked not to add one. It must be built the first way. ⛔ *Remove the enforcer: if the schema permits a claimant field, someone will populate it under pressure, and the mechanism becomes a denunciation channel.*

### 5.2 — ⭐ The separated completeness manifest

**The problem transparency logs do not solve.** Certificate Transparency and its descendants prove that a log is append-only and that a given entry is in it. **They do not prove that the log contains everything it ought to contain.** An operator who never adds a document has added no dishonest entry; every inclusion proof still verifies; every consistency proof still verifies. Omission is invisible to the entire apparatus, because the apparatus reads what was *produced*, and a document that was never produced produces nothing to read.

⚠️ **This is the sharpest form of an instrument failure the institution has recorded repeatedly in its own operations: every check reads an artifact, so no check can report a thing that was never made.** An unstamped document, a workflow that never ran, a field nobody wrote — each is invisible to the check that would have caught it. The log is the same shape.

**The mechanism.** Publish, as an artifact **distinct from the index**, a signed enumeration of a collection's membership and its **cardinality**, so that a third party holding the manifest alone can detect a document's silent removal. The separation is the mechanism, not an implementation detail: **an index cannot attest to its own completeness**, for the same reason a witness cannot corroborate themselves. If the manifest lives inside the index, an operator who removes a document removes its manifest line in the same edit and nothing anywhere disagrees.

**The canonical source.** The mnemonic summary verses — *uddāna* `[V]` — placed at the end of each section and of the whole work. Their function is precisely this: they key off each member of a group, fixing **membership and ordering** `[V]`, and the summaries at the end of a work give **the names and the counts** — of the elders, of the verses in each chapter, and of the whole `[V]`. They were memorised alongside the text by the reciters `[V]`.

⭐ **Two details of the canonical form are load-bearing and both were confirmed rather than assumed.** The summaries carry **counts**, not merely names — cardinality is what makes a removal detectable when a name is also removed. And they are **separate units**, positioned at the boundary of the collection rather than distributed through it, which is what allows a carrier to hold the manifest without holding the collection.

**Against §2.3.** CT gives append-only-ness and split-view detection; the manifest gives completeness against a *declared* expectation. They compose, and neither substitutes for the other. The honest statement of the residual is that the manifest moves the trust problem rather than dissolving it — a signed manifest is only as good as the key that signed it and the party that published it — and §9.5 says so.

**Sig-9 check.** Separation is a **property** when the manifest is signed by a different key and published by a different party than the index. It degrades to a **rule** the moment the same operator holds both, at which point it detects accident and not intent. ⚠️ *This is a real limit and it means the manifest is worth much less inside a single-operator system than it looks.*

## 6 · What must not be inherited

⛔ **A transposition that finds every mechanism inheritable is doing apologetics.** Two of the seven carry capture surfaces, and naming them is claimed in §Claims 13 as a design element of this paper rather than as a caveat on it.

### 6.1 — The assembly's power to exclude

§4.2 argued for a build-time gate operated by a named body. The same mechanism, viewed from one step back, is **an assembly with the power to decide what does not exist.** The second council ended in schism `[V]`, and a schism is what an exclusion looks like from the excluded side.

This institution's own doctrine refuses exactly this shape elsewhere: a guard that depends on the good behaviour of whoever holds it at the moment it is tested is a rule, and rules need a living enforcer with the right incentives at the exact moment nobody can guarantee. **An admission body is a rule wearing a procedure's clothes.**

⭐ **The available guard is §4.8, and it is only partial.** Serving every exclusion with its occasioning case and its amendment history makes the exclusion set auditable, which raises the cost of a bad exclusion without preventing one. **We state plainly that we do not have a property-shaped fix for this and are not claiming one.** The honest position is that a served corpus with a curated boundary has a governance problem that no amount of cryptography touches, and that the corpus should say so on its own surface rather than let the presence of hashes imply otherwise.

### 6.2 — The authority to rule on interpretive standing

§4.6's per-passage standing field is useful and is also a lever. Whoever sets the field decides which passages are to be read as they stand and which are open to inference — and the second category is where interpretation lives. An operator who can mark a passage as requiring inference can, without altering a byte, change what the corpus is understood to say.

⚠️ **Two guards, and the paper is honest that they are mitigations rather than solutions.** The field must be **inside the hashed text**, so that changing it drifts the hash and rotates the proof, making the change as visible as an edit — because it *is* an edit. And the corpus must serve the standing field's own **change history** under §4.8, so a reclassification is as auditable as a removal.

**Related and separate:** the guard that a reciter is not the author of what is recited is claimed and argued in *The Song That Is Not His* and is **cited here rather than re-claimed**, per the placement rule. It bears on §4.6 in an obvious way and this paper adds nothing to it.

### 6.3 — The general form

Both refusals have the same shape and it is worth stating once: **the mechanisms that handle *bytes* transpose cleanly, and the mechanisms that handle *authority* do not.** Inline markers, manifests, variant witnesses, announced elisions and conformance dispositions are all properties of artifacts. Admission and interpretive standing are properties of a body politic, and importing them into a served corpus imports a governance question that the corpus's cryptographic apparatus is entirely powerless to answer — while, dangerously, *looking* as though it has answered it.

## 7 · The threat-model partition

The transposition's most likely misuse is to treat these mechanisms as a complete integrity story. They are not, and the reason is a clean partition that the paper states early enough to be useful.

```
   ORAL TRANSMISSION FEARS          A RETRIEVAL SERVER FEARS
   ──────────────────────────       ─────────────────────────────
   drift        (slow mutation)     substitution  (swap the text)
   forgetting   (loss of a          fabrication   (invent the text)
                 lineage)           silent normalisation
   ──────────────────────────       ─────────────────────────────
              │                                │
              ▼                                ▼
   an uddāna detects OMISSION       a hash detects TAMPERING
   a bhāṇaka group detects DRIFT    an anchor detects BACKDATING
              │                                │
              └──────────► NEITHER IS ◄────────┘
                          SUFFICIENT ALONE
```

**An enumeration detects omission and cannot detect tampering. A hash detects tampering and cannot detect omission.** They are complements, and a system with only one of them has a hole shaped exactly like the other. That partition is the practical reason the two designs of §5 are worth having *together with* the envelope of *Provenance-Carrying Retrieval* rather than instead of it.

⚠️ **The partition also bounds the field-test claim.** The canon's mechanisms were selected against *its* threat model, not ours. Where the two models overlap the transposition is well-motivated; where they do not, the canonical practice is evidence of nothing about our case, and §4 marks which is which.

---

## 8 · Where this sits against the rest of this corpus

Stated explicitly because a corpus that cross-references loosely is a corpus whose reader cannot tell what is claimed where.

| Paper | Its question | Why this one is not it |
|---|---|---|
| *Provenance-Carrying Retrieval* | how does a response carry the means of its own falsification? | that paper builds the **envelope**; this one asks what a long field test selected for, and supplies two mechanisms the envelope does not contain (§5) |
| *Buddha AI and the Living Tipiṭaka* §8 | what makes a canon **authoritative**? | authority over *new* material, decided by a doctrinal body; this paper is about the integrity of a **copy** of existing material |
| *The Borrowable Standard* | what does a corpus need before it can exist? | orthography and encoding — upstream of this paper and disjoint from it |
| *The Song That Is Not His* | who is the author of a recitation? | owns the reciter-is-not-author guard; **cited in §6.2, not re-claimed** |
| *The Last Carrier* (essay) | what has carried this canon, and what carries it now? | the founder's voice, the media chain, and the observation about fragility that §3.1 cites |
| *The Persistence Architecture* | can an apparatus be built so its author can stop? | succession, not transmission integrity |

⭐ **The residue owed elsewhere.** *Provenance-Carrying Retrieval*'s prior-art section currently cites PREMIS, PROV-O, LOCKSS, Memento and Software Heritage and stops, on the line that the archival community has thought about this longer than the machine-learning community has. **The extension — that an oral canon thought about it longer still — is a two-sentence cross-reference belonging to that paper, not a section transplanted from this one.** It is queued against that paper's next revision.

## 9 · Honest limits

*This section contains no canonical material and makes no appeal to tradition. That is deliberate and is the corpus's standing rule for honest-limits sections.*

### 9.1 — Everything here is a detection claim

Restated from §3.3 because it is the limit most likely to be lost in citation. **None of these mechanisms prevents corruption.** They make divergence detectable and attributable. A corpus running all eight can still serve a wrong text; what it cannot easily do is serve a wrong text *silently*. Any use of this paper that implies a correctness guarantee is a misuse, and the paper's own field test is the evidence — the tradition ran this apparatus for two millennia and ended with branches, not with one text.

### 9.2 — Survivorship, at n = 1, over two thousand years

We observe the canon that survived. The claim that these mechanisms *caused* its survival is not testable: there is no control, no comparable case, and no record of the traditions whose apparatus failed. **This is unfalsifiable at n = 1 and the paper does not argue around it.** What survives the objection is narrower and is what §Claims 1 actually says: the mechanisms are *legible as engineering* and have forms worth using on their own merits. Their canonical provenance is a reason to look, never evidence that they work.

### 9.3 — The fitness function was not textual accuracy alone

Sharper than survivorship, and it is the objection we would raise against this paper. The councils had royal patronage; the collections that survived are substantially the collections that had institutional and political backing. **A field test whose fitness function included state support may have selected for political durability, with the textual mechanisms partly along for the ride.** We cannot separate the two. The consequence is stated as a bound on the whole paper: what is offered is **provenance of design — an account of where these ideas come from and why they are worth considering — and never proof of efficacy.**

### 9.4 — Five of the eight are social protocols, and their engineering forms are half the mechanism

§4.2, §4.4, §4.6, §4.7 and §4.8 all presuppose a body of people: an assembly to admit, lineages to preserve divergence, an authority to assign standing, a community to recite before, a tradition to record precedent. **A scheduled re-verification with no assembly to verify before is a cron job talking to itself** — and it is worth saying that this is the paper's own strongest objection to itself, not one an outside reader had to supply.

This bites hardest on §4.7, which is why that subsection is marked as the weakest claim in §4. It bites least on §4.1 and §5.2, which are properties of artifacts and need no one present. **The ranking is the useful output: prefer the mechanisms that survive the removal of the community, and treat the rest as governance proposals wearing engineering clothes.** For this institution the assembly in question is a designed one whose seating is argued elsewhere and is not assumed here.

### 9.5 — The manifest moves the trust problem rather than dissolving it

§5.2's separation is only as good as the independence of the two publishers. In a single-operator deployment — which is what `corpus.333.eco` currently is — the same party holds the index and signs the manifest, so the mechanism detects **accident and drift, not intent.** That is worth having and is far less than it sounds. The design reaches its full strength only with an independent signer, and we do not have one.

### 9.6 — What is actually deployed

Stated so the reader can weigh the rest. `corpus.333.eco` is live and serves the institution's corpus with a provenance envelope. **Of the mechanisms in this paper, the ones with running code are §4.1's inline markers and parts of §4.3's class separation.** §4.2 runs as a build step with a single human operator, which satisfies its letter and not its spirit. **§5.1 and §5.2 — the two designs the paper offers as novel — are not built.** They are specified here at claim scope for exactly that reason. The Tipiṭaka server that would exercise the full set has no date.

⛔ **A reader should treat every efficacy statement in this paper as design reasoning, not as a report of operation.**

### 9.7 — The citation standard, stated rather than assumed

Every canonical locus is marked `[V]` where it has been checked against multiple independent public reference works and translations. **No locus has been checked against the Pāli by a reader of Pāli**, and the authors do not read Pāli. §11 gives the full status and names the check that is owed. A paper about checkable provenance that left its own sourcing standard implicit would be refuted by its own thesis.

### 9.8 — The coherence is not evidence

The mechanisms fit together well. Eight parts of an old apparatus mapping cleanly onto a modern problem is exactly the kind of pattern that is either deeply right or deeply seductive, and the two are indistinguishable from inside. **Each mechanism is individually arguable and should be argued individually; the elegance of the set earns an experiment and does not replace one.** ⛔ The fit between the parts is not evidence for any of them.

## 10 · Adversarial analysis

**A manifest that was always short.** An operator publishes a manifest omitting a document that was never admitted. Nothing detects it — the manifest is internally consistent and the document has no trace anywhere. ⛔ **This is not solvable by the manifest and §5.2 does not claim it is.** It is the omission problem one level up, and its only real answer is §4.2 plus §4.8: an admission decision made by an identified body and published with its reason. That answer is governance, not cryptography, and §6.1 says it is unsolved.

**Collusion between index and manifest signer.** Addressed in §9.5. Under a single operator the separation is hygiene. Its value is a step function in the number of genuinely independent signers, and the step from one to two is the largest.

**The conformance endpoint as an oracle.** An adversary submits many near-miss texts to learn precisely how close a forgery must be to pass. This is real and it is bounded by the design: the endpoint compares against a corpus whose full text is *already public*, so the oracle reveals nothing the adversary could not obtain by reading. ⚠️ **The analysis changes completely for a corpus with non-public members, and a deployment over one should not expose this interface.**

**The conformance endpoint as a cost surface.** Text-in comparison is more expensive than hash-in comparison, and an interface that accepts arbitrary text invites abuse. This is an ordinary engineering problem with ordinary answers and is noted only so that the paper is not read as ignoring it.

**Variant proliferation.** §4.4 refuses to normalise; an adversary submits many spurious "variants" to drown the real ones. The guard is that a variant is served **with its witness**, and a witness is an attested line of transmission rather than a submission. ⚠️ **This makes witness admission the attack surface, which returns to §6.1.** The paper's honest summary is that three of its five adversarial cases terminate in the same unsolved governance problem, and that a reader should regard §6.1 as the real open question rather than a section of caveats.

### 10.6 — Why this paper registers no predictions

The corpus's standing practice is that a paper making an empirical claim registers falsifiable
predictions in the public register. **This paper registers none, and the reason is the honest one
rather than an oversight.** §9.2 and §9.3 disclaim efficacy explicitly: what is offered is
provenance of design, not evidence that these mechanisms work, and a survivorship case at n = 1 over
two thousand years supports no prediction that could fail. The design claims in §4 are arguments,
and arguments are refuted by better arguments rather than by data.

⭐ **One prediction becomes clean the moment §5.1 is built, and is named here so that it is not
invented after the fact:** that a conformance response carrying a *disposition and a prescribed next
action* produces a higher rate of citation correction, by an agent that has received a failing
verification, than a bare match/no-match response does. That is a comparison between two response
schemas over the same corpus, it has an obvious null, and it is measurable. ⛔ **It is not registered
now, because registering a prediction about an unbuilt interface is exactly the unclean registration
the register's own rules bar.** It is owed at the point §5.1 has running code.

## 11 · Citation status — what has been checked, and by what standard

⭐ **This section exists because the paper argues that unchecked claims must be visible, and it would be self-refuting to make its own an exception.**

**Standard applied.** Each locus was checked against multiple independent public reference works, translations and encyclopaedic sources, and is marked `[V]` in the text where that check passed. Checks confirmed both the *location* (which text contains the material) and, where the paper leans on it, the *content* (that the passage says what the paper says it says).

**Checked and passed:** the four great references and their prescribed procedure, including the finding that the disposition falls on the claim and not on the claimant (§5.1) · the councils' recitation procedure and the unanimity requirement (§3.2, §4.2) · the reciter lineages, their specialisation by collection, the attribution of variant readings to different lineages, and the Sri Lankan cave-inscription evidence (§3.1, §3.3) · the mnemonic summaries' function in fixing membership, ordering and counts, and their placement at section boundaries (§5.2) · the elision marker and its recoverable-repetition sense (§4.5) · the fortnightly recitation, the threefold question, silence as an assertion of purity, and concealment after the third asking being itself an offence (§4.7) · each disciplinary rule's origin story, amendments and exceptions (§4.8) · the explicit/inference-requiring distinction and the symmetry of the error (§4.6).

⚠️ **One conflation was caught by this process and is recorded because it is the class of error the remaining check exists to find.** The mnemonic index verses of §5.2 — *uddāna*, with a doubled consonant — are a **different word** from *udāna*, the inspired utterance, which is a genre in the traditional list of text-types and the name of a book of the canon. The two are one diacritical difference apart, and a paper that confused them would have attributed the completeness mechanism to the wrong thing entirely.

⛔ **What this standard does NOT establish, stated at its true size:**

1. **No locus has been verified against the Pāli by a reader of Pāli.** The checks are against translations and reference works. They establish bibliographic and substantive accuracy at the level a careful non-specialist can reach, and no further.
2. **Glosses are not verified.** Where the paper renders a term into an engineering concept, that rendering is the authors' and may not be how a specialist would read it. The *uddāna* case shows the failure mode is real.
3. **Enumeration varies by edition.** §4.6's locus is cited as this corpus cites it; a reader working from another edition may find it numbered differently.
4. **Nothing here has been reviewed by the tradition.** The material is read as engineering by people outside the community of specialists who carry it, and a specialist may reasonably object to the reading itself and not merely to a citation.

⭐ **The check that is owed, and by whom.** Each locus should be confirmed by a reader of Pāli — for this institution, the founder's father, who is the transcription authority named in this corpus, or the Aquarian Sangha. The ask is small and specific: confirm that each cited passage says what this paper says it says. **Until that is done, this section is the paper's honest state and not a formality**, and a reader who finds an error is asked to treat §5.1's own disposition rule as applying here: the finding is about the claim.

## 12 · Cross-venue references

*Provenance-Carrying Retrieval* (the envelope; §5's mechanisms extend it) · *Buddha AI and the Living Tipiṭaka* §8 (canonical authority, distinguished in §4.2) · *The Borrowable Standard* (orthographic and encoding preconditions) · *The Song That Is Not His* (the reciter-is-not-author guard, cited in §6.2) · *The Last Carrier* (essay; the fragility observation in §3.1) · *The Persistence Architecture* (succession, adjacent and distinct) · *Appreciation as World-Building* (the property-over-rule argument used in the Sig-9 checks throughout §4 and §5).

## Coda

The people who built this apparatus were not trying to solve a retrieval problem. They were trying to keep something they thought was worth keeping, under conditions that gave them no reason to expect success, using the only storage medium available to them, which was each other. They lost material. They disagreed, sometimes bitterly, and the disagreements are still legible in what came down. By any standard a modern engineer would apply to a storage system, the thing failed continuously for two thousand years.

And it is still here, and we can tell where it differs from itself, and we can often tell whose hands each difference came through.

That is the result worth taking. **Not a system that did not fail — there is no such system — but a system that failed loudly enough, and with enough attribution attached, that the failures are still auditable twenty centuries later.** Every mechanism in this paper is in service of that one property. It is a smaller promise than the word *integrity* usually implies, and it is the only promise anyone has ever actually kept.
