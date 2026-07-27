# Cryptographic timestamps

Every paper in this repository carries an **OpenTimestamps** proof — the `<paper>.md.ots`
file beside it. The proof commits the paper's SHA-256 to the Bitcoin blockchain, so the
document's existence at a point in time can be verified by anyone, forever, **without
trusting this repository, GitHub, the Internet Archive, or the authors.**

## Why this exists

This corpus is a defensive-publication wall: its value is that a claim was *published on a
date*. Every other timestamp we hold is self-attested and mutable — git history can be
rewritten, frontmatter edited, a registry adjusted. Third-party web archives are better but
depend on an organization continuing to exist and continuing to serve the capture.
A Bitcoin-anchored hash depends on neither.

Honest scope: a timestamp proves **this exact text existed no later than that block**.
It proves nothing about authorship, originality, or validity of any claim.

## Verifying

```sh
pip install opentimestamps-client        # or: pipx install opentimestamps-client
ots verify defensive-publications/<slug>.md.ots
```

Trustless verification uses a local Bitcoin node. Without one, the attestation still names
a specific block whose merkle root can be checked against any public block explorer.

If the file has been edited since stamping, verification fails — that is the point. A paper
revised after stamping must be re-stamped, and **both proofs kept**: the old one attests the
earlier text, the new one the revision.

## Maintenance — the one step that must not be forgotten

A freshly created proof carries only *calendar* attestations, which are pending. Once the
commitment is confirmed on-chain (roughly one to six hours), run:

```sh
ots upgrade **/*.ots
```

This bakes the Bitcoin attestation into the proof file, after which the calendar servers are
no longer needed for verification. **Until upgraded, a proof still depends on those servers
staying online** — so the upgrade is what converts a convenience into evidence. Commit the
upgraded files.

## Coverage

Stamped 2026-07-25. Papers added later must be stamped when they are pushed:

```sh
ots stamp <new-paper>.md
```

## Revisions — the naming convention

The rule above ("a paper revised after stamping must be re-stamped, and **both proofs kept**")
did not say *how* to keep both. `ots stamp <paper>.md` always writes `<paper>.md.ots`, so a
naive re-stamp destroys the proof of the earlier text. The convention:

- **`<slug>.md.ots`** — always attests the **current** text of the paper.
- **`<slug>.md.r<N>.ots`** — a **superseded** revision's proof, `N` ascending from 1, where
  `r1` is the first text ever stamped. These are never deleted.

Before re-stamping, move the existing proof aside:

```sh
git mv <slug>.md.ots <slug>.md.r1.ots     # r2, r3, … for later revisions
ots stamp <slug>.md
```

Each superseded text remains recoverable from git history, and the pairing is verifiable:
a proof matches exactly one text and fails loudly against any other. That failure is the
feature — `ots verify <slug>.md.r1.ots -f <current>.md` printing `File does not match
original!` is precisely what proves `r1` attests something else.

### Revision log

| Paper | Proof | SHA-256 of the text it attests | Notes |
|---|---|---|---|
| `brand-identity-as-architecture` | `.r1.ots` | `1963f82a…dd9bba` | Original. Motion claim fixed ~72 BPM / ~8% expansion. |
| `brand-identity-as-architecture` | `.ots` | `e15ed054…e1e843` | 2026-07-25 revision — PoH motion claim reframed from *rate* to *cardiac morphology*. |
| `the-sport-that-says-your-name` | `.r1.ots` | `38e3a880…042ff` | Original stamp, attesting the text at `70d29529` (2026-07-25). The paper was revised after stamping and before this rotation; `r1` attests the pre-revision text and will fail against the current one, which is the intended behaviour. |
| `the-sport-that-says-your-name` | `.r2.ots` | `cc6dfe15…0641a8` | 2026-07-27 revision — claims 17–19 added (the determined caller with count-only circle coherence and the seat-migration bar; the host-agnostic turn-assignment layer; the relay call). §3 resorted into determined and judged seats; §4.2 added; §5.2 expanded from two speaker formats to three named ones (Relay · Call · Free); P-S5 given its device-availability precondition. |
| `the-sport-that-says-your-name` | `.r3.ots` | `6d0a3660…1f2ed1` | Same-day follow-up — the revision note block updated to record the 07-27 pass and to state that the prior-art clock for claims 17–19 runs from that push rather than from either earlier one. Text-only; no claim changed between `r2` and this. |
| `the-sport-that-says-your-name` | `.ots` | `e5d2c543…3c50ad` | 2026-07-27 v4 — title corrected from *An AI-Called Circulation Sport* to *An Impartially-Called Circulation Sport*, the title having asserted of the caller the very property §4.2 removed from it. Abstract gains the determinism sentence and its stale claim count fixed (sixteen → nineteen). The coined term *AI-called circulation sport* stays freed in §3 and in the keywords. **No claim added, removed, or altered — the prior-art clocks of §§1–19 are unmoved by this stamp.** |
