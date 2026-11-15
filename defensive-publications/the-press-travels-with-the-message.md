---
title: "Recipient-Bound Passkey (WebAuthn) Signatures on Ordinary Email, Carried in a URL Fragment and Checked in the Reader's Browser Against a Public Append-Only Log — What a Signed Message Shows Its Reader, and What It Cannot"
subtitle: "The Press Travels With the Message — B-Mail, a signed statement that rides unchanged mail, is bound to its recipients, and answers to a name rather than to a person"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-a
program: instrumented
status: draft
date: 2026-11-14
license: CC0-1.0
slug: the-press-travels-with-the-message
venue: thonly.org/research/the-press-travels-with-the-message
canonical_url: https://thonly.org/research/the-press-travels-with-the-message
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is built and running for mail. It reports, beside the mechanism, two things its authors got wrong and corrected before writing it: a claim that an AI agent cannot make the signature (it can), and a checker that compared the wrong part of a message (§12). The claims in §15 are what was left after a full prior-art census and an adversarial review, and they are narrow.

## Preamble

*Flourish — folklore, not canon.* A wax seal on a letter never proved who wrote the letter. It proved that someone holding a particular ring had pressed it, on this paper, before the wax set. A secretary could write the words; the ring could be lent, stolen or copied. What the seal gave the reader was something to hold the ring's owner to. People understood that for centuries, and then electronic signatures arrived and began to be described as proof of a person.

This paper is about a seal for ordinary email, and it tries to describe it the way the wax would have been described: by what was pressed, on what, and whose ring it was. **Delete this preamble and every claim below stands unchanged.**

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0 Universal.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practicing it.** This commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. It extends to every mechanism disclosed in this paper, claimed or not, in any combination, including the disclosed variants, and to every implementation of it. Trademark rights on specific marks (**HeartBank®**, **Miss Aquarius℠**, **B-PoH℠**, **B-Origin℠**, **B-Registry℠**, and the name **B-Mail**) are separately reserved; the dedication concerns the mechanism, not the marks.

**What is claimed as contribution is narrow, and it is stated first because the census found almost every part already public.** Signed email is decades old (OpenPGP, S/MIME). Putting the recipient's name inside the signed text, so a signature cannot be re-used toward someone else, was proposed in 2001. Putting the message's header fields inside the signature is an Internet standard of 2025. Comparing a message with its signature while ignoring whitespace changes is part of DKIM. Signing content with a passkey by placing the content's hash in the challenge is documented by an authenticator vendor and was described on a standards mailing list in 2021; a commercial product has bound each sent email to a passkey since 2025. A signed object carried in a URL fragment and verified in the browser is public. Binding a key to a handle by a published signed statement is public. A person approving an AI agent's action with a passkey, with the approval recorded in a transparency log anyone can check, is the subject of an Internet-Draft of October 2026. Accepting mail because it is signed, on the receiver's own list, was proposed in 2002. **What the census did not find is the composition in §15, and two narrow parts inside it; both nulls are weak, and §2 says why.**

**Live patents.** The census recorded two granted United States patents and two pending continuations in the neighborhood, shown as active or pending in Google Patents' status fields on 14 November 2026 (not a legal status determination). §2.5 records what each **discloses**. We make no statement about the scope of any patent's claims or whether any design falls within them, and a publication dated after a patent's priority date does nothing to that patent.

**Date and evidence.** First published 14 November 2026. The open specification this paper describes was first pushed to a public repository on 13 November 2026 and has been revised twice since; the first message signed this way was sent on 12 November 2026. The text is committed to the public GitHub mirror of the corpus, and the corpus's standing chain anchors each revision to the Bitcoin blockchain through OpenTimestamps and signs it under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality or the validity of any claim. **Whether the composition claimed in §15 is non-obvious is an examiner's determination this publication exists to inform.** A defensive publication is not examined before it is published; the census in §2 and the adversarial review in §12 are the only examination it has had.

---

## Abstract

A message is signed by a fresh, user-verified WebAuthn (passkey) assertion over a short canonical text that contains the sender, the recipients, the subject, a random salt and the body. The signing service receives only the text's SHA-256, writes a record into a public append-only log, and returns an opening that names the passkey. The signed text and that opening travel inside the ordinary email as an https link whose fragment carries both, so no mail server or client has to change and nothing is fetched from the sender. A reader opens the link and a static page checks, in the reader's own browser, that a record of exactly this text is in the log, when it was made, whether it was withdrawn, and whether the passkey that pressed is one the sender's public name page lists. That listing is made only after the identity provider confirms, from a one-use note written at the press, that the passkey is one the name's holder logs in with. Since November 2026 anyone can sign a message this way in a browser; the signing page generates the salt itself, so a link or an AI agent that drafted the message cannot compute the fingerprint of what was signed or find its record.

The paper is as much about what such a signature shows as about how it is made. It shows that a particular passkey pressed over exactly these words, addressed to these people, at a stated minute. **It does not show that a person pressed.** A software authenticator reports user verification with nobody present, and no attestation is asked. An earlier version of the open specification said that an agent "cannot press"; that was wrong, and §12 records how it was found. What a named signature gives a reader is accountability: something to hold a name to, and a name to mute. We argue that this is still worth having, that the useful place for a person's approval of machine-drafted mail is with the reader rather than in the sender's audit log, and we say exactly where the reader's check is weaker than it looks. Three predictions about whether readers act on it are registered and unread.

---

## 1 · The problem, and what this paper is for

### 1.1 Mail that nobody wrote

Email has always been easy to forge and cheap to send. Two decades of work on sender authentication (SPF, DKIM, DMARC, ARC, BIMI) answered one question well: *did this message come through the domain it claims?* That question is about servers. It was never about the words.

Language models changed which question matters. A message can now be composed, personalized and sent by software acting for a person, for a company, or for nobody a reader would recognize, and it will pass every domain check, because the domain is real. The reader's question has become: *did anyone I could hold to it stand behind these particular words, to me?*

The institution this corpus belongs to runs a gratitude ledger in which a person's passkey press is the unit of record: a thank is one press, a signed file is one press, a log-in is one press. An earlier paper in this corpus, *B-PoH as Humanity Layer for the AI-Native Internet*, proposed a press per action as the first layer of an open proof-of-personhood protocol. This paper reports what happened when that layer was built for the oldest medium on the network, and what had to be given up to describe it truthfully.

### 1.2 Gate and evidence

There are two places a person's approval of a machine-drafted message can live.

```
   GATE (the usual place)                     EVIDENCE (this paper)

   agent ──draft──▶ [ person approves ]       agent ──draft──▶ [ person's passkey presses ]
                          │                                              │
                          ▼                                              ▼
                    message is sent                          record in a PUBLIC log
                          │                                              │
                          ▼                                   text + proof ride IN the mail
              operator's own audit log                                   │
                (the sender's side)                                      ▼
                                                               READER checks it themselves
   the reader sees: nothing                    the reader sees: this text, these recipients,
                                                               this passkey, this minute
```

