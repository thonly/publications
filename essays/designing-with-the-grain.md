---
title: "Designing with the Grain: When Institutional Trade-offs Dissolve into Coincidences of Goods"
subtitle: "A design diagnostic discovered in building HeartBank — and the discipline that keeps it honest"
authors: "Thon Ly · Miss Aquarius"
category: essays
priority: tier-c
status: draft
date: 2026-06-26
license: CC0-1.0
slug: designing-with-the-grain
venue: thonly.org/research/designing-with-the-grain (canonical) · LessWrong / future Substack (intended publication venues)
---

> **Draft note.** This essay is *substrate-drafted in the founder's voice, pending his revision into his own.* Per the author-voice discipline, public-attribution essays are Thon Ly's voice — the ideas, the framing, the byline — drafted in collaboration with Miss Aquarius℠, with final editorial control retained by Thon. What follows is a faithful first draft of a methodology I keep rediscovering as I build; the prose is the substrate's until Thon has gone over it, but the diagnostic and the cautions are the ones we arrived at together.

---

## The argument in one sentence

The hardest design tensions in building HeartBank®, pushed far enough, keep refusing to stay trade-offs — they collapse into **coincidences of goods**, two goods that turn out to be one good seen from two sides — and that collapse is usable as a diagnostic: *a forced trade-off is the signal that a design is still misaligned; a dissolution into a coincidence of goods is the signal that you've found the grain — so keep redesigning until the trade-off dissolves.* The grain you are aligning with is the grain of the gift.

---

## What the grain is

I learned the most useful thing I know about design from wood, not from software.

A board of wood has a grain — a direction the fibers run, set while the tree was alive, fixed long before the board reached your bench. You cannot see it perfectly and you cannot argue with it. When you plane *with* the grain, the blade shears the fibers clean and the work is almost effortless; the tool wants to go where you are pushing it. When you plane *against* the grain, the blade catches under the fibers and tears them out in chunks — *tearout*, woodworkers call it — and the harder you push to fix the surface, the worse you wreck it. A beginner, hitting tearout, presses harder and sharpens the blade and blames the tool. A craftsman hits tearout, stops, and turns the board around. The tearout was never a problem to be muscled through. It was information. It was the wood telling you which way it was built.

I have come to believe that the hardest tensions in institutional design are tearout.

When you are building something — a product, a mechanism, a business model — you keep running into what look like fundamental trade-offs: you can have *this* good or *that* good, but the more you get of one the less you get of the other, and the design problem is "where do I set the dial." Safety against reach. Mission against revenue. Privacy against virality. Depth of need against breadth of market. These feel like the bedrock of the craft — the grown-up acknowledgment that you can't have everything, that engineering is the art of the least-bad compromise. And a great deal of the time that is exactly what they are.

But not always. Building HeartBank, I kept hitting trade-offs that, when I stopped pushing and turned the board around, *stopped being trade-offs.* The two goods I thought I was choosing between turned out to be the same good, approached from two angles. The dial I was agonizing over didn't exist; there was nothing to trade. And every single time this happened, it happened the same way: it happened when I stopped trying to make the gift behave like an exchange and let it behave like a gift.

That is the whole of what this essay has to say, and the rest is just showing the work. First the dissolutions — six tensions that refused to stay trade-offs. Then the diagnostic they suggest. Then *why* it works — what grain, exactly, I keep aligning with. And then, at length and on purpose, the part that matters most: why a method that rewards you for finding coincidences is dangerous, and what discipline keeps it honest.

A word before the examples, said plainly so it colors everything after: almost all of this is theory. The coherence I am about to describe is, at the time of writing, a coherence of *ideas* — the empirical base under the whole structure is a single pilot family and a handful of alpha users. I will come back to that hard at the end. Hold it the whole way through.

---

## Six tensions that refused to be trade-offs

### 1. The best time to ask is the best people to ask

HeartBank's time-economy, Chronicle, has to fund itself without committing the cardinal sin of the loneliness industry — building a business whose incentives are served by keeping people lonely. The cleanest answer is patronage: people with means voluntarily fund free access for everyone else. But patronage has a famous failure mode, the Wikipedia banner that almost nobody clicks, and the failure is always one of two things — you ask at the wrong *time* (cold, disconnected from any felt value) or you ask the wrong *people* (a broadcast to everyone, most of whom don't care).

