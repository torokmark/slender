from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestKeepIf(TestCase):
    
    def test_keep_if_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.keep_if(lambda k, v: k)).to(be_empty)
 
    def test_keep_if_if_dictionary_contains_elements_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        expect(d1.keep_if(lambda k, v: v % 2 == 0)).to(equal(Dictionary[str, int]({'b': 2, 'd': 4})))
  
    def test_keep_if_if_dictionary_contains_elements_and_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 1})
        expect(d1.keep_if(lambda k, v: v > 9)).to(be_empty)

