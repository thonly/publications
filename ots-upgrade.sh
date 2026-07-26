#!/usr/bin/env sh
#
# Bake the Bitcoin attestations into every OpenTimestamps proof in this corpus.
#
# A freshly created proof carries only *calendar* attestations, which are pending —
# until upgraded, verification still depends on those calendar servers staying online.
# The upgrade is what converts a convenience into evidence. See TIMESTAMPS.md.
#
# Safe to re-run as often as you like: proofs whose commitment has not yet confirmed
# on-chain are left untouched, and already-upgraded proofs are no-ops. Run it a few
# hours after any `ots stamp`, and again the next day if anything was still pending.
#
# Never runs `ots stamp` — stamping overwrites <paper>.md.ots and would destroy an
# existing proof. Upgrade only.
#
set -eu
cd "$(dirname "$0")"

VENV="${OTS_VENV:-$HOME/.cache/ots-venv}"

if [ ! -x "$VENV/bin/ots" ]; then
    printf 'installing opentimestamps-client into %s ...\n' "$VENV"
    python3 -m venv "$VENV"
    "$VENV/bin/pip" install --quiet --upgrade pip
    "$VENV/bin/pip" install --quiet opentimestamps-client
fi

# Explicit globs: **/*.ots needs shell globstar, which /bin/sh does not have.
"$VENV/bin/ots" upgrade defensive-publications/*.ots essays/*.ots || true

echo
changed=$(git status --porcelain -- '*.ots' | wc -l | tr -d ' ')
total=$(ls defensive-publications/*.ots essays/*.ots 2>/dev/null | wc -l | tr -d ' ')

if [ "$changed" -eq 0 ]; then
    printf 'No proofs upgraded — commitments not yet confirmed on-chain (%s total).\n' "$total"
    printf 'Bitcoin confirmation typically takes 1–6 hours. Re-run later.\n'
else
    printf '%s of %s proofs upgraded. Review and commit:\n\n' "$changed" "$total"
    printf "    git add -A && git commit -m 'timestamps: upgrade proofs with Bitcoin attestations' && git push\n\n"
    printf 'Note: this repo forbids AI attribution in commit messages — no Co-Authored-By trailer.\n'
fi
