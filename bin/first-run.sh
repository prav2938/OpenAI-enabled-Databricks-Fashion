#!/bin/bash
set -ex
source ./config.mk

# create virtualenv
if [[ ! -d .ve ]]; then
  ./bin/venv.sh
fi

source .ve/bin/activate

pip install --upgrade pip wheel

# install packages into virtual env
pip install --upgrade pip-tools
pip-sync requirements/requirements.txt