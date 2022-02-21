import json
import yaml


def parse(data, format):
    if format == '.json':
        return json.load(data)
    elif format == '.yml' or format == '.yaml':
        return yaml.safe_load(data)
    else:
        raise Exception("Wrong file format!!!")
