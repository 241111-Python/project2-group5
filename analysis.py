# Generates analysis of dataset in a report style
# Which can be viewed either in terminal or as a markdown file

# Imports
import os, sys
from mdprint import mdprint
from itertools import groupby  # , tee
import statistics as stats
from tabulate import tabulate
import view
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# May need to point to TCL due to current bug with Python 3.13
if sys.version_info.minor == 13:
    os.environ["TCL_LIBRARY"] = r"C:\Program Files\Python313\tcl\tcl8.6"

report_folder = "reports"
figures_folder = os.path.join(report_folder, "figures")


def generate_ranking(f, data: list, indices: list, values: list):
    """Generates a table ranking the dataset by a selected column.

    Args:
        f: file to write out to.
        data: current data source.
        indices: category or categories for table index.
        values: columns to include, table is sorted by first value descending.
    """
    # Sort data by desired group
    dataset = sorted(data, key=lambda x: [getattr(x, i) for i in indices])

    # Group data and get average of desired value
    ranking = []
    for key, group in groupby(dataset, lambda x: [getattr(x, i) for i in indices]):
        # Ignore group if it makes up 1% of data or less
        # iter_1, iter_2 = tee(group)
        # if (len(list(iter_1))) <= (len(data) * 0.01):
        #     continue

        # Calculate column value and append to current row
        entry = [key]
        columns = [[] for _ in range(len(values))]

        for b in group:
            for i, v in enumerate(values):
                columns[i].append(getattr(b, v))

        for e in columns:
            entry.append(round(stats.mean(e), 2))

        ranking.append(entry)

    # Print ranking in markdown format
    ranking.sort(key=lambda x: x[1], reverse=True)
    mdprint(f"Ranking {indices} by avg {values[0]}\n", heading=3, file=f)
    mdprint(
        tabulate(ranking, headers=["Type", *values], tablefmt="github"),
        file=f,
    )
    mdprint("\n", file=f)

    # Print best country for each variety
    if indices == ["region", "variety"]:
        var_set = set()
        best_country_for_var = []

        for r in ranking:
            if r[0][1] not in var_set:
                var_set.add(r[0][1])
                best_country_for_var.append((r[0][1], r[0][0]))

        mdprint("Best Country for each Variety\n", heading=3, file=f)
        mdprint(
            tabulate(
                best_country_for_var,
                headers=["Variety", "Best Country"],
                tablefmt="github",
            ),
            file=f,
        )
        mdprint("\n", file=f)


def generate_count(f, data: list):
    """Generates a table with counts/percents for each category.

    Args:
        f: file to write out to.
        data: current data source.
    """
    # Sort data by desired group
    dataset = sorted(data, key=lambda x: getattr(x, "region"))

    # Group data and get count
    ranking = []
    for key, group in groupby(dataset, key=lambda x: getattr(x, "region")):
        # Calculate column value and append to current row
        e = [key, 0, 0, 0, 0]

        for b in group:
            match b.quality_category:
                case "Premium":
                    e[1] += 1
                case "Good":
                    e[2] += 1
                case "Processing":
                    e[3] += 1
                case "Unripe":
                    e[4] += 1

        ranking.append(e)

    # Convert to percents
    for r in ranking:
        sum_b = sum(r[1:])
        for i in range(4):
            r[i + 1] = f"{round((r[i+1] / sum_b) * 100, 1)}%"

    # Print ranking in markdown format
    ranking.sort(key=lambda x: [x[1], x[2]], reverse=True)
    mdprint(f"Percent of Quality Bananas for each Country\n", heading=3, file=f)
    mdprint(
        tabulate(
            ranking,
            headers=["Quality", "Premium", "Good", "Processing", "Unripe"],
            tablefmt="github",
        ),
        file=f,
    )
    mdprint("\n", file=f)


def generate_correlations(
    f, data: pd.DataFrame, figures: str, filter_by: tuple, graph: bool = False
):
    """Generates a correlations table.

    Args:
        f: file to write out to.
        data: current data source.
        figures: path of where to output figures if graphing is enabling.
        filter_by: tuple containing column and value to filter dataset by.
        graph: option to output graphs.
    """
    # Filter
    data = data.loc[data[filter_by[0]] == filter_by[1]]

    # Get correlation table
    corr = data.corr(numeric_only=True)

    # Generate basic markdown
    corr.columns = [col[:8] for col in corr.columns]
    mdprint("\n", file=f)
    mdprint(
        f"Correlations for Bananas of {filter_by[0]}: {filter_by[1]}", heading=3, file=f
    )
    mdprint(corr.round(2).to_markdown(), file=f)

    if graph:
        # Generate heatmap
        graph_file_path = os.path.join(
            figures, f"heatmap_{' '.join(filter_by).replace(' ', '_')}.png"
        )
        sns.heatmap(corr, annot=True, fmt=".2f", cbar=False)
        plt.title(
            f"Correlations for {filter_by[0]}: {filter_by[1]} Bananas, n = {data.shape[0]}"
        )
        plt.tight_layout()
        plt.savefig(graph_file_path)
        plt.close()
        mdprint(
            f"\n![title](/{graph_file_path})".replace("\\", "/"),
            file=f,
        )


def generate_analysis(data: list, dataset_name: str, graph: bool = False):
    """Generates analysis containing tables and graphs in markdown format.

    Args:
        data: current data source.
        dataset_name: file name of dataset.
        graph: option to output graphs.
    """
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
            "Statistics for Banana Quality and Characteristics\n", heading=1, file=f
        )

        # Date
        now = datetime.datetime.now()
        mdprint(f"Generated at {now.strftime('%H:%M:%S %Y-%m-%d')}\n", file=f)

        # Section 1
        mdprint("Comparison of Bananas by Origin and Variety\n", heading=2, file=f)
        for i in [["variety"], ["region", "variety"]]:
            generate_ranking(
                f,
                data,
                i,
                [
                    "quality_score",
                    "ripeness_index",
                    "sugar_content_brix",
                    "firmness_kgf",
                    "length_cm",
                    "weight_g",
                ],
            )

        generate_count(f, data)

        # Section 2
        mdprint("\n", file=f)
        mdprint(
            "Relationships Between Banana Characteristics and Environment\n\n",
            heading=2,
            file=f,
        )
        for i in [["region"], ["quality_category"]]:
            generate_ranking(
                f,
                data,
                i,
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
            generate_correlations(f, df, new_figs, ("variety", v), graph)

    print(f"Report generated in {new_report}")


def display_report():
    """Prints out selected report in the terminal."""

    # Check reports exist
    if not os.path.exists(report_folder):
        print("\nError: No reports exist.")
        return

    while True:
        # List files from report directory
        data_files = []
        for file in os.listdir(report_folder):
            p = os.path.join(report_folder, file)
            if not os.path.isdir(p):
                data_files.append(file)

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
