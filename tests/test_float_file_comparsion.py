from gendiff.parse_files import open_file
from gendiff import generate_diff


def test_parse_files():
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
