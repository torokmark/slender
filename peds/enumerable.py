import re
import copy

import types

class Enumerable:
    def __init__(self, a=[]):
        self.__array = a

    def __iter__(self):
        return iter(self.__array)


    def all(self, callback):
        if isinstance(callback, re._pattern_type):
            for item in self:
                if isinstance(item, str):
                    if not re.match(callback, item):
                        return False
                else:
                    raise TypeError()
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
                    raise TypeError()
            else:
                return False
        elif isinstance(callback, types.LambdaType):
           return any(list(map(callback, self)))
        else:
            raise TypeError('callback has to be either regex pattern or lambda')


    def chain(self, other):
        a = [x for x in self] 
        if other is None:
            raise TypeError 
        for item in other:
            a.append(item)
        return iter(a) 


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
        return iter(a)


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
        return iter(a)


    def collect(self, callback=None):
        return self.map(callback) 


    def collect_concat(self, callback=None):
        return self.flat_map(callback)


    def count(self, param=None):
        if param is None:
            return len(self.__array)
        elif isinstance(param, int):
            return sum(1 for item in self if param == item)
        elif isinstance(param, types.LambdaType):
            return sum(1 for item in self if param(item))
        else:
            raise TypeError('parameter has to be None, int or lambda')


    def cycle(self, p1=None, p2=None):
        _counter = 0
        def args(c, f):
            if c is None and f is None:
                return -1, None
            if isinstance(c, int) and c > 0:
                if f is None:
                    return c, None
                elif isinstance(f, types.LambdaType):
                    return c, f
                else:
                    raise TypeError
            elif isinstance(c, types.LambdaType):
                return -1, c
            else:
                raise TypeError

        n, func = args(p1, p2)
        while True:
            if _counter == n * len(self.__array):
                break
            else:
                _counter += 1
            value = self.__array[(_counter - 1) % len(self.__array)]
            if func is not None:
                yield func(value)
            else:
                yield value


    def flat_map(self, callback=None):
        if callback == None:
            return iter(self)
        else:
            a = list(map(callback, self))
            return [item for _a in a for item in _a]


    def map(self, callback=None):
        if callback is None:
            return iter(self)
        else:
            return list(map(callback, self))


