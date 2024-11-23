# Functionality for handling user input and presenting options

# Imports


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


def show_entry(data: list):
    """Displays a individual entry from data.

    Args:
        data: current data source.
    """
    while True:
        # Display data range and check user selection
        selection = input(
            f"\nSelect an entry from: 0 - {len(data) - 1}, or type 'q' to return to main options: "
        )
        if selection == "q":
            break
        if not process_input(selection, len(data)):
            continue

        print(data[int(selection)])
