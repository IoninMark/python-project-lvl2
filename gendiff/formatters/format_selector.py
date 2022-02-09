from gendiff.formatters import stylish, plain, _json


def get_formatter(formatter='stylish'):
    if formatter == 'stylish':
        return stylish.format
    if formatter == 'plain':
        return plain.format
    if formatter == 'json':
        return _json.format
