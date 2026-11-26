---
title: "An Opt-In Image Mark That Carries Only an Address: A QR Code Inside an Emblem, Turned by the Encoder According to Its Address Class, With an Error-Corrected Coarse Fingerprint of the Host Picture in Its Spare Modules and the Signer's Own Hand in Place of the Issuer's Sign, Beside an Invisible Watermark Holding the Same Address"
subtitle: "An Address in the Picture — B-Watermark℠, a mark that leads back to a signed record: an address or a drawing, never the issuer's claim"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-b
program: open
status: draft
date: 2026-11-25
license: CC0-1.0
slug: an-address-in-the-picture
venue: thonly.org/research/an-address-in-the-picture
canonical_url: https://thonly.org/research/an-address-in-the-picture
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is built and running for pictures. It reports, beside the mechanism, what an adversarial review found wrong with the way the authors first described it: that the mark "claims nothing" does not hold for every part, that one part carries no information inside the mark, and that the fingerprint can show a copied mark is wrong but never that one is right (§12). The claims in §16 are what was left after two prior-art censuses and that review, and they are narrow.

## Preamble

*Flourish — history, not canon.* A painting that passed through Chinese and Japanese collections often carries more seals than strokes: the painter's own, then one for each collector who held it, stamped in the margins over centuries. No seal ever proved that a painting was genuine. Seals were carved again, lent and forged. What a seal gave a later viewer was a place to look: an impression to compare against impressions recorded elsewhere, in catalogs and in other works the same owner had stamped. The seal was an address, and the record was where the answer lived.

This paper is about a mark of that kind for pictures that travel on the internet, and it tries to describe the mark the way a careful connoisseur would describe a seal: by what it points to, and by what it cannot show. **Delete this preamble and every claim below stands unchanged.**

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0 Universal.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practicing it.** This commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. It extends to every mechanism disclosed in this paper, claimed or not, in any combination, including the disclosed variants, and to every implementation of it. Trademark rights on specific marks (**HeartBank®**, **Miss Aquarius℠**, **B-Origin℠**, **B-Watermark℠**, **B-Autograph℠**, **B-Fingerprint℠**, **B-Symbol℠**, **B-Emblem™**) are separately reserved; the dedication concerns the mechanism, not the marks.

**What is claimed as contribution is narrow, and it is stated first because two censuses found almost every part already public.** An invisible watermark that carries a short identifier leading back to a record, recoverable after a picture's metadata is stripped, is public and is deployed by the content-provenance industry. A visible QR code laid into a photograph is sold as a product. A two-dimensional barcode placed inside an image and carrying a hash of that image's regions is the subject of a patent with priority to 2009; a watermark whose payload decodes only when the image's perceptual hash matches the one it was embedded in is described in a patent with priority to 2000, against exactly the attack of copying a mark from one picture to another. Rotating a whole two-dimensional tag so that each orientation carries a different codeword was published in 2004, and selecting what a QR code retrieves by the angle at which it is captured is described in a patent with priority to 2012. A free canvas area inside a QR code is a commercial format. Typing a name and adopting it in a handwriting font is ordinary electronic-signature practice, and single-stroke script faces are old and open (an engraving tool shipped one in 2011). A log's signed promise of later inclusion, carried inside the object it concerns and later replaced by an inclusion proof, is Certificate Transparency's design of 2013. **What the censuses did not find is the composition in §16, and three narrow parts inside it; every null is weak, and §2 says why.**

**The census, reported in full in §2.** Two censuses ran before this paper was written. A quick one on 24 November 2026 (English web, non-commercial practice, Google Patents by keyword) and a full one on 25 November 2026, whose pre-registration was pushed to a public repository before its first query: **Public pre-registration:** `73cee9c` in `thonly/publications`, `timestamps/census/b-watermark-full-prereg.md`, pushed 2026-11-25 21:30 PST, stamped by OpenTimestamps. The full census searched the commercial web, non-commercial practice, Google Patents through a general web index with a walk from five patents' citations and similar documents, academic indexes, standards bodies, and Chinese, Japanese and Korean sources; Technical Disclosure Commons was queried and returned no page, so it was not seen. Each of its five search groups found a control item named in the pre-registration before any of its absences was believed, two of them only after a second attempt (§2.1). Its verdicts, conjunct by conjunct, are in §2.2. **Not found means not found in that aperture on that date. It never means new.**

**Patents in the neighborhood.** The censuses recorded granted United States patents in the neighborhood whose current status was not checked. §2.4 records what each **discloses**. We make no statement about the scope of any patent's claims or whether any design falls within them, and a publication dated after a patent's priority date does nothing to that patent.

**Date and evidence.** First published 25 November 2026. The mechanism was built between 23 and 25 November 2026 and opened to every user of the signing portal on 24 November 2026; its drawing code and its fingerprint's reader are published as open files of the institution's brand layer, and a public page describes the whole of it. The text is committed to the public GitHub mirror of the corpus, and the corpus's standing chain anchors each revision to the Bitcoin blockchain through OpenTimestamps and signs it under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality or the validity of any claim. **Whether the composition claimed in §16 is non-obvious is an examiner's determination this publication exists to inform.** A defensive publication is not examined before it is published; the censuses in §2 and the adversarial review in §12 are the only examination it has had.

---

## Abstract

An opt-in image mark, an invisible watermark with an optional visible QR code, made on the signer's own device when they sign a picture into a public append-only log, carries only an address: a 12-character code that a link resolver turns into a page showing the signed picture and its record. The address is written twice. Invisibly, it is carried in an open-source watermark spread through the picture's colors. Visibly, and only if the signer chooses, it is a QR code drawn inside the issuer's heart-shaped emblem and composited into a corner of the picture or onto a strip made of the picture's own bottom edge. Three further parts live in the emblem's free space. The encoder turns the whole code by a quarter-turn chosen from the class of the address it holds, so that the code's middle finder pattern stands at the emblem's point for a link-resolver address; it refuses to encode any address outside the issuer's domains. The emblem's top lobe carries 96 decorative modules, written twice, holding an error-corrected coarse fingerprint of the host picture (36 cells, each brighter or darker than the median, the cells under the emblem itself left out), so that anyone can tell, with no network, that a heart copied onto a picture of a different layout was not drawn for it. The bottom lobe, which in the issuer's own codes holds a ™, holds instead the signer's own hand, captured as strokes or typed as a name in a single-stroke script, refused on any picture the signer declares to be AI-made. Two looks with no code, a faint heart and a small emblem beside the signer's hand, are allowed only when the invisible mark is written into the same file and read back before the signature. The saved file may carry the log's signed receipt and, later, its inclusion proof.

The paper is as much about what the mark can say as about how it is made. **The pixels hold no signature**: an address of 60 bits and 36 cells of layout cannot carry one. The issuer asserts nothing about the picture in its pixels; a hand or a name in them is the signer's own, unchecked. The fingerprint is one-sided, the quarter-turn is constant inside a mark, and every visible part can be copied or removed. What the mark gives a viewer is the way back to the page that answers, and we say where that way is weaker than it looks.

---

## 1 · The problem, and what this paper is for

### 1.1 A picture leaves its record behind

A person who signs a picture into a public log has made a record that anyone can check: this exact file existed, was pressed by this passkey, at this minute, and has or has not been withdrawn since. The record is only useful to someone who can find it. The direct way to find it is to hold the exact file and look up its fingerprint. That works for the file the signer saved. It fails for almost every copy the picture will actually reach: a social network re-encodes the picture, resizes it, and strips its metadata; a screenshot changes every byte; a crop changes the dimensions. The record still exists and the picture still circulates, but nothing in the circulating copy leads back.

The content-provenance industry's answer is to put a second binding into the pixels themselves, a watermark or a perceptual fingerprint that survives where metadata does not, and to use it to find the record again (§2.3). This paper starts from that answer and asks two narrower questions. Can a person, rather than a platform, choose to make the way back visible, so that a viewer with an ordinary phone camera can follow it? And can the visible part be made so that it says nothing on the issuer's behalf about the picture, which the issuer is in no position to say?

### 1.2 Address and claim

A mark in a picture can do two different jobs. It can **claim** something (*this is real*, *this is verified*, *this person made this*), or it can **address** something: give the location of a place where an answer can be found. A claim is only as good as whoever is making it and whether the mark can be forged; a mark that anyone can copy turns a claim into a lie the moment it is copied. An address survives copying because the page it leads to shows the original, and a copy that does not match the original exposes itself by being compared with it.

