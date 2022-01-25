NO_VAL = 'NO_SUCH_VALUE'

# flake8: noqa: C901
def plain(diff_list):

    def stringify_plain(current_item, parent_key=''):
        current_key = current_item.get('key')
        children = current_item.get('children', NO_VAL)
        value1 = current_item.get('file1', NO_VAL)
        value2 = current_item.get('file2', NO_VAL)
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if children != NO_VAL:
            new_lines = [stringify_plain(item, key) 
                for item in children 
                if item.get('value', NO_VAL) == NO_VAL]
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
            if item.get('value', NO_VAL) == NO_VAL]
        result = '\n'.join(lines)
    return result


def stringify_value(value):
    """Function stringifies value if it is a dict"""
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value
