from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestSize(TestCase):

    def test_size_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.size()).to(equal(0))

    def test_size_if_dictionary_contains_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.size()).to(equal(3))


