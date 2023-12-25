def build_plain(diff_list, path=''):
    result = ''
    for elem in diff_list:
        if elem['action'] == 'nested':
            result += build_plain(elem['value'], get_path(path, elem['key']))
        elif elem['action'] == 'added':
            result += (f"Property '{get_path(path, elem['key'])}' "
                       f"was added with value: {formatting_value(elem['value'])}\n")
        elif elem['action'] == 'deleted':
            result += f"Property '{get_path(path, elem['key'])}' was removed\n"
        elif elem['action'] == 'changed':
            result += (f"Property '{get_path(path, elem['key'])}' "
                       f"was updated. From {formatting_value(elem['old'])} "
                       f"to {formatting_value(elem['new'])}\n")
    return result


def get_path(path, new_elem):
    if path:
        return f'{path}.{new_elem}'
    return f'{new_elem}'


def formatting_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    return value


def plain(diff_list):
    return build_plain(diff_list).strip()
