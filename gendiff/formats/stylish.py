def stylish(diff_list: list, indent='') -> str:
    result = '{\n'
    for elem in diff_list:
        if elem['action'] == 'nested':
            result = result + add_nested_elem(elem, indent + '  ')
        elif elem['action'] == 'changed':
            result = result + f"{indent + '  '}- {elem['key']}: {formatting_value(elem['old'], indent)}\n"
            result = result + f"{indent + '  '}+ {elem['key']}: {formatting_value(elem['new'], indent)}\n"
        else:
            result = result + (f"{indent + '  '}{formatting_action(elem['action'])}"
                               f"{elem['key']}: {formatting_value(elem['value'], indent)}\n")
    return result + f'{indent}' + '}'


def add_nested_elem(elem, indent):
    formatted_elem = f"{indent}  {elem['key']}: {stylish(elem.get('value'), indent + '  ')}\n"
    return formatted_elem


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
    if value == '':
        return ''
    if not value:
        return 'null'
    return value


def formatting_dict_value(item, indent):
    result = '{\n'
    for keys, values in item.items():
        if isinstance(values, dict):
            result = result + f'{indent}  {keys}:' + formatting_dict_value(values, indent + '  ')
        else:
            print(item)
            result = result + f'{indent}{indent}{keys}: {values}\n'
    return result + f'{indent}' + '  }'
