from os.path import exists as _exists
def in_container():
    return _exists('/.dockerenv')