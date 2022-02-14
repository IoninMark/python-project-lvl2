from gendiff.formatters.stringify import stringify_plain_value

# flake8: noqa: C901
def format(diff):

    def stringify(item, parent_key=''):
        current_key, item_value = item
        item_type = item_value.get('type')
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == 'dict':
            children = item_value.get('children')
            new_lines = [stringify(child, key) 
                for child in list(children.items())
                if child[1].get('type') != 'equal']
            child_str = '\n'.join(new_lines)
            return child_str
        
        if item_type == 'updated':
            value1 = item_value.get('old_val')
            value2 = item_value.get('new_val')
            val1 = stringify_plain_value(value1)
            val2 = stringify_plain_value(value2)
            res_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return res_str

        if item_type == 'removed':
            res_str = f"Property '{key}' was removed"
            return res_str

        if item_type == 'added':
            value = item_value.get('value')
            val = stringify_plain_value(value)
            res_str = f"Property '{key}' was added with value: {val}"
            return res_str

    result = ''
    if diff:
        lines = [stringify(elem) 
            for elem in list(diff.items())
            if elem[1].get('type') != 'equal']
        result = '\n'.join(lines)
    return result
