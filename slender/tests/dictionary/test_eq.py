from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestEq(TestCase):

    def test_eq_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        d2 = Dictionary[str, int]({})
        expect(d1 == d2).to(be_true)

    def test_eq_if_dictionary_has_different_length(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        d2 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        expect(d1 == d2).to(be_false)

    def test_eq_if_dictionary_contains_different_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        d2 = Dictionary[str, int]({'a': 1, 'b': 2, 'd': 4})
        expect(d1 == d2).to(be_false)

    def test_eq_if_dictionary_contains_same_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        d2 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1 == d2).to(be_true)

    def test_eq_if_param_is_different(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1 == [1, 2, 3]).to(be_false)