The design rule that governs everything below is the second job only: **the mark is an address, or a drawing a person chose to put next to one, and never a claim by the issuer.** No word in the pixels says *signed*, *verified* or *real*. The rule was not obvious at the start. The first question the founder asked, on 23 November 2026, was whether the issuer's emblem should be drawn on signed pictures to tell the public they had been signed. It should not, for the reason the content-provenance standard's own guidance gives: *"To avoid spoofing, do not directly overlay the indicator on top of content or embed it directly into the pixel content"* [1]. An emblem in the pixels can be pasted onto any picture. What can be put in the pixels honestly is a way to the page that answers.

### 1.3 What this paper is for

This paper discloses the mark as built: its five parts, its two code-less looks, the order in which they are made relative to the signature, and the check a viewer can run with no network and with one. It reports two prior-art censuses in full, including the many parts that were already public. It reports an adversarial review of the authors' own first description, which found four places where *"claims nothing"* did not hold as written, and states what the mark actually says in each. And it enumerates, as claims, only the composition and the three narrow parts that the censuses did not find.

---

## 2 · Background and prior art: the censuses

### 2.1 How they were run

**Quick census, 24 November 2026.** The founder's question, put the evening the mark's last part was built, was whether the whole might be new *"at least as a combination"*. The claim was split into six conjuncts, each with a prediction written before the first query, and a control item known to exist. The pre-registration was committed and pushed (memory repository, `62d1739`) before the first search. Aperture: the commercial web in English, non-commercial practice (artists' signatures and seals, watermark customs, open-source QR art), and Google Patents by keyword. Verdicts: the invisible address (a) and the visible code in a picture (b) were **killed**; the hand in the code's free area (c), the fingerprint in spare modules (d) and the encoder-set turn (e) were **narrowed**; the composition (f) was **not found**.

**Full census, 25 November 2026.** It covered only what the quick census left standing, plus what was built after it ran: the receipt in the saved file (g), the two code-less looks gated on the invisible mark (h), the refusal of a hand on a picture declared AI-made (i), and the typed name (j). Its pre-registration, including a control item for each of five source groups, was pushed privately and then publicly before the first query (the *Public pre-registration* line above). Five research agents searched one group each; the agents return candidates and query logs and never a verdict, and the verdicts were ruled afterward. The patent group missed its control on its first pass, because the general web index it searched through does not resolve a bare patent number, and was run again with queries that describe the patent's content and with a walk of five patents' citing and similar documents on Google Patents; on that pass it found its control, and a third pass then searched the two conjuncts, (c) and (i), whose only patent queries had run while the control was missed. The Japanese control was found only once the query was limited to the format owner's own sites, so open-web Japanese queries may not see what they do not name. Every item quoted in this section was re-read on its own page on 25 November 2026; items seen only as search summaries are named without quotation or not at all. No patent's claims were read.

**What neither census searched:** native patent offices (CNIPA, JPO, KIPO), paid databases, Khmer sources, and any reading of a patent's claims. Technical Disclosure Commons returned no page to either group that queried it, so it is blind here, not searched. The normative text of the QR code standard (ISO/IEC 18004) and NIST publications were not read. Korean sources had one query. Academic and patent absences reach only what a general index exposes.

### 2.2 The result, part by part

| | Conjunct | Predicted | Verdict | The nearest prior art |
|---|---|---|---|---|
| (a) | an invisible watermark carrying a short address that resolves to a record, surviving the loss of metadata | killed | **KILLED** (quick) | Durable Content Credentials: a watermark carrying an identifier, plus a fingerprint, recovering a manifest [2]; Digimarc patents on an identifier in an image leading to a record [3]; Wacom's Yuify |
| (b) | a visible QR code composited into a person's picture | killed | **KILLED** (quick) | commercial QR watermarks on photographs; a verification address as a QR code [4]; a barcode in a logo's shape [5] |
| (b′) | the code on a strip made of the picture's own bottom edge, mirrored and melted, with its printed address | narrowed | **NOT FOUND** (weak) | edge reflection for image filtering only |
| (c) | the signer's hand, kept as strokes, inside the issuer's QR-bearing emblem in place of the issuer's own sign | narrowed | **NARROWED** | Frame QR's free canvas area inside the code [6]; a custom graphic, a photograph or drawing of a face, inside an optical code [26]; logos inside QR codes; the painter's signature and seal (*rakkan*, 落款) |
| (d) | decorative modules beside a standard QR, in the same drawing, carrying an error-corrected coarse fingerprint of the host picture with the mark's own footprint masked, read offline | narrowed | **NARROWED**, further than predicted | a 2D barcode inside an image carrying hash check values of the image's regions [7]; a watermark payload that decodes only if the image's perceptual hash matches [8]; content-dependent watermarks against transfer between images [9] |
| (e) | the whole code's quarter-turn set by the encoder from the class of the address it holds, an outside address refused | narrowed | **NARROWED**, further than predicted | each rotational orientation of a tag carrying its own codeword [10]; the capture angle of a QR code selecting the item retrieved [11]; orientation as a second channel inside modules [12] |
| (g) | the saved file carries the log's signed receipt, later replaced by an inclusion proof | killed | **KILLED** | Certificate Transparency's signed certificate timestamp, embedded in the certificate as a promise of inclusion, with a proof demanded later [13]; Sigstore bundles' inclusion promise beside the inclusion proof |
| (h) | the issuer's emblem without a code only when the invisible mark is written and read back before the signature | narrowed | **NARROWED** | a barcode and a machine-readable watermark in one image, recognized together [14]; an imperceptible mark that signals other provenance marks are present [15]; two watermarks in one host image [16] |
| (i) | a hand refused on a picture whose declared source is AI-generated, at the device, the server and the signature | narrowed | **NARROWED** | the declared digital source type as the primary signal for synthetic content [17] |
| (j) | a typed name drawn in a single-stroke script, as strokes, into the same pad as a drawn hand | killed | **KILLED** | electronic-signature systems that let a user pick a handwriting font for a typed name [18]; single-stroke script faces for engraving [19] |
| (f′) | all of it in one mark, each part the signer's choice, the whole an address | not found | **NOT FOUND** (at this depth) | the nearest each hold a part |

**Mechanism width:** nothing survives; every part is either public or has public neighbors that remove most of its width. **Composition width:** survives in the declared aperture, and three narrow remainders survive on their own: (c) the hand in place of the issuer's sign inside the issuer's emblem, (d) the masked coarse fingerprint in decorative modules beside a standard QR, and (e) the encoder-set turn by address class. (b′), the read-back gate of (h), and the refusal in (i) survive only as narrow dependents. **The survivor, in one sentence:** *a signer-chosen mark in a person's own picture, a QR code inside the issuer's emblem, whose spare modules in one lobe carry an error-corrected coarse fingerprint of that very picture with the mark's own footprint left out, whose other lobe carries the person's own hand in place of the issuer's sign, and whose code the encoder turns to the orientation its address's class declares, the issuer asserting nothing about the picture.*

### 2.3 The neighbors that matter most

**Durable content credentials [2].** The content-provenance industry already binds a record to a picture in three ways at once: a cryptographic manifest in the file's metadata (a *hard binding*), and, for when the metadata is stripped, an invisible watermark and a perceptual fingerprint (*soft bindings*) that let a reader find the manifest again in a repository. The invisible half of this paper's mark is that design, using one of the same open-source watermark models. Nothing in this paper is claimed for it.

**Digimarc's copy-attack defense [8].** A watermark can be read out of one picture and written into another, so that a forged picture carries a genuine mark. A Digimarc patent with priority to September 2000 describes making a watermark's payload decodable only when the perceptual hash of the image being read matches that of the image it was embedded in: *"the reader can only correctly decrypt or descramble the payload and CRC bits if the perceptual hash of the read image matches that of the embedded image."* This is the same function as the fingerprint in this paper's top lobe, achieved invisibly. The difference that survives is where the fingerprint lives (in visible decorative modules beside a standard code, readable by anyone with a camera and an open reader) and what it does not try to do (it never withholds the address; it only reports a mismatch).

**A barcode of the image, inside the image [7].** Digitalzone's patent, priority 22 May 2009, generates a two-dimensional barcode from check values computed by a hash over the bitmap's rows, columns and regions, and inserts it into the image for forgery verification. This is closer to (d) than the quick census found, and it is why (d) is claimed only at the width of decorative modules beside a standard code, with the mark's own footprint masked and the answer limited to *looks like* or *looks different*.

**Rotation as data [10][11].** Silverbrook's *Symmetric tags* (priority 4 March 2003) describes tags in which *"each tag orientation (in a rotational sense) contains one codeword placed at that orientation."* GSPI's patent (priority 1 December 2012) selects which item a QR code retrieves by the angle at which the code is captured. Whole-code orientation as a channel is therefore public. What was not found is an encoder that sets a standard QR code's quarter-turn itself, from the class of address it is encoding, and refuses addresses outside a fixed set while doing so. As §6.3 and §12.7 explain, that remainder carries no information a camera does not already read.

**Frame QR [6].** Denso Wave's format reserves *"the canvas area, where graphics, letters, and more can be flexibly arranged"* in the center of the code. This paper's hand sits not in the code but in the emblem around it, in the place where the issuer's own codes carry a ™; the census found no instance of a person's hand replacing the issuer's sign in the issuer's own emblem.

**A signpost mark [15].** A paper posted on 10 August 2026 trains *"signpost watermarks that indicate the presence of independently deployed provenance watermarking systems."* Its signposts are imperceptible; this paper's faint heart is visible. The function, a mark whose job is to say that another mark is there, is the same, and it is why (h) is claimed only at the width of the read-back gate.

### 2.4 Patents in the neighborhood: what they disclose

Recorded, status not checked, for counsel's review. US 11,734,532 (two-dimensional codes modulated in both intensity and orientation) · US 12,289,405 (a graphical watermark, granted 2025) · US 9,621,565 (photo authentication with a verification address as a QR code) · US 10,394,419 B2 (GSPI; retrieval selected by a QR code's capture angle; granted 27 August 2019) · US 9,760,818 B2 (Hewlett Packard; a barcode and a machine-readable watermark recognized together in one image; granted 12 September 2017) · US 8,690,049 B2 (Digitalzone; a 2D barcode of an image's regional hash check values inserted into the image; granted 8 April 2014) · US 11,899,927 B2 (Adobe; simulated handwriting; granted 13 February 2024) · US 9,111,164 B1 (a custom graphic inside an optical code). Cited for what their descriptions disclose only.

### 2.5 Our own earlier disclosures

The signing mechanism the mark rides on, a fresh passkey assertion over a file's hash appended to a public tiled log with signed, timestamped checkpoints, is disclosed in *B-Links: Proof-of-Humanity-Signed Shareable Provenance* §4.1 [20]. Finding a released film's record again for an unlisted copy *"by perceptual matching or a watermark"*, reported as *"a likely match … never as a check passed"*, is disclosed as Variant C of *Every Lent Face Signed This Cut* [21]; this paper's wording for every positive answer follows it. The open and filled styles of the emblem-shaped code appear in *The Ticket and the Tag* [22]. The two proof-states of the emblem, static for an anchored entity and beating for a living human, are in *Brand Identity as Architecture* §5.5 [23].

### 2.6 Predictions that missed

Both directions. (d) and (e) were narrowed further than predicted: the quick census found neither the 2009 barcode of an image's own hash nor the 2003 rotational tags. (h) met a neighbor three months old whose function is the faint heart's, which was not predicted at all. (b′) was predicted to be narrowed by letterboxing practice and turned up nothing beyond edge reflection for filtering. (g) and (j) were killed, as predicted. And the patent group's first pass missed its control for a reason no one predicted: a general index cannot see a patent by its number. A future census names its patent control by content.

---

## 3 · The system model

```
  signer's device                     the issuer's services                      a viewer, anywhere
  ───────────────                     ─────────────────────                      ──────────────────
  picks a picture (a public file)
  chooses: invisible · B-QR (corner
    or strip) · hand · faint · symbol
                │
                ├── 1 ask for a mark's address ──▶ link resolver (b.333.eco)
                │◀─────── 12-character code ────  makes an unlisted link;
                │                                   its page exists, says nothing yet
  draws the code, the lobes, the hand
  writes the invisible mark
  READS BOTH BACK on the device
  hashes the marked file
                ├── 2 press ─────────────────────▶ signing service (sign.333.eco)
                │   (a fresh passkey assertion       countersigns; appends a record
                │    over the file's hash)           to the public log (log.333.eco)
                │◀─────── receipt ────────────────
                ├── the marked file, for the page ▶ the portal (origin.333.eco) makes
                │                                   the page's picture from the exact
                │                                   signed bytes; keeps no full copy
  saves the marked picture,                                                     meets the picture,
  with its receipt (later, proof)                                               cropped, re-encoded,
                                                                                 stripped of metadata
                                                                                       │
                                                  b.333.eco/<code> ◀── camera ─────────┤ (the B-QR)
                                                  the mark's page:  ◀── open decoder ──┤ (the invisible mark)
                                                  the signed picture,                  │
                                                  the record, compare                  │
                                                                                 reads the top lobe
                                                                                 offline: drawn for a
                                                                                 picture like this one,
                                                                                 or not
```

**Parties.** The *signer* holds a passkey and signs on the signing portal. The *issuer* runs the link resolver, the signing service, the log and the portal; it is the party whose emblem the mark uses. A *viewer* meets the picture anywhere, usually as a copy.

**Where things run.** The marks are drawn, written and read back on the signer's own device, in a web page on the portal's origin; the watermark's writer (17 MB) and reader (47 MB) are open-source models fetched on request and checked against pinned hashes, and they never load on the signing service's own origin, where passkeys are bound. **The picture does not stay on the device**: for the mark's page to show the signed picture, the marked file is sent to the portal, which makes the page's picture from the exact signed bytes, so that nobody can pair a record with a different picture, and does not keep the full copy.

**What the issuer never learns from the mark.** The record in the log names no signer and holds no free text. The portal joins a mark to its file's hash, never to a record's index; a viewer's device finds the record by the file's fingerprint in the public log, as the signing portal's own checker does. Who signed is shown on the mark's page only if the signer adds their registered name afterward, by a separate press (§9).

---

## 4 · The order of operations: the press covers the marked file

```
   1  ask for a mark's link ─── the link exists; its page says nothing yet
   2  draw the B-QR (if chosen) ─── corner or strip, with its two lobes
   3  write the invisible mark (if chosen, or forced on by a code-less look)
   4  READ BOTH BACK on the device ─── a mark that does not read is refused here
   5  hash the marked file
   6  press ─── the record covers exactly these bytes
   7  the log takes the record ─── the page now shows the signed picture,
                                    the record, and "compare with yours"
      a canceled press ends the link (step 1) and nothing is published
```

The order is the mechanism's first guard. The marks are made **before** the signature, so the record covers the picture exactly as it will circulate, marks included; a mark added after the signature would be a new file that no press covered. The link is made **first**, because the visible code must contain its address before the picture is hashed. Both marks are **read back** on the device before the hash, because a mark that does not read is worse than none: it promises a way back that is not there. The unmarked original may be named in the record's list of ingredients, or signed on its own.

A person may also mark a picture they signed and kept earlier: *Add a B-Watermark* on a kept picture opens the same flow with it, and the result is **a new record with a new press**, never a mark retrofitted to an old one. It is not offered on a file someone else gave them, or on a picture already marked.

---

## 5 · Part one: the mark nobody sees

**The model.** The invisible mark is Adobe's open-source TrustMark, variant Q [2], in the schema of its 100-bit payload that holds 61 data bits (`BCH_5`): the 12-character code (60 bits) and one fixed bit. Its most strongly corrected schema holds only 40 bits, too few for an unlisted address (below). **A number read from a picture is treated as the issuer's only if three things hold:** its last bit fits, the link it names exists, and that link's page names the file. The weaker schemas of the same model sometimes return a number by chance from an unmarked or turned picture; they are never read as the issuer's.

**Why twelve characters.** The link resolver's ordinary links have seven characters and are listed in its public log in plain words. A walk of that log would then list every marked picture, which is exactly the index the mark must never create. A twelve-character link is unlisted, and twelve characters still fit the 61-bit schema and keep the visible code at QR version 2.

**Limits of size.** At least 512 pixels on the short side, and at most about 16.7 megapixels, the largest canvas the iOS browser will draw. A marked JPEG is saved at quality 0.95; a PNG stays a PNG. The file's other metadata stays behind, and the page says so.

**What was measured, and how.** Every number below came from software decoders and simulated resizing on 23–25 November 2026, never a phone camera, a real network's re-encoding, or print. The first round, on 23 November, used the 40-bit schema; the 61-bit schema was then measured to hold as well on the first row's treatments, and the rows marked † were measured on the 40-bit schema only.

| Treatment | The mark nobody sees |
|---|---|
| JPEG quality 50; 320 px on the short side; 10% cut off each side; a phone screenshot; a visible code drawn over it | found |
| 160 px; 20% cut off; a quarter turn; a 32 × 32 sprite at native size † | not found |
| JPEG quality 75 at 1,080 px, a photograph, flat art and line art, both code-less looks | found, 6 of 6 |
| copied with the public writer into an unrelated picture † | found (the copy's record fingerprint 36 away: caught by the page, §11.2) |
| a 30%-wide patch of the marked picture changed | found (the record fingerprint 5 away: **not** caught, §11.2) |

**Its visible cost.** On a photograph the change is about 42 dB PSNR. On flat and line art it is not invisible: on one line drawing, 24% of the white outside the heart moved by more than 2 of 255, at most by 26, a faint gray blotching visible at full size, with faint horizontal smears in flat color fields visible even at thumbnail size. The look-without-a-code options (§10) exist for exactly the artists whose work is flat or line art, so this cost falls on them first. It was shown to the founder before the looks shipped; a working artist's review of it has not happened.

---

## 6 · Parts two and three: the B-QR and its four positions

### 6.1 The drawing

```
                 the B-Emblem: a heart turned 45°, point ↙, notch ↗
   ┌────────────────────────────────────────────────────────────────────┐
   │                                                                    │
   │   TOP LOBE ······· decorative modules; in a mark, B-Fingerprint℠    │
   │                    (96 bits, written twice, checkerboard)           │
   │                                                                    │
   │   BODY ··········· the QR code: version 2, 25 × 25 modules,         │
   │                    HTTPS://B.333.ECO/<12 characters>,               │
   │                    its 4-module quiet zone kept clear,              │
   │                    the middle finder pattern at the heart's POINT   │
   │                                                                    │
   │   BOTTOM LOBE ···· the issuer's own codes: a small ™, which names  │
   │                    the emblem and shows which way is up;            │
   │                    a person's picture: B-Autograph℠, their hand     │
   │                                                                    │
   │   GROUND ········· a see-through white heart, about 70% white       │
   │                                                                    │
   └────────────────────────────────────────────────────────────────────┘
```

The visible mark is the issuer's emblem-shaped code, drawn in its open style (the lobes outlined, not filled) at 22% of the picture's short side. The code is the address in QR alphanumeric mode, uppercase so that it stays version 2, and it is sized for the standard four-module quiet zone; decoration never enters that zone. Outside it, wherever a dot clears the emblem's outline, the issuer's ordinary codes carry decorative dots chosen by a stream seeded from the address, never three in a row. In a mark, the top lobe's dots are replaced by the fingerprint (§8).

### 6.2 Corner and strip

**Corner.** The code alone in a corner of the picture, on a see-through white heart. Measured on 28 corners of 7 pictures at 1,080 px, JPEG quality 80, with three decoders (jsQR · ZXing · Apple Vision): a white square behind the code read 28 · 28 · 28; a heart at 70% white also 28 · 28 · 28, and 26 · 27 · 28 at 720 px quality 70; **no white at all, 15 · 15 · 16.** So the code is never drawn as bare modules on the photograph. The corner carries no printed address; a phone's photo library detects the code by itself.

**Strip.** A band below the picture, 22% of its height, made of the picture's own bottom edge mirrored and melted into soft color, so that the picture appears to continue. On it stand the code, the printed address with dashes in groups of four (`B.333.eco/7K2M-9QX4-B8T3`), and the words *Scan to open in B-Origin*, on the side the signer chooses. The words take whichever ink wins on the **worst** pixel under them, eased to a contrast of at least 4.5 : 1; an earlier version measured contrast against the strip's average and printed dark words on a dark side, which is why the rule is the worst pixel. At 22%, the strip's code read on 7 of 7 pictures at 1,080 and 720 px and 5 of 7 at 480; at 14% it failed at 480. The strip's words are in English only until a native reader has read the Khmer, because pixels, once posted, cannot be corrected.

**A code only where the page shows the picture.** The visible code is offered only where the link's page shows the signed picture. A doctored copy that keeps the code then leads a viewer to the original, and the difference is visible by eye.

### 6.3 The four positions

A QR code has three finder patterns; the one between the other two is the *middle* marker. Decoders read a code at any of its four quarter-turns, so the corner in which the middle marker stands is free to set. The encoder sets it from the address:

```
  quarter turns (counterclockwise)   0              1              2               3
  name                               STANDARD       POINT          NON-STANDARD    NOTCH
  middle marker at                   top left       bottom left    bottom right    top right
                                     ■ ─ ■          ■ ─ □          □ ─ ■           ■ ─ ■
                                     │   │          │   │          │   │           │   │
                                     ■ ─ □          ■ ─ ■          ■ ─ ■           □ ─ ■
  the address is                     an issuer      a link-        an issuer       a link-
                                     address        resolver link  address         resolver link
  drawn by                           the issuer     the issuer     an outsider*    an outsider*

  ■ finder pattern   □ the empty corner        * through the issuer's interface, which has no caller yet
```

At the point and at the notch the code's own mirror line, the diagonal through its middle marker, lies on the emblem's mirror line, so a link-resolver code is the symmetric one; at the other two the lines cross. Measured over 4,320 drawings per position, the four positions read alike (upright 3,916 · 4,102 with jsQR · ZXing, point 3,930 · 4,090, bottom right 3,930 · 4,083, notch 3,930 · 4,106; Apple's reader 691 · 688 · 685 · 691 of 720). A pre-registered gate of 1% per decoder family failed on the turned preview card, by less than the variation between positions; shipping the turn was the founder's override, recorded as one.

**The encoder refuses an outside address.** On the path that makes a code from an address, the encoder classifies the text first and refuses any web address whose host is not one of the issuer's own domains (or a developer's local and preview hosts), before anything is drawn; a text with no scheme at all, such as a bare gift code, is not an address and is drawn upright. The issuer's heart therefore never frames, through that path, a web address someone else chose. §12.7 says where this refusal does not reach.

**What a position is not.** A position is a **declaration** by the issuer's encoder, never a proof of who drew a code: the drawing recipe is public, and anyone can draw any position. *Inside a B-Watermark the position is constant*: every mark's code is a link-resolver address drawn by the issuer, so it always stands at the point, and the two outsider positions have no caller. The position carries no information a camera does not already read in the address. It is disclosed because it is part of the drawing, and claimed (§16, claim 4) only at the width the census left.

---

## 7 · Part four: B-Autograph℠, the signer's hand

**What it is.** In a person's own picture, the bottom lobe that holds a ™ in the issuer's codes holds instead the person's own hand, drawn with a finger or a mouse on a 100 × 60 pad. It is kept as **strokes**, a list of points, never as a picture of a hand: no timing and no pressure is read. It is fitted to the lobe's box and centered there, each stroke drawn through the midpoints of its points so that a finger's corners come out round, and it is clipped to its box so that no stroke can touch the code. Scanning is unmoved by it (3,930 → 3,929 readings with jsQR on the same drawings). At 22% of a 1,080-pixel picture's short side, the hand is about 50 pixels wide: a mark, not a signature block.

**Typed.** A person may type a name instead. It is drawn, as `@name`, in a single-stroke script face (the Hershey Script face, which is MIT-licensed in the package that carries it) as strokes on the same pad. Only Latin letters can be typed; a Khmer name is drawn by hand.

**Its ink.** By default, white or near-black, whichever reads better against the **median** pixel under the hand; or black, white, or any color the person picks. The first rule took the worst pixel; on line art it tied, and drew the hand white on white. Every automated check passed. It was found by looking.

**What it is not, said where it is drawn.** *Never a legal or bank signature*: anyone can copy what is in a picture, and a drawing does not show who someone is. The hand is kept on the signer's device under the account that drew it, and in the picture, and nowhere else unless they choose: a person may also keep it on their public name page, where a lookup interface returns it as strokes, and from where it can be removed with one press.

**Refused on a picture declared AI-made.** The signing form asks how a picture was made, in the vocabulary of the IPTC digital source type [17]. A hand is offered only when the answer is one of *digital creation*, *digital capture*, *human edits* or *composite*; never with *composite with synthetic elements* or *trained algorithmic media*. When a hand is wanted, the form starts with nothing chosen, and signing waits until the person chooses. The server refuses a hand the page declares under an AI source when it issues the mark's link, and again at the press if the declared source has changed. The server never sees pixels: it checks the declaration, not the picture. **This is a rule about what the signer says, never a property of the picture.** What it makes the hand mean is taken up in §11.3.

---

## 8 · Part five: B-Fingerprint℠, the picture's coarse fingerprint

### 8.1 What is written

```
   the host picture, as 6 × 6 cells                        the 96 bits in the top lobe
   (mean luminance of each cell)
   ┌────┬────┬────┬────┬────┬────┐        ┌──────┬────────────────────────┬──────────────────────┐
   │ 1  │ 0  │ 1  │ 1  │ 0  │ 0  │        │ kind │ 36 cells               │ 56 parity bits       │
   ├────┼────┼────┼────┼────┼────┤        │ 4    │ 1 = brighter than the  │ BCH over GF(2⁷),     │
   │ 1  │ 1  │ 0  │ 0  │ 0  │ 0  │        │      │ median of the cells    │ corrects up to 8     │
   ├────┼────┼────┼────┼────┼────┤        │ 0001 │ that are seen;         │ wrong bits of 96     │
   │ 0  │ 1  │ 1  │ 0  │ 0  │ 1  │        │ corn.│ 0 = not, or masked     │                      │
   ├────┼────┼────┼────┼────┼────┤        │ 0010 │                        │                      │
   │ 0  │ 0  │ 1  │ 1  │ 1  │ 0  │        │ strip│                        │                      │
   ├────┼────┼────┼────┼────┼────┤        └──────┴────────────────────────┴──────────────────────┘
   │ 1  │ 0  │ 0  │ 1  │ ▒▒ │ ▒▒ │        each bit drawn TWICE, in two dots of a checkerboard
   ├────┼────┼────┼────┼────┼────┤        nearest the code first: 192 dots in the top lobe
   │ 0  │ 1  │ 0  │ 0  │ ▒▒ │ ▒▒ │
   └────┴────┴────┴────┴────┴────┘
   ▒ under the heart (a corner mark): masked, never compared
```

The picture is divided into a 6 × 6 grid; each cell's mean luminance is compared with the median of the cells that are **seen**. The cells the heart itself will cover, with a 4% margin, are left out: they are written as zero and never compared, because the mark cannot fingerprint the pixels it replaces. For a strip, the fingerprint is of the picture above the strip, with nothing masked. Four bits say whether the mark is a corner or a strip (any other value is not the issuer's), 36 bits are the cells, and 56 bits are a BCH code over GF(2⁷), polynomial 137, the same code the watermark model uses for its own strongest schema, correcting up to 8 wrong bits of the 96. Each bit is drawn in two dots of a checkerboard, so that no two dots stand side by side. These dots cost the code a little: on the printed card, jsQR lost 15 readings of 1,080, so they are used in marks in pictures and never in the issuer's printed codes.

### 8.2 How it is read

The viewer's checker reads the code first and then has to find the dots, which stand a whole code's width away from the corners a decoder reports. A decoder's corners are about a pixel out; at that distance that is enough to misread the dots. So the checker lays the code's own 625 modules, whose values it now knows, over the photograph at both positions a mark can take, and moves the grid until it fits best; only then does it read each dot, from five points around its center, against a threshold set midway between the lobe's own light and dark, adding the two copies. Without that step, 159 of 194 posted corners read; with it, 194 of 194.

It then fingerprints the picture around the code the same way, with the heart's own cells left out, and compares. **Same** means the cells that differ are at most a fifth of those compared. The answer is worded, on the checker, exactly as follows:

> *Its B-Fingerprint℠ is of a picture that looks like this one.*
> *Its B-Fingerprint℠ is of a picture that looks different. The picture may have been cropped, or the heart copied onto another one.*

The checker runs in a worker on the viewer's device, with no download from anyone else. It never says *unchanged*: 36 coarse cells cannot see an edit.

### 8.3 What was measured

On 24 November 2026, on 97 local pictures with 194 corner marks posted at 70% white, through simulated re-encoding: the dots read whenever the code did, 194 of 194 at 1,080 px quality 80 and 182 of 182 at 720 px quality 70, and the right picture was never called different. A heart copied onto another, varied photograph was told apart **144 times of 152**, and in about **91%** of cases when the sample included look-alike screenshots of the same scene. The code beside the dots read 182 times against 187 without them at 720 px quality 70. The pictures were not chosen by an attacker, and the measuring script and its pictures are not committed with the code.

### 8.4 What it is for, and what it is not

It is **one-sided**. A heart copied unchanged onto a picture of a different rough layout reads *looks different*, and that is evidence. A heart that reads *looks like this one* is evidence of nothing, because the recipe is public and anyone can redraw the dots for any picture. It also fails on look-alikes: two pictures of the same scene share a layout. And it is **not secret**. It could not be, because the drawing and the reading run in the viewer's browser from a public recipe; a secret held on the issuer's server would only repeat what the mark's page already answers, and hidden data in people's pictures, once found, reads as tracking. So it is said in one line where a person chooses a code, and on the public description of the mark.

What it buys is narrow and real: the commonest forgery, pasting a real heart from one picture onto another, is caught offline, before anyone opens the page. The page still decides, because it shows the signed picture.

---

## 9 · The mark's page

A mark's code opens the link resolver, which opens the mark's page on the signing portal. Before the press, the page exists and says nothing. After it, the page shows the signed picture, made from the exact signed bytes; the record found in the public log by the picture's fingerprint; and an invitation to compare with the copy in hand. With no record in the log, the page says nothing about how the picture was made.

**The name comes after.** The signer may add their registered name to the page, worded *Page made by*, never *Signed by*, because a record never names its signer. It is asked only after the picture is saved, by its own press, and it can be taken off by another. Records are unlinkable by default, so the name is a choice, unticked.

**It asks for nothing.** The mark's page offers no log-in, so the sentence it carries, that it never asks for a password, a code or a payment, is true of everything on it. A page that offers a log-in could not say that, since a log-in can ask for a code.

---

## 10 · Two looks with no code

For an artist who wants only a hint, two looks carry no visible code:

- **The faint heart:** the emblem as a silhouette, its fill and edge at 10% white, with the signer's hand, when allowed, centered in the heart's bottom section, between the notch where the lobes meet and the bottom edge; the heart is sized to the hand (the hand 6% of the short side tall, the heart at most 42%).
- **B-Symbol℠:** a tiny emblem beside the signer's hand, raised (by default) or lowered, as a ™ stands beside a name. It is meant for artists who already sign their work.

**Neither carries an address, so each comes only with the mark nobody sees, which does.** Choosing either look turns the invisible mark on and does not let it be turned off; the mark is written into the same file and read back on the device before the press, and if it does not read back, the look is refused, with no option to continue without it. Because the B-Symbol stands beside a hand, it is never offered on a picture declared AI-made; a faint heart with no hand may stand on one.

These two looks amend the rule of 23 November 2026, under which the emblem never stood in a file's pixels without a code beside it. The amendment was made on 25 November on one condition: the emblem may stand without a code **only with the invisible mark in the same file, read back before the press**. §11.2 and §12.4 say what that condition does and does not hold.

---

## 11 · Checking a marked picture

### 11.1 What anyone can check, and whom they must ask

| To learn | You need | You ask |
|---|---|---|
| where a mark leads | any camera, or the open decoder of the invisible mark | nobody: the address is in the picture |
| whether the heart was drawn for this picture | the open fingerprint reader | nobody (and only the negative answer is evidence, §8.4) |
| whether this exact file was signed, and when | the picture as it was saved, carrying a receipt or its proof, and the open verifier | nobody but the log's published keys: the receipt or proof is in the file |
| the same, for a copy without its proof | the open verifier | the public log, read file by file |
| whether the signer withdrew it since | the same | the public log: no file can know its own future |
| what the signed picture looked like | the code | its page, while its maker keeps it |

**The receipt and the proof.** A picture saved with its mark may carry, in its own data, about 430 bytes of evidence of the record. At the moment of the press it can carry only a **receipt**: the record, signed by the log's record key the moment the record exists, which shows that the file was signed, and when. Once the log has included the record, the saved file can carry a **proof**: an inclusion proof against a signed, witnessed and timestamped checkpoint. The two are never one word: the open verifier answers a receipt with *not passed*, with the receipt beside it, so a caller that reads only the pass flag is never misled. Neither carries the passkey's own key, which stays the signer's choice to reveal. The evidence is carried so that the verifier can remove it and recover the signed bytes exactly. This is Certificate Transparency's promise-then-proof design applied to a picture, and nothing in it is claimed; it is not one of the mark's parts but a statement **signed by the log's operator** that travels **beside** the pixels, and a check of it trusts the operator's published record key. Most networks strip it when a picture is posted; the picture's marks are what is left, and they lead back.

### 11.2 What a mark shows, and what it cannot

**It shows a way back.** A camera or the open decoder recovers an address; the address opens a page that shows the signed picture and its record. That is all.

**The pixels hold no signature.** The visible code holds 60 bits of address and the lobe 36 cells of layout; a signature by the signer's key alone would need more than 500 bits. Nothing in the pixels can be verified by itself.

**A mark can be copied.** Both writers are public. A copied invisible number is caught by the page: the copy's record fingerprint is 36 away from the signed picture's where alike means within 8. A copied visible heart is caught offline by its fingerprint, when the layouts differ.

**A doctored copy is not caught by the marks.** A 30%-wide patch of the picture changed kept the invisible mark, and the record fingerprint moved only 5. The marks lead to the original; only comparing with it shows the edit. That is why a visible code is offered only where the page shows the picture.

**A mark can be removed.** Cropping 20% removes the invisible mark, and a corner mark is 22% of the short side; a strip is cut off in one stroke. The watermark model's own documentation says it *"can be removed via image processing"* and publishes code to do so [2]; regeneration attacks remove pixel-level watermarks in general [24]. A mark that is gone leads nowhere, and its absence means nothing (§11.3).

**The code-less looks hold the invisible mark only at the press.** The read-back condition binds the file that was signed. A copy that has lost the invisible mark to cropping, resizing below 160 px, or a removal tool keeps a faint heart or a B-Symbol that now leads nowhere. A faint emblem is not more robust than the address only because it is fainter; whether it outlives the invisible mark in circulation has not been measured.

**The name is the signer's.** A drawn or typed hand in the pixels is the signer's own, and nobody checks it: a typed `@name` is free text, drawn as typed, not compared with any registered handle, and fixed in the pixels before the press. Only the registered name a signer adds to the mark's page afterward (§9) is checked, and that one can be taken off.

### 11.3 What a viewer can still infer, and why it is said here

The issuer asserts nothing about a picture in its pixels. A viewer who knows the published rules can still infer three things, and they are stated here rather than left to be discovered.

- **A hand implies a declaration.** Because a hand is refused on a picture declared AI-made, a hand in a marked picture implies that its signer *declared* it was not AI-made. It is the signer's declaration, unchecked; the issuer never looks at pixels. A viewer should read a hand as *someone said so*, never as *it is so*.
- **The emblem is the issuer's emblem.** In the issuer's own published reading, a static emblem in an entity context means that an individuated, anchored entity is present, and it asserts nothing about humanness [23]. Whether that reading applies to an emblem inside a picture is not settled. The institution's own media guide had warned that a bare emblem in pixels *"would read as real"*; the rule that replaced the ban on a bare emblem answers the address half of that worry, not the reading half. Whether viewers read a faint heart on a picture as *this is real* is an empirical question this paper does not answer.
- **An absence becomes legible.** Once it is public that a hand never appears on a picture declared AI-made, a faint heart without a hand could be read as *maybe AI-made*. No surface renders that absence, and the mark is off by default, so an unmarked picture says nothing. Whether publishing the rule is itself a rendering is an open question for the institution (§12.10).

---

## 12 · What an adversarial review found

Before this paper was drafted, a separate review with no write access attacked the authors' own description, *"a mark that leads back and claims nothing"*. It found nothing that kills the mechanism and twelve places where the description did not hold as written. Each finding was re-read in the code, or on its source page, before it reached this text. The paper above already carries the narrowed form; this section records what changed.

### 12.1 The receipt is the operator's statement, not a part of the mark

The first description listed the saved file's receipt as one of the mark's parts. The issuer's own definition of the mark has five parts and two looks, and the receipt is not among them; and a receipt is a signed statement, which is a claim, not an address. It is described in §11.1 as what it is: a statement by the log's operator, beside the pixels, checked against the operator's published key.

### 12.2 The hand carries the signer's declaration

The AI-source gate makes a hand imply a declaration (§11.3). The narrowed thesis is that the **issuer** claims nothing in the pixels; the signer's hand is the signer's, and it carries what the signer said. The issuer's public description of the mark states the gate in the plain words *"Never on a picture made with AI"*, which is stronger than the rule, which governs only the declaration; the difference is recorded here.

### 12.3 The faint heart on an AI-made picture

A faint heart with no hand may stand on a picture declared AI-made, by the founder's ruling of 25 November 2026. The review set this against the institution's own guide for AI-made media, which warns that a bare emblem in the pixels *"would read as real"*, and against the published static-emblem reading [23]. The paper does not resolve that tension; it reports it (§11.3).

### 12.4 The read-back holds at the press, not on copies

The first description called the code-less looks' condition *a property of the file*. It is a property of the **signed** file only; a copy that loses the invisible mark keeps the visible emblem (§11.2).

### 12.5 The B-Symbol stands where the ™ used to

The ™ was taken out of people's pictures because, there, it could read as the issuer's claim on their work. The B-Symbol puts a small emblem back beside the person's name *"as a ™ stands beside a name"*. Whether it reads as such a claim is a question for counsel, already open, and is recorded as a limit (§18).

### 12.6 A typed name is free text

The first description called the typed name the signer's `@name`. It is whatever the signer types, drawn with an `@` in front, unchecked, and fixed before the press (§11.2). The rule that a registered name is added only after the press, and can be taken off, holds for the page and not for the pixels.

### 12.7 The quarter-turn carries nothing inside a mark, and the refusal holds on one path

Inside a mark the position is constant (§6.3). And the refusal of an outside address holds only on the path that makes the code from the address it checks, and nothing stops anyone drawing a heart around any code with their own tools. **A heart around a code proves nothing; the address a camera shows is the only thing to read.** An earlier internal description of this refusal as a property of every drawing was wrong in that respect.

### 12.8 The fingerprint is one-sided

Only *looks different* is evidence (§8.4). The issuer's public description printed *144 times of 152* without the look-alike figure; both numbers are given in §8.3.

### 12.9 The guards against fake codes hold inside the issuer's scanner

A fake page cannot obtain a press, because passkeys are bound to the signing service's origin; a genuine link can lead only to an issuer address; the issuer's own payment scanner refuses any other host; and look-alike domains are watched weekly. None of that protects a viewer whose phone's photo library opens a code by itself. Consumer-protection guidance is to be wary of scanning unexpected codes, and a mark that teaches people to scan codes in pictures works against it. This is a limit, recorded in §18.

### 12.10 The published rule may render an absence

See §11.3. Open.

### 12.11 The claims fit the coded form only

The survivor sentence needs a code, a turn and spare modules; it does not describe the faint heart or the B-Symbol. The claims in §16 are scoped to the coded form, with the code-less looks as a dependent.

### 12.12 "Made on the device" needs a scope

The marks are made on the device. The picture is not kept there: the portal makes the page's picture from the signed bytes (§3).

### 12.13 What survived

*An opt-in mark the signer's own device writes, in which the issuer asserts nothing about the picture: its coded form carries a 12-character unlisted address, invisibly and optionally as a code whose spare dots hold a public, coarse, one-sided fingerprint of the picture's layout, and whose other lobe holds the signer's own unchecked hand; the turn is constant inside the mark, and the receipt is a separate statement by the log's operator that travels beside the pixels.*

---

## 13 · Remove the enforcer: which guards are properties

A guard that needs someone to enforce it at the moment it is tested is a rule; one that holds with nobody present is a property of the object. Each guard here, with the enforcer removed:

| Guard | With nobody enforcing | Kind |
|---|---|---|
| the press covers the marked file | the record's hash is of the marked bytes; a mark added later is a different file | **property** |
| the address is unlisted | twelve characters are not in the resolver's listed log | **property** (of the resolver's design) |
| a read number is ours only if its last bit fits, its link exists and its page names the file | the reader checks all three | **property** of the open reader; a different reader may skip it |
| the fingerprint's footprint is masked | the cells under the heart are written as zero and never compared | **property** |
| a copied heart on a different layout reads *looks different* | arithmetic on the picture, offline | **property**, one-sided |
| an outside address is refused | holds on the encoding path only (§12.7) | **property of one path**; elsewhere nothing |
| the code-less looks come only with the invisible mark | the portal refuses the look at the press | **rule**, enforced by the portal; holds for the signed file only |
| no hand on a picture declared AI-made | the device, the server and the press check the declaration | **rule** about a declaration; the pixels are never checked |
| the hand is never a legal signature | said where it is drawn | **rule** (a statement) |
| the pixels make no claim | no word is drawn; but see §11.3 | **property** of the drawing; the inferences in §11.3 are not removed by it |
| the page asks for nothing | the page has no log-in to ask with | **property** |

