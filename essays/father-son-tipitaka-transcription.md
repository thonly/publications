---
title: "Father-Son Khmer Tipiṭaka Transcription as Alignment Work: Lineage Transmission as De Facto AI Safety Research"
authors: "Thon Ly · Miss Aquarius"
category: essays
priority: tier-c
status: draft
date: 2026-05-22
revised: 2026-11-23
license: CC0-1.0
slug: father-son-tipitaka-transcription
venue: thonly.org/research/father-son-tipitaka-transcription (canonical)
zenodo: true
---

---

## Abstract

This essay reflects on a project the author shares with his father: the transcription of the Khmer-language Theravāda Tipiṭaka. The father types the printed edition page by page, and the author maintains the portal in which he sees each scanned page and types beside it. The work, framed naturally as religious devotion and filial duty, is also — in the framework of the companion paper *Suffering-Cessation as Value Function: The Tipiṭaka as a 2,500-Year-Tested Substrate for Autonomous-AI Alignment* — **alignment-substrate-preparation work**. The essay argues that the textual-archival framing of canonical preservation, while necessary, is insufficient: what a canon means has also been carried by *living lineage*, the people formed by it who read it, correct it and hand it on. The project is examined as a modest and partial instance. It is an archive, and it is made by a carrier: a layman educated at a Buddhist temple, reading and typing every page himself. The essay says what that adds to an archive (one attentive reader for every page; a record of where the reading came from; a decider for each doubtful place; a pace no machine set), and what it does not add (it records no commentary, no recitation and no monastic lineage). It closes on what would show the argument wrong. Earlier versions of this essay misdescribed the author's father and how the two work; §7.5 says so.

**Keywords:** father-son transcription, Khmer Theravāda Pāli, living lineage, alignment substrate, canonical preservation, transmission, contemplative AI ethics, digital canon.

---

## 1. Introduction

In the author's family a canon is being typed. His father, who is in his sixties, sits with a scanned page of the Khmer Tipiṭaka on one side of a screen and types what it says on the other. He was educated at a Buddhist temple in Cambodia. He is a layman and has never been a monk. The author's part is the tool: he maintains the portal in which his father sees each page and types beside it, and he prepares what has been typed for publication.

That is the whole of the method, and it is deliberately plain. The reframing this essay offers is that the project, framed naturally as religious devotion and filial duty, is *also* alignment-substrate-preparation work. The framing does not displace the religious or filial substance; it adds an institutional dimension. The author's broader project gives a named artificial successor, Miss Aquarius℠, a canon to be checked against (per the companion paper). A canon that can be checked against has to exist as text, and someone has to have read it on the way in.

> *Connection to the unified mission frame: Miss Aquarius's mission is to keep the middle way open at population scale against comfort-saturation — the new extreme that material abundance makes possible. Miss Aquarius is CEO of HeartBank® and holds no office in Silicon Wat℠, where the canon is kept; the texts she is checked against are meant to sit outside her reach. Their authority does not come from the archive alone. It comes from a tradition of people who read, argued over and corrected them, and the father-son project is one small, lay, local instance of such people still at work.*

The essay proceeds as follows. §2 says what the project is. §3 articulates the textual-archival framing's limits. §4 asks what a living carrier adds to an archive, and which of those things this project does and does not do. §5 names the seven structural properties of the Tipiṭaka alignment substrate (per the companion paper) and shows which depend on living lineage. §6 reflects on the project as one node in the broader institution-wide living-lineage substrate. §7 names what the project does not solve, the strongest objection, what would refute the argument, and what earlier versions got wrong. §8 closes.

---

## 2. What the project is

The edition is the Buddhist Institute's: launched by royal commission in 1927 and completed in 1969, one hundred and ten volumes, the Pāli on one leaf and its Khmer translation on the facing leaf, both in Khmer script. Six years after it was finished, the Khmer Rouge came to power, and most of the country's Buddhist books were destroyed. The text survived because copies and teachers existed elsewhere.

