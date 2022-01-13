from gendiff import generate_diff


def test_generate_diff():
    diff = generate_diff(
        "/Users/mark/Python/python-project-lvl2/tests/fixtures/file1.json", 
        "/Users/mark/Python/python-project-lvl2/tests/fixtures/file2.json"
        )
    file = open(
        "/Users/mark/Python/python-project-lvl2/tests/fixtures/res_string.txt"
        )
    result = file.read()
    assert diff == result
