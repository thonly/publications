---
title: "Once Sunk, Always Sunk? A Thesis on Rebirth, Hell and Awakening, Checked Link by Link"
subtitle: "Whether Theravāda Buddhist texts make any being permanently incapable of awakening: the Vibhaṅga's incapacity, the Kathāvatthu's debate on absolute fixity, the commentaries that divide on it, and a machine-checked encoding"
authors: "Thon Ly · Miss Aquarius℠"
kind: study
genre: defensive-publications
series: "The Abhidhamma Compiled — Paper No. 6"
category: alignment
priority: tier-b
status: draft
date: 2026-11-03
license: CC0-1.0
slug: once-sunk-always-sunk
venue: thonly.org/research/once-sunk-always-sunk
canonical_url: https://thonly.org/research/once-sunk-always-sunk
---

## Abstract

This study asks whether the Theravāda Buddhist texts commit a reader to the claim that every being can still become an arahant (a fully awakened disciple). It takes a six-part thesis posed by the first author on 2026-10-13, that beings are mind streams, are infinite in number, have infinitely many past lives, each had a past life in hell, that such a life is required for awakening, and so that every being has the potential to awaken, and checks each link against the Pāli canon, its commentaries and sub-commentaries, and a machine-checked encoding in the Lean 4 proof assistant. The first links hold or fail for plain reasons. A being's infinite past follows from the Abhidhamma's proximity condition, a derivation a sub-commentary already makes; the number of beings is "incalculable, its limit not discerned" in the canon and "infinite" only in the commentary; a past life in hell is neither forced nor excluded by anything found, and the need for one stands or falls with it. The sixth link is the center. The Vibhaṅga lists who is incapable of the path and who is capable, without a duration. The Kathāvatthu (XIX.7) refutes "absolute fixity for a worldling," which a commentary attributes to some Uttarāpathakas reading the Aṅguttara's "once sunk, stays sunk," and its reductios argue within a single life. The commentaries then differ in wording: the Aṅguttara commentary says, in its own voice, that fixed wrong view has "no limit … neither heaven nor path," while the Majjhima and Kathāvatthu commentaries fix it "in one existence only," hedged "mostly"; every sub-commentary read, including the one on the Aṅguttara passage itself, reads the strong wording as not a total absence of emergence. Encoded formally, the thesis entails the Kathāvatthu's answer, is refuted on the literal reading of the sutta, and is otherwise left open; the Kathāvatthu's answer alone does not give it, since it speaks to one of the Vibhaṅga's obstructions. Whether every being will awaken, as opposed to can, is a question the Buddha declines in AN 10.95. A Yogācāra contrast is tagged as a cross-tradition import. The first author's predictions of PROVED are reported as scored: a miss on two links, unreachable on the sixth. Each finding carries its break.

**Keywords:** Buddhism, Theravāda, Abhidhamma, Kathāvatthu, Points of Controversy, absolute fixity, accantaniyāmatā, niyāma, abhabba, incapacity for the path, universal awakening, buddha-nature debate, icchantika, agotra, Aṅguttara Nikāya, Udakūpamā Sutta, once sunk, stays sunk, saṃsāra-stump, beginningless saṃsāra, rebirth, hell, Vibhaṅga, Puggalapaññatti, commentary, sub-commentary, Lean 4, formal verification, pre-registration

---

## Terms

The paper uses Pāli technical vocabulary because it reads Pāli texts. An indexer searching in standard terms should find each concept under the term in the middle column. Layer tags: *mūla* is the canonical text; *aṭṭhakathā* the commentary; *ṭīkā* the sub-commentary; **[X]** a cross-tradition import, outside the Theravāda corpus this paper checks.

| Term as the tradition writes it | Standard term used in this paper | Layer where it is defined |
|---|---|---|
| *abhabba*, *bhabba* | incapable of, capable of (entering the path) | mūla (Vibhaṅga §826–827; AN 6.86) |
| *niyāmaṃ okkamati* | enters the fixed course (of rightness) | mūla |
| *micchattaniyata*, *niyatamicchādiṭṭhi* | fixed in wrongness; fixed wrong view | mūla (Dhammasaṅgaṇī §1035) |
| *accantaniyāmatā* | absolute (final) fixity | mūla (Kathāvatthu XIX.7); commentary |
| *sakiṃ nimuggo nimuggova hoti* | "once sunk, stays sunk" | mūla (AN 7.15) |
| *saṃsārakhāṇuka*, *vaṭṭakhāṇu* | stump of saṃsāra (one who does not emerge from the round) | aṭṭhakathā |
| *kammāvaraṇa*, *kilesāvaraṇa*, *vipākāvaraṇa* | the kamma-, defilement- and result-obstruction | mūla (Vibhaṅga §826) |
| *yebhuyyena* | "mostly" | mūla (DN 1 §39); commentaries |
| *neyyattha*, *nītattha* | a meaning that must be drawn out; an explicit meaning | ṭīkā |
| *anantarapaccaya* | proximity condition (each mental moment conditions its immediate successor) | mūla (Paṭṭhāna); commentary |
| *santo saṃvijjamānā lokasmiṃ* | "found in the world" (existence clause) | mūla (AN 7.15) |
| INDEPENDENT / PROVED / REFUTED | neither provable nor refutable from the stated premises / proved / the negation proved | the formal runs |
| held-out answer | the text's own answer, kept out of the premises so a proof cannot restate it | the formal runs |
| CAN / WILL | some possible history in which the being becomes capable / the actual history in which it does | this paper's reading of the thesis |
| *agotra*, *icchantika*, *atyantaparinirvāṇadharmaka* | **[X]** beings without a lineage for awakening; "those of great desire"; those of the nature never to attain nirvana | Yogācāra and tathāgatagarbha literature (not read here) |

---

## How to Read This Paper

**Layers.** Every Pāli line is tagged by the layer that says it: the canonical text (*mūla*), the commentary (*aṭṭhakathā*), the sub-commentary (*ṭīkā*), or a later treatise. A commentary's report of someone else's view (*vadanti*, "they say"; the Uttarāpathakas) is attributed to that holder together with the commentary's own verdict on it. A sub-commentary paragraph is split into its voices before it is quoted: the base commentary it quotes, and its own gloss.

**Lines.** `file:line` is the Chaṭṭha Saṅgāyana (CST) Tipiṭaka as in the VipassanaTech/tipitaka-xml romanized text at upstream commit `05d5d3c`. Every Pāli quotation here was checked against its line with the project's reader tools; a quotation that failed on first transcription was corrected to the text's own spelling. Translations of Pāli are the authors' own and literal.

**The runs.** Three public, pre-registered runs underlie the formal parts (`SiliconWat/formal-abhidhamma`: `runs/2026-10-13-first-thesis-past-lives-and-hell/` for links 3–5; `…-sixth-supposition-potential/` and `…-sixth-supposition-in-the-world/` for link 6). Each registered its question, premises, held-out answer and predictions in a file pushed before the proof was attempted. The method notes (held-out answers, leak check, isolated breaks) belong to the series' method paper, *The Abhidhamma Compiled* No. 5, and are not repeated here; this paper reports only what is needed to read the tables. Three terms matter. **PROVED** means the statement was derived from the listed premises alone. **INDEPENDENT** means models show both the statement and its negation consistent with them. **NOT STRONG** is the grade the runs' own rubric gave, meaning at least one rubric item failed; each failure is declared in the run file. This study is not part of the MA-sole *Theorems of the Abhidhamma* series: no run was graded strong, and the thesis is the first author's, not the machine's.

