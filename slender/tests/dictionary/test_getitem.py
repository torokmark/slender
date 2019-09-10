from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestGetitem(TestCase):

    def setUp(self):
        self.key = 'a'

    def test_getitem_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1[self.key]).to(equal(None))

    def test_getitem_if_dictionary_not_contains_key(self):
        d1 = Dictionary[str, int]({'b': 2, 'c': 3, 'd': 4})
        expect(d1[self.key]).to(equal(None))

    def test_getitem_if_dictionary_contains_element(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1[self.key]).to(equal(1))



