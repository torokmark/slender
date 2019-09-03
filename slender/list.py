import re
import copy
import random
import types

class List:
    def __init__(self, a=[]):
        '''
        Create new instance of List

        Parameters:
        a (list): list of elements for further working
                    It can be `list`, `List`, or `set`
        '''
        if isinstance(a, list):
            self.__array = copy.deepcopy(a)
        elif isinstance(a, List):
            self.__array = copy.deepcopy(a.to_list())
        elif isinstance(a, set):
            self.__array = list(copy.deepcopy(a))
        else:
            raise TypeError


    def __getitem__(self, key):
        '''
        Support of indexing

        Parameters:
        key (int): index

        Returns:
        object: Object on the given index
        '''
        return self.__array[key]


    def __setitem__(self, key, value):
        '''
        Support of assignment via indexing

        Parameters:
        key (int): index
        value (any): the assign object
        '''
        self.__array[key] = value


    def __and__(self, other):
        '''
        Takes the intersection of this and the other lists.

        Parameters:
            other (List): other list (type of `List` or `list`)

        Returns:
            list: List of intersected elements.
        '''
        if isinstance(other, List):
            other = other.to_list()
        if isinstance(other, list):
            s_other = set(other)
            return List([item for item in self if item in s_other])
        else:
            raise TypeError


    def __add__(self, other):
        return self.concat(other)


    def __mul__(self, scalar):
        if isinstance(scalar, int):
            return List(self.__array * scalar)
        else:
            raise TypeError


    def __sub__(self, other):
        return self.difference(other)


    def __lshift__(self, obj):
        return self.append(obj)


    def __eq__(self, other):
        if isinstance(other, List):
            return self.__array == other.to_list()
        else:
            return False

    def __iter__(self):
        return iter(self.__array)


    def __len__(self):
        return len(self.__array)


    def all(self, callback):
        """
        Checks wether all elements are `True`. If one is `False` it returns `False`.

        *callback* can be regex or lambda.
        """
        if isinstance(callback, re.Pattern):
            for item in self:
                if isinstance(item, str):
                    if not re.match(callback, item):
                        return False
                else:
                    raise TypeError('regex only applied against string')
            else:
                return True
        elif isinstance(callback, types.LambdaType):
           return all(list(map(callback, self)))
        else:
            raise TypeError('callback has to be either regex pattern or lambda')


    def any(self, callback):
        """
        Checks wether any element is `True`. If all of them are `False` it returns `False`.
        
        *callback* can be regex or lambda.
        """
        if isinstance(callback, re.Pattern):
            for item in self:
                if isinstance(item, str):
                    if re.match(callback, item):
                        return True 
                else:
                    raise TypeError('regex only applied against string')
            else:
                return False
        elif isinstance(callback, types.LambdaType):
           return any(list(map(callback, self)))
        else:
            raise TypeError('callback has to be either regex pattern or lambda')


    def append(self, obj):
        '''
        Appends one element to the list.

        Returns new `List` object containing the appended element.
        '''
        a = copy.deepcopy(self.__array)
        a.append(obj)
        return List(a)


    def chain(self, other):
        '''
        Appends all elements given as a `list`, or `List`

        Returns new `List` object containing all the appended elements.
        '''
        a = [x for x in self] 
        if other is None and not isinstance(other, list) and not isinstance(other, List):
            raise TypeError 
        for item in other:
            a.append(item)
        return List(a)


    def chunk(self, callback):
        '''
        Divides list into sublists based on wether the callback returns `True` or `False` on elements.

        ```python
        e = List([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        e.chunk(lambda x: x % 2 == 0)
        # => [[False, [3, 1]], [True, [4]], [False, [1, 5, 9]], [True, [2, 6]], [False, [5, 3, 5]]]
        ```
        '''
        a = []
        if isinstance(callback, types.LambdaType):
            for item in self:
                if len(a) > 0 and callback(item) == a[len(a) - 1][0]:
                    a[len(a) - 1][1].append(item)
                else:
                    a.append([callback(item), [item]])
        else:
            raise TypeError
        return List(a)


    def chunk_while(self, callback):
        '''
        Divides list into sublist based on lambda expression.

        ```python
        e = List([1,2,4,9,10,11,12,15,16,19,20,21])
        e.chunk_while(lambda i, j: i + 1 == j)
        # => [[1, 2], [4], [9, 10, 11, 12], [15, 16], [19, 20, 21]]
        ```
        '''
        a = [[self.__array[0]]] if len(self) > 0 else [[]]
        if isinstance(callback, types.LambdaType):
            for i in range(1, len(self.__array)):
                if callback(self.__array[i - 1], self.__array[i]):
                    a[len(a) - 1].append(self.__array[i])
                else:
                    a.append([self.__array[i]])
        else:
            raise TypeError
        return List(a)


    def compact(self):
        '''
        Removes `None` elements from list.
        '''
        return List([item for item in self if item is not None])


    def concat(self, other):
        '''
        Concatenates `other` to self.
        '''
        if other is not None and (not isinstance(other, list) and not isinstance(other, List)):
            raise TypeError
        if isinstance(other, List):
            other = other.to_list()
        a = self.__array
        if other is not None:
            a.extend(other)
        return List(a)


    def count(self, callback=None):
        '''
        Returns length of self if `callback` is not given.

        Returns number of elements if `callback` is `True` on them.
        '''
        if callback is None:
            return len(self.__array)
        elif isinstance(callback, types.LambdaType):
            return sum(1 for item in self if callback(item))
        else:
            raise TypeError('parameter is either None or lambda')


    def cycle(self, num=-1, callback=None):
        '''
        If no parameters are given, it iterates over the list infinitely and yields the next element.

        If `num` is given, it yields the list as many times.

        If `callback` is given it is applied on each element before yield.

        ```python
        e = List(['a', 'b', 'c'])
        e.cycle(2, lambda x: x.upper())
        # => iterator over : ['A', 'B', 'C', 'A', 'B', 'C']
        ```
        '''
        _counter = 0
        while True:
            if _counter == num * len(self.__array):
                break
            else:
                _counter += 1
            value = self.__array[(_counter - 1) % len(self.__array)]
            if callback is not None:
                yield callback(value)
            else:
                yield value


    def delete(self, obj):
        '''
        Deletes all elements from list if they are equal to `obj`
        '''
        return List([item for item in self if item != obj])


    def delete_at(self, idx):
        '''
        Deletes the element at the given index.

        Returns `List` instance of the modified list.
        '''
        arr = copy.deepcopy(self.__array)
        if isinstance(idx, int):
            del arr[idx]
            return List(arr)
        else:
            raise TypeError


    def delete_if(self, callback):
        '''
        Deletes all elements on which `callback` is `True`.
        
        Alias for *reject*.
        
        ```python
        e = List([5, 3, 5, 2, 4])
        e.delete_if(lambda x: x > 3)
        # => [3, 2]
        ```
        '''
        return self.reject(callback)


    def difference(self, other):
        '''
        Takes the disjoint of self and list given as parameter.  

        ```python
        l = List([1, 2, 3, 2])
        l.difference([1, 3])
        # => [2, 2]
        ```
        '''
        if other is not None and not isinstance(other, list) and not isinstance(other, List):
            raise TypeError
        if isinstance(other, List):
            other = other.to_list()
        return List([item for item in self.__array if item not in other])


    def drop(self, n):
        '''
        Returns `List` object containing elements from index `n` inclusive.

        ```python
        e = List([1, 2, 3, 4])
        e.drop(2)
        # => [3, 4]
        ```
        '''
        if isinstance(n, int) and n > 0:
            return List(self.__array[n:])
        else:
            raise TypeError


    def drop_while(self, callback):
        '''
        Returns `List` object containing elements from where `callback` returns `False` first.

        ```python
        e = List([1, 2, 3, 4])
        e.drop_while(lambda x: x < 3)
        # => [3, 4]
        ```
        '''
        if isinstance(callback, types.LambdaType):
            arr = []
            for i in range(0, len(self.__array)):
                if not callback(self.__array[i]):
                    arr = self.__array[i:]
                    break
            return List(arr)
        else:
            raise TypeError


    def each_cons(self, n):
        '''
        Returns list of sublist containing consecutive `n` elements.

        ```python
        e = List([1, 2, 3, 4])
        e.each_cons(3)
        # => [[1, 2, 3], [2, 3, 4]]
        ```
        '''
        if isinstance(n, int) and 0 < n and n <= len(self.__array):
            return List([self.__array[i:i + n] for i in range(len(self.__array) - n + 1)])
        else:
            raise TypeError

    
    def each_slice(self, n, callback=None):
        '''
        Returns list of sublists containing `n` length slices. If `callback` is given, it is applied on each element.

        ```python
        e = List([1, 2, 3, 4, 5])
        e.each_slice(2, lambda i: i * 2)
        # => [[2, 4], [6, 8], [10]]
        ```
        '''
        if not isinstance(n, int) or n < 0 or (callback is not None and not isinstance(callback, types.LambdaType)):
            raise TypeError
        ret = []
        arr = []
        for item in self:
            arr.append(item)
            if len(arr) >= n:
                if callback is not None:
                    ret.append(list(map(callback, arr)))
                else:
                    ret.append(arr)
                arr = []
        if arr:
            if callback is not None:
                ret.append(list(map(callback, arr)))
            else:
                ret.append(arr)
        return List(ret)


    def each_with_index(self, callback=None, start=0):
        '''
        Returns list of sublists containing elements with their indices.


        ```python
        e = List([1, 2, 3, 4])
        e.each_with_index(start=2, callback=lambda index, item: [index, item * index] )
        # => [[2, 6], [3, 12]]
        ```
        '''
        arr = []
        for idx, val in enumerate(self.__array[start:]):
            if callback is None:
                arr.append([idx + start, val])
            elif isinstance(callback, types.LambdaType):
                arr.append(callback(idx + start, val))
            else:
                raise TypeError
        return List(arr)

    
    def each_with_object(self, callback=None, object=None):
        '''
        Returns list of sublists containing elements with objects.  
        
        `callback` is applied on each element in case of not `None`.

        ```
        e = List([1, 2, 3])
        e.each_with_object(object=[], callback=lambda item, obj: (obj.append(item), obj)[-1])
        # => [[1, [1]], [2, [1, 2]], [3, [1, 2, 3]]]
        ```
        '''
        if callback is not None and not isinstance(callback, types.LambdaType):
            raise TypeError

        arr = []
        for item in self:
            if callback is not None:
                arr.append([item, copy.deepcopy(callback(item, object))])
            else:
                arr.append([item, object])
        return List(arr)


    def empty(self):
        '''
        Returns `True` if self contains no elements. Otherwise it returns `False`.
        '''
        return len(self.__array) == 0

    
    def find(self, callback, default=None):
        '''
        Returns the element that matches first with `callback` condition. Otherwise it returns `default`.

        ```python
        e = List([1, 2, 3, 4, 5])
        e.find(lambda x: x % 2 == 0)
        # => 2 
        ```
        '''
        for i in self:
            if callback(i):
                return i
        else:
            if default is not None:
                return default
            else:
                return None


    def find_all(self, callback=None):
        '''
        Returns all elements that match `callback` condition.

        ```python
        e = List([1, 2, 3, 4, 5])
        e.find_all(lambda item: item > 3)
        # => [4, 5]
        ```
        '''
        if isinstance(callback, types.LambdaType):
            return List([item for item in self if callback(item)])
        elif callback is None:
            return List([item for item in self])
        else:
            raise TypeError
   

    def find_index(self, callback):
        '''
        Returns the index of element which matches `callback` condition first.
        '''
        arr = []
        if isinstance(callback, types.LambdaType):
            arr = [idx for idx, val in enumerate(self) if callback(val)]
        return arr[0] if len(arr) > 0 else None


    def find_rindex(self, callback):
        '''
        Returns index of element which matches `callback` condition first from right.
        '''
        arr = copy.deepcopy(self.__array)
        arr.reverse()
        ret = List(arr).find_index(callback)
        return len(self) - 1 - ret if ret is not None else None


    def first(self, num=None):
        '''
        Returns the first `num` elements.
        '''
        if num is not None:
            if isinstance(num, int):
                return self.__array[:num] 
            else:
                raise TypeError
        else:
            return self.__array[0] if len(self.__array) > 0 else None

    
    def first_while(self, callback):
        '''
        Returns sublist from left until `callback` condition returns `True`.

        ```python
        e = List(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
        e.first_while(lambda x: len(x) < 6)
        # => ['apple', 'hola']
        ```
        '''
        if isinstance(callback, types.LambdaType):
            arr = []
            for item in self:
                if callback(item):
                    arr.append(item)
                else:
                    break
            return List(arr)
        else:
            raise TypeError

    
    def flat_map(self, callback=None):
        '''
        Returns flatten out list. If `callback` is not `None` it is applied on all elements first.

        ```python
        e = List([[2, 4], 3, [5, 6, 7]])
        e.flat_map()
        # => [2, 4, 3, 5, 6, 7]

        e = List([[1], 2, 3, 4])
        e.flat_map(lambda i: [i, -i] if isinstance(i, int) else [i, None])
        # => [[1], None, 2, -2, 3, -3, 4, -4]
        ```
        '''
        arr = list(map(callback, self)) if callback is not None else copy.deepcopy(self.__array)
        ret = []
        for i in arr:
            if isinstance(i, list):
                ret.extend(i)
            else:
                ret.append(i)
        return List(ret)


    def grep(self, pattern, callback=None):
        '''
        Returns list of mached elements based on `pattern` of regex.

        `callback` is applied if it is not `None`.

        ```python
        e = List(['apple', 'bear', 'cat', 'anchor'])
        e.grep(re.compile('^a[a-z]*$'), lambda x: x * 2)
        # => ['appleapple', 'anchoranchor']
        ```
        '''
        arr = []
        if isinstance(pattern, re.Pattern) or isinstance(pattern, str):
            arr = [item for item in self if re.search(pattern, item)]
        else:
            raise TypeError

        if callback is not None and isinstance(callback, types.LambdaType):
            arr = list(map(callback, arr)) 
        return List(arr)

    def grep_v(self, pattern, callback=None):
        '''
        Returns list of unmached elements based on `pattern` of regex.

        `callback` is applied if it is not `None`.
        '''
        arr = []
        if isinstance(pattern, re.Pattern) or isinstance(pattern, str):
            arr = [item for item in self if not re.search(pattern, item)]
        else:
            raise TypeError
        if callback is not None and isinstance(callback, types.LambdaType):
            arr = list(map(callback, arr)) 
        return List(arr)

    def group_by(self, callback):
        '''
        Returns dictionary of elements, grouped by `callback` condition.

        Keys based on condition whilst elements assigned to them wether condition returns `True` or not.

        ```python
        e = List(['apple', 'bear', 'dog', 'plum', 'grape', 'cat', 'anchor'])
        e.group_by(lambda x: len(x))
        # => {3 : ['dog', 'cat'], 4 : ['bear', 'plum'], 5 : ['apple', 'grape'], 6 : ['anchor']}
        ```
        '''
        if not isinstance(callback, types.LambdaType):
            raise TypeError
        d = {}
        for item in self:
            k = callback(item)
            if k in d:
                d[k].append(item)
            else:
                d[k] = [item]
        return d


    def include(self, value):
        '''
        Returns `True` if parameter is included in self. Otherwise it returns `False`.
        '''
        return value in self


    def join(self, separator=None):
        '''
        Returns concatenated elements as a string with separator If `separator` is given. Otherwise it is empty string.
        '''
        if separator is None:
            return ''.join(list(map(lambda x: str(x), self.__array)))
        elif isinstance(separator, str):
            return separator.join(list(map(lambda x: str(x), self.__array)))
        else:
            raise TypeError


    def keep_if(self, callback):
        '''
        Returns list of elements on which `callback` condition returns `True`.

        Opposite of `delete_if`. Alias for *find_all*.
        '''
        return self.find_all(callback)


    def map(self, callback=None):
        '''
        Iterates over the elements and applies `callback` if not `None`.
        '''
        if callback is None:
            return List(self.__array)
        else:
            return List(list(map(callback, self)))


    def max(self, callback=None):
        '''
        Returns max value of the list. If `callback` is not `None` it returns max element based on condition.

        ```python
        e = List([1, 2, 3, 4, 5, 6, 7])
        e.max(lambda x: x % 4)
        # => 3
        ```
        '''
        if len(self.__array) == 0:
            return None
        if isinstance(callback, types.LambdaType):
            return max(self.__array, key=callback)
        elif callback is None:
            return max(self.__array)
        else:
            raise TypeError


    def max_n(self, num, callback=None):
        '''
        Returns the first `num` max values of the list. If `callback` is not `None` it returns `num` max elements.
        '''
        if len(self.__array) == 0:
            return List([]) 
        if isinstance(num, int):
            if callback is None:
                arr = sorted(self.__array)
            elif isinstance(callback, types.LambdaType):
                arr = sorted(self.__array, key=callback)
            else:
                raise TypeError
            return List(arr[-num:])
        else:
            raise TypeError


    def min(self, callback=None):
        '''
        Returns min element of the list. If `callback` is not `None` it returns  min element.
        '''
        if not len(self.__array):
            return None
        if isinstance(callback, types.LambdaType):
            return min(self.__array, key=callback)
        elif callback is None:
            return min(self.__array)
        else:
            raise TypeError


    def min_n(self, num, callback=None):
        '''
        Returns list of `num` min elements. If `callback` is not `None` it returns `num` min elements.
        '''
        if not len(self.__array):
            return List([]) 
        if isinstance(num, int):
            if callback is None:
                return List(sorted(self.__array)[:num])
            elif isinstance(callback, types.LambdaType):
                return List(sorted(self.__array, key=callback)[:num])
            else:
                raise TypeError
        else:
            raise TypeError

    
    def none(self, callback=None):
        '''
        Return `False` if all elements are falsy, or `True` otherwise. 
    
        ```python
        e = List([False, None, 'dog', 'plum'])
        e.none()
        # => False

        e = List([None, '', None, 0, False, [], None])
        e.none()
        # => True 
        ```
        '''
        if callback is None:
            for item in self:
                if item:
                    return False
        elif isinstance(callback, types.LambdaType):
            for item in self:
                if callback(item):
                    return False
        else:
            raise TypeError
        return True
   

    def one(self, callback=None):
        '''
        Return `True` if only one truthy element is found.

        ```python
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        e.one(lambda x: len(x) > 5)
        # => True
        ```
        '''
        counter = 0
        if callback is None:
            for item in self:
                if item:
                    counter += 1
        elif isinstance(callback, types.LambdaType):
            for item in self:
                if callback(item):
                    counter += 1 
        else:
            raise TypeError
        return counter == 1

    
    def partition(self, callback=None):
        '''
        Returns list of truthy and falsy elements. If `callback` condition is given, it is applied on all elements.

        ```python
        e = List([5, 3, 5, 2, 4])
        e.partition(lambda x: x > 3)
        # => [[5, 5, 4], [3, 2]]
        ```
        '''
        arr = [[], []]
        if callback is None:
            for item in self:
                if item:
                    arr[0].append(item)
                else:
                    arr[1].append(item)
        elif isinstance(callback, types.LambdaType):
            for item in self:
                if callback(item):
                    arr[0].append(item)
                else:
                    arr[1].append(item)
        else:
            raise TypeError
        return List(arr)


    def reduce(self, callback, init=None):
        '''
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
        '''
        if len(self.__array) == 0:
            return None
        if isinstance(callback, types.LambdaType):
            if init is not None:
                memo = init
                arr = self.__array
            else:
                memo = self.__array[0]
                arr = self.__array[1:]
            for item in arr:
                memo = callback(memo, item)
            return memo
        else:
            raise TypeError


    def reject(self, callback=None):
        '''
        Returns list of elements for which the given callback returns `False`.

        *delete_if* and *reject* methods are aliases.

        ```python
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        e.reject(lambda x: len(x) > 5)
        # => ['apple', 'bear', 'dog', 'plum']
        ```
        '''
        arr = []
        if callback is None:
            arr = [item for item in self if not item]
        elif isinstance(callback, types.LambdaType):
            arr = [item for item in self if not callback(item)]
        else:
            raise TypeError
        return List(arr)


    def reverse(self):
        '''
        Returns reversed list.
        '''
        arr = copy.deepcopy(self.__array)
        arr.reverse()
        return List(arr)


    def rotate(self, num):
        '''
        Returns list of shifted elements.

        ```python
        e = List([1, 2, 4, 4, 5])
        e.rotate(2)
        # => [4, 5, 1, 2, 4]
        ```
        '''
        if isinstance(num, int):
            num = num % len(self)
            return List(self.__array[-num:] + self.__array[:-num])
        else:
            raise TypeError


    def select(self, callback):
        '''
        Returns list of elements where `callback` returns `True`.

        *select* and *find_all* methods are aliases.
        '''
        return self.find_all(callback)


    def shuffle(self):
        '''
        Returns list of shuffled elements of self.
        '''
        arr = copy.deepcopy(self.__array)
        random.shuffle(arr)
        return List(arr)


    def sort(self, callback=None):
        '''
        Returns sorted list of self based on `callback` if not `None`.
        '''
        if callback is None or isinstance(callback, types.LambdaType):
            return List(sorted(self.__array, key=callback))
        else:
            raise TypeError


    def to_list(self):
        '''
        Returns list of elements of self.
        '''
        return copy.deepcopy(self.__array)


    def unique(self, callback=None):
        '''
        Returns list containing unique elements.
        '''
        if callback is None:
            return List(list(set(self.__array)))
        elif isinstance(callback, types.LambdaType):
            d = {}
            for item in self.__array:
                d[callback(item)] = item
            return List(list(d.values()))
        else:
            raise TypeError


    def zip(self, other):
        '''
        Converts any arguments to list, then merges elements of self with corresponding elements from each argument. 

        ```python
        e = List([1, 2, 3])
        e.zip([4, 5, 6])
        # => [[1, 4], [2, 5], [3, 6]]

        e = List([5, 0, 3 ])
        e.zip([])
        # => [[5, None], [0, None], [3, None]] 
        ```
        '''
        if isinstance(other, list) or isinstance(other, List):
            l = max(len(self.__array), len(other))
            arr = []
            for i in range(0, l):
                a = self.__array[i] if i < len(self.__array) else None
                b = other[i] if i < len(other) else None
                arr.append([a, b])
            return List(arr)
        else:
            raise TypeError




