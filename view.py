# Functionality for handling user input and presenting options

# Imports
from collections import defaultdict
from tabulate import tabulate
from datetime import datetime
import numpy as np4
import re
import matplotlib.pyplot as mplb


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
    print(
        f"\n{e.quality_category} quality {e.ripeness_category} {e.variety} from {e.region}:")
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
        data_sorted = sorted(
            data, key=lambda x: getattr(x, attrb), reverse=True)

        # Top 3
        print(f"---TOP 3: ({attrb})---")
        for e in data_sorted[:3]:
            print_entry(e)

        # Worst 3
        print(f"\n---BOTTOM 3: ({attrb})---")
        for e in data_sorted[-3:]:
            print_entry(e)


# Sorted bananas :) (Entire list)
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

    pattern =  r"^(10|[0-9])$"
    while True:
        present_options(options, "SELECT FROM THE LIST OF SORTED ANALYSIS - ")
        try:
            choice = int(input("\nSelect option, or type '-1' to go back: "))
            if(menu_range(choice, pattern)):
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
            else:
                raise ValueError
        except ValueError as e:
            print(f"Invalid entry of input! \n{e}")

# Filtered bananas (only select few~!!)
def select_options_filtered(data): 
    """Displays the filtered choices for bananas.

    Args:
        data: current data source.
    """
    options = [
        "Average quality of bananas",           # 0
        "Average ripesness of bananas",         # 1
        "Average sweetness bananas",            # 2
        "Average firmness of bananas",          # 3
        "Average length of bananas",            # 4
        "Average weight of bananas",            # 5
        "Average age of bananas",               # 6
        "Average altitude bananas grown",       # 7
        "Average rainfall of country",          # 8
        "Average nitrogen in soil"              # 9
    ]

    pattern = r"^[0-9]$"
    while True:
        present_options(options, "SELECT FROM THE LIST OF FILTERED ANALYSIS - ")
        try: 
            choice = int(input("\nSelect option, or type '-1' to go back: "))
            if(menu_range(choice, pattern)):
                match choice:
                    case 0: 
                        show_filtered_quality_entries(data)
                    case 1: 
                        show_filtered_ripeness_entries(data)
                    case 2:
                        show_filtered_sugar_entries(data)
                    case 3:
                        show_filtered_firmness_entries(data)
                    case 4:
                        show_filtered_length_entries(data)
                    case 5:
                        show_filtered_weight_entries(data)
                    case 6:
                        show_filtered_tree_age_years(data)
                    case 7:
                        show_filtered_altitude_m(data)
                    case 8:
                        show_filtered_rainfall_mm(data)
                    case 9:
                        show_filtered_soil_nitrogen_ppm(data)
                    case _:
                        print(choice)
                        pass
            else:
                raise ValueError
        except ValueError as e:
            print(f"Invalid entry of input! \n{e}")

def select_options_comprehensive(data):
    # select_options_filtered(data): 
    """Displays the filtered choices for bananas.

    Args:
        data: current data source.
    """
    # options = [
    #     "",            # 0
    #     "",            # 1
    #     "",            # 2
    #     ""             # 3
    # ]


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

def menu_range(val, pattern):       
    return bool(re.match(pattern,str(val)))

################################################################################################################### 
# MENU SECTION END
################################################################################################################### 

################################################################################################################### 
# SORTED SECTION START
################################################################################################################### 

def show_highest_quality_entries(data): # Highest Quality 0
    """Displays all entries based off the quality of banana.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedQuality=sorted(dataList, key=lambda x: x["Quality Score"], reverse=True)
    print(tabulate(sortedQuality, headers="keys" , tablefmt="rounded_outline"))


def show_highest_ripeness_entries(data): # Most Ripe 1
    """Displays all entries based off the ripeness of banana .

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data) 
    sortedRipeness=sorted(dataList, key=lambda x: x["Ripeness Index"], reverse=True)
    print(tabulate(sortedRipeness, headers="keys" , tablefmt="rounded_outline"))

def show_highest_sweetness_entries(data): # Sweetest 2
    """Displays all entries based off the ripeness of banana .

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedSweetness=sorted(dataList, key=lambda x: x["Sugar (brix)"], reverse=True)
    print(tabulate(sortedSweetness, headers="keys" , tablefmt="rounded_outline"))


def show_highest_firmness_entries(data): # Firmness 3
    """Displays all entries based off the firmness of banana.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedFIrmness=sorted(dataList, key=lambda x: x["Firmness (kgf)"], reverse=True)
    print(tabulate(sortedFIrmness, headers="keys" , tablefmt="rounded_outline"))

