from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestInvert(TestCase):
    
    def test_invert_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.invert()).to(be_empty)
 
    def test_invert_if_dictionary_contains_different_values(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d1.invert()).to(equal(Dictionary[str, int]({1: 'a', 2: 'b'})))
  
    def test_invert_if_dictionary_contains_same_values(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 1})
        expect(d1.invert()).to(equal(Dictionary[str, int]({1: 'b'})))


