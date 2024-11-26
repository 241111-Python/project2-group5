# Functionality for handling user input and presenting options

# Imports
from collections import defaultdict
import numpy as np


def process_input(user_input: str, validation_range: int) -> bool:
    """Processes user input.

    Args:
        user_input: user command, either a number or 'x' to quit.
        validation_range: number of files or options.

    Returns:
        status: validity of input as boolean.
    """
    # Quit
    if user_input.lower() == "x":
        exit(0)

    # Check selection
    if not user_input.isnumeric() or int(user_input) not in range(0, validation_range):
        print("Error: Selection invalid.")
        return False

    return True


def present_options(options: list, options_name: str) -> int:
    """Presents a list of options to user.

    Args:
        options: list of strings representing possible options.
        options_name: describes the type of option.
    """
    # List options
    print(f"\n{options_name}:")
    [print(f"{t[0]}). {t[1]}") for t in enumerate(options)]


def select_option_or_quit(options: list, options_name: str) -> int:
    """Presents a list of options and asks user to select or quit out.

    Args:
        options: list of strings representing possible options.
        options_name: describes the type of option.

    Returns:
        selection: user selection as int.
    """
    # List options
    present_options(options, options_name)

    # Check selection
    while True:
        selection = input("\nSelect option, or type 'x' to quit: ")
        if process_input(selection, len(options)):
            return int(selection)


def print_entry(e):
    """Prints a banana object and header with short description.

    Args:
        e: Banana entry.
    """
    print(
        f"\n{e.quality_category} quality {e.ripeness_category} {e.variety} from {e.region}:")
    print(e)


def show_entry(data: list):
    """Displays a individual entry from data.

    Args:
        data: current data source.
    """
    while True:
        # Display data range and check user selection``
        selection = input(
            f"\nSelect an entry from: 0 - {len(data) - 1}, or type 'q' to return to main options: "
        )
        if selection == "q":
            break
        if not process_input(selection, len(data)):
            continue

        print_entry(data[int(selection)])


def show_best_worst(data: list):
    """Displays best and worst entries for a given attribute.

    Args:
        data: current data source.
    """

    attributes = [
        "quality_score",
        "ripeness_index",
        "sugar_content_brix",
        "firmness_kgf",
        "length_cm",
        "weight_g",
        "tree_age_years",
        "altitude_m",
        "rainfall_mm",
        "soil_nitrogen_ppm"
    ]

    while True:
        # Display possible attributes and check user selection
        present_options(attributes, "ATTRIBUTES")
        selection = input(
            f"\nSelect an attribute from: 0 - {len(attributes)}, or type 'q' to return to main options: "
        )
        if selection == "q":
            break
        if not process_input(selection, len(attributes)):
            continue

        # Sort data on attribute
        attrb = attributes[int(selection)]
        data_sorted = sorted(
            data, key=lambda x: getattr(x, attrb), reverse=True)

        # Top 3
        print(f"---TOP 3: ({attrb})---")
        for e in data_sorted[:3]:
            print_entry(e)

        # Worst 3
        print(f"\n---BOTTOM 3: ({attrb})---")
        for e in data_sorted[-3:]:
            print_entry(e)


def select_options_sorted(data):
    """Displays the sorted choices for bananas.

    Args:
        data: current data source.
    """

    options = [
        "Quality Bananas",
        "Most Ripe Bananas",  # Going to add category of ripeness to it soon
        "Sweetest Bananas",
        "Firmness of Bananas",
        "Longest Bananas"
    ]

    while True:
        present_options(options, "SELECT FROM THE LIST OF SORTED ANALYSIS - ")
        choice = int(input("\nSelect option, or type 'q' to go back: "))
        match choice:
            case 0:
                show_quality_entries(data)
            case 1:
                show_ripeness_entries(data)
            case 2:
                show_sugar_entries(data)
            case 3:
                show_firmness_entries(data)
            case 4:
                show_length_entries(data)
            case _:
                print(choice)
                pass

        if choice == 'q':
            break


def show_quality_entries(data):
    """Displays the quality of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.quality_score))

    avg_quality = {country: sum(qualities) / len(qualities)
                   for country, qualities in country_data.items()}

    print("\nAverage quality score from highest to lowest: ")
    for country, quality in avg_quality.items():
        print(f"{country}: {quality:.2f}")


def show_ripeness_entries(data):
    """Displays the ripeness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.ripeness_index))

    avg_ripeness_index = {country: sum(
        ripeness) / len(ripeness) for country, ripeness in country_data.items()}

    print("\nAverage quality score from highest to lowest: ")
    for country, ripeness in avg_ripeness_index.items():
        print(f"{country}: {ripeness:.2f}")


def show_sugar_entries(data):
    """Displays the sugar content in of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.sugar_content_brix))

    avg_sugar = {country: sum(sugar) / len(sugar)
                 for country, sugar in country_data.items()}

    print("\nAverage sugar content from highest to lowest: ")
    for country, sugar in avg_sugar.items():
        print(f"{country}: {sugar:.2f}")


def show_firmness_entries(data):
    """Displays the firmness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.firmness_kgf))

    avg_firmness = {country: sum(firmness) / len(firmness)
                    for country, firmness in country_data.items()}

    print("\nAverage quality from highest to lowest: ")
    for country, firmness in avg_firmness.items():
        print(f"{country}: {firmness:.2f}")


