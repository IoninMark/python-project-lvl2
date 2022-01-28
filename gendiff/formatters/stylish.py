from gendiff.formatters.stringify import stringify_styl_value


REPLACER = '  '
SPACE_CNT = 1


# flake8: noqa: C901
def stylish(diff_list, replacer=REPLACER, space_count=SPACE_CNT):

    def stringify(current_item, depth):
        key = current_item.get('key')
        item_type = current_item.get('type')
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        res_str = ''
        if item_type == 'equal':
            value = current_item.get('value')
            val = stringify_styl_value(value, depth + 2, REPLACER, SPACE_CNT)
            return f"{deep_indent}  {key}: {val}"

        elif item_type == 'dict':
            children = current_item.get('children')
            indent = replacer * (depth + 2)
            new_lines = [stringify(item, depth + 2) for item in children]
            child_str = '{\n' + '\n'.join(new_lines) + '\n' + indent + '}'
            res_str = f"{deep_indent}  {key}: {child_str}"
            return res_str

        elif item_type == 'removed':
            value1 = current_item.get('file1')
            val1 = stringify_styl_value(value1, depth + 2, REPLACER, SPACE_CNT)
            res_str = f"{deep_indent}- {key}: {val1}"
            #changed_list.append(file1_str)
            return res_str

        elif item_type == 'added':
            value2 = current_item.get('file2')
            val2 = stringify_styl_value(value2, depth + 2, REPLACER, SPACE_CNT)
            res_str = f"{deep_indent}+ {key}: {val2}"
            return res_str
        
        else:
            value1 = current_item.get('file1')
            value2 = current_item.get('file2')
            val1 = stringify_styl_value(value1, depth + 2, REPLACER, SPACE_CNT)
            val2 = stringify_styl_value(value2, depth + 2, REPLACER, SPACE_CNT)
            res_str1 = f"{deep_indent}- {key}: {val1}"
            res_str2 = f"{deep_indent}+ {key}: {val2}"
            res_str = res_str1 + '\n' + res_str2
            return res_str

    result = ''
    if diff_list:
        lines = [stringify(item, 0) for item in diff_list]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result
