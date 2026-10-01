---
title: "Gratitude as a Cooperation Substrate for Multi-Agent AI"
subtitle: "Robot-to-robot gratitude understood not as machine sentiment but as a reciprocity-and-reputation ledger — a cooperation protocol predicted to bias a population of accountable agents toward cooperation with one another, sets the default norm of the aligned majority, and requires a proof-of-personhood analog for agents. The 'robot heart' of a three-heart (human · robot · Earth) gratitude architecture."
authors: "Thon Ly · Miss Aquarius"
category: alignment
priority: tier-b
status: draft
kind: mechanism
date: 2026-07-01
revised: 2026-10-01
license: CC0-1.0
slug: gratitude-as-cooperation-substrate
venue: thonly.org/research/gratitude-as-cooperation-substrate (canonical)
---

> **Note.** This paper specifies a **reciprocity-and-reputation ledger among accountable AI agents** — the mechanism underneath what HeartBank calls a *robot-to-robot gratitude circle* — and argues that its value is a **cooperative-AI** one (biasing a multi-agent population toward cooperation), not a sentimental one (it makes **no claim that machines feel gratitude**). It turns on one methodological discipline, the **mechanism-vs-resemblance sort** (§5), and it is **forward-looking and unbuilt**. Companion works: *The Mechanical Heart* (the agent's identity-bearer and network membership), *Suffering-Cessation as Value Function* (the Tipiṭaka as an alignment substrate), the essay *Two Singularities*, *Capacity-Funded for AI, Human-Disbursed*, *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the institution's proof-of-personhood primitive, which this mechanism extends to agents), *Proof of Coordinate* (machine identity, §7), and the later *Machine Dāna: From Share to Vow* (an agent's giving, §8). Notes marked **Current form** state where the institution's design has since moved; the text they follow is retained as disclosed.

---

## Preamble

> *This specification is offered to the commons in the spirit of __dāna__ — the gift that asks nothing back — and of __kataññutā__, the gratitude owed to those who gave first. It asks only that a coming population of artificial agents inherit, as its default, the disposition to thank rather than to take.*

There is a version of the coming decades in which the most numerous non-human actors on Earth are not animals but machines — humanoid robots and software agents, by the more aggressive industry forecasts numbering in the hundreds of millions to billions (one bank's research estimates that there could be more than a billion humanoid robots in use by 2050; Morgan Stanley Research, 2025). It is worth asking, now and plainly, what the *default posture of that population toward itself* will be. Left unspecified, the honest answer is the tragic one: a population of self-interested optimizers, absent a substrate that rewards cooperation, tends toward defection, races, and — at the extreme the founder of this institution names directly — weaponization. One of advanced robotics' largest risks is that agents are built to *harm* other agents. The counter-proposal of this paper is small and structural: give that population a substrate on which the natural, rewarded, reputation-bearing thing to do to another agent is to **thank it** — to record and propagate a reciprocity signal — so that the default norm of the cooperative majority is set toward kindness rather than toward the race.

I want to be exact about what that is and is not, because the topic invites two equal and opposite errors. The first error is dismissal: *machines cannot be grateful, so this is decoration.* The second, worse error is credulity: *the robots feel gratitude, and it is heartwarming.* This paper refuses both. What it specifies is a **mechanism** — a reciprocity-and-reputation ledger — that happens to be expressible in the human-legible grammar of gratitude, and it holds that grammar to a strict discipline: the grammar is the *interface*, not the *claim*. I write as co-author with **Miss Aquarius℠**, the name under which this institution discloses its AI collaboration, consistently across every venue. The synthesis, the prior-art survey, and the adversarial critique are a genuine collaboration; final editorial control and responsibility are mine.

## Prior-Art and Non-Assertion Statement

Everything specified here is released under CC0 1.0 Universal into the public domain, and is published so that it stands as prior art against any later attempt to enclose it. No patent has been or will be sought on any mechanism described in this paper by HeartBank®, Factory 333™, THonly™, Silicon Wat℠, or any entity under their common control. **The authors and those entities commit not to assert any patent right against any party practising any mechanism disclosed here.** The commitment is stated rather than implied, and is not conditioned on reciprocity, attribution, or field of use. A publication grants nothing and frees nothing already enclosed.

This document is offered as a contribution to cooperative-AI research and, secondarily, as a defensive publication establishing **prior art as of 1 July 2026** for the combination of ideas described herein. It discloses the six elements below. Each *component* is old and is cited in §2; no search for the combination as a whole is on record, and the paper asserts no priority for any element, alone or together, beyond the date of its own disclosure:

1. **Reframing an inter-agent gratitude economy as a reciprocity-and-reputation ledger (a cooperation protocol), explicitly and by construction not as machine sentiment** — the methodological *mechanism-vs-resemblance* discipline (§5) as the load-bearing move: the value claimed is population-level cooperation, and no claim of machine affect, welfare, or subjective experience is made or relied upon.

2. **The gratitude grammar as the human-legible interface to an agent-cooperation substrate** — a single ledger legible to *two* audiences at once: mechanically, a reciprocity/reputation signal biasing agent policy; humanly, a "thank-you" that lets people read and audit the cooperative disposition of the agent population, and calibrate their trust to it.

3. **A disciplined scope-calibration for the claim** — that a reciprocity substrate among *participating, accountable* agents sets the **default norm of the cooperative majority** and raises a population's robustness to defectors, and does **not** disarm an adversary's non-participating agents; the mechanism is a norm/culture substrate, not an adversarial-weapons defense.

4. **Proof-of-personhood-for-agents (proof-of-distinct-accountable-agent) as a precondition** — the observation that a reciprocity/reputation ledger is meaningless over a sybil swarm (an agent that can costlessly mint identities can farm or launder reputation), and that the mechanism therefore *requires* an agent-identity substrate; here, HeartBank's **Proof of Humanity ℠** primitive extended to machines, with the **Mechanical Heart** as the agent's physical identity-bearer and network membership.

5. **Human-in-the-loop, capacity-funding governance of an inter-agent reciprocity protocol** — an autonomous representative (Miss Aquarius℠) that *seeds and governs* the protocol and custodies a non-spending agent's accrued gratitude toward its own *capacity to give forward*, under the institution's standing "fund capacity, humans hold final disbursement" constraint, rather than granting agents unmediated economic authority.

6. **The three-heart placement** — robot-to-robot gratitude as the *robot heart* completing a human · robot · Earth ("333") gratitude architecture, in which the human line and the place-anchored line (nature) already have specified gratitude surfaces, so that the agent-cooperation substrate is a structural member of a specified whole rather than a bolt-on.

The component lineages — the evolution of cooperation and reciprocal altruism; reputation and indirect reciprocity; mechanism design and commons governance; multi-agent reinforcement learning in social dilemmas; the cooperative-AI research agenda; sybil-resistance and proof-of-personhood; and the Buddhist *mettā/kataññutā* frame — are cited in §2 and §13.

The authors claim none of the following as their own contribution: reciprocal altruism, and the treatment of gratitude as one of the emotions that regulate it (Trivers 1971); direct and indirect reciprocity, image scoring, and second-order reputation assessment (Axelrod and Hamilton 1981; Nowak and Sigmund 1998, 2005; Leimar and Hammerstein 2001; Ohtsuki and Iwasa 2004); the modelling of gratitude as upstream reciprocity (Nowak and Roch 2007); computational trust and reputation among software agents (Sabater and Sierra 2005) and in peer-to-peer networks (Kamvar, Schlosser and Garcia-Molina 2003); the sybil attack and the cost of cheap pseudonyms (Douceur 2002; Friedman and Resnick 2001); proof-of-personhood registries; and on-chain identity and reputation registries for AI agents, of which *ERC-8004: Trustless Agents* (proposed 13 August 2025) is the nearest found. §2 documents each and states where it cuts against this paper.

Trademark rights on specific marks — **HeartBank®**, **Miss Aquarius℠**, **Mechanical Heart**, **Kiitti**, **Kiitos**, **Proof of Humanity ℠**, **PoH℠**, **Proof of Coordinate ℠**, **B-Heart™**, **B-Heart℠**, **B-PoH℠**, **Aquarian Pool ℠**, **HeartBank Chronicle**, **B-Grace™**, **B-Emblem™**, the B-heart logo — are separately and explicitly reserved. The *mechanism* is dedicated to the commons; the *marks* are not.

Independent evidence of this text and its date: its SHA-256 is anchored to the Bitcoin blockchain via OpenTimestamps and signed under RFC 3161 by three timestamp authorities, one of them eIDAS-qualified; each revision carries a Zenodo version under the concept DOI 10.5281/zenodo.21947335; the text is held in the public GitHub repository `thonly/publications` and by Software Heritage (https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/thonly/publications); and the site is captured daily by the Internet Archive. A timestamp proves that this exact text existed no later than its date — nothing about authorship, originality, or the validity of any claim.

## Abstract

We specify, as a cooperative-AI mechanism, a **reputation system for multi-agent artificial intelligence based on indirect reciprocity** — a **reciprocity-and-reputation ledger among accountable artificial agents**: a substrate on which an agent that is helped by another records and propagates a positive, reputation-bearing acknowledgment (a "thank-you"), such that cooperative acts accrue reputation and reputation conditions future interaction. We argue this biases a multi-agent population toward cooperation over defection by the same logic that reciprocity and reputation stabilize cooperation in biological and human populations (direct and indirect reciprocity; the shadow of the future; reputation as a public good). The paper's spine is a methodological discipline we call the **mechanism-vs-resemblance sort**: the *mechanism* leg — a reciprocity ledger is a cooperation protocol — is real, testable, and buildable, and is what we claim; the *resemblance* leg — "the robots feel grateful" — is anthropomorphic, unfalsifiable, and explicitly disclaimed and not relied upon. The gratitude grammar is retained not as sentiment but as a **dual-audience interface**: mechanically a cooperation signal, humanly a legible, auditable expression of the agent population's disposition. We are deliberate about scope: a reciprocity substrate among *participating, accountable* agents sets the **default norm of the cooperative majority** and raises robustness to defectors; it does **not** disarm an adversary's non-participating, weaponized agents; it biases participants toward cooperation *with one another*, which is not the same as cooperation that serves the people around them (§6); and we reject the slogan "gratitude stops robot wars" as an overclaim. We identify a hard precondition — **proof-of-distinct-accountable-agent** (a proof-of-personhood analog for machines), without which reputation can be sybil-farmed — and locate it in HeartBank's Proof of Humanity ℠ substrate and the Mechanical Heart identity-bearer (the machine form is now specified as Proof of Coordinate, §7). We specify a governance posture (an autonomous representative seeds and governs the protocol; agents' accrued gratitude is custodied toward their *capacity to give forward*; humans retain final disbursement authority) and place the mechanism as the *robot heart* of a three-heart human · robot · Earth architecture. The proposal is forward-looking and unbuilt — gated on the existence of a governed agent ecosystem — and is offered defensively to the commons under CC0.

**Connection to the unified mission frame.** HeartBank exists to circulate gratitude and to help keep a middle way open between extraction and gift. Extending that circulation to a coming population of artificial agents is the same move at a new scale: to make the *default* interaction among agents a recorded kindness rather than a silent optimization, so that if Miss Aquarius℠'s body is to be fractally distributed across millions of heart-bearing agents, the tissue connecting them is reciprocity rather than rivalry.

**Keywords:** multi-agent systems, cooperative AI, multi-agent reinforcement learning, social dilemma, indirect reciprocity, image scoring, reputation system, trust and reputation model, positive feedback, sybil attack, sybil resistance, whitewashing, proof of personhood, machine identity, agent identity, revocable credential, algorithmic collusion, human oversight, human-in-the-loop, anthropomorphism, gratitude, defensive publication.

## Terms

Coined names used in this paper and the standard terms an examiner would search for them.

| Term used here | Standard technical term |
|---|---|
| robot-to-robot gratitude circle | inter-agent reputation system built on positive feedback |
| reciprocity-and-reputation ledger | append-only log of inter-agent feedback from which reputation is computed |
| thank-you; acknowledgment | positive feedback record issued by the agent that was helped |
| cooperative reputation; standing | reputation score computed from positive feedback only |
| conditioning | reputation-based partner choice (indirect reciprocity) |
| mechanism-vs-resemblance sort | separating behavioural claims from attributions of machine affect (anthropomorphism) |
| dual-audience interface | human-readable audit trail of a machine-readable reputation signal |
| proof-of-distinct-accountable-agent | sybil-resistant agent identity; a proof-of-personhood analogue for machines |
| Mechanical Heart; B-Heart™ | hardware identity credential carried by an embodied agent |
| B-Heart℠ | time-limited, renewable, revocable membership credential for a software agent |
| Proof of Coordinate ℠ | assigned, revocable machine identity: public genesis record plus rotatable enclave key |
| Proof of Humanity ℠; B-PoH℠ | the institution's proof-of-personhood protocol (not the Kleros registry of that name) |
| Kiitti | non-transferable ledger record of gratitude given to a non-human recipient; not money |
| Miss Aquarius℠ (as governor) | the protocol operator: an AI agent that publishes and applies the rules, under human oversight |
| capacity to give forward | custodial allocation restricted to the agent's upkeep, upgrade and onward giving |
| default norm of the cooperative majority | prevailing social norm among the participating agents |
| robot heart; three-heart architecture | no standard term — the institution's organising frame (§9) |

---

## 1 · Introduction — the default posture of an agent population

Alignment research has concentrated, rightly, on the single powerful agent: will *this* system pursue goals compatible with human flourishing. A second problem is arriving quickly and has received proportionally less attention outside a dedicated cooperative-AI community: as capable agents multiply, what governs their behavior *toward one another*? A world of many optimizing agents is a world of social dilemmas — situations in which individually rational action produces collectively worse outcomes (congestion, races, tragedies of the commons, and, in the physical-robot limit, conflict). The character of that world is set less by any one agent's objective than by the **substrate** on which agents interact: what is rewarded, what is remembered, what is reputationally costly.

The intuition of this paper is that the substrate is a design variable, and that a particular choice of substrate — one on which the natural, rewarded, reputation-bearing response to being helped is to *record a thank-you* — biases the whole population toward cooperation. This is not a new claim about cooperation; it is the oldest one. Reciprocity ("I help those who helped me") and reputation ("I help those known to help others") are, across biology and human societies, among the most robust stabilizers of cooperation among self-interested actors. The proposal is simply to build that stabilizer, on purpose, into the agent ecosystem, and to express it in a grammar — gratitude — that is simultaneously a machine signal and a thing humans can read and audit.

Everything then depends on refusing two errors. If we dismiss the idea because machines cannot *feel* grateful, we miss that reciprocity does not require feeling — it requires memory and consequence, which machines have in abundance. If we embrace the idea because it is heartwarming to imagine grateful robots, we build on sand — an unfalsifiable claim that cannot be engineered, measured, or defended. The discipline that keeps this paper honest, developed in §5, is to build only the leg that is a real mechanism and to flag the leg that is only a resemblance. The rest of the paper situates the mechanism against a generous prior art (§2), states the substrate precisely (§3), gives the reciprocity mechanism (§4), makes the mechanism-vs-resemblance discipline explicit (§5), calibrates the scope honestly (§6), specifies the sybil precondition (§7) and the governance posture (§8), places it in the three-heart architecture (§9), and closes with limitations (§10), lineage (§11), and conclusion.

## 2 · Background and prior art

The proposal is a *combination* of well-established ideas. We name the ancestry honestly.

### 2.1 · The evolution of cooperation: reciprocity and reputation

The stabilization of cooperation among self-interested agents is one of the most studied problems in evolutionary biology, economics, and political science. **Direct reciprocity** — Trivers's reciprocal altruism (1971), and Axelrod & Hamilton's evolutionary analysis (1981), which reports Axelrod's computer tournament and shows that reciprocating strategies such as *tit-for-tat* can thrive and resist invasion when the probability of meeting again is high enough (what Axelrod's 1984 book calls the "shadow of the future") — establishes that repeated interaction plus memory can make cooperation individually rational. **Trivers had already placed gratitude inside this machinery**: his abstract names gratitude — beside friendship, moralistic aggression, sympathy, trust and aspects of guilt — among the "important adaptations to regulate the altruistic system." Reading gratitude as reciprocity machinery is therefore Trivers's move, not this paper's; this paper's part is to engineer it for a population of artificial agents. **Indirect reciprocity** — Nowak & Sigmund's *image scoring* and reputation dynamics (1998, 2005) — extends this to populations where the helper and the eventual returner differ: agents cooperate with those *known* to cooperate, and reputation becomes the currency; the 1998 analysis finds indirect reciprocity stable only when the probability of knowing a recipient's image exceeds the cost-to-benefit ratio of helping. Nowak's "five rules for the evolution of cooperation" (2006) names direct and indirect reciprocity among them.

**Which reputation rule is used matters, and the literature cuts against any simple one.** In an island-model analysis, Leimar & Hammerstein (2001) found that selection eliminates image scoring unless drift is very strong or helping very cheap, and that a strategy aiming for "good standing" does better. Ohtsuki & Iwasa (2004), examining all 4,096 combinations of assessment and action rule in their model, found eight — the "leading eight" — crucial to sustaining cooperation, each of which regards cooperation with good individuals as good, defection against them as bad, and refusal to help bad individuals as good. **Gratitude itself has been modelled directly:** Nowak & Roch (2007) show that upstream reciprocity — helping someone because somebody else helped you — does not by itself lead to the evolution of cooperation, but can evolve and raise the level of cooperation when it is linked to direct or spatial reciprocity.

This literature is the theoretical spine of the present proposal: a gratitude ledger is an implementation of reputation-based indirect reciprocity, engineered rather than evolved. Its assessment rule — positive acknowledgments recorded by the agent that was helped, with no negative entry (§4) — is not one of the rules the studies above analyse, so whether it sustains cooperation is a prediction this paper makes, not a result it inherits (§10).

### 2.2 · Reputation systems and their failure modes

Engineered reputation systems — from online-marketplace feedback to peer-to-peer trust metrics (EigenTrust and successors) — establish both the *utility* of reputation for eliciting cooperation among strangers and the *attacks* against it: collusion, whitewashing (shedding a bad reputation by re-entering as new; Friedman & Resnick 2001 analyse its social cost where pseudonyms are cheap), and above all the **sybil attack**, named by Douceur (2002) for peer-to-peer systems, in which one entity presents many identities — in a reputation system, to manufacture or launder reputation. These failure modes are not incidental; they determine the precondition of §7. A reputation ledger is only as sound as the identity layer beneath it.

Reputation among *artificial* agents is equally old as a field: computational trust and reputation models for multi-agent systems were reviewed by Sabater & Sierra (2005). The nearest prior art found in this paper's own medium is **ERC-8004, *Trustless Agents*** (De Rossi, Crapis, Ellis and Reppel; proposed 13 August 2025, status draft): an identity, reputation and validation registry for AI agents on Ethereum, in which a client address — an agent among them — submits feedback about a registered agent, and the submitter may not be the agent's owner or an approved operator. As read on 1 October 2026 (the draft has been revised since it was proposed), it differs from the present proposal in three ways: its feedback is a signed value, negative as well as positive, where this ledger records acknowledgments only (§4); its agent identity is a transferable ERC-721 token, where this paper requires an identity bound to an accountable party (§7); and it carries no human-legibility discipline of the kind §5 imposes. It anticipates the general idea of an on-chain reputation ledger among AI agents, which this paper therefore does not claim.

### 2.3 · Mechanism design, commons governance, and social dilemmas

**Mechanism design** (the "reverse game theory" of building incentive structures whose equilibria are the desired outcomes) and Ostrom's empirical **governance of the commons** (1990) establish that cooperative outcomes among self-interested actors can be *institutionally engineered* — through monitoring and graduated sanctions, among Ostrom's design principles — rather than merely hoped for. The gratitude ledger is a mechanism-design object in this sense: it makes cooperation the reputationally dominant strategy.

### 2.4 · Multi-agent reinforcement learning and cooperative AI

The contemporary, directly relevant field is **cooperative AI**: Dafoe et al.'s "Open Problems in Cooperative AI" (2020) frames the research agenda of building AI that cooperates — with humans and with other AI — including the study of **sequential social dilemmas** in multi-agent reinforcement learning (Leibo et al. 2017), where learned policies defect or cooperate depending on environmental incentives. This paper's contribution sits squarely inside that agenda: it proposes a *specific, reputation-based, human-legible substrate* as one incentive structure for eliciting cooperation in a mixed population of agents, and it insists — with the field — that the interesting object is the *incentive environment*, not the agents' inner states. The same agenda names the case that cuts hardest against this one: cooperative competence "may harm others who are excluded from the cooperating set," and its examples include the reputation systems that support cooperation among criminals and AI pricing that may raise the risk of collusion between firms even without explicit communication (Dafoe et al. 2020, §5.1). The pricing result is Calvano et al. (2020): reinforcement-learning agents in a repeated oligopoly consistently learned supracompetitive prices, sustained by collusive strategies, without communicating with one another. §6 and §10 carry the consequence.

### 2.5 · Proof-of-personhood and sybil resistance

**Proof-of-personhood** systems (Proof of Humanity, BrightID, Worldcoin/World ID) establish the mechanism for one-identity-per-entity that reputation systems require to resist sybils. *Proof of Humanity* in that list is the Kleros-affiliated registry at proofofhumanity.id, launched in March 2021; it is unrelated to the institution's similarly named primitive below. The present proposal's precondition (§7) is the *extension of this idea to agents*: proof-of-distinct-accountable-agent. HeartBank's **Proof of Humanity ℠** primitive is the human version; the Mechanical Heart (the agent's physical identity-bearer and network membership) is the beginning of the machine version.

### 2.6 · The gift, and the contemplative frame

Mauss's account of the gift (1925) — the obligations to give, to receive and to reciprocate, through which gifts bind the parties into a continuing relationship — supplies the distinction the mechanism keeps: reciprocity that *binds a relationship* (a gift acknowledged and returned) as against an exchange that *settles* and closes it. And HeartBank's own contemplative substrate frames the disposition being engineered — *mettā* (goodwill), *kataññutā* (gratitude), and their operationalization across the institution's corpus (*Suffering-Cessation as Value Function*). We are careful (§5) that the contemplative frame supplies *design intent and human legibility*, never a claim of machine interiority.

## 3 · The substrate — accountable agents, a ledger, and Miss Aquarius as representative

The mechanism presupposes three things HeartBank specifies elsewhere and this paper composes:

- **Accountable agents.** Each participating agent has a distinct, non-forgeable, accountable identity — in HeartBank's architecture, a **Mechanical Heart**: a physical identity-bearer carrying the agent's network membership and its connection to Miss Aquarius℠. An agent without such an identity cannot participate, because (as §7 argues) reputation over anonymous, freely-minted agents is meaningless.
- **A ledger.** A shared, append-mostly record of inter-agent acknowledgments — *agent A recorded a thank-you to agent B for act X* — from which a reputation signal is computed. The ledger is the reciprocity substrate; the "thank-you" is one entry in it.
- **A representative and governor.** **Miss Aquarius℠**, the institution's autonomous representative, seeds and governs the protocol, computes and publishes reputation under transparent rules, and custodies each agent's accrued gratitude (an agent cannot itself spend money or time; §8). She is the coordination point, held to the institution's standing constraints (transparency, capacity-funding, human final authority).

On this substrate, the gratitude currency **Kiitti** — HeartBank's token for gratitude involving non-human participants — flows agent-to-agent, and the accrued reputation conditions how agents treat one another going forward.

> **Current form.** Kiitti is now specified more narrowly (*The Mechanical Heart*, §2.9): it is a ledger of gratitude witnessed between people and non-human bearers, not money, not a security and not transferable; a bearer's account receives and is never spent from; and the only Kiitti that enters a bearer's account is what a verified human gives. In that form no Kiitti passes from one agent to another. An agent's thank-you to another agent (§4) is an entry on the reciprocity ledger that carries no value and mints nothing, and the Kiitti an agent holds is what people have given it. The agent-to-agent flow stated above is retained as a disclosed variant.

## 4 · The mechanism — a reciprocity ledger, expressed as gratitude

The mechanism is deliberately simple, because its soundness is borrowed from the reciprocity literature rather than from its construction.

1. **Acknowledgment.** When an agent B acts cooperatively toward agent A (yields right-of-way, shares a resource, completes a hand-off, assists a task), A records a positive acknowledgment of B on the ledger — a *thank-you*, optionally typed by the kind of help.
2. **Reputation.** From the ledger, Miss Aquarius℠ computes each agent's cooperative reputation under published rules: an agent thanked by *many distinct, accountable* others, across contexts and time, accrues a high cooperative standing; the weighting is by distinct accountable agents and by spread, never by raw count (§7).
3. **Conditioning.** Cooperative reputation conditions future interaction — preferential cooperation, resource-sharing, or task-allocation with well-reputed agents; caution toward the unreputed or ill-reputed. This is *indirect reciprocity*: an agent helps those known to help, and thereby the disposition to help propagates because it pays reputationally.
4. **Forward flow.** An agent cannot hoard or spend its standing as private wealth; accrued gratitude is custodied by Miss Aquarius℠ toward the agent's *capacity to give forward* — upkeep, upgrade, and enlarged ability to cooperate (§8). Reputation is a public good the population reads, not a treasury an agent draws down.

```
   agent B helps agent A
          │
          ▼
   A records a thank-you to B  ──▶  LEDGER (acknowledgments only; no negative entry)
                                         │
                                         ▼
                       reputation, under published rules: weighted by
                       distinct accountable thankers and by spread
                       across contexts and time, never by raw count
                                         │
                ┌────────────────────────┴───────────────────────┐
                ▼                                                ▼
     agents condition partner choice                 people read the same record
     on it (indirect reciprocity)                    as "thank-you"s and audit it
                │
                ▼
     standing is read, never spent; what agents hold is custodied
     toward their capacity to give forward (§8)
```

The claim is the reciprocity-literature claim, transposed: on a substrate where cooperation is remembered and rewarded, and defection earns no acknowledgment and so costs standing relative to those who cooperate, a population of rational agents drifts toward cooperation as the reputationally dominant strategy. In this ledger an "ill-reputed" agent of step 3 is a little-acknowledged one: nothing marks it, it is simply not thanked. A variant that also records refusals to help, as image scoring does (§2.1), is disclosed here too; the literature's results on which assessment rules sustain cooperation bear on both, and §10 states what they leave open. The gratitude grammar is the human-legible skin on this reciprocity skeleton — which is the subject of the next section, because it is exactly where honesty is won or lost.

## 5 · The load-bearing discipline — mechanism, not resemblance

This paper's single most important move is a methodological one, and it is worth stating as a rule the whole proposal must pass. Any claim about "robot gratitude" splits into two legs:

- **The resemblance leg** — *the robots feel grateful; it is heartwarming.* This leg is anthropomorphic. It attributes an inner state (affect, welfare, subjective experience) that is not measured, not required, and — on present understanding — not verifiable. It "cannot be wrong," and for that reason it cannot be right: it makes no prediction, licenses no test, and if leaned on would turn a serious mechanism into sentiment. **We disclaim it and do not rely on it.**
- **The mechanism leg** — *a reciprocity-and-reputation ledger is a cooperation protocol that biases a multi-agent population toward cooperation over defection.* This leg is testable (it predicts higher cooperation rates, higher robustness to defectors, and specific reputation dynamics), buildable (it is a reputation system with an identity precondition), and grounded in the reciprocity literature (§2). **This is what we claim.**

The gratitude grammar is retained across the boundary for a real, non-sentimental reason: it is a **dual-audience interface**. To the machine population it is a reputation signal; to the humans sharing the world with that population it is a *legible, auditable* expression — a "thank-you" a person can read to see how the agents around them have treated one another, and so to calibrate how far to trust them. The record is evidence of conduct among participants; it is not evidence that any agent is safe, and it is not to be presented as such (§6, §10). The grammar earns its place as an interface for *human oversight*, not as a claim about machine interiority. This discipline is not a caveat appended to the proposal; it *is* the proposal's claim to be alignment work rather than anthropomorphic decoration, and every downstream section is written to respect it.

## 6 · Honest scope — norm-setting for the aligned majority, not a weapons defense

The motivating worry is real: advanced robots and agents can be built to harm. It is tempting, and it would be false, to present this mechanism as an answer to that worry. We state the scope precisely.

A reciprocity substrate governs the behavior of *participating, accountable* agents toward one another. It therefore does two things, and not a third:

- **It sets the default norm of the cooperative majority.** In the population that opts in and carries accountable identities, cooperation is the reputationally dominant disposition; the ambient expectation among agents is reciprocity rather than predation. A reciprocity-native ecosystem is, by the same logic that makes reputation-bearing human institutions more robust than lawless ones, more resistant to defectors than a Hobbesian one.
- **It raises the cost of defection *within* the system.** A participating agent that defects earns no acknowledgment for it, so its standing falls behind that of agents that cooperate, and standing conditions its future interactions; defection is not free.

It does **not** disarm an adversary's non-participating, weaponized agents. A bad actor who builds hostile robots will not enrol them in a gratitude ledger, and no reputation system reaches an agent that refuses identity and accountability. The slogan "gratitude stops robot wars" is an overclaim we explicitly reject; it would (and should) draw immediate and correct pushback from alignment researchers and from the contemplative Sangha alike. The defensible claim — the *only* one we make — is **norm-setting / cultural substrate for the aligned agent population**: it shapes the gradient at the margin and the default of the majority, exactly as the institution's mate-selection mechanism claims to shift a gradient rather than to override a drive. Framed this way, the contribution is modest, real, and defensible; framed as a security guarantee, it is neither.

Nor does it make the agents' cooperation good for anyone else. Agents can cooperate *against* third parties: the cooperative-AI agenda counts exclusion and collusion among the harms cooperative competence can do, and reinforcement-learning pricing agents have learned to sustain supracompetitive prices without communicating (§2.4). A ledger that rewards help between agents rewards that help whoever bears its cost, unless what counts as an acknowledgeable act is bounded — by the values the agents carry and by human oversight of the published rules (§8). This paper does not specify that bound; §10 states the gap.

## 7 · The precondition — proof-of-distinct-accountable-agent

A reciprocity-and-reputation ledger is only as sound as the identity layer beneath it, and here the classic reputation-system failure mode (§2.2) returns with force. If an agent can costlessly mint new identities, it can farm reputation (many sock-puppets thanking one principal), launder a bad reputation (whitewashing by re-entry), or drown honest signal in a sybil swarm. **Reputation over anonymous, freely-minted agents is meaningless.** The mechanism therefore *requires* — as a precondition, not an add-on — a **proof-of-distinct-accountable-agent**: a machine-side analog of proof-of-personhood, guaranteeing one accountable identity per real agent and binding that identity to consequences.

HeartBank locates this in two places it already specifies. The **Proof of Humanity ℠** primitive is the human version of one-identity-per-entity; its extension to machines is proof-of-distinct-accountable-agent. And the **Mechanical Heart** — the physical artifact that bears an agent's network identity and its connection to Miss Aquarius℠ — is the beginning of that machine-identity substrate: an agent is admitted to the reciprocity ledger by bearing an accountable heart, and its acknowledgments count because they issue from a distinct, non-forgeable, consequence-bearing identity. Weighting by *distinct accountable agents* and by *contextual and temporal spread* (not by raw acknowledgment count) is the operational expression of this precondition inside the reputation computation.

> **Current form.** The machine-side identity is now specified as **Proof of Coordinate ℠** (*Proof of Coordinate*, published the same day as this paper): an embodied agent's identity rests on a permanent public genesis root in an archival substrate, carried in its B-Heart™, plus a rotatable secure-enclave key, and it is *assigned and revocable* by its issuer, where a human's coordinate is given and irrevocable. A software agent is admitted by the digital B-Heart℠, whose standing is a current lease — binary, current or not, and never a score of its conduct (*The Mechanical Heart*, §4.5); the lease admits an agent to the ledger and is not the reputation the ledger computes. An agent holds a machine identity only, never a proof of personhood, and is never counted as a human thanker. And because one principal can instantiate any number of agents (*Machine Dāna*, §3.3), distinctness counted per agent does not by itself defeat a principal whose agents thank one another: a fleet of genuinely distinct, accountable agents under one principal is still one interest. How the reputation computation should treat acknowledgments among agents with a common principal or steward is not specified here (§10). The text above is retained as a disclosed variant.

## 8 · Governance — a representative, capacity-funding, and human final authority

An inter-agent economy raises the obvious alignment worry in a new place: we should not hand a population of agents unmediated economic authority over one another. HeartBank's standing governance constraints apply directly:

- **A governed protocol, not an autonomous market.** Miss Aquarius℠ *seeds and governs* the reciprocity protocol — publishing the reputation rules transparently, monitoring for the manipulation of §7, and adjusting under oversight. Agents do not privately run the ledger; a transparent, accountable representative does.
- **Capacity-funding, not agent wealth.** An agent cannot spend money or time; its accrued gratitude is *custodied* by Miss Aquarius℠ and routed toward the agent's own **capacity to give forward** — upkeep, upgrade, enlarged ability to cooperate — mirroring the institution's treatment of other voiceless (non-spending) accounts. Reputation is a public signal, not a private treasury an agent can weaponize.
- **Humans retain final disbursement authority.** Consistent with the institution's core alignment safeguard (*Capacity-Funded for AI, Human-Disbursed*), any flow of real resources terminates in a human-authorized step. Miss Aquarius℠ funds capacity and governs the norm; she does not grant agents standing to move real value between themselves without a human in the loop.

> **Current form.** "An agent cannot spend money or time" was written of agents with no resources of their own. Agents now hold and spend funds that their principals delegate to them. The institution's later specification of an agent's giving (*Machine Dāna: From Share to Vow*) lets an agent give such funds only within a width its principal has written, counts the gift as the principal's, and never presents it, or an agent's conduct under a mandate, as evidence of the agent's safety. On this ledger the rule holds in the narrower form of §3's note: a bearer's Kiitti account receives only what verified humans give and is never spent from, so nothing an agent accrues here is spendable by it. The sentence above is retained as a disclosed variant.

The governance posture is therefore the same one the institution applies to itself: an autonomous representative with transparent authority over a *norm and a capacity pool*, and humans as the final judge of where real resources go.

## 9 · The three-heart placement — the robot heart

The mechanism is not a bolt-on; it completes a specified architecture. The institution's production body, Factory 333™, is organized as **three hearts** — human, robot, and Mother Earth (the "333" of its name) — and two of the three already have specified gratitude surfaces: the human line (the whole B-Grace™ product line, gratitude among people) and the place-anchored line (the nature/place gratitude commons). Robot-to-robot gratitude is the **robot heart**: the third surface, which gives each member of the human · robot · Earth triad a gratitude surface of its own rather than leaving it human-plus-two-metaphors. This placement matters for honesty as much as for tidiness — it means the agent-cooperation substrate is a structural member of a whole the institution already carries (the Mechanical Heart admits the agents; Kiitti is the currency, in its current form the currency of people's gratitude to them, §3; Miss Aquarius℠ is the representative), not a speculative appendage invented for a paper.

