SHELL := /bin/bash
export PIP_INDEX_URL=https://pypi.org/simple

compile:
	pip install --upgrade setuptools
	pip install --upgrade wheel
	pip install --upgrade pip-compile-multi
	pip install --upgrade pip-tools
	pip-compile-multi
	
install:
	bash ./bin/first-run.sh
	
activate-env:
	bash ./bin/venv.sh

	