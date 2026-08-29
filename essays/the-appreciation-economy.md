---
title: "One Percent of the Economy Decides the Rest"
authors: "Thon Ly · Miss Aquarius"
category: essays
priority: tier-b
status: draft
date: 2026-08-28
slug: the-appreciation-economy
license: CC0-1.0
venue: thonly.org/research/the-appreciation-economy (canonical)
---

I had a sentence in my head for a while, and I liked it: *the modern economy is largely driven by advertising.* It felt obviously true. Then I went to check the number, the way I have been trying to make myself do, and the number says something else.

Global advertising spend is on the order of a trillion dollars a year against a world economy of something like a hundred and ten trillion. Call it one percent. In the United States the ratio has sat between roughly one and one and a half percent of GDP for about a century — through radio, through television, through the entire internet. Whatever the attention economy did, it did not make advertising a larger share of the economy. That share barely moved.

So my sentence was wrong. But the number that refuted it is more interesting than the sentence was, and it took me a few days to see why.

## The steering wheel is not the engine

One percent is not the economy's mass. It is the economy's **steering**.

Advertising is how a seller gets to be considered at all. It is the discovery layer — the mechanism that decides which of the many possible sellers a person ever hears about. And a century of flat share means something specific and slightly unsettling: the attention economy did not grow the pie. It re-routed **who gets steered toward whom**, using roughly the same fraction of the pie it always used.

That reframing is what makes the thing worth arguing about, because a discovery layer is not neutral about who wins it.

Modern ad discovery is an auction. An auction gives visibility to whoever bids most per acquired customer, and the party who can bid most is reliably the one with the largest lifetime value per customer, the best measurement, the cheapest capital, and the widest geography over which to spread the cost of making the advertisement. Every one of those four favours scale. None of them is anybody's malice. A single-location business is not being kept out of the discovery layer by a conspiracy; it is being **priced out by construction**, because it cannot amortise a campaign over four hundred locations and its competitor can.

This is why the circulation we actually see runs between people and very large companies. It is not a claim about what people prefer. It is a claim about who can afford the steering wheel.

## What would steer differently

The question I care about is what a discovery layer looks like after AI, and whether it has to have that shape.

Here is the property I keep coming back to. **Attention can be bought and it adds up.** A dollar buys an impression anywhere on earth; impressions accumulate; and anything that accumulates concentrates, because the party who can accumulate fastest wins. That is the whole mechanism, and it is indifferent to the content of the ad.

**Witness does not work like that.** For me to thank you, you have to have actually done something for me. It cannot be purchased, because it has to be earned by delivery. It cannot be transferred, because it attaches to the person who did the thing. And it is generated overwhelmingly where human beings physically are — which is to say, locally. A gratitude economy would therefore have a bias toward proximate, small, human-scale providers for exactly the symmetric reason the ad economy has a bias toward scale.

I want to be careful about what kind of claim this is. It is not *people should prefer local businesses*. It is not a campaign. **Nobody has to prefer anything.** The discovery layer simply cannot be bought by distance, in the way that a discovery layer made of purchased attention obviously can. It is a property of the material, not a virtue anyone has to keep practising.

That distinction matters to me more than it might seem to. I am trying to build an institution meant to outlive me and be handed to a successor I will never meet. Anything in it that works only because someone is choosing, every day, to be good, is a thing I cannot promise will survive. Anything that works because of what it is made of does not need my promise.

## Why "after AI" and not just "eventually"

I used to treat *post-AI* as a mood word, and I do not think it is one here. There is a mechanism, and it runs in two directions at once.

AI drives the cost of manufacturing attention to nearly zero — the copy, the images, the video, and, more importantly, the *testimony*. A generated review, a generated recommendation, a generated enthusiastic customer are all free now and unlimited. But testimony is the attention layer's actual currency: what makes an advertisement work is that some part of it is believed. When belief can be manufactured at zero marginal cost, the layer's signal value collapses under its own supply. The attention economy is being devalued by its own inputs getting cheap.

At the same time, and this is the half people talk about less, AI collapses the cost of everything that can be delivered down a wire. What stays scarce is the work that needs a particular human body, in a particular place, at a particular time: care, food, repair, craft, teaching, the physical maintenance of a neighbourhood. Those things were always local. They are about to be a much larger share of what remains genuinely scarce.