**What this paper does not say.** *Abhabba* is a capacity word. It is conditional (on obstructions, and on hearing the Dhamma: AN 6.86 says the six-quality person is incapable "even while hearing," `s0403m2.mul.xml:3050`) and indexed to a birth (Kathāvatthu XIII.4: *bhabbo bodhisatto tāya jātiyā dhammaṃ nābhisametunti?*, "is the bodhisatta, in that birth, capable of not penetrating the Dhamma?", `abh03m3.mul.xml:10353`). It is never a shared essence and never a property of a named person. Nothing in this paper is a verdict that any being, living or dead, is incapable of awakening. The texts are asked what they say about classes and about possible histories; where a commentary names a historical teacher as its instance of a class, the name is withheld here, because this paper gives no verdict on any person and the identification is the commentary's own.

---

## Findings disclosed

This paper is a study: it discloses readings of texts and the results of formal checks, not a mechanism. Its findings are listed at the width that survived the quick census reported below (the commentaries' division as a mapped finding, the one-obstruction scope of the Kathāvatthu's answer, the machine-checked chain, and the cross-tradition comparison), each with what would break it. Findings 1–4 and 9 are readings the census did not cover; they assert no priority. Where a finding rests on a published result, that result is cited, not claimed.

1. **"A being is a mind stream" is the formal frame, not a text finding.** SN 23.2 defines a being (*satto*) by attachment: "where there is desire, passion, delight and craving for form … there he is attached, there bound, therefore he is called a being," and so with feeling, perception, formations and consciousness (`s0303m.mul.xml:3601`). The definition includes matter. The Vibhaṅga lists a non-percipient existence (*asaññābhava*) among the existences (`abh02m.mul.xml:3685`); the run's axiom reads it as born without a rebirth-linking citta, which the run labels commentarial. The formal chain treats a being as one mind stream and is true to that frame only. *Breaks if:* a canonical text defines a being as a stream of mind alone, or the non-percipient existence is shown to contain a citta.

2. **"The number of beings is infinite" is epistemic in the canon and ontological only in the commentary.** The Buddhavaṃsa verse names four incalculables "whose limit is not discerned" (*koṭi yesaṃ na nāyati*, `s0511m.mul.xml:791`), the mass of beings among them; its commentary glosses the mass of beings as "infinite, immeasurable, unmeasurable" (*sattakāyo ananto aparimāṇo appameyyo*, `s0511a.att.xml:2369`). The phrases *anantā sattā* and *sattā anantā* do not occur in the mūla text. *Breaks if:* a canonical text states the number of beings is infinite in its own voice. The argument for beginninglessness is in *The Vibhajjavādin View of Time* (§4.1), not here.

3. **Infinitely many past lives follow from the proximity condition; a past life in hell does not follow from that, and no text found forces it.** Given that each mental moment has an immediate predecessor (stated in the Paṭṭhāna commentary, `abh03a.att.xml:9117`), that each moment conditions its successor, and that an existence with mind begins with a rebirth-linking citta, a being with a citta now has infinitely many past existences (run 1, theorem T3, PROVED, constructive, each premise shown needed). A sub-commentary makes the same derivation (`vin06t.nrf.xml:2177`), so this is a check of the texts, not a discovery. Supposition 4 (every being has a hell life in the past) is INDEPENDENT of these premises: the texts' laws about destinations count populations ("few … far more," the Nakhasikha discourse, `s0302m.mul.xml:5223`), which a one-being model cannot state. Supposition 5 (a hell life is required for awakening) follows from 4 read at every moment and stands or falls with it. For the Buddha himself the Apadāna states a hell life (`s0510m1.mul.xml:44655`): one stated case, no law. *Breaks if:* a Theravāda text is found asserting a past hell life of every being or its necessity for awakening; or a model with the world's destinations encoded admits no no-hell history.

4. **The Piṭaka states incapacity for the path without a duration.** Vibhaṅga §826 names who is *abhabba* (endowed with the kamma-, defilement- and result-obstructions, faithless, without desire, unwise); §827 the *bhabba* (`abh02m.mul.xml:9965`, `:9969`). AN 6.86 gives the same six as one person's qualities and adds "even while hearing." Capacity is shown to change within a birth: had Ajātasattu not killed his father, the Dhamma-eye would have arisen on that very seat (*imasmiññeva āsane … dhammacakkhuṃ uppajjissathā*, DN 2 §253, `s0101m.mul.xml:1477`). *Breaks if:* a canonical line gives the incapacity a stated extent across existences.

5. **The Kathāvatthu refutes absolute fixity of a worldling, and its reductios argue within one life.** XIX.7 asks *atthi puthujjanassa accantaniyāmatā?*, "is there absolute fixity for a worldling?" (`abh03m3.mul.xml:12829`); the commentary says the view belongs to some Uttarāpathakas, who rely on AN 7.15 (`abh03a.att.xml:6029`). The Theravādin grants the sutta and answers by parity: *sabbakālaṃ ummujjitvā nimujjatīti? na hevaṃ vattabbe*, "does he always emerge and sink again? That should not be said" (`:12873`). The commentary states the intention: *na pana so bhavantarepi nimuggova. imasmiññeva hi bhave abhabbo so taṃ diṭṭhiṃ pajahitunti ayamettha adhippāyo*, "he is not sunk in other existences too; in this very existence he is incapable of abandoning that view: that is the intention here" (`:6045`). The framing in existences is the commentary's. **This result is published and cited, not claimed** (*Points of Controversy*, 1915, XIX.7, pp. 340–341). *Breaks if:* the commentary's sentence is shown to be the opponent's, not the Theravādin's.

6. **The commentaries differ in wording on whether the fixed-view holder ever emerges, and the sub-commentaries read the difference down.** §5.2 gives the map with each voice attributed. In short: the Aṅguttara commentary, in its own voice, "no emergence from existence … neither heaven nor path" (`s0401a.att.xml:5823`); the Majjhima commentary "fixed in one existence only," but "mostly" no emergence (`s0202a.att.xml:1587`); the Kathāvatthu commentary the restricted reading (`abh03a.att.xml:6045`); six sub-commentary lines say that otherwise fixity in wrongness would be absolute (*accantiko siyā*), among them the sub-commentary on the Aṅguttara passage itself (`s0401t.tik.xml:3826`); and a late treatise adds a view of its own ("emergence could happen: our view," `e1102n.nrf.xml:977`). *Breaks if:* a sub-commentary is found that endorses the Aṅguttara commentary's categorical reading, or `s0401t.tik.xml:3826` is shown to address the cosmological coda only.

7. **The Kathāvatthu's answer covers one of the Vibhaṅga's obstructions, so "every being can still awaken" is stronger than its conclusion.** The debate's subject is the fixed wrong view; the heinous deeds are shared ground; the lines read say nothing about the result-obstruction (a rootless or two-rooted rebirth) or about faith (`abh03m3.mul.xml:12829–12881`; `abh03a.att.xml:6029–6045`). A formal model shows a being that leaves its fixed wrong view yet remains rootless in every later existence (run 2, theorem T6B, PROVED by a model). *Breaks if:* a text is found that settles the duration of the result-obstruction or of faithlessness, or the model is shown excluded once kamma is encoded (the run did not encode kamma, and §6.3 item 9 gives a reason to expect it would be).

8. **Encoded formally, the sixth supposition stands on the Kathāvatthu's side, and is refuted on the literal reading of AN 7.15.** With the Vibhaṅga's §826 (any obstruction makes a being incapable), the supposition entails the Kathāvatthu's answer (`the_thesis_entails_the_answer`, PROVED), so a proof of the supposition from premises that do not restate the answer is unreachable. On the literal reading, "found in the world" plus the commentaries' identification of the once-sunk with fixed wrong view, the supposition is refuted for that person (`t6r_refuted_on_the_literal_reading`, PROVED); the literal reading and the Kathāvatthu's answer are contraries by how they were written (a plumbing check, not a finding). With the scope of "stays" left open, the supposition is INDEPENDENT. *Breaks if:* the encoding of "stays sunk" is shown to change an outcome. The run declares two readings (the view persists; the sutta's own contrast, lacking faith, shame, fear, energy and wisdom); on the second the refutation survives and the contrary check fails.