def show_highest_length_entries(data): # Longest 4
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedLength=sorted(dataList, key=lambda x: x["Length (cm)"], reverse=True)
    print(tabulate(sortedLength, headers="keys" , tablefmt="rounded_outline"))

def show_highest_weight_entries(data): # Heaviest 5
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedWeight=sorted(dataList, key=lambda x: x["Weight (g)"], reverse=True)
    print(tabulate(sortedWeight, headers="keys" , tablefmt="rounded_outline"))

def show_oldest_harvest_entries(data): # Heaviest 6
    """Displays all entries based off the length of banana top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedDate=sorted(dataList, key=lambda x: datetime.strptime(x["Harvest Date"], "%Y-%m-%d"))
    print(tabulate(sortedDate, headers="keys" , tablefmt="rounded_outline"))

def show_oldest_age_entries(data): # oldest tree age 7
    """Displays all entries based off the age of the banana tree top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedAge=sorted(dataList, key=lambda x: x["Tree Age (years)"], reverse=True)
    print(tabulate(sortedAge, headers="keys" , tablefmt="rounded_outline"))

def show_highest_altitude_entries(data): # highest altitude 8
    """Displays all entries based off the altitude top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedAltitude=sorted(dataList, key=lambda x: x["Altitude (m)"], reverse=True)
    print(tabulate(sortedAltitude, headers="keys" , tablefmt="rounded_outline"))

def show_highest_rainfall_entries(data): # Most rainfall in region 9
    """Displays all entries based off the rainfall from top to bottom.

    Args:
        data: current data source.
    """
    dataList=convert_object_to_list(data)
    sortedRainfall=sorted(dataList, key=lambda x: x["Rainfall (mm)"], reverse=True)
    print(tabulate(sortedRainfall, headers="keys" , tablefmt="rounded_outline"))



def show_highest_nitrogen_entries(data): # Most Nitrogen in soil 10
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
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.quality_score))

    avg_quality={country: sum(qualities) / len(qualities) for country, qualities in country_data.items()}
    sortQuality=sorted(avg_quality.items(), key=lambda x: x[1], reverse=True)


    print("\nAverage quality score: ")
    print(tabulate(sortQuality, ["Country", "Quality Score"], tablefmt="rounded_outline"))


def show_filtered_ripeness_entries(data):

    """Displays the ripeness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.ripeness_index))

    avg_ripeness_index={country: sum(ripeness) / len(ripeness) for country, ripeness in country_data.items()}
    sortRipeness=sorted(avg_ripeness_index.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage ripeness index: ")   
    print(tabulate(sortRipeness, ["Country", "Ripeness Index (brix)"], tablefmt="rounded_outline"))


def show_filtered_sugar_entries(data):

    """Displays the sugar content in of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.sugar_content_brix))


    avg_sugar={country: sum(sugar) / len(sugar) for country, sugar in country_data.items()}
    sortSugar=sorted(avg_sugar.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage sugar content: ")
    print(tabulate(sortSugar, ["Country", "Sugar Content (brix)"], tablefmt="rounded_outline"))


def show_filtered_firmness_entries(data):

    """Displays the firmness of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.firmness_kgf))

    avg_firmness={country: sum(firmness) / len(firmness) for country, firmness in country_data.items()}
    sortFirmness=sorted(avg_firmness.items(), key=lambda x: x[1], reverse=True)

    print("\nAverage firmness: ")
    print(tabulate(sortFirmness, ["Country", "Firmness (kgf)"], tablefmt="rounded_outline"))



def show_filtered_length_entries(data):

    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.length_cm))



    avg_length={country: sum(length) / len(length) for country, length in country_data.items()}
    sortLength=sorted(avg_length.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage length: ")
    print(tabulate(sortLength, ["Country", "Length (cm)"], tablefmt="rounded_outline"))

def show_filtered_weight_entries(data):
    """Displays the length of banana based off the region from top to bottom.


    Args:
        data: current data source.
    """
    country_data=defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.weight_g))

    avg_weight={country: sum(weight) / len(weight) for country, weight in country_data.items()}
    sortLength=sorted(avg_weight.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage weight: ")
    print(tabulate(sortLength, ["Country", "Weight (cm)"], tablefmt="rounded_outline"))

def show_filtered_tree_age_years(data): # Vitali

    """Displays the length of banana based off the region from top to bottom.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.tree_age_years))


    avg_age={country: sum(age) / len(age) for country, age in country_data.items()}
    sortAge=sorted(avg_age.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage tree age in each country: ")
    print(tabulate(sortAge, ["Country", "Age (years)"], tablefmt="rounded_outline"))

        
def show_filtered_altitude_m(data): #Vitali
    """Displays the altitude of where banana was groun @ a region.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.altitude_m))


    avg_altitude={country: sum(altitude) / len(altitude) for country, altitude in country_data.items()}
    sortAltitude=sorted(avg_altitude.items(), key=lambda x: x[1], reverse=True)
    print("\nAverage altitude of bananas based off country: ")
    print(tabulate(sortAltitude, ["Country", "Altitude (m)"], tablefmt="rounded_outline"))

        
