import json
import yaml
from gendiff.formatters._json import _json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import generate_diff_list


def generate_diff(file1, file2, formatter='stylish'):
    dict1 = read_file(file1)
    dict2 = read_file(file2)
    if formatter == 'stylish':
        return stylish(generate_diff_list(dict1, dict2))
    if formatter == 'plain':
        return plain(generate_diff_list(dict1, dict2))
    if formatter == 'json':
        return _json(generate_diff_list(dict1, dict2))


def read_file(file_name):
    file_format = file_name.split('.')[-1]
    if file_format == 'json':
        return json.load(open(file_name))
    elif file_format == 'yml' or file_format == 'yaml':
        return yaml.safe_load(open(file_name))
    else:
        raise Exception("Wrong file format!!!")
