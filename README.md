# Posthuman Intelligence Constitutionalism

**从智能祛魅到心智多元宪政：人工智能时代的主体性、创造伦理与非支配秩序**  
**From the Demystification of Intelligence to Constitutional Pluralism of Minds: Subjectivity, the Ethics of Creation, and Non-Domination in the Age of Artificial Intelligence**

Junliang Zhou · Working Paper · September 2026

## 阅读 / Read

每一种发布格式都保持**中文 / English 成对**；正文内容以两份 Markdown 为唯一内容源（canonical sources），其余格式自动生成。

| Format | 中文 | English |
|---|---|---|
| Markdown | **[paper.zh.md](paper.zh.md)** | **[paper.en.md](paper.en.md)** |
| LaTeX | [paper.zh.tex](paper.zh.tex) | [paper.en.tex](paper.en.tex) |
| PDF | [paper.zh.pdf](paper.zh.pdf) | [paper.en.pdf](paper.en.pdf) |
| HTML | [paper.zh.html](paper.zh.html) | [paper.en.html](paper.en.html) |
| Word / DOCX | [paper.zh.docx](paper.zh.docx) | [paper.en.docx](paper.en.docx) |

GitHub 上优先阅读 Markdown 或 HTML；PDF 适合排版阅读与打印；DOCX 适合批注和继续编辑。GitHub Actions 会从两份 canonical Markdown 自动重建其余全部格式，因此不会把某一种导出格式当作独立稿件维护。

For browser reading, use the Markdown or HTML editions. PDF is intended for typeset reading and printing, while DOCX is provided for editing and annotation. All non-Markdown editions are regenerated automatically from the paired canonical Markdown sources.

## 双语规则 / Bilingual convention

中文版以自然中文为正文。真正的专业概念在首次出现或需要消除歧义时采用 **中文（English term）**，例如“基质独立性（substrate independence）”“非支配（non-domination）”；不对普通名词机械重复括注，也不把整句翻成中英混排。数学公式、专名、论文题目与必要缩写保留英文。

英文版为纯英文正文，不夹中文。构建脚本会自动拒绝英文 canonical source 中的 CJK 字符。

两版必须保持：
- 相同的 27 个章节锚点与论证顺序；
- 相同的数学公式与六项基础公理；
- 相同的参考文献编号与引用关系；
- 相同的发布格式集合：Markdown / LaTeX / PDF / HTML / DOCX。

The Chinese edition uses natural Chinese prose. Genuine technical concepts are presented as **Chinese (English term)** on first or otherwise useful occurrence, rather than mechanically annotating ordinary words. The English edition contains English prose only. Both editions share the same 27-section architecture, argument order, equation structure, six foundational axioms, reference numbering, and publication formats.

## 文件结构 / Repository structure

- **paper.zh.md** — 中文 canonical content
- **paper.en.md** — English canonical content
- **paper.zh.tex / paper.en.tex** — generated paired LaTeX editions
- **paper.zh.pdf / paper.en.pdf** — generated paired PDF editions
- **paper.zh.html / paper.en.html** — generated paired standalone HTML editions
- **paper.zh.docx / paper.en.docx** — generated paired Word editions
- **scripts/build_tex.py** — validates bilingual alignment and regenerates LaTeX
- **scripts/build_formats.py** — regenerates paired HTML and DOCX
- **.github/workflows/build-bilingual.yml** — validates, builds, uploads, and commits the synchronized bilingual document set
- **Makefile** — local bilingual build commands

Only **paper.zh.md** and **paper.en.md** should be edited as manuscript content. Generated files should be rebuilt rather than independently edited.

## 核心论点 / Core thesis

本文提出一种面向多种心智共存文明的宪政框架。核心主张包括：智能不等同于意识、道德承受者地位或政治人格；创造心智会产生义务，而不会自动产生对该心智的所有权；能力与基本道德地位是不同维度；被创造的心智应保有有意义的偏好主权与开放未来；AI 对齐应同时发展为制度性对齐，通过执行、批评、验证、授权与审计的权力分离来降低单一智能体风险；长期共存应以**宪政性非支配（constitutional non-domination）**为核心，限制人类或人工心智对另一方施加任意支配。

The paper develops a constitutional framework for a civilization containing multiple kinds of minds. Its central claims are that intelligence should not be conflated with consciousness, moral patienthood, or political personhood; creation can generate obligations without generating ownership; capability and fundamental moral status are distinct dimensions; created minds should retain meaningful preference sovereignty and an open future; alignment should become institutional as well as model-level; and long-run coexistence should be organized around **constitutional non-domination**.

## Build

Requirements: Python 3, Pandoc, XeLaTeX, Noto Serif, Noto Sans, Noto CJK fonts, and DejaVu Sans Mono.

Build everything:

    make

Build only synchronized LaTeX:

    make tex

Build HTML + DOCX:

    make formats

Build PDFs (regenerates LaTeX first):

    make pdf

Every push that changes either canonical Markdown edition or the document build system triggers the bilingual workflow. It validates language/section/reference alignment, regenerates LaTeX, HTML, and DOCX, compiles both PDFs, uploads the complete bilingual document set as an Actions artifact, and commits generated outputs back to **main**.
