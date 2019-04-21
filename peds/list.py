import re
import copy
import random
import types

class List:
    def __init__(self, a=[]):
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
        List of intersected elements.
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
        Short descriptt....

        Parameters:
        callback (lambda or Regex): 

        """
        if isinstance(callback, re._pattern_type):
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
        if isinstance(callback, re._pattern_type):
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
        a = copy.deepcopy(self.__array)
        a.append(obj)
        return List(a)


    def chain(self, other):
        a = [x for x in self] 
        if other is None or not isinstance(other, list):
            raise TypeError 
        for item in other:
            a.append(item)
        return List(a)


    def chunk(self, callback):
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
        a = [[self.__array[0]]]
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
        return List([item for item in self if item is not None])


    def concat(self, other):
        if other is not None and (not isinstance(other, list) and not isinstance(other, List)):
            raise TypeError
        if isinstance(other, List):
            other = other.to_list()
        a = self.__array
        if other is not None:
            a.extend(other)
        return List(a)


    def count(self, callback=None):
        if callback is None:
            return len(self.__array)
        elif isinstance(callback, types.LambdaType):
            return sum(1 for item in self if callback(item))
        else:
            raise TypeError('parameter is either None or lambda')


    def cycle(self, num=-1, callback=None):
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
        return List([item for item in self if item != obj])


    def delete_at(self, num):
        arr = copy.deepcopy(self.__array)
        if isinstance(num, int):
            del arr[num]
            return List(arr)
        else:
            raise TypeError


    def delete_if(self, callback):
        return self.reject(callback)


    def difference(self, other):
        if other is not None and not isinstance(other, list) and not isinstance(other, List):
            raise TypeError
        if isinstance(other, List):
            other = other.to_list()
        return List([item for item in self.__array if item not in other])


    def drop(self, n):
        if isinstance(n, int) and n > 0:
            return List(self.__array[n:])
        else:
            raise TypeError


    def drop_while(self, callback):
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
        if isinstance(n, int) and 0 < n and n <= len(self.__array):
            return List([self.__array[i:i + n] for i in range(len(self.__array) - n + 1)])
        else:
            raise TypeError

    
    def each_slice(self, n, callback=None):
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
        return len(self.__array) == 0

    
    def find(self, callback, default=None):
        for i in self:
            if callback(i):
                return i
        else:
            if default is not None:
                return default
            else:
                return None


    def find_all(self, callback=None):
        if isinstance(callback, types.LambdaType):
            return List([item for item in self if callback(item)])
        elif callback is None:
            return List([item for item in self])
        else:
            raise TypeError
   

    def find_index(self, callback):
        arr = []
        if isinstance(callback, types.LambdaType):
            arr = [idx for idx, val in enumerate(self) if callback(val)]
        return arr[0] if len(arr) > 0 else None


    def find_rindex(self, callback):
        arr = copy.deepcopy(self.__array)
        arr.reverse()
        ret = List(arr).find_index(callback)
        return len(self) - 1 - ret if ret is not None else None


    def first(self, num=None):
        if num is not None:
            if isinstance(num, int):
                return self.__array[:num] 
            else:
                raise TypeError
        else:
            return self.__array[0] if len(self.__array) > 0 else None
    

    
    def first_while(self, callback):
        if isinstance(callback, types.LambdaType):
            arr = []
            for item in self:
                if callback(item):
                    arr.append(item)
                else:
                    break
            return arr
        else:
            raise TypeError

    def flat_map(self, callback=None):
        if callback is None:
            return iter(self)
        else:
            a = list(map(callback, self))
            return [item for _a in a for item in _a]


    def grep(self, pattern, callback=None):
        arr = []
        if isinstance(pattern, re._pattern_type) or isinstance(pattern, str):
            arr = [item for item in self if re.search(pattern, item)]
        else:
            raise TypeError

        if callback is not None and isinstance(callback, types.LambdaType):
            arr = list(map(callback, arr)) 
        return List(arr)

    def grep_v(self, pattern, callback=None):
        arr = []
        if isinstance(pattern, re._pattern_type) or isinstance(pattern, str):
            arr = [item for item in self if not re.search(pattern, item)]
        else:
            raise TypeError
        if callback is not None and isinstance(callback, types.LambdaType):
            arr = list(map(callback, arr)) 
        return List(arr)

    def group_by(self, callback):
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
        return value in self


    def join(self, separator=None):
        if separator is None:
            return ''.join(list(map(lambda x: str(x), self.__array)))
        elif isinstance(separator, str):
            return separator.join(list(map(lambda x: str(x), self.__array)))
        else:
            raise TypeError


    def keep_if(self, callback):
        return self.find_all(callback)


    def map(self, callback=None):
        if callback is None:
            return List(self.__array)
        else:
            return List(list(map(callback, self)))


    def max(self, callback=None):
        if len(self.__array) == 0:
            return None
        if isinstance(callback, types.LambdaType):
            return max(self.__array, key=callback)
        elif callback is None:
            return max(self.__array)
        else:
            raise TypeError


    def max_n(self, num, callback=None):
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
        if not len(self.__array):
            return None
        if isinstance(callback, types.LambdaType):
            return min(self.__array, key=callback)
        elif callback is None:
            return min(self.__array)
        else:
            raise TypeError


    def min_n(self, num, callback=None):
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
        arr = []
        if callback is None:
            arr = [item for item in self if not item]
        elif isinstance(callback, types.LambdaType):
            arr = [item for item in self if not callback(item)]
        else:
            raise TypeError
        return List(arr)


    def reverse(self):
        arr = copy.deepcopy(self.__array)
        arr.reverse()
        return List(arr)


    def rotate(self, num):
        if isinstance(num, int):
            num = num % len(self)
            return List(self.__array[-num:] + self.__array[:-num])
        else:
            raise TypeError


    def select(self, callback=None):
        return self.find_all(callback)


    def shuffle(self):
        arr = copy.deepcopy(self.__array)
        random.shuffle(arr)
        return List(arr)


    def sort(self, callback=None):
        if callback is None or isinstance(callback, types.LambdaType):
            return List(sorted(self.__array, key=callback))
        else:
            raise TypeError


    def to_list(self):
        return copy.deepcopy(self.__array)


    def unique(self, callback=None):
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




