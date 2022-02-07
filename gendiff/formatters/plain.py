from gendiff.formatters.stringify import stringify_plain_value

# flake8: noqa: C901
def plain(diff_list):

    def format(item, parent_key=''):
        current_key = item.get('key').get('value')
        item_type = item.get('key').get('type')
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == 'dict':
            children = item.get('children')
            new_lines = [format(child, key) 
                for child in children
                if child.get('key').get('type') != 'equal']
            child_str = '\n'.join(new_lines)
            return child_str
        
        if item_type == 'updated':
            value1 = item.get('value').get('old_val')
            value2 = item.get('value').get('new_val')
            val1 = stringify_plain_value(value1)
            val2 = stringify_plain_value(value2)
            res_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return res_str

        if item_type == 'removed':
            res_str = f"Property '{key}' was removed"
            return res_str

        if item_type == 'added':
            value = item.get('value')
            val = stringify_plain_value(value)
            res_str = f"Property '{key}' was added with value: {val}"
            return res_str

    result = ''
    if diff_list:
        lines = [format(elem) 
            for elem in diff_list
            if elem.get('key').get('type') != 'equal']
        result = '\n'.join(lines)
    return result
