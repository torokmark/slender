# Welcome to Slender

**Slender** provides chainable, enhanced datastructures over the well-known built-ins.

[![Build Status](https://travis-ci.org/torokmark/slender.svg?branch=master)](https://travis-ci.org/torokmark/slender)
[![Documentation Status](https://readthedocs.org/projects/slender/badge/?version=latest)](https://slender.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/slender.svg?color=blue)](https://pypi.org/project/slender/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slender.svg)](https://github.com/torokmark/slender)
[![PyPI - License](https://img.shields.io/pypi/l/slender.svg)](https://github.com/torokmark/slender/blob/master/LICENSE.md)


* *List* is an enhanced list having all the functionalities that the basic
  `list` buitl-in type has but extended with a lot of useful functions.
* *Set* is a superset, works as the general `set` type but it does a lot more
  that the basic one.
* *Dictionary* is a key-value pair container, like `dict`, which is builded with heavy functionalities.
* *Tuple* is a finate ordered list over the built-in `tuple`.

## Install 

```sh
pip install dast
```

## Usage 

```python
from slender import List

a = List([1, 2, 3, 4, 5]) \
  .delete_if(lambda x: x % 2 == 0) \
  .map(lambda x: x * 2) \
  .chain(['a', 'b']) \
  .each_with_index() \
  .to_list() # => [[0, 2], [1, 6], [2, 10], [3, 'a'], [4, 'b]]
```

## Documentation

For further information, read the documentation that can be found: https://slender.readthedocs.io/
The project page is https://torokmark.github.io/slender

## Contribution

1. Fork it!
2. Make your changes!
3. Send a PR!



