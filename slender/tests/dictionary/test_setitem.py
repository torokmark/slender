from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestSetitem(TestCase):

    def test_setitem_if_dictionary_not_contains_key(self):
        d1 = Dictionary[str, int]({})
        d1['a'] = 1
        expect(d1['a']).to(equal(1))
        expect(len(d1)).to(equal(1))

    def test_setitem_if_dictionary_contains_key(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3, 'd': 4})
        d1['a'] = 10
        expect(d1['a']).to(equal(10))
        expect(len(d1)).to(equal(4))



