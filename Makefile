.PHONY: all check format tex formats pdf clean

all:
	python3 scripts/build_all.py

check:
	python3 scripts/build_all.py --check

format:
	python3 scripts/build_all.py --format --check

tex:
	python3 scripts/build_all.py --tex-only

formats:
	python3 scripts/build_all.py --formats-only

pdf: all

clean:
	rm -rf .build
