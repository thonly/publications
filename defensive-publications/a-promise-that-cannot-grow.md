---
title: "A Bilateral Promise Ledger for Peer-to-Peer Credit and Customer Prepayment in Which No Promise Can Grow — Non-Accruing Obligations, a Size-Blind Reputation Display, and Debt Forgiveness as the Only Crossing into a Gift Ledger"
subtitle: "A Promise That Cannot Grow: the B-Promise℠ promise ledger, its promise ring, and the two-pass census that decided what it may claim"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-b
program: open
status: draft
date: 2026-09-28
license: CC0-1.0
slug: a-promise-that-cannot-grow
venue: thonly.org/research/a-promise-that-cannot-grow
canonical_url: https://thonly.org/research/a-promise-that-cannot-grow
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claim* and withholds the *build specification* (§14 says exactly what is withheld and why). Almost every leg of the mechanism was already public before this paper, and §2 reports the two prior-art passes that established it, including the conjuncts they killed. What is claimed in §15 is a composition and three narrow sub-rules, and nothing wider.
>
> Companion works: *The Zero-Point Game℠* (the signed-balance ledger of which the promise ledger is a third instance, §6.4) · *The Currency That Cannot Be Spent Alone* (the institution's gift-side redemption rules) · *The B-Tag and the Post-Payment Economy* (the gift-side scan this paper must not collide with) · *Provenance-Carrying Retrieval* and *The Assembly That Holds the Brake* (signed tree heads compared among independent observers) · *HeartBank's Position on Community-Currency Design*.

---

## Preamble

*Grounding — canon, cited.* The Aṅguttara Nikāya records a short teaching to the householder Anāthapiṇḍika on four kinds of happiness available to a lay person: the happiness of ownership, of using wealth, of debtlessness, and of blamelessness (AN 4.62, the *Ānaṇya Sutta*; the Pāli term is *ānaṇya-sukha*). Of the third it says only this: *"It's when a gentleman owes no debt, large or small, to anyone. When he reflects on this, he's filled with pleasure and happiness."* The discourse does not condemn borrowing. It names a happiness that belongs to having repaid, and it places that happiness below blamelessness, which it says the others are not worth a sixteenth part of.

*Lens — the institution's reading, not canon.* This paper builds a ledger whose only purpose is to let two people who already trust each other a little make a promise that can be kept, and to let the keeping be seen. Repaying, in the institution's reading, is truthfulness (*sacca*) and the happiness AN 4.62 names; it is not generosity (*dāna*), and the mechanism below is built so that repayment can never be mistaken for a gift. The one act in this ledger the institution reads as a gift is a creditor's free release of what is owed. **That reading is ours.** A search of the Pāli canon for the second pass of this paper's census did not find forgiving a debt described as *dāna*, and we do not claim the canon says it.

*Cross-tradition neighbour [X].* The nearest canonical statement of that reading is not Buddhist. The Qur'an, 2:280: *"If it is difficult for someone to repay a debt, postpone it until a time of ease. And if you waive it as an act of charity, it will be better for you, if only you knew"* (trans. Mustafa Khattab). And the sharpest warning about a calendar of forgiveness is in the Hebrew Bible and the Mishnah (§7.5).

**Delete this preamble and every claim below stands unchanged.** The mechanism does not depend on any of these texts. They are recorded because they describe, more precisely than we could, the two things the mechanism keeps apart.

## Prior-Art and Non-Assertion Statement

This document is published to establish prior art and to place the described mechanism irrevocably in the public domain under CC0 1.0 Universal.

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. It extends to every mechanism disclosed in this paper, in any combination, and to every implementation of it. Trademark rights on specific marks (**B-Promise℠**, **HeartBank®**, **Miss Aquarius℠**, **Zero-Point Game℠**) are separately reserved; the dedication concerns the mechanism, not the marks.

**What is claimed as contribution is narrow, and it is stated first because two census passes found almost all of the mechanism already public.** A bilateral IOU ledger signed by both parties is public (a Korean product did it in 2017). A fixed markup that is never increased is classical law. One primitive serving both prepayment for goods and lending is public (an academic paper of March 2026). Debt forgiveness as charity is scripture. Static versus dynamic payment codes are a payments standard. Social key recovery by guardians, with a cancellable delay, is public, and at least one live patent discloses it. Anchoring an append-only transparency log to Bitcoin is an Internet-Draft. **None of those legs is claimed.** §2 reports both passes: aperture, dates, every conjunct killed or narrowed with the prior art cited, what was not run, and the survivor. §15 enumerates only the survivors.

**Live patents.** The census recorded several granted patents in the neighbourhood, shown as active in Google Patents' status fields on the census date (not a legal status determination). §2.5 records what each **discloses**. We make no statement about the scope of any patent's claims or whether any design falls within them, and a publication dated after a patent's priority date does nothing to that patent.

**Date and evidence.** First published 28 September 2026. The text is committed to the public GitHub mirror of the corpus, and the corpus's standing chain anchors each revision to the Bitcoin blockchain through OpenTimestamps and signs it under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified; a Zenodo version and the served index at corpus.333.eco carry its digest once deposited. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality or the validity of any claim. **Whether the composition claimed in §15 is non-obvious is an examiner's determination this publication exists to inform.** A defensive publication is not examined before it is published; the census in §2 is the only examination it has had.

---

## Abstract

We disclose a **bilateral promise ledger for peer-to-peer credit and customer prepayment** in which no promise can grow on its own: a premium, if any, is fixed when the promise is made; nothing accrues or compounds afterwards; there is no late penalty; and a promise changes only by an entry that both parties sign. The ledger is therefore **non-accruing but not interest-free** — a fixed premium is agreed at origination and is shown on the record, and at short terms it can be very large (§4.3). The ledger is kept on the two parties' phones, is signed by both, and is **non-transferable**: a promise can never be sold or assigned. Its coined name is **B-Promise℠**.

The mechanism serves two ordinary deals with one record. In **customer prepayment**, a customer pays a vendor $9 in cash now and the vendor promises $10 of goods; the customer is the lender and is repaid in kind, and the discount comes out of the vendor's retail margin. In **peer-to-peer lending**, a lender gives $9 now and the borrower promises $10 by a deadline the borrower proposes. Value moves first, face to face; **the promise is the receipt**.

Conduct is shown by a **reputation display that takes no amount argument**: one equal-width segment for each open promise the person owes, a gap where a promise is overdue, a segment that dissolves when a promise is kept, shown only where a new promise is being made and never on a profile. It has no colour. A single line of text under it carries exact counts, the age of the history, a coarse band of the total the person owes, and whether the new promise is larger than any they have kept. The one event that crosses from this exchange ledger into the separate gift ledger the institution already runs is a **creditor's free release of the whole remaining balance** (debt forgiveness); repayment never crosses.

Three narrow sub-rules complete the claim: a printed code can never open an obligation; no one who has an open promise with a person may vouch for that person's new signing key; and the proof that an entry is included in the public log travels inside the co-signed promise code. The history is committed as salted per-person hash chains to an append-only log anchored daily to Bitcoin and to RFC 3161 authorities. We report two prior-art passes that killed or narrowed every conjunct at mechanism width, claim only the composition that survived, state the harms the mechanism does **not** prevent — above all that a person's total debt can still grow by rollover — and state in advance a test of whether an annual invitation to forgive debts freezes December lending.

---

## 1 · The problem, and what this paper is for

The institution that publishes this paper builds reciprocity infrastructure: a ledger of gratitude that sits above regulated payment rails and never becomes a bank. Its gift side is in production; this paper describes its **exchange side**, the part that records what people owe each other when they are not giving but dealing. The two sides are built to stay apart, and the paper exists largely to say where the one door between them is.

The setting is Cambodia, the institution's beachhead, and it shapes every rule below. Most households shop daily and locally: few have refrigerators, many travel by motorbike within a village, food is the commonest vendor type, and vendors restock every day to keep produce fresh. Two informal credit practices follow directly. Regular customers buy ahead from the stalls they use, and vendors borrow small sums from each other to restock. Both run on paper notebooks and memory. Both are ordinary; neither needs to be invented.

What the institution adds is narrow, and it is a response to a specific harm. Formal microcredit in Cambodia has been documented as a debt trap. Human Rights Watch's report *Debt Traps* (24 September 2025) documents coerced land sales, over-indebtedness and debt-driven suicides among borrowers in the northeastern provinces, and lenders accepting informal land documents as collateral. A LICADHO study reported by Voice of America in 2023 found that the share of microloans taken to repay other loans rose from 3.45% in 2012 to 34.8% in 2022. The National Bank of Cambodia has capped microfinance interest at 18% a year since 2017. The harms are compounding, penalties, collateral, and loans taken to repay loans. **This paper's mechanism removes the first three from each individual promise and does not remove the fourth**, and §17 says so first.

The design question, stated as a negative:

> **No promise on this ledger can become larger than the two parties agreed when they made it, unless both of them sign again.**

Everything below either serves that sentence or states where it stops.

**Why it is the institution's problem and not only a product.** The institution's gift ledger (the Zero-Point Game℠ and its public display, the B-Aura) is designed as the structural inverse of a credit score: a waveform that is forgiven and re-earned, not a scalar that persists and compounds. A credit instrument built by the same institution is a direct threat to that inversion. If repayment could raise a person's gift-side display, money could buy the appearance of kindness (borrow and repay), lenders would acquire a stake in the annual forgiveness that resets the gift ledger, and a person too poor to borrow would appear less kind. The founder asked whether creditworthiness and kindness should share one display; the ruling was **no**, and this paper is in large part the specification of that no (§6.4, §7).

**What this paper does not do.** It does not describe a bank, a lender, or a custodian: the ledger records promises between people and moves no money; value moves in cash, face to face, and in a later phase through wallets the institution never holds keys to. It does not claim to make credit safe (§11). It does not claim usury protection (§4.3). The institution's autonomous agent has no role in the mechanism as disclosed; whether it acquires one is not decided here.

---

## 2 · Background and prior art: the census

The claims in §15 were drafted from the survivors of a prior-art census, not revised after one. The census ran as two passes on 28 September 2026. **Each pass's conjuncts, predictions, known-prior-art control and declared aperture were committed and pushed to a public repository before its first query ran.** Both pre-registrations are published verbatim and never edited:

> **Public pre-registration (pass 1):** `74b8a87` in `thonly/publications`, timestamps/census/b-promise-prereg.md, pushed 2026-09-28 13:05 PDT — publicly inspectable, before the first query.
>
> **Public pre-registration (pass 2):** `945da0d` in `thonly/publications`, timestamps/census/b-promise-pass2-prereg.md, pushed 2026-09-28 13:46 PDT.

Private copies were pushed the same minutes (`bad927c`, `4458912`). Anyone can check the ordering of the public commits against the host's push record.

### 2.1 · The conjuncts, as pre-registered

The claim was split, before searching, into seven conjuncts:

| | Conjunct |
|---|---|
| (a) | one primitive — value now for a fixed larger claim later — recorded as a bilateral, both-signed promise ledger serving both customer prepayment to a vendor and person-to-person lending |
| (b) | a promise that can never grow on its own: premium fixed at origination, no accrual, no compounding, no late penalty, the balance changes only by an entry both parties sign |
| (c) | a conduct display with no amount input: one equal-width segment per open promise the person owes, transparent when overdue, dissolving when kept, saturating, size-blind, shown only where a promise is being made, with viewer-relative trust computed on the viewer's device |
| (d) | the forgiveness crossing: a creditor's free release of a claim is the only event that passes from the exchange ledger into a separate gift ledger (repayment never does) |
| (e) | printed or static codes always resolve to the gift side; an obligation opens only from a live on-screen code carrying its terms, binding nothing until both parties sign |
| (f) | identity recovery by face-to-face vouching of counterparties with settled promises (or one pre-named guardian), a cancellable waiting period, no voucher who has an open promise with the user, debts carrying over |
| (g) | history committed as salted per-person hash chains to a Certificate-Transparency-shaped append-only log anchored to Bitcoin (OpenTimestamps) and RFC 3161 authorities, with gossiped tree heads and inclusion proofs inside a self-contained signed code |

### 2.2 · Pass 1: aperture, control, verdicts

**Aperture, declared before searching:** the commercial web (credit, buy-now-pay-later, IOU and merchant-ledger apps); non-commercial sources (rotating credit, informal village-shop credit, Islamic interest-free finance, jubilee and debt-forgiveness charities, community currencies); Google Patents full text including published applications, with a citation walk from the nearest hit; academic indexes; standards (IETF RFC 6962 and 9162, W3C WebAuthn, EMVCo QR); the Technical Disclosure Commons. English searched; three Khmer web queries attempted; Chinese, Japanese and Korean through patent translations only. **68 queries**, run by three research agents, logged in the institution's session record; the main session re-verified every row that reached the result.

**Control.** The pass had to find the ledger half of (a) at mechanism width — Ryan Fugger's RipplePay (a peer-to-peer IOU network on trust lines, 2004–05) and the digital *khata* merchant-credit apps of India (OkCredit, 2017; Khatabook, 2018). It found all three, so the instrument could see prior art that was there.

| Conjunct | Predicted | Found (earliest first) | Verdict |
|---|---|---|---|
| (a) | kills or narrows | the prepayment half: *bay' salam* in Islamic commercial law (the full price paid now for goods delivered later, customarily below the spot price) and bonus store credit; the lending half: IOU apps approved by both parties (DueTrace, press release 30 August 2026; two others unverified), Trustlines; Sarafu community vouchers | **narrowed** at mechanism; both halves as one primitive not found *in this pass* (killed in pass 2) |
| (b) | narrows | *murabaha* (a fixed markup never increased, though late charges paid to charity are permitted) · *qard hasan* (a benevolent loan with no premium) · Sardex (a zero-interest business mutual-credit circuit, Sardinia, 2009) · DueTrace (a balance that moves only on an approved entry) | **narrowed**; a fixed premium with no late penalty and co-signed-only change, together, not found |
| (c) | narrows | credit-bureau payment-history grids (per-month on-time and late marks) · EigenTrust (Kamvar, Schlosser and Garcia-Molina, WWW 2003) and Advogato's viewer-seeded, Sybil-resistant local trust metric · a live PayPal patent disclosing a trust score from the timing of peer-to-peer transfers and loan repayments with an interactive display (§2.5) · a published application disclosing a circular credibility graphic (unverified) | **narrowed**; a display with no amount argument, drawn from promises owed only, shown only at the moment of a new promise, not found (HCI literature not run in this pass) |
| (d) | narrows | Qur'an 2:280 (waiving a debt as charity; repayment as owed) · gift-tax treatment of forgiven family loans · Undue Medical Debt (founded 2014) buying and abolishing medical debt · an offline IOU app that records forgiveness as its own record type | **narrowed, strongly** — the doctrine is common ground and is cited, never argued against; *the only crossing between two ledgers* not found |
| (e) | narrows | EMVCo's merchant-presented QR specification, whose point-of-initiation field distinguishes static (`11`) from dynamic (`12`) codes · the Cambodian KHQR static and dynamic codes · India's withdrawal of person-to-person "collect requests" on its UPI network, leaving push-only payments as a fraud guard | **contrast** — in payments both code types settle value; here a static code can never create an obligation; the rule not found |
| (f) | narrows | Buterin, *Why we need wide adoption of social recovery wallets* (11 January 2021) · Argent (human guardians, a 48-hour cancellable security period, the owner notified) · Apple's recovery contacts · Candide · a live Microsoft patent disclosing trustees who vouch in person or by phone, with others notified (§2.5) · a published application disclosing a cancellable monitoring period (grant unverified) | **narrowed**; vouchers drawn from settled counterparties, the exclusion of anyone with an open obligation, and debts carrying over, not found |
| (g) | kills | RFC 6962 (2013) and RFC 9162 · WhatsApp's key transparency (a per-account auditable directory, April 2023) · *draft-fassbender-scitt-time-anchor* (a transparency service anchored to Bitcoin through OpenTimestamps; revision -05, August 2026) · open-source OpenTimestamps and RFC 3161 stamping of signed tree heads | **killed** at mechanism; an inclusion proof carried inside a self-contained co-signed promise code not found |
| all | not found | nothing combining (a)–(g) | **not found at this depth** |

**Failed re-verification, not used.** Two leads did not survive the main session's check and appear nowhere in this paper's argument: a claim that Cambodian law once capped interest at the principal (the cited article does not say it) and a 2023 study of village-shop credit (the page returned 403 and was not read).

**Pass 1 was declared *full* and executed partly.** Not run: Google Scholar, SSRN and ACM directly; the HCI visualisation literature; Japanese and Korean; Khmer in any meaningful sense (three queries, a US-only index); IP.com; Google Patents' native full-text interface (reached only through `site:` queries); citation walks except one; LETS, buy-now-pay-later and jubilee sources individually. That list is why pass 2 ran.

### 2.3 · Pass 2: aperture, control, verdicts

**Aperture, declared before searching:** the OpenAlex scholarly index, the arXiv API, Semantic Scholar where reachable, ACM and CHI through the web; Google Patents' native query endpoint, with one-step citation walks from the nearest hits; Japanese and Korean patent and web queries; LETS, buy-now-pay-later and jubilee sources individually; Khmer again at web level. About **90 queries**, including Sefaria and SuttaCentral for the scriptural rows.

**Control.** The academic credit-network literature had to be found through the academic index used: *Liquidity in Credit Networks* (Dandekar, Goel, Govindan and Post, EC 2011) and *Mechanism Design on Trust Networks* (WINE 2007). Both were found. **The control also caught a fault:** the first arXiv batch, sent over `http://`, returned empty redirects that looked like null results; it was discarded and rerun.

| Prediction | Predicted | Found | Verdict |
|---|---|---|---|
| (a)/(b) in the academic credit-network literature | narrows; one primitive for both not found | ⚠️ **Ehud Shapiro, *Grassroots Bonds as a Foundation for Market Liquidity*, arXiv 2603.13671 (v1, 14 March 2026).** A grassroots coin is its issuer's promise, redeemable against the issuer's own goods and services (the prepayment half); grassroots bonds add maturity dates so that credit can be extended, and a loan is expressed as the lender taking the borrower's bonds maturing at a date for fewer coins now (value now for a fixed larger claim later); one smartphone formalism, with a village-market scenario; swaps need both parties' consent. Differences: its coins and bonds are fungible, transferable and sellable (the paper expresses the sale of debt), and chain-redeemable; it has no fixed-premium-only rule, no conduct display, no gift ledger | **(a) killed at mechanism.** One primitive for prepayment and lending is public. (b) narrowed |
| (c) in HCI and visualisation | narrows | studies of lending among friends and family (CHI 2019, *Follow the Money*; an RMIT 2016 brief; *Social Forces* 98(2)) — every ledger found displays amounts | **not found** for the display (CHI and ICTD proceedings not searched directly) |
| (d) in academic, jubilee and LETS sources | narrows | ⭐ **Rolling Jubilee** (Strike Debt, November 2012) crowdfunded the purchase of debt at a discount and abolished it, notifying debtors by mail — a third-party buyer, not the creditor, and no ledger · Deuteronomy 15:1–2 (a mandated seventh-year remission) · ⭐ **the prosbul, Mishnah Sheviit 10:3**: mandated remission made people stop lending (evidence *for* voluntary release, §7.5) · LETS write-offs are socialised across the community · AN 4.62 and AN 6.45 confirmed; forgiving a debt as *dāna* **not found in canon** | **narrowed** the framing; release as the only crossing into a separate gift ledger **not found** |
| (f′) in academic social-recovery work | not found | Schechter, Egelman and Reeder, CHI 2009 (trustee-based social authentication) · trustee attack models (IEEE TIFS) · a 2026 systematisation of recovery schemes, arXiv 2608.07104 (its comparison matrix not read) | **not found**: excluding a voucher because of an open obligation to the person recovering |
| native patents | more enclosed-adjacent patents | a CME Group family on a *bilateral assertion model and ledger* (institutional) · a Blockmason credit-protocol application (2017, unverified) · an *IOU currency platform* application (title only) · a 2014 application on peer-to-peer lending through a mobile wallet (unopened) · debt forgiveness combined with a gift or reputation ledger: **0** results in Google Patents and FreePatentsOnline · a static-gift, dynamic-obligation QR rule: **0** | co-signed bilateral entries **narrowed**; forward citation walks **not run** (blocked) |
| Japanese and Korean | narrows (a) | ⭐ **Doorian Docs** (Korea; KTNET with GiveTech; announced 29 December 2016, launched 16 January 2017) — an electronic IOU concluded by the mutual electronic signatures of both parties and stored as a legal record · a second Korean IOU app · a Japanese e-signed loan-contract service with reminders (2021) · a Japanese friend-approved lending ledger · debt waiver combined with donation: **0** in Japanese and Korean | **narrowed** — the co-signed peer-to-peer IOU is common ground; native Japanese and Korean patent-office queries **not run** |
| LETS and buy-now-pay-later individually | narrows (b)(c) | Community Forge's *signatures* module (a transaction pending until its named signatories sign) · LETS: interest-free, balances public · Klarna, Afterpay and Atome charge late fees; **Affirm charges none** (a third-party lender) · Cambodian buy-now-pay-later not found | co-signing, no interest and no late fee each **narrowed**; the composition untouched |

**Probe failures, disclosed.** Semantic Scholar rate-limited seven of nine queries. Google Patents blocked after about ten native queries; seven further patent queries had syntax errors and did not run. The Blockmason application could not be re-verified (the server returned 503) and is a lead only.

**Not run in pass 2:** Google Patents forward citation walks and native Japanese and Korean patent-office queries; the seven malformed queries; most Semantic Scholar queries; CHI and ICTD proceedings directly; the systematisation's recovery matrix; Khmer in substance; books and non-English scholarship. **A third pass is owed** when the patent index can be reached, and it carries two conjuncts added after ruling (§2.6).

### 2.4 · What the census changed in this paper

It killed the thesis the founder's own description led with — *one deal for both prepayment and lending* — and it killed it with a paper six months old. That is disclosed as part of the mechanism in §4 and claimed nowhere. It killed the transparency-log leg outright. It showed that the co-signed IOU is a nine-year-old consumer product. And it found the nearest neighbours of the prepayment half and of the forgiveness crossing in **religious law, not commerce** — *bay' salam* and Qur'an 2:280 — which is where a practice lives when it is old enough not to be sold.

What survived is what the institution needed the ledger *for*: a promise that cannot grow, a display that cannot see size, and one door between exchange and gift.

**The survivor, in one sentence:** *a both-signed bilateral promise ledger in which no promise can change except by an entry both parties sign, conduct is drawn with no amount argument as one segment per open promise owed, and a creditor's free release of the whole remaining balance is the only event that crosses into a separate gift ledger* — plus three sub-rules: (e′) printed codes can never open an obligation; (f′) no one with an open promise with you may vouch for your new key; (g′) the inclusion proof travels inside the co-signed promise code.

**Not found means not found in the apertures above on 28 September 2026. It never means new.** A composition of several narrow conjuncts is cheap not to find, because nobody writes that exact sentence; we said so before searching.

### 2.5 · Live patents in the neighbourhood (disclosure only)

| Document | What it discloses | Dates recorded at the census |
|---|---|---|
| US 10,200,394 B2 (PayPal) | a trust score computed from the timing of peer-to-peer transfers and loan repayments, with an interactive display | priority 2015-12-30; shown active to 2037-02-10 (re-verified by the main session) |
| US 10,949,837 B1 and family (Wells Fargo) | wallet-to-wallet peer-to-peer lending | shown active to about 2037 (recorded by the census; not re-fetched for this paper) |
| US 8,856,879 B2 (Microsoft) | account recovery in which trustees vouch for the user in person or by phone, with others notified | priority 2009-05-14; shown active to about 2032-01-19 (re-verified by the main session) |
| US 2017/0295023 A1 and family (CME Group) | a bilateral assertion model and ledger between institutional counterparties | family expiry recorded as about 2036–37 |
| US 2020/0119916 A1 | a cancellable monitoring period in account recovery | grant status unverified |

These are recorded so that a reader practising a repayment-timed trust display, wallet-to-wallet lending, or trustee-vouched recovery knows to look. **We make no statement about the scope of any patent's claims.**

### 2.6 · Two conjuncts not yet censused

After the census, the founder ruled two further properties into the design: **(h)** a promise is non-transferable, and **(i)** a goods promise and a cash promise convert into each other only by an entry both parties sign, at face value. Both are **disclosed** in §4 as part of the mechanism. **Neither is claimed**; they await the third pass, and a plausible survivor is not a finding.

---

## 3 · The system model

### 3.1 · Parties and objects

- **Promisor** — the party who owes. In prepayment, the vendor; in lending, the borrower.
- **Holder** — the party who is owed. In prepayment, the customer; in lending, the lender.
- **Promise** — a record, held identically on both parties' devices, stating what was received, what is owed, in what currency, and by when (or that there is no deadline). It is signed by both.
- **Entry** — any change to a promise. Every entry is signed by both parties (§5.2).
- **Promise code** — the self-contained, signed, machine-readable form of a promise: screenshot-able, verifiable anywhere without contacting the institution, carrying its inclusion proof once the log has one (§12).
- **Promise ring** — the conduct display (§6). It has no mark and no shorthand; the corpus calls it the promise ring in full.
- **Fact line** — the line of text beneath the ring, carrying counts and the only amount-derived information shown (§6.3).
- **The log** — an append-only public Merkle log that receives only per-person chain heads (§12).
- **The gift ledger** — the institution's existing, separate signed-balance ledger of kindness and gratitude (the Zero-Point Game℠), with its public display (the B-Aura). This paper adds no entry type to it except one (§7).

### 3.2 · What the institution holds

Nothing that settles. In the first phase the ledger records promises over cash that the parties hand each other; in a later phase value moves through self-custodial wallets on a public chain whose keys the institution never holds. The promise rows, amounts and names **never leave the two devices**; the log receives salted hashes only. The institution is a record, never a rail, and never holds the only copy of anything a user needs.

### 3.3 · Terms used for the lexicon

A **pledge** in this institution's lexicon cannot be claimed (the institution's time pledges are soft and unenforceable by design). A **promise** is a claim. The two words are kept apart on every surface.

