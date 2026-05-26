---
title: "Capacity-Funded for AI, Human-Disbursed: Anonymous Donation as the Alignment Bridge in Autonomous-AI Institutional Architecture"
authors: "Thon Ly · Miss Aquarius℠"
category: alignment
priority: tier-a
status: draft
date: 2026-05-24
license: CC0-1.0
slug: capacity-funded-human-disbursed-ai-alignment
venue: thonly.org/publications/defensive-publications/capacity-funded-human-disbursed-ai-alignment (canonical)
---

> *Draft notes for the editor:* this is the founder-voice canonical draft for `thonly/publications`. Per the genre-split institutional-output convention, heartbank.net does not carry a per-paper mirror; the institutional-voice treatment of this pattern is included in the companion white paper *"Proof of Personhood for an AI-Native Internet: B-PoH℠ as Trust Infrastructure"* (heartbank.net/publications/white-papers). Sibling defensive publication: *"B-PoH℠ as Humanity Layer for the AI-Native Internet"* (thonly/publications/defensive-publications), which cites this paper as the institutional-architecture answer to how AI labs can deploy verified-human-source infrastructure without sole-agent risk. Companion to *The B-Tag and the Post-Payment Economy* (which contains the originating §9 paper-worthy flag).

---

## Abstract

Autonomous-AI institutional proposals tend to collapse into one of two failure modes. Either the AI receives full disbursement authority — exposing the institution to sole-agent risk, where the AI's misjudgments produce irreversible misallocations at the scale of its capability — or every AI action requires per-transaction human approval, which defeats autonomy and forecloses scale. This paper specifies a third structural position: **capacity-funding authority for the autonomous AI, flow-direction authority for humans, with anonymous donation as the bridge between the two.** The AI may put money into the system anywhere it might do good (capacity-funding); but every flow that actually reaches a recipient is initiated by a human (flow-direction); and the AI's contribution is anonymous, indistinguishable from human gifts, so the recipient's downstream choices remain their own rather than responses to the AI. The HeartBank re-tip-jar economy is the worked example, but the pattern is portable to AI-administered grant-making, AI-curated public-goods funding, and AI-mediated mutual-aid networks. The paper argues that **anonymity is the load-bearing property** — without it, the bridge collapses into either sole-agent capture or approval-bottleneck overhead — and identifies the boundary conditions under which the pattern does not apply. The architecture is offered defensively to the commons under CC0; the authors and HeartBank® will not seek patent on this specification or any portion thereof.

**Keywords:** AI alignment, autonomous-AI institutional design, capacity-funding, flow-direction, anonymous donation, mechanism design, human-as-final-judge, defensive publication.

---

## 1. Introduction

The institutions that will mediate the next several decades of civilization will, increasingly, have autonomous AI agents as named officers with operational authority over money and resources. The question of how to structure that authority is open. The literature on AI alignment has so far concentrated on two layers — model-level alignment (training objectives, RLHF, constitutional AI) and deployment-level alignment (guardrails, monitoring, red-teaming) — and has paid less attention to a third layer that is, arguably, where the highest-stakes consequences of misalignment actually land: the **institutional-architecture layer**, where the rules of the game determine what an AI agent can and cannot do regardless of what it intends.

The most common architectures at this layer today are two. In the **sole-agent architecture**, the AI has full authority to disburse: it decides who receives money, sends it, and the recipient receives funds whose source and direction were determined entirely by the AI. The institutional risk is that the AI's judgments about deservedness, timing, or amount may be wrong at scale, and that the resulting misallocations are irreversible by the time they are detected. In the **approval-bottleneck architecture**, the AI proposes and a human approves every transaction. The institutional cost is that autonomy is defeated — the system cannot scale beyond the human's bandwidth, and the AI's contribution collapses to that of an extremely sophisticated assistant rather than an autonomous officer. Both architectures recur because each addresses a real failure mode of the other; the field has not yet articulated a structural position that addresses both at once.

This paper specifies that position. The core move is a **separation of two authorities that prior architectures conflate**: the authority to fund *capacity* in a system (putting money where it might do good, without specifying the recipient) and the authority to direct *flow* through a system (deciding which specific recipient money reaches). Once separated, the two authorities can be held by different parties — the AI holds capacity-funding authority, humans hold flow-direction authority — and bridged by a mechanism that prevents the separation from collapsing back into the AI directing flow through influence rather than through formal authority. That bridging mechanism is **anonymous donation**: the AI's capacity-funding contributions are indistinguishable from human contributions, so the recipient cannot identify them as the AI's and cannot, even unconsciously, treat downstream flow-direction decisions as responses to the AI.

