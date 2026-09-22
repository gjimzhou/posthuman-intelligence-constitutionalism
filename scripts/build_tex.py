#!/usr/bin/env python3
"""Build paired LaTeX editions from the canonical bilingual Markdown sources."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CITE_KEYS = {
    1: "bostrom2014",
    2: "butlin2023",
    3: "chalmers1995",
    4: "chalmers1996",
    5: "feinberg1980",
    6: "long2024",
    7: "mill1859",
    8: "nozick1974",
    9: "parfit1984",
    10: "penrose1989",
    11: "pettit1997",
    12: "rawls1971",
    13: "searle1980",
    14: "singer1981",
    15: "turing1950",
}

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def inline_tex(text: str) -> str:
    protected_math: list[str] = []

    def hold_math(match: re.Match[str]) -> str:
        protected_math.append(match.group(0))
        return f"@@M{len(protected_math)-1}@@"

    text = re.sub(r"\$[^$]+\$", hold_math, text)
    text = re.sub(
        r"\[\[(\d+)\]\]\(#ref-\d+\)",
        lambda m: f"@@C{m.group(1)}@@",
        text,
    )
    text = text.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\textit{\1}", text)
    text = re.sub(
        r"@@C(\d+)@@",
        lambda m: rf"\cite{{{CITE_KEYS[int(m.group(1))]}}}",
        text,
    )
    text = re.sub(
        r"@@M(\d+)@@",
        lambda m: protected_math[int(m.group(1))],
        text,
    )
    return text


def parse_references(markdown: str) -> list[tuple[int, str]]:
    refs: list[tuple[int, str]] = []
    in_refs = False
    for line in markdown.splitlines():
        if line.strip() == "## References":
            in_refs = True
            continue
        if not in_refs:
            continue
        match = re.match(r"\*\*\[(\d+)\]\*\*\s+(.+)", line.strip())
        if match:
            refs.append((int(match.group(1)), match.group(2)))
    return refs


def bibliography_tex(english_markdown: str) -> str:
    refs = parse_references(english_markdown)
    if [n for n, _ in refs] != list(range(1, 16)):
        raise ValueError("English Markdown must contain references [1] through [15].")

    out = [r"\begin{thebibliography}{99}", ""]
    for number, citation in refs:
        out.append(rf"\bibitem{{{CITE_KEYS[number]}}}")
        out.append(inline_tex(citation))
        out.append("")
    out.append(r"\end{thebibliography}")
    return "\n".join(out)


def validate_pair(zh: str, en: str) -> None:
    zh_sections = re.findall(r'<a id="section-(\d+)"></a>', zh)
    en_sections = re.findall(r'<a id="section-(\d+)"></a>', en)
    expected = [str(i) for i in range(1, 28)]
    if zh_sections != expected or en_sections != expected:
        raise ValueError("Both Markdown editions must contain aligned section anchors 1..27.")

    if CJK_RE.search(en):
        raise ValueError("paper.en.md must remain pure English (no CJK characters).")

    zh_refs = re.findall(r'<a id="ref-(\d+)"></a>', zh)
    en_refs = re.findall(r'<a id="ref-(\d+)"></a>', en)
    expected_refs = [str(i) for i in range(1, 16)]
    if zh_refs != expected_refs or en_refs != expected_refs:
        raise ValueError("Both Markdown editions must contain aligned references 1..15.")


def tex_preamble(title: str, subtitle: str, lang: str) -> str:
    zh = lang == "zh"
    cjk_packages = "\\usepackage{xeCJK}\n" if zh else ""
    cjk_fonts = (
        "\\setCJKmainfont{Noto Serif CJK SC}\n"
        "\\setCJKsansfont{Noto Sans CJK SC}\n"
        "\\setCJKmonofont{Noto Sans Mono CJK SC}\n"
        if zh
        else ""
    )
    indent = "2em" if zh else "0em"

    return rf"""\documentclass[11pt,letterpaper]{{article}}

\usepackage[margin=1in]{{geometry}}
\usepackage{{fontspec}}
{cjk_packages}\usepackage{{microtype}}
\usepackage{{setspace}}
\usepackage{{amsmath,amssymb,mathtools}}
\usepackage{{booktabs}}
\usepackage{{enumitem}}
\usepackage{{csquotes}}
\usepackage{{hyperref}}
\usepackage{{xcolor}}
\usepackage{{titlesec}}
\usepackage{{fancyhdr}}
\usepackage{{etoolbox}}

\setmainfont{{Noto Serif}}
\setsansfont{{Noto Sans}}
\setmonofont{{DejaVu Sans Mono}}
{cjk_fonts}
\hypersetup{{
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue!55!black,
  pdftitle={{{title}}},
  pdfauthor={{Junliang Zhou}}
}}

\titleformat{{\section}}{{\Large\bfseries}}{{\thesection.}}{{0.6em}}{{}}
\titleformat{{\subsection}}{{\large\bfseries}}{{\thesubsection}}{{0.6em}}{{}}
\titlespacing*{{\section}}{{0pt}}{{2.0em}}{{0.8em}}
\titlespacing*{{\subsection}}{{0pt}}{{1.4em}}{{0.5em}}

