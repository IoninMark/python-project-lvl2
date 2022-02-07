from gendiff.formatters._json import _json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(formatter='stylish'):
    if formatter == 'stylish':
        return stylish
    if formatter == 'plain':
        return plain
    if formatter == 'json':
        return _json
