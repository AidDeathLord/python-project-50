def stylish(diff_list: list, indent='') -> str:
    result = '{\n'
    for elem in diff_list:
        result = result + add_formatted_elem(elem, indent + '  ')
    return result + f'{indent}' + '}\n'


def add_formatted_elem(elem, indent):
    if elem['action'] == 'nested':
        return (f"{indent + '  '}{elem['key']}: "
                f"{stylish(elem.get('value'), indent + '  ')}")
    elif elem['action'] == 'changed':
        return (f"{indent}- {elem['key']}: "
                f"{formatting_value(elem['old'], indent)}\n"
                f"{indent}+ {elem['key']}: "
                f"{formatting_value(elem['new'], indent)}\n")
    else:
        return (f"{indent}{formatting_action(elem['action'])}"
                f"{elem['key']}: {formatting_value(elem['value'], indent)}\n")


def formatting_action(action: str) -> str:
    if action == 'unchanged':
        return '  '
    elif action == 'deleted':
        return '- '
    else:
        return '+ '


def formatting_value(value, indent):
    if isinstance(value, dict):
        return formatting_dict_value(value, indent + '  ')
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'

    return value


def formatting_dict_value(item, indent):
    result = '{\n'
    for keys, values in item.items():
        if isinstance(values, dict):
            result += (f"{indent}    {keys}: "
                       f"{formatting_dict_value(values, indent + '    ')}\n")
        else:
            result = result + f'{indent}    {keys}: {values}\n'
    return result + f'{indent}' + '}'
