import json
import yaml


# Open file and return dict
def open_file(file_path):
    with open(file_path) as f:
        data = f.read()
    if file_path[-5:] == '.json':
        return json.loads(data)
    return yaml.safe_load(data)