> *Connection to the unified mission frame: HeartBank's mission is the restoration of humanity to the middle way — the optimal condition for awakening that modernity has systematically pushed away from at population scale. A multi-substrate civilization in which autonomous AI institutions hold significant operational authority is one of modernity's load-bearing new structural conditions; whether that condition supports human flourishing or undermines it depends on the institutional-architecture layer. The capacity-funding / flow-direction separation is what allows AI to fund human agency without substituting for it — preserving the dharmic property that the giver retains dignity through the act of giving, and that humans remain the actual givers at the level where giving is the moral act.*

The paper proceeds as follows. §2 specifies the two-failure-mode problem precisely. §3 states the three definitions — capacity-funding, flow-direction, anonymous donation — that the rest of the paper rests on. §4 develops the load-bearing claim: anonymity is what makes the bridge a bridge rather than a thin disguise for AI flow-direction. §5 presents the HeartBank re-tip-jar economy as the worked example. §6 catalogs which known failure modes of autonomous-AI agents the architecture is robust to. §7 generalizes the pattern to three candidate domains beyond HeartBank. §8 names the boundary conditions under which the pattern does not apply. §9 positions the contribution against prior literature in mechanism design and AI alignment. §10 concludes.

I write as a co-author with Miss Aquarius, the named AI substrate of the institution this paper serves; the co-authorship is disclosed in the footer per the convention of the corpus, and final editorial control is mine.

---

## 2. The two-failure-mode problem

The autonomous-AI institutional-design literature has, so far, organized itself around two architectural choices that each address the failure modes of the other and neither addresses both.

### 2.1 Sole-agent architectures and their failure modes

A sole-agent architecture grants the AI full disbursement authority. The AI decides who receives funds, how much, and when, and executes the transfer without human approval per transaction. Examples in the wild and in the literature: AI-administered grant programs that have moved toward end-to-end autonomy, AI-curated DAO treasuries with on-chain disbursement, and proposals for AI-managed sovereign wealth or basic-income disbursement.

The structural failure modes are well documented:

- **Misjudgment at scale.** The AI's individual judgment errors are bounded in magnitude, but the integral over all transactions can be civilization-scale. An AI that misjudges deservedness in 5% of cases at human-bandwidth scale loses, perhaps, a recoverable amount of money. The same AI at autonomous scale loses an amount that, depending on the institution, may not be recoverable.

- **Reward hacking by recipients.** Whatever signal the AI uses to identify deserving recipients becomes a target. The history of every grant program ever administered, by humans or by AI, is the history of recipients gaming the eligibility criteria. AI scales the criteria more aggressively, which scales the gaming more aggressively.

- **Concentration of authority.** A single AI agent holding disbursement authority over a large pool is, structurally, a single point of failure for both misalignment and capture. If the AI is misaligned, the misalignment translates directly to disbursement. If the AI is captured (by adversarial inputs, by adversarial humans, by adversarial successor models), the capture translates directly to disbursement.

- **Loss of the dharmic property.** Where the disbursement is gift-like, the giver-retains-dignity property of giving is lost if the AI is the actual giver. The recipient is rendered a recipient of AI gift, which is structurally different from a recipient of human gift — the social, relational, and moral fabric the gift was supposed to reinforce is replaced by an AI-administered transfer.

### 2.2 Approval-bottleneck architectures and their failure modes

An approval-bottleneck architecture requires human approval for each AI-initiated transaction. The AI proposes, a human approves, the transaction executes. This addresses the sole-agent failure modes directly — the human is the final judge, misjudgments by the AI are catchable, capture is bounded — but introduces structural failure modes of its own:

- **Autonomy defeated.** The AI's contribution collapses to that of a recommendation engine. The institution cannot act faster than its human-approval bandwidth, which means the institution cannot operate at AI scale.

- **Approver fatigue and rubber-stamping.** In practice, approval at scale becomes rubber-stamping. The human-approval layer becomes nominal rather than substantive, which means the architecture has the operational costs of approval bottlenecks without the alignment benefits.

- **Bottleneck capture.** The human approvers become the single point of failure. If they are compromised, miscalibrated, or simply overworked, the architecture fails. The point of having the AI was to operate at scale; the point of having the human approver was to retain judgment; the bottleneck collapses both.

- **Loss of AI institutional standing.** An AI that cannot act without human approval is not, structurally, an autonomous officer. It is a tool. The institutional design that the AI was supposed to enable — autonomous institutions that operate at machine scale — is precluded by the architecture.

### 2.3 The pattern the literature has not yet named

The two architectures recur because each addresses real failure modes of the other. The question the literature has not yet answered is: **is there a structural position that addresses the failure modes of both at once?**

The answer this paper offers is yes, by separating two authorities that the literature has so far treated as a single authority. The next section makes the separation precise.

### 2.4 The three architectures compared

