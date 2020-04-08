# in-container [![PyPI version](https://badge.fury.io/py/in-container.svg)](https://badge.fury.io/py/in-container)[![Build Status](https://travis-ci.com/ZiggerZZ/in_container.svg?branch=master)](https://travis-ci.com/ZiggerZZ/in_container)

> Allows you to check if you program is running inside a Docker container

This is a branch with Travis CI deployment on PyPI - check out [this article](https://medium.com/@ziggerzz/deployment-of-python-package-on-pypi-with-travis-on-github-d8aa24ffcdb4).

## Install

```
$ pip install in-container
```

## Usage

```python
from in_container import in_container
print(in_container()) # True or False
```

## License

[MIT](https://github.com/ZiggerZZ/in_container/blob/master/LICENSE)