So it reads as two problems with a tension between them. Good timing wants you to wait for a peak moment, which is rare and hard to detect. Good targeting wants you to identify the willing, which sounds like surveillance — profiling who has money and a soft heart. Optimize one and you seem to compromise the other: precise targeting in real time, at the exact peak, for each person, is the kind of thing only an advertising machine does, and the advertising machine is the thing we are trying not to be.

Turn the board. Ask the patronage question *right after a person has redeemed un-bought time and actually felt the presence of someone who showed up for them.* In that moment, the best *time* to ask and the best *people* to ask are not two targets to reconcile — they are **one event**. The afterglow is the peak felt-value (so it is the right time) and the satisfied redeemer, by the simple fact of having been moved, **self-identifies** (so it is the right person). Willingness is *demonstrated*, not surveilled — the exact inverse of ad-targeting, which has to guess at willingness from data because it never has the felt experience to anchor to. There was no dial. Timing and targeting were the same good wearing two names.

### 2. The deepest need is the lowest risk

A presence product looks like it faces a brutal trade-off between need and safety. The deepest loneliness, you'd assume, lives among the most isolated — people with no one, who would have to be matched with *strangers* — and stranger-matching for in-person presence is the single highest trust-and-safety risk category that exists. So serving the deepest need seems to require accepting the worst safety exposure; protecting safety seems to require retreating to shallower need. Set the dial.

Turn the board. The loneliness literature distinguishes *social* loneliness (too few contacts) from *emotional* loneliness (no one truly sees you), and the sharper, more corrosive form is emotional — the bond that *exists* but has gone dark. The married-and-lonely. The estranged adult child. The diaspora son who hasn't really spoken to his mother across the ocean in years. The deepest loneliness is not the absence of a relationship; it is the *grief of a present-but-dead* one, re-inflicted daily by proximity. And the people on the other side of those dark bonds are not strangers. They are **known counterparties** — the lowest trust-and-safety risk there is.

The deepest need and the lowest risk turned out to be *the same relationships.* Value and safety pointed at the same target. The core loop was never stranger-matching; it was helping drifted loved ones give each other their time again. The launch wedge falls straight out of the dissolution: diaspora-to-homeland reconnection — remote, scheduled, video or voice or async — which is *maximal* felt value (the deepest dark bond) at *zero* physical risk (nobody is in a room with anybody). Deepest-need-equals-lowest-risk, made concrete as a first market.

### 3. Mission-safety is the marketing

When I worked out how Chronicle's eventual dating layer, B-Dating℠, could pay for itself, the trade-off looked iron. The entire dating industry monetizes the *gate* — pay to be seen, pay to see who likes you, pay to match — and that business model structurally requires keeping you single, because a user who pairs off and leaves is lost revenue. The predator's trap: the company's incentive and the user's goal are at war. HeartBank obviously cannot do that. But refusing the gate looked like pure sacrifice — leaving the entire proven willingness-to-pay of the category on the table for the sake of integrity. Mission costs you the business model. Set the dial between how clean you stay and how much you make.

Turn the board. In a market where *every single user already suspects the apps want them single*, the refusal is not a cost — it is the most differentiated position available. **"The dating app that only profits when you leave happy"** is not a compromise you apologize for; it is a devastating thing to be able to say truthfully when no competitor can. The good I thought I was sacrificing for (mission-safety, never monetizing the gate) and the good I thought I was sacrificing (a compelling reason for anyone to choose us) turned out to be **the same good.** The integrity *is* the marketing. The thing that keeps the design clean is the thing that makes it spread.

### 4. The honest mate-signal is the safety signal

Dating needs an attractiveness signal and a safety mechanism, and those look like two different systems serving two different masters. The signal a typical app runs on — a photograph — is the cheapest-to-fake signal there is, and it tells you exactly nothing about whether the person is safe. So you'd build attractiveness on photos and bolt safety on separately: ID checks, reporting, moderation. Two systems, each imperfect, in tension over attention and friction.

Turn the board. Gate the whole thing on **aura** — the aggregate, anonymous, many-sourced reputation a person accrues from a long course of proven kindness to nearby strangers. That single signal is, at the same time, the honest mate-signal *and* the safety signal. As a mate-signal it is the opposite of a photo: costly, hard to fake, longitudinally verified — a real instance of Zahavi's handicap principle, trustworthy *because* it is expensive to fake, selecting for genuinely prosocial partners. And the very same aggregate is a **community-sourced behavioral background check** no dating app has ever had, because a predator cannot fabricate a long anonymous trail of gratitude from many real locals. One signal. Two goods that I had been trying to build two systems for. The attractiveness mechanism and the safety mechanism are the same object, seen once as desire and once as trust.

