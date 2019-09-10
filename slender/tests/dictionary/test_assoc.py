from unittest import TestCase, skip
from expects import *

from slender import Dictionary 

class TestAssoc(TestCase):

    def setUp(self):
        self.key = 'a'

    def test_assoc_if_dictionary_is_empty(self):
        d1 = Dictionary[str, int]({})
        expect(d1.assoc(self.key)).to(equal(None))

    def test_assoc_if_dictionary_contains_element_and_finds_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.assoc('a')).to(equal(['a', 1]))
    
    def test_assoc_if_dictionary_contains_element_and_not_find_match(self):
        d1 = Dictionary[str, int]({'a': 1, 'b': 2, 'c': 3})
        expect(d1.assoc('d')).to(equal(None))


