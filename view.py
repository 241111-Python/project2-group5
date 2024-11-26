# Functionality for handling user input and presenting options

# Imports
from collections import defaultdict
from tabulate import tabulate
from datetime import datetime
import numpy as np

################################################################################################################### 
# MENU SECTION START
################################################################################################################### 

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
    print(f"\n{e.quality_category} quality {e.ripeness_category} {e.variety} from {e.region}:")
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
        data_sorted = sorted(data, key=lambda x: getattr(x, attrb), reverse=True)

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
        "Highest Quality",              # 0
        "Most Ripe",                    # 1
        "Sweetest",                     # 2
        "Firmness",                     # 3
        "Longest",                      # 4
        "Heaviest",                     # 5
        "Oldest Harvest Date",          # 6
        "Oldest Tree Age",              # 7 
        "Altitude",                     # 8
        "Rainfall amount",              # 9
        "Nitrogen in Soil"              # 10
    ]

    while True:
        present_options(options, "SELECT FROM THE LIST OF SORTED ANALYSIS - ")
        choice = int(input("\nSelect option, or type 'q' to go back: "))
        match choice:
            case 0: # 
                show_highest_quality_entries(data)
            case 1: # 
                show_highest_ripeness_entries(data)
            case 2:
                show_highest_sweetness_entries(data)
            case 3:
                show_highest_firmness_entries(data)
            case 4:
                show_highest_length_entries(data)
            case 5:
                show_highest_weight_entries(data)
            case 6:
                show_oldest_harvest_entries(data)
            case 7:
                show_oldest_age_entries(data)
            case 8:
                show_highest_altitude_entries(data)
            case 9:
                show_highest_rainfall_entries(data)
            case 10:
                show_highest_nitrogen_entries(data)
            case _:
                print(choice)     
                pass

        if choice == 'q':
            break

def select_options_filtered(data):
    """Displays the filtered and more advanced sorted choices for bananas.

    Args:
        data: current data source.
    """
    options = [
        "Average quality of bananas",
        "Average of ripe bananas", # Going to add category of ripeness to it soon
        "Average of sweetest bananas",
        "Average firmness of bananas",
        "Average of the longest bananas"
    ]
    while True:
        present_options(options, "SELECT FROM THE LIST OF SORTED ANALYSIS - ")
        choice = int(input("\nSelect option, or type 'q' to go back: "))
        match choice:
            case 0: # Quality
                show_filtered_quality_entries(data)
            case 1: # 
                show_filtered_ripeness_entries(data)
            case 2:
                show_filtered_sugar_entries(data)
            case 3:
                show_filtered_firmness_entries(data)
            case 4:
                show_filtered_length_entries(data)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case _:
                print(choice)     
                pass

        if choice == 'q':
            break


def select_options_comprehensive(data):
    print("placeholder")


def convert_object_to_list(data): # Converts objects to List of dictionaries 
    dataList = [
    {
        "Sample": banana.sample,
        "Variety": banana.variety,
        "Region": banana.region,
        "Quality Score": banana.quality_score,
        "Category": banana.quality_category,
        "Ripeness Index": banana.ripeness_index,
        "Ripeness Category": banana.ripeness_category,
        "Sugar (brix)": banana.sugar_content_brix,
        "Firmness (kgf)": banana.firmness_kgf,
        "Length (cm)": banana.length_cm,
        "Weight (g)": banana.weight_g,
        "Harvest Date": banana.harvest_date,
        "Tree Age (years)": banana.tree_age_years,
        "Altitude (m)": banana.altitude_m,
        "Rainfall (mm)": banana.rainfall_mm,
        "Soil Nitrogen (ppm)": banana.soil_nitrogen_ppm,
    }
    for banana in data
    ]

    return dataList


################################################################################################################### 
# MENU SECTION END
################################################################################################################### 

################################################################################################################### 
# SORTED SECTION START
################################################################################################################### 