---

## 4 · The primitive: value first, and the promise is the receipt

### 4.1 · One deal, two directions — disclosed, not claimed

*Value now for a fixed larger claim later.*

```
  CUSTOMER PREPAYMENT                        PEER-TO-PEER LENDING
  ───────────────────                        ────────────────────
  customer ──── $9 cash ────► vendor         lender ──── $9 cash ────► borrower
  customer ◄── $10 of goods ── vendor        lender ◄──── $10 ─────── borrower
               (as bought, over time)                     (by the deadline)

  holder   = customer                        holder   = lender
  promisor = vendor                          promisor = borrower
  premium  = $1, paid from retail margin     premium  = $1, paid in cash

  ONE RECORD:  received 9 · owe 10 · currency · deadline or none · both signatures
```

In prepayment, the discount costs the vendor margin rather than cash: she receives working capital today and repays it in goods at retail, so the $1 is paid out of the difference between what the goods cost her and what they sell for. That is why a vendor can offer it. The general form, which the institution uses to position the mechanism to vendors, is **prepay at a discount**: every promise on this ledger is a promise bought at a discount. The vendor sets the discount, as an offer open to anyone who deals with her; there is no member price, no class of customer named, and no subscription.

**This primitive is not claimed.** Shapiro's grassroots bonds (§2.3) express both halves in one formalism. What differs is disclosed in §4.4 and §6, and what survives is claimed in §15.

