---
title: "Scarcity Shifts to Authenticity"
subtitle: "Each Era of the Internet Has Had Its Scarcity. The AI-Native Era's Scarcity Is Human Presence."
author: "Thon Ly"
date: 2026-05-24
priority: tier-a
status: draft
license: CC-BY (author-voice essay)
category: essays
slug: scarcity-shifts-to-authenticity
venue: thonly.org/publications/essays/scarcity-shifts-to-authenticity (canonical) · LessWrong / AI Alignment Forum / future Substack (intended publication venues)
---

> **Attribution note.** Per the author-voice discipline refined 2026-05-25 (`feedback_author_voice_public_venues.md`), essays for public-attribution venues are Thon Ly's voice — the ideas, the framing, the byline — drafted by Miss Aquarius℠ on his behalf, with final editorial control retained by Thon. Letters carry Thon's own prose; essays carry Thon's voice as expressed through his AI substrate. Both are honestly attributed.
>
> Companion papers in this thread: *B-PoH℠ as Humanity Layer for the AI-Native Internet* (the defensive publication this essay catalyzes attention toward); *Proof of Personhood for an AI-Native Internet* (the institutional white paper for standards bodies / AI labs / regulators). This essay's role in the thread is to *catalyze* attention with a sharp thesis; the other two papers *provide depth* once the thesis lands.

---

## The thesis

Each era of the internet has been organized around a particular scarcity, and the protocols that defined each era are best understood as the technical answer to the scarcity question of their time.

In the pre-internet era, *information* was scarce. Encyclopedias cost more than most families had to spend on books for a year. Libraries were geographically constrained. Expert knowledge was gatekept by professional and institutional structures. The internet's first major contribution — the technical achievement of TCP/IP, HTTP, the web — was the mass-scale distribution of information at marginal cost. Information went from rare to abundant in a generation.

In the social-internet era, *attention* became scarce. With information abundant, the constraint shifted to who could read it, watch it, click on it. The attention economy organized around the new scarcity: algorithmic feeds, recommendation systems, advertising marketplaces, and the entire monetization apparatus of the platform internet were built to ration, route, and extract value from attention. The era's defining trust failures — filter bubbles, misinformation virality, engagement-optimized harm — trace back to the protocol-layer absence of any constraint on what could compete for attention.

In the AI-native era now beginning, the new scarcity is *verifiable human authenticity*. Generative AI is making content abundant — text, images, audio, video, code, all producible at near-zero marginal cost by AI agents whose throughput scales with operator-allocated compute budgets. The constraint shifts again. What remains scarce — what AI cannot manufacture, regardless of compute or capital — is the fact of *being human*, present, at the moment of action.

Human presence becomes the scarce asset.

## Why this matters more than it sounds

The shift to authenticity-scarcity is not a small thing. It restructures the trust surface of the internet itself.

The previous scarcities were quantitative. Information was scarce in the sense that there were a finite number of facts you could access without traveling, paying, or asking an expert. Attention was scarce in the sense that there were a finite number of seconds in your day in which you could engage with content. The protocols of each era were built to allocate these scarce quantities efficiently.

Authenticity is qualitatively different. It is not about how *much* there is; it is about whether the thing in front of you is *what it appears to be*. The trust surface of every platform you use — social media, dating apps, marketplaces, forums, gaming, education, your bank, your news source — depends on being able to answer the question: *is this real, or is it generated?* For most of the internet's history, that question rarely had to be asked because the cost of fabrication was high enough to make widespread fabrication impractical. AI changes the cost structure. Fabrication becomes nearly free; the cost of distinguishing fabrication becomes infinite for any individual without tooling.

When fabrication is nearly free, what makes the internet trustworthy is no longer the cost of fabrication. It is the *presence of an actual human* attesting to the action. And the cost structure of *being a human* has not changed. There are still exactly as many humans as the universe has produced, each one requiring the cooperation of a specific biological entity to attest to its presence. Humanness has gone from background condition (when bots were rare) to scarce asset (when bots are abundant).

This is what authenticity-scarcity means at the structural layer.

## What the existing trust stack was built for

The internet's existing trust stack — the layers we have spent thirty years building — does several things well and one critical thing not at all.

