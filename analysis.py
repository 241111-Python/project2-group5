# Generates analysis of dataset in a report style
# Which can be viewed either in terminal or as a markdown file

# Imports

import os
from mdprint import mdprint
from itertools import groupby, tee
import statistics as stats
from tabulate import tabulate
import view

report_folder = "reports"


def generate_ranking(f, data: list, indices: list, values: list):
    # Sort data by desired group
    dataset = sorted(data, key=lambda x: [getattr(x, i) for i in indices])

    # Group data and get average of desired value
    ranking = []
    for key, group in groupby(dataset, lambda x: [getattr(x, i) for i in indices]):
        # Ignore group if it makes up 1.5% of data or less
        iter_1, iter_2 = tee(group)
        if (len(list(iter_1))) <= (len(data) * 0.015):
            continue

        # Calculate column value and append to current row
        entry = [key]
        columns = [[] for _ in range(len(values))]

        for b in iter_2:
            for i, v in enumerate(values):
                columns[i].append(getattr(b, v))

        for e in columns:
            entry.append(round(stats.mean(e), 2))

        ranking.append(entry)

    # Print ranking in markdown format
    ranking.sort(key=lambda x: x[1], reverse=True)
    mdprint(f"Ranking\n", heading=3, file=f)
    mdprint(
        tabulate(ranking, headers=["Type", *values], tablefmt="github"),
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

        generate_ranking(
            f,
            data,
            ["region", "variety"],
            ["quality_score", "ripeness_index", "sugar_content_brix"],
        )

    print(f"Report generated in {new_report}")


def display_report():
    if not os.path.exists(report_folder):
        print("\nError: No reports exists.")
        return

    while True:
        # List files from report directory
        data_files = os.listdir(report_folder)

        # Don't list options if only one report exists
        if len(data_files) == 1:
            print()
            with open(os.path.join(report_folder, data_files[0]), "r") as f:
                print(*[row for row in f.readlines()])
            return

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