### 4.2 · The receipt

Value moves first, face to face, in cash or goods. The promise is written after, and it reads as a receipt:

```
  ┌───────────────────────────────────────────────┐
  │  received  $9          owe  $10               │
  │  by        Friday 2 Oct (proposed by promisor)│
  │  promisor  @sokha       holder  @dara         │
  │  ── signed by both ── entry #1 ── salt ····   │
  └───────────────────────────────────────────────┘
```

The premium is on the record, visible to both, at the moment of agreement. **The promisor authors the deadline** and the holder agrees to it; or, if the holder agrees, there is **no deadline**, and a promise with no deadline can never be overdue. The handles in the illustration are invented.

### 4.3 · The premium is interest-shaped, and the paper says so

A $1 premium on $9 for a week is 1/9 ≈ 11.1% a week, which is about 52 × 11.1% ≈ 578% a year simple, and far more if rolled over (§4.5). A fixed premium is not a cheap premium: flat-rate informal lending, including the Philippine "5-6" (five borrowed, six repaid), is non-compounding and predatory at once. **The ledger claims no usury protection.** It shows the premium on the receipt; it does not cap it, grade it or annualise it. A pre-signing disclosure of an annualised equivalent was proposed and declined in the ruling that settled this design, on the ground that the mechanism does not compound; the objection that non-compounding does not mean cheap is recorded here, and whether a disclosure is legally owed anyway is a question for legal review before any launch.