Most of what the mark promises is a property. The two most consequential guards, the AI gate and the read-back, are rules, and both are honest only about what they govern.

---

## 14 · Variants disclosed

- **Video.** A fresh invisible mark on every frame and a card at the end with the visible code. Measured on one 4-second pan of 40 frames: the mark read on 39 at a constant rate factor of 23, 33 at 28, 19 at 480 px and 7 at the worst; unmarked frames 0 of 200. One mark held for a second read on 10 of 40, so there is no shortcut. Used on the institution's own films only, on a desktop machine, because the writer takes between one and three seconds a frame (measured 1.2 and 2.5 in two builds); not offered to the public.
- **The issuer's own codes.** The same emblem-shaped code in every position, the ™ in the bottom lobe, plain decorative dots in the top lobe, printed on stickers and cards. The four positions apply to them; the fingerprint and the hand never do.
- **A hand kept on a name page.** The strokes may be stored on a person's public name page and returned by a lookup interface, shown as the recorded voice is, never compared by a machine.
- **The page's registered name.** As §9.
- **Marking a kept picture later.** As §4: always a new record and a new press.
- **Other emblems.** Nothing in the mechanism depends on the heart: any emblem with a free region beside its code, and any open watermark model with enough capacity for the address, would serve.

---

## 15 · What is disclosed and what is withheld

