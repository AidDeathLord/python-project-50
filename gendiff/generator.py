from gendiff.parse_files import open_file
from gendiff.formats.stylish import stylish


def generate_diff_list(first_dict: dict, second_dict: dict) -> list:
    result = []
    keys = first_dict.keys() | second_dict.keys()
    for key in sorted(keys):
        if key in first_dict.keys() and key in second_dict.keys():
            if first_dict[key] == second_dict[key]:
                result.append({
                    'key': key,
                    'action': 'nested',
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
    print(result)
    return result


def generate_diff(first_file: str, second_file: str, output=stylish) -> str:
    return output(generate_diff_list(open_file(first_file),
                                     open_file(second_file)))