def show_highest_quality_entries(data): # Highest Quality
    """Displays all entries based off the quality of banana.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedQuality=sorted(dataList, key=lambda x: x["Quality Score"], reverse=True)
    print(tabulate(sortedQuality, headers="keys" , tablefmt="rounded_outline"))


def show_highest_ripeness_entries(data): # Most Ripe
    """Displays all entries based off the ripeness of banana .

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data) 
    sortedRipeness=sorted(dataList, key=lambda x: x["Ripeness Index"], reverse=True)
    print(tabulate(sortedRipeness, headers="keys" , tablefmt="rounded_outline"))

def show_highest_sweetness_entries(data): # Sweetest
    """Displays all entries based off the ripeness of banana .

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedSweetness=sorted(dataList, key=lambda x: x["Sugar (brix)"], reverse=True)
    print(tabulate(sortedSweetness, headers="keys" , tablefmt="rounded_outline"))


def show_highest_firmness_entries(data): # Firmness
    """Displays all entries based off the firmness of banana.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedFIrmness=sorted(dataList, key=lambda x: x["Firmness (kgf)"], reverse=True)
    print(tabulate(sortedFIrmness, headers="keys" , tablefmt="rounded_outline"))

def show_highest_length_entries(data): # Longest
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedLength=sorted(dataList, key=lambda x: x["Length (cm)"], reverse=True)
    print(tabulate(sortedLength, headers="keys" , tablefmt="rounded_outline"))

def show_highest_weight_entries(data): # Heaviest
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedWeight=sorted(dataList, key=lambda x: x["Weight (g)"], reverse=True)
    print(tabulate(sortedWeight, headers="keys" , tablefmt="rounded_outline"))

def show_oldest_harvest_entries(data): # Heaviest
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedDate=sorted(dataList, key=lambda x: datetime.strptime(x["Harvest Date"], "%Y-%m-%d"))
    print(tabulate(sortedDate, headers="keys" , tablefmt="rounded_outline"))

def show_oldest_age_entries(data): # oldest tree age
    """Displays all entries based off the age of the banana tree top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedAge=sorted(dataList, key=lambda x: x["Tree Age (years)"], reverse=True)
    print(tabulate(sortedAge, headers="keys" , tablefmt="rounded_outline"))

def show_highest_altitude_entries(data): # highest altitude
    """Displays all entries based off the altitude top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedAltitude=sorted(dataList, key=lambda x: x["Altitude (m)"], reverse=True)
    print(tabulate(sortedAltitude, headers="keys" , tablefmt="rounded_outline"))

def show_highest_rainfall_entries(data): # Most rainfall in region
    """Displays all entries based off the rainfall from top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedRainfall=sorted(dataList, key=lambda x: x["Rainfall (mm)"], reverse=True)
    print(tabulate(sortedRainfall, headers="keys" , tablefmt="rounded_outline"))



def show_highest_nitrogen_entries(data): # Most Nitrogen in soil
    """Displays all entries based off the nitrogen of soil top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedNitrogen=sorted(dataList, key=lambda x: x["Soil Nitrogen (ppm)"], reverse=True)
    print(tabulate(sortedNitrogen, headers="keys" , tablefmt="rounded_outline"))

################################################################################################################### 
# SORTED SECTION END
################################################################################################################### 


################################################################################################################### 
# FILTERED SECTION START
################################################################################################################### 

def show_filtered_quality_entries(data):
    """Displays the quality of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.quality_score)) #

    avg_quality={country: sum(qualities) / len(qualities) for country, qualities in country_data.items()}
    sortQuality=sorted(avg_quality.items(), key=lambda x: x[1], reverse=True)

    print("\nAverage quality score from highest to lowest: ")
    print(tabulate(sortQuality, ["Country", "Quality Score"], tablefmt="rounded_outline"))

def show_filtered_ripeness_entries(data):
    """Displays the ripeness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.ripeness_index)) #

    avg_ripeness_index={country: sum(ripeness) / len(ripeness) for country, ripeness in country_data.items()}
    sortRipeness=sorted(avg_ripeness_index.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage ripeness index from highest to lowest: ")   
    print(tabulate(sortRipeness, ["Country", "Ripeness Index (brix)"], tablefmt="rounded_outline"))


def show_filtered_sugar_entries(data):
    """Displays the sugar content in of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.sugar_content_brix)) #

    avg_sugar={country: sum(sugar) / len(sugar) for country, sugar in country_data.items()}
    sortSugar=sorted(avg_sugar.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage sugar content from highest to lowest: ")
    print(tabulate(sortSugar, ["Country", "Sugar Content (brix)"], tablefmt="rounded_outline"))


def show_filtered_firmness_entries(data):
    """Displays the firmness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.firmness_kgf)) #

    avg_firmness={country: sum(firmness) / len(firmness) for country, firmness in country_data.items()}
    sortFirmness=sorted(avg_firmness.items(), key=lambda x: x[1], reverse=True)

    print("\nAverage firmness from highest to lowest: ")
    print(tabulate(sortFirmness, ["Country", "Firmness (kgf)"], tablefmt="rounded_outline"))


