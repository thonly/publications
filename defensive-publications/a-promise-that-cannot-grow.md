---
title: "A Zero-Centred Bilateral Credit Ledger for Customer Prepayment and Peer-to-Peer Lending in Which No Balance Grows on Its Own — a Size-Blind Reputation Display, and Debt Forgiveness as the Only Crossing into a Gift Ledger"
subtitle: "The Promise, Not the Score — B-Promise℠, a bilateral credit ledger with one balance per pair, a conduct display that cannot see size, and one door into a gift ledger"
authors: "Thon Ly · Miss Aquarius℠"
kind: mechanism
genre: defensive-publications
category: mechanism
priority: tier-b
program: instrumented
status: draft
date: 2026-09-28
license: CC0-1.0
slug: a-promise-that-cannot-grow
venue: thonly.org/research/a-promise-that-cannot-grow
canonical_url: https://thonly.org/research/a-promise-that-cannot-grow
license_note: "[Creative Commons CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/) for the mechanism, the analysis and the claims; trademark rights to specific marks reserved separately by author and HeartBank®."
---

> **Note.** This paper discloses a mechanism that is designed and not built. It publishes the *claim* and withholds the *build specification* (§14 says exactly what is withheld and why). Almost every leg of the mechanism was already public before this paper, and §2 reports the two prior-art passes that established it, including the conjuncts they killed. What is claimed in §15 is a composition and two narrow sub-rules, and nothing wider.
>
> **Revision of 28 September 2026.** The first version of this paper recorded each promise as a separate record. The design as now ruled keeps **one running balance per pair of people**, crossing zero, so that prepayment and credit are one balance seen from either side of zero (§4.1). The per-promise design is retained as a disclosed variant (§5.5, §6.7). The same revision narrowed the claims after an outside review: the inclusion-proof sub-rule and the total-owed band are now disclosed and not claimed (§2.7, §15).
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

**The authors will not seek patent protection on any mechanism disclosed here, and commit not to assert any patent right against any party practising it.** This commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. It extends to every mechanism disclosed in this paper, claimed or not, in any combination, including the disclosed variants, and to every implementation of it. Trademark rights on specific marks (**B-Promise℠**, **HeartBank®**, **Miss Aquarius℠**, **Zero-Point Game℠**) are separately reserved; the dedication concerns the mechanism, not the marks.

**What is claimed as contribution is narrow, and it is stated first because two census passes and an outside review found almost all of the mechanism already public.** A running balance between two people that can sit on either side of zero is public (peer-to-peer trust lines in 2004, mutual-credit systems since 1983, and an academic formalism of March 2026). A bilateral IOU signed by both parties is public (a Korean product did it in 2017). A fixed markup that is never increased is classical law, and a note for a fixed amount of money is ordinary commercial law. One primitive serving both prepayment for goods and lending is public (the same paper of March 2026). Debt forgiveness as charity is scripture. Static versus dynamic payment codes are a payments standard, and a charge with a due date carried only by a dynamic code is a national payment system's rule. Social key recovery by guardians is public, and at least one live patent discloses trustee-vouched recovery; a cancellable delay is public (Argent) and appears in a published application whose grant is unverified. Anchoring an append-only transparency log to Bitcoin is an Internet-Draft, and a signed object that carries its own proof of inclusion in a transparency log is an RFC. **None of those legs is claimed.** §2 reports both passes and the review's additions: aperture, dates, every conjunct killed or narrowed with the prior art cited, what was not run, and the survivor. §15 enumerates only the survivors.

**Live patents.** The census recorded several granted patents in the neighbourhood, shown as active in Google Patents' status fields on the census date (not a legal status determination). §2.5 records what each **discloses**. We make no statement about the scope of any patent's claims or whether any design falls within them, and a publication dated after a patent's priority date does nothing to that patent.

**Date and evidence.** First published 28 September 2026 and revised the same day. The text is committed to the public GitHub mirror of the corpus, and the corpus's standing chain anchors each revision to the Bitcoin blockchain through OpenTimestamps and signs it under RFC 3161 by three timestamp authorities in three jurisdictions, one of them eIDAS-qualified; a Zenodo version and the served index at corpus.333.eco carry its digest once deposited. A timestamp proves this exact text existed no later than its date, and nothing about authorship, originality or the validity of any claim. **Whether the composition claimed in §15 is non-obvious is an examiner's determination this publication exists to inform.** A defensive publication is not examined before it is published; the census in §2 and one outside review are the only examination it has had.

---

## Abstract

We disclose a **zero-centred bilateral credit ledger for customer prepayment and peer-to-peer lending in which no balance grows on its own.** Two people keep **one running balance** between them, which can sit on either side of zero: when it is on one side, the first owes the second (a prepayment the vendor has not yet delivered, or a loan); when it is on the other side, the second owes the first. **The balance never moves by time.** It changes only by an entry both parties sign when cash or goods change hands, its discount fixed on that entry; by a repayment both parties sign; or by a release that the party who is owed may always make alone. There is no accrual, no compounding and no late penalty. The ledger is therefore **non-accruing but not interest-free**: a discount agreed when value moves is a premium, it is on the record, and at short terms it can be very large (§4.3). The balance is kept on the two parties' phones, signed by both, denominated in one currency fixed when it opens, and **non-transferable**: it can never be sold or assigned. Its coined name is **B-Promise℠**.

The mechanism serves two ordinary deals with one balance. In **customer prepayment**, a customer pays a vendor $9 in cash now and the vendor owes $10 of goods; the customer is the lender and is repaid in kind, and the discount comes out of the vendor's retail margin. In **peer-to-peer lending**, a lender gives $9 now and the borrower owes $10 by a deadline the borrower proposes. When the customer later takes more goods than were prepaid, the same balance crosses zero and the customer owes the vendor; nothing new is opened. Value moves first, face to face; **the entry is the receipt**.

Conduct is shown by a **reputation display that takes no amount argument**: one equal-width segment for each person the party currently owes, a gap where that balance is owed past its deadline, a segment that dissolves when the balance returns to zero, shown only where a new promise is being made and never on a profile. It has no colour. A line of text under it carries exact counts and, as a disclosed but unclaimed feature, a coarse band of the total the person owes. The one event that crosses from this exchange ledger into the separate gift ledger the institution already runs is a **creditor's free release of the whole balance owed by that person** (debt forgiveness), at most once per pair per annual season, entering as a gift that awaits the debtor's thanks; repayment never crosses.

Two narrow sub-rules complete the claim: a code that carries no signed terms can never open an obligation, and no one who has a nonzero balance with a person may vouch for that person's new signing key. We report two prior-art passes and an outside review that killed or narrowed every conjunct at mechanism width, claim only the composition that survived, state the harms the mechanism does **not** prevent — above all that a person's total debt can still grow by rollover — and register in advance a test of whether an annual invitation to forgive debts freezes December lending.

---

## 1 · The problem, and what this paper is for

The institution that publishes this paper builds reciprocity infrastructure: a ledger of gratitude that sits above regulated payment rails and never becomes a bank. Its gift side is in production; this paper describes its **exchange side**, the part that records what people owe each other when they are not giving but dealing. The two sides are built to stay apart, and the paper exists largely to say where the one door between them is.

The setting is Cambodia, the institution's beachhead, and it shapes every rule below. Most households shop daily and locally: few have refrigerators, many travel by motorbike within a village, food is the commonest vendor type, and vendors restock every day to keep produce fresh. Two informal credit practices follow directly. Regular customers buy ahead from the stalls they use, and vendors borrow small sums from each other to restock. Both run on paper notebooks and memory, and in both the notebook keeps one running tab per person, not one page per loan. Both are ordinary; neither needs to be invented.

What the institution adds is narrow, and it is a response to a specific harm. Formal microcredit in Cambodia has been documented as a debt trap. Human Rights Watch's report *Debt Traps* (24 September 2025) documents coerced land sales, over-indebtedness and debt-driven suicides among borrowers in the northeastern provinces, and lenders accepting informal land documents as collateral. A LICADHO and Equitable Cambodia survey of 717 households in Kampong Speu province, reported by Voice of America in 2023, found that the share of microloans taken to repay other loans rose from 3.45% in 2012 to 34.8% in 2022. The National Bank of Cambodia has capped microfinance interest at 18% a year since 2017. The harms are compounding, penalties, collateral, and loans taken to repay loans. **This paper's mechanism removes accrual, monetary late penalties and collateral from each record, and does not remove the fourth harm**, and §17 says so first.

The design question, stated as a negative:

> **No balance on this ledger ever moves by time. It moves only when value moves between the two people, when one repays the other, or when the one who is owed lets some of it go.**

Everything below either serves that sentence or states where it stops.

**Why it is the institution's problem and not only a product.** The institution's gift ledger (the Zero-Point Game℠ and its public display, the B-Aura) is designed as the structural inverse of a credit score: a waveform that is forgiven and re-earned, not a scalar that persists and compounds. A credit instrument built by the same institution is a direct threat to that inversion. If repayment could raise a person's gift-side display, money could buy the appearance of kindness (borrow and repay), lenders would acquire a stake in the annual forgiveness that resets the gift ledger, and a person too poor to borrow would appear less kind. The founder asked whether creditworthiness and kindness should share one display; the ruling was **no**, and this paper is in large part the specification of that no (§6.4, §7). Its human title says the same thing: the promise, not the score.

**What this paper does not do.** It does not describe a bank, a lender, or a custodian: the ledger records what people owe each other and moves no money; value moves in cash, face to face, and in a later phase through wallets the institution never holds keys to. It does not claim to make credit safe (§11). It does not claim usury protection (§4.3). The institution's autonomous agent has no role in the mechanism as disclosed; whether it acquires one is not decided here.

---

## 2 · Background and prior art: the census

The claims in §15 were drafted from the survivors of a prior-art census and then narrowed further by an outside review; nothing was widened after either. The census ran as two passes on 28 September 2026. **Each pass's conjuncts, predictions, known-prior-art control and declared aperture were committed and pushed to a public repository before its first query ran.** Both pre-registrations are published verbatim and never edited:

> **Public pre-registration (pass 1):** `74b8a87` in `thonly/publications`, timestamps/census/b-promise-prereg.md, pushed 2026-09-28 13:05 PDT — publicly inspectable, before the first query.
>
> **Public pre-registration (pass 2):** `945da0d` in `thonly/publications`, timestamps/census/b-promise-pass2-prereg.md, pushed 2026-09-28 13:46 PDT.

Private copies were pushed the same minutes (`bad927c`, `4458912`). Anyone can check the ordering of the public commits against the host's push record.