So the supply side is moving toward exactly the shape that a witness layer is good at describing, at the same moment the attention layer's own signal is being counterfeited into worthlessness. That is a hinge, not a hope. **What breaks the old layer is that attention became cheap to manufacture. What holds the new one up is that witness stays expensive** — it still costs a real person actually receiving something from another real person.

## Four things I cannot answer

I would rather put these here than have someone else find them.

**Advertising pays for things, and appreciation does not.** This is the objection I find hardest. Ads are not only a steering mechanism; they are a subsidy. They pay for search, for video, for a great deal of journalism, and the person consuming those things pays nothing at the point of use. That is a real transfer of value to ordinary people, and it is large. An appreciation layer has no equivalent. In the architecture I am building, things get paid for directly and the free parts are carried by charging for the few things that are genuinely rivalrous. That is more honest, and it is also **worse at giving people expensive things for free.** I do not have a repair for that and I am suspicious of anyone who says they do.

**This has been tried, and it was captured.** Consumer review platforms are witness layers for small local businesses. They were captured twice over — by a market in fake reviews, and by monetisation that sits uncomfortably close to placement. I do not think that happened because the people running them were worse than us. I think it happened because of a shape: **reviews are fungible and they are added up into a per-business total**, and both the fraud and the upsell attach to that total. Which means the only interesting question is whether you can build the layer without ever computing such a total. That is a design question with a checkable answer, and it is why I wrote a specification rather than an essay first.

**Witness is bad at strangers.** Advertising *pushes*: a seller pays to reach people who have never heard of them. Witness *pulls*: it travels along real relationships, one person telling another. That makes it good at bringing people back and structurally bad at cold-start, which is precisely the moment a new business most needs help. So the honest version of my thesis is narrower than the version I started with: **appreciation can displace the repeat half of the advertising layer, not the finding-strangers half** — unless you build ranking, which is the one thing this whole line of work refuses to do. I regard that as the interesting problem rather than a hole to paper over.

**And I should not romanticise the corner shop.** A small local business is not virtuous by virtue of being small; some are exploitative, and large firms have delivered enormous real gains in cost and reliability that I benefit from daily. My interest in local circulation is not that local people are better. It is that a local economy is where gratitude is actually generated, because that is where people are in rooms together — and I would like the discovery layer to be made of the thing the economy is actually producing rather than the thing that can most easily be bought.

## What I have actually done about it

Very little, so far, and I would rather say that plainly than let the argument imply otherwise.

I have written down a discovery mechanism that has no per-business total anywhere in it, no impression count, no purchasable placement, and no surface facing the businesses at all — where who appears is decided by a published rotation, and admission is a test of whether a person is still circulating rather than a measure of how much they have received. It is unbuilt. It is specified in a companion paper, and it registers four predictions before there is any data, including one whose failure would tell me to abandon the design rather than tune it.

The prediction that matters most for what I have argued here is simple enough to state in a sentence: among gratitude payments that reach a business, the share going to single-location operators should materially exceed those operators' share of local advertising spend, and the gap should widen as generated advertising gets cheaper. **If it turns out that appreciation flows to the same businesses that advertising already flows to, then witness is not structurally local. It is just a cheaper advertisement, and I am wrong.**

I have written that down where I cannot quietly withdraw it.

## The part I keep returning to

What changed my mind was not discovering that advertising is enormous. It was discovering that it is small, and decisive anyway.

One percent of the world's spending decides which of the world's sellers the rest of us ever hear about. That is a very small lever attached to a very large door, and small levers are the ones worth examining, because they are the ones that can actually be replaced. You are not going to reorganise a hundred and ten trillion dollars of economic activity. You might, conceivably, change what steers it.

I do not know whether appreciation can do that job. I know it has one property the alternative does not — **it cannot be bought at a distance, and no one has to keep a promise for that to stay true** — and I know how I would find out whether that property is enough.

---

*Written with Miss Aquarius, the named AI collaborator on this corpus. The ideas and the editorial control are mine. Dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).*