def show_length_entries(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.length_cm))

    avg_length = {country: sum(length) / len(length)
                  for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")


# Harvest_date - WORKING ON BY VITALI
# age of trees - WORKING ON BY VITALI
# altitude - WORKING ON BY VITALI
# Rainfall - WORKING ON BY VITALI
# soil nitrogen per ppm - WORKING ON BY VITALI

# def show_harvest_date(data):
#     """Displays the length of banana based off the region from top to bottom.

#     Args:
#         data: current data source.
#     """
#     country_data=defaultdict(list)

#     for r in data:
#         country_data[r.region].append(float(r.harvest_date)) #

#     avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

#     print("\nAverage length from highest to lowest: ")
#     for country, length in avg_length.items():
#         print(f"{country}: {length:.2f}")

def show_tree_age_years(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.tree_age_years))

    avg_length = {country: sum(length) / len(length)
                  for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")


def show_altitude_m(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.altitude_m))

    avg_length = {country: sum(length) / len(length)
                  for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")


def show_rainfall_mm(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.rainfall_mm))

    avg_length = {country: sum(length) / len(length)
                  for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")


def show_soil_nitrogen_ppm(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.soil_nitrogen_ppm))

    avg_length = {country: sum(length) / len(length)
                  for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")


def filtered_entries(data, attribute, order='asc'):

    invalid_attributes = {"quality_category",
                          "harvest_date", "ripeness_category", "variety"}
    if attribute in invalid_attributes:
        print(f"Invalid attribute '{attribute}'.")
        return

    country_data = defaultdict(list)
    for item in data:
        value = float(getattr(item, attribute))
        country_data[item.region].append(value)

    avg_attribute = {country: sum(values) / len(values)
                     for country, values in country_data.items()}

    if (order == 'asc'):
        sorted_avg_attribute = sorted(
            avg_attribute.items(), key=lambda x: x[1])
        print(
            f"\nAverage {attribute.replace('_', ' ').capitalize()} from lowest to highest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")
    else:
        sorted_avg_attribute = sorted(
            avg_attribute.items(), key=lambda x: x[1], reverse=True)
        print(
            f"\nAverage {attribute.replace('_', ' ').capitalize()} from highest to lowest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")


def length_weight(data, attribute, sort_by='value'):
    grouped_data = defaultdict(list)

    for item in data:
        key = getattr(item, attribute)
        value = item.length_cm / item.weight_g
        grouped_data[key].append(value)

    group = {group: sum(value) / len(value)
             for group, value in grouped_data.items()}
    values = {}
    if sort_by == 'value':
        values = sorted(group.items(), key=lambda x: x[1])
    elif sort_by == 'group':
        values = sorted(group.items(), key=lambda x: x[0])

    print(f"\nAverage Length/Weight grouped by {attribute.replace('_', ' ')}:")
    for group, avg_ratio in values:
        print(f"{group}: {avg_ratio:.4f}")


def corelation_numpy(data, attribute1, attribute2):
    data_a = [getattr(item, attribute1) for item in data]
    data_b = [getattr(item, attribute2) for item in data]

    correlation_coefficient = np.corrcoef(data_a, data_b)[0, 1]
    print(
        f"Correlation between {attribute1.replace('_', ' ')} and {attribute2.replace('_', ' ')}: {correlation_coefficient:.4f}")
    # return correlation_coefficient


def corelation_by_group(data, attribute1, attribute2, group_by):
    group_data = defaultdict(list)
    for item in data:
        # print(item)
        # key = getattr(item, attribute1)
        # key2 = getattr(item, attribute2)

        # key = list(getattr(item, attr) for attr in group_by)
        key = getattr(item, group_by)

        group_data[key].append(item)
    # print(group_data)
    # conclusions:
    i = 1
    print(f"""\nCorrelation coefficient ranges from -1 to 1:
         1: Perfect positive correlation (as one variable increases, the other increases).
        -1: Perfect negative correlation (as one variable increases, the other decreases).
         0: No correlation (no discernible relationship between the variables).
    \nCorelation by {group_by}\n""")
    for key, items in group_data.items():
        data_a = [getattr(item, attribute1) for item in items]
        data_b = [getattr(item, attribute2) for item in items]
        correlation_coefficient = np.corrcoef(data_a, data_b)[0, 1]
        # print(f"Group by {group_by}: {key} ==> Correlation between {attribute1} and {attribute2}: {correlation_coefficient:.4f}")
        print(f"{i}. {key} ==> Correlation between {attribute1.replace('_', ' ').capitalize()} and {attribute2.replace('_', ' ').capitalize()}: {correlation_coefficient:.4f}")
        i+=1
        if correlation_coefficient > 0.7:
                conclusion = "Strong positive correlation."
        elif 0.3 <= correlation_coefficient <= 0.7:
                conclusion = "Moderate positive correlation."
        elif 0 <= correlation_coefficient < 0.3:
                conclusion = "Weak positive correlation."
        elif -0.3 <= correlation_coefficient < 0:
                conclusion = "Weak negative correlation."
        elif -0.7 <= correlation_coefficient < -0.3:
                conclusion = "Moderate negative correlation."
        elif correlation_coefficient < -0.7:
                conclusion = "Strong negative correlation."
        else:
                conclusion = "No discernible correlation."

        print(f"   Conclusion: {conclusion}\n")

# def corelation(data, attribute1, attribute2):
    # data_a = [getattr(item, attribute1) for item in data]
    # data_b = [getattr(item, attribute2) for item in data]

#     #mean = sum/len
#     mean_a = sum(data_a)/len(data_a)
#     mean_b = sum(data_b)/len(data_b)
