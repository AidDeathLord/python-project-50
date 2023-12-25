from gendiff import generate_diff
import pytest
import os


def get_path(file):
    return os.path.join('tests', 'fixtures', file)


@pytest.mark.parametrize(
    "test_input1,test_input2, output,  expected",
    [
        pytest.param(
            'file1.yml',
            'file2.yaml',
            'stylish',
            'correct_flat_file.txt',
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
            'correct_flat_file.txt'
        ),
        pytest.param(
            'nested_file_1.json',
            'nested_file_2.json',
            'stylish',
            'correct_nested_file.txt'
        ),
        pytest.param(
            'nested_file_1.yml',
            'nested_file_2.yml',
            'stylish',
            'correct_nested_file.txt'
        ),
        pytest.param(
            'nested_file_1.yml',
            'nested_file_2.yml',
            'plain',
            'correct_plain_result.txt'
        ),
        pytest.param(
            'nested_file_1.yml',
            'nested_file_2.yml',
            'json',
            'correct_json_result.txt'
        )
    ],
)
def test_generate_diff(test_input1, test_input2, output, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
    test_path1 = get_path(test_input1)
    test_path2 = get_path(test_input2)
    assert result_data == generate_diff(test_path1, test_path2, output)

