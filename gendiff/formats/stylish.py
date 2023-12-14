def stylish(diff_list: list, indent='') -> str:
    result = '{\n'
    for elem in diff_list:
        result = result + formatting_elem(elem, indent + '  ')
    return result + '}'


def formatting_elem(elem: dict, indent='') -> str:
    if isinstance(elem, dict):
        if elem['action'] == 'nested':
            return f"{indent}  {elem['key']}: {stylish(elem.get('value'), indent=indent + '  ')}"
        elif elem['action'] == 'changed':
            return f"{indent}- {elem['key']}: {formatting_value(elem['old'])}\n"\
                   f"{indent}+ {elem['key']}: {formatting_value(elem['new'])}\n"
        else:
            return f"{indent}{formatting_action(elem['action'])} "\
                   f"{elem['key']}: {formatting_value(elem['value'])}\n"


def formatting_action(action: str) -> str:
    if action == 'unchanged':
        return ' '
    elif action == 'deleted':
        return '-'
    else:
        return '+'


def formatting_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if not value:
        return 'null'
    return value
