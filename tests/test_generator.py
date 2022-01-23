from gendiff import generate_diff
from gendiff.stylish import stylish


def test_generate_diff_json():
    diff = generate_diff(
        "tests/fixtures/file1.json", 
        "tests/fixtures/file2.json"
        )
    file = open(
        "tests/fixtures/res_string.txt"
        )
    result = file.read()
    assert stylish(diff) == result


def test_generate_diff_json_empty_files():
    diff = generate_diff(
        "tests/fixtures/empty_file1.json", 
        "tests/fixtures/empty_file2.json"
        )
    assert stylish(diff) == ''


def test_generate_diff_yaml():
    diff = generate_diff(
        "tests/fixtures/file1.yaml", 
        "tests/fixtures/file2.yaml"
        )
    file = open(
        "tests/fixtures/res_string.txt"
        )
    result = file.read()
    assert stylish(diff) == result


def test_generate_diff_yaml_empty_files():
    diff = generate_diff(
        "tests/fixtures/empty_file1.yaml", 
        "tests/fixtures/empty_file2.yaml"
        )
    assert stylish(diff) == ''