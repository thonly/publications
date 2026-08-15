#!/bin/sh
#
# Store a Zenodo API token in the macOS Keychain, safely and verifiably.
#
#     ./scripts/store-token.sh                    # live  -> zenodo-token
#     ./scripts/store-token.sh zenodo-token-sandbox
#
# WHY THIS EXISTS RATHER THAN A ONE-LINER. Three one-liners were tried and all
# three failed, each silently:
#
#   read -rs TOKEN && security add-generic-password ... -w "$TOKEN"
#       -> zsh captured nothing; stored an empty string.
#   security add-generic-password ... -U -w        (prompting form)
#       -> prompted inconsistently; stored an empty string.
#   security add-generic-password ... -w "$(pbpaste)"
#       -> stored THE COMMAND ITSELF. Copying the command to the clipboard in
#          order to paste it into the terminal overwrites the token that was
#          supposed to be on the clipboard. The ordering trap is unavoidable
#          whenever the instruction is itself something you copy.
#
# Each failure produced a plausible-looking Keychain item and 403s everywhere,
# which reads like a scope problem rather than a storage problem. So this script
# VALIDATES before storing and VERIFIES the round-trip after.
#
# It also passes -A. Without it the item is created with an ACL that blocks
# non-interactive reads, and `security ... -w` then returns exit code 0 and an
# empty string — the worst failure mode of the set.

set -eu

SVC="${1:-zenodo-token}"

printf 'Paste the token for "%s" (input hidden), then press Enter:\n> ' "$SVC"
stty -echo 2>/dev/null || true
IFS= read -r TOKEN || true
stty echo 2>/dev/null || true
printf '\n'

# Strip stray whitespace a paste can carry.
TOKEN=$(printf '%s' "$TOKEN" | tr -d ' \t\r\n')
LEN=${#TOKEN}

if [ "$LEN" -lt 40 ]; then
    printf 'Refusing: got %s characters. A Zenodo token is ~60.\n' "$LEN" >&2
    exit 1
fi

# Reject the exact failure that happened: the command text, a URL, or a shell
# fragment landing in the field instead of a credential.
case "$TOKEN" in
    *security*|*pbpaste*|*http*|*' '*|*'$'*)
        printf 'Refusing: that looks like a command or URL, not a token.\n' >&2
        exit 1 ;;
esac

security add-generic-password -a "$USER" -s "$SVC" -A -U -w "$TOKEN"

# Verify the round-trip. Storing without checking is what made every previous
# attempt look successful while being broken.
GOT=$(security find-generic-password -s "$SVC" -w 2>/dev/null | tr -d '\n' || true)
if [ "$GOT" = "$TOKEN" ]; then
    printf '✅ stored and read back: %s (%s chars)\n' "$SVC" "$LEN"
else
    printf '❌ stored but read-back MISMATCH (got %s chars) — do not trust it.\n' \
        "${#GOT}" >&2
    exit 1
fi
