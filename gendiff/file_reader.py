import json
import yaml


def read_json_file(file_name):
    return json.load(open(file_name))


def read_yaml_file(file_name):
    return yaml.safe_load(open(file_name))
