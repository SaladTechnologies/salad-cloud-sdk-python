#!/bin/bash

USE_VENV=0

for arg in "$@"
do
    case $arg in
        --use-venv)
        USE_VENV=1
        shift
        ;;
    esac
done

if [ "$USE_VENV" -eq 1 ]; then
    python -m venv .venv
    . .venv/bin/activate
fi

pip install build
python -m build --outdir dist .
pip install dist/salad_cloud_sdk-0.9.0-alpha.5-py3-none-any.whl --force-reinstall

if [ "$USE_VENV" -eq 1 ]; then
    deactivate
fi