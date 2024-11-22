# Banana representation

class Banana:

    def __init__(self, **kwargs):
        # Copies keys and values from dict passed in as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        # TODO: Extend string representation with more data
        return f"{self.quality_category} quality {self.ripeness_category} {self.variety} from {self.region}"
