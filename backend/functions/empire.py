from json_functions import get_data_from_json, get_data_from_text


class Empire:
    """A class used to represent the data from the empire.json file.
    """
    countdown = 0
    bounty_hunters = []

    def __init__(self, file):
        """Constructs the Empire object with the specified json file.
        @param `file`: the JSON file
        """
        if (file.startswith("{")):
            # if the data is provided as raw json
            data = get_data_from_text(file)
        else:
            # if the data is provided as a .json file
            data = get_data_from_json(file)
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