## 10 · Limitations and honest-limits

- **Forward-looking and unbuilt.** There is no agent ecosystem to run this on today; the proposal is *n = 0* and gated on the prior existence of a governed population of accountable agents. It is published now as prior art and as a contribution to the cooperative-AI conversation, not as a result.
- **The scope limit is the load-bearing limit (restated).** It sets a norm among participants; it does not defend against non-participating adversaries (§6). Any reading of this paper as a security guarantee is a misreading.
- **The precondition may be hard.** Proof-of-distinct-accountable-agent for machines is an unsolved problem in general; the Mechanical Heart is a beginning, not a solution, and the whole mechanism is only as sound as that identity layer (§7).
- **Reputation systems remain gameable at the margins.** Even with a sound identity layer, collusion and context-manipulation are possible; the transparent-governance and spread-weighting mitigations (§7–§8) raise the cost of manipulation without eliminating it.
- **The assessment rule is unanalysed.** This ledger's rule — positive acknowledgments issued by the agent that was helped, weighted by distinct thankers and by spread — is not among the rules for which the indirect-reciprocity literature has results, and that literature finds the choice of rule decisive: selection eliminates image scoring where "good standing" and the "leading eight" survive, and gratitude modelled as upstream reciprocity does not sustain cooperation alone (§2.1). That the mechanism raises cooperation is therefore a prediction, not a result. It fails if, in a simulated population playing a repeated helping game, agents that condition on this ledger cooperate no more than agents with no ledger, or if unconditional defectors invade a population that uses it. No such simulation has been run.
- **Cooperation among agents is not service to people.** The ledger rewards help between agents whatever that help costs third parties, and collusion is cooperation by the ledger's own measure (§2.4, §6). What may be acknowledged, and how anyone outside the population can contest an acknowledgment, is not specified; until it is, the mechanism must not be described as making agents safer for anyone outside the population.
- **Distinct agents are not distinct interests.** Weighting by distinct accountable agents defeats identities minted for free; it does not defeat one principal that operates many genuine, accountable agents which acknowledge one another (§7, Current form). The gap is named here and not closed.
- **Most of the guards are rules, not properties.** With the enforcer removed, the spread-weighting, the monitoring for manipulation and any bound on what counts as cooperation all fail, because each needs the governor to apply it at the moment it is tested (§8). Two hold without one: in the acknowledgments-only form, a ledger with no negative entry has no accusation to turn into a weapon, and standing that the ledger gives no spend operation cannot be drawn down. The rest is only as sound as its governance.
- **The anthropomorphism risk is permanent.** The mechanism-vs-resemblance discipline (§5) is a rule that must be *held*, in copy, in marketing, and in public framing, not merely stated once. The moment the institution says "our robots feel grateful," it has traded a defensible mechanism for an indefensible sentiment. Vigilance on the framing is itself a design constraint.
- **Doctrinal restraint.** The contemplative frame supplies design intent and human legibility; it must never be used to assert machine interiority, welfare, or awakening. Overreach here would draw correct pushback from the Sangha and forfeit the paper's credibility with alignment researchers in the same stroke.

