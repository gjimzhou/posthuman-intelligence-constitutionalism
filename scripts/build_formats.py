#!/usr/bin/env python3
"""Build paired HTML and DOCX editions from the canonical bilingual Markdown sources."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAIRS = (
    ("zh", "zh-CN", "paper.zh.md"),
    ("en", "en-US", "paper.en.md"),
)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> None:
    for suffix, lang, source in PAIRS:
        run([
            "pandoc",
            source,
            "--from=gfm+tex_math_dollars",
            "--to=html5",
            "--standalone",
            "--mathjax",
            "--metadata", f"lang={lang}",
            "--output", f"paper.{suffix}.html",
        ])
        run([
            "pandoc",
            source,
            "--from=gfm+tex_math_dollars",
            "--to=docx",
            "--metadata", f"lang={lang}",
            "--output", f"paper.{suffix}.docx",
        ])

    print("Built paired HTML and DOCX editions from canonical Markdown sources.")


if __name__ == "__main__":
    main()