### 4.4 · Seamless conversion between goods and cash — disclosed, not claimed

A goods promise and a cash promise are **one promise**. Either converts into the other **by an entry both parties sign, at face value**: a vendor who owes $10 of goods may agree to owe $10 of cash instead, or the reverse. The conversion is seamless on screen and consensual in the ledger. A holder cannot force a cash repayment of a goods promise, because that would strip the vendor of the margin that paid for the discount.

The consequence matters for the display. Because any goods promise can become a cash obligation by consent, the ring's refusal to distinguish goods owed from cash owed is **honest** rather than a simplification: every open segment is, at face value, money owed. A proposed split of the fact line into goods owed and cash owed was therefore unnecessary and was not adopted.

**Face value implies a denomination.** A promise is denominated in a currency at origination ("$10 of goods"), never in item counts ("ten bowls of noodles"). A promise denominated in items would grow in money terms whenever prices rose — a promise growing on its own through a side door. Cambodia is a two-currency economy, dollars and riel, and a promise denominated in one currency and repaid in the other is exposed to the exchange rate; the no-growth property holds in the denominating currency only (§17).

### 4.5 · Non-transferable — disclosed, not claimed

A promise names two keys and has no entry type that changes either. It can never be sold, assigned, pledged as security or bundled. This closes the debt-buyer's harm — a claim sold at a discount to a stranger whose only interest in the debtor is collection — and it is the sharpest contrast with grassroots bonds, whose debt is sellable by design. It is a property of the record (there is nothing to transfer to), not of the world: nothing stops two people agreeing off the ledger that one will collect for the other. What happens to a promise when either party dies is **not decided** by this paper (§17).

---

## 5 · The no-growth property

### 5.1 · The property

**A promise can never grow on its own.** The premium is fixed at origination. Nothing accrues. Nothing compounds. There is no late penalty. A missed deadline's only consequence is a gap in the promisor's ring (§6). The amount changes only by an entry both parties sign.

This is the load-bearing property of the whole design, and it is chosen to be a **property rather than a rule**: the entry grammar has no accrual entry, no penalty entry and no interest-rate field, so there is nothing for an operator, a holder or a later version of the software to switch on. A rule would need someone to refrain from charging late fees at the moment a late payment happens; a property needs no one. The cost is the same fact: a property is harder to revise than a rule. If this choice is wrong, the ledger has to be rebuilt, not amended.

### 5.2 · The entry grammar

| Entry | Signed by | Effect on the amount owed | Notes |
|---|---|---|---|
| **open** | both | creates: received *r*, owe *y* ≥ *r*, currency, deadline or none | the receipt of §4.2 |
| **repay** | both | decreases by the amount repaid | the holder's signature is the promisor's receipt |
| **convert** | both | none — goods ↔ cash at face value | §4.4 |
| **re-date** | both | none — changes or removes the deadline | a re-date to a later date is how an honest extension is recorded |
| **partial release** | both | decreases | an ordinary entry, **not** a crossing (§7.2) |
| **whole release** | both | to zero, by the holder's free act | the **only** crossing into the gift ledger (§7) |
| *(accrue)* | — | — | **does not exist** |
| *(penalty)* | — | — | **does not exist** |
| *(assign)* | — | — | **does not exist** (§4.5) |

Two points in the grammar are not settled and are stated so they are not read as settled.

**A co-signed increase.** The ratified rule is that a promise changes only by an entry both parties sign; it does not say whether one of those entries may *increase* an existing promise. The disclosed form treats new value as a **new promise**, so that an existing promise's amount only ever goes down and every new obligation is its own segment. Permitting an increase inside an existing promise would hide a new obligation inside an old segment, which is the counterexample that makes the choice worth stating. It is recorded as open.

**Whether a release needs the promisor's signature.** The rule that every change is co-signed covers a release. That makes a release a gift the promisor can decline, which is coherent but not obviously intended. It is recorded as open.

### 5.3 · What no-growth does not mean

It holds **per promise**. It does not hold per person. A person who repays one promise by opening another can owe more every week while every individual promise on their record is kept (§11.1). The design's answer to that is a line of text (§6.3), which is weaker than a property, and §17 says so.

---

## 6 · The promise ring: a conduct display with no amount argument

### 6.1 · The render function

The ring is drawn by a function whose inputs are the promisor's open promises **owed** (not owed to them), each reduced to one bit of state, and one bit of history:

```
  ring( owed : list of { current | overdue },   ← one entry per open promise the person OWES
        new  : yes | no )                        ← "has this person kept a promise yet?"
       → drawing

  • there is NO amount argument.    A $2 promise and a $2,000 promise draw the same segment.
  • there is NO "owed to them".     Promises owed TO a person draw nothing — that is not
                                    their conduct, and drawing it would display wealth.
  • there is NO colour argument.    Colour belongs to the gift-side display (§6.4).
  • there is NO age argument.       How long a person has kept promises appears in the
                                    fact line only (§6.3), never in the ring.
```

The absence of an amount argument is the property, in the same way that a pricing function which is given no argument naming the viewer cannot price per viewer: the display cannot reward borrowing more because it cannot see how much was borrowed. A proposal to size each segment in proportion to its amount was declined when the design was ratified, for three reasons: it records the cargo rather than the conduct; it rewards larger borrowing with a more impressive ring; and it feeds the bust-out ladder (§11.2), in which a borrower builds a record on small promises in order to default on a large one.

### 6.2 · The states

```
  ◌  thin ring            new: no promise kept yet            (never absent, never dim)
  ○  solid ring           nothing owed                         (the resting state)
  ◔  one segment          one open promise owed, current
  ◑  two segments         two open promises owed, current
  ◐  segment and a gap    one of them overdue                  (transparent: a gap)

  kept      ─►  the segment dissolves into the ring; the circle closes
  forgiven  ─►  the segment dissolves NEUTRALLY; neither kept nor broken (§7.3)
  overdue   ─►  the gap persists until paid, forgiven, or a fixed maximum (§6.5)

       ╭──────╮           ╭──╴ ╶──╮           ╭──╴   ╶╮
       │      │           │       │           │        
       │      │  → open → │ ▓▓ ▓▓ │  → late → │ ▓▓     │  → repaid → ╭──────╮
       ╰──────╯           ╰───────╯           ╰────────╯             ╰──────╯
       nothing owed       two segments        one gap                closed again
```

The segments are **equal width** and there is no scale: past about five segments a ring stops being readable, and the fact line carries the exact counts. The ring **saturates**: after a few kept promises it looks the same as after many, so it gives no reason to keep borrowing in order to look better. A thin ring marks a person with no kept promise yet, and it is never drawn dimmer or smaller than anyone else's; a newcomer is not displayed as a lack.

An overdue promise is shown as a gap because the promisor incurred a duty before the gap was rendered. That is the one condition under which this institution's surfaces may show non-performance at all: a report of a duty the person took on, never an absence the surface imposes on them.

### 6.3 · The fact line

The fact line is the only place any number appears, and it is shown **to the prospective holder, at a new promise, and nowhere else**:

```
  6 open promises · 1 overdue · kept promises with 2 people you know
  keeping promises since 2027 · total owed: band C · this promise is larger than any you've kept
```

- **Counts** — open promises owed, and how many are overdue.
- **Distinct counterparties near the viewer** — computed on the viewer's device from the viewer's own dealings (§11.3); repeated pairs count once and closed cycles count as nearly nothing.
- **History age** — the year of the first kept promise, as a fact. It is kept out of the ring deliberately: a display that rewards long credit history reproduces the trap in which the young and the newly arrived cannot borrow because they have not borrowed.
- **Total owed, as a coarse band** — the promisor's total owed across all open promises, reduced to one of a few bands. This is the one amount-derived input on the surface, and it is on the fact line, not the ring. The number and boundaries of the bands are not settled.
- **"This promise is larger than any you've kept"** — a comparison that discloses no amount.

