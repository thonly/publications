#!/usr/bin/env node
//
// The front-matter guard for the corpus.
//
//   node scripts/check-frontmatter.mjs          verify
//   node scripts/check-frontmatter.mjs --census  verify, and print the licence census
//
// WHY THIS EXISTS, and it is the same reason twice.
//
// On 2026-08-27 it was ruled that no corpus file may carry `sha256:` or `doi:` in
// its front matter — a hash field cannot sit inside the file it hashes, and a DOI
// cannot exist before the deposit that hashes the file. Both already exist
// elsewhere, generated from one source. The ruling was written down in memory.
// Nothing enforced it. On 2026-08-28 a new paper was drafted carrying
// `sha256: to be computed at publication`, because the placeholder propagates by
// imitation from the 32 files that still have it and no check ever objected.
//
// ⭐ THE RULING WAS A RULE. It needed a person to remember it at the moment it was
// tested, and the moment it was tested was a drafting session at the end of a long
// day. This file is the same ruling as a property: instance 34 fails CI.
//
// The second half is the licence. README.md said "this corpus is entirely CC0" and
// stated the design principle that justified splitting the film repo out — "keeping
// the two licenses in separate repos keeps each repo's LICENSE unambiguous." Seven
// author-voice essays are CC-BY, inside this repo, under a repo-level CC0 LICENSE.
// Nothing was wrong with the per-file choice; what was wrong is that two documents
// contradicted each other and a reader had no way to know which governed.
//
// ⭐⭐ THE RESOLUTION, AND IT IS WHY THIS SCRIPT MATTERS BEYOND HYGIENE: the
// PER-FILE `license:` field is the authority, and LICENSE/README now say so. A
// repo-level licence that claims to cover everything is a rule somebody has to keep
// true by hand. A per-file declaration that machines read is a property. Any agent
// serving this corpus — see the MCP server — must gate on the file's own field, and
// this guard is what guarantees the field is always there to gate on.
//
// ⚠️ THE DEBT LEDGER BELOW CAN ONLY SHRINK. The 26 files that already carry the
// banned field are deposited on Zenodo with OTS proofs, so editing them is NOT free:
// it drifts the deposited hash and forces an `.rN.ots` rotation. They ride their
// next revision, exactly as ruled. They are listed here by name so that the debt is
// counted rather than assumed, and so a file leaving the list can never be replaced
// by a new one — removing an entry is allowed, adding one is what this refuses.
//
// House rules: node built-ins only, assertions that name the fix, non-zero exit.