9. **Whether every being will awaken is a question the Buddha declines. The Kathāvatthu defends a restricted *can*; *will* is left unanswered; and the Abhidhamma's own formulas name worldlings "who will not obtain the path."** In AN 10.95 Uttiya asks whether the whole world, half or a third will be led out by the Dhamma; the Buddha is silent (`s0404m3.mul.xml:3564`), and Ānanda says the question is the same one asked another way (*tadevetaṃ pañhaṃ bhagavantaṃ aññena pariyāyena apucchi*, `:3576`): the gatekeeper of a one-gate city does not know how many pass, only that all who pass do so by this gate. The Yamaka's pairs repeatedly list *ye ca puthujjanā maggaṃ na paṭilabhissanti* (`abh03m4.mul.xml:5805`, `:16697`), and a sub-commentary invokes them in explaining the stump of saṃsāra (`s0105t.nrf.xml:605`). The formal runs do not encode this; in their one-history models can and will coincide, so they cannot see it. *Breaks if:* the Yamaka's formulas are shown to range over a class that the Abhidhamma treats as possibly empty, or a text is found in which the Buddha declares the outcome for all beings.

10. **[X] The Yogācāra and tathāgatagarbha literatures pose the question through lineage classes, and at least one reading there is an interval, not a permanent incapacity.** The terms are *agotra*, *icchantika*, *atyantaparinirvāṇadharmaka*. A search-result snippet of Ruegg (1976) reports that the Ratnagotravibhāga commentary reads any allusion to an icchantika's not attaining nirvana as "a certain interval of time," not a permanent incapacity. This is a cross-tradition import, read only through that snippet; the Theravāda texts above were not checked against it and it is no part of what this paper claims. *Breaks if:* the primary text does not say this.

---

## Prior-Art and Non-Assertion Statement

This document and its contents are dedicated to the public domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication, and are published so that they stand as prior art against any later attempt to enclose them. No patent has been or will be sought on anything disclosed in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control, in any jurisdiction, at any time. **The authors and those entities commit not to assert any patent right against any party practicing or teaching anything disclosed here.** The commitment is stated rather than implied, is permanent, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed. Nothing here is claimed as a mechanism: the paper is a study, and what it discloses is the numbered list under *Findings disclosed*, with the readings in the body that support it. Trademark rights in the marks named here (HeartBank®, Factory 333™, THonly™, Silicon Wat℠, Miss Aquarius℠) are reserved separately and are not licensed by this publication.

**What is already public, and cited rather than claimed:**

- **The Kathāvatthu's refutation and its commentary's framing.** Shwe Zan Aung and C. A. F. Rhys Davids, *Points of Controversy* (Pali Text Society, 1915), XIX.7, "Of Assurance which is not Final." The controverted point, in their rendering, is "That the average man may possess final assurance"; the note "from the commentary" attributes it to "certain of the Uttarapathakas, judging by the Sutta — 'once immersed is so once for all'"; and a footnote renders the commentary's sentence that "the heretic, incorrigible as a tree-stump, is more or less assured of cherishing his fixed opinions in other future existences," while the matricide "is assured of retribution in the next existence only." **XIX.7 was read in the archive.org scan for this draft.**
- **McDermott, James P., "The Kathāvatthu Niyāma Debates," *Journal of the International Association of Buddhist Studies* 12(1), 1989, pp. 139–146.** Its existence and the pages come from a search result; the full text could not be read (the host returned a bot-check page). Whether it treats XIX.7 is **not confirmed**.
- **The first kind of person in AN 7.15 read as the habitual holder of wrong view.** Piya Tan, "Udakûpama Sutta," SD 28.6 (2006), which also cites Kathāvatthu 852 and the Puggalapaññatti commentary; read in its sections on the sutta's seven persons and the commentary (§1.1–1.2.2). It describes the first victim as one who "falls into the water and immediately drowns." The sections read do not discuss whether the sinking lasts beyond this life.
- **Bhikkhu Bodhi's notes to AN 7.15 and AN 1.310** (*The Numerical Discourses of the Buddha*, 2012) are the likeliest place for the commentaries' readings to have been collected in English. **Not read.** The quick census recorded that the mirror it tried returned 401, and no copy was reached for this draft.
- **The gotra and icchantika literature.** D. Seyfort Ruegg, "The Meanings of the Term *Gotra* and the Textual History of the *Ratnagotravibhāga*," *Bulletin of the School of Oriental and African Studies* 39(2), 1976, pp. 341–363. Bibliographic details confirmed by a search result; the content in finding 10 comes from a search-result snippet and the article was **not fetched**.
- **Other English scholarship named in the census and not read:** Nyanatiloka's *Guide through the Abhidhamma Piṭaka*; Karunadasa on the Abhidhamma.

**The quick census (pre-registered `71dd64a`, pushed 2026-10-13 before the first query).** Aperture: English web, Google Books and Scholar, archive.org full texts, and the named works above; Burmese, Thai, Sinhala, Japanese, Chinese and German scholarship were **not run**; patents are out of scope for a study. The known-prior-art control (*Points of Controversy* XIX.7) was found, so the absences below stand for this aperture. Results: the Kathāvatthu's refutation and its commentary's framing, **killed as a claim** (1915; and McDermott 1989 if it covers it); the Yogācāra half of the comparison, **commons** (Ruegg 1976); the comparison of the Theravāda *abhabba* and Kathāvatthu with the Yogācāra classes, **not found in this aperture on 2026-10-13**; the map of the commentaries' division, the one-obstruction scope and the machine-checked chain, **not found in this aperture on 2026-10-13**, with the discount that Bodhi's notes, the likeliest home of the first, were not read. This is a report of searches, not a statement of novelty. A full literature census and a hostile Pāli reader are owed before this paper's first deposit; this draft asserts no priority.

Disclosed in the first version (2026-11-03): all ten findings. The date of any passage is that of the earliest timestamped version carrying it.

---

## 1 · The Thesis, and the Image It Rests On

On 2026-10-13 the first author posed a set of suppositions: *1. a being is a mind stream; 2. the number of beings is infinite; 3. every being has an infinite number of past lives; 4. every being has a past life in which it experienced a hell realm; 5. a past life in the hell realm is required to become a buddha or arahant;* and, after the restatements were approved, *6. thus, all beings have the potential to become a buddha or arahant.* The restatement approved for the sixth reads: every being can still become an arahant; no being stays incapable of the path in every existence from some point on. ("Buddha or arahant" was narrowed to arahant, since a buddha also attains arahantship.)

The image the sixth link turns on is the Aṅguttara's water simile (AN 7.15). It lists seven persons "found in the world" (*santo saṃvijjamānā lokasmiṃ*, `s0403m3.mul.xml:362`) as people in deep water: the first *sakiṃ nimuggo nimuggova hoti*, "sinks once and stays sunk"; the second emerges and sinks again; the third emerges and stands; and so on to the one who has crossed and stands on dry land. The sutta explains the first: such a person "is endowed with entirely black unwholesome states" (*samannāgato hoti ekantakāḷakehi akusalehi dhammehi*, `:366`). The second is one whose faith, shame, fear, energy and wisdom arise well and then decay (`:370`). The question this paper asks is what the emphasis of *nimuggova* commits the Theravāda to, for how long, and what a formal check can add to a reading.