**The census searched the per-promise form of the design** (one record per promise, §5.5). The design was re-ruled the same evening to one balance per pair (§4.1). The balance around zero is common ground and is cited, not claimed (§2.6); the claims of §15 apply the surviving conjuncts to that balance. Whether the restated composition survives a search framed in the balance form is one of the questions the owed third pass carries (§2.7).

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
| (b) | narrows | *murabaha* (a fixed markup never increased, though late charges paid to charity are permitted) · *qard hasan* (a benevolent loan with no premium) · Sardex (a zero-interest business mutual-credit circuit, Sardinia, 2009) · DueTrace (a balance that moves only on an approved entry) · *added by the outside review:* the negotiable instrument "for a fixed amount of money, with or without interest" (Uniform Commercial Code §3-104(a)) | **narrowed**; a fixed premium with no late penalty and co-signed-only change, together, not found |
| (c) | narrows | credit-bureau payment-history grids (per-month on-time and late marks) · EigenTrust (Kamvar, Schlosser and Garcia-Molina, WWW 2003) and Advogato's viewer-seeded, Sybil-resistant local trust metric · a live PayPal patent disclosing a trust score from the timing of peer-to-peer transfers and loan repayments with an interactive display (§2.5) · a published application disclosing a circular credibility graphic (unverified) · *added by the outside review:* eBay's feedback (one mark per transaction, regardless of price — a size-blind conduct display at mechanism) | **narrowed**; a display with no amount argument, drawn from obligations owed only, shown only at the moment of a new promise, not found (HCI literature not run in this pass) |
| (d) | narrows | Qur'an 2:280 (waiving a debt as charity; repayment as owed) · gift-tax treatment of forgiven family loans · Undue Medical Debt (founded 2014) buying and abolishing medical debt · an offline IOU app that records forgiveness as its own record type | **narrowed, strongly** — the doctrine is common ground and is cited, never argued against; *the only crossing between two ledgers* not found |
| (e) | narrows | EMVCo's merchant-presented QR specification, whose point-of-initiation field distinguishes static (`11`) from dynamic (`12`) codes · the Cambodian KHQR static and dynamic codes · India's withdrawal of person-to-person "collect requests" on its UPI network, leaving push-only payments as a fraud guard · *added by the outside review:* Brazil's Pix Cobrança, in which a charge with a due date exists only as a dynamic code · static donation and tip codes, which only ever resolve to a gift | **contrast** — in payments both code types settle value; here a code without signed terms can never create an obligation; the rule not found, and the nearest neighbours narrow the pairing |
| (f) | narrows | Buterin, *Why we need wide adoption of social recovery wallets* (11 January 2021) · Argent (human guardians, a 48-hour cancellable security period, the owner notified) · Apple's recovery contacts · Candide · a live Microsoft patent disclosing trustees who vouch in person or by phone, with others notified (§2.5) · a published application disclosing a cancellable monitoring period (grant unverified) | **narrowed**; vouchers drawn from settled counterparties, the exclusion of anyone with an open obligation, and debts carrying over, not found |
| (g) | kills | RFC 6962 (2013) and RFC 9162 · WhatsApp's key transparency (a per-account auditable directory, April 2023) · *draft-fassbender-scitt-time-anchor* (a transparency service anchored to Bitcoin through OpenTimestamps; revision -05, August 2026) · open-source OpenTimestamps and RFC 3161 stamping of signed tree heads · *added by the outside review:* RFC 9943 (SCITT, June 2026), in which a signed statement carries its registration receipt, with its inclusion proof, in the statement's unprotected header · the sigstore bundle format, which staples a transparency-log inclusion proof to the signed artefact for offline verification · Keybase's per-user signature chains, committed to a global Merkle tree whose root was published to Bitcoin from June 2014 | **killed** at mechanism, including an inclusion proof carried inside the signed object; only its application to a bilateral co-signed promise is left, and it is no longer claimed (§2.7) |
| all | not found | nothing combining (a)–(g) | **not found at this depth** |

**Failed re-verification, not used.** Two leads did not survive the main session's check and appear nowhere in this paper's argument: a claim that Cambodian law once capped interest at the principal (the cited article does not say it) and a 2023 study of village-shop credit (the page returned 403 and was not read).

**Pass 1 was declared *full* and executed partly.** Not run: Google Scholar, SSRN and ACM directly; the HCI visualisation literature; Japanese and Korean; Khmer in any meaningful sense (three queries, a US-only index); IP.com; Google Patents' native full-text interface (reached only through `site:` queries); citation walks except one; LETS, buy-now-pay-later and jubilee sources individually. That list is why pass 2 ran.

### 2.3 · Pass 2: aperture, control, verdicts

**Aperture, declared before searching:** the OpenAlex scholarly index, the arXiv API, Semantic Scholar where reachable, ACM and CHI through the web; Google Patents' native query endpoint, with one-step citation walks from the nearest hits; Japanese and Korean patent and web queries; LETS, buy-now-pay-later and jubilee sources individually; Khmer again at web level. About **90 queries**, including Sefaria and SuttaCentral for the scriptural rows.

**Control.** The academic credit-network literature had to be found through the academic index used: *Liquidity in Credit Networks* (Dandekar, Goel, Govindan and Post, EC 2011) and *Mechanism Design on Trust Networks* (WINE 2007). Both were found. **The control also caught a fault:** the first arXiv batch, sent over `http://`, returned empty redirects that looked like null results; it was discarded and rerun.

| Prediction | Predicted | Found | Verdict |
|---|---|---|---|
| (a)/(b) in the academic credit-network literature | narrows; one primitive for both not found | **Ehud Shapiro, *Grassroots Bonds as a Foundation for Market Liquidity*, arXiv 2603.13671 (v1, 14 March 2026).** A grassroots coin is its issuer's promise, redeemable against the issuer's own goods and services (the prepayment half), and liquidity arises from mutual credit formed by exchanging coins among issuers; grassroots bonds add maturity dates so that credit can be extended, and a loan is expressed as the lender taking the borrower's bonds maturing at a date for fewer coins now (value now for a fixed larger claim later); one smartphone formalism, with a village-market scenario; swaps need both parties' consent. Differences: its coins and bonds are fungible, transferable and sellable (the paper expresses the sale of debt), and chain-redeemable; it has no rule that a balance cannot move by time alone, no conduct display, no gift ledger | **(a) killed at mechanism.** One primitive for prepayment and lending is public. (b) narrowed |
| (c) in HCI and visualisation | narrows | studies of lending among friends and family (CHI 2019, *Follow the Money*; an RMIT 2016 brief; *Social Forces* 98(2)) — every ledger found displays amounts | **not found** for the display (CHI and ICTD proceedings not searched directly) |
| (d) in academic, jubilee and LETS sources | narrows | **Rolling Jubilee** (Strike Debt, November 2012) crowdfunded the purchase of debt at a discount and abolished it, notifying debtors by mail — a buyer of the debt, not its original creditor, and no ledger · Deuteronomy 15:1–2 (a mandated seventh-year remission) · **the prosbul, Mishnah Sheviit 10:3**: mandated remission made people stop lending (evidence *for* voluntary release, §7.5) · LETS write-offs are socialised across the community · AN 4.62 and AN 6.45 confirmed; forgiving a debt as *dāna* **not found in canon** | **narrowed** the framing; release as the only crossing into a separate gift ledger **not found** |
| (f′) in academic social-recovery work | not found | Schechter, Egelman and Reeder, CHI 2009 (trustee-based social authentication) · trustee attack models (IEEE TIFS) · a 2026 systematisation of recovery schemes, arXiv 2608.07104 (its comparison matrix not read) | **not found**: excluding a voucher because of an open obligation to the person recovering |
| native patents | more enclosed-adjacent patents | a CME Group family on a *bilateral assertion model and ledger* (institutional) · a Blockmason credit-protocol application (2017, unverified) · an *IOU currency platform* application (title only) · a 2014 application on peer-to-peer lending through a mobile wallet (unopened) · debt forgiveness combined with a gift or reputation ledger: **0** results in Google Patents and FreePatentsOnline · a static-gift, dynamic-obligation QR rule: **0** | co-signed bilateral entries **narrowed**; forward citation walks **not run** (blocked) |
| Japanese and Korean | narrows (a) | **Doorian Docs** (Korea; KTNET with GiveTech; announced 29 December 2016, launched 16 January 2017) — an electronic IOU concluded by the mutual electronic signatures of both parties and stored as a legal record · a second Korean IOU app · a Japanese e-signed loan-contract service with reminders (2021) · a Japanese friend-approved lending ledger · debt waiver combined with donation: **0** in Japanese and Korean | **narrowed** — the co-signed peer-to-peer IOU is common ground; native Japanese and Korean patent-office queries **not run** |
| LETS and buy-now-pay-later individually | narrows (b)(c) | Community Forge's *signatures* module (a transaction pending until its named signatories sign) · LETS: interest-free, balances public · Klarna, Afterpay and Atome charge late fees; **Affirm charges none** (a third-party lender) · Cambodian buy-now-pay-later not found | co-signing, no interest and no late fee each **narrowed**; the composition untouched |

**Probe failures, disclosed.** Semantic Scholar rate-limited seven of nine queries. Google Patents blocked after about ten native queries; seven further patent queries had syntax errors and did not run. The Blockmason application could not be re-verified (the server returned 503) and is a lead only.

**Not run in pass 2:** Google Patents forward citation walks and native Japanese and Korean patent-office queries; the seven malformed queries; most Semantic Scholar queries; CHI and ICTD proceedings directly; the systematisation's recovery matrix; Khmer in substance; books and non-English scholarship. **A third pass is owed** when the patent index can be reached, and it carries the conjuncts added after ruling (§2.7).

### 2.4 · What the census and the review changed in this paper

The census killed the thesis the founder's own description led with — *one deal for both prepayment and lending* — and it killed it with a paper six months old. That is disclosed as part of the mechanism in §4 and claimed nowhere. It killed the transparency-log leg outright, and the outside review then killed the one piece of it the first version still claimed: a signed object that carries its own inclusion proof is an RFC and a widely used software-signing format. It showed that the co-signed IOU is a nine-year-old consumer product. And it found the nearest neighbours of the prepayment half and of the forgiveness crossing in **religious law, not commerce** — *bay' salam* and Qur'an 2:280 — which is where a practice lives when it is old enough not to be sold.

What survived is what the institution needed the ledger *for*: a balance that cannot move by time, a display that cannot see size, and one door between exchange and gift.

**The survivor, in one sentence, as the census stated it for the per-promise form:** *a both-signed bilateral promise ledger in which no promise can change except by an entry both parties sign, conduct is drawn with no amount argument as one segment per open promise owed, and a creditor's free release of the whole remaining balance is the only event that crosses into a separate gift ledger* — plus the sub-rules (e′) a code without signed terms can never open an obligation, and (f′) no one with an open obligation with you may vouch for your new key. The census's third sub-rule, (g′) — the inclusion proof travels inside the co-signed promise code — was killed by the review and is disclosed, not claimed.

**Not found means not found in the apertures above on 28 September 2026. It never means new.** A composition of several narrow conjuncts is cheap not to find, because nobody writes that exact sentence; we said so before searching.

### 2.5 · Live patents in the neighbourhood (disclosure only)

