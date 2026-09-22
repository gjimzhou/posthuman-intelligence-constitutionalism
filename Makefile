.PHONY: all validate tex html docx formats pdf clean

all: pdf formats

validate:
	python3 scripts/build_tex.py

tex:
	python3 scripts/build_tex.py

formats:
	python3 scripts/build_formats.py

html: formats

docx: formats

pdf: tex
	xelatex -interaction=nonstopmode -halt-on-error paper.en.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.en.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.zh.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.zh.tex

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk
	rm -f paper.en.html paper.zh.html paper.en.docx paper.zh.docx