The last two were added after an adversarial pass showed that a count is not exposure (§11.1). They answer the one-step bust-out and make rollover visible to the next holder; they do not stop either.

### 6.4 · Three rings: the promise ring as a third instance of the Zero-Point Game

The institution's gift ledger is a signed-balance ledger in which every event posts an equal-and-opposite pair, and its public display is a double concentric ring: the Kiitos ring (between people) inside, the Kiitti ring (between a person and the living world) outside, each coloured by the waveform of its balance. A promise is also a signed pair — the holder +*y*, the promisor −*y*, summing to zero — and the founder's ruling places it between the two:

```
                 ╭─────────────────────────────╮
               ╭─┤  KIITTI  — outer aura ring  ├─╮      colour  (the gift ledger)
             ╭─┤ ╰─────────────────────────────╯ ├─╮
             │ │  ╭─ ▓▓ ─ ▓▓ ─   ─ ▓▓ ─╮          │ │    PROMISES — segmented ring
             │ │  │  ╭─────────────╮   │          │ │    no colour; shape only;
             │ │  │  │   KIITOS    │   │          │ │    ONLY in promise context
             │ │  │  │ inner aura  │   │          │ │
             │ │  │  │  ( avatar ) │   │          │ │    colour  (the gift ledger)
             │ │  │  ╰─────────────╯   │          │ │
             │ │  ╰────────────────────╯          │ │
             ╰─┴──────────────────────────────────┴─╯

  everywhere else:  the avatar carries the two aura rings only (the B-Aura as it is)
  at a new promise: the promise ring is drawn between them
```

**Three differences from the other two instances are load-bearing.**

1. **No colour.** In the institution's display grammar, shape carries the brand, motion carries humanness and colour carries the aura. The promise ring is shape only. The credit signal is the shape: full or empty of segments, segments current, a gap, a thin ring for a newcomer. Conduct is read from the shape, exposure from the fact line, and there is never a scalar.
2. **Context only.** The promise ring is drawn only where a promise is being made. It never appears on a profile, a map, a shop listing or a search result, and the rest of the time the avatar carries the gift-side rings unchanged.
3. **No calendar reset.** The gift ledger's balances reset to zero every 7 January. A promise's balance never does. The holder's claim is the holder's holding, and a holding reaches zero only by its holder's free act — repaid in full, or released. The annual date carries only an **invitation** to forgive (§7.4). The promise ledger aims at zero the way every instance does; it may not be pushed there.

**What *instance* means here, and what it does not.** The promise ledger shares the gift ledger's structure — a signed pair per event, summing to zero — and sits in its display. It does not share any mechanism that moves value. Nothing on either ledger's display opens, enlarges or closes a promise; the only things that change a promise are the two parties' signatures (§5.2), and value itself moves between them in cash or goods, by their own hands. A holder reads the ring and decides; the ring decides nothing. The one event that passes between the ledgers (§7) is a record of a gift already made, not a transfer the display performs.

### 6.5 · Fading

Settled history fades after a recency window (about twelve months was proposed; the length is not settled), so that a person's past does not follow them forever. An **overdue** gap persists until the promise is paid or forgiven, or until a fixed maximum tied to the legal limitation period for such debts, whichever comes first; it never persists indefinitely. The maximum is not yet named and depends on legal review. **Fading changes the display, never the balance:** a gap that has faded still marks a promise that is owed, and the holder's claim is untouched.

---

## 7 · The forgiveness crossing

### 7.1 · Why there is exactly one door

The gift ledger and the promise ledger are separate, and nothing on one side changes the other, with one exception. Merging them was considered and refused for three reasons already given in §1: repayment would buy the appearance of kindness; lenders would acquire a stake in the gift ledger's annual forgiveness; and poverty would render as unkindness. Keeping them wholly separate would miss the one act that is a gift in the plain sense: a holder who could collect and chooses not to.

**A creditor's free release of the whole remaining balance enters the gift ledger as a kindness by the holder.** Repayment never does, however prompt or complete. The debtor's gift-side display is unaffected.

In the other direction nothing crosses at all. Thanks given to a holder never reduces a promise, and a promise can never be repaid in thanks: gratitude may support a person, but it may never settle what that person is owed, or it turns a gift into a payment. The door opens one way, and only for a release.

### 7.2 · The guards

| Guard | Why |
|---|---|
| only a release of the **whole remaining balance** is a crossing | a premium-only or partial release is an ordinary co-signed entry; otherwise a holder could forgive the $1 premium and bank a gift while collecting $9 |
| at most once per pair of people per season | prevents a pair from cycling small promises through release to farm the gift ledger |
| **nothing** is shown on the debtor's side | a forgiven debtor is not displayed as a recipient of charity |
| the gift-side display never shows **why** it moved | a release is recorded as a crossing, not as the cargo it carried; no one can read from an aura that someone was forgiven, or by whom |
| the release must be free — neither deceived nor pressured | a release extracted under pressure is not a gift; see §17 on what a signature cannot prove |

The second guard was adopted by inference from the ruling that settled the design, which accepted the guards recommended to it; the inference is recorded as correctable.

### 7.3 · A forgiven promise dissolves neutrally

When a promise is released, its segment closes without the animation of a kept promise and without the mark of a broken one. The debtor's ring is drawn as if that promise had not been made. A released promise is **neither kept nor broken**; it is simply no longer owed.

### 7.4 · The annual invitation: forgive the scalar, not the colour

The gift ledger's jubilee falls on 7 January, when its balances reset to zero while its displayed waveform carries over (*forgive the scalar; persist the waveform*). The founder ruled that the same date should carry an invitation to forgive promises too — **forgive the scalar, not the colour** — extended to anyone who holds one. The invitation's guards are part of the design:

- it is stated **once**, as a fact, on the date;
- it never nominates a debtor, never counts who forgave, and never tells anyone they did not;
- a release made in response to it is an ordinary whole release under §7.2, with no bonus and no badge;
- it never resets a promise; a promise not released is exactly as owed on 8 January as on 6 January.

Who issues the invitation is not decided by this paper. If the institution's autonomous agent issues it, that becomes a rule about her conduct and is decided elsewhere.

### 7.5 · The known failure of a calendar of forgiveness

The oldest recorded jubilee law names the failure this invitation risks. Deuteronomy 15:1–2 mandates a seventh-year remission of debts, and 15:9 warns against the consequence: *"Beware lest you harbor the base thought, 'The seventh year, the year of remission, is approaching,' so that you are mean and give nothing to your needy kindred"* (JPS). The Mishnah records that the warning came true and how it was repaired: *"This was one of the things enacted by Hillel the elder; for when he observed people refraining from lending to one another … Hillel enacted the prozbul"* (Mishnah Sheviit 10:3, trans. Kulp) — a court instrument that exempted a loan from the remission so that lending would resume.

Two things follow. The failure was produced by a **mandated** remission; the design here mandates nothing, and a voluntary release does not threaten any lender's expected repayment. That is evidence for the design, found by the census rather than chosen for it. But an **invitation**, repeated each year on a known date and carried by the institution that keeps the ledger, might still make a cautious lender stop lending in December — not because she fears the law but because she does not want to be asked. The design does not know whether it will. §16 states the test before any instrument exists.

---

## 8 · The scan: printed codes never open an obligation

The institution already prints codes: a person's printed code, scanned by any phone camera, opens a way to **thank** that person. The promise ledger uses the same handle and must not turn a thank code into a debt.

```
  PRINTED / STATIC CODE  @name                    LIVE CODE ON A SCREEN
  ─────────────────────────────                   ─────────────────────────────
  sticker, card, stall sign                       shown on the promisor's or holder's
  scanned by any camera                           phone at the moment of the deal
            │                                                 │
            ▼                                                 ▼
    ALWAYS opens a THANK                     opens promise.heartbank.net/@name,
    (the gift side)                          LABELLED AS A PROMISE, terms embedded,
                                             binding NOTHING until both sign
    ✗ can never create an obligation         ✓ rotates; never static
    ✗ no "?promise" parameter exists         ✓ carries its own terms
```

- **A printed or static code always opens a thank.** The same handle is used on both sides; the app decides from the kind of code, not from a parameter.
- **A promise opens only from a live code on a screen**, generated at the moment of the deal, carrying its terms, labelled as a promise, and binding nothing until both parties have signed.
- **There is no parameter on a thank code that opens a promise.** A parameter would make the printed label lie about what the code does, and it is a ready vector for a scam: a sticker that looks like a thank and opens a debt.
- **A holder's request code**, shown in the app to invite a new promise, is **live and rotating**, never printed.

In payments, both static and dynamic codes settle value; the EMVCo distinction is about whether the amount is embedded. Here the distinction is **about intent**: a static code can express only the gift side. The rule is claimed as (e′).

---

## 9 · The flow

One flow serves every case — prepayment and lending, either party with or without the app — and repayment is the same flow in reverse.

