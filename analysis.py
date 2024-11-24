# Generates analysis of dataset in a report style
# Which can be viewed either in terminal or as a markdown file

# Imports
import os
from mdprint import mdprint
from itertools import groupby, tee
import statistics as stats
from tabulate import tabulate
import view
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Need to point to TCL due to current bug with Python 3.13
os.environ["TCL_LIBRARY"] = r"C:\Program Files\Python313\tcl\tcl8.6"

report_folder = "reports"
figures_folder = "figures"


def generate_ranking(f, data: list, indices: list, values: list):
    # Sort data by desired group
    dataset = sorted(data, key=lambda x: [getattr(x, i) for i in indices])

    # Group data and get average of desired value
    ranking = []
    for key, group in groupby(dataset, lambda x: [getattr(x, i) for i in indices]):
        # Ignore group if it makes up 1% of data or less
        iter_1, iter_2 = tee(group)
        # if (len(list(iter_1))) <= (len(data) * 0.01):
        #     continue

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
    mdprint(f"Ranking {indices} by {values[0]}\n", heading=3, file=f)
    mdprint(
        tabulate(ranking, headers=["Type", *values], tablefmt="github"),
        file=f,
    )
    mdprint("\n", file=f)


def generate_correlations(
    f, data: pd.DataFrame, figures: str, variety: str, region: str
):
    # Filter
    data = data.loc[data["variety"] == variety]
    # data = data.loc[data['region'] == region]

    file_path = os.path.join(figures, f"heatmap_{variety.replace(" ", "_")}.png")

    # Generate heatmap
    corr = data.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cbar=False)
    plt.title(f"Correlations for {variety} Bananas")
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()

    # Generate basic markdown
    corr.columns = [col[:8] for col in corr.columns]
    mdprint("\n", file=f)
    mdprint(f"Correlations for {variety} Bananas", heading=3, file=f)
    mdprint(corr.round(2).to_markdown(), file=f)
    mdprint(
        f"\n![title](..\\{file_path})",
        file=f,
    )


def generate_analysis(data: list, dataset_name):
    # Build paths
    new_report = os.path.join(report_folder, f"report_{dataset_name.split('.')[0]}.md")
    new_figs = os.path.join(figures_folder, f"figures_{dataset_name.split('.')[0]}")

    # Create reports and figures folders
    for f in [report_folder, figures_folder]:
        if not os.path.exists(f):
            os.makedirs(f)
            print(f"Created {f} folder.")
    if not os.path.exists(new_figs):
        os.makedirs(new_figs)

    # Clear old report
    if os.path.exists(new_report):
        os.remove(new_report)
        print("Cleaning existing report.")

    # Print analysis to markdown file

    with open(new_report, "x") as f:
        # Title
        mdprint(
            "Global Analysis of Banana Quality and Characteristics\n", heading=1, file=f
        )

        # Section 1
        mdprint("Comparison of Bananas by Origin and Type\n", heading=2, file=f)
        generate_ranking(
            f,
            data,
            ["region", "variety"],
            [
                "quality_score",
                "ripeness_index",
                "sugar_content_brix",
                "firmness_kgf",
                "length_cm",
                "weight_g",
            ],
        )

        # Section 2
        mdprint(
            "Relationship Between Environment and Banana Characteristics\n\n",
            heading=2,
            file=f,
        )
        generate_ranking(
            f,
            data,
            ["region"],
            ["altitude_m", "rainfall_mm", "soil_nitrogen_ppm", "tree_age_years"],
        )
        generate_ranking(
            f,
            data,
            ["quality_category"],
            [
                "quality_score",
                "altitude_m",
                "rainfall_mm",
                "soil_nitrogen_ppm",
                "tree_age_years",
            ],
        )
        df = pd.DataFrame([vars(d) for d in data])
        for v in df["variety"].unique():
            generate_correlations(f, df, new_figs, v, None)

    print(f"Report generated in {new_report}")


def display_report():
    # Check reports exist
    if not os.path.exists(report_folder):
        print("\nError: No reports exist.")
        return

    while True:
        # List files from report directory
        data_files = os.listdir(report_folder)

        # Don't list options if only one report exists
        if len(data_files) == 0:
            print("Error: No reports found in reports/")
            return
        if len(data_files) == 1:
            print()
            with open(os.path.join(report_folder, data_files[0]), "r") as f:
                print(*[row for row in f.readlines()])
            return

        view.present_options(data_files, "REPORTS")

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