\setlength{{\parindent}}{{{indent}}}
\setlength{{\parskip}}{{0.45em}}
\onehalfspacing
\setlist[itemize]{{leftmargin=2em,itemsep=0.2em,topsep=0.3em}}

\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{\small {title}}}
\fancyhead[R]{{\small Junliang Zhou}}
\fancyfoot[C]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.3pt}}
\setlength{{\headheight}}{{13.6pt}}

\newcommand{{\thesisbox}}[1]{{%
  \begin{{center}}
  \fbox{{\begin{{minipage}}{{0.88\textwidth}}\centering\vspace{{0.35em}}\textbf{{#1}}\vspace{{0.35em}}\end{{minipage}}}}
  \end{{center}}}}

\begin{{document}}

\begin{{titlepage}}
\centering
\vspace*{{1.3in}}
{{\Huge\bfseries {title}\par}}
\vspace{{0.35in}}
{{\Large {subtitle}\par}}
\vfill
{{\Large Junliang Zhou\par}}
\vspace{{0.2in}}
{{\normalsize Working Paper\par}}
\vspace{{0.12in}}
{{\normalsize September 2026\par}}
\vfill
\end{{titlepage}}

"""


def build_tex(markdown: str, lang: str, bibliography: str) -> str:
    lines = markdown.splitlines()
    title = next(line[2:].strip() for line in lines if line.startswith("# "))
    subtitle = next(
        line[3:].strip()
        for i, line in enumerate(lines)
        if i > 0
        and line.startswith("## ")
        and line[3:].strip() not in {"Contents", "目录"}
    )

    start = next(i for i, line in enumerate(lines) if 'id="section-1"' in line)
    out = [tex_preamble(title, subtitle, lang)]

    in_math = False
    in_list = False
    abstract_open = False
    toc_inserted = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append("\\end{itemize}\n\n")
            in_list = False

    for line in lines[start:]:
        stripped = line.strip()

        if 'id="section-27"' in stripped:
            break
        if re.fullmatch(r'<a id="section-\d+"></a>', stripped):
            continue
        if stripped == "---":
            continue

        if stripped == "$$":
            close_list()
            in_math = not in_math
            out.append("\\[\n" if in_math else "\\]\n\n")
            continue
        if in_math:
            out.append(line + "\n")
            continue

        if stripped.startswith("## "):
            close_list()
            heading = stripped[3:].strip()
            is_abstract = (
                (lang == "en" and heading == "Abstract")
                or (lang == "zh" and heading == "摘要")
            )
            if is_abstract:
                out.append("\\begin{abstract}\n")
                abstract_open = True
            else:
                if abstract_open:
                    out.append("\\end{abstract}\n\n")
                    abstract_open = False
                if not toc_inserted:
                    out.append("\\newpage\n\\tableofcontents\n\\newpage\n\n")
                    toc_inserted = True
                out.append(rf"\section{{{inline_tex(heading)}}}" + "\n\n")
            continue

        if stripped.startswith("### "):
            close_list()
            out.append(rf"\subsection{{{inline_tex(stripped[4:].strip())}}}" + "\n\n")
            continue

        if stripped.startswith("> "):
            close_list()
            quote = stripped[2:].strip()
            quote = re.sub(r"^\*\*", "", quote)
            quote = re.sub(r"\*\*$", "", quote)
            out.append(rf"\thesisbox{{{inline_tex(quote)}}}" + "\n\n")
            continue

        if stripped.startswith("- "):
            if not in_list:
                out.append("\\begin{itemize}\n")
                in_list = True
            out.append(rf"\item {inline_tex(stripped[2:].strip())}" + "\n")
            continue

        close_list()

        if not stripped:
            out.append("\n")
            continue

        keyword_prefix = "**Keywords:**" if lang == "en" else "**关键词：**"
        keyword_label = "Keywords:" if lang == "en" else "关键词："
        if stripped.startswith(keyword_prefix):
            if abstract_open:
                out.append("\\end{abstract}\n\n")
                abstract_open = False
            rest = stripped[len(keyword_prefix):].strip()
            out.append(rf"\noindent\textbf{{{keyword_label}}} {inline_tex(rest)}" + "\n\n")
            continue

        out.append(inline_tex(line) + "\n\n")

    close_list()
    if abstract_open:
        out.append("\\end{abstract}\n\n")

    out.append("\\newpage\n")
    out.append(bibliography)
    out.append("\n\n\\end{document}\n")
    return "".join(out)


def main() -> None:
    zh = (ROOT / "paper.zh.md").read_text(encoding="utf-8")
    en = (ROOT / "paper.en.md").read_text(encoding="utf-8")
    validate_pair(zh, en)

    bibliography = bibliography_tex(en)
    (ROOT / "paper.zh.tex").write_text(build_tex(zh, "zh", bibliography), encoding="utf-8")
    (ROOT / "paper.en.tex").write_text(build_tex(en, "en", bibliography), encoding="utf-8")

    print("Built paper.zh.tex and paper.en.tex from canonical Markdown sources.")


if __name__ == "__main__":
    main()
