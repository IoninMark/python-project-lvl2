from gendiff.formatters import stylish, plain, _json


def get_formatter(formatter):
    if formatter == 'stylish':
        return stylish.format
    elif formatter == 'plain':
        return plain.format
    elif formatter == 'json':
        return _json.format
    else:
        raise Exception("Wrong formatter!!!")
