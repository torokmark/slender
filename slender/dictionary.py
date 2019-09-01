
import copy
import types

class Dictionary:

    def __init__(self, d={}):
        if isinstance(d, dictionary):
            self.__dict = copy.deepcopy(d)
        elif isinstance(d, Dictionary):
            self.__dict = copy.deepcopy(d.to_dict())
        else:
            raise TypeError


    @staticmethod
    def try_convert(obj):
        pass


    def __lt__(self, other):
        pass


    def __le__(self, other):
        pass


    def __len__(self):
        pass


    def __eq__(self, other):
        pass


    def __gt__(self, other):
        pass


    def __ge__(self, other):
        pass


    def __getitem__(self, key):
        pass


    def __setitem__(self, key, value):
        pass


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
        pass
    
    def slice(self, *keys):
        pass
    
    def store(self, key, value):
        pass
    
    def to_array(self):
        pass
    
    def to_hash(self):
        pass
    
    def transform_keys(self, key, callback):
        pass
    
    def transform_values(self, value, callback):
        pass
    
    def values_at(self, *key):
        pass
        





















