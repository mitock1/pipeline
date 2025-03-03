# service-template
# Pedro Ferrusca
# A common template to start a web app service using flask or fast api frameworks.
# Feel free to edit everything you might see useful.

A simple template for a python webapp service

1. Install pyenv and python version 3.X.X (update the version to meet your requirements)
    https://github.com/pyenv/pyenv


2. Setup an environment on the adequate version of python (selected above) using
    pyenv local 3.10.X
    python -m venv env

3. Install python-pip tools
    pip install --upgrade pip
    pip install "pip-tools==6.12.0"

4. Install python dependencies
    pip-sync requirements.txt requirements-dev.txt requirements-test.txt
    pip install --no-deps -e .
