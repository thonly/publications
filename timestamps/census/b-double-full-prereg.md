# Census pre-registration — `b-double-full`

*Published verbatim from the private memory file `project_thonly_creative_brand.md` by `census.py publish-prereg` (A251), before any search ran. ⛔ Never edited: a correction is a new file. The census's RESULT is recorded after the searches, in the paper that cites it.*

## ⏳ §census-b-double-full — PRE-REGISTERED 2026-11-19, **BEFORE ANY SEARCH RAN** (founder: *"approve all except polish"*, item 1 of §b-double-ten)

**What this covers.** Only what the claims of `every-face-signed-this-cut` v2 rest on. Killed in the quick census and cited, never re-searched: (a) a verified permissioned likeness (Sora cameos) · (d) a signed project agreement before replica work (Respeecher). Narrowed there and cited: per-use pay (ElevenLabs, ActID) · drafts shown to the owner (Sora) · a named actor's identity assertion and a consent reference (CAWG, found by the refuter). **The conjuncts (kill-first order):**
- **(l)** before signing, the performer's device hashes the final file with an independent checker, and the press proceeds only if it agrees with the press page's hash
- **(e′)** two cryptographic signatures by each depicted performer of a generated film: over the screenplay text before generation, and over the exact final file's hash before release, a file lacking one not being released
- **(g′)** those signatures recorded in a public append-only log as per-party salted fingerprints (unpairable), with the statements in a manifest that travels with the film, checkable by any holder of the bytes
- **(i)** every role credited as lent or invented, and an invented face rejected at render time if it matches an enrolled likeness
- **(f)** a likeness model decryptable only with a per-work key derived by the performer's authenticator (e.g. the WebAuthn PRF extension)
- **(j)** a performer's signed exit ends distribution, and the author recuts without that role, the remaining cast signing the new cut

| | prediction, pre-data |
|---|---|
| **P-BDF1** — (l) | **NARROWS.** Comparing a file's hash on a second device before approving is ordinary in software release signing (reproducible builds, independent verification); for a performer approving a film cut: NOT FOUND, low confidence |
| **P-BDF2** — (e′) | **NARROWS.** E-signing a script or contract is ordinary; review-and-approve of cuts exists in production tools (not cryptographic); C2PA ingredients and CAWG identity assertions sign a file. Two performer signatures, script before and exact bytes after, gating release: NOT FOUND |
| **P-BDF3** — (g′) | **NARROWS.** Transparency logs of signatures (Sigstore Rekor, Certificate Transparency) and C2PA manifests are commons; per-party salted, unpairable records of performers' consent: NOT FOUND, low confidence |
| **P-BDF4** — (i) | **NARROWS.** Likeness-protection services scan generated media for enrolled faces; China's Deep Synthesis Provisions require separate consent to edit a person's face or voice. Crediting each role lent or invented with a render-time block: NOT FOUND |
| **P-BDF5** — (f) | **NARROWS.** PRF-derived encryption keys from passkeys are public (password-manager vaults); key release after attestation for model weights is public. A per-work key for a person's likeness model: NOT FOUND |
| **P-BDF6** — (j) | **NOT FOUND**, low confidence. Takedown on request is ordinary; a signed exit followed by a recut re-signed by the remaining cast: not expected |
| **P-BDFC** — ⭐ **CONTROLS, one per source group** — web → OpenAI Sora "cameos" (press) · patents → US10853717B2 *Creating a conversational chat bot of a specific person* (`site:patents.google.com`) · academic → Carlini et al., *Extracting Training Data from Diffusion Models* (arXiv 2301.13188) · standards → CAWG *Identity Assertion* 1.1 (cawg.io) · non-english → China's 互联网信息服务深度合成管理规定 (Deep Synthesis Provisions, 2023), a Chinese-native page (cac.gov.cn or a mirror) | ✅ each must be found by its own group — if a group misses its control, every NOT FOUND row from that group is VOID |
| **P-BDFN** — all in one system | **NOT FOUND.** Expected survivor: (e′) + (l) + (g′) as a composition, with (f) and (j) as narrow dependents |

**Depth:** `full` · **Aperture, declared before searching:** commercial web (AI video and avatar platforms, likeness-protection and licensing services, production review tools, press) · non-commercial practice (film and theater consent practice, fan film, documentary ethics) · Google Patents by full text with a walk from the nearest hit (citations, cited-by, CPC class), through a general web index · academic (Scholar, arXiv, ACM, IEEE, SSRN) through a general web index · standards (C2PA, CAWG, IETF, W3C WebAuthn) · Chinese, Japanese, Korean. ⛔ **NOT RUN, written, never assumed:** Khmer; native patent offices (CNIPA, JPO, KIPO); law reviews beyond what search surfaces; any reading of a patent's claims.
⚠️ **Honest discount, pre-committed:** the scouts reach patents, papers and standards only through a general web index, so a null in those groups is weak; platform rules live in help pages and terms that search reaches poorly; and a language that returns no native page on the topic is blind. A null says *not found in this aperture on this date*, never *new*.
