import json
import yaml
from pathlib import Path


# Open file and return dict
def open_file(file_path):
    with open(file_path) as f:
        data = f.read()
    match Path(file_path).suffix:
        case '.json':
            return json.loads(data)
        case '.yaml' | '.yml':
            return yaml.safe_load(data)
        case _:
            return {'error': 'file_extension_error'}
