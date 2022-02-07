import json
import pytest
from gendiff import generate_diff


file1_path_json = "tests/fixtures/file1.json"
file2_path_json = "tests/fixtures/file2.json"
file1_path_yaml = "tests/fixtures/file1.yaml"
file2_path_yaml = "tests/fixtures/file2.yaml"
empty_file1_path_json = "tests/fixtures/empty_file1.json"
empty_file2_path_json = "tests/fixtures/empty_file2.json"
empty_file1_path_yaml = "tests/fixtures/empty_file1.yaml"
empty_file2_path_yaml = "tests/fixtures/empty_file2.yaml"
res_stylish_file = "tests/fixtures/res_string_stylish.txt"
res_plain_file = "tests/fixtures/res_string_plain.txt"
res_json_file = "tests/fixtures/res_string_json.txt"


result_stylish = open(res_stylish_file).read()
result_plain = open(res_plain_file).read()


stylish_set = ("stylish", result_stylish)
plain_set = ("plain", result_plain)


@pytest.mark.parametrize("file1", [file1_path_json, file1_path_yaml])
@pytest.mark.parametrize("file2", [file2_path_json, file2_path_yaml])
@pytest.mark.parametrize("formatter,result", [stylish_set, plain_set])
def test_generate_diff(file1, file2, formatter, result):
    diff = generate_diff(file1, file2, formatter)
    assert diff == result


@pytest.mark.parametrize("file1", [file1_path_json, file1_path_yaml])
@pytest.mark.parametrize("file2", [file2_path_json, file2_path_yaml])
def test_generate_diff_json(file1, file2):
    diff = generate_diff(file1, file2, 'json')
    file = open(res_json_file)
    result_dict = json.load(file)
    diff_dict = json.loads(diff)
    assert diff_dict == result_dict


@pytest.mark.parametrize("file1", [
    empty_file1_path_json,
    empty_file1_path_yaml])
@pytest.mark.parametrize("file2", [
    empty_file2_path_json,
    empty_file2_path_yaml])
def test_generate_diff_empty_files(file1, file2):
    diff = generate_diff(file1, file2)
    assert diff == ''
