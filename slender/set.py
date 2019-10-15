
import copy
import types
import typing

VT = typing.TypeVar('VT')

class Set(typing.Generic[VT]):

    def __init__(self, s=set()) -> None:
        if isinstance(s, set):
            self.__set = copy.deepcopy(s)
        elif isinstance(s, Set):
            self.__set = copy.deepcopy(s.to_set())
        else:
            raise TypeError

    def __and__(self, other: 'Set[VT]') -> 'Set[VT]':
        return self.intersection(other)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Set):
            return False
        else:
            if len(self) != len(other):
                return False
            return self.__set == other.to_set()


    def __ge__(self, other: 'Set[VT]') -> bool:
        return self.issuperset(other)


    def __gt__(self, other: 'Set[VT]') -> bool:
        return self.ispropersuperset(other)
    

    def __hash__(self) -> int:
        return hash(str(self))

    
    def __iter__(self):
        return iter(self.__set)


    def __lshift__(self, obj: VT) -> 'Set[VT]':
        return self.add(obj)


    def __le__(self, other: 'Set[VT]') -> bool:
        return self.issubset(other)


    def __len__(self) -> int:
        return len(self.__set) 


    def __lt__(self, other: 'Set[VT]') -> bool:
        return self.ispropersubset(other)

 
    def __or__(self, other: 'Set[VT]') -> 'Set[VT]':
        return self.union(other)


    def __str__(self) -> str:
        return '{' + ", ".join(str(item) for item in self.__set) + '}'
  

    def __sub__(self, other: 'Set[VT]') -> 'Set[VT]':
        return self.subtract(other)


    def add(self, obj: VT) -> 'Set[VT]':
        s = copy.deepcopy(self.__set)
        s.add(obj)
        return Set(s)


    def delete(self, obj: VT) -> 'Set[VT]':
        s = copy.deepcopy(self.__set)
        s.remove(obj)
        return Set(s)


    def delete_if(self, callback: typing.Callable[[VT], bool]) -> 'Set[VT]':
        return self.reject(callback)


    def difference(self, other: 'Set[VT]') -> 'Set[VT]':
        return self.subtract(other)


    def isdisjoint(self, other: 'Set[VT]') -> bool:
        if isinstance(other, Set):
            return self.__set.isdisjoint(other.to_set())
        else:
            return False
   

    def divide(self, callback: typing.Callable[[VT, VT], bool]) -> 'Set[VT]':
        arr = list(self.__set)
        a = [[arr[0]]] if len(self) > 0 else [[]]
        
        for i in range(1, len(arr)):
            if callback(arr[i - 1], arr[i]):
                a[len(a) - 1].append(arr[i])
            else:
                a.append([arr[i]])
        
        s: typing.Set['Set[VT]'] = set()
        for item in a:
            s.add(Set(set(item)))
        return Set[VT](s)


    def empty(self) -> bool:
        return len(self.__set) == 0


    def flatten(self) -> 'Set[VT]':
        s: typing.Set[VT] = set()
        for item in self:
            if isinstance(item, set) or isinstance(item, frozenset):
                s = s.union(item)
            elif isinstance(item, Set):
                s = s.union(item.to_set())
            else:
                s.add(item)
        return Set(s)


    def include(self, obj) -> bool:
        return obj in self 


    def intersect(self, other: 'Set[VT]') -> bool:
        if isinstance(other, set):
            return not self.__set.isdisjoint(other) 
        elif isinstance(other, Set):
            return not self.__set.isdisjoint(other.to_set()) 
        else:
            return False


    def intersection(self, other: 'Set[VT]') -> 'Set[VT]':
        if not isinstance(other, set) and not isinstance(other, Set):
            raise TypeError
        else:
            return Set(set([item for item in self if item in other]))


    def keep_if(self, callback: typing.Callable[[VT], bool]) -> 'Set[VT]':
        return self.select(callback) 


    def map(self, callback: typing.Callable[[VT], typing.Any]) -> 'Set[typing.Any]':
        return Set({callback(item) for item in self})    


    def ispropersubset(self, other: 'Set[VT]') -> bool:
        return len(self) < len(other) and self.__set.issubset(other.to_set())


    def ispropersuperset(self, other: 'Set[VT]') -> bool:
        s: typing.Set[VT] = set()
        if isinstance(other, set):
            s = other
        elif isinstance(other, Set):
            s = other.to_set()
        else:
            raise TypeError
        return len(self) > len(s) and self.__set.issuperset(s)


    def issubset(self, other: 'Set[VT]') -> bool:
        if isinstance(other, set):
            return self.__set.issubset(other)
        elif isinstance(other, Set):
            return self.__set.issubset(other.to_set())
        else:
            raise TypeError


    def issuperset(self, other: 'Set[VT]') -> bool:
        if isinstance(other, set):
            return self.__set.issuperset(other)
        elif isinstance(other, Set):
            return self.__set.issuperset(other.to_set())
        else:
            raise TypeError


    def reject(self, callback: typing.Callable[[VT], bool]) -> 'Set[VT]':
        if not isinstance(callback, types.LambdaType):
            raise TypeError
        else:
            return Set({item for item in self if not callback(item)})


    def select(self, callback: typing.Callable[[VT], bool]) -> 'Set[VT]':
        return Set({item for item in self if callback(item)})

       
    def subtract(self, other: 'Set[VT]') -> 'Set[VT]':
        if isinstance(other, set):
            return Set(self.__set.difference(other))
        elif isinstance(other, Set):
            return Set(self.__set.difference(other.to_set()))
        else:
            raise TypeError


    def to_set(self) -> typing.Set[VT]:
        return copy.deepcopy(self.__set)


    def union(self, other: 'Set[VT]') -> 'Set[VT]':
        if isinstance(other, Set):
            return Set(self.__set.union(other.to_set()))
        else:
            raise TypeError

   