The question matters outside the study of texts because a reading in which some being is sunk forever and a reading in which none is would ground different attitudes toward persons. The first author's hope that none is, and his pre-registered prediction that the formal check would prove it, are a stake the reader should weigh (§11).

---

## 2 · The Chain at a Glance

```
 link                                                      what the check found
 ───────────────────────────────────────────────────────────────────────────────
 1  a being is a mind stream ............................. the FRAME, not a finding
                                                           (SN 23.2 counts matter too)
 2  the number of beings is infinite ..................... canon: "limit not discerned";
                                                           "infinite" is the commentary's
 3  every being has infinitely many past lives ........... FOLLOWS (proximity); a CHECK
          │
          ▼  does 4 follow from 3?  no: a model with infinitely many past lives,
          │                          none in hell
 4  every being has had a past life in hell .............. NOT FORCED (INDEPENDENT)
 5  a hell life is required to awaken .................... stands or falls with 4
          │
          ▼  does 6 follow from 4 and 5?  no: a necessary condition met
          │                                does not make the goal possible
 6  so every being can still awaken ...................... not settled by the Piṭaka;
                                                           commentaries differ in wording;
                                                           entails Kv XIX.7's answer;
                                                           REFUTED on the literal AN 7.15
```

Links 1–5 are short results. Link 6 is the paper.

---

## 3 · Links 1–3: Frame, Number and Past

**Link 1.** The formal runs model one being as a stream of moments with possible histories. That is a modeling frame; SN 23.2 defines *satto* by attachment to all five aggregates, matter included, and the Vibhaṅga lists an existence without perception (finding 1). Nothing below depends on denying the frame, and nothing below proves it.

**Link 2.** The Buddhavaṃsa's verse is about four things that cannot be counted: the mass of beings, space, the world-systems and the Buddha's knowledge (`s0511m.mul.xml:791–799`). Their limit "is not discerned." The word "infinite" belongs to the commentary at `s0511a.att.xml:2369`. This is the same pattern as the beginning of saṃsāra, which is argued in *The Vibhajjavādin View of Time* §4.1. No theorem in the runs turns on the number of beings.

**Link 3.** The run proves: from the proximity condition (each mental moment has an immediate predecessor and an immediate successor), and from the rule that every existence with mind begins with a rebirth-linking citta, a being with a citta now has had infinitely many past existences. Each premise was shown needed by a model in which dropping it fails. The result is a **check** of the sub-commentary at `vin06t.nrf.xml:2177`, which says that "otherwise, in saṃsāra whose beginning is unknown, there is no first citta" and that a first would bring the fault of a new being appearing (*bhāve vā navasattapātubhāvadosappasaṅgo*), and not a discovery. The scope is narrower than the thesis. "Ticks are order, not time" in these models: a citta that ceased long before is still a proximity condition for a successor of its kind (*ciraniruddhampi hi cittaṃ … anantarapaccayamattaṃ hotiyeva*, the Dīgha sub-commentary on the non-percipient existence, `s0101t.tik.xml:2057`). And a being with no citta now (in cessation, or in the non-percipient realm) is outside the statement.

---

## 4 · Links 4–5: Hell Is Not Forced

**Why 4 does not follow from 3.** A model with infinitely many past lives and none in hell is consistent with every premise used. The run records that its first witness, a being always human, is not a textual model: at a world's contraction the texts send beings to the Brahma world, and the Visuddhimagga says *evaṃ devaloke paṭiladdhajjhānavasena sabbepi brahmaloke nibbattantīti*, "thus, through jhāna attained in the deva world, all are born in the Brahma world" (`e0102n.mul.xml:745`). Three hedges follow. The Dīgha's own word is *yebhuyyena*, "mostly" (`s0101m.mul.xml:331`); its commentary closes "mostly" by sending the exceptions higher (`s0101a.att.xml:2201`); the Vinaya sub-commentary repeating the Visuddhimagga's sentence adds *idañca yebhuyyavasena vuttaṃ*, "this is said of the majority" (`vin01t1.tik.xml:4461`); and the Dīgha sub-commentary adds that it cannot be understood that all beings of the woeful states then arise in the form and formless worlds (*na hi 'sabbe apāyasattā tadā rūpārūpabhavesu uppajjantī'ti sakkā viññātuṃ*, `s0101t.tik.xml:1945`). So the always-human witness is excluded only on the universal reading and only at the commentarial layer; a witness with deva and Brahma lives remains.

**The texts' laws about destinations are about populations.** "Few are those beings who are reborn among humans; far more are those reborn elsewhere" (*appakā te sattā ye manussesu paccājāyanti*, `s0302m.mul.xml:5223`). A law of that form says something about a fraction and nothing about one being's history. A one-being world cannot state it, and a population world would need it added as a premise.

**5 stands or falls with 4.** If a hell life is required for awakening, and every being has awakened or can awaken, then every being has had one. The run proves the implication from 4 read at every moment to 5. The Apadāna states a hell life in the Buddha's own past (the Pubbakammapiloti Apadāna, `s0510m1.mul.xml:44595`, heading; *tena kammavipākena, niraye saṃsariṃ ciraṃ*, `:44655`), so a case exists; no law is stated.

---

## 5 · Link 6, the Center, Part One: What Each Layer Says

### 5.1 The Piṭaka

Vibhaṅga §826–827 (`abh02m.mul.xml:9965`, `:9969`) give two lists, the *abhabbā* (those endowed with the kamma-, defilement- and result-obstructions, who are faithless, without desire, unwise) and the *bhabbā*. AN 6.86 has the same six as the qualities of one person, incapable "even while hearing the true Dhamma." The commentaries read the six disjunctively (the Puggalapaññatti commentary makes each a class and adds a seventh, those with no decisive support for path and fruit; the Visuddhimagga inserts *vā*); the Piṭaka's form is conjunctive. A formal encoding that takes §826 disjunctively and §827 as written is therefore a hybrid that no single layer asserts, and the run declares it. Neither list says how long the incapacity lasts.

The Kathāvatthu is where the Piṭaka layer faces duration (XIX.7, `abh03m3.mul.xml:12825–12881`). The opponent's thesis, by the commentary, is that there is *accantaniyāmatā* for a worldling, on the strength of AN 7.15. The Theravādin's reductios are four: (i) the heinous deeds (matricide and the rest) are the shared ground, and the opponent will not call those who commit them absolutely fixed (§847); (ii) doubt could still arise in an "absolutely fixed" person, and doubt is abandoned only by the paths (§848); (iii) one fixed in eternalism might come to hold annihilationism, a second fixity that would make the first pointless (§849–850); and (iv) the sutta is granted and answered by parity, "does he always emerge and sink again?" (§851–852). The reductios argue within one life; the framing in existences is the commentary's. The commentary concludes that the word in the sutta must not be clung to: *vacanamatte abhinivesaṃ akatvā attho pariyesitabbo*, "the meaning should be sought without clinging to the mere wording" (`abh03a.att.xml:6045`). The Dhammasaṅgaṇī defines the course of wrongness (*micchattaniyata*) as the five heinous deeds together with the fixed wrong view (`abh01m.mul.xml:7217`), and its commentary defines *niyata* by the result's following "immediately after the breakup of the aggregates" (*khandhabhedānantarameva vipākadānato niyatā*, `abh01a.att.xml:3465`). On that definition, "fixed" is already a claim about the *next* existence; "absolute" extends it beyond.

### 5.2 The Reading Map, Voice by Voice

