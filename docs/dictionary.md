<h1 id="slender.dictionary.Dictionary">Dictionary</h1>

```python
Dictionary(self, s={})
```

## <

```python
Dictionary.__lt__(self, other: Dictionary[KT, VT]) -> bool
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
Dictionary.__le__(self, other: Dictionary[KT, VT]) -> bool
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
Dictionary.__gt__(self, other: Dictionary[KT, VT]) -> bool
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
Dictionary.compact(self) -> Dictionary[KT, VT]
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
Dictionary.delete_if(self, callback: typing.Callable[[KT, VT], bool]) -> Dictionary[KT, VT]
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
Dictionary.each(self, callback: typing.Callable[[KT, VT], typing.Optional[typing.Any]]) -> Dictionary[KT, VT]
```

Iterates over the dictionary's key-value pairs and call `callback` on each
element.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.each(lambda k, v: k + str(v))
# => Dictionary[str, int]({'a': 'a1', 'b': 'b2', 'c': 'c3'})
```

## each_key

```python
Dictionary.each_key(self, callback: typing.Callable[[KT], typing.Optional[typing.Any]]) -> Dictionary[KT, VT]
```

Iterates over the keyset of the dictionary and assign the values to a key
returned as the result of `callback`.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.each_key(lambda k: k + 'a')
# => Dictionary[str, int]({'aa': 1, 'ba': 2, 'ca': 3})
```

## each_value

```python
Dictionary.each_value(self, callback: typing.Callable[[VT], typing.Optional[typing.Any]]) -> Dictionary[KT, VT]
```

Iterates over the pairs and assign the modified values to their keys.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.each_value(lambda v: v + 1)
# => Dictionary[str, int]({'a': 2, 'b': 3, 'c': 4})
```

## empty

```python
Dictionary.empty(self) -> bool
```

Returns `True` if dictionary has no element.

## get

```python
Dictionary.get(self, key, callback: typing.Callable[[KT], typing.Any] =None) -> typing.Optional[typing.Any]
```

Returns value if dictionary contains key. If key is not in the dictionary it
returns the result of the `callback` on the key. If no `callback` is given, it
returns the default value.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.get('a')
# => 1
d1 = Dictionary[str, int]({})
d1.get('a', lambda k: k + '---')
# => 'a---' 
```

## get_values

```python
Dictionary.get_values(self, *keys: typing.List[KT], callback =None) -> typing.List[VT]
```

Returns the list of values based on the keys parameter. If a key is not present
and `callback` is not `None`
than `callback` is called on that key and that's return value is included in the
result list.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.get_values('a', 'b')
# => [1, 2]
d1 = Dictionary[str, int]({})
d1.get_values('a', 'b', callback=lambda k: k.upper())
# => ['A', 'B']
```

## flatten

```python
Dictionary.flatten(self, level: int =0) -> typing.List[typing.Any]
```

Flats out the embedded dictionaries based on level. 

```python
d1 = Dictionary[str, int]({'a': 1, 'b': [2, 3, [4, 5]]})
d1.flatten(2)
# => ['a', 1, 'b', 2, 3, 4, 5]
```

## has_key

```python
Dictionary.has_key(self, key: KT) -> bool
```

Checks whether dictionary has the given key.

## has_value

```python
Dictionary.has_value(self, value: VT) -> bool
```

Checks whether the dictionary has the given value.

## in

```python
Dictionary.__contains__(self, key: KT) -> bool
```

Checks whether dictionary has the given key.

## invert

```python
Dictionary.invert(self) -> Dictionary[KT, VT]
```

Takes values as keys and assigns given key to its value.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2})
d1.invert()
# => Dictionary[str, int]({1: 'a', 2: 'b'})
```

## keep_if

```python
Dictionary.keep_if(self, callback: typing.Callable[[KT, VT], bool]) -> Dictionary[KT, VT]
```

Selects those key-value pairs that match according to the `callback`.

*keep_if* is an alias for *select*.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
d1.keep_if(lambda k, v: v % 2 == 0)
# => Dictionary[str, int]({'b': 2, 'd': 4}) 
```

## len 

```python
Dictionary.__len__(self) -> int
```

Returns the number of key-value pairs of the dictionary.

## merge

```python
Dictionary.merge(self, other: 'Dictionary[KT, VT]', callback: typing.Callable[[KT, VT, VT], VT]=None) -> Dictionary[KT, VT]
```

Returns a new hash that combines the contents of the receiver and the contents of the given hashes.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2})
d2 = Dictionary[str, int]({'c': 3, 'd': 4})
d1.merge(d2)
# => Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
```

## select

```python
Dictionary.select(self, callback: typing.Callable[[KT, VT], bool]) -> Dictionary[KT, VT]
```
Returns a new dictionary consisting of key-value pairs for which the `callback` returns True.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
d1.select(lambda k, v: v % 2 == 0)
# => Dictionary[str, int]({'b': 2, 'd': 4}) 
```

## size

```python
Dictionary.size(self) -> int
```

Returns the number of key-value pairs in the dictionary.

*size* is an alias for *len*.

## slice

```python
Dictionary.slice(self, *keys) -> Dictionary[KT, VT]
```

Returns a dictionary containing only the given keys and their values.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
d1.slice('a', 'b')
# => Dictionary[str, int]({'a': 1, 'b': 2})
```

## to_dict

```python
Dictionary.to_dict(self) -> typing.Dict[KT, VT]
```

Returns an instance of `dict` containing all the key-value pairs.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
d1.to_dict()
# => {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## to_list

```python
Dictionary.to_list(self) -> typing.List[typing.List[typing.Any]]
```

Returns list of key-value pair where key and value are in a list.

```python
d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
d1.to_list()
# => [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
 
```



