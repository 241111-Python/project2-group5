#!/bin/bash

# Edit with your desired variables
USERNAME="YOUR_USERNAME"
DIR="/mnt/c/Users/$USERNAME/YOUR_PROJECT_FOLDER" # Absolute path where repo exists
DATASET="data/banana_quality_dataset.csv"

# Creates virtual environment if it does not exist
if [ ! -d ".env" ]; then
    cd $DIR/project2-group5 && python3 -m venv .env &&
        source .env/bin/activate &&
        pip3 install -r requirements.txt
fi

# Generates analysis for given dataset
cd $DIR/project2-group5 &&
    source .env/bin/activate &&
    python3 run.py --auto $DATASET
