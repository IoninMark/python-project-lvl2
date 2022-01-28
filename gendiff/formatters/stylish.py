import itertools


REPLACER = '  '
SPACE_CNT = 1


# flake8: noqa: C901
def stylish(diff_list, replacer=REPLACER, space_count=SPACE_CNT):

    def stringify(current_item, depth):
        item_keys = list(current_item.keys())
        key = current_item.get('key')
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        changed_list = []
        res_str = ''
        if 'value' in item_keys:
            value = current_item.get('value')
            val = stringify_value(value, depth + 2)
            return f"{deep_indent}  {key}: {val}"

        if 'children' in item_keys:
            children = current_item.get('children')
            indent = replacer * (depth + 2)
            new_lines = [stringify(item, depth + 2) for item in children]
            child_str = '{\n' + '\n'.join(new_lines) + '\n' + indent + '}'
            res_str = f"{deep_indent}  {key}: {child_str}"
            return res_str

        if 'file1' in item_keys:
            value1 = current_item.get('file1')
            val1 = stringify_value(value1, depth + 2)
            file1_str = f"{deep_indent}- {key}: {val1}"
            changed_list.append(file1_str)

        if 'file2' in item_keys:
            value2 = current_item.get('file2')
            val2 = stringify_value(value2, depth + 2)
            file2_str = f"{deep_indent}+ {key}: {val2}"
            changed_list.append(file2_str)
        res_str = '\n'.join(changed_list)
        return res_str

    result = ''
    if diff_list:
        lines = [stringify(item, 0) for item in diff_list]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result


def stringify_value(value, depth, replacer=REPLACER, space_count=SPACE_CNT):
    """Function stringifies value if it is a dict"""
    replace_dict = {
        None: 'null',
        True: 'true',
        False: 'false'
    }
    if not isinstance(value, dict):
        if value in replace_dict.keys():
            return replace_dict[value]
        else:
            return value
    space = depth + space_count * 2
    new_indent = replacer * space
    current_indent = replacer * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{new_indent}{key}: {stringify_value(val, space)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
