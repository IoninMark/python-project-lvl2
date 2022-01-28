NO_KEY = 'no_such_key'


def generate_diff_list(dict1, dict2):
    """Function compares files and generates
    difference list.
    [
        {
            'key': key_name,
            'type': equal/dict/removed/added/updated
            'children': [..childs {}..], - if both are dicts
            'value': val, - if values are the same
            'file1': val1,
            'file2': val2,
        }
    ]"""
    keys = sorted(list(set(dict1) | set(dict2)))
    res_list = [find_diff(dict1.get(key, NO_KEY), dict2.get(key, NO_KEY), key)
                for key in keys]
    return res_list


def find_diff(elem1, elem2, parent_key):
    if isinstance(elem1, dict) and isinstance(elem2, dict):
        keys = sorted(list(set(elem1) | set(elem2)))
        child_list = [
            find_diff(elem1.get(key, NO_KEY), elem2.get(key, NO_KEY), key)
            for key in keys]
        return {'key': parent_key, 'type': 'dict', 'children': child_list}
    if elem1 != NO_KEY and elem2 == NO_KEY:
        return {'key': parent_key, 'type': 'removed', 'file1': elem1}
    if elem2 != NO_KEY and elem1 == NO_KEY:
        return {'key': parent_key, 'type': 'added', 'file2': elem2}
    if elem1 == elem2:
        return {'key': parent_key, 'type': 'equal', 'value': elem1}
    else:
        return {
            'key': parent_key,
            'type': 'updated',
            'file1': elem1,
            'file2': elem2}
