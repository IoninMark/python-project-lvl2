from gendiff.formatters.stringify_plain import stringify_value
from gendiff.diff_dict_generator import ADDED, DICT, EQUAL, REMOVED, UPDATED

# flake8: noqa: C901
def format(diff):

    def stringify(item, parent_key=''):
        current_key, item_value = item
        item_type = item_value.get('type')
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == DICT:
            children = item_value.get('children')
            new_lines = [stringify(child, key) 
                for child in list(children.items())
                if child[1].get('type') != EQUAL]
            child_str = '\n'.join(new_lines)
            return child_str
        
        if item_type == UPDATED:
            value1 = item_value.get('old_val')
            value2 = item_value.get('new_val')
            val1 = stringify_value(value1)
            val2 = stringify_value(value2)
            item_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return item_str

        if item_type == REMOVED:
            item_str = f"Property '{key}' was removed"
            return item_str

        if item_type == ADDED:
            value = item_value.get('value')
            val = stringify_value(value)
            item_str = f"Property '{key}' was added with value: {val}"
            return item_str

    result = ''
    if diff:
        lines = [stringify(elem) 
            for elem in list(diff.items())
            if elem[1].get('type') != EQUAL]
        result = '\n'.join(lines)
    return result