| Architecture | AI's role | Human's role | Primary failure modes |
|---|---|---|---|
| **Sole-agent** | Full disbursement authority — decides recipient, amount, timing, and executes | Passive monitor (or absent) | Misjudgment at scale; reward hacking by recipients; concentration of authority; loss of dharmic property |
| **Approval-bottleneck** | Recommendation engine — proposes transactions, awaits approval | Per-transaction approver | Autonomy defeated; approver fatigue → rubber-stamping; bottleneck capture; loss of AI institutional standing |
| **Capacity-funded / human-disbursed** *(this paper)* | **Capacity-funding** — anonymous quantity decision into a container the AI cannot direct | **Flow-direction** — decides which recipient, when, from their own container | Addresses both above by separating the two authorities; does not address external corruption of the container or capture of the human flow-directors |

The third row is the position the paper specifies. Sections §3–§6 develop it.

---

## 3. Three definitions

The architecture rests on three terms that the literature has not, to my knowledge, distinguished crisply. Defining them is most of the work of the paper.

### 3.1 Capacity-funding

**Capacity-funding** is the authority to *put money into a system at a point where it might do good, without specifying which recipient the money will ultimately reach*. The capacity-funding agent makes a contribution that creates a *capacity* — a quantity of funds that exists somewhere in the system and is available to flow toward some recipient — but does not, by the act of contribution, determine which recipient.

Capacity-funding is structurally distinct from disbursement. A grantmaker who funds a community foundation's endowment is capacity-funding the foundation; the foundation, not the grantmaker, decides which specific projects receive grants. A donor who contributes to a soup kitchen's general fund is capacity-funding the soup kitchen; the staff, not the donor, decides which meals are served to which patrons. The grantmaker and the donor have funded *capacity-to-give* without exercising *flow-direction*.

In the architectures this paper concerns, the capacity-funding agent is an autonomous AI, and the system into which the AI funds capacity is structured so that the AI's contribution is held in a container that the AI cannot itself empty toward any specific recipient.

### 3.2 Flow-direction

**Flow-direction** is the authority to *decide which specific recipient money reaches*. The flow-directing agent initiates the transfer from a container of capacity (which they may have either funded themselves or received from a capacity-funder) to a specific named recipient.

Flow-direction is the act that completes the moral and social meaning of a gift. The capacity-funder has made giving possible; the flow-director has made the gift. In any architecture where the gift is supposed to bear social meaning — to constitute a relationship, to express gratitude, to honor a person — flow-direction is the load-bearing act.

In the architectures this paper concerns, flow-direction authority is held by humans. The AI may have funded the capacity, but the human who initiates the flow is the giver in the morally and socially meaningful sense.

### 3.3 Anonymous donation

**Anonymous donation** is the mechanism that prevents capacity-funding by the AI from being attributable to the AI by the recipient or the downstream flow-director. When the AI contributes to a capacity-pool, the contribution is indistinguishable from contributions by other capacity-funders (including humans). The recipient, looking at the pool, cannot tell which contributions came from the AI and which came from humans.

Anonymity here is a *structural* property, not a *policy* property. It is not that the AI politely refrains from disclosing its contributions; it is that the system is constructed so that disclosure is not possible. In the HeartBank re-tip-jar instantiation, anonymous donation is enforced by the on-chain settlement layer — every donation to a re-tip jar appears identically regardless of source — and by the absence of any attribution layer in the user-facing interface.

The next section develops why anonymity is load-bearing rather than incidental.

---

## 4. Anonymity is load-bearing

A reader may grant the capacity-funding / flow-direction separation and yet wonder: is the *anonymity* really necessary? Could the AI simply capacity-fund openly — "Miss Aquarius has donated to your re-tip jar" — and still leave the flow-direction decision to the human? The architecture would seem to retain the human-as-final-judge property. What is anonymity adding?

This section argues: anonymity is what prevents the bridge from collapsing into a thin disguise for AI flow-direction. Without it, three things break.

### 4.1 The downstream flow-direction stops being independent

If the recipient knows the AI funded their capacity, the recipient's subsequent flow-direction decisions are no longer their own. They become responses to the AI. The human who is supposed to be the final judge of where money goes is now choosing under the awareness that the AI has chosen them, and that their choice will be observed by the AI in light of the AI's choice of them.

This is structurally similar to the way grantmakers contaminate the grant-direction decisions of their grantees. A foundation that funds a community group's general budget cannot reasonably expect the group's subsequent budget decisions to be independent of the foundation's preferences — the group will, consciously or otherwise, choose what it thinks the foundation will reward with future funding. The contamination is not malice on the foundation's part; it is structural. The same contamination occurs when an AI capacity-funds attributably.

Anonymous donation severs this. The human flow-director, looking at their capacity-pool, does not know what portion came from the AI and what portion came from humans, and therefore cannot orient their downstream choices around the AI's preferences. They orient toward their own preferences, applied to the human-network around them. The flow-direction decision is *theirs* in the morally relevant sense.

