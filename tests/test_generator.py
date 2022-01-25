from gendiff import generate_diff
from gendiff.formatters.plain import plain

def test_generate_diff_stylish_json():
    diff = generate_diff(
        "tests/fixtures/file1.json", 
        "tests/fixtures/file2.json"
        )
    file = open(
        "tests/fixtures/res_string_stylish.txt"
        )
    result = file.read()
    assert diff == result


def test_generate_diff_plain_json():
    diff = generate_diff(
        "tests/fixtures/file1.json", 
        "tests/fixtures/file2.json",
        plain
        )
    file = open(
        "tests/fixtures/res_string_plain.txt"
        )
    result = file.read()
    assert diff == result


def test_generate_diff_json_empty_files():
    diff = generate_diff(
        "tests/fixtures/empty_file1.json", 
        "tests/fixtures/empty_file2.json"
        )
    assert diff == ''


def test_generate_diff_stylish_yaml():
    diff = generate_diff(
        "tests/fixtures/file1.yaml", 
        "tests/fixtures/file2.yaml"
        )
    file = open(
        "tests/fixtures/res_string_stylish.txt"
        )
    result = file.read()
    assert diff == result


def test_generate_diff_plain_yaml():
    diff = generate_diff(
        "tests/fixtures/file1.yaml", 
        "tests/fixtures/file2.yaml",
        plain
        )
    file = open(
        "tests/fixtures/res_string_plain.txt"
        )
    result = file.read()
    assert diff == result


def test_generate_diff_yaml_empty_files():
    diff = generate_diff(
        "tests/fixtures/empty_file1.yaml", 
        "tests/fixtures/empty_file2.yaml"
        )
    assert diff == ''