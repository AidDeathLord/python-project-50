import json


# Open file and return dict
def open_file(file_path):
    return json.load(open(file_path))
