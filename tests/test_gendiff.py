from gendiff.scripts.gen_diff import generate_diff, correcting_output


def test_generate_diff():
    correct_output = '{\n    host: hexlet.io\n  - ip: 10.0.0.10\n  + timeout: 50\n}'
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == correct_output


def test_generate_diff_with_empty_file():
    correct_output = '{\n  + host: hexlet.io\n  + timeout: 50\n}'
    assert generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file2.json') == correct_output


def test_correcting_output():
    result = [['+', 'host', 'hexlet.io']]
    correct = '{\n  + host: hexlet.io\n}'
    assert correcting_output(result) == correct