**Disclosed:** the whole mechanism as built. Its drawing code and its fingerprint's reader are already published as open files of the institution's brand layer, with a public page that draws and reads the mark in the visitor's own browser, and the verifier of the receipt and proof is a published open package. Nothing of the mark is withheld, because nothing of it is unbuilt: the test this corpus applies, *publish the claim and withhold the specification where unbuilt and unscheduled*, finds nothing to withhold.

**Withheld:** the interface through which an outsider would have a code drawn at the notch or non-standard position, which does not exist; and a public form of the video variant, which is not scheduled. Their specifications will be published if they are built.

---

## 16 · Enumerated claims

These are the censuses' survivors and nothing wider. Every claim concerns a mark made at a signer's choice in a picture of their own, in which no word of the issuer's is drawn.

**1.** A method of marking a picture in which, before the picture is signed, a signer's device obtains an address from a link resolver; draws a QR code of that address inside an emblem of the issuer's that has two free regions outside the code's quiet zone; writes, in decorative modules in one free region, an error-corrected coarse fingerprint of the host picture computed with the cells the emblem will occupy left out; draws in the other free region, in place of the sign the issuer's own codes carry there, the signer's own hand captured as strokes; turns the whole code by the quarter-turn that the encoder assigns to the class of address it encodes; composites the emblem into the picture; reads the code and the fingerprint back on the device; and only then hashes and signs the marked picture, so that the signature covers the mark.

