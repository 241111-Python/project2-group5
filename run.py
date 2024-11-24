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
            "Quality Bananas",
            "Most Ripe Bananas", # Going to add category of ripeness to it soon
            "Sweetest Bananas",
            "Firmness of Bananas",
            "Longest Bananas",
            "Generate analysis report",
            "View report"
        ]
        choice = view.select_option_or_quit(options, "OPTIONS")

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
                analysis.generate_analysis(data, source_file)
            case 8:
                analysis.display_report()
            case _:
                # default     
                pass


if __name__ == "__main__":
    main()
