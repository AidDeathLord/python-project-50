from gendiff import generate_diff
from gendiff.formats.stylish import stylish


def test_parse_json_files():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    diff_list = generate_diff(first_file, second_file).lower()
    correct_output = '{\n'\
                     '  - follow: false\n'\
                     '    host: hexlet.io\n'\
                     '  - proxy: 123.234.53.22\n'\
                     '  - timeout: 50\n'\
                     '  + timeout: 20\n'\
                     '  + verbose: true\n'\
                     '}'
    assert correct_output == diff_list


def test_parse_yml_files():
    first_file = 'tests/fixtures/file1.yml'
    second_file = 'tests/fixtures/file2.yaml'
    correct_file = open('tests/fixtures/correct_yml.txt').readlines()
    correct_output = ''.join(correct_file)
    diff_list = generate_diff(first_file, second_file).lower()
    assert correct_output == diff_list


test_parse_yml_files()
