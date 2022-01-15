from gendiff import generate_diff


def test_generate_diff():
    diff = generate_diff(
        "tests/fixtures/file1.json", 
        "tests/fixtures/file2.json"
        )
    file = open(
        "tests/fixtures/res_string.txt"
        )
    result = file.read()
    assert diff == result
