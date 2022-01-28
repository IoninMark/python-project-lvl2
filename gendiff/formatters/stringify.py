import itertools


def stringify_styl_value(value, depth, replacer='  ', space_cnt=1):
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
        lines.append(f'{new_indent}{key}: {stringify_styl_value(val, space)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def stringify_plain_value(value):
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
