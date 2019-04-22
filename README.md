# Welcome to Dast 

**dast** contains types that are similar to the well-known built-in datastructures
on proteins.

* *List* is an enhanced list having all the functionalities that the basic
  `list` buitl-in type has but extended with a lot of useful functions.
* *Set* is a superset, works as the general `set` type but it does a lot more
  that the basic one.
* *Dictionary* is a key-value pair container with builded heavy functionality. 

## Install 

```sh
pip install dast
```

## Usage 

```python
from dast import List

a = List([1, 2, 3, 4, 5])
  .delete_if(lambda x: x % 2 == 0)
  .map(lambda x: x * 2)
  .chain(['a', 'b'])
  .each_with_index()
  .to_list() # => [[0, 2], [1, 6], [2, 10], [3, 'a'], [4, 'b]]
```
## Contribution

1. Fork it!
2. Make your changes!
3. Send an PR!

