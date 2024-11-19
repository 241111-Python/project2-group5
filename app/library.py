# Functionality for reading, parsing, and presenting data

# Imports
import csv


def read_csv(file_name):
    """Reads csv file and converts into a list of dictionaries, each representing an entry.

    Args:
        file_name: name of the csv file

    Returns:
        data: csv converted into list structure
    """
    try:
        with open(file_name, "r") as file:
            data = list(csv.DictReader(file))
    except Exception as e:
        print("Error:", e)
        return

    return data
