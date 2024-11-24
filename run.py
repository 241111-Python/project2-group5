# Project 2, Group 5
# Interactive Terminal

# Imports
import os
import library, view, analysis

def main():
    # Process user input

    # Options
    # Select and read in the data file
    # View an individual entry
    # View a sorted or filtered set of data

    data_dir = "data"
    data = None
    source_path = None

    while True:
        # No data selected
        if not data:
            # List files from data directory
            data_files = os.listdir(data_dir)

            # Check data exists in data folder
            if len(data_files) == 0:
                print("Error: No files found in data/")
                exit(0)

            choice = view.select_option_or_quit(data_files, "FILES")

            # Verify file selected
            source_path = os.path.join(data_dir, data_files[choice])
            if not os.path.exists(source_path):
                print("Error: File not found.")
                continue
            if not source_path.endswith(".csv"):
                print("Error: File not valid.")
                continue

            # Read in data
            data = library.read_csv(source_path)
            source_file = source_path.split(os.sep)[1]

        # Options menu
        options = [
            f"Unload data: {source_file}",
            "View individual entry",
            "View Sorted/Filtered Analysis",
            "View Comprehensive Analysis",
            "Generate analysis report",
            "View report"
        ]
        choice = view.select_option_or_quit(options, "OPTIONS")

        # Execute option
        match choice:
            case 0: 
                data = None  # unload source
                print("Unloaded source. Please select a new file.")
            case 1: # Shows individual entries based off __str__ method @ Banana class
                view.show_entry(data)
            case 2: # Shows filtered/sorted analysis
                view.select_options_sorted(data)
            case 3: # For the more advanced analysis 
                pass
            case 4:
                analysis.generate_analysis(data, source_file)
            case 5:
                analysis.display_report()
            case _:
                # default
                pass


if __name__ == "__main__":
    main()
