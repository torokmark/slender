from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestEach(TestCase):
    
    def test_each_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.each(lambda k, v: k + v)).to(equal(Dictionary[str, int]({})))

    def test_each_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.each(lambda k, v: k + str(v))).to(equal(Dictionary[str, int]({'a': 'a1', 'b': 'b2', 'c': 'c3'})))

