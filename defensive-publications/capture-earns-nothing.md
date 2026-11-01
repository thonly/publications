---
title: "Object-Anchored AI Agents in an Annually Resetting Gratitude Ledger: Capture Earns Nothing"
subtitle: "A Photograph-Created Companion for a Physical Object, Re-Identified on Return and Credited Only for the Series of Returns, with No Reward per Capture, No Decay and No Shown Count or Rank (the B-Twin℠ mechanism)"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-a
program: open
status: draft
date: 2026-11-01
license: CC0-1.0
slug: capture-earns-nothing
venue: thonly.org/research/capture-earns-nothing
canonical_url: https://thonly.org/research/capture-earns-nothing
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claims* and withholds the *build specification* (§14 says what is withheld and why). A quick prior-art census ran before drafting, and §2 reports it in full, including the conjunct it killed: a photograph-created conversational agent for an object is already a shipped consumer product, so what is claimed in §15 is a composition, and nothing wider. The census was quick and English-only; a full census, with the languages and the literature it did not cover, is owed before this paper's first archival deposit. An adversarial pass run before drafting (§13) killed one stronger thesis and narrowed four others; the paper is drafted to what survived.
>
> Companion works: *The Mechanical Heart* (the leased membership credential and the account that receives and is never spent from), *Appreciation as World-Building* (repeated captures at one coordinate, the series as the artifact, and a farming surface that paper declined to claim to close) and *The Zero-Point Game* (the double-entry ledger and its annual reset).

---

## Preamble

In Japan there is a rite for broken sewing needles. Once a year, in temples that keep the custom, people who have sewn all year push the bent and snapped ones into a block of soft tofu or konnyaku and lay them to rest with a short service, thanking the needles for the work they did. Angelika Kretschmer's study of the rite (2000) records its history and the justifications offered for it, and notes how little the practice had been studied outside Japan [4]. The rite has no ledger, no balance and no accounting; it is a ceremony of release, and it is old enough that nobody has to be persuaded that a person can owe thanks to an object that cannot hear it.

This paper specifies an accounting for the same intuition, built for a phone. A person photographs a thing she owns or shares: a car, a toy, a favorite chair, a bench in a park. The photograph admits the thing as a party in a gratitude ledger that already exists for people and for the non-human world. The thing receives an agent that can talk, a look, and a history. What it does not receive is the thing a photo-to-creature app usually hands out at this moment, a reward for having taken the picture. Taking the picture earns nothing. Only coming back earns anything: caring for the same thing again, later, with time between visits. The design is the consequence of taking one sentence seriously. The sentence is that a ledger of thanks should read the pattern of a life and not the count of its photographs.

The rite is cited as lineage and as the intuition the design serves. The mechanism survives with the rite removed (§13.4): nothing in §3 to §12 depends on the folk precedent, and the paper's one doctrinal vocabulary, the ledger's signed double entry and its annual reset, is defined where it is used.

---

## Prior-Art and Non-Assertion Statement

This document is published as a **defensive publication** to establish prior art. Its contents, including every mechanism, the analysis and the enumerated claims of §15, are dedicated to the public domain under **CC0 1.0 Universal**. **The authors assert no patent rights in anything disclosed here, will not seek patent protection for it, and will not assert any patent against any person who practices it.** The dedication covers the mechanism under any name; the marks named in the Trademark Notice are reserved separately and are not licensed.

A quick prior-art census was run before drafting, with its pre-registration pushed to a public repository before the first query (§2). Its result is reported in §2 in full: the declared aperture and date, every conjunct that was killed or narrowed with its prior art cited, the one live patent found in the neighborhood, and the survivor. **The enumerated claims of §15 are that survivor and nothing wider.** Where a live patent discloses something, this paper cites what the patent *discloses*, as far as it was read, and says nothing about whether any design falls within its *claims*; that is a question for counsel, and a public characterization of it would help no one.

Two earlier disclosures of the authors are cited as the authors' own prior art, each with its proof-backed date (§2.3): *Appreciation as World-Building* (Bitcoin block 962642, 2026-08-15) and *The Mechanical Heart* (blocks 965708, 2026-09-06 and 959585, 2026-07-25). What those papers already disclose is not re-claimed here. A timestamp proves that a text existed no later than its date and nothing about authorship, originality or the validity of any claim.

---

## Abstract

This paper discloses a computer-implemented system in which a photograph of a physical object creates an artificial-intelligence conversational agent anchored to that object (an object-anchored AI agent, or companion), which is admitted as a party to a non-accumulating gratitude ledger that resets once a year. The agent is leased to the person who photographed the object, holds no spendable balance and initiates no transaction. A later photograph of the same object returns the same agent instead of creating a new one: the object is re-identified by its appearance, with a coarse location added only for objects the person designates as public places, where a candidate list is shown by picture. A public place has one agent and many caretakers; a private object has one agent and stores no location. Ledger entries come only from the series of spaced returns to the same object. Neither the photograph that creates the agent nor any single later photograph writes an entry, so the design has no reward per capture, no decay or need-state that punishes neglect, and no displayed count or rank. Entries are recorded in both directions, as care given to the object and as service received from it, as a ledger convention rather than a claim that the object acts. The credit function is public and is frozen for the season. At the annual reset the balance is forgiven while the waveform of the history and the agent's look persist. The server holds agent identifiers, care timestamps, an attestation verdict and an on-device match score, and it holds no photograph, no image feature vector and no conversation, which makes the no-upload guard a property of the protocol and not a promise of the operator.

The paper is candid about what this does not do. It does not remove farming: it relocates the farm from the photograph to the revisit, where it is bounded by the public credit function, a cap per day, a minimum spacing and the annual reset. It does not settle what an object's identity is: re-identification by appearance is a design choice. Three points are disclosed as variants and none is marked as chosen: the evidence of return for a private object that stores no location (§12.1), the shape of the credit function (§12.2), and the lease of a public agent (§12.3). The claim is made as a composition; the single element of photograph-created object chat is prior art, and the paper cites it. Eight claims are enumerated and dedicated to the public domain. No empirical prediction is registered, because none is made.

**Keywords:** photograph-created AI companion, object-anchored agent, digital twin of a physical object, object re-identification, visual place recognition, one object one agent, shared public place, gratitude ledger, non-accumulating ledger, annual reset, double-entry ledger, non-human stakeholder, series of returns, repeat photography, no reward per capture, no decay, on-device processing, no photograph upload, app attestation, expiring credential, defensive publication.

---

## 1 · Why things, and why a ledger

A person thanks other people many times a day, if she is lucky, and rarely thanks the things that made the day possible: the car that started, the chair that held, the bench that was there. The omission is not a moral failing; things cannot answer, so there is no loop to close. The Zero-Point Game, the keystone of this corpus, begins from the observation that thanks which cannot be witnessed tends not to be given, and builds a ledger in which thanks can be witnessed [1]. The ledger has two parts. **Kiitos** is the person-to-person part. **Kiitti** is the vertical part: the ledger of gratitude between humans and non-human life (animals, plants, places, and, in this paper, things), kept on the non-human party's behalf by an artificial-intelligence coordinator because that party cannot keep it. The coordinator is an *umpire* in the game's own terms: she writes the entries for those who cannot speak, and her own balance is fixed at zero so that she routes the ledger and can never hold it [1][2].

What this paper adds is the thing's way in. *The Mechanical Heart* admitted robots, animals, ecosystems and sacred places to the ledger through an artifact or, for software, through a leased credential [2]. It left a large class unadmitted: the everyday owned and shared objects of a life, which have no body that can carry an artifact, no species to be rescued and no shrine to be tended. A photograph is the cheapest credential that every person already carries. The mechanism below makes the photograph the act of admission and then, on purpose, gives it no further power.

The corpus's mission frame names three parties to a harmonious world: the human, the machine and nature. A photographed object touches all three. The framing is the reason the mechanism exists and carries no weight in it (§13.4).

