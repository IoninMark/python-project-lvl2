from gendiff.formatters.format_selector import get_formatter
from gendiff.parser import parse
from gendiff.file_reader import read_file, get_format
from gendiff.diff_dict_generator import generate_diff_dict


def generate_diff(file1, file2, formatter='stylish'):
    file1_format = get_format(file1)
    file2_format = get_format(file2)
    dict1 = parse(read_file(file1), file1_format)
    dict2 = parse(read_file(file2), file2_format)
    format_func = get_formatter(formatter)
    return format_func(generate_diff_dict(dict1, dict2))
