def build_plain(diff_list, path=''):
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


def get_path(path, new_elem):
    if path:
        return f'{path}.{new_elem}'
    return f'{new_elem}'


def format_value(value):
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
