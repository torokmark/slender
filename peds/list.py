
import copy

from peds.enumerable import Enumerable

class List(Enumerable):
    def __init__(self, a=[]):
        self.__array = a

    def __getitem__(self, key):
        return self.__array[key]

    def __setitem__(self, key, value):
        self.__array[key] = value

    def __and__(self, other):
        pass

    def __add__(self, other):
        a = copy.deepcopy(self.__array)
        if other is not None:
            a.extend(other)
        return a

    def __mul__(self, scalar):
        pass # scalar can be int or str

    def __sub__(self, other):
        pass

    def __lshift__(self, obj):
        pass

    def __or__(self, other):
        pass

    def __eq__(self, other):
        pass

    def delete_if(self, predicate):
        pass

    def keep_if(self, predicate):
        pass

    def map(self):
        return 'mapppp...'


