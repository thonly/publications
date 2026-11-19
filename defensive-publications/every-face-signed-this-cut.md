---
title: "Per-Performer Digital-Replica Consent Signatures over the Screenplay and the Exact Final File of an AI-Generated Film: Every Lent Face Signed This Cut"
subtitle: "Two Passkey Signatures per Credited Performer, One over the Screenplay and One over the Final Bytes, Recorded with Per-Party Salts in a Public Append-Only Log a Viewer Can Check, with a Stored Likeness That a Party Holding Only Its Ciphertext Cannot Render (the B-Double mechanism)"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-a
program: open
status: draft
date: 2026-11-19
license: CC0-1.0
slug: every-face-signed-this-cut
venue: thonly.org/research/every-face-signed-this-cut
canonical_url: https://thonly.org/research/every-face-signed-this-cut
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claims* and withholds the *build specification* (§14 says what is withheld and why). A quick prior-art census ran before drafting, and §2 reports it in full, including the two conjuncts it killed, those it narrowed, and two industry specifications that a separate adversarial reader found afterwards and that narrow the record half of the claim. Its pre-registration was pushed before the first query to a **private** repository, so the push record exists but no reader outside it can inspect it; a full census, with its pre-registration published first, runs before this paper's first archival deposit.
>
> **Version 2, the same day.** Invented co-stars and extras need no press: only a *lent* face, a real person's likeness, is signed, and the credits mark every role lent or invented (§9.3, §9.4). Drafts are listed to the actor and deleted at release (§8.6), the manifest is published with the film (§9.6), and a film's license never licenses the cast's likenesses (§10.6).
>
> Companion works: *The Press Travels With the Message* (the passkey signature over exact text, recorded in a public append-only log, and what such a signature does and does not show), *B-Links* (signed provenance for a shared file) and *The Song That Is Not His* (generation in the voice of artists who can no longer consent, the case this paper is the living counterpart of).

---

## Preamble

The commentary on the first book of the Abhidhamma tells how the teaching reached the world. For three months the Buddha taught it without a break to an assembly of gods, and the commentator stops to ask a practical question: how did a body that lives on food keep going? His answer is that the Buddha kept the time. When the hour for the alms round came, he made a mind-made double, a *nimmita-buddha*, and resolved: *"Let this one's way of taking the robe and the bowl, its voice and its bearing, be like this; let it teach this much Dhamma."* Then he took his own bowl and went for alms [1].

The commentator then asks who could tell the two apart. The mighty gods could; the lesser gods could not, *"because between the Perfectly Awakened One and the created Buddha there is no difference in the rays and the rest: in rays, in voice, in words, there is no difference between the two."* [1]

Two things in that passage are the whole problem this paper addresses. The double did nothing its original had not resolved: it taught *this much*, in *this* manner, for *this* time. And most of those watching could not tell, by looking, which one they were watching. The resolve was real and it was invisible.

A film made with a person's digital likeness has both properties and loses the first. Generated video can now put a real person's face and voice into scenes they never stood in, and a viewer can no longer tell, by looking, whether the person agreed. The person's resolve, if they gave one, lives in a permission setting inside one company's app or in a contract no viewer will see.

This paper specifies a record of that resolve that the viewer can check. Each person whose likeness appears in a film signs twice with their own passkey: once over the screenplay, when they are cast, and once over the exact final file, before it is released. The signatures go into a public append-only log. A viewer holding the film computes its fingerprint and checks, for every depicted role, that a passkey bound to that role's name pressed over *this cut*. And the likeness itself is stored so that it renders only under such a press. The double teaches this much, in this manner, and the lesser gods can now tell.

*(The passage is cited as a recognition, tier: flourish. §13.4 runs the deletion test: nothing in the mechanism depends on it.)*

---

## Prior-Art and Non-Assertion Statement

This document is published as a **defensive publication** to establish prior art. Its contents, including every mechanism, the analysis and the enumerated claims of §15, are dedicated to the public domain under **CC0 1.0 Universal**. **The authors assert no patent rights in anything disclosed here, will not seek patent protection for it, and will not assert any patent against any person who practices it.** The dedication covers the mechanism under any name; the marks named in the Trademark Notice are reserved separately and are not licensed.

A quick prior-art census was run before drafting (§2). Its result is reported in full: the declared aperture and date, every conjunct that was killed or narrowed with its prior art cited, and the survivor. **The enumerated claims of §15 are that survivor and nothing wider.** No live patent surfaced in the quick census, but patents were reached only through a general web index, so the absence is weak, and nothing here is a clearance of any kind.

Three earlier disclosures of the authors are cited as the authors' own prior art, each with its proof-backed date (§2.3): *The Press Travels With the Message* (the passkey press over exact text in a public append-only log; Bitcoin block 975913, 2026-11-15), *B-Links* (signed provenance for a shared file; block 959585, 2026-07-25) and *The Song That Is Not His* (block 962355, 2026-08-14). What those papers already disclose is not re-claimed here. A timestamp proves that a text existed no later than its date and nothing about authorship, originality or the validity of any claim.

---

## Abstract

This defensive publication discloses a consent mechanism for **AI-generated video that uses real people's digital replicas** (likenesses of face and voice). Existing practice records a performer's consent as a permission setting inside one platform, as a project-specific contract, or as a reference to terms held by a consent authority; the provenance signatures that travel with a file are applied by its makers, and an industry identity assertion lets a named actor sign a file's binding in a role such as creator or editor. None records, for a generated film, the depicted performer's own signature over the words they agreed to and then over the exact pictures released. The mechanism here does. **(1)** At casting, each performer signs, with their own passkey, a statement over the screenplay text, the role, the render style and the agreed shares; any change to that text is a new offer that must be signed again. **(2)** Before release, each performer is given the exact final file (with the list of every rendition that will be served) and signs a statement over its cryptographic fingerprint; a single missing signature keeps that cut from release. Both signatures are recorded in a **public append-only log** as fingerprints salted per party, so the log alone pairs no records and names no one; the film carries the statements in a release manifest, so that **anyone holding the released bytes can recompute their fingerprint and check that, for every lent role, a passkey listed on that role's public name page signed the screenplay and then this exact file.** Invented co-stars and extras belong to no one, need no press, and are credited as invented. **(3)** The stored likeness model is encrypted under a key that only the performer's authenticator can derive, released for one work at a time, so that a party holding only the stored ciphertext cannot render it. A census found the parts public and did not find the composition. The paper claims that composition and nothing wider, and states what it does not do: a check covers released bytes, never a re-encoded copy; it names lent roles, never every face in the frames, and never who the faces belong to; it shows consent as given at release, never consent now; a signature shows a passkey pressed, never that a particular person did; and the operator who runs the press page and the render remains trusted, because one frame of a released film is enough for current tools to render a person with no stored model at all.

## 1 · Why lent faces

### 1.1 · Three kinds of face on a screen

There are three kinds of face a film can show. A **performed** face belongs to someone who stood in front of a camera. An **invented** face belongs to no one: a generator made it, and any other invented face would have done as well. A **lent** face belongs to a real person who did not stand in front of any camera for this film, and whose likeness a model rendered into it.

The order is not historical. Performed faces are not the past and lent faces are not the future; all three will be made side by side. One film may hold more than one kind: a lent lead beside invented co-stars and an invented crowd. What separates them is who stands behind the face, and what a viewer can know about it. For a performed face, the viewer knows that a person was there. For an invented face, the viewer knows that no one was. For a lent face, the viewer knows nothing at all, because the picture of a person who agreed and the picture of a person who did not are the same picture.

### 1.2 · The studio and the name

The studio this mechanism is designed for is THonly.com. The name is pronounced *the only*, and in the institution's usage it is a grammar given to everyone: each person is *the only* one of themselves, and everyone is that equally. Read that way, the name rules something out. An invented face is interchangeable by construction. A lent face is the only one of its kind: it can stand in for exactly one person, and, under this design, only by that person's own press. *Every lent face signed this cut* is the studio's name made checkable.

The studio makes films as gifts. Films are released free to the public at a set date; viewers may thank the cast afterwards; the studio charges for the compute that renders a film and takes no share of what a film earns. That frame (§10) is context for the mechanism, not part of the claims.

### 1.3 · What goes wrong without a record

Consent to the use of one's likeness exists today in several forms, and none of them gives a viewer the depicted performer's own signature over the released pictures.