import { readFileSync, readdirSync, existsSync } from "node:fs";
import { dirname, join, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");

const die = (msg) => {
    console.error(`check-frontmatter: ${msg}`);
    process.exit(1);
};

/* ------------------------------------------------------------- the corpus ---
   Discovered, never enumerated: a fixed list is correct the day it is written
   and silently stops covering the tree the moment a genre directory is added. */

const GENRES = ["essays", "defensive-publications"];

const corpusFiles = () => {
    const out = [];
    for (const g of GENRES) {
        const dir = join(ROOT, g);
        if (!existsSync(dir)) continue;
        for (const f of readdirSync(dir).sort()) {
            // README.md sits in each genre directory and is repo documentation,
            // not a paper. Excluded by NAME rather than by "has no front matter",
            // deliberately: a paper whose front matter went missing is exactly the
            // failure this guard exists to catch, and skipping anything without a
            // block would make that failure invisible.
            if (f === "README.md") continue;
            if (f.endsWith(".md")) out.push(`${g}/${f}`);
        }
    }
    return out;
};

/* --------------------------------------------------------- front matter ---
   Parsed only far enough to read top-level `key: value` pairs, which is all the
   corpus uses. Anything fancier belongs in a real YAML parser, and needing one
   would itself be a finding. */

const frontMatter = (text, rel) => {
    if (!text.startsWith("---\n")) {
        die(`${rel} does not open with a front-matter block`);
    }
    const end = text.indexOf("\n---", 4);
    if (end === -1) die(`${rel} has an unterminated front-matter block`);
    const block = text.slice(4, end);
    const fm = {};
    for (const line of block.split("\n")) {
        const m = line.match(/^([A-Za-z0-9_-]+)\s*:\s*(.*)$/);
        if (m) fm[m[1]] = m[2].trim();
    }
    return fm;
};

/* ---------------------------------------------------------- the two rules --- */

// Ruled 2026-08-27. Both are generated elsewhere from one source: the hash lives
// in the .ots proofs, the weekly RFC 3161 manifests and zenodo-dois.json; the DOI
// lives in zenodo-dois.json -> src/zenodo-dois.ts -> citation_doi.
const BANNED_FIELDS = ["sha256", "doi"];

// Both are open licences and both are deliberate. CC0 for anything that has to
// function as a borrowable standard or a prior-art instrument; CC-BY for
// author-voice essays, where attribution is the point.
const PERMITTED_LICENCES = ["CC0-1.0", "CC-BY (author-voice essay)"];

// ⚠️ SHRINK-ONLY. See the header. Every entry is a file that predates the ruling,
// is deposited, and is cleaned at its next revision. Deleting a line is the fix
// landing; adding one is the bug this script exists to refuse.
const BANNED_FIELD_DEBT = new Set([
    "defensive-publications/aura-gated-anonymous-mate-selection.md",
    "defensive-publications/b-links-signed-provenance.md",
    "defensive-publications/cakkavatti-alignment-charter.md",
    "defensive-publications/certification-by-circulation.md",
    "defensive-publications/eightfold-path-institutional-architecture.md",
    "defensive-publications/gift-tag-time-reveal.md",
    "defensive-publications/giving-is-a-gift-too.md",
    "defensive-publications/gratitude-as-cooperation-substrate.md",
    "defensive-publications/gratitude-riding-currency-tag.md",
    "defensive-publications/incommensurability-preserving-coupler.md",
    "defensive-publications/mechanical-heart.md",
    "defensive-publications/multi-family-membership.md",
    "defensive-publications/need-compiled-questlines.md",
    "defensive-publications/proof-of-coordinate.md",
    "defensive-publications/safety-companion-pack-watch.md",
    "defensive-publications/studio-b-short-phase-bridge.md",
    "defensive-publications/the-assembly-that-holds-the-brake.md",
    "defensive-publications/the-borrowable-standard.md",
    "defensive-publications/the-gift-operation.md",
    "defensive-publications/the-omitted-clause.md",
    "defensive-publications/the-persistence-architecture.md",
    "defensive-publications/the-referee-not-the-governor.md",
    "defensive-publications/the-rethank-multiplier.md",
    "defensive-publications/tipitaka-alignment-substrate.md",
    "defensive-publications/two-layer-reward.md",
    "defensive-publications/verified-human-anonymous-local-giving.md"
]);

// ⚠️ THE SAME CLAIM ALSO APPEARS IN BODY FOOTERS, and it is the more dangerous
// form. `*Document SHA-256 to be computed at publication…` is prose, so the
// front-matter check above cannot see it. The site's module generator strips any
// such line it meets — so the RENDERED page is clean and the MARKDOWN is not.
//
// ⭐ That split is exactly why this matters now: a corpus server reads the
// markdown, not the render. Every guard that has ever checked this claim checked
// the surface the generator fixes, and would have served the sentence it strips.
// Shrink-only, for the same reason as above: these files are deposited.
const BODY_CLAIM_DEBT = new Set([
    "defensive-publications/abhidhamma-executable-process-specification.md",
    "defensive-publications/aura-gated-anonymous-mate-selection.md",
    "defensive-publications/b-links-signed-provenance.md",
    "defensive-publications/b-tag-recommendation-function-methodology.md",
    "defensive-publications/co-presence-gated-redemption.md",
    "defensive-publications/eightfold-path-institutional-architecture.md",
    "defensive-publications/embodied-advocate-pageant.md",
    "defensive-publications/giving-is-a-gift-too.md",
    "defensive-publications/individuation-without-essence.md",
    "defensive-publications/inverted-alms-round.md",
    "defensive-publications/manufactured-universal-giving.md",
    "defensive-publications/mechanical-heart.md",
    "defensive-publications/miss-aquarius-and-aquarian-pool-architecture.md",
    "defensive-publications/patthana-typed-causation-vocabulary.md",
    "defensive-publications/sacrifice-witness-without-discharge.md",
    "defensive-publications/sankhara-dukkha-ai-welfare.md",
    "defensive-publications/steward-routed-alms.md",
    "defensive-publications/the-game-that-graduates-you.md",
    "defensive-publications/the-gift-operation.md",
    "defensive-publications/the-sport-that-says-your-name.md",
    "defensive-publications/the-wager-that-isnt.md",
    "defensive-publications/tipitaka-alignment-substrate.md",
    "defensive-publications/two-layer-reward.md",
    "defensive-publications/verified-human-anonymous-local-giving.md",
    "defensive-publications/vinaya-as-ai-reasoning-training-corpus.md",
    "defensive-publications/vinaya-governance-primitives-distributed-dharma-networks.md"
]);

/* ------------------------------------------------------------------ run --- */

const files = corpusFiles();
if (files.length === 0) die("no corpus files found — is this running from the repo root?");

const problems = [];
const census = {};
let debtSeen = 0;

for (const rel of files) {
    const text = readFileSync(join(ROOT, rel), "utf8");
    const fm = frontMatter(text, rel);

    // 1. Every file declares a licence, and it is one we actually publish under.
    if (!fm.license) {
        problems.push(
            `${rel} declares no \`license:\`.\n` +
                `      fix: add one of ${PERMITTED_LICENCES.map((l) => `"${l}"`).join(" or ")}.\n` +
                `      The per-file field is the AUTHORITY — LICENSE and README defer to it,\n` +
                `      and anything serving this corpus gates on it. A file without one\n` +
                `      cannot be served at all.`
        );
    } else if (!PERMITTED_LICENCES.includes(fm.license)) {
        problems.push(
            `${rel} declares license "${fm.license}", which is not a licence this corpus publishes under.\n` +
                `      permitted: ${PERMITTED_LICENCES.join(" · ")}\n` +
                `      fix: correct the field, or add the licence to PERMITTED_LICENCES here\n` +
                `      and to the table in README.md — deliberately, in one commit.`
        );
    } else {
        census[fm.license] = (census[fm.license] ?? 0) + 1;
    }

    // 2. Neither banned field, unless the file is on the shrink-only debt ledger.
    for (const field of BANNED_FIELDS) {
        if (!(field in fm)) continue;
        if (BANNED_FIELD_DEBT.has(rel)) {
            debtSeen++;
            continue;
        }
        problems.push(
            `${rel} carries \`${field}:\` in its front matter, which was ruled out 2026-08-27.\n` +
                `      A hash field cannot sit inside the file it hashes, and a DOI cannot exist\n` +
                `      before the deposit that hashes the file. Both are generated elsewhere:\n` +
                `      the hash from the .ots proofs and the weekly RFC 3161 manifests, the DOI\n` +
                `      from zenodo-dois.json.\n` +
                `      fix: delete the line. Do NOT add this file to BANNED_FIELD_DEBT — that\n` +
                `      list is for files that predate the ruling and can only shrink.`
        );
    }

    // 3. The body-footer form of the same claim.
    const body = text.slice(text.indexOf("\n---", 4));
    if (/Document SHA-256/.test(body) && !BODY_CLAIM_DEBT.has(rel)) {
        problems.push(
            `${rel} carries a "Document SHA-256 …" claim in its BODY.\n` +
                `      Same 2026-08-27 ruling, harder form: it is prose, so the front-matter\n` +
                `      check cannot see it, and the site's module generator STRIPS it — which\n` +
                `      means the rendered page is clean while the markdown still asserts it.\n` +
                `      Anything reading the markdown directly, a corpus server included, would\n` +
                `      serve the claim the website removes.\n` +
                `      fix: delete the sentence. Do NOT add this file to BODY_CLAIM_DEBT.`
        );
    }
}

if (problems.length) {
    console.error("check-frontmatter: FAILED\n");
    for (const p of problems) console.error(`  - ${p}\n`);
    process.exit(1);
}

const licenceLine = Object.entries(census)
    .sort((a, b) => b[1] - a[1])
    .map(([l, n]) => `${n} ${l}`)
    .join(" · ");

console.log(
    `check-frontmatter: ${files.length} files — ${licenceLine}` +
        (debtSeen ? `; ${debtSeen} pre-ruling files still carry a banned field (they ride their next revision)` : "")
);

if (process.argv.includes("--census")) {
    console.log("\nper-genre:");
    for (const g of GENRES) {
        const inGenre = files.filter((f) => f.startsWith(g + "/"));
        const byLicence = {};
        for (const rel of inGenre) {
            const fm = frontMatter(readFileSync(join(ROOT, rel), "utf8"), rel);
            byLicence[fm.license] = (byLicence[fm.license] ?? 0) + 1;
        }
        console.log(`  ${g}: ${Object.entries(byLicence).map(([l, n]) => `${n} ${l}`).join(" · ")}`);
    }
    if (BANNED_FIELD_DEBT.size) {
        console.log(`\nbanned-field debt (${BANNED_FIELD_DEBT.size} files, shrink-only):`);
        for (const f of [...BANNED_FIELD_DEBT].sort()) console.log(`  ${f}`);
    }
}