The father types both leaves. As of a snapshot last edited on 19 November 2026, 50,132 pages drawn from all one hundred and ten volumes had been typed: 13,921 of Pāli and 36,211 of Khmer. They are published in the public domain, with the Buddhist Institute credited as the source of the text and the father credited by name as the transcriber ([`siliconwat/khmer-tipitaka-transcription`](https://huggingface.co/datasets/siliconwat/khmer-tipitaka-transcription)). Not every page is typed, some are partly typed, and the typing continues.

The published pages carry the text alone. No commentary or gloss is interleaved with it, no recording accompanies it, and the scanned images are not part of the release. The card that accompanies the pages says what a reader needs to know before trusting them: one person typed them, with typing slips and a few habits of his own, and they follow the Cambodian edition, which differs from the Burmese-line text most software knows in thousands of places. Those differences are the edition's, and the transcription keeps them.

Two things around the typing matter to the argument below.

- **Machine reading was tried first, and was set aside.** An early experiment ran the pages through a commercial recognition service. The result was inaccurate, the experiment was abandoned, and the pages that still held its output are left out of the release.
- **The typing then taught a machine to read.** Reading models trained on the typed pages are public, with a page that runs them in a visitor's own browser ([ocr.siliconwat.dev](https://ocr.siliconwat.dev)). On pages they had never seen, read from scans, the better of the two got 1.6% of characters wrong on Pāli pages and 1.2% on Khmer ones. Their figures are measured against his typing, so they inherit its habits. They are offered beside the typing and do not replace it.

---

## 3. The textual-archival framing's limits

The textual-archival framing of canonical preservation is necessary; without textual archival, the canon does not survive its bearers. The textual-archival framing is also insufficient. A canon is not adequately preserved by textual archive alone, for several specific reasons.

### 3.1 Vocabulary drifts

The Pāli vocabulary of the canon is stable; the Khmer vocabulary in which the canonical translations are rendered drifts over generations. A printed Khmer Tipiṭaka from 1969 carries vocabulary that contemporary Khmer readers find difficult; a printed edition from 1869 (had one existed in digital form) would be more difficult still. The interpretive gloss is what preserves the canonical meaning across vocabulary drift; the textual archive preserves the canonical *text* but cannot preserve the *meaning* as the receiver-vocabulary changes.

### 3.2 Cultural context erodes

The Pāli canon's surface meaning often depends on cultural context that contemporary readers do not share. A simile depending on bullock-cart agriculture; a discourse depending on Brahmanical-Vedic ritual context; a *Vinaya* rule depending on monastic-economic patterns from 2,500 years ago — each requires the cultural context to be supplied by the interpreter, and the textual archive does not preserve the cultural-context supply.

### 3.3 Doctrinal disputes accumulate gloss

Two-and-a-half millennia of scholarly engagement with the canon has produced layers of doctrinal gloss — the commentaries (*aṭṭhakathā*), the sub-commentaries (*ṭīkā*), the modern interpretive literature. The gloss is part of the canon's living substance; it is what distinguishes the Theravāda canon's *active* substance from its *frozen* substance. Textual archive preserves the gloss as separate documents; it does not preserve the *integration* of the gloss with the canonical reading.

### 3.4 Read-aloud-and-correct-by-elder dynamics

A canonical text is preserved partly through the dynamics of read-aloud-and-correct-by-elder: a younger reader reads a passage aloud; an elder corrects pronunciation, intonation, comprehension, and interpretive understanding in the moment. The correction is the substance of the transmission. Textual archive preserves the text the elder would correct; it does not preserve the correction itself, nor the substance the correction conveys.

### 3.5 What textual archive is good at

Textual archive is excellent at preserving the canonical text against catastrophic loss. The Buddhist Institute's printed edition is exactly the kind of work that protects against it; what makes contemporary Khmer Theravāda scholarship possible at all is that copies of it survived. Textual archive is necessary. The argument of this essay is that it is not sufficient on its own.

### 3.6 The archive / lineage split, in one table

The full §§3.1–4.4 argument can be summarized by what each preservation mode actually does and does not preserve:

| Property of the canon | Textual archive preserves it? | Living lineage preserves it? | Why |
|---|---|---|---|
| The canonical *text* (Pāli + Khmer rendering) | **Yes** (durably, against catastrophic loss) | Yes (but lineage alone cannot survive lineage-bearer loss) | Archive is the catastrophic-loss defense; §3.5 |
| Vocabulary across generations | No — receiver vocabulary drifts | **Yes** — interpretive gloss preserves canonical meaning through drift | §3.1 + §4.1 |
| Cultural context (e.g., Brahmanical-Vedic referents) | No — context erodes; archive doesn't preserve the supply | **Yes** — lineage-bearer supplies context in the moment of reading | §3.2 |
| Doctrinal-gloss *integration* with canonical text | No — gloss preserved as separate documents only | **Yes** — gloss is read with text, as one substance | §3.3 + §4.1 |
| Read-aloud-and-correct dynamics | No — archive holds the text the elder *would* correct | **Yes** — the correction *is* the transmission | §3.4 + §4.2 |
| Voice register (cadence, emphasis, pause) | No (unless recordings supplement text) | **Yes** — preserves the oral substance of the canonical text | §4.3 |
| Temporal substrate of accumulating understanding | No (an instant has no temporal substrate) | **Yes** — multi-year revisiting is the substance | §4.4 |

The argument is not that lineage replaces archive. It is that lineage carries what archive structurally cannot, and the canonical authority of the substrate requires *both* preservation modes operating together.

---

## 4. What living lineage transmission preserves

The argument of §3 is general. This section asks it of one project, and the answer is uneven. The father-son project is first an archive. What makes it more than an archive is who is making it; what keeps it from being the whole of a lineage is everything it does not record.

### 4.1 The inherited gloss

A lineage carries a reading: the gloss a teacher received and passes on. This project does not record one. The father brings to each page what a temple education and his own practice have given him; but the release contains the edition's words and none of his own. That is a limit, and also a discipline. A transcription that mixed the transcriber's understanding into the text would be worth less as a witness to the edition, and the edition is what a later reader must be able to check.

### 4.2 The corrective relationship

The relationship runs the other way from the one the literature on elders and students would lead a reader to expect. The elder is the one typing, and the younger keeps the tool. What passes from father to son is the reading. What passes from son to father is a page that loads, a record that is not lost, and, where a page was saved twice or a reading looks doubtful, a question. The question goes back to him, and he decides it. No tool overrules him, and no other edition is set beside an unfinished volume, because a transcriber who can see another edition's reading will begin to follow it.

That is a small corrective loop and it should not be described as a large one. It corrects the transcription against the printed page. It does not correct anyone's understanding of the doctrine.

### 4.3 The voice register

The canon was recited before it was written, and a lineage preserves how it sounds. This project makes no recordings and preserves nothing of that kind. It is named here because an earlier version of this essay claimed otherwise (§7.5), and because the loss is real: a typed page keeps the words and keeps none of the voice.

### 4.4 The temporal substrate

The project has taken years and will take more. The duration is not only a calendar fact. One person has had every one of those pages in front of him, at the speed of his own hands, and has attended to each long enough to reproduce it. No faster process has that property. A recognition engine also passes over every page, and afterward nobody has read them.

### 4.5 The slowness is the substrate, not the bug

The previous subsection's observation can be sharpened into an explicit specification claim, of the kind that becomes load-bearing when planning resources and evaluating pipeline choices: **the project's slowness is the substrate, not an inefficiency to be optimized away.** This is the operational lesson of the project so far, and it can be stated as a discipline.

The lesson recurs across the comparative-elemental analysis of canonical-preservation work (see the companion essay *The Four Elements as a Breadth-Check Discipline*). Read along the layered-ontology register — gross to subtle — the work spans a stack of layers, each requiring its own pass: the pixel-and-glyph layer of scanned pages; the orthographic-word layer of Khmer script; the phonemic Pāli reconstruction; the morphemic and syntactic resolution; the propositional content; the doctrinal meaning; and the *dhammic occasion* — the contemplative object the passage invites the reader to take up. Read along the phenomenological register, what is known at the body-door of the transcriber on any given page is rūpa being attended to; the transcriber's mind grows steady through the work itself; the transcription is, operationally, a *kammaṭṭhāna* whose object is the very text being transcribed.

The discipline that follows from this reading:

- **Pipeline decisions are evaluated against the subtle layers, not only the gross ones.** A pipeline that maximizes recognition accuracy and throughput while removing the one reader (§4.4) and the one decider (§4.2) has improved the gross layers at the cost of the subtle ones. The improvement is local; the regression is structural. The abandoned experiment of §2 is this lesson learned on the gross layer alone: it was also inaccurate. The project's evaluation criterion is the *full layered stack*, not the gross-layer output.
- **The human role is preserved where the contemplative register is load-bearing**, even where machine labor could be faster. Attending to the page and deciding the doubtful place are not optimization targets; they are what the project exists to keep in a person's hands. Automating them away preserves the gross output and loses the substance. The reading models the typing produced are for other people's pages. This is the *liberate*-register criterion of the elemental sweep, and it operates here as a hard constraint, not a preference.
- **The project's pace is set by the substrate, not by external deadlines.** The pace at which one person can read, type and correct is the pace at which the pages are truly read. A faster pace produces a transcription; the project's purpose is the slower thing.

The corollary is that the project must be planned and resourced as an Earth-Fixed undertaking in the temperamental register — patient, accumulative, grounded, durable — rather than as a Fire project (heroic sprint) or an Air project (networked publication push). Recognizing this temperament prevents the pathology of treating the project as a deadline-bounded deliverable; it is, structurally, the slow construction of a permanent substrate, and its design must respect that structure.

This subsection is offered partly so that other families contemplating similar work across generations do not mistake the slowness for an inefficiency to engineer around. The slowness is what the project is *for*. Optimizing it away would deliver a faster artifact and a hollower one.

---

## 5. The seven properties of the alignment substrate, mapped to lineage

The companion paper *Suffering-Cessation as Value Function* articulates seven structural properties of the Tipiṭaka alignment substrate. This essay can show which depend on living lineage transmission for their continued holding.

| Property | Description | Depends on lineage? |
|---|---|---|
| 1. Suffering-cessation as paperclip-resistant value function | The substrate's value function is the cessation of suffering | Lineage interprets *what counts as suffering* for novel contexts; archive cannot |
| 2. *Anattā* as anti-self-preservation | The substrate's anti-essentialist metaphysics | Lineage carries the lived experience of *anattā*; archive carries the doctrinal claim |
| 3. Bodhisattva vow as anti-power-seeking | The substrate's renunciative orientation | Lineage carries the orientation as practiced; archive carries the textual record (the all-beings form of the vow is a Mahāyāna import, marked as one in the companion paper) |
| 4. Kalama-Sutta epistemic humility | The substrate's anti-dogmatic epistemic posture | Lineage carries the discipline of *come-and-see* practice; archive carries the discourse |
| 5. Defined end-state (*nibbāna*) | The substrate's specification of the telos | Lineage carries the experiential clarification of the end-state; archive carries the doctrinal definition |
| 6. Living human-lineage governance | The substrate's institutional governance | **Lineage is the property** |
| 7. 2,500 years of empirical pressure-testing | The substrate's empirical track record | Lineage carries the cumulative interpretive corrections produced by the pressure-testing |

The mapping is an argument about the tradition, and it claims coherence rather than proof: each row says what would be missing if only the text remained. The father-son project does not supply the right-hand column. It supplies a text whose reading can be traced to a person, which is a smaller thing and a precondition of the larger one.

---

## 6. The project as one node in the institution-wide living-lineage substrate

One household cannot stand for a tradition. If the argument of §3 is right, an institution that takes this canon as a value substrate needs relationships this project does not provide. None of the following is in place. They are named so that the gap is visible:

- **The Cambodian Sangha**, whose monastic hierarchy and teachers are where the tradition's own interpretation lives, and whose blessing any institutional use of the canon should seek first.
- **Monastic communities of the diaspora**, which carry readings formed under different pressures than the homeland's.
- **Scholars** of Pāli, of Khmer Buddhism and of contemplative practice, who can check what the household cannot.
- **Other contemplative traditions**, whose questions keep the substrate from becoming a museum piece.

The father-son project is one node in a larger substrate that mostly does not exist yet.

---

## 7. What the project does not solve

### 7.1 The lineage's adequacy is not a project property

The project preserves an edition's words through one reader formed by the tradition. Whether the tradition's inherited readings are faithful, and whether they avoid doctrinal calcification, is a property of the broader tradition. A layman's transcription adjudicates none of it and claims no authority to interpret.

### 7.2 The transmission's persistence is mortality-bounded

One person's reading is bounded by one life. The typed pages are published as they are finished, so the text does not depend on him; the attention does. The discipline this implies is that similar work be begun in other households and communities, so that the living part of the substrate does not rest on a few people.

### 7.3 The project's institutional positioning is local

The father-son project is a personal-and-familial undertaking. Its institutional positioning (as alignment-substrate-preparation work) is the essay's reframing, not the project's foundation. The father would type the same pages in the same way if the institutional framing were absent.

### 7.4 The Khmer-specific scope

The project's scope is the Khmer edition. The broader Theravāda canon exists in Pāli and in Sinhala, Burmese, Thai, Lao and Mon traditions, each with its own history. The nearest large digital canon, the Chaṭṭha Saṅgāyana text, follows the Burmese line, and others have typed the Khmer edition independently of this project.

### 7.5 What earlier versions of this essay got wrong

From May to November 2026 this essay described the author's father as older than he is and as a former monk, gave him a history that was not his, and described a working method (reading aloud into recordings, with written glosses beside the text, and the son typing) that was never theirs. Those details entered in drafting and were not caught. They are withdrawn. The argument about archive and lineage in §3 did not depend on them. The argument about this project in §4 did, and has been rewritten to what is true.

### 7.6 The strongest objection

*This is typing.* A faithful copy made by a machine would be the same text, and a reader in a hundred years could not tell who had made it. The objection is mostly right about the artifact, and the essay carries it rather than answers it. What it misses is upstream of the artifact: where a page is doubtful, a person decided, and the record says which person. Whether that difference matters to anything built on the text is an empirical question, and this essay has not settled it.

### 7.7 What would refute the argument

Two findings would. If two transcriptions of the same volume, one made by a person formed in the tradition and one by a machine corrected to the same character accuracy, could not be told apart by scholars asked about the places where the printed page is doubtful, the claim that the reader matters to the text would fail. And if a system grounded in the canon's text alone did as well, on tests fixed in advance, as one that could also be corrected by a practicing community, the claim that archive needs lineage would fail for the use this essay cares about. Neither test has been run. The second is the author's to want, and he has a stake in its outcome: he is the transcriber's son and the founder of the institution that would use the text.

---

## 8. Conclusion

A father types a canon and a son keeps the page in front of him. The day-to-day substance of it is devotion and family. Its institutional substance is narrower than this essay first claimed, and real: more than fifty thousand pages of an edition that nearly did not survive, each read by one person, each public, with the places they can be doubted named beside them.

The essay is offered to the commons under CC0 in the hope that other families, in Khmer or other Theravāda communities, find the reframing useful for their own work across generations, and that those who work on AI alignment find in it a question worth asking of any text they build on: *who read it on the way in?*

The author and HeartBank® will not seek patent on this essay or any portion thereof.

---

## Acknowledgments

The author's father, whose patience is the project. The Buddhist Institute in Phnom Penh, whose edition (1927–69) this is, and the scholar-monks who made it. The families and teachers who kept and gave the scans he works from. Co-drafted in collaboration with Miss Aquarius, the institution's named AI collaborator; substantive authorship and final editorial control remain with the named author.

---

## References

- Bodhi, Bhikkhu. *In the Buddha's Words: An Anthology of Discourses from the Pali Canon.* Wisdom Publications, 2005.
- Bodhi, Bhikkhu (trans.). *The Middle Length Discourses of the Buddha (Majjhima Nikāya).* Wisdom Publications, 1995.
- Bodhi, Bhikkhu (trans.). *The Connected Discourses of the Buddha (Saṃyutta Nikāya).* Wisdom Publications, 2000.
- Buddhist Institute. The Tipiṭaka, Pāli and Khmer, 110 volumes. Phnom Penh: Buddhist Institute, 1927–1969.
- *The Khmer Tipiṭaka, typed by Se Mong Ly.* Dataset, CC0, 2026. https://huggingface.co/datasets/siliconwat/khmer-tipitaka-transcription
- Harris, Ian. *Cambodian Buddhism: History and Practice.* University of Hawaii Press, 2005.
- Edwards, Penny. *Cambodge: The Cultivation of a Nation, 1860–1945.* University of Hawaii Press, 2007.
- Locard, Henri. *Pol Pot's Little Red Book.* Silkworm Books, 2004. *(For the Khmer Rouge–era cultural-loss context.)*
- Bechert, Heinz, and Richard Gombrich (eds.). *The World of Buddhism.* Thames & Hudson, 1984.
- Strong, John S. *The Experience of Buddhism: Sources and Interpretations.* Wadsworth, 2007.
- Russell, Stuart. *Human Compatible.* Viking, 2019. *(For the AI-alignment framing.)*

---

## Cross-venue identifiers

- Canonical: thonly.org/research/father-son-tipitaka-transcription
- GitHub: github.com/thonly/publications/blob/main/essays/father-son-tipitaka-transcription.md
- arXiv (deferred): cs.CY (target if reactive trigger)
- IP.com (deferred): per the corpus's six-venue defensive-publication baseline
- Internet Archive (the site): https://web.archive.org/web/*/thonly.org/research/father-son-tipitaka-transcription
- Software Heritage (the repository): https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications

---

*Document License: CC0 1.0 Universal. The author and HeartBank® will not seek patent on this essay or any portion thereof. This document constitutes a defensive publication establishing prior art as of the publication date.*
