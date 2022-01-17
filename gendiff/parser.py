def generate_diff_str(dict1, dict2):
    """Function generates the formatted string with difference
    between two files."""
    keys = sorted(list(set(dict1) | set(dict2)))
    result = [find_diff_by_key(dict1, dict2, key) for key in keys]
    res_str = '\n'.join(result)
    if res_str != '':
        return '{\n' + res_str + '\n}'
    else:
        return ''


def find_diff_by_key(dict1, dict2, key):
    """Function compares files by key and generates
    difference string for this key."""
    elem1 = dict1.get(key, '')
    elem2 = dict2.get(key, '')
    if elem1 != '' and elem2 == '':
        return f"- {key}: {elem1}"
    if elem2 != '' and elem1 == '':
        return f"+ {key}: {elem2}"
    if elem1 == elem2:
        return f"{key}: {elem1}"
    else:
        return f"- {key}: {elem1}\n+ {key}: {elem2}"
