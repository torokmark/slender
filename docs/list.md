<h1 id="dast.list.List">List</h1>

```python
List(self, a=[])
```

## all

```python
List.all(self, callback)
```

Checks wether all elements are `True`. If one is `False` it returns `False`.

*callback* can be regex or lambda.

## any

```python
List.any(self, callback)
```

Checks wether any element is `True`. If all of them are `False` it returns `False`.

*callback* can be regex or lambda.

## append

```python
List.append(self, obj)
```

Appends one element to the list.

Returns new `List` object containing the appended element.

## chain

```python
List.chain(self, other)
```

Appends all elements given as a `list`, or `List`

Returns new `List` object containing all the appended elements.

## chunk

```python
List.chunk(self, callback)
```

Divides list into sublists based on wether the callback returns `True` or `False` on elements.

```python
e = List([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
e.chunk(lambda x: x % 2 == 0)
# => [[False, [3, 1]], [True, [4]], [False, [1, 5, 9]], [True, [2, 6]], [False, [5, 3, 5]]]
```

## chunk_while

```python
List.chunk_while(self, callback)
```

Divides list into sublist based on lambda expression.

```python
e = List([1,2,4,9,10,11,12,15,16,19,20,21])
e.chunk_while(lambda i, j: i + 1 == j)
# => [[1, 2], [4], [9, 10, 11, 12], [15, 16], [19, 20, 21]]
```

## compact

```python
List.compact(self)
```

Removes `None` elements from list.

## concat

```python
List.concat(self, other)
```

Concatenates `other` to self.

## count

```python
List.count(self, callback=None)
```

Returns length of self if `callback` is not given.

Returns number of elements if `callback` is `True` on them.

## cycle

```python
List.cycle(self, num=-1, callback=None)
```

If no parameters are given, it iterates over the list infinitely and yields the next element.

If `num` is given, it yields the list as many times.

If `callback` is given it is applied on each element before yield.

```python
e = List(['a', 'b', 'c'])
e.cycle(2, lambda x: x.upper())
# => iterator over : ['A', 'B', 'C', 'A', 'B', 'C']
```

## delete

```python
List.delete(self, obj)
```

Deletes all elements from list if they are equal to `obj`

## delete_at

```python
List.delete_at(self, idx)
```

Deletes the element at the given index.

Returns `List` instance of the modified list.

## delete_if

```python
List.delete_if(self, callback)
```

Deletes all elements on which `callback` is `True`.

Alias for *reject*.

```python
e = List([5, 3, 5, 2, 4])
e.delete_if(lambda x: x > 3)
# => [3, 2]
```

## difference

```python
List.difference(self, other)
```

Takes the disjoint of self and list given as parameter.

```python
l = List([1, 2, 3, 2])
l.difference([1, 3])
# => [2, 2]
```

## drop

```python
List.drop(self, n)
```

Returns `List` object containing elements from index `n` inclusive.

```python
e = List([1, 2, 3, 4])
e.drop(2)
# => [3, 4]
```

## drop_while

```python
List.drop_while(self, callback)
```

Returns `List` object containing elements from where `callback` returns `False` first.

```python
e = List([1, 2, 3, 4])
e.drop_while(lambda x: x < 3)
# => [3, 4]
```

## each_cons

```python
List.each_cons(self, n)
```

Returns list of sublist containing consecutive `n` elements.

```python
e = List([1, 2, 3, 4])
e.each_cons(3)
# => [[1, 2, 3], [2, 3, 4]]
```

## each_slice

```python
List.each_slice(self, n, callback=None)
```

Returns list of sublists containing `n` length slices. If `callback` is given, it is applied on each element.

```python
e = List([1, 2, 3, 4, 5])
e.each_slice(2, lambda i: i * 2)
# => [[2, 4], [6, 8], [10]]
```

## each_with_index

```python
List.each_with_index(self, callback=None, start=0)
```

Returns list of sublists containing elements with their indices.


```python
e = List([1, 2, 3, 4])
e.each_with_index(start=2, callback=lambda index, item: [index, item * index] )
# => [[2, 6], [3, 12]]
```

## each_with_object

```python
List.each_with_object(self, callback=None, object=None)
```

Returns list of sublists containing elements with objects.

`callback` is applied on each element in case of not `None`.

```
e = List([1, 2, 3])
e.each_with_object(object=[], callback=lambda item, obj: (obj.append(item), obj)[-1])
# => [[1, [1]], [2, [1, 2]], [3, [1, 2, 3]]]
```

## empty

```python
List.empty(self)
```

Returns `True` if self contains no elements. Otherwise it returns `False`.

## find

```python
List.find(self, callback, default=None)
```

Returns the element that matches first with `callback` condition. Otherwise it returns `default`.

```python
e = List([1, 2, 3, 4, 5])
e.find(lambda x: x % 2 == 0)
# => 2
```

## find_all

```python
List.find_all(self, callback=None)
```

Returns all elements that match `callback` condition.

```python
e = List([1, 2, 3, 4, 5])
e.find_all(lambda item: item > 3)
# => [4, 5]
```

## find_index

```python
List.find_index(self, callback)
```

Returns the index of element which matches `callback` condition first.

## find_rindex

```python
List.find_rindex(self, callback)
```

Returns index of element which matches `callback` condition first from right.

## first

```python
List.first(self, num=None)
```

Returns the first `num` elements.

## first_while

```python
List.first_while(self, callback)
```