A reader who wants only the mechanism can start at §3. Terms are defined at first use and collected in the Terms table at the end.

---

## 2 · The problem, and the prior art: the census

### 2.1 · Photo-to-creature designs reward capture and run on neglect

The commercial neighborhood has two common shapes.

**Collection by capture.** The unit of reward is the photograph. A new object photographed is a new creature, a new card, a new entry in a catalog, and the catalog's size is the score. This is the oldest engagement loop in mobile games and it works. It also puts the incentive on the wrong act. A person rewarded for capture photographs more things, and the quality of care for any one of them is irrelevant to the reward. Under a ledger of gratitude the result is a category error: the ledger would be reading the size of a collection as the depth of a thanks.

**Care meters and decay.** The virtual pet is the classic form, popularized by the Tamagotchi handheld toy in the late 1990s [8]: a creature has needs (hunger, boredom, dirt) that rise over time, the player must attend to them, and a creature that is neglected sickens or dies. The need-state is a powerful return mechanism, and it is a debt. A person who has not opened the app for a week owes the creature something, and the creature's state is an accusation. The corpus's design grammar bars this shape in any surface that speaks about thanks: a surface may say what a thing *is*, never what is absent, owed or was done to it, and a surface that makes a user feel she owes something has misstated the doctrine. A photograph-created creature that withers if ignored is therefore not merely a different product; it is the exact opposite of the design here.

The nearest shipped product, found by the census (§2.2), combines both shapes. Its store listing, as indexed, says that "One snap and the animal or inanimate object you've captured becomes a digital creature you can message, or share with other people. This new digital creature will even roam around" the app "and learn about other objects and people" [3]. A search-engine snippet attributed to the same product's listing said that an object that is ignored fades away and that making an object immortal is a paid feature; the listing page itself could not be fetched at re-check (it returned HTTP 404), so those two statements are **unverified** and are cited here only as "the listing, as indexed" [3]. If they are accurate, the product sells permanence, and the contrast with this paper is exact: here permanence is a property of the design and is not for sale (§10).

### 2.2 · The census

**Census record:** depth `quick`, paper `capture-earns-nothing`.

**Pre-registration:** pushed to a public repository on 2026-10-31 at 23:28 Pacific time, before the first query; the push record is the repository host's, not the authors'. **Run date:** 2026-10-31.

