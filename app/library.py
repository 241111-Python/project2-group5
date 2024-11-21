# Functionality for reading, parsing, and presenting data

# Imports
import csv
from app import model

def read_csv(file_name):
    """Reads csv file and converts into a list of dictionaries, each representing an entry.

    Args:
        file_name: name of the csv file

    Returns:
        data: csv converted into list of Banana objects
    """
    try:
        with open(file_name, "r") as file:
            raw_data = list(csv.DictReader(file))
    except Exception as e:
        print("Error:", e)
        return
    
    # Convert data to list of Banana objects
    return [model.Banana(**b) for b in raw_data]