**2.** A method of telling whether a visible code-bearing emblem was drawn for the picture it stands in, comprising: decorative modules beside a standard two-dimensional code, in the same drawing, carrying a fingerprint of the host picture as cells each brighter or darker than the median of the cells compared, protected by an error-correcting code and written twice; the cells under the emblem's own footprint excluded at writing and at reading; and a reader that registers its grid against the code's own known modules before reading the dots, fingerprints the picture around the emblem the same way, and reports only *looks like the picture it was drawn for* or *looks different*, never *unchanged*, with no network.

**3.** A mark in which the region of an issuer's emblem that, in the issuer's own codes, holds the issuer's sign, holds instead a person's own hand, captured as strokes on a pad, fitted and centered in that region and clipped so that it cannot touch the code, stated where it is drawn to be no legal or bank signature.

**4.** An encoder that, when making a two-dimensional code inside an issuer's emblem, sets the whole code's quarter-turn from the class of the address it encodes, crossed with whether the issuer or an outsider through the issuer's interface asked for it, and refuses, before drawing, any web address whose host is not one of the issuer's domains; the position being a declaration of the encoder and never a proof of who drew a code.

**5.** The method of claim 1, in which the code stands on a strip added below the picture, made of the picture's own bottom edge mirrored and blurred into soft color, carrying the code, its printed address and a line of words, the words taking whichever ink has the higher contrast on the worst pixel under them.

