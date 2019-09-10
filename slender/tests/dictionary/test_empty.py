from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestEmpty(TestCase):
    
    def test_empty_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.empty()).to(be_true)

    def test_empty_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.empty()).to(be_false)


