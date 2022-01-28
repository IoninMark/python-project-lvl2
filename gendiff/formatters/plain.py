from gendiff.formatters.stringify import stringify_plain_value

# flake8: noqa: C901
def plain(diff_list):

    def stringify_plain(current_item, parent_key=''):
        current_key = current_item.get('key')
        item_type = current_item.get('type')
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == 'dict':
            children = current_item.get('children')
            new_lines = [stringify_plain(item, key) 
                for item in children 
                if item.get('type') != 'equal']
            child_str = '\n'.join(new_lines)
            return child_str

        if item_type == 'updated':
            value1 = current_item.get('file1')
            value2 = current_item.get('file2')
            val1 = stringify_plain_value(value1)
            val2 = stringify_plain_value(value2)
            res_str = f"Property '{key}' was updated. From {val1} to {val2}"
            return res_str

        if item_type == 'removed':
            res_str = f"Property '{key}' was removed"
            return res_str

        if item_type == 'added':
            value2 = current_item.get('file2')
            val2 = stringify_plain_value(value2)
            res_str = f"Property '{key}' was added with value: {val2}"
            return res_str

    result = ''
    if diff_list:
        lines = [stringify_plain(item) 
            for item in diff_list 
            if item.get('type') != 'equal']
        result = '\n'.join(lines)
    return result