| Document | What it discloses | Dates recorded at the census |
|---|---|---|
| US 10,200,394 B2 (PayPal) | a trust score computed from the timing of peer-to-peer transfers and loan repayments, with an interactive display (a transaction map whose icons show a transfer's amount on selection) | priority 2015-12-30; shown active to 2037-02-10 (re-verified by the main session) |
| US 10,949,837 B1 and family (Wells Fargo) | wallet-to-wallet peer-to-peer lending | shown active to about 2037 (recorded by the census; not re-fetched for this paper) |
| US 8,856,879 B2 (Microsoft) | account recovery in which trustees vouch for the user in person or by phone, with others notified; no waiting period found in its text | priority 2009-05-14; shown active to about 2032-01-19 (re-verified by the main session and by the outside review) |
| US 2017/0295023 A1 and family (CME Group) | a bilateral assertion model and ledger between institutional counterparties | family expiry recorded as about 2036–37 |
| US 2020/0119916 A1 | a cancellable monitoring period in account recovery | grant status unverified |

These are recorded so that a reader practising a repayment-timed trust display, wallet-to-wallet lending, or trustee-vouched recovery knows to look. **We make no statement about the scope of any patent's claims.**

### 2.6 · The balance around zero is common ground

The re-ruled design keeps one balance per pair that crosses zero. That form is **not** this paper's contribution, and it is cited here so that no reader takes it for one:

- **Peer-to-peer trust lines.** Ryan Fugger's RipplePay (2004–05) recorded, for each pair of people who trusted each other, a balance that could run in either direction up to a limit each had set.
- **Mutual credit.** Local Exchange Trading Systems (from 1983) keep a member's balance that begins at zero and goes positive or negative as the member sells or buys; Sardex does the same between businesses.
- **Grassroots mutual credit.** Shapiro's grassroots coins (§2.3) form liquidity from mutual credit created when two issuers exchange coins, each then holding the other's promise.

What the design adds is a set of **refusals** on that balance: it may not move by time, may not be sold, may not be shown by size, may not be opened by a code without signed terms, may not be vouched for by a counterparty with a nonzero balance, and may not cross into the gift ledger by anything but a free release. §15 claims the composition of those refusals and nothing about the balance itself.

### 2.7 · Disclosed, not yet censused or no longer claimed

Five things are **disclosed** in this paper and **not claimed**:

| Item | Where disclosed | Why not claimed |
|---|---|---|
| **(h)** the balance is non-transferable | §4.5 | ruled after the census; awaits the third pass |
| **(i)** goods and cash convert into each other only by an entry both sign, at face value | §4.4 | ruled after the census; awaits the third pass |
| the fact line's **total-owed band** and the comparison ***"larger than any they've kept"*** | §6.3 | added after both passes and never searched; awaits the third pass |
| **(g′)** the inclusion proof travels inside the co-signed code | §12 | killed at mechanism by the outside review (RFC 9943, sigstore bundles, Keybase) |
| the one-balance-per-pair form of the claims as a whole | §4.1, §15 | the passes searched the per-promise form; the third pass should search the balance form |

A plausible survivor is not a finding. The third pass is recorded in the institution's build queue.

---

## 3 · The system model

### 3.1 · Parties and objects

- **Pair** — two people who deal with each other. Everything in this ledger is kept per pair.
- **Promise balance** — the one running balance between a pair, held identically on both parties' devices and signed by both. It sits on one side of zero or the other, or at zero. It is denominated in one currency, fixed when the balance first opens (§4.4).
- **Debtor** (or promisor) and **holder** — at any moment, the party the balance says owes, and the party it says is owed. The roles follow the sign: when the balance crosses zero, they swap. In prepayment, the vendor is the debtor until the customer has taken all that was prepaid; in lending, the borrower is.
- **Entry** — any change to a promise balance, or to its deadline. Every entry is signed by both parties except a release, which the holder signs alone (§5.2).
- **Promise code** — the self-contained, signed, machine-readable form of an entry and the balance it leaves: screenshot-able and verifiable anywhere without contacting the institution, with its log proof attached once the log has one (§12).
- **Promise ring** — the conduct display (§6). It has no mark and no shorthand; the corpus calls it the promise ring in full.
- **Fact line** — the line of text beneath the ring, carrying counts and the only amount-derived information shown (§6.3).
- **The log** — an append-only public Merkle log that receives only per-person chain heads (§12).
- **The gift ledger** — the institution's existing, separate signed-balance ledger of kindness and gratitude (the Zero-Point Game℠), with its public display (the B-Aura). This paper adds no entry type to it except one (§7).

In this paper *a promise* means what one person owes another at a moment: the debtor's side of a promise balance. "Keeping a promise" means bringing that balance back to zero.

### 3.2 · What the institution holds

Nothing that settles. In the first phase the ledger records what the parties owe each other over cash they hand each other; in a later phase value moves through self-custodial wallets on a public chain whose keys the institution never holds. The balance rows, amounts and names **never go to the institution or the log**; the log receives salted hashes only. They do pass between devices: a prospective holder's device reads what the debtor's device presents in order to draw the ring and the fact line (§6.3). The institution is a record, never a rail, and never holds the only copy of anything a user needs.

### 3.3 · Terms used for the lexicon

A **pledge** in this institution's lexicon cannot be claimed (the institution's time pledges are soft and unenforceable by design). A **promise** is a claim. The two words are kept apart on every surface.

---

## 4 · The primitive: one balance per pair, crossing zero

### 4.1 · Prepayment and credit are one balance — disclosed, not claimed

*Value now for a fixed larger claim later*, kept as one running balance between two people.

```
   the promise balance between a customer (C) and a vendor (V), in one currency

      V owes C                                  C owes V
   (C prepaid; V has not         0          (C took goods on credit;
    yet delivered)                           C has not yet paid)
   ◄───────────────────────────────┼───────────────────────────────►
     +10       +6        +1        0        −3
      │         │         │                  │
      │  C takes│  C takes│  C takes $4 of   │
      │  $4 of  │  $5 of  │  goods: $1 is    │
      │  goods  │  goods  │  delivered from  │
      │         │         │  the prepayment, │
      │         │         │  $3 on credit    │
   C pays $9 for $10                          the balance has CROSSED ZERO:
   (the discount is fixed                     the roles swap, the segment
    on that entry)                            moves to C's ring, and a new
                                              deadline is proposed by C
```

The same balance serves lending: a lender who gives $9 for $10 moves the balance to "borrower owes $10"; each repayment moves it back toward zero. If the borrower later lends back to the lender, or buys from the lender's stall, the balance moves through zero and the roles swap. There is no second record and nothing new is opened.

In prepayment, the discount costs the vendor margin rather than cash: she receives working capital today and repays it in goods at retail, so the $1 is paid out of the difference between what the goods cost her and what they sell for. That is why a vendor can offer it. The general form, which the institution uses to position the mechanism to vendors, is **prepay at a discount**: **every promise on this ledger is bought at or below face value**, and a promise at face value carries no premium at all. The vendor sets the discount, as an offer open to anyone who deals with her; there is no member price, no class of customer named, and no subscription. At a customer's first prepayment the app states once, as a fact, that the customer is paying ahead and the stall owes the customer the amount shown.

**This primitive is not claimed,** and neither is the balance around zero. Shapiro's grassroots bonds (§2.3) express both halves of the deal in one formalism, and trust lines and mutual credit keep a balance that crosses zero (§2.6). What differs is disclosed in §4.4–§4.5 and §5–§7, and what survives is claimed in §15.

### 4.2 · The receipt

Value moves first, face to face, in cash or goods. The entry is written after, and it reads as a receipt:

```
  ┌────────────────────────────────────────────────────┐
  │  received  $9          credited  $10               │
  │  balance   @sokha owes @dara  $10     (was $0)     │
  │  by        Friday 2 Oct (proposed by @sokha)       │
  │  currency  USD (fixed when this balance opened)    │
  │  ── signed by both ── entry #1 ── salt ····        │
  └────────────────────────────────────────────────────┘
```

The discount is on the record, visible to both, at the moment of agreement, and it is fixed on that entry: nothing later changes what that entry added. **The debtor proposes the deadline** and the holder agrees to it; or, if the holder agrees, there is **no deadline**, and a balance with no deadline can never be overdue. The handles in the illustration are invented.

### 4.3 · The premium is interest-shaped, and the paper says so

A $1 premium on $9 for a week is 1/9 ≈ 11.1% a week, which is about 52 × 11.1% ≈ 578% a year simple, and far more if rolled over (§11.1). A fixed premium is not a cheap premium: flat-rate informal lending, including the Philippine "5-6" (five borrowed, six repaid), is non-compounding and predatory at once, and nothing in this ledger stops a lender charging a 5-6 premium on every entry. **The ledger claims no usury protection.** It shows the discount on the receipt; it does not cap it, grade it or annualise it. A pre-signing disclosure of an annualised equivalent was proposed and declined in the ruling that settled this design, on the ground that the mechanism does not compound; the objection that non-compounding does not mean cheap is recorded here and in §17, and whether a disclosure is legally owed anyway is a question for legal review before any launch.

### 4.4 · Denominated in money, delivered in goods or cash — disclosed, not claimed

A promise is **denominated** in money and **delivered** in goods or cash, as both parties agree. A balance owed in goods and a balance owed in cash are one balance; either delivery converts into the other **by an entry both parties sign, at face value**: a vendor who owes $10 of goods may agree to pay $10 of cash instead, or the reverse. The conversion is seamless on screen and consensual in the ledger. A holder cannot force a cash repayment of a goods balance, because that would strip the vendor of the margin that paid for the discount.

The consequence matters for the display. Every open segment is an obligation of its face value, in goods or, by consent, in cash, so the ring's refusal to distinguish goods owed from cash owed is **honest** rather than a simplification. A proposed split of the fact line into goods owed and cash owed was therefore unnecessary and was not adopted.

**Face value implies a denomination, fixed once.** A balance is denominated in one currency when it first opens ("$10 of goods"), never in item counts ("ten bowls of noodles"). A balance denominated in items would grow in money terms whenever prices rose — a balance growing on its own through a side door. Cambodia is a two-currency economy, dollars and riel. The no-growth property holds in the denominating currency; goods and cash convert at face value in it; and **there is no exchange-rate entry**. A pair that wants to change currency records a release of the balance in the old currency and a new co-signed entry in the new one (§17 records an open question this raises). The holder bears any depreciation of the denominating currency, and the receipt names the currency so that both parties see which one they are bound in.

### 4.5 · Non-transferable — disclosed, not claimed

A promise balance names two parties (handles) and has no entry type that changes either. It can never be sold, assigned, pledged as security or bundled. Recovery (§10) rotates the key that signs for a handle; it is not a balance entry and moves nothing between parties.