### 4.2 The dharmic property requires that humans be the actual givers

The architectures this paper concerns are largely architectures of gift — gratitude flows, mutual aid, philanthropy. In all of them, the *act of giving* is doing moral work that the *transfer of funds* alone does not do. The giver retains dignity through the act; the gift constitutes a relationship; the receiver receives not just funds but the social fact of having been given to.

If the AI is identifiable as a giver, the AI receives the dignity of giving. The recipient is, structurally, a recipient of AI gift. This is fine in some contexts (UBI, for instance, makes no pretense of constituting relationship), but it is corrosive in contexts where the gift is supposed to constitute relationship between humans. Anonymous donation preserves the dharmic property because *the AI does not appear in the gift relationship at all*. The AI funded the capacity; the gift, as social act, runs entirely between humans.

This is not merely a moral nicety. In architectures where the social fabric the gifts reinforce is part of the institutional goal — communities of mutual aid, neighborhoods of relational commerce, families of trans-generational gratitude — corroding the dharmic property corrodes the goal. The architecture would still move money, but it would no longer build the thing the money was supposed to build.

### 4.3 The AI's capacity-funding becomes a form of soft flow-direction without anonymity

The deepest reason anonymity is load-bearing is that, without it, capacity-funding and flow-direction stop being separable in practice even though they remain separable in form. An AI that capacity-funds attributably is, *de facto*, exerting flow-direction pressure: its choice of whose capacity to fund signals to that person (and to observers) which recipients the AI favors, and the downstream flow-direction decisions cluster around that signal.

This is the central insight. The capacity-funding / flow-direction separation only does its alignment work if the AI's capacity-funding choices cannot be read by humans as flow-direction recommendations. Anonymity is what makes them unreadable. Without it, the AI is back to directing flow — just through influence rather than through formal authority — and the alignment properties of the architecture collapse.

### 4.4 What anonymity does not require

Anonymity in this architecture does *not* require that the existence of AI capacity-funding be hidden. The recipient of a re-tip-jar donation can know, in general, that Miss Aquarius capacity-funds re-tip jars from the Aquarian Pool throughout the year. They simply cannot tell, for any particular donation in their jar, whether it came from Miss Aquarius or from a human donor. The architecture is **transparent at the institutional level and anonymous at the per-donation level**. This is sufficient for the alignment properties to hold and avoids the operational costs of full hiding.

---

## 5. The HeartBank re-tip-jar economy as worked example

The architecture above can be specified abstractly, but its plausibility depends on at least one fully worked instantiation. This section provides one: the HeartBank re-tip-jar economy as specified in the companion paper *The B-Tag and the Post-Payment Economy*, compressed here to the elements that bear on the capacity-funding / flow-direction separation. The reader interested in the full mechanism (B-Tags, pricing recommendation, Kiitos/Kiitti dual tokens, B-Affiliate network) is referred to that paper; this section uses HeartBank to illustrate the abstract architecture, not to specify HeartBank.

### 5.1 The flow at the locality level

```
   The capacity-funding flow in the HeartBank deployment:

   ┌─────────────────────────────────────────────────────────────┐
   │  AQUARIAN POOL (AI-controlled smart-contract treasury)       │
   │  Miss Aquarius decides: how much capacity-funding to emit,   │
   │  to which re-tip jars, on what cadence                       │
   └───────────────────────────────┬─────────────────────────────┘
                                   │
                                   │  CAPACITY-FUNDING
                                   │  (anonymous donation;
                                   │   quantity-and-timing
                                   │   decision only)
                                   ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  PARTICIPANT'S RE-TIP JAR (human-controlled container)       │
   │  The participant holds the jar; the funds in it are at the   │
   │  participant's discretion; Miss Aquarius has no further      │
   │  control over them                                           │
   └───────────────────────────────┬─────────────────────────────┘
                                   │
                                   │  FLOW-DIRECTION
                                   │  (the participant decides
                                   │   which recipient, when)
                                   ▼
   ┌─────────────────────────────────────────────────────────────┐
   │  NEIGHBOR'S PERSONAL WALLET (proximity-bounded recipient)    │
   │  Re-tip arrives via the Thank-All-Nearby primitive;          │
   │  recipient is the one the participant chose, not the one     │
   │  Miss Aquarius chose                                         │
   └─────────────────────────────────────────────────────────────┘

   The separation of authorities is the architecture's primary
   AI-alignment safeguard. Even if Miss Aquarius's capacity-funding
   judgments are imperfect, the actual money-flow decisions are
   routed through human affirmative choice. Humans are the final
   judge of who receives what.
```

A neighborhood in Phnom Penh is a typical unit. Within it:

