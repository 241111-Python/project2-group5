# Project 2 - Global Analysis of Banana Quality and Characteristics

## Overview: 

An interactive Python project that analyzes a dataset of a sample of 1,000 bananas harvested from eight different countries across the world in 2023. The user can access statistics on an individual banana or a set of bananas filtered by selected criteria through a terminal-based interface. The program also generates a two-part report containing summary statistics and key facts about the data. The first section presents a comparison of bananas divided by origin and type. The second section investigates the relationship between a banana’s physical characteristics and environmental conditions, such as the level of rainfall it received.

## Usage
Setup project and virtual environment:

```
git clone https://github.com/241111-Python/project2-group5.git
python -m venv <venv>
source <venv>/Scripts/activate # bin/activate for Linux 
pip install -r requirements.txt
```

Run:

`python run.py`

Flags:

`-g` : Enables generation of graphs to `figures/` when producing report.

`--auto path/to/source.csv` : Runs on provided dataset in non-interactive mode and exports analysis to `reports/`.

#### Known Issues

Related Issue: [#125235](https://github.com/python/cpython/issues/125235)

Currently there is a bug with Python 3.13 and the `tkinter` library that may prevent the analysis report generation from functioning. The user may run the program without the `-g` flag if this occurs. A pre-generated report is provided in the repository while this issue is being resolved.
