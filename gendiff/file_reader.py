def read_file(file_name):
    return open(file_name)


def get_format(file_name):
    return file_name.split('.')[-1]