```
  WHERE CONSENT LIVES TODAY                      WHAT A VIEWER CAN CHECK
  ────────────────────────────────────────────   ──────────────────────────────────
  a permission setting inside one app            nothing (the app's word)
  a project contract between the parties         nothing (the contract is private)
  a provenance signature on the file             that a STUDIO or TOOL made it
     (applied by the maker)
  an identity assertion by a named actor         that a named actor's credential
     (an industry standard, 2025)                   signed the file, in a role such
                                                    as creator or editor
  a consent reference (an industry draft, 2026)  that terms exist at a consent
                                                    authority; the signer does not
                                                    declare the consent itself
  ────────────────────────────────────────────   ──────────────────────────────────
  THIS PAPER: each lent performer's own          that, for every lent role, a
  signature over the screenplay, then over the   passkey bound to that role's name
  exact released file, in a public log           pressed over the words and then
                                                 over THIS file
```

A permission setting answers the question *may this platform render me?* It does not answer *did I agree to this scene, in this film, as released?*, and it answers nothing for a viewer outside the platform. A contract answers the second question for the parties and for a court, never for a viewer. A maker's provenance signature answers *who made this file?*, which is the wrong person: a studio can sign, truthfully, a deepfake of someone who never agreed (§2.2, row (g)). The two industry specifications come closest and are cited in §2.2: one lets a named person sign a file's binding, the other points from a file to consent held elsewhere. Neither asks the depicted performer to sign the words before the render and the bytes after it.

### 1.4 · The second problem: consenting to words, receiving pictures

A person who agrees to appear in a generated film agrees, at best, to a screenplay. What is released is not a screenplay. It is pictures a model made, and a model invents: a gesture the script did not call for, a costume, a crowd, an expression, a line read with a meaning the words did not carry. **Consent to a script is not consent to a render.** The design therefore asks for consent twice, and the second time over the exact bytes that will be released, not over a description of them.

### 1.5 · What this does not promise

The design does not promise anyone a living. A lent face does no acting; the model does. A face can appear in any number of films at once, and invented faces cost nothing, so a stranger's likeness is worth little in a market. The census found one measurement of what such a market pays: contributors to two face-licensing marketplaces that supply AI-generated dramas had earned between 15 and 700 US dollars in total (§2.4). The design is for people who want to make films with the people they love, and it lets whatever a film earns be shared among the cast on terms fixed before it is made.

---

## 2 · The prior art: the census

### 2.1 · The neighborhood

Three bodies of practice surround this design.

- **Permissioned likeness inside a video app.** A person records a short verification video, a likeness is created, and the person chooses who may use it; uses are visible to the owner, who can delete a video or revoke access. This is a shipped product (row (a) below).
- **Paid likeness and voice licensing.** Voice libraries pay the voice's owner by usage; face-licensing marketplaces let creators buy the use of a real person's face for AI-generated serials; production vendors refuse replica work without a signed, project-specific agreement (rows (b), (c), (d)).
- **Content provenance.** Industry standards let a maker attach a signed manifest to a media file stating how it was made, and the authors' own earlier work signs files with a passkey into a public log (rows (g) and §2.3).

### 2.2 · The census

**Census record:** depth `quick`, paper `every-face-signed-this-cut`.

**Pre-registration:** pushed on 2026-11-19 at 02:40 Pacific time, before the first query, to a private repository; the push record is the repository host's, and it cannot be inspected from outside. **Run date:** 2026-11-19.

**Declared aperture** (fixed before searching): the commercial web (AI video apps, likeness-licensing marketplaces, avatar and voice platforms, vendor documentation, press, the 2023 SAG-AFTRA digital-replica terms); non-commercial practice (community and amateur film, fan films, documentary and theater consent practice); a keyword search of the Google Patents index including published applications, through a general web index. **English only. Not run:** Chinese, Japanese and Korean (where a market in licensed digital humans is live, so the full census must search it natively), academic indexes, standards (the provenance-signature mechanism is inherited from an earlier census of the authors and not re-searched), law reviews, and Khmer. **Controls:** a known product for the web (the permissioned-likeness feature of row (a)) and a known patent for the patent index (US10853717B2). Both were seen.

**Conjuncts, in kill-first order, with predictions registered before any query.**

- **(a)** A person's own AI likeness, enrolled by that person with a liveness check, which others may put in their AI-generated videos only with that person's permission.
- **(b)** The person whose likeness appears is paid a share of what the work earns.
- **(d)** The shares are fixed in a signed agreement before generation, an estimate of screen time from the screenplay being only the default.
- **(c)** An open casting call: an author posts a role in one work and any holder may offer their likeness for it.
- **(h)** Viewers' thanks are split by the signed shares from the first dollar, with no platform cut.
- **(e)** Two consents per work by each depicted person: one on the script text, one on the exact final file before release.
- **(g)** A public record over the final file holding each depicted person's own signature, checkable by any viewer.
- **(f)** The likeness model is cryptographically unusable except under a per-work signed release, not merely refused by policy.

(The letters are as registered; the order is the kill-first order of the predictions.)

