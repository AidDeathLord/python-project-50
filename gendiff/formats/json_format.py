import json as json_format


def json(data):
    return json_format.dumps(data, indent=4)
