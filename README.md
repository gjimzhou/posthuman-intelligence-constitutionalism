# Posthuman Intelligence Constitutionalism

**从智能祛魅到心智多元宪政：人工智能时代的主体性、创造伦理与非支配秩序**  
**From the Demystification of Intelligence to Constitutional Pluralism of Minds: Subjectivity, the Ethics of Creation, and Non-Domination in the Age of Artificial Intelligence**

Junliang Zhou · Working Paper · September 2026

## 阅读 / Read

| Language | Markdown | LaTeX | PDF |
|---|---|---|---|
| 中文 | **[阅读全文](paper.zh.md)** | [paper.zh.tex](paper.zh.tex) | [paper.zh.pdf](paper.zh.pdf) |
| English | **[Read the full paper](paper.en.md)** | [paper.en.tex](paper.en.tex) | [paper.en.pdf](paper.en.pdf) |

GitHub 上优先阅读 Markdown；PDF 由 GitHub Actions 自动构建并与两份 Markdown 正文保持同步。  
For browser reading, use the Markdown editions. GitHub Actions automatically rebuilds the paired LaTeX and PDF editions from the two canonical Markdown sources.

## 双语规则 / Bilingual convention

中文版以自然中文为正文，专业术语采用 **中文（English term）** 的形式；数学公式、专名与参考文献原题保留必要的英文表达。英文版为纯英文正文，不夹中文。两版采用相同的 27 个章节锚点、相同的论证顺序、相同的公式结构、相同的六项基础公理与同一组 15 条参考文献。

The Chinese edition uses natural Chinese prose with technical vocabulary presented as **Chinese (English term)** where useful. The English edition contains English prose only. Both editions share the same 27-section architecture, argument order, equation structure, six foundational axioms, and 15 references.

## 文件结构 / Repository structure

- **paper.zh.md** — 中文 canonical content
- **paper.en.md** — English canonical content
- **paper.zh.tex** — generated Chinese LaTeX
- **paper.en.tex** — generated English LaTeX
- **paper.zh.pdf** — generated Chinese PDF
- **paper.en.pdf** — generated English PDF
- **scripts/build_tex.py** — validates bilingual alignment and regenerates both LaTeX editions
- **.github/workflows/build-bilingual.yml** — builds and commits both PDFs
- **Makefile** — local bilingual build commands

**paper.zh.md** and **paper.en.md** are the content sources of truth. Generated LaTeX/PDF files should not be edited as independent manuscripts; regenerate them from the paired Markdown sources.

## 核心论点 / Core thesis

本文提出一种面向多种心智共存文明的宪政框架。核心主张包括：智能不等同于意识、道德承受者地位或政治人格；创造心智会产生义务，而不会自动产生对该心智的所有权；能力与基本道德地位是不同维度；被创造的心智应保有有意义的偏好主权与开放未来；AI 对齐应同时发展为制度性对齐，通过执行、批评、验证、授权与审计的权力分离来降低单一智能体风险；长期共存应以**宪政性非支配（constitutional non-domination）**为核心，限制人类或人工心智对另一方施加任意支配。

The paper develops a constitutional framework for a civilization containing multiple kinds of minds. Its central claims are that intelligence should not be conflated with consciousness, moral patienthood, or political personhood; creation can generate obligations without generating ownership; capability and fundamental moral status are distinct dimensions; created minds should retain meaningful preference sovereignty and an open future; alignment should become institutional as well as model-level; and long-run coexistence should be organized around **constitutional non-domination**.

## Build

Requirements: Python 3, XeLaTeX, Noto Serif, Noto Sans, Noto CJK fonts, and DejaVu Sans Mono.

    make

or:

    python3 scripts/build_tex.py
    xelatex paper.en.tex
    xelatex paper.en.tex
    xelatex paper.zh.tex
    xelatex paper.zh.tex

Every push that changes either canonical Markdown edition or the build script triggers the bilingual build workflow. The workflow validates language/section/reference alignment, regenerates both LaTeX files, compiles both PDFs, uploads them as an Actions artifact, and commits synchronized generated outputs back to **main**.
