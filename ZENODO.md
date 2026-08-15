# Zenodo — DOIs for the corpus

Zenodo is a CERN-operated open repository. Depositing there gives each paper a
**DOI**: a persistent identifier held by a third-party institution, resolvable
after this site moves or stops, and present in the indexes academics search.

## What this is *not*

**It is not prior art, and it is not an upgrade to the prior-art strategy.** Prior
art needs public availability, which the public render at `thonly.org/research`
plus the Internet Archive / archive.today / perma.cc snapshots already supply. A
DOI adds reach and durability of *reference*, not of *date*. Dating is the job of
the two timestamp legs — see [`TIMESTAMPS.md`](./TIMESTAMPS.md).

It is deliberately the smallest of the three layers, and it is honest to say that
it partly duplicates work already done. It is here because the marginal cost is
near zero and the discoverability is real, not because the corpus needed it.

Note this sits differently from **arXiv**, which is deferred pending first-time
submitter endorsement, and **IP.com** at $395/paper, which is deferred as a worse
use of capital than the Cambodian trademark filings. Zenodo has no endorsement
gate and no fee, which is why it is the one that goes ahead.

## Two routes, and they compose

| | Unit | Effort | Use |
|---|---|---|---|
| **Per-paper** (`scripts/zenodo-deposit.py`) | one DOI per paper | one command | **the main route** — an examiner or citing author looks for *a paper* |
| **Repo-level** (`.zenodo.json` + GitHub releases) | one DOI per release | zero, once enabled | "cite the whole corpus"; a concept DOI that always resolves to the newest release |

They do not conflict. Cite the per-paper DOI when citing a paper.

---

## Setting it up — the steps only you can do

Both routes need an account, and the deposit script needs a token. **These require
your login and cannot be done for you.**

1. **Create the account.** <https://zenodo.org/signup/> — sign in *with GitHub* if
   you want the repo-level route too, since that authorises both at once.
2. **Personal access token** for the deposit script:
   <https://zenodo.org/account/settings/applications/tokens/new/> — scopes
   `deposit:write` and `deposit:actions`. Then:
   ```sh
   export ZENODO_TOKEN=...
   ```
   Do **not** commit it. It is not needed by CI; deposits are run by hand.
3. **Rehearse on the sandbox first.** The sandbox is a full copy of the API that
   mints fake DOIs, so mistakes cost nothing. It needs its *own* separate token
   from <https://sandbox.zenodo.org/account/settings/applications/tokens/new/>:
   ```sh
   ZENODO_TOKEN=<sandbox-token> ./scripts/zenodo-deposit.py --sandbox --create --publish --limit 2
   ```
   Check how the record looks, then delete the sandbox records and continue.
4. **Repo-level route, if you want it:** at <https://zenodo.org/account/settings/github/>
   flip the switch on `thonly/publications`, then cut a GitHub release. Zenodo
   archives that release and mints a DOI using `.zenodo.json`. **Only releases
   created *after* the switch is flipped are archived.**

## Scope — defensive publications first, essays as a separate pass

Decided 2026-08-15. The first deposit run covers **`defensive-publications` only**
(63 papers); the **31 essays are held back**, not excluded.

**The reason is the one-way door, not tidiness.** A DOI is irreversible,
third-party-hosted and un-deletable — the same property the corpus already
recognises for permanent media: *privacy defects go permanent at etch*. **8 of 31
essays reference identifiable family members and named individuals**, against
only incidental illustrative mentions in the defensive publications. That is not a
problem, but it is a set of decisions that deserves its own deliberate reading
rather than arriving as a side effect of a bulk run.

⚠️ **Holding is a SEQUENCING decision and must not harden into exclusion.** The
main benefit of this layer — a persistent address and third-party custody that
survive losing the domain — applies to the essays *at least as much*. They are the
more personally irreplaceable half; permanently excluding them would give the
least reproducible writing the weakest durability, which is backwards.

