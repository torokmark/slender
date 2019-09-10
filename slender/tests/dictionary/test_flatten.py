from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestFlatten(TestCase):
    
    def test_flatten_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.flatten()).to(be_empty)
  
    def test_flatten_if_dictionary_not_contains_embedded_lists(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d1.flatten()).to(equal(['a', 1, 'b', 2]))
  
    def test_flatten_if_dictionary_contains_one_level_embedded_lists(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': [2, 3]})
        expect(d1.flatten(1)).to(equal(['a', 1, 'b', 2, 3]))
        
    def test_flatten_if_dictionary_contains_two_levels_embedded_lists(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': [2, 3, [4, 5]]})
        expect(d1.flatten(2)).to(equal(['a', 1, 'b', 2, 3, 4, 5]))