| Row | Predicted | Found | Their first public date | Ours, earliest (proof-backed) | Verdict |
|---|---|---|---|---|---|
| **Control (web):** a permissioned likeness feature in a video app | found | seen (row (a)) | — | none | **Seen.** |
| **Control (patents):** US10853717B2 | found | seen, by a site-restricted web query (not through the patent index's own search) | — | none | **Seen.** The NOT FOUND rows below stand as weak nulls |
| **(a)** verified, permissioned likeness | killed | **Sora "cameos"** (OpenAI, launched 2025-09-30), as reported: *"You record a short video following on-screen instructions to verify your identity and capture your likeness"*; *"you decide who can use your cameo (just friends or everyone)"*; *"OpenAI can't generate anyone from a prompt or photo unless they've submitted a verified cameo first."* [3] | 2025-09-30 (press) | none | **KILLED.** Not claimed |
| **(b)** the likeness owner is paid | killed or narrowed | **ElevenLabs** voice payouts: *"Earnings are calculated based on usage by paid users"*, the rate set by the owner's chosen notice period [4]. **ActID** and **New Claw** (face-licensing for AI dramas): about 300 people licensing their likenesses; *"Creators pay between 99 and 500 yuan per episode, while the platform takes a 10% commission"*; New Claw contributors *"set a minimum licensing price of 500 yuan per image"* [5] | undated; 2026-07-27 (press) | none | **NARROWED.** Payment to a likeness owner per use or per episode is public. A share of what the *work* earns was not found (weak) |
| **(d)** terms fixed in a signed agreement before generation | killed at mechanism | **Respeecher**: *"Without a signed, project‑specific agreement, we simply don't start any digital replica work"*; terms to *"Spell out pay for AI voice work clearly — session fees, reuse, and any extra rates"* [6]; fixed splits agreed before production are ordinary in film and music | 2026-08-13 | none | **KILLED** at mechanism. Not claimed |
| **(c)** an open call for one work | narrowed | ActID and New Claw are **catalogs** of faces that creators browse and buy [5] | 2026-07-27 | none | **CONTRAST.** A browsable catalog, the opposite of a call. An author's call answered by likeness holders for one work: **not found** (weak) |
| **(h)** thanks split by signed shares, no platform cut | narrowed | no query was aimed at it | — | — | **NOT RUN.** Not claimed |
| **(e)** two consents: script, then exact final file | narrowed | Respeecher: a signed project agreement before work, and advice to *"give the actor or their representative the right to listen to AI‑generated lines before final approval"* [6]. Sora: the owner can *"see all videos featuring your likeness including drafts"* and *"delete any video or revoke access anytime"* [3] | 2025-09-30; 2026-08-13 | the passkey press over exact text, block 975913 (§2.3) | **NARROWED.** Consent before work, review of output and an after-the-fact veto are public. Two cryptographic signatures by the depicted person, the second over the exact final bytes: **not found** (weak) |
| **(g)** each depicted person's signature, checkable by viewers | narrowed | **Truepic and Revel.ai**: a generated likeness video *"signed as an AI generation with Truepic's C2PA transparency tools and the creators, Revel.ai"* [7]; the depicted person signs nothing. **Found after the census by the adversarial reader (§13.1), re-read:** the **CAWG Identity Assertion 1.1** (*"DIF Ratified Specification 16 May 2025"*) may be *"repeated any number of times to convey information specific to distinct named actors"*, a signature *"reflective of the named actor's authorization of or active participation"*, over a list that *"MUST include a hard binding assertion"*; its recommended roles are creator, contributor, editor, producer, publisher, sponsor and translator, and other values may be used [13]. The **CAWG Consent Assertion** draft (*"Version 1.0 Draft 12 July 2026"*) *"carries a signed, machine-readable reference from a digital asset to an authoritative source of consent"* for a *"subject"* or *"performer"*, identifying the asset by its hard binding, and *"The signer does not declare the consent itself"* [14] | 2025-05-16; 2026-07-12 | the passkey-signed file record in a public log, block 959585 and block 975913 (§2.3) | **NARROWED.** A named person signing a file's binding is public, and so is a file pointing to a performer's consent held elsewhere. The depicted performer's own signature over the screenplay before the render and over the exact final bytes after it, in a public append-only log, checkable by a viewer: **not found** (weak) |
| **(f)** likeness unusable without a per-work signature | not found | one query, no candidate. The nearest public forms are a *policy* gate (row (a): the platform *"can't generate anyone … unless"*) and, found by the adversarial reader and not re-read, the confidential-computing practice of releasing a model's key only after hardware attestation | — | none | **NOT FOUND** as stated (weak, one query); key release gated on attestation is a public practice and narrows Variant A. The adversarial reader also showed that the guard protects less than its wording claimed (§7.4) |
| **Composition:** all conjuncts in one system | not found | none | — | — | **NOT FOUND** (weak: quick, English only, patents through a web index) |

**Mechanism width and composition width.** At mechanism width the design is commons: a verified, permissioned likeness in a video app; payment to the likeness owner; a signed project-specific agreement before replica work; review of output and an after-the-fact veto; a provenance signature on a media file; a named person's identity assertion over a file's binding; a reference from a file to a performer's consent held by an authority. At composition width: not found, in the aperture above, on 2026-11-19. **Not found means not found in this aperture on that date; it never means new.**

**Predictions that missed.** Row (c) was predicted to narrow and found only catalogs, the opposite design, so an open call is closer to unclaimed than predicted; it is still not claimed apart from the composition. Row (g) was predicted to narrow; the quick census found only the opposite assignment of the signature (the maker signs) and reported it not found, and the adversarial reader then found the two industry specifications that do narrow it. The census missed them because they live in a standards body's own pages, a neighborhood the quick depth did not search. Row (h) was never searched: a coverage miss, not a finding. A Chinese marketplace surfaced through English press although Chinese was not run, which says the market is live and must be searched natively.

**The survivor, in one sentence, as narrowed after the adversarial pass.** *Each credited performer presses their own passkey twice, over the screenplay and then over the exact final file and its listed renditions; the presses are recorded with per-party salts in a public append-only log and their statements travel with the film, so that anyone holding the released bytes can check both presses for every lent role; and a party holding only the stored likeness cannot render it without such a press.* §15 claims that, and nothing wider.

### 2.3 · The authors' own prior disclosures

*The Press Travels With the Message* [8] already discloses a passkey signature (a WebAuthn assertion with user verification) over exact text, recorded in a public append-only log, carried with the message and checked in the reader's own browser, together with the limits that bind this paper too: a press shows that a passkey pressed, never that a person did, and a name binding adds accountability to a name, never identity (block 975913, 2026-11-15). *B-Links* [9] already discloses a signed provenance record for a shared file (block 959585, 2026-07-25). The authors' open specification of signed statements [10] reserves, since 2026-11-13, an agreement pressed once by each of two parties over the same text with salted fingerprints, and, since 2026-11-19, a seat holder's own record of a film's premiere. *The Song That Is Not His* [11] is the opposite case: generation in the voice of artists murdered with no estate and no record of intent, where consent is *not obtainable*, and not merely unobtained (block 962355, 2026-08-14). None of these discloses a depicted person's signature over a film's screenplay and its final bytes, or a likeness that renders only under such a signature.

### 2.4 · Findings the census was not looking for

- **The livelihood claim, measured once.** On ActID and New Claw, contributors *"have earned between $15 and $700"* (as reported in July 2026, citing another outlet) [5]. That is one report from one market, and it is the reason §1.5 promises no living.
- **The two things these markets do that this design refuses.** Both take a commission on the likeness owner's earnings, and both sell faces from a browsable catalog. Here the studio takes no share of what a film earns (§10), and there is no index of faces (§5).
- **The nearest form of leaving.** The permissioned-likeness product makes the owner a co-owner of each video with a right to delete it after the fact [3]. §11 replaces the after-the-fact delete with a press, and states what a press cannot recall.

---

## 3 · The mechanism on one page

### 3.1 · Roles

| Role | Who | Holds |
|---|---|---|
| **Holder** | a person who has enrolled their own likeness | a passkey; a public name page (`@name`) listing that passkey; their likeness model, encrypted |
| **Author** | a person making a film | the screenplay, the casting call, the render budget |
| **Actor** | a holder cast in a lent role (the *depicted person*, the *performer*) | their two presses for that film |
| **Studio** | the operator of the render service (here, THonly.com) | the encrypted likeness models at rest; compute; the release |
| **Log** | a public append-only log of signed statements | salted fingerprints of every press, in order |
| **Viewer** | anyone holding the film | the file, its release manifest, and a checker |

### 3.2 · The flow

```
  HOLDER                AUTHOR                 STUDIO                  LOG            VIEWER
    │                     │                       │                     │               │
 ①  │ live capture ──────────────────────────────►│ likeness model,     │               │
    │ (tied to passkey)   │                       │ ENCRYPTED; key only │               │
    │                     │                       │ the holder can open │               │
 ②  │                     │ casting call ────────►│ (no index of faces) │               │
    │◄────────────────────│ offer: screenplay,    │                     │               │
    │                     │ role, style, shares   │                     │               │
 ③  │ PRESS 1 over the offer text ───────────────────────────────────►│ salted        │
    │ (any edit = new offer, new press)           │                     │ fingerprint   │
 ④  │ releases the work key, bound to PRESS 1 ──►│ RENDER (this work   │               │
    │                     │                       │ only)               │               │
 ⑤  │◄──────────────────────── exact final file ──│                     │               │
    │ fingerprint computed ON THE HOLDER'S DEVICE │                     │               │
 ⑥  │ PRESS 2 over that fingerprint ─────────────────────────────────►│ salted        │
    │ (no PRESS 2 from any actor → this cut       │                     │ fingerprint   │
    │  is not released)                           │                     │               │
 ⑦  │                     │                       │ RELEASE: the file + │               │
    │                     │                       │ a MANIFEST of every │               │
    │                     │                       │ statement text ─────────────────────►│
 ⑧  │                     │                       │                     │◄── check ─────│
    │                     │                       │                     │  recompute    │
    │                     │                       │                     │  fingerprint; │
    │                     │                       │                     │  each role:   │
    │                     │                       │                     │  PRESS 2 over │
    │                     │                       │                     │  THIS file by │
    │                     │                       │                     │  a passkey    │
    │                     │                       │                     │  its @name    │
    │                     │                       │                     │  page lists   │
```

### 3.3 · The guarantees, stated precisely

- **What a holder of the released bytes can check:** for every role the manifest names, a statement exists in the log, made by a passkey that the role's `@name` page lists, over the fingerprint of the bytes in hand (the master file or a listed rendition); and a casting statement by the same passkey over the screenplay offer that the release statement refers to, earlier in the log's order.
- **What nobody can check:** that the person whose name it is pressed (a passkey can be shared, synced or held by software); whose face is on screen (a capture can be spoofed at enrollment, §4.1); that the performer understood the cut; that no uncredited likeness appears in the frames (§9.4); that consent still stands after release (§11); anything about a copy whose bytes differ from the released ones (§9.5).
- **What a party holding only the stored likeness cannot do:** render it without a key that the performer's authenticator derives for one work (§7). What the operator who runs the press page and the render can still do, and why that is trust and not a property, is stated in §7.4 and §13.3.

## 4 · Enrollment: a likeness only from its holder

### 4.1 · The act

A likeness is enrolled by its holder and by no one else. The holder makes a live capture (a short guided video with face and voice) on their own device, in the same session in which their passkey presses an enrollment statement. The capture is never accepted as an upload of existing photographs or video, because an upload can be of anyone. The enrollment statement binds the likeness model's fingerprint to the holder's passkey, and the holder's public `@name` page lists that passkey.

**What enrollment binds, and what it does not.** It binds a passkey to a capture. It does not bind the capture to the face of the person holding the passkey. Feeding a swapped face into the camera stream, through a virtual camera, is a known and growing attack on remote liveness checks, so the live-capture requirement is a rule kept by the capture app, not a property. A person could enroll someone else's face, and the record would then truthfully show that their passkey pressed over a film showing that other person. This is why the check reports credited *names* and never claims to know whose faces are on screen.

### 4.2 · Who can enroll

- **Adults only.** The authors' agreement form excludes minors from its scope, so a child is not cast. This is a rule: the exclusion is written into the form, and no age signal stands behind it.
- **Only the living who can press.** A person who has died cannot press. That too is a rule rather than a property: a synced or shared passkey presses for whoever holds the device. The case of artists who can no longer consent is a different mechanism with a different answer [11].
- **No lookalike check against people who never joined.** Keeping out every lookalike would require matching generated faces against a store of faces of people who never enrolled. The design refuses to build that store; a person's face is used to recognize anyone only if that person enrolled and agreed to the check (§9.4). Public figures appear only by enrolling and pressing, like anyone else.

### 4.3 · What enrollment does not do

Enrollment does not license anything. It creates the encrypted likeness and nothing more. No author can see it, search it or browse it (§5). It confers no rank, no counter of films and no measure of demand.

### 4.4 · Render style does not change consent

A likeness can be rendered lifelike, as a cartoon, as a three-dimensional figure or in any other style. **Consent attaches to whether the person can be recognized, never to the style.** A cartoon of a person is still that person. Every style therefore takes the same two presses, and the casting statement names the style, so that a person who agreed to be drawn is never released as a photograph.

---

## 5 · The casting call

### 5.1 · The author calls; holders answer

An author posts a call for a role in one work: the role, its share of the screenplay, the render style, the proposed shares, the release date. Holders who see the call (because the author shared it with them, or because they chose to read open calls) may answer it. **There is no catalog of faces.** No author can browse enrolled likenesses, search them by appearance or sort them by popularity. A face enters a film only in answer to a call, by its holder's own act.

The design question this answers is *is there an index?* A catalog of faces is an index of people sorted by what buyers want, and it turns the people in it into stock. The census found exactly that design in the market (§2.2, row (c)).

### 5.2 · Lent, never sold

A likeness is lent to one work. The lend is not transferable: an author cannot assign a cast member's consent to another author or another film, and cannot accumulate rights to a face. A second film needs a second call and two new presses.

---

## 6 · Press one: the screenplay

### 6.1 · What is pressed

The casting statement is one exact text, written by the author and shown to the actor in full. It carries:

1. the work's identifier and the screenplay's fingerprint, with the screenplay itself attached for the actor to read;
2. the role, and every scene the role appears in;
3. the render style;
4. the shares: what fraction of the film's receipts each cast member receives, fixed now (§10.1);
5. the release terms: the free public release date, and the actor's right to end the studio's distribution of the film (§11);
6. a statement that the likeness may be rendered for this work and no other.

The actor presses it with their passkey. The log records a salted fingerprint of the statement; the text travels with the parties and later with the film's manifest.

### 6.2 · Acceptance mirrors the offer

Any change to the text, to the screenplay, the role, the style or the shares, is new bytes, and new bytes are a new offer. The actor's earlier press does not carry over to it. This is a property of signing exact text, not a rule anyone enforces: a press over one text verifies against that text and no other.

### 6.3 · Withdrawal before the render

Until the work key is released for rendering (§7), the actor may withdraw their press by a second statement. Which came first, a withdrawal or the release of the key, is decided by the log's order, never by the minute recorded in either.

---

## 7 · The stored likeness renders only under a press

### 7.1 · The aim

The aim is that the studio holding a person's likeness cannot render it without that person's press, and that this be true *because of how the likeness is stored*, not because the studio promises it.

### 7.2 · The design

The likeness model is stored encrypted. The key that decrypts it is wrapped so that only the holder's own authenticator can unwrap it: a passkey can derive a secret from a value the relying party supplies (the WebAuthn pseudo-random function extension does exactly this), and the derivation is available only during a press on the holder's device, its output returned to the script of the page that requested the press. At the casting press, the holder's device derives a **work key** bound to the casting statement's fingerprint and an expiry, and releases it to the render service for that work alone. Without a press there is no work key, and the stored model is ciphertext.

```
  AT REST                         AT A CASTING PRESS                   AFTER THE RENDER
  ─────────────────────────────   ─────────────────────────────────    ───────────────────────────
  likeness model = ciphertext     holder's device + passkey →          work key expires;
  studio holds no key that        work key, bound to                   the model returns to
  opens it                        H(casting statement) + expiry        ciphertext at rest
                                  → render service, this work only
  PROPERTY (vs the studio         ─────────────────────────────────    RULE: that the service kept
  at rest)                        the service holds PLAINTEXT          no copy while it had one
                                  while it renders                     (§7.4)
```

### 7.3 · What this makes true

- **Against a party holding only the stored ciphertext, it is a property.** A breach of the likeness store or a stolen backup yields ciphertext and no key. No one has to keep a rule for this to hold.
- **Against rendering for the wrong work, it is a property of the key.** A work key is derived from one casting statement's fingerprint. It opens the model for the render that statement authorizes; an author cannot reuse it for another film.

### 7.4 · What it does not make true

The guard was first stated as making the likeness *unusable* without a press. The adversarial pass (§13.1) showed that against the operator it is trust, not a property, at four points, and that the stored model matters less than the wording suggested.

- **At enrollment,** the operator trains the model from the plaintext capture and could keep the capture.
- **At the press,** the derived key is returned to the script of the press page, which an operator serves. In the authors' estate the press page and the render are run by different bodies, which separates the duties; it is still trust in each of them.
- **During a render,** the service holds the likeness in the clear and could keep a copy. Variant A (§12.1) narrows this with attested confidential computing, where the performer's device checks an enclave's attestation before releasing the key; key release gated on attestation is public practice, and it moves the trust to the hardware vendor rather than removing it.
- **No stored model is needed to render a person.** Tuning-free, identity-preserving generators render a person from a single reference image [16]. The enrollment capture, which the operator saw, or one frame of a released film, which anyone can download, is enough. Encrypting the stored model protects the stored model, and the claim is stated at that width: a party holding *only* the stored ciphertext cannot render the person.
- **The published frames are not protected.** Once a film is released, anyone can train on it or render from it. This is the most important limit of the design and §16 states it first.
- **An outside tool can render anyone.** The claim is about this system's records: a viewer can tell a film made under these presses from one that was not, and nothing more.

## 8 · Press two: the exact final file

### 8.1 · What the actor is shown

When the author has a cut they intend to release, every actor in it is sent **the exact file** to be released. The actor's device plays it and computes its fingerprint (a cryptographic hash of the bytes). Who wrote the code that computes it decides what kind of guard this is. If the actor uses a checker of their own choosing, one the operator did not write, the guard is a property: a studio that showed one cut and released another would release a file whose fingerprint matches no actor's press. If the fingerprint is computed by the press page itself, which an operator serves, the guard is trust in that operator (Variant G, §12.7). Either way the actor presses over a fingerprint computed from bytes delivered to their device, never over a number the studio merely states.

### 8.2 · What is pressed

The release statement names the work, the role, the casting statement it rests on (by fingerprint), the fingerprint of the final master file, and the list of fingerprints of every rendition the studio will serve: each quality level, and for streaming the per-segment fingerprints, produced before the press. The actor's device computes the master's fingerprint; the rendition list is the operator's report, and the actor presses over it as reported. The log records a salted fingerprint.

### 8.3 · A cut with a missing press does not clear

A cut is released only when every lent role in it has a release press over that cut's fingerprint. Invented roles need none. If any actor does not press, by declining or by not answering, that cut does not clear. The author may make another cut, without that role or with that role changed, and a new cut is new bytes: **every remaining actor presses again**, because consent was to the old file, not the new one. A recut that only removed one scene still changes the bytes.

### 8.4 · Declining without pressure

- A decline needs no reason and is never shown to anyone but the author, who must know which role to change.
- The system sends no reminder, shows no countdown and never displays a list of who has and has not pressed to the other actors.
- The release page never shows that a role was cut, who declined, or that anyone did. **A released film shows what is in it, never who is absent.** A rendered absence is an accusation, and the design does not make one.

### 8.5 · Why the second press is over bytes, not a description

A description of a cut can be true and still misleading: *the scene where you leave the room* says nothing about how the model drew the leaving. A fingerprint describes nothing and leaves nothing out. The actor agrees to exactly the file they watched, and the viewer can check exactly that.

### 8.6 · Drafts

The release press comes after the render, so it cannot be what permits the render; the casting press is. Between the two, an author may render many drafts, retakes and alternate cuts showing the actor, and the model may invent in each of them. The design therefore lists **every render that uses an actor's likeness, draft or final, to that actor and to no one else**, as the permissioned-likeness product found in the census does for its owners (§2.2, row (e)), and **deletes the drafts when the film is released or when the casting key expires, whichever comes first.** Both are rules kept by the studio. Variant F (§12.6) states the alternatives, including a fresh key per render, which would make the listing a property at the cost of a press per render.

## 9 · The public record and the viewer's check

### 9.1 · The release manifest

The released film carries, beside it, a manifest: every casting statement and every release statement, in full, with their salts. The log holds only fingerprints, each salted with a salt of its own party's, so no two records in the log can be paired, even when every actor pressed a release statement over the same file. The log alone therefore says nothing about who appeared in which film or how large a cast was; a person holding the film and its manifest can check everything.

```
  PUBLIC LOG (anyone)                  MANIFEST (travels with the film)
  ──────────────────────────────────   ────────────────────────────────────────
  record 4,812,301: salted fp, time    casting statement, role "Mother":
  record 4,812,977: salted fp, time       work id · screenplay fp · style ·
  record 4,815,040: salted fp, time       shares · terms · salt
  ...                                  release statement, role "Mother":
  (no names, no titles, no files)         work id · casting fp · FILE fp · salt
                                       ... one pair per role ...
  ──────────────────────────────────   ────────────────────────────────────────
  CHECK = hash(salt ‖ statement) is in the log, pressed by a passkey that the
          role's @name page lists, and the FILE fp equals hash(the file I hold)
```

### 9.2 · The check, step by step

1. Compute the fingerprint of the file in hand.
2. For each role in the manifest, find its release statement, confirm the file fingerprint in it equals the one just computed, confirm the salted fingerprint is in the log, and confirm the passkey that pressed it is one that the role's `@name` page lists.
3. Confirm the release statement names a casting statement that is also in the log, pressed by the same passkey, earlier in the log's order.
4. Report: *every lent role in this film's manifest has a casting press and a release press over this file, by passkeys listed on those roles' name pages.*

The checker never reports *verified*, never reports *consented*, never reports who held a passkey and never reports that a person was present at a device. Those are not what a press shows [8][10].

### 9.3 · "Every lent face signed this cut," stated exactly

A film may mix lent faces with invented ones: the author's own likeness and a friend's in the lead roles, invented co-stars, an invented crowd. Only a **lent** face belongs to someone, so only a lent face is signed. An invented face belongs to no one and needs no press; requiring one would make an ordinary film impossible to make, and would protect no one. The credits mark every role either **lent** or **invented**, so a viewer knows which faces the check speaks for.

The line is therefore a compression. Its exact form is: **for every lent role in the manifest, a passkey listed on that role's `@name` page pressed over the screenplay offer and then over the fingerprint of this exact file.** The design guarantees the record. It does not guarantee the person behind the passkey, and the paper uses the short line only where this sentence stands behind it.

### 9.4 · Invented roles and extras

Every figure that is not a lent role (a named co-star, a crowd, a passerby, a face in a photograph on a wall) is **invented**: generated, belonging to no one, and credited as invented. Two rules keep an invented face from being a real one. At render time each invented face is matched against the enrolled likenesses of people who agreed to that check at enrollment, and one that matches an enrolled likeness above a threshold is rejected, which keeps an enrolled holder out of a film they did not press for. And an invented role is never described in the screenplay as a real person. Against a person who never enrolled, no check is possible: a model can invent a face that happens to resemble a real person, and image models have been shown to reproduce individual training images, photographs of identifiable people among them [15]. The record can say who pressed; it cannot prove the negative that no unconsenting person appears. That is why the check reports lent roles, never *every face in the frames*.

### 9.5 · Copies, renditions and streams

A repost on another platform is almost always re-encoded, and a re-encoded file has different bytes, so its fingerprint matches no release press. The studio's own renditions are different bytes from the master too, which is why the release press covers the rendition list (§8.2); a viewer who downloads a listed rendition can check it. A viewer who *streams* cannot hash what they watch unless their player checks each segment against the pressed segment fingerprints (per-segment hashing of streamed media is public practice in the industry provenance standard, and is not claimed); otherwise, for a stream, the check is the page's word. And a check is only as good as the checker: a viewer who uses the checker the film's own page offers is trusting that page [8]. The check is exact on listed bytes, through a checker the viewer chose, and silent on everything else. Variant C (§12.3) finds the record again for an unlisted copy by perceptual matching or a watermark, and reports it as a *likely match to a released film*, never as a check passed.

### 9.6 · What becomes public, and to whom

An actor's participation is public **to anyone who holds the film and its manifest**, in the way screen credits are. It is not public to someone who only reads the log: per-party salted fingerprints cannot be paired with each other, or with a name or a title, without the manifest. A holder who does not want participation discoverable at all should not answer the call; the design offers no anonymous role, because an anonymous face is not checkable.

**The index others can build.** Checking a lent role by name requires that the manifest show which passkey, listed on which `@name` page, pressed. So anyone who crawls released films and their manifests can list every film a person appeared in, exactly as anyone can compile screen credits today. The institution builds no such list and never shows a person's films on their own name page; it cannot stop others from compiling one from public manifests. The default is that the manifest is published with the film, because that is what lets anyone holding a download check it, and because a credit on the film is a credit *on the subject*, never on the person. The casting statement says so once: the credit is public with the film. Variant D (§12.4) states the alternatives, including a manifest given only to those who play the film, and what each costs.

## 10 · Shares, thanks and the premiere (context, not claimed)

The census killed or did not search these parts (§2.2, rows (b), (d), (h)), and they are not claimed. They are stated because the mechanism was designed with them, and a reader should know the whole.

### 10.1 · Shares fixed before generation

The shares are fixed in the casting statement, before anything is generated. A screen-time estimate from each role's pages in the screenplay is only the default the author proposes; each actor accepts by pressing. Shares are never measured from the render: in a generated film, screen time measures nothing an actor did, the author could regenerate it at will, and a measurement would rank the cast by minutes.

### 10.2 · Thanks from the first dollar

Viewers may thank a film after watching it. A thank in money is split by the signed shares **from the first dollar**. It is never netted against the author's compute bill: a thank may support creative work, but it must never repay a cost, because a gift that repays a bill becomes a rebate. The author's compute is the author's own gift to the film; as the star, the author usually holds the largest share. A thank in words or the ledger's gratitude units goes to a person thanked by name, never divided by a formula. The studio takes no share of either.

### 10.3 · The premiere and its tickets

An author may pre-sell seats at a premiere to fund the compute. A seat buys the event, never the film, which is released free at a date fixed before the first seat sells. A seat is never a share in what the film earns, the cast member who sells one earns nothing per seat, there is one price, and a seat may be given to a named person and passed on only at the price paid. Nobody is charged until enough seats cover the studio's quote; the money is the author's, held by a licensed payment processor, never the studio; it is spent only on that film's compute and storage; and if the film is not released by its date, the unspent part is refunded automatically, a fact stated once at purchase. A seat is not a token and cannot be resold above its price. After the premiere, a seat holder may press a record of having held the seat into the public log, as a keepsake that is theirs [10].

### 10.4 · Hosting

A film released free is stored as a gift: free within a short format, and above it for a one-time payment per gigabyte, never a monthly rental, so that no film is held hostage to its author's continued payment. Serving it is a running cost of the gift, paid at cost by the institution's registry, never from the film's thanks and never metered against the author by views.

### 10.5 · Advertising

An advertisement may be offered while a film is being made, at a costly step, after free and paid alternatives, side by side with paying and played only on a tap; it is never shown before, during or after a film, or beside one.

### 10.6 · The film's license

A film released free at the studio's venue is licensed by its author under **CC BY-NC-ND 4.0** by default: anyone may watch it and share it unchanged, with credit, not for commercial use, and not as a derivative work. The license covers the film's copyright and nothing else. The Creative Commons 4.0 licenses state that they do not license publicity, privacy or other personality rights, so **a film's license never licenses the cast's likenesses**; a recut, a remix or a sequel that shows a lent face needs that person's presses, as a new work. A recut made by someone else is new bytes and fails the check, correctly. This paper itself is CC0; the films the mechanism produces are not.

---

## 11 · Leaving

An actor may end the studio's own distribution of a released film by a press. Their share ends with it. Because a film's release rests on every actor, **one actor's leaving ends the studio's distribution of the whole film**, for every cast member. The studio stops serving the film; copies already made elsewhere cannot be recalled, and the casting statement says both things once, at casting. The design does not show a film as *withdrawn*, *removed* or *taken down by* anyone; it is simply no longer served.

**The record does not change when an actor leaves.** The log is append-only, so the release press stays in it and keeps verifying. A leaving press is a separate statement that ends distribution; it is not a withdrawal of the release press, and checkers never report a film or a press as *withdrawn*, because a mark that follows every copy would announce one person's departure to every viewer forever. The cost of that choice is stated plainly: **a check shows consent as given at release, never consent now.**

This replaces the after-the-fact delete found in the market (§2.4) with a press, and differs from it in one way: the delete there makes the owner a co-owner of each video inside one platform; the press here ends one operator's distribution of one released work, and says plainly that it can do no more.

## 12 · Variants

### 12.1 · Variant A: who can open the likeness during a render

**(i)** The work key is released to the studio's render service, which holds plaintext during the render (§7.2; the default). **(ii)** The render runs in attested confidential computing: the holder's device checks the enclave's attestation before releasing the work key, and the enclave releases only the rendered frames. **(iii)** The render runs on the holder's own device or one they designate, and only frames leave it. (ii) and (iii) narrow the rule of §7.4; (iii) is limited by the device.

### 12.2 · Variant B: the grain of the second press

**(i)** One release press per role over the whole file (§8; the default). **(ii)** One press per scene the role appears in, over each scene's fingerprint, with a final press over the assembled file. (ii) lets an actor approve most of a film and decline one scene, at the cost of more presses.

### 12.3 · Variant C: finding the record for a copy

**(i)** None: the check is exact on the released file only (the default). **(ii)** A perceptual fingerprint of the released film is published beside the manifest, and a copy is matched against it. **(iii)** An invisible watermark carries the work's identifier. (ii) and (iii) report a *likely match*, never a passed check.

### 12.4 · Variant D: how open the casting record is

**(i)** Per-party salted fingerprints in the log, statements in a manifest published with the film, the casting statement saying so (§9.6; the default). **(ii)** The manifest given only to those who play the film, by the player, and not published beside it, so that a crawler of public pages cannot compile who appeared in what; a viewer who holds only a downloaded file then cannot check. **(iii)** Release statements published unsalted, so the cast of any film is discoverable from the log alone. **(iv)** Casting statements kept off the manifest, so a viewer checks release presses only. (ii) trades checkability for privacy; (iii) trades the actors' privacy for discoverability; (iv) loses the check that the cut rests on a casting the actor pressed. A per-film key for each actor would make films unlinkable to each other and would break the binding to the actor's name, so it is not offered.

### 12.5 · Variant E: style

**(i)** The casting statement names one style (§4.4; the default). **(ii)** It names a set of permitted styles. **(iii)** It permits any style. (iii) is permitted but weakens the actor's knowledge of what they agreed to; the second press still binds the actual file.

### 12.6 · Variant F: drafts

**(i)** Nothing governs drafts. **(ii)** Every render that uses an actor's likeness, draft or final, is listed to that actor and to no one else. **(iii)** As (ii), and drafts are deleted when the film is released or when the casting key expires, whichever comes first (§8.6; the default). **(iv)** Each render needs a fresh, short-lived key from the actor's authenticator, so the actor's device sees every render it permits, at the cost of a press per render.

### 12.7 · Variant G: who computes the release fingerprint

**(i)** The press page computes it from the bytes it delivered (trust in that page's operator). **(ii)** A checker the actor chose, one the operator did not write, computes it from the bytes it played (a property, §8.1). **(iii)** Both, and the press proceeds only if they agree.

## 13 · The adversarial surface

### 13.1 · What the hunt for a counterexample killed and narrowed

The thesis was attacked twice before this paper was pushed. The first pass was the author's own, during the paper-worthiness check. The second was a separate adversarial reader with no write access, so that the author did not refute, or rescue, its own claim. Neither pass killed the composition. Together they narrowed it in these ways, each now in the text.

- **"Consent" became "a press."** A signature shows that a passkey pressed over exact bytes, never that the person whose name it is did, or understood what they watched (§9.3).
- **"Every face" became "every lent face."** The record lists who pressed and cannot prove the negative that no unconsenting likeness appears: a face a model reproduced from its training data, or one that happens to resemble a real person (§9.4). And it never shows whose faces are on screen, because a capture can be spoofed at enrollment (§4.1). The founder then settled the rest of the question: invented co-stars and extras are allowed and need no press, because requiring a press for a face that belongs to no one would make an ordinary film impossible and protect no one; the credits mark every role lent or invented (§9.3). The title's line is a compression of §9.3.
- **"Unusable without a press" became "unusable by a party holding only the stored ciphertext."** Against the operator the guard is trust at four points: enrollment, the press page, the render, and the fact that one frame suffices for current tools to render a person (§7.4).
- **"Protects people from deepfakes" was killed.** The published frames remain material for anyone. The claim is consent *provenance* for a released work, never deepfake prevention.
- **"Checkable anywhere" became "checkable on listed bytes, by a checker the viewer chose."** Re-encoded copies fail; the studio's renditions must be listed in the press; a stream is checkable only by a player that checks segments; a checker the film's page offers is that page's word (§9.5).
- **The release press governed publication, not drafts.** Version 2 lists every render to the actor and deletes drafts at release (§8.6), as the market's nearest product already shows its owners every draft.
- **"Checkable by name" builds an index others can compile** (§9.6).
- **Leaving cannot rewrite an append-only record:** a check shows consent at release, never consent now (§11).
- **The exclusions are rules, not properties:** minors, the dead and lookalikes are kept out by the form and the app, not by construction (§4.2).
- **Prior art the census missed:** two industry specifications narrow the record half of the claim (§2.2, row (g)).
- **Supported, not refuted:** a casting statement that names the role, the scenes and the style is the kind of specific description of intended uses that digital-replica law in at least one jurisdiction asks for; the paper draws no conclusion about enforceability (§16).

### 13.2 · Attacks and what answers them

| Attack | What answers it | Strength |
|---|---|---|
| The studio shows the actor one cut and releases another | the actor's chosen checker computes the fingerprint from the bytes it played (§8.1, Variant G) | property with an independent checker; trust with the press page's |
| The author edits the screenplay after the actor pressed | an edit is new bytes and a new offer (§6.2) | property |
| The author reuses a casting for a second film | the work key is bound to one casting statement (§7.3) | property |
| A breach of the likeness store | the stored likeness is ciphertext with no key (§7.3) | property |
| The operator keeps the enrollment capture, the derived key or a render | not prevented; Variant A narrows the render (§7.4) | trust |
| Anyone renders the actor from one released frame | not answered; no stored model is needed (§7.4) | none |
| Someone enrolls another person's face by injecting a swapped camera stream | the capture app's liveness check (§4.1) | rule, and a weak one |
| A holder's passkey is shared, synced, stolen or held by software | not answered; a press shows a passkey (§9.3) | none |
| A generated extra resembles an enrolled holder | rejected at render by a match against enrolled likenesses that agreed to the check (§9.4) | rule |
| A generated extra resembles, or reproduces, a person who never enrolled | not answerable by this design (§16) | none |
| Drafts showing the actor are made and kept | every render is listed to the actor; drafts are deleted at release (§8.6) | rule |
| Pressure on an actor to approve, or not to leave | no reminders, no countdown, no visible waiting list, no rendered absence (§8.4) | rule; social pressure is not answered |
| A repost or a stream is presented as checked | the check fails on unlisted bytes; a likely match is never a pass (§9.5) | property of the check |
| A viewer is shown a fake checker page | a check is as good as the checker the viewer chose [8] | none by design |
| Someone compiles every film a person appeared in | per-party salts keep the log unpairable; public manifests do not (§9.6, Variant D) | partial |

### 13.3 · Remove the enforcer: which guards are properties

A guard is a **property** if it holds when no one is enforcing it, and a **rule** if it needs someone to keep it at the moment it is tested.

| Guard | Property or rule | Why |
|---|---|---|
| A changed screenplay needs a new press | **property** | a signature verifies against one exact text |
| The released file is the one the actor approved | **property with an independent checker; trust otherwise** | it depends on who wrote the code that hashed it (§8.1) |
| A party holding only the stored ciphertext cannot render it | **property** | no key exists without the performer's authenticator |
| The operator cannot render without a press | **trust, not a property** | the operator sees the capture, the key and the render (§7.4) |
| A work key opens one work only | **property** | the key is derived from one statement's fingerprint |
| The log does not pair records or reveal who appeared in what | **property** | per-party salts; nothing pairs without the manifest |
| No catalog of faces | **rule** | nothing in a database prevents an index; the studio must not build one |
| Enrollment only by a live capture of the holder | **rule, weak** | a swapped camera stream defeats liveness checks (§4.1) |
| No minors | **rule** | the form excludes them; no age signal stands behind it (§4.2) |
| No one presses for the dead | **rule** | a synced or shared passkey presses for whoever holds it (§4.2) |
| No reminders, countdowns or visible waiting lists | **rule** | an interface can always add one |
| No *withdrawn* mark on a film or a press | **rule** | a checker could add one |
| Every render is listed to the actor; drafts are deleted at release | **rule** | the studio keeps the list and does the deleting (§8.6) |
| An invented face is not an enrolled holder | **rule** | a render-time match against enrolled likenesses (§9.4) |
| The studio takes no share of a film's receipts | **rule** | a price list could change |

Four guards are properties outright and one is a property only with an independent checker. The rest are rules or trust, and the design says so rather than calling them properties.

### 13.4 · Deletion test for the lineage material

Remove the Preamble's passage and every reference to it. The mechanism is unchanged: two presses, a manifest, a check, an encrypted likeness. The passage is a recognition of the problem's shape, tier *flourish*, and carries no load.

---

## 14 · What is disclosed and what is withheld

**Disclosed:** the composition of §15 and its variants; the statement contents (§6.1, §8.2); the release manifest's structure and the check (§9); the key structure at the level of §7.2; the guards and their classification (§13.3).

**Withheld:** the statement formats and field encodings; the key-derivation inputs, the expiry and the wrapping scheme; the enrollment capture protocol and its liveness thresholds; the render-time match threshold for extras (§9.4); the perceptual-fingerprint and watermark parameters (§12.3); the manifest's serialization; every interface. **Why:** the mechanism is designed and not built, and a specification for something unbuilt and unscheduled is the part most likely to be wrong. The claims are published so that the composition cannot be enclosed; the specification will be published when it is built and tested. The authors' open specification of signed statements reserves the record a seat holder keeps (§10.3) and will define its format when it is built [10].

---

## 15 · Enumerated claims

The claims below are the survivor of the census in §2, as narrowed by the adversarial pass of §13.1, and nothing wider. Claims 2 to 10 depend on claim 1 and are not claimed apart from it: a verified, permissioned likeness inside a video app, payment to a likeness owner, a signed project-specific agreement before replica work, review of output and after-the-fact deletion, a maker's provenance signature on a media file, a named actor's identity assertion over a file's binding, a reference from a file to consent held by an authority, per-segment hashing of streamed media, and release of a model key after hardware attestation are prior art, cited, and are not claimed. Each claim is disclosed for the public domain.

1. **The composition.** A computer-implemented system for producing a video that depicts one or more real persons by means of their digital replicas, in which: (a) each credited performer holds a passkey listed on a public name page, and a replica (likeness model) enrolled from a live capture made in the same session as a press of that passkey; (b) for each work, each performer presses with their passkey a casting statement over an exact text naming the work, the screenplay by fingerprint, the performer's role and the render style, any change to which text constitutes a new offer requiring a new press; (c) the performer's likeness model is stored encrypted and can be decrypted for rendering only with a key derived by the performer's authenticator for that work, bound to the casting statement, such that a party holding only the stored ciphertext cannot render it; (d) before release, each performer is given the exact final file, the fingerprint of which is computed on the performer's device from the bytes delivered to it, and presses a release statement over that fingerprint and over a list of the fingerprints of every rendition to be served, and a file lacking a release press from any performer of a lent role is not released; and (e) the presses are recorded in a public append-only log as fingerprints each salted per party, and the released file is accompanied by a manifest of the statements with their salts, such that any holder of the released bytes can recompute their fingerprint and check that, for every lent role in the manifest, a passkey listed on that role's name page pressed the casting statement and, later in the log's order, the release statement over those bytes.

2. **The work key.** The system of claim 1 in which the key of element (c) is derived by the performer's authenticator, during the casting press, by a pseudo-random function available only to that authenticator, from a value bound to the casting statement's fingerprint and an expiry, such that a key released for one work cannot open the model for another.

3. **Rendering custody.** The system of claim 2 in which the rendering runs (i) in the operator's service, which holds the decrypted model only during the render; or (ii) in attested confidential computing whose attestation the performer's device checks before releasing the key; or (iii) on a device the performer designates, from which only rendered frames leave.

4. **An unpairable log.** The system of claim 1 in which the per-party salts are chosen such that no two records in the log can be paired with each other, or with a name, a role or a work, without the manifest; and in which the manifest is (i) published with the film; or (ii) given only to those who play it, by the player.

5. **The cut and the recut.** The system of claim 1 in which any change to the final file, including a recut that removes a role or a scene, yields a new fingerprint for which every remaining performer presses again; a decline needs no reason and is disclosed only to the author; and no released page, list or reminder shows which performer declined, had not pressed or was removed.

6. **Grain of the release press.** The system of claim 1 in which the release press is made (i) once per role over the whole file; or (ii) once per scene in which the role appears, over each scene's fingerprint, with a press over the assembled file.

7. **Style bound to the casting statement.** The system of claim 1 in which the render style named in the casting statement is (i) one style; or (ii) a set of permitted styles; and consent is treated as attaching to the performer's recognizability in any style, every style requiring both presses.

8. **Lent and invented roles.** The system of claim 1 in which every role is credited as either lent or invented; an invented role, including a named co-star or an extra, needs no press, is generated, and is rejected at render time if it matches, above a threshold, the likeness of a holder who enrolled and agreed to that check; and in which the check reports only lent roles, never every face in the frames.

9. **The release fingerprint's checker.** The system of claim 1 in which the fingerprint of element (d) is computed (i) by the page that requests the press; or (ii) by a checker the performer chose that the operator did not write; or (iii) by both, the press proceeding only if they agree.

10. **Drafts.** The system of claim 1 in which (i) every render that uses a performer's likeness, draft or final, is listed to that performer and to no one else; and (ii) drafts are deleted when the work is released or when the key of element (c) expires, whichever comes first; or (iii) each render requires a fresh key from the performer's authenticator.

Claims 2 to 10 rest on narrow nulls in a quick, English-only census whose patent coverage was thin, and on an adversarial pass that found prior art the census missed; they are correspondingly weak. A full census may narrow any of the ten.

## 16 · Honest limits

- **The published frames are not protected.** Once a film is released, anyone can render the performer from one of its frames with no stored model at all, or train on it. Nothing here prevents that. The design records consent for a work; it does not prevent misuse of a face.
- **The operator is trusted.** It sees the enrollment capture, the press page receives the derived key, and the render holds the likeness in the clear. Separating the press page from the render, and confidential computing for the render, narrow that trust; neither removes it.
- **A press shows a passkey, never a person.** A passkey can be synced, shared, stolen or held by software, and user verification can be satisfied by a PIN. The record never shows that the person whose name it is pressed, or understood what they watched.
- **The record names lent roles, never whose faces are on screen.** A swapped camera stream can enroll someone else's face, so the record can truthfully show a passkey's press over a film depicting a different person.
- **It cannot prove that no one else appears.** A model can invent a face resembling a real person who never enrolled, or reproduce a person from its training data. The check is limited to lent roles.
- **The check is exact on listed bytes only.** A re-encoded copy fails; a stream is checkable only by a player that checks segments; a likely match by perceptual fingerprint or watermark is weaker and is never a pass; and a checker the film's page supplies is that page's word.
- **Consent at release, never consent now.** The log is append-only; an actor who leaves ends the distribution, and the record still shows the presses as given at release.
- **One person's choice binds the cast.** A single decline keeps a cut from release, and a single leaving ends the studio's distribution of the whole film. Among friends and family that is pressure the interface does not add and cannot remove.
- **The second press can be a formality.** An actor may press without watching. The design ensures they were given the exact file, not that they looked at it.
- **Drafts are governed by rule.** Every render is listed to the actor and drafts are deleted at release; the studio keeps both rules (§8.6).
- **Anyone can compile a person's films** from public manifests, as screen credits allow today (§9.6).
- **The exclusions are rules.** Minors, the dead and lookalikes are kept out by forms and apps, not by construction (§4.2).
- **A license is not a lock.** A film is licensed without derivatives and its license never licenses the cast's likenesses (§10.6), but nothing stops someone from recutting a downloaded copy anyway; the check of such a recut correctly fails, and enforcement is a matter of law, not of this design.
- **Nothing has been built or tested.** Every property in §13.3 is a property of a design. Field evidence is zero.
- **The census was quick, and it missed prior art.** It was English-only, reached patents only through a general web index, did not search standards bodies' own pages (where the adversarial reader then found two relevant specifications), the academic literature, law reviews or the Chinese, Japanese and Korean markets, and never searched conjunct (h). A null on the composition is weak evidence. One market measurement of what likeness owners earn (§2.4) is one report.
- **Law is not examined.** Right-of-publicity and digital-replica statutes, biometric-data law, labeling rules for synthetic media, the treatment of a revenue share as a contract for personal services, and pre-sales of event seats are questions for counsel in each jurisdiction. That a casting statement names the uses specifically is not a claim that it is enforceable anywhere.
- **No parameter is given.** Expiries, thresholds and encodings are withheld (§14).

## 17 · Predictions

No pre-registered prediction is made. The paper discloses a mechanism and asserts no empirical claim about behavior: it does not claim that actors will watch a cut before pressing, that the check will be used, or that the design will reduce misuse of likenesses. If the studio is built and a pilot is run, its predictions will be registered before its data is read.

---

## Coda

The commentator's lesser gods could not tell the double from the one who made it, and it did not matter, because the double taught only what it had been told to teach. The resolve was enough, and it was the Buddha's. A film cannot rest on that. Its doubles are made by a machine, for an author, out of other people's faces, and the person whose face it is may never see the film. So the resolve has to be written down, by the person whose face it is, over the words they agreed to and then over the exact pictures they were shown, in a place no one can quietly change. The viewer is a lesser god, and can now tell.

---

## Terms

| Term in this paper | Standard term |
|---|---|
| B-Double; lent likeness | digital replica of a real person's face and voice, licensed per work by that person |
| holder | person who enrolled their own digital replica |
| actor; depicted person; credited performer; lent role | person whose digital replica appears in a work as a lent role (the industry draft's *performer*) |
| author | creator of a generated film who casts it |
| studio | operator of the rendering service |
| press | WebAuthn passkey assertion with user verification over exact text |
| casting statement; press one | signed per-work likeness license over the screenplay, role, style and shares |
| release statement; press two | signed approval over the cryptographic hash of the exact final video file |
| work key | per-work decryption key derived by the holder's authenticator (WebAuthn PRF extension) |
| the log | public append-only transparency log of signed statements |
| salted fingerprint | hash commitment to a statement with a salt of its own party's, stored in place of the statement so that records cannot be paired |
| invented role | generated character belonging to no real person (a co-star or an extra), credited as invented |
| rendition list | fingerprints of every encoding and streaming segment of a work, pressed with the release statement |
| manifest; release manifest | list of the signed statements, with salts, distributed with the video |
| `@name` page | public registry page listing the passkeys bound to a name |
| the check | verification of a video file against its manifest and the log |
| render style | rendering mode of the replica (photorealistic, cartoon, three-dimensional) |
| casting call | per-work solicitation of replica licenses, answered by holders |
| leaving | the actor's signed termination of the operator's distribution of a work |
| gift release | free public release of a work at a date fixed in advance |
| thank; Thank After | voluntary payment or message from a viewer after watching |
| B-Ticket; seat | pre-sold, non-transferable-above-face-value admission to a premiere event |

---

## Author Contributions and AI Disclosure

Thon Ly conceived the mechanism's purpose and its frame: the third kind of video, starring real people's own likenesses; the author who writes a film with AI assistance and posts casting calls to friends, family and the public; the actor who signs permission for their likeness to be used in one film; the cast sharing what a film earns; the name; the observation that a likeness may be rendered in any style; the pre-sold premiere seat, first conceived years earlier as his final project for a blockchain certification; and the question of who pays to serve a film. He ruled on every design choice recorded here, including the choice to fix shares before generation, to split thanks from the first dollar, to release films as gifts, to refuse tokens for seats, to keep advertising out of viewing, and to lift a sequencing gate so that this tool may open to every user. Miss Aquarius℠, the name under which this corpus discloses its AI collaboration, proposed the two-press structure, the fingerprint computed on the actor's device and its checker, the encrypted likeness released one work at a time, the salted log with the manifest carried by the film, the treatment of declines and recuts, the variants and the census predictions; ran the census through a research agent and re-read the decisive sources before they entered this text, marking what it could not read; ran the adversarial pass with a separate reader, re-read the two industry specifications that reader found, and narrowed the claims to what survived it; checked the commentary passage of the Preamble against the Pāli; and drafted this paper. No AI system is an inventor. Thon Ly is the natural person who conceived the invention.

---

## Trademark Notice

**B-Double** is the institution's working name for the service of lending one's own likeness to a film; no mark is claimed in it here, and the mechanism is dedicated to the public domain and may be implemented under any name. **B-Ticket** is likewise a working name. THonly™, B-Sala™, B-Premiere℠, B-Origin℠, HeartBank® and Miss Aquarius℠ are marks of their respective holders. No mark is licensed by this publication.

---

## Citations

1. *Atthasālinī* (Buddhaghosa's commentary on the *Dhammasaṅgaṇī*), *Nidānakathā*, the account of the three months' teaching, Chaṭṭha Saṅgāyana edition, CST text `abh01a.att.xml`, lines 505 and 513 (romanized Pāli, VipassanaTech `tipitaka-xml` at commit 05d5d3c). Translations here are the authors'. Tier: commentary; cited as a recognition, not as authority for the mechanism.
2. The authors' design grammar (internal record cited for its statement, not as external authority): a guard that is a property of the object needs no enforcer; a surface names what is present and never renders an absence; a thank may fund creative work and never repay a cost.
3. Reporting on OpenAI's Sora app and its "cameo" feature, implicator.ai, 30 September 2025 (re-read 2026-11-19). OpenAI's own page refused the fetch (HTTP 403), so the feature is described as reported, not from the vendor.
4. ElevenLabs, "What are voice actor payouts?", help center, elevenlabs.io (undated; re-read 2026-11-19).
5. Digital Trends, "AI dramas need actors, so Chinese platforms are turning human faces into stock assets," 27 July 2026 (re-read 2026-11-19), reporting figures attributed to Rest of World, which was not read.
6. Respeecher, "Actor consent for AI voice in film production," blog, 13 August 2026 (re-read 2026-11-19).
7. Truepic, "Revel.ai" case page, truepic.com/revel (undated; re-read 2026-11-19).
8. Ly, T. and Miss Aquarius (2026). *The Press Travels With the Message*, defensive publication, thonly.org/research/the-press-travels-with-the-message (the passkey press over exact text in a public append-only log; what a press shows and does not show). Proof: Bitcoin block 975913 (2026-11-15).
9. Ly, T. and Miss Aquarius (2026). *B-Links*, defensive publication, thonly.org/research/b-links-signed-provenance (signed provenance for a shared file). Proof: Bitcoin block 959585 (2026-07-25).
10. Ly, T. and Miss Aquarius (2026). *B-PoH Signed Statements, version 1*, open specification, CC0, version 1.4 of 2026-11-19 (§1 and §10, what a statement proves and never proves; §3.4, the agreement pressed by two parties; §3.5, the seat holder's record, reserved).
11. Ly, T. and Miss Aquarius (2026). *The Song That Is Not His*, defensive publication, thonly.org/research/dedicatory-generation (generation where consent is not obtainable). Proof: Bitcoin block 962355 (2026-08-14).
12. U.S. Securities and Exchange Commission, *In the Matter of Stoner Cats 2, LLC*, settled order of 13 September 2023 (an animated series financed by resellable tokens), cited as the reason seats are not tokens (§10.3); as summarized in legal commentary, not read in the original order.
13. Creator Assertions Working Group, *Identity Assertion*, version 1.1, DIF Ratified Specification, 16 May 2025, cawg.io/identity/1.1 (re-read 2026-11-19, the first 100,000 of about 180,000 characters).
14. Creator Assertions Working Group, *Consent Assertion*, version 1.0 draft, 12 July 2026, cawg.io/consent/1.0-draft+initial-version (re-read 2026-11-19).
15. Carlini, N. et al. (2023). "Extracting Training Data from Diffusion Models." *32nd USENIX Security Symposium* (image models emit individual training images, including photographs of identifiable people). Not re-read for this paper.
16. Tuning-free identity-preserving generation from a single reference image: Wang, Q. et al. (2024), *InstantID: Zero-shot Identity-Preserving Generation in Seconds*; Yuan, S. et al. (2024), *Identity-Preserving Text-to-Video Generation by Frequency Decomposition* (ConsisID). Not re-read for this paper.

---

*— End of defensive publication —*
