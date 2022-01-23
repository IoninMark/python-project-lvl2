import itertools


REPLACER = '    '
SPACE_CNT = 1
NO_VAL = 'NO_SUCH_VALUE'

# flake8: noqa: C901
def stylish(diff_list, replacer=REPLACER, space_count=SPACE_CNT):

    def stringify(current_item, depth):
        key = current_item.get('key')
        children = current_item.get('children', NO_VAL)
        value = current_item.get('value', NO_VAL)
        value1 = current_item.get('file1', NO_VAL)
        value2 = current_item.get('file2', NO_VAL)
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        changed_list = []
        res_str = ''
        if value != NO_VAL:
            val = stringify_value(value, depth + 1)
            return f"{deep_indent}  {key}: {val}"

        if children != NO_VAL:
            indent = replacer * (depth + 1)
            new_lines = [stringify(item, depth + 1) for item in children]
            child_str = '{\n' + '\n'.join(new_lines) + '\n' + indent + '  }'
            res_str = f"{deep_indent}  {key}: {child_str}"
            return res_str

        if value1 != NO_VAL:
            val1 = stringify_value(value1, depth + 1)
            file1_str = f"{deep_indent}- {key}: {val1}"
            changed_list.append(file1_str)
        if value2 != NO_VAL:
            val2 = stringify_value(value2, depth + 1)
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
    if not isinstance(value, dict):
        return value
    space = depth + space_count
    new_indent = replacer * space
    current_indent = replacer * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{new_indent}{key}: {stringify_value(val, space)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