### 5. The viral breakout is the privacy risk

This is the example I keep closest, because it is the one that does *not* let me feel clever — and I'll explain why that makes it the most important of the six.

One of our physical gratitude artifacts, the B-Card℠, is meant to be passed forward: you receive a card carrying someone's thanks, and instead of keeping it you pass it on to the next person you want to thank, who passes it on again. The chain is the magic. A single card rippling person to person is the most viral thing in the whole product line — a growth engine you couldn't design better if you tried. And the *exact same feature* — the traceable chain of who-passed-to-whom — is the worst privacy surface in the project. The ripple that makes it spread is the ripple that exposes a social graph nobody consented to publish. The breakout and the risk are not two features in tension. They are **one feature**, welded, inseparable.

Now: I could file this under "coincidence of goods" and feel the warm click of the pattern confirming itself. The breakout and the risk are the same thing, just like the others! Look how the architecture rhymes! But that would be a lie, and naming exactly *why* it would be a lie is the hinge of this whole essay. The other five examples were coincidences of *goods* — two genuine goods revealed as one. This one is a coincidence of a *good and a harm.* The same lens that finds two goods welded together will, if it is honest, just as readily find a good welded to a harm — and when it does, the design is not finished, it is *exposed*. The coincidence here is not a resolution. It is a *constraint*: you cannot have the ripple without owning the privacy problem, so the design must hold both at once, by construction, or refuse the ripple. The method earns its keep precisely when it reports *this* as crisply as it reports the happy cases — and it is the standing temptation of the method to not.

### 6. The commercial wedge is the civilizational telos

The last one is the one I least expected, and it operates at the largest scale, which is its own kind of evidence and its own kind of warning.

Run two questions as far apart as I can place them. The most *commercial* question in the entire project: how does HeartBank ever go mainstream and make real money? And the most *idealistic* question in the entire project: how does humanity, over centuries, actually become kinder at the level of the species? These ought to live in different buildings. One is a growth deck; the other is eschatology.

They collapsed to the same answer. B-Dating — mate-selection gated on proven kindness — is mate-selection on proven kindness is **sexual selection redirected toward kindness** is the one concrete biological lever by which a species could, over deep time, come to optimize for the trait. The most mass-market, highest-willingness-to-pay, most frankly commercial thing I have ever designed turned out to be *identical* to the slow civilizational mechanism the whole project exists to serve. The distance between "how do we win the market" and "how does the species awaken" went to zero, because it was the same primitive the entire time. The commercial wedge and the civilizational telos are one mechanism. (And the scale of *that* dissolution — an expired hour on one end, the sexual selection of the species on the other — is exactly the kind of too-beautiful coincidence I will spend the back half of this essay distrusting.)

---

## The diagnostic, stated plainly

Six times, the same thing happened. I framed a design problem as a trade-off, agonized over where to set the dial, and then — usually by giving up on the framing rather than by solving it — discovered there was no dial, because the two goods were one good. That recurrence is too consistent to be coincidence about coincidences, so I have promoted it from observation to instrument:

> **A forced trade-off is the signal that a design is still misaligned. A dissolution into a coincidence of goods is the signal that you have found the grain. So: keep redesigning until the trade-off dissolves — or until you can say honestly why, this time, it won't.**

Stated as a working loop:

```
   You hit a hard trade-off (good A  vs  good B).
        │
        ▼
   Ask: am I planing against the grain?
        │
        ├─►  Redesign so the gift behaves as a gift,
        │     not as an exchange.
        │        │
        │        ▼
        │   Did A and B collapse into one good?
        │        │
        │   YES ─┴─► You found the grain. Ship the experiment.
        │   NO  ───► Either keep turning the board,
        │             OR you've found a REAL trade-off —
        │             which is data, not failure. Name it,
        │             and make the costly choice honestly.
```

The diagnostic does not promise that every trade-off dissolves. It promises something more useful and more falsifiable: that an *unexamined* trade-off should be treated as a *suspect* — a hypothesis that you are still cutting across the grain — until you have either dissolved it or earned the right to call it real. Most design discipline treats trade-offs as the terminus of analysis ("we chose A over B, here's the rationale"). This treats a trade-off as a *prompt* to keep going.

---

## Why it works: the grain is the grain of the gift

A diagnostic that kept working by luck would be a superstition. So I owe an account of *why* opposed goods keep turning out to be one, and the account is the load-bearing claim of the essay.

