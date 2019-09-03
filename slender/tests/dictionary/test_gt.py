from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestGt(TestCase):

    def test_gt_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        d2 = Dictionary[str, int]({})
        expect(d1 > d2).to(be_false)

    def test_gt_if_dictionary_is_greater(self):
        d1 = Dictionary[str, int]({'a': 1, 'b' : 2, 'c' : 3})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        expect(d1 > d2).to(be_true)

    def test_gt_if_dictionary_values_differ(self):
        d1 = Dictionary[str, int]({'a': 1, 'b' : 20, 'c' : 3})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        expect(d1 > d2).to(be_false)

    def test_gt_if_both_are_equal(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        expect(d1 > d2).to(be_false)

    def test_gt_if_they_overlap(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'b' : 2, 'c' : 3})
        expect(d1 > d2).to(be_false)

    def test_gt_is_less_or_equal(self):
        d1 = Dictionary[str, int]({'a' : 1, 'b' : 2})
        d2 = Dictionary[str, int]({'a' : 1, 'b' : 2, 'z' : 0})
        expect(d1 > d2).to(be_false)


