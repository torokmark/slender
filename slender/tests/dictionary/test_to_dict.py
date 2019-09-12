from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestToDict(TestCase):
    
    def test_to_dict_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.to_dict()).to(be_empty)
 
    def test_to_dict_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        expect(d1.to_dict()).to(equal({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
  

