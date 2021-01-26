'''
Plant class for xml_explorer.py code

'''


class Plant:
    warning = "Failed to properly instantiate plant"

    def __init__(self, **plant_dict):
        # COMMON
        # BOTANICAL
        # ZONE
        # LIGHT
        # PRICE
        # AVAILABILTY

        self.__dict__.update(plant_dict)

    def __iter__(self):
        pass

    def get_info(self):
        return (f"The {self.COMMON} plant sells for {self.PRICE}")

    def get_price(self):
        return float(self.PRICE.replace("$",""))