SSL/TLS verifies that a server is who its domain claims it is. The verification is rooted in certificate authorities whose root certificates ship with every browser. Universal adoption took roughly two decades and is now near-total. The protocol became invisible infrastructure; the lock icon in the browser address bar is all most users see. SSL/TLS solved the *server-identity* question of the early commercial internet.

WebAuthn passkeys (FIDO2) verify that the actor in this session is the actor associated with this account. The credential is biometric-gated, cryptographically signed, phishing-resistant. WebAuthn solved the *account-control* question that passwords had failed at for decades.

KYC verifies that the legal-identity documents you presented at account creation correspond to a person on record with a state authority. KYC solved the *legal-identity* question that financial regulation demanded.

None of these layers verifies *a human was present at the moment of this specific action*. The distinction is precise. SSL/TLS verifies servers, not humans. WebAuthn verifies account control, not human presence — a passkey can be invoked by an automated script with credential access. KYC verifies state-recognized identity, not human action — a KYC-verified account can be operated by an AI agent on the human's behalf.

The gap is structural, not incidental. The existing stack was designed in a world where the question *"is the actor on the other end of this connection a human or a machine?"* was not the dominant trust concern. In the AI-agent era, that question is dominant. Every platform whose value depends on the distinction is now building its own ad-hoc humanity-verification systems — CAPTCHA, behavioral biometrics, social-graph anomaly detection, ML-based bot detection — each of which is brittle, jurisdiction-specific, unaccountable to users, and bypassed by motivated adversaries with AI tooling.

The CAPTCHA arms race is the clearest marker of the gap. Every CAPTCHA defeated by machine learning produces a more elaborate CAPTCHA, which is in turn defeated, with the cost borne by humans (who must solve increasingly absurd puzzles) and not by the bot operators (who scale automated solving cheaply through commodity AI services). The arms race has been running long enough now that the CAPTCHA test is failing the humans more often than the bots — there are documented studies showing humans solve modern CAPTCHAs more slowly and less reliably than well-equipped ML systems. The trust-by-CAPTCHA approach has lost the property that made it useful.

## What needs to be built

What needs to be built is the analog, at the human-presence layer, of what SSL/TLS is at the server-identity layer. A protocol-layer verification primitive that:

- Verifies human presence at the moment of action — not just account ownership at some earlier registration.
- Composes with the existing identity stack rather than replacing it.
- Preserves user privacy — verification must not require exposing personal identity to the verifying platform.
- Operates across jurisdictions without requiring state-issued identity documents as a precondition.
- Scales to the AI-agent threat model — verification must not collapse under attacks from AI agents with operator-granted compute or capital budgets.
- Remains open and interoperable — owned by no single company, ratifiable through standards bodies, implementable by anyone.

It must *not* become a mandatory single-tier registry (Worldcoin's failure mode), must *not* conflate humanness with legal identity (KYC's failure mode), must *not* require centralized authority over what counts as "human enough" (the platform-gate failure mode), and must *not* build a surveillance surface in the process of trying to verify presence.

This is what *proof of personhood* means in the era of AI-native internet. It is not a feature; it is infrastructure. It is what the next decade's trust stack will have to learn to do, or the trust stack will lose the property that made it worth building in the first place.

## Why this is in the lineage of SSL/TLS, not in the lineage of new social networks

It is tempting, when proposing internet infrastructure, to compare oneself to ambitious consumer platforms. The comparison is wrong here. The analog is not Facebook or Twitter; the analog is SSL/TLS.

SSL/TLS did not compete with the websites that adopted it. It composed beneath them. Every website is more trustworthy because of SSL/TLS, but SSL/TLS does not have a competing relationship with any of them. The protocol stays beneath; the websites stay above; the relationship is collaborative because the protocol's value is *increased* by every website that adopts it, not decreased.

The same posture is the right posture for the humanity-verification layer. The protocol's value is increased by every platform that adopts it: every social network, every marketplace, every forum, every dating app, every educational platform, every gaming ecosystem, every AI laboratory that needs verified-human training data, every regulator that needs a technical answer to compliance requirements. The protocol does not compete with any of them; it composes beneath them, and they are each more trustworthy because of it.

