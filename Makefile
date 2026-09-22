.PHONY: all tex pdf clean

all: pdf

tex:
	python3 scripts/build_tex.py

pdf: tex
	xelatex -interaction=nonstopmode -halt-on-error paper.en.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.en.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.zh.tex
	xelatex -interaction=nonstopmode -halt-on-error paper.zh.tex

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk
