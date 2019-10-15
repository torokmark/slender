<h1 id="slender.set.Set">Set</h1>

```python
Set(self, s=set())
```

## &

```python
Set.__and__(self, other: Set[VT]) -> Set[VT]
```

Returns the intersection of self and `other`.

*&* and *intersection* are aliases.

## ==

```python
Set.__eq__(self, other: object) -> bool
```

Returns `True` if self and `other` are equal otherwise `False`.

## -

```python
Set.__sub__(self, other: Set[VT]) -> Set[VT]
```

Returns the difference of two sets.

*-* and *subtract* are aliases.

## >

```python
Set.__ge__(self, other: Set[VT]) -> bool
```

Returns `True` if self is superset of `other`.

*>* and *ispropersuperset* are aliases.

## >=

```python
Set.__gt__(self, other: Set[VT]) -> bool
```

Returns `True` if self is proper superset of `other`.

*>=* and *issuperset* are aliases.

## <<

```python
Set.__lshift__(self, obj: VT) -> Set[VT]
```

Add one element to the `Set` object.

*<<* and *add* are aliases.

```python
s = Set({1, 2, 3}) << 1
# => {1, 2, 3}
s = Set({1, 2, 3}) << 4
# => {1, 2, 3, 4}
```

## <=

```python
Set.__le__(self, other: Set[VT]) -> bool
```

Returns `True` if self is subset of `other`. Otherwise it returns `False`.

*<=* *issubset* are aliases.

## <

```python
Set.__lt__(self, other: Set[VT]) -> bool
```

Returns `True` if self is proper subset of `other`. Otherwise it returns `False`.

*<* and *ispropersubset* are aliases.

## |

```python
Set.__or__(self, other: Set[VT]) -> Set[VT]
```

Returns the union of the current object and `other`.

*|* and *union* are aliases.

```python
Set({1, 2, 3}) | Set({2, 3, 4})
# => {1, 2, 3, 4}
```

## add

```python
Set.add(self, obj: VT) -> Set[VT]
```

Returns a new set containing the newly added element.

*<<* and *add* are aliases.

## delete

```python
Set.delete(self, obj: VT) -> Set[VT]
```

Returns a new set without the `obj` element.

## delete_if

```python
Set.delete_if(self, callback: typing.Callable[[VT], bool]) -> Set[VT]
```

Returns a new set without containing all elements that passed the `callback` condition.

*reject* and *delete_if* are aliases.

```python
e = Set({1, 2, 3, 4})
e.delete_if(lambda x: x % 2 == 0)
# => {1, 3}
```

## difference

```python
Set.difference(self, other: Set[VT]) -> Set[VT]
```

Returns the difference of the current object and `other`.

*difference* and *delete_if* are aliases.

```python
e = Set({1, 2, 3, 4})
o = Set({2, 3})
e.difference(o)
# => {1, 4}
```

## isdisjoint

```python
Set.isdisjoint(self, other: Set[VT]) -> bool
```

Returns `True` if self and `other` sets are disjoint to each other. Otherwise `False`.

## divide

```python
Set.divide(self, callback: typing.Callable[[VT, VT], bool]) -> Set[VT]
```

It groups elements based on the `callback` condition.

```python
e = Set({1, 3, 4, 6, 9, 10, 11})
e.divide(lambda i, j: abs(i - j) == 1)
# => { Set({1}), Set({3, 4}), Set({6}), Set({9, 10, 11}) }
```

## emtpy

```python
Set.empty(self) -> bool
```

Returns wether the current object is empty or not.

## flatten

```python
Set.flatten(self) -> Set[VT]
```

Returns a flat-out set.

## hash

```python
Set.__hash__(self) -> int
```

Returns the hash value of the instance.

## include

```python
Set.include(self, obj) -> bool
```

Return `True` if `obj` is in the current set object, otherwise it returns `False`.

## intersect

```python
Set.intersect(self, other: Set[VT]) -> bool
```

Returns `True` if current object and `other` has mutual values, `False` otherwise.

## intersection

```python
Set.intersection(self, other: Set[VT]) -> Set[VT]
```

Returns a new set containing the intersection of the current and `other` objects.

## ispropersubset

```python
Set.ispropersubset(self, other: Set[VT]) -> bool
```

Returns `True` if self is proper subset of `other`. `False` otherwise.

## ispropersuperset

```python
Set.ispropersuperset(self, other: Set[VT]) -> bool
```

Returns `True` if self is proper superset of `other`. `False` otherwise.

## issubset

```python
Set.issubset(self, other: Set[VT]) -> bool
```

Returns `True` if self is subset of `other`, `False` otherwise.

## issuperset

```python
Set.issuperset(self, other: Set[VT]) -> bool
```

Returns `True` if self is superset of `other`, `False` otherwise.

## iter

```python
Set.__iter__(self)
```

Returns an iterator object of the instance.

## keep_if

```python
Set.keep_if(self, callback: typing.Callable[[VT], bool]) -> Set[VT]
```

Return set of elements on which `callback` condition returns `True`.

*keep_if* and *select* are aliases.

```python
e = Set({1, 2, 3, 4})
e.keep_if(lambda x: x % 2 == 0)
# => {2, 4}
```

## len

```python
Set.__len__(self) -> int
```

Returns the number of elements in the set.

## map

```python
Set.map(self, callback: typing.Callable[[VT], typing.Any]) -> Set[typing.Any]
```

Retuns a new set containing transformed element based on `callback`.

If `callback` returns the same value on different elements, the resulted set contains the values without duplication.

## reject

```python
Set.reject(self, callback: typing.Callable[[VT], bool]) -> Set[VT]
```

Returns a new set without containing all elements that passed the `callback` condition.

*reject* and *delete_if* are aliases.

```python
e = Set({1, 2, 3, 4})
e.reject(lambda x: x % 2 == 0)
# => {1, 3}
```

## select

```python
Set.select(self, callback: typing.Callable[[VT], bool]) -> Set[VT]
```

Return set of elements on which `callback` condition returns `True`.

*keep_if* and *select* are aliases.

```python
e = Set({1, 2, 3, 4})
e.select(lambda x: x % 2 == 0)
# => {2, 4}
```

## str

```python
Set.__str__(self) -> str
```

Returns the string representation of the set.

## subtract

```python
Set.subtract(self, other: Set[VT]) -> Set[VT]
```

Returns the difference of two sets.

## to_set

```python
Set.to_set(self) -> typing.Set[VT]
```

Returns the current object as a built-in `set`.

## union

```python
Set.union(self, other: Set[VT]) -> Set[VT]
```

Returns the union of the current object and `other`.

```python
Set({1, 2, 3}).union({2, 3, 4})
# => {1, 2, 3, 4}
```

