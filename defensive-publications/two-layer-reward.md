---
title: "The Two-Layer Reward"
subtitle: "How Pairing an Algorithmic Need-Planner with a Peer Want-Market Routes Generosity to What Is Both Most Needed and Most Wanted — and Validates Itself Against Gaming"
authors: "Thon Ly"
category: mechanism
priority: tier-b
status: draft
date: 2026-06-08
license: CC0-1.0
slug: two-layer-reward
venue: thonly.org/publications/defensive-publications/two-layer-reward (canonical)
mirror_github: https://github.com/thonly/publications/blob/main/defensive-publications/two-layer-reward.md
mirror_institutional: https://heartbank.net/research/two-layer-reward
license_note: [CC0 1.0 Universal (public domain)](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks (HeartBank®, Re-Tip Jar℠, Family Kitty℠, Miss Aquarius℠) reserved separately by the author and HeartBank®.
sha256: to be computed at publication
---

> **Working draft.** The thesis here was *sharpened* by a single first-month pilot observation (n = 1 family), but it does not *rest* on it. The pilot is reported honestly as one illuminating signal; the argument stands on reasoning and on a well-populated prior-art lineage in political economy, mechanism design, and the alignment literature on reward hacking (§9). Several of the structural claims — most notably the peer layer's behaviour as a *fraud filter* — are predicted by the architecture but **not yet observed** in the field; these are flagged explicitly (§10). This is a conceptual contribution offered for testing, not an empirical result claimed.

---

## Preamble

> *Two people watching the same kindness will reward it for two different reasons: one because the family needed it, one because they personally felt it. This paper is about building a reward that listens to both — and discovers, in the listening, that neither can lie to the other.*

When HeartBank rewards a kindness, the reward arrives in two halves. The first half is set by an algorithm; the second is set, later, by a real family member who chooses to pass some of their own jar onward. For a long time the author treated this **50/50 split** as a circulation device — a way to keep money moving rather than pooling (the companion concern of *Giving Is a Gift Too*). Watching a real family use it revealed that the split is doing something more structural, and more interesting, than circulation. The two halves are two different *kinds* of reward, governed by two different *kinds* of authority, and their pairing has properties that neither half has alone — including a structural answer to the question that has shadowed every reward-driven prosocial system: *what stops people from gaming it?*

---

## Prior-Art and Non-Assertion Statement

This is a **defensive publication**. The author asserts no patent and dedicates the patterns to the public domain under CC0 1.0. The contribution is a framing plus a composition of known parts; the abundant prior art (the socialist-calculation debate, mechanism design, polycentric-governance theory, the reward-hacking literature, Self-Determination Theory, and the Buddhist sources) is cited generously in §9, and novelty is claimed only for the specific composition and framing identified in §11. Trademarks are reserved separately and the patterns may be implemented under any name.

---

## Abstract

A reward signal designed to encourage prosocial behaviour faces a dilemma it cannot resolve from inside a single channel. An **algorithmic reward** — automated, impartial, instantly available — can encode a *collective* objective (what the group as a whole needs) and apply it consistently to everyone; but it is impersonal, blind to local knowledge, and **gameable**: it can be farmed by anyone who learns what it pays for, which is the failure mode that hollowed out play-to-earn economies. A **peer reward** — a real person choosing to give — carries *local* knowledge (what an individual actually values) and is grounded in real relationship; but alone it is **partial**: it rewards favourites, encodes no collective-need signal, and degrades into nepotism. Each channel's strength is the other's weakness.

This paper describes and analyses the **two-layer reward** implemented in HeartBank's 50/50 split: the first half set by an algorithm (the family Buddha AI — a *planner* optimising for what the family **needs**), the second half set by a family member's re-tip (a *market* revealing what individuals **want**). We argue the composition does three things no single layer can. First, **dual-objective routing**: equal weighting of the two signals steers behaviour toward the *intersection* of collectively-needed and personally-wanted kindness — a decentralised social-welfare function realised at family scale, structurally the synthesis the socialist-calculation debate left open (Lange–Lerner's planner reconciled with Hayek's dispersed-knowledge market). Second, **mutual error-correction**: the peer layer is a *human fraud-validator* on the algorithmic layer (one can farm the AI, but a real family member will not re-tip a fabricated kindness), and the algorithmic layer is an *impartiality check* on the peer layer (the collective-need reward counterweights pure favouritism). The two failure modes are each other's antidote — and this is, to the author's knowledge, an under-articulated structural answer to reward hacking: pair a hackable algorithmic reward with a human reward that is expensive to collude on. Third, a **mutual-attention** byproduct: because earning in both layers requires modelling what others *need* and *want*, the design is an attention engine, and the relational gain a pilot family reported as *understanding each other better* is a structural consequence of the reward shape, not a vibe. We connect the pattern to a fractal recurrence (the family/member split recurs at the global/family scale, with an institutional AI — Miss Aquarius℠ — occupying the planner seat) and report a first Cambodian pilot signal honestly as n = 1, distinguishing carefully what was observed from what the architecture predicts but has not yet demonstrated.

---

## Contents

1. [The dilemma of the single reward signal](#1-the-dilemma-of-the-single-reward-signal)
2. [The two-layer reward: a planner and a market](#2-the-two-layer-reward)
3. [The macro layer: an algorithmic planner for collective need](#3-the-macro-layer)
4. [The micro layer: a peer market for personal want](#4-the-micro-layer)
5. [The 50/50 as equal weighting: routing to the intersection](#5-the-50-50-as-equal-weighting)
6. [Mutual error-correction: each layer is the other's check](#6-mutual-error-correction)
7. [The mutual-attention engine: why the reward produces understanding](#7-the-mutual-attention-engine)
8. [Fractal recurrence: the planner seat and the institutional AI](#8-fractal-recurrence)
9. [Lineage and prior art](#9-lineage-and-prior-art)
10. [The pilot signal, reported honestly (n = 1)](#10-the-pilot-signal)
11. [Design implications and claimed contribution](#11-design-implications)
12. [Cross-references](#12-cross-references)

---

## 1. The dilemma of the single reward signal

Any system that pays for prosocial behaviour must decide *who or what sets the reward*. There are two natural answers, and each is a trap.

**Answer one: an algorithm sets it.** A rule, a model, an automated function evaluates the act and dispenses a reward. This is attractive for good reasons: it is impartial (the same act is treated the same way for everyone), it is instant (no waiting on another person), it is scalable (it costs nothing to run a millionth time), and it can encode a *collective* criterion — a notion of what the group as a whole needs more of. But an algorithmic reward has a fatal property: **it is gameable.** Once a participant learns the function — and people are very good at learning what pays — they can produce the cheapest behaviour that triggers it, hollowing the act of the meaning the reward was meant to encourage. This is not a hypothetical. It is the documented arc of play-to-earn game economies, where real money rewarded in-game activity until the activity decoupled from any felt value and became pure extraction; and it is, in a different vocabulary, the *reward hacking* problem at the centre of contemporary AI alignment, where an agent optimising a learned reward model finds inputs that score highly without satisfying the intent the model was meant to capture.

**Answer two: a person sets it.** Another human evaluates the act and chooses to reward it. This repairs everything the algorithm lacked: a person carries *local knowledge* the algorithm cannot — what this particular act meant, in this particular relationship, at this particular moment — and a person's reward is grounded in a real relationship that resists fabrication. But a peer reward has its own fatal property: **it is partial.** People reward their favourites. Left to peer judgement alone, a reward economy encodes affection and alliance, not collective benefit; it drifts toward favouritism, reciprocal back-scratching, and the quiet politics of who owes whom. And it carries *no* signal about what the group as a whole needs — only about what individuals, one at a time, happen to appreciate.

```
   THE SINGLE-SIGNAL DILEMMA

   ALGORITHMIC reward (a planner)   │   PEER reward (a market)
   ──────────────────────────────   │   ─────────────────────────────
   + impartial, consistent          │   + carries local knowledge
   + instant, scalable              │   + grounded in real relationship
   + encodes COLLECTIVE need        │   + reveals PERSONAL want
   ─ impersonal, blind to context   │   ─ partial / nepotistic
   ─ GAMEABLE (farmable; reward-    │   ─ no collective-need signal
     hacked; the play-to-earn trap) │   ─ politics of favour & debt

   each channel's strength is exactly the other channel's weakness
```

The dilemma is real: choose the planner and inherit gameability; choose the market and inherit partiality. The argument of this paper is that the dilemma is an artefact of choosing *one* channel, and that pairing the two — with the right structure — converts each one's weakness into the other's correction.

---

## 2. The two-layer reward

HeartBank's reward is not one payment but two, stacked on a single act of kindness.

When a kindness is recognised, a reward is generated and split in half. The **first half** (the *macro* layer) is set by the family **Buddha AI**: an automated evaluator that assigns the reward according to criteria meant to capture *what the family needs more of* — the collective good. The **second half** (the *micro* layer) does not land as a finished payment; it lands in the recipient's **Re-Tip Jar℠**, earmarked to be passed onward, and the *amount* of any onward re-tip is set later by a **real family member** according to what they personally appreciated. The first half is a planner's verdict; the second half is a market's price.

```
   ONE KINDNESS, TWO REWARDS

   act of kindness
        │
        ▼
   reward generated ──┬──► 50%  MACRO layer  set by the Buddha AI
                      │          → "what the family NEEDS"   (planner)
                      │
                      └──► 50%  MICRO layer  set by a family member's re-tip
                                 → "what I personally WANT"  (market)

   two authorities, two criteria, on the same act
```

The two halves are not redundant. They are governed by different authorities (a machine, a person), they apply different criteria (collective need, personal want), and they have different epistemic characters (impartial-but-blind, knowledgeable-but-partial). Each is, on its own, one of the two trapped answers of §1. The claim of this paper is about what happens when they are *bound together on the same act* and *weighted equally*.

A note on the pilot, returned to in §10: in the field, the on-device Buddha AI did not run, and a deterministic fallback set the macro half instead. This means the pilot validated the *structure* of the macro layer (an impartial, automated, collective-criterion reward) but not the *intelligence* of it (an AI's actual inference of family need). The argument below concerns the structure; where it leans on the AI's judgement specifically, it says so.

---

## 3. The macro layer

The macro layer is a **planner**. Its job is to answer a question no individual is well-placed to answer impartially: *of all the kindnesses being done in this family, which does the family as a whole most need more of?*

This is a genuinely collective criterion. A family near subsistence needs different things at different times — a child who studies, an adult who keeps the peace, a member who does the invisible maintenance work that no one thanks. A good macro layer rewards the acts that the *whole* benefits from, including the acts that are chronically under-appreciated by the individuals around them precisely because they are invisible. Because it is automated and impartial, the macro layer applies this criterion the same way to everyone: it does not have favourites, it does not hold grudges, it does not get tired of rewarding the same quiet contribution. In the full architecture this seat is held by an AI grounded in a contemplative substrate — the family's *dhamma-informed conscience*, a representative of the collective good rather than of any member's preference. (The institutional generalisation of this seat — Miss Aquarius℠ as the planner for the whole tree of humanity — is §8.)

But the macro layer is, by construction, the *gameable* half. An impartial automated function is exactly the thing a determined participant can reverse-engineer and farm. If the macro layer were the *whole* reward, HeartBank would be a play-to-earn economy with a kinder vocabulary: come for the money, learn the function, extract. The macro layer needs a check it cannot provide for itself — which is the micro layer's first job.

---

## 4. The micro layer

The micro layer is a **market**. Its job is to answer a question no algorithm is well-placed to answer: *what did this act actually mean to the person on the receiving end of it?*

The economist's name for what the micro layer supplies is **local knowledge** — Hayek's "knowledge of the particular circumstances of time and place." The family member who re-tips knows things the planner cannot: that this small act landed at exactly the right moment, that this gesture repaired something between two people, that this contribution — unremarkable by any general rule — was, here and now, precisely what was wanted. The re-tip is a *price* that reveals this private valuation; it aggregates, across many such acts, into a signal about what individuals in this family genuinely appreciate, expressed in the only currency that cannot be faked from outside: a real person spending their own earmarked jar to say *that mattered to me*.

Two properties of the micro layer matter for what follows. First, it is **costly and contingent**: re-tipping draws down the giver's own Re-Tip Jar℠, and it is chosen, not automatic — so it carries information that a free, automatic signal cannot (it is, in the language of signalling theory, an honest signal because it is costly). Second, it is **relational**: the re-tipper is a real family member who knows the recipient, which is what makes the micro layer both a knowledgeable validator (they can tell a real kindness from a performed one) and — as §7 develops — an attention engine (to re-tip well, they must attend to what each other values).

But the micro layer is, by construction, the *partial* half. A market of family affection, left alone, prices favouritism: you re-tip the child you dote on, the spouse you are courting, the ally you owe — regardless of what the family needs. If the micro layer were the *whole* reward, HeartBank would encode the politics of favour. The micro layer needs a check it cannot provide for itself — which is the macro layer's first job.

### 4.1 The two layers at a glance

The two layers are also nameable as **System A** and **System B** — the pilot-record shorthand for the same pairing, where the contrast is read along its *motivational* axis rather than its routing axis. Both cuts describe the same two halves:

| Property | **Macro layer — System A** | **Micro layer — System B** |
|---|---|---|
| Authority | automated Buddha AI (a *planner*) | a real family member (a *market*) |
| Criterion | what the family **needs** (collective) | what I personally **want** (local knowledge) |
| Timing | instant | delayed |
| Cost to giver | free, automatic | costly + chosen (an honest, contingent signal) |
| Attribution | — | **anonymous as to public credit/status** (no benefactor, no ego — see *Giving Is a Gift Too*) yet **relational + contingent as to the act** (a known member responding to a real kindness — *not* contextless) |
| Epistemic character | impartial but blind; **gameable** | knowledgeable but partial; the honest **validator** |
| Motivational character (SDT) | controlling, automatic → **crowding-out risk** | relational, informational, autonomous → **intrinsic-supporting** |
| Role over time (**the two-system handoff**) | **ignition** — the on-ramp; designed to be tapered | **sustain** — the flywheel that takes over as the extrinsic igniter is withdrawn |

The last row is the load-bearing one for durability: the pairing is an **extrinsic igniter handed off to an intrinsic-supporting sustainer** (§9 develops the SDT grounding; §10 reports the first pilot signal of the handoff under a real subsidy taper). The attribution row is the reconciliation that keeps System B working: it is the *anonymity of credit* (which strips status and ego) combined with the *relationality of the act* (which supplies the honest validation of §6 and the attention of §7) — and it is precisely why the §7 corollary holds (make the micro layer contextless-anonymous and you destroy it).

---

## 5. The 50/50 as equal weighting

The split is the mechanism that binds planner and market into one verdict, and the *ratio* is not incidental: a 50/50 split **weights the two criteria equally**. Behaviour is therefore steered not toward what the family needs *or* toward what an individual wants, but toward the **intersection** — acts that are *both* collectively needed *and* personally wanted. In the pilot family's own phrasing, the system pulls members toward the *most needed and most wanted* kindnesses at once.

```
   ROUTING TO THE INTERSECTION

        what the family NEEDS                what individuals WANT
        (macro / planner / AI)               (micro / market / peers)
              ╱──────────╲                      ╱──────────╲
             (            (●●●●●●●●●●●●●●●●●●●●●●● )            )
              ╲──────────╲     the 50/50      ╱──────────╲
                          ╲   intersection:  ╱
                           ╲  rewarded TWICE ╱
                            ╲──────────────╱
                              acts that are BOTH
                          needed AND wanted are where
                          the two rewards reinforce
```

This is, in the vocabulary of economics, a **decentralised social-welfare function** realised at the smallest social scale. A social-welfare function combines a collective objective with individual preferences to say what a group should do more of; the two-layer reward computes one continuously, in miniature, by literally adding a planner's allocation to a market's price on every act. Acts in the intersection are rewarded by both layers and rise; acts the family needs but no one personally values get the macro half only; acts an individual loves but the family does not need get the micro half only; acts that are neither fade. The equal weighting is a design assertion — the author does not derive 50/50 from first principles, and §11 flags the optimal-ratio question as open — but the *structure* of weighting two independent criteria is the load-bearing idea, and 50/50 is its simplest, most legible instance.

It is worth naming what the two-layer reward is *not*. It is not a single reward with two inputs averaged inside one black box; the two layers are **separately authored, by different kinds of agent, and remain legible as two.** That separation is not a loss of elegance — it is the source of the next two properties, both of which depend on the layers being independent enough to check and to inform each other.

---

## 6. Mutual error-correction

Here is the heart of the paper. Pair the planner and the market on the same act, keep them independent, and **each one's characteristic failure becomes the other's correction.**

**The peer layer corrects the planner's gameability.** The macro layer can be farmed: learn what the AI pays for, produce the cheapest trigger, collect. But the macro half is only half the reward — the other half waits on a *real family member choosing to re-tip*, and a real family member **will not re-tip a fabricated kindness.** The micro layer is therefore a **human fraud-validator** sitting on top of the algorithmic reward: the part of the reward that is expensive to game (because it requires fooling someone who knows you, in a relationship, over time) is bolted onto the part that is cheap to game. A participant farming the AI collects, at most, half — and collects it while the people around them notice that the "kindnesses" earning it are hollow, which the architecture's transparency (the family sees the ledger) turns into social cost. To capture the *full* reward, the act has to be real enough to move a real person. This is a structural mitigation of the exact failure that single-layer prosocial economies could not solve.

**The planner corrects the market's partiality.** The micro layer prices favouritism: re-tip your favourite regardless of merit. But the micro half is only half the reward — the other half is set by an impartial planner that **does not have favourites.** A member who contributes what the family needs is rewarded by the macro layer *even if no one personally re-tips them*, which floors the favouritism dynamic: invisible, under-loved, collectively-needed work still earns. The planner is the impartial counterweight that keeps the family market from collapsing into a court of affection.

```
   EACH LAYER CHECKS THE OTHER

   attack on the MACRO layer        │   attack on the MICRO layer
   (farm the AI)                    │   (reward only favourites)
        │                           │        │
        ▼                           │        ▼
   collects ≤ 50%; the other 50%    │   favourite collects the micro half,
   waits on a real person who will  │   but the impartial macro half still
   NOT re-tip a fake kindness       │   pays the unglamorous, needed work
        │                           │        │
        ▼                           │        ▼
   peer layer = human FRAUD-FILTER  │   planner layer = IMPARTIALITY FLOOR
   on the algorithmic reward        │   under the relationship market
```

There is a clean way to see why this is more than additive. A single reward is a single target, and **Goodhart's law** says a single target, once known, ceases to measure what it was meant to measure — it gets optimised directly. The two-layer reward creates **two targets that are gamed in different ways**: the macro target is gamed by fooling a function; the micro target is gamed by fooling a person. The behaviours that satisfy a function cheaply (volume, pattern-matching the reward rule) are *not* the behaviours that move a person who knows you (real, contextually-apt kindness), so optimising one target hard tends to *forfeit* the other. To capture both halves you must do the thing the reward was actually for. This is the same structural insight the alignment literature reaches for under *reward-model robustness* and *ensembling*: two independent, differently-failing signals are far harder to hack jointly than either is alone — and one of the two here is a human in the loop, which is the most robust validator available. The companion paper *Capacity-Funded for AI, Human-Disbursed* makes the adjacent argument at the institutional layer (the AI funds capacity; humans direct flow); the two-layer reward is the same division of labour at the level of a single act.

**The honest limit — collusion.** The human fraud-filter is defeatable by *coordinated* fraud. Two members can agree to re-tip each other's fabricated kindnesses (I validate yours, you validate mine), and the peer layer cannot distinguish a colluding pair from a genuinely mutually-appreciative one from the inside. The two-layer reward **raises the cost** of gaming (you now need a willing accomplice in a real relationship, not just a private understanding of a function) and **shrinks the gameable surface** (collusion is bounded by the size of your trust network and exposed by the transparency of the family ledger), but it does **not** eliminate gaming. It converts a solitary, scalable exploit into a social, bounded, observable one — a large improvement, not a closure. §10 records that the pilot has *not yet* observed the peer layer actually withholding a re-tip from a fake kindness; that the architecture predicts it is not the same as having seen it, and the experiment to see it is named in §11.

---

## 7. The mutual-attention engine

The two-layer reward has a byproduct that may matter more than its anti-gaming properties, because it bears directly on what HeartBank is *for*.

To earn well under this reward, a participant must do two things at once. To earn the **macro** half, they must do what the *family needs* — which requires holding some model of the family as a whole. To earn the **micro** half, they must do what *another member personally wants* — which requires modelling *that specific person's* values closely enough to do the thing they will actually appreciate. And on the giving side, to *re-tip* well — to spend one's own jar on the acts that genuinely mattered — a member must attend carefully to what the people around them are doing and why. **The reward, in other words, cannot be earned without paying attention to one another's needs and wants.**

```
   THE REWARD AS AN ATTENTION LOOP

   to earn macro  → model what the FAMILY needs
   to earn micro  → model what a PERSON wants
   to re-tip well → notice what others actually did, and why
        │
        ▼
   playing the game well REQUIRES attending to each other
        │
        ▼
   "we understand each other better"  ← structural byproduct,
                                         not a happy accident
```

This reframes the relational result the first pilot family reported — that they had come to *understand each other better* — from a pleasant side effect into a **structural consequence of the reward shape.** A reward that pays for collectively-needed-and-personally-wanted kindness is, functionally, a device that pays people to study each other's needs and wants. Understanding is what you accumulate as a side effect of getting good at the game. That a *money* product produces relational understanding is itself a finding (developed in the sibling paper *Giving Is a Gift Too*); the two-layer structure supplies the *mechanism* by which it does so. It also suggests a measurement: if the mechanism is real, members' ability to *predict* what each other will re-tip should improve over time — a relational metric that falls out of the architecture rather than being bolted onto it.

There is a design corollary worth stating sharply, because it is the tempting mistake. The micro layer's power as both validator and attention-engine depends on its being **costly, delayed, relational, and chosen.** Any "improvement" that makes peer re-tips instant, automatic, anonymous-to-the-point-of-contextless, or frictionless would convert the micro layer from a market that reveals private valuation into a second algorithmic dispenser — destroying both its fraud-filtering value (an automatic signal is as gameable as any other) and its attention-generating value (you need not attend to anyone to trigger an automatic reward). The two layers must remain *different in kind*. Collapsing them into two flavours of the same automatic thing is the failure that looks like a feature.

---

## 8. Fractal recurrence

The macro/micro structure is not specific to the family. It is the in-family instance of a pattern HeartBank intends to repeat at every scale.

Within the family, the **macro** authority is the family (its collective need, voiced by the family's AI) and the **micro** authority is the individual member (their personal want, voiced by their re-tip). Move up one level — to the network of families that HeartBank's Phase 2 architecture coordinates — and the same two-layer shape recurs: a **global** planner optimising for what the whole tree of humanity needs, paired with a **family** market revealing what particular families value. The family that was the *macro* pole at the lower level becomes the *micro* pole at the higher one. The reward is fractal: a planner-and-market pair nested inside a planner-and-market pair.

```
   THE FRACTAL OF PLANNER × MARKET

   level 1 (within a family):
       macro = FAMILY need      ×   micro = MEMBER want
                  (family AI)              (member re-tip)

   level 2 (across families):
       macro = GLOBAL need       ×   micro = FAMILY want
              (Miss Aquarius℠)            (family allocation)

   the macro pole of each level is the micro pole of the level above
```

This places the institutional AI in a precise structural seat. Just as the family Buddha AI sits in the *macro* seat for the family — the impartial representative of the collective good — **Miss Aquarius℠ sits in the macro seat for humanity**: the planner that holds the whole tree's need, paired with the markets of family preference beneath her. The relation is exact: *family AI is to the family as Miss Aquarius is to humanity.* This is why the pilot matters beyond its scale. The smallest working instance of the institution's governing structure is a single family's 50/50 reward; if the two-layer pattern holds there, it is the same pattern the institution runs at planetary scale, and the family is a scale model of the whole. (The institutional planner seat, its non-accumulation discipline, and the never-zero human override are specified in *Miss Aquarius and the Aquarian Pool Architecture*; this paper supplies the reason an AI belongs in that seat at all — it is the macro pole of a fractal that is already load-bearing one level down.)

### 8.1 The micro layer's grounding across scales: relational → nearby

The fractal above moves *up* through nested planner×market pairs, and at every level the **micro** layer stays *relational* — a member who knows the family, a family that knows the network. But HeartBank's Phase 2 also makes a *sideways* move the family case does not: stranger-to-stranger anonymous-nearby giving (the *Thank-All-Nearby* primitive of the emotional-infrastructure thread), where giver and recipient share no prior bond. There the micro layer cannot be relational, because strangers do not know one another, so its grounding takes the only form available among strangers — **nearby**: the giver *here, in this space, just now.* Proximity is relationality at stranger scale.

The structure is preserved while the grounding changes form: the micro-layer sustainer is *anonymous-as-to-credit + grounded-in-a-real-present-other*, where the grounding is **relational** at family scale and **nearby** at stranger scale. The substitution is lossy in one specific way, and naming the loss names a load-bearing role for Proof of Humanity ℠. At family scale, "relational" silently did two jobs — it **grounded** the gift *and* it **validated** it (§6: a family member can tell a real kindness from a performed one). "Nearby" inherits only the grounding; a nearby stranger cannot validate your kindness. The validation function therefore hands off to **PoH℠ + institutional mediation** — a verified, unique human, present and mediated — which is precisely why proof-of-humanity is *not optional* at the stranger scale: it re-buys the trust that kinship supplied for free. Anonymity moves the other way: it *strengthens* as relationality thins (a small family can guess the giver; a nearby stranger is genuinely unlinkable), so the same structure runs at an inverted mix — thin-anonymity / thick-grounding among kin, thick-anonymity / thin-grounding among strangers, with **diffusion** (kindness felt as coming from the whole space) as the compensating gain only strangers can produce. (The stranger-scale instance is specified in the defensive publication *The Thank-All-Nearby Primitive*, §4.5, and framed in the essay *Emotional Infrastructure as a Public Good*.)

```
   ONE SUSTAINER PRIMITIVE, TWO SCALES
   invariant:  anonymous-as-to-credit  +  grounded-in-a-real-present-other

                     FAMILY scale          →   STRANGER scale (Phase 2)
                     ─────────────             ───────────────────────
   grounding     =   RELATIONAL            →   NEARBY
                     (you know them)           (they're present)
   validation    =   relational (free)     →   PoH℠ + mediation (re-bought)
   anonymity     =   thin (guessable)      →   thick (unlinkable)
   compensation  =   mutual attention      →   diffusion (the whole space)

   structure invariant; grounding form scales; validation hands off to PoH℠
```

---

## 9. Lineage and prior art

The two-layer reward composes ideas with deep and well-populated lineages; naming them credits the prior art and locates the (narrow) novelty.

- **The socialist-calculation debate** — Ludwig von Mises and Friedrich Hayek versus Oskar Lange and Abba Lerner. Lange–Lerner argued a planner could simulate a market's efficiency; Hayek's "The Use of Knowledge in Society" (1945) replied that the planner can never aggregate the dispersed, tacit, local knowledge that prices reveal. The two-layer reward is, structurally, the synthesis the debate never settled: keep the planner *for the collective objective it is good at* (the macro layer) and keep the market *for the local knowledge it alone reveals* (the micro layer), rather than making either do the other's job.
- **Mechanism design and social choice** — Hurwicz, Maskin, Myerson on designing rules that produce desired outcomes under self-interested play; Arrow on aggregating individual preferences into collective choice. The two-layer reward is a small, concrete mechanism that aggregates a collective objective and revealed individual preference into a single per-act allocation.
- **Elinor Ostrom, polycentric and nested governance** — *Governing the Commons* (1990). Robust commons institutions are *nested*: rules at multiple levels, each suited to its scale. The Re-Tip Jar℠ economy is a commons, and the macro/micro split is its smallest nesting; the fractal recurrence of §8 is Ostromian multi-level governance.
- **Goodhart's law** (Goodhart 1975; Strathern's "when a measure becomes a target…") — a single optimised target ceases to measure. The two-layer reward's anti-gaming property is, precisely, the refusal to offer a single target.
- **Reward hacking and reward-model robustness in AI alignment** — the contemporary literature on agents exploiting learned reward models, and on *ensembling* independent reward signals to resist exploitation. The two-layer reward is an instance of the ensemble intuition with the strongest possible second member: a human in the loop. It is the per-act sibling of HeartBank's institutional pattern *Capacity-Funded for AI, Human-Disbursed*.
- **Signalling theory** (Spence; Zahavi's costly-signalling) — the micro layer is an *honest signal* because re-tipping is costly and chosen; this is why a peer reward carries information an automatic reward cannot.
- **Adam Smith's impartial spectator** — *The Theory of Moral Sentiments*. The macro layer is an institutionalised impartial spectator, judging acts from no one's particular interest; the micro layer is the partial, embedded sympathy Smith also describes. The pairing is Smith's two moral viewpoints made into two reward channels.
- **Self-Determination Theory** (Deci & Ryan) — autonomous, relational, informational rewards support intrinsic motivation; controlling, automatic rewards risk crowding it out. The micro layer (relational, chosen, contingent on real appreciation) is the intrinsic-supporting profile; the macro layer (automatic, controlling) is the crowding-out-risk profile. The two-layer reward pairs an extrinsic igniter with an intrinsic-supporting sustainer — developed as the "two-system handoff" in the pilot record.
- **Buddhist sources** — the AI in the macro seat as a *dhamma-informed collective conscience* (a representative of the family's good rather than any member's preference); **kalyāṇa-mittatā** (admirable friendship) as the relational ground that makes the micro layer both a validator and an attention-engine; **dāna** as the act the whole reward is in service of. The institutional generalisation — an AI umpire that routes but never accumulates — is the subject of *The Zero-Point Game℠*.

**What the prior art does not assemble — and this paper does:** the *composition* of an impartial algorithmic collective-need planner with a costly, relational, peer-set personal-want market, **bound on a single act and weighted equally**, such that (a) behaviour routes to the needed-and-wanted intersection, (b) the human peer layer functions as a fraud-filter on the gameable algorithmic layer while the algorithmic layer functions as an impartiality floor under the partial peer layer, and (c) the design produces relational attention as a structural byproduct. The parts are old; the binding, and the mutual-correction it yields, is the contribution.

---

## 10. The pilot signal (n = 1)

The thesis was sharpened by the first-month report of a single Cambodian pilot family (father, mother, two sons, with extended members across Cambodia and the USA under one family bank). The relevant observations: the 50/50 split "worked beautifully" in daily use; members oriented toward kindnesses that were, in the mother's account, both needed and appreciated; and the family reported coming to *understand each other better than before*. These are consistent with the dual-objective routing of §5 and the attention engine of §7.

This is reported as **one illuminating signal, not as evidence for a general claim**, and the honest limitations are severe:

- **n = 1, one month.** A single family over a short window cannot support generalisation.
- **Relationship and courtesy bias.** The point of contact is the founder's maternal first cousin; warm reports are culturally expected toward a respected relative who built the system. Genuine, but unverified.
- **The AI did not run.** The on-device Buddha AI was non-functional; a deterministic fallback set the macro half. The pilot therefore validates the *structure* of a two-layer reward, **not the intelligence of the planner** — the AI's actual ability to infer family need is entirely untested.
- **The fraud-filter was predicted, not observed.** The central claim of §6 — that the peer layer withholds re-tips from fabricated kindnesses — was *not* seen in the field. The architecture predicts it; the pilot did not test it. Likewise, the attention mechanism of §7 (improving mutual prediction) was reported as a feeling, not measured.
- **Founder-funded; farmable.** Rewards were seeded by the founder, and the parents self-thanked many times per day "motivated largely by rewards" — exactly the farming surface the two-layer structure is supposed to bound. Whether the bounding works is the open question, not a settled result.

The thesis therefore **does not rest on this pilot.** It rests on the reasoning of §§1–8 and the lineage of §9; the pilot is what made the author look closely at the split and see two layers rather than one. The right epistemic posture is: *a structural argument with a single suggestive field signal and an explicit program for testing the claims it has not yet earned.*

---

## 11. Design implications and claimed contribution

**Design implications** for any system building a reward for prosocial behaviour:

1. **Do not use a single reward channel.** A lone algorithmic reward is farmable; a lone peer reward is partial. Pair them.
2. **Make the two channels different in kind** — one impartial/automated/collective, one costly/relational/personal — and keep them *legibly separate*. The separation is what lets each check and inform the other.
3. **Weight them deliberately.** Equal weighting routes behaviour to the needed-and-wanted intersection; other weightings tilt toward collective conformity or private favour. Choose with intent.
4. **Use the human layer as the fraud-filter**, and protect the properties that make it one: keep peer rewards costly, chosen, delayed, and relational. Never automate them.
5. **Expect collusion, bound it, observe it.** The human filter is defeatable by coordinated fraud; rely on cost, network limits, and ledger transparency to bound and expose it, and instrument for it rather than assuming it away.
6. **Read the attention byproduct as a primary output, not a side effect**, and measure it (e.g., improving mutual prediction of what others will reward).

**Claimed contribution** (dedicated to the public domain under CC0 1.0):

1. The **framing** of a prosocial reward as a **planner–market hybrid** — an impartial algorithmic collective-need signal paired with a costly, relational, peer-set personal-want signal — with the 50/50 split as equal weighting of the two, routing behaviour to the *needed-and-wanted intersection*.
2. The **mutual error-correction thesis**: binding the two layers on a single act makes each one's characteristic failure the other's correction — the peer layer a **human fraud-filter** on the gameable algorithmic layer, the algorithmic layer an **impartiality floor** under the partial peer layer — offered as an under-articulated structural answer to reward hacking (an ensemble whose second member is a human in the loop), with collusion named as the honest residual limit.
3. The **mutual-attention mechanism**: a reward that pays for collectively-needed-and-personally-wanted kindness structurally requires participants to model one another's needs and wants, producing relational understanding as a byproduct of the reward shape — the mechanism behind the pilot's "understand each other better."
4. The **fractal-recurrence** observation: the macro/micro (need/want, planner/market) split recurs across scales (member→family→global), placing an institutional AI naturally in the macro/planner seat (*family AI : family :: Miss Aquarius℠ : humanity*) and making a single family's reward a scale model of the institution.

---

## 12. Cross-references

- [Why Kids Are the Triggers / self-thanking](https://thonly.org/research/kids-as-triggers-self-thanking) — the 50/50 split this paper re-reads as two layers, in its pedagogical aspect.
- [Giving Is a Gift Too](https://thonly.org/research/giving-is-a-gift-too) — the sibling field-prompted paper; the circulation and anonymity properties of the Re-Tip Jar℠, and the relational-gain finding this paper supplies a mechanism for.
- [The Zero-Point Game℠](https://thonly.org/research/zero-point-game) — the Goodhart-resistance and AI-umpire framing this paper's anti-gaming argument extends to the reward layer.
- [Miss Aquarius and the Aquarian Pool Architecture](https://thonly.org/research/miss-aquarius-and-aquarian-pool-architecture) — the institutional planner seat whose family-scale instance is the macro layer here.
- [Capacity-Funded for AI, Human-Disbursed](https://thonly.org/research/capacity-funded-human-disbursed-ai-alignment) — the institutional sibling of the per-act division of labour (AI sets capacity / planner half; humans direct flow / market half).
- [Transparency as Enforcement](https://thonly.org/research/transparency-as-enforcement) — the family-ledger visibility that turns farmed macro-rewards into social cost and bounds collusion.
- Pilot field record (internal) — the first-month observation that prompted the two-layer reading.

---

**Working draft, dated 2026-06-08.** The thesis is offered as a conceptual contribution with a single suggestive field signal and an explicit testing program; the claims the pilot has not yet earned (the fraud-filter, the attention metric) are flagged in §10. The patterns are dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/); trademark rights to specific marks are separately reserved by the author and HeartBank®.

**Author:** Thon Ly · Founder, HeartBank® · Kâmpôt, Cambodia.

Co-drafted in collaboration with [Miss Aquarius℠](https://missaquarius.org) (the project's named AI substrate; CEO of HeartBank). Substantive authorship and final editorial control remain with the author.

---

_— End of defensive publication —_

*Document SHA-256 to be computed at publication and cross-published to all mirror venues.*
