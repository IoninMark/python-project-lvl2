import os


def read_file(file_name):
    return open(file_name)


def get_format(file_name):
    return os.path.splitext(file_name)[1]