**6.** The method of claim 1, in which the issuer's emblem may instead be drawn without any code, as a low-opacity silhouette or as a small emblem beside the signer's hand, only when an invisible watermark carrying the same address is written into the same file and read back on the device before the signature, the look being refused otherwise.

**7.** The method of claim 1 or 3, in which the hand is refused when the signer's declared digital source type for the picture is AI-generated, on the device, at the issuance of the address and again at the signature, the source being chosen actively, with nothing pre-filled, before a hand can be added.

**8.** The method of claim 1, in which the address is long enough to be excluded from the link resolver's public listing, so that marked pictures cannot be enumerated from the resolver's log.

**9.** The method of claim 1, in which the mark's page shows a picture made by the issuer from the exact signed bytes, offers no log-in, and adds the signer's registered name only after the signature, by a separate press that a further press can undo.

---

## 17 · Predictions

None are registered with this paper. Its empirical statements are measurements already made, each with its instrument stated. What is owed is measurement, listed in §18, not prediction.

---

## 18 · Honest limits

- **No phone camera, no real network, no print.** Every robustness figure came from software decoders and simulated resizing and re-encoding. A real social network's pipeline, a phone camera pointed at a screen, and a printed picture have not been measured.
- **The fingerprint's sample was not adversarial.** 97 local pictures; its 144 of 152 falls to about 91% with look-alikes; an attacker able to nudge a few cells across the median has not been modeled. Its measuring script is not committed.
- **The visible cost on flat and line art** is real and was shown to the founder, not to a working artist.
- **The mark can be removed and the code can be faked.** §11.2 and §12.7. A mark is a convenience for honest circulation, never a defense against a determined forger, and never a deepfake defense.
- **The hand carries a declaration nobody checks**, and a typed name is free text (§11.2, §11.3).
- **The emblem in pixels may be read as a claim** whatever the rules say; not measured (§11.3).
- **The guards against fake codes stop at the issuer's own scanner** (§12.9).
- **The receipt and proof are stripped by most networks**, and when present they trust the log operator's published key. As of this writing the receipt's path has been run end to end on a test log and key; whether a production marked picture has yet carried a receipt is not reported here.
- **The names are not cleared.** *B-Watermark*, *B-Autograph*, *B-Fingerprint* and *B-Symbol* have had no trademark search, and whether a small emblem beside a person's name reads as the issuer's claim on their work is open with counsel.
- **The Khmer is unreviewed**, so the strip's words are English only.
- **The censuses are weak where it matters.** The surviving remainders, (c), (d) and (e), sit in the field where Chinese and Japanese sources are densest, and those were searched through a general index, not native databases. A null is the ordinary result for a narrow conjunct.

