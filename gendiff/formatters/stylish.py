from hashlib import new
from gendiff.formatters.stringify import stringify_styl_value


REPLACER = '  '
SPACE_CNT = 1


# flake8: noqa: C901
def format(diff, replacer=REPLACER, space_count=SPACE_CNT):

    def stringify(item, depth):
        key, item_value = item
        item_type = item_value.get('type')
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        res_str = ''

        if item_type == 'dict':
            children = item_value.get('children')
            indent = replacer * (depth + 2)
            new_lines = [
                stringify(child, depth + 2) 
                for child in list(children.items())
            ]
            child_str = '{\n' + '\n'.join(new_lines) + '\n' + indent + '}'
            res_str = f"{deep_indent}  {key}: {child_str}"
            return res_str

        if item_type == 'updated':
            value1 = item_value.get('old_val')
            value2 = item_value.get('new_val')
            val1 = stringify_styl_value(value1, depth + 2, REPLACER, SPACE_CNT)
            val2 = stringify_styl_value(value2, depth + 2, REPLACER, SPACE_CNT)
            res_str1 = f"{deep_indent}- {key}: {val1}"
            res_str2 = f"{deep_indent}+ {key}: {val2}"
            res_str = res_str1 + '\n' + res_str2
            return res_str

        value = item_value.get('value')
        val = stringify_styl_value(value, depth + 2, REPLACER, SPACE_CNT)

        if item_type == 'equal':
            return f"{deep_indent}  {key}: {val}"

        if item_type == 'removed':
            res_str = f"{deep_indent}- {key}: {val}"
            return res_str

        if item_type == 'added':
            res_str = f"{deep_indent}+ {key}: {val}"
            return res_str

    result = ''
    if diff:
        lines = [stringify(elem, 0) for elem in list(diff.items())]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result
