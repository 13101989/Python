#!/bin/sh

echo "Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt
echo "Finished installing dependencies"

echo "Running pylint checks"
pylint src
echo "Finished running pylint checks"

echo "Running mypy checks"
mypy src
echo "Finished running mypy checks"

echo "Running flake8 checks"
flake8 src
echo "Finished running flake8 checks"

echo "Running pytest"
pytest --cov .
echo "Finished running tests"

echo"Building Sphinx documentation"
make html
echo "Finished building documentation"
