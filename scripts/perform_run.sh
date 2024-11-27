#!/bin/bash

# Selects a default dataset if no path supplied
DATASET=${1:-"data/banana_quality_dataset_SMALL.csv"}

# Creates virtual environment if it does not exist
if [ ! -d ".env" ]; then
    python3 -m venv .env &&
        source .env/bin/activate &&
        pip3 install -r requirements.txt
fi

# Generates analysis for given dataset
source .env/bin/activate &&
    python3 run.py --auto "$DATASET"
