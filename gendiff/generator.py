from gendiff.parse_files import open_file


def generate_diff_dict(first_dict, second_dict):
    keys = first_dict.keys() | second_dict.keys()
    return keys


def generate_diff(first_file, second_file):
    return generate_diff_dict(open_file(first_file),
                              open_file(second_file))
