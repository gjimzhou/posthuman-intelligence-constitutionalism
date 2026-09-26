"""Stage the reading website without modifying canonical manuscript exports."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
OUT.mkdir(exist_ok=True)
shutil.copy2(ROOT / "site/index.html", OUT / "index.html")
shutil.copytree(ROOT / "site/assets", OUT / "assets", dirs_exist_ok=True)
TRACKER = '<script defer src="assets/analytics.js" data-project="posthuman-intelligence-constitutionalism"></script>'
for lang in ("en", "zh"):
    for extension in ("html", "pdf", "docx"):
        source = ROOT / f"paper.{lang}.{extension}"
        assert source.is_file() and source.stat().st_size > 100, source
        if extension == "html":
            text = source.read_text()
            assert "</head>" in text and "</body>" in text, source
            text = text.replace("</head>", TRACKER + "\n</head>", 1)
            (OUT / source.name).write_text(text)
        else:
            shutil.copy2(source, OUT / source.name)
(OUT / ".nojekyll").touch()
print("Staged homepage, both HTML editions and four downloads.")