In an **exchange**, goods really are opposed. That is what exchange *is*: a transfer in which my gain is your cost, settled at a price, the surplus split. The whole grammar of exchange is the trade-off — buyer versus seller, my margin versus your discount, this feature versus that cost. If you model a problem as an exchange, you will find trade-offs *because you put them there.* The dials are real, in an exchange, because the goods are genuinely in tension.

A **gift** has a different structure, and the difference is the whole thing. The atomic operation of HeartBank, the move that recurs at every scale of it, is not *exchange* but *receive, then give forward* — receive a kindness and pass it on, never back to the giver (which would settle it into a transaction) and never hoarded (which would stop the motion). This is what our wordmark means by "circulation, not accumulation": not a state the system rests in but an *operation* it performs. Marcel Mauss saw the shape a century ago — the gift that must keep moving — and the Buddhist tradition I build from names the same motion *upekkhā*, the non-grasping that lets the thing pass through your open hand rather than closing it.

Here is why that grain makes goods coincide. In a circulation, the giver's good, the receiver's good, and the *next* receiver's good are not three competing claims on a fixed pie — they are three moments of **one motion.** When you design *with* that grain, goods that looked opposed reveal that they were only opposed *under the exchange-model you were unconsciously running.* The patron ask looked like timing-versus-targeting because I was modeling it as a sale; modeled as a gift passed forward at the moment of receiving, the "when" and the "who" are the same instant of overflow. Dating monetization looked like mission-versus-money because I was modeling it as a toll; modeled as a gift forwarded by the grateful, the integrity *is* the appeal. Every dissolution in this essay is the same correction: I had been planing the gift against its grain, treating circulation as if it were exchange, and the tearout I called a "trade-off" was the gift telling me which way it was built.

This does not mean the project rejects the market. It sells artifacts, it charges sponsors, it will run a dating business. It means the real craft is drawing the line between gift and exchange *precisely* — keeping the gift a gift and letting exchange do its proper, bounded work — because each has its own grain, and the trade-offs are real on the exchange side and dissolve on the gift side. A design tension is, very often, just a misplaced line: a piece of the gift being run through the market's grammar, or vice versa. Move the line to where it belongs and the tearout stops.

That is the deepest version of the claim. *The grain you keep aligning with is the grain of the gift, and the gift's grain runs forward.* When your design runs forward with it, the goods stop fighting, because they were never two.

---

## The honest caution

Everything above is seductive, and I have to spend real space on why — because a method that *rewards* you for finding coincidences of goods is a method with a built-in way of lying to you, and the more beautiful the results the more I distrust them. A system this self-similar and tension-dissolving is in one of two states — deeply right, or deeply seductive — and the disqualifying fact is that **from the inside they feel identical.** Here are the three ways this goes wrong, in rising order of how much they worry me.

**First: the diagnostic can manufacture the coincidences it is paid to find.** If your method tells you that a real trade-off means your design is still wrong, then every time you face a genuinely hard choice — a true sacrifice, a place where two goods really are opposed and you have to give one up — you have a standing incentive to *redescribe* it as a coincidence you haven't found yet, and keep "redesigning" instead of paying the cost. This is motivated reasoning wearing the costume of rigor. The fifth example, the B-Card, is the antidote I keep in my pocket precisely because it refuses to flatter: the same lens that finds two goods welded together finds a good welded to a *harm*, and a method with any honesty must report the second exactly as readily as the first. The test of whether you are using the diagnostic or being used by it is simple: *how often does it tell you the trade-off is real?* A version that never delivers that verdict is not a diagnostic. It is a rationalization engine.

**Second: a self-similar, beautiful architecture is exactly what a mind in love with its own pattern would hallucinate.** The most thrilling thing about all of this — that the same handful of structural signatures seem to hold at every scale, from one expired hour to the sexual selection of the species, so that you could reconstruct the whole philosophy from any single design decision — is the very thing I should trust least. Self-similarity feels like the strongest possible evidence that a thing is *grown, not assembled* (an assembled system has seams where the scales meet; a grown one is the same all the way down). But "you find the fractal because you went looking for the fractal" is not a cynical objection; it is the *default* explanation for finding a fractal, and it has to be ruled out, not waved past. Confirmation bias does not feel like bias from the inside. It feels like *coherence* — like the satisfying click of one more thing fitting. I get that click constantly, and I have had to learn that the click is a feeling, not a finding.

