from gendiff.formats.stylish import stylish
from gendiff.parse_files import open_file


def generate_diff_list(first_dict: dict, second_dict: dict) -> list:
    result = []
    keys = first_dict.keys() | second_dict.keys()
    for key in sorted(keys):
        if key in first_dict.keys() and key in second_dict.keys():
            if isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
                result.append({
                    'key': key,
                    'action': 'nested',
                    'value': generate_diff_list(first_dict.get(key), second_dict.get(key))
                })
            elif first_dict[key] == second_dict[key]:
                result.append({
                    'key': key,
                    'action': 'unchanged',
                    'value': first_dict[key]
                })
            else:
                result.append({
                    'key': key,
                    'action': 'changed',
                    'old': first_dict[key],
                    'new': second_dict[key]
                })
        elif key in first_dict.keys():
            result.append({
                'key': key,
                'action': 'deleted',
                'value': first_dict[key]
            })
        else:
            result.append({
                'key': key,
                'action': 'added',
                'value': second_dict[key]
            })
    return result


def generate_diff(first_file: str, second_file: str, output=stylish) -> str:
    return output(generate_diff_list(open_file(first_file),
                                     open_file(second_file)))
