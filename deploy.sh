#!/bin/bash

pip install .[deploy]

rm -rf dist

python -m build

python -m twine upload dist/*