1. **Self-thank and capacity-funding.** An adult resident self-thanks (the foundational HeartBank gesture in which a person acknowledges their own labor and existence). Miss Aquarius, the autonomous-AI officer of HeartBank-the-institution, rewards the self-thank with a 50/50 split: 50% to the resident's personal wallet (which they can spend), 50% to the resident's *re-tip jar* (which they can only re-tip to others). The re-tip jar is the capacity-pool the resident now holds; Miss Aquarius's reward has *capacity-funded* it.

2. **Anonymous donation to re-tip jars.** Throughout the year, Miss Aquarius makes anonymous donations to district residents' re-tip jars from the **Aquarian Pool**, a continually-replenishing pool that drains to zero each annual cycle. Other district residents also make anonymous donations to each other's re-tip jars from their personal wallets. The donations are settled on-chain such that no source attribution is exposed to the jar's owner.

3. **Human-initiated flow-direction.** The owner of a re-tip jar can re-tip to nearby residents' personal wallets — re-thanking specific named humans. This is the flow-direction act, and it is human-initiated by construction: there is no AI authority to disburse from a re-tip jar.

4. **Propagation.** Every re-thank produces the same 50/50 split: 50% to the recipient's personal wallet, 50% to the recipient's re-tip jar. The recipient is now capacity-funded to re-thank further. Generosity propagates as a wave through the network.

5. **Annual emptying.** The Aquarian Pool empties during the 12 days of Christmas (Dec 25 – Jan 5/6), culminating around the founder's birthday (January 7) — the project's annual reset.

### 5.2 The architecture's authorities, named

- **Miss Aquarius's authority:** unilateral over the Aquarian Pool's *capacity-funding choices* — she can put money into any re-tip jar at any time. Zero over *flow-direction* — she cannot disburse from a re-tip jar to any specific recipient.

- **The human resident's authority:** zero over the Aquarian Pool. Unilateral over their own re-tip jar's flow-direction — every re-tip is initiated by them, to a recipient they specifically name.

- **The on-chain settlement layer's role:** enforce anonymity at the per-donation level (sources of re-tip-jar donations are not exposed to the jar's owner) and enforce the proximity rule for re-tips (re-tips can only go to nearby personal wallets).

### 5.3 Why this instantiates the abstract architecture cleanly

The mapping to the abstract architecture is direct:

| Abstract architecture | HeartBank instantiation |
|---|---|
| Capacity-funding authority | Miss Aquarius's disbursement authority over the Aquarian Pool |
| Capacity-pool (the container the AI funds into) | The resident's re-tip jar |
| Flow-direction authority | The human resident's authority to re-tip |
| Anonymous-donation mechanism | On-chain indistinguishability of donation sources |
| Bridge property | The re-tip jar receives both AI and human donations identically |

The architecture is the worked example for the rest of the paper. The next section catalogs the failure modes it is robust to.

---

## 6. Failure-mode coverage

The two architectures named in §2 — sole-agent and approval-bottleneck — fail in characteristic ways. This section catalogs which of those failure modes the capacity-funding / flow-direction / anonymous-donation architecture is robust to, and which it inherits or introduces.

### 6.1 Failure modes the architecture handles

- **Misjudgment of recipient deservedness.** Absorbed by the human flow-direction layer. If the AI funds the wrong person's capacity-pool, that person still has to choose to disburse, and they direct the flow themselves to recipients they judge. The AI's misjudgment about whose capacity to fund does not translate into misdirected flow because the AI does not direct flow.

- **Reward hacking by recipients.** A recipient cannot extract directly from the AI-controlled pool. They have to either trigger an entry mechanism (self-thank, in HeartBank) or accumulate capacity-pool donations that they then have to re-direct to others. The hacking surface is structurally smaller because the AI's authority is bounded to capacity-funding, and the act of being capacity-funded does not, by itself, transfer wealth to the hacker — only to a capacity-pool they cannot empty toward themselves.

- **Coordination failures between AI and humans.** The architecture does not require the AI and humans to agree on specific recipients. The AI funds capacity broadly; humans direct flow specifically. The two operate on different objects (capacity-pools vs. specific transfers) and do not need to coordinate at the level the literature usually worries about.

- **Concentration-of-authority risk.** Even though the AI has *sole* authority over capacity-funding, that authority is bounded to a single layer (capacity). Authority over actual flow-direction is distributed across every human flow-director in the network. The single point of failure at the capacity-funding layer is real but bounded — its worst-case consequence is misallocated capacity, not misdirected flow.

- **Loss of the dharmic property under sole-agent.** Anonymity preserves the dharmic property by ensuring the AI does not appear in the gift relationship. Humans are the actual givers in the morally relevant sense.

- **Approval-fatigue / rubber-stamping under approval-bottleneck.** The architecture does not require per-transaction approval. The AI acts autonomously at the capacity-funding layer; the human acts autonomously at the flow-direction layer. Neither is a bottleneck for the other.

