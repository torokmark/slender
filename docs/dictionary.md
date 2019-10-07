<h1 id="slender.dictionary.Dictionary">Dictionary</h1>

```python
Dictionary(self, s={})
```

## <

```python
Dictionary.__lt__(self, other: 'Dictionary[KT, VT]') -> bool
```

Checks whether the right dictionary contains the left one.

```python
d1 = Dictionary({'a': 1, 'b': 2})
d2 = Dictionary({'a': 1, 'b': 2, 'c': 3})
d3 = Dictionary({'a': 1, 'b': 2, 'c': 3})
d4 = Dictionary({'a': 1, 'b': 2, 'c': 0})
d1 < d2 # => True
d2 < d1 # => False
d2 < d3 # => False 
d2 < d4 # => False
```

## <=

```python
Dictionary.__le__(self, other: 'Dictionary[KT, VT]') -> bool
```

Checks whether the right dictionary contains or equals to the left one.

```python
d1 = Dictionary({'a': 1, 'b': 2})
d2 = Dictionary({'a': 1, 'b': 2, 'c': 3})
d3 = Dictionary({'a': 1, 'b': 2, 'c': 3})
d4 = Dictionary({'a': 1, 'b': 2, 'c': 0})
d1 <= d2 # => True
d2 <= d1 # => False
d2 <= d3 # => True 
d2 <= d4 # => False
```

## ==

```python
Dictionary.__eq__(self, other: object) -> bool
```

Checks whether the two dictionary is equivalent based on their key-value pairs.

## >

```python
Dictionary.__gt__(self, other: 'Dictionary[KT, VT]') -> bool
```

Checks whether the left dictionary contains the left one.

## >=

```python
Dictionary.__ge__(self, other) -> bool
```

Checks whether the left dictionary contains or equals to the left one.

## []

```python
Dictionary.__getitem__(self, key: KT) -> VT

Dictionary.__setitem__(self, key: KT, value: VT) -> None
```

Supports reading a value on a given key and assigning new value via `[]` operator.

## any

```python
Dictionary.any(self, callback: typing.Callable[[KT, VT], bool]) -> bool
```

Checks wether any element is `True`. If all of them are `False` it returns `False`.

Type of *callback* is `typing.Callable` and returns bool.

## assoc

```python
Dictionary.assoc(self, key: KT) -> typing.Optional[typing.List[typing.Any]]
```

Checks whether the dictionary contains the given key.

```python
d = Dictionary({'a': 1, 'b': 2})
d.assoc('b') # => ['b', 2]
```

## compact

```python
Dictionary.compact(self) -> 'Dictionary[KT, VT]'
```

Removes key-values pairs where value is `None`.

```python
Dictionary({'a': None, 'b': 1, 'c': None}).compact() # => Dictionary({'b': 1})
```

## default

```python
Dictionary.default(self, key: KT) -> None
```

It sets the default value of the dictionary.

## delete

```python
Dictionary.delete(self, key: KT, callback: typing.Callable[[KT], VT] =None) -> typing.Optional[VT]
```

Deletes the key-value if `key` exists, else executes callback with the parameter
key. If `callback` is `None`, it returns `None`.

## delete_if

```python
Dictionary.delete_if(self, callback: typing.Callable[[KT, VT], bool]) -> 'Dictionary[KT, VT]'
```

Deletes all key-value pairs where `callback` is `True` on the given pair.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.delete_if(lambda k, v: k=='a').to_dict()
# => {'b': 2, 'c': 3}
```

## dig

```python
Dictionary.dig(self, *keys) -> typing.Optional[VT]
```

Extracts the nested value specified by the sequence of key objects by calling 
dig at each step, returning `None` if any intermediate step is `None`.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
d1.dig('b', 'bb', 'bbb')
# => 2
d1 = Dictionary[str, int]({'a': 1, 'b': {'ba':1, 'bb': {'bba': 1, 'bbb': 2}}, 'c': 3})
d1.dig('b', 'cbb', 'bbc')
# => None
```

## each

```python
```


## each_key

## each_value

## empty

## get

## get_values

## flatten

## has_key

## has_value

## in

## invert

## keep_if

## len 

## merge

## select

## size

## slice

## to_list

## to_dict


