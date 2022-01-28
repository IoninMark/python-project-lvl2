import itertools
import json


# flake8: noqa: C901
def _json(diff_list):

    def make_dict(current_item, dictionary):
        key = current_item.get('key')
        item_type = current_item.get('type')
        changed_dict = {}
        child_dict = {}
        if item_type == 'equal':
            value = current_item.get('value')
            dictionary[key] = value
            return
       
        if item_type == 'dict':
            children = current_item.get('children')
            for child in children:
                make_dict(child, child_dict)
            dictionary[key] = child_dict
            return

        if item_type == 'removed' or item_type == 'updated':
            value1 = current_item.get('file1')
            changed_dict['file1'] = value1
        if item_type == 'added' or item_type == 'updated':
            value2 = current_item.get('file2')
            changed_dict['file2'] = value2
        dictionary[key] = changed_dict
        return
    
    res_dict = {}
    for item in diff_list:
        make_dict(item, res_dict)
    return json.dumps(res_dict)
