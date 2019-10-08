
import copy
import typing

from slender import List

KT = typing.TypeVar('KT')
VT = typing.TypeVar('VT')

class Dictionary(typing.Generic[KT, VT]):

    def __init__(self, d={}) -> None:
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
        self.__default: typing.Optional[KT] = None


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
        for k, v in self.__dict.items():
            if k not in other.to_dict() or v != other.to_dict()[k]:
                return False
        else:
            return True


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


    def __ge__(self, other) -> bool:
        if len(self.__dict) < len(other):
            return False
        for key in other.to_dict(): 
            if key not in self.__dict or self.__dict[key] != other.to_dict()[key]:
                return False
        else:
            return True


    def __getitem__(self, key: KT) -> VT:
        return self.__dict.get(key, self.__default)

    def __setitem__(self, key: KT, value: VT) -> None:
        self.__dict[key] = value 


    def __contains__(self, key: KT) -> bool:
         return key in self.__dict

    
    def any(self, callback: typing.Callable[[KT, VT], bool]) -> bool:
        if callback is None:
            raise TypeError
        for key in self.__dict:
            if callback(key, self.__dict[key]):
                return True
        else:
            return False

            
    def assoc(self, key: KT) -> typing.Optional[typing.List[typing.Any]]:
        return [key, self.__dict[key]] if self.__dict.get(key) else None

    
    def compact(self) -> 'Dictionary[KT, VT]':
        d = {}
        for k in self.__dict:
            if self.__dict[k]:
                d[k] = self.__dict[k]
        return Dictionary[KT, VT](d)
   

    def default(self, key: KT) -> None:
        self.__default = key


    def delete(self, key: KT, callback: typing.Callable[[KT], VT] =None) -> typing.Optional[VT]:
        if key in self.__dict:
            value = self.__dict[key]
            del self.__dict[key]
            return value
        elif callback:
            return callback(key)
        else:
            return None


    def delete_if(self, callback: typing.Callable[[KT, VT], bool]) -> 'Dictionary[KT, VT]':
        ret = {}
        for key in self.__dict:
            if not callback(key, self.__dict[key]):
                ret[key] = self.__dict[key]
        return Dictionary[KT, VT](ret)


    def dig(self, *keys) -> typing.Optional[VT]:
        h = self.__dict
        v: VT
        for key in keys:
            if key in h:
                if isinstance(h, dict):
                    v = h[key]  # code-smell to avoid mypy failure, Grrhhh
                    h = h[key]
            else:
                return None
        return v if len(keys) > 0 else None


    def each(self, callback: typing.Callable[[KT, VT], typing.Optional[typing.Any]]) -> 'Dictionary[KT, VT]':
        ret = {}
        for key in self.__dict:
            ret[key] = callback(key, self.__dict[key])
        return Dictionary[KT, VT](ret)


    def each_key(self, callback: typing.Callable[[KT], typing.Optional[typing.Any]]) -> 'Dictionary[KT, VT]':
        ret = {}
        for key in self.__dict:
            ret[callback(key)] = self.__dict[key]
        return Dictionary[KT, VT](ret)
    

    def each_value(self, callback: typing.Callable[[VT], typing.Optional[typing.Any]]) -> 'Dictionary[KT, VT]':
        ret = {}
        for key in self.__dict:
            ret[key] = callback(self.__dict[key])
        return Dictionary[KT, VT](ret)


    def empty(self) -> bool:
        return len(self.__dict) == 0


    def get(self, key, callback: typing.Callable[[KT], typing.Any] =None) -> typing.Optional[typing.Any]:
        if key in self.__dict:
            return self.__dict[key]
        elif callback:
            return callback(key)
        else:
            return self.__default


    def get_values(self, *keys: typing.List[KT], callback =None) -> typing.List[VT]:
        ret: typing.List[typing.Any] = [] 
        for key in keys:
            if key in self.__dict:
                ret.append(self.__dict[key])
            elif callback:
                ret.append(callback(key))
            else:
                raise KeyError 
        return ret


    def flatten(self, level: int =0) -> typing.List[typing.Any]:
        raw_list = []
        for k, v in self.__dict.items():
            raw_list.append(k)
            raw_list.append(v)

        return self.__flatten(raw_list, level)
    

    def __flatten(self, l, level):
        if level <= 0:
            return l
            
        flat_list = []
        for v in l:
            if isinstance(v, list):
                flat_list.extend(v)
            else:
                flat_list.append(v)
        
        return self.__flatten(flat_list, level - 1)


    def has_key(self, key: KT) -> bool:
        return key in self.__dict 

    
    def has_value(self, value: VT) -> bool:
        return value in self.__dict.values() 


    def invert(self) -> 'Dictionary[KT, VT]':
        _dict = {}
        for k, v in self.__dict.items():
            _dict[v] = k

        return Dictionary[KT, VT](_dict)


    def keep_if(self, callback: typing.Callable[[KT, VT], bool]) -> 'Dictionary[KT, VT]':
        return self.__select(callback) 

    def merge(self, other: 'Dictionary[KT, VT]', callback: typing.Callable[[KT, VT, VT], VT]=None) -> 'Dictionary[KT, VT]':
        _dict: typing.Dict[KT, VT] = copy.deepcopy(self.__dict)
        if isinstance(other, dict):
            _other = other
        elif isinstance(other, Dictionary):
            _other = other.to_dict()
        else:
            raise TypeError

        for k, v in _other.items():
            if _dict.get(k) and callback is not None:
                _dict[k] = callback(k, _dict[k], _other[k])
            else:
                _dict[k] = v
        return Dictionary[KT, VT](_dict)

    def select(self, callback: typing.Callable[[KT, VT], bool]) -> 'Dictionary[KT, VT]':
        return self.__select(callback) 

    
    def __select(self, callback: typing.Callable[[KT, VT], bool]) -> 'Dictionary[KT, VT]':
        _dict: typing.Dict[KT, VT] = {}
        for k, v in self.__dict.items():
            if callback(k, v):
                _dict[k] = v
        return Dictionary[KT, VT](_dict)


    def size(self) -> int:
        return len(self.__dict.keys()) 
    
    def slice(self, *keys) -> 'Dictionary[KT, VT]':
        _dict: typing.Dict[KT, VT] = {}
        for key in keys:
            if key in self.__dict:
                _dict[key] = self.__dict[key]

        return Dictionary[KT, VT](_dict)
    

    def to_list(self) -> typing.List[typing.List[typing.Any]]:
        _list: typing.List[typing.Any] = []
        for k, v in self.__dict.items():
            _list.append([k, v])
        return _list
    
    def to_dict(self) -> typing.Dict[KT, VT]:
        return copy.deepcopy(self.__dict) 
    
    





