```sh
./scripts/zenodo-deposit.py --dir defensive-publications --create --publish
./scripts/zenodo-deposit.py --dir essays --create --publish        # the later pass
```

### The trigger for essays (founder, 2026-08-15): **on final draft, not on a date**

Essays deposit when they leave draft — *"essays when I publish (final drafts)."*
Currently 30 of 31 carry `status: draft`, so the essays pass waits on that field,
not on a calendar. Re-run the essays command whenever a batch reaches final.

### ⚠️ Why the defensive publications do NOT wait on the same trigger

All 63 also carry `status: draft`, which looks like an inconsistency and is not.
**The trigger differs because the function differs:**

- A **defensive publication is time-indexed** — its entire value is being on the
  record early. Withholding it until "final" inverts the thing it exists to do,
  and these have been publicly deployed and timestamped for months already.
- An **essay is not time-indexed.** Nothing is lost by polishing first, and the
  first indexed version is the one most cited — which is exactly why the corpus
  already defers arXiv and IP.com to publication-ready.

Revision is handled either way: a changed paper deposits as a **new version**, and
the concept DOI always resolves to the newest text. Depositing a draft is
therefore not a commitment to that wording — only to the record existing.

## Running it for real

```sh
./scripts/zenodo-deposit.py                     # dry run — prints, sends nothing
./scripts/zenodo-deposit.py --create            # real DRAFTS (deletable)
./scripts/zenodo-deposit.py --create --publish  # mints real DOIs
./scripts/zenodo-deposit.py --only <slug>       # one paper
```

⚠️ **Publishing is irreversible.** A published Zenodo record cannot be deleted,
only superseded by a new version. That is the property that makes a DOI worth
having, and it is also why the script defaults to a dry run, why `--publish`
refuses to work without `--create`, and why the sandbox exists. Start with
`--limit 2`.

## Revisions

State is kept in `zenodo-dois.json` — slug → `{deposition_id, doi, concept_doi,
sha256}`. On each run the script re-hashes every paper:

- **unchanged SHA-256** → skipped entirely.
- **changed SHA-256** → deposited as a **new version** of the existing record, not
  as a new record. The concept DOI keeps resolving to the newest text while every
  earlier text keeps its own version DOI.

This mirrors the `.r<N>.ots` rotation convention in `TIMESTAMPS.md`: the current
text and every superseded text each stay separately citable.

## Metadata

Generated from each paper's own frontmatter, so the DOI record cannot drift from
the paper. `title`, `subtitle`, `authors`, `date`, `category`, `priority` and the
`**Keywords:**` line all map through; the abstract becomes the description; the
license is fixed to CC0.

Three deliberate choices worth knowing about:

- **The author name is deposited as `Ly, Thon`, not `Thon Ly`,** with ORCID
  **[0009-0009-4503-8575](https://orcid.org/0009-0009-4503-8575)**. DataCite and
  every reference manager expect "Family, Given"; handed the display form they
  have to guess which half is the surname, and across 96 records they guess wrong
  often enough to matter. The papers themselves are untouched — this is a
  citation-metadata form, not a change to the corpus.
- **Miss Aquarius is listed as a creator, and deliberately has no ORCID.** The
  standing rule is that the AI collaboration is disclosed openly, under the same
  name, at every venue — dropping her to look conventional would break the
  consistency that makes the disclosure meaningful. But ORCID identifies *human
  researchers* and carries an assertion about a person; claiming one for an AI
  co-author would misstate what the identifier certifies. **This is a permanent
  asymmetry, not a gap to close later.**
- **Every record carries the document's SHA-256** and states that it is Bitcoin-
  and RFC 3161-attested. The DOI record therefore points at the evidence rather
  than asking to be taken on trust — which is the whole reason the three layers
  exist together.

## Status

⚠️ **The API path is written and dry-run tested against all 96 papers, but has
never been executed against Zenodo** — that needs a token. Rehearse on
`--sandbox` before the first real run, and treat the first two records as the
real test.
