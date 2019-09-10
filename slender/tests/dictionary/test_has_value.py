from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestHasValue(TestCase):
    
    def test_has_value_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.has_value(1)).to(be_false)
 
    def test_has_value_if_dictionary_contains_elements_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d1.has_value(2)).to(be_true)
  
    def test_has_value_if_dictionary_contains_elements_and_not_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2})
        expect(d1.has_value(3)).to(be_false)


