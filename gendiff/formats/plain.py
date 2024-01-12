from typing import Union


def build_plain(diff_list, path=''):
    """convert the list of differences into a string with a correct output"""
    result = ''
    for elem in diff_list:
        match elem['action']:
            case 'nested':
                result += build_plain(elem['value'],
                                      get_path(path, elem['key']))
            case 'added':
                result += (f"Property '{get_path(path, elem['key'])}' "
                           f"was added with value: "
                           f"{format_value(elem['value'])}\n")
            case 'deleted':
                result += (f"Property '{get_path(path, elem['key'])}' "
                           f"was removed\n")
            case 'changed':
                result += (f"Property '{get_path(path, elem['key'])}' "
                           f"was updated. From {format_value(elem['old'])} "
                           f"to {format_value(elem['new'])}\n")
    return result


def get_path(path: str, new_elem: str) -> str:
    """creating the correct output of the element"""
    if path:
        return f'{path}.{new_elem}'
    return f'{new_elem}'


def format_value(value: Union[str, int, bool, dict]) -> str:
    """depending on the type, format the value to string"""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    return str(value)


def plain(diff_list):
    return build_plain(diff_list).strip()
