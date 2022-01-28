NO_VAL = 'NO_SUCH_VALUE'

# flake8: noqa: C901
def plain(diff_list):

    def stringify_plain(current_item, parent_key=''):
        item_keys = list(current_item.keys())
        current_key = current_item.get('key')
        value1 = current_item.get('file1', NO_VAL)
        value2 = current_item.get('file2', NO_VAL)
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if 'children' in item_keys:
            children = current_item.get('children')
            new_lines = [stringify_plain(item, key) 
                for item in children 
                if 'value' not in item.keys()]
            child_str = '\n'.join(new_lines)
            return child_str

        if value1 != NO_VAL and value2 != NO_VAL:
            val1 = stringify_value(value1)
            val2 = stringify_value(value2)
            res_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return res_str
        elif value1 != NO_VAL:
            res_str = f"Property '{key}' was removed"
            return res_str
        elif value2 != NO_VAL:
            val2 = stringify_value(value2)
            res_str = f"Property '{key}' was added with value: {val2}"
            return res_str

    result = ''
    if diff_list:
        lines = [stringify_plain(item) 
            for item in diff_list 
            if 'value' not in item.keys()]
        result = '\n'.join(lines)
    return result


def stringify_value(value):
    """Function stringifies value if it is a dict"""
    replace_dict = {
        None: 'null',
        True: 'true',
        False: 'false'
    }
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        if value in replace_dict.keys() and type(value) is not int:
            return replace_dict[value]
        else:
            return value
