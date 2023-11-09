import json
import yaml


# Open file and return dict
def open_file(file_path):
    if file_path[-5:] == '.json':
        return json.load(open(file_path))
    return yaml.load(open(file_path), Loader=yaml.FullLoader)
