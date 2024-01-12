import json as json_format


def json(data):
    """convert list of differences into json"""
    return json_format.dumps(data, indent=4)
