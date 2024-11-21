# Functionality for handling user input and presenting options


def process_input(user_input, validation_range):
    """Processes user input.

    Args:
        user_input: user command, either a number or 'x' to quit.
        validation_range: number of files or options.

    Returns:
        status: validity of input.
    """
    # Quit
    if user_input.lower() == "x":
        exit(0)

    # Check selection
    if not user_input.isnumeric() or int(user_input) not in range(0, validation_range):
        print("Error: Selection invalid.")
        return False

    return True


def present_options(options, options_name) -> int:
    """Presents a list of options to user.

    Args:
        options: list of strings representing possible options.
        options_name: describe the type of option

    Returns:
        selection: user selection, or '-1' if invalid
    """
    # List options
    print(f"\n{options_name}:")
    [print(f"{t[0]}). {t[1]}") for t in enumerate(options)]

    # Check selection
    selection = input("\nSelect option, or type 'x' to quit: ")
    if not process_input(selection, len(options)):
        return -1

    return int(selection)
