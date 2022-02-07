from gendiff.formatters.format_selector import get_formatter
from gendiff.parser import get_dict


def generate_diff(file1, file2, formatter='stylish'):
    file1_format = file1.split('.')[-1]
    file2_format = file2.split('.')[-1]
    dict1 = get_dict(file1, file1_format)
    dict2 = get_dict(file2, file2_format)
    format_func = get_formatter(formatter)
    return format_func(generate_diff_list(dict1, dict2))


def generate_diff_list(dict1, dict2):
    """Function compares files and generates
    difference list.
    [
        {
            'key': {
                'type': equal/dict/removed/added/updated,
                'value': key_name
                },
            'children': [..childs {}..], - if both are dicts
            'value': value
        }
    ]"""
    result = []
    set1 = set(dict1)
    set2 = set(dict2)
    com_keys = set1 & set2
    add_keys = set2 - set1
    dell_keys = set1 - set2
    for add_key in add_keys:
        item = {
            'key': {
                'type': 'added',
                'value': add_key
            },
            'value': dict2.get(add_key)
        }
        result.append(item)

    for dell_key in dell_keys:
        item = {
            'key': {
                'type': 'removed',
                'value': dell_key
            },
            'value': dict1.get(dell_key)
        }
        result.append(item)

    for com_key in com_keys:
        elem1 = dict1.get(com_key)
        elem2 = dict2.get(com_key)
        if elem1 == elem2:
            item = {
                'key': {
                    'type': 'equal',
                    'value': com_key
                },
                'value': dict1.get(com_key)
            }
            result.append(item)
        else:
            if isinstance(elem1, dict) and isinstance(elem2, dict):
                item = {
                    'key': {
                        'type': 'dict',
                        'value': com_key
                    },
                    'children': generate_diff_list(elem1, elem2)
                }
                result.append(item)
            else:
                item = {
                    'key': {
                        'type': 'updated',
                        'value': com_key
                    },
                    'value': {
                        'old_val': dict1.get(com_key),
                        'new_val': dict2.get(com_key)
                    }
                }
                result.append(item)

    sorted_result = sorted(result, key=lambda k: k['key']['value'])
    return sorted_result