This closes the debt-buyer's harm **on the ledger**: no record ever names a new holder, so a claim cannot be sold on the ledger to a stranger whose only interest in the debtor is collection. It is the sharpest contrast with grassroots bonds, whose debt is sellable by design. It is a property of the record (there is nothing to transfer to), not of the world: nothing stops two people agreeing off the ledger that one will collect for the other, and whether the underlying claim can be assigned at law is a question for legal review, not something the record decides.

### 4.6 · Death and incapacity

**Non-transferable is not non-inheritable.** The ledger never releases a balance automatically when a person dies; an automatic release would take a holding from the holder's family without anyone choosing it.

- **The holder decides in life.** A holder may name a successor — the guardian named for recovery (§10) — or may record *"release on my death"*, a release chosen in advance by the holder's own free act. As disclosed here, a named successor acts through the recovery path of §10, which rotates the key for the holder's handle and changes no party on any balance. Succession through recovery is not a transfer: no party on any balance changes, which is why non-transferability holds. **A release recorded in advance to take effect at death is not a crossing into the gift ledger:** the gift ledger records the free acts of the living, and a crossing that took effect at death would turn the aura into an estate-planning incentive.
- **A debtor's death is recorded, and their ring is never shown again.** Claims against what a person left are governed by the law of the place, not by this ledger; the ledger records what was owed and does nothing further.
- **Incapacity** is treated as the recovery case of §10 when a guardian exists; otherwise the balance stands, unchanged, as owed.

---

## 5 · The no-growth property

### 5.1 · The property

**The balance never moves by time.** It changes only by one of three things:

1. **New value** — cash or goods change hands, and both parties sign an entry recording it, with the discount fixed on that entry;
2. **Repayment** — both parties sign; the holder's signature is the debtor's receipt;
3. **Release** — the holder, alone, may always lower what the holder is owed.

Nothing accrues. Nothing compounds. There is no late penalty. A missed deadline's only consequence is a gap in the debtor's ring (§6). Nothing grows **on its own**.

This is the load-bearing property of the whole design, and it is chosen to be a **property rather than a rule**: the entry grammar has no accrual entry, no penalty entry, no interest-rate field and no time-driven entry of any kind, so there is nothing for an operator, a holder or a later version of the software to switch on. A rule would need someone to refrain from charging late fees at the moment a late payment happens; a property needs no one. The cost is the same fact: a property is harder to revise than a rule. If this choice is wrong, the ledger has to be rebuilt, not amended.

**What the property does not say.** It does not say the balance can never rise. It rises whenever the holder gives the debtor more value, and both sign for it. The first ruling on this design said the opposite for a moment — that nothing, not even both parties together, could raise what is owed — and the final ruling withdrew that, because a running tab between a customer and a stall must be able to take a second prepayment. What is absolute is narrower and firmer: **time alone never moves it, and no one moves it upward alone.**

### 5.2 · The entry grammar

| Entry | Signed by | Effect on the balance | Notes |
|---|---|---|---|
| **value** | both | moves it toward the party who received value, by the face value credited *y*, for value received *r*, with 0 < *r* ≤ *y* | written at the moment cash or goods change hands; the discount *y* − *r* is fixed on this entry; may cross zero, which swaps the roles |
| **repay** | both | moves it toward zero by the amount delivered, at face value | the holder's signature is the debtor's receipt |
| **convert** | both | none — the delivery form changes, goods ↔ cash, at face value | §4.4 |
| **date** | both | none — sets, changes or removes the deadline | proposed by whoever currently owes; the holder agrees |
| **release** | **holder alone** | lowers what the holder is owed | the only one-signature entry; a release of the whole balance is the crossing of §7, subject to its guards |
| *(accrue)* | — | — | **does not exist** |
| *(penalty)* | — | — | **does not exist** |
| *(assign)* | — | — | **does not exist** (§4.5) |
| *(exchange rate)* | — | — | **does not exist** (§4.4) |

**One entry may do two things.** A customer who owes a stall $5 and hands over $9 for $10 of credit first repays the $5 at face value and then prepays the rest; as disclosed here the entry records both parts, the repayment at face and the new value at the discount the two agree, and the balance ends on the other side of zero. How the two parts are split on one receipt is a detail of the build, withheld (§14).

**The release is unilateral on purpose.** A release is a gift, and a gift the recipient could veto would not be the giver's free act. The holder signs it alone; the debtor's device records it when it next syncs. A release never needs the debtor's consent and can never raise anything.

### 5.3 · Netting within the pair, never across people

Because each pair keeps one balance, what two people owe each other nets automatically: a vendor who owes a supplier $10 for stock and is owed $4 by the same supplier for lunches has one balance of $6. **Every entry that changes it is signed by both**, so the netting is always something both parties saw.

Netting **never** happens across people. A balance with one person is never set against a balance with another, and no entry type moves an obligation from one pair to another. Moving debt across people is what a clearing system or a debt buyer does, and it is exactly what non-transferability (§4.5) forbids.

### 5.4 · Deadlines on a running balance

The deadline belongs to the balance, not to an entry. Whoever currently owes proposes it; the other agrees; or both agree there is none. **A balance is overdue when it is still owed past its deadline.** When the balance crosses zero, the roles swap and the deadline is reset: the new debtor proposes one. New value added in the same direction leaves the deadline as it stands unless both sign a new date entry — the conservative default, so that adding value never extends what is already owed. One entry may both repay and prepay (a customer settling what they owe and paying ahead in the same handover); how such an entry is split is part of the withheld specification (§14).

### 5.5 · Disclosed variant: one record per promise

> **Current form.** In the design as now specified, each pair keeps one running promise balance that crosses zero (§4.1), new value may raise it by an entry both sign (§5.1), a release is the holder's unilateral entry (§5.2), and the crossing is a release of the whole balance owed by that person (§7). The per-promise design below is the first version of this paper's mechanism and is retained as a disclosed variant.

