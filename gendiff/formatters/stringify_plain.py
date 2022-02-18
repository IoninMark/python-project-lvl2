def stringify_value(value):
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
