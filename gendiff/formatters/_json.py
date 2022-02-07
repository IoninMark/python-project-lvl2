import itertools
import json


# flake8: noqa: C901
def _json(diff_list):

    def format(item, dictionary):
        key = item.get('key').get('value')
        item_type = item.get('key').get('type')
        child_dict = {}
        
        if item_type == 'dict':
            children = item.get('children')
            for child in children:
                format(child, child_dict)
            dictionary[key] = child_dict
            return
        
        if item_type == 'updated':
            value1 = item.get('value').get('old_val')
            value2 = item.get('value').get('new_val')
            dictionary[key] = {
                'type': item_type,
                'old_value': value1,
                'new_value': value2
                }
            return
        
        value = item.get('value')
        dictionary[key] = {
                'type': item_type,
                'value': value
                }
        return
    
    res_dict = {}
    for elem in diff_list:
        format(elem, res_dict)
    return json.dumps(res_dict)