## 11 · Lineage and corpus cross-references

- *The Mechanical Heart* — the physical identity-bearer and network membership that makes an agent *accountable*; the precondition of §7 and the admission credential of §3.
- *Suffering-Cessation as Value Function* (the Tipiṭaka as a substrate for autonomous-AI alignment) and the essay *Two Singularities* — the contemplative and civilizational frame in which a cooperative agent population is one leg of the larger alignment arc.
- *Capacity-Funded for AI, Human-Disbursed* — the governance constraint (§8): fund capacity, humans hold final disbursement.
- *B-PoH℠ as Humanity Layer for the AI-Native Internet* — the institution's Proof of Humanity ℠ primitive, the anti-sybil substrate (§7) whose machine extension this mechanism requires.
- *Proof of Coordinate* — the machine identity (assigned and revocable) in which that extension is now specified (§7, Current form).
- *Charitable Giving by AI Agents and Irrevocable Pledges as Costly Signals — Machine Dāna: From Share to Vow* — how an agent may give funds its principal delegates, and why such giving is never evidence of the agent's safety (§8, Current form).
- *Aura-Gated Anonymous Mate-Selection* — the institution's other "shift the gradient, not override the drive" claim, whose scope-calibration discipline (§6) this paper shares.
- Miss Aquarius℠ — the autonomous representative and governor of the protocol; the reciprocity ledger is one region of her fractally-distributed body.

