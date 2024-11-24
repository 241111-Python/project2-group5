# Functionality for handling user input and presenting options

# Imports
from collections import defaultdict

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

    Returns:
        selection: user selection as int, or '-1' if invalid.
    """
    # List options
    print(f"\n{options_name}:")
    [print(f"{t[0]}). {t[1]}") for t in enumerate(options)]

    # Check selection
    selection = input("\nSelect option, or type 'x' to quit: ")
    if not process_input(selection, len(options)):
        return -1

    return int(selection)


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

        print(data[int(selection)])



def show_quality_entries(data):
    """Displays the quality of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.quality_score)) #

    avg_quality={country: sum(qualities) / len(qualities) for country, qualities in country_data.items()}

    print("\nAverage quality score from highest to lowest: ")
    for country, quality in avg_quality.items():
        print(f"{country}: {quality:.2f}")

def show_ripeness_entries(data):
    """Displays the ripeness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.ripeness_index)) #

    avg_ripeness_index={country: sum(ripeness) / len(ripeness) for country, ripeness in country_data.items()}

    print("\nAverage quality score from highest to lowest: ")
    for country, ripeness in avg_ripeness_index.items():
        print(f"{country}: {ripeness:.2f}")

def show_sugar_entries(data):
    """Displays the sugar content in of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.sugar_content_brix)) #

    avg_sugar={country: sum(sugar) / len(sugar) for country, sugar in country_data.items()}

    print("\nAverage sugar content from highest to lowest: ")
    for country, sugar in avg_sugar.items():
        print(f"{country}: {sugar:.2f}")

def show_firmness_entries(data):
    """Displays the firmness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.firmness_kgf)) #

    avg_firmness={country: sum(firmness) / len(firmness) for country, firmness in country_data.items()}

    print("\nAverage quality from highest to lowest: ")
    for country, firmness in avg_firmness.items():
        print(f"{country}: {firmness:.2f}")

def show_length_entries(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.length_cm)) #

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")