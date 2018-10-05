import os


def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_resource(file):
    return os.path.join(module_path(), "res", file)
