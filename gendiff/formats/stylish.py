from typing import Union


INDENT_QUANT = 4
REPLACER = ' '


def build_stylish(diff_list: list, depth: int) -> str:
    """convert the list of differences into a string with a correct output"""
    result = '{\n'
    for elem in diff_list:
        result = result + add_formatted_elem(elem, depth)
    return result + f'{depth * REPLACER}' + '}\n'


def add_formatted_elem(elem: dict, depth: int) -> str:
    """depending on the action, convert the element to string"""
    offset = depth + INDENT_QUANT
    indent = (offset - 2) * REPLACER
    key, value = elem.get('key'), elem.get('value')
    action = elem['action']
    match action:
        case 'nested':
            return f"{indent}  {key}: {build_stylish(value, offset)}"
        case 'changed':
            return (f"{indent}- {key}: {format_value(elem['old'], depth)}\n"
                    f"{indent}+ {key}: {format_value(elem['new'], depth)}\n")
        case 'unchanged':
            return f"{indent}  {key}: {format_value(elem['value'], depth)}\n"
        case 'deleted':
            return f"{indent}- {key}: {format_value(elem['value'], depth)}\n"
        case 'added':
            return f"{indent}+ {key}: {format_value(elem['value'], depth)}\n"


def format_value(elem: Union[str, int, bool, dict], depth: int) -> str:
    """depending on the type, format the value to string"""
    if isinstance(elem, dict):
        indent = (depth + INDENT_QUANT * 2) * REPLACER
        result = '{\n'
        for key, value in elem.items():
            if isinstance(value, dict):
                result += (f'{indent}{key}: '
                           f'{format_value(value, depth + INDENT_QUANT)}\n')
            else:
                result += f'{indent}{key}: {value}\n'
        return result + f'{(depth + INDENT_QUANT) * REPLACER}' + '}'

    if isinstance(elem, bool):
        return 'true' if elem else 'false'
    if elem is None:
        return 'null'
    return elem


def stylish(diff_list: list) -> str:
    return build_stylish(diff_list, 0).strip()
