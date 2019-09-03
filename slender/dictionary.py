
import copy
import typing

KT = typing.TypeVar('KT')
VT = typing.TypeVar('VT')

class Dictionary(typing.Generic[KT, VT]):

    def __init__(self, d={}):
        '''
        Create new instance of Dictionary 

        Parameters:
        a (dicitonary): Dictionary of key-value pairs
                    It can be `dict`, or `Dictionary` 
        '''
        if isinstance(d, dict):
            self.__dict = copy.deepcopy(d)
        elif isinstance(d, Dictionary):
            self.__dict = copy.deepcopy(d.to_dict())
        else:
            raise TypeError


    @staticmethod
    def try_convert(obj):
        pass


    def __lt__(self, other: 'Dictionary[KT, VT]') -> bool:
        '''
        Suport of < operator

        Parameters:
        other (Dictionary): dictionary on the right side

        Returns:
        value (bool): returns True or False
        '''
        if not self.__dict and not other.to_dict():
            return False
        if len(self.__dict) >= len(other):
            return False
        for key in self.__dict:
            if key not in other.to_dict().keys() or self.__dict[key] != other.to_dict()[key]:
                return False
        else:
            return True


    def __le__(self, other: 'Dictionary[KT, VT]') -> bool:
        '''
        Suport of <= operator

        Parameters:
        other (Dictionary): dictionary on the right side

        Returns:
        value (bool): returns True or False
        '''
        if len(self.__dict) > len(other):
            return False
        for key in self.__dict:
            if key not in other.to_dict().keys() or self.__dict[key] != other.to_dict()[key]:
                return False
        else:
            return True


    def __len__(self) -> int:
        return len(self.__dict)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dictionary):
            return False
        if len(self.__dict) != len(other):
            return False
        ret = [key for key in self.__dict if key in other.to_dict()]
        return True if len(ret) == len(self.__dict) else False

    def __gt__(self, other: 'Dictionary[KT, VT]') -> bool:
        if not self.__dict and not other.to_dict():
            return False
        if len(self.__dict) <= len(other):
            return False
        for key in other.to_dict(): 
            if key not in self.__dict or self.__dict[key] != other.to_dict()[key]:
                return False
        else:
            return True


    def __ge__(self, other):
        if len(self.__dict) < len(other):
            return False
        for key in other.to_dict(): 
            if key not in self.__dict or self.__dict[key] != other.to_dict()[key]:
                return False
        else:
            return True


    def __getitem__(self, key):
        pass


    def __setitem__(self, key, value):
        pass


    def __contains__(self, key: KT) -> bool:
         return key in self.__dict

    
    def any(self, pattern=None, callback=None):
        pass


    def assoc(self, obj):
        pass

    
    def compact(self):
        pass

    
    def compare_by_identity(self):
        pass


    def default(self, key=None):
        pass


    def delete(self, key, callback=None):
        pass


    def delete_if(self, callback):
        pass


    def dig(self, *key):
        pass


    def each(self, callback):
        pass


    def each_key(self, callback):
        pass


    def each_value(self, callback):
        pass


    def empty(self):
        pass


    def get(self, key, callback=None):
        pass


    def get_values(self, keys, callback=None):
        pass


    def flatten(self, level=None):
        pass


    def has_key(self, key):
        pass

    
    def has_value(self, value):
        pass


    def include(self, key):
        pass


    def invert(self):
        pass


    def keep_if(self, callback):
        pass


    def merge(self, other, callback=None):
        pass


    def rassoc(self, obj):
        pass


    def reject(self, key, value, callback):
        pass
    
    def replace(self, hsh):
        pass
    
    def select(self, key, value, callback):
        pass
    
    def size(self):
        return len(self.__dict.keys()) 
    
    def slice(self, *keys):
        pass
    
    def store(self, key, value):
        pass
    
    def to_array(self):
        pass
    
    def to_dict(self):
        return copy.deepcopy(self.__dict) 
    
    def transform_keys(self, key, callback):
        pass
    
    def transform_values(self, value, callback):
        pass
    
    def values_at(self, *key):
        pass
        





















