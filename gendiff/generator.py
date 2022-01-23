import json
import yaml
from gendiff.parser import generate_diff_list


def generate_diff(file1, file2):
    dict1 = read_file(file1)
    dict2 = read_file(file2)
    return generate_diff_list(dict1, dict2)


def read_file(file_name):
    file_format = file_name.split('.')[-1]
    if file_format == 'json':
        return json.load(open(file_name))
    elif file_format == 'yml' or file_format == 'yaml':
        return yaml.safe_load(open(file_name))
    else:
        print("Wrong file format!!!")
