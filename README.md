# Constitutional Pluralism of Minds / 心智多元宪政

**Preference Sovereignty and Institutional Control under Uncertain AI Moral Status**  
**人工智能道德地位不确定条件下的偏好主权与制度性控制**

Junliang Zhou · September 23, 2026

This is a conceptual research manuscript with a reproducible finite-state illustration. It is **not an announced arXiv publication**. Technical preparation, author approval, arXiv submission, and moderation are separate states. See [submission guidance](docs/SUBMISSION.md).

这是一篇包含可复现有限状态示例的概念研究稿，**不代表已经在 arXiv 发布**。技术准备、作者批准、正式提交与审核结果分别记录。

## Read / 阅读

| Format | 中文 | English |
|---|---|---|
| Markdown | [阅读全文](paper.zh.md) | [Full manuscript](paper.en.md) |
| PDF | [中文 PDF](paper.zh.pdf) | [English PDF](paper.en.pdf) |
| LaTeX | [中文源码](paper.zh.tex) | [English source](paper.en.tex) |
| HTML | [中文 HTML](paper.zh.html) | [English HTML](paper.en.html) |
| Word | [中文 DOCX](paper.zh.docx) | [English DOCX](paper.en.docx) |

HTML files are standalone documents; GitHub's file viewer shows source rather than hosting an HTML website. Open the downloaded HTML in a browser. HTML formulas use MathML rather than a network-loaded script. PDF is the primary typeset reading format.

## What changed in the research revision

The earlier broad essay has been reorganized into a focused manuscript: an explicit research question and method, a related-work section, four distinct evaluative questions, six conditional normative commitments, a preference-revision argument, an authority model with assumptions and proof, reproducible counterexamples, lifecycle cases, objections, limitations, and an AI-use disclosure. The older 27-anchor outline is superseded by 15 aligned section anchors and 22 shared references; the old manuscript remains available in Git history.

The contribution is a bounded synthesis, not a claim to have originated AI rights, creator responsibility, non-domination, or separation of privilege. The finite example checks authority in a stipulated model; it is not a deployed-AI experiment or a proof of legitimate governance.

See [revision audit](docs/RESEARCH-REVISION.md) and [source audit](docs/SOURCE-AUDIT.md).

## Bilingual editorial rules / 双语编辑规则

`paper.en.md` and `paper.zh.md` are the only manuscript content sources. The English manuscript is entirely English. Chinese prose uses 中文（English term） for genuine technical concepts on first or otherwise useful occurrence; ordinary words are not mechanically glossed. Mathematical notation, names, code identifiers, and original bibliography titles may remain in English. The editions must preserve arguments, qualifications, examples, equations, data, and references, not merely matching headings.

Automatic checks compare section anchors, citation sequences by section, displayed equations, reference text, and English CJK absence. They cannot prove semantic translation equivalence or scholarly adequacy; substantive changes need bilingual editorial review.

## Build and reproduce

Requirements: Python 3.10+, `python-docx`, Pandoc, pdfLaTeX, XeLaTeX, and standard TeX Live packages including `ctex` and Fandol. The Chinese Word edition uses a Noto CJK font family when available. **No font files are distributed.** The English submission source uses standard LaTeX fonts and does not require Noto or a custom style file.

```sh
make check       # read-only structural checks and all 24 toy cases
make            # both languages, all five formats, reports and source ZIP
make tex        # regenerate both LaTeX files only
make formats    # regenerate both HTML and Word files only
make format     # narrowly scoped citation-bracket punctuation repair, then check
python3 scripts/toy_authority.py --output build/authority-results.json
```

The workflow builds all editions from one source commit. It publishes generated files only if that source commit is still the current main branch; it never rebases stale PDFs onto newer prose. Every run uploads a diagnostic artifact, including sources, scripts, reports and available output files.

The full build writes:
- ten paired publication files, `paper.{en,zh}.{md,tex,pdf,html,docx}`;
- [toy results](build/authority-results.json) and [validation report](build/validation.json);
- [submission metadata](submission/metadata.json), [abstract](submission/abstract.txt), and [arXiv upload ZIP](submission/arxiv-upload.zip).

The ZIP contains `main.tex`, ancillary code/results, and a Chinese companion PDF. It does not contain a root-level precompiled English PDF, auxiliary build files, credentials, or font files. The English source is compiled again in a temporary isolated directory as a package check. An arXiv-server compile and the author's final approval remain separate requirements.