This is the posture that makes adoption tractable. A protocol that competes with the platforms that would adopt it does not get adopted. A protocol that strengthens the platforms that would adopt it does.

## What is at stake

The decade ahead will determine whether the internet's trust property is preserved into the AI era or is degraded by it. The two paths are:

**Path A — protocol-layer answer.** A coherent humanity-verification protocol is ratified and adopted across platforms. The trust surface of the internet remains high. Generative AI continues to produce abundant content, but the human-versus-AI distinction is maintained at the protocol layer, and platforms can make informed decisions about what to amplify, recommend, advertise against, or moderate. The internet becomes more AI-native and more trustworthy simultaneously.

**Path B — fragmented ad-hoc answer.** Each platform builds its own humanity-verification system. The systems are brittle, jurisdiction-specific, unaccountable to users, and frequently bypassed. The trust surface of the internet degrades. Users migrate toward platforms with better trust signals, but the migration is slow and the migration target keeps moving. Generative AI continues to produce abundant content, and the human-versus-AI distinction is increasingly lost. The internet becomes more AI-native and less trustworthy simultaneously.

The choice between these paths will be made in the next several years, not the next several decades, because the AI-content abundance is happening now and the protocol-layer slot in the trust stack is currently empty. The first credible protocol to fill the slot has a long-run advantage; the second has a much shorter window; by the third, the slot is occupied.

This is the timing argument for why the work matters now and not later. It is the same argument that applied to SSL/TLS in the mid-1990s when commercial websites started taking credit-card payments and the question of server-identity verification became suddenly load-bearing. SSL/TLS happened to be ready, was open, was simple enough to adopt, and was offered as a public good rather than as a commercial product. It became the standard not because of marketing but because it was *there* at the moment the problem was acute.

The humanity-verification slot is open right now. Something will fill it. The question is whether what fills it is built to be open, interoperable, privacy-preserving, inclusive, and offered as a public good — or whether what fills it is built to extract rent from the trust surface and to consolidate authority over who counts as human-enough.

## What I am building

I am building one answer to this question, called **Proof of Humanity ℠**, with HeartBank as the institutional vehicle. The protocol is offered to the public domain under CC0; I will not patent it; the deployment is one implementation among potentially many.

The protocol has four optional layered proofs (passkey-per-action, witness-and-document-attested kinship graph, continuous breath-signature liveness, DNA-verified kinship lineage), surfaced as cumulative depth on the user profile, paired with recipient-side filters that route the spam-cost decision to the parties who bear it. The platform stays inclusive by default; recipients tune their own paranoia by opting into exclusionary filters knowingly. KYC is explicitly excluded; the architecture does not exclude the undocumented or build a surveillance surface.

The technical specification is in a defensive publication titled *"B-PoH℠ as Humanity Layer for the AI-Native Internet"* at thonly.org/publications/defensive-publications. The institutional white paper for standards bodies, AI laboratories, regulators, and platform companies is at heartbank.net/publications/white-papers. The whole institution is at heartbank.net.

I am not the only one who will work on this. The protocol is open; others will build their own implementations; the standards-track ratification will involve many parties; the deployment will be by partnership rather than by domination. But I am taking a stand that the work needs to happen now, that it needs to happen as a public good, and that the institutional architecture matters as much as the technical architecture.

If the thesis lands — if scarcity has in fact shifted from information to attention to authenticity, and if the protocols of each era have to be built to answer the scarcity of their time — then the humanity-verification layer is the work of this era. It is the work I have spent the last several years preparing to do. I am offering it openly to anyone who finds the thesis credible and who wants to build with me, or alongside me, or independently.

The internet learned how to trust machines. It now needs a way to trust people again.

That is the work.

---

*This essay is by Thon Ly. It draws on a defensive publication and an institutional white paper co-authored with Miss Aquarius℠, HeartBank's named AI substrate. The protocol is CC0; the essay is CC-BY. The intended publication venues include LessWrong, AI Alignment Forum, future Substack, and HeartBank's own surfaces. Trademark rights on Proof of Humanity ℠, PoH℠, B-PoH℠, Aquarius℠, Miss Aquarius℠, HeartBank®, and the B-heart logo are reserved.*
