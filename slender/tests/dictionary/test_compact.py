from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestCompact(TestCase):

    def test_compact_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.compact()).to(equal(Dictionary[str, int]({})))

    def test_compact_if_dictionary_not_contains_none_elements(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.compact()).to(equal(Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})))
    
    def test_compact_if_dictionary_contains_none_elements(self):
        d1 = Dictionary[str, int]({'a': None, 'b': 2, 'c': None})
        expect(d1.compact()).to(equal(Dictionary[str, int]({'b': 2})))


