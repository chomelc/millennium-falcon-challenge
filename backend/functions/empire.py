from json_functions import get_data_from_json


class Empire:
    """A class used to represent the data from the empire.json file.
    """
    countdown = 0
    bounty_hunters = []

    def __init__(self, path_to_file):
        """Constructs the Empire object with the specified json file.
        @param `path_to_file`: the path to the JSON file
        """
        data = get_data_from_json(path_to_file)
        self.countdown = data['countdown']
        self.bounty_hunters = data['bounty_hunters']

    def get_countdown(self):
        """Returns the `countdown` attribute of the Empire object
        @return the `countdown` attribute of the Empire object
        """
        return self.countdown

    def get_bounty_hunters(self):
        """Returns the `bounty_hunters` attribute of the Empire object
        @return the `bounty_hunters` attribute of the Empire object
        """
        return self.bounty_hunters