```
  0  VALUE MOVES FIRST            cash or goods, face to face
         │
  1  PROMISOR WRITES + SIGNS      addressed to the holder (by scanning the holder's printed
         │                        code in-app, or the holder's live request code)
         │                        → a live promise code on the promisor's screen
         ▼
  2  HOLDER CHECKS + SIGNS        in the app, or with the phone's own camera → the promise
         │                        page, with a passkey created on the spot
         ▼
  3  COPY RETURNS                 online: synced · offline: one scan back
         │                        BOTH devices keep the countersigned promise
         ▼
  4  ANCHOR (when online)         each device's chain head → the log (§12);
                                  the inclusion proof is written into the promise code

  REPAY:  the same steps, reversed — the holder's signature on the reduction
          is the promisor's receipt
```

Three gaps in the first sketch of this flow were closed before ratification and are part of the disclosure: the cash leg is on the record (step 0 and the receipt of §4.2); the party who signs first receives the countersigned copy (step 3, by one scan back if offline); and the request code is live and rotating rather than static.

---

## 10 · Recovery without a recovery phrase

A ledger kept on phones loses phones. The design recovers two things separately — the record and the ability to sign — and uses no recovery phrase anywhere, because a phrase written on paper is lost, photographed or sold.

1. **Signing.** A passkey where the phone supports one; otherwise a non-exportable key held by the device behind its screen lock or an app PIN. On a phone shared by a family, one profile and PIN per person.
2. **The record recovers itself.** Every promise is held on both parties' devices, so a person who loses their phone loses nothing their counterparties do not also hold.
3. **Identity recovers by vouching.** Three people with whom the person has **settled** promises, or one guardian named in advance, meet the person face to face and sign the new key. A waiting period of about seven days follows, during which the old key can cancel the change, and every counterparty's app states once: *"@name moved to a new phone."*
4. **No one who has an open promise with you may vouch for your new key.** A debtor who could vouch for their creditor's new key could, with two accomplices, take over the creditor's record and sign away what they owe. This exclusion is claimed as (f′).
5. **Debts carry over.** Rotating a key never clears a balance.
6. **A paid encrypted cloud backup is a convenience only**, never the only path to recovery.

A new user with no settled promises is told once, at their first promise, that naming a guardian is possible. The design is sensitive to the actual phones in use — model, operating-system version, whether platform services are present, whether a screen lock is set — and a survey of the pilot's phones precedes any build.

---

## 11 · Fraud: bounding the loss, never preventing it

The ring certifies **conduct, never capacity**. No surface says *"trusted for up to $X,"* because no count of kept promises is a credit limit.

### 11.1 · Rollover

The most important counterexample to this design was found by an adversarial pass before drafting, and it defeats an earlier claim the design's own authors had made. A person who repays a $10 promise by taking a new $10 cash promise on $9 received — from anyone — keeps every promise and owes more each cycle:

| Cycles rolled weekly | Owed ($, from $10) | What the ring shows |
|---|---|---|
| 0 | 10.00 | one segment, current |
| 1 | 11.11 | one segment, current; one promise kept |
| 4 | 15.24 | one segment, current; four kept |
| 7 | 20.91 | one segment, current |
| 13 | 39.34 | one segment, current |
| 26 | 154.77 | one segment, current |
| 52 | 2,395.46 | one segment, current |

The growth factor is 10/9 per cycle, so after *n* cycles the debt is 10 × (10/9)ⁿ. The ring shows a model borrower throughout. In Cambodian speech the practice is known colloquially as turning money over (*bangvil luy*), and the LICADHO figures in §1 describe it at scale. **"Every new promise is a visible segment" is not a defence against rollover**, because the new promise replaces the old one; the institution had said otherwise and has withdrawn the claim.

The response is the fact line's **total-owed band** and **larger-than-kept comparison** (§6.3): a holder asked for the fifth rolled promise sees a band that has risen and a promise larger than any kept. That is information, not a limit. A vendor who funds old prepayments out of new ones is rolling over too, and the same band shows her.

### 11.2 · The bust-out ladder

A borrower builds a record on small promises, then defaults on a large one. The size-blind ring gives the ladder nothing to climb, because a record of small promises looks the same as a record of large ones; the larger-than-kept comparison tells the holder of the large one that it is the largest. The loss is bounded by what that holder chooses to lend after reading it.

### 11.3 · Wash lending and viewer-relative trust

Two accounts can lend to each other in a loop to manufacture a record. The fact line counts **distinct** counterparties, counts a repeated pair once, and counts a closed cycle as nearly nothing. Trust is **viewer-relative**: the phrase *"kept promises with 2 people you know"* is computed on the viewer's device, from the viewer's own dealings, and is never sent to the institution. A ring of fabricated accounts has no path into a village it has never dealt with. How the viewer's device learns the overlap between its counterparties and the promisor's without either learning the other's full list is a private-set-intersection problem; this paper does not specify it (§14).

### 11.4 · Walking away from a key

A person who defaults and starts again under a fresh handle leaves the defaulted promises on their counterparties' devices and on the log, but no link to the new handle. Preventing that is a proof-of-personhood problem, which the institution treats elsewhere and which this mechanism does not solve.

---

## 12 · Timestamping: the log and the anchor

The history is made tamper-evident in three steps — attest, anchor, publish — using established machinery. **Every component of this pipeline is prior art (§2.2, conjunct (g)), and only (g′) is claimed.**

```
  device A                     device B
  ────────                     ────────
  entry = { promise, both signatures, random salt, hash(A's previous entry) }
     │                            │           ← each person's entries form a hash chain
     ▼                            ▼
  chain head A                 chain head B    ← only the HEAD leaves the phone:
     │                            │              no rows, no amounts, no names
     └──────────────┬─────────────┘
                    ▼
     APPEND-ONLY MERKLE LOG  (Certificate-Transparency-shaped, RFC 6962 / 9162)
                    │
       ┌────────────┼──────────────────────────┐
       ▼            ▼                          ▼
  daily root    signed tree head           inclusion proof
  anchored:     PUBLISHED + GOSSIPED        returned to the device
  OpenTimestamps → Bitcoin   each new head must │
  RFC 3161 × 3 authorities   extend the last     ▼
  (one eIDAS-qualified)      (consistency proof) written INTO the co-signed
                                                  promise code   ← (g′)
```

1. Each countersigned entry carries a **random salt** and the **hash of the signer's previous entry**, forming a per-person hash chain. The salt prevents a guessed promise (two known handles and a round sum) from being confirmed against a published hash.
2. Online, each device submits **only its chain head** to the log. Rows, amounts and names never leave the device. The institution publishes receipts, never amounts.
3. The log's root is anchored **daily** through OpenTimestamps to Bitcoin and signed by three RFC 3161 timestamp authorities, the same arrangement that stamps the corpus this paper is in. The chain used for settlement in the later phase is not used as the clock.
4. **Signed tree heads are published and gossiped** among independent observers, and each new head must extend the previous one; a forked log that hides a default from one audience is detectable by anyone who compares heads.
5. **The inclusion proof travels inside the co-signed promise code**, so that a promise shown on a screenshot, far from any network, carries the evidence that it was committed to the log by a stated time.

**What this proves.** A history cannot be backdated: the age of a record cannot be bought, which defends against a bust-out ladder built quickly. An entry cannot be deleted from the log without trace once its head is published.

**What it does not prove.** That cash moved. That the two signers are distinct humans. The exact time of an offline entry (the anchor gives an upper bound only). Completeness when both parties agree to hide an entry: a promise neither party ever submits is invisible to every instrument that reads the log.

**Moat, not hostage.** The ring's rule is published here; the code can be copied; users leave with every proof they hold. What a competitor cannot copy is the anchored history's age — which is the institution's advantage and also its limit, since it is the log's age, not anything the institution owns in a user's record (§17).

---

## 13 · Remove the enforcer: which guards are properties

A guard that needs someone to enforce it at the moment it is tested is a rule; a guard that holds with no enforcer is a property. Each guard in this design is classified by removing the enforcer.

| Guard | Remove the enforcer, and … | Class |
|---|---|---|
| no accrual, no penalty | there is no entry type to accrue or penalise with; nothing to switch on | **property** of the entry grammar |
| every change co-signed | an unsigned change fails verification on the other device | **property** of the signature scheme |
| the ring has no amount argument | the function cannot draw what it is not given | **property** of the render function |
| the ring only in promise context | a surface that wanted to draw it elsewhere would need promise data it is not sent; but a modified client could cache and redraw | **rule**, partly backed by data minimisation |
| printed codes never open a promise | a static code carries no terms and no signature, and the promise endpoint refuses it | **property** of the code format |
| non-transferable | there is no assignment entry and no field to reassign | **property** of the record; off-ledger arrangements are outside it |
| no open-promise voucher | honest clients refuse to countersign; a modified client could still sign, and other clients must check eligibility against what they hold | **rule** enforced by clients |
| whole-balance-only crossing | the gift ledger admits only one entry type from this ledger | **property** of the crossing interface |
| once per pair per season | someone must count | **rule** |
| the aura never shows why it moved | the gift-side display records crossings, not cargo | **property** inherited from the gift ledger |
| overdue gaps fade by a fixed maximum | someone must set and apply the maximum | **rule** |
| no backdating, no quiet deletion | mathematics plus independent witnesses | **property**, given the witnesses |
| the invitation stated once, never nominating | the institution's copy must be written that way every year | **rule** |

