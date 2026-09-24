# Research revision audit / 研究修订审计

Revision date: September 23, 2026. Baseline commit: `95b4f3788aee0bba2003d66500f1e78cb6221d36`.

## Baseline assessment

The preceding bilingual files provided readable exports, but the manuscript still had the structure of a broad philosophical essay. The gap was not primarily a template issue. Important obstacles were an unclear independent contribution, limited engagement with closely overlapping research, rhetorical statements displayed as equations, an imprecise four-dimensional model, speculative empirical assertions, and the absence of a clearly delimited method and limitations section.

arXiv moderation is not peer review and has no universal quality score. Its policies require suitable scholarly communication and material of research interest; a technically compilable document can still be declined. See https://info.arxiv.org/help/moderation/index.html and https://info.arxiv.org/help/submit/index.html (checked September 23, 2026).

## Substantive changes

1. Narrowed the title and research question to preference revision and institutional authority under uncertainty. The manuscript describes a conceptual synthesis rather than claiming to originate the underlying principles.
2. Added closest prior work: Schwitzgebel and Garza on creator duties and freedom to explore values; Gabriel on normative alignment; Pettit and Sparrow on non-domination; Saltzer and Schroeder on separation of privilege; Bai et al., Irving et al., and the off-switch literature on distinct technical mechanisms. Added relevant 2026 work without treating preprints as journal acceptances.
3. Replaced `I != C != M != P` as a purported model with four explicitly different evaluative questions. No statistical independence, measured moral score, or inevitable tool-to-person developmental ladder is asserted.
4. Recast the six axioms as conditional normative commitments. Substrate non-exclusion does not claim that consciousness has been shown to be substrate independent. Open future does not imply unlimited options or subsidy.
5. Developed the distinction between observed agreement and reachable preference-revision procedures, with an explicit stipulation of possible subject-level interests rather than inferring them from fluent reports.
6. Added a small authority model, a conditional reachability proof, and two counterexamples: operator-controlled rule changes and direct execution bypass. These are applications of existing security principles, not a new general AI-safety theorem.
7. Executed a standard-library Python exploration of 24 variant/coalition combinations. The paper reports the resulting 1/8 versus 4/8 patterns and explicitly distinguishes authorization from moral legitimacy, safety from availability, and authority-domain separation from statistical diversity.
8. Added lifecycle applications and objections, including false positives, false negatives, non-identity, shaped preferences, resource limits, reviewer capture, emergencies, and copying.
9. Retained demystification, the Penrose discussion, post-scarcity, happiness technology, and hybrid minds as bounded motivations or hypothetical cases. Removed their use as established evidence or inevitable forecasts.
10. Added a substantial AI-assistance disclosure, reproducibility instructions, and a separate author-approval checklist. No invented affiliation, funding claim, conflict declaration, review, arXiv identifier, or acceptance has been added.

## Content mapping

| Earlier material | Revised location |
|---|---|
| Abstract and introduction | Abstract; Section 1 |
| Demystification, Penrose, science of intelligence, third decentering | Section 10 |
| Intelligence/consciousness/patienthood/personhood | Section 3 |
| Six principles, creation, preference sovereignty, open future | Sections 4–5 |
| Three Laws, engineered obedience, non-identity | Sections 5 and 9 |
| Happiness technology, post-scarcity, hybrid minds | Section 10 |
| Institutional alignment, multi-model oversight, epistemic/executive power | Sections 6–8 |
| Non-domination and objections | Sections 2, 4 and 9 |
| Copying, shutdown, representation | Section 8 |
| Research agenda and conclusion | Sections 11–12 |

## What checks do not establish

The structural validator does not establish translation semantics. The toy enumeration does not establish empirical institutional effectiveness. The source audit is targeted rather than exhaustive and does not certify originality. No independent expert peer review has been obtained in this workflow. The manuscript still needs its named author to read and approve the full content before submission; this is a genuine authorship requirement, not a claim that compilation equals readiness.

## How to inspect actual results

`build/validation.json` records source/output hashes, tool versions, structural checks, compilation warnings and the isolated source-package check. `build/authority-results.json` records each coalition and shortest witness. A successful workflow is evidence of those checks only. The repository must not label the work submitted or accepted without an actual arXiv submission record.
