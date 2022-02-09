from gendiff.file_reader import read_json_file, read_yaml_file


def parse(file_name, format):
    if format == 'json':
        return read_json_file(file_name)
    elif format == 'yml' or format == 'yaml':
        return read_yaml_file(file_name)
    else:
        raise Exception("Wrong file format!!!")


def get_format(file_name):
    return file_name.split('.')[-1]
