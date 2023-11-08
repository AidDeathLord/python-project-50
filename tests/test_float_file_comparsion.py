from gendiff.parse_files import open_file
from gendiff import generate_diff


def test_parse_json_files():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    diff_list = generate_diff(first_file, second_file)
    print(diff_list)
    correct_output = '{\n'\
                     '  - follow: False\n'\
                     '    host: hexlet.io\n'\
                     '  - proxy: 123.234.53.22\n'\
                     '  - timeout: 50\n'\
                     '  + timeout: 20\n'\
                     '  + verbose: True\n'\
                     '}'
    assert correct_output == diff_list


def test_parse_yml_files():
    first_file = 'tests/fixtures/file1.yml'
    second_file = 'tests/fixtures/file2.yaml'
    correct_file = open('tests/fixtures/correct_yml.txt').readlines()
    correct_output = ''.join(correct_file)
    assert generate_diff(first_file, second_file) == correct_output.lower()


test_parse_yml_files()
