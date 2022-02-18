from collections import OrderedDict


ADDED = 'added'
DICT = 'dict'
EQUAL = 'equal'
REMOVED = 'removed'
UPDATED = 'updated'


def generate_diff_dict(dict1, dict2):
    """Function compares files and generates
    difference dictionary.
        {
            'key': {
                'type': equal/dict/removed/added/updated,
                'value': value
                'old_val': old_value - for updated
                'new_val': new_value - for updated
                'children': [..childs {}..] - for dict
                }
        }
    """
    result = {}
    set1 = set(dict1)
    set2 = set(dict2)
    com_keys = set1 & set2
    add_keys = set2 - set1
    dell_keys = set1 - set2
    for add_key in add_keys:
        result[add_key] = {
            'type': ADDED,
            'value': dict2.get(add_key)
        }

    for dell_key in dell_keys:
        result[dell_key] = {
            'type': REMOVED,
            'value': dict1.get(dell_key)
        }

    for com_key in com_keys:
        elem1 = dict1.get(com_key)
        elem2 = dict2.get(com_key)
        if elem1 == elem2:
            result[com_key] = {
                'type': EQUAL,
                'value': elem1
            }
        else:
            if isinstance(elem1, dict) and isinstance(elem2, dict):
                result[com_key] = {
                    'type': DICT,
                    'children': generate_diff_dict(elem1, elem2)
                }
            else:
                result[com_key] = {
                    'type': UPDATED,
                    'old_val': elem1,
                    'new_val': elem2
                }

    sorted_result = OrderedDict(sorted(result.items(), key=lambda k: k))
    return sorted_result
