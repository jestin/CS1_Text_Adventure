PYTHON = python3
LINTER = pylint
LINTER_OPTIONS = --disable=W0614,W0622,W0401,C0103,C0114,C0116
MAIN=main.py

all: lint

lint:
	$(LINTER) $(LINTER_OPTIONS) $(MAIN)

run:
	$(PYTHON) $(MAIN)

