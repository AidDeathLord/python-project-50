INDENT_QUANT = 4
MARKS = {
    'deleted': '-',
    'added': '+',
    'unchanged': ' '
}


def get_indent(depth: int) -> str:
    indent = (depth - 1) * INDENT_QUANT * ' '
    return str(indent)


def build_stylish(diff_list: list, depth=0) -> str:
    result = '{\n'
    for elem in diff_list:
        result = result + add_formatted_elem(elem, depth)
    depth += 1
    return result + f'{get_indent(depth)}' + '}\n'


def add_formatted_elem(elem: dict, depth: int) -> str:
    depth += 1
    match elem['action']:
        case 'nested':
            return (f"{get_indent(depth)}  {MARKS['unchanged']} {elem['key']}: "
                    f"{build_stylish(elem.get('value'), depth)}")
        case 'changed':
            return (f"{get_indent(depth)}  {MARKS['deleted']} {elem['key']}: "
                    f"{format_value(elem['old'], depth)}\n"
                    f"{get_indent(depth)}  {MARKS['added']} {elem['key']}: "
                    f"{format_value(elem['new'], depth)}\n")
        case 'unchanged':
            return (f"{get_indent(depth)}  {MARKS['unchanged']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")
        case 'deleted':
            return (f"{get_indent(depth)}  {MARKS['deleted']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")
        case 'added':
            return (f"{get_indent(depth)}  {MARKS['added']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")


def format_value(value, depth):
    if isinstance(value, dict):
        return formatting_dict_value(value, depth)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


def formatting_dict_value(item, depth):
    depth += 1
    result = '{\n'
    for keys, values in item.items():
        if isinstance(values, dict):
            result += (f"{get_indent(depth)}  {MARKS['unchanged']} {keys}: "
                       f"{formatting_dict_value(values, depth)}\n")
        else:
            result = result + (f"{get_indent(depth)}  {MARKS['unchanged']} "
                               f"{keys}: {values}\n")
    return result + f'{get_indent(depth)}' + '}'


def stylish(diff_list):
    return build_stylish(diff_list).strip()
