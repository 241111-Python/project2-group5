# Project 2, Group 5
# Interactive Terminal

# Imports
import os
from app import library


def process_input(user_input, validation_range):
    """Processes user input.

    Args:
        user_input: user command, either a number or 'x' to quit.
        validation_range: number of files or options

    Returns:
        status: validity of input
    """
    # Quit
    if user_input.lower() == "x":
        loop_flag = False
        exit(0)

    # Check selection
    if not user_input.isnumeric() or int(user_input) not in range(1, validation_range):
        print("Selection invalid.")
        return False

    return True


def main():
    # Process user input

    # Options
    # Select and read in the data file
    # View an individual entry
    # View a sorted or filtered set of data

    loop_flag = True
    data_dir = "data"
    data = None

    while loop_flag:
        # No data selected
        if not data:
            # List files from data directory
            data_files = os.listdir(data_dir)
            print("\nFILES:")
            [print("{}). {}".format(t[0] + 1, t[1])) for t in enumerate(data_files)]
            print()

            # Check selection
            selection = input("Select datasource, or type x to quit: ")
            if not process_input(selection, len(data_files) + 1):
                continue

            # Verify file
            source_file = os.path.join(data_dir, data_files[int(selection) - 1])
            if not os.path.exists(source_file):
                print("File not found.")
                continue
            if not source_file.endswith(".csv"):
                print("File not valid.")
                continue

            # Read in data
            data = library.read_csv(source_file)
            continue

        # Options menu
        print("\nOPTIONS:")
        print("1). Unload data")

        # Check selection
        selection = input("Select option, or type x to quit: ")
        if not process_input(selection, 3):
            continue

        # Execute option
        match selection:
            case "1":
                data = None  # unload source
                print("Unloaded source. Please select a new file.")
            case _:
                # default
                pass


if __name__ == "__main__":
    main()
