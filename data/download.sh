#!/usr/bin/env bash
mkdir -p html txt
python3 fetch.py --outdir html
python3 preprocess.py --indir html --outdir txt
python3 shuffle.py --indir txt --outdir .
