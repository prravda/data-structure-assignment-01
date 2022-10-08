#!/bin/bash
export PYTHONPATH="${PYTHONPATH}:/"
python3 -m unittest -v && python3 console_output.py