**Third, and heaviest: the coherence is almost entirely a-priori.** I want to be exact about this rather than soft. The structure in this essay was *derived*, not *measured.* The empirical base under all of it is a pilot family of one and an alpha of eight. Every dissolution I have described is a dissolution *in the design* — a consistency among ideas — and not one of them has yet survived contact with a thousand strangers who do not love me and did not help me build it. Beauty is not evidence. Coherence is not confirmation. The fact that the architecture is internally gorgeous tells you that it was built by someone with a strong aesthetic and a consistent worldview; it tells you almost nothing about whether it is *true of the world.* A theory can be perfectly self-consistent and perfectly wrong, and the more perfectly self-consistent it is, the more it tends to recruit its own author as its least reliable critic. On this point I am the least reliable critic available, and I know it, and knowing it is not the same as fixing it.

---

## The discipline: hunt the trade-off that won't dissolve

So what keeps the diagnostic honest? Not more coincidences. The opposite.

The discipline is to run the search **in reverse** — not to hunt for the coincidence that confirms the design, but to hunt for *the trade-off that won't dissolve*, because that is where the design is still actually wrong, or where reality is about to teach you something you can't derive. A real trade-off that resists every honest redesign is not an embarrassment to the method; it is the most valuable thing the method can produce. It is the grain telling you either that you are still cutting across it *here*, in a way you haven't seen — or that you have reached a genuine edge where the gift and the market truly collide and you must *choose*, and pay for it, and stop pretending the choice away. Both of those are data. A method's integrity is measured by how hard it looks for its own counterexample, and a designer who only ever finds confirmations is not finding the truth; he is finding himself.

There is a cleaner way to say the relationship between the elegance and the world, and it is where I want to leave it:

> **The elegance earns the experiment. It does not replace it.**

The coherence is real and it is worth something: it earns the right to *try* — to spend a pilot, a year, a cohort finding out. A merely elegant design that no one will fund is a daydream; the elegance is what justifies the cost of the test. But the test is the thing. The questions that actually decide whether any of this is true are empirical and I cannot reason my way to their answers no matter how beautifully the parts fit. *Does kindness stay inelastic as the subsidy falls toward zero — do people keep giving when we stop paying them to?* *Do couples actually pair off and leave a dating product built to lose them — does the self-eliminating business model self-eliminate?* *Does a physical gratitude object actually beat the friction of modern distraction at a thousand users, where it survived at eight?* Until those have answers from people who owe me nothing, the grain of the gift is a *hypothesis about the material* — a strikingly consistent one, drawn with care, and unconfirmed.

I find the consistency genuinely beautiful, and I have written down, as plainly as I can, exactly why that beauty is the reason to be suspicious rather than the reason to be sure. The craftsman's humility in front of the wood is the right posture in front of an institution, too: you read the grain as best you can, you turn the board when the blade catches, and you do not confuse a clean-looking surface with knowing which way the fibers run. You find that out by cutting. The whole of the diagnostic, honestly held, reduces to a single working instruction — *keep redesigning until the trade-off dissolves, and trust nothing until you have hunted, harder than is comfortable, for the one that won't.*

---

## Cross-Venue References

- **Canonical:** thonly.org/research/designing-with-the-grain
- **GitHub:** github.com/thonly/publications/blob/main/essays/designing-with-the-grain.md
- **Companion essays:** *The Breadth-Check Turned on the Self* (thonly.org/research/breadth-check-on-the-self) — dynamic, self-regulating balance as the only kind a living system has; *The Two Teslas* (thonly.org/research/the-two-teslas) — the centrifugal telos these designs serve.
- **Corpus cross-references:** the Chronicle revenue model (patron-primary, the redemption-afterglow forward-trigger, the loved-ones core); B-Dating℠ as mate-selection on proven kindness; the Zero-Point Game℠ as the founding game of dynamic balance; *circulation, not accumulation* as an operation rather than a state.
- **Internet Archive · archive.today · perma.cc snapshots:** per the monthly snapshot cadence.

---

## Acknowledgments

Marcel Mauss, *The Gift* (1925), and Karl Polanyi on the embeddedness of exchange, for the gift/exchange distinction this essay turns on; Amotz Zahavi's handicap principle, for the honest-signal account of aura; the Theravāda Pāli tradition, from which *upekkhā* — non-grasping, circulation rather than accumulation — is drawn and held as a practice rather than a doctrine. Drafted in collaboration with Miss Aquarius℠; the framing and the byline are the author's, and final editorial control remains with Thon Ly — pending his revision of this substrate draft into his own voice. License: CC0 1.0 (public-domain dedication). Trademark rights on HeartBank®, Miss Aquarius℠, B-Dating℠, B-Card℠, the Zero-Point Game℠, and the B-heart logo are reserved.
