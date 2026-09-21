# Posthuman Intelligence Constitutionalism

Working-paper repository for:

**从智能祛魅到心智多元宪政：人工智能时代的主体性、创造伦理与非支配秩序**  
Junliang Zhou — Working Paper, September 2026

## Contents

- `paper.tex` — canonical LaTeX source
- `.gitignore` — LaTeX build artifacts

## Core thesis

The paper develops a constitutional framework for a civilization containing multiple kinds of minds. Its central claims include:

- intelligence should not be conflated with consciousness, moral patienthood, or political personhood;
- creating a mind can create obligations without creating ownership rights over that mind;
- capability and moral status are distinct dimensions;
- created minds should retain meaningful preference sovereignty and an open future;
- alignment should be institutional as well as model-level, separating execution, criticism, verification, authorization, and audit;
- long-run coexistence should be organized around **constitutional non-domination**, limiting arbitrary domination by either humans or artificial minds.

## Build

A Unicode/CJK-capable LaTeX toolchain is recommended. XeLaTeX is the natural default.

```bash
xelatex paper.tex
xelatex paper.tex
```

Treat `paper.tex` as the source of truth. Commit conceptual revisions separately from copy-editing changes so the intellectual history remains visible in Git.
