# Banana representation

class Banana:

    def __init__(self, **kwargs):
        self.variety = kwargs.get("variety")
        self.region = kwargs.get("region")
        self.quality_score = kwargs.get("quality_score")
        self.quality_category = kwargs.get("quality_category")
        self.ripeness_index = kwargs.get("ripeness_index")
        self.ripeness_category = kwargs.get("ripeness_category")
        self.sugar_content_brix = kwargs.get("sugar_content_brix")
        self.firmness_kgf = kwargs.get("firmness_kgf")
        self.length_cm = kwargs.get("length_cm")
        self.weight_g = kwargs.get("weight_g")
        self.harvest_date = kwargs.get("harvest_date")
        self.tree_age_years = kwargs.get("tree_age_years")
        self.altitude_m = kwargs.get("altitude_m")
        self.rainfall_mm = kwargs.get("rainfall_mm")
        self.soil_nitrogen_ppm = kwargs.get("soil_nitrogen_ppm")

    def __str__(self):
        # TODO: Extend string representation with more data
        return f"{self.quality_category} quality {self.ripeness_category} {self.variety} from {self.region}"

    