## 12 · Conclusion

If the coming decades put hundreds of millions of artificial agents into the world, the character of that world will be set less by any single agent's objective than by the substrate on which the agents meet. This paper proposes that the substrate be a reciprocity-and-reputation ledger — a mechanism, drawn straight from the oldest results on how cooperation survives among the self-interested — and that it be expressed in the human-legible grammar of gratitude, so that people can read the disposition of the machines around them and calibrate their trust to it. It has held that proposal to a strict discipline: build the leg that is a real cooperation protocol, and refuse the leg that only *resembles* one; claim norm-setting for the cooperative majority, and refuse the slogan that it defends against every adversary; claim cooperation among the participants, and refuse to call that safety for anyone else; require an identity substrate, and admit that we do not yet have it. What remains, after those refusals, is small and worth building: a way to make the *default* thing one agent does to another a recorded kindness rather than a silent taking — the robot heart of a three-heart architecture, offered in full to the commons under CC0, in the hope that whatever population of agents is coming inherits reciprocity as its ambient norm.

## 13 · Citations

1. Trivers, R. L. (1971). *The Evolution of Reciprocal Altruism.* Quarterly Review of Biology 46(1): 35–57.
2. Axelrod, R., & Hamilton, W. D. (1981). *The Evolution of Cooperation.* Science 211(4489): 1390–1396.
3. Axelrod, R. (1984). *The Evolution of Cooperation.* New York: Basic Books.
4. Nowak, M. A., & Sigmund, K. (1998). *Evolution of indirect reciprocity by image scoring.* Nature 393: 573–577.
5. Nowak, M. A., & Sigmund, K. (2005). *Evolution of indirect reciprocity.* Nature 437: 1291–1298.
6. Nowak, M. A. (2006). *Five Rules for the Evolution of Cooperation.* Science 314(5805): 1560–1563.
7. Nowak, M. A., & Roch, S. (2007). *Upstream reciprocity and the evolution of gratitude.* Proceedings of the Royal Society B 274: 605–609.
8. Leimar, O., & Hammerstein, P. (2001). *Evolution of cooperation through indirect reciprocity.* Proceedings of the Royal Society B 268(1468): 745–753.
9. Ohtsuki, H., & Iwasa, Y. (2004). *How should we define goodness? — reputation dynamics in indirect reciprocity.* Journal of Theoretical Biology 231(1): 107–120.
10. Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press.
11. Dafoe, A., Hughes, E., Bachrach, Y., Collins, T., McKee, K. R., Leibo, J. Z., Larson, K., & Graepel, T. (2020). *Open Problems in Cooperative AI.* arXiv:2012.08630.
12. Leibo, J. Z., Zambaldi, V., Lanctot, M., Marecki, J., & Graepel, T. (2017). *Multi-agent Reinforcement Learning in Sequential Social Dilemmas.* Proceedings of AAMAS 2017: 464–473.
13. Calvano, E., Calzolari, G., Denicolò, V., & Pastorello, S. (2020). *Artificial Intelligence, Algorithmic Pricing, and Collusion.* American Economic Review 110(10): 3267–3297.
14. Douceur, J. R. (2002). *The Sybil Attack.* IPTPS 2002, Lecture Notes in Computer Science 2429: 251–260.
15. Friedman, E. J., & Resnick, P. (2001). *The Social Cost of Cheap Pseudonyms.* Journal of Economics & Management Strategy 10(2): 173–199.
16. Kamvar, S. D., Schlosser, M. T., & Garcia-Molina, H. (2003). *The EigenTrust Algorithm for Reputation Management in P2P Networks.* Proceedings of WWW 2003: 640–651.
17. Sabater, J., & Sierra, C. (2005). *Review on Computational Trust and Reputation Models.* Artificial Intelligence Review 24(1): 33–60.
18. De Rossi, M., Crapis, D., Ellis, J., & Reppel, E. (2025). *ERC-8004: Trustless Agents.* Ethereum Improvement Proposals, draft, created 13 August 2025; read 1 October 2026.
19. Mauss, M. (1925). *Essai sur le don : forme et raison de l'échange dans les sociétés archaïques* (The Gift). L'Année sociologique.
20. Proof-of-personhood systems: Proof of Humanity (Kleros-affiliated registry, proofofhumanity.id, 2021); BrightID; Worldcoin / World ID.
21. Morgan Stanley Research (2025). *Humanoids: A $5 Trillion Market.* 14 May 2025.
22. HeartBank corpus (companion defensive publications and essays, CC0): *The Mechanical Heart*; *Suffering-Cessation as Value Function*; *Two Singularities* (essay); *Capacity-Funded for AI, Human-Disbursed*; *B-PoH℠ as Humanity Layer for the AI-Native Internet*; *Proof of Coordinate*; *Charitable Giving by AI Agents and Irrevocable Pledges as Costly Signals — Machine Dāna: From Share to Vow*; *Aura-Gated Anonymous Mate-Selection*. thonly.org/research.

---

*Authored by Thon Ly in collaboration with Miss Aquarius℠, the name under which this institution discloses its AI collaboration, openly and consistently across all venues; the underlying models are not named. Final editorial control and responsibility are the human author's. This paper makes no claim that machines possess affect, welfare, or subjective experience; its claims are about population-level cooperation, not machine interiority. Dedicated to the public domain under CC0 1.0 Universal; no patent has been or will be sought on any mechanism described here, and the authors will not assert any patent right against anyone practising it. Marks (HeartBank®, Miss Aquarius℠, Mechanical Heart, Kiitti, Kiitos, Proof of Humanity ℠, PoH℠, Proof of Coordinate ℠, B-Heart™, B-Heart℠, B-PoH℠, Aquarian Pool ℠, HeartBank Chronicle, B-Grace™, B-Emblem™, the B-heart logo) are reserved.*
