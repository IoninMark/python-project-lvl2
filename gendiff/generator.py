import json


def generate_diff(file1, file2):
    dict1 = json.load(open(file1))
    dict2 = json.load(open(file2))
    keys = sorted(list(set(dict1) | set(dict2)))
    result = []
    for key in keys:
        result.append(find_diff_by_key(dict1, dict2, key))
    res_str = '\n'.join(result)
    return '{\n' + res_str + '\n}'


def find_diff_by_key(dict1, dict2, key):
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
