from gendiff.formats.stylish import stylish
from gendiff.parse_files import open_file
from gendiff.formats.plain import plain
from gendiff.formats.json_format import json


FORMAT = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}
ERRORS = {
    'file_extension_error': 'ERROR!!!\nFile has the wrong extension!'
}


def generate_diff_list(dict_1: dict, dict_2: dict) -> list:
    """compare two dictionaries and return a list of changes"""
    result = []
    keys = dict_1.keys() | dict_2.keys()
    for key in sorted(keys):
        if key not in dict_1.keys():
            result.append({
                'key': key,
                'action': 'added',
                'value': dict_2[key]
            })
        elif key not in dict_2.keys():
            result.append({
                'key': key,
                'action': 'deleted',
                'value': dict_1[key]
            })
        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            result.append({
                'key': key,
                'action': 'nested',
                'value': generate_diff_list(dict_1.get(key),
                                            dict_2.get(key))
            })
        elif dict_1[key] == dict_2[key]:
            result.append({
                'key': key,
                'action': 'unchanged',
                'value': dict_1[key]
            })
        else:
            result.append({
                'key': key,
                'action': 'changed',
                'old': dict_1[key],
                'new': dict_2[key]
            })
    return result


def generate_diff(first_file: str, second_file: str, output='stylish') -> str:
    """generates a list of differences
       and outputs them in the selected format"""
    dict_1 = open_file(first_file)
    dict_2 = open_file(second_file)
    check_result, error = check_for_errors(dict_1, dict_2)
    if check_result:
        return ERRORS[error]
    return FORMAT[output](generate_diff_list(dict_1, dict_2))


def check_for_errors(*args: dict) -> (bool, str):
    for elem in args:
        if 'error' in elem.keys():
            return True, elem.get('error')
    return False, ''