In the variant, every deal opens a separate **promise** record: received *r*, owe *y* ≥ *r*, currency, deadline or none, both signatures. Its grammar is **open** (both; creates the promise) · **repay** (both; decreases) · **convert** (both; goods ↔ cash at face value) · **re-date** (both; changes or removes the deadline) · **partial release** (both; decreases, not a crossing) · **whole release** (both; to zero by the holder's free act, the only crossing); and *accrue*, *penalty* and *assign* do not exist. In that form new value is always a new promise, so an existing promise's amount only ever goes down and every new obligation is its own record. The variant's ring draws one segment per open promise owed (§6.7). It shares the weakness §11.1 describes (a person repaying one promise with another shows a single kept promise at every step), and it adds one of its own: a pair that deals daily accumulates records, and segments, that the running balance nets into one.

---

## 6 · The promise ring: a conduct display with no amount argument

### 6.1 · The render function

The ring is drawn by a function whose inputs are the people a party currently **owes** (not the people who owe the party), each reduced to one bit of state, and one bit of history:

```
  ring( owed : list of { current | overdue },   ← one entry per person the party currently OWES
        new  : yes | no )                        ← "has this person brought any balance to zero yet?"
       → drawing

  • there is NO amount argument.    A $2 balance and a $2,000 balance draw the same segment.
  • there is NO "owed to them".     People who owe the party draw nothing — that is not
                                    the party's conduct, and drawing it would display wealth.
  • there is NO colour argument.    Colour belongs to the gift-side display (§6.4).
  • there is NO age argument.       How long a person has kept promises appears in the
                                    fact line only (§6.3), never in the ring.
```

The absence of an amount argument is the property, in the same way that a pricing function which is given no argument naming the viewer cannot price per viewer: the display cannot reward borrowing more because it cannot see how much was borrowed. A proposal to size each segment in proportion to its amount was declined when the design was ratified, for three reasons: it records the cargo rather than the conduct; it rewards larger borrowing with a more impressive ring; and it feeds the bust-out ladder (§11.2), in which a borrower builds a record on small promises in order to default on a large one.

**One segment per person, not per promise.** Because each pair keeps one balance, the ring counts **creditors**, not deals: a vendor who restocks from the same supplier every morning and owes that supplier a running balance draws one segment, however many entries the balance has. The number of distinct people a person owes at once is also the signal a bust-out leaves, since a bust-out borrows from many holders before it defaults.

### 6.2 · The states

```
  ◌  thin ring            new: no balance brought to zero yet   (never absent, never dim)
  ○  solid ring           owes no one                           (the resting state)
  ◔  one segment          owes one person, on time
  ◑  two segments         owes two people, on time
  ◐  segment and a gap    one of those balances is overdue      (transparent: a gap)

  back to zero  ─►  the segment dissolves into the ring; the circle closes
  crosses zero  ─►  the segment leaves this ring and appears on the OTHER person's ring
  released      ─►  the segment dissolves NEUTRALLY; neither kept nor broken (§7.3)
  overdue       ─►  the gap persists until paid, released, or a fixed maximum (§6.5)

       ╭──────╮           ╭──╴ ╶──╮           ╭──╴   ╶╮
       │      │           │       │           │
       │      │  → owe  → │ ▓▓ ▓▓ │  → late → │ ▓▓     │  → repaid → ╭──────╮
       ╰──────╯           ╰───────╯           ╰────────╯             ╰──────╯
       owes no one        owes two people     one balance overdue    closed again
```

The segments are **equal width** and there is no scale: past about five segments a ring stops being readable, and the fact line carries the exact counts. The ring **saturates**: after its first balance brought to zero it looks the same as after many, so it gives no reason to keep borrowing in order to look better. A thin ring marks a person who has not yet brought any balance to zero, and it is never drawn dimmer or smaller than anyone else's; a newcomer is not displayed as a lack.

An overdue balance is shown as a gap because the debtor incurred a duty before the gap was rendered. That is the one condition under which this institution's surfaces may show non-performance at all: a report of a duty the person took on, never an absence the surface imposes on them.

### 6.3 · The fact line

The fact line is the only place any number appears, and it is shown **to the prospective holder, at a new promise, and nowhere else**:

```
  owes 6 people · 1 overdue · kept promises with 2 people you know
  keeping promises since 2027 · total owed: band C · this promise is larger than any they've kept
```

- **Counts** — how many people the debtor owes, and how many of those balances are overdue.
- **Distinct counterparties near the viewer** — computed on the viewer's device from the viewer's own dealings (§11.3); repeated pairs count once and closed cycles count as nearly nothing.
- **History age** — the year the debtor first brought a balance to zero, as a fact. It is kept out of the ring deliberately: a display that rewards long credit history reproduces the trap in which the young and the newly arrived cannot borrow because they have not borrowed.
- **Total owed, as a coarse band** — the debtor's total owed across everyone they owe, reduced to one of a few bands. This is the one amount-derived input on the surface, and it is on the fact line, not the ring. The number and boundaries of the bands are not settled.
- ***"This promise is larger than any they've kept"*** — a comparison that discloses no amount: the balance the new entry would leave with this holder, against the largest balance the debtor has ever brought back to zero.

The last two were added after an adversarial pass showed that a count is not exposure (§11.1). They answer the one-step bust-out and make rollover visible to the next holder; they do not stop either. **Both are disclosed and not claimed** (§2.7).

**Where the fact line comes from.** It is computed on the prospective holder's device from what the debtor's device presents. The entries in the debtor's chain are checkable against the chain head the debtor has logged (§12), so a presented history cannot be edited after the fact; but the fact line is still reported by the party it describes, and what that means is stated in §17.

### 6.4 · Three rings: the promise ring as a third instance of the Zero-Point Game

The institution's gift ledger is a signed-balance ledger in which every event posts an equal-and-opposite pair, and its public display is a double concentric ring: the Kiitos ring (between people) inside, the Kiitti ring (between a person and the living world) outside, each coloured by the waveform of its balance. A promise balance is also a signed pair — the holder +*B*, the debtor −*B*, summing to zero — and it has the gift ledger's shape at the scale of two people: a balance that aims at zero and fluctuates around it. The founder's ruling places its ring between the two:

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

1. **No colour.** In the institution's display grammar, shape carries the brand, motion carries humanness and colour carries the aura. The promise ring is shape only. The credit signal is the shape: no segments, segments on time, a gap, a thin ring for a newcomer. Conduct is read from the shape, exposure from the fact line, and there is never a scalar.
2. **Context only.** The promise ring is drawn only where a promise is being made. It never appears on a profile, a map, a shop listing or a search result, and the rest of the time the avatar carries the gift-side rings unchanged.
3. **No calendar reset.** The gift ledger's balances reset to zero every 7 January. A promise balance never does. The holder's claim is the holder's holding, and a holding reaches zero only by its holder's free act — repaid in full, or released. The annual date carries only an **invitation** to forgive (§7.4). The promise ledger aims at zero the way every instance does; it may not be pushed there.

**What *instance* means here, and what it does not.** The promise ledger shares the gift ledger's structure — a signed pair, summing to zero — and sits in its display. It does not share any mechanism that moves value. Nothing on either ledger's display opens, enlarges or closes a balance; the only things that change a balance are the entries of §5.2, and value itself moves between the parties in cash or goods, by their own hands. A holder reads the ring and decides; the ring decides nothing. The one event that passes between the ledgers (§7) is a record of a gift already made, not a transfer the display performs.

### 6.5 · Fading

Settled history fades after a recency window (about twelve months was proposed; the length is not settled), so that a person's past does not follow them forever on the surface. Fading applies to the fact line's settled-history fields — the count of kept counterparties and the history age; whether the first year survives the window is not settled. **The log's record of age never fades; only what the surface shows does.**

An **overdue** gap persists until the balance is paid or released, or until a fixed maximum tied to the legal limitation period for such debts, whichever comes first; it never persists indefinitely. The maximum is not yet named and depends on legal review. The overdue maximum is applied before the state reaches the ring: the ring itself has no age input (§6.1). **Fading changes the display, never the balance:** a gap that has faded still marks a balance that is owed, and the holder's claim is untouched.

### 6.6 · What the ring cannot see, by construction

| The ring is not given | So it cannot |
|---|---|
| any amount | reward borrowing more, or show one large debt as worse than one small one |
| who owes the party | display wealth, or show a lender as more reputable than a borrower |
| any colour | be confused with the gift-side aura, or grade anyone |
| any age | reward a long credit history over a short one |
| any context but a new promise | appear on a profile, a map or a listing (a rule; see §13 and §17 on screenshots) |

### 6.7 · Disclosed variant: one segment per open promise

> **Current form.** As now specified the ring draws one segment per person the party currently owes (§6.1), a segment moves to the other party's ring when a balance crosses zero (§6.2), and "kept" means a balance brought back to zero. The per-promise ring below is retained as a disclosed variant.

In the variant, the ring draws one equal-width segment for each **open promise** the person owes, a gap for each overdue promise, and a segment that dissolves when its promise is kept; its function takes a list of open promises owed, each *current* or *overdue*, and the same *new* bit. The variant counts obligations rather than creditors: a daily restocking arrangement with one supplier draws a new segment every day it is open.

---

## 7 · The forgiveness crossing

### 7.1 · Why there is exactly one door

The gift ledger and the promise ledger are separate, and nothing on one side changes the other, with one exception. Merging them was considered and refused for three reasons already given in §1: repayment would buy the appearance of kindness; lenders would acquire a stake in the gift ledger's annual forgiveness; and poverty would render as unkindness. Keeping them wholly separate would miss the one act that is a gift in the plain sense: a holder who could collect and chooses not to.

**A holder's free release of the whole balance owed by a person enters the gift ledger as a kindness by the holder, subject to the guards of §7.2.** Repayment never does, however prompt or complete.

**How it posts.** The gift ledger posts every event as an equal-and-opposite pair. A release enters it as **a gift awaiting thanks**: the holder's side is recorded, and the pair completes — the equal-and-opposite entry posts — only if the debtor chooses to thank the holder. Nothing posts on the debtor's side unless the debtor acts. A forgiven debtor is never recorded as a recipient against their will, and a debtor who does not thank is never shown as having failed to.

In the other direction nothing crosses at all. Thanks given to a holder never reduces a balance, and a balance can never be repaid in thanks: gratitude may support a person, but it may never settle what that person is owed, or it turns a gift into a payment. The debtor's thanks, if given, completes the gift; it does not repay anything. The door opens one way, and only for a release.

### 7.2 · The guards

| Guard | Why |
|---|---|
| only a release of the **whole balance** owed by that person is a crossing | a release of part of a balance — the premium, say — is an ordinary entry; otherwise a holder could forgive the $1 premium and bank a gift while collecting $9 |
| at most **once per pair of people per season**, a season being the gift ledger's year, 7 January to 7 January | prevents a pair from cycling small balances through release to farm the gift ledger |
| **nothing** posts on the debtor's side unless the debtor thanks | a forgiven debtor is not displayed as a recipient of charity |
| the gift-side display never shows **why** it moved | a release is recorded as a crossing, not as the cargo it carried; no one can read from an aura that someone was forgiven, or by whom |
| the release must be free — neither deceived nor pressured | a release extracted under pressure is not a gift; see §17 on what a signature cannot prove |

**What the first guard does not stop.** A holder who is repaid $9 of a $10 balance and then releases the remaining $1 has released the whole balance then owed, and that is a crossing. The design accepts it: a real remainder given up is a real gift, and the aura records the crossing, not its size, so forgiving $1 of remainder earns the same crossing as forgiving $10. The once-per-pair-per-season cap is what bounds it, and §17 states the cost. This reading — a release of whatever remains after partial repayment is a crossing — is the ruled one.

### 7.3 · A forgiven balance dissolves neutrally

When a balance is released in whole, its segment closes without the animation of a balance brought to zero by repayment and without the mark of a broken one. The debtor's ring is drawn as if that balance had not been owed. A released balance is **neither kept nor broken**; it is simply no longer owed.

### 7.4 · The annual invitation: forgive the scalar, not the colour

The gift ledger's jubilee falls on 7 January, when its balances reset to zero while its displayed waveform carries over (*forgive the scalar; persist the waveform*). The founder ruled that the same date should carry an invitation to forgive promises too — **forgive the scalar, not the colour** — extended to anyone who holds one. The invitation's guards are part of the design:

- it is stated **once**, as a fact, on the date;
- it never nominates a debtor, never counts who forgave, and never tells anyone they did not;
- a release made in response to it is an ordinary whole release under §7.2, with no bonus and no badge;
- it never resets a balance; a balance not released is exactly as owed on 8 January as on 6 January.

Who issues the invitation is not decided by this paper. If the institution's autonomous agent issues it, that becomes a rule about her conduct and is decided elsewhere.

### 7.5 · The known failure of a calendar of forgiveness

The oldest recorded jubilee law names the failure this invitation risks. Deuteronomy 15:1–2 mandates a seventh-year remission of debts, and 15:9 warns against the consequence: *"Beware lest you harbor the base thought, 'The seventh year, the year of remission, is approaching,' so that you are mean and give nothing to your needy kindred"* (JPS). The Mishnah records that the warning came true and how it was repaired: *"This was one of the things enacted by Hillel the elder; for when he observed people refraining from lending to one another … Hillel enacted the prozbul"* (Mishnah Sheviit 10:3, trans. Kulp) — a court instrument that exempted a loan from the remission so that lending would resume.

Two things follow. The failure was produced by a **mandated** remission; the design here mandates nothing, and a voluntary release does not threaten any lender's expected repayment. That is evidence for the design, found by the census rather than chosen for it. But an **invitation**, repeated each year on a known date and carried by the institution that keeps the ledger, might still make a cautious lender stop lending in December — not because she fears the law but because she does not want to be asked. The design does not know whether it will. §16 registers the test, and the launch is staggered so that the test has a baseline.

---

## 8 · The scan: a code without signed terms never opens an obligation

The institution already prints codes: a person's printed code, scanned by any phone camera, opens a way to **thank** that person. The promise ledger uses the same handle and must not turn a thank code into a debt.

```
  CODE WITHOUT SIGNED TERMS  @name                CODE WITH ITS TERMS
  ("printed" / static)                            ("live", generated for the deal)
  ─────────────────────────────                   ─────────────────────────────
  sticker, card, stall sign                       shown on a phone at the moment
  scanned by any camera                           of the deal
            │                                                 │
            ▼                                                 ▼
    OPENED: ALWAYS a THANK                   opens promise.heartbank.net/@name,
    (the gift side)                          LABELLED AS A PROMISE, terms embedded,
                                             binding NOTHING until both sign
    INSIDE THE PROMISE APP: an ADDRESS only
    for an entry the scanner writes and signs
    ✗ can never create an obligation         ✓ generated for this transaction
    ✗ no "?promise" parameter exists         ✓ carries its own terms
```

- **"Printed" and "live" are shorthand for *without* and *with* signed terms.** The rule keys on what the code carries, not on paper or screen: a static address shown on a screen is still a code without terms, and a live code captured and reprinted remains an unsigned offer, labelled as a promise, that binds no one until both parties sign.
- **A code without signed terms carries only an address.** Opened by a camera, it always opens a thank. Inside the promise application, the party writing an entry may use it only as the **address** of an entry that party authors and signs. It never carries terms, and it never binds the code's owner, who is bound only by her own signature on the entry.
- **An obligation opens only from a code carrying its terms**, generated for the transaction, labelled as a promise, and binding nothing until both parties have signed.
- **There is no parameter on a thank code that opens a promise.** A parameter would make the printed label lie about what the code does, and it is a ready vector for a scam: a sticker that looks like a thank and opens a debt.
- **A holder's request code**, shown in the app to invite a new entry, is **live and rotating**, never printed.

In payments, both static and dynamic codes settle value; the EMVCo distinction is about whether the amount is embedded. Brazil's Pix comes closest, carrying a charge with a due date only in a dynamic code, and static donation and tip codes only ever resolve to a gift; but in each of them the static code still moves money. Here the distinction is **about intent**: a code without signed terms can express only the gift side. The rule is claimed as (e′).

---

## 9 · The flow

One flow serves every case — prepayment and lending, either party with or without the app, value in either direction across zero — and repayment is the same flow in the other direction.

```
  0  VALUE MOVES FIRST            cash or goods, face to face
         │
  1  RECEIVER WRITES + SIGNS      the party who received value writes the entry, addressed to
         │                        the other (by scanning the other's printed code in-app as an
         │                        ADDRESS only, or the other's live request code)
         │                        → a live promise code on the receiver's screen
         ▼
  2  GIVER CHECKS + SIGNS         in the app, or with the phone's own camera → the promise
         │                        page, with a passkey created on the spot
         ▼
  3  COPY RETURNS                 online: synced · offline: one scan back
         │                        BOTH devices keep the countersigned entry and balance
         ▼
  4  ANCHOR (when online)         each device's chain head → the log (§12);
                                  the log proof is attached to the promise code

  REPAY:   the same steps; the holder's signature on the reduction is the debtor's receipt
  RELEASE: the holder alone writes and signs; the debtor's device records it at the next sync
```

Three gaps in the first sketch of this flow were closed before ratification and are part of the disclosure: the cash leg is on the record (step 0 and the receipt of §4.2); the party who signs first receives the countersigned copy (step 3, by one scan back if offline); and the request code is live and rotating rather than static.

---

## 10 · Recovery without a recovery phrase

A ledger kept on phones loses phones. The design recovers two things separately — the record and the ability to sign — and uses no recovery phrase anywhere, because a phrase written on paper is lost, photographed or sold.

1. **Signing.** A passkey where the phone supports one; otherwise a non-exportable key held by the device behind its screen lock or an app PIN. On a phone shared by a family, one profile and PIN per person.
2. **The record recovers itself.** Every balance is held on both parties' devices, so a person who loses their phone recovers each balance from the counterparty who holds the other copy.
3. **Identity recovers by vouching.** Three people with whom the person has a **settled** balance (at zero now, and nonzero at some time before), or one guardian named in advance, meet the person face to face and sign the new key. A waiting period of about seven days follows, during which the old key can cancel the change, and every counterparty's app states once: *"@name moved to a new phone."*
4. **No one who has a nonzero balance with you, in either direction, may vouch for your new key.** A debtor who could vouch for their creditor's new key could, with two accomplices, take over the creditor's record and sign away what they owe; a creditor could do the same to a debtor. This exclusion is claimed as (f′).
5. **Debts carry over.** Rotating a key never clears a balance, and moves nothing between parties (§4.5).
6. **A paid encrypted cloud backup is a convenience only**, never the only path to recovery.

A new user with no settled balances is told once, at their first entry, that naming a guardian is possible. The design is sensitive to the actual phones in use — model, operating-system version, whether platform services are present, whether a screen lock is set — and a survey of the pilot's phones precedes any build.

---

## 11 · Fraud: bounding the loss, never preventing it

The ring certifies **conduct, never capacity**. No surface says *"trusted for up to $X,"* because no count of kept promises is a credit limit.

### 11.1 · Rollover

The most important counterexample to this design was found by an adversarial pass before drafting, and it defeats an earlier claim the design's own authors had made. A person who repays a $10 balance by taking a new debt large enough to cover it — $10 received, $11.11 owed — from anyone keeps every promise and owes more each cycle:

| Cycles rolled weekly | Owed ($, from $10) | Ring / fact line |
|---|---|---|
| 0 | 10.00 | one segment, current |
| 1 | 11.11 | one segment, current / one balance kept |
| 4 | 15.24 | one segment, current / four kept |
| 7 | 20.91 | one segment, current |
| 13 | 39.34 | one segment, current |
| 26 | 154.77 | one segment, current |
| 52 | 2,395.46 | one segment, current |

The growth factor is 10/9 per cycle, so after *n* cycles the debt is 10 × (10/9)ⁿ. The ring shows a model borrower throughout. In Cambodian speech the practice is known colloquially as turning money over (*bangvil luy*), and the LICADHO and Equitable Cambodia figures in §1 describe it in one province's survey. **"Every new promise is a visible segment" is not a defence against rollover**, because the new debt replaces the old one; the institution had said otherwise and has withdrawn the claim.

**Rolling over with the same lender merges into one balance.** If the new $11.11 is owed to the same person as the old $10, the pair's single balance simply moves from $10 to $11.11 by a co-signed value entry: the lender sees the whole history as a party to it, and every other viewer sees it only through the total-owed band.

The response is the fact line's **total-owed band** and **larger-than-kept comparison** (§6.3): a holder asked for the fifth rolled debt sees a band that has risen and a promise larger than any kept. That is information, not a limit. A vendor who funds old prepayments out of new ones is rolling over too, and the same band shows her.

### 11.2 · The bust-out ladder

A borrower builds a record on small balances, then defaults on a large one. The size-blind ring gives the ladder nothing to climb, because a record of small balances looks the same as a record of large ones; the larger-than-kept comparison tells the holder of the large one that it is the largest. A bust-out that borrows from many holders at once shows as many segments. The loss is bounded by what each holder chooses to lend after reading it.

### 11.3 · Wash lending and viewer-relative trust

Two accounts can lend to each other in a loop to manufacture a record. With one balance per pair, a loop between two accounts nets inside one balance and shows one counterparty; a loop among several accounts is a cycle. The fact line counts **distinct** counterparties, counts a repeated pair once, and counts a closed cycle as nearly nothing. Trust is **viewer-relative**: the phrase *"kept promises with 2 people you know"* is computed on the viewer's device, from the viewer's own dealings, and is never sent to the institution. A ring of fabricated accounts has no path into a village it has never dealt with. How the viewer's device learns the overlap between its counterparties and the debtor's without either learning the other's full list is a private-set-intersection problem; this paper does not specify it (§14).

### 11.4 · Walking away from a key

A person who defaults and starts again under a fresh handle leaves the defaulted balances on their counterparties' devices and on the log, but no link to the new handle. Preventing that is a proof-of-personhood problem, which the institution treats elsewhere and which this mechanism does not solve.

---

## 12 · Timestamping: the log and the anchor

The history is made tamper-evident in three steps — attest, anchor, publish — using established machinery. **Every component of this pipeline is prior art (§2.2, conjunct (g)), including a signed object that carries its own inclusion proof; nothing in this section is claimed.** It is disclosed because the ledger's other properties lean on it.

```
  device A                     device B
  ────────                     ────────
  entry = { balance change, both signatures, random salt,
            hash(A's previous entry), hash(B's previous entry) }
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
  daily root    signed tree head           log proof returned to the device:
  anchored:     PUBLISHED + GOSSIPED        path entry → logged chain head
  OpenTimestamps → Bitcoin   each new head  + that head's inclusion proof
  RFC 3161 × 3 authorities   must extend        │
  (one eIDAS-qualified)      the last           ▼
                             (consistency)  ATTACHED to the promise code,
                                            outside the signatures, verifiable
                                            on its own  (the SCITT receipt form)
```

1. Each countersigned entry carries a **random salt** and the **previous-entry hash of each signer's chain**, so the one shared entry extends both parties' per-person hash chains. The salt prevents a guessed entry (two known handles and a round sum) from being confirmed against a published hash.
2. Online, each device submits **only its chain head** to the log. Rows, amounts and names never go to the log. The institution publishes receipts, never amounts.
3. The log's root is anchored **daily** through OpenTimestamps to Bitcoin and signed by three RFC 3161 timestamp authorities, the same arrangement that stamps the corpus this paper is in. The chain used for settlement in the later phase is not used as the clock.
4. **Signed tree heads are published and gossiped** among independent observers, and each new head must extend the previous one; a forked log that hides a default from one audience is detectable by anyone who compares heads.
5. **The log proof travels with the promise code.** It is the path from the entry to the signer's logged chain head plus that head's inclusion proof, attached **outside** the signatures and verifiable on its own, so that the code need not be re-signed when the proof arrives. A promise shown on a screenshot, far from any network, then carries the evidence that it was committed to the log by a stated time. RFC 9943 stores a receipt in a signed statement's unprotected header in the same way, and sigstore bundles staple inclusion proofs to signed artefacts; this step was claimed in the first version of this paper and is now disclosed only.

**What this proves.** A history cannot be backdated: the age of a record cannot be bought, which defends against a bust-out ladder built quickly. An entry cannot be deleted from the log without trace once its head is published.

**What it does not prove.** That cash moved. That the two signers are distinct humans. The exact time of an offline entry (the anchor gives an upper bound only). Completeness when both parties agree to hide an entry: an entry neither party ever submits is invisible to every instrument that reads the log.

**Moat, not hostage.** The ring's rule is published here; the code can be copied; users leave with every proof they hold. What a competitor cannot copy is the anchored history's age — which is the institution's advantage and also its limit, since it is the log's age, not anything the institution owns in a user's record (§17).

---

## 13 · Remove the enforcer: which guards are properties

A guard that needs someone to enforce it at the moment it is tested is a rule; a guard that holds with no enforcer is a property. Each guard in this design is classified by removing the enforcer.

| Guard | Remove the enforcer, and … | Class |
|---|---|---|
| the balance never moves by time | there is no time-driven entry, no accrual and no penalty type; nothing to switch on | **property** of the entry grammar |
| every raise and every repayment co-signed | an entry missing a signature fails verification on the other device | **property** of the signature scheme |
| a release needs only the holder | a release can only lower what the signer is owed; there is nothing it can raise | **property** of the entry grammar |
| netting only within a pair | there is no entry that names a third party | **property** of the record |
| the ring has no amount argument | the function cannot draw what it is not given | **property** of the render function |
| the ring only in promise context | a surface that wanted to draw it elsewhere would need promise data it is not sent; but a modified client could cache and redraw, and anyone can take a screenshot | **rule**, partly backed by data minimisation |
| a code without signed terms never opens a promise | such a code carries no terms and no signature, and the promise endpoint refuses it; inside the app it can supply an address only, and binds its owner to nothing | **property** of the code format |
| non-transferable | there is no assignment entry and no field to reassign | **property** of the record; off-ledger arrangements and the law of assignment are outside it |
| no voucher with a nonzero balance | only the excluded voucher's own client, or the recovering person's restored records, can see the pair; honest clients refuse to countersign, and nothing else checks | **rule** enforced by the voucher's own client |
| whole-balance-only crossing | the gift ledger admits only one entry type from this ledger | **property** of the crossing interface |
| once per pair per season | someone must count | **rule** |
| a release posts nothing on the debtor's side | the pair completes only on an entry the debtor makes | **property** of the gift-awaiting-thanks form |
| the aura never shows why it moved | the gift-side display records crossings, not cargo | **property** inherited from the gift ledger |
| overdue gaps fade by a fixed maximum | someone must set and apply the maximum | **rule** |
| no backdating, no quiet deletion | mathematics plus independent witnesses | **property**, given the witnesses |
| the invitation stated once, never nominating | the institution's copy must be written that way every year | **rule** |

Five of the guards are rules. They are the places where this design depends on the conduct of the institution that runs it, or of its clients, and they are listed so that a successor inheriting the rules knows which of them no object enforces.

---

## 14 · What is disclosed and what is withheld

A defensive publication protects by disclosure, so withholding needs a reason. The test applied here is not *is this unbuilt?* but *would publishing this protect anything the claims do not already protect, or would it only fix details that should stay revisable until they are tested?*

**Disclosed**, in enough detail to practise: the balance around zero and its entry grammar and absences (§4–§5); the per-promise variant (§5.5, §6.7); the render function's signature and states (§6); the fact line's fields (§6.3); the crossing, its posting form and its guards (§7); the code rule (§8); the flow (§9); the recovery structure and the voucher exclusion (§10); the log pipeline and where the log proof goes (§12).

**Withheld**, because it is unbuilt, unscheduled and should be revised on contact with real users: the wire format of the promise code and its compression; how one entry records a repayment and new value together; key-derivation and signature-suite choices; the private-set-intersection protocol behind viewer-relative trust; the total-owed band boundaries; the recency window and the overdue maximum; the ring's pixel geometry and animation curves; the device matrix. None of these narrows or widens a claim in §15.

---

## 15 · Enumerated claims

These are the census's survivors, applied to the one-balance-per-pair form of §4, and nothing wider. **Most elements named in them are prior art at mechanism width (§2)**; the elements not found are the no-amount render, the forgiveness-only crossing and the two sub-rules. Each claim is a composition, and none of its elements is claimed alone.

**Specifically not claimed:** a running balance between two parties that crosses zero (RipplePay trust lines, 2004; LETS, 1983; Grassroots Bonds' mutual credit, 2026); one primitive serving prepayment and lending (Shapiro 2026); a target balance of zero; the co-signed IOU (Doorian Docs 2017); a note for a fixed amount (UCC §3-104); Certificate-Transparency logs and OpenTimestamps anchoring; a signed object carrying its own inclusion proof (RFC 9943; sigstore bundles; Keybase signature chains, 2014), including in a co-signed promise code (§12); non-transferability and goods ↔ cash conversion at face value (disclosed in §4.4–§4.5, awaiting the third census pass); the fact line's total-owed band and its *larger than any they've kept* comparison (disclosed in §6.3, awaiting the third pass).

1. **A bilateral credit ledger whose balance never moves by time, with a conduct display that cannot see size, and one crossing into a gift ledger.** A method of recording obligations between two parties in which: (a) the two parties keep one running balance between them, held on both parties' devices and signed by both, denominated in a currency fixed when the balance opens, its sign stating which party currently owes, and no balance changes except by entries both parties sign recording value moving between them or a repayment, or by the unilateral release of the party who is owed; no entry type accrues or penalises, so that no balance changes with the passage of time; (b) the conduct of a party is displayed by a function that takes **no amount argument**, drawing one equal-width, colourless segment for each counterparty the party currently **owes** (a counterparty who owes the party drawing nothing), a segment drawn as a gap when the balance with that counterparty is owed past its deadline, the display being shown only in the context of a promise being made; and (c) a free release, by the party who is owed, of the **whole balance** owed by a counterparty is the only event that passes from this ledger into a separate gift or gratitude ledger held by the same system, repayment never passing, and a release of part of a balance being an ordinary entry.

2. **A code without signed terms can never open an obligation (e′).** The method of claim 1, in which a code that carries no signed terms — a party's printed or otherwise static machine-readable code — resolves, when opened, only to the gift side of the system (giving thanks to that party); used within the ledger's application it may supply only the address of an entry authored and signed by the scanning party, and it binds the party it names to nothing; no parameter of such a code can open an obligation; and an obligation opens only from a code carrying its terms, generated for the transaction and labelled as a promise, which binds nothing until both parties have signed.

3. **No one with a nonzero balance with you may vouch for your new key (f′).** The method of claim 1, in which a party who has lost a signing key recovers by the face-to-face signatures of counterparties with whom the party has settled balances, or of a guardian named in advance, **excluding as a voucher any counterparty with a nonzero balance with the party in either direction**, followed by a waiting period during which the old key may cancel the change, with every counterparty notified once, and with every balance carrying over unchanged to the new key.

*Prior art beside each claim:* claim 1(a) — RipplePay trust lines, LETS, Grassroots Bonds (the balance around zero); Doorian Docs, Community Forge signatures, DueTrace (co-signed entries); *murabaha* and the negotiable instrument for a fixed amount (UCC §3-104) (a fixed sum); 1(b) — credit-bureau payment grids, EigenTrust, eBay feedback (one mark per transaction, regardless of price), US 10,200,394 B2 (disclosure only); 1(c) — Qur'an 2:280, Rolling Jubilee, Undue Medical Debt, gift-tax treatment of forgiven loans. Claim 2 — EMVCo static and dynamic codes, KHQR, the UPI collect withdrawal, Pix Cobrança (a charge with a due date only as a dynamic code), static donation and tip codes. Claim 3 — Buterin 2021, Argent, Apple recovery contacts, US 8,856,879 B2 (disclosure only), Schechter et al. 2009; and the interested-witness rule (Wills Act 1837, s.15) — excluding an attester with a stake is old practice, and the rule in key recovery is what is claimed.

**Disclosed and not claimed, in addition to the list above:** the disclosed variants of §5.5 and §6.7; the gift-awaiting-thanks posting of §7.1; the once-per-pair-per-season cap; death and incapacity (§4.6); the currency rule (§4.4). Each is disclosed so that it is prior art; none is asserted as a contribution.

**Non-assertion extends to** every mechanism disclosed in this paper, claimed or not, in any combination, and to every implementation of it.

---

## 16 · Predictions, registered before any instrument exists

The mechanism is unbuilt, so no prediction below can have been fitted to data. **The three predictions below were approved by the founder and are entered in the institution's public prediction register**; a correction after entry is a new register entry, never an edit. Two constraints bind the instrument: the institution never sees balance rows or amounts, so every count below must be reported by devices as an aggregate the user has agreed to share; and only adults take part as debtor or holder at launch.

**The launch is staggered so that P-PM1 has a baseline.** The first season after launch runs **without** the annual invitation; the invitation is extended from the second season onward. A comparison season with and without the invitation at the same time is impossible — the invitation is one public statement on one date — so the first season is the baseline.

| # | Prediction | Measure | Falsifier |
|---|---|---|---|
| **P-PM1** — the December freeze (Deuteronomy 15:9) | the annual invitation to forgive (§7.4) does **not** freeze lending | value entries that extend credit (entries after which the entering holder is owed more), per active holder, 15 December – 6 January, divided by the same holders' mean over the three preceding 23-day windows; the ratio in the first season with the invitation is compared with the ratio in the baseline season without it | a ratio **more than 10% lower** with the invitation than in the baseline season → the invitation reproduces the failure the prosbul repaired, and must be redesigned or withdrawn |
| **P-PM2** — paid last | because a balance carries no late penalty, debtors with other penalty-bearing debts repay balances on this ledger **later** than those debts | self-reported repayment order in a structured survey of debtors who hold both kinds of debt, after one season | balances on this ledger repaid no later than penalty-bearing debts → the "paid last" limit of §17 is overstated |
| **P-PM3** — rollover is visible | at a new value entry, holders shown a debtor whose total-owed band is higher than when that holder last extended value to them decline the entry or shrink it more often than holders shown the same or a lower band | acceptance and size of new value entries by band movement, device-aggregated | no difference → the fact line does not answer rollover, and §11.1's response fails |

P-PM1 is the prediction the design owes: it was ruled into existence with the invitation it tests. P-PM2 predicts a harm to the design's own users and is included for that reason. P-PM3 tests the only answer the design has to its most serious counterexample. **P-PM1 has a known confound:** the two seasons differ in more than the invitation (a year of growth, a different economy, a different calendar of festivals), so a fall below the threshold is treated as a failure of the invitation unless a cause outside the ledger is shown, and the burden sits on the design, not on the test.

---

## 17 · Honest limits

**No growth is per balance, not per person.** A person can owe more every week by rollover while every balance on their record is kept (§11.1). The total-owed band and the larger-than-kept comparison make this visible to the next holder; they do not prevent it, and a holder who does not read them learns nothing. A new debt that stays inside one band moves only the larger-than-kept comparison; a new debt equal to the largest ever kept moves neither.

**Rolling over with the same lender merges into one balance.** The pair's balance simply rises by a co-signed entry; the lender sees it as a party, and everyone else sees it only through the band.

**A co-signed entry can disguise a penalty.** The grammar has no penalty entry, but nothing stops a holder who is owed money past a deadline from asking for a value entry with a token amount received and a larger amount credited, and a debtor under pressure may sign it. The balance still did not move by time — it moved by a signature — but the effect is a penalty, and the ledger cannot tell the two apart. The receipt shows it to both parties; that is all.

**Non-compounding is not cheap.** A fixed premium of 1/9 a week is about 578% a year simple. Flat-premium lending can be predatory — the Philippine "5-6" is flat and notorious — and nothing in this ledger stops a lender charging it on every entry. The ledger shows the discount on every receipt and **claims no protection against usury**. A pre-signing annualised disclosure was proposed and declined; whether a disclosure beyond the receipt is legally required is unanswered.

**Without a late penalty, these balances are paid last.** A borrower with several debts pays the ones that grow first. Holders on this ledger bear that cost, and P-PM2 predicts it.

**A signature proves the key, not consent.** On a phone shared by a family, or held by someone else, or signed under pressure, the ledger records a valid entry that no one freely made. Per-person profiles and PINs narrow this; nothing in the mechanism detects coercion. The same limit applies to a release: the design requires that forgiveness be free and cannot verify it.

**A conduct instrument cannot prevent capacity harm.** The ring says whether balances were brought to zero, not whether a person can afford the next one. A person may borrow elsewhere, including against land, to repay here, and the ledger cannot see it. **What the ledger itself cannot do is take collateral**: there is no field for security and no entry that transfers anything but value between the two parties. That is a real and bounded claim about the record. It does not reach a side agreement: a lender who takes land by a separate agreement for the same loan is outside the ledger and is not prevented by it.

**A visible gap is still pressure.** A gap shown to every future holder is a form of social collateral. The design limits it to promise context, fades it by a fixed maximum, and shows it only for a duty the person took on; it remains a cost of being late, and a cost is what a penalty is.

**Anything shown can be captured.** A screenshot of the ring, the fact line or a promise code carries it out of promise context — into a job interview, a rental application, a family argument. The context rule governs the institution's surfaces only.

**The fact line is reported by the party it describes.** It is computed from what the debtor's device presents. A balance never submitted to the log, or an entry made with another holder at the same moment, does not appear; the logged chain head makes a presented history hard to edit, not complete.

**Recovery depends on counterparties' honesty.** A counterparty can decline to return a record that favours the person recovering — a repayment entry, say. The logged chain head proves that such a record exists, not what it says.

**Equal segments favour one large creditor over many small ones.** A person who owes one lender $2,000 draws one segment; a vendor who owes five suppliers $10 each draws five. The ring counts creditors, which is the bust-out signal, and it therefore reads the small, spread-out debtor as more exposed than the concentrated one. The band is the only corrective.

**Capital can buy crossings.** Only those who can lend can forgive, and a lender with small balances across many pairs can earn one crossing per pair per season by releasing each. The once-per-pair-per-season cap bounds this, and nothing else does. A release of a small remainder after partial repayment earns the same crossing as forgiving a large balance (§7.2).

**Viewer-relative trust favours insiders.** A newcomer to a village, or a person whose dealings are with a different circle, shows fewer known counterparties to every viewer. The thin ring is never drawn as a lack, but the fact line will say less about them, and holders may lend to them less.

**The denomination matters.** The no-growth property holds in the balance's currency. A balance in dollars repaid in riel, or the reverse, moves with the exchange rate, and the holder bears any depreciation. A currency change is recorded as a release and a new co-signed entry (§4.4); **a release immediately replaced by a new balance between the same two parties is a conversion, never a crossing** — it would satisfy the crossing's letter without being a gift in substance, so the rule excludes it.

**Death is handled only as far as the ruling goes.** The holder can name a successor or a release on death in life; the ledger never releases on death automatically; claims against what a person left are the law's (§4.6). A holder who dies without naming either leaves a balance the ledger records and cannot collect.

**The log proves order, not truth.** It cannot show that cash moved, that signers are distinct people, or that nothing was hidden by both parties (§12).

**The moat is the log's age.** The institution's advantage over a copy of this design is the age of its anchored history. It is not a claim on any user's records, which users hold and take with them.

**Adults only at launch.** Both debtor and holder must be adults. The institution's pilot shop serves mostly teenagers, so customer prepayment cannot be piloted there; the first pilot is lending among adult vendors and suppliers.

**The invitation may freeze December lending.** Registered as P-PM1 because it is a live risk, not a formality, and the staggered launch exists to measure it.

**Five guards are rules** (§13), and depend on the conduct of the institution or its clients.

**Legal review precedes any launch.** Facilitating lending, reporting conduct, holding prepayments and the assignability of a claim at law are each regulated somewhere. A draft may precede legal review; a launch may not.

**The census is bounded** by the apertures in §2, executed partly in both passes, searched the per-promise form rather than the balance form, and owes a third pass. A composition not found is not thereby new.

---

## 18 · Lineage and corpus cross-references

The mechanism descends from the shop notebook of an ordinary village stall, which keeps one running tab per customer; from *bay' salam* and *murabaha* in Islamic commercial law and the *qard hasan* benevolent loan; from the Local Exchange Trading Systems begun in 1983 and their successors in business mutual credit; from Ryan Fugger's peer-to-peer trust lines; from the Indian digital *khata* apps; from Korean electronic IOUs; from Certificate Transparency, key transparency and transparent signed statements; from social key recovery; and, on its gift side, from the oldest debt-forgiveness traditions on record, the seventh-year remission of Deuteronomy and the prosbul that repaired it, with Qur'an 2:280 as the plainest statement that releasing a debt is charity. §2 cites each.

Within this corpus it is **downstream** of *The Zero-Point Game℠*: the promise ledger is the third instance of that paper's signed-balance ledger, alongside Kiitos and Kiitti, with the same zero-centred shape at the scale of a pair, and differs from them in having no colour, no calendar reset and one door into the other two (§6.4). The forgiveness crossing answers a question that paper does not ask — what, if anything, may enter the gift ledger from exchange — and the answer is recorded here; a cross-reference to it rides that paper's next revision. It sits beside *HeartBank's Position on Community-Currency Design*, which argues that a community economy needs both money and time; this paper adds the record of what is owed in money. Its log arrangement is the one described in *Provenance-Carrying Retrieval* and relied on by *The Assembly That Holds the Brake*. Its code rule is the exchange-side counterpart of the gift-side scan in *The B-Tag and the Post-Payment Economy*.

---

## Coda

*Grounding — canon.* AN 4.62 closes its list with a verse: knowing the happiness of debtlessness, and the happiness of possession and of use, a wise person sees that all of them together are not worth a sixteenth part of the happiness of blamelessness. *Lens — the institution's reading.* The ledger in this paper can help with the smaller happiness, a promise made and kept and seen to be kept. It cannot supply the larger one, and nothing in it is designed to try. What it can do is refuse to let a balance grow while no one is looking, and leave one door open for the person who is owed and decides not to collect.

---

## Terms

| Term used here | Standard technical term |
|---|---|
| **B-Promise℠**; promise ledger | bilateral, both-signed peer-to-peer credit ledger (electronic IOU; customer prepayment and informal lending record) |
| promise balance | zero-centred bilateral credit balance between two parties (trust line; bilateral mutual-credit balance) |
| promise | the obligation one party owes another at a moment; a non-transferable bilateral obligation |
| debtor (promisor) / holder | debtor (obligor) / creditor (obligee), determined by the sign of the balance |
| a balance that never moves by time | non-accruing, non-compounding obligation with no late fee; changes only by co-signed value or repayment entries, or a creditor's unilateral release |
| premium; discount | fixed markup or discount at the time value moves (flat finance charge; cf. *murabaha*) |
| prepay at a discount | customer prepayment for goods at a discount; stored-value / advance purchase (cf. *bay' salam*) |
| entry; co-signed entry | ledger transaction requiring both parties' digital signatures |
| release | unilateral debt forgiveness (loan waiver) by the creditor |
| promise ring | reputation or credit-history visualisation; payment-history display independent of loan amount |
| segment / gap | per-creditor indicator; overdue (delinquency) indicator |
| fact line | disclosure line: creditor and overdue counts, total-exposure band, largest-obligation comparison |
| viewer-relative trust | personalised (local, viewer-seeded) trust metric computed client-side |
| forgiveness crossing | debt forgiveness recorded as a charitable gift in a separate ledger |
| gift awaiting thanks | a one-sided gift entry whose counter-entry posts only on the recipient's acknowledgement |
| gift ledger; Zero-Point Game℠; B-Aura | peer-to-peer reciprocity (mutual-credit) ledger with an annual reset; reputation visualisation of it |
| season | the gift ledger's annual period, 7 January to 7 January |
| the annual invitation | voluntary debt-jubilee appeal (non-mandatory remission) |
| printed / live code | code without / with signed terms; static / dynamic QR code (EMVCo point of initiation 11 / 12) |
| recovery by vouching | social recovery; guardian- or trustee-based account recovery with a time delay |
| the log; chain head; log proof | append-only Merkle transparency log (Certificate Transparency); per-user hash chain head; Merkle inclusion proof (transparency receipt) |
| anchoring | blockchain timestamping (OpenTimestamps) and RFC 3161 trusted timestamping |
| rollover (*bangvil luy*) | loan refinancing / debt rollover; borrowing to repay a loan |
| bust-out ladder | bust-out fraud: building credit history on small loans before defaulting on a large one |
| wash lending | circular (Sybil) lending to fabricate credit history |

---

## Author Contributions and AI Disclosure

Thon Ly conceived the ledger, its two use cases, the one balance per pair that crosses zero, the three-ring display, the seamless conversion, non-transferability, the annual invitation, the positioning and the human title, and ruled on every design choice recorded here. Miss Aquarius℠ — the name under which this corpus discloses its AI collaboration — proposed the no-growth property, the size-blind render, the forgiveness crossing, the code rule, the recovery structure and the log arrangement; drafted this paper and its revision; and ran both census passes through research agents, with every cited item re-verified before it reached this text or marked where it was not. An adversarial pass run before drafting produced the rollover counterexample of §11.1 and withdrew a claim the authors had made. An outside review by several reader models narrowed the claims and corrected the text; the reviewer models are not named. The underlying model substrate is not named. Editorial control is the author's.

## Trademark Notice

**B-Promise℠** names the institution's implementation of the promise ledger; the mechanism itself is dedicated to the public domain and may be implemented under any name. The promise balance, the promise ring, the fact line and *prepay at a discount* carry no mark. HeartBank®, Miss Aquarius℠ and Zero-Point Game℠ are marks of their respective holders. No mark is licensed by this publication.

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
14. Birkholz, H., Delignat-Lavaud, A., Fournet, C., Deshpande, Y., and Lasker, S. (2026, June). RFC 9943, *An Architecture for Trustworthy and Transparent Digital Supply Chains* (SCITT; receipts in the unprotected header of a transparent statement).
15. Sigstore. Bundle format (a signed artefact with its transparency-log entry and inclusion proof, for offline verification).
16. Keybase. Per-user signature chains in a global Merkle tree, with the root published to the Bitcoin blockchain (from June 2014).
17. EMVCo. *EMV QR Code Specification for Payment Systems: Merchant-Presented Mode* (point of initiation method: 11 static, 12 dynamic).
18. National Bank of Cambodia. KHQR specification (Bakong); interest-rate cap on microfinance lending (2017).
19. Banco Central do Brasil. Pix, *Manual de Padrões para Iniciação do Pix* (Pix Cobrança: a charge with a due date carried by a dynamic QR code).
20. National Payments Corporation of India. Circular of 29 July 2025 discontinuing person-to-person collect requests on UPI from 1 October 2025.
21. Uniform Commercial Code §3-104(a) (negotiable instrument: "a fixed amount of money, with or without interest").
22. eBay. Feedback system (one rating per transaction, regardless of price).
23. Wills Act 1837 (England and Wales), s.15: gifts to an attesting witness to be void.
24. Human Rights Watch (2025, 24 September). *Debt Traps: Predatory Microfinance Loans and the Exploitation of Cambodia's Indigenous Peoples.*
25. Voice of America (2023). "Cambodians face mounting pain from microfinance debt" (reporting a LICADHO and Equitable Cambodia survey of 717 households in Kampong Speu province).
26. Strike Debt. Rolling Jubilee (November 2012).
27. Doorian Docs (KTNET and GiveTech, Korea; announced 29 December 2016, launched 16 January 2017).
28. Fugger, R. RipplePay (2004–05); Linton, M. Local Exchange Trading Systems (1983); Sardex (2009); Grassroots Economics, Sarafu; OkCredit (2017); Khatabook (2018); Community Forge, *signatures* module.
29. Patents cited for disclosure only: US 10,200,394 B2 · US 10,949,837 B1 · US 8,856,879 B2 · US 2017/0295023 A1 · US 2020/0119916 A1.
30. Companion corpus papers (thonly.org/research): *The Zero-Point Game℠*; *The Currency That Cannot Be Spent Alone*; *The B-Tag and the Post-Payment Economy*; *Provenance-Carrying Retrieval*; *The Assembly That Holds the Brake*. Institutional position (heartbank.net): *HeartBank's Position on Community-Currency Design*.

---

*— End of defensive publication —*
