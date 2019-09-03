from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestLen(TestCase):

    def test_len_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(len(d1)).to(equal(0))

    def test_len_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(len(d1)).to(equal(3))



