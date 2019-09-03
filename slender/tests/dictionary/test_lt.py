from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestLt(TestCase):

    def test_lt_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        d2 = Dictionary[str, int]({})
        expect(d1 < d2).to(be_false)

    def test_lt_if_dictionary_is_less(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'a': 1, 'b' : 2, 'c' : 3})
        expect(d1 < d2).to(be_true)

    def test_lt_if_dictionary_values_differ(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'a': 1, 'b' : 20, 'c' : 3})
        expect(d1 < d2).to(be_false)

    def test_lt_if_both_are_equal(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        expect(d1 < d2).to(be_false)

    def test_lt_if_they_overlap(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'b' : 2, 'c' : 3})
        expect(d1 < d2).to(be_false)

    def test_lt_is_greater_or_equal(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2, 'z' : 0})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        expect(d1 < d2).to(be_false)