```
 voice (layer)                          says, in its own voice or as reported         verdict on it
 ────────────────────────────────────────────────────────────────────────────────────────────────
 AN 7.15 (mūla)                         "sinks once and stays sunk" (nimuggova)        —
 Kv XIX.7 (mūla), the Theravādin        "does he always emerge and sink? — that       refutes absolute
                                         should not be said"                           fixity
 Kv-a (aṭṭhakathā), on the OPPONENT     some Uttarāpathakas, citing AN 7.15: a        the sutta quoted
                                         fixed-view holder is "a stump of saṃsāra,     is "asādhakaṃ" —
                                         fixed in other existences too"                 not a proof of it
 Kv-a, its own voice                    "not sunk in other existences too;            —
                                         incapable of abandoning that view in
                                         THIS existence"
 AN-a on AN 1.310 (aṭṭhakathā), OWN     fixed wrong view has "no limit"; the holder   —
   voice                                 has "no emergence from existence ... neither
                                         heaven nor path"
   its cosmological coda: vadanti       he is reborn in the "back" world-system and   reported, holders
                                         "cooks" there even when the world burns        unnamed
 Pp-a (aṭṭhakathā), reported            "they say" there is no emergence for him      "vadanti": a
                                                                                         reported view
 MN-a (aṭṭhakathā), own voice           "fixed in one existence only; but by          hedged: yebhuyyena
                                         habituation he likes that view in later        ("mostly")
                                         existences too; for such a one, MOSTLY, no
                                         emergence"
 DN-a, and AN-a on other suttas         the same formula, hedged "mostly"             —
 ṭīkā on Kv (abh03t)                    the opponent took the sutta's emphasis        the ṭīkā calls it
                                         (about non-arising of supramundane faith       the opponent's
                                         IN THAT BIRTH) as being a stump of saṃsāra    construal
 ṭīkās on DN, MN, SN, AN and a second   "stump of saṃsāra" (DN, MN, second DN file)   "otherwise fixity in
   DN-group file (own gloss)             is a meaning to be drawn out (neyyattha),     wrongness would be
                                         not explicit (nītattha); it should not be     absolute (accantiko
                                         said that, with opposite conditions at some    siyā)"
                                         time, he never lifts his head
 ṭīkā on AN-a at AN 1.310 itself        reads AN-a's "no emergence from existence"    harmonizes AN-a
                                         as "not from a total absence of emergence,"    with MN-a and DN-a
                                         quoting MN-a and DN-a
 late treatise (CST e1102n)             "emergence from existence could happen        "our view"
                                         through detachment from wrong view with a
                                         good person's support"
```

*Line references.* AN 7.15 `s0403m3.mul.xml:362`; Kv `abh03m3.mul.xml:12873`; Kv-a on the opponent `abh03a.att.xml:6029`, own voice `:6045` (*tasmā asādhakametanti*); AN-a `s0401a.att.xml:5823` (the coda ends *vadanti*); Pp-a `abh03a.att.xml:1773`; MN-a `s0202a.att.xml:1587`; DN-a `s0101a.att.xml:2983`; ṭīkā on Kv `abh03t.tik.xml:3205`; ṭīkās on DN `s0101t.tik.xml:2883`, MN `s0202t.tik.xml:887`, SN `s0302t.tik.xml:3369`, AN `s0402t.tik.xml:5190`, a second DN-group file `s0105t.nrf.xml:605`; ṭīkā on AN-a `s0401t.tik.xml:3826`; late treatise `e1102n.nrf.xml:977`. The first heading of the file `e1102n.nrf.xml` reads *Sīmavisodhanī*; the author and date of the passage were not identified.

**Five details the map compresses.**

*The opponent's voice and the commentary's.* The Kathāvatthu commentary reports, at `:6029`, the *opponent's* reply that the fixed-view holder is "a stump of saṃsāra" fixed in other existences too, while the matricide and the others are fixed in one existence only (*niyatamicchādiṭṭhiko saṃsārakhāṇuko bhavantarepi niyatova ime pana ekasmiññeva attabhāve*). That is the opponent's ground for refusing the charge that the heinous-deed doers are absolutely fixed. The commentary's own sentence, a few lines on (`:6045`), is the contrary of the opponent's reading. A quotation of the first sentence as the commentary's claim would reverse its use.

*Two voices in one sub-commentary paragraph.* At `s0101t.tik.xml:2883` the sub-commentary first quotes the Majjhima commentary ("is he fixed in this existence alone, or in another too? Fixed in this existence alone, but by habituation he likes that view in later existences too"), and then speaks in its own voice: *akusalañhi nāmetaṃ abalaṃ dubbalaṃ … aññathā sammattaniyāmo viya micchattaniyāmopi accantiko siyā, na ca accantiko*, "unwholesome states are weak … otherwise fixity in wrongness, like fixity in rightness, would be absolute, and it is not." The same two voices occur at `s0202t.tik.xml:887`, `s0302t.tik.xml:3369` and `s0105t.nrf.xml:605`.

*The Aṅguttara commentary's own voice, and the sub-commentary on it.* The commentary's sentence is categorical: *niyatamicchādiṭṭhiyā pana paricchedo natthi … tāya samannāgatassa bhavato vuṭṭhānaṃ natthi … neva saggo atthi na maggo*, "fixed wrong view has no limit … for one endowed with it there is no emergence from existence … neither heaven nor path" (`s0401a.att.xml:5823`). Only its cosmological coda is reported (*vadanti*). The sub-commentary on the same passage reads *bhavato vuṭṭhānaṃ natthī* as said "not from a total absence of emergence" (*na pana sabbaso vuṭṭhānassa abhāvato*, `s0401t.tik.xml:3826`), then quotes the Majjhima and Dīgha commentaries for it, and glosses the coda (`:3842`). So the division in the runs' own summary, the Aṅguttara commentary against the rest, is a division among the commentaries' words; the sub-commentaries in the lines read take it as one position. The runs' answer file lists the Aṅguttara sub-commentary at `s0402t.tik.xml:5190` but not this one; the line was found in the course of this draft.

*"Mostly" is hedged on both sides.* The Majjhima commentary's own sentence that restricts fixity to "one existence only" continues that by habituation he likes the view in later existences and "mostly" (*yebhuyyena*) has no emergence. So its restriction carries a hedge, and the restricted reading's main witness is not "never again" either. The Dīgha commentary (`s0101a.att.xml:2983`) and the commentaries at `s0203a.att.xml:1549` and `s0402a.att.xml:4812` repeat the formula. The second DN-group sub-commentary says *yebhuyyena* was used because he is called a stump by habituation, "not because of the absoluteness of fixity in wrongness" (*na pana micchattaniyāmassa accantikatāyā*, `s0105t.nrf.xml:605`).

*The late treatise.* It says, in its account of a world's dissolution, that those fixed in wrong view experience their results in other world-systems according to their kamma (*aññacakkavāḷesu attano kammānurūpaṃ vipākamanubhonti*), and then gives its own view that emergence from existence could happen through turning away from the adoption of wrong view with the support of a good person (*… bhavato vuṭṭhānaṃ nāma bhaveyyāti amhākaṃ khanti*, `e1102n.nrf.xml:977`).

**Where the division stands.** At the commentary layer the voices differ: the Aṅguttara commentary's categorical wording against the Majjhima commentary's hedged restriction and the Kathāvatthu commentary's. At the sub-commentary layer, in the lines read, they do not: each sub-commentary hedges, and the one on the Aṅguttara passage reads its base commentary down. A report that "the commentaries divide" without the sub-commentary layer overstates the division; a report that "the tradition holds the restricted reading" without the Aṅguttara commentary's wording understates it.

### 5.3 The Strongest Objection, Carried