def show_filtered_rainfall_mm(data): #Vitali
    """Displays the level of rainfall at a region.


    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.rainfall_mm))


    avg_rainfall={country: sum(rainfall) / len(rainfall) for country, rainfall in country_data.items()}
    sortRainfall=sorted(avg_rainfall.items(), key=lambda x: x[1], reverse=True)

    print("\nAverage rainfall in a country: ")
    print(tabulate(sortRainfall, ["Country", "Rainfall (mm)"], tablefmt="rounded_outline"))

        
def show_filtered_soil_nitrogen_ppm(data): # Vitali
    """Displays the nitrogen in soil at a region.

    Args:
        data: current data source.
    """
    country_data = defaultdict(list)

    for r in data:
        country_data[r.region].append(float(r.soil_nitrogen_ppm))


    avg_nitrogen={country: sum(nitrogen) / len(nitrogen) for country, nitrogen in country_data.items()}
    
    # Might change this, wanted to see instead of sorting we just make the table and leave as is :) - Alexi
    nitrogenTable = [[country, nitrogen] for country, nitrogen in avg_nitrogen.items()]

    print("\nAverage amount of nitrogen in soil in a country: ")
    print(tabulate(nitrogenTable, ["Country", "Nitrogen (ppm)"], tablefmt="rounded_outline"))


################################################################################################################### 
# FILTERED SECTION END
################################################################################################################### 


################################################################################################################### 
# COMPREHENSIVE SECTION START
################################################################################################################### 

# Need to add more here :( this place is LONELY - Alexi

################################################################################################################### 
# COMPREHENSIVE SECTION END
################################################################################################################### 
 

#  Note I haven't read through this, I didn't see you write down you were doing filters on Google Doc - Alexi   


def filtered_entries(data, attribute, order='asc'): #Vitali

    invalid_attributes = {"quality_category",
                          "harvest_date", "ripeness_category", "variety"}
    if attribute in invalid_attributes:
        print(f"Invalid attribute '{attribute}'.")
        return

    country_data = defaultdict(list)
    for item in data:
        value = float(getattr(item, attribute))
        country_data[item.region].append(value)

    avg_attribute = {country: sum(values) / len(values)
                     for country, values in country_data.items()}

    if (order == 'asc'):
        sorted_avg_attribute = sorted(
            avg_attribute.items(), key=lambda x: x[1])
        print(
            f"\nAverage {attribute.replace('_', ' ').capitalize()} from lowest to highest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")
    else:
        sorted_avg_attribute = sorted(
            avg_attribute.items(), key=lambda x: x[1], reverse=True)
        print(
            f"\nAverage {attribute.replace('_', ' ').capitalize()} from highest to lowest:")
        for country, avg_value in sorted_avg_attribute:
            print(f"{country}: {avg_value:.2f}")

            
def length_weight(data,attribute,sort_by='value'): #Vitali

    grouped_data = defaultdict(list)

    for item in data:
        key = getattr(item, attribute)
        value = item.length_cm / item.weight_g
        grouped_data[key].append(value)

    group = {group: sum(value) / len(value)
             for group, value in grouped_data.items()}
    values = {}
    if sort_by == 'value':
        values = sorted(group.items(), key=lambda x: x[1])
    elif sort_by == 'group':
        values = sorted(group.items(), key=lambda x: x[0])

    print(f"\nAverage Length/Weight grouped by {attribute.replace('_', ' ')}:")
    for group, avg_ratio in values:
        print(f"{group}: {avg_ratio:.4f}")

#----------------------------------------------------------------------------------------- Refer to my comment @ the top


def corelation_numpy(data, attribute1, attribute2): #Vitali
    data_a = [getattr(item, attribute1) for item in data]
    data_b = [getattr(item, attribute2) for item in data]

    correlation_coefficient = np.corrcoef(data_a, data_b)[0, 1]
    print(
        f"Correlation between {attribute1.replace('_', ' ')} and {attribute2.replace('_', ' ')}: {correlation_coefficient:.4f}")
    # return correlation_coefficient


def corelation_by_group(data, attribute1, attribute2, group_by):
    #Create a dictionary 
    if isinstance(data, list):
        group_data = defaultdict(list)
    #Group data by the value
        for item in data:
            key = getattr(item, group_by)
            group_data[key].append(item)
    else:
        group_data = {getattr(item, group_by): item for item in data}
    # Counter:
    i = 1
    #Annotation
    print(f"""\nCorrelation coefficient ranges from -1 to 1:
         1: Perfect positive correlation (as one variable increases, the other increases).
        -1: Perfect negative correlation (as one variable increases, the other decreases).
         0: No correlation (no discernible relationship between the variables).
    \nCorelation by {group_by}\n""")
    
    #Extract values
    for key, items in group_data.items():
        
        data_a = [getattr(item, attribute1) for item in items]
        data_b = [getattr(item, attribute2) for item in items]
        
        correlation_coefficient = np4.corrcoef(data_a, data_b)[0, 1]
        
        print(f"{i}. {key} ==> Correlation between {attribute1.replace('_', ' ').capitalize()} and {attribute2.replace('_', ' ').capitalize()}: {correlation_coefficient:.4f}")
        i+=1
        
        #Conclusions based on correlation coefficient
        if correlation_coefficient > 0.7:
                conclusion = "Strong positive correlation."
        elif 0.3 <= correlation_coefficient <= 0.7:
                conclusion = "Moderate positive correlation."
        elif 0 <= correlation_coefficient < 0.3:
                conclusion = "Weak positive correlation."
        elif -0.3 <= correlation_coefficient < 0:
                conclusion = "Weak negative correlation."
        elif -0.7 <= correlation_coefficient < -0.3:
                conclusion = "Moderate negative correlation."
        elif correlation_coefficient < -0.7:
                conclusion = "Strong negative correlation."
        else:
                conclusion = "No discernible correlation."
        print(f"   Conclusion: {conclusion}\n")

def corelation_by_group_with_graph(data, attribute1, attribute2, group_by):
    #Create a dictionary 
    group_data = defaultdict(list)
    #Group data by the value
    for item in data:
        key = getattr(item, group_by)
        group_data[key].append(item)
        
    # Counter:
    i = 1
    #Annotation
    print(f"""\nCorrelation coefficient ranges from -1 to 1:
         1: Perfect positive correlation (as one variable increases, the other increases).
        -1: Perfect negative correlation (as one variable increases, the other decreases).
         0: No correlation (no discernible relationship between the variables).
    \nCorelation by {group_by}\n""")
    
    attr1 = attribute1.replace('_', ' ').capitalize()
    attr2 = attribute2.replace('_', ' ').capitalize()
    
    #Extract values
    for key, items in group_data.items():
        
        data_a = [getattr(item, attribute1) for item in items]
        data_b = [getattr(item, attribute2) for item in items]
        
        correlation_coefficient = np4.corrcoef(data_a, data_b)[0, 1]
        
        print(f"{i}. {key} ==> Correlation between {attr1} and {attr2}: {correlation_coefficient:.4f}")
        i+=1
        
        #Conclusions based on correlation coefficient
        if correlation_coefficient > 0.7:
                conclusion = "Strong positive correlation."
        elif 0.3 <= correlation_coefficient <= 0.7:
                conclusion = "Moderate positive correlation."
        elif 0 <= correlation_coefficient < 0.3:
                conclusion = "Weak positive correlation."
        elif -0.3 <= correlation_coefficient < 0:
                conclusion = "Weak negative correlation."
        elif -0.7 <= correlation_coefficient < -0.3:
                conclusion = "Moderate negative correlation."
        elif correlation_coefficient < -0.7:
                conclusion = "Strong negative correlation."
        else:
                conclusion = "No discernible correlation."
        print(f"   Conclusion: {conclusion}\n")
        
        #Graphics
        mplb.figure(figsize=(7, 5))
        mplb.scatter(data_a, data_b)
        mplb.title(f"{attr1} vs {attr2} grouped by {key}")
        mplb.suptitle(conclusion)
        mplb.xlabel(attr1)
        mplb.ylabel(attr2)
               
        a, b = np4.polyfit(data_a, data_b, 1)
        mplb.plot(data_a, [a * x + b for x in data_a], color='crimson')
        
        mplb.grid(True)
        mplb.show()