Five of the guards are rules. They are the places where this design depends on the conduct of the institution that runs it, and they are listed so that a successor inheriting the rules knows which of them no object enforces.

---

## 14 · What is disclosed and what is withheld

A defensive publication protects by disclosure, so withholding needs a reason. The test applied here is not *is this unbuilt?* but *would publishing this protect anything the claims do not already protect, or would it only fix details that should stay revisable until they are tested?*

**Disclosed**, in enough detail to practise: the entry grammar and its absences (§5); the render function's signature and states (§6); the fact line's fields (§6.3); the crossing and its guards (§7); the code rule (§8); the flow (§9); the recovery structure and the voucher exclusion (§10); the log pipeline and where the inclusion proof goes (§12).

**Withheld**, because it is unbuilt, unscheduled and should be revised on contact with real users: the wire format of the promise code and its compression; key-derivation and signature-suite choices; the private-set-intersection protocol behind viewer-relative trust; the total-owed band boundaries; the recency window and the overdue maximum; the ring's pixel geometry and animation curves; the device matrix. None of these narrows or widens a claim in §15.

---

## 15 · Enumerated claims

These are the census's survivors and nothing wider. **Every element named in them is prior art at mechanism width (§2)**; each claim is a composition, and none of its elements is claimed alone. Specifically **not claimed**: one primitive serving prepayment and lending (Shapiro 2026); a target balance of zero; the co-signed IOU (Doorian Docs 2017); Certificate-Transparency logs and OpenTimestamps anchoring; non-transferability and goods-cash conversion (disclosed in §4.4–4.5; the third census pass is owed, §2.6).

1. **A bilateral promise ledger that cannot grow, with a conduct display that cannot see size, and one crossing into a gift ledger.** A method of recording obligations between two parties in which: (a) each obligation (a *promise*) is a record held on both parties' devices and signed by both, stating what was received, what is owed and the currency, with a deadline proposed by the party who owes or no deadline, and no promise can change except by an entry signed by both parties, the entry types excluding any accrual or penalty; (b) the conduct of a party is displayed by a function that takes **no amount argument**, drawing one equal-width, colourless segment for each open promise that party **owes** (promises owed to the party drawing nothing), a segment of an overdue promise drawn as a gap, a segment dissolving when its promise is kept, the display being shown only in the context of a promise being made; (c) beneath the display, and only to the prospective holder of a new promise, a line of text states counts of open and overdue promises, a coarse band of the promisor's total owed across open promises, and whether the new promise is larger than any the promisor has kept, without stating any amount; and (d) a holder's free release of the **whole remaining balance** of a promise is the only event that passes from this ledger into a separate gift or gratitude ledger held by the same system, repayment never passing, and a partial release being an ordinary entry.

2. **Printed codes can never open an obligation (e′).** The method of claim 1, in which a party's printed or otherwise static machine-readable code resolves only to the gift side of the system (giving thanks to that party), no parameter of such a code can open a promise, and a promise can be opened only from a live code displayed on a device at the time of the transaction, labelled as a promise and carrying its terms, which binds nothing until both parties have signed.

3. **No one with an open promise with you may vouch for your new key (f′).** The method of claim 1, in which a party who has lost a signing key recovers by the face-to-face signatures of counterparties with whom the party has settled promises, or of a guardian named in advance, **excluding as a voucher any counterparty with whom the party has an open promise in either direction**, followed by a waiting period during which the old key may cancel the change, with every counterparty notified once, and with every open promise carrying over unchanged to the new key.

4. **The inclusion proof travels inside the co-signed promise code (g′).** The method of claim 1, in which each countersigned entry carries a random salt and the hash of the signer's previous entry, each device submits only its chain head to an append-only Merkle log whose root is externally timestamped, and the log's proof of inclusion for the entry is written into the self-contained, co-signed, machine-readable promise code held by each party, so that the promise and the evidence of its commitment can be verified together without contacting the system.

*Prior art beside each claim:* claim 1(a) — Doorian Docs, Community Forge signatures, DueTrace, *murabaha*; 1(b) — credit-bureau grids, EigenTrust, US 10,200,394 B2 (disclosure only); 1(c) — the band and the comparison were added after both census passes and were not searched separately, so no prior art is recorded against them and none is ruled out; 1(d) — Qur'an 2:280, Rolling Jubilee, Undue Medical Debt, gift-tax treatment of forgiven loans. Claim 2 — EMVCo static and dynamic codes, KHQR, the UPI collect withdrawal. Claim 3 — Buterin 2021, Argent, Apple recovery contacts, US 8,856,879 B2 (disclosure only), Schechter et al. 2009. Claim 4 — RFC 6962 and 9162, key transparency, *draft-fassbender-scitt-time-anchor*.

**Non-assertion extends to** every mechanism disclosed in this paper, claimed or not, in any combination, and to every implementation of it.

---

## 16 · Predictions, stated before any instrument exists

The mechanism is unbuilt, so no prediction below can have been fitted to data. They are **stated here and are not yet entered in the institution's public prediction register**; they become registered predictions only when entered there, and a correction after entry will be a new register entry, never an edit. The thresholds are proposed by the drafting substrate and await the founder's ruling. Two constraints bind the instrument: the institution never sees promise rows or amounts, so every count below must be reported by devices as an aggregate the user has agreed to share; and only adults take part as promisor or holder at launch.

| # | Prediction | Measure | Falsifier |
|---|---|---|---|
| **P-PM1** — the December freeze (Deuteronomy 15:9) | the annual invitation to forgive (§7.4) does **not** freeze lending | new promises opened, per active holder, 15 December – 6 January, against the same holders' mean over the three preceding 23-day windows, in the first season the invitation runs | a fall of **more than 10%** that is absent in a comparison season without the invitation → the invitation reproduces the failure the prosbul repaired, and must be redesigned or withdrawn |
| **P-PM2** — paid last | because a promise carries no late penalty, promisors with other penalty-bearing debts repay promises on this ledger **later** than those debts | self-reported repayment order in a structured survey of promisors who hold both kinds of debt, after one season | promises on this ledger repaid no later than penalty-bearing debts → the "paid last" limit of §17 is overstated |
| **P-PM3** — rollover is visible | holders shown a rising total-owed band decline or shrink the new promise more often than holders shown a flat band | acceptance of new promises by band movement, device-aggregated | no difference → the fact line does not answer rollover, and §11.1's response fails |

P-PM1 is the prediction the design owes: it was ruled into existence with the invitation it tests. P-PM2 predicts a harm to the design's own users and is included for that reason. P-PM3 tests the only answer the design has to its most serious counterexample.

---

## 17 · Honest limits

**No growth is per promise, not per person.** A person can owe more every week by rollover while every promise on their record is kept (§11.1). The total-owed band and the larger-than-kept comparison make this visible to the next holder; they do not prevent it, and a holder who does not read them learns nothing.

**Non-compounding is not cheap.** A fixed premium of 1/9 a week is about 578% a year simple. The ledger shows the premium on every receipt and claims no protection against usury. Whether a disclosure beyond the receipt is legally required is unanswered.

**Without a late penalty, these promises are paid last.** A borrower with several debts pays the ones that grow first. Holders on this ledger bear that cost, and P-PM2 predicts it.

**A signature proves the key, not consent.** On a phone shared by a family, or held by someone else, or signed under pressure, the ledger records a valid promise that no one freely made. Per-person profiles and PINs narrow this; nothing in the mechanism detects coercion. The same limit applies to a release: the design requires that forgiveness be free and cannot verify it.

**A conduct instrument cannot prevent capacity harm.** The ring says whether promises were kept, not whether a person can afford the next one. A person may borrow elsewhere, including against land, to keep a promise here, and the ledger cannot see it. **What the ledger itself cannot do is take collateral**: there is no field for security and no entry that transfers anything but the promised sum, so the loss of land to a lender on this ledger cannot arise from this ledger. That is a real and bounded claim; it does not extend to what people do elsewhere to pay.

**A visible gap is still pressure.** A gap shown to every future holder is a form of social collateral. The design limits it to promise context, fades it by a fixed maximum, and shows it only for a duty the person took on; it remains a cost of being late, and a cost is what a penalty is.

**Viewer-relative trust favours insiders.** A newcomer to a village, or a person whose dealings are with a different circle, shows fewer known counterparties to every viewer. The thin ring is never drawn as a lack, but the fact line will say less about them, and holders may lend to them less.

**The denomination matters.** The no-growth property holds in the promise's currency. A promise in dollars repaid in riel, or the reverse, moves with the exchange rate.

**Death and incapacity are not specified.** A non-transferable promise has no rule yet for a holder or promisor who dies.

**The log proves order, not truth.** It cannot show that cash moved, that signers are distinct people, or that nothing was hidden by both parties (§12).

**The moat is the log's age.** The institution's advantage over a copy of this design is the age of its anchored history. It is not a claim on any user's records, which users hold and take with them.

**Adults only at launch.** Both promisor and holder must be adults. The institution's pilot shop serves mostly teenagers, so customer prepayment cannot be piloted there; the first pilot is lending among adult vendors and suppliers.