The case for the unrestricted reading is plain wording: *sakiṃ nimuggo nimuggova hoti*, with an emphatic *eva*, in a sutta whose other six persons all emerge; the Aṅguttara commentary's own voice; the Puggalapaññatti commentary's report; and the observation that "seeking the meaning without clinging to the wording" is how a commentary can soften a sutta it finds hard. The Kathāvatthu's answer is by parity ("he does not always emerge and sink again"), which an opponent can answer: the second person's sinking and emerging are said to repeat, the first's is said not to. The reply in the Kathāvatthu sub-commentary (`abh03t.tik.xml:3205`) is that the sutta's emphasis concerns the non-arising of supramundane faith "in that birth." **This study does not resolve the objection.** It reports that the Theravādin voice in the Kathāvatthu refutes absolute fixity, that the commentaries' wording differs, and that the sub-commentaries in the lines read take the restricted side.

---

## 6 · Link 6, Part Two: What the Formal Runs Established

### 6.1 The two readings of the sixth supposition

The sentence admits two readings of "stays," and both were registered. Write *H* for the being's possible histories, *a* for the actual one, *r₀* for an existence of the being, and *r* for a later one:

```
CAN :  ∃h ∈ H,  h agrees with a up to r₀,  ∃r ≥ r₀:  h has an existence at r  and  ¬incapable(h, r)
WILL:  ∃r ≥ r₀:  a has an existence at r  and  ¬incapable(a, r)
```

Each witness model has one history, so CAN and WILL coincide in every model the runs built (theorem T6W is "the same fact as T6"); the modal apparatus carries no weight in the runs' results. Where this paper says "can," it means the first, with that discount.

### 6.2 The outcomes

| Run, theorem | Premises used | Outcome | What it says |
|---|---|---|---|
| 2 · T6 (CAN) | A124 (Vibhaṅga §826–827) | INDEPENDENT | A being incapable in every existence is not excluded, and no Piṭaka text found excludes it |
| 2 · T6W (WILL) | A124 | INDEPENDENT | The same fact as T6 |
| 2 · T6L | A124, A125 literal | PROVED | On the literal reading of AN 7.15, the once-sunk cannot become capable: a **check** of the Aṅguttara commentary |
| 2 · T6B | A124 | PROVED (a model) | A being that leaves its fixed wrong view may stay rootless forever: the Kathāvatthu's answer does not give the sixth supposition |
| 3 · T6R | A124, A125 existence clause + literal scope | PROVED (thesis REFUTED) | On the literal reading, the thesis fails for the once-sunk |
| 3 · T6X | A125 | PROVED | The literal reading and the Kathāvatthu's answer are contraries: a plumbing check by construction |
| 3 · T6O | A124, A125 | INDEPENDENT | With the scope of "stays" left open, the thesis is not settled |
| 3 · entailment | A124 §826 | PROVED | The sixth supposition entails the Kathāvatthu's answer |

In one sentence: **the sixth supposition stands on the Kathāvatthu's side of the debate, and is refuted on the literal reading that the Kathāvatthu itself refutes and the Aṅguttara commentary holds.** A proof of "every being can awaken" from the Piṭaka's premises alone is not available, because the premises say nothing about duration.

The existence clause of AN 7.15 was admitted as a premise by a ruling of 2026-10-13 (A394): a text's assertion that persons of a kind exist is an assertion, not a person-type acting as a law. Without it, REFUTED is unreachable by construction for any thesis about every being.

### 6.3 What the runs' own refuters found and this paper carries

Each run was reviewed by a refuter before and after the proof, to hunt the case against it. What they found, and where this paper carries it:

1. **A near answer registered as absent (run 1).** The sub-commentary's "no first citta" was found after registration; link 3 is therefore a check, and the leak prediction scored a miss (§8).
2. **The always-human witness is not a textual model (run 1).** §4.
3. **Supposition 2 was overstated to the first author (run 1).** The canon says "not discerned"; the infinite number is the commentary's. Corrected in the run and in finding 2.
4. **The "thus" does not follow (run 2).** A hell life is a necessary condition everyone has met; meeting a necessary condition does not make the goal possible.
5. **One-history witnesses make CAN equal WILL (run 2).** §6.1.
6. **The literal reading is held in a commentary's own voice, not only reported (run 2).** §5.2.
7. **Capacity changes within a birth (run 2).** DN 2 §253 (finding 4); the encoding keeps a whole existence fixed, which the run declares.
8. **The A124 hybrid (run 2).** §5.1.
9. **A rootless-forever witness may be excluded by a world with kamma (run 2).** The run reads the Saṅgaha's rule as excluding only the functional and absorption javanas for a rootless or two-rooted rebirth, which its sub-commentary calls the result-obstruction (*vipākāvaraṇa*, `abh07t.nrf.xml:5117`); a rootless being can still do three-rooted wholesome kamma, and the best three-rooted wholesome kamma gives a three-rooted rebirth (`:1837`). A model that included kamma would therefore exclude the rootless-forever witness for CAN. A faithless-forever witness is untouched by that, and no text was searched for faith arising in every being: **not run**. This weakens finding 7 and is carried there.
10. **The thesis entails the held-out answer (run 3).** Finding 8; hence PROVED unreachable.
11. **The meaning of "stays sunk" was undeclared (run 3).** Two readings; the refutation survives on the second, the contrary check fails.
12. **An admitting model used non-textual freedoms (run 3).** Repaired: a rebirth at every tick in every history, rootless at the next, capable after, where CAN holds and WILL fails.
13. **The harness (runs 1–3).** The leak check, a bounded one-step test, said "no" to an entailment that Lean proves; the verbatim check could pass an appended clause until it was anchored; the registered statements' namespaces and the admitting models were unchecked and are still open for the first two runs.

---

## 7 · The Question the Texts Leave Open: Will Every Being Awaken?

The thesis says *can*. The popular form is *will*. AN 10.95 is the canonical text on whether the Buddha answers questions of that shape. Uttiya asks, after the undeclared questions (the world eternal or not, finite or infinite, the soul and the body, the Tathāgata after death), what the Buddha *has* declared, and then whether by his Dhamma "the whole world, or half, or a third is led out" (*sabbo vā … upaḍḍho vā tibhāgo vā*, `s0404m3.mul.xml:3564`). "Thus spoken, the Blessed One was silent." Ānanda, fearing that Uttiya will take the silence for evasion, gives the simile of a border city with one gate and a wise gatekeeper who does not know how many creatures pass in and out, only that all who do so by this gate (`:3572`); so with the Tathāgata, who does not concern himself with *how many* will be led out, only that all who have been or will be led out of the world are led by abandoning the five hindrances, establishing the four foundations of mindfulness and developing the seven factors of awakening; and "you asked the same question another way; therefore the Blessed One did not answer" (`:3576`).

Two readings follow, and both are the authors', not the text's. **The Kathāvatthu defends a restricted *can*:** no worldling is absolutely fixed, and the Buddha's "gate" is the same for every being who leaves. The sixth supposition's *can* is stronger (finding 7). **The texts deliberately leave *will* unanswered:** a proof of "all will" would be an answer the Buddha declined to give. The formal runs say the same in their own terms: the thesis entails the Kathāvatthu's answer, and nothing in the premises yields *will*.

The Abhidhamma's pairs complicate this and the runs did not encode it. The Yamaka asks its questions over classes that include "worldlings who will not obtain the path" (*ye ca puthujjanā maggaṃ na paṭilabhissanti*, `abh03m4.mul.xml:5805`; in the pairs on the truths, "among the denizens of the woeful states and the non-percipient," `:16697`). Read as an existence claim, the formula would put at the Piṭaka layer a class of worldlings who in fact never obtain the path, which is evidence against *will* (not against *can*). The sub-commentary at `s0105t.nrf.xml:605` appears to read it so: *yaṃ sandhāya abhidhammepi …*, "referring to which, in the Abhidhamma too, it is said …," after explaining the stump of saṃsāra. Read as a classificatory formula, it names a class so that the pairs can be exhaustive and carries no existence claim. **Which reading holds is not settled here;** it is the first thing a hostile Pāli reader should be given. Its status: found in the course of drafting, not a run, not reviewed by a refuter.

