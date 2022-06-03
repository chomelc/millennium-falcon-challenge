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
