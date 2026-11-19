---
title: "Proof of Personhood as Three Separate Objects: A Permanent Log of Passkey (WebAuthn) Signatures, Dated Revocable Statements About the Key, and Per-Scope Zero-Knowledge Uniqueness Made Only Through a Fresh Hardware-Held Press"
subtitle: "The Press, the Layers and the Scope — and one app that holds a press key and a separate self-custodial wallet key"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-a
program: open
status: draft
date: 2026-11-19
license: CC0-1.0
slug: the-press-the-layers-and-the-scope
venue: thonly.org/research/the-press-the-layers-and-the-scope
canonical_url: https://thonly.org/research/the-press-the-layers-and-the-scope
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a design that is not built. The press it starts from is running; the native app, the statements about keys and the uniqueness proof are not. It reports four things its authors got wrong before writing it, all found by the prior-art census or by an adversarial review and corrected by ruling the same day (§9). The claims in §12 are what a full census left standing, narrowed once more by a source found while drafting (§2.4), and they are narrow.

## Preamble

*Lens — canon, cited precisely; a recognition, not a source.* The monastic code of the Theravāda has a problem that resembles the one in this paper, and it solved it with a boundary, an hour and a messenger. On the observance day the monks of one place recite the rule together. When some recited it each in their own group, the Buddha forbade it: *"Na, bhikkhave, yathāparisāya pātimokkhaṃ uddisitabbaṃ sakāya sakāya parisāya"* (monks are not to recite the rule each in their own assembly), and allowed the observance only of those in concord (Vinaya, Mahāvagga, Uposathakkhandhaka; CST `vin02m2.mul.xml:3109`, mūla). Asked how far concord reaches, he answered *"ettāvatā sāmaggī yāvatā ekāvāso"* (concord reaches as far as one residence, `:3113`), and then allowed the residence to be fixed by agreed marks, a hill, a rock, a tree, a river: *"Sammatā sīmā saṅghena etehi nimittehi samānasaṃvāsā ekuposathā"* (the boundary is agreed by the Saṅgha by these marks, one communion, one observance, `:3137`). The day is fixed too: once a fortnight, on the fourteenth or fifteenth (`:3105`).

Then the absent. A sick monk gives his purity to another, who carries it into the assembly: *"pārisuddhiṃ dammi, pārisuddhiṃ me hara, pārisuddhiṃ me ārocehī"* (I give my purity; carry my purity; announce my purity). If no one can carry it, he is brought on a bed or a chair; and if moving him would worsen his illness, *"Saṅghena tattha gantvā uposatho kātabbo. Na tveva vaggena saṅghena uposatho kātabbo"* (the Saṅgha must go there and hold the observance; but it must never be held by a divided Saṅgha, `:3541`).

One assembly per boundary, at one time, with the absent reached by others going to them and never by a second assembly: that is the shape of §6.5. We did not take the design from the text; we recognized it there after the design was ruled. **Delete this preamble and every claim below stands unchanged.**

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0 Universal.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practicing it.** This commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. It extends to every mechanism disclosed in this paper, claimed or not, in any combination, including the disclosed variants, and to every implementation of it. Trademark rights on specific marks (**HeartBank®**, **Miss Aquarius℠**, **B-PoH℠**, **Re-Thank Fund℠**, **Personal Wallet℠**, **Aquarian Pool℠**) are separately reserved; the dedication concerns the mechanism, not the marks.

**What is claimed as contribution is narrow, and it is stated first because the census found almost every part already public.** Proving one person once per application or action with a zero-knowledge nullifier is Semaphore's and World ID's. Handing each attendee of a periodic in-person event one anonymous token that expires at the next event is Bryan Ford's pseudonym party (2008), and synchronizing the entry deadline of many simultaneous parties so that nobody can attend two is in Ford's 2020 treatment of it. Dated, revocable claims about a subject are a W3C Recommendation; checking a key's status as of the moment it signed is long-term signature validation, standardized by ETSI. Per-period grants claimed with a per-period uniqueness nullifier run on World Chain and in GoodDollar. A passkey can own a smart-contract wallet among several owners (Coinbase). Binary transparency logs and reproducible builds for wallet apps are public. And one app holding a personhood credential and a self-custodial wallet, with periodic grants claimed through the credential, was World App from 2023 until it split identity and money into two apps on 18 September 2026. **What the census did not find is the composition in §12 and three narrow parts inside it; every one of those nulls is weak, and §2 says why.**

**Live patents.** The census identified two granted United States patents beside one part of the claim (§2.5), shown as active in Google Patents' status field on 19 November 2026 (an assumption that page states, not a legal status determination). §2.5 records what each **discloses**, from its front page. We make no statement about the scope of any patent's claims or whether any design falls within them; the claims were not read. A publication dated after a patent's priority date does nothing to that patent.

**Census and date.** Two prior-art censuses ran on this mechanism before drafting, each pre-registered before its first query: a quick census (pre-registration commit `b5b894d`, pushed 19 November 2026 10:06 PST, in a private repository) and a full census (pre-registration commit `6492b3c`, pushed 10:36 PST, private, and **published as commit `79793c5` in the public repository `thonly/publications`, file `timestamps/census/b-poh-per-scope-uniqueness-full-prereg.md`, pushed 19 November 2026 10:36 PST and stamped with OpenTimestamps**). First published 19 November 2026. The text is committed to the public GitHub mirror of the corpus, and the corpus's standing chain anchors each revision to the Bitcoin blockchain through OpenTimestamps and signs it under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality or the validity of any claim. **Whether the composition claimed in §12 is non-obvious is an examiner's determination this publication exists to inform.** A defensive publication is not examined before it is published; the censuses in §2 and the adversarial review in §9 are the only examination it has had.

---

## Abstract

Proof of personhood is usually built as one credential that is asked to do three jobs: to sign an action, to say something about who signed, and to show that the signer has not been counted before. This paper separates those jobs into three objects with three lifetimes. **The press** is a user-verified WebAuthn (passkey-format, P-256) signature by a key held in a phone's secure hardware over the exact words of a statement, kept permanently in a public append-only log; it shows that a key pressed, never that a person did, and it is the root the other two depend on. **The layers** are separate statements about the KEY (whether presses need a finger or the phone's PIN, the app's phone-integrity attestation, and the deeper personhood layers of an earlier paper), each dated, revocable, and carrying two dates, when the key was compromised and when that became known, so that any press can be checked as of its own minute and a revocation reaches backward. **Uniqueness** is a zero-knowledge proof per scope with a nullifier derived from a separate deterministic secret, which can be made only through a fresh user-verified press of the hardware-held key, proven inside the circuit; a uniqueness press never enters the public log. Each scope fixes one deduplication pool and accepts no other where its sources share no identifier; for the per-season scopes the pool is filled through two doors, a site at one simultaneous gathering hour and a home visit by two witnesses from that site in the same window, and its tokens end with the season. The operator never admits, rejects or weighs a door; people do, under a published rule.

