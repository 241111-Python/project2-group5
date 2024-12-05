# Project 2 - Global Analysis of Banana Quality and Characteristics

## Overview: 

An interactive Python project that analyzes a dataset of a sample of 1,000 bananas harvested from eight different countries across the world in 2023. The user can access statistics on an individual banana sample or a set of bananas sorted by selected criteria through a terminal-based interface. Users can also view summary statistics and examine correlations between pertinent variables in the dataset, such as the relationship between a banana’s physical characteristics and the environmental conditions in which it grew. In addition, the program generates an extended Markdown-style external report with graphs and informational tables presenting a comparison of bananas by origin and type. 

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

`-g` : Enables generation of graphs to `reports/` when running correlation analysis or producing external report.

`--auto path/to/source.csv` : Runs on provided dataset in non-interactive mode and exports analysis to `reports/`.

#### Known Issues

Related Issue: [#125235](https://github.com/python/cpython/issues/125235)

Currently there is a bug with Python 3.13 and the `tkinter` library in Windows that may prevent graph generation from functioning. The user may run the program without the `-g` flag if this occurs. Pre-generated figures are provided in the repository while this issue is being resolved.
