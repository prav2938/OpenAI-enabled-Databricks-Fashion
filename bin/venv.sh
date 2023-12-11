#!/bin/bash
set -ex
source ./config.mk

# create virtual environment

python3 -m venv .ve --prompt="${ENV_NAME}"

# activate environment
echo "activating virtual environment"
source .ve/bin/activate