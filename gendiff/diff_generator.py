from gendiff.formatters.format_selector import get_formatter
from gendiff.parser import parse, get_format


def generate_diff(file1, file2, formatter='stylish'):
    file1_format = get_format(file1)
    file2_format = get_format(file2)
    dict1 = parse(file1, file1_format)
    dict2 = parse(file2, file2_format)
    format_func = get_formatter(formatter)
    return format_func(generate_diff_list(dict1, dict2))


def generate_diff_list(dict1, dict2):
    """Function compares files and generates
    difference list.
    [
        {
            'key': {
                'type': equal/dict/removed/added/updated,
                'value': value
                'old_val': old_value - for updated
                'new_val': new_value - for updated
                'children': [..childs {}..] - for dict
                }
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
            add_key: {
                'type': 'added',
                'value': dict2.get(add_key)
            }
        }
        result.append(item)

    for dell_key in dell_keys:
        item = {
            dell_key: {
                'type': 'removed',
                'value': dict1.get(dell_key)
            }
        }
        result.append(item)

    for com_key in com_keys:
        elem1 = dict1.get(com_key)
        elem2 = dict2.get(com_key)
        if elem1 == elem2:
            item = {
                com_key: {
                    'type': 'equal',
                    'value': dict1.get(com_key)
                }
            }
            result.append(item)
        else:
            if isinstance(elem1, dict) and isinstance(elem2, dict):
                item = {
                    com_key: {
                        'type': 'dict',
                        'children': generate_diff_list(elem1, elem2)
                    }
                }
                result.append(item)
            else:
                item = {
                    com_key: {
                        'type': 'updated',
                        'old_val': dict1.get(com_key),
                        'new_val': dict2.get(com_key)
                    }
                }
                result.append(item)

    sorted_result = sorted(result, key=lambda k: list(k.keys())[0])
    return sorted_result
