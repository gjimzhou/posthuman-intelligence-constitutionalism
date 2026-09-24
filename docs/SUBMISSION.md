# arXiv submission package and author checklist

Status: **prepared candidate, not submitted**. No arXiv account authorization, existing identifier, license selection, or author final approval was supplied in this workflow. No arXiv identifier is invented or inferred from GitHub publication.

## Package

After a successful full build, `submission/arxiv-upload.zip` contains:

```text
main.tex
anc/paper.zh.pdf
anc/toy_authority.py
anc/authority-results.json
anc/README.txt
```

Select `main.tex` and **pdfLaTeX** for the English main paper. The Chinese PDF is a translation companion, not a second independent study. Chinese LaTeX, Markdown, HTML and Word remain available as paired repository files. The ancillary directory intentionally contains no TeX source or font files. arXiv supports ancillary files with TeX-based submissions; supplementary text is not separately indexed. Check the server's treatment of the companion during submission.

The English source has an embedded bibliography and uses standard TeX Live packages. The build recompiles the extracted source in a temporary directory with shell escape disabled. This is a local package test, **not a test on arXiv's servers**. Inspect arXiv's own generated PDF before completing submission.

## Metadata

`submission/metadata.json` and `submission/abstract.txt` are populated from the English canonical manuscript, avoiding divergence between the form and the paper. The suggested primary category is **cs.CY (Computers and Society)**, because the manuscript concerns AI ethics and governance. This is an editorial fit assessment, not an arXiv classification decision or a guarantee of acceptance. No cross-list is preselected.

License and arXiv ID remain null until the author supplies the actual choices and records. The submitter must choose a distribution license and agree to the submission terms. Do not invent an institution or add an affiliation without the author's explicit confirmation.

## Author-controlled steps

Before submission, the author must read the full English paper and check the Chinese translation; verify that the research question, examples, limited formal claims, references and AI-use disclosure accurately represent the work; and determine any applicable rights, funding or conflict disclosures. No statement of completed independent human review has been inserted.

Sign in through the author's own arXiv account. A new account or category may require endorsement. If there is an existing arXiv record for this paper, use its replacement/version procedure rather than create a duplicate. No existing ID has been established here. For a new paper, upload the source ZIP, inspect the generated PDF, complete metadata and license selections, review all declarations, and submit. Record the actual submission identifier and later moderation result separately in this file and in metadata; uploading a file or preparing a GitHub commit is not proof of submission.

arXiv's author self-submission policy and limited proxy arrangements apply. This workflow does not possess an authenticated arXiv submission connector and does not bypass that boundary. Never store account passwords or authentication tokens in this repository.

## Official instructions checked September 23, 2026

- Submission and author requirements: https://info.arxiv.org/help/submit/index.html
- Moderation, scholarly standards and significant AI-tool disclosure: https://info.arxiv.org/help/moderation/index.html
- TeX package preparation: https://info.arxiv.org/help/submit_tex.html
- Ancillary files: https://info.arxiv.org/help/ancillary_files.html
- Categories: https://arxiv.org/category_taxonomy
- Endorsement: https://info.arxiv.org/help/endorsement.html
- License choices: https://info.arxiv.org/help/license/index.html
- Proxy submission: https://info.arxiv.org/help/third_party_submission.html

arXiv is not a peer-reviewed journal. Professional formatting and a passing build do not certify scholarly acceptance; originality, substantive research interest and category fit remain subject to moderation.