Returns sublist from left until `callback` condition returns `True`.

```python
e = List(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
e.first_while(lambda x: len(x) < 6)
# => ['apple', 'hola']
```

## flat_map

```python
List.flat_map(self, callback=None)
```

Returns flatten out list. If `callback` is not `None` it is applied on all elements first.

```python
e = List([[2, 4], 3, [5, 6, 7]])
e.flat_map()
# => [2, 4, 3, 5, 6, 7]

e = List([[1], 2, 3, 4])
e.flat_map(lambda i: [i, -i] if isinstance(i, int) else [i, None])
# => [[1], None, 2, -2, 3, -3, 4, -4]
```

## grep

```python
List.grep(self, pattern, callback=None)
```

Returns list of mached elements based on `pattern` of regex.

`callback` is applied if it is not `None`.

```python
e = List(['apple', 'bear', 'cat', 'anchor'])
e.grep(re.compile('^a[a-z]*$'), lambda x: x * 2)
# => ['appleapple', 'anchoranchor']
```

## grep_v

```python
List.grep_v(self, pattern, callback=None)
```

Returns list of unmached elements based on `pattern` of regex.

`callback` is applied if it is not `None`.

## group_by

```python
List.group_by(self, callback)
```

Returns dictionary of elements, grouped by `callback` condition.

Keys based on condition whilst elements assigned to them wether condition returns `True` or not.

```python
e = List(['apple', 'bear', 'dog', 'plum', 'grape', 'cat', 'anchor'])
e.group_by(lambda x: len(x))
# => {3 : ['dog', 'cat'], 4 : ['bear', 'plum'], 5 : ['apple', 'grape'], 6 : ['anchor']}
```

## include

```python
List.include(self, value)
```

Returns `True` if parameter is included in self. Otherwise it returns `False`.

## join

```python
List.join(self, separator=None)
```

Returns concatenated elements as a string with separator If `separator` is given. Otherwise it is empty string.

## keep_if

```python
List.keep_if(self, callback)
```

Returns list of elements on which `callback` condition returns `True`.

Opposite of `delete_if`. Alias for *find_all*.

## map

```python
List.map(self, callback=None)
```

Iterates over the elements and applies `callback` if not `None`.

## max

```python
List.max(self, callback=None)
```

Returns max value of the list. If `callback` is not `None` it returns max element based on condition.

```python
e = List([1, 2, 3, 4, 5, 6, 7])
e.max(lambda x: x % 4)
# => 3
```

## max_n

```python
List.max_n(self, num, callback=None)
```

Returns the first `num` max values of the list. If `callback` is not `None` it returns `num` max elements.

## min

```python
List.min(self, callback=None)
```

Returns min element of the list. If `callback` is not `None` it returns  min element.

## min_n

```python
List.min_n(self, num, callback=None)
```

Returns list of `num` min elements. If `callback` is not `None` it returns `num` min elements.

## none

```python
List.none(self, callback=None)
```

Return `False` if all elements are falsy, or `True` otherwise.

```python
e = List([False, None, 'dog', 'plum'])
e.none()
# => False

e = List([None, '', None, 0, False, [], None])
e.none()
# => True
```

## one

```python
List.one(self, callback=None)
```

Return `True` if only one truthy element is found.

```python
e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
e.one(lambda x: len(x) > 5)
# => True
```

## partition

```python
List.partition(self, callback=None)
```

Returns list of truthy and falsy elements. If `callback` condition is given, it is applied on all elements.

```python
e = List([5, 3, 5, 2, 4])
e.partition(lambda x: x > 3)
# => [[5, 5, 4], [3, 2]]
```

## reduce

```python
List.reduce(self, callback, init=None)
```

Combines all elements of enum by applying a binary operation.

The *inject* and *reduce* methods are aliases.

```python
e = List([1, 2, 3, 4, 5, 6])
e.reduce(lambda sum, x: sum + x)
# => 21

e = List(['apple', 'bear', 'dog', 'plum'])
e.reduce(lambda memo, s: memo + s, '')
# => 'applebeardogplum'
```

## reject

```python
List.reject(self, callback=None)
```

Returns list of elements for which the given callback returns `False`.

*delete_if* and *reject* methods are aliases.

```python
e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
e.reject(lambda x: len(x) > 5)
# => ['apple', 'bear', 'dog', 'plum']
```

## reverse

```python
List.reverse(self)
```

Returns reversed list.

## rotate

```python
List.rotate(self, num)
```

Returns list of shifted elements.

```python
e = List([1, 2, 4, 4, 5])
e.rotate(2)
# => [4, 5, 1, 2, 4]
```

## select

```python
List.select(self, callback)
```

Returns list of elements where `callback` returns `True`.

*select* and *find_all* methods are aliases.

## shuffle

```python
List.shuffle(self)
```

Returns list of shuffled elements of self.

## sort

```python
List.sort(self, callback=None)
```

Returns sorted list of self based on `callback` if not `None`.

## to_list

```python
List.to_list(self)
```

Returns list of elements of self.

## unique

```python
List.unique(self, callback=None)
```

Returns list containing unique elements.

## zip

```python
List.zip(self, other)
```

Converts any arguments to list, then merges elements of self with corresponding elements from each argument.

```python
e = List([1, 2, 3])
e.zip([4, 5, 6])
# => [[1, 4], [2, 5], [3, 6]]

e = List([5, 0, 3 ])
e.zip([])
# => [[5, None], [0, None], [3, None]]
```