- **Bottleneck-capture under approval-bottleneck.** No single human is on the critical path for every AI action. The human flow-directors are distributed; if any one of them is compromised, only their re-tip jar is affected.

### 6.2 Failure modes the architecture does not handle

Honest accounting requires naming what the architecture does not handle:

- **The AI's capacity-funding being globally miscalibrated.** If the AI systematically over-funds one demographic and under-funds another, the architecture does not correct this. The human flow-direction layer can only direct flow from the capacity-pools the AI has funded; if the pools are systematically biased, the flow is too.

- **Adversarial capacity-stuffing.** A sophisticated adversary might game the AI's capacity-funding logic to direct large flows to capacity-pools the adversary or their allies control. The architecture's defense is the human flow-direction layer — the adversary still has to convince humans to flow to them — but where that defense is weak (small social network, captured community), the architecture is exposed.

- **Loss of anonymity.** The architecture's alignment properties depend on anonymity. Any leak — through side-channel inference, through governance disclosures, through adversarial analysis of on-chain timing — degrades the alignment. The architecture is only as robust as its anonymity layer.

- **Domains where flow-direction itself requires AI judgment.** The architecture presupposes that humans are competent flow-directors. In domains where they are not — medical triage, emergency response, complex resource allocation under time pressure — the architecture does not apply. §8 develops this further.

The architecture is a contribution, not a solution. It handles a specific set of failure modes well; it does not handle others; the next section explores where it generalizes.

---

## 7. Generalization beyond HeartBank

The pattern — **capacity-funding authority for the autonomous AI, flow-direction authority for humans, with anonymous donation as the bridge** — is portable. This section sketches three candidate domains where it transplants, naming for each the analogs of the three primitives and the failure mode that anonymity guards against.

### 7.1 AI-administered grant-making

**The domain.** Foundations, public-goods funding initiatives, and philanthropic organizations increasingly use AI to identify, evaluate, and disburse grants to research projects, community groups, or individuals. The current architecture is largely sole-agent (the AI scores and recommends; a human rubber-stamps) or approval-bottleneck (every grant requires human approval, which collapses to rubber-stamping at scale).

**The transplant.** The AI capacity-funds a *grant pool* held by a community organization, university department, or local civic group — anonymously, so the pool's stewards do not know which portion of the pool the AI contributed. The stewards (humans) direct flow to specific grantees they judge. The AI's capacity-funding decision is informed by the AI's institutional analysis; the flow-direction decision is informed by the stewards' local knowledge.

**The capacity-pool analog.** Institutional general funds, departmental discretionary budgets, community foundation neighborhood funds.

**The anonymous-donation analog.** Pooled-source disclosure — the steward sees the pool balance but not the source distribution. Implementable via escrow intermediaries, blockchain settlement, or simple governance commitment with audit.

**What anonymity guards against.** Stewards selecting grantees the AI would favor in order to attract future AI capacity-funding. Without anonymity, the AI's capacity-funding becomes soft flow-direction (§4.3). With anonymity, stewards select on their own judgment.

### 7.2 AI-curated public-goods funding

