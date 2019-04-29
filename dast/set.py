
import copy
import types

class Set:

    def __init__(self, s=set()):
        if isinstance(s, set):
            self.__set = s
        elif isinstance(s, Set):
            self.__set = s.to_set()
        else:
            raise TypeError

    def __and__(self, other):
        return self.intersection(other)


    def __eq__(self, other):
        if not isinstance(other, set) and not isinstance(other, Set):
            raise TypeError
        else:
            if len(self) != len(other):
                return False

            if isinstance(other, set):
                return self.__set == other
            elif isinstance(other, Set):
                return self.__set == other.to_set()


    def __ge__(self, other):
        return self.issuperset(other)


    def __gt__(self, other):
        return self.ispropersuperset(other)
    

    def __hash__(self):
        return hash(str(self))

    
    def __iter__(self):
        return iter(self.__set)


    def __lshift__(self, obj):
        return self.add(obj)


    def __le__(self, other):
        return self.issubset(other)


    def __len__(self):
        return len(self.__set) 


    def __lt__(self, other):
        return self.ispropersubset(other)

 
    def __or__(self, other):
        return self.union(other)


    def __str__(self):
        return '{' + ", ".join(str(item) for item in self.__set) + '}'
  

    def __sub__(self, other):
        return self.subtract(other)


    def add(self, obj):
        s = copy.deepcopy(self.__set)
        s.add(obj)
        return Set(s)


    def delete(self, obj):
        s = copy.deepcopy(self.__set)
        s.remove(obj)
        return Set(s)


    def delete_if(self, callback):
        return self.reject(callback)


    def difference(self, other):
        return self.subtract(other)


    def isdisjoint(self, other):
        if isinstance(other, set):
            return self.__set.isdisjoint(other)
        elif isinstance(other, Set):
            return self.__set.isdisjoint(other.to_set())
        else:
            raise TypeError

    
    def divide(self, callback):
        if not isinstance(callback, types.LambdaType):
            raise TypeError
        arr = list(self.__set)
        a = [[arr[0]]] if len(self) > 0 else [[]]
        if isinstance(callback, types.LambdaType):
            for i in range(1, len(arr)):
                if callback(arr[i - 1], arr[i]):
                    a[len(a) - 1].append(arr[i])
                else:
                    a.append([arr[i]])
        else:
            raise TypeError
        s = set()
        print(a)
        for item in a:
            s.add(Set(set(item)))
        return Set(s)


    def empty(self):
        return len(self.__set) == 0


    def flatten(self):
        s = set()
        for item in self:
            if isinstance(item, set) or isinstance(item, frozenset):
                s = s.union(item)
            elif isinstance(item, Set):
                s = s.union(item.to_set())
            else:
                s.add(item)
        return Set(s)

    def include(self, obj):
        return obj in self 


    def intersect(self, other):
        if isinstance(other, set):
            return not self.__set.isdisjoint(other) 
        elif isinstance(other, Set):
            return not self.__set.isdisjoint(other.to_set()) 
        else:
            raise TypeError


    def intersection(self, other):
        if not isinstance(other, set) and not isinstance(other, Set):
            raise TypeError
        else:
            return Set(set([item for item in self if item in other]))


    def keep_if(self, callback):
        return self.select(callback) 


    def map(self, callback):
        if isinstance(callback, types.LambdaType):
            return Set({callback(item) for item in self})    
        else:
            raise TypeError

    def ispropersubset(self, other):
        s = set()
        if isinstance(other, set):
            s = other 
        elif isinstance(other, Set):
            s = other.to_set()
        else:
            raise TypeError
        return len(self) < len(s) and self.__set.issubset(s)


    def ispropersuperset(self, other):
        s = set()
        if isinstance(other, set):
            s = other
        elif isinstance(other, Set):
            s = other.to_set()
        else:
            raise TypeError
        return len(self) > len(s) and self.__set.issuperset(s)


    def issubset(self, other):
        if isinstance(other, set):
            return self.__set.issubset(other)
        elif isinstance(other, Set):
            return self.__set.issubset(other.to_set())
        else:
            raise TypeError


    def issuperset(self, other):
        if isinstance(other, set):
            return self.__set.issuperset(other)
        elif isinstance(other, Set):
            return self.__set.issuperset(other.to_set())
        else:
            raise TypeError


    def reject(self, callback):
        if not isinstance(callback, types.LambdaType):
            raise TypeError
        else:
            return Set({item for item in self if not callback(item)})


    def select(self, callback):
        if isinstance(callback, types.LambdaType):
            return Set({item for item in self if callback(item)})
        else:
            raise TypeError

       
    def subtract(self, other):
        if isinstance(other, set):
            return Set(self.__set.difference(other))
        elif isinstance(other, Set):
            return Set(self.__set.difference(other.to_set()))
        else:
            raise TypeError


    def to_set(self):
        return copy.deepcopy(self.__set)


    def union(self, other):
        if isinstance(other, set):
            return Set(self.__set.union(other))        
        elif isinstance(other, Set):
            return Set(self.__set.union(other.to_set()))
        else:
            raise TypeError

   