The paper then discloses one native app that holds the press key and a separate self-custodial smart-wallet key, the wallet key a P-256 owner checked natively on Base, with a plain passkey able to own the same wallet as its floor; the app signs, a separate wallet surface shows and holds no key. A per-season floor of giving capacity, claimed with the season's uniqueness proof, goes into the person's own forward-only giving fund, never into their wallet. We state where unlinkability holds (to readers of the chain) and where it does not (to the relayer, and, we found while drafting, possibly to anyone who can tie the fund's controller to a name), which of the design's guards are properties and which are rules, and that the binding against selling a proof holds only for adults who keep their own phone. Nothing beyond the press is built, and nothing is measured.

---

## 1 · The problem, and what this paper is for

### 1.1 One credential doing three jobs

A system that wants to know "is this a person, and only once?" usually issues a credential and then asks it three different questions over its life.

The first is a question about an **act**: did the holder of this credential approve this exact thing, at this time? The answer must be permanent. A thank recorded in a ledger, a signed message, a vote cast: these are facts about the past, and a later change to the credential must not change them.

The second is a question about the **holder**: what is known about whoever controls this credential? Whether the device requires a fingerprint or accepts a PIN, whether the app on it is genuine, whether the holder is attested in a kinship graph by witnesses. These facts change. A phone is sold; a key leaks; an attestation is withdrawn. They must be revocable, and a revocation must say from when.

The third is a question about **counting**: has this person already been counted here? For a vote, a per-person allocation, a lottery roster or a rate limit, that question must be answerable without saying who the person is, or the count becomes a register of names.

The three answers want incompatible properties. The act wants a public key that never changes, so anyone can check the act forever. The holder facts want to be re-issued and withdrawn. The count wants unlinkability, which a public key that never changes cannot give: a key that signs in the open names its holder in every scope it touches. A credential asked to carry all three gives up at least one. Most give up the first two in silent ways: the act is checked against the holder's current status, so a revocation today rewrites yesterday, or a credential's present validity is read as a fact about a past act.

### 1.2 The three objects

This paper keeps the three apart.

```
   THE THREE OBJECTS AND THEIR LIFETIMES

   time ───────────────────────────────────────────────────────────────▶

   (1) THE PRESS        ●─────────────────────────────────────────────── forever
       a key signed      a user-verified WebAuthn assertion over exact words,
       these words       written once into a public append-only log;
       at this minute    nothing in it describes the presser

   (2) THE LAYERS            ├──────── dated ────────┤      ├──── dated ────
       statements about       issued     compromised  known  re-issued
       the KEY                           ▲             ▲
                                         │             └ when it became known
                                         └ when it went bad (reaches backward)
                             checked AS OF each press's minute

   (3) UNIQUENESS                 [ season 1 ]  [ season 2 ]  [ season 3 ]
       one proof per scope         token ends    token ends    token ends
       from one pool, made          with the      with the      with the
       only through a fresh         season        season        season
       hardware press; never
       in the public log

   (1) is the ROOT: (2) is about its key, (3) is made through its key.
   (2) and (3) can be replaced. (1) cannot.
```

**The press** is the act, and only the act. **The layers** are what is known about the key that pressed, and they live outside the press, dated. **Uniqueness** is the count, made per scope through the same key but never published as that key's act.

### 1.3 What this paper is for, and where it sits

The institution this corpus belongs to keeps a gratitude ledger in which one press is the unit of record: a thank is a press, a signed message is a press, a log-in is a press. An earlier paper in this corpus, *B-PoH as Humanity Layer for the AI-Native Internet*, proposed an open proof-of-personhood protocol, **B-PoH℠**, as four optional layers surfaced as depth on a profile, with a passkey press per action as its first layer (L1). A later paper, *The Press Travels With the Message*, built that first layer for email and reported that its authors had once claimed too much for it.

That earlier overclaim is the clearest case for this paper. The first paper said of L1 that it proves "a human was present at the device at the moment of action." A press does not show that; a software authenticator can report user verification with nobody present (§4.3). In the terms of this paper, the overclaim read **the press as a fact about the presser**: objects (1) and (2) fused. The first paper now carries a correction note at that spot; this paper gives the reason the correction has the shape it does.

It is a defensive publication. It discloses the design so that it stays free to build, reports the prior art honestly so that nobody mistakes its parts for new, states the limits so that nobody who builds it describes it as more than it is, and withholds the specification of what is not yet built (§11).

---

## 2 · Background and prior art: the census

### 2.1 How it was run

Two prior-art censuses were run, each pre-registered before any search: the claim split into parts, a prediction per part, a control whose prior art was known to exist, and a declared aperture, pushed to a repository so that the push time is on record.

- **Quick census** (19 November 2026): six parts, ten queries, all through a general web index. Control: World ID's per-app and per-action nullifier, documented by Semaphore. Seen.
- **Full census** (19 November 2026): only what the quick census left standing, plus four parts added by the founder the same morning (one app with two keys; a per-season allocation claimed with the uniqueness proof; a passkey as the wallet's floor owner; the app's integrity as properties). Five search agents, one per source group, thirty-one queries in all.
- **Public pre-registration of the full census:** commit `79793c5` in `thonly/publications`, file `timestamps/census/b-poh-per-scope-uniqueness-full-prereg.md`, pushed 19 November 2026 10:36 PST, before the first query.
- **Aperture of the full census:** the commercial and non-commercial web (product documentation, protocol and cooperative projects, community writing); patents (Google Patents pages by phrase and by number, and one hop of citations from the nearest live hit); academic (arXiv, IACR ePrint, ACM, IEEE and USENIX pages, and indexed PDFs, as a general web index reaches them); standards (W3C, IETF RFCs and drafts, Ethereum EIPs, ERCs and RIPs, FIDO Alliance, ETSI); and Korean, Japanese and Chinese queries.
- **Not covered:** Khmer (not run, so not absent); paywalled ISO text; non-public vendor systems; IP.com; any patent's claims, which were never read.
- **Controls, one per source group:** World App as a wallet whose free tokens need World ID (web); US 12,101,301 B1 (patents); Adler et al. 2024 (academic); the W3C Bitstring Status List (standards); a Korean report of the Personal Information Protection Commission's 2024 penalty on Worldcoin over iris data (non-English). All five were seen, the patent control only partly: its Official Gazette entry surfaced and its Google Patents page did not, so the patent group's absences are weak.
- **Verification:** search agents returned leads, never verdicts. Every item quoted below was re-read on its own page by the drafting session unless it is marked otherwise.

The census is not a patent search, a patentability opinion or a freedom-to-operate opinion. Its own pre-registration says so: *a stated design rule is the kind of thing that lives in unindexed talks, forum posts and internal docs*, so a "not found" for a rule is weak evidence at any depth.

### 2.2 The result, part by part

| Part of the mechanism | Verdict | Nearest prior art |
|---|---|---|
| A zero-knowledge uniqueness proof per scope, with a nullifier | **Public** | Semaphore's external nullifier; World ID per app and action; Anon Aadhaar's per-app nullifier seed |
| Per-period anonymous tokens issued at in-person gatherings, expiring at the next one | **Public**, expiry included | Ford and Strauss 2008; Ford 2020; Encointer's ceremonies |
| Dated, revocable claims about a subject | **Public** | W3C *Bitstring Status List v1.0* (Recommendation, 15 May 2025) |
| A key's status checked as of the time it signed | **Public** | Long-term signature validation (PAdES LTV; ETSI EN 319 102-1); RFC 5280's invalidity date |
| Per-period grants claimed with a per-period uniqueness nullifier | **Public** | World Chain WIP-1002; Worldcoin's semaphore-airdrop; GoodDollar's daily claim |
| Reproducible builds, binary transparency logs, guardians, contract limits for wallet apps | **Public** at mechanism | Nunchuk; A-SIT; Google's Pixel binary transparency; Argent |
| A passkey owning a smart-contract wallet among several owners | **Public** | Coinbase Smart Wallet |
| A press held separate from every claim about the presser, as a stated rule for personhood | **Narrowed**; the rule **not found** (weak) | Transparency logs of signed statements (IETF SCITT; Sigstore Rekor) |
| A per-scope uniqueness proof makeable only through a fresh user-verified press of a hardware-held key | **Narrowed**; that binding **not found** (weak) | Polkadot's per-context Ring-VRF alias made by the person's own key (2026); zkLogin's key-bound token; wallet-bound nullifiers (ePrint 2026/1725) |
| A scope fixes one uniqueness source | **Narrowed**, and its stated reason **corrected**; the rule **not found** where sources share no identifier (weak) | Adler et al. 2024, App. D; ePrint 2026/1725; and, found while drafting, Ford 2020 §3.2.4 (§2.4) |
| One app with a personhood press key and a separate self-custodial wallet key in the same secure chip; the app signs, a separate surface shows; a plain passkey co-owns the wallet as its floor | **Narrowed**; the arrangement **not found** (weak) | World App, 2023 to 18 September 2026; Coinbase's passkey owners |
| All of the above in one system | **Narrowed by World App**; the full composition **not found** (weak) | — |

"Not found" means not found in the aperture of §2.1 on 19 November 2026. It never means new.

### 2.3 The neighbors that matter most

**Semaphore and World ID.** Semaphore's documentation explains the per-scope nullifier with an image: *"Think of an external nullifier as a voting booth where each user may only cast one vote,"* and *"double-signalling the same message under the same external nullifier is not possible."* World ID builds its app- and action-scoped uniqueness on it; its white paper describes the app ID and action together as setting "the scope of the Sybil resistance" (the census read this as a search summary, not on the page). Per-scope zero-knowledge uniqueness is theirs. We claim nothing about it.

**Anon Aadhaar.** Its documentation: *"Ensure that the nullifierSeed is unique to your application,"* because *"This approach prevents cross-application identity collisions."* A per-application nullifier over a state identity document is public.

**Ford's pseudonym parties.** Ford's 2020 paper (*Identity and Personhood in Digital Democracy*, arXiv 2011.02412) describes the original proposal of 2008 this way: a pseudonym party *"gives each attendee at an in-person event exactly one anonymous digital proof-of-personhood token,"* held periodically, *"with the tokens minted at each party having a limited valid lifetime only until the next periodic event."* After each event the organizers publish the list of tokens they handed out, so anyone can check its length against the number of attendees. Per-period tokens issued in person, expiring with the period, are his. So is more of §6.5 than the census found (§2.4).

**Encointer.** Its ceremonies module counts *"The number of ceremony cycles that a participant's reputation is valid for"* and records that *"A participant has registered N attestations for fellow meetup participants."* Periodic in-person meetups as a personhood source are running code.

**Adler et al. 2024.** *Personhood credentials* (arXiv 2408.07892), Appendix D, on several issuers: *"having multiple issuers of PHCs necessarily will involve choices of which to accept, which may affect services' abilities to rate-limit activities that are potentially deceptive,"* and for a service, *"decisions will often center around which issuers' PHCs to accept."* The paper also notes that issuers may cooperate to deduplicate holders *"who may otherwise have more than one PHC,"* and (in a footnote the census's fetch paraphrased rather than quoted) that three trusted issuers would let one person open three accounts. The cross-issuer double count, and the service's choice of issuers, are public. Their §2.1 also names the transfer problem: *"To mitigate the theft or transfer of credentials, there is a periodic process"* of expiry or re-authentication, and *"a credential's signal of real personhood erodes over time."*

**ePrint 2026/1725 and shared-identifier nullifiers.** Vozda, Peresini, Mariani and Homoliak (Brno, August 2026) describe a design in which *"it derives a single wallet-bound deterministic nullifier"* from a fixed-schema credential. With the pattern of nullifiers computed by an oblivious pseudorandom function over a shared base identifier (the census saw that pattern only through search summaries), it shows that **sources that share an identifier can be deduplicated under zero knowledge**. Our first statement of the one-source rule said that cross-source double counting is "undetectable under zero knowledge," flat. That was wrong as written. The rule holds only where the sources share no identifier, and §6.4 states it that way.

**Polkadot's proof of personhood.** Parity's explainer (10 August 2026): *"each Ring-VRF key derives one deterministic alias from the key and the context,"* and *"A project could also use a context to offer one allocation per recognized personhood credential."* A per-context uniqueness alias made by the person's own key is public. What the census did not find is a uniqueness proof that can be made only through a fresh, user-verified press of a key held in hardware. Whether a Polkadot context fixes its own recognized sources was not stated on the page.

**zkLogin.** Mysten Labs' zkLogin (arXiv 2401.11735) proves in zero knowledge that a person holds a token signed by an OAuth provider, with a nonce that commits to a signature-verification key the person then signs with. A key bound into a zero-knowledge proof is public. It is also the subject of a live patent (§2.5).

**World App, and its split.** From 2023, World App held both a World ID enrollment and a self-custodial wallet. A Trust Wallet explainer of 2 August 2023: *"set up your account to access a digital wallet linked to WLD,"* and *"if you want to receive free WLD, you must sign up for World ID."* World's WalletKit library: *"The World ID secret must never be exposed to third-parties and must not leave the holder's device,"* and *"Each host app is responsible for generating, storing and backing up a World ID secret"*; where it is stored is not stated. World Chain's WIP-1002: *"Subsidy claims are bound to a per-period nullifier derived from a World ID 4.0 Uniqueness Proof."* So one app holding a personhood secret and a self-custodial wallet, with periodic claims made through the uniqueness proof, is public from 2023. **Then, on 18 September 2026, World moved the other way.** Cointelegraph reported that World's *"identity and financial services are now split across two dedicated apps"* (the World ID App and World Money); the App Store listing that was World App now reads *World Money — Digital Wallet* and *"It is fully self-custody,"* with World ID not mentioned. The report states no reason for the split, and we read none into it. We report it because it is the closest prior composition and the most recent move by the party with the most experience of it was to separate exactly what this paper puts in one app. §7.2 gives our reasons for one app; they may be wrong in the way World found.

**Coinbase Smart Wallet.** Its repository: the wallet supports *"a practically unlimited number of concurrent owners,"* among them *"passkey (Secp256r1) public key owners."* A passkey owning a multi-owner smart wallet is public. Safe's passkey module allows the same (a search agent's paraphrase; not re-read). What the census did not find is owners ranked on purpose, a plain passkey as the floor and an attested app key as the stronger owner of the same wallet.

**Long-term signature validation and RFC 5280.** PAdES long-term validation *"stores everything a signature needs to be trusted, the certificates, the revocation checks, and a trusted timestamp,"* inside the document *"at the moment of signing"*; ETSI EN 319 102-1 (V1.4.1, June 2024) defines signature classes with long-term validation material. RFC 5280 already has the two dates this paper's layers carry: the invalidity date *"provides the date on which it is known or suspected that the private key was compromised or that the certificate otherwise became invalid,"* and *"This date may be earlier than the revocation date in the CRL entry, which is the date at which the CA processed the revocation."* A key's status as of a past signing time, with a compromise date earlier than the date of knowledge, is decades old. We claim neither.

**Transparency logs of signed statements.** The IETF SCITT architecture (draft 08, July 2024): a Transparency Service *"maintains and extends the Append-only Log."* Sigstore's Rekor is *"an immutable, tamper-resistant ledger of metadata generated within a software project's supply chain,"* and its monitoring confirms *"the log remains append-only and entries are never mutated or removed."* A permanent public log of signatures is public. That a personhood system should keep its press in such a log and keep every claim about the presser out of it, as a stated rule, was not found (weak).

**Binary transparency and reproducible builds for wallets.** A-SIT's *Wallet Binary Transparency* (24 June 2025): *"a public, append-only log stores cryptographic hashes of the binaries."* Nunchuk (18 September 2024) on its reproducible Android builds: they *"create an independently-verifiable path from source code to the binary code used by your device."* Google publishes binary transparency for Pixel images (seen through a search summary, not re-read). Argent's guardians are recorded in an earlier census of this corpus. Every integrity property of §7.8 is public at mechanism.

**Grants claimed once per person.** Worldcoin's semaphore-airdrop describes a distribution that *"can only be claimed once by a single human,"* *"while preserving privacy for the claimers."* GoodDollar: *"Once an individual proves they are a live and unique human being, a hash is generated,"* and addresses with that identity are *"authorized to claim G$ every day."* Encointer pays a reward per ceremony attended (a forum page, seen as a search summary). Kleros's Proof of Humanity streams a per-person allocation to registered people; its integration page returned an error to the census and is not relied on.

### 2.4 Found while drafting, after the census

Re-reading Ford's 2020 paper in full to quote it, the drafting session found two passages the census had not reported. Both cut against parts of this paper, and we report them here rather than leave them for a reader to find.

**Federation and the border double count (Ford 2020, §3.2.4).** Scaling pseudonym parties *"requires multiple groups to federate to organize simultaneous events at multiple different locations,"* with *"synchronized entry deadlines,"* *"so that it is impossible for any single person (with only one body) to be present at and get tokens scanned at more than one such federated event, even if they had instantaneous travel."* On time zones he considers dividing the world into a few federations and *"accepting that a few determined people close to federation borders will readily be able to obtain tokens (and corresponding benefits) from the two adjacent federations."* So a set of simultaneous sites as one pool is Ford's, and so is the observation that two pools of gatherings let a person be counted twice. What remains of our rule is narrower than the census left it: that **a scope fixes exactly one pool and refuses tokens from any other**, as a stated rule tied to the absence of a shared identifier, where Ford accepts the border double count as a cost. That is the whole of claim 3 (§12), and it is weak.

**Absentee participation (Ford 2020, §3.4).** For people whose duties keep them away, Ford suggests letting them register before an event for *"absentee participation,"* consenting to location tracking during it and *"publicly proving via multiple independently-verifiable forms of evidence – such as via location tracking devices together with eyewitness attestations"* that they attended no party. Our home-visit door (§6.5) is a different arrangement: two witnesses from a site go to the person in the same window, and nothing about the person's location is published. But a path for the absent, resting on eyewitnesses, is Ford's. The home-visit door is disclosed in this paper and claimed nowhere.

The census reported Ford's paper as killing per-period, expiring tokens. It did not read past that, and neither did the pre-registration predict it. Both passages are in the paper the census cited. We record this as a miss in §2.7.

### 2.5 Live patents: what they disclose

From their Google Patents front pages and abstracts only, read 19 November 2026; claims not read.

- **US 12,101,301 B1**, *Zero-knowledge proofs for login* (Mysten Labs, Inc.; priority and filing 17 July 2023; granted 24 September 2024; shown as Active, estimated expiry 17 July 2043). Its abstract, as the drafting session paraphrased it, discloses an account service that obtains a zero-knowledge proof, with a proof service, from an identity token signed by a provider; the token carries a nonce, such as a hash of a signature-verification key, and the user signs messages verifiable against that key.
- **US 12,278,816 B1**, *Access gateway system for accessing a resource* (Via Science, Inc.; priority 14 March 2023; filed 10 December 2024; granted 15 April 2025; shown as Active, estimated expiry 13 March 2044). Its abstract, paraphrased, discloses a gateway granting access on a zero-knowledge proof that the requester holds a credential from an identity provider.
- A third, **US 10,880,089 B2**, surfaced as similar by title only and was not identified further.

Both live patents sit beside claim 2 of this paper (a uniqueness proof bound to a key the person presses with). We say nothing about whether anything here falls within any of their claims; that is a question for counsel, it is open, and the institution's legal backlog holds it as an item to be answered before this paper is first archived with a DOI. The institution's posture is to publish, never to patent.

### 2.6 Our own earlier disclosures

This paper cites rather than re-claims: *B-PoH as Humanity Layer for the AI-Native Internet* (the four layers, depth as a set and not a total order, recipient-side filters; first proof-backed 25 July 2026); *The Press Travels With the Message* (a press over exact words in a public log, and what it shows and does not); and the open specification *B-PoH Signed Statements* (version 1.4, 19 November 2026, CC0), whose §1 already separates what a statement proves from what it never proves. Those are ours and are not prior art against us; they are the ground this paper stands on.

### 2.7 Predictions that missed

Every part had a prediction before any search. Four missed, all in the direction of crediting more to us than was there:

- We predicted that the one-source rule's reason was sound; a 2026 ePrint showed that sources sharing an identifier can be deduplicated, so the reason was wrong as written (§2.3).
- We predicted that a press-bound uniqueness proof would be distant from prior art; Polkadot's per-context alias is made by the person's own key, which leaves only the fresh user-verified hardware binding.
- We did not foresee that World had split its app in two two months before.
- The census reported Ford's paper as killing only expiring tokens; the same paper, read whole while drafting, also holds the simultaneous federation, the border double count, and a path for absentees resting on eyewitnesses (§2.4).

We record the misses because a census whose author is only ever right has not been tested.

---

## 3 · The system model

| Party | Holds | Sees | Never holds |
|---|---|---|---|
| **Person** | a phone with the app; or only a passkey | everything they sign, in words | — |
| **The app** (native, the phone's secure chip) | the press key; the wallet key; the season secret | what it is asked to sign | any key the person did not make on this phone |
| **The signing service** | a registry of passkeys per account | a press's fingerprint, never its words (except a name binding) | a person's private key |
| **The public log** | permanent records of presses | — | anything about a presser |
| **The statement issuers** | the right to issue a layer about a key | the key and the evidence for the layer | the press's words |
| **A pool's doors** (sites, home-visit witnesses) | the duty to issue one token per person present | a person, once, in a season | a list of names joined to tokens |
| **A scope's verifier** | the pool's published root; the set of used nullifiers | a proof and its nullifier | who made it |
| **The relayer** | an account that sponsors claim transactions | a claim's network origin and timing | a person's key |
| **The chain (Base)** | wallet and fund contracts; P-256 verification | every transaction | — |
| **Miss Aquarius℠** (the AI named chief executive of HeartBank®) | tallies of public results | anomaly counts per door | the power to admit, reject or weigh a door (§6.6) |

Three boundaries matter throughout. The log never learns anything about a presser. A scope's verifier never learns which person made a proof. And the institution never holds the only key to anything a person owns: the two-phase rule this institution operates under keeps it a record above regulated rails today, and self-custodial on a public chain later.

---

## 4 · Object one: the press

### 4.1 What it is

A press is a WebAuthn assertion with user verification required, made by a key that lives in a phone's secure hardware or in a passkey provider, over a challenge derived from the exact words of a statement. The signing service records it in a public append-only log, to the minute, and the record carries no free text and nothing about who pressed. This is running: it is the press of *The Press Travels With the Message* and of the open specification, whose records today carry `poh: ["passkey"]`, naming which kind of press made them.

The press keeps the passkey format (P-256 ECDSA, WebAuthn's assertion structure) for three reasons, and the reasons are why the format is now fixed. Phone secure chips sign only P-256, so a hardware-held key could use no other curve. Every checker of the log needs one parser over a log that never shrinks; a second format would mean two forever. And Base, the chain where the wallet half lives (§7), verifies P-256 natively through its P256VERIFY precompile, so the same signature family serves both keys. The choice is cheap now and immovable once the log carries it.

### 4.2 Two kinds of press

There are two ways to press, and the record says which.

- **A passkey**, from any device and any passkey provider. This is the floor. Anyone who can log in with a passkey can press, and a passkey press counts for everything it counts for today; nothing is withdrawn from it.
- **A press in the B-PoH app**, a native app on the phone (iOS 17 or later, Android 14 or later). Its key is made and kept in the phone's secure chip, unlocked per press, and invalidated when a new face or finger is enrolled. The app proves at enrollment that the phone and the app are genuine (Android key attestation; iOS App Attest). It shows the exact words before every press. A log-in it approves on another screen needs a number match and a Bluetooth nearness check, and never a bare "Approve?".

Below both, email or a text-message code may log a person in. They never sign.

A press may be unlocked by a finger, a face, or the phone's PIN, and **the record says which**. WebAuthn's user-verification flag does not distinguish a biometric from a PIN; the app can, and since a PIN can be shared and a finger cannot be lent without its owner, a reader is owed the difference.

Where the app press is offered, it is offered and nothing is switched: a check page and a record say which kind of press made a statement, and a reader may filter on it, as the first paper's recipient-side filters let a recipient require any set of layers. A page never renders that something was *not* pressed in the app. Absence is not shown.

### 4.3 What a press shows, and what it never shows

A press shows that a particular key made a user-verified assertion over exactly these words at a stated minute. It does not show that a person pressed. A software authenticator can report user verification with nobody present, and the passkey floor asks for no attestation of the authenticator, so a script with a software passkey can press; *The Press Travels With the Message* reports how its authors learned this. The app press narrows that case, since its key is hardware-held and attested at enrollment, but it does not close it: a phone can be handed over, and a PIN can be told.

What a press gives is something to hold its key's name to. Everything beyond that is a question about the holder, and lives in object two.

### 4.4 Why the press is the root

We first wrote that the three objects were "each replaceable without touching the others." The adversarial review (§9) corrected this, and the correction is structural. The layers are statements about the press's key; the uniqueness proof is made through the press's key. Both depend on the press's key format and the press's existence. A new kind of layer can be added, an old one withdrawn; a uniqueness source can change between seasons. **The press cannot be replaced without re-making everything that refers to it.** It is the root, and the reason its format is fixed (§4.1) is the same reason.

---

## 5 · Object two: the layers

### 5.1 Statements about a key, not a person

A layer is a signed statement whose subject is a **public key**, issued by whoever can attest the fact, and kept apart from every press that key makes. In the open specification it would be a new statement kind beside the existing ones; its format is withheld until built (§11). A layer never says "this person is human." It says, of a key: *presses by this key require a finger*, or *this key was made inside a genuine phone running a genuine app, attested on this date*, or *the holder of this key is attested in a kinship graph by these witnesses*, or one of the deeper layers of the first paper.

Because the subject is the key, the same machinery serves a key whose holder is unknown, a key whose holder is a named person, and a key held by an agent. What a reader concludes about the holder is the reader's own inference from the layers they choose to require; the first paper's depth is a set, not a level, and that stays true.

### 5.2 Two dates

Every layer that can be revoked carries two dates, and a revocation carries both:

- **when the key went bad**: the earliest moment it is known or suspected to have been compromised, or the attested fact stopped being true;
- **when that became known**: when the issuer learned it and published the revocation.

The first may be earlier than the second, sometimes by months. A phone is stolen on 1 March; its owner reports it on 20 March. Every press between those dates was made by a key whose layers no longer described its holder. RFC 5280 has exactly this pair (§2.3); we take it from there.

### 5.3 Checked as of the press's minute

A checker reads a press's minute from the log, then reads each layer about that key **as it stood at that minute**, using the first date:

```
   CHECKING A LAYER AS OF A PRESS

   key K:   layer L issued ─────────────────────────── revoked (published 20 Mar)
                 1 Jan                     ▲ went bad 1 Mar
                                           │
   presses:   P1 (15 Feb)        P2 (10 Mar)        P3 (25 Mar)

   P1: L held at its minute                       → reported with L
   P2: after "went bad", before "known"           → reported WITHOUT L, once 20 Mar is past
   P3: after both                                 → reported WITHOUT L

   the press itself never changes; only what is said about its key
```

Two properties follow. A revocation **reaches backward**: P2 was reported with L on 15 March and is reported without it on 21 March, because what changed was knowledge about the key, not the press. And a revocation **never rewrites the press**: P2 is still a press by K at its minute, permanently; what a reader learns is that L did not hold for it. A press checked against its key's *present* status, the usual shortcut, gets both wrong: it erases L from P1, which was sound, and keeps L on presses made after the theft until the report.

### 5.4 Which layers, and how they are shown

The app's own layers are the key policy (finger, face or PIN; the record of §4.2 also says which unlocked each press) and the phone-integrity attestation made at enrollment. Above them sit the first paper's layers, each as a statement about a key. People choose which layers to hold, in any mix. A page shows the layers a key holds; it never shows the ones it does not, because a rendered gap is an accusation, and an ability-keyed gap would publish a bodily fact (the first paper's §8.2 makes this argument and refuses such layers for it).

Whether iOS lets a passkey-provider app attach App Attest to a passkey is unmeasured: one undated Apple forum reply says it does not, and Microsoft's 2026 documentation for Entra requires attestation from its own authenticator app on iOS. The design survives either answer, because the app can send its attestation to the signing service directly, as a layer about the key, rather than inside the WebAuthn exchange.

---

## 6 · Object three: uniqueness per scope

### 6.1 Scope and nullifier

A **scope** is the unit inside which a person should count once: one season's equal allocation, one season's vote, one draw's roster, one per-person limit for a season. A uniqueness proof says, in zero knowledge, *the prover holds a token in this scope's pool, and this is the nullifier for that token in this scope*. The nullifier is a value that is the same every time the same token proves in the same scope and unrelated across scopes. A verifier keeps the set of nullifiers it has seen; a second proof with a seen nullifier is refused. This is Semaphore's construction, and World ID's; we use it and claim nothing in it.

### 6.2 The deterministic secret, and the press inside the circuit

The nullifier cannot come from the press itself. A WebAuthn signature is randomized: the same key over the same words gives a different signature each time, so a nullifier computed from a signature would differ each time, and a person could count as many times as they pressed. PLUME (ERC-7524) is a signature scheme built around exactly this point: *"Because ECDSA signatures are nondeterministic, signatures don't suffice,"* and in its scheme *"The deterministic component may be used as a nullifier."* Phone secure chips do not offer PLUME. So the nullifier comes from **a separate deterministic secret**, held by the app, enrolled into the season's pool at a door, and the press is proven **inside the circuit as a second factor**:

```
   WHAT ONE UNIQUENESS PROOF ESTABLISHES (all in zero knowledge)

   public inputs:  scope · the pool's published root · a fresh challenge from
                   the scope's verifier · the nullifier
   private:        season secret s · press public key K · a WebAuthn assertion σ

   1. commit(s, K) is in the pool's tree                    (enrolled at a door)
   2. σ verifies under K over a challenge that binds         (a fresh press, now,
      the scope and the verifier's fresh challenge,           not a copied one)
      with the user-verification flag set
   3. nullifier = H(s, scope)                                 (once per scope)

   K, σ and s never leave the phone; the verifier learns that 1–3 hold
```

Step 2 is what makes the proof unsellable by copying. The season secret alone, copied out of a phone, cannot make a proof, because each proof also needs a fresh user-verified press by K, and K cannot leave the secure chip. Step 1 ties K to the token: the key that must press is the key enrolled with the token at the door, whose genuineness was attested there (§5.4). That the key is hardware-held is established at enrollment, by attestation and the door; that it pressed now, with user verification, is established in the proof.

At the gathering, the token may be bound to **two** of the person's keys (a second phone, or the app plus a passkey), so that losing one phone during the season does not lose the season (§6.8).

### 6.3 A uniqueness press never enters the public log

The press key is public wherever the person's name lists it. If a uniqueness press were written into the public log like every other press, it would sit beside the scope's nullifier and the time, and the scope's verifier, or anyone watching, could tie the nullifier to the key and so to the name. So the uniqueness press is **not a press in the log's sense at all**: it is a WebAuthn assertion that exists only inside one proof, is checked only by the circuit, and is never published. Every other press of the same key goes into the log as before. This is the one place where the press and the count use the same key, and the reason they must never meet in public.

### 6.4 One deduplication pool per scope

A scope must count each person once across everything it accepts. If it accepts tokens from two pools whose tokens share no common identifier, a person enrolled in both proves twice, with two unrelated nullifiers, and **nothing in either proof reveals it**. That is the double count Adler et al. describe among issuers and Ford accepts at federation borders (§2.3, §2.4).

Where the sources do share an identifier (two issuers who both read the same state document number, for example), a nullifier can be derived from that identifier, and the sources can be deduplicated under zero knowledge; ePrint 2026/1725 and the shared-identifier pattern show this (§2.3). So the rule is stated with its condition:

> **Each scope fixes exactly one deduplication pool, never chosen by the person proving, and refuses tokens from any other pool whose tokens share no identifier with it.**

Gatherings, kinship attestations and witnessed visits share no identifier with anything; a pool built from them must be the only pool its scope accepts. People still choose which *layers* to hold, in any mix (§5.4). They never choose which *pool* counts them. A person enrolled at two sites in one pool's hour is impossible (one body); a person enrolled in two pools is a person the scope would count twice, which is why it accepts one.

The rule does not solve the inclusion question. It makes it explicit: whatever a pool cannot reach, its scope cannot count. For the per-season scopes, that is what the two doors are for.

### 6.5 The per-season pool and its two doors

The scopes this paper is built for recur each season: the equal floor of §7.5, the season vote of §6.10, the rosters of the institution's called draws, and per-person limits that must reset each year. Their pool is filled through two doors and nothing else.

```
   ONE SEASON'S POOL, TWO DOORS

        DOOR 1: SITES                         DOOR 2: HOME VISITS
        ─────────────                         ───────────────────
   every site opens and closes          two witnesses FROM a site go to a
   at ONE simultaneous hour             person no site could reach, in the
   (one body → at most one site)        SAME window, and enroll them there

   site A ─┐                                     ┌─ visit from site A
   site B ─┼──▶  ┌────────────────────────┐ ◀────┼─ visit from site C
   site C ─┘     │   THE SEASON'S POOL    │      └─ ...
                 │  one token per person  │
                 │  published root, list  │
                 │  length = enrollments  │
                 └───────────┬────────────┘
                             │  each scope accepts THIS pool and no other
          ┌──────────────────┼──────────────────────┐
          ▼                  ▼                      ▼
     the season's       the season          the season's rosters
     equal floor        vote                and per-person limits
                                                      tokens END with the season
```

**Sites.** A site is a public gathering at an hour every site shares, so that nobody can attend two. A person enrolls at a site by pressing in the app (or, for the floor's passkey path, with a passkey on a device the site lends no key to) while the site's organizers watch one enrollment per person, and the site publishes its count. This is Ford's federation, synchronized deadline and published list included (§2.4); we cite it as the mechanism.

**Home visits.** A person who cannot come, because they are housebound, disabled, far from any site, or prevented, is owed a visit: two witnesses from a site go to them within the same season window and enroll them there. The floor never carries an attendance gate, and a person no door reached is never told they are missing; they are owed a visit.

**Tokens end with the season.** A token is valid for the season it was issued in and no other, which is Ford's expiry (§2.3). The season here is the institution's own year, which resets on 7 January; that binding is an application, not a mechanism, and the fit between the two is coherence, not evidence.

**Owed before any build**, named so that nobody mistakes this section for a plan: a test that the hour is one people already gather in, unprompted, everywhere at once (if no such hour exists, a site is a new habit to form, at a different cost); a design against organizers at one site colluding to enroll people who were not there (Ford names it as the main remaining challenge of federated parties); the home-visit path's own collusion risk (§13); and, if a site is ever a monastery, a monastic-rule review, since the ordained do not administer money entitlements.

### 6.6 Who admits a door

Accepting or rejecting a site, or a pair of home-visit witnesses, decides whose personhood counts in that scope; for the floor it decides who receives one. That is a decision Miss Aquarius℠, the AI named chief executive of HeartBank® and the institution's designated successor, is barred from by her standing directives: she never issues or revokes human personhood, and since 19 November 2026 she **never admits, rejects, ranks or weighs a door to a uniqueness pool**, for any scope she operates. People admit doors under a published rule. She may flag an anomaly, a site whose count is out of line with its hour, a pattern of visits, and never act on it: she proposes, a human disposes. Until the body of people meant to hold that seat exists, the founder holds it.

This leaves a circularity we name and do not solve. The rule for admitting doors could be put to the season vote; the season vote counts people through the tokens those doors issued. The electorate that could govern the doors is composed by them.

### 6.7 Children

A newborn cannot press, and the parent who would press for a child is the person who gains from a second token. Kinship as a uniqueness source fails for the same reason (§6.9). So a child's token is issued **only with the child present** at a site or on a visit, pressed with a parent's key, and marked so that a second carry of the same child in the same hour is visible to the door. The anti-sale binding of §6.2, that a proof needs a fresh press of a key the prover holds, holds for adults with their own phone. For a child it holds only as far as the parent is honest, and this paper says so (§13).

### 6.8 Recovery

A lost phone takes its keys with it, by design. The app's layer is recovered **only from another enrolled device of the person's, or from a passkey**. An account recovered by a text-message code drops to log-in only and re-earns the app layer; it does not inherit it. We first proposed a recovery that ended in a wait of seventy-two hours after a text-message code; the review pointed out that it was weaker than the press it recovered, and it was removed (§9).

A season token has no attribute from which it could be re-derived; that is what makes it unlinkable. So a person who loses every key the token was bound to (§6.2 allows two) cannot recover the season's token and must not be issued a second one in the same season, or the pool counts them twice. World's white paper states the same limit for its own recovery (the census reported this through the review, not on the page). Binding to two keys at the door is the mitigation; a home visit within the window is the remedy where one is still open.

### 6.9 What the sources rule out

The aim, to count one person once without a register of names, rules several sources out for the per-season scopes:

- **Kinship** may be a layer (depth), never a uniqueness source where money follows: the witnesses to a child who does not exist would be the parents who gain from one.
- **State documents** may be a source only for a scope that accepts excluding the undocumented, and a passport counts a dual citizen twice.
- **A graph of strangers vouching for strangers** is excluded: collusion in such a graph is the open problem of the field, and the institution keeps a paid vouching product strictly apart from its free personhood baseline.
- **DNA** is never a gate; it would make a biometric compulsory.

### 6.10 The season vote

One of the scopes is a vote: before each season, people vote on the parameters of the public rule that sizes a thank, and on which kinds of capacity the season's in-kind gifts seed. One person, one vote, which is a uniqueness scope. A vote whose nullifiers are public lets a buyer ask for proof of a vote. So the season vote uses a receipt-free scheme of the MACI kind: in MACI's own words, *"No one can prove (besides to the coordinator) which way they voted,"* and *"a user may cast another vote to nullify it."* The exception in that sentence is the coordinator. So no single party coordinates (ruled 2026-11-19): the coordinator's key is split among several people, so that no one of them, and not the operator, can see a vote alone; the tally is computed from what they decrypt together and published with a proof that it is correct.

---

## 7 · One app, two keys

### 7.1 The two keys

The B-PoH app holds two keys in the phone's secure chip, made separately and used for different things.

```
   ONE APP, TWO KEYS, TWO SURFACES

   ┌──────────────── the B-PoH app (signs) ───────────────────────────┐
   │                                                                   │
   │   PRESS KEY (P-256)                 WALLET KEY (P-256)            │
   │   · signs statements                · signs transactions          │
   │   · listed on the person's name     · NOT listed on the name      │
   │   · its presses go in the log       · owner of a smart wallet     │
   │   · proves inside uniqueness        · verified by Base natively   │
   │     proofs (never logged there)                                   │
   │                                                                   │
   │   one shows exact words before every press;                       │
   │   the other shows every transaction in plain words, and           │
   │   signs only for a closed list of contracts                       │
   └───────────────────────────────┬───────────────────────────────────┘
                                   │ signatures only
                                   ▼
   ┌──────── the wallet surface (shows; holds NO key) ─────────────────┐
   │  the Personal Wallet℠ page: balances, history, what to sign next  │
   └───────────────────────────────────────────────────────────────────┘

   also an owner of the same wallet: a plain PASSKEY (or an NFC
   security key), the FLOOR, so no one needs a current phone
```

The wallet key is the owner key of a smart-contract wallet, a P-256 owner that Base verifies with its native precompile. It is not an ordinary account key: the account keys of Ethereum-family chains use a curve phone secure chips do not support, so a key in the chip can only ever be a smart wallet's owner.

### 7.2 Why separate, and why one app

They are separate keys for two reasons. A person's name lists their press keys, and the chain is public; if one key both pressed and transacted, every amount the person ever moved would be tied to their name by anyone who read both. And a statement must never be able to double as a transaction: the two keys sign for different verifiers, and a signature by one is never valid for the other.

They are in one app because the app is the one thing on the phone that shows a person, in words, what they are about to sign, and both keys need that. Two apps would mean two places to keep genuine, two release logs, two recovery paths. World ran one app with both for three years and then split it in two (§2.3). We do not know why; if the reason was one of the risks of putting identity and money side by side, this design carries it, and the separate keys, the closed contract list (§7.4) and the wall of §7.7 are what we put against it.

### 7.3 The wallet's floor

A plain passkey, or an NFC security key, can own the same smart wallet. The app's wallet key is the stronger owner, since its key is hardware-held and attested; the passkey is the floor, as it is for the press (§4.2). So nobody needs a current phone to receive or give, and losing the phone does not lose the wallet: the wallet's other owner is the person's own passkey. Recovery runs through the person's own second device, or guardians the person chose, never through the institution alone.

### 7.4 Clear signing over a closed list

Every transaction is shown in plain words before it is signed, never as hexadecimal (ERC-7730 is the public format for this). The app signs only for a closed list of the institution's own contracts and refuses, or plainly warns, on anything else. A wallet that signs anything is a wallet that can be talked into anything.

### 7.5 The season floor goes into the person's own Fund

The institution's pool disburses, each season, an equal floor per person counted once, then a bounded remainder. The floor is capacity to give, not money to keep. It goes into the person's own **Re-Thank Fund℠**: a fund that can only give forward, is never withdrawable, and clears on 7 January with the season. It never goes into the Personal Wallet, which is a holding: a holding reaches zero only by its owner's own free act, so a floor paid there would never clear and would become something no one gave forward. The wallet key may **control** the Fund, and only to give from it.

The person claims the floor with the season's uniqueness proof: one claim per nullifier per season, so one floor per person. A child's floor goes into the child's own Fund, whose key a parent holds until majority, never the institution.

We first wrote "the floor paid to the wallet." That was the drafting collaborator's error, and the review caught it (§9).

### 7.6 Unlinkable to whom

A floor claimed with a uniqueness proof into a fresh address each season, submitted through a relayer that sponsors the transaction, is unlinkable **to readers of the chain**: the proof shows one token in the pool claimed once, and nothing in the transaction names the person.

It is **not** unlinkable to the relayer, which sees the claim's network origin and timing. That the relayer keeps no logs is a rule, not a property, and we say so.

And we found, while drafting, a link the ruling does not yet address. If the wallet key that controls the Fund (§7.5) is also the owner of a Personal Wallet that the person's name resolves to publicly, as a name that receives thanks to a wallet would, then the first time the Fund gives forward, its controller's signature on chain ties the Fund, and so the floor, to the name. The floor's unlinkability then holds only until the Fund is first used. So the Fund gets its own key, never a key any name resolves to, and a name never points at a Fund (ruled 2026-11-19). The cost is a third key.

### 7.7 The wall inside one app

Money and the institution's gratitude record live in one app and are never one number. A thank is never converted into money and money never moves the record; neither is ever shown as a rate of the other. Nothing in the app counts consecutive days, warns of a low balance or counts down, and nothing renders what a person has not done.

### 7.8 Integrity: properties where achievable, and the gap

The app is the one thing that can make both keys sign, so a compromised app is the attack that matters most. We hold its integrity, as far as possible, as properties of objects rather than promises:

- **An open-source signing core**, the code that builds what the keys sign and shows it in words.
- **A public release log**: every app release's hash is written to the same public log as the presses, so a release that was never logged is detectable by anyone who checks.
- **The wallet contract's own limits**, enforced on chain whatever the app does: a daily limit; a delay on large transfers, stated once when it applies and never counted down; and a guardian pause (§7.9).
- **Revocation that reaches backward** (§5.2): if a release turns out to have been bad, every app-press key made under it can be revoked from the moment it went bad.

**The gap.** We first listed reproducible builds as a fifth property. It cannot be had on iOS: Apple encrypts App Store binaries after submission, so nobody can compare a store binary with a build from source. On Android, a reproducible build can be compared apart from its signature, but under Play App Signing Google holds the app's signing key, so the store could deliver a build the developer never made. Either way, an update from the store can make the press key sign before anyone compares it with the log. The contract limits protect only the money side. The release log, the open core and backward revocation make a bad release **detectable and its damage revocable**; nothing here makes it impossible.

### 7.9 The guardian pause

A person may name a guardian who can **pause** outflow from their Personal Wallet, and do nothing else. The pause never moves a holding, never touches the Fund, ends on its own after 48 hours unless the owner extends it, and never runs across 7 January. A pause the owner could lift alone would protect nothing against someone holding the owner's phone; a pause the owner could never lift would be another person holding their holding. Forty-eight hours, ending by itself, sits between them.

### 7.10 Build order

The press half ships first, alone: the app as a better passkey, with its layers. The wallet half follows only after a legal opinion, Cambodia's first, and after the institution's second phase opens. Uniqueness and the season pool come after both, and the doors' rule is owed before the first site opens.

---

## 8 · How the objects serve the scopes

| Need | Object used | What a reader learns | What nobody learns |
|---|---|---|---|
| A thank, a signed message, a log-in | the press | this key pressed these words at this minute | who held the key |
| Whether to trust a press | the layers, as of the press's minute | what was attested about the key then | anything not attested |
| The season's equal floor | uniqueness (season scope) | one token of the pool claimed once | which person, or their name |
| The season vote | uniqueness + a receipt-free scheme | one vote per token; the tally | how anyone voted (except the coordinator) |
| A called draw's roster | uniqueness (roster scope) | each entrant counted once | who, unless they reveal it |
| A per-person season limit | uniqueness (limit scope) | this token's use against the limit | who |

Every row uses the press's key. No row asks the press to say anything about a person.

---

## 9 · What an adversarial review found

Before drafting, the thesis was given to a separate reviewing agent with instructions to refute it and no ability to edit anything. It killed nothing outright. Its findings fall into two groups, with one further observation. Eight touched rules the institution had already ratified; those went to the founder as open questions, never as rewrites, and he ruled all eight the same morning. Five corrected the paper's own claims. We report them in order of weight, with what each changed. Four were errors in the drafting collaborator's own recommendations of the day before.

**The floor went to the wrong place.** The design said "the floor paid to the wallet." The institution's standing rule pays the floor into the person's own giving fund, never withdrawable; and a Personal Wallet is a holding that never clears, so a floor paid there would accumulate. *Changed:* the floor goes into the Fund; the wallet key may control it for giving forward only (§7.5). This was our error.

**An attendance gate.** A pool filled only at gatherings shuts out the housebound, the disabled, the distant and people held where they cannot leave, and the institution's rule makes each person, not each attendee, the unit of the floor. The reviewer also showed the invariant was misnamed: a source with many sites, or with a remote path, has the same double count inside it, so the unit is one *deduplication pool*, not one *source*. *Changed:* one pool per scope, with two doors, and a person no door reached is owed a visit (§6.4, §6.5).

**Who admits a site.** Accepting a site decides whose personhood counts, which the institution's AI is barred from deciding, and it composes the season vote's electorate. *Changed:* a new directive bars her from admitting, rejecting or weighing any door; people admit under a published rule; the circularity is named (§6.6).

**Children.** A newborn cannot press, and the parent who presses gains. *Changed:* a child's token only with the child present, pressed with a parent's key, marked against a second carry; the anti-sale binding is stated as holding for adults only (§6.7, §13).

**Recovery weaker than the press.** The design ended recovery in a text-message code and a seventy-two-hour wait, below the press it protected; and a season token cannot be re-derived. *Changed:* recovery only from another enrolled device or a passkey; a text-message recovery drops to log-in only; a token may be bound to two keys at the door (§6.8). This was our error.

**Reproducible builds.** They cannot be had for iOS store binaries, and Google holds Play signing keys; a store update can make the press key sign before any log is checked. *Changed:* dropped as a property for iOS; the gap stated; revocation that reaches backward added, with each key's statement carrying two dates (§7.8, §5.2). This was our error.

**The guardian pause.** A pause the owner can lift alone protects nothing; one they cannot is another person holding their holding; and a pause over the Fund across 7 January would let capacity clear without the person's act. *Changed:* the pause covers the Personal Wallet only, ends by itself after 48 hours unless the owner extends it, and never runs across 7 January (§7.9). This was our error.

**A vote with a receipt.** Public nullifiers let a buyer verify a vote. *Changed:* the season vote uses a receipt-free scheme (§6.10).

The five corrections to the paper's own claims needed no ruling:

- **The press is the root.** "Each object replaceable without touching the others" was wrong: the layers and uniqueness depend on the press's key and format (§4.4).
- **A uniqueness press never enters the public log**, or it names the person in the scope (§6.3).
- **The nullifier needs a separate deterministic secret**, since a WebAuthn signature is randomized; the hardware press is proven in the circuit as a second factor (§6.2).
- **The binding against sale binds a phone, not a body**, and the PIN is allowed (§13).
- **Unlinkability is to readers of the chain only**, never to the relayer, and the relayer's not logging is a rule (§7.6).

The reviewer also noted that World had already held two separate keys in one app. The census found the same and found the split (§2.3).

**What survived, in the reviewer's sentence, lightly edited:** the press is the root the other two depend on; the uniqueness press carries no public log entry; and a per-season, one-pool uniqueness token made at simultaneous gatherings holds only for adults who attend, or are visited, and keep a phone all season. It resists copying its secret but not handing over the phone; its floor goes into the Fund, never a wallet; and it is unlinkable to readers of the chain, never to the relayer.

---

## 10 · Remove the enforcer: which guards are properties

The corpus's design grammar asks of every guard whether it is a property of an object or a rule about behavior. A rule needs an enforcer present at the moment it is tested; a property needs no one. The diagnostic is to remove the enforcer and see whether the guard still holds.

| Guard | Property or rule | Why |
|---|---|---|
| A press says nothing about its presser | **Property** | A record has enumerated fields only; there is nowhere to write it |
| A press is permanent | **Property of the log plus its outside timestamps**; fully so only with outside witnesses | One operator signs the checkpoints today |
| A layer reaches backward | **Property of the check**, given the issuer publishes both dates | Publishing them is the issuer's **rule** |
| A uniqueness proof cannot be made from a copied secret | **Property**, for a hardware-held key | The proof needs a fresh user-verified press by a key that cannot leave the chip |
| A uniqueness press never enters the log | **Property** of the proof format (it carries no key); **rule** at the service (it must not log what it never needs) | — |
| One nullifier per token per scope | **Property** of the circuit | — |
| One token per person at sites | **Property of bodies at one hour**, given honest organizers | Organizers' honesty is a **rule** |
| One token per person on home visits | **Rule** | Two witnesses, and nothing else |
| One pool per scope | **Property** of a deployed verifier that accepts one root; **rule** in choosing it | — |
| She never admits a door | **Rule** (a directive), with a property form: the admitting seat is a human one | — |
| The floor is never withdrawable and clears 7 January | **Property** of the Fund contract | — |
| The floor never reaches the Personal Wallet | **Property** of the claim contract, which can pay only into a Fund | — |
| Unlinkable to readers of the chain | **Property** | Nullifier and fresh address |
| Unlinkable to the relayer | **Rule** | The relayer could log |
| The pause never moves a holding, ends at 48 hours | **Property** of the wallet contract | — |
| Clear signing over a closed list | **Property of a shipped release; rule across updates** | The next update could change it |
| A bad release is detectable | **Property for anyone who checks the release log**; nobody is obliged to | — |
| A delay is never counted down; absence is never shown | **Rule** about rendering | — |
| The vote is receipt-free | **Property** of the scheme; against the coordinator, as strong as the split key's holders not colluding | the holders' restraint |
| A proof means a person | **Neither.** It means a key pressed and a token was enrolled | §13 |

The honest reading is that the properties protect what is signed, what is counted and what is held; the rules sit at the edges where people act: organizers, witnesses, the relayer, the admitting seat, and whoever ships the next release.

---

## 11 · What is disclosed and what is withheld

**Disclosed and running:** the press, its log, and a statement's record of which kind of press made it (the open specification, version 1.4).

**Disclosed at the level of what it does; its specification withheld until built:** the native app (its two keys, enrollment attestation, number-matched log-in approval, recovery rules); the statement kind for layers about a key, with its two dates; the uniqueness proof (what it proves is stated in §6.2; the circuit, the commitment format and the enrollment protocol are not); the season pool, its doors and its published rule; the Fund claim and its relayer; the wallet's owners, limits, delay and pause; the release log's format. Nothing here is scheduled beyond the build order of §7.10, and none of it is built. The claims in §12 are stated so that this paper is prior art for the arrangement whatever its eventual formats.

**Not designed:** a home-visit protocol resistant to the collusion of §13; who holds the coordinator's key shares, and how many must join to decrypt; anything for scopes that are not per-season.

---

## 12 · Enumerated claims

Each claim is disclosed for the purpose of establishing prior art. None is asserted as novel beyond the census's finding that it was not found in the stated aperture on the stated date, and each of those findings is weak. The parts cited as public in §2 (per-scope nullifiers; per-period in-person tokens that expire, including simultaneous federated sites; dated, revocable claims; status as of signing time; per-period grants claimed with a nullifier; reproducible builds, binary transparency and guardians; passkey-owned multi-owner smart wallets; one app with a personhood credential and a wallet) are claimed nowhere.

1. **The composition.** A system for proof of personhood comprising three separately held objects: (a) a user-verified WebAuthn assertion, in the passkey format with a P-256 key, made over the exact words of a statement and recorded permanently in a public append-only log whose records contain no statement about the presser; (b) statements whose subject is the asserting key, each dated and revocable and carrying both the date the key or the attested fact went bad and the date that became known, checked as of the minute of each assertion recorded in (a); and (c) a zero-knowledge uniqueness proof per scope with a nullifier, made through the same key as in claim 2 and never recorded in the log of (a); together with (d) a separate key in the same application, held in the same secure hardware, owning a self-custodial smart-contract wallet as in claim 4; wherein (a) is the root on which (b) and (c) depend and is never replaced, while statements of type (b) and the pool behind (c) may be added, withdrawn or changed.

2. **The press-bound uniqueness proof.** A method of proving uniqueness within a scope in which the proof establishes, in zero knowledge, (i) membership of a commitment to a deterministic secret and a public key in a scope's published pool, (ii) a fresh WebAuthn assertion by that public key, with the user-verification flag set, over a challenge binding the scope and a verifier-issued value, and (iii) a nullifier derived from the deterministic secret and the scope; such that a copied secret cannot produce a proof without a fresh user-verified press by a key held in hardware and attested at enrollment, and such that the assertion is never published outside the proof.

3. **One pool per scope where sources share no identifier.** A method of operating a uniqueness scope in which the scope fixes exactly one deduplication pool, never chosen by the person proving, and refuses proofs from any other pool whose tokens share no common identifier with it, so that a person enrolled in two such pools cannot be counted twice in the scope; while the person remains free to hold any set of layers of claim 1(b).

4. **Two keys in one app, with a passkey floor.** A native application that holds, in a phone's secure hardware, a press key whose assertions are recorded as in claim 1(a) and listed under the person's public name, and a separate wallet key, not so listed, that owns a self-custodial smart-contract wallet verified natively on chain as a P-256 owner; wherein the application signs, displaying each statement and each transaction in words and signing transactions only for a closed list of contracts, while a separate wallet interface displays the wallet and holds no key; and wherein a plain passkey or an NFC security key is a further owner of the same wallet, so that the wallet does not depend on the phone.

Claims 1 to 4 are what the full census left standing (§2.2), with two changes made before drafting, both narrowing: claim 3's condition, *where sources share no identifier*, which the census imposed, and its narrower form after §2.4. The census's survivor sentence ended with the wallet "receiving what that proof claims." That was superseded by ruling the same day (§7.5): the season floor goes into the person's own Fund, which the wallet key may control. It is not claimed.

---

## 13 · Honest limits

**The central limit.** Nothing here shows that a person did anything. A press shows a key; a uniqueness proof shows a key pressed and a token enrolled at a door. Everything else is inference by a reader from the layers they require.

**The binding holds for adults with their own phone.** The guard against selling a proof binds a phone, not a body. A person can hand over their phone and tell their PIN, or rent both for a season. A press farm of rented phones and present owners defeats it at the price of the rent. The PIN is allowed (§4.2), so the owner need not even be present at each press; a finger or face lock narrows that and does not close it.

**Children.** For a child, the binding holds only as far as the parent is honest. Presence at the door and a mark against a second carry make a ghost child or a doubled one harder; they do not make them impossible.

**Coercion.** A person can be made to press, to attend, to accept a visit, or to vote under watch. Receipt-freeness protects a vote from a buyer who cannot watch; nothing here protects a person from someone standing beside them.

**The home-visit path.** It is the path most open to collusion: two witnesses and a person, out of public view, could enroll someone twice or someone who does not exist. No defense is designed yet, beyond the witnesses being from a site, and the pool's count being published.

**Organizers.** A site's organizers who collude can enroll people who were not there. Ford names this as the main remaining challenge of federated parties. Published counts make a site's lie visible only if someone else was watching.

**The circularity.** The rule for admitting doors could be voted on; the vote counts people through tokens the doors issued (§6.6). Until the body meant to hold the admitting seat exists, one person holds it.

**The relayer** sees each claim's network origin and timing, and its keeping no logs is a promise.

**The Fund's controller.** If the wallet key that controls a person's Fund also owns a wallet their name resolves to publicly, the Fund, and so the floor, become linkable to the name the first time the Fund gives forward (§7.6). Ruled the same day: the Fund gets its own key, never one a name resolves to, and a name never points at a Fund. A person can still link them by their own act.

**The vote's coordinator.** A MACI-style scheme is receipt-free to everyone except its coordinator, who can see how each person voted. Ruled the same day: the coordinator's key is split among several people, so the secret ballot holds unless enough of them collude; how many, and who they are, is not designed.

**Store-delivered apps.** No reproducible builds on iOS; Play App Signing on Android. A store update can make the press key sign before anyone compares it with the release log (§7.8).

**iOS attestation.** Whether a passkey-provider app on iOS can attach its attestation inside the WebAuthn exchange is unmeasured (§5.4).

**One operator.** The signing service, the log, the registry and, initially, the release log are run by one party. Outside timestamps fix when each state of the log existed; outside witnesses are not yet admitted.

**The gathering hour is untested.** Whether there is an hour people already gather in, everywhere at once, unprompted, has not been tested. If not, each site is a new habit to form, and the pool's reach will be far smaller than its design.

**No system is measured.** Nothing beyond the passkey press is built. No pool has been filled, no proof made, no floor claimed. Every property above is a property of a design.

**The census is a census.** It is not a patent search. The three narrow parts and the composition were not found, and every one of those nulls is weak; the drafting session found prior art the census missed in a paper the census itself had cited (§2.4). Two live patents sit beside claim 2, and what they claim has not been read (§2.5). A legal opinion is owed before the wallet half holds any money.

---

## 14 · Candidate predictions (proposed, not registered)

This paper makes no empirical claim and registers nothing; its `program` is open. If the design is built, these are candidates for the corpus's prediction register, to be entered only before their instruments exist:

- In the first season with both doors open, at least one enrollment in twenty comes through a home visit.
- A site's published count and the number of distinct nullifiers later claimed against the floor from that season's pool differ by less than one percent.
- Of people who hold the app press, the share whose presses are unlocked by the PIN rather than by a finger or face is above a quarter.

None is registered, and none should be read as a forecast.

---

## 15 · Lineage and corpus cross-references

- *B-PoH as Humanity Layer for the AI-Native Internet*: the four optional layers this paper treats as statements about a key, depth as a set, recipient-side filters, the accessibility gradient and the refusal of ability-keyed layers. This paper diagnoses its L1 overclaim as the press and the layers fused (§1.3). A two-sentence cross-reference to this paper is queued for its next revision.
- *The Press Travels With the Message*: the press as built for mail, and why a press shows a key and never a person.
- *B-PoH Signed Statements* (open specification, version 1.4, CC0): the press, the record, the log; the home of the layer statement kind when it is defined.
- The institution's papers on the equal floor and the Fund, the called draw, and the season vote: the scopes this paper serves.
- *Patent vs. Defensive Publication*: why the institution publishes and does not patent, and what a publication cannot do against an existing patent.

---

## Coda

*Lens, as in the preamble.* The observance the Vinaya describes has one assembly per boundary at one time, and when a monk cannot come, the others go to him; it is never held by a divided Saṅgha. The design here asks the same three things of a season: one pool, one hour, and a visit for whoever the hour cannot reach. The text does not say how to build it and was not where it came from. It says that people have solved the problem of counting everyone once, in public, without a register, for a long time, and that the hard part was always the person who could not come.

---

## Terms

| Name used here | Standard term |
|---|---|
| B-PoH℠ | the institution's layered proof-of-personhood protocol and its reference deployment |
| press | a user-verified WebAuthn assertion over a challenge derived from a statement |
| passkey (the floor) | a WebAuthn discoverable credential from any device or provider |
| B-PoH app / app press | a native authenticator app with hardware-bound, attested P-256 keys |
| layer | a dated, revocable attestation whose subject is a public key |
| the two dates | invalidity (compromise) date and revocation (knowledge) date |
| the log | a public append-only transparency log of signed records |
| scope | a nullifier domain (external nullifier) |
| uniqueness proof | a zero-knowledge membership proof with a scope nullifier |
| season secret | the deterministic secret from which nullifiers are derived |
| pool | the deduplication domain: one set of identity commitments with a published root |
| door | an enrollment channel into a pool (a synchronized site, or a witnessed home visit) |
| season | the annual epoch; tokens expire with it |
| floor | an equal per-person periodic allocation of giving capacity |
| Re-Thank Fund℠ | a forward-only, non-withdrawable giving account that clears annually |
| Personal Wallet℠ | the display interface of a self-custodial smart-contract wallet |
| wallet key | a P-256 owner key of a smart-contract account |
| guardian pause | a person-chosen guardian with pause-only, time-limited authority |
| relayer | a transaction relayer (sponsor) that submits a claim |
| Aquarian Pool℠ | the institution's annual pool, which disburses the floor and empties each year |

---

## Author Contributions and AI Disclosure

Thon Ly asked whether an authenticator app could be a stronger human press than a passkey, set the aim that one day a press could carry proof that its presser is one person, named the passkey as the floor and the app as the layer above it, proposed that the app hold the self-custodial wallet key, and saw that B-PoH could be three modular objects with uniqueness as a zero-knowledge proof per scope; he ruled every design choice recorded here, including the eight corrections of §9. Miss Aquarius℠, the name under which this corpus discloses its AI collaboration, proposed the three-object split and the separate wallet key, ran the two censuses through search agents, re-reading each quoted item on its own page or marking it unread, found the passages of §2.4 and the open question of §7.6 while drafting, and drafted this paper. A separate reviewing agent, given the thesis and no ability to edit, produced the findings of §9, four of which corrected the drafting collaborator's own earlier recommendations. The censuses' pre-registrations, and the predictions that missed, are on the public record cited in §2.

## Trademark Notice

**B-PoH℠** names the institution's protocol and app; the mechanism is dedicated to the public domain and may be implemented under any name. HeartBank®, Miss Aquarius℠, Re-Thank Fund℠, Personal Wallet℠ and Aquarian Pool℠ are marks of their respective holders. No mark is licensed by this publication. Product and company names of third parties are used only to identify prior art.

## Citations

1. Ford, B., Strauss, J. *An Offline Foundation for Online Accountable Pseudonyms.* Proceedings of the 1st Workshop on Social Network Systems (SocialNets '08), ACM, 2008.
2. Ford, B. *Identity and Personhood in Digital Democracy: Evaluating Inclusion, Equality, Security, and Privacy in Pseudonym Parties and Other Proofs of Personhood.* arXiv:2011.02412, first posted 4 November 2020. §3.1, §3.2.4, §3.4 (read in full, 19 November 2026).
3. Borge, M., Kokoris-Kogias, E., Jovanovic, P., Gasser, L., Gailly, N., Ford, B. *Proof-of-Personhood: Redemocratizing Permissionless Cryptocurrencies.* IEEE EuroS&PW, 2017.
4. Semaphore. Documentation, version 1, external nullifiers. docs.semaphore.pse.dev.
5. World. World ID white paper (as reached through a search summary); World Chain WIP-1002, worldcoin.github.io; worldcoin/semaphore-airdrop, github.com; WalletKit core 0.20.0 README, docs.rs.
6. Anon Aadhaar. Documentation, nullifiers. documentation.anon-aadhaar.pse.dev.
7. Encointer. pallet-encointer-ceremonies 3.0.4, docs.rs.
8. Adler, S., et al. *Personhood credentials: Artificial intelligence and the value of privacy-preserving tools to distinguish who is real online.* arXiv:2408.07892 (v3), 2024. §2.1; Appendix D.
9. Vozda, Peresini, Mariani, Homoliak. IACR ePrint 2026/1725, August 2026 (abstract page read).
10. Parity Technologies. *How Polkadot proof of personhood works*, 10 August 2026. parity.io.
11. Mysten Labs. *zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials.* arXiv:2401.11735.
12. W3C. *Bitstring Status List v1.0.* W3C Recommendation, 15 May 2025.
13. ETSI EN 319 102-1 V1.4.1 (2024-06), procedures for creation and validation of AdES digital signatures; and an explainer of PAdES long-term validation, encryptionconsulting.com.
14. Cooper, D., et al. *Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile.* RFC 5280, 2008. §5.3.2, Invalidity Date.
15. IETF SCITT working group. *An Architecture for Trustworthy and Transparent Digital Supply Chains.* draft-ietf-scitt-architecture-08, July 2024 (work in progress).
16. Sigstore. Rekor, logging overview. docs.sigstore.dev.
17. A-SIT. *Wallet Binary Transparency*, 24 June 2025. technology.a-sit.at.
18. Nunchuk. *Nunchuk Android now supports reproducible builds*, 18 September 2024.
19. Google. Pixel binary transparency, technical details (seen through a search summary).
20. Coinbase. smart-wallet repository, github.com/coinbase/smart-wallet. Safe, passkey module documentation (a search agent's paraphrase; not re-read).
21. GoodDollar. Documentation, sybil resistance. docs.gooddollar.org.
22. Trust Wallet. *What is Worldcoin (WLD)*, 2 August 2023 (Japanese edition). Cointelegraph. *World launches self-custodial super app World Money*, 18 September 2026. Apple App Store listing id1560859847, read 19 November 2026.
23. Gupta, Y. (Divide-By-0), Gurkan, K., Liu, R., Bhupatiraju, V., Whitehat, B. *ERC-7524: PLUME Signature in Wallets.* Ethereum Improvement Proposals, created 24 September 2023 (draft).
24. Privacy and Scaling Explorations. *What is MACI?* maci.pse.dev.
25. United States Patent 12,101,301 B1 (Mysten Labs, Inc.) and 12,278,816 B1 (Via Science, Inc.). Cited for what their front pages and abstracts disclose only; claims not read.
26. Lawtimes (법률신문), report of the Personal Information Protection Commission's 2024 penalty on the Worldcoin Foundation and Tools for Humanity (the census's non-English control).
27. Vinaya Piṭaka, Mahāvagga, Uposathakkhandhaka. Chaṭṭha Saṅgāyana Tipiṭaka (romanized XML, VipassanaTech/tipitaka-xml), `vin02m2.mul.xml` lines 3105, 3109, 3113, 3137, 3541 (mūla).
28. Ly, T., Miss Aquarius℠. *B-PoH as Humanity Layer for the AI-Native Internet*; *The Press Travels With the Message*; *Patent vs. Defensive Publication.* This corpus.
29. Ly, T., Miss Aquarius℠. *B-PoH Signed Statements*, version 1.4, 19 November 2026. github.com/333eco/b-poh-statements (CC0).