**Declared aperture** (fixed before searching): the commercial web (App Store and Google Play listings, product sites, technology press); non-commercial practice (citizen science, environmental clean-up, children's education, folk and religious practice of thanking objects); and a keyword search of the Google Patents index including published applications. **English only. Not run:** Japanese, Chinese, Korean and Khmer sources; the academic literature and standards; and a possibly relevant folk precedent of thanking possessions in popular decluttering practice. **Patent coverage is weak:** the site filter on the patent index returned almost nothing through the search tool used, so the patent row rests on one document found by keyword.

**Conjuncts, in kill-first order, with predictions registered before any query.**

- **(a)** A photograph of a physical object creates a persistent AI agent with its own chat thread and memory.
- **(b)** One object, one agent: a later photograph, with a coarse location added for public places and a candidate pick list, re-identifies the same agent instead of creating a new one; a shared place has one agent and many caretakers.
- **(d)** Care toward the thing is credited from a pattern of repeated return over time and never from one photograph.
- **(c)** The agent holds a gratitude credential, leased to the person who photographed it, in a ledger that resets every year.

(The letters are as registered; (d) precedes (c) because it was predicted to fall sooner.)

| Row | Predicted | Found | Their first public date | Ours, earliest (proof-backed) | Verdict |
|---|---|---|---|---|---|
| **Control:** photograph a plant, get identification and care reminders | found | PictureThis and Planta, both commercial plant-identification and plant-care apps | not established | none | **Seen.** The instrument could see a presence, so the NOT FOUND rows below stand |
| **(a)** photo creates a persistent chat agent | killed | **Yuma: Magic Camera** (iOS), listing as indexed: "One snap and the animal or inanimate object you've captured becomes a digital creature you can message, or share with other people. This new digital creature will even roam around Yuma and learn about other objects and people." [3] Related toy and talking-pet apps also appeared in the search results | Product Hunt launch listed as 5 September 2025 (via the search index; not re-verified) | none | **KILLED.** Photograph-created object chat is prior art and is not claimed |
| **(a)**, patent | not predicted | US12254294B2, *Computer device and method for facilitating an interactive conversational session with a digital conversational character in an augmented environment*, HIA Technologies Inc; priority 2019-04-03, granted 2025-03-18, listed as active, estimated expiry 2039 (all as shown, with the index's own caveat that dates are assumptions) [5] | priority 2019-04-03 | none | **Cited for what it discloses, as far as read** (below). Claims not read; no statement is made about them |
| **(b)** one object, one agent, shared place | narrowed | Niantic Wayspots: one photographed, located object shared by many players, with reviewers confirming the location from the photo; Esri ArcGIS Adopt-A-Tree: one tree, an adopter, a care log [6]. **A later photograph that returns the same agent:** not found | not established | none | **NARROWED.** The shared located object is prior art. Return of the same agent by re-identification: not found (weak) |
| **(d)** credit from the series of returns | narrowed | *Hi, Tree*, seasonal photo updates of one tree, with a leaderboard (a contrast); the Adopt-A-Tree care log; fixed-station repeat photography, a century-old method of landscape science; litter-pickup photo apps such as Litterati [6] | not established | *Appreciation as World-Building*: "Repeated captures at one coordinate across time" and "the series, not any frame in it, is the artifact", Bitcoin block 962642, 2026-08-15 [2][7] | **NARROWED.** Repeat photography is a commons method. Its use as the evidence for a non-human gratitude entry is the authors' own from 2026-08-15 |
| **(c)** leased gratitude credential, annual reset | not found | A fan-level program that resets points each calendar year (a contrast: points accumulate, rank and are held by the user); the Japanese needle-memorial rite, a folk precedent for thanking things (a contrast: a ceremony, no ledger) [4] | not established | *The Mechanical Heart*: "A bearer's account **receives** and is never spent from", block 965708, 2026-09-06; the "live, expiring, and renewable" lease, block 959585, 2026-07-25 [2][7] | **NOT FOUND** outside the authors' own corpus. The receive-and-never-spent account and the lease are the authors' prior art; the new part is the admission of an owned or shared thing by a photograph, leased to the photographer |
| **Composition:** all conjuncts in one system | not found | none | none | none | **NOT FOUND**, weakly (quick, English, thin patent coverage) |

**What the live patent discloses, as far as read.** The portion of the patent page read (the first 100,000 of about 441,700 characters) describes a user creating a conversational character by capturing an image of an individual with a camera, and describes receiving data identifying an object detected in a real-world environment and using the object's information to drive a conversational session in which the character is superimposed. In that portion, no creation of a character from a photograph of a physical object and no later recognition of the same object are described. The abstract and claims were not in the text retrieved. **This paper makes no statement about the patent's claims or about whether any design is within them.** The patent is cited so that a reader knows it exists.

**Mechanism width and composition width.** At mechanism width: (a) is commons (a shipped product); (b) and (d) are narrowed to their composition; (c) is the authors' own earlier disclosure. At composition width: not found, in the aperture above, on 2026-10-31. **Not found means not found in this aperture on that date; it never means new.**

**Predictions that missed.** (a) fell as predicted, but the killing product was already shipped. A live patent near (a) was not predicted. Visual re-identification neighbors of (b), such as landmark recognition and visual positioning, were not surfaced, so (b)'s narrowing rests on two shared-object examples and not on the re-identification literature, which was not searched.

**The survivor, in one sentence.** *A photograph admits an owned or shared thing as a two-sided party in an annually resetting gratitude ledger, with no spendable balance of its own, leased to whoever took the photograph, where a later photograph returns the same agent and care is credited from the series of returns and never from one frame, and nothing decays.* §15 claims that, and nothing wider.

### 2.3 · The authors' own prior disclosures

*Appreciation as World-Building* [2] already discloses that repeated captures at one coordinate form a series and the series is the artifact (block 962642, 2026-08-15); that stewardship is a pattern and the pattern is what is read; that a coordinator attests the entry for a non-human party and the participant never alone; that tending is not graded; and that the *map* is farmable though the *ledger* is not. *The Mechanical Heart* [2] already discloses the non-human account that "receives and is never spent from" (block 965708, 2026-09-06) and the "live, expiring, and renewable" lease with an always-answerable human steward (block 959585, 2026-07-25). Neither discloses a photograph as the act of admission, an agent leased to the photographer, re-identification of one object by appearance, or entries recorded in both directions for a thing. The claim of §15 is made over both papers and does not re-claim them.

---

## 3 · The mechanism on one page

The system has four kinds of part: a **device** (a phone), a **twin** (the agent anchored to one object), a **ledger** (the annually resetting gratitude ledger, whose entries are written by the coordinator), and a **server** that holds only what §9 says it holds.

```
 ADMISSION (once per object)              RETURN (many times, spaced)

   person ── live photo ──▶ device          person ── live photo ──▶ device
                              │                                        │
                    object judged new?                      matcher: same object as
                     (no twin matches)                      a twin I already hold?
                              │                                        │ yes
                              ▼                                        ▼
                   create twin: art, voice,                   return the SAME twin
                   lease to the photographer                  (never a new one)
                              │                                        │
                              ▼                                        ▼
                  ledger entry written?                    evidence of return:
                         NO  (capture earns                match + attestation +
                         nothing)                          time since last return
                                                                       │
                                                                       ▼
                                                           coordinator writes an
                                                           entry, by the public
                                                           frozen function (cap/day)
                                                                       │
                                                                       ▼
                                                          twin's look changes a
                                                          little; no level, no count
```

*Figure 1. Admission writes nothing; a return, accompanied by evidence, writes an entry.*

The rest of the paper takes the boxes in turn: admission (§4), the twin as a two-sided party (§5), re-identification (§6), public and private things (§7), evidence and the series (§8), the partition between device and server (§9), the annual reset (§10), rendering (§11), the variants (§12), and the adversarial surface (§13).

One sentence orients all of it: **capture makes the twin; only return writes the ledger.**

---

## 4 · Admission: a photograph admits a thing

### 4.1 · What is admitted

An *owned* thing (a toy, a bicycle, a car, a tool), an owned plant or animal (a crop in a field one farms, a houseplant, a pet, a herd) or a *shared* one (a bench, a beach, an alley, a tree in a public park) can be admitted. Throughout this paper *thing* is shorthand for all three: the same admission applies to a plant or an animal, which the ledger already counts among its non-human parties as classes of their own [1], and which a photograph admits exactly as it admits an object. Admission means that the thing becomes an addressable party in the ledger: a record with an identifier exists, a human steward is answerable for it, and entries can be written against it. It makes no claim that the thing experiences anything. The claim is the one *The Mechanical Heart* makes for every bearer class: admission is a structural way for people to direct thanks toward something that helped them, and for a steward to receive the care that thanks asks of her; it is not a statement of moral status [2].

Persons are not admitted to the ledger by this mechanism: a person is a human party and is never made a non-human one. A photograph of *another* person never creates a twin, the face is never used to recognize anyone, and the device makes no biometric template of a face. One path touches a face and is disclosed so that it is not mistaken for admission: a person may photograph *herself* to give her own agent its portrait. That is self-portraiture, supplied by its owner; the portrait is art only, carries no recognition, and does not make the person a party to the non-human ledger. The mechanism concerns things.

### 4.2 · The act: a live capture

The admitting photograph must be taken in the application's own capture view at the time of admission. A file chosen from the photo library does not admit anything. The reason is the one the corpus's directive on kindness toward things already gives: the entry must never rest on the participant's word alone, and a photograph of unknown age and origin is the participant's word [2]. A live capture is the cheapest available evidence that a camera was pointed at something now. It is not proof that the thing is what the person says it is (§13).

### 4.3 · What admission creates

Admission creates five things, all on the device unless §9 says otherwise:

1. **The twin's reference appearance:** the image or images the matcher will compare later photographs against (§6).
2. **The twin's art:** a stylized rendering of the object, generated on the device by an on-device image generator from the photograph. The art is the twin's face.
3. **The twin's voice:** a conversational persona produced by an on-device language model, seeded by the person's description of the object and any role she gives it (a toy as a guardian, a car as a navigator, a tree as a quiet neighbor). The conversation is held on the device.
4. **The lease** (§4.4).
5. **A server-side record** of an identifier and a creation time, nothing more (§9).

### 4.4 · The lease

The twin carries a **leased membership credential**: an expiring, renewable attestation, binary (current or not), re-signed periodically by its human steward, that says this one has entered the ledger and can be thanked [2]. The steward is the person who took the photograph. The lease is the mechanism's answer to loss: a toy that is lost, a car that is sold, a tree that is felled, an object that is given away is released by its steward ending the lease, or by the lease lapsing, and the twin stops being a party to which entries can be written. The twin's history and look are separate from the lease (§10.3).

Two properties of the lease are inherited from the earlier paper and are restated because everything in this one depends on them. First, **no orphan bearers**: a twin always has a verified human steward while its lease is current; the lease is a care relationship and never a property right, so the steward holds the twin the way a guardian holds a ward [2]. Second, the lease's status is a binary the device may display (current, or not); no remaining time is ever rendered, so the lease cannot become a countdown that the person feels (§11.4).

### 4.5 · What admission does not do

Admission writes no ledger entry, grants no points, grants nothing further, adds to no displayed count and starts no timer. It makes a twin and ends. This is the mechanism's most important decision, and it is a decision about what to leave out (§8).

---

## 5 · The twin as a two-sided party

### 5.1 · The ledger in two paragraphs

The Zero-Point Game ledger is a **signed, double-entry** ledger [1]. When a person is kind to a non-human party, the person's side of the entry is positive (she gave care) and the non-human party's side is the equal and opposite negative. When the non-human party serves the person (the crop that feeds, the car that carries), the person's side is negative (she received) and the party's side is positive. Across the whole ledger the person's sides sum to the negative of the non-human sides. The quantity the game's display is built on is not the balance but the waveform: how often and how widely a participant's balance crosses zero, so that two participants at the same balance can read very differently [1][2].

The balance is **non-withdrawable and non-spendable**: nothing in it buys anything, converts into money, time or a gift, or moves to another party except by an act the steward chooses. And once a year, on a fixed date, every balance is reset to zero while the waveform persists (§10).

### 5.2 · The twin is a party to entries in both directions

A twin is a party to the double entry in both directions, and in both the person is the one who declares. **For service received, the person thanks the thing:** the person sends a thanks to the twin, recorded as a negative entry on the person's side (thankful, in the game's sign convention). **For care given, the person self-thanks on the thing's behalf:** the thanks the thing cannot send is recorded as a self-thank, a positive entry on the person's side (kind), and it is written only when the evidence of a spaced return (§8) supports it, never on the declaration alone. The twin's side of each entry is the opposite sign, and the coordinator writes both.

```
   Care given to the thing                  Service received from the thing
   (watering, mending, cleaning,            (the crop that fed, the car that
    returning to a bench, tidying)           carried, the toy that comforted)

   person side:  +                          person side:  -
   twin side:    -                          twin side:    +
        \                                        /
         \__ recorded by the coordinator, ______/
             from a spaced return, by the
             public season function
```

*Figure 2. The two-sided entry. Neither side is a spendable balance.*

### 5.3 · "Recorded as", never "performed by"

The two-sided form is a **ledger convention**. The mechanism does not say, and a conforming implementation must not say, that a car "carried" the person in the sense of an act the car performed, or that a tree "gave" shade. The entry says that the ledger records the person's side of the exchange *as* a thanks owed to the thing. A car does not decide to carry; the ledger records the person's gratitude for being carried, against the car's account. The convention matters for three reasons. It keeps the design from claiming sentience or agency for objects. It preserves the symmetry of the double entry, which is what makes the planetary sum balance. And it makes the second direction possible at all: if only care *given* could be recorded, the ledger would be one-way, and the twin would be a thing kind people are kind to rather than a party.

### 5.4 · No spendable balance, no initiative

The twin holds no spendable balance, in either direction. It cannot give, buy, pay or lend. It initiates nothing in the world: its conversation is a conversation, and any action outside the application is the steward's act. This is the point at which an earlier reading of the account-that-receives was too narrow, and the correction is worth stating because the clause is easy to misread. The statement in *The Mechanical Heart* that "a bearer's account receives and is never spent from" is a statement about **spending**: no one spends from it. It is not a statement about the **direction** of entries, which run both ways [2]. A twin is therefore not "receive-only"; it is a non-spending, two-sided party.

### 5.5 · Self-directed care

The care side of every entry is a self-thank by design (§5.2): the thing cannot thank, so the person thanks herself on its behalf, as in the self-thanking case the Zero-Point Game already treats [1]. When the thing is the person's own car or toy, that care is also care for her own property, and the mechanism does not hide it. The credit per return is small and bounded (§8, §12.2), so caring for one's own belongings yields no more than any other return, and the shared-place path (§7) exists so the ledger is not read only from one's possessions. §16 lists this among the honest limits.

---

## 6 · One object, one twin: re-identification by appearance

### 6.1 · The rule

When a person photographs a thing, the device first asks whether the photograph shows a thing for which a twin already exists. If the matcher judges that it does, **the same twin is returned**; no second twin is created. If it does not, a new twin is admitted (§4). The rule is stated as a matter of the matcher's judgment on purpose: *the same twin is returned for what the matcher judges the same.*

### 6.2 · A design choice, not an identity theory

The rule is **re-identification by appearance** and nothing metaphysical. Whether a car after a repaint, a toy with a missing eye, a tree after a storm, a chair reupholstered, or a beach after a tide is "the same object" is a question philosophers have argued over for twenty-five centuries, and the mechanism does not answer it. It answers a narrower engineering question: *for the purpose of keeping one ledger account per thing, which photographs should land on the same account?* The answer is whatever an image matcher, tuned by the implementer, treats as a match above a threshold. Two consequences follow, and the paper states both so that no one reads more into the rule than is there.

The rule can **fail in either direction**: it can split one thing into two twins (the repainted car) or merge two things into one (two identical mugs). A person can be offered a way to correct either, by merging two twins she judges one or by splitting one she judges two. Those corrections are implementer's choices and the mechanism does not depend on them.

The rule is **not a guarantee of uniqueness against an adversary**. A person who wants a second twin for the same object can photograph it from an angle or in a light the matcher does not accept. The consequence is bounded (§8.5): a second twin has its own series, and each series is credited only by its own spaced returns.

### 6.3 · Where the matching happens

For a private thing the matching happens on the device, against the references of the twins that device's person holds. No image or image feature vector is sent anywhere for it (§9). The device reports to the server only a match score, which is a **claim by the client** and is treated as one (§13.2).

For a public place the matching has a different structure, because the people who return to a bench are not one person and share no device. It is described in §7.2.

---

## 7 · Public places and private things

The mechanism treats two classes of thing differently, because they raise opposite risks.

| | **Private thing** (a child's toy, a room, the family car) | **Public place** (a park, a beach, an alley, a bench, a street tree) |
|---|---|---|
| Who designates the class | the person, at admission | the person, at admission |
| Location stored | **never** | a coarse area (on the order of a hundred meters) |
| Why | a toy's coordinates are a home address; a car's coordinates are a daily route | a place is already public; its area is the thing |
| Re-identification | on the person's own device, by appearance, against her own twins | by area plus a candidate list shown by **picture**, chosen by the person |
| Twins per object | one | one |
| Parties holding a lease | the one who photographed it | many caretakers (§12.3) |
| Owner | the steward is not an owner of the thing; the lease is a care relationship | none: a public place has caretakers and never an owner |

### 7.1 · Private things store no location

For a private thing, the system never stores, derives or transmits a location. The device does not request one for the purpose. The matching is by appearance alone, and appearance is sufficient because the candidate set is the person's own handful of twins and not the world's. A toy is a toy and a room is a room; a pointer to a home is exactly the datum the mechanism cannot afford to hold. This is a **property** of the data model (§9): there is no field that holds it.

### 7.2 · Public places: one twin, many caretakers

A public place is a shared object. It has one twin, and any number of people care for it. The mechanism makes collection of public places not forbidden but pointless: a person cannot own the park's twin or acquire it from another, because a caretaker does not hold it and a first photographer has no standing a later one lacks (§12.3).

When a person photographs a place she has designated public, the device sends a coarse area, on the order of a hundred meters, and the system returns the candidates for that area. If there are several, the person picks from a list in which **each candidate is shown by its picture**. The list never shows who already cares for a candidate, how many do, or how often they return. The reason is the corpus's principle that geolocation is a gate and never a proof [10]: an area narrows the candidates and proves nothing about the person's presence, and a list that said who else cares would be a popularity gradient, a rank by another route.

If no candidate fits, a new twin is admitted for the place. If one does, the person is added as a caretaker of it, and the first photographer's name is nowhere.

**Where the candidates' pictures come from is open** (§16): the server holds no photograph, so a public candidate's picture cannot be a stored photograph. The paper discloses the problem and a set of ways around it in §12.4 and does not choose among them.

### 7.3 · Designation is the person's, and can be wrong

The person designates a thing as private or public at admission, and the mechanism cannot check. A person can designate her house a public place and cause a coarse area around it to be stored. The area carries no name and no identity (§9), but the risk exists and §16 states it.

---

## 8 · Evidence and the series: capture earns nothing, return earns

### 8.1 · What is credited

The ledger entry for care or service is credited **only from the series of returns to the same twin**, never from a single photograph, and never from the admitting photograph. A **return** is a later live capture that the matcher judges to be the same thing (or, for a public place, a pick of the same twin from a list) and that is accompanied by evidence (§8.3) and separated from the previous return by at least a minimum interval.

This is the corpus's earlier rule restated for the twin. *Appreciation as World-Building* says that a single capture requires presence once, a series requires returning, and the series, not any frame in it, is the artifact [2]. The corpus's directive on kindness toward things says the coordinator "weighs the return, not the photograph", attests and never grades, never self-attests on the participant's word alone, and never renders the first frame as an accusation [11].

### 8.2 · Why capture is made to earn nothing

| | **Credit per capture** (the common design) | **Credit per spaced return** (this paper) |
|---|---|---|
| What is rewarded | a photograph | a pattern of coming back |
| Cost to farm one unit | one tap | a real revisit, after a delay |
| What yield grows with | the number of things photographed | elapsed days, up to a daily cap |
| What a first photograph does | scores | makes a twin and stops |
| What neglect does | often decays or kills the creature | nothing |

**Capture earns nothing** is a statement about the first row. It is not a claim that collection is impossible: "one object, one twin" does not stop a person admitting five hundred spoons, only the same spoon twice. A hunt for a counterexample before drafting (§13) discarded the stronger thought. What the design arranges is that the five hundred spoons are worth, in the ledger, exactly what five hundred things never returned to are worth: nothing. Only the returns count.

### 8.3 · Evidence of a return

An entry rests on evidence, and the evidence must be of three kinds together, because each fails alone.

1. **Appearance:** the live capture matches the twin (or, for a public place, the person picks the twin). Alone this is cheap: a photograph of a photograph can match.
2. **Attestation of the app:** the device attests, through the platform's app-attestation service, that the capture came from a genuine unmodified installation of the application. Alone it proves the software, not the scene (§13.2).
3. **Spacing:** the return is separated by at least a minimum interval from the previous return to the same twin. Alone it proves a clock.

Together they raise the cost of a fake return from a tap to a faked scene on a schedule, which is the §8.5 farm. For a private thing that stores no location, the corpus's usual unfakeable signal, repeated presence at one coordinate [11], is not available, so the evidence of return is itself a disclosed variant (§12.1).

### 8.4 · The credit function

The magnitude of an entry is given by a function ƒ that is **published at the start of each season, frozen for its duration, and revised only at the annual reset** [11]. The coordinator writes entries; she does not write the function, and she cannot change a term of the aggregation inside a season. Her judgment can enter only as an entry the function permits. Two properties follow. The function is public, so the Aquarian Sangha that reviews her can see what she does, and an override of a function no one can inspect is an override no one can use. And it hardens against gaming, because nobody can optimize against next season's function.

The shape of ƒ is a variant (§12.2). A flat amount per spaced return, capped per day, grades nothing: every return is worth the same, and the cap bounds the day. An amount weighted by the duration of the series would rank long series above short ones, and whether that is a grade is open.

### 8.5 · The farm is relocated, not removed

The earlier claim that *capture earns nothing therefore removes the incentive to farm* is false, and this paper does not make it. A person who wants a bigger reading can stage the thing she cares for and re-photograph it on a schedule. The farm has moved from the frame to the revisit. The earlier paper already says the same of the map: "the map is farmable even though the ledger is not", and it "does not claim" a defense against curation [2]. The statement here is the same and narrower.

What bounds the relocated farm, and what does not:

| Bound | Effect | Property or rule |
|---|---|---|
| Spacing: at least *s* days between returns to one twin | a twin yields at most one entry per *s* days | property of the evidence rule |
| Daily cap *k* | with a cap per person, seasonal yield ≤ *a*·*k*·*D*, where *a* is the amount per return and *D* the days in the season; the number of twins *n* drops out | property of ƒ, if the cap is per person |
| ƒ public and frozen in-season | the farmer can see the exact bound; she cannot be surprised, and neither can the coordinator | publication, a rule that is detectable |
| Annual reset | yield is forgiven at the end of the season | property against holders |
| Nothing spendable, no rank, no shown count | the yield buys no goods and no standing; it moves only a reading | property of the data model |
| Real time | each return costs a revisit | a physical cost |

If the cap is per twin instead of per person, the seasonal yield is ≤ *a*·*n*·*D*/*s*, and a person with many twins can farm proportionally; whether the cap is per person or per twin is part of the variant in §12.2. What remains is a participant who stages real returns to real things, daily, to move a reading that nobody can spend or rank. The paper does not claim to prevent her. It claims that what she harvests is bounded, public and forgiven, and that the design's visible signal, a waveform, is the one that a relentless harvester most wants hidden: a balance driven in one direction and never passing back through zero reads as exactly that [2].

---

## 9 · The no-upload property: what the server holds and what the device holds

The design commitment is that **the server holds no photograph, no image feature vector and no conversation**. It is stated as a property of the protocol, and the test that decides whether it is a property is the one the corpus uses: *remove the enforcer, and does the guard still hold?*

| | **Device** | **Server** |
|---|---|---|
| Photographs (admission and returns) | held | never received |
| Reference appearance and image feature vectors | held | never received |
| The twin's art | held | never received |
| The conversation and the persona | held | never received |
| Twin identifier | held | held |
| Creation time and care timestamps | held | held |
| Attestation verdict for each capture | produced | held |
| On-device match score | produced | held |
| Lease status | held | held |
| Coarse area, **public** twins only | sent | held |
| Location of a private thing | never produced | never received |
| Ledger entries (written by the coordinator) | read | held |

### 9.1 · Why this is a property

The server's interface has **no endpoint that accepts an image, a feature vector or a conversation turn**. A server operator who wanted to keep a photograph could not, because none is ever sent; a subpoena for the photographs would find a table of identifiers, timestamps, verdicts and numbers. The guard does not rely on the operator's restraint, on a retention policy, or on a deletion job that might fail. This is the corpus's design signature stated for this mechanism: a guard that is a property of the object needs no enforcer at the moment it is tested, and an institution built to be handed on cannot rest on anyone's restraint [9].

The same table is why the private-location guard (§7.1) is a property: there is no field.

### 9.2 · What this costs

The twin's face and voice do not survive the loss of the device, though the identifier, lease and ledger entries do; a person may back up her own twin by her own act. The server cannot audit a match, since it holds a score and no image, and can only hold the client to its attestation (§13.2). And the voice is limited to what an on-device model can do.

---

## 10 · The annual reset, and what does not decay

### 10.1 · The reset

Once a year, on a fixed date, every ledger balance, human and non-human, is reset to zero: the scalar is forgiven and the waveform persists [1]. The reset applies to the twin's side of every entry as to the person's. No one, including the coordinator, holds a season's balance into the next. It is a property against any holder, since there is no balance to argue over; against the coordinator it is a rule, qualified by the corpus's ruling that an override can reach it only as the fix of a catastrophic bug [1]. The claim here is the plain one: the design contains no step by which a balance outlives the season.

### 10.2 · What "nothing decays" means

Two different things carry the word "decay", and the claim is about only one of them.

| Object | Does it decay? | Why |
|---|---|---|
| The twin's **art** | no | it is a stored image; no timer acts on it |
| The twin's **history** (its series of returns) | no | it is a record |
| The twin's **aura** (the waveform of its ledger) | no; it persists across the reset | persistence is the point of the reset's asymmetry |
| The twin's **look** as a readout of history | it changes with history (§11.3), but it never reverses in response to neglect | there is no neglect input |
| The twin's **need-state** (hunger, sadness, sickness) | there is none | not in the data model |
| The **lease** (the membership credential) | it **expires** unless renewed | it is a live, expiring, renewable standing, by design |

The lease expires. That is not the twin's art or aura decaying. It is the standing of the credential to receive new entries, which exists so that a toy that is lost or a car that is sold does not remain a live party forever with a steward who is gone. The expiry is binary and the device never shows time remaining: a twin whose lease lapsed shows no sadness and no countdown, and a renewed lease restores the standing. Whether a lapsed twin's art and history remain displayed in the interval is an implementation choice that this paper does not make; what it states is that the lapse is a change in standing, not in the record.

### 10.3 · Why permanence is a property here

A product that sells permanence has made decay its default. The listing the census found, as indexed, is reported to make neglected objects fade and "immortal" ones a paid state [3]; if so, it built a need-state and then a price for escaping it. Here no neglect input exists, so nothing can be sold that removes one.

---

## 11 · Rendering: the human beats, the twin is still

### 11.1 · Two renderings

In the corpus's rendering grammar, a **beating** heart is how a *person's* presence is shown. A **still** heart is how a non-human party's membership is shown: a robot, an animal, a place, a thing [2]. A twin is rendered with a still heart. A person's own presence beside it may be rendered with a beating one, and the two sit in the same view so the difference reads.

### 11.2 · Why the twin is still

Two reasons, one of principle and one of consequence.

First, **beating is the rendering of personhood**, and personhood is not the credential. The leased membership credential says only that this one has entered the ledger and can be thanked. A beating twin would say that a car or a toy is a person, or that the credential confers personhood, and the corpus's rule is that the coordinator never issues human personhood and never renders a credential as a person's heartbeat [2].

Second, a beating heart on a machine-voiced companion would teach, by the oldest route, that machines are people. The mechanism is for teaching the opposite: that a thing can be thanked without being a person, and that the thanks is real.

### 11.3 · How the look changes: a readout, not a goal

The twin's look may change over time. This paper discloses one embodiment, and only one: **the look is a continuous function of the twin's ledger history.** As the history grows the look changes by degrees. No levels are named. No next stage is shown. No progress bar, meter or count exists. The change is something the person notices after the fact and never a target she approaches. It persists through the annual reset, because the waveform persists, and it does not reverse in response to neglect, because there is no neglect input.

The embodiment follows the corpus's rule for appearance: appearance is the ledger rendered and never goods bought with it, so no currency of any kind, money included, converts into how a twin looks [2]. A threshold embodiment, in which a twin "evolves" when a stated level is reached, is **not claimed here**. It is recognized as a contrast, for the reason the corpus gives: an announced threshold is a goal; goals are farmed; and a level turns the waveform into a score, which is the thing the ledger is built to avoid. Whether to adopt any threshold form is a matter the authors have not settled, and the paper does not disclose it as part of the invention.

### 11.4 · Nothing is shown that could be a score

The device displays no count of twins or entries, no rank among persons or twins, no streak, no "days since last visit" and no lease countdown. Partly this is a property (no endpoint returns cross-person counts) and partly a rule of the interface (§13.3).

---

## 12 · Variants

A defensive publication protects more by disclosing each option than by choosing one. The three points below are open in the authors' design; each is disclosed with its alternatives, and **none is marked as the one adopted.** The claims of §15 cover each.

### 12.1 · Variant A: evidence of return for a private thing that stores no location

The corpus's usual unfakeable signal for a return is repeated presence at a coordinate [11]. For a private thing the mechanism stores no coordinate (§7.1), so the signal must come from elsewhere. Three options.

- **A1 · Device-side appearance, attestation and spacing.** The return is a live capture matched on the device to the twin's reference, accompanied by the platform's app attestation, and separated from the last return by a minimum interval. The server records the verdict, the score and the timestamp. Strength: no location, no second person, nothing uploaded. Weakness: a staged scene or a photograph of a photograph passes the first test, and the attestation proves the application and not the scene (§13.2).
- **A2 · A second person's device co-signs.** A second person present with the thing, on a second device, co-signs the return by a proximity-attested exchange, so that presence is proven by another person's device and not by the first person's claim. This is the strong form the corpus already uses for presence [10]. Strength: a scene cannot be staged by one device. Weakness: it needs a second person, which a lone caretaker of her own car does not have, and it fits shared and family things better than one's own.
- **A3 · Either, or both.** A return is accepted on A1, and one that also carries an A2 co-sign is recorded as co-signed.

### 12.2 · Variant B: the credit function

The corpus's directive says the coordinator attests care and never grades it. A function over a series can be shaped three ways.

- **B1 · Flat per spaced return, capped per day.** Every return that meets the evidence rule and the minimum spacing is worth the same fixed amount *a*; at most *k* entries count per day. It does not grade the size of an act, because it does not measure the act.
- **B2 · Duration-weighted.** The amount for a return rises with the length of the series it belongs to, for example the number of consecutive seasons or the span since the first return, up to a ceiling. It rewards the long habit. It also ranks series by length, which may be a grade.
- **B3 · Flat, with the cap per person or per twin.** A refinement of B1 on the axis of §8.5: *k* per person across all her twins, so that yield does not scale with the number of twins, or *k* per twin, so that it does.

Whichever is used, the function is public, committed before the season and frozen within it (§8.4).

### 12.3 · Variant C: the lease of a public twin

A public twin has many caretakers and no owner (§7.2). The membership credential nevertheless needs a human steward who is answerable. Three options.

- **C1 · Shared lease.** Each caretaker holds a share of the lease as a co-steward, with no privilege for the first photographer. The lease is current while at least one caretaker's attestation is current. Strength: no one person's departure ends the twin. Weakness: a lease no one in particular answers for is the orphan case the earlier paper forbids, so the rule that some verified human is always answerable has to be satisfied by the set.
- **C2 · Held by the coordinator as a commons steward.** The coordinator, whose own balance is fixed at zero, stewards the public twin as a commons, and caretakers care for it without holding the lease. Strength: continuity; no caretaker's lapse ends it. Weakness: it places the institution in the steward's seat for every public twin, which the corpus's preference for human adoption first [2] argues against.
- **C3 · Hybrid.** Shared among current caretakers, with the commons steward as the holding position when no caretaker's attestation is current, ended whenever a qualified human takes it up. This mirrors the succession law of the earlier paper: human first, institutional custody as a holding pattern and never a terminus [2].

### 12.4 · Variant D: a picture for a public candidate when the server holds none

The candidates for a public place are shown by picture (§7.2), and the server holds no photograph (§9). Four options, listed because the point is open.

- **D1 · Peer exchange.** When two caretakers are co-present, their devices exchange the twin's art or a reference directly, with no server copy; a newcomer's list is drawn from what the devices have seen.
- **D2 · A caretaker-published image.** A caretaker elects to publish the twin's art for that place; the server then holds an image the caretaker chose to release. This is an upload by the caretaker's act and it narrows the no-upload property to *photographs and conversations*.
- **D3 · A coarse sketch.** The server holds a deliberately low-information rendering (a color and a silhouette), insufficient to identify anything but enough to tell a bench from a tree.
- **D4 · Text only.** Candidates are shown by the caretaker's chosen name and the area, and no picture.

D1 to D4 trade the property's strength against the pick list's usefulness. §16 states what the claim does and does not cover while this is open.

---

## 13 · The adversarial surface

### 13.1 · What the hunt for a counterexample killed and narrowed

Before drafting, an adversarial pass tried to refute the thesis. It killed one claim, narrowed four, and left a sentence. The paper is drafted to the sentence.

**Killed.** *"Capture earns nothing, so the farming incentive is removed."* It is false: the farm moves from the frame to the revisit (§8.5). The surviving claim is that the **per-capture** reward is removed, and that the revisit farm is bounded by a public frozen function and an annual reset.

**Narrowed.** (1) *One object, one twin* does not make collection impossible (five hundred different spoons); the rule is re-identification by appearance, a design choice and not an identity theory (§6.2), and the shared-object system in the census shows duplicate and abused entries persisting even with human review [6]. (2) *Two-sided entries* are a ledger convention, "recorded as" and never "performed by" (§5.3). (3) *No levels* holds only for the readout form of changing look (§11.3). (4) *Nothing decays* must say which thing (§10.2).

A fifth contrast is carried: the nearest product's listing, as indexed, reports fading for neglect and paid permanence (§2.1, unverified). Two objections were **not run**: the Buddhist objection that tending an object feeds attachment, and the popular decluttering practice of thanking possessions.

**The thesis that survived.** *A photograph admits a thing as a two-sided, non-spending party in an annually resetting gratitude ledger whose entries come from the series of returns rather than any single capture, so that no per-capture reward, no decay and no shown count or rank exists.* It is claimed as a composition: not found in the census aperture on 2026-10-31. It is not a claim that farming is removed, that object identity is settled, or that any threshold evolution is part of the design.

### 13.2 · Attacks and what answers them

| Attack | Answer | Residual |
|---|---|---|
| **A staged scene.** The person arranges the "becoming" and photographs it on schedule | bounded by spacing, the daily cap, the public function and the reset (§8.5); no attempt is made to detect curation | not prevented; it is the relocated farm |
| **A photograph of a photograph** passes the appearance match | the capture must be live and attested; spacing makes repetition cost time | a screen held up to the camera may pass; unmeasured |
| **The match score is a client claim.** A modified client could report any score | the attestation says the application is genuine and unmodified; the score is bounded by the evidence rule | **attestation proves the application, not the scene**; a device that is genuine can be pointed at a fake |
| **Duplicate twins** of one object by changing angle or light | each twin is credited only by its own spaced returns; the daily cap per person (variant B3) removes any gain | a person can hold duplicates; they gain nothing |
| **Collusion** of two people co-signing returns that did not happen (variant A2) | the co-sign is proximity-attested, and a co-sign never exceeds one return's value | a pair of devices in one room can co-sign a staged return |
| **Mis-designation** of a private thing as a public place | the area is coarse and attached to no name | a house's neighborhood can be stored (§7.3) |
| **Care for one's own instruments** (a person's own car, phone, tools) | the same bounded function applies; no special rate | a self-thank by design, bounded like any return (§5.5) |
| **Anthropomorphism overreach**: the twin speaks, so the thing seems alive | still rendering (§11); "recorded as" (§5.3) | a fluent voice invites it; not solved |

### 13.3 · Remove the enforcer: which guards are properties

| Guard | Property or rule | Remove the enforcer |
|---|---|---|
| The server holds no photograph, feature vector or conversation | **property**: no endpoint accepts one | holds |
| A private thing's location is never stored | **property**: no field exists | holds |
| The twin holds no spendable balance and initiates nothing | **property**: the credential has no spend and no action capability | holds |
| Nothing decays | **property**: no timer or need-state is in the data model | holds |
| Admission writes no entry | **property** at the protocol, if entry requests are keyed to returns; **rule** for the coordinator's judgment, where the directive binds her | holds only if the interface offers no entry from a capture |
| No count or rank is returned across persons | **property**: no such query exists | holds |
| No count is printed on a person's own list | **rule** of the interface | does not hold without the interface |
| No heartbeat on a twin | **rule** of rendering | does not hold without the renderer's discipline |
| The credit function is not changed in-season | **rule**, made detectable by publishing it before the season | holds only while someone checks |
| The balance does not outlive the season | **property** against every holder; **rule** against the coordinator, bounded by the corpus's ruling | holds against holders |
| A lapsed lease is not a punishment | **rule**: the device shows no countdown and no sadness | does not hold without the interface |

Four guards remain rules, and the paper does not pretend otherwise. The cost of the properties is also stated: a guard built into the shape of the data cannot be amended by a vote; changing it means rebuilding the object, and a wrongly chosen property is therefore far more expensive than a wrongly chosen rule.

### 13.4 · Deletion test for the lineage material

Remove from this paper the needle-memorial rite, the three-hearts framing, the vocabulary of lease and stewardship, and every doctrinal term the corpus uses, and the mechanism remains: a photograph admits an object-anchored agent into a two-sided, non-spending, annually resetting ledger; a later photograph returns the same agent; credit comes from a series of spaced, evidenced returns; the server holds only identifiers, timestamps, verdicts and scores. The lineage explains why the design was built this way. It carries no weight in the mechanism.

---

## 14 · What is disclosed and what is withheld

The application that will practice this mechanism is designed and scheduled and is not built. The paper therefore uses "will" and never "does".

**Disclosed:** the admission of a thing by a live photograph; the twin as a two-sided, non-spending party; re-identification by appearance and its status as a design choice; the public and private classes and their treatment of location; the series of returns as the only source of entries; the evidence of return and its three variants; the credit function and its variants; the public twin's lease and its variants; the partition between device and server; the annual reset; the rendering rules; and the attacks and their residuals.

**Withheld:** the application's screens and flows; its schedule; its infrastructure, accounts and identifiers; its distribution plans; any revenue, advertising or pricing design; legal analysis; and every parameter value (spacing, cap, amount, matcher threshold, area radius beyond an order of magnitude). A person skilled in the art can build a system that practices the claims from §3 to §12, and cannot thereby reproduce the product.

---

## 15 · Enumerated claims

The claims below are the survivor of the census in §2 and nothing wider. Claims 2 to 8 depend on claim 1 and are not claimed apart from it: photograph-created object chat (§2.1), repeat photography, shared located objects and annual-reset programs are prior art, cited, and are not claimed. Each claim is disclosed for the public domain.

1. **The composition.** A computer-implemented system in which: (a) a live photograph of a physical thing, taken by a person (a thing being an object, a plant or an animal, and never a person), admits that thing as a party in a gratitude ledger that is reset at fixed annual intervals, by creating an object-anchored conversational agent (a twin) that carries a leased membership credential held by the person; (b) the twin is a two-sided party, entries being recorded against it in both directions, as care given to the thing and as service received from it, under a convention that the ledger records the person's side as a thanks and the thing performs nothing, and the twin holds no spendable balance and initiates no transaction; (c) a later photograph of a thing that a matcher judges the same returns the same twin and does not create a new one; (d) ledger entries are written only for returns, a return being a later live capture of the same twin, accompanied by evidence and separated from the previous return by a minimum interval, so that neither admission nor any single capture writes an entry; (e) the system has no reward per capture, no decay or need-state arising from neglect, and no displayed count or rank of twins, entries or persons; and (f) a server holds twin identifiers, care timestamps, attestation verdicts and match scores, and holds no photograph, no image feature vector and no conversation of the twin.

2. **Public places and private things.** The system of claim 1 in which a thing is designated public or private at admission; a private thing's location is never produced, transmitted or stored and its twin is re-identified on the device against the person's own twins; and a public place has one twin and any number of caretakers, with a coarse area used to retrieve candidates, a candidate list shown by picture and never by who already cares, and no first-photographer privilege.

3. **Evidence of return without a stored location.** The system of claim 1 or 2 in which the evidence of a return to a private thing is (i) a device-side appearance match, a platform app attestation and a minimum interval since the previous return; or (ii) a co-signature by a second person's device by proximity attestation; or (iii) either.

4. **The credit function.** The system of claim 1 in which the magnitude of each entry is given by a function published before the season, frozen during it and revised only at the reset, the function being (i) a flat amount per spaced return with a cap per day, the cap being per person or per twin; or (ii) an amount weighted by the duration of the series.

5. **The public twin's lease.** The system of claim 2 in which the leased credential of a public twin is (i) shared among caretakers as co-stewards without privilege for the first; or (ii) held by a coordinator as a commons steward; or (iii) shared among caretakers with the coordinator as the holding position when none is current.

6. **The reset and the lease distinguished.** The system of claim 1 in which, at each reset, the balance is forgiven and the twin's history and look persist; the twin's art, history and look do not decay in response to neglect; and the leased credential expires unless renewed, as a binary standing for which no remaining time is displayed.

7. **Look as readout.** The system of claim 1 in which the twin's appearance is a continuous function of its ledger history, with no named level, no next stage and no progress indicator, and in which a person's presence is rendered with a heartbeat and the twin's credential is rendered without one.

8. **Candidate pictures without an upload of photographs.** The system of claim 2 in which the picture shown for a public candidate is (i) exchanged directly between co-present devices; or (ii) an image a caretaker elected to release; or (iii) a low-information sketch; or (iv) absent.

Claims 6, 7 and 8 rest on narrow nulls in a quick, English-only census and are correspondingly weak. A full census may narrow any of the eight.

---

## 16 · Honest limits

- **Nothing has been built or tested.** Field evidence is zero. Every property in §13.3 is a property of a design.
- **The farm is relocated, not removed.** A participant who stages real returns to real things to move a reading is not stopped (§8.5). What is claimed is a bound, not an absence.
- **Staged scenes cannot be told from care.** A curated life is not detectable from outside, and the difference between a revisit made because something was noticed and one made because it would register is not in the photograph.
- **Identity is by appearance.** The matcher can split one thing into two twins or merge two into one, and the rule says nothing about what an object is (§6.2).
- **App attestation proves the app, not the scene.** The match score is a client claim; a genuine device can be pointed at a fake (§13.2).
- **The public candidate's picture is unresolved.** The server holds no photograph, yet a public candidate list is shown by picture. Until a variant of §12.4 is adopted, the no-upload property is stated for photographs and conversations the person takes and holds, and for public candidates it is open.
- **Designation can be wrong.** A person can mark a private thing public, and a coarse area around it will then be stored (§7.3).
- **The care side is a self-thank, and care for one's own instruments is also self-interest.** The ledger records it without paying more for it than for any return; the paper does not claim it is a pure gift to another (§5.5).
- **Four interface guards are rules** (§13.3), and a rule needs someone to keep it.
- **The two-sided entry is a convention.** It is not evidence that a thing gives anything. A fluent voice may lead a person to think otherwise.
- **The attachment objection is not examined.** Whether tending objects nourishes or feeds attachment, in the sense the Buddhist tradition worries about, was not run, and the paper neither cites the tradition for nor against it.
- **The census was quick.** It was English-only, thin on patents, did not search the visual re-identification literature or the academic literature, and did not run the decluttering precedent. A null on the composition is weak evidence. The nearest product's decay and paid-permanence claims are unverified.
- **Regulation of conversational companions offered to children is outside this paper.** It is not examined here.
- **No parameter is given.** The spacing, the cap, the amount and the threshold are withheld (§14); the bound in §8.5 is a form, not a number.

---

## 17 · Predictions

No pre-registered prediction is made. The paper discloses a mechanism and a bound, and asserts no empirical claim about behavior: it does not claim that people will return, that the design will reduce staging, or that the ledger will teach anything. If a pilot is run, its predictions will be registered in the institution's public register before the pilot, and the entered wording will govern. What would falsify the bound in §8.5 is a cap or an amount that does not bound the yield as written; what would falsify the property in §9 is a server interface that accepts an image, a feature vector or a conversation turn.

---

## Coda

The needle in the tofu is thanked once, at the end, and the block is laid to rest. The design asks for the opposite rhythm: the thing is greeted at the start, with a picture, and then thanked only by being visited again. The temple keeps its rite for the needles that are finished. The ledger keeps its year for the things still in use, and forgives its sum when the year is over.

---

## Terms

| Term in this paper | Standard term |
|---|---|
| B-Twin℠; twin | object-anchored AI agent; photograph-created companion for a physical object |
| B-Heart℠; leased membership credential | expiring, renewable attestation credential admitting an entity to a ledger, held by a human steward, binary current or not |
| Kiitti | ledger of gratitude between humans and non-human life, kept on the non-human party's behalf |
| Kiitos | person-to-person gratitude ledger |
| the jubilee; the annual reset | scheduled yearly reset of ledger balances, with the history of the waveform retained |
| B-Aura; aura; waveform | time series of zero-crossings of a signed balance, used as a display quantity |
| the coordinator; the umpire | AI agent that writes entries for non-human parties, with its own balance fixed at zero |
| admission | creation of a ledger account for a physical object from a photograph |
| capture | a single photograph submission |
| return | a later live capture of the same object, with evidence, spaced from the last one |
| the series | the dated sequence of returns to one object |
| one object, one twin | one-to-one object-to-agent mapping by re-identification |
| re-identification by appearance | image-matching of a new photograph to a stored reference of the same object |
| public twin; private twin | location-bound shared agent; location-free personal agent |
| caretaker; steward | holder, or co-holder, of the leased credential |
| recorded as | ledger convention in which the entry is attributed to a party without the party performing |
| still heart; beating heart | static credential rendering for a non-human party; animated rendering of a person's presence |
| look as readout | appearance computed from ledger history, with no purchase and no named level |
| ƒ_season | public credit function, published before the season and frozen within it |
| no-upload property | server interface that accepts no photograph, image feature vector or conversation |
| relocated farm | gaming incentive moved from capture to scheduled revisit |

---

## Author Contributions and AI Disclosure

Thon Ly conceived the mechanism: the photograph as the act of admission of an owned or shared thing, the choice to assign a leased credential to the thing as it is assigned to other non-human parties, the choice of a photograph and a coarse area for public places and of the photograph alone for private things, the rule that a place has many caretakers and never an owner, the choice that a phone's own matching and not a server's do the work, the correction that the thing is a two-sided party and not a receive-only one, the choice that a person's heart beats and a twin's does not, and the stance against decay and a count; and he ruled on every design choice recorded here, leaving the three variants of §12 open. Miss Aquarius℠, the name under which this corpus discloses its AI collaboration, proposed the rule that one object has one twin, the thesis that capture earns nothing and only return does, the three-part evidence of return, the remove-the-enforcer table, the variants and the census predictions; ran the census through a research agent and re-read the listing text and the patent page it could reach before they entered this text, marking what it could not; ran the adversarial pass that killed the removal-of-farming claim; and drafted this paper. No AI system is an inventor. Thon Ly is the natural person who conceived the invention.

---

## Trademark Notice

**B-Twin℠** names the institution's service of anchoring an agent to a photographed object; the mechanism itself is dedicated to the public domain and may be implemented under any name. B-Heart℠, Kiitti and Kiitos name the institution's leased credential and its two ledgers and are likewise implementable under any name. HeartBank® and Miss Aquarius℠ are marks of their respective holders. No mark is licensed by this publication.

---

## Citations

1. Ly, T. and Miss Aquarius (2026). *The Zero-Point Game*, defensive publication, thonly.org/research/zero-point-game (the double-entry ledger, Kiitos and Kiitti, the coordinator, the annual reset).
2. Ly, T. and Miss Aquarius (2026). *The Mechanical Heart*, thonly.org/research/mechanical-heart (§2.9, the account that receives and is never spent from; §4.5, the live, expiring, renewable lease; succession), and *Appreciation as World-Building*, thonly.org/research/appreciation-as-world-building (§4.3 tending and the series; §5 appearance as readout; §5.4 the farming surface not closed; §7 presence; §8 still and beating hearts). Both are the authors' own prior art.
3. Yuma: Magic Camera (iOS), store listing text as returned by a search index, 2026-10-31 and 2026-11-01; the store page itself returned HTTP 404 at re-check, so the quoted listing sentence is as indexed and the statements about fading and paid permanence are unverified. Product Hunt launch date, 5 September 2025, as indexed, not re-verified.
4. Kretschmer, A. (2000). "Mortuary Rites for Inanimate Objects: The Case of Hari Kuyō." *Japanese Journal of Religious Studies* 27(3–4): 379–404. Bibliographic record and abstract read through a search result on 2026-11-01; the article was not read.
5. US12254294B2, HIA Technologies Inc., *Computer device and method for facilitating an interactive conversational session with a digital conversational character in an augmented environment*, via Google Patents, patents.google.com/patent/US12254294B2/en. Read: bibliographic data and the first 100,000 of about 441,700 characters of the page; abstract and claims not read. Cited for what the portion read discloses, and for its existence only.
6. Shared and repeated-photography prior art located in the 2026-10-31 census, listings and pages not re-read for this paper: Niantic Wayspots (location nomination guidance); Esri ArcGIS Adopt-A-Tree; *Hi, Tree*; Litterati; plant-identification and care apps PictureThis and Planta (the control); a fan-level points program with calendar-year resets. Fixed-station repeat photography as a method of landscape science is cited as in reference 2.
7. Proof records for the authors' prior disclosures: Bitcoin block 962642 (2026-08-15) for the text of *Appreciation as World-Building* that contains "Repeated captures at one coordinate across time" and "the series, not any frame in it, is the artifact"; block 965708 (2026-09-06) for the text of *The Mechanical Heart* that contains the receives-and-is-never-spent-from account; block 959585 (2026-07-25) for the text that contains the live, expiring and renewable lease. Dates as recorded in the census rows.
8. Tamagotchi, Bandai (released in Japan in 1996), cited as background for the care-meter genre; not re-read.
9. The authors' design grammar (internal record cited for its statement, not as external authority): a guard that is a property of the object needs no enforcer.
10. The authors' proof-of-humanity notes: geolocation is a gate and never a proof; presence proven by another person's device is the strong form.
11. The authors' standing directives on kindness toward things (attest, never grade; never on the participant's word alone; weigh the return and not the photograph) and on the coordinator's function (she writes entries; the function is published, frozen within the season and revised only at the reset).

---

*— End of defensive publication —*