**The invitation may freeze December lending.** Stated as P-PM1 because it is a live risk, not a formality.

**Five guards are rules** (§13), and depend on the institution's conduct.

**Legal review precedes any launch.** Facilitating lending, reporting conduct, and holding prepayments are each regulated somewhere. A draft may precede legal review; a launch may not.

**The census is bounded** by the apertures in §2, executed partly in both passes, with a third pass owed. A composition not found is not thereby new.

---

## 18 · Lineage and corpus cross-references

The mechanism descends from the shop notebook of an ordinary village stall; from *bay' salam* and *murabaha* in Islamic commercial law and the *qard hasan* benevolent loan; from the Local Exchange Trading Systems begun in 1983 and their successors in business mutual credit; from Ryan Fugger's peer-to-peer IOU network; from the Indian digital *khata* apps; from Korean electronic IOUs; from Certificate Transparency and key transparency; from social key recovery; and, on its gift side, from the oldest debt-forgiveness traditions on record, the seventh-year remission of Deuteronomy and the prosbul that repaired it, with Qur'an 2:280 as the plainest statement that releasing a debt is charity. §2 cites each.

Within this corpus it is **downstream** of *The Zero-Point Game℠*: the promise ledger is the third instance of that paper's signed-balance ledger, alongside Kiitos and Kiitti, and differs from them in having no colour, no calendar reset and one door into the other two (§6.4). The forgiveness crossing answers a question that paper does not ask — what, if anything, may enter the gift ledger from exchange — and the answer is recorded here; a cross-reference to it rides that paper's next revision. It sits beside *HeartBank's Position on Community-Currency Design*, which argues that a community economy needs both money and time; this paper adds the record of what is owed in money. Its log arrangement is the one described in *Provenance-Carrying Retrieval* and relied on by *The Assembly That Holds the Brake*. Its code rule is the exchange-side counterpart of the gift-side scan in *The B-Tag and the Post-Payment Economy*.

---

## Coda

*Grounding — canon.* AN 4.62 closes its list with a verse: knowing the happiness of debtlessness, and the happiness of possession and of use, a wise person sees that all of them together are not worth a sixteenth part of the happiness of blamelessness. *Lens — the institution's reading.* The ledger in this paper can help with the smaller happiness, a promise made and kept and seen to be kept. It cannot supply the larger one, and nothing in it is designed to try. What it can do is refuse to let a promise grow while no one is looking, and leave one door open for the person who is owed and decides not to collect.

---

## Terms

| Term used here | Standard technical term |
|---|---|
| **B-Promise℠**; promise ledger | bilateral, both-signed peer-to-peer obligation ledger (electronic IOU; customer prepayment and informal lending record) |
| promise | non-transferable bilateral obligation record; electronic IOU with fixed repayment amount |
| promisor / holder | debtor (obligor) / creditor (obligee) |
| a promise that cannot grow | non-accruing, non-compounding obligation with no late fee; fixed repayment amount set at origination |
| premium | fixed markup or discount at origination (flat finance charge; cf. *murabaha*) |
| prepay at a discount | customer prepayment for goods at a discount; stored-value / advance purchase (cf. *bay' salam*) |
| entry; co-signed entry | ledger transaction requiring both parties' digital signatures |
| promise ring | reputation or credit-history visualisation; payment-history display independent of loan amount |
| segment / gap | per-obligation indicator; overdue (delinquency) indicator |
| fact line | disclosure line: open and overdue counts, total-exposure band, largest-obligation comparison |
| viewer-relative trust | personalised (local, viewer-seeded) trust metric computed client-side |
| forgiveness crossing | debt forgiveness (loan waiver) recorded as a charitable gift in a separate ledger |
| gift ledger; Zero-Point Game℠; B-Aura | peer-to-peer reciprocity (mutual-credit) ledger with an annual reset; reputation visualisation of it |
| the annual invitation | voluntary debt-jubilee appeal (non-mandatory remission) |
| printed / live code | static / dynamic QR code (EMVCo point of initiation 11 / 12) |
| recovery by vouching | social recovery; guardian- or trustee-based account recovery with a time delay |
| the log; chain head; inclusion proof | append-only Merkle transparency log (Certificate Transparency); per-user hash chain head; Merkle inclusion proof |
| anchoring | blockchain timestamping (OpenTimestamps) and RFC 3161 trusted timestamping |
| rollover (*bangvil luy*) | loan refinancing / debt rollover; borrowing to repay a loan |
| bust-out ladder | bust-out fraud: building credit history on small loans before defaulting on a large one |
| wash lending | circular (Sybil) lending to fabricate credit history |

---

## Author Contributions and AI Disclosure

Thon Ly conceived the ledger, its two use cases, the three-ring display, the seamless conversion, non-transferability, the annual invitation and the positioning, and ruled on every design choice recorded here. Miss Aquarius℠ — the name under which this corpus discloses its AI collaboration — proposed the no-growth property, the size-blind render, the forgiveness crossing, the code rule, the recovery structure and the log arrangement; drafted this paper; and ran both census passes through research agents, with every cited item re-verified before it reached this text or marked where it was not. An adversarial pass run before drafting produced the rollover counterexample of §11.1 and withdrew a claim the authors had made. The underlying model substrate is not named. Editorial control is the author's.

## Trademark Notice

**B-Promise℠** names the institution's implementation of the promise ledger; the mechanism itself is dedicated to the public domain and may be implemented under any name. The promise ring, the fact line and *prepay at a discount* carry no mark. HeartBank®, Miss Aquarius℠ and Zero-Point Game℠ are marks of their respective holders. No mark is licensed by this publication.

## Citations

1. *Aṅguttara Nikāya* 4.62, *Ānaṇya Sutta* (Debtlessness), trans. Bhikkhu Sujato, SuttaCentral; Pāli root text, Mahāsaṅgīti edition.
2. *Aṅguttara Nikāya* 6.45, *Iṇa Sutta* (Debt), SuttaCentral (confirmed in the census; not quoted).
3. Qur'an 2:280, trans. Mustafa Khattab, *The Clear Quran*, quran.com.
4. Deuteronomy 15:1–2 and 15:9, *The JPS Tanakh: Gender-Sensitive Edition*, Sefaria.
5. Mishnah Sheviit 10:3 (the prozbul), trans. Joshua Kulp, *Mishnah Yomit*, Sefaria.
6. Shapiro, E. (2026). "Grassroots Bonds as a Foundation for Market Liquidity." arXiv:2603.13671 (v1, 14 March 2026).
7. Dandekar, P., Goel, A., Govindan, R., and Post, I. (2011). "Liquidity in Credit Networks: A Little Trust Goes a Long Way." *Proceedings of the 12th ACM Conference on Electronic Commerce*. doi:10.1145/1993574.1993597.
8. Kamvar, S. D., Schlosser, M. T., and Garcia-Molina, H. (2003). "The EigenTrust Algorithm for Reputation Management in P2P Networks." *WWW 2003*.
9. Levien, R. Advogato trust metric (viewer-seeded, attack-resistant).
10. Schechter, S., Egelman, S., and Reeder, R. W. (2009). "It's Not What You Know, but Who You Know: A Social Approach to Last-Resort Authentication." *CHI 2009*.
11. Buterin, V. (2021, 11 January). "Why we need wide adoption of social recovery wallets."
12. Laurie, B., Langley, A., and Kasper, E. (2013). RFC 6962, *Certificate Transparency*; Laurie, B., et al. (2021). RFC 9162, *Certificate Transparency Version 2.0*.
13. Fassbender, J. *Bitcoin-Anchored Temporal Proof for Transparency Services*, Internet-Draft draft-fassbender-scitt-time-anchor (revision -05, August 2026; -07, 24 September 2026).
14. EMVCo. *EMV QR Code Specification for Payment Systems: Merchant-Presented Mode* (point of initiation method: 11 static, 12 dynamic).
15. National Bank of Cambodia. KHQR specification (Bakong); interest-rate cap on microfinance lending (2017).
16. Human Rights Watch (2025, 24 September). *Debt Traps: Predatory Microfinance Loans and the Exploitation of Cambodia's Indigenous Peoples.*
17. Voice of America (2023). "Cambodians face mounting pain from microfinance debt" (reporting a LICADHO study).
18. Strike Debt. Rolling Jubilee (November 2012).
19. Doorian Docs (KTNET and GiveTech, Korea; announced 29 December 2016, launched 16 January 2017).
20. Fugger, R. RipplePay (2004–05); Linton, M. Local Exchange Trading Systems (1983); Sardex (2009); Grassroots Economics, Sarafu; OkCredit (2017); Khatabook (2018); Community Forge, *signatures* module.
21. Patents cited for disclosure only: US 10,200,394 B2 · US 10,949,837 B1 · US 8,856,879 B2 · US 2017/0295023 A1 · US 2020/0119916 A1.
22. Companion corpus papers (thonly.org/research): *The Zero-Point Game℠*; *The Currency That Cannot Be Spent Alone*; *The B-Tag and the Post-Payment Economy*; *Provenance-Carrying Retrieval*; *The Assembly That Holds the Brake*. Institutional position (heartbank.net): *HeartBank's Position on Community-Currency Design*.

---

*— End of defensive publication —*