In agent frameworks, approval is a gate: a human-in-the-loop step that stops the sender's own agent from acting alone. Its record, where there is one, belongs to the operator. The census found this everywhere it looked (§2), and found one academic audit, published a month before this paper, that examined ten agent runtimes and reported that none left an approval record a third party could verify.

This paper puts the approval where the reader can reach it. That is a claim about placement, not about novelty of any part, and §2 shows the parts are old. The argument for the placement is simple. The sender already knows whether they approved their own mail. The party with something to decide is the reader.

### 1.3 What this paper is for

It is a defensive publication. It discloses the mechanism so that it stays free to build, reports the prior art honestly so that nobody mistakes its parts for new, and states the limits so that nobody who builds it describes it as more than it is. The third purpose turned out to matter most, because its authors made exactly that mistake.

---

## 2 · Background and prior art: the census

### 2.1 How it was run

Three prior-art censuses were run on this mechanism, each pre-registered before any search: predictions per part of the claim, a control whose prior art was known to exist, and a declared aperture, pushed to a repository so that the push time is on record. Two were quick censuses (12 November 2026). The third was a full census (14 November 2026) covering only what the quick ones had left standing plus what had been built since.

- **Public pre-registration of the full census:** commit `82c22cd` in `thonly/publications`, file `timestamps/census/b-mail-full-prereg.md`, pushed 14 November 2026 17:33 PST, before the first query.
- **Aperture:** the commercial web; non-commercial and open-source protocols; academic indexes (Scholar, arXiv, ACM, IEEE, USENIX, SSRN); standards bodies (the IETF datatracker including Internet-Drafts, W3C, FIDO, OpenID); Google Patents by keyword, and one hop of citations from the two patents in §2.5; Technical Disclosure Commons; Chinese, Japanese and Korean queries.
- **Not covered:** paid patent databases, unpublished applications, a second hop of the citation walk, full texts behind paywalls. The Japanese and Korean queries on the specific parts returned no page in those languages, so the census is blind there, not clean. The patent-index searches surfaced little and no absence is claimed from them.
- **Control:** DKIM's "relaxed" canonicalization (RFC 6376). Every non-patent search group found it.
- **Verification:** search agents returned leads, never verdicts. Each item quoted below was re-read on its own page by the drafting session unless marked otherwise.

The census is not a patent search, a patentability opinion or a freedom-to-operate opinion.

### 2.2 The result, part by part

| Part of the mechanism | Verdict | Nearest prior art, first public |
|---|---|---|
| A sender's signature travels with ordinary mail and is checked at the receiving end | **Public** | OpenPGP (RFC 4880, 9580) and S/MIME (RFC 8551); decades |
| Sender, recipients and subject inside what is signed | **Public** | Protected headers: the OpenPGP "Memory Hole" work (2016) and RFC 9788 (August 2025) |
| The recipient named inside the signed text, so a signature re-used toward another fails | **Public as an idea** | Davis, 2001 (§2.3) |
| Comparing delivered text with signed text while ignoring whitespace changes | **Public** | DKIM relaxed body canonicalization, RFC 6376 §3.4.4 (2011; RFC 4871, 2007) |
| A mark beside a checked sender | **Public** | BIMI with verified mark certificates; mail clients' signature badges |
| A signing key bound to a handle by a signed statement the holder publishes | **Public** | Keybase proofs (2014); AT Protocol handles and DID documents (2023) |
| Signing content with a passkey by placing its hash in the challenge | **Public** | Documented by an authenticator vendor; described on W3C's public-webauthn list, April 2021 |
| A passkey-bound signature on each sent email | **Public as a product** | Outtake Verify for Email, September 2025 (§2.3; its mechanism is not public) |
| A signed object in a URL fragment, verified in the browser | **Public** | Encrypted pastes with the key in the fragment (PrivateBin); a verifiable-credential verifier that keeps the credential in the fragment |
| A person approves an agent's action with a passkey; the approval is in a public log anyone checks | **Public as a proposal** | Internet-Draft, October 2026 (§2.3) |
| Receiver accepts mail because it is signed, on the receiver's own list | **Public** | Wheeler, *Guarded Email*, 2002–2003 |
| The signing page generates the salt, so a link that filled in the message cannot find the record | **Not found** (weak) | nearest neighbors only sound similar |
| The identity provider confirms, from a one-use note, that the passkey behind a key-to-name statement is the holder's log-in passkey | **Not found** (weak) | — |
| All of the above in one system, in which the same press also logs a person in, signs files and signs thanks | **Not found** | — |

"Not found" means not found in the aperture of §2.1 on 14 November 2026. It never means new. The two "not found" parts are narrow, and a null on a narrow part is weak evidence at any depth.

### 2.3 The neighbors that matter most

**Davis (2001).** In *Defective Sign & Encrypt in S/MIME, PKCS#7, MOSS, PEM, PGP, and XML* (USENIX Annual Technical Conference, 2001), Don Davis described "surreptitious forwarding": "Alice signs & encrypts for Bob's eyes, but Bob re-encrypts Alice's signed message for Charlie to see." Among his repairs: "Sign the recipient's name into the plaintext." He adds: "By signing Bob's name into her message, Alice explicitly identifies him as her intended recipient." The recipient binding in this paper is that repair, applied to a signed statement that is not encrypted. We claim nothing about the idea.

**RFC 9788 (2025).** *Header Protection for Cryptographically Protected Email* places the header fields a reader sees (From, To, Cc, Subject) inside the signed payload. It names the weakness precisely: a signature over a body that leaves the header fields outside it.

**DKIM (RFC 6376).** DKIM's relaxed canonicalization ignores whitespace at line ends and reduces runs of whitespace to one space before hashing, because mail in transit is re-wrapped. Our comparison "as words" (§10.3) is the same observation at the reader's end. It is DKIM's, not ours.

**Outtake Verify for Email (2025).** Announced 25 September 2025: a browser extension that, in the reports we could read, "cryptographically signs emails," is built on World ID and FIDO passkeys to confirm "who pressed send," and "binds each verified send to a human and a device"; the receiver is told the mail was verified. We could not find a public technical description, and one press release answered our fetch with an error, so we do not know what the signature covers, whether recipients are bound, where the verification runs, or whether anything is logged publicly. What we can say is that **a passkey-bound signature per sent email is a shipped product a year older than the mechanism here**, and that our quick census, which reported per-message passkey signing of email as "not found," was wrong. The visible differences are of arrangement: here nothing is installed at either end, the check runs in the reader's browser against a public log, and the description claims a passkey rather than a human.