def show_filtered_length_entries(data):
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.length_cm))

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}
    sortLength=sorted(avg_length.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage length from highest to lowest: ")
    print(tabulate(sortLength, ["Country", "Length (cm)"], tablefmt="rounded_outline"))


################################################################################################################### 
# FILTERED SECTION END
################################################################################################################### 


################################################################################################################### 
# COMPREHENSIVE SECTION START
################################################################################################################### 


################################################################################################################### 
# COMPREHENSIVE SECTION END
################################################################################################################### 
 
        
def show_tree_age_years(data): # Vitali
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.tree_age_years)) #

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")
        
def show_altitude_m(data): #Vitali
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.altitude_m)) #

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")
        
        
def show_rainfall_mm(data): #Vitali
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.rainfall_mm)) #

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")
        
        
def show_soil_nitrogen_ppm(data): # Vitali
    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.soil_nitrogen_ppm)) #

    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}

    print("\nAverage length from highest to lowest: ")
    for country, length in avg_length.items():
        print(f"{country}: {length:.2f}")        

def filtered_entries(data, attribute, order='asc'): #Vitali

    invalid_attributes = {"quality_category", "harvest_date", "ripeness_category", "variety"}
    if attribute in invalid_attributes:
        print(f"Invalid attribute '{attribute}'.")
        return

    country_data = defaultdict(list)
    for item in data:
        value = float(getattr(item, attribute))
        country_data[item.region].append(value)


    avg_attribute = {country: sum(values) / len(values) for country, values in country_data.items()}

    if (order == 'asc'):
        sorted_avg_attribute = sorted(avg_attribute.items(), key=lambda x: x[1])
        print(f"\nAverage {attribute.replace('_', ' ')} from lowest to highest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")
    else:
        sorted_avg_attribute = sorted(avg_attribute.items(), key=lambda x: x[1], reverse=True)
        print(f"\nAverage {attribute.replace('_', ' ')} from highest to lowest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")
            
def length_weight(data,attribute,sort_by='value'): #Vitali
    grouped_data = defaultdict(list)
    
    for item in data:
        key = getattr(item, attribute) 
        value = item.length_cm / item.weight_g  
        grouped_data[key].append(value)
    
    group = {group: sum(value) / len(value) for group, value in grouped_data.items()}
    values = {}
    if sort_by == 'value':
        values = sorted(group.items(), key=lambda x: x[1])
    elif sort_by == 'group':
        values = sorted(group.items(), key=lambda x: x[0])
    
    print(f"\nAverage Length/Weight grouped by {attribute.replace('_', ' ')}:")
    for group, avg_ratio in values:
        print(f"{group}: {avg_ratio:.4f}")



def corelation_numpy(data, attribute1, attribute2): #Vitali
    data_a = [getattr(item, attribute1) for item in data]
    data_b = [getattr(item, attribute2) for item in data]
    
    correlation_coefficient = np.corrcoef(data_a, data_b)[0, 1]
    print(f"Correlation between {attribute1} and {attribute2}: {correlation_coefficient:.4f}")
    # return correlation_coefficient

# def corelation(data, attribute1, attribute2):
    # data_a = [getattr(item, attribute1) for item in data]
    # data_b = [getattr(item, attribute2) for item in data]
              
#     #mean = sum/len
#     mean_a = sum(data_a)/len(data_a)
#     mean_b = sum(data_b)/len(data_b)
    
    