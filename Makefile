# This Makefile requires the following commands to be available:
# * python2
# * virtualenv

DEPS:=requirements.txt
PIP:="venv/bin/pip"
TWINE:="venv/bin/twine"
CMD_FROM_VENV:=". venv/bin/activate; which"
TOX=$(shell "$(CMD_FROM_VENV)" "tox")
PYTHON=$(shell "$(CMD_FROM_VENV)" "python")
TOX_PY_LIST="$(shell $(TOX) -l | grep ^py | xargs | sed -e 's/ /,/g')"


.PHONY: tox pyclean clean venv test lint isort setup.py publish

tox: venv setup.py
	$(TOX)

pyclean:
	@find . -name *.pyc -delete
	@rm -rf *.egg-info build
	@rm -rf coverage.xml .coverage

clean: pyclean
	@rm -rf venv
	@rm -rf .tox
	@rm -rf dist

venv:
	@virtualenv venv
	@$(PIP) install -U "pip>=10.0" -q
	@$(PIP) install -r $(DEPS)

test: clean tox

test/%: venv pyclean
	$(TOX) -e $(TOX_PY_LIST) -- $*

lint: venv
	@$(TOX) -e lint
	@$(TOX) -e isort-check

isort: venv
	@$(TOX) -e isort-fix

setup.py: venv
	$(PYTHON) setup_gen.py
	@$(PYTHON) setup.py check --restructuredtext

publish: setup.py
	$(PYTHON) setup.py sdist
	@$(TWINE) upload dist/*
