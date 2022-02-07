import json
import yaml


def get_dict(file_name, format):
    if format == 'json':
        return json.load(open(file_name))
    elif format == 'yml' or format == 'yaml':
        return yaml.safe_load(open(file_name))
    else:
        raise Exception("Wrong file format!!!")
