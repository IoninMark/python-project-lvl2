import itertools
from gendiff.diff_dict_generator import ADDED, DICT, EQUAL, REMOVED, UPDATED


REPLACER = '  '
SPACE_CNT = 1


# flake8: noqa: C901
def format(diff):

    replacer = REPLACER
    space_count = SPACE_CNT   
    
    def stringify(item, depth):
        key, item_value = item
        item_type = item_value.get('type')
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        item_str = ''

        if item_type == DICT:
            children = item_value.get('children')
            indent = replacer * (depth + 2)
            new_lines = [
                stringify(child, depth + 2) 
                for child in list(children.items())
            ]
            child_str = '{\n' + '\n'.join(new_lines) + '\n' + indent + '}'
            item_str = f"{deep_indent}  {key}: {child_str}"
            return item_str

        if item_type == UPDATED:
            value1 = item_value.get('old_val')
            value2 = item_value.get('new_val')
            val1 = stringify_value(value1, depth + 2, REPLACER, SPACE_CNT)
            val2 = stringify_value(value2, depth + 2, REPLACER, SPACE_CNT)
            res_str1 = f"{deep_indent}- {key}: {val1}"
            res_str2 = f"{deep_indent}+ {key}: {val2}"
            item_str = res_str1 + '\n' + res_str2
            return item_str

        value = item_value.get('value')
        val = stringify_value(value, depth + 2, REPLACER, SPACE_CNT)

        if item_type == EQUAL:
            return f"{deep_indent}  {key}: {val}"

        if item_type == REMOVED:
            item_str = f"{deep_indent}- {key}: {val}"
            return item_str

        if item_type == ADDED:
            item_str = f"{deep_indent}+ {key}: {val}"
            return item_str

    result = ''
    if diff:
        lines = [stringify(elem, 0) for elem in list(diff.items())]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result


def stringify_value(value, depth, replacer='  ', space_cnt=1):
    """Function stringifies value"""
    replace_dict = {
        None: 'null',
        True: 'true',
        False: 'false'
    }
    if not isinstance(value, dict):
        if value in replace_dict.keys() and type(value) is not int:
            return replace_dict[value]
        else:
            return value
    space = depth + space_cnt * 2
    new_indent = replacer * space
    current_indent = replacer * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{new_indent}{key}: {stringify_value(val, space)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