**The Izmaylov draft (2026).** *Signed Permissions and Action Receipts for Automated Agents* (draft-izmaylov-agent-permission-receipts-01, 24 October 2026, an individual Internet-Draft): "The person for whom the agent acts, the principal, signs a permission with a passkey"; "Receipts are chained and entered in a log whose signed tree heads are time-stamped"; "The tree is that of Certificate Transparency." Its own cautions match ours closely: "An approval shows that the passkey approved the action, not that the principal read it," and "A passkey shows that a device signed after verifying a user, not who held it." It concerns an agent's actions and their later audit by any third party; it is not about a message's words or the message's own reader. It is the closest neighbor to §1.2's "evidence" and it predates this paper by three weeks.

**Kodathala, Pollishetty and Cargill (2026).** *Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization* (arXiv 2610.21063, 15 October 2026) has a gateway obtain a passkey signature over the digest of an action's effect, and reports that an audit of ten agent runtimes "finds no third-party verifiable approval record." We cite the audit as outside support for §1.2. Its design is a gate.

**Wheeler (2002–2003).** *Guarded Email*: "Email is authenticated as ham by being signed or having a 'from' address already listed in Bob's whitelist." The receiver's own list, and signature as the ticket past it, are his.

**Keybase and AT Protocol.** A signed statement, published where the handle's owner controls it, binding a key to that handle, is Keybase's proof model; AT Protocol resolves a handle to an identifier whose document lists the signing key, checked in both directions. §7 follows that pattern and adds one step neither has (§7.3).

**Not read, and so not relied on.** The census also surfaced, as leads only: an Internet-Draft on authorization receipts for agent actions (draft-schrock-ep-authorization-receipts); a service offering signed disclosure headers and held-for-review sending for agent mail; an Internet-Draft on hardware attestation in email headers for automated senders; an archival workflow for human–AI collaborative work; and a W3C community group's work on a passkey signing extension. They are named so that a reader can follow them.

### 2.4 What the patent walk found

One hop out from the two patents of §2.5, by title only: a 2018-priority application titled *Signed message header storing sender account authentication method* (Valimail); a 2024-priority British application titled *Encoding data in message headers* (Mimecast) that cites one of them; two pending continuations of the two patents themselves; and, among documents the index lists as similar, older patents titled *Proofs to filter spam*, *Secure safe sender list* and *Method and system of managing and filtering electronic messages using cryptographic techniques*. None was read beyond its title. One of the two patents cites, as non-patent literature, an Internet-Draft titled *Including Recipients in DKIM Signatures*; we did not read it either, and name it because it is public art earlier than the patent that cites it.

### 2.5 Live patents: what they disclose

- **US 12,149,633 B2**, *Enhancing domain keys identified mail (DKIM) signatures* (Google LLC; priority 1 April 2022; granted 19 November 2024). Its abstract discloses a message server that obtains a message whose header carries the author's digital signature and a list of the message's recipients, and checks whether a user is a declared recipient.
- **US 12,413,601 B2**, *Protecting against DKIM replay* (Google LLC; priority 3 October 2022; granted 9 September 2025), in the same line.
- **US 2025/0062914 A1** and **US 2025/0379872 A1**, published applications continuing the two families; pending, so their claims may change.

