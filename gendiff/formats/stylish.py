def stylish(diff_list: list, indent='') -> str:
    result = '{\n'
    for elem in diff_list:
        result = result + formatting_elem(elem, indent + '  ')
    return result + '}'


def formatting_elem(elem: dict, indent='') -> str:
    if elem['action'] == 'changed':
        return f"{indent}- {elem['key']}: {elem['old']}\n"\
               f"{indent}+ {elem['key']}: {elem['new']}\n".lower()
    else:
        return f"{indent}{formatting_action(elem['action'])} "\
               f"{elem['key']}: {elem['value']}\n".lower()


def formatting_action(action: str) -> str:
    if action == 'nested':
        return ' '
    elif action == 'deleted':
        return '-'
    else:
        return '+'