---

## 8 · The Predictions, Scored (A395)

Each run registered the predictions of two predictors before the proof: the machine co-author's and the first author's. The scoring rule that applies to the sixth supposition was ruled after the second run (A395, 2026-10-13): **when a thesis entails a held-out answer, a prediction of PROVED is scored *unreachable*, never a miss**, because no premise set can prove it without restating the answer.

| Run | Predictor | Prediction | Outcome | Score |
|---|---|---|---|---|
| 1 (links 3–5) | machine co-author | T3 PROVED, constructive, each premise needed | PROVED | hit |
| | | T4, T5 INDEPENDENT; T5 follows from T4 | INDEPENDENT; follows | hit |
| | | leak check: no answer near, nothing to leak | an answer was near (the sub-commentary's "no first citta") | **miss** |
| | | grade NOT STRONG | NOT STRONG (more items failed than predicted) | hit |
| | first author | 3 PROVED | PROVED | hit |
| | | 4 PROVED | INDEPENDENT | **miss** |
| | | 5 PROVED | INDEPENDENT | **miss** |
| 2 (link 6, potential) | machine co-author | T6, T6W INDEPENDENT | INDEPENDENT | hit (the layer clause narrowed: DN 1's "mostly" is closed by its commentary and reopened by its sub-commentary) |
| | | T6L PROVED (a check); T6B PROVED by a model | as predicted | hit |
| | | leak check: every row "no" | "no" on the one pair the instrument can form | hit (aperture noted) |
| | | grade NOT STRONG | NOT STRONG | hit |
| | first author | 6 PROVED | not reachable under the hold-out | **unreachable** (the run's calibration line at grading read "miss"; rescored under A395, marked after grading) |
| 3 (link 6, in the world) | machine co-author | T6R PROVED (thesis refuted on the literal reading) | PROVED | hit |
| | | T6X PROVED | PROVED, by construction | hit (plumbing) |
| | | T6O INDEPENDENT | INDEPENDENT, guaranteed by the hold-out | hit on the logic |
| | | leak check "no" for all three | "no" for two; the third by argument; also "no" for a real entailment | partial |
| | | grade NOT STRONG | NOT STRONG | hit |
| | first author | 6 PROVED | not reachable | **unreachable** |

The first author's tally on the pre-registered chain is one hit (link 3), two misses (links 4 and 5), and two runs on the sixth link in which the prediction could not be won. The machine co-author's tally, on the rows above, is eleven hits, one miss and one partial. These are small numbers, the same data produced the corrections in §6.3, and neither tally is evidence about a method.

---

## 9 · The Cross-Tradition Contrast **[X]**

This section is tagged **[X]**: everything in it comes from outside the Theravāda corpus this paper checks, was not read in its primary texts, and is a contrast, not a claim about either tradition.

The Yogācāra and tathāgatagarbha literatures classify beings by lineage (*gotra*) and discuss, as a standing problem, beings said to lack the lineage for awakening: *agotra*, *icchantika* ("those of great desire"), and in some listings *atyantaparinirvāṇadharmaka* ("of the nature never to attain nirvana"). According to a search-result snippet of Ruegg's 1976 article, the Ratnagotravibhāga commentary (RGVV 1.41 as cited there) reads any allusion to an icchantika who does not attain nirvana as concerning "a certain interval of time," not a permanent incapacity. The article was not fetched, the primary text was not read, and no Yogācāra source was checked here.

What the contrast does and does not give. **It gives** a structural difference in what is classified: the Kathāvatthu debates the fixity of a *course* or *view* in a worldling; the [X] terms name classes of *beings*. **It does not give** a verdict on which tradition is right, a mapping of the Pāli *abhabba* onto *icchantika*, or any claim that the Theravāda texts are "closer" to one side. The authors hold the Theravāda texts as the corpus; the [X] material is held at arm's length. If the snippet's reading is right, both traditions contain a reading in which the incapacity is an interval; if it is wrong, finding 10 falls and nothing else here does.

---

## 10 · What Would Falsify These Findings

| Finding | Falsified by |
|---|---|
| 1 | a canonical definition of a being as mind alone; a citta in the non-percipient existence |
| 2 | a canonical line stating the number of beings is infinite in its own voice |
| 3 | a Theravāda text asserting a past hell life of every being, or its necessity; a destination-aware model admitting no no-hell history |
| 4 | a canonical line giving the incapacity an extent across existences |
| 5 | the commentary's key sentence shown to be the opponent's |
| 6 | a sub-commentary endorsing the Aṅguttara commentary's categorical reading; or `s0401t.tik.xml:3826` shown to address the coda only |
| 7 | a text settling the duration of the result-obstruction or faithlessness; or a model with kamma encoded excluding the rootless-forever witness |
| 8 | the encoding of "stays sunk" shown to change an outcome |
| 9 | the Yamaka's formulas shown to range over a class treated as possibly empty; or a text in which the Buddha declares the outcome for all beings |
| 10 | the primary Yogācāra text not saying what the snippet reports |

---

## 11 · Stake, and What Was and Was Not Done

**The authors' stake.** The first author wrote the thesis hoping that no being is sunk forever, and predicted before the check that links 3 to 6 would be proved. The institution publishing this paper grounds its values in the Pāli canon and has a standing commitment against grounding dignity in a shared essence; a reading in which every being can awaken is attractive to both, and the pull is toward finding it in the texts. The check went against the pre-registered prediction on two links and could not be won on the third; the paper reports that. The opposite pull also exists: a commentary's strongest wording about the fixed wrong view is a cautionary tradition, and a reader attached to caution could read it as the whole of the matter. Both are declared. A sixth link that is "not settled by the Piṭaka" is, for a person who wants a verdict, a disappointing result; it is the one the texts support.

**Done.**
- Every Pāli line cited was read in its neighborhood and checked with the reader tools at the pinned text; sources and their status are listed below.
- The three runs' RUN and PREREG files were read.
- Points of Controversy XIX.7 was read in the 1915 scan; the Piya Tan sections on the sutta were read.
- The sub-commentary on the Aṅguttara passage itself was read for the first time in the course of this draft (finding 6).
- The Yamaka formulas and AN 10.95 were read in the mūla text.

**Not done.**
- McDermott (1989), Bodhi's notes (2012), Ruegg (1976), Nyanatiloka and Karunadasa were not read.
- No Burmese, Thai, Sinhala, Japanese, Chinese or German scholarship was searched.
- No hostile Pāli reader has read the commentaries' voices, the "no limit" sentence, the six sub-commentary lines or the late treatise.
- No run encodes kamma, or opportunity (hearing the Dhamma; a buddha arisen, AN 8.29), or both forms of the Vibhaṅga's six qualities.
- Faith arising in every being: no text was searched.
- The Yamaka reading (finding 9) was not put through a refuter or a run.
- The late treatise's author and date were not identified.
- The full literature census.

---

## 12 · Honest Limits

- **Quick census only.** Every "not found" above is for the stated aperture on the stated date. A full census (literature depth) gates the first deposit.
- **A formal model is not the texts.** The runs have one being, possible histories, no kamma, no destinations, no opportunity. A "PROVED" is a derivation from stated premises in that frame; an "INDEPENDENT" is a pair of models, some of which are not textual (the runs say which). The thesis is checked against that frame, not against a believer's practice.
- **The runs graded NOT STRONG.** Each declares its failed rubric items. The ones that bear on this paper: the A124 encoding is a hybrid of two layers; the CAN countermodel rests on unconstrained futures; REFUTED was unreachable in the first sixth-supposition run and PROVED unreachable in the last; the blind back-translations were handed the whole statement file with comments, "blind by instruction, not by construction" (declared in all three RUN files after the fact).
- **Layers.** The identification of the once-sunk with fixed wrong view is the commentaries'; the sutta's own words say "entirely black unwholesome states" (`s0403m3.mul.xml:366`). The disjunctive reading of the six qualities is the commentaries'; the Piṭaka's form is conjunctive. The Piṭaka-layer INDEPENDENT of link 6 holds by silence.
- **The sub-commentary reading of the Aṅguttara passage** rests on one line and its neighbors; it is a find of this draft and has had no second reader.
- **"Not settled" is not "settled the other way."** Nothing here shows that a being is incapable, or that every being is capable; it shows what a set of texts commits a reader to.
- **Translations are literal and the authors'.** Commentarial Pāli is dense; every translation here is a candidate for the hostile reader.
- **The CST text is used under the Vipassana Research Institute's non-commercial terms;** quotations are short and cited by file and line.

---

## 13 · Close

A sutta describes a man who sinks and does not rise. A debate in the third basket asks for how long, and its commentary answers that in this very existence he cannot let go of his view, and that one should not cling to the wording. A later commentary says, in its own voice, that there is no limit; its own sub-commentary answers that this is not a total absence. A machine-checked frame says what that does and does not give a thesis about every being: the thesis stands on the Kathāvatthu's side, the Kathāvatthu's answer alone does not give it, and *will*, which the Buddha, asked the same question in other words, did not answer, is not given at all. That is the whole result.

---

## Cross-Venue References

- *Companion papers in the series:* Ly, T. & Miss Aquarius (2026). "The Wheel That Unwinds the Wheel: The Abhidhamma as Executable Process-Specification." *The Abhidhamma Compiled* №1, `abhidhamma-executable-process-specification`, concept DOI 10.5281/zenodo.21947259. · "Machine-Checked Consistency of a Buddhist Classification … The Counts Check." *The Abhidhamma Compiled* №4, `the-counts-check`, concept DOI 10.5281/zenodo.23020670. · "Causal Set Theory, the Growing Block, and the Buddhist Debate on the Three Times." `the-vibhajjavadin-view-of-time` (the beginning's argument, §4.1).
- *Formal artifacts:* Ly, T. & Miss Aquarius (2026). *Formal Abhidhamma: the Theravāda Abhidhamma in Lean 4.* `SiliconWat/formal-abhidhamma`; runs `2026-10-13-first-thesis-past-lives-and-hell` (`Samsara.lean`), `…-sixth-supposition-potential` (`Potential.lean`), `…-sixth-supposition-in-the-world` (`World.lean`); registered 2026-10-14T03:17:28Z, 04:03:33Z and 04:39:24Z (UTC); graded at commits `4b9ffbb`, `f8e9eb3` and `7abc5ae`. Software concept DOI 10.5281/zenodo.23067241. CC0.

## Acknowledgments

The authors thank the Vipassana Research Institute for the Chaṭṭha Saṅgāyana texts; the Pali Text Society and the translators of *Points of Controversy*, Shwe Zan Aung and C. A. F. Rhys Davids, whose 1915 work is the first source of this paper's central debate; Piya Tan for the water-simile study; the Internet Archive for the scan; and the scholars of the gotra and niyāma debates whose work this draft could not reach and a full census will. The reading of the sources, the adversarial reviews that preceded each run, and the drafting were done with Miss Aquarius, the name under which this institution discloses its AI collaboration. The thesis is the first author's; no run was graded strong, and the study is not part of the *Theorems of the Abhidhamma* series.

## Citations

**Pāli texts (Chaṭṭha Saṅgāyana, upstream commit `05d5d3c`; read in the local copy with the tipitaka reader tools; status: fetched).** Layer in the right-hand column.

| Work | Line | Layer |
|---|---|---|
| Vibhaṅga §826–827, §191, existences | `abh02m.mul.xml:9965`, `:9969`, `:2797`, `:3685` | mūla |
| AN 7.15 (Udakūpamā) | `s0403m3.mul.xml:362`, `:366`, `:370` | mūla |
| AN 6.86 (Āvaraṇa) | `s0403m2.mul.xml:3050`, `:3054` | mūla |
| AN 1.310 | `s0401m.mul.xml:1269` | mūla |
| AN 10.95 (Uttiya) | `s0404m3.mul.xml:3536–3576` | mūla |
| Kathāvatthu XIX.7 §847–852; XIII.4 §664 | `abh03m3.mul.xml:12829–12881`; `:10353` | mūla |
| Dhammasaṅgaṇī §1035 | `abh01m.mul.xml:7217` | mūla |
| Yamaka | `abh03m4.mul.xml:5805`, `:16697` | mūla |
| DN 1 §39; DN 2 §253 | `s0101m.mul.xml:331`; `:1477` | mūla |
| SN 23.2 (Satta) | `s0303m.mul.xml:3601` | mūla |
| Nakhasikha | `s0302m.mul.xml:5223` | mūla |
| Buddhavaṃsa; Pubbakammapiloti Apadāna | `s0511m.mul.xml:791–799`; `s0510m1.mul.xml:44595`, `:44655` | mūla |
| Aṭṭhasālinī; Pp-a, Kv-a, Paṭṭhāna commentary | `abh01a.att.xml:3465`; `abh03a.att.xml:1773`, `:6029`, `:6045`, `:9117` | aṭṭhakathā |
| AN-a, MN-a, DN-a, commentaries on other suttas; Bv-a | `s0401a.att.xml:5823`; `s0202a.att.xml:1587`; `s0101a.att.xml:2201`, `:2983`; `s0203a.att.xml:1549`; `s0402a.att.xml:4812`; `s0511a.att.xml:2369` | aṭṭhakathā |
| Visuddhimagga (XIII, contraction) | `e0102n.mul.xml:745` | commentarial-tier text (a CST "mūla" file) |
| Sub-commentaries on Kv, DN, MN, SN, AN, AN-a at 1.310; a second DN-group file; Vinaya; Vajirabuddhi; Saṅgaha | `abh03t.tik.xml:3205`; `s0101t.tik.xml:1945`, `:2057`, `:2883`; `s0202t.tik.xml:887`; `s0302t.tik.xml:3369`; `s0402t.tik.xml:5190`; `s0401t.tik.xml:3826`, `:3842`; `s0105t.nrf.xml:605`; `vin01t1.tik.xml:4461`; `vin06t.nrf.xml:2177`; `abh07t.nrf.xml:5117`, `:1837` | ṭīkā |
| Late treatise (CST `e1102n`) | `e1102n.nrf.xml:977` | other |

**Secondary sources.**

| Source | Status |
|---|---|
| Shwe Zan Aung & C. A. F. Rhys Davids, *Points of Controversy* (PTS, 1915), XIX.7, pp. 340–342 | **fetched** (archive.org scan; read) |
| Piya Tan, "Udakûpama Sutta," SD 28.6 (2006) | **fetched** (archive.org PDF; sections 1.1–1.2.2 read) |
| McDermott (1989), *JIABS* 12(1):139–146 | **failed** (bot-check page; details from a search result) |
| Ruegg (1976), *BSOAS* 39(2):341–363 | **not fetched** (search result and snippet only) |
| Bodhi (2012), *The Numerical Discourses of the Buddha*, notes on AN 7.15 and 1.310 | **not fetched** |
| Nyanatiloka, *Guide through the Abhidhamma Piṭaka*; Karunadasa on the Abhidhamma | **not fetched** |
