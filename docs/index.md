# Welcome to Dast 

**dast** provides chainable, enhanced datastructures over the well-known built-ins.

[![Build Status](https://travis-ci.org/torokmark/dast.svg?branch=master)](https://travis-ci.org/torokmark/dast)
[![Documentation Status](https://readthedocs.org/projects/dast/badge/?version=latest)](https://dast.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/dast.svg?color=blue)](https://pypi.org/project/dast/)

* *List* is an enhanced list having all the functionalities that the basic
  `list` buitl-in type has but extended with a lot of useful functions.
* *Set* is a superset, works as the general `set` type but it does a lot more
  that the basic one.
* *Dictionary* is a key-value pair container, like `dict`, which is builded with heavy functionalities.

## Install 

```sh
pip install dast
```

## Usage 

```python
from dast import List

a = List([1, 2, 3, 4, 5]) \
  .delete_if(lambda x: x % 2 == 0) \
  .map(lambda x: x * 2) \
  .chain(['a', 'b']) \
  .each_with_index() \
  .to_list() # => [[0, 2], [1, 6], [2, 10], [3, 'a'], [4, 'b]]
```

## Documentation

For further information, read the documentation that can be found: [https://dast.readthedocs.io/](https://dast.readthedocs.io/)

## Contribution

1. Fork it!
2. Make your changes!
3. Send a PR!



