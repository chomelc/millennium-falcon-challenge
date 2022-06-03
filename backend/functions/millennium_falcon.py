from enum import auto
from json_functions import get_data_from_json


class MillenniumFalcon:
    """A class used to represent the data from the millennium-falcon.json file.
    """
    autonomy = 0
    departure = ''
    arrival = ''
    routes_db = ''

    def __init__(self, path_to_file):
        """Constructs the MilleniumFalcon object with the specified json file.
        @param `path_to_file`: the path to the JSON file
        """
        data = get_data_from_json(path_to_file)
        self.autonomy = data['autonomy']
        self.departure = data['departure']
        self.arrival = data['arrival']
        self.routes_db = data['routes_db']

    def get_autonomy(self):
        """Returns the `autonomy` attribute of the MillenniumFalcon object
        @return the `autonomy` attribute of the MillenniumFalcon object
        """
        return self.autonomy

    def get_departure(self):
        """Returns the `departure` attribute of the MillenniumFalcon object
        @return the `departure` attribute of the MillenniumFalcon object
        """
        return self.departure

    def get_arrival(self):
        """Returns the `arrival` attribute of the MillenniumFalcon object
        @return the `arrival` attribute of the MillenniumFalcon object
        """
        return self.arrival

    def get_routes_db(self):
        """Returns the `routes_db` attribute of the MillenniumFalcon object
        @return the `routes_db` attribute of the MillenniumFalcon object
        """
        return self.routes_db
