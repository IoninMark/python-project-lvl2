import itertools
import json


NO_VAL = 'NO_SUCH_VALUE'

# flake8: noqa: C901
def _json(diff_list):

    def make_dict(current_item, dictionary):
        key = current_item.get('key')
        children = current_item.get('children', NO_VAL)
        value = current_item.get('value', NO_VAL)
        value1 = current_item.get('file1', NO_VAL)
        value2 = current_item.get('file2', NO_VAL)
        changed_dict = {}
        child_dict = {}
        if value != NO_VAL:
            dictionary[key] = value
            return
       
        if children != NO_VAL:
            for child in children:
                make_dict(child, child_dict)
            dictionary[key] = child_dict
            return

        if value1 != NO_VAL:
            changed_dict['file1'] = value1
        if value2 != NO_VAL:
            changed_dict['file2'] = value2
        dictionary[key] = changed_dict
        return
    
    res_dict = {}
    for item in diff_list:
        make_dict(item, res_dict)
    return json.dumps(res_dict)
