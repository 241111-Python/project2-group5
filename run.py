# Project 2, Group 5
# Interactive Terminal

# Imports
import os
import library, view


def main():
    # Process user input

    # Options
    # Select and read in the data file
    # View an individual entry
    # View a sorted or filtered set of data

    data_dir = "data"
    data = None
    source_file = None

    while True:
        # No data selected
        if not data:
            # List files from data directory
            data_files = os.listdir(data_dir)
            choice = view.present_options(data_files, "DATASETS")
            if choice == -1:
                continue

            # Verify file selected
            source_file = os.path.join(data_dir, data_files[choice])
            if not os.path.exists(source_file):
                print("Error: File not found.")
                continue
            if not source_file.endswith(".csv"):
                print("Error: File not valid.")
                continue

            # Read in data
            data = library.read_csv(source_file)

        # Options menu
        options = [
            f"Unload data: {source_file.split("\\")[1]}",
            "View individual entry",
            "Quality Bananas",
            "Most Ripe Bananas", # Going to add category of ripeness to it soon
            "Sweetest Bananas",
            "Firmness of Bananas",
            "Longest Bananas",
        ]
        choice = view.present_options(options, "OPTIONS")
        if choice == -1:
            continue

        # Execute option
        match choice:
            case 0:
                data = None  # unload source
                print("Unloaded source. Please select a new file.")
            case 1:
                view.show_entry(data)
            case 2:
                view.show_quality_entries(data)
            case 3:
                view.show_ripeness_entries(data)
            case 4:
                view.show_sugar_entries(data)
            case 5:
                view.show_firmness_entries(data)
            case 6:
                view.show_length_entries(data)
            case 7:
                print("placeholder")
            case 8:
                print("placeholder")
            case 7:
                print("placeholder")
            case 8:
                print("placeholder")
            case _:
                # default     
                pass


if __name__ == "__main__":
    main()