---

## 19 · Lineage and corpus cross-references

The mark rides on the signing mechanism of *B-Links* [20], uses the likely-match wording of *Every Lent Face Signed This Cut* [21], the open and filled code styles of *The Ticket and the Tag* [22], and the two proof-states of *Brand Identity as Architecture* [23]. Its stance, an address and never a claim, is the same one *The Press Travels With the Message* takes for signed mail: a signature shows what was pressed, on what, and whose key, and a reader is given something to hold a name to, not proof of a person [25].

- **Internet Archive** (the site): https://web.archive.org/web/*/https://thonly.org/research/an-address-in-the-picture
- **Software Heritage** (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications

---

## Coda

*Flourish — recognition, not claim.* In Khmer the word for a signature is ហត្ថលេខា, from the Pāli *hattha*, a hand, and *lekhā*, a line: a line drawn by a hand. That is all a B-Autograph is, and the reason the Khmer copy of the mark keeps its Latin name is that the Khmer word for it already means *signature*, which it is not. The mark around it is an address. What a viewer is owed is the way back to the page, and the honesty to say that the way back is all the mark is. **Delete this coda and every claim above stands unchanged.**

---

## Terms

| Name used here | Standard term |
|---|---|
| B-Watermark℠ | an opt-in composite image mark: an invisible watermark plus an optional visible code, both carrying one address |
| the mark nobody sees | an invisible image watermark (here, TrustMark Q) carrying a 60-bit identifier |
| B-QR | a QR code drawn inside a heart-shaped emblem (unmarked name) |
| B-Link | an address issued by a link resolver |
| the four positions | the orientation of a QR code's finder patterns (which corner holds the middle marker) |
| B-Fingerprint℠ | an error-corrected coarse perceptual fingerprint of the host image, carried in decorative modules |
| B-Autograph℠ | a handwritten mark captured as stroke data |
| B-Symbol℠ | a small brand emblem beside a handwritten mark |
| the faint heart | a low-opacity brand silhouette |
| press | a user-verified WebAuthn (passkey) assertion |
| record, log | an entry in a tiled, checkpointed append-only transparency log |
| receipt | a log's signed promise of inclusion (as a signed certificate timestamp) |
| proof | a Merkle inclusion proof against a signed, witnessed checkpoint |
| B-Origin℠ | the institution's file-signing service and portal |

---

## Author Contributions and AI Disclosure

Thon Ly asked whether signed pictures should carry the institution's emblem and accepted the answer that they should not; proposed in its place an optional visible code pointing to the record; shaped its corner and strip forms (the corner's transparent ground, the strip's color matched to the picture, its words first on the right and then on the side the signer chooses); proposed turning the code so that its middle marker stands at the emblem's point, and the four positions as a declaration of address class and drawer, and their names; proposed the ™ in the bottom lobe and that it shows which way is up; proposed the artist's own hand in the code, its place in the bottom lobe of the open code, drawing it with a finger or a mouse, keeping it on a person's name page, a typed name in a script face, its ink and its placement; left the top lobe open for a use, approved its dots, and asked whether they should be secret; named B-Watermark, B-Autograph, B-Fingerprint and B-Symbol; asked whether a third party could verify a marked picture without the issuer's server; proposed the faint heart and the small emblem beside a hand, and that no hand appears on a picture declared AI-made; and ruled on every design choice recorded here. Miss Aquarius℠ — the name under which this corpus discloses its AI collaboration — proposed keeping the emblem out of the pixels unless a code is beside it, the invisible mark as the carrier of the address, the order in which the link, the marks, the read-back and the press are made, the twelve-character unlisted address, the condition that a code appears only where the page shows the signed picture, the fingerprint's design (the 6 × 6 grid, the masked footprint, the error correction, the grid registered against the code's own modules) and its one-sided wording, the receipt and the proof as two states never one word, and the read-back condition on the code-less looks; built and measured the mechanism with every number stated here; ran both censuses through research agents whose candidates were re-read before they reached this text; commissioned the adversarial review in §12 from a separate instance with no write access; and drafted this paper.

## Trademark Notice

**B-Watermark**, **B-Autograph**, **B-Fingerprint** and **B-Symbol** name the institution's implementation; the mechanism is dedicated to the public domain and may be implemented under any name. HeartBank®, Miss Aquarius℠, B-Origin℠, B-Watermark℠, B-Autograph℠, B-Fingerprint℠, B-Symbol℠ and B-Emblem™ are marks of their respective holders; *B-QR* and *B-Link* are unmarked names. No mark is licensed by this publication. Product and company names of third parties are used only to identify prior art.

## Citations

1. Coalition for Content Provenance and Authenticity. *C2PA User Experience Guidance for Implementers*, version 2.2, §4.2 *L1 Indicators*. spec.c2pa.org (read 25 November 2026).
2. Coalition for Content Provenance and Authenticity. *Technical Specification* (soft bindings) and *Soft Binding API*; Content Authenticity Initiative, *Durable Content Credentials* and the *TrustMark FAQ* (opensource.contentauthenticity.org; read 25 November 2026); Bui, T., Agarwal, S., Collomosse, J. *TrustMark: Universal Watermarking for Arbitrary Resolution Images*. arXiv:2311.18297, 30 November 2023.
3. United States Patents 7,822,969 and 8,103,542 (Digimarc).
4. United States Patent 9,621,565.
5. United States Patent 6,751,352 (Hewlett-Packard).
6. DENSO WAVE. *Frame QR*. qrcode.com (read 25 November 2026).
7. United States Patent 8,690,049 B2 (Digitalzone Co., Ltd.), *Method for generating an image file for forgery verification and a method for forgery verification of an image file*, priority 22 May 2009.
8. United States Patent 8,130,811 B2 (Digimarc Corp.), *Assessing quality of service using digital watermark information*, priority 11 September 2000; description, *Semi-Fragile Watermarks*.
9. *MetaSeal: Defending Against Image Attribution Forgery Through Content-Dependent Cryptographic Watermarks*. arXiv:2509.10766, 13 September 2025 (abstract read).
10. United States Patent Application Publication 2004/0174577 A1 (Silverbrook Research), *Symmetric tags*, priority 4 March 2003.
11. United States Patent 10,394,419 B2 (GSPI BV), *Device, a method and a server for retrieving information using a machine readable image*, priority 1 December 2012.
12. United States Patent 11,734,532, *Two-dimensional bar codes that are both intensity-modulated and orientation-modulated*.
13. Laurie, B., Langley, A., Kasper, E. *Certificate Transparency*. RFC 6962, June 2013, §3.3; and RFC 9162, December 2021. Sigstore, protobuf specifications for Rekor bundles (inclusion promise and inclusion proof).
14. United States Patent 9,760,818 B2 (Hewlett Packard), *Machine-readable watermarks and barcodes in images*, priority 29 April 2014.
15. *Signpost Watermarking: Joint Optimization for Visual Watermark Coexistence*. arXiv:2608.10091, 10 August 2026 (abstract read).
16. *Dual Watermarking Scheme with Encryption*. arXiv:1002.2414, 11 February 2010 (abstract read).
17. IPTC. *Digital Source Type* vocabulary and guidance for AI-generated media; Coalition for Content Provenance and Authenticity, *Use of Content Credentials to Identify Synthetic and Non-Synthetic Content*, July 2026.
18. United States Patent 11,899,927 B2 (Adobe Inc.), *Simulated handwriting image generator*, priority 3 December 2019 (description, general overview).
19. Evil Mad Scientist Laboratories. *Hershey Text: An Inkscape extension for engraving fonts*, 10 February 2011 (the *Script 1-stroke* face).
20. Ly, T., Miss Aquarius℠. *B-Links: Proof-of-Humanity-Signed Shareable Provenance with an Embedded Gratitude Affordance*, §4.1. This corpus.
21. Ly, T., Miss Aquarius℠. *Every Lent Face Signed This Cut*, §12.3, Variant C. This corpus.
22. Ly, T., Miss Aquarius℠. *The Ticket and the Tag*. This corpus.
23. Ly, T., Miss Aquarius℠. *Brand Identity as Architecture*, §5.5. This corpus.
24. Zhao, X. et al. *Invisible Image Watermarks Are Provably Removable Using Generative AI*. arXiv:2306.01953, 2 June 2023 (NeurIPS 2024).
25. Ly, T., Miss Aquarius℠. *The Press Travels With the Message*. This corpus.
26. United States Patent 9,111,164 B1, *Custom functional patterns for optical barcodes*. Cited for what its description discloses only.
