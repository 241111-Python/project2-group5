# Generates analysis of dataset in a report style
# Which can be viewed either in terminal or as a markdown file

# Imports

import os
from mdprint import mdprint
from itertools import groupby
import statistics as stats
from tabulate import tabulate
import view

report_folder = "reports"


def generate_ranking(f, data: list, index: str, values: list):
    # Sort data by desired group
    dataset = sorted(data, key=lambda x: getattr(x, index))

    # Group data and get average of desired value
    ranking = []
    for key, group in groupby(dataset, lambda x: getattr(x, index)):
        entry = [key]
        elements = [[] for _ in range(len(values))]

        for b in group:
            for i, v in enumerate(values):
                elements[i].append(getattr(b, v))

        for e in elements:
            entry.append(round(stats.mean(e), 2))

        ranking.append(entry)

    # Print ranking in markdown format
    ranking.sort(key=lambda x: x[1], reverse=True)
    mdprint(f"Ranking of {index}s\n", heading=3, file=f)
    mdprint(
        tabulate(ranking, headers=[index, *values], tablefmt="github"),
        file=f,
    )
    mdprint("\n", file=f)


def generate_analysis(data: list, dataset_name):
    # Create reports folder
    if not os.path.exists("reports"):
        os.makedirs("reports")
        print("Created reports folder.")

    new_report = os.path.join(report_folder, f"report_{dataset_name.split('.')[0]}.md")

    # Clear old report
    if os.path.exists(new_report):
        os.remove(new_report)
        print("Cleaning existing report.")

    # Print analysis to markdown file
    with open(new_report, "x") as f:
        mdprint(
            "Global Analysis of Banana Quality and Characteristics\n", heading=1, file=f
        )
        mdprint("Comparison of Bananas by Origin and Type\n", heading=2, file=f)

        generate_ranking(f, data, "region", ["quality_score", "ripeness_index"])

    print(f"Report generated in {new_report}")


def display_report():
    if not os.path.exists(report_folder):
        print("\nError: No reports exists.")
        return

    while True:
        # List files from report directory
        data_files = os.listdir(report_folder)
        view.present_options(data_files, "FILES")

        # check user selection
        selection = input(
            f"\nSelect an entry from: 0 - {len(data_files) - 1}, or type 'q' to return to main options: "
        )
        if selection == "q":
            break
        if not view.process_input(selection, len(data_files)):
            continue

        # Show report in terminal
        print()
        with open(os.path.join(report_folder, data_files[int(selection)]), "r") as f:
            print(*[row for row in f.readlines()])
