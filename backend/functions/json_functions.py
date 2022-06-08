import json


def get_data_from_json(path_to_file):
    """Reads and returns the content of a json file as a dictionnary.
    @param `path_to_file`: the path to the JSON file
    @return the fetched data as a dictionnary
    """
    f = open(path_to_file)
    data = json.load(f)
    f.close()
    return data


def get_data_from_text(text):
    """Reads and returns raw json data as a dictionnary.
    @param `text`: the raw JSON data
    @return the data as a dictionnary
    """
    return json.loads(text)