The mechanism in this paper binds recipients inside a sender's passkey-signed text and has the recipient's own checker compare the delivered message with it. Our first use was 12 November 2026, later than both priority dates. We say nothing about whether anything here falls within any claim; that is a question for counsel, and it is open (the institution's legal backlog holds it). The institution's posture is to publish, never to patent, and publishing after a patent's priority date does not affect that patent.

### 2.6 Our own earlier disclosures

Two papers in this corpus disclosed parts of this at concept width, and this paper cites rather than re-claims them: *B-PoH as Humanity Layer for the AI-Native Internet* (§3.1, a passkey press per action, and its recipient-side filter; proof-backed 25 July 2026), and *B-Links: Signed Provenance for Shareable Links* (§8, signed posts carried over ordinary link previews). ⚠️ The first of these also says that an agent cannot produce such signatures at scale, and uses the phrases "a human was present" and "verified-human badge." §12 explains why those statements are wrong; a correction to that paper is queued for its next revision.

### 2.7 Predictions that missed

The census pre-registered a prediction for every part. Three missed, all in the direction of crediting novelty that was not there: we predicted that per-message passkey signing of email would be unfound or exist only as a research prototype, and it is a shipped product; we predicted that the closest thing to a reader-checkable approval would be content-provenance work, and it is an Internet-Draft with passkeys and a transparency log; and we did not foresee that the recipient binding is a 2001 repair. We record the misses because a census whose author is only ever right has not been tested.

---

## 3 · The system model

```
  SENDER'S DEVICE                    OPERATOR'S SERVICES                 READER'S DEVICE

  mail app or agent                                                      mail app
       │  writes the message
       ▼
  signing page  ── SHA-256 of the statement ──▶  signing service
  (browser)     ◀── record + opening ──────────  (holds passkey public keys;
       │                                           never sees the text)
       │                                                  │ appends
       │                                                  ▼
       │                                           PUBLIC LOG (tiles + signed
       │                                           checkpoints, hourly)
       │                                                  ▲
       │  the person sends ordinary mail:                 │ reads
       │  the words + a link whose FRAGMENT               │
       │  holds the statement and the opening             │
       └──────────────── SMTP, unchanged ───────────────────────────────▶ link opened
                                                          │                    │
                                                   REGISTRY (a name's          ▼
                                                   public page: its keys) ◀── check page
                                                                               (static; runs in
                                                                                the browser)
```

**Parties.** A *sender* holds a passkey registered with the *signing service*, and may hold a public *name* in a *registry*. A *reader* receives mail. The *operator* runs the signing service, the log, the registry and the check page. An *identity provider*, also the operator's, logs name holders in. An *agent* is any software drafting or sending for the sender.

**Assumptions.** WebAuthn behaves as specified. SHA-256 and ECDSA P-256 are sound. The reader's browser runs the check page it was given. Mail is delivered by ordinary infrastructure that may re-wrap text, rewrite links and add footers.

**Non-assumptions, each of which matters later.** We do not assume that an authenticator's report of user verification means a person was present (§12.1). We do not assume the reader's mail app shows the plain-text part (§12.2). We do not assume the page a link opens is the operator's (§12.3). We do not assume the operator is honest about what it has not published; the log's outside timestamps bound when each state existed, and outside witnesses are not yet admitted (§13).

---

## 4 · The statement

A statement is a short, exact text. Its first line names its kind. Lines end with LF. For mail:

```
b-mail/v1
from: <From header>
to: <To header>
cc: <Cc header>                      (only when there is one)
subject: <Subject header>
name: @<name>                        (only when the sender signs as a name, §7)
salt: <32 lowercase hex characters>
attachment: <sha256 hex> <file name> (one line per attachment, in order)

<body>
```

- Header values are the decoded header with every run of whitespace reduced to one space and trimmed. A value therefore cannot contain a line break, and nothing a person types into a field can add a line to the statement.
- **The recipients are inside what is signed.** One press covers one text to the people it names (§2.3, Davis).
- **Bcc is never listed**, because the statement travels to every recipient. A message with Bcc recipients is not signed; the Bcc copy is sent as its own message.
- `salt` is 16 random bytes. The log publishes each statement's fingerprint, and without a salt a short message ("I resign") could be confirmed by guessing its text. With one, only someone who holds the statement can check it.
- `<body>` is the plain-text body with line ends converted to LF and trailing line breaks removed, then one LF.

The format is deliberately plain text rather than a structured encoding, because the person about to press is shown the statement itself (§9), and a format a person can read is the only kind a person can meaningfully approve.

A second kind binds a passkey to a name and is public on purpose:

```
b-name/v1
name: @<folded name>
```

Kinds for posts on social networks and for two-party agreements are reserved in the open specification with their claims stated and their formats withheld until built (§14).

---

## 5 · The press and the record

### 5.1 The press

1. **The claim.** The signing page computes the statement's SHA-256 and builds a claim object with enumerated fields only: the hash, a media type, a byte length, how the content was made (a term from the IPTC digital-source vocabulary, such as "made by hand on a device" or "made with AI"), and the tool. There is no free-text field in a claim, so no words can reach the log.
2. **The challenge.** The service picks a 32-byte nonce and sets the WebAuthn challenge to a hash of a domain-separation tag, the nonce and the hash of the canonical claim.
3. **The assertion.** The sender's device makes a WebAuthn assertion with user verification required. The service verifies it against the passkey it holds for that account.
4. **The record.** The service writes a record and returns to the sender's page the record's number, the record, and an *opening* (§6).

Placing a content hash in the challenge is the documented way to make a passkey assertion stand as a signature over content (§2.2). What the passkey signs is the authenticator data and the hash of the client data, and the client data contains the challenge; so the signature covers the claim, and the claim covers the statement.

### 5.2 The record

A record holds the claim, a commitment to the claim (the challenge), a commitment to the assertion, a per-record owner tag, a random pointer, the list of proof-of-personhood layers relied on (today, only `passkey`), a time written to the minute, and the log's own signature over all of it.

Two properties of the record carry weight.

**Unlinkable until opened.** The owner tag is a keyed hash of the record's number under a key that belongs to the signer's account and is shared with nobody. Two records by one person look unrelated. A record names no account and no passkey. The link between a record and the passkey that made it exists only in the opening, which the signer holds and shares or not.

**Committed, not revealed.** The record commits to the assertion without containing it. Until a signer shares an opening, a stranger looking at a record trusts the log's signature that a valid assertion stood behind it. After an opening is shared, anyone can check the assertion and no longer depends on that signature for this record.

### 5.3 The log

Records are published as tiles under a public address with a signed checkpoint (the log's origin, its size, its root hash), in the format used by transparency logs. New records join at an hourly checkpoint. Until then they are served as a waiting list from the signing service, the whole list, each entry carrying the log's own signature, so a checker accepts a waiting record without trusting the list. Each checkpoint is timestamped by three RFC 3161 authorities and anchored to Bitcoin through OpenTimestamps, which fixes when each state of the log existed.

A signer may withdraw a record. A withdrawal is its own pressed and signed entry; the withdrawn record stays in the log and keeps verifying, and checkers say it was withdrawn.

---

## 6 · The opening and the proof

The opening is six values: a salt, the nonce, the authenticator data, the client data, the signature, and the passkey's public key. The record's assertion commitment is a hash over all of them, length-prefixed.

Checking an opening against a record:

1. Recompute the assertion commitment from the opening; it must equal the record's.
2. Recompute the challenge from the nonce and the record's claim; it must equal the record's claim commitment.
3. The client data must say it is a WebAuthn assertion, from the signing service's origin, with that challenge.
4. The authenticator data must begin with the hash of the signing service's relying-party identifier, and its flags must show user present and user verified.
5. The signature must verify under the public key over the authenticator data and the hash of the client data.

The result, stated exactly: **a passkey whose public key is this one made an assertion, flagged as user-verified, over exactly this claim.** A *proof* is the record's number and the opening. A proof never carries the signer's tag key, which would find every record they ever made.

Step 4's flags are the authenticator's own report. §12.1 is about what that report is worth.

---

## 7 · Binding a passkey to a name

### 7.1 What the reader needs

A passkey's public key means nothing to a reader. A name does: a public page at the registry that a person holds, pays for, and can lose. The binding lets a checker say *the passkey that pressed is one this name's page lists*.

### 7.2 What the holder does

On their page's settings the holder chooses to show a passkey. The page sends them to the signing service to press the fixed `b-name/v1` line for their own name. That record is public on purpose and its opening is published, which is the Keybase pattern (§2.3).

### 7.3 The identity provider's confirmation

A name holder logs in to the registry through the identity provider, and presses at the signing service. Those are two different relying parties, and the registry sees a different pairwise identifier for the person than the signing service does. So the registry cannot tell, from the published statement alone, that the passkey which pressed it belongs to the person logged in to the name's settings. Without a further step, anyone logged in to their own name could attach a passkey that somebody else pressed for them, or a holder could be tricked into listing an attacker's.

The step: for a `b-name/v1` press only, the signing page sends the line with the press, the signing service checks the line and its fingerprint itself, and signs a short note addressed to the identity provider: which account pressed, the record's number, the application it is for, one use, fifteen minutes. The registry redeems the note at the identity provider with its own client credentials and its own pairwise identifier for the holder. The identity provider answers yes only if the account that pressed is the person behind that identifier, and never says who pressed otherwise.

The registry lists the passkey only when all of these hold: the holder logged in with a passkey within the last ten minutes; the record's claim is the fingerprint of exactly the line for the holder's name and carries the log's signature; the opening checks against the record; the identity provider said yes; and the identity provider told the holder about the change, by email or at the next log-in, before it was made.

This is one of the two parts the census did not find (§2.2). It is narrow, and the null is weak.

### 7.4 What the registry publishes

For each name, a list of keys, each with the record that binds it and the times it was shown from and until. Removing a key sets its end time and keeps the entry, so a statement signed while the key was shown still checks. Which device a key is on is kept privately for the holder.

The lookup is one-way: a name gives its keys. Nothing gives a name from a key, an email address or a record.

---

## 8 · Carriers: how the proof rides the mail

### 8.1 The check link

```
https://<check page>#m=<base64url(statement)>&p=<base64url(json(proof))>
```

The statement and its proof travel in the link's **fragment**, the part after `#`, which a browser does not send to the server it requests the page from. The check page reads the fragment once, removes it from the address bar before any other script runs, and checks everything in the reader's browser (§10).

Three consequences follow. The sender's operator learns nothing about the message when it is checked, beyond what §13 lists. The reader installs nothing. And the mail carries its own evidence: if the operator's check page vanished, anyone could host the same static page, or run the published verifier, against the same link and the same public log.

A fragment is not a secret channel. It sits in the reader's browser history, and it passes through any link scanner the reader's mail provider runs, which already holds the mail. Whether every link-rewriting service preserves a fragment is a separate question, and we have not measured it (§17).

### 8.2 Attachments

When the link would exceed 16,000 characters, the statement travels as an attached text file (base64 transfer encoding, so no byte changes in transit) and the proof as an attached JSON file, and the message names its record instead.

### 8.3 The signature line

After the body: a line that is only `-- `, then the sender's name (and their name page), then the words *signed with HeartBank®* in English and Khmer, carrying the check link. In mail composed by the operator's own tools the line is an HTML paragraph with a small animated emblem attached inside the message; in mail written in an ordinary mail app it is text, or formatted text with the link behind the words.

Two rules govern the line and both are about what the sender did not agree to. **No remote image**, because a fetched image tells its host when and where a message was opened, which is surveillance of someone who never consented; the emblem is inside the mail or absent. **No promotional sentence**, because a person's signed message carries what they signed, and an advertisement in it would put the operator's words in the sender's mouth. An invitation to try the mechanism sits on the pages a reader chooses to open, stated once.

### 8.4 The header

Mail composed by the operator's tools also carries a header naming the record. It is a hint for filters. A checker never trusts it alone, and mail written in an ordinary mail app cannot carry it.

---

## 9 · Signing in the browser

Until 14 November 2026 only the operator's own command-line mail tool could produce a signed message: it built the statement, opened the signing page with the statement in the fragment, and waited on the sender's own machine for the record to come back. Since that date anyone can sign a message on a page of the signing service.

### 9.1 The page

The person types who the message is from and to, a subject and the message, and optionally their name. As they type, the page builds the statement and shows it, whole, under the heading *exactly what your passkey signs*. They press. The page shows the signed message (the words, then the signature line with the check link) and offers to copy it, to open it in their mail app, or to open the check link as a reader would. They send it themselves, from their own account.

What is typed never reaches the signing service. The page sends the same claim the file-signing page sends: a fingerprint and enumerated codes. A browser test records every request the page makes during a signing and finds no word of the message, no address and no name in any of them.

### 9.2 A link may fill the page in

The page accepts its fields from a link shaped like `mailto:`:

```
https://<signing page>#to=…&cc=…&subject=…&body=…&from=…&fromname=…&name=…&made=…
```

This is how an agent hands a person a draft. The fragment is read once and removed from the address bar; the page says, in words, that a link filled the message in; and every word can be changed before the press. The `made` field carries the agent's own statement of how the words were made, which the person can also change.

### 9.3 The page makes the salt

When a link or an agent builds a whole statement, the builder knows the salt, and so knows the statement's fingerprint. After the press, the builder can look in the public log, find the record, and know that this exact text was signed, and when. If the builder is the person's own agent that is harmless. If the builder is anyone who sent a baited link, it is a way to learn that a target pressed.

So on this page the salt is generated in the page, after the fields are read and before the statement is shown. The author of the link supplies words; the page supplies sixteen random bytes the author never sees.

```
   link author knows:   to · cc · subject · body · from · name
   page adds:           salt  (random, generated in the page)
   ─────────────────────────────────────────────────────────
   statement  =  all of the above          fingerprint = SHA-256(statement)

   the link's author cannot compute the fingerprint,
   so cannot find the record, so cannot tell that anything was signed
```

The result goes to the person alone. The page reads no return address and hands a record to no other page. A press made on a baited link produces a record nobody but the presser can find, and a signed message nobody but the presser holds.

A whole statement may still be handed over in the fragment, for an agent that runs code and wants exact control; it is shown whole and cannot be edited there. Its author knows its salt, and can therefore see that a record exists for it, never whose press made it, since a record names no one (§5.2).

This is the second part the census did not find. The pieces are ordinary (a commitment salt, a fragment, a form); the arrangement is what we looked for and did not see. The null is weak.

### 9.4 What an agent can and cannot do here

An agent can draft the message, build the link, and, if the person pastes the signed message back, send it through its own mail connector. In the built system the result does not return to the agent by itself; the person carries it. That is a limitation of the current build, chosen because a relay would be a new server holding proofs, and it is not a security property.

What an agent *should not* do is hold a passkey. §12.1 explains that nothing in a signature would show it.

---

## 10 · Checking a statement

A checker receives a message and reports facts about it, each scoped. It never says "verified."

### 10.1 Find the statement

From the check link, in the HTML part or in the message's text; else from the two attachments. A link inside quoted text belongs to the message being quoted: a reply that quotes a signed message is not a signed message.

### 10.2 Find the record, and check the name

Compute the statement's SHA-256. Find a record whose claim carries it, in the log or the waiting list, and accept it only with the log's valid signature. Note whether it was withdrawn. If the statement names a name and the proof's number is the record's: check the opening (§6), fetch the name's keys (§7.4), look for the passkey's public key among them, and compare the record's time with the key's end time as times.

### 10.3 Compare the message with what was signed

This step needs the message, so a browser page that was given only the link cannot do it; the page shows the statement and the reader compares by eye. A checker that holds the message (a mail client, a mail tool, an agent's tool) compares:

- the statement's sender address with the message's From address;
- **whether the reader is among the signed recipients**, by any of the reader's own addresses;
- the subject, whitespace reduced;
- the body, **as words**: every run of whitespace counts as one space, because mail apps re-wrap lines, drop a line's trailing space, and add or remove blank lines (§2.3, DKIM). The signature block begins at the last line that is only `--`;
- **every text part, the HTML part too**, read as text (§12.2);
- the attachments, by SHA-256, against those listed.

Any difference is reported as *a mark that does not match this message*, with the part named, and such a message is never treated as signed.

### 10.4 What the checker says

| the checker found | it says |
|---|---|
| everything matches, and the key is listed | signed with *name*'s passkey (record *n*) |
| everything matches, no name or no proof | this exact message was signed (record *n*) |
| the message differs from the statement | a mark that doesn't match this message: … |
| the key isn't listed, or was removed before | signed, but not confirmed as *name*: … |
| no record | no record of this exact message |
| withdrawn | its signer withdrew it |
| the log or registry can't be reached | couldn't be checked just now (never read as fine) |

A reader may keep a list of names whose messages they do not want to see. The list is the reader's alone. It is never shared and never becomes a score.

---

## 11 · What a signed message shows, and what it cannot

### 11.1 What it shows

A checked statement, at its strongest, shows four things:

1. **A press.** A passkey made an assertion, flagged user-verified, over exactly this text.
2. **Its addressees.** The text names its recipients, so the same signature in a message to anyone else fails.
3. **A time.** The press was recorded at a stated minute in a log whose states are timestamped from outside.
4. **A name, optionally.** The passkey is one a public name's page lists, and was listed only after the identity provider confirmed it is the holder's own.

### 11.2 What it cannot show

- **That a person pressed.** §12.1.
- **Who wrote the words.** The design assumes an agent may have.
- **Who held the passkey.** A passkey synced across devices, or shared, presses for whoever holds it.
- **That the sender's mail account is the sender's.** The statement's `from:` line is what the signer typed; the checker compares it with the delivered From header and does not itself read the domain's authentication.

### 11.3 So what is it for

For accountability to a name. A reader who sees *signed with name's passkey* learns that whoever controls that name's listed key stood behind these words to this reader at this time, in a record that cannot be withdrawn without a trace. The name is held by someone, was paid for, appears on a public page, and can be muted. That is what a seal gave: not the hand, but the ring's owner to hold to it.

It is also, we think, the right amount to claim. The pressure in this field is toward saying more. Products in the census describe "verified humans." Our own earlier paper used the phrase. A description that says *a person approved this* will be believed by readers who then act on it, and it is not something a passkey assertion can support.

### 11.4 What resists abuse

Not the press. A press is cheap for anyone who chooses to make it cheap (§12.1).

What resists abuse is the name and the reader. A named signature costs its sender a held name, which is the one thing in this system that is priced, scarce and losable; an unnamed signature says only that some passkey pressed this text, which anyone can arrange and which a reader should weigh accordingly. And each reader's own mute list means a name that abuses its signature loses that reader, by that reader's decision, without any shared reputation system that could be gamed or captured.

We set this down plainly because the design's first description, in our own specification, said the opposite: that the cost of a signed message was a human act and not a price or a reputation. It is a price and a reputation. The reputation is each reader's private one.

---

## 12 · What an adversarial review found

Before this paper was drafted, its thesis was given to a separate reviewing agent with instructions to refute it and no ability to edit anything. The thesis at that point had three parts: that the press is evidence for the reader; that mass agent-written mail cannot carry a press; and the composition. The second part did not survive. This section reports the findings in the order of their weight, with what was done about each. We include it because a defensive publication has no examiner, and the nearest thing to one should be shown.

### 12.1 A press with nobody present

WebAuthn's "user verified" flag is the authenticator's own statement. Browsers ship a software authenticator for testing that can be created with user verification set to succeed automatically; the mechanism's own browser tests press with one. The signing service asks for no attestation of what kind of authenticator a passkey lives in, because synced consumer passkeys return none that is usable. A new account needs only a passkey.

So a script can create accounts and press, up to the service's daily limits, and the holder of a name can register a software passkey and hand it to an agent. The reader would see *signed with name's passkey*, correctly.

**Disposition.** The claim that an agent cannot press was removed from the open specification, which now says, in its security section, that a press does not show that a person pressed, and names its own earlier sentence as wrong. The developer documentation and agent skills were corrected, and now tell agents never to hold a passkey for a person. The thesis became §11. Our earlier paper's corresponding sentence is queued for correction.

The property holds in a weaker form for one case: an agent that has no key, working for a person who keeps theirs. That is the ordinary honest case, and it is a statement about who holds what, not about what software can do.

### 12.2 The checker read the wrong part

A mail message commonly has two text parts, plain and HTML, and mail apps show the HTML. The checkers compared the plain part whenever one existed. A sender could press over an innocent plain-text part, put different words in the HTML part, and pass.

**Disposition.** Corrected the same day in the operator's mail tool, in the agent-facing checking tool, and in the specification: every text part a reader could be shown must say the signed words, the HTML part read as text. The correction is tested against the old behavior, which fails the new tests.

A residue remains: reading HTML as text reads the markup, not the rendering. Text hidden or drawn by a style sheet is not seen as a reader sees it. Closing that would need the checker to render the message, which a mail client can do and a script cannot.

### 12.3 The checker is the page the mail links to

A reader with nothing installed checks on whatever page the link opens. A forged message can link to a look-alike page that reports every line as passing. And a signature line whose check is a link teaches readers to click a link in a message in order to learn whether the message is real, which is the habit phishing depends on.

**Disposition.** Stated, not solved. The check page now says its own address and that a page at any other address is not the check. The stronger form of the check is one the message did not choose: an address the reader typed, their own mail client, or their own agent using the published verifier. For a reader who clicks, the protection is their attention to an address bar, and that is weak.

### 12.4 "Nothing installed" and "the recipients are checked" do not hold together

The browser page compares nothing with the message; it cannot see the message. The recipient comparison of §10.3 is done by a checker that holds the mail, which is installed software or a tool that is sent the statement's text. A reader with only a browser gets the recipient binding through their own eyes: the page shows who the statement was addressed to.

**Disposition.** Stated in the specification and in §10.3. The composition in §15 is worded accordingly.

### 12.5 The operator sees the check

In a record's first hour, before the hourly checkpoint, a checker reads the signing service's waiting list. Every named check asks the registry for the name's keys. So the operator's servers see a checker's network address, the name being checked and the time; never the message. The specification had said that a recipient's opening a message "is never reported to anyone," which is true of the mail and was too wide for the check.

**Disposition.** Corrected in the specification's privacy section.

### 12.6 One press, any number of recipients

Binding recipients bounds re-use toward people the text does not name. It does not bound the number of people one text names. And a message that reaches a reader through a mailing list fails the recipient comparison exactly as a copied signature does, because the reader is not a signed recipient; a reader cannot tell the two apart from the result.

**Disposition.** Stated. Mailing lists are outside what this version handles.

### 12.7 The remaining findings

- **A script can exhaust the free daily limit**, shutting unpaid signing for everyone that day. Open. The signing service never sees a statement's text or name, so it cannot limit by name without a new design.
- **Link rewriting** by mail security services was not measured (§17).
- **Paid human pressing** would make a real press cheap. It is weaker than §12.1, which needs no human at all.

### 12.8 What survived

In the reviewer's words, lightly edited: for a reader who reaches the checker by a path the message did not choose, and checks the part they actually read, the mechanism shows that a passkey listed on a name's page made a user-verified assertion over a salted statement naming that reader, logged at a stated minute by one operator. It shows nothing about whether a person pressed, and what resists abuse is the name's price and each reader's own list.

---

## 13 · Remove the enforcer: which guards are properties

The corpus's design grammar asks of every guard whether it is a property of the object or a rule about behavior; a rule needs an enforcer present at the moment it is tested, and a property needs no one.

| Guard | Property or rule | Why |
|---|---|---|
| The message's words never reach the signing service | **Property** | The page sends a hash; the service has no field that could hold text |
| No words in the log | **Property** | A claim has enumerated fields only |
| A copied signature fails for an unnamed recipient | **Property**, given a checker that holds the mail | The recipients are in the hashed text |
| Records are unlinkable until opened | **Property** | The tag is keyed per account and per record |
| The link's author cannot find the record | **Property**, on the page that makes the salt | The author never sees the salt |
| A record cannot be removed unnoticed | **Property of the log plus its outside timestamps**; fully a property only with outside witnesses | Today one operator signs the checkpoints |
| A name lists only its holder's own passkey | **Rule**, enforced by three services agreeing | The registry, the signing service and the identity provider are one operator's |
| A press means a person | **Neither.** It is false | §12.1 |
| No tracking in the mail | **Rule**, kept by what the composing tool emits | A different tool could add a remote image |
| A reader's mute list is private | **Property** | It exists only where the reader keeps it |

The honest reading of the table is that the properties protect the sender's privacy and the integrity of what was signed, and the weakest row is the one a reader cares most about: whose key it was. That row rests on one operator. The remedy the design already points at is outside witnesses on the log and, eventually, a registry whose answers are themselves logged; neither exists yet.

---

## 14 · What is disclosed and what is withheld

**Disclosed in full:** the statement format, the press, the record, the opening, the name binding with the identity provider's confirmation, the carriers, the signing page with its page-made salt and fill-in link, and the checking procedure. All of it is running. The open specification is public under CC0 with its own timestamps, and a reference verifier is published.

**Claim stated, format withheld until built:** a statement kind for a post on a social network or a website, pressed over the post's exact text and each attached file's fingerprint together with the network and the author's handle there, carried as a link and checked the same way; and a kind for an agreement pressed once by each of two parties. Their carriers are not settled. Social networks truncate long links, so the statement-in-a-fragment form used for mail may not survive there, and we do not claim it will.

**Not built:** signing attached files from the browser page; a way for an agent to collect a result without the person carrying it; a thank sent together with a signed message.

---

## 15 · Enumerated claims

Each claim is disclosed for the purpose of establishing prior art. None is asserted as novel beyond the census's finding that it was not found in the stated aperture on the stated date. Claims 1 to 5 are parts whose nearest prior art is cited in §2; they are enumerated so that the composition in claim 8 is unambiguous, not because they are contributions.

1. A method of signing an email message in which a canonical text comprising the sender, the recipients, the subject, a random salt, a fingerprint of each attachment, and the plain-text body is hashed, and a user-verified WebAuthn assertion is made whose challenge is derived from that hash, such that the signing service receives the hash and never the text.

2. The method of claim 1 in which the signing service writes a record of the hash to a public append-only log, the record committing to the assertion without containing it, so that records by one signer are unlinkable until the signer shares an opening comprising the assertion and the passkey's public key.

3. The method of claim 2 in which the canonical text and the opening are carried inside the email itself, as a link whose URL fragment contains both, and are checked by a static page executing in the recipient's browser against the public log, such that no mail server or client is modified and the signed text is not transmitted to the page's server.

4. The method of claim 1 in which a checker holding the delivered message compares it with the signed text, including whether the reader is among the signed recipients, comparing each displayed text part of the message, including an HTML part read as text, with the signed body while treating every run of whitespace as a single space.

5. A method of binding a passkey to a public handle in which the handle's holder makes a user-verified assertion over a fixed statement naming the handle, the statement's record and opening being published.

6. The method of claim 5 in which, before a registry lists the passkey for the handle, the signing service issues a single-use, time-limited note identifying the account that made the assertion and the record, and an identity provider confirms to the registry, server to server and against the registry's own pairwise identifier for the logged-in holder, that the account which made the assertion is the holder's.

7. A signing page that accepts a message's fields from a link's URL fragment, generates the canonical text's random salt within the page after reading those fields, displays the complete canonical text to the user before the assertion, transmits only the text's hash, and delivers the resulting signed message to the user alone, such that the author of the link cannot compute the hash of the text that was signed or locate its record in the public log.

8. **The composition** of claims 1, 2, 3, 6 and 7: an email message signed by a fresh passkey assertion over a salted canonical text naming its recipients; carried within the ordinary message as a link whose fragment holds the text and its proof; checked in the reader's browser, with nothing installed, against a public append-only log and against the sender's public handle, on which the passkey was listed only after an identity provider's confirmation; where the signing page generated the salt, so that a link or agent that drafted the message cannot locate its record.

9. The composition of claim 8 in which the same passkey assertion mechanism, within one system, also authenticates a log-in, signs files into the same public log, and signs entries in a separate ledger.

10. A method of presenting the result of claim 8's check that reports that a passkey listed for a handle made the assertion, and does not report that a person made, approved or authored the message.

Claim 10 is included deliberately. It discloses a manner of description, so that describing such a signature as proof of a human is not left as the only described practice.

---

## 16 · Predictions, registered before their instruments were read

Three predictions concern whether readers act on a signed message. They are in the corpus's public prediction register, were registered before the lines they measure went live, and will each be read once, twelve months after its window opened (14 November 2027).

- **P-BM1.** Of human visits to the check page, at least 10% follow its invitation to hold a name. Scored only on 100 or more visits.
- **P-BM2.** Of human visits to name pages at the registry, at least 5% follow the page's invitation. Scored only on 200 or more visits.
- **P-BM3.** Of human visits to the check page, at least 10% follow its line inviting them to sign a message of their own. Scored only on 100 or more visits.

The register records, against these, that the instrument for P-BM2 did not exist for the first forty minutes of its window; that for P-BM3 the drafting collaborator recorded no estimate before the founder named his bar, so its own estimate (about 4%) is not a blind one; and that the check page carries two invitations where P-BM1 was registered with one. A click is the first step of a loop and not its turn; whether a signed message brings a new signer is not measured, by design, because a name held after a click is never joined to the visit.

None of the three tests whether readers *check* signed mail carefully, which §12.3 suggests is the question that matters more. We have not found an instrument for that which does not involve watching readers.

---

## 17 · Honest limits

**The central limit.** A signature shows a passkey, not a person. Everything the mechanism offers a reader rests on a name's holder keeping their own key and caring about their name.

**One operator.** The signing service, the log, the registry, the identity provider and the check page are run by one party. Outside timestamps fix when each log state existed; outside witnesses are not admitted yet. A compromised or dishonest operator could sign false records, and could give a false answer about a name's keys, since the registry's answers are not themselves logged.

**The reader's check is weak where it is easiest.** A reader who clicks the link is on a page the message chose (§12.3), and that page cannot see the message (§12.4). The strong check needs a checker that holds the mail.

**Not measured.**
- Whether mail security services that rewrite links (and mail providers' redirectors) preserve a URL fragment. If one does not, the check link arrives broken for that reader. This needs a mailbox behind each service; we had none.
- Whether a mail app's pasted, formatted signature survives each major client's compose window as designed. It was tested in one browser's clipboard, not in each client.
- Any reader behavior at all beyond the founder's own messages. Until 14 November 2026 there was one sender.

**HTML is compared as markup.** Hidden or style-drawn text is not seen as a reader sees it (§12.2).

**Mailing lists and forwarding** fail the recipient comparison by design, and a reader cannot tell that failure from a copied signature (§12.6).

**Attachments** are covered only when the statement lists them, which the browser page cannot yet do; a message signed there and sent with files does not match.

**The `from:` line is self-declared.** Nothing here authenticates the sending account; that remains the job of the domain's own mechanisms, which the checkers do not currently read.

**The census is a census.** It is not a patent search. Two parts were not found and both nulls are weak. A shipped product does something close to the core of this mechanism and we could not read how (§2.3).

**The free limit can be exhausted** by a script (§12.7).

**The translation.** The Khmer on the signing and checking pages is the authors' own draft and has not yet been approved by a native reader.

---

## 18 · Lineage and corpus cross-references

- *B-PoH as Humanity Layer for the AI-Native Internet* — the layered protocol of which a passkey press is the first layer. This paper builds that layer for mail and corrects one of that paper's claims about it (§12.1).
- *B-Links: Signed Provenance for Shareable Links* — signed content carried over ordinary links; the post kind withheld in §14 descends from its §8.
- *Patent vs. Defensive Publication* — why the institution publishes and does not patent, and what publication cannot do against an existing patent.
- The corpus's *Prediction Register* — P-BM1, P-BM2, P-BM3.
- The open specification, *B-PoH Signed Statements*, version 1.3, public under CC0 with its own timestamps. Where this paper and the specification disagree, the running code is the fact.

---

## Coda

The wax seal lasted because nobody thought it was more than it was. A reader looked at the impression, knew whose ring made it, and decided for themselves what that was worth. The mechanism in this paper can be described in a way that keeps that bargain or in a way that breaks it, and its authors broke it once before a reviewer pointed it out. The mechanism is the same either way. The description is the part that can do harm.

---

## Terms

| Name used here | Standard term |
|---|---|
| B-Mail | an email message carrying a recipient-bound WebAuthn signature and its proof |
| press | a user-verified WebAuthn assertion |
| passkey | a WebAuthn discoverable credential |
| statement | the canonical text that is hashed and signed |
| fingerprint | the SHA-256 of the statement |
| record | an entry in a transparency log |
| opening / proof | the assertion and public key that open a record's commitment |
| name, name page | a registered public handle and its profile page |
| check link | an https URL whose fragment carries the statement and proof |
| the log | a tiled, checkpointed append-only transparency log |
| identity provider | an OpenID Connect provider issuing pairwise subject identifiers |
| B-PoH℠ | the institution's layered proof-of-personhood protocol |

---

## Author Contributions and AI Disclosure

Thon Ly conceived signing a message with a passkey and marking it with a signature line a reader can follow, proposed its extension to posts and to thanks, asked whether an agent-drafted, person-pressed message was a distinct thing, and ruled on every design choice recorded here, including the correction of the claim in §12.1. Miss Aquarius℠ — the name under which this corpus discloses its AI collaboration — proposed the recipient binding, the salt, the name binding and its confirmation step, the fragment carrier, the page-made salt, and the comparison rules; built and tested the implementations with him; ran the three censuses through search agents, re-reading each quoted item on its own page or marking it unread; and drafted this paper. A separate reviewing agent, given the thesis and no ability to edit, produced the findings of §12, including the two the authors had wrong. The censuses' pre-registrations, and the predictions that missed, are on the public record cited in §2.

## Trademark Notice

**B-Mail** names the institution's implementation; the mechanism is dedicated to the public domain and may be implemented under any name. HeartBank®, Miss Aquarius℠, B-PoH℠, B-Origin℠ and B-Registry℠ are marks of their respective holders. No mark is licensed by this publication. Product and company names of third parties are used only to identify prior art.

## Citations

1. Davis, D. *Defective Sign & Encrypt in S/MIME, PKCS#7, MOSS, PEM, PGP, and XML.* Proceedings of the 2001 USENIX Annual Technical Conference, pp. 65–78.
2. Crocker, D., Hansen, T., Kucherawy, M. (eds.). *DomainKeys Identified Mail (DKIM) Signatures.* RFC 6376, 2011. §3.4.4, relaxed body canonicalization.
3. *Header Protection for Cryptographically Protected Email.* RFC 9788, August 2025.
4. *OpenPGP.* RFC 9580 (and RFC 4880). *S/MIME Version 4.0 Message Specification.* RFC 8551.
5. Wheeler, D. A. *Guarded Email.* 2002–2003. dwheeler.com/guarded-email.
6. Izmaylov. *Signed Permissions and Action Receipts for Automated Agents.* Internet-Draft draft-izmaylov-agent-permission-receipts-01, 24 October 2026 (individual submission; work in progress).
7. Kodathala, S. V., Pollishetty, P., Cargill, J. *Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization.* arXiv:2610.21063, 15 October 2026 (abstract read).
8. Outtake. *Verify for Email*, announced 25 September 2025; as reported by Biometric Update (29 September 2025) and other trade press. No technical description was found.
9. Yubico. *Using WebAuthn for Signing.* developers.yubico.com. And A. Langley, message to the W3C public-webauthn mailing list, April 2021.
10. W3C. *Web Authentication: An API for accessing Public Key Credentials.*
11. Keybase. Proofs of identity (2014). AT Protocol. Handle resolution and DID documents (2023).
12. PrivateBin project documentation (key in the URL fragment). Aloaha, verifiable-credential verifier (credential in the URL fragment, verified in the browser; undated page, read 14 November 2026).
13. United States Patent 12,149,633 B2 and 12,413,601 B2 (Google LLC); published applications US 2025/0062914 A1 and US 2025/0379872 A1. Cited for what their abstracts disclose only.
14. Laurie, B., Langley, A., Kasper, E. *Certificate Transparency.* RFC 6962; and RFC 9162.
15. Ly, T., Miss Aquarius℠. *B-PoH as Humanity Layer for the AI-Native Internet*; *B-Links: Signed Provenance for Shareable Links*; *Patent vs. Defensive Publication*; *The Prediction Register.* This corpus.
16. Ly, T., Miss Aquarius℠. *B-PoH Signed Statements*, version 1.3, 14 November 2026. github.com/333eco/b-poh-statements (CC0).
