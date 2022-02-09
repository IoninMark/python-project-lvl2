from gendiff.formatters.stringify import stringify_plain_value

# flake8: noqa: C901
def format(diff_list):

    def stringify(item, parent_key=''):
        current_key = list(item.keys())[0]
        item_type = item.get(current_key).get('type')
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == 'dict':
            children = item.get(current_key).get('children')
            new_lines = [stringify(child, key) 
                for child in children
                if list(child.values())[0].get('type') != 'equal']
            child_str = '\n'.join(new_lines)
            return child_str
        
        if item_type == 'updated':
            value1 = item.get(current_key).get('old_val')
            value2 = item.get(current_key).get('new_val')
            val1 = stringify_plain_value(value1)
            val2 = stringify_plain_value(value2)
            res_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return res_str

        if item_type == 'removed':
            res_str = f"Property '{key}' was removed"
            return res_str

        if item_type == 'added':
            value = item.get(current_key).get('value')
            val = stringify_plain_value(value)
            res_str = f"Property '{key}' was added with value: {val}"
            return res_str

    result = ''
    if diff_list:
        lines = [stringify(elem) 
            for elem in diff_list
            if list(elem.values())[0].get('type') != 'equal']
        result = '\n'.join(lines)
    return result
