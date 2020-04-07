from os import path as _path


def in_container():
    path = '/proc/self/cgroup'
    return (
        _path.exists('/.dockerenv') or
        _path.isfile(path) and any('docker' in line for line in open(path))
    )
