INDENT_QUANT = 2


def indent(depth):
    return depth * INDENT_QUANT * ' '


def build_stylish(diff_list: list, depth=0) -> str:
    result = '{\n'
    for elem in diff_list:
        result = result + add_formatted_elem(elem, depth=+1)
    return result + f'{indent(depth)}' + '}\n'


def add_formatted_elem(elem, depth):
    marks = {
        'nested': ' ',
        'deleted': '-',
        'added': '+',
        'unchanged': ' '
    }
    match elem['action']:
        case 'nested':
            return (f"{indent(depth)}{marks['nested']} {elem['key']}: "
                    f"{build_stylish(elem.get('value'), depth)}")
        case 'changed':
            return (f"{indent(depth)}{marks['deleted']} {elem['key']}: "
                    f"{format_value(elem['old'], depth)}\n"
                    f"{indent(depth)}{marks['added']} {elem['key']}: "
                    f"{format_value(elem['new'], depth)}\n")
        case 'unchanged':
            return (f"{indent(depth)}{marks['unchanged']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")
        case 'deleted':
            return (f"{indent(depth)}{marks['deleted']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")
        case 'added':
            return (f"{indent(depth)}{marks['added']} "
                    f"{elem['key']}: {format_value(elem['value'], depth)}\n")


def format_value(value, depth):
    # if isinstance(value, dict):
    #     depth += 1
    #     return formatting_dict_value(value, depth)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


# def formatting_dict_value(item, depth):
#     result = '{\n'
#     for keys, values in item.items():
#         if isinstance(values, dict):
#
#             result += (f"{indent(depth)}    {keys}: "
#                        f"{formatting_dict_value(values, depth=+2}\n")
#         else:
#             result = result + f'{indent}    {keys}: {values}\n'
#     return result + f'{indent}' + '}'


def stylish(diff_list):
    return build_stylish(diff_list).strip()