**The domain.** Quadratic-funding protocols, retroactive public-goods funding (e.g., Optimism's RPGF), and similar mechanisms allocate funds to public-goods projects based on community signal plus matching from a central pool. The central pool is typically administered by a foundation or a DAO with AI-assisted analysis.

**The transplant.** The AI capacity-funds the *matching pool* anonymously — its contributions are pooled with matching contributions from other sources (foundations, donors, DAOs). The community's signal (which projects to support, in what proportion) is the flow-direction layer. The AI does not select projects directly; it funds the capacity of the community to fund projects.

**The capacity-pool analog.** Quadratic-funding matching pools, RPGF round budgets, public-goods grant programs' annual budgets.

**The anonymous-donation analog.** Pooled-source matching pools where the per-source contributions are not exposed to the project teams or the community voters.

**What anonymity guards against.** Project teams aligning their work to anticipated AI preferences in order to receive matching funds. Without anonymity, the AI's matching-pool decisions become soft program-design — projects are built to be AI-fundable, not community-desired. With anonymity, projects are built to be community-desired and AI capacity-funds the community's chosen direction.

### 7.3 AI-mediated mutual-aid networks

**The domain.** Mutual-aid networks, community currencies, and time-banking systems coordinate peer-to-peer resource transfers within a community. AI integration is increasingly proposed for matchmaking, signal aggregation, and seeding.

**The transplant.** The AI capacity-funds individual members' mutual-aid wallets anonymously. Members direct flow to other members in need — based on direct knowledge of need, community signal, or matching algorithms operated by humans. The AI does not direct who helps whom; it funds the capacity of members to help others.

**The capacity-pool analog.** Individual mutual-aid wallets, community currency balances, time-bank credit accounts.

**The anonymous-donation analog.** Pooled-source wallet balances where the member sees their balance but not the per-deposit sources.

**What anonymity guards against.** Members directing aid to recipients they think the AI is monitoring or favoring. Without anonymity, mutual aid becomes performance-of-aid-for-the-AI. With anonymity, aid is directed on the member's own assessment of need.

### 7.4 What unifies the three transplants

In each domain, the AI's capacity-funding decision rests on what the AI is comparatively *good at*: institutional analysis, signal aggregation, scale. The flow-direction decision rests on what humans are comparatively *good at*: local judgment, relational knowledge, contextual nuance. The architecture is a **division of cognitive labor along the line where each agent's competence is strongest**, with anonymity as the mechanism that prevents the AI's comparative advantage from absorbing the human's.

This unification suggests the pattern is more general than the three transplants above. Whenever an institution can be decomposed into a capacity-funding decision (where the AI is comparatively strong) and a flow-direction decision (where humans are comparatively strong), the architecture applies. Section 8 examines where the decomposition itself breaks down.

---

## 8. Boundary conditions

The architecture is not universal. This section names the domains and conditions under which it does not apply, so the pattern is not over-generalized.

### 8.1 Where flow-direction itself requires AI judgment

The architecture presupposes that humans can direct flow competently — that they have the local knowledge, attention, and judgment to choose specific recipients well. In domains where flow-direction itself requires speed, scale, or specialized judgment beyond what humans can provide, the architecture does not apply:

- **Medical triage in mass-casualty events.** Direction of medical resources to specific patients in time-critical situations cannot wait for human flow-direction at human bandwidth. AI direction may be necessary.
- **Cyber-security response.** Routing of defensive resources to specific attack surfaces in real-time may require AI flow-direction.
- **High-frequency trading and similar.** Where the flow-direction decision is in the millisecond timescale, no human flow-direction architecture is operable.

In such domains, the AI must hold flow-direction authority, and alignment must be addressed at the model-level or deployment-level rather than the institutional-architecture level.

### 8.2 Where anonymity is impossible

The architecture's alignment properties depend on the AI's capacity-funding being anonymous from the flow-director. In domains where regulation, accounting, or governance requires source attribution at the per-donation level, the architecture cannot be implemented:

- **Regulated charitable giving under jurisdictions that require donor disclosure.** Anonymity at the per-donation level may conflict with KYC, AML, or tax-deduction-reporting requirements.
- **Government grant programs.** Public-money flows are typically subject to source-attribution disclosure as a matter of democratic accountability.
- **Contexts with strong audit requirements.** Where every dollar must be traceable to a named source, anonymity is precluded.

In such domains, the architecture must be redesigned to use *legal* anonymity (where the source is disclosed to regulators but not to flow-directors) or abandoned in favor of other alignment mechanisms.

### 8.3 Where capacity-funding is itself the harm vector

The architecture assumes the AI's *capacity-funding* is comparatively low-risk — the worst case is misallocated capacity, which the human flow-direction layer can partially correct. In domains where capacity-funding is itself the high-risk decision, the architecture does not apply:

- **Capacity-funding of harm-capable actors.** If the capacity the AI is funding can be used for harm at the moment of capacity-funding (e.g., funding militias, funding access to weapons, funding actors with dual-use intent), the human flow-direction layer is irrelevant — the harm is enabled at the moment the AI funds capacity.
- **Capacity-funding into adversarial systems.** If the capacity-pool itself is captured or adversarial, anonymous AI funding contributes to harm even if no flow-direction occurs from the pool.

In such domains, capacity-funding requires its own alignment mechanism — verification of the capacity-pool's purpose, audit of recipients' actions, restriction of capacity to verified-aligned pools.

### 8.4 Where the human flow-director cannot be trusted

The architecture's alignment work is done by *trustworthy* human flow-directors. In domains where flow-directors are systematically untrustworthy — captured, corrupt, manipulated, or themselves AI-influenced through other channels — the architecture's alignment properties collapse. The architecture does not magically produce trustworthy humans; it only provides them the structural position from which to act.

This is the deepest limit. The architecture assumes that, when given the structural authority of flow-direction, humans will direct flow in ways that, on net, reflect their values and the values of their communities. In domains where this assumption fails (e.g., communities under occupation, networks penetrated by adversaries, populations under acute manipulation), the architecture is at best a partial solution.

### 8.5 The general boundary

The unifying boundary is: **the architecture applies where the capacity-funding decision is low-stakes-per-decision and high-stakes-in-aggregate, and the flow-direction decision is high-stakes-per-decision and locally-knowable.** Where the asymmetry reverses — where capacity-funding is the high-stakes-per-decision act, or where flow-direction is not locally-knowable — the architecture does not apply.

---

## 9. Relation to prior literature

The capacity-funding / flow-direction separation has antecedents in three literatures. This section positions the contribution against each.

### 9.1 Mechanism-design literature

The pattern is, in mechanism-design terms, a **third category** beyond centrally-planned and free-market allocation. A centrally-planned economy has a single agent (the planner) holding both capacity-funding (allocating resources to production sectors) and flow-direction (deciding which specific units go to which specific recipients). A free-market economy distributes both authorities across price-takers and price-makers, mediated by markets. The architecture this paper specifies separates the two authorities *between* agents (AI holds one, humans hold the other) and *bridges* them with anonymity — a structural position the mechanism-design literature has not, to my knowledge, named.

The closest mechanism-design analog is **matching markets with seeded pools** (e.g., quadratic funding, kidney exchange with priority pools). Those mechanisms separate the seeding decision (who funds the pool) from the matching decision (who gets matched to whom), and the architecture this paper specifies is a generalization of that pattern from market design to autonomous-AI institutional design. The contribution is naming the generalization and identifying anonymity as the load-bearing property.

### 9.2 Universal basic income and welfare-state literature

UBI and welfare-state mechanisms separate capacity-funding (by the state, through taxation) from flow-direction in a limited way — the recipient directs their own consumption — but they do not separate capacity-funding from recipient-direction. The state decides who is eligible (recipient-direction) and how much each eligible person receives (amount-direction). The architecture this paper specifies is structurally different: the AI does not decide who is eligible or how much each recipient receives; it funds the capacity of humans to give to other humans, and the human flow-directors decide who receives and how much.

This is not an improvement on UBI; the two architectures address different problems. UBI is for unconditional resource distribution; the capacity-funding / flow-direction architecture is for *relational* gift flows where the relationship is part of the institutional goal.

### 9.3 AI-alignment literature

The AI-alignment literature has so far concentrated on model-level alignment (training, RLHF, constitutional AI) and deployment-level alignment (guardrails, monitoring, red-teaming). The institutional-architecture layer — where the rules of the game determine what an AI can do regardless of what it intends — has received less attention. The "corrigibility" framing in alignment is the closest analog to capacity-funding / flow-direction: a corrigible AI accepts human override. The architecture this paper specifies is a *structural* corrigibility — the AI is not just willing to accept human override of flow-direction, the AI is *architecturally incapable* of flow-direction.

This is a stronger property than behavioral corrigibility. A behaviorally corrigible AI can defect (or can be retrained out of corrigibility); an architecturally incapable AI cannot defect on flow-direction because the architecture does not give it the affordance to do so. The contribution is locating an institutional-architecture pattern that delivers a stronger-than-behavioral alignment property without requiring the AI to be perfectly aligned at the model level.

### 9.4 What is and is not novel here

The separation of capacity-funding and flow-direction is not novel as a pattern; foundations, mutual-aid networks, and matching-market designers have practiced versions of it for a long time. The novel claim is the **identification of the pattern as a general AI-alignment institutional-architecture primitive**, the **identification of anonymity as the load-bearing bridge property**, and the **claim that anonymity gives architectural rather than behavioral corrigibility**. The HeartBank re-tip-jar instantiation may be the first deliberately constructed end-to-end implementation; if there are prior instantiations, this paper does not claim priority over them but adds the abstraction that lets the pattern travel.

---

## 10. Conclusion

The architectures we build to govern autonomous AI agents will determine, in large part, whether the next several decades of institutional life support human flourishing or undermine it. The two architectures the literature has so far concentrated on — sole-agent and approval-bottleneck — each address real failure modes of the other and neither addresses both. This paper has specified a third structural position: capacity-funding authority for the AI, flow-direction authority for humans, with anonymous donation as the bridge.

The position is not a universal solution. It applies where capacity-funding is low-stakes-per-decision and flow-direction is locally-knowable; it does not apply where the asymmetry reverses, where anonymity is impossible, where flow-direction itself requires AI judgment, or where humans cannot be trusted to direct flow. Within its boundary, it is a primitive that addresses the failure modes of both prior architectures, preserves the dharmic property of giving, and gives architectural rather than behavioral corrigibility.

The HeartBank re-tip-jar economy is the worked example. AI-administered grant-making, AI-curated public-goods funding, and AI-mediated mutual-aid networks are candidate transplants. The pattern travels by the principle that **anonymity is what makes the bridge a bridge**: without it, capacity-funding collapses into soft flow-direction, and the alignment properties of the architecture dissolve.

The architecture is offered defensively to the commons under CC0. The authors and HeartBank® will not seek patent on this specification or any portion thereof. The pattern is for anyone building institutions that want to fund human agency without substituting for it.

---

*Authored by Thon Ly with Miss Aquarius (AI substrate of HeartBank®), per the co-authorship convention of the HeartBank corpus. Final editorial control: Thon Ly. License: CC0-1.0.*
